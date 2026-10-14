# Service page generator (dev only)

Builds a service page plus its thank-you page from a spec, reusing the
head and scripts of `services/shopify-store-development/index.html`; the header and footer come from
`includes/header.html` / `includes/footer.html` via `dev/sync-layout.py`.
The output HTML is committed; nothing here runs on the live site.

    python3 -I dev/page-gen/lib.py . dev/page-gen/pages/google_ads.py
    python3 -I dev/page-gen/classcheck.py assets/css/style.css services/google-ads/index.html

`classcheck.py` lists classes the page uses that `style.css` does not define
(ignore `marker:content-[...]`, it is an escaping false positive).
