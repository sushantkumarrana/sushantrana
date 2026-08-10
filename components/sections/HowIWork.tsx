"use client";

import { motion } from "framer-motion";
import { useInViewport } from "../useInViewport";
import Reveal from "../Reveal";

const STEPS = [
  { n: "01", kicker: "30-minute consultation", title: "Discovery", desc: "Understand the business problem, review current marketing, and identify the gaps worth closing." },
  { n: "02", kicker: "One week", title: "Research", desc: "Website, brand, accounts, customer journey, and competitors. Find the weaknesses before recommending anything." },
  { n: "03", kicker: "Fix the foundations", title: "Implementation", desc: "Remove bottlenecks in priority order: branding, systems, and campaigns, before spending on scale." },
  { n: "04", kicker: "Compound", title: "Growth", desc: "Launch the complete revenue system: traffic, conversion, follow-up, and reporting, built for sustainable scale." },
];

function Step({ step, fromRight, i }: { step: (typeof STEPS)[0]; fromRight: boolean; i: number }) {
  const { ref, inView } = useInViewport<HTMLDivElement>();
  return (
    <div ref={ref} className={`flex ${fromRight ? "md:justify-end" : "md:justify-start"}`}>
      <motion.div
        initial={{ opacity: 0, x: fromRight ? 80 : -80 }}
        animate={inView ? { opacity: 1, x: 0 } : {}}
        transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
        className="relative w-full rounded-3xl border border-[var(--color-line)] bg-white p-8 md:w-[52%]"
      >
        <div className="mb-4 flex items-center gap-4">
          <span className="grid h-12 w-12 place-items-center rounded-2xl bg-orange font-[family-name:var(--font-display)] font-extrabold text-white">
            {step.n}
          </span>
          <span className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
            {step.kicker}
          </span>
        </div>
        <h3 className="text-2xl font-extrabold text-ink">{step.title}</h3>
        <p className="mt-3 text-body">{step.desc}</p>
      </motion.div>
    </div>
  );
}

export default function HowIWork() {
  return (
    <section className="section">
      <div className="wrap-wide text-center">
        <Reveal>
          <span className="script-label">How I work</span>
          <h2 className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            A process with <span className="text-orange">no mystery</span> in it
          </h2>
        </Reveal>
      </div>

      <div className="wrap relative mt-16">
        {/* center line */}
        <div className="absolute left-1/2 top-0 hidden h-full w-0.5 -translate-x-1/2 bg-gradient-to-b from-orange/0 via-orange to-orange/0 md:block" />
        <div className="flex flex-col gap-10 md:gap-16">
          {STEPS.map((s, i) => (
            <Step key={s.n} step={s} fromRight={i % 2 === 1} i={i} />
          ))}
        </div>
      </div>
    </section>
  );
}
