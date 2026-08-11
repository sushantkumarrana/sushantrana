import type { Metadata } from "next";
import ComingSoon from "@/components/ComingSoon";
import { sectionTrail } from "@/components/Breadcrumbs";
import { catchAllCanonical } from "@/lib/seo";

// Optional catch-all: matches /about and /about/anything.
// Real pages added later as app/about/<slug>/page.tsx take precedence
// over this route, so links start working the moment a page exists.
// Self-referencing canonical per URL: /about and every /about/<slug> the
// catch-all serves point at themselves, never at the section root.
export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const { slug } = await params;
  return {
    title: "About | Sushant Rana",
    description: "This page is currently being built and will be live soon.",
    robots: { index: false, follow: true },
    alternates: { canonical: catchAllCanonical("about", slug) },
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
  const name = slug?.length ? titleCase(slug[slug.length - 1]) : "About";
  return (
    <ComingSoon
      pageName={name}
      crumbs={sectionTrail({ label: "About", base: "about" }, slug)}
    />
  );
}
