/**
 * Content for /services/shopify-store-development.
 *
 * The section order follows the layout the client approved. All wording here
 * is written fresh for this site rather than lifted from any reference page,
 * so the page carries no duplicate-content or attribution risk.
 *
 * SHOPIFY_FAQS also feeds FAQPage JSON-LD in the route, so the visible
 * accordion and the structured data can never disagree — a requirement of
 * Google's FAQ guidelines.
 */

export const CTA_LABEL = "Get your free Shopify store quote";

/** Hero proof tiles. Figures supplied by Sushant Rana. */
export const HERO_STATS = [
  { n: "8+", label: "Years in performance marketing" },
  { n: "50+", label: "Client brands" },
  { n: "4.2x", label: "Average conversion lift" },
  { n: "4-6wk", label: "Launch timeline" },
];

/* --------------------------------------------------- store experiences */

export const STORE_EXPERIENCE_POINTS = [
  "Homepage design that matches your brand guide",
  "Collection and product templates",
  "Best experienced cart and checkout journey",
  "Mobile and fold phone first responsive",
];

export const PRODUCT_PAGE_POINTS = [
  "Add to cart and buy now that follow the scroll",
  "Zoomable gallery with video support",
  "Ratings, answers and reassurance where doubt appears",
  "Bundle, upsell and cross sell blocks",
];

export const PRODUCT_CARD_POINTS = [
  "Size, colour and pack pickers on the card",
  "Live pricing with discount and offer badges",
  "Benefit icons and reassurance marks",
  "Add to cart without reloading the page",
];

/* ------------------------------------------------- custom development */

export const CUSTOM_DEV_POINTS = [
  {
    t: "Conversion engineering",
    d: "Journey mapping, reassurance cues, scarcity where it is honest, and a checkout stripped of friction. All of it decided before the first component is written.",
  },
  {
    t: "A foundation that scales",
    d: "Structured so your hundredth order and your busiest festive week run on the same theme, with no rebuild in between.",
  },
];

export const STORE_PAGES = [
  "Homepage",
  "Product page",
  "Collections",
  "Cart drawer",
  "Checkout",
  "About and contact",
];

export const TECH_STACK = ["Liquid", "Tailwind", "Alpine.js", "Klaviyo", "Judge.me", "GA4"];

/* ------------------------------------------------------------ process */

/** Three-stage sprint shown beside the project panel. */
export const SPRINT = [
  {
    n: "01",
    t: "Discover and sketch",
    d: "I study your brand, your buyers and your targets, then hand you wireframes and visual mockups in the first fortnight. Nothing gets coded until you sign those off.",
  },
  {
    n: "02",
    t: "Develop and integrations",
    d: "Theme development, app connections, payment configuration and content transfer all move together instead of queueing behind one another.",
  },
  {
    n: "03",
    t: "Go live and optimise",
    d: "Quality checks, a speed pass, an SEO sweep and a calm launch. A month of aftercare follows, so early wrinkles get ironed out quickly.",
  },
];

export const SPRINT_TIMELINE = [
  { t: "Discovery", w: "W1" },
  { t: "Design", w: "W1-2" },
  { t: "Build", w: "W2-5" },
  { t: "Testing", w: "W5" },
  { t: "Launch", w: "W6" },
];

/**
 * The interactive four-step walkthrough further down the page.
 * `art` selects the illustration frame drawn for that step.
 */
export const PROCESS = [
  {
    n: "01",
    t: "Discovery and strategy",
    art: "search" as const,
    d: "I dig into your brand, your buyers, your rivals and your targets. What comes out of that week is the blueprint every later decision points back to.",
    detail: [
      "Buyer and category research",
      "Competitor teardown",
      "Store map and page inventory",
    ],
  },
  {
    n: "02",
    t: "Design and wireframes",
    art: "design" as const,
    d: "Every page arrives as a finished visual before code starts. You approve each screen, so nothing is a surprise when the build lands.",
    detail: ["Wireframes for every template", "Full visual design", "Two revision rounds"],
  },
  {
    n: "03",
    t: "Build and quality checks",
    art: "build" as const,
    d: "Hand written Liquid, tested across browsers and on real handsets. Nothing ships while a journey is still broken somewhere.",
    detail: ["Hand coded theme", "Cross device testing", "Payment and app setup"],
  },
  {
    n: "04",
    t: "Launch and tuning",
    art: "launch" as const,
    d: "I run the launch, watch the numbers and keep improving through the first month, so the store is stronger in week four than it was on day one.",
    detail: ["Managed go live", "Speed and SEO pass", "30 days of aftercare"],
  },
];

/* ---------------------------------------------------------- what you get */

