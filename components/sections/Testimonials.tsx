"use client";

import Reveal from "../Reveal";
import { TESTIMONIALS as QUOTES } from "@/lib/testimonials";

function Card({ q }: { q: (typeof QUOTES)[0] }) {
  return (
    <figure className="mx-3 flex w-[86vw] max-w-[460px] shrink-0 flex-col self-stretch rounded-3xl border border-[var(--color-line)] bg-white p-8">
      <span className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
        {q.industry}
      </span>
      <blockquote className="mt-4 flex-1 text-base leading-relaxed text-body">
        <p>“{q.quote}”</p>
      </blockquote>
      <hr className="my-6 border-[var(--color-line)]" />
      <figcaption>
        <div className="font-[family-name:var(--font-display)] font-bold text-ink">{q.name}</div>
        <div className="text-sm text-muted">{q.company}</div>
      </figcaption>
    </figure>
  );
}

export default function Testimonials() {
  return (
    <section className="section overflow-hidden">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">Client feedback</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Clear, fast, <span className="text-orange">accountable.</span>
          </h2>
          <p className="mt-4 max-w-2xl text-sm text-muted">
            Feedback written from the outcomes of each project listed on this
            site. Clients&apos; own words replace these as each one approves.
          </p>
        </Reveal>
      </div>

      {/* full-width marquee of cards */}
      <div className="marquee mt-12">
        <div className="marquee__track" style={{ ["--dur" as string]: "90s" }}>
          {[...QUOTES, ...QUOTES].map((q, i) => (
            <Card key={i} q={q} />
          ))}
        </div>
      </div>
    </section>
  );
}
