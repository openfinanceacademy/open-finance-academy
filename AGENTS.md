# Open Finance Academy

This is a Markdown/Jekyll static site deployed to GitHub Pages. Source files are built into `_site/`; edit source, never generated output.

## Quality and reasoning standards

- Apply critical thinking to every change: identify assumptions, distinguish facts from interpretation, consider counterexamples and edge cases, and do not accept an attractive or plausible answer without checking it.
- Write for human understanding and learning. Use clear, plain language, define unfamiliar terms at first use, explain the reasoning behind conclusions, and organize material so a learner can follow it independently.
- Prioritize correctness over speed. Re-check calculations, claims, examples, code, configuration, and rendered output. When evidence is incomplete or uncertain, say so explicitly rather than guessing.
- Write inclusively and respectfully. Avoid stereotypes, unnecessary jargon, exclusionary assumptions, and language that treats one experience as universal. Prefer examples and wording that represent varied backgrounds, abilities, identities, and financial circumstances.
- Treat accessibility as a requirement, not an enhancement. Use meaningful headings, descriptive link text, sufficient contrast, readable structure, accessible tables and images, useful alternative text, and content that remains understandable without relying on color, layout, audio, or hover behavior.
- Double-check every source before relying on it. Fetch the source, confirm that it is authoritative and current enough for the claim, verify that the cited passage actually supports the statement, and preserve the relevant citation in the required format.
- Confirm that every link introduced or changed is reachable and resolves to the intended page. Check internal links against the built site and check external links directly when possible.
- If a source or link cannot be reached by the agent, do not assume it works or cite it as verified. Escalate to a human and ask them to confirm whether they can view it in a browser; record the uncertainty and human confirmation before treating it as verified.

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
