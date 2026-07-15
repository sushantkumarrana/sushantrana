/* Generators for every page except index.html — new House of Web design. */
"use strict";

const P = require("./partials");
const D = require("./data");
const S = require("./services");
const { icon, ctaBand, breadcrumbs, breadcrumbSchema, SITE } = P;

/* ---------- shared helpers ---------- */
function pageHero(opts) {
  return `    <section class="page-hero" aria-labelledby="page-title">
      <div class="blob hero__blob hero__blob--a" aria-hidden="true" style="opacity:.12"></div>
      <div class="deco-grid" aria-hidden="true"></div>
      <div class="container" style="position:relative;z-index:1">
        ${opts.crumbs ? breadcrumbs(opts.crumbs) : ""}
        <span class="eyebrow">${opts.label}</span>
        <h1 id="page-title" class="reveal">${opts.h1}</h1>
        <p class="lead reveal" style="max-width:60ch">${opts.lead}</p>
        ${opts.cta ? `<p style="margin-top:28px"><a class="btn btn--primary btn--lg" href="consultation.html" data-popup-open data-cta="${opts.ctaSource || "page-hero"}">Book Free Consultation ${icon("arrow-right", "icon-sm")}</a></p>` : ""}
      </div>
    </section>`;
}

function proofSection(name) {
  return `    <section class="section" aria-labelledby="proof-title">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">Results</span>
          <h2 id="proof-title" class="reveal">What this looks like when it works</h2>
          <p class="reveal">Representative outcomes from engagements using this approach.</p>
        </div>
        <!-- REPLACE: client-verified metrics for ${name} -->
        <div class="stat-grid" style="grid-template-columns:repeat(auto-fit,minmax(200px,1fr));max-width:820px;margin-inline:auto">
          ${S.PROOF_DEFAULT.map((s, i) => `<div class="stat reveal" data-delay="${i * 70}">
            <span class="stat__value">${s.prefix || ""}<span data-count="${s.value}"${s.decimals ? ` data-decimals="${s.decimals}"` : ""}>0</span>${s.suffix || ""}</span>
            <span class="stat__label">${s.label}</span>
          </div>`).join("\n          ")}
        </div>
      </div>
    </section>`;
}

function miniFaq(faq, idPrefix) {
  return `    <section class="section" aria-labelledby="${idPrefix}-faq-title" style="background:var(--sky-bg)">
      <div class="container container--narrow">
        <div class="section-head section-head--center">
          <span class="eyebrow">FAQ</span>
          <h2 id="${idPrefix}-faq-title" class="reveal">Common questions</h2>
        </div>
        <div class="acc reveal" data-acc-single>
          ${faq.map(([q, a], i) => `<div class="acc-item">
            <button type="button" class="acc-trigger" aria-expanded="false" aria-controls="${idPrefix}-faq-${i}"><span>${q}</span>${icon("plus", "acc-icon")}</button>
            <div class="acc-panel" id="${idPrefix}-faq-${i}"><p class="acc-body">${a}</p></div>
          </div>`).join("\n          ")}
        </div>
      </div>
    </section>`;
}

function approachSection(approach) {
  return `    <section class="section" aria-labelledby="approach-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">How I approach it</span>
          <h2 id="approach-title" class="reveal">The working method</h2>
        </div>
        <div class="grid steps-grid">
          ${approach.map(([t, p], i) => `<div class="step-card reveal" data-delay="${i * 80}">
            <h3 style="font-size:1.15rem;margin-bottom:6px">${t}</h3>
            <p style="color:var(--gray-med);font-size:0.94rem">${p}</p>
          </div>`).join("\n          ")}
        </div>
      </div>
    </section>`;
}

function includedSection(included, title) {
  return `    <section class="section" aria-labelledby="included-title" style="background:var(--sky-bg)">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">What's included</span>
          <h2 id="included-title" class="reveal">${title || "Everything the engagement covers"}</h2>
        </div>
        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(280px,1fr))">
          ${included.map(([ic, t, p], i) => `<article class="card hover-glow reveal" data-delay="${(i % 3) * 70}">
            <span class="card__icon">${icon(ic)}</span>
            <h3 style="font-size:1.15rem">${t}</h3>
            <p style="font-size:0.94rem">${p}</p>
          </article>`).join("\n          ")}
        </div>
      </div>
    </section>`;
}

function problemSection(svc) {
  return `    <section class="section" aria-labelledby="problem-title">
      <div class="container container--narrow">
        <span class="eyebrow">The problem this solves</span>
        <h2 id="problem-title" class="reveal">${svc.problemH}</h2>
        ${svc.problemP.map((p) => `<p class="reveal" style="margin-top:18px;color:var(--gray-med)">${p}</p>`).join("\n        ")}
      </div>
    </section>`;
}

