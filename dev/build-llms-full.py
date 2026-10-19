"""Builds llms-full.txt: the visible text of every page in sitemap.xml, in one file.

    python3 -I dev/build-llms-full.py

Run after changing page content or sitemap.xml, then commit llms-full.txt.
Only each page's <main> is used (no header, footer, forms, scripts or
aria-hidden decoration), in sitemap order.
"""
import re
import sys
from html import unescape
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://sushantrana.com"
SKIP = {"script", "style", "svg", "form", "noscript", "template", "button", "select", "textarea"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
BLOCK = {"p", "div", "section", "article", "header", "footer", "ul", "ol", "table", "tr", "details",
         "summary", "blockquote", "figure", "figcaption", "dl", "dt", "dd", "br", "hr"}


class MainText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.in_main, self.skip = [], False, 0

    def handle_starttag(self, tag, attrs):
        if tag == "main":
            self.in_main = True
        a = dict(attrs)
        if self.in_main and tag == "img" and a.get("alt") and not self.skip:
            self.out.append(f" [Image: {a['alt']}] ")
        if not self.in_main or tag in VOID and tag != "br":
            return
        if (self.skip or tag in SKIP or a.get("aria-hidden") == "true" or "hidden" in a
                or "marquee" in a.get("class", "")):  # marquees repeat their text to loop
            self.skip += 1
            return
        if re.fullmatch(r"h[1-6]", tag):
            self.out.append("\n\n" + "#" * min(int(tag[1]) + 1, 6) + " ")  # page title is the only "#"
        elif tag == "li":
            self.out.append("\n- ")
        elif tag in ("td", "th"):
            self.out.append(" | ")
        elif tag in BLOCK:
            self.out.append("\n")
        elif tag in ("span", "a"):
            self.out.append(" ")  # adjacent inline tags have no whitespace between them

    def handle_endtag(self, tag):
        if tag == "main":
            self.in_main = False
        if not self.in_main and tag != "main" or tag in VOID:
            return
        if self.skip:
            self.skip -= 1
        elif re.fullmatch(r"h[1-6]", tag) or tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if self.in_main and not self.skip:
            self.out.append(re.sub(r"\s+", " ", data))

    def text(self):
        lines = [re.sub(r" +", " ", l).strip() for l in "".join(self.out).split("\n")]
        lines = [l for l in lines if l not in ("-", "|")]
        return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def meta(html, pattern):
    m = re.search(pattern, html, re.S)
    return unescape(m.group(1)).strip() if m else ""


def main():
    urls = re.findall(r"<loc>(.*?)</loc>", (ROOT / "sitemap.xml").read_text())
    head = (ROOT / "llms.txt").read_text().split("\n## ")[0].strip()
    parts = [head, f"This file holds the full text of all {len(urls)} pages listed in {SITE}/sitemap.xml. "
             f"Page index: {SITE}/llms.txt"]
    for url in urls:
        rel = url.removeprefix(SITE).strip("/")
        page = ROOT / rel / "index.html"
        if not page.exists():
            sys.exit(f"FAIL {url}: no {page.relative_to(ROOT)}")
        html = page.read_text()
        p = MainText()
        p.feed(html)
        body = p.text()
        if not body:
            sys.exit(f"FAIL {url}: no <main> text")
        title = meta(html, r"<title>(.*?)</title>")
        desc = meta(html, r'<meta name="description" content="(.*?)"')
        parts.append(f"---\n\n# {title}\n\nURL: {url}\n\n{desc}\n\n{body}")
    (ROOT / "llms-full.txt").write_text("\n\n".join(parts) + "\n")
    print(f"llms-full.txt: {len(urls)} pages")


main()
