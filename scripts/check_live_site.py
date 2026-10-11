#!/usr/bin/env python3
"""Verify the public Quarto site, its content links, and its unchanged assets."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen
import json
import re
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.generator = ""
        self.links = set()
        self.publication_dois = []
        self.images = set()
        self.classes = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "article" and attrs.get("data-doi"):
            self.publication_dois.append(attrs["data-doi"])
        self.classes.update(attrs.get("class", "").split())
        if tag == "meta" and attrs.get("name") == "generator":
            self.generator = attrs.get("content", "")
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.add(attrs[key])
        if tag == "img" and attrs.get("src"):
            self.images.add(attrs["src"])


def fetch(base, path):
    url = urljoin(base.rstrip("/") + "/", path)
    request = Request(
        url + "?deployment-check=" + str(time.time_ns()),
        headers={"User-Agent": "Ricardo-Santos-Website-Check", "Cache-Control": "no-cache"},
    )
    with urlopen(request, timeout=20) as response:
        return response.read()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check(base, source):
    names = sorted(str(path.relative_to(source).with_suffix(".html")) for path in source.rglob("*.qmd") if path.name != "404.qmd")
    pages = {}
    for name in names:
        page = Page(fetch(base, name).decode("utf-8"))
        require(page.generator.lower().startswith("quarto"), f"{name}: public page is not the Quarto website")
        require(any(urlsplit(link).path.endswith("styles.css") for link in page.links), f"{name}: website stylesheet is missing")
        pages[name] = page

    projects = []
    project_file = source / "data/projects.json"
    if project_file.exists():
        projects = json.loads(project_file.read_text(encoding="utf-8"))["projects"]
        for project in projects:
            link = "projects/" + project["slug"] + ".html"
            require(link in pages["research.html"].links, f"Project is missing from the research overview: {link}")
        expected_projects = {"projects/" + project["slug"] + ".html" for project in projects}
        overview_links = {link for link in pages["research.html"].links if link.startswith("projects/") and urlsplit(link).path.endswith(".html")}
        require(overview_links == expected_projects, "Public Research overview has unexpected or missing main projects")

    home = pages["index.html"]
    require("intro" in home.classes, "The public homepage is missing the research introduction")
    index = (source / "index.qmd").read_text(encoding="utf-8")
    profiles = re.search(r'<div class="profile-links"[^>]*>(.*?)</div>', index, flags=re.S)
    require(profiles is not None, "Professional profiles are missing from the source homepage")
    for link in Page(profiles.group(1)).links:
        require(link in home.links, f"Homepage profile link is missing: {link}")

    data = json.loads((source / "data/publications.json").read_text(encoding="utf-8"))
    expected = {"https://doi.org/" + item["doi"] for item in data["published"]}
    expected.update(item["url"] for item in data.get("outreach", []))
    for link in expected:
        require(link in pages["publications.html"].links, f"Publication or outreach link is missing: {link}")

    papers = {paper["doi"]: paper for paper in data["published"]}
    for project in projects:
        name = "projects/" + project["slug"] + ".html"
        page = pages[name]
        ordered_dois = sorted(project.get("publication_dois", []), key=lambda doi: papers[doi]["year"])
        require(page.publication_dois == ordered_dois, f"{name}: public project publications are missing or out of chronological order")
        project_links = {"https://doi.org/" + doi for doi in ordered_dois}
        project_links.update(project.get("outreach_urls", []))
        outreach = {item["url"]: item for item in data.get("outreach", [])}
        project_links.update(
            "https://www.youtube-nocookie.com/embed/" + outreach[url]["youtube_id"]
            for url in project.get("outreach_urls", []) if outreach[url].get("youtube_id") and not outreach[url].get("image")
        )
        if project.get("project_url"):
            project_links.add(project["project_url"])
        if project.get("photo"):
            require(any(urlsplit(src).path.endswith(project["photo"]) for src in page.images), f"{name}: project photograph is missing")
            require(any(urlsplit(src).path.endswith(project["photo"]) for src in pages["research.html"].images), f"{name}: overview photograph is missing")
            if project.get("photo_credit_url"):
                project_links.add(project["photo_credit_url"])
        for photo in project.get("gallery", []):
            require(any(urlsplit(src).path.endswith(photo["image"]) for src in page.images), f"{name}: gallery photograph is missing: {photo['image']}")
            require(any(urlsplit(link).path.endswith(photo["image"]) for link in page.links), f"{name}: full gallery photograph link is missing: {photo['image']}")
        project_links.update(
            outreach[url]["credit_url"] for url in project.get("outreach_urls", [])
            if outreach[url].get("credit_url")
        )
        for url in project.get("outreach_urls", []):
            if outreach[url].get("image"):
                require(any(urlsplit(src).path.endswith(outreach[url]["image"]) for src in page.images), f"{name}: outreach image is missing")
        for link in project_links:
            require(link in page.links, f"{name}: public project link is missing: {link}")

    for item in data.get("outreach", []):
        if item.get("image"):
            require(any(urlsplit(src).path.endswith(item["image"]) for src in pages["publications.html"].images), "Outreach image is missing")
        if item.get("credit_url"):
            require(item["credit_url"] in pages["publications.html"].links, "Outreach author credit is missing")
    assets = {"styles.css", "assets/Ricardo_CV.pdf"}
    assets.update(item["image"] for item in data.get("outreach", []) if item.get("image"))
    assets.update(project["photo"] for project in projects if project.get("photo"))
    assets.update(photo["image"] for project in projects for photo in project.get("gallery", []))
    assets.update(path for path in Page(index).images if path.startswith("assets/"))
    for path in sorted(assets):
        require(fetch(base, path) == (source / path).read_bytes(), f"Public asset differs from the source: {path}")

    print(f"Verified the public Quarto website: {len(pages)} pages, {len(projects)} main projects and their chronological paper lists, professional profiles, {len(expected)} publication/outreach links, and {len(assets)} matching assets.")


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else "https://ricardoansantos.github.io/"
    source = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else ROOT
    for attempt in range(6):
        try:
            check(base, source)
            return
        except Exception as error:
            if attempt == 5:
                raise
            print(f"Public site not ready ({error}); retrying in 10 seconds.", flush=True)
            time.sleep(10)


if __name__ == "__main__":
    main()
