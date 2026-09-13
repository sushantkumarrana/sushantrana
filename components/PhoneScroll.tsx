"use client";

import { useState } from "react";
import { ChevronDown } from "lucide-react";

/**
 * A phone frame whose screen scrolls on its own.
 *
 * The screenshot is a tall image inside an `overflow-y-auto` screen, so the
 * whole store page can be explored inside the phone without any JavaScript —
 * native scrolling does the work, and touch scrolling still works on mobile.
 *
 * `src` points at a tall mobile screenshot in /public/services/shopify/. Until
 * that file exists the frame falls back to a built mock of a product page, so
 * the section never renders an empty or broken box.
 */
export default function PhoneScroll({
  src,
  alt,
  label,
  sub,
  dark = false,
}: {
  src: string;
  alt: string;
  label: string;
  sub?: string;
  /** Frame styling for the dark section band. */
  dark?: boolean;
}) {
  const [failed, setFailed] = useState(false);

  // Clamped width so two frames still fit side by side on a 360px phone, and
  // so the pair never crowds the copy column on desktop. `container-type` lets
  // every part of the handset be sized in cqw — one set of proportions that
  // holds at 124px and at 206px, instead of radii that look chunky small and
  // mean large.
  return (
    <div className="w-[clamp(124px,38vw,206px)] shrink-0 [container-type:inline-size]">
      <div className="relative">
        {/* side buttons, sitting just outside the titanium rail */}
        <span
          aria-hidden
          className="absolute -left-[1.2cqw] top-[17cqw] h-[7cqw] w-[1.4cqw] rounded-l-full bg-[#2b2b2e]"
        />
        <span
          aria-hidden
          className="absolute -left-[1.2cqw] top-[28cqw] h-[11cqw] w-[1.4cqw] rounded-l-full bg-[#2b2b2e]"
        />
        <span
          aria-hidden
          className="absolute -left-[1.2cqw] top-[42cqw] h-[11cqw] w-[1.4cqw] rounded-l-full bg-[#2b2b2e]"
        />
        <span
          aria-hidden
          className="absolute -right-[1.2cqw] top-[34cqw] h-[16cqw] w-[1.4cqw] rounded-r-full bg-[#2b2b2e]"
        />

        {/* titanium rail */}
        <div
          className={`relative rounded-[16cqw] p-[1.1cqw] shadow-[0_30px_60px_-25px_rgba(0,0,0,0.65)] ${
            dark
              ? "bg-[linear-gradient(150deg,#6f6f74_0%,#2f2f33_28%,#17171a_60%,#4a4a4f_100%)]"
              : "bg-[linear-gradient(150deg,#5a5a5f_0%,#232326_30%,#0e0e10_62%,#3d3d42_100%)]"
          }`}
        >
          {/* black bezel between rail and glass */}
          <div className="rounded-[15cqw] bg-black p-[1.4cqw]">
            <div className="relative aspect-[9/19.5] overflow-hidden rounded-[13.5cqw] bg-white">
              <div
                /* data-lenis-prevent: Lenis smooth-scrolls the whole document
                   and swallows wheel events, so without this the screen never
                   scrolls under the cursor — the page scrolls past instead.
                   touch-pan-y keeps the native drag on touch devices. */
                data-lenis-prevent
                className="h-full touch-pan-y overflow-y-auto overscroll-contain [-webkit-overflow-scrolling:touch] [scrollbar-width:none] [&::-webkit-scrollbar]:hidden"
              >
                {failed ? (
                  <MockProductPage />
                ) : (
                  // Plain <img>: the screen scrolls a full-length screenshot
                  // whose real height is unknown, which next/image cannot
                  // express.
                  // eslint-disable-next-line @next/next/no-img-element
                  <img
                    src={src}
                    alt={alt}
                    loading="lazy"
                    decoding="async"
                    onError={() => setFailed(true)}
                    className="block w-full"
                  />
                )}
              </div>

              {/* Dynamic Island and home indicator sit above the screenshot and
                  stay put while it scrolls underneath, the way the real
                  hardware behaves. */}
              <span
                aria-hidden
                className="pointer-events-none absolute left-1/2 top-[2.4cqw] h-[7.5cqw] w-[27cqw] -translate-x-1/2 rounded-full bg-black"
              >
                <span className="absolute right-[2cqw] top-1/2 h-[3cqw] w-[3cqw] -translate-y-1/2 rounded-full bg-[#101014]" />
              </span>
              <span
                aria-hidden
                className="pointer-events-none absolute bottom-[1.8cqw] left-1/2 h-[1.1cqw] w-[34cqw] -translate-x-1/2 rounded-full bg-black/45 mix-blend-luminosity"
              />
            </div>
          </div>
        </div>
      </div>

      <p
        className={`mt-3 flex items-center justify-center gap-1.5 text-[11px] font-semibold uppercase tracking-widest ${
          dark ? "text-white/50" : "text-muted"
        }`}
      >
        <ChevronDown aria-hidden className="h-3.5 w-3.5 animate-bounce" />
        Scroll inside
      </p>
      <p
        className={`mt-2 text-center text-sm font-extrabold ${dark ? "text-white" : "text-ink"}`}
      >
        {label}
      </p>
      {sub && (
        <p className={`text-center text-xs ${dark ? "text-white/60" : "text-muted"}`}>{sub}</p>
      )}
    </div>
  );
}

