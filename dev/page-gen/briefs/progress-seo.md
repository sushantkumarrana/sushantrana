# Progress: SEO service pages (agent for docs 08-12)

- [done] pages/local_seo.py -> /services/local-seo/ (+ /thank-you-local-seo/). Generator clean, classcheck clean, title 52, desc 137, 1 h1, 2 forms, ld+json WebPage/Service/FAQPage/BreadcrumbList, no Shopify in main.
- [done] pages/technical_seo.py -> /services/technical-seo/ (+ /thank-you-technical-seo/). Generator clean, classcheck clean, title 45, desc 149, 1 h1, 2 forms, all 4 ld types, no Shopify in main.
- [done] pages/on_page_seo.py -> /services/on-page-seo/ (+ /thank-you-on-page-seo/). Generator clean, classcheck clean, title 45, desc 144, 1 h1, 2 forms, all 4 ld types, no Shopify in main.
- [done] pages/ecommerce_seo.py -> /services/ecommerce-seo/ (+ /thank-you-ecommerce-seo/). Generator clean, classcheck clean, title 55, desc 142, 1 h1, 2 forms, all 4 ld types. Shopify appears in main, allowed: doc 11 names Shopify.
- [done] pages/enterprise_seo.py -> /services/enterprise-seo/ (+ /thank-you-enterprise-seo/). Generator clean, classcheck clean, title 54, desc 142, 1 h1, 2 forms, all 4 ld types, no Shopify in main.

## Notes
- Brief: dev/page-gen/briefs/AGENT-BRIEF.md. Docs: scratchpad/docs/<NN>_*.txt (see brief for path).
- Build: `python3 -I dev/page-gen/lib.py . dev/page-gen/pages/<x>.py`; classcheck: `python3 -I dev/page-gen/classcheck.py assets/css/style.css <path>/index.html` (ignore marker:content-[&#x27;&#x27;]).
- SEO check script (scratchpad, not in repo): scratchpad/ck/verify.py <html files> prints title/desc length, h1 count, form count, ld types, Shopify count in main.
- local_seo.py was left from the interrupted run; reviewed against doc 08, all content present, rebuilt, passes. Doc's opening question "Do you want more customers..." folded away (hero must start "I am Sushant Rana..."); same idea is kept in intro.
- Each spec is self-contained: helpers (rows, note, code, toggle) copied per file; extra lucide icons added via L.ICON.update in the spec.
- Pages without projects use cta2 ("See what I ...", "#types").
- Meta descriptions trimmed to <=155 and start with the focus keyword.
- Leak check placement: technical = section 06 speed; on-page = 06 intent; ecommerce = 04 challenge; enterprise = section 04 advantage (light split); basics 01 is the dark split with the 'Fix one page' / 'Fix the template' toggle demo.
- Mid CTA band placed under "What you get" cards (as in google_ads.py), not after section 06.
- On-page: doc writes "on page"; spec uses "on-page" (hyphenated) everywhere incl. title "On-Page SEO Services That Rank | Sushant Rana".
- Technical/on-page: hero intro folds the doc's opening question into the end of paragraph 1 (after the required "I am Sushant Rana..." start).
- Mocks: all tagged "Example", placeholders only (yourbusiness.com, Product one), no figures.

## Next step
All five pages done and verified. Only remaining step: report back to the coordinator per the brief. No commit, no dev server.
