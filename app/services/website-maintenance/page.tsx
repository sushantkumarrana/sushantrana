import type { Metadata } from "next";
import WebsiteMaintenance from "@/components/WebsiteMaintenance";
import { SITE_URL, canonicalUrl } from "@/lib/seo";
import { MAINTENANCE_FAQS, PLANS } from "@/lib/maintenance";

const PAGE_URL = canonicalUrl("/services/website-maintenance");

const TITLE = "Website Maintenance Services in India | Sushant Rana";
const DESCRIPTION =
  "Website maintenance plans from ₹18,000/year for WordPress, Shopify, Wix, Webflow, Framer and custom sites. Backups, updates, security and fixes.";

// Page-specific share image (1200x630), cropped from the licensed hero photo.
const OG_IMAGE = `${SITE_URL}/services/maintenance/og-website-maintenance.jpg`;

export const metadata: Metadata = {
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: PAGE_URL },
  robots: {
    index: true,
    follow: true,
    googleBot: { index: true, follow: true, "max-image-preview": "large", "max-snippet": -1 },
  },
  openGraph: {
    title: "Website Maintenance Services",
    description: DESCRIPTION,
    url: PAGE_URL,
    siteName: "Sushant Rana",
    type: "website",
    locale: "en_US",
    images: [{ url: OG_IMAGE, width: 1200, height: 630, alt: "Website maintenance services by Sushant Rana" }],
  },
  twitter: {
    card: "summary_large_image",
    title: "Website Maintenance Services",
    description: DESCRIPTION,
    images: [OG_IMAGE],
  },
};

// Same graph shape as the Shopify page: Person by @id, breadcrumbs left to
// <Breadcrumbs>. Offers use the rupee figures shown on the page, pre-GST.
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
    },
    {
      "@type": "Service",
      "@id": SERVICE_ID,
      name: "Website maintenance",
      serviceType: "Website maintenance",
      description:
        "Yearly website maintenance plans for WordPress, Shopify, Wix, Squarespace, Webflow, Framer and custom-coded websites, covering backups, security scanning, CMS and plugin updates, bug fixes, content changes, SSL and domain monitoring.",
      url: PAGE_URL,
      image: OG_IMAGE,
      provider: { "@id": PERSON_ID },
      areaServed: { "@type": "Country", name: "India" },
      hasOfferCatalog: {
        "@type": "OfferCatalog",
        name: "Website maintenance plans",
        itemListElement: PLANS.map((p) => ({
          "@type": "Offer",
          name: `${p.name} (${p.hours})`,
          price: p.price.replace(/[^\d]/g, ""),
          priceCurrency: "INR",
          itemOffered: { "@type": "Service", name: `${p.name} website maintenance plan` },
        })),
      },
    },
    {
      "@type": "FAQPage",
      "@id": `${PAGE_URL}#faq`,
      isPartOf: { "@id": PAGE_ID },
      mainEntity: MAINTENANCE_FAQS.map((f) => ({
        "@type": "Question",
        name: f.q,
        acceptedAnswer: { "@type": "Answer", text: f.a },
      })),
    },
  ],
};

/** INR → other currencies, refreshed daily at most. The page still renders in
 *  rupees if the rate service is down. */
async function getRates(): Promise<Record<string, number> | null> {
  try {
    const res = await fetch("https://open.er-api.com/v6/latest/INR", {
      next: { revalidate: 86400 },
    });
    const data = await res.json();
    return data.result === "success" ? data.rates : null;
  } catch {
    return null;
  }
}

export default async function Page() {
  const rates = await getRates();
  return (
    <>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
      />
      <WebsiteMaintenance rates={rates} />
    </>
  );
}
