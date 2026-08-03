"use client";

/** Full-width straight marquee band (black or orange) used as a divider
 *  between sections. Pauses on hover. */
export default function StraightMarquee({
  items,
  variant = "ink",
  dur = 40,
  reverse = false,
}: {
  items: string[];
  variant?: "ink" | "orange";
  dur?: number;
  reverse?: boolean;
}) {
  const bg = variant === "orange" ? "bg-orange text-white" : "bg-[#0a0a0a] text-white";
  const base = Array.from({ length: 4 }).flatMap(() => items);
  return (
    <div className={`marquee py-2.5 ${bg} ${reverse ? "marquee--rev" : ""}`}>
      <div className="marquee__track" style={{ ["--dur" as string]: `${dur}s` }}>
        {[...base, ...base].map((t, i) => (
          <span
            key={i}
            className="mx-4 inline-flex items-center gap-4 whitespace-nowrap font-[family-name:var(--font-display)] text-[clamp(0.85rem,1.6vw,1.25rem)] font-bold"
          >
            {t}
            <span className="opacity-70">✦</span>
          </span>
        ))}
      </div>
    </div>
  );
}
