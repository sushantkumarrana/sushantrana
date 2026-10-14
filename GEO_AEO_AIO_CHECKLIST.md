# GEO + AEO + AIO — Pre-launch & Ongoing Checklist

**For:** a website built with HTML, CSS, and PHP, maintained using Claude / Claude Code.  
**Last reviewed:** 15 October 2026.  
**Companion documents:** `CLAUDE.md` and `SEO_LAUNCH_CHECKLIST.md`.

> **How to use:** Claude must audit every public route and its shared PHP template against this list before launch and after relevant edits. Record `PASS`, `FAIL`, `NOT TESTED`, or `N/A` with evidence. Do not mark a live Google/ChatGPT/analytics check PASS without actual access and verification.

## 0. Understand the terms correctly

- **SEO:** Search Engine Optimization — the foundational discipline covering crawlability, indexing, relevance, quality, UX and search visibility.
- **GEO:** Generative Engine Optimization — industry label for making useful, trustworthy information discoverable and citable in generative AI experiences.
- **AEO:** Answer Engine Optimization — industry label for providing accurate, easy-to-understand answers to users' questions, including conventional search and AI-assisted answers.
- **AIO:** Ambiguous, non-standard industry shorthand (often “AI Optimization” or “Artificial Intelligence Optimization”); in this project it means **AI Search Readiness**, not a separate Google-approved ranking system.
- **AI Overviews and AI Mode:** specific Google Search features, **not** synonyms for AIO.

**Reality check:** In Google's official guidance, good SEO is the foundation for generative AI search; there is no mandatory AI-only schema, `llms.txt` file, tiny-content “chunking” technique, or magic metadata. Visibility, citations, rankings and traffic cannot be guaranteed. Optimize for users first, not for manipulating AI responses.

## Priority legend

- **P0 / pre-launch blocker:** Production public content unintentionally blocked, broken main site, security/privacy exposure or other critical foundation problem.
- **P1 / fix soon:** Important content/indexability/entity accuracy/schema/UX issue affecting core business pages.
- **P2 / useful improvement:** Research, richer helpful explanations, authentic authority-building or analytics refinements.
- **N/A:** Not relevant to this website (for example `Product` schema on a non-ecommerce website).

## A. AI-search crawlability & access (technical foundation)

- [ ] [P0] Every public indexable page that should appear in Search returns genuine HTTP `200`, not a soft 404 or accidental redirect.
- [ ] [P0] Production pages have no accidental `noindex`, `nosnippet`, `X-Robots-Tag: noindex`, or global robots exclusion; staging is protected independently.
- [ ] [P0] Googlebot and Bingbot can access intended pages through `robots.txt`, WAF, CDN, and server firewall rules; confirm with crawler tools/logs where available.
- [ ] [P1] Intended Google generative-AI participation is verified in **Search Console → Settings → Search generative AI**. Default may be 'Include'; do not change this account-level setting without owner permission.
- [ ] [P1] Google snippet eligibility is maintained for pages intended to appear as supporting sources. Any `max-snippet`, `data-nosnippet`, or `nosnippet` decisions are deliberate, not blindly removed.
- [ ] [P1] `https://` and preferred hostname, canonical URLs, redirects, sitemap and indexable URL status are consistent.
- [ ] [P1] Canonical URLs are absolute and correct; duplicate query/filter/campaign variants do not compete as separate main pages.
- [ ] [P1] Important content is present in server-rendered HTML from PHP (or otherwise reliably rendered); it is not accessible only after a click, login, blocked JS or animation.
- [ ] [P1] Primary internal links use real `<a href="...">` elements with sensible anchor text; key landing pages are not orphaned.
- [ ] [P1] A current sitemap with only canonical 200/indexable URLs is accessible; real `lastmod` values reflect material modifications.
- [ ] [P1] No incorrect `robots.txt` directives accidentally block CSS/JS/images required to render or understand main content.
- [ ] [P1] User-selected AI crawler policy is written down, verified in live robots.txt and respected in host/CDN bot rules; avoid generic "allow all AI robots" advice.
- [ ] [P2] If AI crawler access matters, check authentic server logs and official bot IP/user-agent guidance rather than trusting a spoofable user-agent string alone.
- [ ] [P2] Test 1–3 public URLs as a browser without credentials and inspect their rendered HTML, visible text, links and structured data.

