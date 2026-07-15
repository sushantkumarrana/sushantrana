/* index.html — interactive homepage. House of Web design, SEO-Discovery IA. */
"use strict";

const { icon, ctaBand, SITE } = require("./partials");
const D = require("./data");

function statTile(s, i) {
  const attrs = `data-count="${s.value}"` + (s.decimals ? ` data-decimals="${s.decimals}"` : "") + (s.comma ? ' data-format="comma"' : "");
  return `<div class="stat reveal" data-delay="${(i % 4) * 70}">
            <!-- REPLACE: client-verified metric -->
            <span class="stat__value">${s.prefix || ""}<span ${attrs}>0</span>${s.suffix || ""}</span>
            <span class="stat__label">${s.label}</span>
          </div>`;
}

function csCard(cs, i) {
  return `<article class="card cs-card hover-glow reveal" data-cat="${cs.tags}" data-delay="${(i % 3) * 80}">
            <p class="cs-card__industry">${cs.industry}</p>
            <h3>${cs.title}</h3>
            <dl>
              <div><dt>Problem</dt><dd>${cs.problem}</dd></div>
              <div><dt>Strategy</dt><dd>${cs.strategy}</dd></div>
              <div><dt>Execution</dt><dd>${cs.execution}</dd></div>
            </dl>
            <p class="cs-card__result">${icon("growth-chart", "icon-sm")} ${cs.results}</p>
          </article>`;
}

function blogCard(post, i) {
  return `<article class="blog-card hover-glow reveal" data-delay="${(i % 3) * 80}">
            <a class="blog-card__media" href="blog-post.html" tabindex="-1" aria-hidden="true">
              <img src="assets/img/${post.img}" alt="" width="800" height="500" loading="lazy">
            </a>
            <div class="blog-card__body">
              <p class="blog-card__meta"><span>${post.category}</span><span>·</span><time datetime="${post.date}">${post.dateLabel}</time></p>
              <h3><a href="blog-post.html">${post.title}</a></h3>
              <p>${post.excerpt}</p>
              <a class="text-link" href="blog-post.html">Read article ${icon("arrow-right", "icon-sm")}</a>
            </div>
          </article>`;
}

function comparisonTable() {
  const c = D.COMPARISON;
  const cell = (v) => {
    if (v[0] === "yes") return '<span class="cmp-yes" aria-hidden="true">✔</span><span class="visually-hidden">Yes</span>';
    if (v[0] === "no") return '<span class="cmp-no" aria-hidden="true">✘</span><span class="visually-hidden">No</span>';
    return v[0];
  };
  return `<div class="cmp-scroll reveal" role="region" aria-label="How I compare" tabindex="0">
          <table class="cmp-table">
            <thead><tr><th scope="col">What you get</th>
              <th scope="col" class="cmp-us">${c.cols[0]}</th>
              <th scope="col">${c.cols[1]}</th>
              <th scope="col">${c.cols[2]}</th></tr></thead>
            <tbody>
              ${c.rows.map((r) => `<tr><th scope="row">${r[0]}</th>
                <td class="cmp-us">${cell(r[1])}</td>
                <td>${cell(r[2])}</td>
                <td>${cell(r[3])}</td></tr>`).join("\n              ")}
            </tbody>
          </table>
        </div>`;
}

function faqBlock() {
  return `<div data-faq>
          <div class="faq-cats filter-chips" role="group" aria-label="Filter questions by topic">
            ${D.FAQ_CATS.map(([k, l], i) => `<button type="button" class="filter-chip" data-cat="${k}" aria-pressed="${i === 0 ? "true" : "false"}">${l}</button>`).join("\n            ")}
          </div>
          <div class="acc" data-acc-single>
            ${D.HOME_FAQ.map(([cat, q, a], i) => `<div class="acc-item" data-acc-cat="${cat}">
              <button type="button" class="acc-trigger" aria-expanded="false" aria-controls="faq-${i}">
                <span>${q}</span>${icon("plus", "acc-icon")}
              </button>
              <div class="acc-panel" id="faq-${i}"><p class="acc-body">${a}</p></div>
            </div>`).join("\n            ")}
          </div>
        </div>`;
}

