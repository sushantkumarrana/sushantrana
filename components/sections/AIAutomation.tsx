"use client";

import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import Reveal from "../Reveal";
import Counter from "../Counter";
import { useInViewport } from "../useInViewport";

const capabilities = [
  "CRM automation", "Lead scoring", "Sales pipeline automation",
  "AI assistants", "WhatsApp automation", "Automated reporting systems",
  "Email nurture sequences", "Meeting scheduling", "Chatbots & live chat",
  "Data enrichment",
];

const stages = [
  { h: "New", card: "Inbound lead", dot: "bg-black/30" },
  { h: "Scored", card: "Qualified · 82", dot: "bg-orange" },
  { h: "Qualified", card: "Routed to sales", dot: "bg-green-500" },
];

const activity = [
  { t: "Lead scored 82/100", s: "just now" },
  { t: "WhatsApp auto-reply sent", s: "2s ago" },
  { t: "Routed to sales rep", s: "5s ago" },
  { t: "Weekly report generated", s: "1m ago" },
];

export default function AIAutomation() {
  const { ref, inView } = useInViewport<HTMLDivElement>();
  const [stage, setStage] = useState(0);

  useEffect(() => {
    if (!inView) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const t = setInterval(() => setStage((s) => (s + 1) % stages.length), 1600);
    return () => clearInterval(t);
  }, [inView]);

  return (
    <section className="section">
      <div className="wrap-wide grid items-stretch gap-12 lg:grid-cols-2">
        <Reveal>
          <span className="script-label">AI automation</span>
          <h2 className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)]">
            The work that runs <span className="text-orange">while you sleep</span>
          </h2>
          <p className="mt-4 max-w-lg text-muted">
            Automation that scores leads, moves pipelines, and reports itself — so nothing leaks between marketing and sales.
          </p>
          <ul className="mt-8 grid gap-3 sm:grid-cols-2">
            {capabilities.map((c) => (
              <li key={c} className="flex items-center gap-3 rounded-xl border border-[var(--color-line)] bg-white px-4 py-3 font-medium text-ink">
                <span className="grid h-7 w-7 place-items-center rounded-lg bg-orange/10 text-orange">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 4 4L19 7" /></svg>
                </span>
                {c}
              </li>
            ))}
          </ul>
        </Reveal>

        {/* live pipeline demo */}
        <Reveal delay={0.1}>
          <div ref={ref} className="card flex h-full flex-col overflow-hidden">
            <div className="flex items-center gap-2 border-b border-[var(--color-line)] bg-black/[0.03] px-5 py-3 text-xs font-semibold uppercase tracking-wide text-muted">
              <span className="h-2 w-2 rounded-full bg-orange" /> Lead pipeline · system demo
            </div>

            {/* board with a deal moving through stages */}
            <div className="grid grid-cols-3 gap-2 p-3 sm:gap-3 sm:p-5">
              {stages.map((col, ci) => (
                <div key={col.h} className="rounded-xl bg-black/[0.03] p-1.5 sm:rounded-2xl sm:p-3">
                  <h4 className="mb-2 text-center text-[0.58rem] font-bold uppercase tracking-wide text-muted sm:mb-3 sm:text-[0.68rem]">{col.h}</h4>
                  <div className="flex items-center gap-1.5 rounded-lg border border-[var(--color-line)] bg-white px-2 py-2 text-[0.7rem] font-semibold leading-tight text-ink shadow-sm sm:gap-2 sm:rounded-xl sm:px-3 sm:py-2.5 sm:text-sm">
                    <span className={`h-1.5 w-1.5 shrink-0 rounded-full ${col.dot} sm:h-2 sm:w-2`} />
                    {col.card}
                  </div>
                  {/* the animated deal that hops between columns */}
                  <div className="relative mt-2 h-9">
                    {stage === ci && (
                      <motion.div
                        layoutId="deal"
                        transition={{ type: "spring", stiffness: 200, damping: 22 }}
                        className="absolute inset-x-0 flex items-center gap-1.5 rounded-lg bg-orange px-2 py-1.5 text-[0.7rem] font-semibold leading-tight text-white shadow-lg sm:gap-2 sm:rounded-xl sm:px-3 sm:py-2 sm:text-sm"
                      >
                        <span className="h-1.5 w-1.5 shrink-0 rounded-full bg-white sm:h-2 sm:w-2" /> Acme →
                      </motion.div>
                    )}
                  </div>
                </div>
              ))}
            </div>

            {/* metrics */}
            <div className="grid grid-cols-3 gap-px bg-[var(--color-line)]">
              {[
                { v: 128, label: "Leads processed", suf: "" },
                { v: 42, label: "Qualified rate", suf: "%" },
                { v: 5, label: "Response time", suf: " min" },
              ].map((m) => (
                <div key={m.label} className="bg-white py-5 text-center">
                  <div className="font-[family-name:var(--font-display)] text-2xl font-extrabold text-orange">
                    <Counter value={m.v} suffix={m.suf} />
                  </div>
                  <div className="mt-1 text-[0.68rem] text-muted">{m.label}</div>
                </div>
              ))}
            </div>

            {/* activity feed — fills the space, keeps the panel alive */}
            <div className="flex-1 border-t border-[var(--color-line)] p-5">
              <p className="mb-3 text-xs font-bold uppercase tracking-wider text-muted">Automation activity</p>
              <ul className="grid gap-2">
                {activity.map((a, i) => (
                  <li key={a.t} className="flex items-center justify-between rounded-lg bg-black/[0.03] px-3 py-2 text-sm">
                    <span className="flex items-center gap-2 text-ink">
                      <span className="grid h-5 w-5 place-items-center rounded-full bg-orange/10 text-orange">
                        <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 4 4L19 7" /></svg>
                      </span>
                      {a.t}
                    </span>
                    <span className="text-xs text-muted">{a.s}</span>
                  </li>
                ))}
              </ul>
            </div>

            <p className="px-5 pb-4 text-center text-xs text-muted">Illustrative system demo — not live client data.</p>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
