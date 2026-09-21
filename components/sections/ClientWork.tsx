import Link from "next/link";
import Reveal from "../Reveal";
import ImgOrPlaceholder from "../ImgOrPlaceholder";
import { CLIENTS } from "@/lib/clients";

/**
 * Client work grid on /about.
 *
 * Every fact a search engine or an LLM needs — client name, industry, location,
 * services delivered, outcome — is plain text in the markup. Nothing is behind a
 * tab, hover or accordion, so the page reads the same to a crawler as it does to
 * a visitor.
 *
 * Each card is one link target (the case study) using the stretched-link
 * pattern: the case-study link paints an ::after over the whole card, and the
 * client's own website link sits above it on z-10. That keeps the "click the
 * card" behaviour without nesting one anchor inside another.
 */
export default function ClientWork() {
  return (
    <section id="clients" className="section" aria-labelledby="clients-heading">
      <div className="wrap-wide text-center">
        <Reveal>
          <span className="script-label">Client work</span>
          <h2
            id="clients-heading"
            className="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
          >
            Brands I have <span className="text-orange">worked with</span>
          </h2>
          <p className="mx-auto mt-5 max-w-3xl text-lg text-muted">
            Nine businesses across renovation, overseas education, ecommerce,
            martial arts, legal services and fire safety engineering, in India,
            the UAE, Canada, Switzerland and the United States. Each one bought a
            different service, from a single ad account to a full website and
            revenue system.
          </p>
        </Reveal>
      </div>

      <ul className="wrap mt-14 grid list-none gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {CLIENTS.map((c, i) => (
          <li key={c.slug} className="flex">
            <Reveal delay={(i % 3) * 0.05} className="flex w-full">
              <article className="card group relative flex w-full flex-col p-6">
                <figure className="m-0">
                  <ImgOrPlaceholder
                    src={`/clients/${c.slug}-website.webp`}
                    alt={`Screenshot of the ${c.fullName ?? c.name} website`}
                    /* the screenshots are all 1400×765 — matching the box to
                       that ratio is what stops `cover` cropping their sides */
                    ratio="1400/765"
                    seed={i}
                    /* thin brand-orange frame around the screenshot; `!` because
                       ImgOrPlaceholder sets its own neutral border */
                    className="!border-2 !border-orange"
                    sizes="(min-width: 1024px) 360px, (min-width: 640px) 45vw, 88vw"
                  />
                  <figcaption className="sr-only">
                    {c.fullName ?? c.name} website. {c.industry}, {c.location}.
                  </figcaption>
                </figure>

                <h3 className="mt-5 flex flex-wrap items-baseline gap-x-3 gap-y-1 text-xl font-extrabold text-ink">
                  {c.name}
                  {c.url ? (
                    <a
                      href={c.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="relative z-10 font-[family-name:var(--font-display)] text-xs font-semibold text-muted underline underline-offset-4 hover:text-orange"
                    >
                      Visit website
                    </a>
                  ) : null}
                </h3>

                <p className="mt-1 font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">
                  {c.industry} · {c.location}
                </p>

                <p className="mt-3 text-sm text-body">{c.summary}</p>

                {c.result ? (
                  <p className="mt-3 text-sm text-ink">
                    <strong className="font-extrabold">Result:</strong> {c.result}
                  </p>
                ) : null}

                <h4 className="sr-only">Services delivered to {c.name}</h4>
                <ul className="mt-4 flex flex-wrap gap-2">
                  {c.services.map((s) => (
                    <li
                      key={s}
                      className="rounded-full border border-[var(--color-line)] bg-white px-3 py-1 font-[family-name:var(--font-display)] text-xs font-semibold text-ink"
                    >
                      {s}
                    </li>
                  ))}
                </ul>

                <div className="mt-6 pt-1">
                  {/* Stretched link: covers the card, so the whole card opens
                      the case study. The "Visit website" link next to the client
                      name sits above it on z-10. */}
                  <Link
                    href={`/case-studies/${c.slug}`}
                    className="font-[family-name:var(--font-display)] text-sm font-semibold text-orange after:absolute after:inset-0 after:content-['']"
                  >
                    Read the {c.fullName ?? c.name} case study →
                  </Link>
                </div>
              </article>
            </Reveal>
          </li>
        ))}
      </ul>
    </section>
  );
}
