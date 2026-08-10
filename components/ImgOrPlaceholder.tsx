"use client";

import { useEffect, useState } from "react";
import Placeholder from "./Placeholder";

/** Renders the real image; falls back to the orange Placeholder if the file
 *  isn't in /public yet (so the layout never shows a broken image). */
export default function ImgOrPlaceholder({
  src,
  alt,
  ratio = "3/4",
  seed = 0,
  className = "",
}: {
  src: string;
  alt: string;
  ratio?: string;
  seed?: number;
  className?: string;
}) {
  const [failed, setFailed] = useState(false);

  // clear the error when we point at a different file
  useEffect(() => setFailed(false), [src]);

  if (failed) return <Placeholder ratio={ratio} label={alt} seed={seed} className={className} />;

  return (
    <div
      className={`overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white ${className}`}
      style={{ aspectRatio: ratio }}
    >
      {/* key={src}: remounts on tab change so a previous error never sticks */}
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        key={src}
        src={src}
        alt={alt}
        onError={() => setFailed(true)}
        className="h-full w-full object-cover"
      />
    </div>
  );
}
