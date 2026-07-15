/* All site content data. Truthful to an 8-year solo consultant; every
   unverified figure carries a REPLACE marker. */
"use strict";

/* ---------- hero floating stats + stats bar ---------- */
// REPLACE: verify every figure with real client data before launch
const STATS = [
  { prefix: "", value: 8, suffix: "+", label: "Years in growth & performance" },
  { prefix: "₹", value: 50, suffix: "L+", label: "Ad spend managed" },
  { prefix: "₹1–", value: 2, suffix: " Cr", label: "Revenue generated for clients" },
  { prefix: "", value: 11.2, suffix: "×", decimals: 1, label: "Best B2B campaign ROAS" },
];

/* ---------- industries (tabbed) ---------- */
const INDUSTRY_TABS = [
  ["healthcare", "Healthcare", "Appointment-driven demand where trust and compliance decide the sale.", ["Local + treatment-intent search", "Reminder & no-show automation", "Reputation and review systems"]],
  ["education", "Education", "Intake-deadline cycles where lead quality beats lead volume.", ["Qualified enquiry campaigns", "Counsellor lead scoring", "Nurture to enrolment"]],
  ["manufacturing", "Manufacturing", "Long B2B cycles where the pipeline must be visible and predictable.", ["Specification-intent search", "Procurement retargeting", "Quote-ready funnels"]],
  ["saas", "SaaS & Tech", "Demand engines that move past founder-led sales to inbound demos.", ["Category & competitor search", "Trial nurture automation", "Demo-booking funnels"]],
  ["construction", "Construction", "Credibility infrastructure that wins larger tenders and projects.", ["Capability-led websites", "Developer & PMC targeting", "Tender-stage remarketing"]],
  ["fashion", "Fashion & D2C", "Escaping the discount spiral with margin-aware paid social.", ["Creative-velocity testing", "Catalog by margin", "Retention email flows"]],
  ["professional", "Professional Services", "Predictable acquisition beyond referrals for high-value services.", ["High-intent search", "Case-fit qualification", "CRM follow-up automation"]],
  ["realestate", "Real Estate", "Site visits and qualified enquiries, not portal lead dumps.", ["Budget-qualifying forms", "WhatsApp scheduling", "Cost-per-visit reporting"]],
];

/* ---------- services (4 pillars) ---------- */
const PILLARS = [
  ["strategy", "Brand Strategy & Consulting", "Positioning, offer, messaging, and go-to-market — the thinking layer every campaign stands on.", "services.html#brand-strategy"],
  ["performance-marketing", "Performance Marketing", "Google, Meta, TikTok, Snapchat, LinkedIn, Microsoft, and Amazon Ads — measured to revenue.", "performance-marketing.html"],
  ["ai-automation", "AI Automation", "CRM automation, lead scoring, pipelines, AI assistants, WhatsApp, and reporting that runs itself.", "services.html#ai-automation"],
  ["web-development", "Website Development", "Shopify, WordPress, Wix Studio, Webflow, and custom builds — assets, not brochures.", "development.html"],
];

/* ---------- how I work (timeline) ---------- */
const PROCESS = [
  ["Discovery", "30-minute consultation", "Understand the business problem, review current marketing, and identify the gaps worth closing."],
  ["Research", "One week", "Website, brand, accounts, customer journey, and competitors — find the weaknesses before recommending anything."],
  ["Implementation", "Fix the foundations", "Remove bottlenecks in priority order: branding, systems, and campaigns — before spending on scale."],
  ["Growth", "Compound", "Launch the complete revenue system — traffic, conversion, follow-up, and reporting — built for sustainable scale."],
];

/* ---------- performance platforms (marquee) ---------- */
const PERF_PLATFORMS = [
  ["ppc-ads", "Google Ads"], ["social", "Meta Ads"], ["performance-marketing", "LinkedIn Ads"],
  ["spark", "TikTok Ads"], ["target", "Snapchat Ads"], ["search", "Microsoft Ads"], ["cart", "Amazon Ads"],
];

