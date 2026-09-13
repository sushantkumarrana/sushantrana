"use client";

import Link from "next/link";
import {
  Check,
  GraduationCap,
  Gauge,
  Minus,
  Palette,
  Plug,
  Search,
  Smartphone,
  type LucideIcon,
} from "lucide-react";
import Nav from "./Nav";
import Footer from "./Footer";
import Reveal from "./Reveal";
import FloatingLogos from "./FloatingLogos";
import StraightMarquee from "./StraightMarquee";
import BackToTop from "./BackToTop";
import MobileBookBar from "./MobileBookBar";
import Breadcrumbs from "./Breadcrumbs";
import PhoneScroll from "./PhoneScroll";
import ImgOrPlaceholder from "./ImgOrPlaceholder";
import FinalCTA from "./sections/FinalCTA";
import HeroForm from "./shopify/HeroForm";
import QuotePopup from "./shopify/QuotePopup";
import { AnimatedNumber } from "./shopify/animate";
import LogoStrip from "./shopify/LogoStrip";
import ProcessSteps from "./shopify/ProcessSteps";
import ReviewSlider from "./shopify/ReviewSlider";
import ProductCards from "./shopify/ProductCards";
import {
  AnalyticsPanel,
  GrowthPanel,
  ProjectDashboard,
  StoreOverview,
} from "./shopify/Mocks";
import { CLIENTS } from "@/lib/clients";
import {
  COMPARE_ROWS,
  COMPETITIVE_EDGE,
  CTA_LABEL,
  CUSTOM_DEV_POINTS,
  HERO_STATS,
  PRODUCT_CARD_POINTS,
  PRODUCT_PAGE_POINTS,
  RELATED_SERVICES,
  REVENUE_MACHINE,
  SHOPIFY_FAQS,
  SPRINT,
  SPRINT_TIMELINE,
  STORE_EXPERIENCE_POINTS,
  STORE_PAGES,
  TECH_STACK,
  WHAT_YOU_GET,
  WHY_CHOOSE,
} from "@/lib/shopify";

/* ------------------------------------------------------------------ bits */

/** Photographic band, reusing the same background image as the homepage
 *  closing CTA so the dark sections across the site read as one family. */
function ImageBand({
  children,
  labelledBy,
  className = "",
}: {
  children: React.ReactNode;
  labelledBy: string;
  className?: string;
}) {
  return (
    <section
      aria-labelledby={labelledBy}
      className={`relative bg-[#050505] bg-cover bg-center bg-no-repeat ${className}`}
      style={{ backgroundImage: "url(/footer/footer-bg.png)" }}
    >
      {/* Decoration is clipped here rather than on the <section>: an
          overflow-hidden ancestor turns into the scroll container and stops
          position: sticky working for the panels inside. */}
      <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
        {/* keeps text legible whatever the photograph is doing underneath */}
        <span className="absolute inset-0 bg-black/45" />
        <span className="absolute left-1/2 top-0 h-80 w-[36rem] -translate-x-1/2 rounded-full bg-orange/25 blur-[120px]" />
      </div>
      <div className="relative">{children}</div>
    </section>
  );
}

function Tick({ children, light = false }: { children: React.ReactNode; light?: boolean }) {
  return (
    <li className={`flex items-start gap-3 ${light ? "text-white" : "text-ink"}`}>
      <span className="mt-0.5 grid h-6 w-6 shrink-0 place-items-center rounded-full bg-orange text-white">
        <Check aria-hidden className="h-3.5 w-3.5" strokeWidth={3} />
      </span>
      <span className="font-medium">{children}</span>
    </li>
  );
}

function Tag({ children, light = false }: { children: React.ReactNode; light?: boolean }) {
  return (
    <span
      className={`inline-flex rounded-full px-4 py-1.5 font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest ${
        light
          ? "border border-white/20 bg-white/10 text-orange-300"
          : "border border-[var(--color-line)] bg-white text-orange"
      }`}
    >
      {children}
    </span>
  );
}

