"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Reveal from "../Reveal";

const OLD = [
  "Disconnected tactics, restarted every quarter",
  "Leads that leak between marketing and sales",
  "Guesswork reporting and vanity metrics",
  "Spikes that reset the moment spend stops",
];
const NEW = [
  "One engine: positioning → traffic → conversion → follow-up",
  "Tracked, scored pipelines with no leads leaking",
  "Reporting you can act on, every week",
  "Growth that compounds month over month",
];

export default function RealityOfGrowth() {
  const [tab, setTab] = useState<"old" | "new">("new");
  const items = tab === "old" ? OLD : NEW;

  return (
    <section className="section">
      <div className="wrap text-center">
        <Reveal>
          <span className="script-label">The reality of growth</span>
          <h2 className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Most businesses don&apos;t have a marketing problem.{" "}
            <span className="text-orange">They have a systems problem.</span>
          </h2>
          <p className="mx-auto mt-5 max-w-xl text-muted">
            Campaigns generate spikes. Systems generate compounding revenue.
          </p>
        </Reveal>

        {/* toggle */}
        <div className="mx-auto mt-10 inline-flex gap-2 rounded-full border border-[var(--color-line)] bg-white p-1.5">
          <button
            onClick={() => setTab("old")}
            aria-pressed={tab === "old"}
            className={`rounded-full px-6 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold transition ${
              tab === "old" ? "bg-[#e11900]/10 text-[#c21500]" : "text-muted hover:text-ink"
            }`}
          >
            The scattered way
          </button>
          <button
            onClick={() => setTab("new")}
            aria-pressed={tab === "new"}
            className={`rounded-full px-6 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold transition ${
              tab === "new" ? "bg-orange text-white" : "text-muted hover:text-ink"
            }`}
          >
            The revenue system
          </button>
        </div>

        {/* card */}
        <div className="mx-auto mt-8 max-w-2xl">
          <AnimatePresence mode="wait">
            <motion.div
              key={tab}
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -16 }}
              transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
              className="card p-8 text-left"
            >
              <p className="mb-6 font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                {tab === "old" ? "Scattered campaigns" : "A connected revenue system"}
              </p>
              <ul className="grid gap-4">
                {items.map((it) => (
                  <li key={it} className="flex items-start gap-3 text-ink">
                    <span
                      className={`mt-0.5 grid h-6 w-6 shrink-0 place-items-center rounded-full text-sm ${
                        tab === "old" ? "bg-[#e11900]/10 text-[#c21500]" : "bg-orange/10 text-orange"
                      }`}
                    >
                      {tab === "old" ? "✕" : "✓"}
                    </span>
                    <span className="font-medium">{it}</span>
                  </li>
                ))}
              </ul>
            </motion.div>
          </AnimatePresence>
        </div>
      </div>
    </section>
  );
}
