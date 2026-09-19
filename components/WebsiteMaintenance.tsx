import Image from "next/image";
import Link from "next/link";
import {
  ArrowRight,
  Check,
  Code2,
  Gauge,
  Palette,
  Search,
  Server,
  ShieldCheck,
  type LucideIcon,
} from "lucide-react";
import Nav from "./Nav";
import Footer from "./Footer";
import Reveal from "./Reveal";
import BackToTop from "./BackToTop";
import MobileBookBar from "./MobileBookBar";
import Breadcrumbs from "./Breadcrumbs";
import FinalCTA from "./sections/FinalCTA";
import { ImageBand, Tag, Tick } from "./ServiceBits";
import { CurrencyProvider, Localized, PriceNote } from "./LocalCurrency";
import MaintenanceForm from "./maintenance/MaintenanceForm";
import MaintenancePopup from "./maintenance/MaintenancePopup";
import PlatformLogo from "./maintenance/PlatformLogo";
import {
  COVERAGE,
  CTA_LABEL,
  DOWNTIME_STORY,
  FAQ_GROUPS,
  HERO_STATS,
  PLANS,
  PLATFORMS,
  RELATED_SERVICES,
  SECURITY_POINTS,
  UPDATE_POINTS,
  WHY_CHOOSE,
} from "@/lib/maintenance";

const COVERAGE_ICONS: Record<string, LucideIcon> = {
  gauge: Gauge,
  shield: ShieldCheck,
  search: Search,
  code: Code2,
  palette: Palette,
  server: Server,
};

/** Licensed stock photos, 1400-1600px WebP, in /public/services/maintenance/. */
const IMG = (name: string) => `/services/maintenance/${name}.webp`;

const HERO_PLATFORMS = PLATFORMS.filter((p) =>
  ["WordPress", "Shopify", "Wix", "Webflow", "Framer", "Squarespace"].includes(p.name)
);

/** From the Essential plan, so every item is true of every plan. */
const HERO_INCLUDES = [
  "Scheduled backups",
  "Security scans",
  "Disaster recovery",
  "SSL and domain monitoring",
  "Hosting and webmail support",
  "Broken link fixes",
];

const H2 = "text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold";

/** Every CTA below opens the maintenance form popup (href="#contact"). */
function Cta({ children = CTA_LABEL }: { children?: React.ReactNode }) {
  return (
    <a href="#contact" className="btn btn-primary group shrink-0 whitespace-nowrap">
      {children}
      <ArrowRight aria-hidden className="ml-2 h-4 w-4 transition-transform group-hover:translate-x-1" />
    </a>
  );
}

