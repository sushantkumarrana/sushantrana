import type { MetadataRoute } from "next";
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
  ];
}
