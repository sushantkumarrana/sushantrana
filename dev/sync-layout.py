"""Stamps the shared header and footer into every page.

    python3 -I dev/sync-layout.py            # all pages
    python3 -I dev/sync-layout.py path/index.html ...

Edit includes/header.html or includes/footer.html, run this, commit. Each
page's <header>...</header> and <footer>...</footer> are replaced; the nav
link for the page's own URL is highlighted (keep the include files neutral).
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOP_ON = "bg-orange text-white font-semibold shadow-[0_10px_24px_-12px_rgba(var(--orange-rgb),0.7)]"
OFF = "text-body hover:bg-black/5 hover:text-orange"
GROUPS = {"/services/": "Services", "/industries/": "Industries", "/case-studies/": "Case Studies"}


def url_of(page: Path) -> str:
    rel = page.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    return "/" + rel[: -len("index.html")] if rel.endswith("/index.html") else "/" + rel


def highlight(html: str, path: str) -> str:
    cur = "/blog/" if path.startswith("/blog/") else path
    if f'href="{cur}"' not in html:
        return html
    in_dropdown = False

    def mark(m):
        nonlocal in_dropdown
        a = m.group(1)
        href = f'href="{cur}"'
        if "rounded-full px-3.5 py-2" in a:  # desktop top-level link
            return "<a " + a.replace(OFF, TOP_ON) + 'aria-current="page" ' + href
        if "rounded-xl px-3.5 py-2.5" in a:  # industries / case studies item
            a = a.replace(OFF, "bg-orange font-semibold text-white shadow-[0_10px_24px_-10px_rgba(var(--orange-rgb),0.7)]")
            in_dropdown = True
        elif "rounded-lg px-2.5 py-1.5" in a:  # services item
            a = a.replace("text-body hover:text-orange", "bg-orange font-semibold text-white")
            in_dropdown = True
        elif "block rounded-lg px-3 py-2" in a:  # mobile item
            a = a.replace("text-sm text-body", "text-sm bg-orange font-semibold text-white")
        elif "block rounded-xl px-3 py-3" in a:  # mobile top-level link
            a = a.replace("font-semibold text-ink", "font-semibold bg-orange text-white")
        else:
            return m.group(0)  # logo, Book an Appointment button: never marked
        return '<a aria-current="page" ' + a + href

    html = re.sub(r'<a ([^>]*)href="' + re.escape(cur) + '"', mark, html)
    for prefix, name in GROUPS.items():
        if in_dropdown and cur.startswith(prefix):
            html = re.sub(
                r'<button ([^>]*)data-dd-btn="' + name + r'" data-on="([^"]*)" data-off="([^"]*)"',
                lambda m: "<button " + m.group(1).replace(OFF, m.group(2)) + f'data-dd-btn="{name}" data-on="" data-off=""',
                html, count=1)
    return html


def stamp(html: str, path: str) -> str:
    header = (ROOT / "includes/header.html").read_text().strip()
    footer = (ROOT / "includes/footer.html").read_text().strip()
    a, b = html.find("<header"), html.find("</header>")
    c, e = html.find("<footer"), html.find("</footer>")
    assert 0 <= a < b < c < e, path
    return html[:a] + highlight(header, path) + html[b + 9:c] + footer + html[e + 9:]


def pages():
    out = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    return [ROOT / p for p in out if not p.startswith(("dev/", "_originals/", "includes/", "leadsforme/"))]


if __name__ == "__main__":
    targets = [Path(p).resolve() for p in sys.argv[1:]] or pages()
    changed = 0
    for p in targets:
        s = p.read_text()
        if "<header" not in s:
            continue
        t = stamp(s, url_of(p))
        if t != s:
            p.write_text(t)
            changed += 1
    print(f"{len(targets)} pages checked, {changed} updated")
