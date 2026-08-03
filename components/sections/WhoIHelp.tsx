"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Reveal from "../Reveal";

const INDUSTRIES = [
  { key: "healthcare", label: "Healthcare", desc: "Appointment-driven demand where trust and compliance decide the sale.", points: ["Local + treatment-intent search", "Reminder & no-show automation", "Reputation and review systems"] },
  { key: "education", label: "Education", desc: "Intake-deadline cycles where lead quality beats lead volume.", points: ["Qualified enquiry campaigns", "Counsellor lead scoring", "Nurture to enrolment"] },
  { key: "manufacturing", label: "Manufacturing", desc: "Long B2B cycles where the pipeline must be visible and predictable.", points: ["Specification-intent search", "Procurement retargeting", "Quote-ready funnels"] },
  { key: "saas", label: "SaaS & Tech", desc: "Demand engines that move past founder-led sales to inbound demos.", points: ["Category & competitor search", "Trial nurture automation", "Demo-booking funnels"] },
  { key: "construction", label: "Construction", desc: "Credibility infrastructure that wins larger tenders and projects.", points: ["Capability-led websites", "Developer & PMC targeting", "Tender-stage remarketing"] },
  { key: "fashion", label: "Fashion & D2C", desc: "Escaping the discount spiral with margin-aware paid social.", points: ["Creative-velocity testing", "Catalog by margin", "Retention email flows"] },
  { key: "professional", label: "Professional Services", desc: "Predictable acquisition beyond referrals for high-value services.", points: ["High-intent search", "Case-fit qualification", "CRM follow-up automation"] },
  { key: "realestate", label: "Real Estate", desc: "Site visits and qualified enquiries, not portal lead dumps.", points: ["Budget-qualifying forms", "WhatsApp scheduling", "Cost-per-visit reporting"] },
];

export default function WhoIHelp() {
  const [active, setActive] = useState(0);
  const cur = INDUSTRIES[active];

  return (
    <section className="section">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">Who I help</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Growth systems, tuned to your <span className="text-orange">industry</span>
          </h2>
          <p className="mt-4 max-w-xl text-muted">The mechanics change by market. The discipline doesn&apos;t.</p>
        </Reveal>

        <div className="mt-10 flex flex-wrap gap-2.5">
          {INDUSTRIES.map((ind, i) => (
            <button
              key={ind.key}
              onClick={() => setActive(i)}
              aria-pressed={i === active}
              className={`rounded-full px-5 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold transition ${
                i === active
                  ? "bg-ink text-white"
                  : "border border-[var(--color-line)] bg-white/60 text-body hover:border-ink/30 hover:text-ink"
              }`}
            >
              {ind.label}
            </button>
          ))}
        </div>

        <AnimatePresence mode="wait">
          <motion.div
            key={cur.key}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
            className="mt-8 rounded-3xl border border-[var(--color-line)] bg-white p-8 md:p-10"
          >
            <h3 className="text-2xl font-extrabold text-orange">{cur.label}</h3>
            <p className="mt-3 max-w-2xl text-body">{cur.desc}</p>
            <ul className="mt-6 grid gap-3 sm:grid-cols-3">
              {cur.points.map((p) => (
                <li key={p} className="flex items-center gap-3 font-medium text-ink">
                  <span className="grid h-6 w-6 shrink-0 place-items-center rounded-full bg-orange/10 text-sm text-orange">✓</span>
                  {p}
                </li>
              ))}
            </ul>
          </motion.div>
        </AnimatePresence>
      </div>
    </section>
  );
}
