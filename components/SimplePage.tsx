"use client";

import type { ReactNode } from "react";
import Nav from "./Nav";
import Footer from "./Footer";
import ConsultPopup from "./ConsultPopup";
import BackToTop from "./BackToTop";
import MobileBookBar from "./MobileBookBar";
import FloatingLogos from "./FloatingLogos";
import Reveal from "./Reveal";

/** Shared shell for the small utility pages (404, thank-you, coming-soon)
 *  so they carry the same nav, footer and theme as the homepage. */
export default function SimplePage({
  label,
  title,
  accent,
  children,
  actions,
}: {
  label: string;
  title: string;
  accent?: string;
  children?: ReactNode;
  actions?: ReactNode;
}) {
  return (
    <>
      <Nav />
      <main className="relative overflow-hidden bg-section">
        <FloatingLogos />
        <div className="wrap relative z-10 flex min-h-[78svh] flex-col items-center justify-center py-32 text-center">
          <Reveal>
            <span className="script-label">{label}</span>
            <h1 className="mt-4 text-[clamp(2rem,5vw,3.6rem)] font-extrabold text-ink">
              {title} {accent ? <span className="text-orange">{accent}</span> : null}
            </h1>
          </Reveal>

          {children ? (
            <Reveal delay={0.1}>
              <div className="mx-auto mt-5 max-w-xl text-lg text-muted">{children}</div>
            </Reveal>
          ) : null}

          {actions ? (
            <Reveal delay={0.18}>
              <div className="mt-9 flex flex-wrap items-center justify-center gap-4">{actions}</div>
            </Reveal>
          ) : null}
        </div>
      </main>
      <Footer />
      <ConsultPopup />
      <BackToTop />
      <MobileBookBar />
    </>
  );
}
