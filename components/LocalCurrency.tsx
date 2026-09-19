"use client";

import { createContext, useContext, useEffect, useState, type ReactNode } from "react";

/**
 * Shows rupee prices in the visitor's own currency.
 *
 * The page is rendered in INR (what Google India and the JSON-LD see), then the
 * browser's time zone picks the currency after hydration. Time zone rather than
 * navigator.language because most Indian browsers report "en-US".
 *
 * ponytail: time zone → currency table covers the markets this site sells to;
 * anything unlisted falls back to USD. Add a zone here if a new market matters.
 */

type Rates = Record<string, number>; // units of currency per 1 INR

const EUR_ZONES = [
  "Amsterdam", "Athens", "Berlin", "Bratislava", "Brussels", "Dublin", "Helsinki",
  "Lisbon", "Ljubljana", "Luxembourg", "Madrid", "Malta", "Monaco", "Paris",
  "Riga", "Rome", "Tallinn", "Vienna", "Vilnius", "Zagreb",
];
const CAD_ZONES = [
  "Toronto", "Vancouver", "Edmonton", "Winnipeg", "Halifax", "St_Johns", "Regina",
  "Montreal", "Moncton", "Whitehorse", "Yellowknife", "Iqaluit",
];

const ZONE_CURRENCY: Record<string, string> = {
  "Asia/Kolkata": "INR",
  "Asia/Calcutta": "INR",
  "Asia/Dubai": "AED",
  "Asia/Riyadh": "SAR",
  "Asia/Qatar": "QAR",
  "Asia/Kuwait": "KWD",
  "Asia/Bahrain": "BHD",
  "Asia/Muscat": "OMR",
  "Asia/Singapore": "SGD",
  "Europe/London": "GBP",
  "Pacific/Auckland": "NZD",
  "Africa/Johannesburg": "ZAR",
  ...Object.fromEntries(EUR_ZONES.map((c) => [`Europe/${c}`, "EUR"])),
  ...Object.fromEntries(CAD_ZONES.map((c) => [`America/${c}`, "CAD"])),
};

function currencyFromZone(tz: string): string {
  if (ZONE_CURRENCY[tz]) return ZONE_CURRENCY[tz];
  if (tz.startsWith("Australia/")) return "AUD";
  return "USD";
}

/** Rounds converted prices so they read like prices, not exchange maths. */
function niceRound(n: number): number {
  if (n >= 1000) return Math.round(n / 10) * 10;
  if (n >= 100) return Math.round(n / 5) * 5;
  return Math.round(n);
}

type Ctx = { currency: string; rate: number } | null;
const CurrencyCtx = createContext<Ctx>(null);

export function CurrencyProvider({ rates, children }: { rates: Rates | null; children: ReactNode }) {
  const [ctx, setCtx] = useState<Ctx>(null);

  useEffect(() => {
    if (!rates) return;
    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
    const currency = currencyFromZone(tz);
    const rate = rates[currency];
    // Syncing with the browser's time zone, which the server cannot know.
    // eslint-disable-next-line react-hooks/set-state-in-effect
    if (currency !== "INR" && rate) setCtx({ currency, rate });
  }, [rates]);

  return <CurrencyCtx.Provider value={ctx}>{children}</CurrencyCtx.Provider>;
}

/** True once a non-INR currency is active. */
export function useForeignCurrency(): string | null {
  return useContext(CurrencyCtx)?.currency ?? null;
}

/** Converts one rupee amount string ("18,000", "18K") in the active currency. */
function convert(digits: string, compact: boolean, { currency, rate }: NonNullable<Ctx>): string {
  const inr = Number(digits.replace(/,/g, "")) * (compact ? 1000 : 1);
  return new Intl.NumberFormat("en", {
    style: "currency",
    currency,
    maximumFractionDigits: 0,
    notation: compact && inr * rate >= 10000 ? "compact" : "standard",
  }).format(niceRound(inr * rate));
}

/** Renders `text` with every ₹ amount in it swapped for the visitor's currency. */
export function Localized({ text }: { text: string }) {
  const ctx = useContext(CurrencyCtx);
  if (!ctx) return <>{text}</>;
  return <>{text.replace(/₹(\d+(?:,\d+)*)(K)?/g, (_, d: string, k?: string) => convert(d, !!k, ctx))}</>;
}

/** Tax note under the plans: GST applies in India; elsewhere, say the figure
 *  is a conversion. The rates link is the attribution the free API requires. */
export function PriceNote() {
  const currency = useForeignCurrency();
  if (!currency) {
    return <>Prices are plus 18% GST. Larger or more complex sites may need a custom quote.</>;
  }
  return (
    <>
      Prices shown in {currency}, converted from Indian rupees at today&apos;s rate. The
      final price is confirmed on the call.{" "}
      <a
        href="https://www.exchangerate-api.com"
        target="_blank"
        rel="noopener noreferrer"
        className="underline underline-offset-2"
      >
        Rates by Exchange Rate API
      </a>
    </>
  );
}
