/* Shared page chrome: head, header, footer, ambient layers, icons, wrapper.
   Every page is assembled from these so markup stays identical sitewide. */
"use strict";

const { ICONS } = require("./icons");

const SITE = {
  base: "https://sushantrana.com", // REPLACE if the production domain differs
  name: "Sushant Rana",
  tagline: "Business Growth Consultant",
};

/* ---------- icons: premium duotone set ---------- */
// Aliases map legacy/semantic names onto the generated icon family.
const ICON_ALIASES = {
  megaphone: "performance-marketing", chart: "analytics-dashboard", trend: "growth-chart",
  users: "partnership", refresh: "conversion", shield: "shield-trust", code: "web-development",
  nodes: "node-graph", compass: "strategy", mail: "email", x: "x-twitter", cursor: "cursor",
  layout: "layout", search: "search", gear: "gear", brain: "brain", spark: "spark",
  target: "target", funnel: "funnel", cart: "cart", clock: "clock", calendar: "calendar",
};
function icon(name, cls) {
  const raw = ICONS[name] || ICONS[ICON_ALIASES[name]];
  if (!raw) return "";
  const klass = "icon" + (cls ? " " + cls : "");
  return raw.replace("<svg ", '<svg class="' + klass + '" aria-hidden="true" focusable="false" ');
}

/* ---------- favicon (inline data URI) ---------- */
const FAVICON =
  "data:image/svg+xml," +
  encodeURIComponent(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="f" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#38bdf8"/><stop offset="1" stop-color="#1780C5"/></linearGradient></defs><rect width="64" height="64" rx="15" fill="url(#f)"/><text x="32" y="43" font-family="Poppins,Arial,sans-serif" font-size="30" font-weight="800" fill="#fff" text-anchor="middle">SR</text></svg>'
  );

/* ---------- <head> ---------- */
function head(opts) {
  const url = SITE.base + "/" + (opts.path === "index.html" ? "" : opts.path);
  const ogImage = SITE.base + "/assets/img/og-cover.svg"; // REPLACE: 1200x630 PNG/JPG for real OG rendering
  const schemas = (opts.schema || [])
    .map((s) => '<script type="application/ld+json">' + JSON.stringify(s) + "</script>")
    .join("\n  ");
  return `<meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${opts.title}</title>
  <meta name="description" content="${opts.description}">
  ${opts.noindex ? '<meta name="robots" content="noindex, follow">' : ""}
  <link rel="canonical" href="${url}">
  <meta property="og:type" content="${opts.ogType || "website"}">
  <meta property="og:site_name" content="Sushant Rana — Business Growth Consultant">
  <meta property="og:title" content="${opts.title}">
  <meta property="og:description" content="${opts.description}">
  <meta property="og:url" content="${url}">
  <meta property="og:image" content="${ogImage}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${opts.title}">
  <meta name="twitter:description" content="${opts.description}">
  <meta name="theme-color" content="#EAF4FB">
  <link rel="icon" href="${FAVICON}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/style.css">
  <script src="assets/js/main.js" defer></script>
  ${schemas}`;
}

/* ---------- global ambient (subtle, fixed) ---------- */
function ambient() {
  return `<div class="ambient" aria-hidden="true"><div class="ambient__grid"></div></div>`;
}

/* ---------- nav data ---------- */
const PERF_LINKS = [
  ["google-ads.html", "Google Ads"],
  ["meta-ads.html", "Meta Ads"],
  ["tiktok-ads.html", "TikTok Ads"],
  ["snapchat-ads.html", "Snapchat Ads"],
  ["linkedin-ads.html", "LinkedIn Ads"],
  ["microsoft-ads.html", "Microsoft Ads"],
  ["amazon-ads.html", "Amazon Ads"],
];
const DEV_LINKS = [
  ["shopify-development.html", "Shopify"],
  ["wordpress-development.html", "WordPress"],
  ["wix-studio-development.html", "Wix Studio"],
  ["webflow-development.html", "Webflow"],
  ["custom-development.html", "Custom"],
];

