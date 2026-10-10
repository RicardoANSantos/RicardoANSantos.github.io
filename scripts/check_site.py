#!/usr/bin/env python3
"""Check the rendered site's local links, fragments, images, and expected pages."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links, self.ids, self.images, self.titles = [], set(), [], []
        self.title_active = False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.links.append(a[key])
        if tag == "img":
            self.images.append(a)
        if tag == "title":
            self.title_active = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_active = False

    def handle_data(self, text):
        if self.title_active:
            self.titles.append(text)


def main():
    errors = []
    files = list(DIST.rglob("*.html"))
    pages = {p.resolve(): Page(p.read_text(encoding="utf-8")) for p in files}
    expected = {"index.html", "research.html", "publications.html", "cv.html", "photos.html", "contact.html", "404.html"}
    missing = expected - {p.name for p in files}
    errors.extend(f"Missing page: {p}" for p in missing)
    refs = 0
    for path, page in pages.items():
        if not page.titles:
            errors.append(f"{path.name}: missing document title")
        for img in page.images:
            if not img.get("alt"):
                errors.append(f"{path.name}: image without alt text")
        for link in page.links:
            target = urlsplit(link)
            if target.scheme or target.netloc or link.startswith("data:"):
                continue
            if target.path:
                local = (DIST / unquote(target.path.lstrip("/"))) if target.path.startswith("/") else (path.parent / unquote(target.path))
            else:
                local = path
            local = local.resolve()
            if local.is_dir():
                local /= "index.html"
            refs += 1
            if not local.exists():
                errors.append(f"{path.name}: missing local target {link}")
            elif target.fragment and local.suffix == ".html" and local in pages:
                fragment = unquote(target.fragment)
                if fragment not in pages[local].ids:
                    errors.append(f"{path.name}: missing fragment {link}")
    data = json.loads((ROOT / "data/publications.json").read_text(encoding="utf-8"))
    pub = (DIST / "publications.html").read_text(encoding="utf-8") if (DIST / "publications.html").exists() else ""
    for paper in data["published"]:
        if "https://doi.org/" + paper["doi"] not in pub:
            errors.append(f"Publication DOI missing from output: {paper['doi']}")
    if not (DIST / "assets/Ricardo_CV.pdf").exists():
        errors.append("Downloadable CV is missing")
    prohibited = {"AGENTS.md", "README.md", "SETUP.md", "UPDATE_WORKFLOW.md", "publications.json", "hosting.json"}
    errors.extend(f"Source-only file leaked into site: {p.name}" for p in DIST.rglob("*") if p.name in prohibited)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Verified {len(files)} pages, {refs} local references, image descriptions, CV, and {len(data['published'])} publication DOI links.")


if __name__ == "__main__":
    main()
