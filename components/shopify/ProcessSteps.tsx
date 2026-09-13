"use client";

import { useEffect, useRef, useState } from "react";
import { PROCESS } from "@/lib/shopify";

/**
 * Scroll-driven walkthrough of the four build stages.
 *
 * The section pins itself for a few viewport heights and the character walks
 * the track as you scroll, so all four stages are seen in order before the page
 * moves on.
 *
 * The two layouts differ below the pin. On a large screen the four cards sit
 * side by side and the active one lifts. On a phone they are stacked on one
 * spot: the next card slides up over the last, so it reads as the cards
 * changing rather than the page scrolling.
 *
 * Every stage's copy is rendered at all times — the interaction only changes
 * which card is highlighted — so crawlers and screen readers get the whole
 * process regardless of scroll position.
 */

type Art = (typeof PROCESS)[number]["art"];

const clamp = (v: number, lo: number, hi: number) => Math.min(hi, Math.max(lo, v));

/** The prop in the character's hand, swapped per stage. */
function Tool({ art }: { art: Art }) {
  if (art === "search")
    return (
      <g>
        <circle cx="0" cy="0" r="13" fill="rgba(255,255,255,0.9)" stroke="#0a0a0a" strokeWidth="3.5" />
        <line x1="9" y1="9" x2="21" y2="21" stroke="#0a0a0a" strokeWidth="5" strokeLinecap="round" />
      </g>
    );
  if (art === "design")
    return (
      <g>
        <rect x="-13" y="-13" width="26" height="26" rx="4" fill="#fff" stroke="#0a0a0a" strokeWidth="3" />
        <path d="M-13 -4h26M-4 -13v26" stroke="#0a0a0a" strokeWidth="2" opacity=".4" />
        <circle cx="6" cy="6" r="3" fill="#ff4d00" />
      </g>
    );
  if (art === "build")
    return (
      <g>
        <path d="M-11 10 3-4" stroke="#0a0a0a" strokeWidth="6" strokeLinecap="round" />
        <path
          d="M2-13a9.5 9.5 0 1 0 10.5 10.5L6-.5-.5-7z"
          fill="#fff"
          stroke="#0a0a0a"
          strokeWidth="3"
          strokeLinejoin="round"
        />
      </g>
    );
  return (
    <g>
      <path
        d="M0-16c6.5 5.5 9.5 12.5 9.5 20L0 9l-9.5-5c0-7.5 3-14.5 9.5-20z"
        fill="#fff"
        stroke="#0a0a0a"
        strokeWidth="3"
        strokeLinejoin="round"
      />
      <circle cx="0" cy="-3" r="3.5" fill="#ff4d00" />
      <path d="M-4.5 10-9 18M4.5 10l4.5 8" stroke="#ff4d00" strokeWidth="3.5" strokeLinecap="round" />
    </g>
  );
}

/**
 * Flat-illustration likeness of Sushant: the wavy black hair, heavy black
 * frames and full beard from the site logo, drawn in the brand orange.
 */
