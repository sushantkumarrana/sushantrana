/**
 * Single source of truth for the canonical origin.
 *
 * Every canonical, JSON-LD @id, sitemap <loc> and robots.txt Host must resolve
 * to this exact origin: https, apex (no www), no trailing components. Anything
 * arriving on www is 301'd here by the redirect rule in next.config.ts.
 */
export const SITE_URL = "https://sushantrana.com";

/**
 * Builds an absolute canonical URL for a route.
 *
 * The site runs with Next's default trailing-slash behaviour: `/services/`
 * 308s to `/services`, so canonicals are slash-less throughout — including the
 * homepage, which Next's metadata resolver normalises to a bare origin. The
 * sitemap and JSON-LD go through this same helper so all three emit a
 * byte-identical string; a stray slash in only one of them reads as a mismatch.
 */
export function canonicalUrl(path = "/"): string {
  return `${SITE_URL}${`/${path}`.replace(/\/+/g, "/").replace(/\/+$/, "")}`;
}

/**
 * Canonical for an optional catch-all route: joins the section with whatever
 * slug segments were matched, so /services/google-ads self-references rather
 * than pointing every placeholder at the section root.
 */
export function catchAllCanonical(section: string, slug?: string[]): string {
  return canonicalUrl([section, ...(slug ?? [])].join("/"));
}
