default:
    @just --list

serve:
    jekyll serve --livereload

build:
    jekyll build

check: build
    python3 scripts/check_site.py
    git diff --check

clean:
    rm -rf _site .jekyll-cache

open:
    open http://127.0.0.1:4000
