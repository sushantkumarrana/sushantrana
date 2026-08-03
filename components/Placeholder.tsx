"use client";

import { motion } from "framer-motion";

/**
 * Light-theme image placeholder — swap for a real <img>/<Image> later.
 * Neutral light surface + subtle orange accent + "add image" chip + tilt.
 */
export default function Placeholder({
  ratio = "4/3",
  label = "Your image",
  className = "",
  seed = 0,
  tilt = true,
  dark = false,
}: {
  ratio?: string;
  label?: string;
  className?: string;
  seed?: number;
  tilt?: boolean;
  dark?: boolean;
}) {
  const base = dark ? "#0d0d0d" : "#ececec";
  const hue = 18 + (seed % 3) * 4;
  return (
    <motion.div
      className={`group relative overflow-hidden rounded-3xl border ${className}`}
      style={{
        aspectRatio: ratio,
        background: base,
        borderColor: dark ? "rgba(255,255,255,.1)" : "rgba(10,10,10,.1)",
      }}
      whileHover={tilt ? { scale: 1.01 } : undefined}
      transition={{ type: "spring", stiffness: 200, damping: 18 }}
    >
      <div
        className="absolute -left-1/5 -top-1/5 h-2/3 w-2/3 rounded-full opacity-50 blur-3xl"
        style={{ background: `radial-gradient(circle, hsl(${hue} 100% 50% / .35), transparent 65%)` }}
      />
      <div
        className="absolute -bottom-1/5 -right-1/5 h-2/3 w-2/3 rounded-full opacity-30 blur-3xl"
        style={{ background: `radial-gradient(circle, hsl(${hue + 6} 100% 45% / .3), transparent 65%)` }}
      />
      <div
        className="absolute inset-0 opacity-[0.12]"
        style={{
          backgroundImage: `radial-gradient(${dark ? "rgba(255,122,60,.9)" : "rgba(255,77,0,.9)"} 1px, transparent 1px)`,
          backgroundSize: "22px 22px",
        }}
      />
      {label ? (
        <div
          className="absolute left-4 top-4 inline-flex items-center gap-2 rounded-full border px-3 py-1.5 backdrop-blur"
          style={{
            borderColor: dark ? "rgba(255,255,255,.14)" : "rgba(10,10,10,.12)",
            background: dark ? "rgba(0,0,0,.4)" : "rgba(255,255,255,.6)",
          }}
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#ff4d00" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <rect x="3" y="3" width="18" height="18" rx="3" />
            <circle cx="9" cy="9" r="1.6" />
            <path d="m21 15-5-5L5 21" />
          </svg>
          <span className="font-[family-name:var(--font-display)] text-[0.72rem] font-semibold uppercase tracking-wide text-orange">
            {label}
          </span>
        </div>
      ) : null}
    </motion.div>
  );
}
