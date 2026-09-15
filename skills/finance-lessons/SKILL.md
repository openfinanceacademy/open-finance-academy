---
name: finance-lessons
description: Write or revise Open Finance Academy lessons, knowledge area indexes, and glossary entries using the repository's accessible teaching structure and linked global glossary.
---

# Finance lessons

Use this skill for all lessons in this repository. Resolve the paths below from the repository root. Read the relevant existing area index, `_data/glossary.yml`, and `knowledge/money-and-financial-fundamentals/index.md` before writing. Use the fundamentals lesson as a structural example; choose examples and depth suited to the new topic.

## Location and navigation

- Keep the 18 area landing pages at `knowledge/<area>/index.md` with URLs `/knowledge/<area>/`.
- Put additional lesson Markdown files inside the appropriate area folder, with explicit permalinks such as `/knowledge/<area>/<lesson>/`. Link them from that area's index.
- Use `layout: default`, a descriptive `title`, and a stable `permalink` in front matter.
- Include links to the parent area or Knowledge overview and the global Glossary. Use Jekyll's `relative_url` filter for site links.
- Update `knowledge.md` or the area index when publishing a lesson so availability descriptions stay accurate. Unwritten areas retain their planned-topic status.

## Lesson structure

Every complete lesson follows this teaching structure. Headings and length can vary with the subject.

1. **Title and learning purpose.** State in ordinary language what the reader will understand or be able to do. Identify prerequisites, or say none are needed.
2. **Navigation and reading guidance.** Link back to the area or overview and to the glossary. Explain that bold linked terms are newly introduced vocabulary.
3. **Assumptions.** Before numerical examples, identify invented amounts and rates, time periods, and relevant treatment of fees, taxes, deposits, withdrawals, or uncertainty. Identify jurisdictions and dates when rules depend on them.
4. **In this lesson.** Provide a short linked contents list for the main sections.
5. **Explanations and worked examples.** Build from familiar situations to the concept, then to calculations. Introduce and define terms before relying on them. Show what each calculation means and explain the result. Use tables when they make comparisons clearer.
6. **Check your understanding.** Include questions that let the reader apply the ideas. Put answers afterward with reasoning and calculations, not just final values. Scale question count to the lesson.
7. **Terms introduced in this lesson.** Include a recap linking to the global glossary, generated from the page's `glossary_terms` metadata.
8. **Keep learning.** Link to relevant next lessons or area pages and identify planned content honestly.

An area index that only lists planned topics or links to lessons does not need artificial exercises or numerical examples. When it teaches a concept or introduces a term, apply the same explanation and glossary conventions. Focused edits should preserve existing lesson structure without requiring unrelated rewrites.

## Write for understanding

- Explain each new finance term at its first meaningful use, make that occurrence bold, and link it to its glossary definition. Apply this to terms introduced in tables too.
- Use everyday language around the technical vocabulary. Explain unfamiliar abbreviations, mathematical notation, and units before using them.
- Start with a concrete example before a general formula. Show intermediate steps, specify periods for rates, and distinguish exact results from estimates and rounded amounts.
- Explain relevant limitations and tradeoffs. Keep assumed returns distinct from guaranteed outcomes and nominal amounts distinct from purchasing power.
- Cite authoritative sources beside the explanations they support. Verify financial claims and calculations; check current primary sources for changing rules or rates. Prefer invented, clearly labeled teaching amounts when live data is unnecessary.

## Numbered citations

Lessons cite external sources with kramdown footnotes, not inline prose links.

- Place the marker after the punctuation of the sentence it supports: `...explains money.[^1]`. Number footnotes in order of first appearance.
- Put footnote definitions under a final `## References` heading, after "Keep learning" (kramdown renders footnote bodies at the end of the document, so this heading must come last). Format: `[^1]: Bank of England, "What is money?" — <https://www.bankofengland.co.uk/explainers/what-is-money>`.
- Every substantive section needs at least one citation to a reputable source: central banks, regulators (SEC/Investor.gov, CFPB, FDIC, FINRA, IRS), standard setters (FASB, IFRS Foundation), or international bodies (IMF, BIS, OECD, World Bank). Avoid commercial blogs unless nothing official exists.
- Only cite a URL after fetching it and confirming it supports the claim. Internal site links (glossary, other lessons) use regular `relative_url` links, never footnotes.

## Maintain the global glossary in the same change

Definitions live in `_data/glossary.yml`. Before adding a term, check for an existing entry and reuse its ID. New entries have this shape:

```yaml
- id: interest
  term: Interest
  definition: Money paid for the use of money, such as money earned on savings or charged on borrowing.
```

Use unique, stable lowercase IDs with hyphens between words. Write definitions that stand alone in plain language. Quote YAML values when punctuation would otherwise make them invalid.

Link the first introduction in the lesson like this:

```markdown
**[Interest]({{ '/glossary/' | relative_url }}#interest)** is money paid for the use of money.
```

Register every term the page introduces or explains in its front matter. Map the glossary ID to the actual section anchor containing its explanation, without a leading `#`:

```yaml
glossary_terms:
  interest: how-interest-works
  principal: how-interest-works
```

Register reused terms too when the new lesson explains them. `glossary.md` automatically builds references to all registered pages and sections; do not maintain a second manual reference list. It does not infer references from prose links. Keep metadata, glossary entries, and inline links synchronized in the same change. When moving an explanation or renaming a heading, update its mapped anchor and any inbound links.

Use the existing term recap pattern:

```liquid
{% assign lesson_terms = site.data.glossary | sort: 'term' %}
{% for term in lesson_terms %}{% if page.glossary_terms[term.id] %}
- [{{ term.term }}]({{ '/glossary/' | relative_url }}#{{ term.id }})
{% endif %}{% endfor %}
```

## Verify before finishing

- Run `jekyll build` and `git diff --check`.
- Check the rendered lesson, including contents anchors, tables, term recap, and parent and next-page navigation.
- Check that each introduced term has a definition and matching `glossary_terms` registration. IDs must be unique and references must point to real rendered heading anchors.
- Follow lesson-to-glossary links and glossary-to-lesson references, including reused terms with multiple references. Check for unrendered Liquid syntax.
- Recalculate worked examples and practice answers, including rounding and matching rate periods. Confirm source links support the associated explanations.
- Run `python3 scripts/check_math.py` (also part of `just check`). It re-evaluates inline statements shaped like `$100 × 1.05 = $105` and fails on mismatches. Write worked examples in that explicit form so the checker covers them; arithmetic that lives only in tables or prose without an equals sign must be verified by hand.
- Edit source files only; do not commit generated `_site/` output.
