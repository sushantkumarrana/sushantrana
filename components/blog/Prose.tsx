import { Fragment, type ReactNode } from "react";
import { headingId, type Block } from "@/lib/prose";

/**
 * Renders a post body. Server component — no interactivity, so the article
 * ships as static HTML and the text is in the document for crawlers.
 */

/** Minimal inline markup: **bold**, *italic*, and {{fill me in}}.
 *
 *  Deliberately not a markdown parser — the content is ours, so anything
 *  richer belongs in a new block type where it can be styled properly rather
 *  than smuggled into a string.
 *
 *  {{...}} marks a detail the author still has to supply (a jurisdiction, an
 *  address). It renders loud on purpose: a legal page that quietly ships with
 *  "[city]" in it is worse than one that shouts about it. */
function inline(text: string): ReactNode {
  const parts = text.split(/(\*\*[^*]+\*\*|\*[^*]+\*|\{\{[^}]+\}\})/g);
  return parts.map((p, i) => {
    if (p.startsWith("{{") && p.endsWith("}}") && p.length > 4) {
      return (
        <mark
          key={i}
          title="Placeholder — replace before relying on this document"
          className="rounded bg-yellow-200 px-1.5 py-0.5 text-[0.9em] font-semibold text-yellow-900"
        >
          {p.slice(2, -2)}
        </mark>
      );
    }
    if (p.startsWith("**") && p.endsWith("**") && p.length > 4) {
      return (
        <strong key={i} className="font-semibold text-ink">
          {p.slice(2, -2)}
        </strong>
      );
    }
    if (p.startsWith("*") && p.endsWith("*") && p.length > 2) {
      return <em key={i}>{p.slice(1, -1)}</em>;
    }
    return <Fragment key={i}>{p}</Fragment>;
  });
}

export default function Prose({ blocks }: { blocks: Block[] }) {
  return (
    <div className="text-[1.06rem] leading-[1.8] text-body">
      {blocks.map((b, i) => {
        switch (b.t) {
          case "h2":
            return (
              <h2
                key={i}
                /* id matches tableOfContents() so the sidebar links land here.
                   scroll-mt clears the fixed nav, which would otherwise cover
                   the heading you just jumped to. */
                id={headingId(b.text)}
                className="mt-12 scroll-mt-28 text-[clamp(1.4rem,2.6vw,1.9rem)] font-extrabold text-ink first:mt-0"
              >
                {b.text}
              </h2>
            );

          case "h3":
            return (
              <h3 key={i} className="mt-8 text-xl font-bold text-ink">
                {b.text}
              </h3>
            );

          case "p":
            return (
              <p key={i} className="mt-5">
                {inline(b.text)}
              </p>
            );

          case "ul":
            return (
              <ul key={i} className="mt-5 grid gap-3">
                {b.items.map((it, j) => (
                  <li key={j} className="relative pl-6">
                    <span className="absolute left-0 top-[0.7em] h-1.5 w-1.5 rounded-full bg-orange" />
                    {inline(it)}
                  </li>
                ))}
              </ul>
            );

          case "ol":
            return (
              <ol key={i} className="mt-5 grid gap-3">
                {b.items.map((it, j) => (
                  <li key={j} className="relative pl-9">
                    <span className="absolute left-0 top-[0.15em] grid h-6 w-6 place-items-center rounded-full bg-orange/12 text-xs font-bold text-orange">
                      {j + 1}
                    </span>
                    {inline(it)}
                  </li>
                ))}
              </ol>
            );

          case "quote":
            return (
              <blockquote
                key={i}
                className="my-10 border-l-[3px] border-orange pl-6 font-[family-name:var(--font-display)] text-[clamp(1.1rem,2vw,1.35rem)] font-semibold leading-snug text-ink"
              >
                {inline(b.text)}
              </blockquote>
            );

          case "callout":
            return (
              <aside
                key={i}
                className="my-10 rounded-2xl border border-orange/25 bg-orange/[0.06] p-6"
              >
                <p className="font-[family-name:var(--font-display)] text-sm font-bold uppercase tracking-wide text-orange">
                  {b.title}
                </p>
                <p className="mt-2 text-body">{inline(b.text)}</p>
              </aside>
            );
        }
      })}
    </div>
  );
}
