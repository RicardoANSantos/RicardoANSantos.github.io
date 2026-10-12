# Research project photos and details

The four main projects and their pages are generated from `data/projects.json`
by `scripts/render_projects.py`. Ricardo confirmed the following groupings on
11–12 October 2026.

Ongoing projects are shown newest first: MEMELAND, Younger Dryas Working Group,
then ADAPT. Keep this order
in `data/projects.json`; the generator uses the project array order for the cards.
Each main project has a highlighted “My contribution” section. HOLMODRIVE uses
Ricardo’s account of his modern leaf-wax calibration, climate and vegetation
reconstructions, and collaborative lake-sediment studies.

## Photo slots

| Project | Suggested image | Current grouping |
| --- | --- | --- |
| MEMELAND | Supplied project logo, displayed in full | Ongoing |
| Younger Dryas Working Group | Supplied group logo and two Basel meeting images | Ongoing |
| ADAPT | Supplied Lake Rotsee shoreline photo | Ongoing |
| HOLMODRIVE · Lake Peixão | Supplied coring photograph, four-photo gallery, and lake-formation illustration | Past |

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
The Younger Dryas Working Group page is now a main project generated from the
project data. Other standalone topic pages are not additional main-project cards.

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
Set `layout` to `wide` for an illustration that spans both columns at its natural
aspect ratio; set `kind` to `illustration` for the correct link and credit labels.
Optional `source_name` and `source_url` add a linked source beneath the image.
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

## National Geographic lake-formation illustration

Ricardo supplied the three-stage illustration on 11 October 2026 and identified
it as part of the National Geographic outreach feature. The matching original
1024 × 406 PNG is published at
https://content.nationalgeographic.pt/medio/import/attachment/revistas/265/GrandeAngular/l3.png
and stored at `assets/outreach/peixao-glacial-lake-formation.png`.

It appears first in the HOLMODRIVE gallery at full width, followed by the four
uploaded photographs. Its natural aspect ratio preserves all three stages of
glacier retreat and lake formation. Link National Geographic Portugal as the
source, using the existing feature URL. The individual illustrator was not
verified; do not assign the main photograph's Filipe Patrocínio credit to this
illustration. The heading is “Project images”, with the existing
`project-photos` anchor retained.

## Project funding acknowledgments

Projects with confirmed funding have a Funding section near the bottom of their
detailed pages. The structured `funding` record in `data/projects.json` supplies
Funder and Grant fields, with `source_url` linking the grant number to the
official project or funder record. Funder logos retain their original colours
and proportions. The Younger Dryas Working Group has no funding record or section,
as requested by Ricardo on 12 October 2026.

Ricardo supplied the funding details on 11 October 2026. HOLMODRIVE was funded
by Fundação para a Ciência e a Tecnologia (FCT), Portugal, under
`PTDC/CTA-GEO/29029/2017`. ADAPT was funded by an SNSF Eccellenza Professorial
Fellowship to S. Nemiah Ladd, `PCEFP2_194211`. The SNSF record confirms the
project and recipient; the project-authored Dryad record uses this full grant
identifier: https://datadryad.org/dataset/doi%3A10.5061/dryad.nvx0k6f0v.
MEMELAND is funded by an ERC Synergy Grant under Horizon Europe,
grant agreement `101166850`, and started on 1 July 2025, as recorded at
https://cordis.europa.eu/project/id/101166850.

The MEMELAND date is the project's start date, not Ricardo's appointment date.
Do not extend a project's funding acknowledgment to unrelated work or add
funders, recipient roles, amounts, or grant dates without confirmation.

## ADAPT PhD research overview

Ricardo supplied an expanded account of his PhD work on 11 October 2026.
ADAPT's `overview_text` presents this account in four paragraphs beside the
Rotsee photo: supervision at Basel, the source-effects problem, modern German
calibration work, and vegetation-corrected records from Rotsee and Owasco.
The text uses “accounts for” vegetation effects and describes reduced isotope
shifts, avoiding a claim that all vegetation effects or uncertainty are eliminated.
This account does not establish a completed PhD or a new publication status.

The optional `overview_links` array provides exact text labels and HTTPS URLs.
The renderer inserts links while escaping the surrounding prose, preserves
paragraph breaks, and validates that every label occurs in `overview_text`.
Prof. Nemiah Ladd links to the user-supplied University of Basel profile:
https://duw.unibas.ch/en/research-groups/organic-geochemistry/team/ladd/.
The existing plain-text HOLMODRIVE overview renders identically.

## ADAPT sections aligned with the PhD overview

Ricardo requested alignment of the contribution, research question, project
description, and approach with his expanded PhD account on 11 October 2026.
The contribution and research question focus on separating hydroclimate from
terrestrial and aquatic lipid source changes, naming modern German calibration
and the vegetation-corrected Rotsee and Owasco records.

The About and Approach sections retain the wider ADAPT project’s algal aims,
including lipid biomarkers and sedimentary DNA, 20th-century phosphorus changes,
Roman-period water quality, natural variability over 10,000 years, and macroalgae
reconstructed using lipid distributions and H/C isotopes. The page distinguishes
these project aims from Ricardo’s specific PhD contribution.

Ricardo also requested the geographic label to reflect Germany or temperate
settings. Both the Research card and ADAPT detail page use
“Temperate lakes · Germany · Switzerland · USA”.

## Younger Dryas Working Group

Ricardo supplied the working-group description on 12 October 2026. The group was
formed in September 2024, and he co-coordinates it with Cecile Blanchet while
leading the lake-sediment biomarker compilation. The existing
`projects/younger-dryas.qmd` page is now generated from the main-project data.

The `collaborators` field supplies the Collaborators section. No external project
website was supplied, so the optional website link is omitted. The green
contribution box covers the 15–10.5 cal ka BP plant-wax compilation and the
chronological uncertainty and sample exclusions around transition boundaries.

The original logo is reused under
`assets/projects/younger-dryas-working-group-logo.png`. Ricardo uploaded the two
Basel meeting images on 12 October 2026; their captions describe the hybrid
discussion on 18 June 2026 and the first in-person meeting on 17–19 June 2026.
Both gallery images link to their original full-size files.

Cecile Blanchet links to her GFZ profile:
https://www.gfz.de/en/staff/cecile.blanchet/sec46.
Chanamon (Mork) Panbut's full name was confirmed in her self-authored EAG article:
https://www.eagblog.org/news/mork/.

## Homepage toolkit landscape

Ricardo supplied the landscape image in his “Lipid biomarkers toolkit” upload.
It is shown beside the section heading at its natural landscape proportions,
with a link to the original. The heading and photograph have their own layout;
the three focus cards stay in a separate, full-width grid below. On mobile,
the heading and landscape stack above the focus cards.
