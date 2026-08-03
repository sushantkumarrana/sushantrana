"use client";

import Reveal from "./Reveal";

/** About Me — centered title + landscape banner with a faint marquee running
 *  BEHIND it, edge-to-edge (Agero "What we do" style), then the paragraph. */
export default function AboutMe() {
  return (
    <section id="about" className="section overflow-hidden">
      <div className="wrap-wide text-center">
        <Reveal>
          <span className="script-label">About Me</span>
          <h2 className="mt-4 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink">
            What I actually do
          </h2>
        </Reveal>
      </div>

      {/* banner with faint full-width marquee behind */}
      <div className="relative mt-8 flex items-center justify-center">
        {/* full-viewport-width faint marquee */}
        <div className="marquee pointer-events-none absolute left-1/2 top-1/2 w-screen -translate-x-1/2 -translate-y-1/2" aria-hidden>
          <div className="marquee__track" style={{ ["--dur" as string]: "50s" }}>
            {Array.from({ length: 8 }).map((_, i) => (
              <span
                key={i}
                className="mx-6 font-[family-name:var(--font-display)] text-[clamp(3rem,12vw,9rem)] font-extrabold leading-none text-orange"
              >
                Revenue Systems
              </span>
            ))}
          </div>
        </div>

        <Reveal delay={0.1} className="relative z-10 w-[90%] max-w-2xl">
          <div className="overflow-hidden rounded-3xl border border-[var(--color-line)] shadow-xl">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src="/about/about.png" alt="Sushant Rana" className="w-full" />
          </div>
        </Reveal>
      </div>

      <div className="wrap-wide text-center">
        <Reveal delay={0.15}>
          <p className="mx-auto mt-8 max-w-3xl text-lg text-body">
            I&apos;m Sushant Rana <span className="font-semibold text-orange">(Business Growth Consultant)</span>.
            I build revenue systems that combine business strategy, performance
            marketing, tracking + AI automation, and conversion-focused funnels
            into one scalable growth engine. Every engagement is senior-led and
            designed to help businesses generate predictable growth, improve
            operational efficiency, and maximize return on every marketing
            investment. Backed by 8+ years of experience across four global markets.
          </p>
        </Reveal>
      </div>
    </section>
  );
}
