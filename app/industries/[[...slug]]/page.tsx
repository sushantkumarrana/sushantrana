import type { Metadata } from "next";
import ComingSoon from "@/components/ComingSoon";

// Optional catch-all: matches /industries and /industries/anything.
// Real pages added later as app/industries/<slug>/page.tsx take precedence
// over this route, so links start working the moment a page exists.
export const metadata: Metadata = {
  title: "Industries | Sushant Rana",
  description: "This page is currently being built and will be live soon.",
  robots: { index: false, follow: true },
};

const titleCase = (s: string) =>
  s.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

export default async function Page({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}) {
  const { slug } = await params;
  const name = slug?.length ? titleCase(slug[slug.length - 1]) : "Industries";
  return <ComingSoon pageName={name} />;
}
