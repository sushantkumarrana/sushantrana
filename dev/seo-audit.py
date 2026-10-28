#!/usr/bin/env python3
"""SEO pre-push audit for every page in the repo (see SEO_LAUNCH_CHECKLIST.md).

Run from the repo root before every push:  python3 -I dev/seo-audit.py
Exit code 1 if any FAIL. WARN lines are worth a look but do not block.
Checks what can be checked offline: titles, descriptions, H1, canonical,
robots meta, Open Graph, JSON-LD, breadcrumbs, FAQ schema vs visible FAQ,
image alt/size/format, internal links (broken or redirecting), orphan pages,
sitemap vs indexable pages, robots.txt. Speed (LCP/CLS) and Search Console
need a live site: run PageSpeed Insights / GSC after deploy.
"""
import json
import re
import sys
from collections import defaultdict
from html import unescape
from pathlib import Path

SITE = "https://sushantrana.com"
ROOT = Path(".")
SKIP = {"dev", "_originals", "includes", "leadsforme", "supabase", "node_modules", ".git", ".claude", "api"}
# 301s in .htaccess: old path -> new path
REDIRECTS = {"/thank-you/": "/thank-you-consultation/", "/services/shopify-store-development/thank-you/": "/thank-you-website/",
             "/services/website-maintenance/thank-you/": "/thank-you-website/"}

fails, warns = [], []


def fail(url, msg):
    fails.append(f"FAIL {url}: {msg}")


def warn(url, msg):
    warns.append(f"WARN {url}: {msg}")


def url_of(path):
    rel = path.parent.as_posix()
    return "/" if rel == "." else f"/{rel}/"


pages = {}
for p in sorted(ROOT.rglob("index.html")):
    if p.parts[0] in SKIP:
        continue
    pages[url_of(p)] = p.read_text(encoding="utf-8")


def meta(html, attr, name):
    m = re.search(rf'<meta {attr}="{re.escape(name)}" content="([^"]*)"', html)
    return unescape(m.group(1)) if m else None


def exists(href):
    """Does a site-relative href resolve to a real file or page (or a 301 we keep)?"""
    path = href.split("#")[0].split("?")[0]
    if not path or path in REDIRECTS:
        return True
    f = ROOT / path.lstrip("/")
    return f.is_file() or (f / "index.html").is_file() or (f / "index.php").is_file() or path.startswith("/api/")


info = {}
jobs = set()
inbound = defaultdict(set)
for url, html in pages.items():
    robots = meta(html, "name", "robots") or ""
    noindex = "noindex" in robots
    info[url] = {"noindex": noindex, "title": None, "desc": None}
    placeholder = "Under development" in html
    if placeholder and not noindex:
        fail(url, "coming-soon placeholder is indexable (add noindex, keep out of sitemap)")
    if url.startswith("/thank-you") and not noindex:
        fail(url, "thank-you page must be noindex")

    t = re.findall(r"<title>([^<]*)</title>", html)
    if len(t) != 1:
        fail(url, f"{len(t)} <title> tags")
    else:
        info[url]["title"] = unescape(t[0]).strip()
    d = meta(html, "name", "description")
    if not d:
        fail(url, "missing meta description")
    info[url]["desc"] = d
    if len(re.findall(r'<meta name="description"', html)) > 1:
        fail(url, "duplicate meta description")
    h1 = len(re.findall(r"<h1[\s>]", html))
    if h1 != 1:
        (warn if noindex else fail)(url, f"{h1} <h1> tags")
    if not re.search(r'<html[^>]* lang="[a-z]', html):
        fail(url, "missing <html lang>")
    if 'name="viewport"' not in html:
        fail(url, "missing viewport meta")

    canon = re.findall(r'<link rel="canonical" href="([^"]*)"', html)
    if len(canon) != 1 and not noindex:
        fail(url, f"{len(canon)} canonical tags")
    elif canon and not noindex and canon[0] != SITE + url:
        fail(url, f"canonical {canon[0]} is not {SITE + url}")
    if not noindex:
        for prop in ("og:title", "og:description", "og:image", "og:url"):
            if not meta(html, "property", prop):
                warn(url, f"missing {prop}")

    # JSON-LD
    types, faq_qs = set(), []
    for block in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>', html, re.S):
        try:
            data = json.loads(block)
        except ValueError as e:
            fail(url, f"invalid JSON-LD: {e}")
            continue
        for node in (data.get("@graph", [data]) if isinstance(data, dict) else data):
            ts = node.get("@type")
            types.update(ts if isinstance(ts, list) else [ts])
            if node.get("@type") == "FAQPage":
                faq_qs += [q.get("name", "") for q in node.get("mainEntity", [])]
    if not noindex and url != "/" and "BreadcrumbList" not in types:
        fail(url, "no BreadcrumbList schema")
    visible_faq = re.search(r'id="faq', html) is not None
    if visible_faq and not noindex and "FAQPage" not in types:
        fail(url, "visible FAQ but no FAQPage schema")
    if faq_qs:
        text = unescape(re.sub(r"<script.*?</script>|<[^>]+>", " ", html, flags=re.S))
        for q in faq_qs:
            if q not in text:
                fail(url, f"FAQ schema question not visible on page: {q[:60]}")
    if url == "/" and not types & {"Organization", "ProfessionalService", "LocalBusiness", "Person"}:
        fail(url, "home page has no business/person schema")

    # GEO / AEO / AI search readiness (GEO_AEO_AIO_CHECKLIST.md)
    if not noindex:
        if re.search(r'content="[^"]*\b(nosnippet|max-snippet:0)\b|data-nosnippet', html):
            warn(url, "snippet restriction (nosnippet / max-snippet:0 / data-nosnippet): make sure it is deliberate")
        if re.search(r'<meta name="(ai|llm|geo)[^"]*"', html, re.I):
            fail(url, "invented AI meta tag (no search engine uses it)")
        h1_end = html.find("</h1>")
        nxt = re.search(r"<h[23][\s>]", html[h1_end:]) if h1_end > 0 else None
        intro = unescape(re.sub(r"<[^>]+>", " ", html[h1_end:h1_end + (nxt.start() if nxt else 3000)]))
        if h1_end > 0 and len(re.sub(r"\s+", " ", intro).strip()) < 80:
            warn(url, "no answer-first intro under the H1 (say what it is, who it is for, the next step)")
        if url.startswith("/blog/") and url != "/blog/" and not (types & {"Article", "BlogPosting"} and '"author"' in html and '"datePublished"' in html):
            fail(url, "blog post without Article/BlogPosting schema (author + datePublished)")
        for prof in set(re.findall(r'href="(https://(?:www\.)?(?:linkedin|instagram|facebook|twitter|x|youtube)\.com/?)"', html)):
            fail(url, f"social link points to the platform home page, not a real profile: {prof}")
    jobs.update(re.findall(r'"jobTitle":"([^"]*)"', html))

    # images
    for tag in re.findall(r"<img\b[^>]*>", html):
        src = re.search(r'\ssrc="([^"]*)"', tag)
        src = src.group(1) if src else ""
        if " alt=" not in tag:
            fail(url, f"img without alt: {src}")
        fills_box = 'data-nimg="fill"' in tag or "h-full w-full" in tag  # sized by its container, no shift
        if not fills_box and not (re.search(r'\swidth="', tag) and re.search(r'\sheight="', tag)):
            warn(url, f"img without width/height (layout shift): {src}")
        if src.startswith("/") and not re.search(r"\.(webp|avif|svg|ico)(\?|$)", src):
            warn(url, f"img not WebP/AVIF/SVG: {src}")
        if src.startswith("/") and not exists(src):
            fail(url, f"broken img src {src}")

    # internal links
    for href in set(re.findall(r'<a\b[^>]*\shref="(/[^"]*)"', html)):
        path = href.split("#")[0].split("?")[0]
        if not exists(href):
            fail(url, f"broken link {href}")
            continue
        if path in REDIRECTS:
            warn(url, f"link goes through a 301: {href} -> {REDIRECTS[path]}")
        elif path and not path.endswith("/") and "." not in path.rsplit("/", 1)[-1]:
            warn(url, f"link without trailing slash (extra 301 hop): {href}")
        target = path if path.endswith("/") else path + "/"
        if target != url:
            inbound[target].add(url)

