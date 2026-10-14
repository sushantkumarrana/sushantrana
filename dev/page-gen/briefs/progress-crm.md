# Progress: CRM / automation pages (25-29)

- [done] pages/zoho_crm.py -> /services/zoho-crm/ (classcheck clean; title 55, desc 148, 1 h1, ld WebPage/Service/FAQPage/BreadcrumbList, 2 forms, no Shopify in main)
- [done] pages/hubspot_crm.py -> /services/hubspot-crm/ (classcheck clean; title 58, desc 147, 1 h1, ld ok, 2 forms, no Shopify)
- [done] pages/gohighlevel.py -> /services/gohighlevel/ (classcheck clean after swapping border-dashed/ml-auto/max-w/rounded-*-md for existing classes + inline style; title 54, desc 134, 1 h1, ld ok, 2 forms, no Shopify)
- [done] pages/sales_funnel_setup.py -> /services/sales-funnel-setup/ (classcheck clean after h-36/rounded-t-xl swap; title 55, desc 141, 1 h1, ld ok, 2 forms, no Shopify)
- [done] pages/email_automation.py -> /services/email-automation/ (classcheck clean after left-[15px] -> inline style; title 50, desc 152, 1 h1, ld ok, 2 forms, no Shopify)

## Notes
- zoho_crm.py from the interrupted run was reviewed against doc 25: all content present, rebuilt, checks pass. Left as is.
- Each spec is self-contained (helpers seg/note/label/row/rows/flow copied from zoho_crm.py, not imported).
- CRM pages (25-27) use L.crm_section("Google Ads", ...) with body/bullets reworded for that CRM.
- Interactive visuals: Zoho = pipeline board tabs; HubSpot = contact record timeline (click > form > email > call > won); GHL = separate tools vs one system toggle + trigger/action flows with nested tabs (site.js scopes nested data-tabs via closest()).
- Meta descriptions trimmed from doc (doc versions >155), focus keyword kept at start.
- Mock text is example copy tagged "Example"; no figures. GHL calendar mock shows example time slots and a ★★★★★ glyph row (no rating number).
- Sales funnel: leak_check sits in the dark basics split (website leaking buyers); section 04 stages split has the interactive funnel stage picker; no crm_section (not a CRM page).
- Email automation: leak_check in dark basics split; section 04 split has trigger picker (signs up / leaves cart / buys / goes quiet) with email timelines. Form list size ranges are user options, not claims.
- No projects section (no published CRM client).
- Verify helper: scratchpad chk/verify.py (title/desc length, h1 count, ld types, form count, Shopify in main). Recreate if missing.

## Next step
All five pages done and verified. Only the final report to the coordinator remains. No commit (not asked).
