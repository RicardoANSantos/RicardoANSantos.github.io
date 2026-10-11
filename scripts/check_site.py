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
        self.publication_dois = []
        self.text = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "article" and a.get("data-doi"):
            self.publication_dois.append(a["data-doi"])
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
        self.text.append(text)
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
    projects = json.loads((ROOT / "data/projects.json").read_text(encoding="utf-8"))["projects"]
    overview = pages.get((DIST / "research.html").resolve())
    expected_projects = {"projects/" + project["slug"] + ".html" for project in projects}
    overview_links = {link for link in overview.links if link.startswith("projects/") and urlsplit(link).path.endswith(".html")} if overview else set()
    if overview_links != expected_projects:
        errors.append("Research overview does not match the main projects in data/projects.json")
    papers = {paper["doi"]: paper for paper in data["published"]}
    for project in projects:
        path = "projects/" + project["slug"] + ".html"
        page = pages.get((DIST / path).resolve())
        if page is None:
            errors.append(f"Missing project page: {path}")
            continue
        ordered_dois = sorted(project.get("publication_dois", []), key=lambda doi: papers[doi]["year"])
        if page.publication_dois != ordered_dois:
            errors.append(f"{path}: project publications are missing or out of chronological order")
        expected_links = {"https://doi.org/" + doi for doi in ordered_dois}
        expected_links.update(project.get("outreach_urls", []))
        outreach = {item["url"]: item for item in data.get("outreach", [])}
        expected_links.update(
            "https://www.youtube-nocookie.com/embed/" + outreach[url]["youtube_id"]
            for url in project.get("outreach_urls", []) if outreach[url].get("youtube_id") and not outreach[url].get("image")
        )
        if project.get("project_url"):
            expected_links.add(project["project_url"])
        if project.get("funding"):
            funding = project["funding"]
            if "funding" not in page.ids or funding["grant_number"] not in " ".join(page.text):
                errors.append(f"{path}: funding section or grant number is missing")
            expected_links.add(funding["source_url"])
        for link in expected_links:
            if link not in page.links:
                errors.append(f"{path}: missing project, publication, or outreach link: {link}")
    if not (DIST / "assets/Ricardo_CV.pdf").exists():
        errors.append("Downloadable CV is missing")
    prohibited = {"AGENTS.md", "README.md", "SETUP.md", "UPDATE_WORKFLOW.md", "publications.json", "projects.json", "PROJECT_CONTENT.md", "hosting.json"}
    errors.extend(f"Source-only file leaked into site: {p.name}" for p in DIST.rglob("*") if p.name in prohibited)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        raise SystemExit(1)
    print(f"Verified {len(files)} pages, {refs} local references, image descriptions, CV, {len(data['published'])} publication DOI links, and {len(projects)} main projects with chronological paper lists.")


if __name__ == "__main__":
    main()
