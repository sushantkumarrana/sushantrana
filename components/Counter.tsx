"use client";

import { useEffect, useState } from "react";
import { useInViewport } from "./useInViewport";

/**
 * Counts up to `value` when scrolled into view. `prefix`/`suffix` wrap it
 * (e.g. ₹ / L+ / × ). Non-numeric values (e.g. "AI") render as-is.
 */
export default function Counter({
  value,
  prefix = "",
  suffix = "",
  decimals = 0,
  duration = 1400,
}: {
  value: number | string;
  prefix?: string;
  suffix?: string;
  decimals?: number;
  duration?: number;
}) {
  const { ref, inView } = useInViewport<HTMLSpanElement>();
  const [n, setN] = useState(0);

  const numeric = typeof value === "number";

  useEffect(() => {
    if (!inView || !numeric) return;
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setN(value as number);
      return;
    }
    let raf = 0;
    const start = performance.now();
    const tick = (t: number) => {
      const p = Math.min(1, (t - start) / duration);
      const eased = 1 - Math.pow(1 - p, 3);
      setN((value as number) * eased);
      if (p < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [inView, numeric, value, duration]);

  return (
    <span ref={ref} className="tabular-nums">
      {numeric ? `${prefix}${n.toFixed(decimals)}${suffix}` : (value as string)}
    </span>
  );
}
