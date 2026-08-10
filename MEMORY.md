# sushantrana.com — Project Memory

Handoff doc. Read this first in a new chat to resume without repeating history.

---

## Project

- **Location:** `~/Desktop/sushantrana-next/`
- **Stack:** Next.js 16 App Router · TypeScript · Tailwind v4 · Framer Motion · Three.js (`@react-three/fiber` + `drei`) · Lenis smooth scroll
- **Old static site** (source for real copy): `~/Desktop/sushantrana-deploy.zip`
- **Run:** `cd ~/Desktop/sushantrana-next && npm run dev` → localhost:3000
- **Build:** `npm run build` — passes.

---

## Design tokens (locked)

- **Hero + hero image bg** = **white `#ffffff`**
- **Every section after** = **grey stone `#dcdcdc`** (transparent sections over one grey `bg-section` region)
- **Accent** = **orange `#FF4D00`** (`--color-orange`) · hover `#E64500` · light `#FF7A3C`
- Text: ink `#0a0a0a` · body `#2a2a2a` · muted `#5a5a5a`
- Line: `rgba(10,10,10,.10)`

### Fonts (all Google Fonts, wired in `app/layout.tsx`)

- Display + body: **Plus Jakarta Sans** (Cal Sans lookalike) → `--font-jakarta`
- Cursive section labels: **Playwrite Tanzania** (`Playwrite_TZ`) → `--font-cookie`, class `.script-label` (18px, orange)
- Devanagari (kept in codebase but not currently used in UI): **Mukta** → `--font-deva`
- Ephesis kept but unused

### Utility classes (`app/globals.css`)

- `.wrap` (1200px) · `.wrap-wide` (1400px) · `.section` (padding-block clamp 44–84px)
- `.btn.btn-primary` (orange), `.btn-dark`, `.btn-outline`
- `.script-label` (cursive orange 18px)
- `.card` (white surface, orange lift on hover)
- `.marquee` + `.marquee__track` (pure CSS, hover-pause, duplicated track loops via `translateX(-50%)`)
- `.glass` / `.glass-dark` (glassmorphism)
- `.grad-ink-orange` · `.grad-orange-ink` (gradients)
- `.glow-orange` (radial blur glow)
- Reduced-motion respected globally.

---

## Homepage structure (top→bottom)

`components/Home.tsx` — one `<main>` with white hero region + wrapped grey region containing `<FloatingLogos />` behind + all grey sections.

1. **Hero** (white) — `<HeroIcons />` (4 small floating: Google Ads, Meta, Wix, GA4 — desktop only) + `<RotatingHeadline />` (4 questions cycling every 4.4s: leads / ROAS (dropping on line 2) / converting / scaling — orange word) + "Because you have marketing campaigns — not a revenue system." + paragraph + **"Book an Appointment"** button
2. **Hero image** (white) — `/hero/hero.png`, 98% width
3. **Tools marquee** (grey) — 12 branded chips (no title): google-ads, meta, tiktok, instagram, zoho, wordpress, linkedin, hubspot, klaviyo, webflow, wix, ga4
4. **Diagonal cross marquees** — 2 ribbons (black + orange) at ±7°, thin `py-2`, 110s/100s, both scroll right→left
5. **About Me** — cursive label + "What I actually do" + full-color orange "Revenue Systems" marquee behind landscape banner `/about/about.png` + full paragraph (Sushant Rana / Business Growth Consultant / 8+ yrs / 4 markets)
6. **Who I Can Help** — image-only bento (5 tiles, no big titles) + "I help brands with results, not reports"
7. **Reality of Growth** — 2-line title, toggle scattered/system, animated card
8. **[STRAIGHT MARQUEE — BLACK]** Performance Marketing / Web Dev / AI Automation / SEO / CRO
9. **Who I Help** — 8 industry pill tabs, single white card swaps (no images inside)
10. **What I Do** — 4 vertical services (left) + 2 images swap on click (right; desktop only, hidden on mobile)
11. **My Numbers** — cursive "My experience" + "journey by the Numbers" · 3 offset cards on orange-glow background: `$10K+` spent · `20+` clients (58% wide) · `6.2×` revenue · orange border, orange glow
12. **[STRAIGHT MARQUEE — ORANGE]** Strategy / Positioning / Automation / Reporting / Growth
13. **How I Work** — 4 timeline steps, orange center line, cards slide alternating L↔R on scroll
14. **Performance Marketing** — cursive "Performance marketing" + platform marquee + 4 tiles (**4×** Best B2B ROAS, ₹50L+, 4 markets, 92%) + split card (copy + checklist + "See full approach") + right card (animated rank bars + growing bar chart)
15. **[STRAIGHT MARQUEE — BLACK]** CRM Automation / Lead Scoring / WhatsApp / Reporting / AI Assistants
16. **AI Automation** — 10 capability chips (left) + live pipeline demo w/ deal hopping New→Scored→Qualified (`layoutId="deal"`) + 3 metric counters + Automation Activity feed
17. **Selected Results** — tabbed (All/Performance/Automation/Web) case cards: industry + 3 metrics + Challenge + Solution + "Read full case study"
18. **[STRAIGHT MARQUEE — ORANGE]** 4× ROAS / ₹50L+ Managed / 4 Markets / Senior-Led / 100% Owned
19. **Testimonials** — full-width marquee of quote cards (industry + quote + divider + name/company + logo slot)
20. **Tech Stack** — 2 marquee rows with real logos
21. **Blog** — 3 posts with real cover images `/blog/post-1.png` … `-3.png`
22. **[STRAIGHT MARQUEE — ORANGE]** Book a Free Call / Revenue Systems / Not Just Campaigns / Let's Build
23. **FAQ** — 12 Q, 2 columns, small +/× icon (h-5)
24. **Final CTA** — "Let's build a system that keeps growing." on footer-bg image + `bg-black/35` overlay
25. **Footer** (`components/Footer.tsx`) — full `/footer/footer-bg.png` image (no overlay), mouse-follow orange glow, white logo (`/logo-white.png`) top + big white logo across the base, 3 link cols (Services, Advertising, Development) + Get-in-touch block (email, markets, Book-a-call, socials)