/* ---------- AI automation capabilities ---------- */
const AI_CAPS = [
  "CRM automation", "Lead scoring", "Sales pipeline automation",
  "AI assistants", "WhatsApp automation", "Automated reporting systems",
];

/* ---------- why hire me (differentiators) ---------- */
const WHY_HIRE = [
  ["handshake", "One point of accountability", "You talk to the person doing the work — no account-manager layer, no outsourced pod."],
  ["revenue-system", "Systems over campaigns", "Everything is built to compound: positioning, traffic, conversion, follow-up, and retention as one engine."],
  ["globe", "Cross-border experience", "Engagements across Australia, Canada, the USA, and India — budgets managed in local currency."],
  ["brain", "Full-stack, senior-led", "Strategy, ads, automation, and site under one roof — aligned to your revenue number, not a channel KPI."],
];

/* ---------- comparison (what makes me different) ---------- */
const COMPARISON = {
  cols: ["Sushant Rana", "In-house junior", "Typical agency"],
  rows: [
    ["Senior operator doing the work", ["yes"], ["no"], ["Varies"]],
    ["Owns the revenue number", ["yes"], ["Partly"], ["Owns a channel KPI"]],
    ["Strategy + ads + automation + site", ["yes"], ["no"], ["Usually one silo"]],
    ["Direct access, no account layer", ["yes"], ["yes"], ["no"]],
    ["Cross-border (AU · CA · US · IN)", ["yes"], ["no"], ["Varies"]],
    ["Transparent, you own every account", ["yes"], ["yes"], ["Sometimes"]],
  ],
};

/* ---------- core values ---------- */
const VALUES = [
  ["target", "Customer First", "Every decision starts with the person buying, not the channel selling."],
  ["brain", "Psychology Before Marketing", "Understand why people buy before spending a rupee on reaching them."],
  ["shield-trust", "Transparency", "Full access to accounts, data, and reporting. You own everything, always."],
  ["partnership", "Long-Term Partnerships", "Systems compound. I build for the second year, not the first month."],
  ["spark", "Innovation", "New tools earn their place by producing results, not by being new."],
  ["knowledge", "Continuous Learning", "Platforms change monthly. Staying current is part of the job."],
];

/* ---------- tech stack (marquee) ---------- */
const TECH_STACK = [
  ["ppc-ads", "Google Ads"], ["social", "Meta Ads"], ["performance-marketing", "LinkedIn"],
  ["analytics-dashboard", "GA4"], ["gear", "GTM"], ["search", "Microsoft Clarity"],
  ["crm", "HubSpot"], ["crm", "Zoho CRM"], ["email", "Klaviyo"], ["node-graph", "Make / Zapier"],
  ["cart", "Shopify"], ["layout", "WordPress"], ["web-development", "Webflow"], ["layout", "Wix Studio"],
  ["robot", "ChatGPT"], ["brain", "Claude"], ["spark", "Gemini"],
];

/* ---------- global markets ---------- */
const GLOBAL_MARKETS = [
  ["Australia", "Performance campaigns & growth systems", "AUD budgets"],
  ["Canada", "Paid media managed in local currency", "CAD $9,000/mo managed"],
  ["United States", "Cross-border demand generation", "USD campaigns"],
  ["India", "Full-stack growth engagements", "Home market"],
];

