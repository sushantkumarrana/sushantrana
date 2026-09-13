"use client";

import { AnimatedNumber, GrowBar, GrowBars } from "./animate";

/**
 * The illustrated panels that sit beside the copy columns: a store overview, a
 * project tracker, a post-launch metrics card and an analytics summary.
 *
 * All four render on a white surface so they stay legible on the grey sections
 * and on the photographic bands alike.
 *
 * Every number counts up and every bar grows from zero as its panel scrolls
 * into view, so a reader sees the figure arrive rather than find it already
 * sitting there.
 *
 * They are interface illustrations rather than screenshots of a live client
 * account, so each carries a visible "Example" chip. Numbers a reader could
 * mistake for a specific client's results are deliberately absent.
 */

function Chip({ children }: { children: React.ReactNode }) {
  return (
    <span className="rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider text-muted">
      {children}
    </span>
  );
}

function Panel({
  title,
  right,
  children,
}: {
  title: string;
  right?: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <figure className="m-0 overflow-hidden rounded-3xl border border-[var(--color-line)] bg-white shadow-[0_30px_70px_-40px_rgba(10,10,10,0.45)]">
      <figcaption className="flex items-center justify-between border-b border-[var(--color-line)] px-5 py-4">
        <span className="font-[family-name:var(--font-display)] text-sm font-bold text-ink">
          {title}
        </span>
        <span className="flex items-center gap-2">
          {right}
          <Chip>Example</Chip>
        </span>
      </figcaption>
      <div className="p-5">{children}</div>
    </figure>
  );
}

function Stat({ n, l }: { n: string; l: string }) {
  return (
    <div className="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5">
      <p className="font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">
        <AnimatedNumber value={n} />
      </p>
      <p className="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{l}</p>
    </div>
  );
}

/** Fixed heights — no randomness, so server and client render identically. */
const BARS = [34, 42, 38, 55, 48, 62, 58, 71, 66, 80, 74, 92];

function BarChart({ label }: { label: string }) {
  return (
    <div className="mt-4">
      <p className="text-[10px] font-bold uppercase tracking-wider text-muted">{label}</p>
      <GrowBars values={BARS} className="mt-3 h-24" />
      <div className="mt-2 flex justify-between text-[10px] font-medium text-muted">
        <span>Jan</span>
        <span>Jun</span>
        <span>Dec</span>
      </div>
    </div>
  );
}

export function StoreOverview({ pages, stack }: { pages: string[]; stack: string[] }) {
  return (
    <Panel title="Shopify store overview" right={<Chip>Custom build</Chip>}>
      <div className="grid grid-cols-2 gap-3">
        <Stat n="Fast" l="Load time" />
        <Stat n="Mobile" l="Designed first" />
        <Stat n="2.0" l="Editable sections" />
        <Stat n="100%" l="Yours to keep" />
      </div>

      <p className="mt-5 text-[10px] font-bold uppercase tracking-wider text-muted">Store pages</p>
      <ul className="mt-2.5 grid list-none grid-cols-2 gap-2">
        {pages.map((p) => (
          <li
            key={p}
            className="rounded-lg border border-[var(--color-line)] bg-white px-3 py-2 text-xs font-medium text-body"
          >
            {p}
          </li>
        ))}
      </ul>

      <p className="mt-5 text-[10px] font-bold uppercase tracking-wider text-muted">Tech stack</p>
      <ul className="mt-2.5 flex list-none flex-wrap gap-2">
        {stack.map((s) => (
          <li
            key={s}
            className="rounded-full border border-orange/30 bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange"
          >
            {s}
          </li>
        ))}
      </ul>
    </Panel>
  );
}

