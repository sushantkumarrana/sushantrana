"use client";

import { useEffect, useRef, useState } from "react";

/**
 * Native IntersectionObserver trigger. framer-motion's whileInView/useInView
 * proved unreliable on Next 16 + React 19 here (stuck hidden), so we drive the
 * trigger ourselves and let Framer Motion handle the animation via `animate`.
 */
export function useInViewport<T extends HTMLElement>(
  once = true,
  rootMargin = "0px 0px -5% 0px"
) {
  const ref = useRef<T>(null);
  const [inView, setInView] = useState(false);

  useEffect(() => {
    const el = ref.current;
    if (!el) return;
    if (typeof IntersectionObserver === "undefined") {
      setInView(true);
      return;
    }
    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setInView(true);
          if (once) io.disconnect();
        } else if (!once) {
          setInView(false);
        }
      },
      { rootMargin, threshold: 0.1 }
    );
    io.observe(el);
    return () => io.disconnect();
  }, [once, rootMargin]);

  return { ref, inView };
}
