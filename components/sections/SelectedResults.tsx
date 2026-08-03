"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Reveal from "../Reveal";

type Tag = "performance" | "automation" | "web";
const CASES: {
  tag: Tag;
  industry: string;
  name: string;
  metrics: { v: string; l: string }[];
  challenge: string;
  solution: string;
}[] = [
  {
    tag: "performance", industry: "Manufacturing · B2B",
    name: "Industrial equipment maker turns dealer enquiries into a pipeline",
    metrics: [{ v: "11.2×", l: "ROAS" }, { v: "B2B", l: "Search-led" }, { v: "100%", l: "Pipeline visibility" }],
    challenge: "Relied on trade shows and word of mouth. Enquiries were unpredictable and sales had no visibility on the next order.",
    solution: "Positioned around lead time and certification, built search-led demand on Google & Microsoft Ads, LinkedIn retargeting, and a scored CRM pipeline.",
  },
  {
    tag: "performance", industry: "Healthcare",
    name: "Multi-location clinic fills its calendar without discounting",
    metrics: [{ v: "-47%", l: "Cost / appointment" }, { v: "+33%", l: "Show-up rate" }, { v: "1Q", l: "To results" }],
    challenge: "Bookings depended on referrals. A previous agency generated calls, but mostly price shoppers who never showed.",
    solution: "Shifted from symptom to treatment-decision keywords, call tracking, per-branch extensions, and WhatsApp booking + reminder automation.",
  },
  {
    tag: "automation", industry: "Education",
    name: "Training institute doubles qualified admissions enquiries",
    metrics: [{ v: "2.8×", l: "More MQLs" }, { v: "-38%", l: "Cost / enrolment" }, { v: "5 min", l: "Lead routing" }],
    challenge: "Spent heavily on Meta but counsellors said the leads never answered the phone.",
    solution: "Lead scoring and qualification at the form level, Meta lead-gen with qualifying forms, and CRM automation routing hot leads within five minutes.",
  },
  {
    tag: "performance", industry: "SaaS · B2B",
    name: "SaaS platform moves from founder-led sales to inbound demos",
    metrics: [{ v: "Weekly", l: "Demo pipeline" }, { v: "Stable", l: "CAC" }, { v: "Inbound", l: "Engine" }],
    challenge: "Had product-market fit, but every demo was hand-won by the founder on LinkedIn.",
    solution: "Built a demand engine around manual reporting pain, LinkedIn thought-leader ads, category search, and HubSpot trial-nurture workflows.",
  },
  {
    tag: "web", industry: "Construction",
    name: "Commercial contractor wins larger tenders with a credibility engine",
    metrics: [{ v: "Bigger", l: "Tenders won" }, { v: "New", l: "Capability site" }, { v: "PMC", l: "Targeted" }],
    challenge: "A capable contractor kept losing large tenders to less-qualified firms with slicker positioning.",
    solution: "Rebuilt the site around proof and capability, developer & PMC targeting, and tender-stage remarketing to stay top of mind.",
  },
];

const FILTERS: { key: "all" | Tag; label: string }[] = [
  { key: "all", label: "All" },
  { key: "performance", label: "Performance" },
  { key: "automation", label: "Automation" },
  { key: "web", label: "Web" },
];

export default function SelectedResults() {
  const [filter, setFilter] = useState<"all" | Tag>("all");
  const shown = CASES.filter((c) => filter === "all" || c.tag === filter);

  return (
    <section id="results" className="section">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">Selected results</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Fewer campaigns. <span className="text-orange">Bigger outcomes.</span>
          </h2>
          <p className="mt-4 max-w-xl text-muted">A sample of engagements across Australia, Canada, the USA, and India.</p>
        </Reveal>

        <div className="mt-8 flex flex-wrap gap-2.5">
          {FILTERS.map((f) => (
            <button
              key={f.key}
              onClick={() => setFilter(f.key)}
              aria-pressed={filter === f.key}
              className={`rounded-full px-5 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold transition ${
                filter === f.key ? "bg-ink text-white" : "border border-[var(--color-line)] bg-white/60 text-body hover:text-ink"
              }`}
            >
              {f.label}
            </button>
          ))}
        </div>

        <motion.div layout className="mt-8 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <AnimatePresence mode="popLayout">
            {shown.map((c) => (
              <motion.article
                key={c.name}
                layout
                initial={{ opacity: 0, scale: 0.96 }}
                animate={{ opacity: 1, scale: 1 }}
                exit={{ opacity: 0, scale: 0.96 }}
                transition={{ duration: 0.35 }}
                className="card flex flex-col p-7"
              >
                <span className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                  {c.industry}
                </span>
                <h3 className="mt-3 text-lg font-extrabold leading-snug text-ink">{c.name}</h3>

                <div className="my-5 grid grid-cols-3 gap-2 border-y border-[var(--color-line)] py-4">
                  {c.metrics.map((m) => (
                    <div key={m.l} className="text-center">
                      <div className="font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">{m.v}</div>
                      <div className="mt-1 text-[0.66rem] leading-tight text-muted">{m.l}</div>
                    </div>
                  ))}
                </div>

                <div className="space-y-3 text-sm">
                  <div>
                    <p className="font-[family-name:var(--font-display)] text-[0.7rem] font-bold uppercase tracking-wider text-muted">The challenge</p>
                    <p className="mt-1 text-body">{c.challenge}</p>
                  </div>
                  <div>
                    <p className="font-[family-name:var(--font-display)] text-[0.7rem] font-bold uppercase tracking-wider text-muted">The solution</p>
                    <p className="mt-1 text-body">{c.solution}</p>
                  </div>
                </div>

                <a href="#" className="mt-6 inline-flex items-center gap-2 font-[family-name:var(--font-display)] text-sm font-semibold text-orange transition hover:gap-3">
                  Read full case study
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
                </a>
              </motion.article>
            ))}
          </AnimatePresence>
        </motion.div>
      </div>
    </section>
  );
}
