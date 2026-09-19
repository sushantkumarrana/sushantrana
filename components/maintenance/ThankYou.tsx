"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { MessageCircle, Phone, SearchCheck, Wrench } from "lucide-react";
import Nav from "../Nav";
import Footer from "../Footer";
import {
  MAINTENANCE_LEAD_KEY,
  MAINTENANCE_WHATSAPP,
  maintenanceLeadMessage,
  whatsappUrl,
  type MaintenanceLead,
} from "@/lib/whatsapp";

/** WhatsApp opens this long after the page loads. */
const DELAY_MS = 4000;

const NEXT_STEPS = [
  {
    icon: SearchCheck,
    t: "We evaluate your website",
    d: "We go through your site the way a visitor and Google would: loading speed, security warnings, broken pages and links, forms, checkout, and the platform, plugins or apps it runs on. Anything already broken goes on a short list.",
  },
  {
    icon: Phone,
    t: "We contact you and discuss",
    d: "We call or WhatsApp you on the number you gave, walk you through what we found and answer your questions. Then we suggest the plan that fits your site. You decide only after that conversation.",
  },
  {
    icon: Wrench,
    t: "We start your maintenance",
    d: "Once you agree, we collect the logins we need, take a full backup, fix the urgent issues first, and then keep the site updated, backed up and monitored for the rest of the plan.",
  },
];

/**
 * Confirmation screen for the maintenance form. Reads the answers the form left
 * in sessionStorage, clears them, and opens WhatsApp with them typed out. The
 * visitor still presses send; nothing is sent on their behalf.
 */
