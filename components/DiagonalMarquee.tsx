"use client";

/**
 * Two marquee ribbons crossing in an X (Agero-style). Small angle + tall band
 * + very wide ribbons so both span edge-to-edge and cross at the centre.
 * Each ribbon pauses on hover.
 */
function Strip({
  items,
  variant,
  rotate,
  z,
  reverse,
  dur,
}: {
  items: string[];
  variant: "orange" | "ink";
  rotate: number;
  z: number;
  reverse?: boolean;
  dur: number;
}) {
  const bg = variant === "orange" ? "bg-orange text-white" : "bg-[#0a0a0a] text-white";
  const base = Array.from({ length: 10 }).flatMap(() => items);
  return (
    <div
      className={`marquee absolute left-1/2 top-1/2 w-[220%] py-2 shadow-xl ${bg} ${reverse ? "marquee--rev" : ""}`}
      style={{ transform: `translate(-50%,-50%) rotate(${rotate}deg)`, zIndex: z, ["--dur" as string]: `${dur}s` }}
    >
      <div className="marquee__track">
        {[...base, ...base].map((t, i) => (
          <span
            key={i}
            className="mx-5 inline-flex items-center gap-5 whitespace-nowrap font-[family-name:var(--font-display)] text-[clamp(0.9rem,1.7vw,1.4rem)] font-bold"
          >
            {t}
            <span className="opacity-70">✦</span>
          </span>
        ))}
      </div>
    </div>
  );
}

export default function DiagonalMarquee() {
  return (
    <div className="relative h-[150px] w-full overflow-hidden md:h-[210px]">
      <Strip
        items={["8+ Years Experience", "4 Markets Served", "Senior-Led", "100% Owned Accounts"]}
        variant="ink"
        rotate={-7}
        z={1}
        dur={110}
      />
      <Strip
        items={["Performance Marketing", "Web Development", "AI Automation", "SEO"]}
        variant="orange"
        rotate={7}
        z={2}
        dur={100}
      />
    </div>
  );
}
