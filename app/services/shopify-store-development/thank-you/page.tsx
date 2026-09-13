import type { Metadata } from "next";
import ShopifyThankYou from "@/components/shopify/ThankYou";

// A confirmation screen has no search value and must never be indexed: it would
// compete with the service page and could be landed on with no context.
export const metadata: Metadata = {
  title: "Thank you | Shopify store quote | Sushant Rana",
  description: "Your Shopify store enquiry has been received.",
  robots: { index: false, follow: false },
};

export default function Page() {
  return <ShopifyThankYou />;
}
