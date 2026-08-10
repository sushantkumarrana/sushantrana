import type { Metadata } from "next";
import ComingSoon from "@/components/ComingSoon";

export const metadata: Metadata = {
  title: "Coming soon | Sushant Rana",
  description: "This page is currently being built and will be live soon.",
  // placeholder content — don't let it get indexed as thin content
  robots: { index: false, follow: true },
};

export default function ComingSoonPage() {
  return <ComingSoon />;
}
