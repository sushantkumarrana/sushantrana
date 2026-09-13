"use client";

import Image from "next/image";
import Link from "next/link";
import Nav from "./Nav";
import Footer from "./Footer";
import Reveal from "./Reveal";
import FloatingLogos from "./FloatingLogos";
import StraightMarquee from "./StraightMarquee";
import ConsultPopup from "./ConsultPopup";
import BackToTop from "./BackToTop";
import MobileBookBar from "./MobileBookBar";
import Breadcrumbs from "./Breadcrumbs";
import ImgOrPlaceholder from "./ImgOrPlaceholder";
import ClientWork from "./sections/ClientWork";
import FinalCTA from "./sections/FinalCTA";
import { ABOUT_FAQS } from "@/lib/about-faq";

const TIMELINE = [
  {
    n: "01",
    kicker: "2017",
    title: "Learning the craft",
    desc: "Started digital marketing under a mentor and took my first freelance projects on the side. Small budgets, real accountability, and the fastest way to learn what actually moves a number.",
  },
  {
    n: "02",
    kicker: "October 2018 – March 2025",
    title: "Digital Marketing Manager, House Of Web",
    desc: "Six and a half years running campaigns, websites and tracking for clients across four markets. Paid media, SEO, CRO, and the reporting that keeps all three honest.",
  },
  {
    n: "03",
    kicker: "March 2025 – present",
    title: "Project Manager, WebIncline",
    desc: "Leading cross-functional delivery across performance marketing, web development and CRM operations, turning business requirements into systems that ship on time.",
  },
  {
    n: "04",
    kicker: "Today",
    title: "Consulting as Sushant Rana",
    desc: "Alongside the job, I consult and deliver services independently under my own company, Sushant Rana. Senior-led engagements only, so the person you talk to is the person doing the work.",
  },
];

const EXPERTISE = [
  { t: "Performance marketing", d: "Google Ads and Meta Ads built around pipeline, not impressions." },
  { t: "CRM and marketing automation", d: "Zoho CRM, GoHighLevel and HubSpot: pipelines, workflows, and email, SMS and WhatsApp nurture." },
  { t: "Sales funnel strategy", d: "Landing pages, offers and follow-up sequences that turn traffic into booked calls." },
  { t: "Website development", d: "WordPress, Elementor and Shopify builds tuned for speed and conversion." },
  { t: "Tracking and reporting", d: "Google Tag Manager and GA4 set up so every rupee is traceable to a result." },
  { t: "SEO and conversion rate optimisation", d: "Organic visibility and page-level testing compounding on top of paid." },
];

/**
 * Photo grid for /public/about/behind-the-work/.
 *
 * Filenames are descriptive on purpose — image search reads them — and the alt
 * text describes what is actually in each frame. If a photo is swapped, update
 * its alt and caption with it.
 *
 * `position` anchors the 4:3 crop. The two portrait shots would otherwise be
 * cut through the middle, losing the face.
 */
const GALLERY = [
  {
    file: "sushant-rana-client-strategy-call.webp",
    alt: "Sushant Rana on a video call with a client at his desk, talking through strategy",
    caption: "Client strategy call",
    position: "50% 22%",
  },
  {
    file: "sushant-rana-google-ads-campaign-review.webp",
    alt: "Sushant Rana presenting a Google Ads campaign dashboard to his team in a meeting room",
    caption: "Google Ads campaign review",
  },
  {
    file: "sushant-rana-gohighlevel-crm-automation-planning.webp",
    alt: "Sushant Rana mapping a GoHighLevel CRM automation workflow on a whiteboard, from lead capture to follow-up",
    caption: "CRM automation planning",
    position: "50% 18%",
  },
  {
    file: "sushant-rana-shopify-store-design-review.webp",
    alt: "Sushant Rana reviewing an ecommerce store design in Figma with his development team",
    caption: "Store design review",
  },
  {
    file: "sushant-rana-ecommerce-design-development-sprint.webp",
    alt: "Sushant Rana walking developers through a mobile and desktop store design during a build sprint",
    caption: "Design and development sprint",
  },
  {
    file: "sushant-rana-monthly-google-ads-performance-report.webp",
    alt: "Sushant Rana presenting a monthly Google Ads performance report to clients on a video call",
    caption: "Monthly performance reporting",
  },
];

