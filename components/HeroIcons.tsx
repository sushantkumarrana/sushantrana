"use client";

/** 4 small floating tool icons in the hero — Google Ads, Meta, Wix, GA4.
 *  Positioned at the corners so they never sit under the headline. */
const ICONS = [
  { f: "google-ads", top: "20%", left: "8%", size: 44, dur: 16, delay: 0, anim: "drift1" },
  { f: "meta", top: "24%", left: "86%", size: 46, dur: 20, delay: 1.5, anim: "drift2" },
  { f: "ga4", top: "66%", left: "10%", size: 42, dur: 18, delay: 0.8, anim: "drift2" },
  { f: "wix", top: "64%", left: "88%", size: 44, dur: 22, delay: 2, anim: "drift1" },
];

export default function HeroIcons() {
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 hidden overflow-hidden md:block">
      {ICONS.map((l, i) => (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          key={i}
          src={`/logos/${l.f}.png`}
          alt=""
          className="absolute select-none opacity-80"
          style={{
            top: l.top,
            left: l.left,
            width: l.size,
            height: l.size,
            objectFit: "contain",
            animation: `${l.anim} ${l.dur}s ease-in-out ${l.delay}s infinite`,
          }}
        />
      ))}
    </div>
  );
}
