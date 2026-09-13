# Open Finance Academy

Open Finance Academy is a community-driven project for learning, building, and sharing practical knowledge about open finance.

The project is also a Markdown-powered static site deployed to GitHub Pages at [openfinance.academy](https://openfinance.academy).

## Vision

We believe everyone has the right to pursue financial freedom and access the knowledge and tools needed to protect themselves from financial exploitation and repression. Open Finance Academy makes financial technology easier to understand, more accessible to build with, and more open to everyone.

We want open finance to expand people’s choices, privacy, and agency, not make it easier to control or profit from them.

Too much financial education is locked behind paywalls, putting essential knowledge out of reach for people with lower incomes and for historically underrepresented communities. We are building an open alternative: practical, high-quality resources that anyone can access and contribute to.

## What You’ll Find Here

- Beginner-friendly lessons on finance and financial technology
- Practical guides for working with open financial data and APIs
- Examples, projects, and experiments for hands-on learning
- Resources for developers, researchers, educators, and curious builders

## Learning Topics

The curriculum will grow over time and may include:

- Financial fundamentals
- Open banking and open finance
- APIs, data standards, and interoperability
- Privacy, security, and responsible data use
- Digital identity and payments
- Decentralized finance and blockchain
- Building and evaluating financial products

## Getting Started

This project is in its early stages. Start by exploring the available lessons and examples, or open an issue with a topic you would like to see covered. Site content lives in Markdown files and is built with Jekyll.

To preview the site locally with Jekyll installed:

```sh
jekyll serve
```

See [DOMAIN_SETUP.md](DOMAIN_SETUP.md) for GitHub Pages and custom-domain setup instructions.

## Contributing

The [Knowledge outline](knowledge.md) links to 18 major areas. Each area has an index at `knowledge/<area>/index.md` containing lessons or planned topics. Add future lessons and resources within that area's folder and link them from its index page.

### Knowledge terms and the global glossary

When adding or editing a lesson or knowledge index:

1. Explain each new finance term on first use, in plain language. Make that first occurrence bold and link it to the glossary: `**[Interest]({{ '/glossary/' | relative_url }}#interest)**`.
2. Add new definitions to `_data/glossary.yml` with a unique, stable `id`, a readable `term`, and a plain-language `definition`. Reuse existing entries for terms already defined.
3. Register each term the page explains in its YAML front matter, mapping the glossary ID to the heading anchor where the explanation appears:

   ```yaml
   glossary_terms:
     interest: how-interest-works
     principal: how-interest-works
   ```

4. The [global glossary](glossary.md) automatically lists terms alphabetically and builds reference links from this metadata. Register existing terms on new pages too, so their references appear. Keep anchors and metadata in sync when changing headings.
5. Use worked examples, state assumptions, and link authoritative sources beside the explanations they support. Build with `jekyll build` and check that term links and glossary references reach the correct sections.

See [Money and financial fundamentals](knowledge/money-and-financial-fundamentals/index.md) for a complete example, including a term recap generated from the same metadata.

Contributions are welcome. You can help by:

- Improving explanations and examples
- Suggesting lessons or learning paths
- Sharing useful resources
- Reporting errors or broken links
- Building practical exercises and projects

Please open an issue or pull request to get involved.

## Status

Early development. Content, structure, and tooling are still being shaped.

## License

License information will be added as the project develops.