export default function MaintenanceThankYou() {
  const [href, setHref] = useState<string | null>(null);
  const [left, setLeft] = useState(Math.round(DELAY_MS / 1000));
  const [auto, setAuto] = useState(false);

  useEffect(() => {
    // Read but do not delete yet: React runs this effect twice in development,
    // and deleting on the first run left the second run with nothing, so the
    // redirect never started. The entry is cleared just before leaving.
    let lead: Partial<MaintenanceLead> | null = null;
    try {
      const raw = sessionStorage.getItem(MAINTENANCE_LEAD_KEY);
      if (raw) lead = JSON.parse(raw) as Partial<MaintenanceLead>;
    } catch {
      // Malformed or blocked storage: generic message.
    }

    const url = whatsappUrl(maintenanceLeadMessage(lead), MAINTENANCE_WHATSAPP);
    const paint = requestAnimationFrame(() => {
      setHref(url);
      setAuto(true);
    });

    // Always counts down and opens WhatsApp, with the answers when there are
    // some and a generic message when not. ?preview=1 runs the countdown
    // without leaving, so the screen itself can be checked.
    const preview = new URLSearchParams(window.location.search).has("preview");
    const countdown = setInterval(() => setLeft((n) => Math.max(0, n - 1)), 1000);
    const jump = preview
      ? undefined
      : setTimeout(() => {
          try {
            sessionStorage.removeItem(MAINTENANCE_LEAD_KEY);
          } catch {}
          window.location.href = url;
        }, DELAY_MS);

    return () => {
      cancelAnimationFrame(paint);
      clearInterval(countdown);
      clearTimeout(jump);
    };
  }, []);

  return (
    <>
      <Nav />
      <main className="bg-white px-5 pb-24 pt-32">
        <div className="mx-auto max-w-3xl text-center">
          <span
            className="mx-auto grid h-16 w-16 place-items-center rounded-full bg-orange/15 text-orange"
            aria-hidden
          >
            <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <path d="m5 12 4 4L19 7" />
            </svg>
          </span>

          <p className="script-label mt-6">Request received</p>
          <h1 className="mt-4 text-[clamp(1.9rem,6vw,3.4rem)] font-extrabold leading-tight text-ink">
            Thank you. <span className="text-orange">We have received your request.</span>
          </h1>

          {/* countdown to WhatsApp */}
          <div className="mx-auto mt-8 flex max-w-md items-center gap-5 rounded-3xl border border-[var(--color-line)] bg-[#fff7f3] p-5 text-left">
            {auto ? (
              <span className="relative grid h-16 w-16 shrink-0 place-items-center" aria-live="polite">
                <svg viewBox="0 0 64 64" className="absolute inset-0 -rotate-90" aria-hidden>
                  <circle cx="32" cy="32" r="28" fill="none" stroke="currentColor" strokeWidth="5" className="text-orange/15" />
                  <circle
                    cx="32"
                    cy="32"
                    r="28"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="5"
                    strokeLinecap="round"
                    className="text-orange"
                    strokeDasharray={176}
                    style={{ strokeDashoffset: 0, animation: `wa-ring ${DELAY_MS}ms linear forwards` }}
                  />
                </svg>
                <span className="font-[family-name:var(--font-display)] text-2xl font-extrabold text-ink">{left}</span>
                <span className="sr-only">seconds until WhatsApp opens</span>
              </span>
            ) : (
              <span className="grid h-16 w-16 shrink-0 place-items-center rounded-full bg-[#25D366] text-white">
                <MessageCircle aria-hidden className="h-7 w-7" />
              </span>
            )}
            <div>
              <p className="font-semibold text-ink">
                {auto
                  ? `Opening WhatsApp in ${left} second${left === 1 ? "" : "s"}…`
                  : "Send your details on WhatsApp"}
              </p>
              <p className="mt-0.5 text-sm text-muted">
                Your answers are already typed out. Just press send.
              </p>
              {href && (
                <a href={href} className="mt-2 inline-flex text-sm font-semibold text-orange underline underline-offset-4" rel="noopener">
                  Open WhatsApp now
                </a>
              )}
            </div>
          </div>
        </div>

        {/* next steps */}
        <section className="mx-auto mt-20 max-w-5xl" aria-labelledby="next-heading">
          <h2 id="next-heading" className="text-center text-[clamp(1.6rem,4vw,2.6rem)] font-extrabold text-ink">
            What are the <span className="text-orange">next steps?</span>
          </h2>

          <ol className="relative mt-12 grid list-none gap-10 md:grid-cols-3 md:gap-6">
            {/* connecting line behind the numbers */}
            <span aria-hidden className="absolute left-[16.66%] right-[16.66%] top-8 hidden h-1 rounded-full bg-gradient-to-r from-orange via-orange/60 to-orange/25 md:block" />
            {NEXT_STEPS.map((s, i) => (
              <li key={s.t} className="relative text-center">
                <span className="relative mx-auto grid h-16 w-16 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-2xl font-extrabold text-white shadow-[0_10px_30px_-8px_rgba(var(--orange-rgb),.7)] ring-8 ring-white">
                  {i + 1}
                </span>
                <div className="card mt-6 p-7 text-left">
                  <span className="flex items-center gap-3">
                    <span className="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">
                      <s.icon aria-hidden className="h-5 w-5" />
                    </span>
                    <span className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                      Step {i + 1}
                    </span>
                  </span>
                  <h3 className="mt-4 text-xl font-extrabold text-ink">{s.t}</h3>
                  <p className="mt-2.5 text-body">{s.d}</p>
                </div>
              </li>
            ))}
          </ol>
        </section>

        <p className="mt-14 text-center text-sm text-muted">
          Not using WhatsApp? Email{" "}
          <a href="mailto:me@sushantrana.com" className="font-semibold text-orange underline underline-offset-4">
            me@sushantrana.com
          </a>{" "}
          · back to{" "}
          <Link href="/services/website-maintenance" className="font-semibold text-orange underline underline-offset-4">
            website maintenance
          </Link>
        </p>
      </main>
      <style>{`@keyframes wa-ring { to { stroke-dashoffset: 176; } }`}</style>
      <Footer />
    </>
  );
}