/* ---------- case studies (9) ---------- */
// REPLACE: all case studies below are plausible placeholders. Verify every
// metric and client detail with real, client-approved data before launch.
const CASE_STUDIES = [
  {
    industry: "Manufacturing · B2B", tags: "performance",
    title: "Industrial equipment maker turns dealer enquiries into a pipeline",
    problem: "A precision components manufacturer relied on trade shows and word of mouth. Enquiries were unpredictable and sales had no visibility on the next order.",
    strategy: "Positioned around lead time and certification — what buyers actually compare — and built search-led demand capture on Google and Microsoft Ads.",
    execution: "High-intent search, LinkedIn retargeting for procurement, a CRM pipeline with lead scoring, and quote-request pages built for engineers.",
    results: "11.2× ROAS on the flagship campaign and a quoting pipeline sales now plans production around. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "Healthcare", tags: "performance automation",
    title: "Multi-location clinic fills its calendar without discounting",
    problem: "Bookings depended on referrals. A previous agency's campaigns generated calls, but mostly price shoppers who never showed.",
    strategy: "Shifted targeting from symptom keywords to treatment-decision keywords and rebuilt the offer around consultation quality.",
    execution: "Google Search with call tracking, per-branch location extensions, WhatsApp booking automation, and reminder workflows.",
    results: "Cost per booked appointment down 47% and show-up rate up by a third in one quarter. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "Education", tags: "performance automation",
    title: "Training institute doubles qualified admissions enquiries",
    problem: "An education brand spent heavily on Meta but counsellors said the leads never answered the phone.",
    strategy: "Introduced lead scoring and qualification at the form level — fewer, better leads — aligned to intake deadlines.",
    execution: "Meta lead-gen with qualifying forms, Google Search for course demand, CRM automation routing hot leads within five minutes.",
    results: "2.8× more marketing-qualified leads at a 38% lower cost per enrolment conversation. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "SaaS · B2B", tags: "performance",
    title: "SaaS platform moves from founder-led sales to inbound demos",
    problem: "A workflow SaaS had product-market fit, but every demo was hand-won by the founder on LinkedIn.",
    strategy: "Built a demand engine around the problem the product kills — manual reporting — rather than the feature list.",
    execution: "LinkedIn thought-leader ads, Google Search on category terms, a demo landing page, and HubSpot trial-nurture workflows.",
    results: "Inbound demos grew from a handful a month to a consistent weekly pipeline at a sustainable CAC. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "Construction", tags: "web",
    title: "Commercial contractor wins larger tenders with a credibility engine",
    problem: "A contracting firm lost commercial tenders to better-presented competitors despite stronger delivery records.",
    strategy: "Treated the website and case documentation as sales infrastructure procurement teams could verify before shortlisting.",
    execution: "New project-portfolio website, downloadable capability statements, LinkedIn campaigns to developers, and tender-stage remarketing.",
    results: "Shortlist rate on submitted tenders improved measurably within two quarters. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "Fashion · D2C", tags: "performance web",
    title: "Fashion label escapes the discount spiral",
    problem: "A D2C fashion brand was profitable only during sales. Full-price sell-through was weak and repeat rates falling.",
    strategy: "Rebuilt the journey around collection storytelling and post-purchase flows instead of permanent promotions.",
    execution: "Meta catalog by margin, TikTok creative testing, Klaviyo repeat-purchase flows, and AOV-focused bundling on Shopify.",
    results: "AOV up 24% and a growing share of full-price revenue. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "Professional Services", tags: "performance automation",
    title: "Law practice builds a predictable client acquisition channel",
    problem: "A specialist law practice depended entirely on referrals with no way to grow beyond its network.",
    strategy: "Positioned around one high-value practice area and built search for the exact moments clients look for help.",
    execution: "Google Search with strict negatives, an intake form that pre-qualified case fit, and CRM automation for follow-up.",
    results: "A steady flow of qualified consultations at a cost per case the partners signed off on. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "Real Estate", tags: "performance automation",
    title: "Developer sells out a project phase with qualified site visits",
    problem: "A residential developer generated thousands of portal leads, but site visits — what sells apartments — stayed flat.",
    strategy: "Moved budget from portals to owned campaigns and made the site visit, not the lead, the conversion event.",
    execution: "Budget-qualifying forms on Google and Meta, WhatsApp automation for brochures and scheduling, and cost-per-visit reporting.",
    results: "Cost per qualified site visit dropped sharply and the phase closed ahead of plan. <!-- REPLACE: client-verified metric -->",
  },
  {
    industry: "D2C · Wellness", tags: "performance",
    title: "Wellness brand scales internationally without breaking its CAC",
    problem: "A wellness D2C brand had saturated its home market; scaling spend pushed CAC past breakeven.",
    strategy: "Expanded to Canada and the UAE with localised offers and currency-specific pricing instead of copy-pasting campaigns.",
    execution: "Market-by-market launch on Meta and Google Shopping, CAD and AED budget management, server-side tracking, and localised pages.",
    results: "Two new markets contributing revenue at an LTV/CAC of 3.6× within six months. <!-- REPLACE: client-verified metric -->",
  },
];

