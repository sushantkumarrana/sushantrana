import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async redirects() {
    return [
      // Thank-you pages are named after the form that leads to them, so a
      // GA4 / GTM / Ads conversion can be tied to one form by page path.
      // The old shared-name URLs stay working for anyone with them bookmarked.
      { source: "/thank-you", destination: "/thank-you-consultation", statusCode: 301 },
      {
        source: "/services/shopify-store-development/thank-you",
        destination: "/thank-you-shopify-store-development",
        statusCode: 301,
      },
      {
        source: "/services/website-maintenance/thank-you",
        destination: "/thank-you-website-maintenance",
        statusCode: 301,
      },
      // Canonical host is the apex, https, non-www. Anything arriving on
      // www.sushantrana.com is sent straight to the same path on the apex in a
      // single hop. `statusCode: 301` rather than `permanent: true` because the
      // latter emits 308; 301 is what search consoles and older clients expect
      // for a host change. The `host` condition means this can never loop —
      // the destination host doesn't match the rule.
      {
        source: "/:path*",
        has: [{ type: "host", value: "www.sushantrana.com" }],
        destination: "https://sushantrana.com/:path*",
        statusCode: 301,
      },
    ];
  },
};

export default nextConfig;
