#!/usr/bin/env python3
"""Generate the research overview and project pages from data/projects.json."""
from html import escape
from pathlib import Path
import json
import re

from render_publications import authors_html

ROOT = Path(__file__).resolve().parents[1]
CAMERA = '<svg viewBox="0 0 64 48" width="64" height="48" fill="none" aria-hidden="true"><path d="M8 12h12l5-7h14l5 7h12v30H8V12Z" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/><circle cx="32" cy="26" r="10" stroke="currentColor" stroke-width="1.5"/><path d="M47 18h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>'


def photo_html(project, prefix="", caption=False):
    title = escape(project["title"], quote=True)
    if project.get("photo"):
        path = escape(prefix + project["photo"], quote=True)
        alt = escape(project["photo_alt"], quote=True)
        content = f'<img src="{path}" alt="{alt}" loading="lazy" decoding="async">'
        if caption and project.get("photo_caption"):
            content += "<figcaption>" + escape(project["photo_caption"]) + "</figcaption>"
    else:
        content = (
            f'<div class="project-photo-placeholder" role="img" aria-label="Photo placeholder for {title}">'
            + CAMERA
            + '<span>Project photo to come</span>'
            + '</div>'
        )
    return '<figure class="project-photo">' + content + '</figure>'


def card_html(project):
    title = escape(project["title"])
    url = "projects/" + project["slug"] + ".html"
    phase = escape(project["phase"])
    if project.get("period"):
        phase += " · " + escape(project["period"])
    return "\n".join([
        '<article class="project-card">',
        f'<a class="project-photo-link" href="{url}" aria-label="Explore {title}">',
        photo_html(project),
        '</a>',
        '<div class="project-card-copy">',
        f'<p class="eyebrow">{escape(project["location"])}</p>',
        f'<h3><a href="{url}">{title}</a></h3>',
        f'<p>{escape(project["summary"])}</p>',
        f'<p class="project-phase">{phase}</p>',
        f'<a class="project-more" href="{url}">Explore project <span aria-hidden="true">→</span></a>',
        '</div>',
        '</article>',
    ])



def project_papers(project, bibliography):
    papers = {paper["doi"]: paper for paper in bibliography["published"]}
    # Stable sorting preserves the supplied within-year publication order.
    return sorted(
        (papers[doi] for doi in project.get("publication_dois", [])),
        key=lambda paper: paper["year"],
    )


def publication_html(paper):
    doi = escape(paper["doi"], quote=True)
    journal = escape(paper["journal"])
    if paper.get("details"):
        journal += ", " + escape(paper["details"])
    return "\n".join([
        f'<article class="publication" data-doi="{doi}">',
        f'<h3><a href="https://doi.org/{doi}">{escape(paper["title"])}</a></h3>',
        f'<p class="authors">{authors_html(paper["authors"])}</p>',
        f'<p class="journal"><em>{journal}</em> · {paper["year"]}</p>',
        f'<p class="doi"><a href="https://doi.org/{doi}">DOI: {doi} ↗</a></p>',
        '</article>',
    ])


def outreach_html(item):
    url = escape(item["url"], quote=True)
    outlet = escape(item["outlet"])
    if item.get("language"):
        outlet += " · " + escape(item["language"])
    lines = [
        '<article class="publication">',
        f'<h3><a href="{url}">{escape(item["title"])}</a></h3>',
        f'<p class="journal"><em>{outlet}</em></p>',
        f'<p class="authors">{escape(item["description"])}</p>',
        f'<p class="doi"><a href="{url}">{escape(item.get("link_label", "Read more"))} ↗</a></p>',
    ]
    if item.get("youtube_id"):
        video_id = item["youtube_id"]
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            raise ValueError(f"Invalid YouTube video ID: {video_id}")
        lines.append(
            '<div class="project-video">'
            f'<iframe src="https://www.youtube-nocookie.com/embed/{video_id}" '
            f'title="{escape(item["title"], quote=True)}" loading="lazy" '
            'width="560" height="315" referrerpolicy="strict-origin-when-cross-origin" '
            'allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe>'
            '</div>'
        )
    lines.append('</article>')
    return "\n".join(lines)


