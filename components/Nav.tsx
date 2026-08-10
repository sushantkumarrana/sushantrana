"use client";

import { useEffect, useRef, useState, type ComponentType } from "react";
import { usePathname } from "next/navigation";
import Link from "next/link";
import { AnimatePresence, motion } from "framer-motion";
import {
  Target,
  Search,
  Code2,
  Users,
  ArrowUpRight,
  ChevronDown,
  Star,
} from "lucide-react";

type Leaf = { label: string; href: string };
type IconType = ComponentType<{ className?: string; strokeWidth?: number }>;
type Group = { heading: string; icon: IconType; items: Leaf[] };
type Top =
  | { label: string; href: string; type: "link" }
  | { label: string; type: "mega"; columns: Group[] }
  | { label: string; type: "flat"; items: Leaf[] };

const slug = (s: string) =>
  s.toLowerCase().replace(/&/g, "and").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

const svc = (heading: string, icon: IconType, items: string[]): Group => ({
  heading,
  icon,
  items: items.map((i) => ({ label: i, href: `/services/${slug(i)}` })),
});

const flat = (base: string, items: string[]): Leaf[] =>
  items.map((i) => ({ label: i, href: `/${base}/${slug(i)}` }));

const NAV: Top[] = [
  { label: "Home", href: "/", type: "link" },
  { label: "About Me", href: "/about", type: "link" },
  {
    label: "Services",
    type: "mega",
    columns: [
      svc("Performance Marketing", Target, [
        "Google Ads",
        "Meta Ads",
        "LinkedIn Ads",
        "YouTube Ads",
        "Google Shopping Ads",
        "Amazon Ads",
        "Lead Generation",
        "Remarketing",
      ]),
      svc("SEO Services", Search, [
        "Local SEO",
        "Technical SEO",
        "Ecommerce SEO",
        "Enterprise SEO",
        "SEO Audit",
        "Link Building",
        "Content SEO",
      ]),
      svc("Website Development", Code2, [
        "WordPress Development",
        "Ecommerce Website",
        "Landing Pages",
        "Website Redesign",
        "Website Maintenance",
      ]),
      svc("CRM Solutions", Users, [
        "Zoho CRM",
        "HubSpot CRM",
        "GoHighLevel",
        "Sales Funnel Setup",
        "Pipeline Management",
        "Email Automation",
        "Reporting Dashboard",
        "CRM Consulting",
      ]),
    ],
  },
  {
    label: "Industries",
    type: "flat",
    items: flat("industries", [
      "Healthcare",
      "Education",
      "Manufacturing",
      "Automobile",
      "Real Estate",
      "Legal Firms",
      "Finance",
      "Ecommerce",
      "Travel",
      "SaaS",
      "Local Businesses",
      "B2B Companies",
    ]),
  },
  {
    label: "Case Studies",
    type: "flat",
    items: flat("case-studies", [
      "Google Ads",
      "Meta Ads",
      "SEO",
      "AI Automation",
      "CRM",
      "Website Development",
    ]),
  },
];

const STATS = [
  { n: "8+", label: "years experience" },
  { n: "4", label: "markets served" },
  { n: "120+", label: "systems built" },
];

const spring = { duration: 0.2, ease: [0.16, 1, 0.3, 1] as const };

