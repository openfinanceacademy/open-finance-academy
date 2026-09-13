# Repository instructions

Open Finance Academy is a Markdown and Jekyll site for accessible financial education.

## Lessons and knowledge content

Before creating or editing any lesson, knowledge area index, or glossary entry, read and follow [the finance lesson skill](skills/finance-lessons/SKILL.md). Apply it to every lesson, including lessons added inside an existing area's folder.

Use `knowledge/money-and-financial-fundamentals/index.md` as the worked example. The shared conventions are plain-language explanations, clearly introduced terms, worked examples, practice questions with explained answers, and glossary links in both directions. Scale the depth to the topic; preserve the structure when making focused edits.

## Site structure

- `knowledge.md` is the overview of the 18 major finance areas.
- `knowledge/<area>/index.md` is each area's landing page, containing a lesson or planned topics and links to lessons.
- Additional lessons belong inside the relevant `knowledge/<area>/` folder.
- `_data/glossary.yml` contains shared definitions; `glossary.md` renders the alphabetical glossary and references from page metadata.
- `_layouts/default.html` contains the shared navigation, including Knowledge and Glossary.
- `assets/css/style.css` contains shared styles.

Preserve stable page URLs and glossary IDs. Update inbound links and reference metadata when a heading anchor changes. Keep planned content clearly distinguished from published lessons.

## Validation

Run `jekyll build` after content changes. Check rendered local links and heading anchors, glossary references, and example arithmetic. Run `git diff --check`. Edit source files rather than generated `_site/` output.