/* ---------- service page ---------- */
function servicePage(svc) {
  const parent = svc.group === "perf" ? ["performance-marketing.html", "Performance Marketing"] : ["development.html", "Development"];
  const crumbs = [["index.html", "Home"], parent, [null, svc.name]];
  const content = [
    pageHero({ crumbs, label: svc.name, h1: svc.h1, lead: svc.hero, cta: true, ctaSource: svc.file.replace(".html", "") }),
    problemSection(svc),
    includedSection(svc.included),
    approachSection(svc.approach),
    proofSection(svc.name),
    miniFaq(svc.faq, "svc"),
    ctaBand({ source: svc.file.replace(".html", "") }),
  ].join("\n");
  return P.page({ path: svc.file, title: svc.metaTitle, description: svc.metaDesc, active: svc.group === "perf" ? "perf" : "dev", schema: [breadcrumbSchema(crumbs, svc.file)], content });
}

/* ---------- perf hub ---------- */
function perfHubPage() {
  const hub = S.PERF_HUB;
  const crumbs = [["index.html", "Home"], [null, "Performance Marketing"]];
  const content = [
    pageHero({ crumbs, label: "Performance Marketing", h1: hub.h1, lead: hub.hero, cta: true, ctaSource: "performance-marketing" }),
    `    <section class="section" aria-labelledby="platforms-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Platforms</span>
          <h2 id="platforms-title" class="reveal">The budget goes where your buyers are</h2>
          <p class="reveal">Platform choice is an output of research, not a preference. Each has its own dedicated approach.</p>
        </div>
        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
          ${P.PERF_LINKS.map(([href, label], i) => `<article class="card hover-glow tilt reveal" data-tilt="4" data-delay="${(i % 3) * 70}">
            <span class="card__icon">${icon("performance-marketing")}</span>
            <h3 style="font-size:1.2rem">${label}</h3>
            <a class="text-link" href="${href}">How I run ${label} ${icon("arrow-right", "icon-sm")}</a>
          </article>`).join("\n          ")}
          <article class="card hover-glow reveal">
            <span class="card__icon">${icon("cart")}</span>
            <h3 style="font-size:1.2rem">Etsy Ads</h3>
            <p style="font-size:0.94rem">Marketplace advertising for craft and design brands — managed within e-commerce engagements.</p>
          </article>
        </div>
      </div>
    </section>`,
    `    <section class="section" aria-labelledby="angle-title" style="background:var(--sky-bg)">
      <div class="container container--narrow" style="text-align:center">
        <span class="eyebrow">The angle</span>
        <h2 id="angle-title" class="reveal">Lead quality over lead volume</h2>
        <p class="reveal" style="margin:16px auto 0;color:var(--gray-med)">I say it explicitly because most reporting hides it: a cheap lead that never answers the phone is the most expensive thing you can buy. Campaigns here optimise toward qualified conversations and measured revenue — with your CRM, not the ad platform, as the source of truth.</p>
        <ul class="pill-grid reveal" style="justify-content:center;margin-top:26px">
          ${hub.campaignTypes.map((t) => `<li class="pill pill--sm">${t}</li>`).join("\n          ")}
        </ul>
      </div>
    </section>`,
    includedSection(hub.measurement, "The measurement layer"),
    proofSection("Performance Marketing"),
    miniFaq([
      ["Which platform should my business start with?", "Wherever your buyers show intent first. Existing demand goes to search (Google, Microsoft); demand creation goes to social (Meta, TikTok, LinkedIn). The discovery call answers this for your specific case — before any budget moves."],
      ["Do you work alongside in-house teams?", "Yes. Strategy with your team executing, or full hands-on management — both work. Either way your team keeps access to everything and learns as we go."],
      ["How do you report performance?", "A monthly report built on revenue metrics: qualified leads, CAC, ROAS, and pipeline — pulled from your CRM and analytics, not screenshots of ad dashboards."],
      ["Can you audit my current campaigns first?", "That's the recommended starting point. A paid audit gives you a prioritised fix list you can execute with me or without me — no lock-in either way."],
    ], "perf"),
    ctaBand({ source: "performance-marketing" }),
  ].join("\n");
  return P.page({ path: hub.file, title: hub.metaTitle, description: hub.metaDesc, active: "perf", schema: [breadcrumbSchema(crumbs, hub.file)], content });
}

