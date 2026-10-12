#!/usr/bin/env python3
"""Generate the publications and outreach page from structured records."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def authors_html(value):
    return escape(value).replace("Santos, R. N.", "<strong>Santos, R. N.</strong>")



def outreach_credit_html(item):
    name = escape(item["credit_name"])
    if item.get("credit_url"):
        name = f'<a href="{escape(item["credit_url"], quote=True)}">{name}</a>'
    return f'<p class="outreach-credit">{escape(item.get("credit_label", "Credit"))}: {name}</p>'


def outreach_image_html(item, prefix=""):
    if not item.get("image"):
        return ""
    path = Path(item["image"])
    if not item["image"].startswith("assets/") or ".." in path.parts:
        raise ValueError("Outreach images must be inside assets/")
    if not (ROOT / path).is_file() or not item.get("image_alt"):
        raise ValueError("Outreach image is missing or has no alt text")
    src = escape(prefix + item["image"], quote=True)
    alt = escape(item["image_alt"], quote=True)
    url = escape(item["url"], quote=True)
    link_attrs = ""
    play = ""
    if item.get("youtube_id"):
        label = escape("Watch " + item["title"] + " on YouTube", quote=True)
        link_attrs = f' class="outreach-video-link" aria-label="{label}"'
        play = (
            '<span class="outreach-play" aria-hidden="true">'
            '<svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor">'
            '<path d="M7 4v16l14-8z"/></svg></span>'
        )
    return (
        '<figure class="outreach-image">'
        f'<a href="{url}"{link_attrs}><img src="{src}" alt="{alt}" loading="lazy" decoding="async">{play}</a>'
        '</figure>'
    )


def main():
    data = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
    seen = set()
    for paper in data["published"]:
        doi = paper["doi"]
        if doi in seen or not doi.startswith("10."):
            raise ValueError(f"Duplicate or malformed DOI: {doi}")
        seen.add(doi)
    lines = [
        '---', 'title: "Publications & outreach"',
        'description: "Research papers, outreach, and science communication."',
        '---', '',
        '## Peer-reviewed publications', '', '```{=html}'
    ]
    for year in sorted({p["year"] for p in data["published"]}, reverse=True):
        lines.append(f'<h3 class="publication-year" id="publications-{year}">{year}</h3>')
        for paper in (p for p in data["published"] if p["year"] == year):
            doi = escape(paper["doi"], quote=True)
            journal = escape(paper["journal"])
            if paper.get("details"):
                journal += ", " + escape(paper["details"])
            lines.extend([
                '<article class="publication">',
                f'<h3><a href="https://doi.org/{doi}">{escape(paper["title"])}</a></h3>',
                f'<p class="authors">{authors_html(paper["authors"])}</p>',
                f'<p class="journal"><em>{journal}</em> · {year}</p>',
                f'<p class="doi"><a href="https://doi.org/{doi}">DOI: {doi} ↗</a></p>',
                '</article>'
            ])
    lines.extend(['```', ''])
    if data.get("outreach"):
        lines.extend(['## Outreach {.outreach}', '', '```{=html}'])
        for item in data["outreach"]:
            url = escape(item["url"], quote=True)
            outlet = escape(item["outlet"])
            if item.get("language"):
                outlet += " · " + escape(item["language"])
            lines.extend([
                '<article class="publication outreach-item' + (' outreach-item--with-image' if item.get("image") else '') + '">',
                *([outreach_image_html(item)] if item.get("image") else []),
                '<div class="outreach-copy">',
                f'<h3><a href="{url}">{escape(item["title"])}</a></h3>',
                f'<p class="journal"><em>{outlet}</em></p>',
                *([f'<p class="outreach-award"><strong>{escape(item["recognition"])}</strong></p>'] if item.get("recognition") else []),
                f'<p class="authors">{escape(item["description"])}</p>',
                *([outreach_credit_html(item)] if item.get("credit_name") else []),
                f'<p class="doi"><a href="{url}">{escape(item.get("link_label", "Read more"))} ↗</a></p>',
                '</div>',
                '</article>'
            ])
        lines.extend(['```', ''])
    (ROOT / "publications.qmd").write_text("\n".join(lines), encoding="utf-8")
    print(f'Publications: {len(data["published"])} published, {len(data.get("outreach", []))} outreach items.')


if __name__ == "__main__":
    main()
