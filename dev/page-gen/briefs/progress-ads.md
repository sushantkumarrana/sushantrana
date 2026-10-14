# Progress: ads pages (agent for docs 01, 03-07)

Brief: dev/page-gen/briefs/AGENT-BRIEF.md. Reference spec: dev/page-gen/pages/google_ads.py.
Docs: /private/tmp/claude-501/-Users-sushantrana-Sushant-sushantrana-next/3740c5f7-4a09-42a6-b6a6-6f0bbed531da/scratchpad/docs/<NN>_*.txt
Build: `python3 -I dev/page-gen/lib.py . dev/page-gen/pages/<name>.py` then
`python3 -I dev/page-gen/classcheck.py assets/css/style.css <path>/index.html` (from repo root).

## Pages
- [done] pages/performance_marketing.py -> /services/performance-marketing/ (classcheck clean, SEO checks pass: title 54, desc 152)
- [done] pages/meta_ads.py -> /services/meta-ads/ (classcheck clean, SEO checks pass: title 54, desc 151)
- [done] pages/linkedin_ads.py -> /services/linkedin-ads/ (classcheck clean, SEO checks pass: title 50, desc 153)
- [done] pages/youtube_ads.py -> /services/youtube-ads/ (classcheck clean, SEO checks pass: title 52, desc 154)
- [done] pages/amazon_ads.py -> /services/amazon-ads/ (classcheck clean, SEO checks pass: title 45, desc 145)
- [done] pages/google_shopping_ads.py -> /services/google-shopping-ads/ (classcheck clean, SEO checks pass: title 43, desc 151; 'Shopify' in main is from the doc)

## Notes
- No spec files existed from the interrupted run; starting fresh.
- Phone-frame mock markup copied from services/shopify-store-development (classes exist in style.css).
- Perf marketing: crm_section("Google and Meta") output is string-replaced to fix grammar ("learns" -> "learn", "sees" -> "see").
- Intro "markets" wording: perf marketing + Meta say "India, the UAE, the US and Canada" (UAE backed by Yalla/4S projects); other pages keep the doc's "India, the US and Canada".
- Google Shopping: no crm_section (store sales, not CRM leads; does not read naturally).

- Meta: placements + ad types are two tabs_showcase sections; phone() helper in meta_ads.py. Who-chip 'Coaches and course creators' links /industries/education/.
- LinkedIn: leak_check used as a 'Is LinkedIn right for you?' fit check (doc section 07 is honest advice, not a leak). Targeting = dark split with tab-based audience builder.
- Amazon: no crm/projects (per orchestrator). Leak check sits in the ACoS/TACoS section (doc 07) with formula cards.
- Perf marketing CTA shortened to 'Book your free strategy call' (doc's full text overflowed the hero at 375px because .btn is nowrap); form title keeps the full doc wording. LinkedIn form step labels shortened to Ads/Buyers for the same reason.
- All 6 pages checked on the already-running localhost:8090 server: no horizontal overflow at 360px and 375px. (google_ads itself overflows at 360px, not ours.)

## Next step
All 6 pages done and verified. Only the report to the coordinator remains.
