# sushantrana.com — plain HTML/CSS/JS version

No Node.js, no React, no build step. Every page is a normal `.html` file.

## Folder map

| Path | What it is |
| --- | --- |
| `index.html`, `about/index.html`, `blog/…/index.html` … | One folder per URL, so `/about/` works on any host |
| `includes/header.html`, `includes/footer.html` | The one shared nav and footer; `dev/sync-layout.py` stamps them into every page |
| `dev/page-gen/` | Generator for the service and industry pages (dev only) |
| `assets/css/style.css` | All styling (Tailwind output, readable) plus the animation rules at the bottom |
| `assets/js/site.js` | All interactivity: menus, popups, forms, tabs, counters, scroll animations |
| `assets/vendor/` | Lenis (smooth scroll) and libphonenumber (phone validation) |
| `assets/fonts/` | Self-hosted Google Fonts |
| `img/<width>/…webp` | Pre-resized images used by the `srcset`s |
| `api/lead.php` | Receives every lead form: saves to Supabase, emails via Resend |
| `api/heartbeat.php` | Keeps the Supabase Free project awake |
| `.htaccess` | www → apex, http → https, old thank-you URLs, 404 page, caching |

## Deploy on Hostinger (shared hosting or any PHP host)

1. hPanel → Advanced → Git: deploy this repo's `main` branch to `public_html/`
   (or upload everything in this folder, including the hidden `.htaccess` files).
2. Copy `api/config.sample.php` to `api/config.php` and fill in the Supabase and Resend keys.
3. hPanel → Advanced → Cron Jobs, every 6 hours:
   `curl -s https://sushantrana.com/api/heartbeat.php > /dev/null`
   and daily at 02:30 IST (visit totals and 90-day clean-up for the leads panel):
   `php ~/domains/sushantrana.com/public_html/api/cron-daily.php`
4. Open the site, submit the consultation form once, confirm the email arrives.

## Editing

- Text: open the page's `index.html` and edit.
- Nav or footer: edit `includes/header.html` or `includes/footer.html`, then run `python3 -I dev/sync-layout.py`. Keep the header markup neutral: the script highlights each page's own link.
- A new blog post: copy an existing `blog/<slug>/index.html`, change the content, then add it to `blog/index.html`, the home page's "Latest insights", `sitemap.xml` and `llms.txt`.
- After changing page text or `sitemap.xml`: run `python3 -I dev/build-llms-full.py` to rebuild `llms-full.txt` (the text of every sitemap page in one file, for AI crawlers).
- Styling: Tailwind classes in the HTML resolve against `assets/css/style.css`. A class that is not already used somewhere on the site does not exist in that file; write plain CSS for it at the bottom instead.
