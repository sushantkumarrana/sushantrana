"use client";

import Reveal from "../Reveal";
import Placeholder from "../Placeholder";

// image tiles only — the pain-point text lives inside your screenshot images
const TILES = [
  { label: "Budget allocation", ratio: "4/3", span: "" },
  { label: "Reliable support team", ratio: "4/3", span: "" },
  { label: "Performance partner", ratio: "4/3", span: "" },
  { label: "Sales plateaued", ratio: "21/9", span: "sm:col-span-2" },
  { label: "Supportive team", ratio: "4/3", span: "" },
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
          <div className="grid grid-cols-2 gap-4 sm:grid-cols-3">
            {TILES.map((t, i) => (
              <Placeholder key={t.label} ratio={t.ratio} label={t.label} seed={i} tilt={false} className={t.span} />
            ))}
          </div>
        </Reveal>
      </div>
    </section>
  );
}
