import { Check } from "lucide-react";

/* Shared building blocks for the service pages. */

/** Photographic band, reusing the same background image as the homepage
 *  closing CTA so the dark sections across the site read as one family. */
export function ImageBand({
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
      style={{ backgroundImage: "url(/footer/footer-bg.webp)" }}
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

export function Tick({ children, light = false }: { children: React.ReactNode; light?: boolean }) {
  return (
    <li className={`flex items-start gap-3 ${light ? "text-white" : "text-ink"}`}>
      <span className="mt-0.5 grid h-6 w-6 shrink-0 place-items-center rounded-full bg-orange text-white">
        <Check aria-hidden className="h-3.5 w-3.5" strokeWidth={3} />
      </span>
      <span className="font-medium">{children}</span>
    </li>
  );
}

export function Tag({ children, light = false }: { children: React.ReactNode; light?: boolean }) {
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
