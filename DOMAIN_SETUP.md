# Domain Setup

The site uses `openfinance.academy` as its canonical domain in `_config.yml` and `CNAME`. When deploying with GitHub Actions, the custom domain must also be saved in the repository's Pages settings; GitHub does not use the `CNAME` file to configure it.

## GitHub Pages

For `openfinanceacademy/open-finance-academy`:

1. Open [**Settings > Pages**](https://github.com/openfinanceacademy/open-finance-academy/settings/pages).
2. Set the source to **GitHub Actions**.
3. Under **Custom domain**, enter `openfinance.academy` and save.
4. Enable HTTPS after the DNS records have propagated.

The workflow in `.github/workflows/pages.yml` builds and deploys on every push to `main`. To deploy the current `main` manually, open **Actions > Deploy Jekyll site to GitHub Pages > Run workflow**. The build uploads `_site/`, and the deployment uses the `github-pages` environment. No personal access token or deployment secret is needed.

The workflow takes the base path from GitHub Pages, so links also work at `https://openfinanceacademy.github.io/open-finance-academy/` before a custom domain is configured. With the custom domain configured, the base path is empty.

Check the workflow's build and deployment jobs in **Actions** if publishing fails. A failure in **Setup Pages** usually means Pages has not been enabled with **GitHub Actions** as its source.

See GitHub's [custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) and [custom-domain documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## DNS for `openfinance.academy`

At the domain provider, use these records:

- `A` record for `@` to `185.199.108.153`
- `A` record for `@` to `185.199.109.153`
- `A` record for `@` to `185.199.110.153`
- `A` record for `@` to `185.199.111.153`
- `CNAME` record for `www` to `openfinanceacademy.github.io`

## DNS for `openfinance.wiki`

GitHub Pages supports one custom domain per site. Configure `openfinance.wiki` as a URL redirect at the domain provider, forwarding to `https://openfinance.academy`.

If the provider does not offer URL forwarding, host a small redirect site for `openfinance.wiki` separately. Do not add a second `CNAME` file to this repository, because it would replace the canonical domain.
