# Where to drop your images

Everything in this `public/` folder is served from the site root.
Example: `public/hero/hero.jpg`  →  used in code as `/hero/hero.jpg`.

Drop files with the **exact names below** and I'll wire them in (or rename freely and
tell me). SVG or PNG preferred for logos; JPG/WebP for photos.

---

## hero/
- `hero.jpg`  — main hero image, **1008 × 567**

## about/
- `about.jpg`  — your portrait / working shot (About Me section)

## logos/  (tools — transparent SVG/PNG, square-ish)
google-ads · meta-ads · tiktok-ads · gohighlevel · zoho · shopify · wordpress ·
linkedin-ads · snapchat-ads · amazon-ads · ga4 · gtm · clarity · hubspot ·
zoho-crm · klaviyo · make-zapier · webflow · wix · chatgpt · claude · gemini
(e.g. `logos/google-ads.svg`)

## services/  (What I Do — 2 images per service, portrait 3:4)
- `brand-1`, `brand-2`
- `performance-1`, `performance-2`
- `ai-1`, `ai-2`
- `web-1`, `web-2`

## who-i-help/  (optional — one per industry, 4:3)
healthcare · education · manufacturing · saas · construction · fashion ·
professional · realestate

## testimonials/  (client company logos + optional avatars)
- `logo-1` … `logo-5`  (company logos)
- `avatar-1` … (optional client photos)

## blog/  (post cover images, 16:10)
- `post-1`, `post-2`, `post-3`

## case-studies/  (optional cover images)
- `case-1` …

---

After you add files, tell me "assets added" (or which folders) and I'll swap the
placeholders for real `<Image>` tags.

## clients/  (website screenshots shown on /about — landscape 16:10, WebP/PNG)
`yalla-renovation-website.webp` · `4s-study-abroad-website.webp` ·
`achievers-perfect-career-institute-website.webp` · `ourknots-website.webp` ·
`warriors-cove-website.webp` · `bazayan-website.webp` · `touch-abroad-website.webp` ·
`trust-legal-website.webp` · `elixir-engineering-website.webp`
(e.g. `clients/bazayan-website.webp` — the filename must be the slug in
`lib/clients.ts` plus `-website.webp`. Missing files fall back to the placeholder
box, so drop them in any time.)

## about/  (photo grid on /about — landscape 4:3)
- `work-1` … `work-6` — client calls, campaign reviews, build sprints, events.
  Captions and alt text live in `components/About.tsx` (`GALLERY`); update them
  if a slot gets a different photo.

## services/shopify/  (Shopify service page — all WebP)
Phone frames (full-length mobile screenshots, 560px wide, any height — they
scroll inside the frame). A missing file falls back to a built-in wireframe.
- `home-1.webp` · `home-2.webp` — the "Whole storefronts" band
- `product-page-1.webp` · `product-page-2.webp` — the "Product pages" band
- `product-page-3.webp` — spare, not currently placed

Portfolio strip (portrait cards, 720px wide):
- `work-1.webp` … `work-6.webp`

Product-card photos (square, 600x600):
- `card-oraah.webp` — Oraah Sugar Balance Tea pouch
- `card-ben-bag.webp` — Ben Classic Handbag
Missing files fall back to a tinted block, so the card still works.

Labels and alt text live in `components/ShopifyDevelopment.tsx`.

**Adding more:** drop the full-size PNG in `_originals/shopify/` (gitignored),
then resize and convert before it goes in `public/` — the raw exports were
10-55MB each and would have shipped ~200MB to every visitor:
```
sips --resampleWidth 560 in.png --out /tmp/r.png && cwebp -q 78 /tmp/r.png -o out.webp
```
Phone screenshots: 560px wide. Portfolio cards: 720px wide. WebP cannot exceed
16383px in either direction, which is why the tall ones are resized first.

## clients/  (website screenshots, not logos)
`<slug>-website.webp` — a screenshot of the client's own site, used on /about.
The wordmark strip on the Shopify page has no logo files, so it renders each
client's name as type instead. Drop `<slug>-logo.png` (transparent, ~200x60) if
real logos ever become available and the strip picks them up automatically.

## services/maintenance/  (Website maintenance page — WebP, 1400px wide, 4:3 crop)
- `hero.webp` · `site-down.webp` · `updates.webp` · `security.webp`
Licensed Magnific/Freepik stock photos; full-size originals in `_originals/maintenance/`.
Alt text lives in `components/WebsiteMaintenance.tsx`.

## logos/platforms/  (platform logos on the maintenance page — SVG)
simple-icons (CC0) SVGs recoloured to each brand's hex. **Missing: `magento.svg`**
— drop it in, then set `logos: ["magento"]` for Magento in `lib/maintenance.ts`.
