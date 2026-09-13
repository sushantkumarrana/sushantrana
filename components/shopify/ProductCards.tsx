"use client";

import { useState } from "react";
import { Check, Minus, Plus } from "lucide-react";

/**
 * Two working product cards, the kind I build into a Shopify collection grid.
 *
 * They are deliberately interactive rather than pictures of an interface: a
 * visitor can change the pack size and watch the price and unit rate update, or
 * pick a colour, choose a quantity and add to the bag. That is the whole point
 * of the section — a card that lets someone decide from the grid, without ever
 * opening the product page.
 *
 * Nothing leaves the browser. There is no cart behind this, so the button
 * settles back to its resting state after confirming.
 *
 * Photos live at /public/services/shopify/. A missing file falls back to a
 * tinted block, so the card is never broken while artwork is being swapped.
 */

type Status = "idle" | "adding" | "added";

const inr = (n: number) => `₹${n.toLocaleString("en-IN")}`;

/** Runs the Add → Adding… → Added → Add cycle, mirroring a real AJAX add. */
function useAddToCart(onDone?: () => void) {
  const [status, setStatus] = useState<Status>("idle");

  const add = () => {
    if (status !== "idle") return;
    setStatus("adding");
    setTimeout(() => {
      setStatus("added");
      setTimeout(() => {
        setStatus("idle");
        onDone?.();
      }, 1500);
    }, 900);
  };

  return { status, add };
}

function Photo({
  src,
  alt,
  badge,
  round,
}: {
  src: string;
  alt: string;
  badge: string;
  round?: boolean;
}) {
  const [failed, setFailed] = useState(false);
  return (
    <div className="relative aspect-square overflow-hidden bg-[linear-gradient(135deg,#ffece3_0%,#ffd6c4_100%)]">
      {failed ? (
        <span
          aria-hidden
          className={`absolute left-1/2 top-1/2 h-1/2 w-1/2 -translate-x-1/2 -translate-y-1/2 bg-orange/25 ${
            round ? "rounded-full" : "rounded-xl"
          }`}
        />
      ) : (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={src}
          alt={alt}
          loading="lazy"
          decoding="async"
          onError={() => setFailed(true)}
          className="h-full w-full object-cover"
        />
      )}
      <span className="absolute left-2.5 top-2.5 rounded bg-orange px-2 py-0.5 text-[9px] font-bold uppercase tracking-wide text-white">
        {badge}
      </span>
    </div>
  );
}

function Stars({ count }: { count: string }) {
  return (
    <p className="mt-1.5 text-[11px] font-semibold text-ink">
      <span className="text-orange" aria-hidden>
        ★★★★★
      </span>{" "}
      <span className="text-muted">{count}</span>
    </p>
  );
}

/* ------------------------------------------------ card one: pack pricing */

const PACKS = [
  { label: "1 pack", total: 399, unit: 399 },
  { label: "2 pack", total: 699, unit: 350 },
  { label: "3 pack", total: 949, unit: 316 },
];

function PackCard() {
  const [pack, setPack] = useState(0);
  const { status, add } = useAddToCart(() => setPack(0));
  const chosen = PACKS[pack];

  return (
    <article className="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">
      <Photo
        src="/services/shopify/card-oraah.webp"
        alt="Oraah Sugar Balance Tea pouch, a herbal blend for managing blood sugar"
        badge="Bestseller"
        round
      />
      <div className="p-3.5 text-center">
        <div className="flex flex-wrap justify-center gap-1.5">
          {["Herbal", "Ayurvedic"].map((t) => (
            <span
              key={t}
              className="rounded-full bg-orange/10 px-2 py-0.5 text-[9px] font-bold uppercase tracking-wide text-orange"
            >
              {t}
            </span>
          ))}
        </div>

        <h3 className="mt-2 text-sm font-extrabold leading-tight text-ink">
          Oraah Sugar Balance Tea for Diabetes
        </h3>
        <p className="mt-1 text-[11px] text-muted">Karela, jamun and gudmar blend</p>
        <Stars count="4.8 (312)" />

        <fieldset className="mt-2.5">
          <legend className="sr-only">Choose a pack size</legend>
          <div className="flex flex-wrap justify-center gap-1.5">
            {PACKS.map((p, i) => (
              <button
                key={p.label}
                type="button"
                aria-pressed={i === pack}
                onClick={() => setPack(i)}
                className={`rounded-lg border px-2 py-1 text-[10px] font-bold transition ${
                  i === pack
                    ? "border-orange bg-orange text-white"
                    : "border-[var(--color-line)] text-ink hover:border-orange hover:text-orange"
                }`}
              >
                {p.label}
              </button>
            ))}
          </div>
        </fieldset>

        <p className="mt-3 font-[family-name:var(--font-display)] text-lg font-extrabold text-ink">
          {inr(chosen.total)}
        </p>
        <p className="text-[10px] font-semibold text-muted" aria-live="polite">
          {inr(chosen.unit)} per pack
        </p>

        <button
          type="button"
          onClick={add}
          className={`mt-2.5 grid h-9 w-full place-items-center rounded-full text-[11px] font-bold uppercase tracking-wide text-white transition ${
            status === "added" ? "bg-[#15803d]" : status === "adding" ? "bg-orange-600" : "bg-orange"
          }`}
        >
          <span className="flex items-center gap-1.5">
            {status === "added" && <Check aria-hidden className="h-3.5 w-3.5" strokeWidth={3} />}
            {status === "idle" ? "Add to cart" : status === "adding" ? "Adding…" : "Added"}
          </span>
        </button>

        <div className="mt-2.5 flex justify-center gap-2 border-t border-[var(--color-line)] pt-2.5">
          {["No added sugar", "Ayush certified"].map((t) => (
            <span key={t} className="text-[8px] font-bold uppercase tracking-wide text-muted">
              {t}
            </span>
          ))}
        </div>
      </div>
    </article>
  );
}

