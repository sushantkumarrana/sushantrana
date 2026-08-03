"use client";

import { motion, type Variants } from "framer-motion";
import { Fragment, type ReactNode } from "react";
import { useInViewport } from "./useInViewport";

const variants: Variants = {
  hidden: { opacity: 0, y: 44 },
  show: {
    opacity: 1,
    y: 0,
    // springy bounce so titles/cards clearly animate in on scroll
    transition: { type: "spring", stiffness: 120, damping: 13, mass: 0.7 },
  },
};

export default function Reveal({
  children,
  delay = 0,
  className,
  as = "div",
}: {
  children: ReactNode;
  delay?: number;
  className?: string;
  as?: "div" | "span" | "li" | "section";
}) {
  const { ref, inView } = useInViewport<HTMLDivElement>();
  const MotionTag = motion[as] as typeof motion.div;
  return (
    <MotionTag
      ref={ref}
      className={className}
      variants={variants}
      initial="hidden"
      animate={inView ? "show" : "hidden"}
      transition={{ delay }}
    >
      {children}
    </MotionTag>
  );
}

/** Word-by-word headline reveal (Agero-style). Native IO trigger + Framer
 *  stagger — reliable above and below the fold. */
const wordContainer: Variants = {
  hidden: {},
  show: { transition: { staggerChildren: 0.04 } },
};
const wordChild: Variants = {
  hidden: { y: "110%" },
  show: { y: 0, transition: { duration: 0.6, ease: [0.16, 1, 0.3, 1] } },
};

export function RevealWords({
  text,
  className,
}: {
  text: string;
  className?: string;
}) {
  const words = text.split(" ");
  const { ref, inView } = useInViewport<HTMLSpanElement>();
  return (
    <motion.span
      ref={ref}
      className={className}
      aria-label={text}
      variants={wordContainer}
      initial="hidden"
      animate={inView ? "show" : "hidden"}
    >
      {words.map((w, i) => (
        <Fragment key={i}>
          <span
            className="inline-block overflow-hidden align-bottom"
            aria-hidden
          >
            <motion.span className="inline-block" variants={wordChild}>
              {w}
            </motion.span>
          </span>
          {i < words.length - 1 ? " " : ""}
        </Fragment>
      ))}
    </motion.span>
  );
}
