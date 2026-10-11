# Research project photos and details

The three main projects and their pages are generated from `data/projects.json`
by `scripts/render_projects.py`. Ricardo confirmed the following groupings on
11 October 2026.

## Photo slots

| Project | Suggested image | Current grouping |
| --- | --- | --- |
| ADAPT | Lake Rotsee, sediment coring, aquatic plants, or laboratory work | Ongoing |
| MEMELAND | A relevant lake, sampling site, landscape, or project fieldwork | Ongoing |
| HOLMODRIVE · Lake Peixão | Lake Peixão, fieldwork, or sediment coring | Past |

## What Ricardo can send

- One landscape photograph for each project card and detailed page.
- A short caption with known location and date, plus photographer credit.
- His specific role or research contribution within MEMELAND.
- Optional project participation dates, further papers, or corrections to descriptions.

Notes and files are enough; Ricardo does not need to write polished website text.
Leave unknown roles, locations, and dates unstated.

## Replacing a placeholder

Save the supplied image under `assets/projects/` with a descriptive filename.
Set `photo` in the project record to its path relative to the website root,
such as `assets/projects/holmodrive-peixao-fieldwork.jpg`, and supply
`photo_alt` and `photo_caption`. Run `quarto render`, commit the regenerated
pages, then check the build and public deployment. Use Ricardo's supplied or
explicitly authorized photographs of the project.

## Related publications and outreach

Maintain citation metadata in `data/publications.json`. Project
`publication_dois` and `outreach_urls` reference those records. Project papers
are displayed oldest first; order DOI references chronologically within a year.
HOLMODRIVE currently includes five papers, the National Geographic Portugal
feature, and Ricardo’s project video. The video is embedded in the project’s
Outreach section and linked from Publications & outreach. ADAPT includes DOI `10.1029/2025PA005401`.
Do not add papers to MEMELAND without a supplied or verified project association.

The earlier standalone research-topic pages remain available for existing links.
They are not additional main-project cards.
