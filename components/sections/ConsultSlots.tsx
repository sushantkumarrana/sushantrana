"use client";

import Reveal from "../Reveal";

export default function ConsultSlots() {
  return (
    <section className="section">
      <div className="wrap">
        <Reveal>
          {/* grey section; card uses the footer image as its background */}
          <div
            className="relative overflow-hidden rounded-[32px] bg-[#050505] bg-cover bg-center p-10 text-center md:p-16"
            style={{ backgroundImage: "url(/footer/footer-bg.png)" }}
          >
            <div className="pointer-events-none absolute inset-0 bg-black/35" />
            <div className="relative">
              <span className="eyebrow !border-white/15 !bg-white/10 !text-orange-300">
                <span className="dot-live" /> 4 consult slots open this week
              </span>
              <h2 className="mx-auto mt-6 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] text-white">
                Talk to the person who&apos;ll <span className="text-orange-300">do the work</span>
              </h2>
              <p className="mx-auto mt-4 max-w-md text-white/75">
                A 30-minute call to pressure-test your growth — no junior handoff, no pitch deck.
              </p>
              <a href="#contact" className="btn btn-primary mt-8">Book Free Consultation</a>
            </div>
          </div>
        </Reveal>
      </div>
    </section>
  );
}