export function ProjectDashboard({ timeline }: { timeline: { t: string; w: string }[] }) {
  return (
    <Panel title="Project tracker" right={<Chip>On track</Chip>}>
      <div className="flex items-end justify-between">
        <div>
          <p className="font-[family-name:var(--font-display)] text-3xl font-extrabold text-ink">
            <AnimatedNumber value="72%" />
          </p>
          <p className="text-[11px] font-semibold text-muted">Week 4 of 6</p>
        </div>
        <div className="flex gap-2 text-center">
          {[
            { n: "38", l: "done" },
            { n: "5", l: "active" },
            { n: "9", l: "left" },
          ].map((x) => (
            <span
              key={x.l}
              className="rounded-xl border border-[var(--color-line)] bg-white px-3 py-2"
            >
              <span className="block font-[family-name:var(--font-display)] text-sm font-bold text-ink">
                <AnimatedNumber value={x.n} duration={900} />
              </span>
              <span className="text-[10px] uppercase tracking-wide text-muted">{x.l}</span>
            </span>
          ))}
        </div>
      </div>

      <div className="mt-4 h-1.5 overflow-hidden rounded-full bg-ink/10" aria-hidden>
        <GrowBar width="72%" />
      </div>

      <p className="mt-5 text-[10px] font-bold uppercase tracking-wider text-muted">
        Sprint timeline
      </p>
      <ol className="mt-2.5 grid list-none grid-cols-5 gap-1.5">
        {timeline.map((s, i) => (
          <li
            key={s.t}
            className={`rounded-lg border px-2 py-2 text-center ${
              i < 3 ? "border-orange/30 bg-orange/10" : "border-[var(--color-line)] bg-white"
            }`}
          >
            <span className="block text-[10px] font-bold text-ink">{s.t}</span>
            <span className="text-[9px] text-muted">{s.w}</span>
          </li>
        ))}
      </ol>

      <div className="mt-5 flex items-center justify-between rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3">
        <span className="text-[11px] font-semibold uppercase tracking-wide text-muted">
          Launch window
        </span>
        <span className="font-[family-name:var(--font-display)] text-sm font-bold text-orange">
          4-6 weeks
        </span>
      </div>
    </Panel>
  );
}

export function GrowthPanel() {
  return (
    <Panel title="What I watch after launch">
      <div className="grid grid-cols-2 gap-3">
        <Stat n="Conv. rate" l="Sessions to orders" />
        <Stat n="AOV" l="Average order value" />
        <Stat n="Load time" l="Real handsets" />
        <Stat n="Bounce" l="Landing page exits" />
      </div>
      <BarChart label="The shape of a healthy trading year" />
      <p className="mt-4 text-xs leading-relaxed text-muted">
        Every store I hand over ships with GA4 and ecommerce tracking already
        connected, so these four numbers are visible from the first week instead
        of being pieced together six months later.
      </p>
    </Panel>
  );
}

export function AnalyticsPanel() {
  const rows = [
    { l: "Direct", v: "42%" },
    { l: "Organic", v: "31%" },
    { l: "Paid", v: "18%" },
    { l: "Social", v: "9%" },
  ];
  return (
    <Panel title="Analytics overview" right={<Chip>Last 30 days</Chip>}>
      <div className="grid grid-cols-2 gap-3">
        <Stat n="Revenue" l="Split by channel" />
        <Stat n="Orders" l="Daily trend" />
        <Stat n="Funnel" l="Where buyers drop" />
        <Stat n="AOV" l="Effect of bundles" />
      </div>
      <BarChart label="Revenue by month" />

      <p className="mt-5 text-[10px] font-bold uppercase tracking-wider text-muted">
        Traffic sources
      </p>
      <ul className="mt-2.5 grid list-none gap-2">
        {rows.map((r, i) => (
          <li key={r.l} className="flex items-center gap-3">
            <span className="w-16 shrink-0 text-xs font-medium text-body">{r.l}</span>
            <span className="h-1.5 flex-1 overflow-hidden rounded-full bg-ink/10" aria-hidden>
              <GrowBar width={r.v} delay={i * 90} />
            </span>
            <span className="w-9 shrink-0 text-right text-xs font-bold text-ink">
              <AnimatedNumber value={r.v} />
            </span>
          </li>
        ))}
      </ul>
    </Panel>
  );
}