/* ---------- dev hub ---------- */
function devHubPage() {
  const hub = S.DEV_HUB;
  const crumbs = [["index.html", "Home"], [null, "Development"]];
  const devServices = S.SERVICES.filter((s) => s.group === "dev");
  const content = [
    pageHero({ crumbs, label: "Website Development", h1: hub.h1, lead: hub.hero, cta: true, ctaSource: "development" }),
    `    <section class="section" aria-labelledby="dev-platforms-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Platforms</span>
          <h2 id="dev-platforms-title" class="reveal">Built on the platform your business actually needs</h2>
          <p class="reveal">Platform choice follows the business case — catalogue size, team skills, integrations, and budget.</p>
        </div>
        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
          ${devServices.map((s, i) => `<article class="card hover-glow tilt reveal" data-tilt="4" data-delay="${(i % 3) * 70}">
            <span class="card__icon">${icon("web-development")}</span>
            <h3 style="font-size:1.2rem">${s.name}</h3>
            <p style="font-size:0.94rem">${s.hero.split(". ")[0]}.</p>
            <a class="text-link" href="${s.file}">Explore ${s.name.toLowerCase()} ${icon("arrow-right", "icon-sm")}</a>
          </article>`).join("\n          ")}
          <article class="card hover-glow reveal">
            <span class="card__icon">${icon("funnel")}</span>
            <h3 style="font-size:1.2rem">Landing Pages &amp; Funnels</h3>
            <p style="font-size:0.94rem">Campaign-specific pages and funnel systems, built for message match and measurement.</p>
          </article>
        </div>
      </div>
    </section>`,
    `    <section class="section" aria-labelledby="asset-title" style="background:var(--sky-bg)">
      <div class="container container--narrow">
        <span class="eyebrow">The principle</span>
        <h2 id="asset-title" class="reveal">A website is a business asset, not a digital brochure</h2>
        <p class="reveal" style="margin-top:18px;color:var(--gray-med)">A brochure describes you. An asset produces for you. The difference is structural: pages built around buying decisions, forms that qualify, tracking that attributes revenue, and load times that don't tax your ad spend.</p>
        <p class="reveal" style="margin-top:18px;color:var(--gray-med)">Because I also run the campaigns that send traffic, nothing gets built that can't convert it. The site and the marketing are one system, designed together.</p>
      </div>
    </section>`,
    proofSection("Website Development"),
    miniFaq([
      ["Which platform is right for my business?", "Shopify for serious e-commerce, WordPress for content depth and ownership, Webflow for design-led marketing sites, Wix Studio for fast premium service-business sites, custom for conversion-critical builds. The honest recommendation comes after understanding your team and roadmap."],
      ["Do you redesign existing sites or only build new ones?", "Both — and sometimes the answer is a focused conversion fix rather than a full rebuild. An audit tells us which."],
      ["What does a typical build cost and take?", "Scope drives both, but most builds land between two and six weeks. You get a fixed quote after discovery — no hourly surprises."],
      ["Will my site be built to run marketing on?", "Yes — that's the point. Tracking, landing page structure, and CRO foundations are part of the build, not an add-on later."],
    ], "dev"),
    ctaBand({ source: "development" }),
  ].join("\n");
  return P.page({ path: hub.file, title: hub.metaTitle, description: hub.metaDesc, active: "dev", schema: [breadcrumbSchema(crumbs, hub.file)], content });
}

/* ---------- services overview ---------- */
function servicesPage() {
  const crumbs = [["index.html", "Home"], [null, "Services"]];
  const pillarBlock = (id, num, label, title, copy, list, ic, rev) => `    <section class="section" id="${id}" aria-labelledby="${id}-t"${num % 2 ? ' style="background:var(--sky-bg)"' : ""}>
      <div class="container split${rev ? " split--rev" : ""}">
        <div class="split__content">
          <span class="eyebrow">Pillar 0${num} · ${label}</span>
          <h2 id="${id}-t" class="reveal">${title}</h2>
          <p class="reveal">${copy}</p>
        </div>
        <div class="split__media">
          <ul class="cap-list card ${rev ? "reveal-l" : "reveal-r"}" style="padding:30px">
            ${list.map((i) => `<li>${icon("check", "icon-sm")} ${i}</li>`).join("\n            ")}
          </ul>
        </div>
      </div>
    </section>`;
  const content = [
    pageHero({ crumbs, label: "Services", h1: "Four disciplines. One revenue engine.", lead: "Strategy, performance marketing, AI automation, and website development — designed to work as one machine, available as one engagement or separately.", cta: true, ctaSource: "services" }),
    pillarBlock("brand-strategy", 1, "Brand Strategy", "Strategy before spend", "Positioning, messaging, and offers built on customer psychology — the thinking layer every campaign stands on. Deliverables are working documents, not decoration.", ["Positioning & messaging", "Customer psychology & market research", "Competitor analysis", "Offer creation & pricing", "Customer journey & funnel planning", "Product launch & sales strategy"], "strategy", false),
    pillarBlock("performance-marketing", 2, "Performance Marketing", "Qualified demand, measured to revenue", "Google, Meta, LinkedIn, TikTok, Snapchat, Microsoft, and Amazon — with one explicit bias: lead quality over lead volume. Your CRM is the scoreboard.", ["Search, Shopping & Performance Max", "Paid social & lead generation", "Remarketing & full-funnel sequencing", "GA4, GTM & server-side tracking", "CRO & landing pages", "CRM integration & email marketing"], "performance-marketing", true),
    pillarBlock("ai-automation", 3, "AI Automation", "The hours you stop losing", "Practical business automation — not experiments. Leads scored and routed in minutes, follow-ups that send themselves, and reports that build themselves every Monday.", ["CRM automation & lead scoring", "Sales pipeline automation", "AI assistants for sales & support", "WhatsApp automation", "Workflow automation", "Automated reporting systems"], "ai-automation", false),
    pillarBlock("website-development", 4, "Website Development", "Websites that earn their keep", "Shopify, WordPress, Wix Studio, Webflow, and custom builds — every one an asset measured in enquiries and orders, with tracking and conversion structure built in.", ["Conversion-first design & build", "Performance engineering (Core Web Vitals)", "SEO architecture & schema", "Analytics & server-side tracking", "Landing pages & funnels", "Documentation & full ownership"], "web-development", true),
    miniFaq([
      ["Can I engage one pillar without the others?", "Yes. Many clients start with a single need — an ad account rescue, a website build — and expand once the first engagement proves out."],
      ["What does an engagement typically look like?", "Discovery call, one week of research, then a scoped proposal: fixed-fee for projects, monthly for ongoing management. Everything stays in your ownership."],
      ["Who does the actual work?", "I do. There's no account-manager layer or outsourced pod — you work directly with the person responsible for the result."],
      ["How do you measure success?", "Revenue metrics agreed up front: qualified leads, CAC, ROAS, pipeline, or sales — depending on the engagement."],
    ], "svc"),
    ctaBand({ source: "services" }),
  ].join("\n");
  return P.page({ path: "services.html", title: "Services — Brand Strategy, Performance Marketing, AI Automation, Development | Sushant Rana", description: "Business growth services built as one revenue system: brand strategy, performance marketing, AI automation, and website development.", active: "services", schema: [breadcrumbSchema(crumbs, "services.html")], content });
}