/** `icon` maps to a lucide icon in the component. */
export const WHAT_YOU_GET = [
  {
    icon: "palette" as const,
    t: "A theme designed for your brand",
    d: "Your storefront is drawn from scratch around your identity, matched to your references, and shaped so every screen pushes gently towards checkout.",
  },
  {
    icon: "gauge" as const,
    t: "Performance engineering",
    d: "Trimmed code, right sized images and deferred loading. Speed is not a vanity score, it is the difference between a sale and a closed tab.",
  },
  {
    icon: "smartphone" as const,
    t: "Designed for the phone first",
    d: "Most of your buyers arrive on a handset, so the phone layout is drawn first and the desktop version grows out of it, never the other way round.",
  },
  {
    icon: "search" as const,
    t: "An SEO foundation from day one",
    d: "Titles, descriptions, structured data, clean URLs, alt text and a sitemap all ship with the store, so organic traffic can start building immediately.",
  },
  {
    icon: "plug" as const,
    t: "Apps wired in properly",
    d: "Klaviyo, Yotpo, ReCharge, Judge.me and the rest of your stack are connected and configured, not bolted on and left half set up.",
  },
  {
    icon: "graduation" as const,
    t: "Training and handover",
    d: "You finish knowing how to run the store yourself: recorded walkthroughs, written notes and a month of support while you settle in.",
  },
];

/* ------------------------------------------------------------ why me */

export const REVENUE_MACHINE = [
  {
    t: "Choices grounded in evidence",
    d: "Layout, button placement and page order come from what tracking and testing actually show, not from whichever mockup looked prettiest.",
  },
  {
    t: "Ruthless about speed",
    d: "Every additional second of waiting quietly costs you buyers. Lean code and a pre launch audit keep the store quick, because quick pages earn more.",
  },
  {
    t: "Your brand, never a template",
    d: "A shopper should recognise your store instantly. I build something distinctive rather than dressing up a theme thousands of others already run.",
  },
];

export const WHY_CHOOSE = [
  {
    t: "Written by hand, start to finish",
    d: "No page builder, no recycled template. Every piece of Liquid, CSS and JavaScript is written for your catalogue, so nothing arrives bloated with features you will never switch on.",
  },
  {
    t: "You deal with me, not a queue",
    d: "There is no account manager passing your notes to a team you never meet. The person you brief is the person writing the code.",
  },
  {
    t: "A month of aftercare",
    d: "Launch day is the start, not the exit. You get thirty days of tuning, fixes and improvements while the first real traffic arrives.",
  },
];

export const COMPETITIVE_EDGE = [
  {
    t: "Current, not dated",
    d: "I pick up new tooling early, from AI assistants to modern front end patterns, so your store does not feel three years old the month it launches.",
  },
  {
    t: "Fewer manual hours",
    d: "Automations, tailored workflows and connected systems remove the copy and paste work that quietly eats your week.",
  },
  {
    t: "A better journey for shoppers",
    d: "From usability reviews to phone first layouts, every touchpoint is judged on whether it helps someone buy, not on whether it looks clever.",
  },
  {
    t: "Analytics behind every call",
    d: "GA4 and ecommerce tracking are wired in from the start, so decisions rest on recorded behaviour rather than opinion.",
  },
  {
    t: "Ready for what comes next",
    d: "Built on Shopify's current foundations, including Online Store 2.0 sections and checkout extensibility, so future features slot in instead of forcing a rebuild.",
  },
];

/* ------------------------------------------------------- comparison */

export const COMPARE_ROWS = [
  { label: "Cost", me: "Quoted upfront", freelancer: "Hard to predict", agency: "Three to five times higher" },
  { label: "Pricing model", me: "Fixed project fee", freelancer: "Billed by the hour", agency: "Ongoing retainer" },
  { label: "Start of work", me: "Inside 48 hours", freelancer: "A week or two of waiting", agency: "Two to four week queue" },
  { label: "Turnaround", me: "One to four weeks", freelancer: "Rarely predictable", agency: "Eight to sixteen weeks" },
  { label: "Code", me: "Written by hand", freelancer: "Quality varies", agency: "Usually template based" },
  { label: "Performance", me: "Tuned before launch", freelancer: "Inconsistent", agency: "Middling" },
  { label: "Theme editor support", me: "Every section editable", freelancer: "Partial", agency: "Basics only" },
  { label: "After launch", me: "30 days included", freelancer: "Charged extra", agency: "Retainer required" },
  { label: "Who owns the code", me: "You do, entirely", freelancer: "Depends on the deal", agency: "Risk of lock-in" },
];

/* ------------------------------------------------------------- FAQs */

/** `link` points an answer at the blog post that covers it in depth. It is
 *  rendered under the visible answer only; the JSON-LD keeps the plain text. */
