"use client";

import { useEffect, useState } from "react";

const links = [
  { label: "Services", href: "#services" },
  { label: "Work", href: "#results" },
  { label: "Case Studies", href: "#results" },
  { label: "Blog", href: "#blog" },
  { label: "About", href: "#about" },
];

export default function Nav() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 120);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <header className="fixed inset-x-0 top-0 z-50 px-3">
      <nav
        className={`mx-auto flex items-center justify-between transition-all duration-500 ${
          scrolled
            ? "mt-3 max-w-5xl rounded-full border border-[var(--color-line)] bg-white/85 px-5 py-2.5 shadow-[0_12px_40px_-12px_rgba(0,0,0,0.25)] backdrop-blur-xl"
            : "mt-0 max-w-[1400px] px-2 py-3"
        }`}
      >
        <a href="#top" className="flex items-center">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/logo.png" alt="Sushant Rana" className={`w-auto transition-all ${scrolled ? "h-11" : "h-14"}`} />
        </a>

        <ul className="hidden items-center gap-1 lg:flex">
          {links.map((l) => (
            <li key={l.label}>
              <a
                href={l.href}
                className="rounded-full px-4 py-2 font-[family-name:var(--font-display)] text-sm font-medium text-body transition hover:bg-black/5 hover:text-orange"
              >
                {l.label}
              </a>
            </li>
          ))}
        </ul>

        <div className="flex items-center gap-3">
          <span className="hidden sm:block">
            <a href="#contact" className="btn btn-primary !min-h-[44px] !px-6 text-sm">
              Book an Appointment
            </a>
          </span>
          <button
            aria-label="Toggle menu"
            aria-expanded={open}
            onClick={() => setOpen((v) => !v)}
            className="grid h-11 w-11 place-items-center rounded-xl border border-[var(--color-line)] bg-white lg:hidden"
          >
            <span className="relative block h-3 w-5">
              <span className={`absolute left-0 top-0 h-0.5 w-5 bg-ink transition ${open ? "translate-y-[5px] rotate-45" : ""}`} />
              <span className={`absolute bottom-0 left-0 h-0.5 w-5 bg-ink transition ${open ? "-translate-y-[5px] -rotate-45" : ""}`} />
            </span>
          </button>
        </div>
      </nav>

      {open && (
        <div className="mx-auto mt-2 max-w-5xl rounded-3xl border border-[var(--color-line)] bg-white p-5 shadow-xl lg:hidden">
          <ul className="flex flex-col gap-1">
            {links.map((l) => (
              <li key={l.label}>
                <a
                  href={l.href}
                  onClick={() => setOpen(false)}
                  className="block rounded-xl px-4 py-3 font-[family-name:var(--font-display)] text-lg font-medium text-ink"
                >
                  {l.label}
                </a>
              </li>
            ))}
            <li className="mt-3">
              <a href="#contact" onClick={() => setOpen(false)} className="btn btn-primary w-full">
                Book an Appointment
              </a>
            </li>
          </ul>
        </div>
      )}
    </header>
  );
}