### OpenAI crawler distinction — do not mix these up

- [ ] [P1] Decide whether **`OAI-SearchBot`** may crawl public pages for ChatGPT Search; allow it only if that matches the owner's distribution policy.
- [ ] [P2] Decide **separately** whether **`GPTBot`** may crawl for potential model training. Blocking GPTBot does not mean you must block OAI-SearchBot.
- [ ] [P2] Understand that **`ChatGPT-User`** handles some user-triggered visits; it is not the automatic search crawler, and robots rules may not control all user-triggered fetches.
- [ ] [P2] If advertising on ChatGPT, review **`OAI-AdsBot`** landing-page accessibility separately; this is relevant only to submitted ads, not organic SEO.
- [ ] [P1] Verify that robots.txt is not internally contradictory and any user-agent group contains valid syntax. Never publish a placeholder example without reviewing its effect on your site.

**Optional example (use ONLY after choosing the policy, not as an automatic default):**

```txt
# Example: allow ChatGPT search discovery while excluding OpenAI training crawl
User-agent: OAI-SearchBot
Allow: /

User-agent: GPTBot
Disallow: /

# Apply Googlebot/Bingbot and other site-wide rules separately as needed.
# If a site-wide group exists, review how crawler-specific groups interact.
```

## B. AEO — Helpful answer-focused content

- [ ] [P1] Every key page answers its main visitor question/intention accurately and clearly, rather than hiding the answer in promotional filler.
- [ ] [P1] Where appropriate, the page opens with a concise direct explanation of **what it is, who it is for, and the main benefit/action**.
- [ ] [P1] Use a meaningful unique H1 and logical H2/H3 headings that match the actual topics; headings are written for human scanning, not keywords alone.
- [ ] [P1] Key services/products have concrete attributes (features, specifications, delivery/eligibility, use cases, limitations and next steps where relevant).
- [ ] [P1] Questions worth answering are chosen from genuine customer needs, support queries, sales conversations and search research, not bulk-generated long-tail variations.
- [ ] [P1] Price, timings, process, location, warranties/returns, scope of service and exclusions are explained wherever commercially and factually relevant; don't invent details.
- [ ] [P1] Answers distinguish facts from opinions, estimates, promises and eligibility conditions.
- [ ] [P1] Important claims are checked and, where warranted, linked to reputable primary sources or documented original evidence.
- [ ] [P1] Clearly identify the business/author and provide legitimate contact, about, policy, support and trust information as appropriate.
- [ ] [P2] Build an FAQ section ONLY when it genuinely helps users, with real visible questions and non-duplicative, complete answers.
- [ ] [P2] Use tables, steps, comparisons and examples where they help users understand the information; never add arbitrary formats just to “feed AI.”
- [ ] [P2] Include accurate short summaries / key definitions on complex topics when useful; do not force every page into unnatural 40–60 word answers.
- [ ] [P2] Provide clear contextual internal links to detailed explanations instead of creating shallow near-duplicate pages for every phrasing.
- [ ] [P2] Check that content reads naturally in the actual audience's language (English, Hindi, Hinglish, etc.) and matches `lang` / hreflang where applicable.
- [ ] [P2] Ensure the mobile version contains the same important content and information as desktop.

**2026 update:** Google's FAQ rich-result feature stopped appearing in Google Search in May 2026 and documentation was removed in June 2026. Useful on-page FAQs can still be good for users. **Do not add `FAQPage` schema solely to promise Google FAQ rich results.**

## C. GEO — Originality, credibility and citation-worthiness