const EDUCATION = [
  { t: "ITFT College, Chandigarh", d: "Bachelor of Business Administration (BBA), Marketing Management." },
  { t: "Army Public School, Chandimandir", d: "Schooling before the BBA, where the discipline came from." },
  { t: "Based in Chandigarh, India", d: "Working remotely with clients in India, the UAE, Canada, Switzerland and the United States." },
];

export default function About() {
  return (
    <>
      <Nav />
      <main>
        {/* ============ INTRO (white): portrait first, copy centred under it ============ */}
        <section className="relative overflow-hidden bg-white" aria-labelledby="about-heading">
          <div className="wrap relative z-10 pt-28">
            <Breadcrumbs trail={[{ label: "About" }]} />
          </div>

          <div className="wrap relative z-10 py-10 md:py-14">
            <Reveal>
              <div className="overflow-hidden rounded-3xl border border-[var(--color-line)] shadow-xl">
                {/* First thing on the page, so this is the LCP image: priority,
                    never lazy. */}
                <Image
                  src="/about/sushant-rana-speaking-ai-advertising-panel.webp"
                  alt="Sushant Rana speaking on a panel discussion about AI in advertising, covering AI-powered Google Ads and Meta Ads"
                  width={1600}
                  height={900}
                  priority
                  sizes="(max-width: 768px) 92vw, 1160px"
                  className="h-auto w-full"
                />
              </div>
            </Reveal>

            {/* copy runs the full width of the image above it, not a narrower column */}
            <div className="mt-12 text-center">
              <Reveal delay={0.1}>
                <span className="script-label">About us</span>
                <h1
                  id="about-heading"
                  className="mt-4 text-[clamp(2rem,5vw,3.6rem)] font-extrabold text-ink"
                >
                  Sushant Rana, building{" "}
                  <span className="text-orange">revenue systems</span> since 2017
                </h1>
                <p className="mt-6 text-lg text-body">
                  I&apos;m Sushant Rana, a project manager and business growth
                  consultant based in Chandigarh, India. I started doing digital
                  marketing in 2017, first learning under someone else while
                  freelancing, then through full-time roles. I still hold a
                  full-time job today, and alongside it I consult and deliver
                  services independently under my own company, Sushant Rana.
                </p>
                <p className="mt-4 text-lg text-body">
                  That mix is deliberate. The job keeps me shipping large
                  projects with real teams and real budgets every week. The
                  consulting keeps me close to owners who need a revenue system,
                  not a vendor. In between, I have delivered{" "}
                  <Link href="#clients" className="font-semibold text-orange underline underline-offset-4">
                    work for nine client brands
                  </Link>{" "}
                  across five countries, and I write about how those systems are
                  built in{" "}
                  <Link href="/blog" className="font-semibold text-orange underline underline-offset-4">
                    my articles on revenue systems and lead quality
                  </Link>
                  .
                </p>
                <a href="#contact" className="btn btn-primary mt-9">
                  Book a free consultation
                </a>
              </Reveal>
            </div>
          </div>
        </section>

        {/* ============ GREY REGION ============ */}
        <div className="relative overflow-hidden bg-section">
          <FloatingLogos />

          <div className="relative z-10">
            <StraightMarquee
              variant="ink"
              dur={55}
              items={["Since 2017", "Freelance", "In-house", "Consulting", "Senior-led"]}
            />

            {/* ---- journey ---- */}
            <section className="section" aria-labelledby="journey-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">The journey</span>
                  <h2
                    id="journey-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    From freelancer to <span className="text-orange">project manager</span>
                  </h2>
                </Reveal>
              </div>

              <ol className="wrap mt-14 grid list-none gap-6 md:grid-cols-2">
                {TIMELINE.map((s, i) => (
                  <li key={s.n} className="flex">
                    <Reveal delay={(i % 2) * 0.06} className="flex w-full">
                      <article className="card w-full p-8">
                        <p className="mb-4 flex items-center gap-4">
                          <span className="grid h-12 w-12 place-items-center rounded-2xl bg-orange font-[family-name:var(--font-display)] font-extrabold text-white">
                            {s.n}
                          </span>
                          <time className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                            {s.kicker}
                          </time>
                        </p>
                        <h3 className="text-2xl font-extrabold text-ink">{s.title}</h3>
                        <p className="mt-3 text-body">{s.desc}</p>
                      </article>
                    </Reveal>
                  </li>
                ))}
              </ol>
            </section>

            {/* ---- clients ---- */}
            <ClientWork />

            <StraightMarquee
              variant="orange"
              dur={50}
              reverse
              items={["Google Ads", "Meta Ads", "Zoho CRM", "HubSpot", "GoHighLevel", "GA4"]}
            />

            {/* ---- expertise ---- */}
            <section className="section" aria-labelledby="expertise-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">What we do</span>
                  <h2
                    id="expertise-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Six disciplines, <span className="text-orange">one engine</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    Most businesses buy these separately and wonder why nothing
                    compounds. Performance marketing, CRM automation and the
                    website only work together when one person owns the whole
                    chain from click to closed deal. These are the same six
                    disciplines behind{" "}
                    <Link href="/" className="font-semibold text-orange underline underline-offset-4">
                      the revenue systems I build for clients
                    </Link>
                    .
                  </p>
                </Reveal>
              </div>

              {/* two-up from the smallest screen: these cards are short enough
                  that one per row wasted most of a phone viewport */}
              <ul className="wrap mt-14 grid list-none grid-cols-2 gap-3 sm:gap-6 lg:grid-cols-3">
                {EXPERTISE.map((e, i) => (
                  <li key={e.t} className="flex">
                    <Reveal delay={(i % 3) * 0.05} className="flex w-full">
                      <article className="card w-full p-4 sm:p-7">
                        <h3 className="text-base font-extrabold text-ink sm:text-xl">{e.t}</h3>
                        <p className="mt-2 text-sm text-body sm:mt-3 sm:text-base">{e.d}</p>
                      </article>
                    </Reveal>
                  </li>
                ))}
              </ul>
            </section>

            {/* ---- education ---- */}
            <section className="section" aria-labelledby="background-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">Background</span>
                  <h2
                    id="background-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Education and <span className="text-orange">base</span>
                  </h2>
                </Reveal>
              </div>

              <ul className="wrap mt-12 grid list-none gap-6 md:grid-cols-3">
                {EDUCATION.map((e, i) => (
                  <li key={e.t} className="flex">
                    <Reveal delay={(i % 3) * 0.06} className="flex w-full">
                      <article className="card w-full p-7">
                        <h3 className="text-xl font-extrabold text-ink">{e.t}</h3>
                        <p className="mt-3 text-body">{e.d}</p>
                      </article>
                    </Reveal>
                  </li>
                ))}
              </ul>
            </section>


            {/* ---- photo grid: /public/about/behind-the-work/ (see GALLERY) ---- */}
            <section className="section" aria-labelledby="gallery-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">In practice</span>
                  <h2
                    id="gallery-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Behind the <span className="text-orange">work</span>
                  </h2>
                  <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                    Client sessions, campaign reviews, build sprints and the
                    occasional stage. The day-to-day behind the results above.
                  </p>
                </Reveal>
              </div>

              <ul className="wrap mt-12 grid list-none gap-5 sm:grid-cols-2 lg:grid-cols-3">
                {GALLERY.map((g, i) => (
                  <li key={g.file}>
                    <Reveal delay={(i % 3) * 0.05}>
                      <figure className="m-0">
                        <ImgOrPlaceholder
                          src={`/about/behind-the-work/${g.file}`}
                          alt={g.alt}
                          ratio="4/3"
                          position={g.position}
                          seed={i + 3}
                          sizes="(min-width: 1024px) 380px, (min-width: 640px) 45vw, 88vw"
                        />
                        <figcaption className="mt-3 text-sm text-muted">{g.caption}</figcaption>
                      </figure>
                    </Reveal>
                  </li>
                ))}
              </ul>
            </section>
            {/* ---- FAQ: native <details> so every answer stays in the DOM,
                    readable by crawlers and AI assistants without JavaScript ---- */}
            <section className="section" aria-labelledby="faq-heading">
              <div className="wrap-wide text-center">
                <Reveal>
                  <span className="script-label">FAQ</span>
                  <h2
                    id="faq-heading"
                    className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
                  >
                    Questions about <span className="text-orange">working with me</span>
                  </h2>
                </Reveal>
              </div>

              <div className="wrap mt-12 grid gap-4 md:grid-cols-2">
                {ABOUT_FAQS.map((f, i) => (
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

            <FinalCTA />
          </div>
        </div>
      </main>
      <Footer />
      <ConsultPopup />
      <BackToTop />
      <MobileBookBar />
    </>
  );
}
