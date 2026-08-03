"use client";

import Reveal from "../Reveal";

const ROW1 = [
  { n: "Google Ads", f: "google-ads" }, { n: "Meta Ads", f: "meta" }, { n: "LinkedIn", f: "linkedin" },
  { n: "GA4", f: "ga4" }, { n: "Google Tag Manager", f: "gtm" }, { n: "TikTok", f: "tiktok" },
  { n: "HubSpot", f: "hubspot" }, { n: "Zoho CRM", f: "zoho" }, { n: "Mailchimp", f: "mailchimp" },
];
const ROW2 = [
  { n: "Make", f: "make" }, { n: "Zapier", f: "zapier" }, { n: "WordPress", f: "wordpress" },
  { n: "Webflow", f: "webflow" }, { n: "Wix Studio", f: "wix" }, { n: "Klaviyo", f: "klaviyo" },
  { n: "ChatGPT", f: "chatgpt" }, { n: "Gemini", f: "gemini" },
];

function Row({ items, dur, reverse }: { items: { n: string; f: string }[]; dur: number; reverse?: boolean }) {
  return (
    <div className={`marquee ${reverse ? "marquee--rev" : ""}`}>
      <div className="marquee__track" style={{ ["--dur" as string]: `${dur}s` }}>
        {[...items, ...items].map((t, i) => (
          <span key={i} className="mx-3 inline-flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-6 py-4 font-[family-name:var(--font-display)] font-semibold text-ink">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={`/logos/${t.f}.png`} alt={t.n} className="h-7 w-7 object-contain" />
            {t.n}
          </span>
        ))}
      </div>
    </div>
  );
}

export default function TechStack() {
  return (
    <section className="section">
      <div className="wrap-wide">
        <Reveal className="text-center">
          <span className="script-label">Tech stack</span>
          <h2 className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            The tools behind the <span className="text-orange">system</span>
          </h2>
        </Reveal>
      </div>
      <div className="mt-12 flex flex-col gap-4">
        <Row items={ROW1} dur={38} />
        <Row items={ROW2} dur={32} reverse />
      </div>
    </section>
  );
}
