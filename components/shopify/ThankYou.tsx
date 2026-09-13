"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import Nav from "../Nav";
import Footer from "../Footer";
import { SHOPIFY_LEAD_KEY, shopifyLeadMessage, whatsappUrl, type ShopifyLead } from "@/lib/whatsapp";

/** How long the visitor sees the message before WhatsApp opens. */
const DELAY_MS = 2500;

/**
 * Confirmation screen for the Shopify enquiry form.
 *
 * It reads the answers the form left in sessionStorage, builds a pre-filled
 * WhatsApp message from them and sends the visitor there after a short pause.
 * Nothing is sent automatically — WhatsApp opens with the message typed out and
 * the visitor presses send.
 *
 * The entry is cleared once read, so a refresh or a back-navigation cannot
 * replay someone else's details on a shared device.
 */
export default function ShopifyThankYou() {
  const [href, setHref] = useState<string | null>(null);
  const [left, setLeft] = useState(Math.round(DELAY_MS / 1000));

  useEffect(() => {
    let lead: Partial<ShopifyLead> | null = null;
    try {
      const raw = sessionStorage.getItem(SHOPIFY_LEAD_KEY);
      if (raw) {
        lead = JSON.parse(raw) as Partial<ShopifyLead>;
        sessionStorage.removeItem(SHOPIFY_LEAD_KEY);
      }
    } catch {
      // Malformed or unavailable storage: fall through to the generic message.
    }

    const url = whatsappUrl(shopifyLeadMessage(lead));
    // Next frame, not synchronously: setting state in the effect body costs an
    // extra render pass before the browser has painted anything.
    const paint = requestAnimationFrame(() => setHref(url));

    // ?preview=1 holds the page open so the screen itself can be checked
    // without being bounced to WhatsApp two seconds later.
    if (new URLSearchParams(window.location.search).has("preview")) {
      return () => cancelAnimationFrame(paint);
    }

    const countdown = setInterval(() => setLeft((n) => Math.max(0, n - 1)), 1000);
    const jump = setTimeout(() => {
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
      <main className="grid min-h-[100dvh] place-items-center bg-white px-5 py-32">
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

          <h1 className="mt-4 text-[clamp(1.9rem,6vw,3.6rem)] font-extrabold leading-tight text-ink">
            Wait, do not leave this page.{" "}
            <span className="text-orange">I am opening WhatsApp for you.</span>
          </h1>

          <p className="mx-auto mt-6 max-w-xl text-lg text-body">
            Your enquiry is with me. In a moment WhatsApp will open with your
            details already typed out, so you only have to press send and we can
            carry on the conversation there.
          </p>

          <p className="mt-8 font-[family-name:var(--font-display)] text-sm font-bold uppercase tracking-widest text-muted">
            <span aria-live="polite">
              Redirecting in {left} second{left === 1 ? "" : "s"}
            </span>
          </p>

          {href && (
            <a href={href} className="btn btn-primary mt-6" rel="noopener">
              Open WhatsApp now
            </a>
          )}

          <p className="mt-10 text-sm text-muted">
            Not using WhatsApp? Email me at{" "}
            <a
              href="mailto:me@sushantrana.com"
              className="font-semibold text-orange underline underline-offset-4"
            >
              me@sushantrana.com
            </a>{" "}
            or head back to{" "}
            <Link
              href="/services/shopify-store-development"
              className="font-semibold text-orange underline underline-offset-4"
            >
              Shopify store development
            </Link>
            .
          </p>
        </div>
      </main>
      <Footer />
    </>
  );
}
