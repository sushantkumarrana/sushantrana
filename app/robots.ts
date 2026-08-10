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

// Utility pages (/thank-you, /coming-soon) are deliberately NOT disallowed
// here. They already emit `noindex` in their own metadata, and a robots.txt
// Disallow would stop crawlers from ever fetching the page to read that
// noindex — the two directives cancel each other out. Crawlable + noindex is
// the combination that actually keeps a page out of the index.

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      { userAgent: "*", allow: "/" },
      ...AI_BOTS.map((userAgent) => ({
        userAgent,
        allow: "/",
      })),
    ],
    sitemap: `${BASE}/sitemap.xml`,
    host: BASE,
  };
}
