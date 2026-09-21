import { CLIENTS } from "@/lib/clients";

/**
 * Two-row client wordmark strip, scrolling in opposite directions.
 *
 * Names come from the same CLIENTS list the /about page uses, so the strip can
 * never show a brand Sushant has not actually worked with. Drop a transparent
 * logo at /public/clients/<slug>-logo.png and set `logo: true` on that client
 * in lib/clients.ts; until then the name renders as text, which is a real
 * credit either way. (No speculative request + onError fallback: that 404'd
 * for every client and put nine errors in the console on every page view.)
 */
function Mark({ slug, name, logo }: { slug: string; name: string; logo?: boolean }) {
  return (
    <span className="mx-8 inline-flex shrink-0 items-center opacity-60 grayscale transition hover:opacity-100 hover:grayscale-0">
      {!logo ? (
        <span className="whitespace-nowrap font-[family-name:var(--font-display)] text-lg font-extrabold tracking-tight text-ink md:text-xl">
          {name}
        </span>
      ) : (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={`/clients/${slug}-logo.png`}
          alt={name}
          loading="lazy"
          decoding="async"
          className="h-8 w-auto object-contain md:h-10"
        />
      )}
    </span>
  );
}

function Row({ reverse = false, dur = 46 }: { reverse?: boolean; dur?: number }) {
  const base = [...CLIENTS, ...CLIENTS];
  return (
    <div className={`marquee-nofade overflow-hidden ${reverse ? "marquee--rev" : ""}`}>
      <div className="marquee__track py-3" style={{ ["--dur" as string]: `${dur}s` }}>
        {[...base, ...base].map((c, i) => (
          <Mark key={`${c.slug}-${i}`} slug={c.slug} name={c.fullName ?? c.name} logo={c.logo} />
        ))}
      </div>
    </div>
  );
}

export default function LogoStrip() {
  return (
    <section className="section" aria-label="Brands I have worked with">
      <p className="text-center text-xs font-bold uppercase tracking-[0.18em] text-muted">
        Trusted by brands across five countries
      </p>
      <div className="mt-8 grid gap-2">
        <Row />
        <Row reverse dur={52} />
      </div>
    </section>
  );
}