function navLink(href, label, active) {
  return `<a class="nav__link" href="${href}"${active ? ' aria-current="page"' : ""}>${label}</a>`;
}

function brand() {
  return `<a class="brand" href="index.html"><span class="brand__mark">SR</span> Sushant Rana</a>`;
}

/* ---------- header ---------- */
function header(active) {
  const dd = (id, label, links, hubHref) => `
        <li class="nav__item nav__item--dropdown">
          <button type="button" class="nav__toggle" aria-expanded="false" aria-controls="${id}">
            ${label} ${icon("chevron-down", "icon-sm")}
          </button>
          <div class="nav__dropdown" id="${id}">
            <a href="${hubHref}">All ${label}</a>
            ${links.map(([h, l]) => `<a href="${h}">${l}</a>`).join("\n            ")}
          </div>
        </li>`;
  return `<header class="site-header">
    <div class="container site-header__inner">
      ${brand()}
      <nav class="nav" aria-label="Primary">
        <ul class="nav__list">
          <li class="nav__item">${navLink("index.html", "Home", active === "home")}</li>
          <li class="nav__item">${navLink("services.html", "Services", active === "services")}</li>${dd("dd-perf", "Performance Marketing", PERF_LINKS, "performance-marketing.html")}${dd("dd-dev", "Development", DEV_LINKS, "development.html")}
          <li class="nav__item">${navLink("blog.html", "Blog", active === "blog")}</li>
          <li class="nav__item">${navLink("contact.html", "Contact", active === "contact")}</li>
          <li class="nav__item"><a class="btn btn--primary nav__cta" href="consultation.html" data-popup-open data-cta="header">Book a Consultation</a></li>
        </ul>
      </nav>
      <button type="button" class="drawer-toggle" aria-expanded="false" aria-controls="mobile-drawer" aria-label="Open menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>
  <nav class="drawer" id="mobile-drawer" aria-label="Mobile">
    <ul class="drawer__list">
      <li><a class="drawer__link" href="index.html">Home</a></li>
      <li><a class="drawer__link" href="services.html">Services</a></li>
      <li>
        <button type="button" class="drawer__accordion-toggle" aria-expanded="false" aria-controls="drawer-sub-perf">
          Performance Marketing ${icon("chevron-down", "icon-sm")}
        </button>
        <div class="drawer__sub" id="drawer-sub-perf"><div>
          <a href="performance-marketing.html">All Performance Marketing</a>
          ${PERF_LINKS.map(([h, l]) => `<a href="${h}">${l}</a>`).join("\n          ")}
        </div></div>
      </li>
      <li>
        <button type="button" class="drawer__accordion-toggle" aria-expanded="false" aria-controls="drawer-sub-dev">
          Development ${icon("chevron-down", "icon-sm")}
        </button>
        <div class="drawer__sub" id="drawer-sub-dev"><div>
          <a href="development.html">All Development</a>
          ${DEV_LINKS.map(([h, l]) => `<a href="${h}">${l}</a>`).join("\n          ")}
        </div></div>
      </li>
      <li><a class="drawer__link" href="blog.html">Blog</a></li>
      <li><a class="drawer__link" href="contact.html">Contact</a></li>
    </ul>
    <div class="drawer__cta">
      <a class="btn btn--primary btn--lg" style="width:100%" href="consultation.html" data-popup-open data-cta="drawer">Book a Consultation</a>
    </div>
  </nav>`;
}