- [ ] [P1] Main pages contain distinctive information that cannot be swapped with any competitor (actual method, results, portfolio, examples, expertise or firsthand details).
- [ ] [P1] No copied/scraped competitor copy, mass-produced generic articles, misleading testimonials, fake credentials or invented data.
- [ ] [P1] Business name, industry, key offerings, official logo and contact information match across Home, About, Contact, service pages and credible external profiles.
- [ ] [P1] At least one useful primary-source proof point is present on important conversion pages where the business has such evidence (real work, sample, case study, demo, certification or verifiable customer feedback).
- [ ] [P1] Claims involving statistics, laws, medical/financial issues, prices or dates have source, scope and current review when required.
- [ ] [P1] Pages give enough context for a quoted statement to remain accurate when seen away from its original paragraph.
- [ ] [P2] Byline / author bio is added for expert articles when authorship genuinely matters; never fake names or expertise.
- [ ] [P2] Publish case studies with permissions and defensible results (what problem, methodology, outcome and caveats) when applicable.
- [ ] [P2] Produce optional link-worthy resources—original studies, tools, comparison guides, demos or reference content—only where useful to your audience.
- [ ] [P2] Identify high-value themes and user questions; cover related subtopics adequately inside coherent content clusters without creating dozens of thin keyword permutations.
- [ ] [P2] Review high-impact content when facts change; date-stamp only real meaningful updates, not artificial 'freshness' edits.
- [ ] [P2] Seek authentic third-party mentions, expert contributions and relevant earned citations with approval. Avoid paid/fake mentions, link farms and mass forum spam.
- [ ] [P2] Track mentions and citations as observed signals, not a promise of AI ranking or guaranteed ChatGPT recommendation.

## D. Entity and structured-data clarity

- [ ] [P1] Use accurate `Organization` or applicable subtype data with legal/trading name, correct URL, logo and true identity details where supported.
- [ ] [P1] `sameAs` URLs (if used) link to actual official profiles—not unrelated directories or a list of fabricated accounts.
- [ ] [P1] Service/product descriptions match on-page content, GBP/merchant data (if applicable), and any actual structured data.
- [ ] [P1] Use `LocalBusiness` only for a legitimate eligible business location or relevant supported entity; never invent address, hours, ratings or service areas.
- [ ] [P1] Use `Product` / `Offer` / merchant listing markup only when there is a real purchasable product and maintained price, currency, availability etc.
- [ ] [P1] Use `Article` / `BlogPosting`, `BreadcrumbList`, and other types only where genuinely appropriate; match the visible page content.
- [ ] [P1] Validate JSON-LD syntax and applicable Google-supported features; no duplicate/conflicting schema generated by shared and page-specific PHP templates.
- [ ] [P1] Do not claim Google, ChatGPT or Gemini require special “GEO schema”, `AIOptimization` schema, `llms.txt`, invented `<meta name="ai">`, or mandatory FAQPage markup.
- [ ] [P2] Clear About/Contact pages explain real entity identity, industry, specializations, audience, service areas and official public profiles.
- [ ] [P2] For multilingual sites, set `<html lang>` and reciprocal `hreflang` only for real separate localized URLs; ensure translations are meaningful.
- [ ] [P2] Keep public business details accurate in credible local directories, professional sites, industry listings and partner pages. Off-site editing and submissions need authorization.

## E. Multimedia, mobile and AI-agent readability

- [ ] [P1] Important images have descriptive informative `alt` text when appropriate; decorative imagery has empty alt, not keyword stuffing.
- [ ] [P1] Product imagery and descriptions accurately represent the actual items, dimensions, materials and variants. Do not use misleading synthetic images as proof of real outcomes.
- [ ] [P1] On mobile, headings, copy, pricing/offer details, CTAs, tables and forms remain readable and usable; test keyboard and touch interactions.
- [ ] [P1] Main navigation, forms and important actions have clear labels and understandable semantics; link actions work without hidden hover-only controls.
- [ ] [P1] No important text exists only in graphics with no accessible textual equivalent.
- [ ] [P2] Helpful video has a meaningful title/caption/transcript where appropriate; useful original images have consistent image SEO.
- [ ] [P2] For sites where automated assistants may help shoppers or customers, keep product/service data consistent, tasks understandable and forms predictable; never bypass authentication or security for agents.
- [ ] [P2] Consider agent-friendly conventions and emerging commerce integrations only for actual business needs; they are NOT a generic AI search prerequisite.