export default function Nav() {
  const pathname = usePathname() || "/";
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState<string | null>(null);
  const [mobileOpen, setMobileOpen] = useState(false);
  const [mobileExpanded, setMobileExpanded] = useState<string | null>(null);
  const closeTimer = useRef<number | null>(null);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 120);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setOpen(null);
        setMobileOpen(false);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  const closeAll = () => {
    setOpen(null);
    setMobileOpen(false);
    setMobileExpanded(null);
  };

  const hoverOpen = (label: string) => {
    if (closeTimer.current) window.clearTimeout(closeTimer.current);
    setOpen(label);
  };
  const hoverClose = () => {
    if (closeTimer.current) window.clearTimeout(closeTimer.current);
    closeTimer.current = window.setTimeout(() => setOpen(null), 130);
  };

  const isActive = (href: string) =>
    href === "/" ? pathname === "/" : pathname.startsWith(href);

  const topIsActive = (t: Top) => {
    if (t.type === "link") return isActive(t.href);
    if (t.type === "flat") return t.items.some((i) => isActive(i.href));
    return t.columns.some((c) => c.items.some((i) => isActive(i.href)));
  };

  const megaTop = NAV.find((n) => n.label === open && n.type === "mega") as
    | Extract<Top, { type: "mega" }>
    | undefined;

  return (
    <header className="fixed inset-x-0 top-0 z-50 px-3" onMouseLeave={hoverClose}>
      <nav
        aria-label="Primary"
        className={`mx-auto flex items-center justify-between transition-all duration-500 ${
          scrolled
            ? "mt-3 max-w-6xl rounded-full border border-[var(--color-line)] bg-white/85 px-5 py-2.5 shadow-[0_12px_40px_-12px_rgba(0,0,0,0.25)] backdrop-blur-xl"
            : "mt-0 max-w-[1400px] px-2 py-3"
        }`}
      >
        <Link href="/" onClick={closeAll} className="flex items-center" aria-label="Sushant Rana home">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src="/logo.png" alt="Sushant Rana" className={`w-auto transition-all ${scrolled ? "h-11" : "h-14"}`} />
        </Link>

        <ul className="hidden items-center gap-0.5 lg:flex">
          {NAV.map((t) => {
            const active = topIsActive(t);
            const isOpen = open === t.label;
            const base =
              "flex items-center rounded-full px-3.5 py-2 font-[family-name:var(--font-display)] text-sm font-medium transition";
            const state = active || isOpen
              ? "bg-orange text-white font-semibold shadow-[0_10px_24px_-12px_rgba(var(--orange-rgb),0.7)]"
              : "text-body hover:bg-black/5 hover:text-orange";

            if (t.type === "link") {
              return (
                <li key={t.label}>
                  <Link href={t.href} onClick={closeAll} className={`${base} ${state}`} aria-current={active ? "page" : undefined}>
                    {t.label}
                  </Link>
                </li>
              );
            }

            return (
              <li key={t.label} className="relative" onMouseEnter={() => hoverOpen(t.label)}>
                <button
                  type="button"
                  className={`${base} ${state}`}
                  aria-haspopup="true"
                  aria-expanded={isOpen}
                  onClick={() => setOpen((v) => (v === t.label ? null : t.label))}
                  onFocus={() => setOpen(t.label)}
                >
                  {t.label}
                  <ChevronDown
                    className={`ml-1 h-3.5 w-3.5 opacity-70 transition-transform ${isOpen ? "rotate-180" : ""}`}
                    strokeWidth={2.5}
                  />
                </button>

                {/* Compact single-column dropdown (flat menus) */}
                {t.type === "flat" && (
                  <AnimatePresence>
                    {isOpen && (
                      <motion.div
                        initial={{ opacity: 0, y: -6, scale: 0.98 }}
                        animate={{ opacity: 1, y: 0, scale: 1 }}
                        exit={{ opacity: 0, y: -6, scale: 0.98 }}
                        transition={spring}
                        className="absolute left-0 top-full mt-2 w-72 origin-top-left"
                      >
                        <div className="rounded-2xl border border-[var(--color-line)] bg-white/95 p-2 shadow-[0_24px_60px_-20px_rgba(10,10,10,0.28)] backdrop-blur-xl">
                          <ul className="flex flex-col gap-0.5">
                            {t.items.map((i, idx) => {
                              const act = isActive(i.href);
                              const feat = idx === 0;
                              return (
                                <li key={i.href}>
                                  <Link
                                    href={i.href}
                                    onClick={closeAll}
                                    aria-current={act ? "page" : undefined}
                                    className={`group flex items-center justify-between rounded-xl px-3.5 py-2.5 text-sm transition ${
                                      feat
                                        ? "bg-orange font-semibold text-white shadow-[0_10px_24px_-10px_rgba(var(--orange-rgb),0.7)]"
                                        : act
                                        ? "bg-black/5 text-orange"
                                        : "text-body hover:bg-black/5 hover:text-orange"
                                    }`}
                                  >
                                    <span>{i.label}</span>
                                    {feat ? (
                                      <Star className="h-3.5 w-3.5 fill-white" />
                                    ) : (
                                      <ArrowUpRight className="h-4 w-4 opacity-0 transition-opacity group-hover:opacity-60" />
                                    )}
                                  </Link>
                                </li>
                              );
                            })}
                          </ul>
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                )}
              </li>
            );
          })}
        </ul>

        <div className="flex items-center gap-3">
          <span className="hidden sm:block">
            <Link href="/contact/book-strategy-call" className="btn btn-primary !min-h-[44px] !px-6 text-sm">
              Book an Appointment
            </Link>
          </span>
          <button
            aria-label="Toggle menu"
            aria-expanded={mobileOpen}
            onClick={() => setMobileOpen((v) => !v)}
            className="grid h-11 w-11 place-items-center rounded-xl border border-[var(--color-line)] bg-white lg:hidden"
          >
            <span className="relative block h-3 w-5">
              <span className={`absolute left-0 top-0 h-0.5 w-5 bg-ink transition ${mobileOpen ? "translate-y-[5px] rotate-45" : ""}`} />
              <span className={`absolute bottom-0 left-0 h-0.5 w-5 bg-ink transition ${mobileOpen ? "-translate-y-[5px] -rotate-45" : ""}`} />
            </span>
          </button>
        </div>
      </nav>

      {/* Desktop mega panel (Services) */}
      <AnimatePresence>
        {megaTop && (
          <motion.div
            key={megaTop.label}
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={spring}
            className="mx-auto mt-2 hidden max-w-6xl lg:block"
            onMouseEnter={() => hoverOpen(megaTop.label)}
            onMouseLeave={hoverClose}
          >
            <div className="overflow-hidden rounded-3xl border border-[var(--color-line)] bg-[#f6f5f2]/95 shadow-[0_24px_70px_-20px_rgba(10,10,10,0.32)] backdrop-blur-xl">
              {/* column count follows the data: 4 service columns + 1 featured
                  card. Hard-coding 6 left an empty column when a column was
                  removed, which is what caused the dead space on the right. */}
              <div
                className="grid gap-4 p-5"
                style={{ gridTemplateColumns: `repeat(${megaTop.columns.length + 1}, minmax(0, 1fr))` }}
              >
                {megaTop.columns.map((c) => {
                  const Icon = c.icon;
                  return (
                    <div key={c.heading} className="rounded-2xl bg-white/70 p-4">
                      <div className="mb-3 flex items-center gap-2">
                        <span className="grid h-8 w-8 place-items-center rounded-lg bg-black/5 text-ink">
                          <Icon className="h-4 w-4" strokeWidth={2} />
                        </span>
                        <span className="font-[family-name:var(--font-display)] text-sm font-bold text-ink">
                          {c.heading}
                        </span>
                      </div>
                      <ul className="flex flex-col gap-0.5">
                        {c.items.map((i, idx) => {
                          const act = isActive(i.href);
                          const feat = idx === 0;
                          return (
                            <li key={i.href}>
                              <Link
                                href={i.href}
                                onClick={closeAll}
                                aria-current={act ? "page" : undefined}
                                className={`flex items-center justify-between rounded-lg px-2.5 py-1.5 text-sm transition ${
                                  feat
                                    ? "bg-orange font-semibold text-white"
                                    : act
                                    ? "text-orange"
                                    : "text-body hover:text-orange"
                                }`}
                              >
                                <span>{i.label}</span>
                                {feat && <Star className="h-3 w-3 fill-white" />}
                              </Link>
                            </li>
                          );
                        })}
                      </ul>
                    </div>
                  );
                })}

                {/* Featured case study card */}
                <Link
                  href="/case-studies"
                  onClick={closeAll}
                  className="group relative flex flex-col justify-between overflow-hidden rounded-2xl p-5 grad-ink-orange"
                >
                  <div>
                    <span className="inline-flex items-center gap-1.5 rounded-full border border-white/20 bg-white/10 px-2.5 py-1 text-[0.62rem] font-bold uppercase tracking-[0.1em] text-white">
                      <span className="h-1.5 w-1.5 rounded-full bg-orange" /> Featured
                    </span>
                    <p className="mt-4 font-[family-name:var(--font-display)] text-lg font-bold leading-tight text-white">
                      From scattered spend to a revenue system in 90 days
                    </p>
                    <p className="mt-2 text-xs text-white/60">AI Automation · B2B · 2025</p>
                  </div>
                  <span className="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-orange-300">
                    Read the case study
                    <ArrowUpRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                  </span>
                </Link>
              </div>

              {/* Footer stats bar */}
              <div className="flex items-center justify-between border-t border-[var(--color-line)] bg-white/50 px-6 py-3">
                <div className="flex items-center gap-6">
                  {STATS.map((s) => (
                    <span key={s.label} className="text-xs text-muted">
                      <strong className="font-[family-name:var(--font-display)] text-sm font-bold text-ink">{s.n}</strong>{" "}
                      {s.label}
                    </span>
                  ))}
                </div>
                <Link
                  href="/services"
                  onClick={closeAll}
                  className="inline-flex items-center gap-1 text-sm font-semibold text-orange transition hover:gap-2"
                >
                  View all Services <ArrowUpRight className="h-4 w-4" />
                </Link>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Mobile drawer */}
      <AnimatePresence>
        {mobileOpen && (
          <motion.div
            initial={{ opacity: 0, y: -8 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -8 }}
            transition={spring}
            /* data-lenis-prevent: Lenis hijacks wheel/touch globally, which
               blocked scrolling inside this drawer. */
            data-lenis-prevent
            className="mx-auto mt-2 max-h-[calc(100dvh-120px)] max-w-5xl touch-pan-y overflow-y-auto overscroll-contain rounded-3xl border border-[var(--color-line)] bg-white p-4 pb-8 shadow-xl lg:hidden"
          >
            <ul className="flex flex-col">
              {NAV.map((t) => {
                if (t.type === "link") {
                  const active = isActive(t.href);
                  return (
                    <li key={t.label}>
                      <Link
                        href={t.href}
                        onClick={closeAll}
                        aria-current={active ? "page" : undefined}
                        className={`block rounded-xl px-3 py-3 font-[family-name:var(--font-display)] text-base font-semibold ${
                          active ? "text-orange" : "text-ink"
                        }`}
                      >
                        {t.label}
                      </Link>
                    </li>
                  );
                }
                const expanded = mobileExpanded === t.label;
                const cols =
                  t.type === "mega" ? t.columns : [{ heading: t.label, icon: null as IconType | null, items: t.items }];
                return (
                  <li key={t.label} className="border-b border-[var(--color-line)] last:border-0">
                    <button
                      type="button"
                      aria-expanded={expanded}
                      onClick={() => setMobileExpanded((v) => (v === t.label ? null : t.label))}
                      className="flex w-full items-center justify-between rounded-xl px-3 py-3 font-[family-name:var(--font-display)] text-base font-semibold text-ink"
                    >
                      <span>{t.label}</span>
                      <ChevronDown className={`h-4 w-4 opacity-70 transition-transform ${expanded ? "rotate-180" : ""}`} />
                    </button>
                    <AnimatePresence initial={false}>
                      {expanded && (
                        <motion.div
                          initial={{ height: 0, opacity: 0 }}
                          animate={{ height: "auto", opacity: 1 }}
                          exit={{ height: 0, opacity: 0 }}
                          transition={spring}
                          className="overflow-hidden"
                        >
                          <div className="px-2 pb-3">
                            {cols.map((c) => {
                              const Icon = c.icon;
                              return (
                                <div key={c.heading} className="mb-2">
                                  {t.type === "mega" && Icon && (
                                    <div className="mb-1 mt-2 flex items-center gap-2 px-2 text-[0.68rem] font-bold uppercase tracking-[0.12em] text-orange">
                                      <Icon className="h-3.5 w-3.5" strokeWidth={2.5} />
                                      {c.heading}
                                    </div>
                                  )}
                                  <ul className="flex flex-col">
                                    {c.items.map((i) => {
                                      const act = isActive(i.href);
                                      return (
                                        <li key={i.href}>
                                          <Link
                                            href={i.href}
                                            onClick={closeAll}
                                            aria-current={act ? "page" : undefined}
                                            className={`block rounded-lg px-3 py-2 text-sm ${
                                              act ? "text-orange" : "text-body"
                                            }`}
                                          >
                                            {i.label}
                                          </Link>
                                        </li>
                                      );
                                    })}
                                  </ul>
                                </div>
                              );
                            })}
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </li>
                );
              })}
              <li className="mt-3">
                <Link href="/contact/book-strategy-call" onClick={closeAll} className="btn btn-primary w-full">
                  Book an Appointment
                </Link>
              </li>
            </ul>
          </motion.div>
        )}
      </AnimatePresence>
    </header>
  );
}
