import type { ReactNode } from "react";
import Reveal from "../Reveal";

/** Closing CTA band. Defaults to the homepage copy; service pages pass their
 *  own heading, sub-line and button label. */
export default function FinalCTA({
  heading = (
    <>
      Let&apos;s build a system that <span className="text-orange-300">keeps growing.</span>
    </>
  ),
  sub = "One call. One engine. Strategy, ads, automation, and site, aligned to your revenue goal.",
  cta = "Book Free Consultation",
}: {
  heading?: ReactNode;
  sub?: string;
  cta?: string;
}) {
  return (
    <section id="contact" className="section">
      <div className="wrap">
        <Reveal>
          <div className="relative overflow-hidden rounded-[36px] bg-[#050505] bg-cover bg-center p-10 text-center md:p-20" style={{ backgroundImage: "url(/footer/footer-bg.webp)" }}>
            {/* dark overlay so text stays readable (matches Talk-to-person card) */}
            <div className="pointer-events-none absolute inset-0 bg-black/35" />
            {/* soft orange glow */}
            <div className="pointer-events-none absolute left-1/2 top-0 h-72 w-72 -translate-x-1/2 rounded-full bg-orange/40 blur-[100px]" />
            <div className="relative">
              <h2 className="mx-auto max-w-3xl text-[clamp(2rem,5vw,3.6rem)] text-white">
                {heading}
              </h2>
              <p className="mx-auto mt-5 max-w-xl text-white/80">{sub}</p>
              <a href="#" data-consult className="btn btn-primary mt-9">{cta}</a>
              <p className="mt-5 font-[family-name:var(--font-display)] text-sm font-semibold text-white/70">
                No obligation · Senior-led · 4 markets
              </p>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