/* ---------- case studies ---------- */
function caseStudiesPage() {
  const crumbs = [["index.html", "Home"], [null, "Case Studies"]];
  const content = [
    pageHero({ crumbs, label: "Case Studies", h1: "Problems, strategies, and measured results.", lead: "Nine engagements across nine industries — each following the same arc: understand the buyer, fix the system, measure to revenue." }),
    `    <section class="section" aria-label="Case study list">
      <div class="container">
        <div data-filter-group>
          <div class="filter-chips" role="group" aria-label="Filter case studies">
            <button type="button" class="filter-chip" data-filter="all" aria-pressed="true">All</button>
            <button type="button" class="filter-chip" data-filter="performance" aria-pressed="false">Performance</button>
            <button type="button" class="filter-chip" data-filter="automation" aria-pressed="false">Automation</button>
            <button type="button" class="filter-chip" data-filter="web" aria-pressed="false">Web</button>
          </div>
          <div class="grid cs-grid">
            ${D.CASE_STUDIES.map((cs, i) => `<article class="card cs-card hover-glow reveal" data-cat="${cs.tags}" data-delay="${(i % 3) * 70}">
              <p class="cs-card__industry">${cs.industry}</p>
              <h3>${cs.title}</h3>
              <dl>
                <div><dt>Problem</dt><dd>${cs.problem}</dd></div>
                <div><dt>Strategy</dt><dd>${cs.strategy}</dd></div>
                <div><dt>Execution</dt><dd>${cs.execution}</dd></div>
              </dl>
              <p class="cs-card__result">${icon("growth-chart", "icon-sm")} ${cs.results}</p>
            </article>`).join("\n            ")}
          </div>
        </div>
      </div>
    </section>`,
    ctaBand({ headline: "Your industry could be the tenth.", copy: "The first step is a 30-minute conversation about where your growth is leaking.", source: "case-studies" }),
  ].join("\n");
  return P.page({ path: "case-studies.html", title: "Case Studies | Sushant Rana — Business Growth Consultant", description: "Business growth case studies across healthcare, manufacturing, SaaS, education, real estate, and D2C — problem, strategy, execution, and results.", active: "cases", schema: [breadcrumbSchema(crumbs, "case-studies.html")], content });
}