/** Panel columns pin while the copy column beside them keeps scrolling, so a
 *  short illustration stays in view until its section is finished. Large
 *  screens only — on a phone the two columns are stacked, and pinning one of
 *  them there would just hide the text. */
const STICKY = "lg:sticky lg:top-24 lg:self-start";

const GET_ICONS: Record<string, LucideIcon> = {
  palette: Palette,
  gauge: Gauge,
  smartphone: Smartphone,
  search: Search,
  plug: Plug,
  graduation: GraduationCap,
};

/** Phone screens: full-length mobile screenshots of real builds, served from
 *  /public/services/shopify/ as WebP. A missing file falls back to the built-in
 *  wireframe rather than a broken frame. */
const STORE_PHONES = [
  {
    file: "home-1",
    label: "Homepage",
    sub: "Store one",
    alt: "Full mobile homepage of a Shopify store designed and built by Sushant Rana",
  },
  {
    file: "home-2",
    label: "Homepage",
    sub: "Store two",
    alt: "Full mobile homepage of a second Shopify store designed and built by Sushant Rana",
  },
];
const PRODUCT_PHONES = [
  {
    file: "product-page-1",
    label: "Product page",
    sub: "Store one",
    alt: "Full mobile Shopify product page built by Sushant Rana, showing the gallery, variants and add to cart",
  },
  {
    file: "product-page-3",
    label: "Product page",
    sub: "Store two",
    alt: "Second full mobile Shopify product page built by Sushant Rana, showing pricing, reviews and trust signals",
  },
];

/** Shopify builds shown in the results block. Only OurKnots has a published
 *  figure (from lib/clients); Hunzo and Iksha describe the build instead of
 *  quoting a number nobody has supplied. */
const OURKNOTS = CLIENTS.find((c) => c.slug === "ourknots");
const SHOPIFY_RESULTS = [
  {
    name: "OurKnots",
    industry: "Laces and borders",
    result: OURKNOTS?.result ?? "Shopify store design and development",
  },
  {
    name: "Hunzo.in",
    industry: "Baby products",
    result: "Shopify store design and development for a brand selling baby care and baby essentials.",
  },
  {
    name: "Iksha The Label",
    industry: "Artificial and American diamond jewellery",
    result: "Shopify store design and development for an artificial and American diamond jewellery label.",
  },
];

/** Portfolio slots. Each falls back to a placeholder until the screenshot is
 *  added at /public/services/shopify/work-N.webp. */
const WORK_SLOTS = [1, 2, 3, 4, 5, 6];

