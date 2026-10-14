# Progress: industry pages (20-24)

Build: `python3 -I dev/page-gen/lib.py . dev/page-gen/pages/<spec>.py`, then
`python3 -I dev/page-gen/classcheck.py assets/css/style.css <path>/index.html`.

- [done] dental_marketing.py -> /industries/dental/ (reviewed, rebuilt; classcheck clean; SEO checks passed)
- [done] auto_repair_marketing.py -> /industries/auto-repair/ (reviewed, rebuilt; classcheck clean; SEO checks passed)
- [done] real_estate_marketing.py -> /industries/real-estate/ (built; classcheck clean; SEO checks passed)
- [done] education_marketing.py -> /industries/education/ (built; classcheck clean after swapping bg-ink/25 and w-1/3; SEO checks passed)
- [done] law_firm_marketing.py -> /industries/legal-firms/ (built; classcheck clean; SEO checks passed)

## Notes
- Shared mock helpers (map_area, place_rows, search_ad, social_ad, landing, reviews, tracking, steps, pick_demo) are copied into each spec; a copy lives in the scratchpad helpers.py. Specs use `HID = L.HID`.
- industries/real-estate, education, legal-firms already existed as generic "Industries | Sushant Rana" placeholder copies (tracked in git); the generator overwrites them as the task intends.
- Mid-page CTA band text from each doc is placed in the "What you get" section (brief pattern), not after section 04 where the doc puts it.
- Titles trimmed to <=60: education uses "Education Marketing Services for Admissions | Sushant Rana" (doc's is 63 chars). Descriptions trimmed to <=155 keeping the focus keyword.
- crm_section on every page, adapted per industry (front desk marks booked appointments / service desk marks booked jobs / team marks serious leads and site visits / counsellors mark admissions / intake team marks signed clients).
- Education season planner uses illustrative bar widths only (tagged Example, no numbers). Panel 3 line "Demand settles, so spend settles too" paraphrases the doc's "then settles".
- Law: projects_section(["trust"]) only; describe Trust Legal as website rebuild + maintenance, never ads/marketing results.

## Next step
All 5 pages built and verified (title<=60, desc<=155, one h1, WebPage/Service/FAQPage/BreadcrumbList, 2 step forms, no Shopify in main, no duplicate ids). Nothing left except reporting back; no commit.