/* ---------- blog ---------- */
function blogPage() {
  const crumbs = [["index.html", "Home"], [null, "Blog"]];
  const cats = [["all", "All"], ["marketing", "Marketing"], ["ai", "AI"], ["strategy", "Business Strategy"], ["automation", "Automation"], ["case-studies", "Case Studies"]];
  const content = [
    pageHero({ crumbs, label: "Blog", h1: "Thinking you can take to work.", lead: "Essays on revenue systems, performance marketing, and practical AI — written from client work, not theory." }),
    `    <section class="section" style="padding-top:24px" aria-label="Articles">
      <div class="container">
        <div data-filter-group>
          <div class="filter-chips" role="group" aria-label="Filter articles by category">
            ${cats.map(([key, label], i) => `<button type="button" class="filter-chip" data-filter="${key}" aria-pressed="${i === 0 ? "true" : "false"}">${label}</button>`).join("\n            ")}
          </div>
          <div class="grid blog-grid">
            ${D.BLOG_POSTS.map((post, i) => `<article class="blog-card hover-glow reveal" data-cat="${post.cat}" data-delay="${(i % 3) * 70}">
              <a class="blog-card__media" href="blog-post.html" tabindex="-1" aria-hidden="true"><img src="assets/img/${post.img}" alt="" width="800" height="500" loading="lazy"></a>
              <div class="blog-card__body">
                <p class="blog-card__meta"><span>${post.category}</span><span>·</span><time datetime="${post.date}">${post.dateLabel}</time></p>
                <h3><a href="blog-post.html">${post.title}</a></h3>
                <p>${post.excerpt}</p>
                <a class="text-link" href="blog-post.html">Read article ${icon("arrow-right", "icon-sm")}</a>
              </div>
            </article>`).join("\n            ")}
          </div>
        </div>
      </div>
    </section>`,
    ctaBand({ source: "blog" }),
  ].join("\n");
  return P.page({ path: "blog.html", title: "Blog — Marketing, AI & Business Strategy | Sushant Rana", description: "Articles on revenue systems, performance marketing, AI automation, and business strategy from consultant Sushant Rana.", active: "blog", schema: [breadcrumbSchema(crumbs, "blog.html")], content });
}

/* ---------- blog post ---------- */
function blogPostPage() {
  const post = D.BLOG_POSTS[0];
  const crumbs = [["index.html", "Home"], ["blog.html", "Blog"], [null, "Revenue Systems vs Marketing Campaigns"]];
  const schema = [
    breadcrumbSchema(crumbs, "blog-post.html"),
    { "@context": "https://schema.org", "@type": "BlogPosting", headline: post.title, description: post.excerpt, datePublished: post.date, author: { "@type": "Person", name: "Sushant Rana", jobTitle: "Business Growth Consultant" }, image: SITE.base + "/assets/img/" + post.img, mainEntityOfPage: SITE.base + "/blog-post.html" },
  ];
  const content = `    <article>
      <header class="page-hero article-hero">
        <div class="deco-grid" aria-hidden="true"></div>
        <div class="container" style="max-width:840px;position:relative;z-index:1">
          ${breadcrumbs(crumbs)}
          <span class="eyebrow">${post.category}</span>
          <h1 class="reveal" style="font-size:clamp(2rem,4vw,3.2rem)">Revenue Systems vs Marketing Campaigns: Why One Compounds and the Other Expires</h1>
          <p class="article__meta"><span>By Sushant Rana</span><span>·</span><time datetime="${post.date}">${post.dateLabel}</time><span>·</span><span>${post.read} read</span></p>
        </div>
      </header>
      <div class="section" style="padding-top:40px">
        <div class="container" style="max-width:840px">
          <div class="article">
            <p class="lead">Two businesses spend the same budget on the same platform. One grows every quarter. The other renegotiates with a new agency every six months. The difference is rarely the ads. It's what the ads are plugged into.</p>
            <h2>Campaigns are events. Systems are infrastructure.</h2>
            <p>A campaign has a start date, an end date, and a budget that disappears when it stops. It can be brilliant and still leave nothing behind. A revenue system is different: positioning, offer, traffic, conversion, follow-up, and retention — connected, measured, and owned by the business.</p>
            <p>When a campaign ends, its learnings evaporate into a slide deck. When a system runs, every month of data makes the next month cheaper: better negative keywords, sharper messaging, cleaner lead scoring, higher repeat rates.</p>
            <blockquote>A campaign buys you a month of growth. A system builds you a machine that produces it.</blockquote>
            <h2>The five components campaigns borrow but never build</h2>
            <p>Every high-performing campaign quietly depends on assets that outlast it. If nobody builds them deliberately, every campaign starts from zero.</p>
            <ul>
              <li><strong>Positioning</strong> — a defensible answer to "why you", so ads never compete on price alone.</li>
              <li><strong>Offer architecture</strong> — entry points matched to buying readiness.</li>
              <li><strong>Conversion infrastructure</strong> — landing pages and forms that answer objections and qualify intent.</li>
              <li><strong>Follow-up automation</strong> — because the fastest responder wins deals the best advertiser loses.</li>
              <li><strong>Measurement</strong> — revenue attribution your finance team would sign, not platform-reported conversions.</li>
            </ul>
            <h2>What to do with this</h2>
            <p>Before the next campaign brief, audit the system it plugs into. Three questions expose most gaps:</p>
            <ol>
              <li>If we paused all ads today, what would keep producing leads next month?</li>
              <li>What happens — precisely, minute by minute — after someone submits a form?</li>
              <li>Which number would our CFO accept as proof marketing made money?</li>
            </ol>
            <p>If any answer is "nothing", "not sure", or "clicks" — the budget's biggest opportunity isn't a new campaign. It's the system underneath.</p>
          </div>
          <div style="margin-top:56px">
            ${ctaBand({ id: "post-cta", source: "blog-post", headline: "Want this diagnosis run on your business?", copy: "The 30-minute consultation covers exactly these questions." }).replace('<section class="section" aria-labelledby="post-cta-title">', '<div>').replace("</section>", "</div>")}
          </div>
        </div>
      </div>
    </article>`;
  return P.page({ path: "blog-post.html", title: post.title + " | Sushant Rana", description: post.excerpt, active: "blog", ogType: "article", schema, content });
}

