import { POSTS_BY_DATE } from "@/lib/blog";
import { canonicalUrl } from "@/lib/seo";

// llms.txt (llmstxt.org): Markdown map of the site for AI assistants. Built
// from the same sources as the sitemap so new blog posts appear automatically.
// Only list indexable pages here, same rule as app/sitemap.ts.
export const dynamic = "force-static";

export function GET() {
  const posts = POSTS_BY_DATE.map(
    (p) => `- [${p.title}](${canonicalUrl(`/blog/${p.slug}`)}): ${p.excerpt}`,
  ).join("\n");

  const body = `# Sushant Rana

> Business growth consultant building revenue systems, not just marketing campaigns: strategy, performance marketing (Google Ads, Meta Ads), SEO, CRM and AI automation, and website development. Running digital marketing since 2017 for brands across India, the UAE, Canada, Switzerland and the USA. Based in Chandigarh, India.

## Pages

- [Home](${canonicalUrl("/")}): Overview of services, results and client work.
- [About](${canonicalUrl("/about")}): Background, experience and the brands Sushant has worked with.

## Services

- [Shopify Store Development](${canonicalUrl("/services/shopify-store-development")}): New stores, redesigns, theme development and migrations, delivered in 4-6 weeks.
- [Website Maintenance](${canonicalUrl("/services/website-maintenance")}): Maintenance plans from ₹18,000/year for WordPress, Shopify, Wix, Webflow, Framer and custom sites.

## Blog

- [Blog](${canonicalUrl("/blog")}): Articles on revenue systems, lead quality and practical AI automation.
${posts}

## Optional

- [Privacy Policy](${canonicalUrl("/privacy-policy")})
- [Terms and Conditions](${canonicalUrl("/terms-and-conditions")})
`;

  return new Response(body, {
    headers: { "Content-Type": "text/markdown; charset=utf-8" },
  });
}
