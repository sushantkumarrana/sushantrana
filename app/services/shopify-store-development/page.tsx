import type { Metadata } from "next";
import ShopifyDevelopment from "@/components/ShopifyDevelopment";
import { SITE_URL, canonicalUrl } from "@/lib/seo";
import { SHOPIFY_FAQS, WHAT_YOU_GET } from "@/lib/shopify";

const PAGE_URL = canonicalUrl("/services/shopify-store-development");

const TITLE = "Shopify Store Development Services | Sushant Rana";
const DESCRIPTION =
  "Custom Shopify store development by Sushant Rana: new stores, redesigns, theme development and migrations, built to convert and handed over in 4-6 weeks. Get a free quote.";

const OG_IMAGE = `${SITE_URL}/og.jpg`;

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  // Self-referencing canonical, slash-less, matching the sitemap byte for byte.
  alternates: { canonical: PAGE_URL },
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true, "max-image-preview": "large", "max-snippet": -1 },
  },
  openGraph: {
    title: "Shopify Store Development Services",
    description: DESCRIPTION,
    url: PAGE_URL,
    siteName: "Sushant Rana",
    type: "website",
    locale: "en_US",
    images: [
      {
        url: OG_IMAGE,
        width: 1200,
        height: 630,
        alt: "Shopify store development services by Sushant Rana",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Shopify Store Development Services",
    description: DESCRIPTION,
    images: [OG_IMAGE],
  },
};

/**
 * Structured data.
 *
 * The Person is referenced by @id rather than redeclared: the homepage already
 * defines that entity, so this page adds a Service and a FAQPage that hang off
 * it instead of creating a second Sushant Rana in the graph.
 *
 * BreadcrumbList is intentionally absent here — the <Breadcrumbs> component
 * emits its own from the trail it actually renders, and two lists would
 * conflict.
 *
 * No Review or AggregateRating: the quotes on the page are illustrative, and
 * rating markup without genuine, attributable reviews is a policy breach.
 */
const PERSON_ID = `${SITE_URL}/#person`;
const PAGE_ID = `${PAGE_URL}#webpage`;
const SERVICE_ID = `${PAGE_URL}#service`;

const structuredData = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebPage",
      "@id": PAGE_ID,
      url: PAGE_URL,
      name: TITLE,
      description: DESCRIPTION,
      inLanguage: "en",
      isPartOf: { "@id": `${SITE_URL}/#website` },
      about: { "@id": SERVICE_ID },
      mainEntity: { "@id": SERVICE_ID },
      primaryImageOfPage: { "@type": "ImageObject", url: OG_IMAGE, width: 1200, height: 630 },
      significantLink: [
        canonicalUrl("/services/ecommerce-seo"),
        canonicalUrl("/services/google-shopping-ads"),
        canonicalUrl("/services/website-maintenance"),
      ],
    },
    {
      "@type": "Service",
      "@id": SERVICE_ID,
      name: "Shopify store development",
      serviceType: "Shopify store development",
      category: "Ecommerce website development",
      description:
        "Design, development, redesign and migration of Shopify stores, including custom theme development, product and collection setup, app and payment integration, speed work and conversion optimisation.",
      url: PAGE_URL,
      provider: { "@id": PERSON_ID },
      // Countries named in the hero copy on this page.
      areaServed: [
        { "@type": "Country", name: "India" },
        { "@type": "Country", name: "United Arab Emirates" },
        { "@type": "Country", name: "Canada" },
        { "@type": "Country", name: "Australia" },
        { "@type": "Country", name: "United States" },
      ],
      audience: { "@type": "BusinessAudience", name: "Ecommerce and D2C brands" },
      availableChannel: {
        "@type": "ServiceChannel",
        serviceUrl: PAGE_URL,
        availableLanguage: ["en", "hi"],
      },
      hasOfferCatalog: {
        "@type": "OfferCatalog",
        name: "What a Shopify store build includes",
        itemListElement: WHAT_YOU_GET.map((s) => ({
          "@type": "Offer",
          itemOffered: { "@type": "Service", name: s.t, description: s.d },
        })),
      },
    },
    {
      "@type": "FAQPage",
      "@id": `${PAGE_URL}#faq`,
      isPartOf: { "@id": PAGE_ID },
      mainEntity: SHOPIFY_FAQS.map((f) => ({
        "@type": "Question",
        name: f.q,
        acceptedAnswer: { "@type": "Answer", text: f.a },
      })),
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
      <ShopifyDevelopment />
    </>
  );
}