**Floating overlays (rendered at end of `<Home>`):**
- `<ConsultPopup />` — glassmorphism modal. Delegated click listener: opens on any anchor/button whose `href="#contact"`, has `data-consult`, or text starts with "book". Fields: Name, Email, Phone (added), Business, Message. Esc/backdrop/× close. **No calendar embed yet** — user still owes calendar link.
- `<BackToTop />` — orange arrow, appears at scroll>600, bottom-24 on mobile (above sticky bar), bottom-6 desktop
- `<MobileBookBar />` — sticky bottom "Book an Appointment" bar, `sm:hidden`

---

## Nav (`components/Nav.tsx`)

- Floating pill header, J.Scott-style. **Fixed top**. On `scrollY > 120`: shrinks to max-w-5xl rounded-full white/85 backdrop pill; logo h-14→h-11.
- Desktop: logo + 5 links (Services, Work, Case Studies, Blog, About) + "Book an Appointment" btn
- Mobile: logo + hamburger only (btn hidden; sticky bottom bar covers CTA). Fixed the unlayered `.btn{display:inline-flex}` beating `hidden` by wrapping the button in `<span className="hidden sm:block">`.

---

## Assets

All in `~/Desktop/sushantrana-next/public/`.

- `logo.png` — header logo (from user's `करते (4).png`)
- `logo-white.png` — footer white logo (from `करते (3).png`)
- `app/icon.png` — favicon (from `Untitled design (12).png`)
- `hero/hero.png` — 1008×567 hero banner
- `about/about.png` — About-Me portrait banner (landscape)
- `blog/post-1.png` … `post-3.png` — blog covers
- `footer/footer-bg.png` — footer + Final CTA + Consult card background
- `logos/*.png` — 23 tool logos, semantic names: google-ads, meta, tiktok, instagram, mailchimp, bing, chatgpt, gemini, ga4, gtm, hubspot, klaviyo, linkedin, wordpress, webflow, wix, zoho, make, zapier, microsoft, growth **(bad)**, gohighlevel **(bad — actually AISensy)**, clarity **(bad — wrong)**
- `png-logo/*.png` — 19 blurred background floating logos (`components/FloatingLogos.tsx` uses these numerically at 15% opacity, blur 2px, `drift1`/`drift2` keyframes)

### ⚠️ Assets user still owes

- **Correct `gohighlevel.png`** and **`clarity.png`** in `public/logos/` (uploaded files are wrong — dropped from marquee + hero + Tech Stack, replaced with correct ones)
- **Calendar link** (Google Appointment Schedule / Calendly / Cal.com) — wire into `ConsultPopup.tsx` when ready
- Optional: Shopify / Snapchat / Amazon / Claude logos

---

## Reveals & animation

- `components/useInViewport.ts` — native IntersectionObserver hook. **Do NOT use framer-motion `whileInView` / `useInView` — dead on Next 16 + React 19 in this stack; every reveal stuck hidden.** Always drive with `animate={inView ? "show" : "hidden"}` and this hook.
- `components/Reveal.tsx` — spring-bounce reveal (stiffness 120, damping 13). Also exports `RevealWords`.
- Reveal trigger margin: `-5%` from bottom.
- Card hover lift + orange glow — in `.card:hover` in globals.

---

## Gotchas (real, hit in this project)

1. **framer-motion `whileInView` is broken** on Next 16 + React 19 → replaced with native IO hook (above). Do not regress.
2. **MCP browser preview pane runs with `document.hidden = true`** → all rAF animations (framer, r3f, counters, marquees) freeze mid-frame. Screenshots look broken but the real browser plays fine. To verify: use `npm run build` + force-reveal CSS injection, not raw screenshots. Force-reveal:
   ```js
   const s=document.createElement('style');s.textContent='[style*="opacity"]{opacity:1!important;}';document.head.appendChild(s);
   ```
3. Unlayered CSS (`.btn`, `h2{color}`) beat Tailwind utilities. Fix: wrap in `@layer base` (h2 fix applied), or wrap element in a span for utility to bite (btn fix in Nav).
4. Turbopack sometimes caches a stale error from mid-edit save. Fix: `rm -rf .next && npm run dev`.
5. `qlmanage`/`ffmpeg` not available in this env → couldn't parse user's `.mov` recordings. Ask user for site URLs instead of videos.

---

## Content decisions

- **Rotating hero questions** (`RotatingHeadline.tsx`): 4 lines — "Why aren't you getting enough **leads**?" · "Why is your **ROAS**⏎dropping?" (forced br) · "Why aren't your visitors **converting**?" · "Why isn't your business **scaling**?" · rotates every 4.4s
- Removed the 5th "Why is your marketing not delivering predictable revenue?" (broke to 3 lines, shifted layout)
- Hero button: **"Book an Appointment"** (was "Book a FREE appointment with me")
- Real **My Numbers**: `$10K+/month · 20+ clients · 6.2× revenue`
- Best ROAS: **4×** (was 11.2×)
- About Me copy: locked (business growth consultant, revenue systems, 8+ yrs, 4 markets)
- Sections **removed**: "What Makes Me Different", "Where I Work" (Markets), "Talk to the person" (ConsultSlots) — files kept but unused
- FAQ = 12 Qs, 2 cols

---

## Git status

- Local repo initialized at `~/Desktop/sushantrana-next/`, all 108 files staged
- **Commit NOT made yet.** Target: `github.com/sushantkumarrana/sushantrana`
- `gh` authed as both `gaccesswebi-rgb` and `sushantkumarrana` (active)
- Blocker: `sushantkumarrana`'s PAT lacks `createRepository` scope → user must create the empty repo manually at github.com/new (owner `sushantkumarrana`, name `sushantrana`, public, no README/gitignore), then next chat runs:
  ```bash
  cd ~/Desktop/sushantrana-next
  git commit -m "Initial commit"
  git remote add origin https://github.com/sushantkumarrana/sushantrana.git
  git push -u origin main
  ```

---

## Open TODO

1. [ ] User creates GitHub repo `sushantkumarrana/sushantrana` → commit + push
2. [ ] Correct GoHighLevel + Clarity logo files → drop in `public/logos/`
3. [ ] Calendar embed link → wire into `ConsultPopup.tsx`
4. [ ] Optional: Shopify / Snapchat / Amazon / Claude logos
5. [ ] Real testimonials (currently illustrative)
6. [ ] Other pages: About, Work, Case Studies, Services, Blog listing, individual blog/case pages, Privacy, Terms

---

## Quick sanity checklist for next chat

- `npm run dev` should serve on :3000 · `npm run build` should pass
- White hero → grey rest → dark footer, orange `#FF4D00` accents
- Floating pill nav on scroll
- Cursive Playwrite Tanzania labels above each section title
- All "Book" CTAs open the glass popup
- Marquee order: black · orange · black · orange · orange (5 straight strips between the grey sections)
