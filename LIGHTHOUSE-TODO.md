# Lighthouse to-do — sushantrana.com

Tested 2026-10-13 on PageSpeed Insights (Lighthouse 13.5.0), home page, after
the switch to plain HTML/PHP. This file is hidden from visitors (.htaccess
blocks every .md).

| | Performance | Accessibility | Best Practices | SEO |
|---|---|---|---|---|
| Mobile | 94 | 95 | 100 | 100 |
| Desktop | 95 | 95 | 100 | 100 |

| Metric | Mobile | Desktop |
|---|---|---|
| First Contentful Paint | 1.2 s | 0.3 s |
| Largest Contentful Paint | 2.7 s | 1.3 s |
| Total Blocking Time | 30 ms | 50 ms |
| Cumulative Layout Shift | 0.001 | 0.004 |
| Speed Index | 4.1 s | 1.6 s |

Re-test after each fix: https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fsushantrana.com%2F
(flush the Hostinger CDN cache first, or the old copy gets tested).

## Fix first (biggest effect)

1. **Hero image starts loading late (mobile LCP 2.7 s).** LCP breakdown: 980 ms
   "resource load delay" before `/img/…/hero/hero.webp` even starts. Add to the
   `<head>` of `index.html`:
   `<link rel="preload" as="image" href="/img/750/hero/hero.webp" imagesrcset="(same srcset as the hero img)" imagesizes="98vw" fetchpriority="high">`
2. **Oversized images on desktop (save ~132 KiB).** The `sizes` attributes are
   wider than the images really render:
   - hero: `sizes="98vw"` → renders 1308 px wide inside the container; use
     `sizes="(max-width: 1340px) 98vw, 1308px"`.
   - about image and `reports/r2`: `sizes="(max-width: 768px) 100vw, 1100px"` →
     renders ~670 px and ~835 px; set the real widths.
3. **Render-blocking CSS (mobile, est. 420 ms).** `assets/css/style.css` (16 KiB)
   blocks first paint. Inline the above-the-fold CSS in `<head>` and load the
   rest with `media="print" onload="this.media='all'"`, or at least minify it.
4. **Google Tag Manager is the heaviest thing on the page (295 KiB, 137 KiB
   unused, 2 of the 3 long tasks).** In GTM, remove tags you no longer use, and
   check whether GA4 is loaded twice (GTM container + a separate gtag
   `G-WYC4TDCW0D`). Optionally delay GTM until first scroll/click.

## Smaller wins

5. **Low colour contrast (accessibility 95 → 100).** Failing:
   - "Book an Appointment" button (`.btn-primary`: white on orange).
   - Orange marquee strips ("Performance Marketing ✦ Web Development ✦ …") and
     the "Revenue Systems" big text in the logo band.
   - "The revenue system" tab button and the "A CONNECTED REVENUE SYSTEM" label.
   - "Strategy ✦ Positioning ✦ …" marquee.
   Darken the orange for text/buttons (aim for 4.5:1 against white), or make
   the text darker/bolder.
6. **Cache lifetime.** `style.css`, `site.js`, `lenis.min.js` are cached 7 days.
   Add a version query (`style.css?v=2`) when they change, then raise them to
   1 year in `.htaccess`.
7. **Minify `assets/js/site.js`** (save 4.5 KiB). Keep the readable copy for
   editing; upload a minified one.
8. **Layout shift from the web font** on the hero line "Why aren't you getting
   enough leads?" (CLS 0.001–0.004, already fine). Optional: `size-adjust` on the
   fallback font.
9. **Forced reflow (48 ms)** in `site.js`: a layout read after a DOM write
   during startup. Batch reads before writes.

## Security headers (Best Practices "Trust and safety", unscored)

10. Add to `.htaccess` (test that GTM and fonts still load):
    - `Strict-Transport-Security: max-age=31536000; includeSubDomains`
    - `X-Frame-Options: SAMEORIGIN` (or CSP `frame-ancestors 'self'`)
    - `Cross-Origin-Opener-Policy: same-origin`
    - A Content-Security-Policy that allows googletagmanager.com,
      google-analytics.com and open.er-api.com (currency rates).

## Not done yet

- Only the home page was tested. Run the same on
  `/services/shopify-store-development/`, `/services/website-maintenance/`,
  `/blog/` and one blog post.