def page_text(project, bibliography):
    group = "Ongoing project" if project["group"] == "ongoing" else "Past project"
    anchor = "ongoing-projects" if project["group"] == "ongoing" else "past-projects"
    facts = [('Focus', project["phase"])]
    if project.get("period"):
        facts.append(('Period', project["period"]))
    if project.get("role"):
        facts.append(('My role', project["role"]))
    facts_html = "".join(f'<div><dt>{escape(label)}</dt><dd>{escape(value)}</dd></div>' for label, value in facts)
    lines = [
        '---',
        'title: ' + json.dumps(project["title"], ensure_ascii=False),
        'description: ' + json.dumps(project["summary"], ensure_ascii=False),
        'body-classes: project-page',
        '---', '', '```{=html}',
        '<section class="project-overview" aria-label="Project overview">',
        '<div class="project-overview-copy">',
        f'<p class="eyebrow">{escape(project["location"])}</p>',
        f'<p class="project-group">{group}</p>',
        f'<p class="project-lead">{escape(project["summary"])}</p>',
        f'<dl class="project-facts">{facts_html}</dl>',
        f'<p><a class="project-more" href="{escape(project["project_url"], quote=True)}">Project website <span aria-hidden="true">↗</span></a></p>',
        '</div>',
        photo_html(project, "../", caption=True),
        '</section>',
        '```', '',
        '## Research question', '', project["question"], '',
        '## About the project', '', project["about"], '',
        '## Approach', '', project["approach"], '',
    ]
    papers = project_papers(project, bibliography)
    if papers:
        lines.extend(['## Publications', ''])
        if len(papers) > 1:
            lines.extend(['Listed from oldest to newest.', ''])
        lines.append('```{=html}')
        lines.extend(publication_html(paper) for paper in papers)
        lines.extend(['```', ''])
    if project.get("outreach_urls"):
        outreach = {item["url"]: item for item in bibliography.get("outreach", [])}
        lines.extend(['## Outreach {.outreach}', '', '```{=html}'])
        lines.extend(outreach_html(outreach[url]) for url in project["outreach_urls"])
        lines.extend(['```', ''])
    lines.extend([
        '::: {.project-page-links}',
        f'[← {group}s](../research.qmd#{anchor}) · [Publications & outreach](../publications.qmd) · [Get in touch](../contact.qmd)',
        ':::', '',
    ])
    return "\n".join(lines)


def main():
    data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    projects = data["projects"]
    bibliography = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
    known_dois = {paper["doi"] for paper in bibliography["published"]}
    known_outreach = {item["url"] for item in bibliography.get("outreach", [])}
    seen = set()
    for project in projects:
        slug = project["slug"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in seen:
            raise ValueError(f"Duplicate or invalid project slug: {slug}")
        seen.add(slug)
        if project["group"] not in {"ongoing", "past"}:
            raise ValueError(f"Invalid project group: {slug}")
        if not project.get("project_url", "").startswith("https://"):
            raise ValueError(f"Missing HTTPS project website: {slug}")
        dois = project.get("publication_dois", [])
        urls = project.get("outreach_urls", [])
        if len(dois) != len(set(dois)) or not set(dois) <= known_dois:
            raise ValueError(f"Duplicate or unknown project publication: {slug}")
        if len(urls) != len(set(urls)) or not set(urls) <= known_outreach:
            raise ValueError(f"Duplicate or unknown project outreach: {slug}")
        if project.get("photo"):
            path = Path(project["photo"])
            if not project["photo"].startswith("assets/") or ".." in path.parts:
                raise ValueError(f"Photo must be inside assets/: {slug}")
            if not (ROOT / path).is_file() or not project.get("photo_alt"):
                raise ValueError(f"Photo is missing or has no alt text: {slug}")
    lines = [
        '---', 'title: "Research"',
        'description: "ADAPT, MEMELAND, and HOLMODRIVE: ongoing and past research on biomarkers, climate, and environmental change."',
        '---', '', '::: {.page-intro}', data["introduction"], ':::', '',
        data["context"], '', '```{=html}',
        '<nav class="project-jumps" aria-label="Research sections">',
        '<a href="#ongoing-projects">Ongoing projects <span aria-hidden="true">↓</span></a>',
        '<a href="#past-projects">Past projects <span aria-hidden="true">↓</span></a>',
        '</nav>', '```', '',
    ]
    for group, heading in [('ongoing', 'Ongoing projects'), ('past', 'Past projects')]:
        lines.extend([
            f'## {heading} {{#{group}-projects}}', '', '```{=html}',
            f'<div class="projects-grid projects-grid--{group}">',
        ])
        lines.extend(card_html(project) for project in projects if project["group"] == group)
        lines.extend(['</div>', '```', ''])
    lines.extend([
        '## Collaboration and scientific exchange', '',
        'I welcome conversations about biomarker proxy development, vegetation correction, '
        'multi-proxy reconstructions, and human–environment interactions. [Get in touch →](contact.qmd)', '',
    ])
    (ROOT / "research.qmd").write_text("\n".join(lines), encoding="utf-8")
    directory = ROOT / "projects"
    directory.mkdir(exist_ok=True)
    for project in projects:
        (directory / (project["slug"] + ".qmd")).write_text(page_text(project, bibliography), encoding="utf-8")
    print(f'Research: {len(projects)} projects, {sum(p["group"] == "ongoing" for p in projects)} ongoing and {sum(p["group"] == "past" for p in projects)} past.')


if __name__ == "__main__":
    main()
