> v2.1 — all 9 reviewed fixes + polish applied (carousel timer guard, popup reopen race, tab/carousel/form ARIA, section--tight, mobile CRM, truthful hero stat). Verified: 0 console errors, 0 broken links, contrast AA.

# NOTES — Sushant Rana Personal Brand Website (v2 redesign)

Static site: HTML5 + CSS3 + vanilla JS. No frameworks, no runtime CDN
dependencies, no build step required to view — open any `.html` file directly
or serve the folder with any static server.

This is the **v2 redesign**: House of Web colour concept, SEO-Discovery-inspired
information architecture, rounded/friendly Agero styling, an interactive
rotating-question hero, and interactivity in every section.

---

## 1. Design system (what changed from v1)

| Area | v2 value |
|---|---|
| Primary blue | `#1780C5` (House of Web) · 600 `#136AA5` · 700 `#0F5688` · tint `#EAF4FB` |
| Accent | sky `#38BDF8`; decorative gradient `#1780C5 → #38BDF8` |
| **Button gradient** | `#0F5688 → #136AA5` — kept darker so white text stays ≥5.78:1 (AA) |
| Headings | **Poppins** (600/700/800) |
| Body | **Montserrat** (400–700) |
| Surfaces | rounded (cards 28px, pills 100px, buttons 14px), brand-tinted shadows |
| Footer | dark (`--ink`) with light deco-grid |
| CTAs | short, **single line** (`white-space:nowrap`), e.g. "Book Free Consultation" |
| Icons | 49 **premium duotone SVGs** (gradient fill + currentColor stroke) in `build/icons.js` |

All colour lives on `:root` in `assets/css/style.css`. Intentional raw hex in
component rules: the red "before" state (`#B4341C`, `#FDECEC`) and the AA button
gradient stops (`#0F5688`/`#136AA5`).

## 2. Interactive hero (the centerpiece)

The headline rotates the five questions on a 3.2s loop with a fade+slide+blur
animation, above a fixed answer line:

> Why aren't you getting enough leads? → Why is your ROAS dropping? → Why aren't
> your visitors converting? → Why isn't your business scaling? → Why is your
> marketing not delivering predictable revenue?
> **Because you have marketing campaigns — not a revenue system.**

Zero layout shift (reserved rotator height), `aria-live="polite"`, pauses when
the tab is hidden, disabled under `prefers-reduced-motion` (hard text swap).
Logic in `main.js → initHeroRotator`.

## 3. Every section is interactive

| Section | Interaction |
|---|---|
| Hero | rotating questions + floating glass stat cards (drift) |
| Stats bar | count-up on scroll |
| The Reality | segmented **toggle** — scattered ↔ revenue-system (crossfade) |
| Who I Help | 8-industry **tab switcher** (keyboard: arrow keys) |
| Services | hover **tilt** cards + glow (pointer-fine only) |
| How I Work | animated **timeline** (alternating reveal-l/r) |
| Performance | logo **marquee** (pause on hover) + animated **rank-bars** |
| AI Automation | **live CRM board** — lead animates New→Scored→Qualified on a loop |
| Case Studies | **filter chips** (All/Performance/Automation/Web) |
| Why hire me / Values / Global | staggered scroll reveals + hover-glow |
| What makes me different | **comparison table** (us vs junior vs agency) |
| Testimonials | auto-advancing **carousel** with dots (pauses on hover/focus) |
| Tech stack | second **marquee** |
| FAQ | **categorized accordion** (chips filter; single-open) |
| Final CTA | animated aurora band |

Every animation is `transform`/`opacity`/`filter` only and collapses to its
end-state under `prefers-reduced-motion`. Cursor/tilt effects are disabled on
touch (`pointer: coarse`) and when reduced-motion is set.

## 4. Build system

Compiled HTML is committed — you never need Node to *view* the site.

```bash
node build/build.js     # regenerate all 25 pages + images + robots + sitemap
node build/serve.js     # optional local dev server (http://localhost:8901)
```

`build/` modules: `partials.js` (head/header/footer/ambient/wrapper),
`icons.js` (49 duotone icons), `data.js` (all content), `home.js` (homepage
sections), `pages.js` (every other page), `services.js` (service-page data),
`build.js` (orchestrator). The four `asset-*.md` files are the design-asset
sources the redesign was generated from (safe to delete).

## 5. Libraries used

**None.** Pure vanilla CSS + JS.
- JS shipped: **~8 KB gzipped** · CSS: **~11 KB gzipped** (budget was 150 KB JS)
- Only external request: Google Fonts (preconnect + `display=swap`)

## 6. Wiring the form endpoint

`assets/js/main.js` top:

```js
var FORM_ENDPOINT = "https://example.com/api/consultation"; // REPLACE
```

Popup + consultation-page form POST JSON `{ fullName, email, phone, company,
website, service, challenge, source }` then redirect to `thank-you.html` (2.5 s
safety timeout guarantees the redirect). `source` records which page/CTA opened
the popup. Point it at Formspree / Basin / a Make webhook / your own API.

## 7. Analytics (GTM-ready, no container hardcoded)

`window.dataLayer` events: `popup_open`, `form_submit`, `form_error`. Paste your
GTM snippet into `head()` in `build/partials.js` and rebuild — nothing else needed.

## 8. Every REPLACE marker (`grep -rn "REPLACE" *.html assets/js build`)

- `FORM_ENDPOINT` (main.js) and `SITE.base` domain (partials.js).
- OG image `assets/img/og-cover.svg` → real 1200×630 PNG/JPG.
- Footer social links are `#` placeholders → real profile URLs.
- Hero stat cards + stats bar + all case-study metrics: verify before launch.
- Testimonials: placeholder quotes/names pending client permission.
- "Slots open this week" urgency copy — keep genuinely accurate.
- Live CRM widget is explicitly labelled "system demo — not live client data".
- Legal pages: date, analytics stack, form provider, jurisdiction, contact email.
- Public email currently `me@sushantrana.com` — confirm.
- Blog: 9 cards → one full article template (`blog-post.html`); write the other 8.

## 9. Truthfulness stance

SEO Discovery's section *structure* was adopted, but none of its big-agency
claims (22 years, 400 experts, Forbes awards) — Sushant is a solo 8-year
consultant. No fabricated awards, no invented clients. Every unverified number
carries a REPLACE marker.

## 10. Verified in QA

- 25 pages build; unknown URLs return the styled 404.
- Zero console errors; all internal links + anchors resolve; one `<h1>`/page;
  unique title + description + canonical + OG/JSON-LD (Person, ProfessionalService,
  FAQPage, BreadcrumbList, BlogPosting) per page.
- **No horizontal scroll at 390 / 768 / 1440** (`scrollWidth === clientWidth` on
  every page; `overflow-x: clip` on root).
- All interactive components verified functionally: rotating hero, industry tabs,
  compare toggle, tilt cards, timeline, marquees, live CRM loop, case/blog/FAQ
  filters, categorized accordion, testimonial carousel, counters.
- Popup opens from every CTA, traps focus, closes 4 ways (ESC/backdrop/X/Maybe
  Later), validates 5 rules inline, returns focus, redirects to thank-you.
- Contrast retuned to WCAG AA: body 13.6:1, secondary 6.3:1 (5.7:1 on tinted
  sections), links/headings 7.8:1, white on buttons ≥5.78:1.
- `prefers-reduced-motion` collapses every animation; touch disables tilt.

Environment note: the in-app Browser pane intermittently stopped painting
(tab reported `hidden`), which blanks *screenshots* — verification was done via
DOM/measurement assertions plus the hero renders that did capture. It is not a
site defect; real browsers paint normally.
