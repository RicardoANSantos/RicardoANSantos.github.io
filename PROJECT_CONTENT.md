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

## Supplied HOLMODRIVE photograph

The sediment-coring photograph supplied by Ricardo is also published as `l1.png`
in the National Geographic Portugal article. Its original pixels are stored in
`assets/projects/holmodrive-peixao-coring.png`. Credit Filipe Patrocínio on the
Research card and project page, with his website link, https://filipepatrocinio.com/. The project-page
image preserves the full portrait; the overview card uses a crop centered at 70%.
The National Geographic entry credits Filipe for text and photography.
Ricardo uploaded the separate branded National Geographic cover in commit
`aa66d219a3982a66a694d1ff3a3d7bbbcd69da42` on 11 October 2026.
Its original JPEG is stored as `assets/outreach/national-geographic-peixao-cover.jpg`.
The image retains the full cover, text, and logo and links to the feature.
The outreach record's `image` and `image_alt` fields produce the same cover
on Publications & outreach and the HOLMODRIVE page. It appears beside the title
and text on desktop and above them on mobile.
Keep the “Text and photography” credit linking to https://filipepatrocinio.com/.

Project pages with real photos use a compact 280 px photograph, keeping the full
portrait visible and avoiding the tall empty column beside the introduction.