/* ------------------------------------- card two: colour, quantity, price */

const COLOURS = [
  { name: "Tan", hex: "#b5773f" },
  { name: "Black", hex: "#111111" },
  { name: "Ivory", hex: "#f2efe9" },
  { name: "Maroon", hex: "#6d1b2e" },
  { name: "Blue", hex: "#1f5fc4" },
  { name: "Beige", hex: "#d8c8a6" },
];

const PRICE = 499;
const MRP = 1699;

function ColourCard() {
  const [colour, setColour] = useState<number | null>(null);
  const [qty, setQty] = useState(1);
  const { status, add } = useAddToCart(() => {
    setColour(null);
    setQty(1);
  });

  const ready = colour !== null;

  return (
    <article className="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">
      <Photo
        src="/services/shopify/card-ben-bag.webp"
        alt="Ben Classic Handbag in tan canvas, carried over the shoulder"
        badge="-71%"
      />
      <div className="p-3.5 text-center">
        <div className="flex flex-wrap justify-center gap-1.5">
          {["Canvas", "Everyday tote"].map((t) => (
            <span
              key={t}
              className="rounded-full bg-orange/10 px-2 py-0.5 text-[9px] font-bold uppercase tracking-wide text-orange"
            >
              {t}
            </span>
          ))}
        </div>

        <h3 className="mt-2 text-sm font-extrabold leading-tight text-ink">Ben Classic Handbag</h3>
        <p className="mt-1 text-[11px] text-muted">Roomy tote with a laptop sleeve</p>
        <Stars count="5.0 (2 reviews)" />

        <fieldset className="mt-2.5">
          <legend className="sr-only">Choose a colour</legend>
          <div className="flex flex-wrap justify-center gap-1.5">
            {COLOURS.map((c, i) => (
              <button
                key={c.name}
                type="button"
                title={c.name}
                aria-label={c.name}
                aria-pressed={i === colour}
                onClick={() => setColour(i)}
                className={`h-5 w-5 rounded-full border-2 transition ${
                  i === colour ? "border-orange" : "border-[var(--color-line)] hover:border-orange"
                }`}
                style={{ backgroundColor: c.hex }}
              />
            ))}
          </div>
          <p className="mt-1.5 text-[10px] font-semibold text-muted" aria-live="polite">
            {ready ? COLOURS[colour].name : "Pick a colour"}
          </p>
        </fieldset>

        <p className="mt-2 font-[family-name:var(--font-display)] text-lg font-extrabold text-ink">
          {inr(PRICE * qty)}{" "}
          <span className="text-xs font-medium text-muted line-through">{inr(MRP * qty)}</span>
        </p>

        {/* the quantity stepper only appears once a colour is chosen, the same
            way a real card reveals the next decision rather than showing all
            of them at once */}
        <div
          className={`grid overflow-hidden transition-[grid-template-rows,opacity] duration-300 ${
            ready ? "grid-rows-[1fr] opacity-100" : "grid-rows-[0fr] opacity-0"
          }`}
        >
          <div className="min-h-0">
            <div className="mt-2 flex items-center justify-center gap-2">
              <button
                type="button"
                aria-label="Reduce quantity"
                onClick={() => setQty((q) => Math.max(1, q - 1))}
                className="grid h-6 w-6 place-items-center rounded-full border border-[var(--color-line)] text-ink transition hover:border-orange hover:text-orange"
              >
                <Minus aria-hidden className="h-3 w-3" strokeWidth={3} />
              </button>
              <span
                className="w-6 font-[family-name:var(--font-display)] text-sm font-bold text-ink"
                aria-live="polite"
              >
                {qty}
              </span>
              <button
                type="button"
                aria-label="Increase quantity"
                onClick={() => setQty((q) => Math.min(9, q + 1))}
                className="grid h-6 w-6 place-items-center rounded-full border border-[var(--color-line)] text-ink transition hover:border-orange hover:text-orange"
              >
                <Plus aria-hidden className="h-3 w-3" strokeWidth={3} />
              </button>
            </div>
          </div>
        </div>

        <button
          type="button"
          onClick={add}
          disabled={!ready}
          className={`mt-2.5 grid h-9 w-full place-items-center rounded-full text-[11px] font-bold uppercase tracking-wide transition ${
            !ready
              ? "cursor-not-allowed bg-ink/10 text-muted"
              : status === "added"
                ? "bg-[#15803d] text-white"
                : status === "adding"
                  ? "bg-orange-600 text-white"
                  : "bg-orange text-white"
          }`}
        >
          <span className="flex items-center gap-1.5">
            {status === "added" && <Check aria-hidden className="h-3.5 w-3.5" strokeWidth={3} />}
            {!ready
              ? "Pick a colour"
              : status === "idle"
                ? "Add to bag"
                : status === "adding"
                  ? "Adding…"
                  : "Added"}
          </span>
        </button>

        <div className="mt-2.5 flex justify-center gap-2 border-t border-[var(--color-line)] pt-2.5">
          {["Free shipping", "7 day returns"].map((t) => (
            <span key={t} className="text-[8px] font-bold uppercase tracking-wide text-muted">
              {t}
            </span>
          ))}
        </div>
      </div>
    </article>
  );
}

export default function ProductCards() {
  return (
    <div className="grid grid-cols-2 gap-4">
      <PackCard />
      <ColourCard />
    </div>
  );
}
