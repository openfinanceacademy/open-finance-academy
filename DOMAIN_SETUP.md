# Domain Setup

The site is configured to use `openfinance.academy` as its canonical GitHub Pages domain through `CNAME`.

## GitHub Pages

After creating the GitHub repository:

1. Open **Settings > Pages**.
2. Set the source to **GitHub Actions**.
3. Confirm that the custom domain is `openfinance.academy`.
4. Enable HTTPS after the DNS records have propagated.

## DNS for `openfinance.academy`

At the domain provider, use these records:

- `A` record for `@` to `185.199.108.153`
- `A` record for `@` to `185.199.109.153`
- `A` record for `@` to `185.199.110.153`
- `A` record for `@` to `185.199.111.153`
- `CNAME` record for `www` to `<github-user>.github.io`

Replace `<github-user>` with the GitHub account or organization that owns the repository.

## DNS for `openfinance.wiki`

GitHub Pages supports one custom domain per site. Configure `openfinance.wiki` as a URL redirect at the domain provider, forwarding to `https://openfinance.academy`.

If the provider does not offer URL forwarding, host a small redirect site for `openfinance.wiki` separately. Do not add a second `CNAME` file to this repository, because it would replace the canonical domain.
