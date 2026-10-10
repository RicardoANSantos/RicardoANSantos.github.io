# Ricardo N. Santos — professional website

A Quarto website presenting research in organic geochemistry and paleoclimate.

## Pages

- `index.qmd`: biography and selected research
- `research.qmd`: research themes and projects
- `data/publications.json`: published papers and manuscripts
- `cv.qmd`: readable CV; `assets/Ricardo_CV.pdf`: full downloadable CV
- `photos.qmd`: photographs
- `contact.qmd`: professional contact and research profiles

## Build

```sh
quarto render
python3 scripts/check_site.py
```

The build creates `dist/`. A push to `main` triggers the GitHub Pages workflow;
pull requests run the build and checks without publishing.

Read `SETUP.md` for initial publication and `UPDATE_WORKFLOW.md` for future updates.
AI assistants should read `AGENTS.md` first.

Initial content is based on Ricardo's October 2026 CV and supplied photographs.
The website uses Quarto's bundled assets and system fonts. No analytics, paid
plugins, public chatbot, or visitor account are required.
