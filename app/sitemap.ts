import type { MetadataRoute } from "next";
import { POSTS_BY_DATE } from "@/lib/blog";
import { canonicalUrl } from "@/lib/seo";

export default function sitemap(): MetadataRoute.Sitemap {
  // Only real, indexable pages belong here. The section catch-alls currently
  // render "coming soon" placeholders and emit `noindex`, so listing them would
  // submit thin, non-indexable content to Google. Add each page here as it goes
  // live. URLs are built with canonicalUrl() so every <loc> is byte-identical
  // to that page's canonical tag.
  return [
    {
      url: canonicalUrl("/"),
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 1,
    },
    {
      url: canonicalUrl("/blog"),
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 0.8,
    },
    // lastModified is the post's own date, not build time — telling Google an
    // unchanged article was modified on every deploy trains it to ignore the
    // field entirely.
    ...POSTS_BY_DATE.map((p) => ({
      url: canonicalUrl(`/blog/${p.slug}`),
      lastModified: new Date(`${p.date}T00:00:00Z`),
      changeFrequency: "monthly" as const,
      priority: 0.7,
    })),
    {
      url: canonicalUrl("/privacy-policy"),
      lastModified: new Date(),
      changeFrequency: "yearly",
      priority: 0.3,
    },
    {
      url: canonicalUrl("/terms-and-conditions"),
      lastModified: new Date(),
      changeFrequency: "yearly",
      priority: 0.3,
    },
  ];
}
