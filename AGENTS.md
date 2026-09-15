# Open Finance Academy

This is a Markdown/Jekyll static site deployed to GitHub Pages. Source files are built into `_site/`; edit source, never generated output.

## Commands

- Install the pinned Pagefind dependency with `npm ci` (Node.js 22+ is expected).
- `just build` runs `jekyll build` and then `npm run search:index`.
- `just check` builds, runs `python3 scripts/check_site.py`, runs `python3 scripts/check_math.py` (re-verifies inline worked-example arithmetic in `knowledge/`), and runs `git diff --check`.
- `just serve` builds the site and serves `_site` on port 4000. Plain `jekyll serve` does not build the Pagefind index.
- For a subpath build, pass the same base path to Jekyll and the checker: `jekyll build --baseurl /your-path` and `python3 scripts/check_site.py --baseurl /your-path`.

## Content rules

- Before editing a lesson, knowledge index, or glossary entry, read `skills/finance-lessons/SKILL.md`; use `knowledge/money-and-financial-fundamentals/index.md` as the structural example.
- Keep knowledge area indexes at `knowledge/<area>/index.md`; put additional lessons in that area folder and link them from its index and, when appropriate, `knowledge.md`.
- Preserve stable permalinks and glossary IDs. New or explained terms need a matching `_data/glossary.yml` definition, first-use glossary link, and `glossary_terms` front-matter mapping to the real section anchor.
- Keep planned topics clearly labeled as planned. Use `relative_url` for internal Markdown/Liquid links.
- Published pages need unique, accurate `description` front-matter; preserve heading anchors or update every inbound link and glossary reference when changing headings.
- Knowledge pages cite sources with numbered kramdown footnotes (`[^1]`) defined under a final `## References` heading; see the citation rules in `skills/finance-lessons/SKILL.md`. Never cite a URL without fetching it and confirming it supports the claim.

Run `just check` after site changes, and inspect rendered links, anchors, glossary references, and worked-example arithmetic. The GitHub Pages workflow also builds the search index and runs `scripts/check_site.py` with its configured base path.