/* ---------- testimonials ---------- */
// REPLACE: all testimonials are placeholders pending client-approved quotes
const QUOTES = [
  { quote: "Sushant didn't start with ads. He started with our customers — why they buy, why they leave. The campaigns that came out of that research outperformed anything we'd run before.", name: "Placeholder Name", role: "Founder, D2C Brand <!-- REPLACE: client name, role, permission -->" },
  { quote: "The lead scoring and CRM automation alone paid for the engagement. Our sales team stopped chasing dead leads and started closing warm ones.", name: "Placeholder Name", role: "Sales Director, B2B Manufacturer <!-- REPLACE: client name, role, permission -->" },
  { quote: "Finally, a consultant who talks about revenue and payback period instead of impressions. The monthly report is five numbers we actually use in board meetings.", name: "Placeholder Name", role: "CEO, SaaS Company <!-- REPLACE: client name, role, permission -->" },
];

/* ---------- blog (9 posts) ---------- */
const BLOG_POSTS = [
  { category: "Business Strategy", cat: "strategy", title: "Revenue Systems vs Marketing Campaigns: Why One Compounds and the Other Expires", excerpt: "Campaigns end. Systems compound. The structural difference between businesses that grow predictably and businesses that buy growth one month at a time.", date: "2026-06-18", dateLabel: "18 Jun 2026", read: "8 min", img: "blog-revenue-systems.svg" },
  { category: "Marketing", cat: "marketing", title: "Lead Quality Over Lead Volume: The Metric Shift That Changes Everything", excerpt: "A thousand leads that never answer the phone cost more than a hundred that do. How to rebuild campaigns around qualified conversations.", date: "2026-06-04", dateLabel: "4 Jun 2026", read: "6 min", img: "blog-lead-quality.svg" },
  { category: "AI", cat: "ai", title: "Practical AI Automation for Businesses That Don't Have a Data Team", excerpt: "You don't need ML engineers. You need five workflows: lead scoring, follow-up, reporting, routing, and reactivation.", date: "2026-05-21", dateLabel: "21 May 2026", read: "7 min", img: "blog-ai-automation.svg" },
  { category: "Marketing", cat: "marketing", title: "Why Running Ads Without Positioning Burns Money", excerpt: "If your ad says what every competitor's ad says, the auction decides on price alone. Positioning is the cheapest performance lever you're not using.", date: "2026-05-08", dateLabel: "8 May 2026", read: "5 min", img: "blog-positioning.svg" },
  { category: "Automation", cat: "automation", title: "The Five-Minute Rule: What Happens to Leads After the Form Submit", excerpt: "Speed-to-lead is the highest-leverage fix in most funnels. How CRM automation turns response time from hours into minutes.", date: "2026-04-23", dateLabel: "23 Apr 2026", read: "6 min", img: "blog-speed-to-lead.svg" },
  { category: "Business Strategy", cat: "strategy", title: "Customer Psychology Precedes Media Buying", excerpt: "Targeting finds people. Psychology converts them. The research step that separates profitable accounts from expensive ones.", date: "2026-04-09", dateLabel: "9 Apr 2026", read: "7 min", img: "blog-psychology.svg" },
  { category: "Case Studies", cat: "case-studies", title: "Anatomy of an 11.2× ROAS B2B Campaign", excerpt: "A teardown of the structure behind a manufacturing campaign: keyword intent, quote-ready landing pages, and a sales team in the loop.", date: "2026-03-26", dateLabel: "26 Mar 2026", read: "9 min", img: "blog-b2b-roas.svg" },
  { category: "AI", cat: "ai", title: "AI Assistants in Sales Pipelines: Where They Help and Where They Hurt", excerpt: "AI that drafts follow-ups and scores leads earns its keep. AI that talks to your customers unsupervised does not. A field guide.", date: "2026-03-12", dateLabel: "12 Mar 2026", read: "6 min", img: "blog-ai-sales.svg" },
  { category: "Automation", cat: "automation", title: "Reporting Systems That Executives Actually Read", excerpt: "One dashboard, five numbers, sent every Monday. How to automate reporting that drives decisions instead of decorating them.", date: "2026-02-26", dateLabel: "26 Feb 2026", read: "5 min", img: "blog-reporting.svg" },
];

