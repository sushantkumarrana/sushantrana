"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";

/**
 * Glassmorphism consultation popup. Opens on any "Book…" CTA click
 * (delegated: href="#contact", [data-consult], or link text starting "Book").
 */
export default function ConsultPopup() {
  const [open, setOpen] = useState(false);
  const [sent, setSent] = useState(false);

  useEffect(() => {
    const onClick = (e: MouseEvent) => {
      const el = (e.target as HTMLElement)?.closest("a,button") as HTMLElement | null;
      if (!el) return;
      const href = el.getAttribute("href");
      const txt = (el.textContent || "").trim().toLowerCase();
      if (el.hasAttribute("data-consult") || href === "#contact" || txt.startsWith("book")) {
        e.preventDefault();
        setSent(false);
        setOpen(true);
      }
    };
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("click", onClick);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("click", onClick);
      document.removeEventListener("keydown", onKey);
    };
  }, []);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
  }, [open]);

  return (
    <AnimatePresence>
      {open && (
        <motion.div
          className="fixed inset-0 z-[100] grid place-items-center p-4"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        >
          <div className="absolute inset-0 bg-black/50 backdrop-blur-sm" onClick={() => setOpen(false)} />
          <motion.div
            className="glass relative w-full max-w-md rounded-[28px] p-8 md:p-10"
            initial={{ scale: 0.94, y: 20 }}
            animate={{ scale: 1, y: 0 }}
            exit={{ scale: 0.94, y: 20 }}
            transition={{ type: "spring", stiffness: 220, damping: 22 }}
          >
            <button
              aria-label="Close"
              onClick={() => setOpen(false)}
              className="absolute right-5 top-5 grid h-9 w-9 place-items-center rounded-full bg-black/5 text-ink transition hover:bg-black/10"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round"><path d="M6 6l12 12M18 6 6 18" /></svg>
            </button>

            {sent ? (
              <div className="py-8 text-center">
                <div className="mx-auto mb-4 grid h-14 w-14 place-items-center rounded-full bg-orange/15 text-orange">
                  <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round"><path d="m5 12 4 4L19 7" /></svg>
                </div>
                <h3 className="text-2xl font-extrabold text-ink">Request received</h3>
                <p className="mt-2 text-muted">I&apos;ll reach out within one business day.</p>
              </div>
            ) : (
              <>
                <span className="script-label">Book a call</span>
                <h3 className="mt-1 text-[clamp(1.6rem,4vw,2.2rem)] font-extrabold text-ink">
                  Free 30-minute consultation
                </h3>
                <p className="mt-2 text-sm text-muted">
                  Tell me a little about your business — I&apos;ll reply within a day.
                </p>
                <form
                  className="mt-6 grid gap-3"
                  onSubmit={(e) => {
                    e.preventDefault();
                    setSent(true);
                  }}
                >
                  <input required placeholder="Your name" className="rounded-xl border border-[var(--color-line)] bg-white/70 px-4 py-3 text-ink outline-none focus:border-orange" />
                  <input required type="email" placeholder="Email" className="rounded-xl border border-[var(--color-line)] bg-white/70 px-4 py-3 text-ink outline-none focus:border-orange" />
                  <input required type="tel" placeholder="Phone number" className="rounded-xl border border-[var(--color-line)] bg-white/70 px-4 py-3 text-ink outline-none focus:border-orange" />
                  <input placeholder="Business / website" className="rounded-xl border border-[var(--color-line)] bg-white/70 px-4 py-3 text-ink outline-none focus:border-orange" />
                  <textarea rows={3} placeholder="What do you want to grow?" className="rounded-xl border border-[var(--color-line)] bg-white/70 px-4 py-3 text-ink outline-none focus:border-orange" />
                  <button type="submit" className="btn btn-primary mt-1 w-full">Request my slot</button>
                </form>
              </>
            )}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
