import type { Metadata } from "next";
import LegalPage from "@/components/LegalPage";
import { TERMS } from "@/lib/legal";
import { canonicalUrl } from "@/lib/seo";

const DESCRIPTION =
  "The terms that govern use of sushantrana.com — what the site is, how enquiries work, intellectual property, liability, and governing law.";

export const metadata: Metadata = {
  title: "Terms & Conditions | Sushant Rana",
  description: DESCRIPTION,
  alternates: { canonical: canonicalUrl("/terms-and-conditions") },
  robots: { index: true, follow: true },
};

export default function Page() {
  return (
    <LegalPage
      label="Legal"
      title="Terms &"
      accent="Conditions"
      crumb="Terms & Conditions"
      intro={DESCRIPTION}
      blocks={TERMS}
      otherHref="/privacy-policy"
      otherLabel="Read the Privacy Policy"
    />
  );
}
