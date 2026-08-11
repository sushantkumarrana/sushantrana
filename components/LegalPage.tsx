import Link from "next/link";
import Nav from "./Nav";
import Footer from "./Footer";
import ConsultPopup from "./ConsultPopup";
import BackToTop from "./BackToTop";
import MobileBookBar from "./MobileBookBar";
import Reveal from "./Reveal";
import Breadcrumbs from "./Breadcrumbs";
import Prose from "./blog/Prose";
import { LEGAL_LAST_UPDATED } from "@/lib/legal";
import { formatDate } from "@/lib/blog";
import { tocOf, type Block } from "@/lib/prose";

/** Shell for Privacy Policy and Terms & Conditions: same nav, footer and
 *  theme as the rest of the site, with a sticky contents list — these are long
 *  documents and people arrive looking for one specific clause. */
export default function LegalPage({
  label,
  title,
  accent,
  crumb,
  intro,
  blocks,
  otherHref,
  otherLabel,
}: {
  label: string;
  title: string;
  accent?: string;
  /** Breadcrumb text. Separate from title/accent, which are split for the
   *  two-colour headline and would read "Terms &" on their own. */
  crumb: string;
  intro: string;
  blocks: Block[];
  /** Cross-link to the sibling document — they reference each other. */
  otherHref: string;
  otherLabel: string;
}) {
  const toc = tocOf(blocks);

  return (
    <>
      <Nav />
      <main className="bg-section pb-20 pt-32 md:pt-36">
        <div className="wrap">
          <Breadcrumbs trail={[{ label: crumb }]} className="mb-6" />
          <Reveal>
            <span className="script-label">{label}</span>
            <h1 className="mt-4 text-[clamp(2rem,5vw,3.4rem)] font-extrabold text-ink">
              {title} {accent ? <span className="text-orange">{accent}</span> : null}
            </h1>
            <p className="mt-4 max-w-2xl text-lg text-muted">{intro}</p>
            <p className="mt-4 text-sm text-muted">
              Last updated{" "}
              <time dateTime={LEGAL_LAST_UPDATED}>{formatDate(LEGAL_LAST_UPDATED)}</time>
            </p>
          </Reveal>

          {/* The nav is the grid item itself, so `self-start` is what makes the
              sticky work: the item stays content-height while its containing
              block is the full-height grid area, giving it room to travel.
              (A sticky element nested *inside* a grid item needs the opposite —
              a stretched parent. See BlogSidebar.) */}
          <div className="mt-12 grid gap-10 lg:grid-cols-[260px_minmax(0,1fr)]">
            {/* contents */}
            <nav
              aria-label="On this page"
              data-lenis-prevent
              className="top-24 max-h-[calc(100dvh-7rem)] touch-pan-y self-start overflow-y-auto overscroll-contain rounded-2xl border border-[var(--color-line)] bg-white/70 p-5 lg:sticky"
            >
              <p className="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-[0.14em] text-muted">
                Contents
              </p>
              <ol className="mt-3 grid gap-1.5">
                {toc.map((h, i) => (
                  <li key={h.id} className="flex gap-2.5 text-sm">
                    <span className="font-semibold text-orange">
                      {String(i + 1).padStart(2, "0")}
                    </span>
                    <a href={`#${h.id}`} className="text-body transition hover:text-orange">
                      {h.text}
                    </a>
                  </li>
                ))}
              </ol>
              <Link
                href={otherHref}
                className="mt-5 inline-block border-t border-[var(--color-line)] pt-4 text-sm font-semibold text-orange transition hover:underline"
              >
                {otherLabel} →
              </Link>
            </nav>

            <div className="rounded-3xl border border-[var(--color-line)] bg-white/70 p-7 md:p-10">
              <Prose blocks={blocks} />
            </div>
          </div>
        </div>
      </main>
      <Footer />
      <ConsultPopup />
      <BackToTop />
      <MobileBookBar />
    </>
  );
}
