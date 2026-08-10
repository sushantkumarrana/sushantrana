import type { Metadata } from "next";
import Home from "@/components/Home";
import { SITE_URL, canonicalUrl } from "@/lib/seo";

export const metadata: Metadata = {
  alternates: { canonical: canonicalUrl("/") },
};

// Structured data for the only indexable page on the site. Every url/@id below
// uses the canonical https + apex origin, so the entity graph agrees with the
// canonical tag and the sitemap instead of splitting the entity across hosts.
// The @id values are stable fragment identifiers, which is what lets WebPage,
// WebSite and Person reference each other rather than duplicating themselves.
const PERSON_ID = `${SITE_URL}/#person`;
const SITE_ID = `${SITE_URL}/#website`;
const PAGE_ID = `${SITE_URL}/#webpage`;

const structuredData = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Person",
      "@id": PERSON_ID,
      name: "Sushant Rana",
      url: canonicalUrl("/"),
      jobTitle: "Business Growth Consultant",
      mainEntityOfPage: { "@id": PAGE_ID },
      email: "mailto:me@sushantrana.com",
      image: {
        "@type": "ImageObject",
        url: `${SITE_URL}/about/about.png`,
      },
      description:
        "Business growth consultant building revenue systems — strategy, performance marketing, and AI automation working as one engine.",
      knowsAbout: [
        "Performance Marketing",
        "Growth Strategy",
        "Marketing Automation",
        "Paid Advertising",
        "Conversion Rate Optimization",
      ],
    },
    {
      "@type": "WebSite",
      "@id": SITE_ID,
      url: canonicalUrl("/"),
      name: "Sushant Rana",
      description:
        "Revenue systems, not just campaigns. Strategy, performance marketing, and AI automation as one engine.",
      publisher: { "@id": PERSON_ID },
      inLanguage: "en",
    },
    {
      "@type": "WebPage",
      "@id": PAGE_ID,
      url: canonicalUrl("/"),
      name: "Sushant Rana — Business Growth Consultant | Revenue Systems, Not Just Campaigns",
      description:
        "I build revenue systems, not just marketing campaigns — strategy, performance marketing, and AI automation working as one engine. 8+ years, 4 markets.",
      isPartOf: { "@id": SITE_ID },
      about: { "@id": PERSON_ID },
      publisher: { "@id": PERSON_ID },
      primaryImageOfPage: {
        "@type": "ImageObject",
        url: `${SITE_URL}/hero/hero.png`,
      },
      inLanguage: "en",
    },
  ],
};

export default function Page() {
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
      />
      <Home />
    </>
  );
}
