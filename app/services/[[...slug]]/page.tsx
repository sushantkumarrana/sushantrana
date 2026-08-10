import type { Metadata } from "next";
import ComingSoon from "@/components/ComingSoon";
import { catchAllCanonical } from "@/lib/seo";

// Optional catch-all: matches /services and /services/anything.
// Real pages added later as app/services/<slug>/page.tsx take precedence
// over this route, so links start working the moment a page exists.
// Self-referencing canonical per URL: /services and every /services/<slug> the
// catch-all serves point at themselves, never at the section root.
export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const { slug } = await params;
  return {
    title: "Services | Sushant Rana",
    description: "This page is currently being built and will be live soon.",
    robots: { index: false, follow: true },
    alternates: { canonical: catchAllCanonical("services", slug) },
  };
}

const titleCase = (s: string) =>
  s.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

export default async function Page({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}) {
  const { slug } = await params;
  const name = slug?.length ? titleCase(slug[slug.length - 1]) : "Services";
  return <ComingSoon pageName={name} />;
}