export default function WebsiteMaintenance({ rates }: { rates: Record<string, number> | null }) {
  return (
    <>
      <Nav />
      <CurrencyProvider rates={rates}>
        <main id="main">
          {/* ================= HERO: copy + 3-step form ================= */}
          <section className="relative overflow-hidden bg-white" aria-labelledby="maint-heading">
            <span
              aria-hidden
              className="pointer-events-none absolute -right-40 top-10 h-[34rem] w-[34rem] rounded-full bg-orange/10 blur-[120px]"
            />
            <div className="wrap relative z-10 pt-24">
              <Breadcrumbs
                trail={[{ label: "Services", href: "/services" }, { label: "Website Maintenance" }]}
              />
            </div>

            <div className="wrap relative z-10 grid items-start gap-8 py-6 md:py-10 lg:grid-cols-[1fr_1fr] lg:gap-12">
              <Reveal className="order-1 lg:pt-6">
                <Tag>Website maintenance services</Tag>
                <h1
                  id="maint-heading"
                  className="mt-4 text-[clamp(2rem,7vw,2.9rem)] font-extrabold leading-[1.08] text-ink"
                >
                  Website maintenance that keeps your site{" "}
                  <span className="text-orange">fast, secure and up to date</span>
                </h1>
                <p className="mt-4 max-w-xl text-body">
                  A website starts ageing the day it launches. Plugins go out of
                  date, links break, certificates expire. Whether it runs on
                  WordPress, Shopify, Wix, Webflow, Framer or custom code, my team
                  handles the backups, updates, fixes and small changes on a
                  yearly plan, so your site keeps working while you run the
                  business.
                </p>

                <div className="mt-6 rounded-2xl border border-[var(--color-line)] bg-white/70 p-5">
                  <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                    Every plan includes
                  </p>
                  <ul className="mt-3 grid list-none gap-x-5 gap-y-2.5 sm:grid-cols-2">
                    {HERO_INCLUDES.map((t) => (
                      <li key={t} className="flex items-start gap-2 text-sm font-medium text-ink">
                        <Check aria-hidden className="mt-0.5 h-4 w-4 shrink-0 text-orange" strokeWidth={3} />
                        {t}
                      </li>
                    ))}
                  </ul>
                </div>

                <ul className="mt-6 flex list-none flex-wrap items-center gap-3" aria-label="Platforms maintained">
                  {HERO_PLATFORMS.map((p) => (
                    <li
                      key={p.name}
                      title={p.name}
                      className="grid h-12 w-12 place-items-center rounded-2xl border border-[var(--color-line)] bg-white shadow-sm"
                    >
                      <span className="scale-75">
                        <PlatformLogo name={p.name} logos={p.logos} />
                      </span>
                    </li>
                  ))}
                  <li className="text-sm font-semibold text-muted">+ {PLATFORMS.length - HERO_PLATFORMS.length} more</li>
                </ul>

                <dl className="mt-8 grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-[var(--color-line)] bg-[var(--color-line)] sm:grid-cols-4">
                  {HERO_STATS.map((s) => (
                    <div key={s.label} className="bg-[#fff7f3] px-3 py-3.5 text-center">
                      <dt className="sr-only">{s.label}</dt>
                      <dd>
                        <span className="block font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">
                          <Localized text={s.n} />
                        </span>
                        <span className="mt-0.5 block text-[10px] font-semibold uppercase leading-tight tracking-wide text-muted">
                          {s.label}
                        </span>
                      </dd>
                    </div>
                  ))}
                </dl>
              </Reveal>

              <Reveal delay={0.1} className="order-2">
                <div id="get-started" className="scroll-mt-28">
                  <MaintenanceForm />
                </div>
              </Reveal>
            </div>
          </section>

          {/* ================= WHY IT MATTERS: full-bleed photo + timeline ================= */}
          <section
            className="relative isolate overflow-hidden bg-[#0b0b0b]"
            aria-labelledby="why-heading"
          >
            <Image
              src={IMG("site-down")}
              alt="Worried business owner staring at his laptop after his website went down"
              fill
              sizes="100vw"
              className="-z-10 object-cover object-[75%_25%]"
            />
            <span
              aria-hidden
              className="absolute inset-0 -z-10 bg-gradient-to-r from-black via-black/70 to-transparent max-lg:bg-black/70"
            />
            <div className="wrap py-20 md:py-28">
              <Reveal className="max-w-xl">
                <Tag light>Why it matters</Tag>
                <h2 id="why-heading" className={`mt-5 ${H2} text-white`}>
                  The site launched fine.{" "}
                  <span className="text-orange-300">Two months later, it broke.</span>
                </h2>
                <p className="mt-5 text-white/80">
                  A business skips maintenance to save money. Then one update or
                  an expired certificate takes the site down, the agency that
                  built it has moved on, and every day offline costs enquiries
                  and trust. A plan costs less than one lost week of leads.
                </p>
              </Reveal>

              <ol className="mt-12 grid list-none gap-4 sm:grid-cols-2 lg:grid-cols-4">
                {DOWNTIME_STORY.map((s, i) => (
                  <li key={s.when}>
                    <Reveal delay={i * 0.08}>
                      <article
                        className={`h-full rounded-3xl border p-6 backdrop-blur-md ${
                          i === DOWNTIME_STORY.length - 1
                            ? "border-orange/60 bg-orange/20"
                            : "border-white/15 bg-white/[0.07]"
                        }`}
                      >
                        <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange-300">
                          {s.when}
                        </p>
                        <h3 className="mt-2 text-lg font-extrabold text-white">{s.t}</h3>
                        <p className="mt-1.5 text-sm text-white/70">{s.d}</p>
                      </article>
                    </Reveal>
                  </li>
                ))}
              </ol>

              <div className="mt-10 flex flex-wrap items-center gap-4">
                <Cta>Stop it happening to my site</Cta>
                <span className="text-sm text-white/60">Free site check with every enquiry</span>
              </div>
            </div>
          </section>

          {/* ================= PLANS ================= */}
          <section className="section bg-section" id="plans" aria-labelledby="plans-heading">
            <div className="wrap-wide text-center">
              <Reveal>
                <span className="script-label">Maintenance plans</span>
                <h2 id="plans-heading" className={`mx-auto mt-5 max-w-5xl ${H2} text-ink`}>
                  Yearly plans, <span className="text-orange">priced by the hours you need</span>
                </h2>
                <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                  Pick the monthly hours that fit your site. Every plan covers
                  backups, security checks and support.
                </p>
              </Reveal>
            </div>

            <ul className="wrap mt-14 grid list-none items-stretch gap-6 md:grid-cols-3">
              {PLANS.map((p, i) => (
                <li key={p.name} className="flex">
                  <Reveal delay={i * 0.06} className="flex w-full">
                    <article
                      className={`relative flex w-full flex-col rounded-3xl p-8 ${
                        p.featured ? "grad-ink-orange text-white shadow-2xl md:-my-4 md:py-12" : "card"
                      }`}
                    >
                      {p.featured && (
                        <span className="absolute -top-3 left-8 rounded-full bg-orange px-3 py-1 font-[family-name:var(--font-display)] text-[11px] font-bold uppercase tracking-widest text-white">
                          Most picked
                        </span>
                      )}
                      <h3 className={`text-xl font-extrabold ${p.featured ? "text-white" : "text-ink"}`}>
                        {p.name}
                      </h3>
                      <p className={`mt-1 text-sm ${p.featured ? "text-white/70" : "text-muted"}`}>{p.hours}</p>
                      <p className="mt-6">
                        <span
                          className={`font-[family-name:var(--font-display)] text-4xl font-extrabold ${
                            p.featured ? "text-white" : "text-ink"
                          }`}
                        >
                          <Localized text={p.price} />
                        </span>
                        <span className={`ml-1.5 text-sm ${p.featured ? "text-white/70" : "text-muted"}`}>/ year</span>
                      </p>
                      <ul className="mt-7 grid flex-1 list-none content-start gap-3">
                        {p.items.map((it) => (
                          <li key={it} className="flex items-start gap-2.5 text-sm">
                            <Check
                              aria-hidden
                              className={`mt-0.5 h-4 w-4 shrink-0 ${p.featured ? "text-orange-300" : "text-orange"}`}
                              strokeWidth={3}
                            />
                            <span className={p.featured ? "text-white/90" : "text-body"}>{it}</span>
                          </li>
                        ))}
                      </ul>
                      <a
                        href="#contact"
                        data-consult
                        data-plan={p.name}
                        className={`btn mt-8 w-full ${p.featured ? "btn-primary" : "btn-outline"}`}
                      >
                        Choose {p.name}
                      </a>
                    </article>
                  </Reveal>
                </li>
              ))}
            </ul>
            <p className="wrap mt-8 text-center text-sm text-muted">
              <PriceNote />
            </p>
          </section>

          {/* ================= COVERAGE: bento grid ================= */}
          <section className="section bg-white" aria-labelledby="coverage-heading">
            <div className="wrap">
              <Reveal className="flex flex-wrap items-end justify-between gap-6">
                <div>
                  <span className="script-label">What is covered</span>
                  <h2 id="coverage-heading" className={`mt-5 max-w-2xl ${H2} text-ink`}>
                    Every part of the site, <span className="text-orange">looked after</span>
                  </h2>
                </div>
                <p className="max-w-sm text-body">
                  Six areas, one team. Whatever breaks, it is already somebody&apos;s job.
                </p>
              </Reveal>

              <ul className="mt-12 grid list-none auto-rows-fr gap-4 sm:grid-cols-2 lg:grid-cols-4">
                <li className="relative min-h-72 overflow-hidden rounded-3xl sm:col-span-2 lg:row-span-2">
                  <Image
                    src={IMG("hero")}
                    alt="Developer working late on a laptop in a dark office"
                    fill
                    sizes="(min-width: 1024px) 50vw, 100vw"
                    className="object-cover"
                  />
                  <span aria-hidden className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent" />
                  <div className="absolute inset-x-0 bottom-0 p-7">
                    <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange-300">
                      Behind the scenes
                    </p>
                    <p className="mt-2 max-w-md text-xl font-extrabold text-white">
                      Checks, backups and fixes run on a schedule, whether or not
                      anything looks wrong.
                    </p>
                  </div>
                </li>

                {COVERAGE.map((c, i) => {
                  const Icon = COVERAGE_ICONS[c.icon] ?? Check;
                  return (
                    <li key={c.t} className="flex">
                      <Reveal delay={(i % 2) * 0.05} className="flex w-full">
                        <article className="group w-full rounded-3xl border border-[var(--color-line)] bg-section p-6 transition hover:-translate-y-1 hover:border-orange hover:bg-white hover:shadow-xl">
                          <span className="grid h-11 w-11 place-items-center rounded-2xl bg-white text-orange shadow-sm transition group-hover:bg-orange group-hover:text-white">
                            <Icon aria-hidden className="h-5 w-5" strokeWidth={2} />
                          </span>
                          <h3 className="mt-4 text-lg font-extrabold text-ink">{c.t}</h3>
                          <p className="mt-2 text-sm text-body">{c.d}</p>
                        </article>
                      </Reveal>
                    </li>
                  );
                })}

                <li className="sm:col-span-2">
                  <Reveal className="h-full">
                    <div className="grad-ink-orange flex h-full flex-col justify-between gap-6 rounded-3xl p-7 sm:flex-row sm:items-center">
                      <p className="max-w-xs text-xl font-extrabold text-white">
                        Not sure what your site needs? Start with a free check.
                      </p>
                      <Cta>Get my free site check</Cta>
                    </div>
                  </Reveal>
                </li>
              </ul>
            </div>
          </section>

          {/* ================= PLATFORMS: logo tiles ================= */}
          <section className="section bg-section" aria-labelledby="platforms-heading">
            <div className="wrap text-center">
              <Reveal>
                <Tag>Every platform</Tag>
                <h2 id="platforms-heading" className={`mx-auto mt-5 max-w-4xl ${H2} text-ink`}>
                  Not just WordPress. <span className="text-orange">Any CMS, any code.</span>
                </h2>
                <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                  Hosted builders, open-source CMS, ecommerce platforms, hand
                  coded and AI-built sites. If it is live, it can be maintained.
                </p>
              </Reveal>

              <ul className="mx-auto mt-12 grid max-w-5xl list-none grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6">
                {PLATFORMS.map((p, i) => (
                  <li key={p.name}>
                    <Reveal delay={(i % 6) * 0.03} className="h-full">
                      <div className="flex h-full flex-col items-center justify-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-3 py-5 transition hover:-translate-y-1 hover:border-orange hover:shadow-lg">
                        <PlatformLogo name={p.name} logos={p.logos} />
                        <span className="font-[family-name:var(--font-display)] text-sm font-semibold text-ink">
                          {p.name}
                        </span>
                      </div>
                    </Reveal>
                  </li>
                ))}
                <li>
                  <a
                    href="#contact"
                    className="flex h-full flex-col items-center justify-center gap-2 rounded-2xl bg-orange px-3 py-5 text-white transition hover:-translate-y-1 hover:shadow-lg"
                  >
                    <ArrowRight aria-hidden className="h-7 w-7" />
                    <span className="font-[family-name:var(--font-display)] text-sm font-semibold">
                      Yours is not listed?
                    </span>
                  </a>
                </li>
              </ul>

              <div className="mt-10">
                <Cta>Get my website maintained</Cta>
              </div>
            </div>
          </section>

          {/* ================= UPDATES: card overlapping photo ================= */}
          <section className="bg-white py-20 md:py-28" aria-labelledby="updates-heading">
            <div className="wrap grid items-center lg:grid-cols-12">
              <Reveal className="lg:col-span-8 lg:col-start-5 lg:row-start-1">
                <div className="relative aspect-[4/3] overflow-hidden rounded-[32px] lg:aspect-[16/11]">
                  <Image
                    src={IMG("updates")}
                    alt="Developer typing code with programming screens in front"
                    fill
                    sizes="(min-width: 1024px) 66vw, 100vw"
                    className="object-cover"
                  />
                </div>
              </Reveal>
              <Reveal
                delay={0.1}
                className="relative z-10 -mt-16 mx-3 lg:col-span-6 lg:col-start-1 lg:row-start-1 lg:mx-0 lg:mt-0"
              >
                <div className="rounded-[28px] border border-[var(--color-line)] bg-white p-7 shadow-2xl md:p-10">
                  <Tag>Updates and changes</Tag>
                  <h2 id="updates-heading" className={`mt-5 ${H2} text-ink`}>
                    Updates done properly, <span className="text-orange">not just clicked</span>
                  </h2>
                  <p className="mt-4 text-body">
                    A careless update is one of the most common reasons a site
                    breaks. Every change is checked before and after, so the site
                    you had in the morning still works in the evening.
                  </p>
                  <ul className="mt-6 grid list-none gap-3">
                    {UPDATE_POINTS.map((p) => (
                      <Tick key={p}>{p}</Tick>
                    ))}
                  </ul>
                  <div className="mt-8">
                    <Cta>Hand over my updates</Cta>
                  </div>
                </div>
              </Reveal>
            </div>
          </section>

          {/* ================= SECURITY: panoramic photo + floating points ================= */}
          <section className="bg-section py-20 md:py-28" aria-labelledby="security-heading">
            <div className="wrap">
              <Reveal className="mx-auto max-w-3xl text-center">
                <Tag>Backups and security</Tag>
                <h2 id="security-heading" className={`mt-5 ${H2} text-ink`}>
                  If something goes wrong, <span className="text-orange">the site comes back</span>
                </h2>
                <p className="mx-auto mt-5 max-w-2xl text-body">
                  Hacks, bad updates and hosting failures happen to sites of every
                  size. What matters is having a clean copy and someone ready to
                  restore it.
                </p>
              </Reveal>

              <Reveal className="mt-12">
                <div className="relative aspect-[16/9] overflow-hidden rounded-[32px] md:aspect-[21/8]">
                  <Image
                    src={IMG("security")}
                    alt="Rows of server racks in a data centre"
                    fill
                    sizes="100vw"
                    className="object-cover"
                  />
                  <span aria-hidden className="absolute inset-0 bg-gradient-to-t from-black/50 to-transparent" />
                </div>
              </Reveal>

              <ul className="relative z-10 mx-3 -mt-10 grid list-none gap-3 sm:grid-cols-2 md:-mt-16 md:mx-8 lg:grid-cols-4">
                {SECURITY_POINTS.map((p, i) => (
                  <li key={p}>
                    <Reveal delay={i * 0.06} className="h-full">
                      <div className="flex h-full items-start gap-3 rounded-2xl bg-white p-5 shadow-xl">
                        <span className="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange text-white">
                          <ShieldCheck aria-hidden className="h-4 w-4" />
                        </span>
                        <span className="text-sm font-semibold text-ink">{p}</span>
                      </div>
                    </Reveal>
                  </li>
                ))}
              </ul>

              <div className="mt-12 text-center">
                <Cta>Protect my website</Cta>
              </div>
            </div>
          </section>

          {/* ================= WHY ME: numbered cards ================= */}
          <ImageBand labelledBy="choose-heading">
            <div className="wrap grid items-end gap-10 py-20 md:py-28 lg:grid-cols-[0.9fr_1.1fr]">
              <Reveal>
                <Tag light>Why me</Tag>
                <h2 id="choose-heading" className={`mt-5 ${H2} text-white`}>
                  One team that already knows{" "}
                  <span className="text-orange-300">how your site works</span>
                </h2>
                <p className="mt-5 max-w-md text-white/75">
                  No ticket queues and no new person every month. The same people
                  look after your site from the first check onwards.
                </p>
                <div className="mt-8">
                  <Cta>Talk to me about your site</Cta>
                </div>
              </Reveal>
              <ol className="grid list-none gap-4">
                {WHY_CHOOSE.map((w, i) => (
                  <li key={w.t}>
                    <Reveal delay={i * 0.08}>
                      <article className="flex gap-5 rounded-3xl border border-white/15 bg-white/[0.06] p-6 backdrop-blur-sm">
                        <span className="font-[family-name:var(--font-display)] text-4xl font-extrabold leading-none text-orange-300">
                          0{i + 1}
                        </span>
                        <div>
                          <h3 className="text-lg font-extrabold text-white">{w.t}</h3>
                          <p className="mt-1.5 text-white/75">{w.d}</p>
                        </div>
                      </article>
                    </Reveal>
                  </li>
                ))}
              </ol>
            </div>
          </ImageBand>

          <div className="bg-section">
            {/* ---- FAQ: native <details> keeps every answer in the DOM ---- */}
            <section className="section" id="faq" aria-labelledby="faq-heading">
              <div className="wrap grid gap-10 lg:grid-cols-[0.8fr_2fr]">
                <Reveal className="lg:sticky lg:top-28 lg:self-start">
                  <span className="script-label">Common questions</span>
                  <h2 id="faq-heading" className={`mt-5 ${H2} text-ink`}>
                    Website maintenance <span className="text-orange">questions, answered</span>
                  </h2>
                  <p className="mt-4 text-body">
                    Cost, platforms, security and how we work together. Still
                    unsure? Ask me directly.
                  </p>
                  <div className="mt-7">
                    <Cta>Ask my question</Cta>
                  </div>
                </Reveal>

                <div className="grid gap-10">
                  {FAQ_GROUPS.map((g) => (
                    <div key={g.h}>
                      <h3 className="mb-4 font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                        {g.h}
                      </h3>
                      <div className="grid gap-3">
                        {g.items.map((f) => (
                          <details
                            key={f.q}
                            className="group overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"
                          >
                            <summary className="flex cursor-pointer items-center justify-between gap-4 px-6 py-5 font-[family-name:var(--font-display)] font-semibold text-ink marker:content-['']">
                              <h4 className="text-base font-semibold">{f.q}</h4>
                              <span className="grid h-5 w-5 shrink-0 place-items-center rounded-full bg-ink/5 text-ink transition-transform duration-300 group-open:rotate-45 group-open:bg-orange group-open:text-white">
                                <svg width="10" height="10" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" aria-hidden="true">
                                  <path d="M7 1v12M1 7h12" />
                                </svg>
                              </span>
                            </summary>
                            <p className="px-6 pb-6 text-sm text-body">
                              <Localized text={f.a} />
                            </p>
                          </details>
                        ))}
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </section>

            {/* ---- related services ---- */}
            <section className="pb-4" aria-labelledby="related-heading">
              <div className="wrap text-center">
                <h2 id="related-heading" className="text-2xl font-extrabold text-ink">
                  Services that pair with <span className="text-orange">website maintenance</span>
                </h2>
                <ul className="mt-7 flex list-none flex-wrap justify-center gap-3">
                  {RELATED_SERVICES.map((r) => (
                    <li key={r.href}>
                      <Link
                        href={r.href}
                        className="inline-flex rounded-full border border-[var(--color-line)] bg-white px-5 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold text-ink transition hover:border-orange hover:text-orange"
                      >
                        {r.label}
                      </Link>
                    </li>
                  ))}
                </ul>
              </div>
            </section>

            <FinalCTA
              heading={
                <>
                  Keep your website <span className="text-orange-300">running like day one</span>
                </>
              }
              sub="Tell me what your site runs on and what keeps going wrong. I will check it for free and suggest the right plan."
              cta={CTA_LABEL}
            />
          </div>
        </main>
        {/* This page's own popup in place of the site-wide ConsultPopup: every
            CTA opens the three-step maintenance form. Inside the currency
            provider so plan prices in the form are localised too. */}
        <MaintenancePopup />
      </CurrencyProvider>
      <Footer />
      <BackToTop />
      <MobileBookBar label={CTA_LABEL} />
    </>
  );
}
