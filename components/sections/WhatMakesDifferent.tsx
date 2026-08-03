"use client";

import Reveal from "../Reveal";

const VALUES = [
  { t: "Senior-led", d: "You work directly with the person responsible for the result — no account-manager layer, no outsourced pod." },
  { t: "Owns the number", d: "One operator accountable to revenue, not to activity or vanity dashboards." },
  { t: "Transparency", d: "Full access to accounts, data, and reporting. You own everything, always." },
  { t: "Long-term partnerships", d: "Systems compound. I build for the second year, not the first month." },
  { t: "Innovation", d: "New tools earn their place by producing results, not by being new." },
  { t: "Continuous learning", d: "Platforms change monthly. Staying current is part of the job." },
];

function Card({ v }: { v: (typeof VALUES)[0] }) {
  return (
    <div className="card h-full w-full shrink-0 p-7">
      <div className="mb-4 grid h-11 w-11 place-items-center rounded-xl bg-orange/10 text-orange">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m9 12 2 2 4-4" /><circle cx="12" cy="12" r="9" /></svg>
      </div>
      <h3 className="text-lg font-extrabold text-ink">{v.t}</h3>
      <p className="mt-2 text-sm text-body">{v.d}</p>
    </div>
  );
}

export default function WhatMakesDifferent() {
  return (
    <section className="section">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">What makes me different</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            One senior operator who <span className="text-orange">owns the number</span>
          </h2>
        </Reveal>
      </div>

      {/* desktop grid */}
      <div className="wrap-wide mt-12 hidden gap-6 md:grid md:grid-cols-3">
        {VALUES.map((v, i) => (
          <Reveal key={v.t} delay={i * 0.05}>
            <Card v={v} />
          </Reveal>
        ))}
      </div>

      {/* mobile: auto-scrolling marquee (so all cards are discoverable) */}
      <div className="marquee mt-10 md:hidden">
        <div className="marquee__track" style={{ ["--dur" as string]: "36s" }}>
          {[...VALUES, ...VALUES].map((v, i) => (
            <div key={i} className="mx-2 w-[78vw]">
              <Card v={v} />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
