"use client";

import { TESTIMONIALS } from "@/lib/testimonials";

/**
 * Two-row review wall that drifts in opposite directions, in the style of a
 * review-platform feed.
 *
 * The quotes are the site's own illustrative testimonials, so the card
 * deliberately omits review-platform chrome — no provider logo, no review
 * counts, no dates. Those signal a verified third-party review, and inventing
 * them would misrepresent feedback that has not been published anywhere.
 * The note under the heading says as much in plain text.
 */

const AVATAR_TINTS = [
  "bg-orange text-white",
  "bg-ink text-white",
  "bg-[#c2410c] text-white",
  "bg-[#7c2d12] text-white",
  "bg-[#ea580c] text-white",
];

const initials = (name: string) =>
  name
    .replace(/[^A-Za-z. ]/g, "")
    .split(/[. ]+/)
    .filter(Boolean)
    .slice(0, 2)
    .map((p) => p[0]?.toUpperCase())
    .join("");

function ReviewCard({ q, i }: { q: (typeof TESTIMONIALS)[number]; i: number }) {
  return (
    <figure className="mx-2.5 flex w-[80vw] max-w-[380px] shrink-0 flex-col self-stretch rounded-2xl border border-[var(--color-line)] bg-white p-5">
      <div className="flex items-center gap-3">
        <span
          aria-hidden
          className={`grid h-10 w-10 shrink-0 place-items-center rounded-full font-[family-name:var(--font-display)] text-sm font-extrabold ${
            AVATAR_TINTS[i % AVATAR_TINTS.length]
          }`}
        >
          {initials(q.name)}
        </span>
        <span className="min-w-0">
          <span className="block truncate font-[family-name:var(--font-display)] text-sm font-bold text-ink">
            {q.name}
          </span>
          <span className="block truncate text-xs text-muted">
            {q.company} · {q.industry}
          </span>
        </span>
      </div>

      <p className="mt-3 text-sm text-orange" aria-label="Five out of five">
        <span aria-hidden>★★★★★</span>
      </p>

      <blockquote className="mt-2 flex-1 text-sm leading-relaxed text-body">{q.quote}</blockquote>
    </figure>
  );
}

function Row({ reverse = false, dur = 64 }: { reverse?: boolean; dur?: number }) {
  const base = reverse ? [...TESTIMONIALS].reverse() : TESTIMONIALS;
  const doubled = [...base, ...base, ...base, ...base];
  return (
    <div className={`marquee-nofade overflow-hidden ${reverse ? "marquee--rev" : ""}`}>
      <div className="marquee__track items-stretch py-2.5" style={{ ["--dur" as string]: `${dur}s` }}>
        {[...doubled, ...doubled].map((q, i) => (
          <ReviewCard key={`${q.name}-${i}`} q={q} i={i} />
        ))}
      </div>
    </div>
  );
}

export default function ReviewSlider() {
  return (
    <section className="section" aria-labelledby="reviews-heading">
      <div className="wrap-wide text-center">
        <span className="script-label">Client feedback</span>
        <h2
          id="reviews-heading"
          className="mx-auto mt-5 max-w-4xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink"
        >
          What founders say after <span className="text-orange">working with me</span>
        </h2>
        <p className="mx-auto mt-4 max-w-2xl text-sm text-muted">
          Feedback written from the outcomes of each project listed on this
          site. Clients&apos; own words replace these as each one approves.
        </p>
      </div>

      <div className="mt-12 grid gap-3">
        <Row dur={140} />
        <Row reverse dur={160} />
      </div>
    </section>
  );
}