/* ---------- categorized FAQ ---------- */
const HOME_FAQ = [
  ["working", "How is your pricing structured?", "Project work is fixed-fee, quoted after the discovery call. Ongoing performance and automation retainers are monthly, scoped to the channels and hours involved. You always know the number before any work starts — no percentage-of-spend surprises."],
  ["working", "What happens on the free consultation call?", "Thirty minutes. You describe the business, the goal, and what you've tried. I ask questions, look at what you share, and tell you honestly whether I can help. If I can, you get a scoped proposal. If not, I'll point you somewhere useful."],
  ["working", "Who does the actual work?", "I do. There's no account-manager layer or outsourced pod — you work directly with the person responsible for the result."],
  ["working", "How do we communicate during an engagement?", "A shared Slack or WhatsApp channel for the day-to-day, a scheduled monthly review call, and email for anything formal. You talk to me directly."],
  ["pricing", "Is there a minimum ad budget you work with?", "No hard number, but paid campaigns need enough budget to generate useful data — typically a few hundred dollars a month at minimum. On the call I'll tell you whether your budget fits your goal, or whether organic and automation should come first."],
  ["pricing", "How long does a typical project take?", "Research takes about a week. Website builds run two to six weeks. Paid campaigns show meaningful data within four to six weeks and stabilise over a quarter. Anyone promising results in a week is guessing."],
  ["channels", "Which advertising platforms do you manage?", "Google, Meta (Facebook and Instagram), LinkedIn, TikTok, Snapchat, Microsoft, and Amazon. Where to spend comes from where your buyers are — not from a preference for any platform."],
  ["channels", "Do you build websites, or only run marketing on them?", "Both. I build on Shopify, WordPress, Wix Studio, Webflow, and custom stacks — and because I also run campaigns, everything is built to convert and to measure."],
  ["channels", "What does AI automation actually mean for my business?", "Practical workflows: leads scored and routed in minutes, follow-ups that send themselves, WhatsApp answered out of hours, and reports that build themselves. No experimental tools in production."],
  ["results", "What does monthly management include?", "Campaign optimisation, budget management, creative and copy iterations, landing page recommendations, tracking maintenance, and a monthly report focused on revenue — not vanity metrics. You keep full ownership and admin access."],
  ["results", "How do you measure success?", "Revenue metrics agreed up front: qualified leads, CAC, ROAS, and pipeline contribution — pulled from your CRM and analytics, not screenshots of ad dashboards."],
  ["results", "What support do I get after a project ends?", "Every build ships with documentation and a handover call. Websites include 30 days of post-launch fixes. After that, move to a retainer or engage ad-hoc — nothing is locked in."],
];
const FAQ_CATS = [["all", "All"], ["working", "Working together"], ["pricing", "Pricing"], ["channels", "Channels"], ["results", "Results"]];

module.exports = {
  STATS, INDUSTRY_TABS, PILLARS, PROCESS, PERF_PLATFORMS, AI_CAPS, WHY_HIRE,
  COMPARISON, VALUES, TECH_STACK, GLOBAL_MARKETS, CASE_STUDIES, QUOTES,
  BLOG_POSTS, HOME_FAQ, FAQ_CATS,
};
