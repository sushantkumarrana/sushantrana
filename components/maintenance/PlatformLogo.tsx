"use client";

import { useState } from "react";
import { Code2, Sparkles } from "lucide-react";

/** Platform logo tile. A logo file that is missing (Magento, until one is
 *  uploaded to /public/logos/platforms/) falls back to an icon, never a broken
 *  image. */
export default function PlatformLogo({ name, logos }: { name: string; logos: string[] }) {
  const [failed, setFailed] = useState<string[]>([]);
  const shown = logos.filter((l) => !failed.includes(l));
  const Fallback = name.startsWith("AI") ? Sparkles : Code2;

  return (
    <span className="flex h-10 items-center justify-center gap-2">
      {shown.length ? (
        shown.map((l) => (
          // eslint-disable-next-line @next/next/no-img-element -- tiny local SVGs, nothing for next/image to optimise
          <img
            key={l}
            src={`/logos/platforms/${l}.svg`}
            alt={`${name} logo`}
            width={36}
            height={36}
            className="h-9 w-auto max-w-[76px] object-contain"
            onError={() => setFailed((f) => [...f, l])}
          />
        ))
      ) : (
        <Fallback aria-hidden className="h-9 w-9 text-orange" strokeWidth={1.75} />
      )}
    </span>
  );
}