/* ---------- contact ---------- */
function contactPage() {
  const crumbs = [["index.html", "Home"], [null, "Contact"]];
  const content = [
    pageHero({ crumbs, label: "Contact", h1: "Let’s talk about your growth.", lead: "One conversation is enough to know whether I can help. Book the free consultation, or reach out directly." }),
    `    <section class="section" style="padding-top:24px" aria-label="Contact options">
      <div class="container">
        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">
          <div class="card hover-glow reveal">
            <span class="card__icon">${icon("calendar")}</span>
            <h3>Book a consultation</h3>
            <p>A free 30-minute call. You talk, I ask questions, and you leave with an honest read on your growth gaps.</p>
            <a class="btn btn--primary" href="consultation.html" data-popup-open data-cta="contact-card">Book Free Consultation</a>
          </div>
          <div class="card hover-glow reveal" data-delay="70">
            <span class="card__icon">${icon("email")}</span>
            <h3>Email</h3>
            <p>For proposals, partnerships, or anything that needs a paper trail.</p>
            <!-- REPLACE: confirm public contact email -->
            <a class="text-link" href="mailto:me@sushantrana.com">me@sushantrana.com ${icon("arrow-right", "icon-sm")}</a>
          </div>
          <div class="card hover-glow reveal" data-delay="140">
            <span class="card__icon">${icon("clock")}</span>
            <h3>Response time</h3>
            <p>Consultation requests get a personal reply within one business day, with proposed call times.</p>
          </div>
        </div>
      </div>
    </section>`,
    ctaBand({ headline: "The fastest route is the consultation call.", copy: "Every enquiry is reviewed personally — tell me about the business, and I'll come prepared.", source: "contact" }),
  ].join("\n");
  return P.page({ path: "contact.html", title: "Contact | Sushant Rana — Business Growth Consultant", description: "Contact Sushant Rana — book a free 30-minute business growth consultation or reach out directly by email.", active: "contact", schema: [breadcrumbSchema(crumbs, "contact.html")], content });
}

