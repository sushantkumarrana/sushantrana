import type { MetadataRoute } from "next";

const BASE = "https://sushantrana.com";

// AI assistants / answer engines. Allowing these lets the site be cited in
// ChatGPT, Claude, Perplexity, Gemini and AI Overviews.
const AI_BOTS = [
  "GPTBot",            // OpenAI crawler (training + retrieval)
  "OAI-SearchBot",     // ChatGPT search index
  "ChatGPT-User",      // ChatGPT browsing on a user's behalf
  "ClaudeBot",         // Anthropic crawler
  "Claude-User",
  "Claude-SearchBot",
  "anthropic-ai",
  "PerplexityBot",     // Perplexity index
  "Perplexity-User",
  "Google-Extended",   // Gemini / AI Overviews grounding
  "Applebot",
  "Applebot-Extended", // Apple Intelligence
  "Bingbot",
  "meta-externalagent",
  "Amazonbot",
  "DuckAssistBot",
  "cohere-ai",
  "YouBot",
  "CCBot",             // Common Crawl (feeds many models)
];

// Utility pages: crawlable for link discovery, kept out of the index
// via each page's own robots meta, and excluded here too.
const PRIVATE = ["/thank-you", "/coming-soon"];

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: "*", allow: "/", disallow: PRIVATE },
      ...AI_BOTS.map((userAgent) => ({
        userAgent,
        allow: "/",
        disallow: PRIVATE,
      })),
    ],
    sitemap: `${BASE}/sitemap.xml`,
    host: BASE,
  };
}
