"use client";

import { useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import Reveal from "../Reveal";
import ImgOrPlaceholder from "../ImgOrPlaceholder";

const SERVICES = [
  { key: "brand", title: "Brand Strategy & Consulting", desc: "Positioning, offer, messaging, and go-to-market: the thinking layer every campaign stands on.", imgs: ["Positioning workshop", "Messaging framework"] },
  { key: "performance", title: "Performance Marketing", desc: "Google, Meta, TikTok, Snapchat, LinkedIn, Microsoft, and Amazon Ads, measured to revenue.", imgs: ["Campaign dashboard", "ROAS report"] },
  { key: "seo", title: "AI SEO", desc: "Rank where buyers now search: Google, AI Overviews, and LLM answers, with content and technical SEO built to be cited.", imgs: ["Search visibility", "AI answer coverage"] },
  { key: "ai", title: "AI Automation", desc: "CRM automation, lead scoring, pipelines, AI assistants, WhatsApp, and reporting that runs itself.", imgs: ["Pipeline automation", "AI assistant flow"] },
  { key: "web", title: "Website Development", desc: "Shopify, WordPress, Wix Studio, Webflow, and custom builds. Assets, not brochures.", imgs: ["Store build", "Landing page"] },
];

export default function WhatIDo() {
  const [active, setActive] = useState(0);
  const cur = SERVICES[active];

  return (
    <section id="services" className="section">
      <div className="wrap-wide">
        <Reveal>
          <span className="script-label">What I do</span>
          <h2 className="mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)]">
            Four disciplines. <span className="text-orange">One revenue engine.</span>
          </h2>
          <p className="mt-4 max-w-xl text-muted">Most consultants sell one of these. Growth needs them working together.</p>
        </Reveal>

        <div className="mt-12 grid gap-8 lg:grid-cols-[1fr_1.05fr]">
          {/* left: vertical services */}
          <div className="flex flex-col gap-3">
            {SERVICES.map((s, i) => {
              const on = i === active;
              return (
                <button
                  key={s.key}
                  onClick={() => setActive(i)}
                  className={`rounded-2xl border p-6 text-left transition ${
                    on ? "border-orange bg-white shadow-lg" : "border-[var(--color-line)] bg-white/50 hover:bg-white"
                  }`}
                >
                  <div className="flex items-center justify-between gap-4">
                    <h3 className={`text-xl font-extrabold ${on ? "text-orange" : "text-ink"}`}>{s.title}</h3>
                    <span className={`grid h-8 w-8 shrink-0 place-items-center rounded-full text-sm transition ${on ? "bg-orange text-white" : "bg-ink/5 text-ink"}`}>
                      {on ? "–" : "+"}
                    </span>
                  </div>
                  <AnimatePresence initial={false}>
                    {on && (
                      <motion.p
                        initial={{ height: 0, opacity: 0 }}
                        animate={{ height: "auto", opacity: 1 }}
                        exit={{ height: 0, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                        className="overflow-hidden text-body"
                      >
                        <span className="mt-3 block">{s.desc}</span>
                      </motion.p>
                    )}
                  </AnimatePresence>
                </button>
              );
            })}
          </div>

          {/* right: 2 images swap on click — desktop only */}
          <div className="hidden lg:sticky lg:top-6 lg:block lg:self-start">
            {/* Keyed remount (no AnimatePresence): with mode="wait" the old pair
                stays mounted until its exit finishes, so a stalled animation
                leaves the wrong images on screen. This swaps instantly. */}
            <motion.div
              key={cur.key}
              className="grid grid-cols-2 gap-4"
              initial={{ opacity: 0, scale: 0.96, y: 16 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
            >
              {cur.imgs.map((label, idx) => (
                <ImgOrPlaceholder
                  key={`${cur.key}-${idx}`}
                  src={`/disciplines/${cur.key}/${idx + 1}.png`}
                  alt={label}
                  ratio="3/4"
                  seed={active + idx}
                />
              ))}
            </motion.div>
          </div>
        </div>
      </div>
    </section>
  );
}