/* ---------- consultation (standalone) ---------- */
function consultationPage() {
  const serviceOptions = ["Brand Consulting", "Performance Marketing", "Google Ads", "Meta Ads", "TikTok Ads", "LinkedIn Ads", "AI Automation", "CRM Automation", "Shopify Development", "WordPress Development", "Wix Studio Development", "Webflow Development", "Custom Development", "Complete Business Growth Strategy"];
  const content = `    <section class="landing-hero" aria-labelledby="page-title">
      <div class="blob hero__blob hero__blob--a" aria-hidden="true" style="opacity:.14"></div>
      <div class="deco-grid" aria-hidden="true"></div>
      <div class="container split" style="align-items:start;position:relative;z-index:1">
        <div class="split__content">
          <span class="eyebrow"><span class="pulse-dot" aria-hidden="true"></span> Free business consultancy</span>
          <h1 id="page-title" class="reveal" style="font-size:clamp(2rem,4.2vw,3.3rem)">Not getting enough leads? Book a 30–60 minute business consultancy session.</h1>
          <p class="lead reveal">No pitch, no obligation. We go through your business, your marketing, and your numbers — and you leave with a clear picture of what's blocking growth and what to fix first.</p>
          <ul class="cap-list reveal" style="margin-top:30px">
            <li>${icon("check", "icon-sm")} Personal review of your website and marketing before the call</li>
            <li>${icon("check", "icon-sm")} Honest assessment — including “you don’t need me yet”</li>
            <li>${icon("check", "icon-sm")} A prioritised list of growth gaps you keep either way</li>
            <li>${icon("check", "icon-sm")} Reply within one business day</li>
          </ul>
        </div>
        <div class="split__media">
          <div class="landing-form reveal-r">
            <h2 style="font-size:1.5rem">Let’s Understand Your Business</h2>
            <p style="color:var(--gray-med);font-size:0.95rem;margin-top:8px">Tell me about your business and I’ll personally review your requirements before our consultation.</p>
            <form novalidate data-consult-form-inline>
              <div class="form-grid-2">
                <div class="field"><label for="c-name">Full Name <span class="req" aria-hidden="true">*</span></label><input type="text" id="c-name" name="fullName" autocomplete="name" required><p class="field__error" aria-live="polite"></p></div>
                <div class="field"><label for="c-email">Business Email <span class="req" aria-hidden="true">*</span></label><input type="email" id="c-email" name="email" autocomplete="email" required><p class="field__error" aria-live="polite"></p></div>
                <div class="field"><label for="c-phone">Phone Number <span class="req" aria-hidden="true">*</span></label><input type="tel" id="c-phone" name="phone" autocomplete="tel" inputmode="tel" required><p class="field__error" aria-live="polite"></p></div>
                <div class="field"><label for="c-company">Company Name</label><input type="text" id="c-company" name="company" autocomplete="organization"><p class="field__error" aria-live="polite"></p></div>
                <div class="field field--full"><label for="c-website">Website</label><input type="url" id="c-website" name="website" autocomplete="url" placeholder="https://"><p class="field__error" aria-live="polite"></p></div>
                <div class="field field--full"><label for="c-service">Services Required <span class="req" aria-hidden="true">*</span></label><select id="c-service" name="service" required><option value="">Select a service</option>${serviceOptions.map((s) => `<option value="${s}">${s}</option>`).join("")}</select><p class="field__error" aria-live="polite"></p></div>
                <div class="field field--full"><label for="c-challenge">Biggest Business Challenge <span class="req" aria-hidden="true">*</span></label><textarea id="c-challenge" name="challenge" rows="4" required placeholder="Describe your biggest challenge, your current marketing efforts, and what you want to achieve."></textarea><p class="field__error" aria-live="polite"></p></div>
              </div>
              <input type="hidden" name="source" value="consultation.html" data-source-field>
              <button type="submit" class="btn btn--primary btn--lg">Book Free Consultation</button>
              <p class="form-note">Your details are used only to prepare for the consultation. No newsletters, no lists.</p>
            </form>
          </div>
        </div>
      </div>
    </section>`;
  return P.page({ path: "consultation.html", title: "Book a Free Business Consultancy Session | Sushant Rana", description: "Not getting enough leads? Book a free 30–60 minute business consultancy session with Sushant Rana — strategy, marketing, and automation reviewed personally.", minimalChrome: true, schema: [], content });
}

/* ---------- thank you ---------- */
function thankYouPage() {
  const content = `    <section class="page-hero" aria-labelledby="page-title" style="padding-bottom:0">
      <div class="deco-grid" aria-hidden="true"></div>
      <div class="container" style="text-align:center;max-width:760px;position:relative;z-index:1">
        <span class="eyebrow" style="margin-inline:auto"><span class="pulse-dot" aria-hidden="true"></span> Request received</span>
        <h1 id="page-title" class="reveal">Thank you. Your request is in.</h1>
        <p class="lead reveal">Your consultation request has been received and will be reviewed personally — not by an autoresponder.</p>
      </div>
    </section>
    <section class="section" aria-labelledby="next-title">
      <div class="container" style="max-width:960px">
        <h2 id="next-title" class="section-head section-head--center reveal" style="margin-bottom:40px">What happens next</h2>
        <div class="grid steps-grid">
          <div class="step-card reveal"><h3 style="font-size:1.1rem;margin-bottom:6px">Personal review</h3><p style="font-size:0.95rem;color:var(--gray-med)">I read your submission and take a first look at your website and marketing before we ever speak.</p></div>
          <div class="step-card reveal" data-delay="80"><h3 style="font-size:1.1rem;margin-bottom:6px">Scheduling email</h3><p style="font-size:0.95rem;color:var(--gray-med)">Within one business day you'll receive a reply with proposed times for your 30–60 minute session.</p></div>
          <div class="step-card reveal" data-delay="160"><h3 style="font-size:1.1rem;margin-bottom:6px">The consultation</h3><p style="font-size:0.95rem;color:var(--gray-med)">We go through your business and growth gaps together. You keep the findings whether or not we work together.</p></div>
        </div>
        <p style="text-align:center;margin:44px auto 0;color:var(--gray-med)">Expected response time: <strong style="color:var(--ink)">within one business day</strong>.</p>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:28px">
          <a class="btn btn--ghost" href="blog.html">Read the blog ${icon("arrow-right", "icon-sm")}</a>
          <a class="btn btn--ghost" href="case-studies.html">Browse case studies ${icon("arrow-right", "icon-sm")}</a>
        </div>
      </div>
    </section>`;
  return P.page({ path: "thank-you.html", title: "Thank You — Request Received | Sushant Rana", description: "Your consultation request has been received. Here's what happens next.", noindex: true, schema: [], content });
}

