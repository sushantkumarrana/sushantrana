import Link from "next/link";
import type { Metadata } from "next";
import SimplePage from "@/components/SimplePage";

export const metadata: Metadata = {
  title: "Thank you | Sushant Rana",
  description: "Your request has been received. I'll be in touch within one business day.",
  // utility page — keep it out of search results
  robots: { index: false, follow: true },
};

export default function ThankYou() {
  return (
    <SimplePage
      label="Request received"
      title="Thanks — I'll be in"
      accent="touch shortly."
      actions={
        <>
          <Link href="/" className="btn btn-primary">
            Back to home
          </Link>
          <Link href="/#blog" className="btn btn-outline">
            Read the blog
          </Link>
        </>
      }
    >
      <p>
        Your details are with me. I reply personally within one business day,
        usually sooner. If it&apos;s urgent, email{" "}
        <a href="mailto:hello@sushantrana.com" className="font-semibold text-orange">
          hello@sushantrana.com
        </a>
        .
      </p>
    </SimplePage>
  );
}