## F. Channel-appropriate discoverability

- [ ] [P1] Check important pages with Google Search Console URL Inspection after they are live; verify canonical/indexing/snippet access rather than assuming eligibility from the sitemap.
- [ ] [P1] Check **Search Console → Settings → Search generative AI** owner preference before AI search visibility work; respect opt-out decisions.
- [ ] [P1] Set up Bing Webmaster Tools and submit a sitemap where relevant; verify Bing indexing rather than assuming Google indexing implies Bing indexing.
- [ ] [P2] When available for the site, review **Google Search Console → Generative AI performance report** (AI Overviews / AI Mode impressions). As of Aug 31, 2026 the feature is rolled out worldwide, but the report may not appear with insufficient impressions.
- [ ] [P2] When available, review **Bing Webmaster Tools → AI Performance** for Microsoft Copilot and related cited pages/grounding queries; data is sampled/aggregated, not a full prompt log.
- [ ] [P2] If relevant, verify current **Google Business Profile** details and (for actual sellers) **Google Merchant Center** catalog/feed; don't create fake business premises or products.
- [ ] [P2] Compare search visibility and referred user conversions via GA4/source and campaign data; distinguish observable clicks from AI references with no referral.
- [ ] [P2] Track a small, fixed set of actual buyer/customer questions across major public AI/search experiences, noting observation date, geography/account variability and exact cited URL (if any).
- [ ] [P2] Record source mentions and answer accuracy, not only whether the brand name appears. AI responses can change across time, user, model and phrasing.
- [ ] [P2] Do not label third-party “AI visibility scores,” authority scores or prompt-monitoring estimates as official Google/OpenAI ranking data.

## G. PHP / server-rendered website implementation

- [ ] [P1] Shared PHP `<head>` include accepts per-route SEO inputs and outputs exactly one accurate title, description and canonical link; output values safely escaped.
- [ ] [P1] Important page copy and internal links exist in the server response from PHP; don't require JavaScript for all core content.
- [ ] [P1] Structured data is emitted with safe JSON encoding (`json_encode` with proper flags) using actual verified page data.
- [ ] [P1] Meta robots (HTML) and `X-Robots-Tag` (HTTP) do not conflict across PHP templates, redirects, caching/CDN or staging config.
- [ ] [P1] Error routes send correct statuses before output; missing pages are not 200 “soft 404s.”
- [ ] [P1] Verify live robots.txt and sitemap are actually served at the intended public URL regardless of whether they are static files or PHP-generated.
- [ ] [P1] Re-test `<head>` and actual rendered answers after editing shared PHP includes or routing; one template change may affect many pages.
- [ ] [P2] HTML language declarations, headings, lists, blockquotes, tables and form labels are correctly structured to assist visitors and machine reading alike.
- [ ] [P2] Use lightweight HTML/CSS/JS and cache headers without caching one URL's title/schema onto another URL.
- [ ] [P2] If a blog/CMS is added later, enforce editorial factual review and per-post uniqueness rather than publishing unreviewed generated pages.

## H. Practices to avoid / optional items

- [ ] [P1] No AI-content scaled spam, doorway pages, purchased followed links, fabricated awards/reviews, fake expert profiles or mass-produced answer fragments.
- [ ] [P1] No statement that creating a file/schema will force Google AI Overviews, ChatGPT or Copilot to cite the website.
- [ ] [P1] No automatic changes to crawler policies or Google Search Console AI participation controls without explicit project owner approval.
- [ ] [P2] `llms.txt` is **optional and not used by Google Search** for AI features. Add only for a documented third-party use case and maintain it; don't consider its absence a launch failure.
- [ ] [P2] No arbitrary answer length, exact-match prompt count, “citation density,” word count, keyword density or one-sentence paragraphs mandated by AI SEO folklore.
- [ ] [P2] No blanket recommendation to add `FAQPage`, `Speakable`, or other schema without eligibility and a real fit.
- [ ] [P2] No indiscriminate AI bot blocking or allow-all rules; model training and search discovery are separate product/policy choices.

