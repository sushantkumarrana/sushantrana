# Website SEO Launch Checklist — HTML / CSS / PHP

**Purpose:** Full pre-launch, launch-day and post-launch audit for a server-rendered or hybrid HTML/CSS/PHP site. Use with `CLAUDE.md`. This is a checklist and audit specification, **not** evidence that a website has already been checked.

## How to use
1. Replace domain/market placeholders; ask Claude to inspect the REAL code, generated HTML, public staging environment, and production site where access is available.
2. Mark every item **PASS / FAIL / NOT TESTED / N/A**. Attach URL, relevant source file and proof; explain N/A.
3. Priority: **P0 = launch blocker**, **P1 = fix before/soon after launch**, **P2 = ongoing improvement**. A specific site's risk can increase severity.
4. Technical and on-page work is auditable pre-launch; backlinks and Search Console results generally depend on launch/access and should not block an otherwise ready new site.
5. Track URL inventory, issue owners and remediation in the audit table below. Do not turn unverified assumptions into PASS.

**This site:** Production domain `https://sushantrana.com` | Preferred host: apex (no www) | Business: Sushant Rana, business growth consultant | Markets: India, UAE, USA, Canada, Australia | Language: English | Hosting: Hostinger (Apache/LiteSpeed, `.htaccess`) | Automated pre-push check: `python3 -I dev/seo-audit.py`

## A. Site inventory and architecture
- [ ] Discover all indexable routes and content templates from routing configuration, PHP includes/controllers and navigation.
- [ ] Build a URL inventory: homepage, about, services, service details, contact, location, blog/articles, product/category, policies, thank-you, search/pagination and custom landing pages as applicable.
- [ ] Assign purpose, search intent and unique primary topic to each indexable URL; identify duplicate/cannibalizing topics.
- [ ] Define target language, market, service area and factual business entity information.
- [ ] Confirm crawlable architecture: important pages accessible by direct `<a href>` links and generally within a few meaningful clicks.
- [ ] Confirm XML sitemap plan and preferred URL structures before launch.
- [ ] Check that template changes don't cause missing content or duplicated metadata across PHP pages.
- [ ] Maintain an explicit redirect map for renamed URLs and old domain paths if this is a migration.

## B. On-page SEO — every public, indexable page
- [ ] Unique, specific, useful `<title>` accurately matching visible page content and user intent.
- [ ] Unique and truthful `<meta name="description">` with compelling value proposition, not keyword stuffing.
- [ ] One clear primary visible H1 conveying the page topic; H2/H3 used hierarchically and meaningfully.
- [ ] Content solves target user's question with original useful details, not filler or thin AI-generated copy.
- [ ] Intent matches query type: informational, comparison, commercial, transactional, or navigational.
- [ ] Important information appears as crawlable visible HTML text (not only image text or CSS `::before`).
- [ ] Target phrase appears naturally where it helps clarity (title/H1/intro/body/anchor), with related wording rather than repeated stuffing.
- [ ] No arbitrary keyword-density, 60-character title or 300-word minimum rules treated as Google requirements.
- [ ] Clear business facts: services, location served, process, benefits, evidence, truthful credentials, ways to contact.
- [ ] Useful internal links to related service/detail/content/contact pages with descriptive anchor text.
- [ ] External references cited where factual authority or user usefulness warrants them.
- [ ] Content is current, accurate, proofread, consistent with what the business really offers.
- [ ] Clear conversion path: accessible CTAs, contact details, working forms and usable mobile buttons.
- [ ] Duplicate/near-identical landing pages, doorway city pages and copied content reviewed and consolidated as needed.
- [ ] Real authorship, editorial responsibility, organization details and relevant first-hand experience represented accurately (not fabricated).
- [ ] If present: article byline/dates only if genuine; product pricing/availability only when up-to-date; FAQ answers actually visible.
- [ ] Natural page slug, human-readable breadcrumbs when relevant, consistent internal URL format.
- [ ] `lang` matches actual page language; multilingual content gets appropriately localized text rather than mere keyword translation.
- [ ] Page-specific OG title, description, image and preferred sharing URL are correct (optional social sharing optimization).
- [ ] No outdated `meta keywords` stuffing or misleading 'SEO score = rankings' statements.

