"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";

// Real rotating CTA questions from the current site; orange = key word.
const QUESTIONS: { pre: string; hot: string; post: string; br?: boolean }[] = [
  { pre: "Why aren’t you getting enough ", hot: "leads", post: "?" },
  { pre: "Why is your ", hot: "ROAS", post: " dropping?", br: true },
  { pre: "Why aren’t your visitors ", hot: "converting", post: "?" },
  { pre: "Why isn’t your business ", hot: "scaling", post: "?" },
];

export default function RotatingHeadline() {
  const [i, setI] = useState(0);

  useEffect(() => {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const t = setInterval(() => setI((v) => (v + 1) % QUESTIONS.length), 4400);
    return () => clearInterval(t);
  }, []);

  const q = QUESTIONS[i];

  return (
    <h1 className="relative mx-auto flex min-h-[3.8em] max-w-6xl items-center justify-center text-balance text-[clamp(2.1rem,6vw,5.2rem)] font-extrabold leading-[1.08] text-ink sm:min-h-[2.6em]">
      <AnimatePresence mode="wait">
        <motion.span
          key={i}
          className="block"
          initial={{ opacity: 0, y: 24, filter: "blur(8px)" }}
          animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
          exit={{ opacity: 0, y: -24, filter: "blur(8px)" }}
          transition={{ duration: 0.55, ease: [0.16, 1, 0.3, 1] }}
        >
          {q.pre}
          <span className="text-orange">{q.hot}</span>
          {q.br ? <br /> : null}
          {q.post}
        </motion.span>
      </AnimatePresence>
    </h1>
  );
}
