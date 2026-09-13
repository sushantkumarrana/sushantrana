"use client";

import { useEffect, useState } from "react";
import { AnimatePresence, motion } from "framer-motion";
import HeroForm from "./HeroForm";

/**
 * The Shopify page's own enquiry popup.
 *
 * It replaces the site-wide ConsultPopup on this page so that every call to
 * action here opens the same three-step store-build form as the hero, rather
 * than the shorter general consultation form. Only one of the two is ever
 * mounted, otherwise a single click would open both.
 *
 * The trigger list matches ConsultPopup's so existing CTAs keep working:
 * href="#contact", [data-consult], or link text that starts with "book".
 */
export default function QuotePopup() {
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onClick = (e: MouseEvent) => {
      const el = (e.target as HTMLElement)?.closest("a,button") as HTMLElement | null;
      if (!el) return;
      if (el.closest("[data-quote-modal]")) return;

      const href = el.getAttribute("href") || "";
      const txt = (el.textContent || "").trim().toLowerCase();
      const isCTA =
        el.hasAttribute("data-consult") ||
        el.hasAttribute("data-quote") ||
        href === "#contact" ||
        href.startsWith("/contact") ||
        txt.startsWith("book") ||
        txt.startsWith("get your free");

      if (!isCTA) return;
      // Capture phase + stopPropagation: Next's <Link> handles clicks on the
      // React root, which runs before a bubble-phase document listener.
      e.preventDefault();
      e.stopPropagation();
      setOpen(true);
    };
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    document.addEventListener("click", onClick, true);
    document.addEventListener("keydown", onKey);
    return () => {
      document.removeEventListener("click", onClick, true);
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
          role="dialog"
          aria-modal="true"
          aria-label="Request a Shopify store quote"
        >
          <div
            className="absolute inset-0 bg-black/55 backdrop-blur-sm"
            onClick={() => setOpen(false)}
          />
          <motion.div
            data-quote-modal
            /* Lenis hijacks wheel and touch globally, which would trap
               scrolling inside a form this tall on a short screen. */
            data-lenis-prevent
            className="relative max-h-[calc(100dvh-2rem)] w-full max-w-md touch-pan-y overflow-y-auto overscroll-contain rounded-[28px]"
            initial={{ scale: 0.94, y: 20 }}
            animate={{ scale: 1, y: 0 }}
            exit={{ scale: 0.94, y: 20 }}
            transition={{ type: "spring", stiffness: 220, damping: 22 }}
          >
            <button
              type="button"
              aria-label="Close"
              onClick={() => setOpen(false)}
              className="absolute right-4 top-4 z-10 grid h-9 w-9 place-items-center rounded-full bg-black/5 text-ink transition hover:bg-black/10"
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
                <path d="M6 6l12 12M18 6 6 18" />
              </svg>
            </button>
            <HeroForm />
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
