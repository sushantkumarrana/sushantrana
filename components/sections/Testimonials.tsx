"use client";

import Reveal from "../Reveal";

// NOTE: illustrative — replace with real client quotes/logos when available.
const QUOTES = [
  { industry: "Manufacturing", quote: "Sales finally plans production around a pipeline they can actually see.", name: "R. Mehta", company: "Precision Components Co." },
  { industry: "Healthcare", quote: "Fewer price-shoppers, more booked appointments that actually show up.", name: "Dr. A. Kapoor", company: "Multi-Clinic Group" },
  { industry: "Education", quote: "The leads answer the phone now. Counsellors stopped complaining.", name: "S. Nair", company: "Skill Institute" },
  { industry: "SaaS", quote: "We went from founder-chased demos to a weekly inbound pipeline.", name: "J. Fernandes", company: "Workflow SaaS" },
  { industry: "Fashion & D2C", quote: "Margin-aware paid social replaced the discount spiral entirely.", name: "P. Shah", company: "D2C Label" },
];

function Card({ q }: { q: (typeof QUOTES)[0] }) {
  return (
    <figure className="mx-3 flex w-[86vw] max-w-[440px] shrink-0 flex-col rounded-3xl border border-[var(--color-line)] bg-white p-8">
      <span className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
        {q.industry}
      </span>
      <blockquote className="mt-4 flex-1 font-[family-name:var(--font-display)] text-lg font-medium leading-snug text-ink">
        “{q.quote}”
      </blockquote>
      <hr className="my-6 border-[var(--color-line)]" />
      <figcaption className="flex items-center justify-between gap-4">
        <div>
          <div className="font-[family-name:var(--font-display)] font-bold text-ink">{q.name}</div>
          <div className="text-sm text-muted">{q.company}</div>
        </div>
        <div className="grid h-11 w-20 place-items-center rounded-lg bg-black/5 text-[0.6rem] font-semibold uppercase tracking-wide text-muted">
          logo
        </div>
      </figcaption>
    </figure>
  );
}

export default function Testimonials() {
  return (
    <section className="section overflow-hidden">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">In clients&apos; words</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Clear, fast, <span className="text-orange">accountable.</span>
          </h2>
        </Reveal>
      </div>

      {/* full-width marquee of cards */}
      <div className="marquee mt-12">
        <div className="marquee__track" style={{ ["--dur" as string]: "44s" }}>
          {[...QUOTES, ...QUOTES].map((q, i) => (
            <Card key={i} q={q} />
          ))}
        </div>
      </div>
    </section>
  );
}
