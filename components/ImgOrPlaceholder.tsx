"use client";

import { useEffect, useState } from "react";
import Image from "next/image";
import Placeholder from "./Placeholder";

/** Renders the real image; falls back to the orange Placeholder if the file
 *  isn't in /public yet (so the layout never shows a broken image). */
export default function ImgOrPlaceholder({
  src,
  alt,
  ratio = "3/4",
  seed = 0,
  className = "",
  sizes = "(min-width: 1024px) 25vw, 50vw",
}: {
  src: string;
  alt: string;
  ratio?: string;
  seed?: number;
  className?: string;
  /** Must describe the real rendered width. A caller that hides this behind a
   *  breakpoint (`hidden lg:block`) leaves the box at 0px wide, and the browser
   *  then falls back to the largest srcset candidate — a 3840px download for a
   *  thumbnail. Pass an accurate value rather than relying on the default. */
  sizes?: string;
}) {
  const [failed, setFailed] = useState(false);

  // clear the error when we point at a different file
  useEffect(() => setFailed(false), [src]);

  if (failed) return <Placeholder ratio={ratio} label={alt} seed={seed} className={className} />;

  return (
    <div
      className={`relative overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white ${className}`}
      style={{ aspectRatio: ratio }}
    >
      {/* key={src}: remounts on tab change so a previous error never sticks.
          fill needs the wrapper to be positioned, hence `relative` above. */}
      <Image
        key={src}
        src={src}
        alt={alt}
        fill
        sizes={sizes}
        onError={() => setFailed(true)}
        className="object-cover"
      />
    </div>
  );
}
