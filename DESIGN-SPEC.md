# sushantrana.com — Design Spec v2 (my understanding of your brief)

> Red-line anything wrong. ❓ = I need your answer before building. Nothing built yet.

---

## COLORS (changed — confirm)
- Primary/brand **orange `#FF4D00`** — never a full-page background; OK as **black→orange gradient** (footer, some backgrounds, marquee strips), and for buttons / some titles / some words.
- **Hero section + the image right below it = WHITE background.** Font = near-black.
- **Every section AFTER that = grey stone `#DCDCDC`.**
- Footer = black + orange gradient.

## GLOBAL
- Glassmorphism for forms & popups (frosted glass panels).
- Smooth scroll + scroll animations everywhere; cards animate in; every button has hover; every section has hover feel.
- Marquees wherever they fit; **hover pauses any marquee.**
- Multi-page site (see PAGES).

## FONTS ❓
- Headings: **Cal Sans** (you named it).
- A **cursive accent** for small flourishes (like Agero's "(hello)"). My pick: **Instrument Serif italic** or a script — confirm in questions.
- Body: need one — my pick **General Sans** or **Inter**.

## ICONS ❓ (you asked me to choose a "luxury" set)
- My pick: **Phosphor Icons** (thin/duotone = premium) or **Hugeicons**. Confirm in questions.

## LIBRARIES (tell me and you'll fetch)
- GSAP + ScrollTrigger (scroll animations, pin, slide, graph grow)
- Lenis (smooth scroll)
- Swiper or Splide (marquees / testimonial carousels) — or pure CSS marquee
- Tailwind CSS
- (No jQuery needed unless you prefer it — GSAP covers it.)

---

## HOMEPAGE SECTIONS (top → bottom)

1. **Header/Nav** — WHITE, **NOT sticky**. Left: name + logo. Center: menu. Right: "Book an Appointment" button.

2. **Hero** — WHITE bg, centered.
   - 3–4 big CTA lines (copy from current site): "Why is your ROAS dropping?", "Why aren't your visitors converting?", … Some words in orange. Big type.
   - Paragraph below: "Because you have marketing campaigns — not a revenue system. I build revenue systems…" (from current site).
   - Button: **"Book a FREE appointment with me"**.
   - A **peek** of the section-below image must show at hero bottom (hint there's more).

3. **Hero image** — WHITE bg, image **1008×567** (you provide; placeholder for now).

4. **Tools marquee** — logos: Google Ads, Meta Ads, TikTok Ads, GoHighLevel, Zoho, Shopify, WordPress (you provide logos).
   - Below it: **two diagonal (crossing X) marquees** — one behind, one in front — like the Agero orange/black diagonal strips. Hover pauses.

5. **About Me** — NOT the boring left-image/right-text. Use the Agero **"What we do"** style: centered title + image with a **marquee running behind the image**, then About-Me paragraph below. Uses your photo.

--- (from here down: **grey `#DCDCDC`** bg) ---

6. **The Reality of Growth** — keep exactly as current; just recolor to grey-stone theme; I'll match box/button colors + click states.

7. **Who I Help** — keep the industry-buttons pattern (content swaps per industry). Active button = a non-orange accent; the revealed box = bright white, black content, **orange titles**. Can add images.

8. **What I Do** — title + 4 services kept, new presentation:
   - 4 services stacked **vertically on the left**; click a service → **2 images open on the right** showing what I do there; click another → its 2 images replace them. (Video 2.) You'll provide images. ❓ (see questions)

9. **How I Work** — keep content+presentation; make it taller so on scroll slides **alternate**: slide 1 right→left, slide 2 left→right, etc.

10. **Performance Marketing** — same content, but **more numbers**: animated graphs that grow small→big (like the site you'll link). Platform icons kept, recolored to theme. ❓ link

11. **AI Automation** — keep content + funnel/pipeline animation, **enhance + add content** (per your screenshot).

12. **Selected Results (case studies)** — tabbed by channel (click Ads → ads case studies, etc.). Each card: **project name → 3 metrics → Challenge → Solution → "Read full case study" button.** (Tenfold case-study style.)

13. **What Makes Me Different** — keep, but on **mobile** show all columns are reachable: arrows or auto-scroll left/right.

14. **In Clients' Words (testimonials)** — rebuild: **full-width**, cards in a **marquee (left→right)**. Each card: industry name → quote → divider → (left) client name + company, (right) company logo.

15. **Tech Stack** — keep; **real logos** (you provide).

16. **Blog** — keep; **real images** on posts (placeholder vectors for now).

17. **3 Consult Slots Open This Week** — keep as-is.

18. **FAQ** — keep, but **two columns** (split the list left/right).

19. **Let's Build a System That Keeps Growing** — keep as-is (perfect).

20. **Footer** — rebuild: black→orange gradient, **mouse-move animation** behind, big **faded "सुशांत राणा / Sushant Rana"** at the very bottom (House-of-Web style). All page links grouped.

---

## PAGES (multi-page)
Home · About Me (new) · Work · Case Studies · Services · Blog · Testimonials · Privacy Policy · Terms & Conditions · (individual blog/case-study pages)

## IMAGES / PLACEHOLDERS
Everywhere an image is mentioned → put an internet vector placeholder now; you drop real files into `/assets` later.

---

## ❓ QUESTIONS I NEED ANSWERED BEFORE BUILDING
1. **Framework** — see the popup. (Enhance your existing static site vs continue the Next.js rebuild.)
2. **Videos** — I can't open the 3 `.mov` files here. Instead, please **paste the website URLs** shown in:
   - Video 1 (the site with the running GIF — "What I do" ref) → I'll inspect it live and tell you code-vs-provide.
   - Video 3 / 12.36 (the performance-marketing animated-graph site) → the link you mentioned.
   - Video 2 (4-services click-to-open-images) — I understood from your text; confirm: exactly **2 images per service**, images swap on click? ❓
3. **Icons + fonts** — see popup.
4. **Hero image 1008×567** and **tool/company logos** — send when ready (I'll use placeholders meanwhile).
5. **"What Makes Me Different" mobile** — prefer arrows or auto-scroll? (I'll default to arrows + drag.)
