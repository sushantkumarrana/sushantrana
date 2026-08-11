import type { Metadata } from "next";
import ComingSoon from "@/components/ComingSoon";
import { sectionTrail } from "@/components/Breadcrumbs";
import { catchAllCanonical } from "@/lib/seo";

// Safety net: the header/footer CTAs point at /contact/... and are normally
// intercepted by ConsultPopup. If JS hasn't hydrated yet (or is disabled) the
// click falls through to a real navigation, so this must resolve, not 404.
// Self-referencing canonical per URL: /contact and every /contact/<slug> the
// catch-all serves point at themselves, never at the section root.
export async function generateMetadata({
  params,
}: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const { slug } = await params;
  return {
    title: "Contact | Sushant Rana",
    description: "Book a free 30-minute consultation.",
    robots: { index: false, follow: true },
    alternates: { canonical: catchAllCanonical("contact", slug) },
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
  const name = slug?.length ? titleCase(slug[slug.length - 1]) : "Contact";
  return (
    <ComingSoon
      pageName={name}
      crumbs={sectionTrail({ label: "Contact", base: "contact" }, slug)}
    />
  );
}