function homeContent() {
  return `
    <!-- ============ 1. HERO (rotating questions) ============ -->
    <section class="hero" aria-labelledby="hero-heading">
      <div class="blob hero__blob hero__blob--a" aria-hidden="true"></div>
      <div class="blob hero__blob hero__blob--b" aria-hidden="true"></div>
      <div class="deco-grid" aria-hidden="true"></div>
      <div class="container hero__inner">
        <div class="hero__copy">
          <span class="eyebrow eyebrow--plain"><span class="pulse-dot" aria-hidden="true"></span> Business Growth Consultant · 8+ years</span>
          <h1 id="hero-heading" class="hero__headline">
            <span class="hero__rotator">
              <span class="hero__question is-active">Why aren’t you getting enough leads?</span>
            </span>
            <span class="hero__answer">Because you have marketing campaigns — <span class="hero__answer-accent">not a revenue system.</span></span>
          </h1>
          <p class="hero__sub">I build revenue systems, not just marketing campaigns — strategy, performance marketing, and AI automation working as one engine.</p>
          <div class="hero__cta-row">
            <a class="btn btn--primary btn--lg" href="consultation.html" data-popup-open data-cta="hero">Book Free Consultation ${icon("arrow-right", "icon-sm")}</a>
          </div>
          <div class="hero__trust">
            <span>8+ yrs</span><span class="sep">•</span>
            <span><strong>₹50L+</strong> ad spend managed</span><span class="sep">•</span>
            <span>4 countries</span><span class="sep">•</span>
            <span><strong>11.2×</strong> ROAS</span>
          </div>
        </div>
        <div class="hero__stats" aria-label="Key results">
          <!-- REPLACE: client-verified metrics -->
          <article class="hero-stat hero-stat--1"><p class="hero-stat__value">11.2×</p><p class="hero-stat__label">Best B2B ROAS</p></article>
          <article class="hero-stat hero-stat--2"><p class="hero-stat__value">₹50L+</p><p class="hero-stat__label">Ad spend managed</p></article>
          <article class="hero-stat hero-stat--3"><p class="hero-stat__value">4</p><p class="hero-stat__label">Countries served</p></article>
          <article class="hero-stat hero-stat--4"><p class="hero-stat__value">AI</p><p class="hero-stat__label">Automations shipped</p></article>
        </div>
      </div>
      <a href="#stats" class="scroll-cue" aria-label="Scroll to explore">Scroll to explore ${icon("chevron-down", "icon-sm")}</a>
    </section>

    <!-- ============ 2. STATS BAR ============ -->
    <section class="section section--tight" id="stats" aria-label="Results in numbers">
      <div class="container">
        <div class="stat-grid">
          ${D.STATS.map(statTile).join("\n          ")}
        </div>
      </div>
    </section>

    <!-- ============ 3. THE REALITY (before/after slider) ============ -->
    <section class="section" aria-labelledby="reality-title">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow"><span class="pulse-dot" aria-hidden="true"></span> The reality of growth</span>
          <h2 id="reality-title" class="reveal">Most businesses don’t have a marketing problem.<br>They have a <span class="text-accent">systems</span> problem.</h2>
          <p class="reveal">Campaigns generate spikes. Systems generate compounding revenue. Drag the handle to see the gap I close.</p>
        </div>
        <div class="compare reveal-scale" data-tabs>
          <div class="compare__switch" role="tablist" aria-label="Compare the two approaches">
            <button class="compare__opt compare__opt--old" role="tab" data-tab="old">The scattered way</button>
            <button class="compare__opt compare__opt--new" role="tab" data-tab="new">The revenue system</button>
          </div>
          <div class="tab-body">
            <div class="tab-panel" role="tabpanel" data-panel="old">
              <div class="compare__card compare__card--old">
                <p class="compare__tag">Scattered campaigns</p>
                <ul class="compare__list">
                  <li>Disconnected tactics, restarted every quarter</li>
                  <li>Leads that leak between marketing and sales</li>
                  <li>Guesswork reporting and vanity metrics</li>
                  <li>Spikes that reset the moment spend stops</li>
                </ul>
              </div>
            </div>
            <div class="tab-panel is-hidden" hidden role="tabpanel" data-panel="new">
              <div class="compare__card compare__card--new">
                <p class="compare__tag">A connected revenue system</p>
                <ul class="compare__list">
                  <li>One engine: positioning → traffic → conversion → follow-up</li>
                  <li>Tracked, scored pipelines — no leads leaking</li>
                  <li>Reporting you can act on, every week</li>
                  <li>Growth that compounds month over month</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ 4. WHO I HELP (industry tabs) ============ -->
    <section class="section" aria-labelledby="industries-title" style="background:var(--sky-bg)">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Who I help</span>
          <h2 id="industries-title" class="reveal">Growth systems, tuned to your industry</h2>
          <p class="reveal">The mechanics change by market. The discipline doesn’t.</p>
        </div>
        <div class="tabs reveal" data-tabs>
          <div class="tab-row" role="tablist" aria-label="Industries">
            ${D.INDUSTRY_TABS.map(([k, label]) => `<button class="pill-tab" role="tab" data-tab="${k}">${label}</button>`).join("\n            ")}
          </div>
          <div class="tab-body">
            ${D.INDUSTRY_TABS.map(([k, label, ctx, levers], idx) => `<div class="tab-panel${idx ? " is-hidden" : ""}"${idx ? " hidden" : ""} role="tabpanel" data-panel="${k}">
              <div class="card" style="border-radius:var(--r-card)">
                <h3>${label}</h3>
                <p style="color:var(--gray-med)">${ctx}</p>
                <ul class="cap-list" style="margin-top:8px">
                  ${levers.map((lv) => `<li>${icon("check", "icon-sm")} ${lv}</li>`).join("\n                  ")}
                </ul>
              </div>
            </div>`).join("\n            ")}
          </div>
        </div>
      </div>
    </section>

    <!-- ============ 5. SERVICES (tilt cards) ============ -->
    <section class="section" aria-labelledby="services-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">What I do</span>
          <h2 id="services-title" class="reveal">Four disciplines. One revenue engine.</h2>
          <p class="reveal">Most consultants sell one of these. Growth needs them working together.</p>
        </div>
        <div class="grid pillar-grid">
          ${D.PILLARS.map(([ic, t, p, href], i) => `<article class="card hover-glow tilt reveal" data-tilt="4" data-delay="${(i % 4) * 70}">
            <span class="card__icon">${icon(ic)}</span>
            <h3>${t}</h3>
            <p>${p}</p>
            <a class="text-link" href="${href}">Explore ${t.split(" ")[0].toLowerCase()} ${icon("arrow-right", "icon-sm")}</a>
          </article>`).join("\n          ")}
        </div>
      </div>
    </section>

    <!-- ============ 6. HOW I WORK (timeline) ============ -->
    <section class="section" aria-labelledby="process-title" style="background:var(--sky-bg)">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">How I work</span>
          <h2 id="process-title" class="reveal">A process with no mystery in it</h2>
        </div>
        <ol class="timeline">
          ${D.PROCESS.map(([t, meta, p], i) => `<li class="timeline-step ${i % 2 ? "reveal-r" : "reveal-l"}">
            <div class="timeline-marker"><span class="timeline-num">0${i + 1}</span>${i < D.PROCESS.length - 1 ? '<span class="timeline-line"></span>' : ""}</div>
            <div class="timeline-card">
              <span class="timeline-kicker">${meta}</span>
              <h3>${t}</h3>
              <p>${p}</p>
            </div>
          </li>`).join("\n          ")}
        </ol>
      </div>
    </section>

    <!-- ============ 7. PERFORMANCE MARKETING (marquee + rank-bars) ============ -->
    <section class="section" aria-labelledby="perf-title">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">Performance marketing</span>
          <h2 id="perf-title" class="reveal">Paid channels that pay back</h2>
          <p class="reveal">Managed across the platforms your buyers actually use — with budgets tracked to the rupee and dollar. <strong>Lead quality over lead volume.</strong></p>
        </div>
      </div>
      <div class="marquee marquee-mask reveal" aria-label="Advertising platforms">
        <div class="marquee-track">
          ${[...D.PERF_PLATFORMS, ...D.PERF_PLATFORMS].map(([ic, l], i) => `<span class="marquee-chip"${i >= D.PERF_PLATFORMS.length ? ' aria-hidden="true"' : ""}>${icon(ic, "icon-sm")} ${l}</span>`).join("\n          ")}
        </div>
      </div>
      <div class="container" style="margin-top:44px">
        <div class="split">
          <div class="split__content">
            <p class="cs-card__industry">₹50L+ ad spend managed · CAD $9,000 &amp; AED 10,000 monthly budgets</p>
            <h3 style="font-size:1.6rem;margin:8px 0 16px">Where the budget goes is an output of research — not habit.</h3>
            <p style="color:var(--gray-med)">Search captures existing demand. Social creates it. Every campaign optimises toward qualified conversations and measured revenue, with your CRM as the source of truth.</p>
            <p style="margin-top:20px"><a class="text-link" href="performance-marketing.html">See the full approach ${icon("arrow-right", "icon-sm")}</a></p>
          </div>
          <div class="split__media">
            <div class="card reveal" style="padding:28px">
              <div class="rankbars">
                <!-- REPLACE: illustrative channel weighting -->
                <div class="rankbar-row"><div class="rankbar-label"><span>High-intent search</span><span>92%</span></div><div class="rankbar-track"><div class="rank-bar" style="--w:92%"></div></div></div>
                <div class="rankbar-row"><div class="rankbar-label"><span>Paid social & creative</span><span>84%</span></div><div class="rankbar-track"><div class="rank-bar" style="--w:84%"></div></div></div>
                <div class="rankbar-row"><div class="rankbar-label"><span>Retargeting & nurture</span><span>76%</span></div><div class="rankbar-track"><div class="rank-bar" style="--w:76%"></div></div></div>
                <div class="rankbar-row"><div class="rankbar-label"><span>Measurement & CRO</span><span>88%</span></div><div class="rankbar-track"><div class="rank-bar" style="--w:88%"></div></div></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ============ 8. AI AUTOMATION (live CRM board) ============ -->
    <section class="section" aria-labelledby="ai-title" style="background:var(--sky-bg)">
      <div class="container split split--rev">
        <div class="split__content">
          <span class="eyebrow">AI automation</span>
          <h2 id="ai-title" class="reveal">The work that runs while you sleep</h2>
          <p class="reveal">Automation that scores leads, moves pipelines, and reports itself — so nothing leaks between marketing and sales.</p>
          <ul class="cap-list" style="margin-top:22px">
            ${D.AI_CAPS.map((c) => `<li>${icon("check", "icon-sm")} ${c}</li>`).join("\n            ")}
          </ul>
        </div>
        <div class="split__media">
          <div class="live-panel reveal-scale" data-crm>
            <div class="live-head"><span class="pulse-dot" aria-hidden="true"></span> Lead pipeline · system demo</div>
            <div class="crm-board" style="padding:16px">
              <div class="crm-col"><h4>New</h4><div class="crm-slot"><span class="crm-card" data-crm-lead><span class="dot"></span> Inbound lead</span></div></div>
              <div class="crm-col"><h4>Scored</h4><div class="crm-slot"><span class="crm-card is-ghost"><span class="dot"></span> Qualified · 82</span></div></div>
              <div class="crm-col"><h4>Qualified</h4><div class="crm-slot"><span class="crm-card is-ghost"><span class="dot"></span> Routed to sales</span></div></div>
            </div>
            <div class="live-metrics">
              <div class="live-metric"><p class="live-value" data-crm-count>0</p><p class="live-cap">Leads processed</p></div>
              <div class="live-metric"><p class="live-value" data-live="42" data-live-jitter="3" data-live-suffix="%">42%</p><p class="live-cap">Qualified rate</p></div>
              <div class="live-metric"><p class="live-value" data-live="5" data-live-jitter="2" data-live-suffix=" min">5 min</p><p class="live-cap">Response time</p></div>
            </div>
          </div>
          <p class="form-note" style="margin-top:10px;text-align:center">Illustrative system demo — not live client data.</p>
        </div>
      </div>
    </section>

    <!-- ============ 9. CASE STUDIES (filter) ============ -->
    <section class="section" aria-labelledby="cases-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Selected results</span>
          <h2 id="cases-title" class="reveal">Fewer campaigns. Bigger outcomes.</h2>
          <p class="reveal">A sample of engagements across Australia, Canada, the USA, and India.</p>
        </div>
        <div data-filter-group>
          <div class="filter-chips" role="group" aria-label="Filter case studies">
            <button type="button" class="filter-chip" data-filter="all" aria-pressed="true">All</button>
            <button type="button" class="filter-chip" data-filter="performance" aria-pressed="false">Performance</button>
            <button type="button" class="filter-chip" data-filter="automation" aria-pressed="false">Automation</button>
            <button type="button" class="filter-chip" data-filter="web" aria-pressed="false">Web</button>
          </div>
          <div class="grid cs-grid">
            ${D.CASE_STUDIES.map(csCard).join("\n            ")}
          </div>
        </div>
        <p style="margin-top:40px;text-align:center"><a class="btn btn--ghost" href="case-studies.html">View all case studies ${icon("arrow-right", "icon-sm")}</a></p>
      </div>
    </section>

    <!-- ============ 10. WHY CLIENTS HIRE ME ============ -->
    <section class="section" aria-labelledby="why-title" style="background:var(--sky-bg)">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Why founders bring me in</span>
          <h2 id="why-title" class="reveal">One senior operator who owns the number</h2>
        </div>
        <div class="grid pillar-grid">
          ${D.WHY_HIRE.map(([ic, t, p], i) => `<article class="card hover-glow reveal" data-delay="${(i % 4) * 70}">
            <span class="card__icon">${icon(ic)}</span>
            <h3 style="font-size:1.15rem">${t}</h3>
            <p>${p}</p>
          </article>`).join("\n          ")}
        </div>
      </div>
    </section>

    <!-- ============ 11. WHAT MAKES ME DIFFERENT (comparison) ============ -->
    <section class="section" aria-labelledby="diff-title">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">What makes me different</span>
          <h2 id="diff-title" class="reveal">Built for how buyers actually decide</h2>
          <p class="reveal">Tracked pipelines, automated reporting, and one accountable operator — compared honestly.</p>
        </div>
        ${comparisonTable()}
      </div>
    </section>

    <!-- ============ 12. TESTIMONIALS (carousel) ============ -->
    <section class="section" aria-labelledby="testi-title" style="background:var(--sky-bg)">
      <div class="container container--narrow">
        <div class="section-head section-head--center">
          <span class="eyebrow">In clients’ words</span>
          <h2 id="testi-title" class="reveal">What working together feels like</h2>
        </div>
        <div class="carousel reveal" data-carousel role="group" aria-roledescription="carousel" aria-label="Client testimonials">
          <div class="carousel__track">
            ${D.QUOTES.map((q) => `<figure class="carousel__slide card quote-card">
              <span class="card__icon" aria-hidden="true">${icon("quote")}</span>
              <blockquote>“${q.quote}”</blockquote>
              <figcaption><strong>${q.name}</strong> ${q.role}</figcaption>
            </figure>`).join("\n            ")}
          </div>
          <div class="carousel__dots"></div>
        </div>
      </div>
    </section>

    <!-- ============ 13. CORE VALUES ============ -->
    <section class="section" aria-labelledby="values-title">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">Operating principles</span>
          <h2 id="values-title" class="reveal">How I work with clients</h2>
        </div>
        <div class="grid value-grid">
          ${D.VALUES.map(([ic, t, p], i) => `<article class="card hover-glow reveal" data-delay="${(i % 3) * 70}">
            <span class="card__icon">${icon(ic)}</span>
            <h3 style="font-size:1.1rem">${t}</h3>
            <p style="font-size:0.92rem">${p}</p>
          </article>`).join("\n          ")}
        </div>
      </div>
    </section>

    <!-- ============ 14. TECH STACK (marquee) ============ -->
    <section class="section section--tight" aria-labelledby="stack-title">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">Tech stack</span>
          <h2 id="stack-title" class="reveal">The tools behind the system</h2>
        </div>
      </div>
      <div class="marquee marquee-mask reveal" aria-label="Tools and platforms">
        <div class="marquee-track">
          ${[...D.TECH_STACK, ...D.TECH_STACK].map(([ic, l], i) => `<span class="marquee-chip"${i >= D.TECH_STACK.length ? ' aria-hidden="true"' : ""}>${icon(ic, "icon-sm")} ${l}</span>`).join("\n          ")}
        </div>
      </div>
    </section>

    <!-- ============ 15. GLOBAL REACH ============ -->
    <section class="section" aria-labelledby="global-title" style="background:var(--sky-bg)">
      <div class="container">
        <div class="section-head section-head--center">
          <span class="eyebrow">Where I work</span>
          <h2 id="global-title" class="reveal">Growth systems across <span class="text-accent">four</span> markets</h2>
          <p class="reveal">Australia, Canada, the USA, and India — with budgets managed in local currency.</p>
        </div>
        <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(220px,1fr))">
          ${D.GLOBAL_MARKETS.map(([country, ctx, note], i) => `<article class="card hover-glow reveal" data-delay="${(i % 4) * 70}" style="align-items:flex-start">
            <span class="card__icon">${icon("globe")}</span>
            <h3 style="font-size:1.15rem">${country}</h3>
            <p style="font-size:0.92rem">${ctx}</p>
            <p class="cs-card__industry">${note}</p>
          </article>`).join("\n          ")}
        </div>
      </div>
    </section>

    <!-- ============ 16. LATEST INSIGHTS ============ -->
    <section class="section" aria-labelledby="insights-title">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Latest insights</span>
          <h2 id="insights-title" class="reveal">Thinking you can use</h2>
        </div>
        <div class="grid blog-grid">
          ${D.BLOG_POSTS.slice(0, 3).map(blogCard).join("\n          ")}
        </div>
        <p style="margin-top:40px;text-align:center"><a class="btn btn--ghost" href="blog.html">Browse all articles ${icon("arrow-right", "icon-sm")}</a></p>
      </div>
    </section>

    <!-- ============ 17. TALK TO A STRATEGIST ============ -->
    <section class="section" aria-labelledby="talk-title">
      <div class="container container--narrow" style="text-align:center">
        <span class="urgency reveal" data-urgency data-slots="4" data-slots-min="1" aria-live="polite">
          <span class="pulse-dot" aria-hidden="true"></span>
          <span><strong><span data-slots-count>4</span> consult slots</strong> open this week <!-- REPLACE: keep honest --></span>
        </span>
        <h2 id="talk-title" class="reveal" style="margin-top:20px">Talk to the person who’ll do the work</h2>
        <p class="lead reveal" style="margin:14px auto 0;max-width:46ch">A 30-minute call to pressure-test your growth — no junior handoff, no pitch deck.</p>
        <p style="margin-top:26px"><a class="btn btn--primary btn--lg" href="consultation.html" data-popup-open data-cta="talk">Book Free Consultation ${icon("arrow-right", "icon-sm")}</a></p>
      </div>
    </section>

    <!-- ============ 18. FAQ (categorized) ============ -->
    <section class="section" aria-labelledby="faq-title" style="background:var(--sky-bg)">
      <div class="container container--narrow">
        <div class="section-head section-head--center">
          <span class="eyebrow">FAQ</span>
          <h2 id="faq-title" class="reveal">Questions before we start</h2>
          <p class="reveal">Straight answers on scope, pricing, and how engagements run.</p>
        </div>
        ${faqBlock()}
      </div>
    </section>

    <!-- ============ 19. FINAL CTA ============ -->
${ctaBand({ id: "final-cta", source: "home-final", headline: "Let’s build a system that keeps growing.", copy: "One call. One engine. Strategy, ads, automation, and site — aligned to your revenue goal." })}`;
}

function homeSchemas() {
  return [
    { "@context": "https://schema.org", "@type": "Person", name: "Sushant Rana", jobTitle: "Business Growth Consultant", url: SITE.base + "/", knowsAbout: ["Performance Marketing", "Brand Strategy", "AI Automation", "Website Development", "Google Ads", "Meta Ads"] },
    { "@context": "https://schema.org", "@type": "ProfessionalService", name: "Sushant Rana — Business Growth Consultant", url: SITE.base + "/", description: "Business growth consulting: brand strategy, performance marketing, AI automation, and website development.", founder: { "@type": "Person", name: "Sushant Rana" }, areaServed: ["India", "Australia", "Canada", "United States"] },
    { "@context": "https://schema.org", "@type": "FAQPage", mainEntity: D.HOME_FAQ.map(([cat, q, a]) => ({ "@type": "Question", name: q, acceptedAnswer: { "@type": "Answer", text: a } })) },
  ];
}

module.exports = { homeContent, homeSchemas };
