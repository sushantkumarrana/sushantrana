import type { MetadataRoute } from "next";

const BASE = "https://sushantrana.com";

export default function sitemap(): MetadataRoute.Sitemap {
  // Only real, indexable pages belong here. The section catch-alls currently
  // render "coming soon" placeholders, so listing them would submit thin
  // content to Google. Add each page here as it goes live.
  return [
    {
      url: BASE,
      lastModified: new Date(),
      changeFrequency: "weekly",
      priority: 1,
    },
  ];
}
