"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Reveal from "../Reveal";

const FAQS = [
  { q: "How is your pricing structured?", a: "Project work is fixed-fee, quoted after the discovery call. Ongoing performance and automation retainers are monthly, scoped to the channels and hours involved. You always know the number before any work starts — no percentage-of-spend surprises." },
  { q: "What happens on the free consultation call?", a: "Thirty minutes. You describe the business, the goal, and what you've tried. I ask questions, look at what you share, and tell you honestly whether I can help. If I can, you get a scoped proposal. If not, I'll point you somewhere useful." },
  { q: "Who does the actual work?", a: "I do. There's no account-manager layer or outsourced pod — you work directly with the person responsible for the result." },
  { q: "How do we communicate during an engagement?", a: "A shared Slack or WhatsApp channel for the day-to-day, a scheduled monthly review call, and email for anything formal. You talk to me directly." },
  { q: "Is there a minimum ad budget you work with?", a: "No hard number, but paid campaigns need enough budget to generate useful data — typically a few hundred dollars a month at minimum. On the call I'll tell you whether your budget fits your goal." },
  { q: "How long does a typical project take?", a: "Research takes about a week. Website builds run two to six weeks. Paid campaigns show meaningful data within four to six weeks and stabilise over a quarter. Anyone promising results in a week is guessing." },
  { q: "Which advertising platforms do you manage?", a: "Google, Meta (Facebook and Instagram), LinkedIn, TikTok, Snapchat, Microsoft, and Amazon. Where to spend comes from where your buyers are — not from a preference for any platform." },
  { q: "Do you build websites, or only run marketing on them?", a: "Both. I build on Shopify, WordPress, Wix Studio, Webflow, and custom stacks — and because I also run campaigns, everything is built to convert and to measure." },
  { q: "What does AI automation actually mean for my business?", a: "Practical workflows: leads scored and routed in minutes, follow-ups that send themselves, WhatsApp answered out of hours, and reports that build themselves. No experimental tools in production." },
  { q: "What does monthly management include?", a: "Campaign optimisation, budget management, creative and copy iterations, landing page recommendations, tracking maintenance, and a monthly report focused on revenue. You keep full ownership and admin access." },
  { q: "How do you measure success?", a: "Revenue metrics agreed up front: qualified leads, CAC, ROAS, and pipeline contribution — pulled from your CRM and analytics, not screenshots of ad dashboards." },
  { q: "What support do I get after a project ends?", a: "Every build ships with documentation and a handover call. Websites include 30 days of post-launch fixes. After that, move to a retainer or engage ad-hoc — nothing is locked in." },
];

function Item({ q, a }: { q: string; a: string }) {
  const [open, setOpen] = useState(false);
  return (
    <div className="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">
      <button
        onClick={() => setOpen((v) => !v)}
        aria-expanded={open}
        className="flex w-full items-center justify-between gap-4 px-6 py-5 text-left"
      >
        <span className="font-[family-name:var(--font-display)] font-semibold text-ink">{q}</span>
        <span className={`grid h-5 w-5 shrink-0 place-items-center rounded-full transition-transform duration-300 ${open ? "rotate-45 bg-orange text-white" : "bg-ink/5 text-ink"}`}>
          <svg width="10" height="10" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><path d="M7 1v12M1 7h12" /></svg>
        </span>
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="overflow-hidden"
          >
            <p className="px-6 pb-6 text-sm text-body">{a}</p>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export default function FAQ() {
  const half = Math.ceil(FAQS.length / 2);
  const cols = [FAQS.slice(0, half), FAQS.slice(half)];
  return (
    <section className="section">
      <div className="wrap-wide">
        <Reveal className="text-center">
          <span className="script-label">FAQ</span>
          <h2 className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Questions before we <span className="text-orange">start</span>
          </h2>
          <p className="mx-auto mt-4 max-w-xl text-muted">Straight answers on scope, pricing, and how engagements run.</p>
        </Reveal>

        <div className="mt-12 grid gap-4 md:grid-cols-2 md:gap-6">
          {cols.map((col, ci) => (
            <div key={ci} className="flex flex-col gap-4">
              {col.map((f) => (
                <Item key={f.q} q={f.q} a={f.a} />
              ))}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
