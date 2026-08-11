import type { Metadata } from "next";
import LegalPage from "@/components/LegalPage";
import { PRIVACY_POLICY } from "@/lib/legal";
import { canonicalUrl } from "@/lib/seo";

const DESCRIPTION =
  "What sushantrana.com collects when you submit an enquiry, who processes it, how long it is kept, and how to have it corrected or deleted.";

export const metadata: Metadata = {
  title: "Privacy Policy | Sushant Rana",
  description: DESCRIPTION,
  alternates: { canonical: canonicalUrl("/privacy-policy") },
  // Indexable and crawlable: a policy that search engines can't see reads as
  // a missing policy to anyone checking, including ad platform reviewers.
  robots: { index: true, follow: true },
};

export default function Page() {
  return (
    <LegalPage
      label="Legal"
      title="Privacy"
      accent="Policy"
      crumb="Privacy Policy"
      intro={DESCRIPTION}
      blocks={PRIVACY_POLICY}
      otherHref="/terms-and-conditions"
      otherLabel="Read the Terms & Conditions"
    />
  );
}