## C. Images, media and accessibility
- [ ] Informative images have meaningful `alt`; decorative images use empty `alt=""`.
- [ ] Images relevant to page and licensed/owned for use; no misleading AI-generated proof of work.
- [ ] Dimensions explicitly known where possible to reduce layout shift.
- [ ] Resize to actual display needs; optimize file size and use modern formats with compatible fallback.
- [ ] Responsive image markup (`srcset`, `sizes`) where useful.
- [ ] Logo, site icons and main business image are high quality; image URLs work without login.
- [ ] Do not lazy-load primary above-the-fold LCP image without evaluating impact; defer off-screen images.
- [ ] Video has useful supporting description/captions when relevant; embeds don't unnecessarily block rendering.
- [ ] Mobile text readable; contrast, keyboard navigation, skip links/focus visibility, meaningful labels and errors checked.
- [ ] Every form control has a label; buttons/links have distinguishable accessible names.

## D. Technical SEO and crawlability
- [ ] HTTPS works with valid certificate, mixed content eliminated.
- [ ] Preferred hostname (www or non-www) enforced; HTTP and alternate host resolve with tested 301/308 redirects to canonical URLs.
- [ ] Slash/no-slash and `/index.php` / `/index.html` duplicates resolved consistently without redirect loops.
- [ ] Public indexable pages return genuine HTTP 200; missing pages 404; intended removals 410 where appropriate.
- [ ] No soft 404s or global catch-all redirects of missing content to homepage.
- [ ] Correct self-referencing or otherwise deliberate absolute `rel="canonical"` on canonical pages; only one effective canonical signal.
- [ ] Canonicals, redirects, hreflang, internal links and sitemap agree on the same preferred URL.
- [ ] Query parameters for ads/tracking don't create unwanted duplicate canonical URLs; real distinct content is not accidentally canonicalized away.
- [ ] robots meta and `X-Robots-Tag` headers checked on all page types; no unintended `noindex`, `nofollow` or `none`.
- [ ] `/robots.txt` available with sensible rules and production sitemap location, not accidental `Disallow: /`.
- [ ] Staging and private previews restricted with authentication; do not rely on robots.txt for confidentiality.
- [ ] Production not accidentally protected by staging password or server-level block.
- [ ] When intentionally `noindex`ing a page, allow applicable crawlers to see the directive; robots blocking can prevent Google from seeing `noindex`.
- [ ] `/sitemap.xml` loads as valid XML; uses absolute, canonical, HTTP-200, indexable URLs only.
- [ ] Sitemap excludes admin routes, staging, 404/redirecting URLs, thank-you forms, duplicate/filter variants and intentionally `noindex` URLs.
- [ ] Sitemap `lastmod` is omitted or reflects real significant updates, not today's date for everything.
- [ ] Main navigation/footer links are normal crawlable anchors; audit broken internal links and redirect chains.
- [ ] Important CSS/JS/image files are accessible to search crawlers and load reliably.
- [ ] Dynamic server-rendered content appears in the HTML response; essential content not dependent on fragile client-only logic.
- [ ] HTML `<head>` markup valid: charset, viewport, title, descriptions, canonicals, OG and JSON-LD no conflicts.
- [ ] Canonical/tag contents output-escaped correctly, including quotation marks and special characters.
- [ ] Correct `Content-Type` and UTF-8 character encoding; Hindi and English text renders correctly.
- [ ] If genuinely multilingual: implement correct reciprocal hreflang with matching localized URLs and optional `x-default`; otherwise N/A.
- [ ] If pagination exists: each meaningful page has crawlable navigation and a sensible index/canonical strategy; do not canonicalize genuinely unique paginated pages to page 1 reflexively.
- [ ] If filtered faceted URLs exist: decide which are valuable indexable landing pages and control crawl explosion appropriately.
- [ ] Set suitable host/server caching and compression; verify caching doesn't show one page's SEO tags on another.
- [ ] Content security and WAF rules don't mistakenly block legitimate browsers/search crawlers.
- [ ] Core Web Vitals and mobile rendering tested on representative homepage, service/detail and contact templates.

