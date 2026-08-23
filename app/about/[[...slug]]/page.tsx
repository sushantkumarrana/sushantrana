import type { Metadata } from "next";
import About from "@/components/About";
import ComingSoon from "@/components/ComingSoon";
import { sectionTrail } from "@/components/Breadcrumbs";
import { SITE_URL, canonicalUrl, catchAllCanonical } from "@/lib/seo";
import { CLIENTS } from "@/lib/clients";
import { ABOUT_FAQS } from "@/lib/about-faq";

// Optional catch-all: /about is the real About page, /about/anything is still a
// placeholder. A separate app/about/page.tsx cannot exist alongside this route
// (Next rejects two routes of the same specificity), so the root case is
// handled here. Real pages added later as app/about/<slug>/page.tsx take
// precedence over the placeholder branch.
const ABOUT_URL = canonicalUrl("/about");

const TITLE =
  "About Sushant Rana — Growth Consultant & Project Manager, Chandigarh";
const DESCRIPTION =
  "Sushant Rana has run digital marketing since 2017 — Google Ads, Meta Ads, CRM automation, SEO and website development for nine client brands across India, the UAE, Canada, Switzerland and the USA.";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const { slug } = await params;

  if (!slug?.length) {
    return {
      title: TITLE,
      description: DESCRIPTION,
      alternates: { canonical: ABOUT_URL },
      openGraph: {
        title: TITLE,
        description: DESCRIPTION,
        url: ABOUT_URL,
        siteName: "Sushant Rana",
        type: "profile",
        locale: "en_US",
        images: [
          {
            url: "/about/about.png",
            width: 1778,
            height: 884,
            alt: "Sushant Rana — business growth consultant and project manager, Chandigarh, India",
          },
        ],
      },
      twitter: {
        card: "summary_large_image",
        title: TITLE,
        description: DESCRIPTION,
        images: ["/about/about.png"],
      },
    };
  }

  return {
    title: "About | Sushant Rana",
    description: "This page is currently being built and will be live soon.",
    robots: { index: false, follow: true },
    alternates: { canonical: catchAllCanonical("about", slug) },
  };
}

// Reuses the homepage Person @id so both pages describe one entity rather than
// creating a second Sushant Rana in the graph. Client organisations are emitted
// as `mentions` — they are named on the page, so the schema mirrors what a
// reader actually sees. `url` is only set for clients whose domain is
// confirmed; a guessed sameAs would be a fabricated citation.
const PERSON_ID = `${SITE_URL}/#person`;
const PAGE_ID = `${ABOUT_URL}#webpage`;

const structuredData = {
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "AboutPage",
      "@id": PAGE_ID,
      url: ABOUT_URL,
      name: TITLE,
      description: DESCRIPTION,
      inLanguage: "en",
      isPartOf: { "@id": `${SITE_URL}/#website` },
      about: { "@id": PERSON_ID },
      mainEntity: { "@id": PERSON_ID },
      primaryImageOfPage: {
        "@type": "ImageObject",
        url: `${SITE_URL}/about/about.png`,
        width: 1778,
        height: 884,
      },
      mentions: CLIENTS.map((c) => ({
        "@type": "Organization",
        name: c.fullName ?? c.name,
        ...(c.fullName ? { alternateName: c.name } : {}),
        ...(c.url ? { url: c.url } : {}),
        description: c.summary,
      })),
    },
    {
      "@type": "Person",
      "@id": PERSON_ID,
      name: "Sushant Rana",
      url: canonicalUrl("/"),
      mainEntityOfPage: { "@id": PAGE_ID },
      jobTitle: "Project Manager & Business Growth Consultant",
      email: "mailto:me@sushantrana.com",
      image: {
        "@type": "ImageObject",
        url: `${SITE_URL}/about/about.png`,
      },
      description:
        "Business growth consultant and project manager who has worked in digital marketing since 2017, covering performance marketing, CRM automation, SEO and website development.",
      address: {
        "@type": "PostalAddress",
        addressLocality: "Chandigarh",
        addressRegion: "Chandigarh",
        addressCountry: "IN",
      },
      // Verified profile from his own LinkedIn — the entity anchor that lets
      // search engines reconcile "Sushant Rana" here with the same person there.
      sameAs: [
        "https://www.linkedin.com/in/sushant-kumar-rana-030879114",
      ],
      worksFor: { "@type": "Organization", name: "WebIncline" },
      alumniOf: [
        { "@type": "CollegeOrUniversity", name: "ITFT College Chandigarh" },
        { "@type": "School", name: "Army Public School, Chandimandir" },
      ],
      knowsAbout: [
        "Performance Marketing",
        "Google Ads",
        "Meta Ads",
        "CRM Implementation",
        "Marketing Automation",
        "Sales Funnels",
        "WordPress Development",
        "Shopify",
        "Google Tag Manager",
        "GA4",
        "SEO",
        "Conversion Rate Optimization",
      ],
      knowsLanguage: ["English", "Hindi", "Punjabi"],
    },
    {
      "@type": "FAQPage",
      "@id": `${ABOUT_URL}#faq`,
      isPartOf: { "@id": PAGE_ID },
      mainEntity: ABOUT_FAQS.map((f) => ({
        "@type": "Question",
        name: f.q,
        acceptedAnswer: { "@type": "Answer", text: f.a },
      })),
    },
  ],
};

const titleCase = (s: string) =>
  s.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

export default async function Page({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}) {
  const { slug } = await params;

  if (!slug?.length) {
    return (
      <>
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(structuredData) }}
        />
        <About />
      </>
    );
  }

  return (
    <ComingSoon
      pageName={titleCase(slug[slug.length - 1])}
      crumbs={sectionTrail({ label: "About", base: "about" }, slug)}
    />
  );
}
