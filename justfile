default:
    @just --list

serve:
    jekyll serve --livereload

build:
    jekyll build

clean:
    rm -rf _site .jekyll-cache

open:
    open http://127.0.0.1:4000
