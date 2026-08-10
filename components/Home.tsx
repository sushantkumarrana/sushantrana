"use client";

import Nav from "./Nav";
import Image from "next/image";
import Footer from "./Footer";
import Reveal from "./Reveal";
import RotatingHeadline from "./RotatingHeadline";
import DiagonalMarquee from "./DiagonalMarquee";
import AboutMe from "./AboutMe";
import FloatingLogos from "./FloatingLogos";
import HeroIcons from "./HeroIcons";
import ConsultPopup from "./ConsultPopup";
import StraightMarquee from "./StraightMarquee";
import BackToTop from "./BackToTop";
import MobileBookBar from "./MobileBookBar";
import WhoICanHelp from "./sections/WhoICanHelp";
import MyNumbers from "./sections/MyNumbers";
import RealityOfGrowth from "./sections/RealityOfGrowth";
import WhoIHelp from "./sections/WhoIHelp";
import WhatIDo from "./sections/WhatIDo";
import HowIWork from "./sections/HowIWork";
import PerformanceMarketing from "./sections/PerformanceMarketing";
import AIAutomation from "./sections/AIAutomation";
import SelectedResults from "./sections/SelectedResults";
import Testimonials from "./sections/Testimonials";
import TechStack from "./sections/TechStack";
import Blog from "./sections/Blog";
import FAQ from "./sections/FAQ";
import FinalCTA from "./sections/FinalCTA";

const Arrow = () => (
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
    <path d="M5 12h14M13 6l6 6-6 6" />
  </svg>
);

// tools that have a real logo in /public/logos
const tools = [
  { n: "Google Ads", f: "google-ads" }, { n: "Meta Ads", f: "meta" },
  { n: "TikTok Ads", f: "tiktok" }, { n: "Instagram", f: "instagram" },
  { n: "Zoho", f: "zoho" }, { n: "WordPress", f: "wordpress" },
  { n: "LinkedIn Ads", f: "linkedin" }, { n: "HubSpot", f: "hubspot" },
  { n: "Klaviyo", f: "klaviyo" }, { n: "Webflow", f: "webflow" },
  { n: "Wix Studio", f: "wix" }, { n: "GA4", f: "ga4" },
];

export default function Home() {
  return (
    <>
      <Nav />
      <main id="top">
        {/* ============ HERO (white) ============ */}
        <section className="relative overflow-hidden bg-white">
          <HeroIcons />
          <div className="wrap relative z-10 flex min-h-[82svh] flex-col items-center justify-center pt-28 pb-16 text-center sm:pt-24">
            <div className="w-full">
              <RotatingHeadline />
            </div>

            <Reveal delay={0.1}>
              <p className="mt-6 text-[clamp(1.25rem,2.4vw,1.9rem)] font-bold text-ink">
                Because you have marketing campaigns,{" "}
                <span className="text-orange">not a revenue system.</span>
              </p>
            </Reveal>

            <Reveal delay={0.18}>
              <p className="mx-auto mt-5 max-w-2xl text-lg text-muted">
                I build revenue systems, not just marketing campaigns: strategy,
                performance marketing, and AI automation working as one engine.
              </p>
            </Reveal>

            <Reveal delay={0.26}>
              <a href="#contact" className="btn btn-primary mt-9">
                Book an Appointment <Arrow />
              </a>
            </Reveal>
          </div>
        </section>

        {/* ============ HERO IMAGE (white, peeks above the fold) ============ */}
        <section className="bg-white pb-20">
          <Reveal>
            {/* minimal side margins — image reads big */}
            <div className="mx-auto w-[98%] overflow-hidden rounded-[28px]">
              {/* The LCP image — priority so it is preloaded rather than lazy. */}
              <Image src="/hero/hero.png" alt="Sushant Rana revenue systems" width={1700} height={925} priority sizes="98vw" className="h-auto w-full" />
            </div>
          </Reveal>
        </section>

        {/* ============ GREY REGION (blurred floating logos behind everything) ============ */}
        <div className="relative overflow-hidden bg-section">
          <FloatingLogos />

          <div className="relative z-10">
            {/* tools marquee (no title) */}
            <section className="py-12">
              <div className="marquee">
                <div className="marquee__track" style={{ ["--dur" as string]: "34s" }}>
                  {[...tools, ...tools].map((t, i) => (
                    <span
                      key={i}
                      className="mx-3 inline-flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-6 py-4 font-[family-name:var(--font-display)] text-base font-semibold text-ink"
                    >
                      <Image src={`/logos/${t.f}.png`} alt={t.n} width={28} height={28} className="h-7 w-7 object-contain" />
                      {t.n}
                    </span>
                  ))}
                </div>
              </div>
            </section>

            <section>
              <DiagonalMarquee />
            </section>

            <AboutMe />
            <WhoICanHelp />
            <RealityOfGrowth />
            <StraightMarquee variant="ink" dur={55} items={["Performance Marketing", "Web Development", "AI Automation", "SEO", "CRO"]} />
            <WhoIHelp />
            <WhatIDo />
            <MyNumbers />
            <StraightMarquee variant="orange" dur={50} reverse items={["Strategy", "Positioning", "Automation", "Reporting", "Growth"]} />
            <HowIWork />
            <PerformanceMarketing />
            <StraightMarquee variant="ink" dur={55} items={["CRM Automation", "Lead Scoring", "WhatsApp", "Reporting", "AI Assistants"]} />
            <AIAutomation />
            <SelectedResults />
            <StraightMarquee variant="orange" dur={55} reverse items={["4× ROAS", "₹50L+ Managed", "4 Markets", "Senior-Led", "100% Owned"]} />
            <Testimonials />
            <TechStack />
            <Blog />
            <StraightMarquee variant="orange" dur={50} reverse items={["Book a Free Call", "Revenue Systems", "Not Just Campaigns", "Let's Build"]} />
            <FAQ />
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