export const SHOPIFY_FAQS: { q: string; a: string; link?: { href: string; label: string } }[] = [
  {
    q: "How long does a Shopify store build take?",
    a: "Most builds run between one and four weeks. A tightly scoped store can be live in seven to ten days, while a larger custom catalogue takes three to four weeks. You get a dated schedule before anything is agreed.",
  },
  {
    q: "What does the price cover?",
    a: "Scoping, design, hand written development, two revision rounds, the responsive build, browser and device testing, and thirty days of support after launch. Nothing is added to the invoice later.",
  },
  {
    q: "Who owns the code and the design files?",
    a: "You do, completely. Source files, design assets and the theme are handed over when the project closes. There is no licence to renew and no vendor to stay tied to.",
  },
  {
    q: "How many revision rounds are included?",
    a: "Two rounds come as standard. Further rounds are available at a flat hourly rate, though most projects are settled after the first.",
  },
  {
    q: "What if I need changes once the store is live?",
    a: "The first thirty days cover fixes and small adjustments at no cost. Beyond that I work either on a monthly retainer or task by task, whichever suits you.",
  },
  {
    q: "How does payment work?",
    a: "Half to begin and half on delivery is the usual arrangement. Longer projects can be split across milestones instead. Bank transfer and UPI both work for clients in India.",
  },
  {
    q: "Will you sign an NDA?",
    a: "Yes. Send yours across before we talk specifics, or use mine if that is easier.",
  },
  {
    q: "Can I see examples of stores you have built?",
    a: "Yes. On the discovery call I walk you through relevant projects and live links, so you can judge the work rather than take my word for it.",
  },
  {
    q: "How quickly do you respond to support requests?",
    a: "You will hear back within a few working hours, and most issues are resolved inside a day or two. Anything breaking on a live storefront is handled the same day.",
  },
  {
    q: "Will my existing apps still work?",
    a: "Yes. The usual ecommerce stack, including Klaviyo, ReCharge, Yotpo, Judge.me, Gorgias and the common shipping tools, is carried across and reconfigured properly.",
  },
  {
    q: "What if I am unhappy with the result?",
    a: "Then it is not finished. I would rather return to the drawing board than hand over a storefront you would hesitate to share.",
  },
  {
    q: "Do you handle putting the store live?",
    a: "Yes. The new theme goes up as a duplicate for review first, then goes live while you watch, and I stay reachable for the following day.",
  },
  {
    q: "How will we communicate during the project?",
    a: "Short written updates on WhatsApp or Slack, a call whenever a decision needs one, and one shared document holding the brief, the mockups and every decision made.",
  },
  {
    q: "What do you need from me to start?",
    a: "Your current store link if there is one, any brand guidelines, a few reference sites you admire, and a short note on what the store has to achieve. A structured questionnaire follows kickoff.",
  },
  {
    q: "Do you offer ongoing support after the first month?",
    a: "Yes. Monthly retainers cover continued optimisation, design updates, app work and fixes for store owners who would rather not manage it themselves.",
  },
  {
    q: "Will my store look different from other Shopify sites?",
    a: "Yes. Nothing is reused between clients. Wireframes start from your catalogue and your customers, so the finished storefront belongs to your brand alone.",
    link: {
      href: "/blog/will-my-shopify-store-look-different",
      label: "Why most Shopify stores look alike, and how to avoid it",
    },
  },
  {
    q: "Can I edit the content myself afterwards?",
    a: "Yes. Every section is exposed in the Shopify theme editor, so wording, images, colours and buttons can all be changed without touching code.",
  },
  {
    q: "What if I want to add products or new sections later?",
    a: "The store is built on Online Store 2.0 with reusable sections, so you can add products, collections and pages yourself. Bring me back only when you want something genuinely new built.",
  },
  {
    q: "Can you move my products across from another platform?",
    a: "Yes. Products, customer records, order history, redirects and the SEO groundwork all come across, which is what keeps your existing rankings intact through the move.",
  },
  {
    q: "Which apps will I actually need?",
    a: "Only the ones that earn their place. I suggest a short, deliberate stack for reviews, email and retention, set it up correctly, and leave the rest out so the store stays fast.",
  },
];

/** Cluster links, matching the internal-link plan for the web development hub. */
export const RELATED_SERVICES = [
  { label: "Website maintenance", href: "/services/website-maintenance" },
  { label: "Ecommerce SEO", href: "/services/ecommerce-seo" },
  { label: "Google Shopping Ads", href: "/services/google-shopping-ads" },
  { label: "D2C Meta Ads", href: "/services/meta-ads" },
  { label: "Sales funnel setup", href: "/services/sales-funnel-setup" },
];
