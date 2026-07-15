/* Site generator. Run `node build/build.js` from the site root.
   Output is committed — the site runs by opening the HTML files directly. */
"use strict";

const fs = require("fs");
const path = require("path");

const P = require("./partials");
const D = require("./data");
const S = require("./services");
const { homeContent, homeSchemas } = require("./home");
const G = require("./pages");

const ROOT = path.join(__dirname, "..");

function write(file, content) {
  fs.writeFileSync(path.join(ROOT, file), content);
  console.log("✓", file);
}

/* ---------- SVG placeholder images (brand-blue gradient + label) ---------- */
function placeholderSvg(w, h, label, sub) {
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" role="img" aria-label="${label} placeholder image">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#EAF4FB"/><stop offset="0.55" stop-color="#CFE6FA"/><stop offset="1" stop-color="#AFD4F5"/>
    </linearGradient>
    <radialGradient id="o1" cx="0.2" cy="0.15" r="0.6"><stop offset="0" stop-color="#38BDF8" stop-opacity="0.4"/><stop offset="1" stop-color="#38BDF8" stop-opacity="0"/></radialGradient>
    <radialGradient id="o2" cx="0.85" cy="0.9" r="0.6"><stop offset="0" stop-color="#1780C5" stop-opacity="0.35"/><stop offset="1" stop-color="#1780C5" stop-opacity="0"/></radialGradient>
  </defs>
  <rect width="${w}" height="${h}" fill="url(#g)"/>
  <rect width="${w}" height="${h}" fill="url(#o1)"/>
  <rect width="${w}" height="${h}" fill="url(#o2)"/>
  <g fill="none" stroke="#1780C5" stroke-opacity="0.22" stroke-width="2">
    <circle cx="${w * 0.82}" cy="${h * 0.2}" r="${Math.min(w, h) * 0.14}"/>
    <circle cx="${w * 0.16}" cy="${h * 0.82}" r="${Math.min(w, h) * 0.2}"/>
  </g>
  <text x="50%" y="${sub ? "47%" : "50%"}" text-anchor="middle" font-family="Poppins, Arial, sans-serif" font-size="${Math.max(16, Math.min(w, h) * 0.05)}" font-weight="bold" fill="#0F5688" opacity="0.8">${label}</text>
  ${sub ? `<text x="50%" y="56%" text-anchor="middle" font-family="Arial, sans-serif" font-size="${Math.max(12, Math.min(w, h) * 0.032)}" fill="#136AA5" opacity="0.6">${sub}</text>` : ""}
</svg>
`;
}

const IMAGES = [["og-cover.svg", 1200, 630, "Sushant Rana", "Business Growth Consultant"]];
D.BLOG_POSTS.forEach((p) => IMAGES.push([p.img, 800, 500, p.category, "Article image placeholder"]));

/* ---------- pages ---------- */
write("index.html", P.page({
  path: "index.html",
  title: "Sushant Rana — Business Growth Consultant | Revenue Systems, Not Just Campaigns",
  description: "I build revenue systems, not just marketing campaigns. Business growth consulting through strategy, performance marketing, and AI automation across 4 countries.",
  active: "home",
  schema: homeSchemas(),
  content: homeContent(),
}));

S.SERVICES.forEach((svc) => write(svc.file, G.servicePage(svc)));
write("performance-marketing.html", G.perfHubPage());
write("development.html", G.devHubPage());
write("services.html", G.servicesPage());
write("case-studies.html", G.caseStudiesPage());
write("blog.html", G.blogPage());
write("blog-post.html", G.blogPostPage());
write("contact.html", G.contactPage());
write("consultation.html", G.consultationPage());
write("thank-you.html", G.thankYouPage());
write("privacy-policy.html", G.legalPage("privacy-policy.html", "Privacy Policy | Sushant Rana", "Privacy Policy", G.PRIVACY_BODY));
write("terms-conditions.html", G.legalPage("terms-conditions.html", "Terms & Conditions | Sushant Rana", "Terms & Conditions", G.TERMS_BODY));
write("404.html", G.notFoundPage());

/* ---------- images ---------- */
IMAGES.forEach(([name, w, h, label, sub]) => write(path.join("assets/img", name), placeholderSvg(w, h, label, sub)));

/* ---------- robots + sitemap ---------- */
const PAGES_FOR_SITEMAP = [
  "index.html", "services.html", "performance-marketing.html",
  ...S.SERVICES.map((s) => s.file),
  "development.html", "case-studies.html", "blog.html", "blog-post.html",
  "contact.html", "consultation.html", "privacy-policy.html", "terms-conditions.html",
];
write("robots.txt", `User-agent: *\nAllow: /\nDisallow: /thank-you.html\n\nSitemap: ${P.SITE.base}/sitemap.xml\n`);
write("sitemap.xml", `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${PAGES_FOR_SITEMAP.map((p) => `  <url><loc>${P.SITE.base}/${p === "index.html" ? "" : p}</loc></url>`).join("\n")}
</urlset>
`);

console.log("\nBuild complete: " + (14 + S.SERVICES.length) + " pages + " + IMAGES.length + " images.");
