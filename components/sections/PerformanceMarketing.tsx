"use client";

import { motion } from "framer-motion";
import Reveal from "../Reveal";
import Counter from "../Counter";
import { useInViewport } from "../useInViewport";

const platforms = ["Google Ads", "Meta Ads", "LinkedIn Ads", "TikTok Ads", "Snapchat Ads", "Microsoft Ads", "Amazon Ads"];
const bars = [
  { label: "High-intent search", w: 92 },
  { label: "Paid social & creative", w: 84 },
  { label: "Retargeting & nurture", w: 76 },
  { label: "Measurement & CRO", w: 88 },
];
const chart = [30, 38, 45, 52, 61, 73, 88, 100];

function RankBar({ label, w, i }: { label: string; w: number; i: number }) {
  const { ref, inView } = useInViewport<HTMLDivElement>();
  return (
    <div ref={ref}>
      <div className="mb-2 flex justify-between text-sm">
        <span className="font-[family-name:var(--font-display)] font-semibold text-ink">{label}</span>
        <span className="font-semibold text-orange">{w}%</span>
      </div>
      <div className="h-3 overflow-hidden rounded-full bg-black/5">
        <motion.div
          className="h-full rounded-full bg-orange"
          initial={{ width: 0 }}
          animate={inView ? { width: `${w}%` } : {}}
          transition={{ duration: 1.1, delay: i * 0.1, ease: [0.16, 1, 0.3, 1] }}
        />
      </div>
    </div>
  );
}

function GrowthChart() {
  const { ref, inView } = useInViewport<HTMLDivElement>();
  return (
    <div ref={ref} className="flex h-44 items-end gap-2">
      {chart.map((h, i) => (
        <motion.div
          key={i}
          className={`flex-1 rounded-t-lg ${i < 3 ? "bg-black/15" : "bg-orange"}`}
          initial={{ height: 0 }}
          animate={inView ? { height: `${h}%` } : {}}
          transition={{ duration: 0.9, delay: i * 0.08, ease: [0.16, 1, 0.3, 1] }}
        />
      ))}
    </div>
  );
}

export default function PerformanceMarketing() {
  return (
    <section className="section">
      <div className="wrap-wide">
        <Reveal className="text-center">
          <span className="script-label">Performance marketing</span>
          <h2 className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Paid channels that <span className="text-orange">pay back</span>
          </h2>
          <p className="mx-auto mt-4 max-w-2xl text-muted">
            Managed across the platforms your buyers actually use. Budgets tracked to the rupee and dollar. Lead quality over lead volume.
          </p>
        </Reveal>

        {/* platform marquee */}
        <div className="marquee mt-10">
          <div className="marquee__track" style={{ ["--dur" as string]: "28s" }}>
            {[...platforms, ...platforms].map((p, i) => (
              <span key={i} className="mx-3 rounded-full border border-[var(--color-line)] bg-white px-6 py-3 font-[family-name:var(--font-display)] text-sm font-semibold text-ink">
                {p}
              </span>
            ))}
          </div>
        </div>

        {/* number tiles */}
        <div className="mt-12 grid grid-cols-2 gap-4 md:grid-cols-4">
          {[
            { v: 4, dec: 0, suf: "×", label: "Best B2B ROAS" },
            { v: 50, pre: "₹", suf: "L+", label: "Ad spend managed" },
            { v: 4, suf: "", label: "Markets served" },
            { v: 92, suf: "%", label: "High-intent focus" },
          ].map((s, i) => (
            <Reveal key={i} delay={i * 0.06}>
              <div className="card p-6 text-center">
                <div className="text-grad font-[family-name:var(--font-display)] text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold leading-none">
                  <Counter value={s.v} decimals={s.dec ?? 0} prefix={s.pre ?? ""} suffix={s.suf} />
                </div>
                <div className="mt-2 text-xs font-semibold uppercase tracking-wide text-muted">{s.label}</div>
              </div>
            </Reveal>
          ))}
        </div>

        {/* split: copy + animated graphs */}
        <div className="mt-8 grid gap-6 lg:grid-cols-2">
          <Reveal className="card flex flex-col p-8">
            <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
              ₹50L+ managed · CAD $9,000 &amp; AED 10,000 monthly
            </p>
            <h3 className="mt-3 text-2xl font-extrabold text-ink">
              Where the budget goes is an output of research, not habit.
            </h3>
            <p className="mt-4 text-body">
              Search captures existing demand. Social creates it. Every campaign optimises toward qualified conversations and measured revenue, with your CRM as the source of truth.
            </p>
            <ul className="mt-6 grid gap-3">
              {[
                "Qualified conversations over raw clicks",
                "Your CRM is the single source of truth",
                "Budget reallocated to winners, weekly",
                "Creative tested on velocity, not opinion",
              ].map((t) => (
                <li key={t} className="flex items-start gap-3 text-sm font-medium text-ink">
                  <span className="mt-0.5 grid h-5 w-5 shrink-0 place-items-center rounded-full bg-orange/10 text-orange">
                    <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 4 4L19 7" /></svg>
                  </span>
                  {t}
                </li>
              ))}
            </ul>
            <div className="mt-auto pt-6">
              <a href="#contact" className="inline-flex items-center gap-2 font-[family-name:var(--font-display)] text-sm font-semibold text-orange transition hover:gap-3">
                See the full approach
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </a>
            </div>
          </Reveal>

          <Reveal delay={0.1} className="card p-8">
            <div className="grid gap-5">
              {bars.map((b, i) => (
                <RankBar key={b.label} label={b.label} w={b.w} i={i} />
              ))}
            </div>
            <div className="mt-8 border-t border-[var(--color-line)] pt-6">
              <p className="mb-4 font-[family-name:var(--font-display)] text-sm font-semibold text-ink">Pipeline momentum</p>
              <GrowthChart />
            </div>
          </Reveal>
        </div>
      </div>
    </section>
  );
}