function Character({ art, walking }: { art: Art; walking: boolean }) {
  return (
    <svg
      viewBox="0 0 130 150"
      width="130"
      height="150"
      role="img"
      aria-label="Illustration of Sushant Rana working on the selected stage"
      className={walking ? "animate-[bob_1.1s_ease-in-out_infinite]" : undefined}
    >
      <ellipse cx="65" cy="143" rx="27" ry="5" fill="#0a0a0a" opacity=".12" />

      {/* legs */}
      <path d="M55 140V102M75 140V102" stroke="#141414" strokeWidth="10" strokeLinecap="round" />

      {/* torso */}
      <path d="M65 56c-16 0-25 10-25 25v23h50V81c0-15-9-25-25-25z" fill="#ff4d00" />
      {/* collar */}
      <path d="M57 57 65 68l8-11" fill="none" stroke="#0a0a0a" strokeWidth="2.5" opacity=".35" />
      {/* logo mark on the chest */}
      <circle cx="65" cy="86" r="6" fill="none" stroke="#fff" strokeWidth="2.2" opacity=".9" />
      <circle cx="65" cy="86" r="2" fill="#fff" opacity=".9" />

      {/* arm holding the tool */}
      <path d="M84 84 102 66" stroke="#ff4d00" strokeWidth="10" strokeLinecap="round" />
      <circle cx="102" cy="66" r="5" fill="#e8b98f" />

      {/* head */}
      <ellipse cx="65" cy="34" rx="19" ry="20" fill="#e8b98f" />
      {/* beard */}
      <path
        d="M46 33c0 16 8 24 19 24s19-8 19-24c0 6-4 9-6 14-2 6-6 9-13 9s-11-3-13-9c-2-5-6-8-6-14z"
        fill="#141414"
      />
      <path d="M50 40c2 12 8 18 15 18s13-6 15-18c-1 10-6 15-15 15s-14-5-15-15z" fill="#141414" />
      {/* moustache */}
      <path d="M58 40q7 4 14 0-7 6-14 0z" fill="#141414" />
      {/* wavy hair */}
      <path
        d="M45 30c-1-13 8-22 20-22s21 9 20 22c-2-4-4-6-6-9-3 3-6 3-9 1-2 3-6 4-9 2-3 3-6 3-9 0-3 2-5 3-7 6z"
        fill="#141414"
      />
      <path d="M50 12c4-3 9-4 15-4s11 1 15 4c-5-1-10-1-15-1s-10 0-15 1z" fill="#141414" />
      {/* heavy black frames */}
      <g stroke="#0a0a0a" strokeWidth="2.6" fill="rgba(255,255,255,.55)">
        <rect x="50" y="27" width="13" height="10" rx="3" />
        <rect x="67" y="27" width="13" height="10" rx="3" />
      </g>
      <path d="M63 31h4M50 30l-4 1M80 30l4 1" stroke="#0a0a0a" strokeWidth="2.4" strokeLinecap="round" />
      {/* eyes */}
      <circle cx="56.5" cy="32" r="1.7" fill="#0a0a0a" />
      <circle cx="73.5" cy="32" r="1.7" fill="#0a0a0a" />

      {/* the tool */}
      <g transform="translate(108 60)">
        <Tool art={art} />
      </g>
    </svg>
  );
}

