# Research project photos and details

The three main projects and their pages are generated from `data/projects.json`
by `scripts/render_projects.py`. Ricardo confirmed the following groupings on
11 October 2026.

Ongoing projects are shown newest first: MEMELAND before ADAPT. Keep this order
in `data/projects.json`; the generator uses the project array order for the cards.
Each main project has a highlighted “My contribution” section. HOLMODRIVE uses
Ricardo’s account of his modern leaf-wax calibration, climate and vegetation
reconstructions, and collaborative lake-sediment studies.

## Photo slots

| Project | Suggested image | Current grouping |
| --- | --- | --- |
| MEMELAND | Supplied project logo, displayed in full | Ongoing |
| ADAPT | Supplied Lake Rotsee shoreline photo | Ongoing |
| HOLMODRIVE · Lake Peixão | Supplied coring photograph and four-photo project gallery | Past |

## What Ricardo can send

- One photograph for each project card and detailed page, plus 2–4 gallery photos.
- A short caption with known location and date, plus photographer credit.
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
feature, and Ricardo’s project video. The video has a small linked thumbnail with a play icon beside its title in both
the project’s Outreach section and Publications & outreach. ADAPT includes DOI `10.1029/2025PA005401`.
Do not add papers to MEMELAND without a supplied or verified project association.

The earlier standalone research-topic pages remain available for existing links.
They are not additional main-project cards.

## Supplied HOLMODRIVE photograph

The sediment-coring photograph supplied by Ricardo is also published as `l1.png`
in the National Geographic Portugal article. Its original pixels are stored in
`assets/projects/holmodrive-peixao-coring.png`. Credit Filipe Patrocínio on the
Research card and project page, with his website link, https://filipepatrocinio.com/. The project-page
image preserves the full portrait; the overview card uses a crop centered at 70%.
Past-project overview cards take their height from the text, with a smaller
cropped photograph beside it. The portrait image must not expand the whole card.
On mobile, the image stacks above the text.
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

The original YouTube thumbnail for `WWDSYIWuOYk` is stored at
`assets/outreach/lake-peixao-video-thumbnail.jpg`, sourced from
`https://i.ytimg.com/vi/WWDSYIWuOYk/mqdefault.jpg`.
The video entry uses the existing `image` and `image_alt` fields.
Its thumbnail and “Watch on YouTube” link open the video, and the play icon
identifies it as a video. Keep the compact layout instead of a large embedded player.

## INTIMATE Summer School outreach

The INTIMATE Summer School 2022 blog post and related highlights video appear
in Publications & outreach. Ricardo supplied the links and group photograph;
they are not associated with a research-project page.
The blog entry includes the EGU Best Blog Post Award, public vote, already
recorded in his CV. Keep the recognition visible beneath the blog title.

The original 1024 × 750 WebP group photograph is stored at
`assets/outreach/intimate-summer-school-2022-group.webp`. The same image is
published at
`https://blogs.egu.eu/divisions/cl/files/2022/11/Ricardo-N.-Sanotos_00-1024x750.webp`.
The article identifies the location as Kokkila and credits Francesco Muschitiello;
keep his photograph credit with this entry.

The video thumbnail is stored at
`assets/outreach/intimate-summer-school-2022-video-thumbnail.jpg`, sourced from
`https://i.ytimg.com/vi/2F66bkFZ7iA/mqdefault.jpg`.
Both entries use the existing compact thumbnail layout, with a play icon and
YouTube link for the video.

## MEMELAND contribution and logo

Ricardo confirmed on 11 October 2026 that he will take over Tobias Schneider’s
MEMELAND contribution. The page describes his upcoming biomarker research with
Prof. Nathalie Dubois and the Eawag team without assigning an employment title,
start date, or changing his homepage affiliation.
The summary covers fecal sterols and bile acids for grazing and manuring,
lake nutrient and oxygen conditions, leaf-wax radiocarbon and refractory organic
carbon for soil erosion, and plant biomarkers for cultivation and hemp retting.
The Eawag team description is at https://memeland.no/en/Team/eawag.html.

The supplied logo matches the original PNG at
`https://memeland.no/en/Materials/Logos/MEMELAND.png` and is stored at
`assets/projects/memeland-logo.png`. Set `photo_kind` to `logo` so the Research
card displays it in full with `object-fit: contain`; preserve the original pixels.
`contribution` supplies the highlighted “My contribution” section on the project
page. Do not describe the logo as a photograph or assign a photographer credit.

## ADAPT scope, research aims, and supplied Rotsee photo

Ricardo confirmed on 11 October 2026 that ADAPT also studied lakes in the USA.
The Research card and project page therefore label the study area as
“Switzerland · USA”. The summary follows the official project description at
https://duw.unibas.ch/en/forschungsgruppen/organic-geochemistry/adapt/:
modern algal calibration with lipid biomarkers and sedimentary DNA, Swiss lake
records of 20th-century phosphorus changes and Roman-period water-quality
impacts, natural variability over 10,000 years, and climatic context and
macroalgae reconstructed with plant waxes and H/C isotopes.
Keep the original Swiss-lake aims distinct from the wider geographic scope.

Ricardo uploaded the supplied Lake Rotsee shoreline photo showing trees, the lake
at sunset, and a nature-reserve sign. Its original bytes are stored at
`assets/projects/adapt-rotsee.jpg`. ADAPT uses it on the Research card and project
page, with a compact crop on the card and the full portrait on the project page.
Alt text and the caption “Lake Rotsee, Switzerland.” are supplied in the project
data. Leave photographer credit unstated unless Ricardo confirms it.

## Project galleries

A project's optional `gallery` array in `data/projects.json` supplies photos
beneath its description and approach, before its papers. Each record contains
`image`, `alt`, and an optional `caption`, `credit_name`, and `credit_url`.
The generator displays two columns on desktop and one on small screens.
Previews show the whole image; select one to open the original file.
Keep the Research overview card compact, using its existing main photograph.

Ricardo uploaded four HOLMODRIVE photographs in the “Peixao fotos” commit on
11 October 2026: the Lake Peixão landscape, coring equipment, the field team
with sediment-core tubes, and laboratory work. Their original bytes are stored
under descriptive names in `assets/projects/holmodrive-peixao-*` and shown in
that sequence on the project page. The original upload filenames remain available.
Dates and photographer credits for these four photographs were not supplied;
do not assign the existing main-photo credit to the gallery.

## HOLMODRIVE introduction and contribution

Ricardo supplied a fuller personal account on 11 October 2026. His time at IPMA
and the University of Lisbon, the lake setting at approximately 1,700 m, and his
leadership of organic geochemistry on PEX19-01 appear beside the main photo.
The optional `overview_text` field supplies these short paragraphs beneath the
project website link. The detailed `contribution` field covers modern calibration,
the last 2,000 years of vegetation and hydroclimate, and collaborative core studies.

Keep the C₂₉ δ²H finding specific to Lake Peixão sediments, rather than a universal
claim about leaf waxes. The calibration paper (10.3389/fenvs.2022.994377) supports
that interpretation. The reconstruction paper (10.1016/j.quascirev.2024.108796)
describes changing Atlantic and Mediterranean influences through the Medieval
Climate Anomaly and Little Ice Age. Preserve the displayed isotope notation,
the full main photograph, and the project gallery.