/* ---------- footer ---------- */
function footer(minimal) {
  if (minimal) {
    return `<footer class="site-footer site-footer--minimal">
    <div class="container site-footer__inner" style="padding-block:28px">
      <div class="footer-bottom">
        <p>© 2026 Sushant Rana. All rights reserved.</p>
        <nav aria-label="Legal">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-conditions.html">Terms &amp; Conditions</a>
        </nav>
      </div>
    </div>
  </footer>`;
  }
  return `<footer class="site-footer">
    <div class="deco-grid-light" aria-hidden="true"></div>
    <div class="container site-footer__inner">
      <div class="footer-grid">
        <div class="footer-brand">
          ${brand()}
          <p>Business growth consultant. I build revenue systems — strategy, performance marketing, and AI automation working as one engine.</p>
          <div class="footer-social">
            <!-- REPLACE: real social profile URLs -->
            <a href="#" aria-label="LinkedIn profile">${icon("linkedin")}</a>
            <a href="#" aria-label="Instagram profile">${icon("instagram")}</a>
            <a href="#" aria-label="X (Twitter) profile">${icon("x-twitter")}</a>
            <a href="#" aria-label="YouTube channel">${icon("youtube")}</a>
          </div>
        </div>
        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">All Services</a></li>
            <li><a href="performance-marketing.html">Performance Marketing</a></li>
            <li><a href="development.html">Website Development</a></li>
            <li><a href="case-studies.html">Case Studies</a></li>
            <li><a href="consultation.html">Free Consultation</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Advertising</h4>
          <ul>
            ${PERF_LINKS.map(([h, l]) => `<li><a href="${h}">${l}</a></li>`).join("\n            ")}
          </ul>
        </div>
        <div class="footer-col">
          <h4>Development</h4>
          <ul>
            ${DEV_LINKS.map(([h, l]) => `<li><a href="${h}">${l}</a></li>`).join("\n            ")}
            <li><a href="blog.html">Blog</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 Sushant Rana. All rights reserved.</p>
        <nav aria-label="Legal">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-conditions.html">Terms &amp; Conditions</a>
        </nav>
      </div>
    </div>
  </footer>`;
}

/* ---------- breadcrumbs ---------- */
function breadcrumbs(items) {
  const html = items
    .map(([href, label], i) => {
      const node = href ? `<a href="${href}">${label}</a>` : `<span aria-current="page">${label}</span>`;
      const sep = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true" style="transform:rotate(-90deg)"><path d="m6 9 6 6 6-6"/></svg>`;
      return i === 0 ? node : sep + node;
    })
    .join("");
  return `<nav class="breadcrumbs" aria-label="Breadcrumb">${html}</nav>`;
}

function breadcrumbSchema(items, path) {
  return {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map(([href, label], i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: label,
      item: SITE.base + "/" + (href || path),
    })),
  };
}

/* ---------- CTA band (single-line CTA) ---------- */
function ctaBand(opts) {
  const o = opts || {};
  return `<section class="section" aria-labelledby="${o.id || "cta"}-title">
      <div class="container">
        <div class="cta-band reveal-scale">
          <div class="cta-band__aurora" aria-hidden="true"></div>
          <h2 id="${o.id || "cta"}-title">${o.headline || "Let’s build a system that keeps growing."}</h2>
          <p>${o.copy || "One call. One engine. Strategy, ads, automation, and site — aligned to your revenue goal."}</p>
          <a class="btn btn--white btn--lg" href="consultation.html" data-popup-open data-cta="${o.source || "cta-band"}">Book Free Consultation</a>
          <p class="cta-band__reassure">${o.reassure || "No obligation · Senior-led · 4 markets"}</p>
        </div>
      </div>
    </section>`;
}

/* ---------- full page wrapper ---------- */
function page(opts) {
  const chrome = opts.minimalChrome
    ? `<header class="site-header is-scrolled">
    <div class="container site-header__inner">
      ${brand()}
      <span class="font-display" style="color:var(--gray-med);font-weight:600;font-size:0.85rem">Business Growth Consultant</span>
    </div>
  </header>`
    : header(opts.active);
  return `<!DOCTYPE html>
<html lang="en">
<head>
  ${head(opts)}
</head>
<body${opts.bodyClass ? ' class="' + opts.bodyClass + '"' : ""}>
  <a class="skip-link" href="#main">Skip to content</a>
  ${ambient()}
  ${chrome}
  <main id="main">
${opts.content}
  </main>
  ${footer(opts.minimalChrome)}
</body>
</html>
`;
}

module.exports = { SITE, icon, head, header, footer, ambient, brand, breadcrumbs, breadcrumbSchema, ctaBand, page, PERF_LINKS, DEV_LINKS };
