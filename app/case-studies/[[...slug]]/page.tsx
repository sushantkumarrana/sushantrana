import type { Metadata } from "next";
import ComingSoon from "@/components/ComingSoon";
import { sectionTrail } from "@/components/Breadcrumbs";
import { catchAllCanonical } from "@/lib/seo";

// Optional catch-all: matches /case-studies and /case-studies/anything.
// Real pages added later as app/case-studies/<slug>/page.tsx take precedence
// over this route, so links start working the moment a page exists.
// Self-referencing canonical per URL: /case-studies and every /case-studies/<slug> the
// catch-all serves point at themselves, never at the section root.
export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const { slug } = await params;
  return {
    title: "Case Studies | Sushant Rana",
    description: "This page is currently being built and will be live soon.",
    robots: { index: false, follow: true },
    alternates: { canonical: catchAllCanonical("case-studies", slug) },
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
  const name = slug?.length ? titleCase(slug[slug.length - 1]) : "Case Studies";
  return (
    <ComingSoon
      pageName={name}
      crumbs={sectionTrail({ label: "Case Studies", base: "case-studies" }, slug)}
    />
  );
}
