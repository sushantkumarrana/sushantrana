"use client";

import Reveal from "../Reveal";

// 3 tiles on top + 1 landscape spanning the full width beneath
// alt text matches what each image actually shows
const TOP = [
  { src: "/reports/r1.png", alt: "Looking for a performance partner who truly understands your brand" },
  { src: "/reports/r3.png", alt: "I will be your virtual assistant for performance marketing" },
  { src: "/reports/r4.png", alt: "Unsure how to allocate budget across channels" },
];

export default function WhoICanHelp() {
  return (
    <section className="section">
      <div className="wrap-wide grid gap-10 lg:grid-cols-[0.85fr_1.7fr] lg:items-center">
        <Reveal>
          <span className="script-label">Who I can help</span>
          <h2 className="mt-4 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink">
            I help brands with <span className="text-orange">results,</span> not reports
          </h2>
          <p className="mt-4 max-w-sm text-muted">
            If any of these sound familiar, that&apos;s exactly the gap I close.
          </p>
        </Reveal>

        <Reveal delay={0.1}>
          <div className="grid grid-cols-3 items-start gap-4">
            {TOP.map((t) => (
              <div
                key={t.src}
                className="aspect-square overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white transition duration-300 hover:-translate-y-1 hover:shadow-[0_20px_50px_-24px_rgba(255,77,0,0.45)]"
              >
                {/* Fixed 1:1 box keeps the row level whatever ratio lands here.
                    r1/r4 are square so they fill with zero crop; r3 is 4:5 so it
                    loses a little background top/bottom, never the copy. */}
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img src={t.src} alt={t.alt} className="h-full w-full object-cover" />
              </div>
            ))}

            {/* landscape image extended across all three columns */}
            <div className="col-span-3 overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white transition duration-300 hover:-translate-y-1 hover:shadow-[0_20px_50px_-24px_rgba(255,77,0,0.45)]">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img src="/reports/r2.png" alt="Marketing that actually generates income: paid media, SEO, app ads, creative, tracking and reporting" className="w-full" />
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