## E. PHP / hosting / production correctness
- [ ] All changed `.php` files pass `php -l`; verify PHP version supported by target server.
- [ ] Shared `<head>` / SEO helper used correctly; page-specific metadata passed to it once (no duplicates).
- [ ] PHP routing maps pretty URLs to real templates and correct HTTP status codes.
- [ ] Redirects and status headers set before output, with no 'headers already sent' warnings.
- [ ] Canonical base URL loaded from validated configuration, never unsanitized request host.
- [ ] HTML is escaped using correct encoding; JSON-LD produced via safe JSON encoding rather than unsafe string concatenation.
- [ ] Input validation, CSRF protection, spam prevention and parameterized DB queries present wherever applicable.
- [ ] `.env`, credentials, backups, private config, database dumps, git history and server errors not web accessible.
- [ ] Public debug mode, PHP stack traces and directory listing disabled.
- [ ] Custom 404 page preserves actual HTTP 404 response.
- [ ] Forms submit correctly and produce a clear success/error state; check emails/DB persistence if used.
- [ ] Thank-you pages are only indexable if there is a genuine public search intent; avoid exposing personal info.
- [ ] Error logs and uptime monitoring available; backups and rollback instructions documented.
- [ ] Test production-equivalent Apache/Nginx rewrite/caching rules (do not assume `.htaccess` works on Nginx).

## F. Structured data (only applicable types)
- [ ] Determine actual eligible entities/pages before adding JSON-LD; schema is not required for every page.
- [ ] Home/About: truthful `Organization` (or suitable subtype) details, official logo URL and real `sameAs` profiles when useful.
- [ ] Actual eligible local presence: `LocalBusiness` subtype and accurate public address, phone, hours, locality and URL when appropriate.
- [ ] Breadcrumbs: `BreadcrumbList` matches page hierarchy and visible navigation.
- [ ] Articles: `Article` or `BlogPosting` with genuine author/date/headline/image details when appropriate.
- [ ] Single product pages: `Product` and `Offer` data only with reliable prices, currency, availability, return/shipping info if applicable.
- [ ] Avoid fictitious review stars, invented `aggregateRating`, hidden FAQs or unsupported rich-result promises.
- [ ] Every structured-data statement matches visible page content and resolves to real URLs.
- [ ] Test applicable pages with Google Rich Results Test and generic JSON-LD with Schema Markup Validator.
- [ ] Fix critical validation issues and document warnings/feature limitations.

## G. Site speed & Core Web Vitals
- [ ] Test mobile and desktop using PageSpeed Insights/Lighthouse on EACH representative page type.
- [ ] Target good real-user Core Web Vitals: LCP <=2.5s, INP <=200ms, CLS <=0.1 at the 75th percentile.
- [ ] Optimize hero/LCP image delivery and avoid unnecessary render-blocking resources.
- [ ] Eliminate major layout shifts from images, embeds, fonts and late banners.
- [ ] Keep JS small, defer noncritical scripts and avoid expensive long tasks/third-party tags.
- [ ] Use browser caching and server compression (Brotli/Gzip as available) and inspect TTFB.
- [ ] Test on slow network/low-end phone conditions where possible, not only fast desktop.
- [ ] Verify lazy loading doesn't hide key content or degrade UX.
- [ ] Record lab scores as diagnostics, not as evidence of real-user CWV without field data.

## H. Local SEO — only if real local business/service area
- [ ] Accurate public name, address and phone (NAP) consistent across site and actual public listings.
- [ ] Contact page has address/service area, phone, hours, business email and map when helpful.
- [ ] Claim or set up Google Business Profile where eligible; correct primary/secondary categories.
- [ ] Verify website/phone/address ownership and categories per Business Profile rules.
- [ ] Build helpful location/service-area landing pages only when each gives genuinely distinct value.
- [ ] Ask for real customer reviews ethically; no fake or incentive-conditioned reviews.
- [ ] Keep business details consistent on credible local citations; remove duplicates.
- [ ] If no eligible real local presence, skip physical-location claims and local business markup.