## I. Pre-launch sign-off (the minimum evidence)

- [ ] An inventory covers **all indexable routes** and their page types; high-priority pages audited individually.
- [ ] Homepage, About, service/product pages, Contact and helpful articles (if present) have accurate entity facts and satisfy visitor intent.
- [ ] Critical search/AI discovery blockers are resolved; remaining optional GEO/AEO tasks are clearly separated from blockers.
- [ ] No deceptive claims, manufactured proof, unsupported structured-data assertions or unapproved bot control changes.
- [ ] Status of Google AI inclusion, GSC, Bing/AI reporting and ChatGPT crawler policy is documented as `PASS/FAIL/NOT TESTED/N/A` with actual evidence.
- [ ] Owner has reviewed any needed content claims, crawler privacy/training choices, brand profile links and external outreach proposals.
- [ ] After launch, repeat checks on real public URLs and periodically review live indexing, AI visibility and lead quality.

## J. Mandatory Claude audit output

1. **Executive result:** `GO`, `CONDITIONAL GO`, or `NO-GO` with a short explanation.
2. **URL inventory:** page type, canonical, index directive, question/intent served, structured data and visible evidence.
3. **Findings table:** `Priority | URL | Area (SEO / GEO / AEO / AIO) | Check | Evidence | Exact file + line | Fix | Test actually run | Status | Owner`.
4. **Repairs:** enumerate files edited and actual post-fix verification (including `php -l` where relevant).
5. **Cannot verify yet:** Search Console account settings/reports, public search inclusion and crawler/log visibility, if access absent.
6. **Follow-up:** Launch Day, Week 1, Days 30/60; owner-approval items distinct from automated code fixes.

### Ready-to-paste Claude Code instruction

> Read `CLAUDE.md`, `SEO_LAUNCH_CHECKLIST.md`, and `GEO_AEO_AIO_CHECKLIST.md` completely. Audit this actual HTML/CSS/PHP repository and all indexable routes for traditional SEO, GEO, AEO and AI Search Readiness. Prioritize crawlability, accurate helpful answer-first information, original evidence, entity consistency, valid relevant schema, ChatGPT/Google/Bing crawler policy, mobile usability, and Google/Bing AI visibility measurement. Fix safe code-level problems without altering the design or inventing business facts. Do not create AI-only schema, useless `llms.txt`, fake FAQ rich-result promises, or thin prompt-variant pages. Never claim a live index check or GSC setting was verified without account/live-site access. Deliver evidence-based per-URL PASS/FAIL/NOT TESTED/N/A, changes made, unresolved owner actions and a GO/NO-GO decision.

## Official sources / evidence (reviewed October 2026)

- Google: Generative AI optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google: AI features & your website: https://developers.google.com/search/docs/appearance/ai-features
- Google: Search Console AI inclusion control: https://support.google.com/webmasters/answer/16908024
- Google: Search Console Generative AI performance report: https://support.google.com/webmasters/answer/16984139
- Google: Search documentation changelog (FAQ rich result deprecated May 2026; `llms.txt` clarification June 2026): https://developers.google.com/search/updates
- OpenAI: Crawlers & user agents (OAI-SearchBot / GPTBot / ChatGPT-User / OAI-AdsBot): https://developers.openai.com/api/docs/bots
- Bing Webmaster Tools: AI Performance: https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c
- Google: Helpful, reliable people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

**Important:** This is a build/audit checklist, not evidence that your specific website has been checked. To audit a site, Claude must inspect the real repository, route output and—after deployment—live URLs and authorized search properties.
