# Progress: SEO + web pages (link building, GBP, SEO audit, WordPress, landing pages)

- [done] pages/link_building.py -> /services/link-building/ (classcheck clean; title 49, desc 146, 1 h1, 2 forms, ld WebPage/Service/FAQPage/BreadcrumbList, no Shopify)
- [done] pages/google_business_profile.py -> /services/google-business-profile/ (classcheck clean; title 57, desc 140, 1 h1, 2 forms, ld ok, no Shopify)
- [done] pages/seo_audit.py -> /services/seo-audit/ (classcheck clean; title 44, desc 135, 1 h1, 2 forms, ld ok, no Shopify, tags balanced)
- [done] pages/wordpress_development.py -> /services/wordpress-development/ (classcheck clean; title 53, desc 136, 1 h1, 2 forms, ld ok, no Shopify, tags balanced)
- [done] pages/landing_pages.py -> /services/landing-pages/ (classcheck clean; title 56, desc 137, 1 h1, 2 forms, ld ok, tags balanced; 'Shopify' appears 4x in main: FAQ q+a from doc and the related chip, allowed since the doc FAQ mentions Shopify)

## Notes
- Build: `python3 -I dev/page-gen/lib.py . dev/page-gen/pages/<x>.py`; classcheck: `python3 -I dev/page-gen/classcheck.py assets/css/style.css <path>/index.html`. SEO check script (scratchpad, not in repo) prints title/desc length, h1 count, form count, ld types, Shopify count in main.
- Class gotchas (not in style.css): w-4/5, border-4, border-dashed, border-ink/80, bg-ink/20, rounded-[20px], arbitrary sm:grid-cols-[..]. Use border-2 border-ink/25, bg-ink/15, rounded-2xl/[28px], flex layouts. Also `w-4/5` does not exist in style.css; use w-1/2, w-2/3, w-3/4, w-5/6, w-full.
- link_building: previous run's spec was complete; only change was meta desc switched to the doc's own (146 chars). Who-I-help chips have no doc section; body text written from the doc's intro.
- GBP: extra lucide icons (pin, star, message) added via L.ICON.update in the spec. Elixir project NOT used (its published story is SEO + Google Ads, not GBP, so it would not read naturally). "What you get" has 7 cards (doc lists 7 items) in lg:grid-cols-4. Meta desc trimmed from doc (doc's was >155). Leak check tied to section 06 "active vs forgotten".
- seo_audit: CTA "Get your free website SEO audit", submit "Request my free audit". Report mock uses word ratings only (Good / Needs work / Missing, Ahead / Behind), tagged Example. projects_section(["elixir","achievers"]). "What you get" cards derived from sections 04/05/06 (doc has no separate list). Meta desc trimmed (dropped "Request your free audit now.").
- wordpress: monitor/mobile lucide icons added locally. Projects bazayan/trust/achievers/touch with h2 'Websites we have built and run'; nothing says they are WordPress. Shopify Development link from doc's internal-link notes NOT added (brief: no Shopify text in main unless doc body mentions it). Who chips: Consultants/Local shops/Startups have no industry page, so unlinked. Meta desc = doc's minus 'Get your free WordPress quote.' Missing classes to avoid: col-span-2, p-2.5.
- landing_pages: star icon added locally. Leak check sits in the text column of the 04 'secret' split (split 'after'); anatomy tabs (Headline/Offer/Proof/Form/CTA) are the visual. Basics: ad-promise mirror + homepage vs landing page toggle. 'What you get' cards built from doc section 06 list. Meta desc rewritten from doc's (was >155) to lead with the focus keyword.
- Existing services/seo-audit, wordpress-development, landing-pages pages are overwritten by the generator (assigned paths).

## Next step
All five pages done and verified. Nothing left except the coordinator's review. Not done by design: no dev server/visual check, no commit, sitemap/llms.txt not touched (google-business-profile is a new URL and needs a sitemap entry by whoever owns sitemap.xml).
