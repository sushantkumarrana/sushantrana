"use client";

/** Blurred tool logos drifting behind the grey sections. Decorative. */
const LOGOS = [
  { f: "1", top: "6%", left: "5%", size: 96, dur: 22, delay: 0, anim: "drift1" },
  { f: "2", top: "20%", left: "84%", size: 112, dur: 28, delay: 2, anim: "drift2" },
  { f: "3", top: "34%", left: "12%", size: 84, dur: 25, delay: 1, anim: "drift2" },
  { f: "4", top: "30%", left: "70%", size: 100, dur: 30, delay: 3, anim: "drift1" },
  { f: "5", top: "50%", left: "88%", size: 90, dur: 26, delay: 0.5, anim: "drift1" },
  { f: "6", top: "56%", left: "6%", size: 104, dur: 24, delay: 2.5, anim: "drift2" },
  { f: "7", top: "70%", left: "78%", size: 92, dur: 29, delay: 1.5, anim: "drift2" },
  { f: "8", top: "76%", left: "18%", size: 88, dur: 27, delay: 3.5, anim: "drift1" },
  { f: "9", top: "88%", left: "60%", size: 96, dur: 23, delay: 1, anim: "drift1" },
  { f: "10", top: "44%", left: "40%", size: 80, dur: 31, delay: 2, anim: "drift2" },
];

export default function FloatingLogos() {
  return (
    <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden">
      {LOGOS.map((l, i) => (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          key={i}
          src={`/png-logo/${l.f}.png`}
          alt=""
          className="absolute select-none opacity-[0.15]"
          style={{
            top: l.top,
            left: l.left,
            width: l.size,
            height: l.size,
            filter: "blur(2px)",
            animation: `${l.anim} ${l.dur}s ease-in-out ${l.delay}s infinite`,
          }}
        />
      ))}
    </div>
  );
}
