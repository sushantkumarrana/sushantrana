# Brief for building service pages (shared by every page agent)

Repo: /Users/sushantrana/Sushant/sushantrana-next (plain HTML/CSS/JS + PHP, no build step for the live site).
Content docs (plain text, one per page): /private/tmp/claude-501/-Users-sushantrana-Sushant-sushantrana-next/3740c5f7-4a09-42a6-b6a6-6f0bbed531da/scratchpad/docs/<NN>_<Name>.txt
Ignore the "How To Implement This Page" and "Pillar And Blog Plan" parts of each doc except for internal link ideas.

## What you produce
For each page: ONE spec file `dev/page-gen/pages/<snake_name>.py`, then run
    python3 -I dev/page-gen/lib.py . dev/page-gen/pages/<snake_name>.py
which writes `<path>/index.html` and `thank-you-<slug>/index.html`.

## Hard rules
1. Files you may create/modify: only your own spec files, and the two HTML outputs the generator writes for your pages. Do NOT edit dev/page-gen/lib.py, assets/css/style.css, assets/js/site.js, sitemap.xml, llms.txt, api/*, the nav in any page, or any other page. NEVER touch services/shopify-store-development/ or services/website-maintenance/. No git commit, no push.
2. No invented claims. Do not write any number, statistic, result, client name, testimonial, price, timeline, guarantee, certification or partner badge that is not in the page's doc text or in `L.PROJECTS` (published facts). Example mocks/illustrations must carry the tag "Example" and use generic placeholders ("Your business", "yourbusiness.com", "Product one") with no realistic performance figures.
3. Voice: "I + my team". Hero intro starts like: 'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I ...'. Elsewhere first person (I/we) as in the doc. "You work directly with me" stays.
4. Use ALL doc content: H1 (split into ("lead", "orange tail")), both intro paragraphs, every numbered section (01-09) with every H3 item, every process step, the mid-page CTA band text, the closing CTA, and EVERY FAQ (keep wording, light edits only). Meta title from doc (<=60 chars), meta description <=155 chars (trim doc's if longer, keep focus keyword).
5. Only CSS classes that already exist in assets/css/style.css. After building run
       python3 -I dev/page-gen/classcheck.py assets/css/style.css <path>/index.html
   and swap any listed class for an existing one (ignore `marker:content-[&#x27;&#x27;]`). Do not add CSS.
6. Python is < 3.12: no backslashes inside f-string {expressions}; precompute such strings in variables.
7. Form submit label must not start with "Book" or "Get your free" (site.js turns those into popup openers; the generator asserts this). CTA buttons elsewhere SHOULD use the doc's CTA text (e.g. "Book your free Meta Ads strategy call").
8. Icons: only keys in `L.ICON` (chev, check, plus, minus, target, search, users, gauge, wallet, click, chart, pen, layers, phone, sliders, file, play, repeat, bag, image, zap, shield). If you need another lucide icon, define the svg markup locally in your spec.

## Reference
- Approved example: dev/page-gen/pages/google_ads.py (read it fully first). Match its quality and section rhythm.
- Generator API (dev/page-gen/lib.py, available as `L` in your spec): hero (via PAGE), marquee, split(s, dark, flip), icon_cards, dark_cards, process (steps need "short" label <=10 chars), cta_band, chips_section, faq, contact, section_bg, figure, svg, pill, E, plus shared widgets:
  - `L.tabs_showcase({...})` tabs with a mock per item (pass "mock" HTML for each item; hand-build mocks like google_ads MOCKS wherever feasible, default_mock is the fallback),
  - `L.leak_check(title, intro, [(statement, why)...], (msg_none, msg_some, msg_most), cta, unit)` self-check,
  - `L.crm_section(platform, cta, h2=None, body=None, bullets=None)` the "ads only work properly when your CRM is connected" section with its toggle demo,
  - `L.projects_section(keys, (h2a, h2b), body)` client work tabs with real screenshots; keys from L.PROJECTS only.
  - `data-mirror="x"` input + `data-mirror-out="x"` spans give a live-typing demo (see the SERP demo in google_ads.py).
- PAGE dict keys: copy every key used in google_ads.py (path, slug, form_name, service, service_name, thanks_what, category, service_desc, audience, countries, offer_name, offers, title, og_title, og_alt, desc, cta, trail, related, faq, hero{pill,h1,intro_html,cta2,stats}, form{title,sub,submit,steps}), then PAGE["sections"].

## Every page must have (interactive like the Shopify page)
- Hero with the 3-step form (Contact is automatic; add 2 steps of service-specific questions, at least one radio/checkbox chip question, required ones marked "req": True).
- Hero stats, ONLY these published figures:
  ads/marketing pages: [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")]
  all other pages:     [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")]
- A keyword marquee, at least one dark split with a custom interactive/illustrative visual, a tabs_showcase for the doc's main "what I do / types" section with hand-built mocks, a leak_check self-check tied to the doc's problem/secret/difference section, the scroll process, the "what you get" icon cards with the mid CTA band, why-me dark cards, who-I-help chips (link to existing industry pages), related service chips, FAQ, contact.
- Optional per brief below: crm_section, projects_section.

## Existing URLs you may link to
Services: /services/google-ads/ /services/meta-ads/ /services/linkedin-ads/ /services/youtube-ads/ /services/amazon-ads/ /services/google-shopping-ads/ /services/performance-marketing/ /services/remarketing/ /services/lead-generation/ /services/local-seo/ /services/technical-seo/ /services/on-page-seo/ /services/ecommerce-seo/ /services/enterprise-seo/ /services/link-building/ /services/google-business-profile/ /services/seo-audit/ /services/content-seo/ /services/wordpress-development/ /services/shopify-store-development/ /services/landing-pages/ /services/website-maintenance/ /services/website-redesign/ /services/ecommerce-website/ /services/zoho-crm/ /services/hubspot-crm/ /services/gohighlevel/ /services/crm-consulting/ /services/sales-funnel-setup/ /services/email-automation/ /services/whatsapp-automation/ /services/reporting-dashboard/
Industries: /industries/ecommerce/ /industries/local-businesses/ /industries/healthcare/ /industries/dental/ /industries/auto-repair/ /industries/real-estate/ /industries/education/ /industries/legal-firms/ /industries/b2b-companies/ /industries/saas/ /industries/finance/ /industries/travel/ /industries/manufacturing/ /industries/automobile/

## Check before reporting
- generator runs clean, classcheck clean,
- title <=60, description <=155, exactly one <h1>, ld+json has WebPage, Service, FAQPage and a BreadcrumbList,
- both forms present: `grep -c 'data-step-form="generic"'` gives the hero form and the modal form,
- no "Shopify" text inside <main> unless the doc mentions it.

## Report back (short)
Per page: path, thank-you URL, dataLayer event (lead_<form_name>), sections included, which doc content (if any) you left out and why, and any claim you were unsure about.

## Progress log (memory across restarts)
Keep `dev/page-gen/briefs/progress-<group>.md` (ads, seo, seo-web, industries, crm). If it exists when you start, read it FIRST and continue from its "Next step". Update it after every page: one line per page `[done|doing|todo] <spec file> -> <path>` (with classcheck / SEO check status), a short "Notes" list (decisions, omitted doc content, unsure claims), and "Next step". A fresh agent with no memory must be able to continue from it.
