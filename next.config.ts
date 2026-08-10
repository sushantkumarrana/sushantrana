import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async redirects() {
    return [
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
