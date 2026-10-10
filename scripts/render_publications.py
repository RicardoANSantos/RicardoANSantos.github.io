#!/usr/bin/env python3
"""Generate the publication page from the authoritative structured bibliography."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def authors_html(value):
    return escape(value).replace("Santos, R. N.", "<strong>Santos, R. N.</strong>")


def main():
    data = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
    seen = set()
    for paper in data["published"]:
        doi = paper["doi"]
        if doi in seen or not doi.startswith("10."):
            raise ValueError(f"Duplicate or malformed DOI: {doi}")
        seen.add(doi)
    lines = [
        '---', 'title: "Publications"',
        'description: "Peer-reviewed publications and manuscripts by Ricardo N. Santos."',
        '---', '', '::: {.page-intro}',
        'Research on lipid biomarkers, paleohydroclimate, vegetation, and lake-sediment archives. '
        '[My Google Scholar profile](https://scholar.google.com/citations?user=VAgWEa4AAAAJ&hl=en) '
        'provides an additional overview.', ':::', '',
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
    lines.extend(['```', '', '## Manuscripts in review and preparation {.manuscripts}', '',
                  'Status as listed in my October 2026 CV. These manuscripts have not yet been published.', '',
                  '```{=html}'])
    for paper in data["manuscripts"]:
        status = escape(paper["status"])
        if paper.get("journal"):
            status += " · " + escape(paper["journal"])
        lines.extend(['<article class="publication">',
                      f'<p class="pub-status">{status}</p>',
                      f'<h3>{escape(paper["title"])}</h3>',
                      f'<p class="authors">{authors_html(paper["authors"])}</p>',
                      '</article>'])
    lines.extend(['```', ''])
    (ROOT / "publications.qmd").write_text("\n".join(lines), encoding="utf-8")
    print(f'Publications: {len(data["published"])} published, {len(data["manuscripts"])} manuscripts.')


if __name__ == "__main__":
    main()
