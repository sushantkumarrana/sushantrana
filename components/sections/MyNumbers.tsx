"use client";

import Reveal from "../Reveal";
import Counter from "../Counter";

const STATS = [
  { v: 10, prefix: "$", suffix: "K+", dec: 0, label: "Spent every month across campaigns", w: "lg:w-[68%]", off: "lg:mr-auto" },
  { v: 20, prefix: "", suffix: "+", dec: 0, label: "Happy clients I've helped grow", w: "lg:w-[58%]", off: "lg:ml-auto" },
  { v: 6.2, prefix: "", suffix: "×", dec: 1, label: "Revenue generated every month", w: "lg:w-[60%]", off: "lg:mr-auto" },
];

export default function MyNumbers() {
  return (
    <section className="section">
      <div className="wrap-wide grid gap-12 lg:grid-cols-[0.8fr_1.5fr] lg:items-center">
        <Reveal>
          <span className="script-label">My experience</span>
          <h2 className="mt-4 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink">
            My performance marketing journey by the <span className="text-orange">Numbers</span>
          </h2>
        </Reveal>

        {/* cards on an orange-glow backdrop (like the reference's blue) */}
        <div className="relative">
          <div className="glow-orange pointer-events-none absolute right-0 top-1/2 h-[120%] w-[70%] -translate-y-1/2 opacity-60" />
          <div className="relative flex flex-col gap-5">
            {STATS.map((s, i) => (
              <Reveal key={s.label} delay={i * 0.1} className={`${s.w} ${s.off}`}>
                <div className="flex items-center gap-5 rounded-2xl border-2 border-orange/40 bg-white p-6 shadow-[0_16px_40px_-24px_rgba(255,77,0,0.5)] md:p-8">
                  <div className="shrink-0 font-[family-name:var(--font-display)] text-[clamp(2.4rem,6vw,4.4rem)] font-extrabold leading-none text-ink">
                    <Counter value={s.v} prefix={s.prefix} suffix={s.suffix} decimals={s.dec} />
                  </div>
                  <p className="font-[family-name:var(--font-display)] text-base font-semibold leading-tight text-ink">
                    {s.label}
                  </p>
                </div>
              </Reveal>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
