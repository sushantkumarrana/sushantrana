"use client";

import { useEffect, useState } from "react";
import { useInViewport } from "../useInViewport";

/**
 * Scroll-triggered animation primitives for the illustrated panels: numbers
 * count up, bars grow from zero, charts rise from the baseline. Each waits
 * until its own element is on screen, and each honours prefers-reduced-motion
 * by jumping straight to the final value.
 */

const reduced = () =>
  typeof window !== "undefined" &&
  window.matchMedia("(prefers-reduced-motion: reduce)").matches;

/** Eased 0 → 1 progress once `start` flips true. */
function useProgress(start: boolean, duration = 1300) {
  const [p, setP] = useState(0);

  useEffect(() => {
    if (!start) return;
    let raf = 0;
    if (reduced()) {
      // Jump to the end, but on the next frame rather than synchronously —
      // a setState in the effect body forces a second render pass.
      raf = requestAnimationFrame(() => setP(1));
      return () => cancelAnimationFrame(raf);
    }
    const t0 = performance.now();
    const tick = (t: number) => {
      const x = Math.min(1, (t - t0) / duration);
      setP(1 - Math.pow(1 - x, 3));
      if (x < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [start, duration]);

  return p;
}

/**
 * Counts a display string up from zero, keeping whatever wraps the number.
 * "72%" counts to 72, "4.2x" to 4.2 with one decimal, "₹1,499" keeps its
 * prefix. A value with no digits ("Fast", "Mobile") renders unchanged.
 */
export function AnimatedNumber({ value, duration }: { value: string; duration?: number }) {
  const { ref, inView } = useInViewport<HTMLSpanElement>();
  const p = useProgress(inView, duration);

  const m = /^([^\d]*)([\d,]+(?:\.\d+)?)(.*)$/.exec(value);
  if (!m) return <span>{value}</span>;

  const [, prefix, digits, suffix] = m;
  const target = Number(digits.replace(/,/g, ""));
  const decimals = digits.includes(".") ? digits.split(".")[1].length : 0;
  const grouped = digits.includes(",");
  const current = target * p;

  return (
    <span ref={ref} className="tabular-nums">
      {prefix}
      {grouped
        ? current.toLocaleString("en-IN", {
            minimumFractionDigits: decimals,
            maximumFractionDigits: decimals,
          })
        : current.toFixed(decimals)}
      {suffix}
    </span>
  );
}

/** Vertical bar chart that rises from the baseline. One observer for the set,
 *  rather than one per bar. */
export function GrowBars({ values, className = "" }: { values: number[]; className?: string }) {
  const { ref, inView } = useInViewport<HTMLDivElement>();
  return (
    <div ref={ref} className={`flex items-end gap-1.5 ${className}`} aria-hidden>
      {values.map((h, i) => (
        <span
          key={i}
          className="flex-1 rounded-t bg-gradient-to-t from-orange/25 to-orange transition-[height] duration-[1100ms] ease-[cubic-bezier(0.16,1,0.3,1)]"
          style={{
            height: inView ? `${h}%` : "0%",
            // a short cascade left to right reads as the chart drawing itself
            transitionDelay: `${i * 55}ms`,
          }}
        />
      ))}
    </div>
  );
}

/** Horizontal fill that runs out to `width` (a percentage string). */
export function GrowBar({
  width,
  className = "",
  delay = 0,
}: {
  width: string;
  className?: string;
  delay?: number;
}) {
  const { ref, inView } = useInViewport<HTMLSpanElement>();
  return (
    <span
      ref={ref}
      aria-hidden
      className={`block h-full rounded-full bg-orange transition-[width] duration-[1200ms] ease-[cubic-bezier(0.16,1,0.3,1)] ${className}`}
      style={{ width: inView ? width : "0%", transitionDelay: `${delay}ms` }}
    />
  );
}
