# GitHub Pages setup

Website repository: https://github.com/RicardoANSantos/RicardoANSantos.github.io

Public website address after deployment: https://ricardoansantos.github.io/

## One-time hosting setting

1. Open the repository's **Settings → Pages**:
   https://github.com/RicardoANSantos/RicardoANSantos.github.io/settings/pages
2. Under **Build and deployment**, select **GitHub Actions** as the source.
3. Open **Actions → Build and publish website** and use **Run workflow** if the
   initial run happened before Pages was enabled. Alternatively, ask the assistant
   to retry the publication after confirming that setting.
4. Wait for both the build and deployment jobs to succeed, then open the website.

The GitHub connection used for preparation can edit repository files but does not
expose Pages administration. The initial Pages setting must be selected by the owner.
The separately hosted preparation preview is private and is not the public website.

## Future updates

Read `UPDATE_WORKFLOW.md`. An assistant with access to this repository can update
content and push authorized changes. The workflow renders and checks the website;
only successful builds are published. Pull requests run checks without publishing.

## Local editing

Install Quarto from https://quarto.org/docs/download/. Quarto 1.7.34 is pinned in
our publishing workflow. Python 3 is needed, with no extra packages.

Run `quarto preview` to preview locally.

Before publishing, run `quarto render` followed by `python3 scripts/check_site.py`.

The generated website is in `dist/`. Do not edit generated HTML directly.