/** Wireframe of a mobile product page, shown until a real screenshot is added.
 *  Long on purpose — the point of the frame is that it scrolls. */
function MockProductPage() {
  const bar = (w: string, dark = false) => (
    <div className={`h-2.5 rounded-full ${dark ? "bg-ink/70" : "bg-ink/15"}`} style={{ width: w }} />
  );
  return (
    <div className="bg-white pb-6" aria-hidden>
      <div className="flex items-center justify-between border-b border-[var(--color-line)] px-3 py-2.5">
        {bar("34%", true)}
        {bar("18%")}
      </div>
      <div className="relative aspect-square w-full overflow-hidden bg-[linear-gradient(135deg,#ffece3_0%,#ffd6c4_100%)]">
        <div className="absolute left-1/2 top-1/2 h-1/2 w-1/2 -translate-x-1/2 -translate-y-1/2 rounded-2xl bg-orange/25" />
        <span className="absolute left-2 top-2 rounded bg-orange px-2 py-0.5 text-[8px] font-bold uppercase tracking-wide text-white">
          Bestseller
        </span>
      </div>
      <div className="flex gap-1.5 px-3 py-2">
        {[0, 1, 2, 3].map((i) => (
          <div key={i} className="h-9 flex-1 rounded-md bg-ink/10" />
        ))}
      </div>
      <div className="space-y-2 px-3">
        {bar("80%", true)}
        {bar("55%")}
        <div className="flex items-center gap-2 pt-1">
          <span className="text-orange text-xs">★★★★★</span>
          {bar("30%")}
        </div>
        <p className="pt-1 text-lg font-extrabold text-ink">
          ₹1,499 <span className="text-xs font-medium text-muted line-through">₹2,199</span>
        </p>
        <div className="flex gap-1.5 pt-1">
          {["S", "M", "L"].map((s) => (
            <span
              key={s}
              className="grid h-7 w-7 place-items-center rounded-lg border border-[var(--color-line)] text-[10px] font-bold text-ink"
            >
              {s}
            </span>
          ))}
        </div>
        <div className="mt-2 grid h-9 place-items-center rounded-full bg-orange text-[11px] font-bold text-white">
          Add to cart
        </div>
        <div className="grid h-9 place-items-center rounded-full border border-ink/20 text-[11px] font-bold text-ink">
          Buy it now
        </div>
      </div>
      <div className="mt-4 grid grid-cols-3 gap-2 bg-section px-3 py-3 text-center">
        {["Free ship", "Easy return", "Secure pay"].map((t) => (
          <span key={t} className="text-[8px] font-bold uppercase tracking-wide text-muted">
            {t}
          </span>
        ))}
      </div>
      <div className="space-y-2 px-3 py-4">
        {bar("45%", true)}
        {bar("100%")}
        {bar("92%")}
        {bar("70%")}
      </div>
      <div className="grad-orange-ink mx-3 h-24 rounded-xl" />
      <div className="space-y-2 px-3 py-4">
        {bar("38%", true)}
        {[0, 1, 2].map((i) => (
          <div key={i} className="rounded-lg border border-[var(--color-line)] p-2">
            <span className="text-orange text-[9px]">★★★★★</span>
            <div className="mt-1.5 space-y-1.5">
              {bar("100%")}
              {bar("62%")}
            </div>
          </div>
        ))}
      </div>
      <div className="space-y-2 px-3">
        {bar("52%", true)}
        <div className="flex gap-2">
          {[0, 1].map((i) => (
            <div key={i} className="flex-1">
              <div className="aspect-square rounded-lg bg-ink/10" />
              <div className="mt-1.5 space-y-1">
                {bar("80%")}
                {bar("40%")}
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
