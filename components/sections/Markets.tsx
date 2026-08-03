"use client";

import Reveal from "../Reveal";

const MARKETS = [
  { c: "Australia", d: "Performance campaigns & growth systems", tag: "AUD budgets" },
  { c: "Canada", d: "Paid media managed in local currency", tag: "CAD $9,000/mo managed" },
  { c: "United States", d: "Cross-border demand generation", tag: "USD campaigns" },
  { c: "India", d: "Full-stack growth engagements", tag: "Home market" },
];

export default function Markets() {
  return (
    <section className="section">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">Where I work</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Growth systems across <span className="text-orange">four markets</span>
          </h2>
          <p className="mt-4 max-w-xl text-muted">Australia, Canada, the USA, and India — with budgets managed in local currency.</p>
        </Reveal>
        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {MARKETS.map((m, i) => (
            <Reveal key={m.c} delay={i * 0.06}>
              <div className="card h-full p-7 transition hover:-translate-y-1">
                <h3 className="text-xl font-extrabold text-ink">{m.c}</h3>
                <p className="mt-3 text-sm text-body">{m.d}</p>
                <p className="mt-6 font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">{m.tag}</p>
              </div>
            </Reveal>
          ))}
        </div>
      </div>
    </section>
  );
}
