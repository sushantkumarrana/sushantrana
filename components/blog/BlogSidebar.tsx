import LeadForm from "../LeadForm";

/**
 * Sticky blog sidebar: the booking form, and nothing else.
 *
 * Sticks below the fixed nav and scrolls internally if the panel is ever taller
 * than the viewport — plain `position: sticky` would clip the bottom of a tall
 * panel on a short laptop screen with no way to reach it.
 *
 * Hidden below `lg`; the mobile layout renders BookPanel inline instead,
 * because a sticky column on a phone just eats the screen.
 */
export default function BlogSidebar() {
  return (
    /* The column must stretch to the full grid-row height or the sticky child
       has no distance to travel and scrolls away with the article. That means
       the parent grid must NOT use items-start on this column. */
    <aside className="hidden self-stretch lg:block">
      <div
        data-lenis-prevent
        className="sticky top-24 max-h-[calc(100dvh-7rem)] touch-pan-y overflow-y-auto overscroll-contain pb-2"
      >
        <BookPanel />
      </div>
    </aside>
  );
}

/** The booking panel. Exported so the mobile layout can render it inline. */
export function BookPanel() {
  return (
    <div className="glass rounded-3xl p-6">
      <span className="script-label">Book an appointment</span>
      <h3 className="mt-1 text-xl font-extrabold leading-tight text-ink">
        Free 30-minute consultation
      </h3>
      <p className="mt-2 text-sm text-muted">
        Pick the service you need. I&apos;ll reply within one business day.
      </p>
      <div className="mt-5">
        {/* "short" variant: name/email/phone + the two dropdowns. Keeps the
            sticky panel inside a laptop viewport. */}
        <LeadForm compact fields="short" submitLabel="Request my slot" />
      </div>
    </div>
  );
}