## I. Tracking and conversion readiness
- [ ] Google Search Console property ownership verified **after domain is available** (requires account access).
- [ ] Submit production XML sitemap in Search Console and review any errors.
- [ ] Inspect representative production URLs (home, service, contact, article/product) for indexability and selected canonical after crawl.
- [ ] GA4/GTM configured when chosen; avoid duplicate tags/pageviews.
- [ ] Define valuable events (form submission, confirmed lead, call clicks, purchases where applicable).
- [ ] Test real end-to-end conversion path including failure cases and consent where required.
- [ ] Lead conversion fires on actual success, not merely button click, unless intentionally defined otherwise.
- [ ] UTM parameters supported without becoming canonical URLs or permanently redirecting to tracking variants.
- [ ] Privacy notice/cookie consent and data handling reflect actual technologies and applicable law; legal review if needed.
- [ ] Baseline dashboards: organic traffic, landing pages, GSC queries/CTR/indexing, lead conversions and CWV.

## J. Off-page SEO (manual strategy, mostly after launch)
- [ ] Official social profiles, business directory entries and brand references accurately link to preferred HTTPS homepage.
- [ ] Identify relevant niche associations, legitimate memberships, professional profiles and local chambers.
- [ ] Find relevant editorial PR opportunities: useful studies, case studies, original resources, expert interviews and partnerships.
- [ ] Create a credible 'linkable asset' (original tool/data/research/guide) aligned with users' needs.
- [ ] Reclaim legitimate unlinked brand mentions by polite outreach where appropriate.
- [ ] Find genuinely relevant broken-link replacement opportunities; provide useful replacement content.
- [ ] Review competitor editorial link patterns for ideas, not for copying spam or buying links.
- [ ] Track earned mentions, referring domains, referral visits and relevant qualified leads over time.
- [ ] Avoid pretending every directory, social profile or press release guarantees SEO value.

## K. Backlink quality & link-spam protection
- [ ] Never buy followed links for ranking manipulation or automate mass directory/forum submissions.
- [ ] Avoid PBNs, automated comments, link farms, excessive reciprocal links, paid link wheels and irrelevant bulk guest-post schemes.
- [ ] Vet link relevance, editorial context, real human audience, website quality, authenticity and possible referral value.
- [ ] Use `rel="sponsored"` or `rel="nofollow"` for paid/sponsored outbound links, as required by policy; use `rel="ugc"` for relevant UGC links.
- [ ] Do not automatically add `nofollow` to all natural editorial external citations.
- [ ] Maintain an outreach log: partner/site, reason, pitch, response, target URL, status and results. Outreach requires explicit approval.
- [ ] Monitor GSC manual actions and suspicious patterns if applicable; don't reflexively disavow every unknown link.
- [ ] Do not confuse a commercial SEO tool's proprietary 'domain authority' metric with Google's official ranking score.

## L. AI search discoverability (Google AI Overviews / AI Mode and other discovery)
- [ ] Foundation: useful, indexable, snippet-eligible content, crawlable internal links and accurate structured data.
- [ ] Answer real user questions directly and clearly; cite sources and show genuine expertise/proof where it exists.
- [ ] Use original examples, process details, images and updated factual information where beneficial.
- [ ] Entity info (name, logo, services and official profiles) is consistent across owned pages and credible mentions.
- [ ] Any crawler-specific restrictions represent intentional business/content policy; do not make unsupported universal 'allow all AI bots' claims.
- [ ] Do not treat `llms.txt`, magic AI schema, special AI metadata or GEO checklists as prerequisites for Google AI Overview eligibility.
- [ ] Set expectations: no guarantee of appearing in an AI response, ranking, rich result or indexed page.

