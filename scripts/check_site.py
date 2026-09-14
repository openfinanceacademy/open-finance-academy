#!/usr/bin/env python3
"""Check rendered metadata, sitemap coverage, and local links using only stdlib."""

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.meta = {}
        self.canonicals = []
        self.titles = []
        self.schemas = []
        self.h1_count = 0
        self.capture = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'meta':
            key = attrs.get('name', attrs.get('property'))
            self.meta.setdefault(key, []).append(attrs.get('content', ''))
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonicals.append(attrs.get('href', ''))
        if tag in ('a', 'link') and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in ('img', 'script') and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'title':
            self.titles.append('')
            self.capture = self.titles
        if tag == 'script' and attrs.get('type') == 'application/ld+json':
            self.schemas.append('')
            self.capture = self.schemas

    def handle_data(self, data):
        if self.capture is not None:
            self.capture[-1] += data

    def handle_endtag(self, tag):
        if tag in ('title', 'script'):
            self.capture = None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', nargs='?', default='_site')
    parser.add_argument('--url', default='https://openfinance.academy')
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    root = Path(args.directory)
    base = args.baseurl.rstrip('/')
    origin = args.url.rstrip('/')
    home = origin + base + '/'
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    pages = {}
    for path in root.rglob('*.html'):
        relative = path.relative_to(root).as_posix()
        url_path = base + '/' + relative
        if url_path.endswith('/index.html'):
            url_path = url_path[:-10]
        pages[url_path] = Page(path.read_text())
    check(bool(pages), 'No HTML pages found; run jekyll build first.')

    for path, page in pages.items():
        expected = origin + path
        check(page.canonicals == [expected], f'{path}: incorrect or duplicate canonical')
        check(len(page.titles) == 1 and bool(page.titles[0].strip()), f'{path}: missing or duplicate title')
        check(page.h1_count == 1, f'{path}: expected one primary heading')
        for key in ('description', 'og:title', 'og:description', 'og:url', 'og:type',
                    'og:site_name', 'twitter:title', 'twitter:description', 'twitter:card'):
            values = page.meta.get(key, [])
            check(len(values) == 1 and bool(values[0].strip()), f'{path}: missing or duplicate {key}')
        check(page.meta.get('og:url') == [expected], f'{path}: social URL differs from canonical')
        check(page.meta.get('description') == page.meta.get('og:description') == page.meta.get('twitter:description'),
              f'{path}: inconsistent descriptions')
        check(bool(page.schemas), f'{path}: missing structured data')
        for schema in page.schemas:
            try:
                data = json.loads(schema)
                graph = {item['@type']: item for item in data['@graph']}
                check(data['@context'] == 'https://schema.org', f'{path}: incorrect schema context')
                check(graph['WebPage']['url'] == expected, f'{path}: incorrect structured page URL')
                check(graph['WebSite']['url'] == home, f'{path}: incorrect structured site URL')
                if path != base + '/':
                    crumbs = graph['BreadcrumbList']['itemListElement']
                    check([x['position'] for x in crumbs] == list(range(1, len(crumbs) + 1)),
                          f'{path}: incorrect breadcrumb positions')
                    check(crumbs[0]['item'] == home and crumbs[-1]['item'] == expected,
                          f'{path}: incorrect breadcrumb URLs')
                    page.links.extend(x['item'] for x in crumbs)
                if page.meta.get('og:type') == ['article']:
                    check(bool(graph['BlogPosting']['datePublished']), f'{path}: missing article date')
            except (ValueError, KeyError, TypeError) as error:
                errors.append(f'{path}: invalid structured data: {error}')

        for link in page.links:
            resolved = urlsplit(urljoin(expected, link))
            if resolved.scheme not in ('http', 'https') or resolved.netloc != urlsplit(origin).netloc:
                continue
            target = unquote(resolved.path)
            if base and not target.startswith(base + '/'):
                errors.append(f'{path}: link escapes base path: {link}')
                continue
            disk_path = root / target[len(base):].lstrip('/')
            check(target in pages or disk_path.is_file(), f'{path}: broken local link: {link}')
            if resolved.fragment and target in pages:
                check(unquote(resolved.fragment) in pages[target].ids, f'{path}: broken anchor: {link}')

    for field, values in (
        ('title', [p.titles[0] for p in pages.values() if p.titles]),
        ('description', [p.meta['description'][0] for p in pages.values() if p.meta.get('description')]),
    ):
        for value, count in Counter(values).items():
            check(count == 1, f'Duplicate {field}: {value}')

    try:
        sitemap = ET.parse(root / 'sitemap.xml')
        locations = [x.text for x in sitemap.findall('{*}url/{*}loc')]
        check(len(locations) == len(set(locations)), 'Duplicate sitemap URLs')
        check(set(locations) == {origin + path for path in pages}, 'Sitemap does not match rendered pages')
        robots = (root / 'robots.txt').read_text()
        check('Sitemap: ' + home + 'sitemap.xml' in robots, 'robots.txt has incorrect sitemap URL')
        check('Disallow: /' not in robots, 'robots.txt blocks crawling')
    except (OSError, ET.ParseError) as error:
        errors.append(f'Invalid discovery files: {error}')

    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} pages: metadata, structured data, sitemap, local links, and anchors passed.')


if __name__ == '__main__':
    main()
