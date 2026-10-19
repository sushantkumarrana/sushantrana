# sushantrana.com — plain HTML/CSS/JS + PHP

No Node.js, no React, no build step. Edit the files directly; what is in this
repo is exactly what runs on the live site. Read `README.md` for the folder
map, deploy steps and editing rules.

- Pages: one folder per URL with an `index.html` (`about/index.html`, `blog/<slug>/index.html` …). Every page is plain HTML; no page is PHP.
- Header and footer live once in `includes/header.html` and `includes/footer.html`. After editing either, run `python3 -I dev/sync-layout.py` to stamp them into every page (it also highlights each page's own nav link). Never edit a page's header/footer by hand.
- Service pages are generated from specs: `dev/page-gen/` (see its README).
- Styling: `assets/css/style.css`. Interactivity and animations: `assets/js/site.js`. After changing either, run `python3 -I dev/sync-layout.py`: it stamps `?v=<hash>` on every CSS/JS link, so browsers (which cache them for a week) fetch the new file.
- Lead forms post to `api/lead.php`. Keys live in `api/config.php` (git-ignored).
- Local preview: `php -S localhost:8090 dev/router.php` from the repo root.
- `.htaccess` hides `dev/`, `supabase/`, `.claude/` and every `.md` file from visitors.

## SEO before every push (new or changed pages)

Push to `html-site` is a live deploy. Before every push:

1. `python3 -I dev/seo-audit.py` must end with **0 FAIL** (it checks titles, descriptions, H1, canonical, robots, OG, JSON-LD, breadcrumbs, FAQ schema vs visible FAQ, image alt/size/WebP, broken and redirecting links, orphan pages, sitemap and robots.txt for every page).
2. Walk the relevant sections of `SEO_LAUNCH_CHECKLIST.md` and `GEO_AEO_AIO_CHECKLIST.md` (GEO, AEO, AI search readiness) and follow `SEO-RULES.md`. Latest full audit: `AI-SEARCH-AUDIT.md`.
3. A new indexable page needs: unique title and description, one H1, canonical with trailing slash, BreadcrumbList, FAQ section + FAQPage schema where it has real Q&A, WebP images with alt/width/height, at least one link to it from another page, and an entry in `sitemap.xml` (URL with trailing slash) and `llms.txt`, then `python3 -I dev/build-llms-full.py` (rebuild it after any page text change too). Placeholders and thank-you pages stay `noindex` and out of the sitemap.
4. GEO/AEO: open with a plain answer under the H1 (what it is, who it is for, next step); show real proof (case data, screenshots) with its source and caveats; keep business facts (name, phone, email, Chandigarh, countries served) identical everywhere; never invent AI-only schema or meta tags, schema-only FAQs, or claims; never change robots.txt crawler policy or Search Console AI settings without Sushant's approval.
5. Check it at 360px wide (no horizontal scroll) and run PageSpeed Insights on the live URL after deploy (target LCP ≤ 2.5 s, CLS ≤ 0.1).
