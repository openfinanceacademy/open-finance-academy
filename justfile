default:
    @just --list

serve: build
    python3 -m http.server 4000 --directory _site

build:
    jekyll build
    npm run search:index

check: build
    python3 scripts/check_site.py
    git diff --check

clean:
    rm -rf _site .jekyll-cache

open:
    open http://127.0.0.1:4000
