"use client";

import { useRef } from "react";
import Image from "next/image";
import Link from "next/link";

const slug = (s: string) =>
  s.toLowerCase().replace(/&/g, "and").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

// Every link resolves: real pages win, anything not built yet lands on the
// section catch-all, which renders the "coming soon" placeholder.
const COLS: { h: string; base: string; items: string[] }[] = [
  { h: "Services", base: "services", items: ["All Services", "Performance Marketing", "Website Development", "Case Studies", "Free Consultation"] },
  { h: "Advertising", base: "services", items: ["Google Ads", "Meta Ads", "TikTok Ads", "Snapchat Ads", "LinkedIn Ads", "Microsoft Ads", "Amazon Ads"] },
  { h: "Development", base: "services", items: ["Shopify", "WordPress", "Wix Studio", "Webflow", "Custom"] },
];

const socials: { label: string; href: string }[] = [
  { label: "LinkedIn", href: "https://www.linkedin.com/" },
  { label: "Instagram", href: "https://www.instagram.com/" },
  { label: "YouTube", href: "https://www.youtube.com/" },
];

export default function Footer() {
  const ref = useRef<HTMLElement>(null);

  const onMove = (e: React.MouseEvent) => {
    const el = ref.current;
    if (!el) return;
    const r = el.getBoundingClientRect();
    el.style.setProperty("--mx", `${e.clientX - r.left}px`);
    el.style.setProperty("--my", `${e.clientY - r.top}px`);
  };

  return (
    <footer
      ref={ref}
      onMouseMove={onMove}
      className="relative overflow-hidden bg-[#050505] text-white/75"
    >
      {/* background image — full, no overlay */}
      <div className="pointer-events-none absolute inset-0 bg-cover bg-center" style={{ backgroundImage: "url(/footer/footer-bg.png)" }} />
      {/* mouse-follow orange glow */}
      <div
        className="pointer-events-none absolute inset-0 opacity-70 transition-opacity"
        style={{ background: "radial-gradient(420px circle at var(--mx, 50%) var(--my, 0px), rgba(255,77,0,0.20), transparent 70%)" }}
      />

      <div className="wrap-wide relative [text-shadow:0_1px_10px_rgba(0,0,0,0.55)]">
        <div className="grid gap-12 py-16 md:grid-cols-[1.7fr_1fr_1fr_1fr_1.3fr]">
          {/* brand */}
          <div>
            <Image src="/logo-white.png" alt="Sushant Rana" width={284} height={64} className="h-16 w-auto" />
            {/* Same copy as the home page About Me section, kept verbatim so the
                two never drift apart. */}
            <p className="mt-5 max-w-sm text-sm text-white/60">
              I&apos;m Sushant Rana <span className="font-semibold text-orange">(Business Growth Consultant)</span>.
              I build revenue systems that combine business strategy, performance
              marketing, tracking + AI automation, and conversion-focused funnels
              into one scalable growth engine. Every engagement is senior-led and
              designed to help businesses generate predictable growth, improve
              operational efficiency, and maximize return on every marketing
              investment. Backed by 8+ years of experience across four global markets.
            </p>
          </div>

          {/* link columns */}
          {COLS.map((col) => (
            <div key={col.h}>
              <h4 className="mb-4 text-xs font-bold uppercase tracking-widest text-white/45">{col.h}</h4>
              <ul className="flex flex-col gap-2.5 text-sm">
                {col.items.map((i) => (
                  <li key={i}>
                    <Link href={`/${col.base}/${slug(i)}`} className="text-white/70 transition hover:text-orange">
                      {i}
                    </Link>
                  </li>
                ))}
              </ul>
            </div>
          ))}

          {/* get in touch block (replaces old Company column) */}
          <div>
            <h4 className="mb-4 text-xs font-bold uppercase tracking-widest text-white/45">Get in touch</h4>
            <a href="mailto:me@sushantrana.com" className="block text-sm text-white/80 transition hover:text-orange">
              me@sushantrana.com
            </a>
            <p className="mt-1 text-sm text-white/60">India · USA · Canada · Australia</p>
            <a href="#contact" className="btn btn-primary mt-5 !min-h-[46px] !px-6 text-sm">Book a free call</a>
            <div className="mt-6 flex flex-wrap gap-3">
              {socials.map((s) => (
                <a
                  key={s.label}
                  href={s.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="rounded-full border border-white/15 px-3 py-1.5 text-xs text-white/70 transition hover:border-orange hover:text-orange"
                >
                  {s.label}
                </a>
              ))}
            </div>
          </div>
        </div>

        <div className="flex flex-wrap items-center justify-between gap-4 border-t border-white/10 py-6 text-sm text-white/50">
          <span>© 2026 Sushant Rana. All rights reserved.</span>
          <nav className="flex gap-6">
            {/* Top-level URLs, not /about/… — these are real pages now, and the
                convention is what ad-platform and compliance reviewers look for. */}
            <Link href="/privacy-policy" className="transition hover:text-orange">Privacy Policy</Link>
            <Link href="/terms-and-conditions" className="transition hover:text-orange">Terms &amp; Conditions</Link>
          </nav>
        </div>
      </div>

      {/* full-white logo across the footer base
          extra bottom padding on mobile so the sticky Book bar never covers it */}
      <div className="relative select-none overflow-hidden px-4 pb-28 sm:pb-8">
        {/* Oversized decorative wordmark at the very bottom of the page. */}
        <Image src="/logo-white.png" alt="Sushant Rana" width={1774} height={400} sizes="85vw" className="mx-auto h-auto w-[85%] max-w-5xl" />
      </div>
    </footer>
  );
}
