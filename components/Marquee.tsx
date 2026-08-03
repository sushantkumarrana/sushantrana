"use client";

import type { ReactNode } from "react";

/**
 * Pure-CSS infinite marquee. Renders the children twice so the -50%
 * translate loops seamlessly.
 */
export default function Marquee({
  items,
  duration = 32,
  reverse = false,
  className = "",
  renderItem,
}: {
  items: string[];
  duration?: number;
  reverse?: boolean;
  className?: string;
  renderItem?: (item: string, i: number) => ReactNode;
}) {
  const Item = ({ item, i }: { item: string; i: number }) =>
    renderItem ? (
      <>{renderItem(item, i)}</>
    ) : (
      <span className="mx-8 inline-flex items-center gap-4 text-[clamp(1.6rem,4vw,3.2rem)] font-[family-name:var(--font-display)] font-semibold text-ink">
        {item}
        <span className="text-orange text-[0.7em]">✦</span>
      </span>
    );

  const group = (
    <div className="marquee__track" aria-hidden>
      {[...items, ...items].map((item, i) => (
        <Item item={item} i={i} key={i} />
      ))}
    </div>
  );

  return (
    <div
      className={`marquee ${reverse ? "marquee--rev" : ""} ${className}`}
      style={{ ["--dur" as string]: `${duration}s` }}
    >
      {group}
    </div>
  );
}
