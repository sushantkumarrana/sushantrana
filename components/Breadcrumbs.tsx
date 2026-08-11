import Link from "next/link";
import { ChevronRight } from "lucide-react";
import { canonicalUrl } from "@/lib/seo";

export type Crumb = { label: string; href?: string };

const titleCase = (s: string) =>
  s.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());

/**
 * Trail for a section catch-all: Services → Google Ads for /services/google-ads.
 *
 * Every matched segment becomes a crumb, so a nested URL reads as a full path
 * rather than collapsing to the section root. The final segment is the current
 * page and gets no href.
 */
export function sectionTrail(
  section: { label: string; base: string },
  slug?: string[]
): Crumb[] {
  const segments = slug ?? [];
  return [
    { label: section.label, href: segments.length ? `/${section.base}` : undefined },
    ...segments.map((s, i) => ({
      label: titleCase(s),
      href:
        i < segments.length - 1
          ? `/${section.base}/${segments.slice(0, i + 1).join("/")}`
          : undefined,
    })),
  ];
}

/**
 * Small breadcrumb trail, shown at the top of every page below the home page.
 *
 * Emits its own BreadcrumbList JSON-LD so the markup and what Google reads can
 * never disagree — pass `jsonLd={false}` on pages that already declare the list
 * inside a larger @graph (the blog article does).
 *
 * "Home" is prepended automatically; pass only the trail after it. The last
 * crumb is the current page and is never a link.
 */
export default function Breadcrumbs({
  trail,
  jsonLd = true,
  className = "",
}: {
  trail: Crumb[];
  jsonLd?: boolean;
  className?: string;
}) {
  const items: Crumb[] = [{ label: "Home", href: "/" }, ...trail];

  const data = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    itemListElement: items.map((c, i) => ({
      "@type": "ListItem",
      position: i + 1,
      name: c.label,
      ...(c.href ? { item: canonicalUrl(c.href) } : {}),
    })),
  };

  return (
    <>
      {jsonLd && (
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
        />
      )}
      <nav aria-label="Breadcrumb" className={className}>
        <ol className="flex flex-wrap items-center gap-1 text-xs text-muted">
          {items.map((c, i) => {
            const last = i === items.length - 1;
            return (
              <li key={`${c.label}-${i}`} className="flex items-center gap-1">
                {i > 0 && (
                  <ChevronRight aria-hidden className="h-3.5 w-3.5 shrink-0 opacity-50" />
                )}
                {last || !c.href ? (
                  // The current page: marked for assistive tech, and truncated
                  // so a long article title can't wrap the trail onto 3 lines.
                  <span aria-current="page" className="max-w-[52vw] truncate font-semibold text-ink sm:max-w-none">
                    {c.label}
                  </span>
                ) : (
                  <Link href={c.href} className="transition hover:text-orange">
                    {c.label}
                  </Link>
                )}
              </li>
            );
          })}
        </ol>
      </nav>
    </>
  );
}