export default function ShopifyDevelopment() {
  return (
    <>
      <Nav />
      <main id="main">
        {/* ================= HERO ================= */}
        <section className="relative overflow-hidden bg-white" aria-labelledby="shopify-heading">
          <div className="wrap relative z-10 pt-24">
            <Breadcrumbs
              trail={[
                { label: "Services", href: "/services" },
                { label: "Shopify Store Development" },
              ]}
            />
          </div>

          <div className="wrap relative z-10 grid items-start gap-8 py-6 md:py-8 lg:grid-cols-[1.05fr_0.95fr] lg:gap-12">
            {/* headline first on every screen */}
            <Reveal className="order-1">
              <Tag>Shopify store development</Tag>
              <h1
                id="shopify-heading"
                className="mt-4 text-[clamp(2rem,7vw,2.7rem)] font-extrabold leading-[1.08] text-ink"
              >
                Shopify store development that{" "}
                <span className="text-orange">starts selling on first day</span>
              </h1>
              <p className="mt-4 max-w-xl text-body">
                I am <strong className="font-semibold text-ink">Sushant Rana</strong>, and I
                have a team of Shopify developers who build custom stores for
                brands across India, the UAE, Canada, Australia and the United
                States. No recycled themes, no page builders, every screen
                shaped around turning a visitor into a buyer.
              </p>

              <div className="mt-6 flex flex-wrap gap-3">
                <a href="#contact" className="btn btn-primary">
                  {CTA_LABEL}
                </a>
                <a href="#work" className="btn btn-outline">
                  See recent Shopify work
                </a>
              </div>
            </Reveal>

            {/* the form sits inside the first screen — second on mobile, beside
                the headline on desktop */}
            <Reveal delay={0.1} className="order-2 lg:row-span-2">
              <HeroForm />
            </Reveal>

            <Reveal className="order-3 lg:col-start-1">
              <dl className="grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-[var(--color-line)] bg-[var(--color-line)] sm:grid-cols-4">
                {HERO_STATS.map((s) => (
                  <div key={s.label} className="bg-[#fff7f3] px-3 py-3.5 text-center">
                    <dt className="sr-only">{s.label}</dt>
                    <dd>
                      <span className="block font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">
                        <AnimatedNumber value={s.n} />
                      </span>
                      <span className="mt-0.5 block text-[10px] font-semibold uppercase leading-tight tracking-wide text-muted">
                        {s.label}
                      </span>
                    </dd>
                  </div>
                ))}
              </dl>
            </Reveal>
          </div>

          <div className="wrap-wide relative z-10 border-t border-[var(--color-line)]">
            <LogoStrip />
          </div>
        </section>

        {/* ================= WHOLE STOREFRONTS (photo band) ================= */}
        <ImageBand labelledBy="store-heading">
          <div className="wrap grid items-center gap-16 py-20 md:py-28 lg:grid-cols-2">
            <Reveal>
              <Tag light>Complete store design</Tag>
              <h2
                id="store-heading"
                className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-white"
              >
                Amazing store experience,{" "}
                <span className="text-orange-300">not just a basic ecommerce website</span>
              </h2>
              <p className="mt-5 max-w-xl text-white/80">
                We create a seamless, cohesive shopping experience across your
                entire store, from the homepage to checkout. Every page is
                thoughtfully designed to engage customers, build confidence and
                guide them smoothly towards a great purchase.
              </p>
              <ul className="mt-7 grid list-none gap-3.5">
                {STORE_EXPERIENCE_POINTS.map((p) => (
                  <Tick key={p} light>
                    {p}
                  </Tick>
                ))}
              </ul>
              <a href="#contact" className="btn btn-primary mt-9">
                Get your storefront designed
              </a>
            </Reveal>

            <Reveal delay={0.1}>
              <div className="flex justify-center gap-6">
                {STORE_PHONES.map((p) => (
                  <PhoneScroll
                    key={p.file}
                    dark
                    src={`/services/shopify/${p.file}.webp`}
                    alt={p.alt}
                    label={p.label}
                    sub={p.sub}
                  />
                ))}
              </div>
            </Reveal>
          </div>
        </ImageBand>

        {/* ================= PRODUCT PAGES ================= */}
        <section className="bg-white" aria-labelledby="product-pages-heading">
          <div className="wrap grid items-center gap-16 py-20 md:py-28 lg:grid-cols-2">
            <Reveal className="order-2 lg:order-1">
              <div className="flex justify-center gap-6">
                {PRODUCT_PHONES.map((p) => (
                  <PhoneScroll
                    key={p.file}
                    src={`/services/shopify/${p.file}.webp`}
                    alt={p.alt}
                    label={p.label}
                    sub={p.sub}
                  />
                ))}
              </div>
            </Reveal>

            <Reveal delay={0.1} className="order-1 lg:order-2">
              <Tag>Product pages</Tag>
              <h2
                id="product-pages-heading"
                className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
              >
                Product page that{" "}
                <span className="text-orange">turns browsers into buyers</span>
              </h2>
              <p className="mt-5 max-w-xl text-body">
                A product page is where the decision actually happens. Each one
                I build answers the question a shopper is holding at that exact
                moment, then puts the next step directly under their thumb.
              </p>
              <ul className="mt-7 grid list-none gap-3.5">
                {PRODUCT_PAGE_POINTS.map((p) => (
                  <Tick key={p}>{p}</Tick>
                ))}
              </ul>
              <a href="#contact" className="btn btn-primary mt-9">
                Get a product page like this
              </a>
            </Reveal>
          </div>
        </section>

        {/* ================= GREY REGION ================= */}
        <div className="relative bg-section">
          <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
            <FloatingLogos />
          </div>

          <div className="relative z-10">
            {/* ---- product cards ---- */}
            <section className="section" aria-labelledby="product-cards-heading">
              <div className="wrap grid items-start gap-14 lg:grid-cols-2">
                <Reveal>
                  <Tag>Product cards</Tag>
                  <h2
                    id="product-cards-heading"
                    className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Product card that <span className="text-orange">drives revenue</span>
                  </h2>
                  <p className="mt-5 max-w-xl text-body">
                    Most shoppers judge a product before they ever open its
                    page. The cards I build carry the variant picker, the price,
                    the proof and the add to cart button, so a decision can be
                    made straight from the grid.
                  </p>
                  <ul className="mt-7 grid list-none gap-3.5">
                    {PRODUCT_CARD_POINTS.map((p) => (
                      <Tick key={p}>{p}</Tick>
                    ))}
                  </ul>
                  <a href="#contact" className="btn btn-primary mt-9">
                    Get custom product cards
                  </a>
                </Reveal>

                <Reveal delay={0.1} className={STICKY}>
                  <ProductCards />
                </Reveal>
              </div>
            </section>

            <div className="py-8">
              <StraightMarquee
                fade={false}
                variant="ink"
                dur={55}
                items={[
                  "Shopify",
                  "Theme development",
                  "Migrations",
                  "Speed",
                  "Checkout",
                  "Conversion",
                ]}
              />
            </div>

            {/* ---- custom development ---- */}
            <section className="section" aria-labelledby="custom-dev-heading">
              <div className="wrap grid items-start gap-14 lg:grid-cols-2">
                <Reveal className={`order-2 lg:order-1 ${STICKY}`}>
                  <StoreOverview pages={STORE_PAGES} stack={TECH_STACK} />
                </Reveal>

                <Reveal delay={0.1} className="order-1 lg:order-2">
                  <Tag>Custom development</Tag>
                  <h2
                    id="custom-dev-heading"
                    className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Your Shopify store,{" "}
                    <span className="text-orange">designed to generate revenue</span>
                  </h2>
                  <p className="mt-5 max-w-xl text-body">
                    Nothing here comes out of a drag and drop builder. Your
                    Shopify theme is architected from the first component
                    upwards: quick to load, honest to your brand, and shaped so
                    the path to checkout never doubles back on itself.
                  </p>
                  <ul className="mt-8 grid list-none gap-5">
                    {CUSTOM_DEV_POINTS.map((p) => (
                      <li key={p.t} className="card p-6">
                        <h3 className="text-lg font-extrabold text-ink">{p.t}</h3>
                        <p className="mt-2 text-body">{p.d}</p>
                      </li>
                    ))}
                  </ul>
                </Reveal>
              </div>
            </section>
          </div>
        </div>

        {/* ================= SPRINT (photo band) ================= */}
        <ImageBand labelledBy="sprint-heading">
          <div className="wrap grid items-start gap-16 py-20 md:py-28 lg:grid-cols-2" id="process">
            <Reveal>
              <Tag light>How the build runs</Tag>
              <h2
                id="sprint-heading"
                className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-white"
              >
                From sketch to live Shopify store{" "}
                <span className="text-orange-300">in 4-6 weeks</span>
              </h2>
              <p className="mt-5 max-w-xl text-white/80">
                One sequence, followed on every project, with you told where
                things stand at each stage. No silent weeks, no scope quietly
                growing, no launch date that keeps sliding.
              </p>
              <ol className="mt-8 grid list-none gap-5">
                {SPRINT.map((s) => (
                  <li key={s.n} className="flex gap-4">
                    <span className="grid h-11 w-11 shrink-0 place-items-center rounded-2xl bg-orange font-[family-name:var(--font-display)] font-extrabold text-white">
                      {s.n}
                    </span>
                    <div>
                      <h3 className="text-lg font-extrabold text-white">{s.t}</h3>
                      <p className="mt-1.5 text-white/75">{s.d}</p>
                    </div>
                  </li>
                ))}
              </ol>
              <a href="#contact" className="btn btn-primary mt-9">
                Book a call about your build
              </a>
            </Reveal>

            <Reveal delay={0.1} className={STICKY}>
              <ProjectDashboard timeline={SPRINT_TIMELINE} />
            </Reveal>
          </div>
        </ImageBand>

        {/* ================= GREY REGION 2 ================= */}
        <div className="relative bg-section">
          <div className="relative z-10">
            {/* ---- what I measure ---- */}
            <section className="section" aria-labelledby="results-heading">
              <div className="wrap grid items-start gap-14 lg:grid-cols-2">
                <Reveal className={`order-2 lg:order-1 ${STICKY}`}>
                  <GrowthPanel />
                </Reveal>

                <Reveal delay={0.1} className="order-1 lg:order-2">
                  <Tag>The measure of a build</Tag>
                  <h2
                    id="results-heading"
                    className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Shopify stores that <span className="text-orange">deliver real sales</span>
                  </h2>
                  <p className="mt-5 max-w-xl text-body">
                    A launch is only worth celebrating if the store starts
                    trading. These are Shopify stores built for real brands, and
                    the same standard every new storefront is held to.
                  </p>
                  <ul className="mt-8 grid list-none gap-4">
                    {SHOPIFY_RESULTS.map((c) => (
                      <li key={c.name} className="card p-6">
                        <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                          {c.industry}
                        </p>
                        <h3 className="mt-1.5 text-lg font-extrabold text-ink">{c.name}</h3>
                        <p className="mt-2 text-body">{c.result}</p>
                      </li>
                    ))}
                  </ul>
                  <Link
                    href="/about#clients"
                    className="mt-7 inline-flex font-semibold text-orange underline underline-offset-4"
                  >
                    See every brand I have worked with
                  </Link>
                </Reveal>
              </div>
            </section>

            {/* ---- portfolio strip ---- */}
            <section className="section" id="work" aria-labelledby="work-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">Recent work</span>
                  <h2
                    id="work-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Storefronts I have <span className="text-orange">built and rebuilt</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    Recent Shopify and ecommerce builds drifting past. Hover to pause on one.
                  </p>
                </Reveal>
              </div>

              {/* Portrait cards drifting left to right on their own. Hovering
                  pauses the track so a screenshot can actually be looked at. */}
              <div className="marquee-nofade marquee--rev mt-12 overflow-hidden">
                <ul
                  className="marquee__track list-none py-2"
                  style={{ ["--dur" as string]: "70s" }}
                  aria-label="Recent store builds"
                >
                  {[...WORK_SLOTS, ...WORK_SLOTS].map((n, i) => (
                    <li key={`${n}-${i}`} className="mx-1.5 w-[58vw] max-w-[236px] shrink-0">
                      <figure className="m-0">
                        <ImgOrPlaceholder
                          src={`/services/shopify/work-${n}.webp`}
                          alt={`Full-page screenshot of Shopify store build number ${n} by Sushant Rana`}
                          /* Tall portrait, anchored to the top: a storefront is
                             judged on its header and hero, and `cover` would
                             otherwise crop to the middle of the page. */
                          ratio="3/8"
                          position="top"
                          seed={i}
                          sizes="(min-width: 768px) 236px, 58vw"
                        />

                      </figure>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="wrap mt-8 text-center">
                <Link href="/about#clients" className="btn btn-outline">
                  View the full client list
                </Link>
              </div>
            </section>

            <ReviewSlider />

            <div className="py-8">
              <StraightMarquee
                fade={false}
                variant="orange"
                dur={50}
                reverse
                items={[
                  "New store setup",
                  "Theme design",
                  "Redesign",
                  "Migration",
                  "Apps and payments",
                  "Speed",
                ]}
              />
            </div>

            {/* ---- what you get ---- */}
            <section className="section" aria-labelledby="get-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">What you get</span>
                  <h2
                    id="get-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Everything a Shopify store <span className="text-orange">needs to compete</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    A finished, trading storefront is handed over, not a
                    half-built theme with a list of things left for you to sort
                    out.
                  </p>
                </Reveal>
              </div>

              <ul className="wrap mt-14 grid list-none gap-5 sm:grid-cols-2 lg:grid-cols-3">
                {WHAT_YOU_GET.map((w, i) => {
                  const Icon = GET_ICONS[w.icon] ?? Check;
                  return (
                    <li key={w.t} className="flex">
                      <Reveal delay={(i % 3) * 0.05} className="flex w-full">
                        <article className="card w-full p-7">
                          <span className="grid h-12 w-12 place-items-center rounded-2xl bg-orange/10 text-orange">
                            <Icon aria-hidden className="h-6 w-6" strokeWidth={2} />
                          </span>
                          <h3 className="mt-5 text-xl font-extrabold text-ink">{w.t}</h3>
                          <p className="mt-2.5 text-body">{w.d}</p>
                        </article>
                      </Reveal>
                    </li>
                  );
                })}
              </ul>
            </section>

            {/* ---- interactive process ---- */}
            <section className="section" aria-labelledby="process-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">Step by step</span>
                  <h2
                    id="process-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    How a build runs, <span className="text-orange">from concept to launch</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    Pick a stage to follow along, or read all four below.
                  </p>
                </Reveal>
              </div>

              <ProcessSteps />
            </section>
          </div>
        </div>

        {/* ================= SELLING MACHINES (photo band) ================= */}
        <ImageBand labelledBy="machine-heading">
          <div className="wrap py-20 md:py-28">
            <div className="text-center">
              <Reveal>
                <Tag light>Why me</Tag>
                <h2
                  id="machine-heading"
                  className="mx-auto mt-5 max-w-4xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-white"
                >
                  I do not hand over websites.{" "}
                  <span className="text-orange-300">I hand over selling machines.</span>
                </h2>
                <p className="mx-auto mt-5 max-w-2xl text-white/75">
                  Plenty of studios will give you something handsome. What you
                  actually need is a storefront that earns its keep every day it
                  is live.
                </p>
              </Reveal>
            </div>

            <ul className="mt-14 grid list-none gap-6 md:grid-cols-3">
              {REVENUE_MACHINE.map((r, i) => (
                <li key={r.t} className="flex">
                  <Reveal delay={(i % 3) * 0.06} className="flex w-full">
                    <article className="w-full rounded-3xl border border-white/15 bg-white/[0.06] p-7 backdrop-blur-sm">
                      <h3 className="text-xl font-extrabold text-white">{r.t}</h3>
                      <p className="mt-3 text-white/75">{r.d}</p>
                    </article>
                  </Reveal>
                </li>
              ))}
            </ul>
          </div>
        </ImageBand>

        {/* ================= GREY REGION 3 ================= */}
        <div className="relative bg-section">
          <div className="relative z-10">
            {/* ---- why founders choose me ---- */}
            <section className="section" aria-labelledby="choose-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">Why founders choose me</span>
                  <h2
                    id="choose-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Why founders hand me{" "}
                    <span className="text-orange">their Shopify stores</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    Building the store is the easy half. Building something that
                    keeps earning is the part worth paying for.
                  </p>
                </Reveal>
              </div>

              <ul className="wrap mt-14 grid list-none gap-6 md:grid-cols-3">
                {WHY_CHOOSE.map((w, i) => (
                  <li key={w.t} className="flex">
                    <Reveal delay={(i % 3) * 0.06} className="flex w-full">
                      <article className="card w-full p-7">
                        <h3 className="text-xl font-extrabold text-ink">{w.t}</h3>
                        <p className="mt-3 text-body">{w.d}</p>
                      </article>
                    </Reveal>
                  </li>
                ))}
              </ul>

              <div className="wrap mt-10">
                <Reveal>
                  <div className="grad-ink-orange relative overflow-hidden rounded-[36px] p-10 text-center md:p-14">
                    <span
                      aria-hidden
                      className="pointer-events-none absolute left-1/2 top-0 h-64 w-64 -translate-x-1/2 rounded-full bg-orange/40 blur-[100px]"
                    />
                    <div className="relative">
                      <Tag light>My commitment</Tag>
                      <h3 className="mx-auto mt-5 max-w-3xl text-[clamp(1.4rem,3vw,2.2rem)] font-extrabold text-white">
                        If the new storefront does not beat the one you have, I
                        keep working until it does.
                      </h3>
                      <p className="mx-auto mt-4 max-w-2xl text-white/75">
                        Quicker pages, a cleaner experience on a phone and a
                        shorter path to checkout. That is the bar the build has
                        to clear before I call it finished.
                      </p>
                      <div className="mt-8 flex flex-wrap justify-center gap-3">
                        <a href="#contact" className="btn btn-primary">
                          {CTA_LABEL}
                        </a>
                        <a href="#work" className="btn btn-outline !border-white/30 !text-white">
                          See recent work
                        </a>
                      </div>
                    </div>
                  </div>
                </Reveal>
              </div>
            </section>

            {/* ---- competitive edge ---- */}
            <section className="section" aria-labelledby="edge-heading">
              <div className="wrap grid items-start gap-14 lg:grid-cols-2">
                <Reveal>
                  <Tag>The edge</Tag>
                  <h2
                    id="edge-heading"
                    className="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Where the edge over{" "}
                    <span className="text-orange">your competitors comes from</span>
                  </h2>
                  <p className="mt-5 max-w-xl text-body">
                    Usability reviews, speed work, phone first layouts and the
                    custom functionality your operation actually needs, so the
                    storefront keeps pace with the business behind it.
                  </p>
                  <ul className="mt-8 grid list-none gap-4">
                    {COMPETITIVE_EDGE.map((e) => (
                      <li key={e.t} className="card p-5">
                        <h3 className="text-base font-extrabold text-ink">{e.t}</h3>
                        <p className="mt-1.5 text-sm text-body">{e.d}</p>
                      </li>
                    ))}
                  </ul>
                </Reveal>

                <Reveal delay={0.1} className={STICKY}>
                  <AnalyticsPanel />
                </Reveal>
              </div>
            </section>

            {/* ---- comparison ---- */}
            <section className="section" id="compare" aria-labelledby="compare-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">The difference</span>
                  <h2
                    id="compare-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Working with me, a freelancer,{" "}
                    <span className="text-orange">or an agency</span>
                  </h2>
                </Reveal>
              </div>

              <div className="wrap mt-12">
                <Reveal>
                  <div className="overflow-x-auto rounded-3xl border border-[var(--color-line)] bg-white">
                    <table className="w-full border-collapse text-left sm:min-w-[640px]">
                      <caption className="sr-only">
                        Cost, timeline, code quality, support and ownership compared across
                        Sushant Rana, a freelancer and an agency
                      </caption>
                      <thead>
                        <tr className="border-b border-[var(--color-line)]">
                          <th scope="col" className="px-3 py-3 sm:px-5 sm:py-4">
                            <span className="sr-only">What you are comparing</span>
                          </th>
                          <th
                            scope="col"
                            className="border-b-2 border-orange bg-orange/10 px-2 py-3 text-center font-[family-name:var(--font-display)] text-[13px] font-extrabold text-orange sm:px-5 sm:py-4 sm:text-base"
                          >
                            Sushant Rana
                          </th>
                          <th
                            scope="col"
                            className="px-2 py-3 text-center font-[family-name:var(--font-display)] text-[13px] font-extrabold text-ink sm:px-5 sm:py-4 sm:text-base"
                          >
                            Freelancers
                          </th>
                          <th
                            scope="col"
                            className="px-2 py-3 text-center font-[family-name:var(--font-display)] text-[13px] font-extrabold text-ink sm:px-5 sm:py-4 sm:text-base"
                          >
                            Agencies
                          </th>
                        </tr>
                      </thead>
                      <tbody>
                        {COMPARE_ROWS.map((r) => (
                          <tr key={r.label} className="border-b border-[var(--color-line)] last:border-0">
                            <th
                              scope="row"
                              className="border-r border-[var(--color-line)] px-3 py-3 text-[11px] font-semibold text-ink sm:px-5 sm:py-4 sm:text-sm"
                            >
                              {r.label}
                            </th>
                            <td className="border-r border-[var(--color-line)] bg-orange/5 px-2 py-3 text-center text-[11px] font-semibold text-ink sm:px-5 sm:py-4 sm:text-left sm:text-sm">
                              <span className="sm:flex sm:items-center sm:gap-2">
                                <Check
                                  aria-hidden
                                  className="hidden h-4 w-4 shrink-0 text-orange sm:block"
                                  strokeWidth={3}
                                />
                                {r.me}
                              </span>
                            </td>
                            <td className="border-r border-[var(--color-line)] px-2 py-3 text-center text-[11px] text-muted sm:px-5 sm:py-4 sm:text-left sm:text-sm">
                              <span className="sm:flex sm:items-center sm:gap-2">
                                <Minus aria-hidden className="hidden h-4 w-4 shrink-0 opacity-50 sm:block" />
                                {r.freelancer}
                              </span>
                            </td>
                            <td className="px-2 py-3 text-center text-[11px] text-muted sm:px-5 sm:py-4 sm:text-left sm:text-sm">
                              <span className="sm:flex sm:items-center sm:gap-2">
                                <Minus aria-hidden className="hidden h-4 w-4 shrink-0 opacity-50 sm:block" />
                                {r.agency}
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </Reveal>
              </div>
            </section>

            {/* ---- related services ---- */}
            <section className="section" aria-labelledby="related-heading">
              <div className="wrap text-center">
                <Reveal>
                  <h2 id="related-heading" className="text-2xl font-extrabold text-ink">
                    Services that pair with a <span className="text-orange">Shopify build</span>
                  </h2>
                  <p className="mx-auto mt-4 max-w-2xl text-muted">
                    A store earns more when the traffic, the follow-up and the
                    upkeep are handled alongside it.
                  </p>
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
                </Reveal>
              </div>
            </section>

            {/* ---- FAQ: native <details> keeps every answer in the DOM ---- */}
            <section className="section" id="faq" aria-labelledby="faq-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">Common questions</span>
                  <h2
                    id="faq-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Shopify store development{" "}
                    <span className="text-orange">questions, answered</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    Timelines, pricing, ownership, migrations and support. If
                    yours is not here, ask me on the call.
                  </p>
                </Reveal>
              </div>

              <div className="wrap mt-12 grid gap-4 md:grid-cols-2">
                {SHOPIFY_FAQS.map((f, i) => (
                  <Reveal key={f.q} delay={(i % 2) * 0.05}>
                    <details className="group overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">
                      <summary className="flex cursor-pointer items-center justify-between gap-4 px-6 py-5 font-[family-name:var(--font-display)] font-semibold text-ink marker:content-['']">
                        <h3 className="text-base font-semibold">{f.q}</h3>
                        <span className="grid h-5 w-5 shrink-0 place-items-center rounded-full bg-ink/5 text-ink transition-transform duration-300 group-open:rotate-45 group-open:bg-orange group-open:text-white">
                          <svg width="10" height="10" viewBox="0 0 14 14" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" aria-hidden="true">
                            <path d="M7 1v12M1 7h12" />
                          </svg>
                        </span>
                      </summary>
                      <p className="px-6 pb-6 text-sm text-body">{f.a}</p>
                    </details>
                  </Reveal>
                ))}
              </div>
            </section>

            <FinalCTA
              heading={
                <>
                  Ready to build <span className="text-orange-300">your Shopify store?</span>
                </>
              }
              sub="Tell me what you sell and where you want the business to be in a year. I will come back with a plan, a price and a launch date."
              cta={CTA_LABEL}
            />
          </div>
        </div>
      </main>
      <Footer />
      {/* This page's own popup, in place of the site-wide ConsultPopup: every
          CTA here opens the three-step store-build form from the hero. Only one
          popup may be mounted, or a single click would open both. */}
      <QuotePopup />
      <BackToTop />
      <MobileBookBar label={CTA_LABEL} />
    </>
  );
}