/* ---------- legal ---------- */
function legalPage(file, title, heading, body) {
  const crumbs = [["index.html", "Home"], [null, heading]];
  const content = [
    pageHero({ crumbs, label: "Legal", h1: heading, lead: "Last updated: 1 July 2026 <!-- REPLACE: confirm date and have this document reviewed by counsel -->" }),
    `    <section class="section" style="padding-top:24px">
      <div class="container">
        <div class="card" style="padding:clamp(28px,5vw,52px)">
          <div class="prose">
${body}
          </div>
        </div>
      </div>
    </section>`,
  ].join("\n");
  return P.page({ path: file, title, description: heading + " for sushantrana.com — how this website handles your information.", schema: [breadcrumbSchema(crumbs, file)], content });
}

const PRIVACY_BODY = `            <p>This policy explains what information this website collects, how it is used, and the choices you have.</p>
            <h2>Information collected</h2>
            <p>When you submit the consultation form, you provide: name, business email, phone number, company name, website, the service you're interested in, and a description of your business challenge. This information is used solely to review your request and conduct the consultation.</p>
            <h2>Analytics</h2>
            <p>This site may use analytics tools (such as Google Analytics 4 and Microsoft Clarity) to understand how visitors use it. This data is aggregated and does not identify you personally. <!-- REPLACE: confirm the final analytics stack and cookie usage --></p>
            <h2>How information is used</h2>
            <ul><li>To respond to consultation requests and prepare for calls.</li><li>To improve the website and its content.</li><li>Never sold, rented, or shared with third parties for their marketing.</li></ul>
            <h2>Data retention</h2>
            <p>Consultation submissions are retained for as long as needed to serve the enquiry and any resulting engagement, after which they are deleted on request or per standard retention practice.</p>
            <h2>Your rights</h2>
            <p>You may request a copy of the personal data held about you, ask for it to be corrected, or ask for it to be deleted. Email <a href="mailto:me@sushantrana.com">me@sushantrana.com</a> <!-- REPLACE: confirm contact email --> and the request will be honoured within 30 days.</p>
            <h2>Third-party services</h2>
            <p>Form submissions are processed by a form-handling service; fonts are served by Google Fonts. <!-- REPLACE: list final providers once the form endpoint is wired --></p>
            <h2>Changes to this policy</h2>
            <p>Material changes will be reflected on this page with an updated date above.</p>`;

const TERMS_BODY = `            <p>These terms govern your use of this website. By using the site, you accept them.</p>
            <h2>Use of this website</h2>
            <p>Content on this site is provided for general information about consulting services. It does not constitute professional advice for your specific situation until an engagement is agreed in writing.</p>
            <h2>Consultations</h2>
            <p>The free consultation is a scoping conversation. It creates no obligation on either side, and no client relationship exists until a written proposal is accepted.</p>
            <h2>Intellectual property</h2>
            <p>All content on this site — text, design, and graphics — belongs to Sushant Rana unless otherwise noted. You may not reproduce it commercially without written permission.</p>
            <h2>Case studies and results</h2>
            <p>Results described on this site reflect specific client situations. They are illustrations, not promises — outcomes depend on market, budget, execution, and factors outside any consultant's control.</p>
            <h2>Limitation of liability</h2>
            <p>This website is provided "as is". To the maximum extent permitted by law, Sushant Rana is not liable for damages arising from use of this site or reliance on its content.</p>
            <h2>Governing law</h2>
            <p>These terms are governed by the laws of India. <!-- REPLACE: confirm governing jurisdiction with counsel --></p>
            <h2>Contact</h2>
            <p>Questions about these terms: <a href="mailto:me@sushantrana.com">me@sushantrana.com</a> <!-- REPLACE: confirm contact email --></p>`;

/* ---------- 404 ---------- */
function notFoundPage() {
  const content = `    <section class="error-hero" aria-labelledby="page-title">
      <div class="deco-grid" aria-hidden="true"></div>
      <div class="container" style="position:relative;z-index:1">
        <p class="error-code" aria-hidden="true">404</p>
        <h1 id="page-title" style="font-size:clamp(1.8rem,3.5vw,2.6rem)">This page doesn’t exist — but your growth plan can.</h1>
        <p class="lead" style="margin-inline:auto">The link is broken or the page has moved. Here’s the way back.</p>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:16px">
          <a class="btn btn--primary" href="index.html">Back to home</a>
          <a class="btn btn--ghost" href="consultation.html" data-popup-open data-cta="404">Book Free Consultation</a>
        </div>
      </div>
    </section>`;
  return P.page({ path: "404.html", title: "Page Not Found | Sushant Rana", description: "The page you're looking for doesn't exist.", noindex: true, schema: [], content });
}

module.exports = { servicePage, perfHubPage, devHubPage, servicesPage, caseStudiesPage, blogPage, blogPostPage, contactPage, consultationPage, thankYouPage, legalPage, PRIVACY_BODY, TERMS_BODY, notFoundPage };