## M. Mandatory pre-launch GO/NO-GO checks
- [ ] All P0 bugs fixed or explicitly approved with documented residual risk; recommendation marked GO / CONDITIONAL GO / NO-GO.
- [ ] Homepage + every core money/service page respond 200, show correct title/H1/canonical and are mobile usable.
- [ ] No production-wide index block; staging is restricted; production redirects and valid HTTPS confirmed.
- [ ] robots and sitemap production versions tested, not merely generated as files.
- [ ] Navigation, contact, main CTAs, submission success and any purchase funnel tested.
- [ ] Security/privacy exposures, PHP errors and misconfigured 404 status eliminated.
- [ ] SEO page inventory reviewed; high-value page duplication and broken links resolved.
- [ ] Deploy/rollback plan documented with backups.

## N. Launch day and after launch
### Launch day (requires public production access)
- [ ] Crawl live site and verify HTTP statuses, headings, meta tags, canonicals, headers, assets, internal links and forms.
- [ ] Confirm robots/indexability differences between staging and production are correct.
- [ ] Test alternate origins (`http`, `https`, `www`, non-www), redirects and sitemap URLs.
- [ ] Submit sitemap and inspect key URLs in Search Console (account access required).
- [ ] Verify real GA4 activity and test actual lead events (account access required).

### First week
- [ ] Check GSC pages/indexing report, crawl anomalies, security/manual-action alerts and submitted sitemap status.
- [ ] Investigate genuine 404s, redirect problems, canonical mismatch and noindex exclusions.
- [ ] Check mobile UX, performance and form delivery logs; fix high-impact findings.
- [ ] Validate important search snippets and brand/entity consistency when Google begins displaying results.

### First 30 days and recurring
- [ ] Track impressions, queries, clicks, CTR, organic landing page conversions and field CWV when sufficient data exists.
- [ ] Improve titles/snippets/content based on actual user intent and GSC evidence, not just vanity rankings.
- [ ] Publish high-value helpful content with clear business ownership and review cycles.
- [ ] Work on relevant editorial citations/outreach if approved; track earned coverage and referrals.
- [ ] Re-run checklist after major URL, template, navigation, product/service or platform changes.

## SEO audit evidence table (Claude must fill this in)

| Priority | URL / route | Check / issue | Evidence (HTTP, HTML, file:line, tool) | Fix | Verification | Status | Owner |
|---|---|---|---|---|---|---|---|
| P0/P1/P2 | /example | Example: duplicate canonical | Actual rendered source, not assumption | Proposed action | Retest URL + response | NOT TESTED | TBD |

## Quick commands (adapt to environment; never claim they ran when they did not)

```bash
# Inspect status, redirects, headers and index directives
curl -I https://YOUR-DOMAIN.com/
curl -IL http://YOUR-DOMAIN.com/
curl -s https://YOUR-DOMAIN.com/robots.txt
curl -s https://YOUR-DOMAIN.com/sitemap.xml

# PHP syntax: execute for each actual changed PHP file
php -l path/to/file.php

# Inspect rendered title and robots/canonical tags (basic hints only)
curl -sL https://YOUR-DOMAIN.com/ | grep -Ei '<title>|name=["\x27]robots|rel=["\x27]canonical|name=["\x27]description'
```

Recommended manual tools: **Google Search Console**, **PageSpeed Insights**, **Lighthouse**, **Google Rich Results Test**, **Schema Markup Validator**, browser mobile devtools, and (if available) a full-site crawler. A raw text `curl` test cannot simulate all browser behavior.

## Prompt to run with Claude after adding these files

> Scan this actual HTML/CSS/PHP repository and follow `CLAUDE.md` and `SEO_LAUNCH_CHECKLIST.md`. Inventory every public route and template, audit the code and any accessible staging/production URLs. Fix safe P0/P1 code issues first without changing design or breaking existing features; request approval before risky redirects, significant content rewrites, external outreach or paid tools. Do not claim live Google indexing or analytics validation without access. Return a URL-by-URL evidence table with PASS/FAIL/NOT TESTED/N/A, exact changed files, tests executed, launch GO/NO-GO and a prioritized post-launch plan.

## Official source references (recheck for updates)
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/crawling-indexing
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/crawling-indexing/block-indexing
- https://developers.google.com/search/docs/crawling-indexing/canonicalization
- https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- https://developers.google.com/search/docs/appearance/core-web-vitals
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/appearance/ai-features
- https://code.claude.com/docs/en/memory