# duplicates
for key in ("title", "desc"):
    seen = defaultdict(list)
    for url, i in info.items():
        if i[key] and not i["noindex"]:
            seen[i[key]].append(url)
    for v, urls in seen.items():
        if len(urls) > 1:
            fail(", ".join(urls), f"duplicate {key}: {v[:70]}")

# orphans
for url, i in info.items():
    if not i["noindex"] and url != "/" and not inbound[url]:
        fail(url, "orphan page: no internal link points to it")

# sitemap
sm = Path("sitemap.xml").read_text()
locs = re.findall(r"<loc>([^<]*)</loc>", sm)
indexable = {SITE + u for u, i in info.items() if not i["noindex"]}
for loc in locs:
    path = loc[len(SITE):] or "/"
    if loc not in indexable:
        fail("sitemap.xml", f"{loc} is not an indexable canonical URL" + (" (missing trailing slash?)" if path + "/" in info else ""))
for u in sorted(indexable - set(locs)):
    fail("sitemap.xml", f"indexable page missing: {u}")

# robots.txt
robots = Path("robots.txt").read_text()
if re.search(r"(?m)^Disallow:\s*/\s*$", robots):
    fail("robots.txt", "Disallow: / blocks the site")
def blocked(bot):
    """True if robots.txt disallows / for this bot (its own group, else the * group)."""
    groups, cur = {}, []
    for line in robots.splitlines():
        k, _, v = line.partition(":")
        k, v = k.strip().lower(), v.strip()
        if k == "user-agent":
            if cur and cur[-1] != "@rules":
                cur.append(v.lower())
            else:
                cur = [v.lower()]
            groups.setdefault(v.lower(), [])
        elif k in ("allow", "disallow") and cur:
            for ua in cur:
                if ua != "@rules":
                    groups[ua].append((k, v))
            cur.append("@rules")
    rules = groups.get(bot.lower(), groups.get("*", []))
    return any(k == "disallow" and v == "/" for k, v in rules)


for bot in ("Googlebot", "Bingbot", "OAI-SearchBot"):
    if blocked(bot):
        fail("robots.txt", f"{bot} is blocked from the site")
if re.search(r"(?mi)^Disallow:\s*/(assets|img|css|js)\b", robots):
    fail("robots.txt", "blocks CSS/JS/images needed to render pages")
if len(jobs) > 1:
    warn("schema", f"Person jobTitle differs between pages: {sorted(jobs)}")
if f"Sitemap: {SITE}/sitemap.xml" not in robots:
    fail("robots.txt", "no Sitemap line")

for line in fails + warns:
    print(line)
print(f"\n{len(pages)} pages, {sum(not i['noindex'] for i in info.values())} indexable, {len(locs)} in sitemap: {len(fails)} FAIL, {len(warns)} WARN")
sys.exit(1 if fails else 0)
