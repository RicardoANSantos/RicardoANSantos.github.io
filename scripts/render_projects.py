#!/usr/bin/env python3
"""Generate the research overview and project pages from data/projects.json."""
from html import escape
from pathlib import Path
import json
import re

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


def page_text(project):
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
        '</div>',
        photo_html(project, "../", caption=True),
        '</section>',
        '```', '',
        '## Research question', '', project["question"], '',
        '## About the project', '', project["about"], '',
        '## Approach', '', project["approach"], '',
    ]
    if project.get("links"):
        lines.extend(['## Related work', ''])
        lines.extend(f'- [{item["label"]} ↗]({item["url"]})' for item in project["links"])
        lines.append('')
    lines.extend([
        '::: {.project-page-links}',
        f'[← {group}s](../research.qmd#{anchor}) · [Publications & outreach](../publications.qmd) · [Get in touch](../contact.qmd)',
        ':::', '',
    ])
    return "\n".join(lines)


def main():
    data = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))
    projects = data["projects"]
    seen = set()
    for project in projects:
        slug = project["slug"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in seen:
            raise ValueError(f"Duplicate or invalid project slug: {slug}")
        seen.add(slug)
        if project["group"] not in {"ongoing", "past"}:
            raise ValueError(f"Invalid project group: {slug}")
        if project.get("photo"):
            path = Path(project["photo"])
            if not project["photo"].startswith("assets/") or ".." in path.parts:
                raise ValueError(f"Photo must be inside assets/: {slug}")
            if not (ROOT / path).is_file() or not project.get("photo_alt"):
                raise ValueError(f"Photo is missing or has no alt text: {slug}")
    lines = [
        '---', 'title: "Research"',
        'description: "Ongoing and past projects in organic geochemistry and paleoclimate."',
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
        (directory / (project["slug"] + ".qmd")).write_text(page_text(project), encoding="utf-8")
    print(f'Research: {len(projects)} projects, {sum(p["group"] == "ongoing" for p in projects)} ongoing and {sum(p["group"] == "past" for p in projects)} past.')


if __name__ == "__main__":
    main()