export default function ProcessSteps() {
  const wrapRef = useRef<HTMLDivElement>(null);
  /** 0 → 1 across the pinned scroll distance. Drives both the character's
   *  position and which stage is active. */
  const [progress, setProgress] = useState(0);
  const [walking, setWalking] = useState(false);
  /** The stacked-deck transforms are inline, and inline styles beat utility
   *  classes, so they must not be emitted at all on the desktop layout. */
  const [stacked, setStacked] = useState(false);

  useEffect(() => {
    const mq = window.matchMedia("(max-width: 1023px)");
    const sync = () => setStacked(mq.matches);
    sync();
    mq.addEventListener("change", sync);
    return () => mq.removeEventListener("change", sync);
  }, []);

  useEffect(() => {
    let frame = 0;
    let stopWalk: ReturnType<typeof setTimeout>;

    const onScroll = () => {
      if (frame) return;
      frame = requestAnimationFrame(() => {
        frame = 0;
        const el = wrapRef.current;
        if (!el) return;
        const r = el.getBoundingClientRect();
        const travel = r.height - window.innerHeight;
        if (travel <= 0) return;
        setProgress(clamp(-r.top / travel, 0, 1));
        setWalking(true);
        clearTimeout(stopWalk);
        stopWalk = setTimeout(() => setWalking(false), 220);
      });
    };

    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    return () => {
      window.removeEventListener("scroll", onScroll);
      window.removeEventListener("resize", onScroll);
      if (frame) cancelAnimationFrame(frame);
      clearTimeout(stopWalk);
    };
  }, []);

  const active = clamp(Math.floor(progress * PROCESS.length), 0, PROCESS.length - 1);
  const step = PROCESS[active];

  return (
    // Roughly one screen of scroll per stage, plus room to read the last one
    // before the pin releases.
    <div ref={wrapRef} className="relative h-[300vh] lg:h-[340vh]">
      <div className="sticky top-0 flex min-h-[100dvh] items-center py-10 lg:py-16">
        <div className="w-full">
          {/* stage */}
          <div className="wrap">
            <div className="relative overflow-hidden rounded-[32px] border border-[var(--color-line)] bg-white px-6 pb-8 pt-6">
              <div
                className="flex justify-start transition-transform duration-500 ease-[cubic-bezier(0.16,1,0.3,1)]"
                style={{ transform: `translateX(calc(${progress} * (100% - 130px)))` }}
              >
                <Character art={step.art} walking={walking} />
              </div>

              <ol className="relative mt-2 grid list-none grid-cols-4 gap-2">
                <span
                  aria-hidden
                  className="absolute left-[12.5%] right-[12.5%] top-[13px] h-1 rounded-full bg-ink/10"
                />
                <span
                  aria-hidden
                  className="absolute left-[12.5%] top-[13px] h-1 rounded-full bg-orange transition-[width] duration-300"
                  style={{ width: `calc(${progress} * 75%)` }}
                />
                {PROCESS.map((s, i) => (
                  <li key={s.n} className="relative text-center">
                    <button
                      type="button"
                      onClick={() => setProgress(i / (PROCESS.length - 1))}
                      aria-current={i === active ? "step" : undefined}
                      className="group flex w-full flex-col items-center gap-2"
                    >
                      <span
                        className={`grid h-7 w-7 place-items-center rounded-full border-2 font-[family-name:var(--font-display)] text-xs font-extrabold transition ${
                          i <= active
                            ? "border-orange bg-orange text-white"
                            : "border-ink/15 bg-white text-muted group-hover:border-orange"
                        }`}
                      >
                        {s.n}
                      </span>
                      <span
                        className={`text-xs font-semibold transition sm:text-sm ${
                          i === active ? "text-ink" : "text-muted group-hover:text-orange"
                        }`}
                      >
                        {s.t}
                      </span>
                    </button>
                  </li>
                ))}
              </ol>
            </div>
          </div>

          {/* Every stage stays rendered at all times — the interaction only
              moves and fades them — so crawlers and screen readers get the
              whole process no matter where the scroll sits. */}
          <ol className="wrap relative mt-8 grid h-[300px] list-none grid-cols-1 gap-5 sm:h-[250px] lg:h-auto lg:grid-cols-4">
            {PROCESS.map((s, i) => {
              const offset = i - active;
              return (
                <li
                  key={s.n}
                  className="absolute inset-x-0 top-0 flex lg:relative lg:inset-auto lg:z-auto"
                  style={
                    stacked
                      ? {
                          // the active card sits on top; the rest fall back
                          // behind it in the order they will arrive
                          zIndex: 40 - Math.abs(offset),
                          // A deck: the stages still to come sit a few pixels
                          // lower and slightly smaller, so only a sliver of
                          // each shows under the active card. Finished stages
                          // lift away and fade out.
                          transform:
                            offset >= 0
                              ? `translateY(${Math.min(offset, 3) * 9}px) scale(${
                                  1 - Math.min(offset, 3) * 0.025
                                })`
                              : `translateY(${offset * 24}px) scale(${1 + offset * 0.02})`,
                          opacity: offset < 0 ? 0 : 1,
                          transition:
                            "transform 550ms cubic-bezier(0.16,1,0.3,1), opacity 400ms ease",
                        }
                      : undefined
                  }
                >
                  <article
                    className={`w-full rounded-3xl border bg-white p-6 transition-[border-color,box-shadow,transform,opacity] duration-500 ${
                      i === active
                        ? "border-orange shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)] lg:-translate-y-2"
                        : "border-[var(--color-line)] lg:opacity-70"
                    }`}
                  >
                    <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                      Step {s.n}
                    </p>
                    <h3 className="mt-2 text-lg font-extrabold text-ink">{s.t}</h3>
                    <p className="mt-2 text-sm text-body">{s.d}</p>
                    <ul className="mt-4 grid list-none gap-1.5">
                      {s.detail.map((d) => (
                        <li key={d} className="flex items-start gap-2 text-xs font-medium text-muted">
                          <span aria-hidden className="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-orange" />
                          {d}
                        </li>
                      ))}
                    </ul>
                  </article>
                </li>
              );
            })}
          </ol>
        </div>
      </div>
    </div>
  );
}
