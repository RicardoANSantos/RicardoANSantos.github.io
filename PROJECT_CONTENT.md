# Research project photos and details

The research overview and individual project pages are generated from
`data/projects.json` by `scripts/render_projects.py`.

## Photo slots

| Project | Suggested image | Current grouping |
| --- | --- | --- |
| Lake Rotsee | The lake, sediment coring, or sediment cores | Ongoing |
| Owasco Lake | The lake, field site, or sediment work | Ongoing |
| Aquatic-plant biomarkers | Charophytes, macrophytes, sampling, or laboratory work | Ongoing |
| Younger Dryas Working Group | A meeting, group photo, or related fieldwork | Ongoing |
| Lake Peixão | The lake, fieldwork, or sediment coring | Past MSc research, 2019–2021 |

The groupings are provisional. Lake Peixão refers to the completed MSc phase;
its later collaborative research is not being declared finished. Confirm other
groupings rather than inferring completion from a publication date.

## What Ricardo can send

For each project, supply:
- One landscape photograph for the overview card and project page; extra photos
  or a figure can be added later.
- A short caption with known location and date, plus photographer credit.
- Confirmation of ongoing/past status, project dates, and Ricardo's role.
- Any corrections or notes for the current short description.
- Optional collaborator names, project/funding links, or a related publication.

Notes and files are enough; Ricardo does not need to write polished website text.

## Replacing a placeholder

Save the supplied image under `assets/projects/` with a descriptive filename.
In its project record, set `photo` to the path relative to the website root,
such as `assets/projects/rotsee-fieldwork.jpg`, and supply `photo_alt` and
`photo_caption`. Generate both the overview and the detailed page by running
`quarto render`, then check the build and public deployment. Do not use an
unrelated landscape image as a photograph of a named study site.
