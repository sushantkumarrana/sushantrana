/**
 * Contact-detail validation, shared by the browser and the API route.
 *
 * The browser copy exists to give people an answer while they type. The server
 * copy is the one that decides — anything here can be bypassed by posting to
 * /api/lead directly, so the route runs the same checks again plus a live DNS
 * lookup that the browser cannot do.
 *
 * Nothing in this file imports libphonenumber: its metadata is 40 kB gzipped
 * and would land in the bundle of every page. `validatePhone` pulls it in with
 * a dynamic import, so it downloads only once someone actually touches the
 * phone field.
 */

import { COUNTRY_BY_ISO } from "./countries";

export type Check = { ok: boolean; error?: string; hint?: string };

const OK: Check = { ok: true };

/* ------------------------------------------------------------------ email */

/**
 * Deliberately stricter than the RFC. The RFC permits quoted local parts and
 * bare-hostname domains that no real business inbox uses, and every address
 * that reaches this form is meant to be one I can reply to.
 */
const EMAIL_RE = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,63}$/;

/** Throwaway-inbox providers. Not exhaustive — it never can be — but these are
 *  the ones that actually show up on lead forms. */
const DISPOSABLE = new Set([
  "10minutemail.com", "20minutemail.com", "33mail.com", "guerrillamail.com",
  "guerrillamail.info", "guerrillamail.net", "sharklasers.com", "grr.la",
  "mailinator.com", "mailinator.net", "trashmail.com", "trashmail.net",
  "temp-mail.org", "tempmail.com", "tempmailo.com", "tempr.email",
  "throwawaymail.com", "yopmail.com", "yopmail.net", "getnada.com",
  "nada.email", "dispostable.com", "maildrop.cc", "fakeinbox.com",
  "spamgourmet.com", "mytemp.email", "moakt.com", "emailondeck.com",
  "mohmal.com", "inboxbear.com", "burnermail.io", "tempinbox.com",
  "mailnesia.com", "spam4.me", "byom.de", "discard.email", "spambog.com",
  "einrot.com", "harakirimail.com", "tmail.ws", "linshiyouxiang.net",
]);

/** Domains people mistype most, checked with edit distance below. */
const COMMON_DOMAINS = [
  "gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.in", "yahoo.co.uk",
  "hotmail.com", "hotmail.co.uk", "outlook.com", "live.com", "msn.com",
  "icloud.com", "me.com", "aol.com", "proton.me", "protonmail.com",
  "zoho.com", "rediffmail.com", "gmx.com", "mail.com", "yandex.com",
];

/** Levenshtein, capped: we only care whether it is 1 or 2 edits away. */
function editDistance(a: string, b: string, max = 2): number {
  if (Math.abs(a.length - b.length) > max) return max + 1;
  let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    const cur = [i];
    let best = i;
    for (let j = 1; j <= b.length; j++) {
      const v = Math.min(
        prev[j] + 1,
        cur[j - 1] + 1,
        prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1)
      );
      cur[j] = v;
      if (v < best) best = v;
    }
    if (best > max) return max + 1; // whole row already too far — stop early
    prev = cur;
  }
  return prev[b.length];
}

/** "gmial.com" -> "gmail.com". Returns null when nothing is close enough. */
export function suggestDomain(domain: string): string | null {
  const d = domain.toLowerCase();
  if (COMMON_DOMAINS.includes(d)) return null;
  let best: string | null = null;
  let bestDist = 3;
  for (const c of COMMON_DOMAINS) {
    const dist = editDistance(d, c);
    if (dist < bestDist) {
      bestDist = dist;
      best = c;
    }
  }
  return bestDist <= 2 ? best : null;
}

export const emailDomain = (email: string) =>
  email.slice(email.lastIndexOf("@") + 1).toLowerCase();

/**
 * Syntax, shape and provider checks. Does NOT prove the domain exists — that
 * needs DNS, which only the server can do (see checkEmailDomain in the API
 * route). Safe to call from either side.
 */
export function validateEmail(raw: string): Check {
  const email = raw.trim();

  if (!email) return { ok: false, error: "Email is required." };
  if (/\s/.test(email)) return { ok: false, error: "An email address can't contain spaces." };
  if (email.length > 254) return { ok: false, error: "That email address is too long." };

  const at = email.split("@").length - 1;
  if (at === 0) return { ok: false, error: "That's not an email address — it needs an @ sign." };
  if (at > 1) return { ok: false, error: "An email address can only have one @ sign." };

  const [local, domain] = email.split("@");
  if (!local) return { ok: false, error: "Add the part before the @ sign." };
  if (local.length > 64) return { ok: false, error: "The part before the @ is too long." };
  if (!domain) return { ok: false, error: "Add the part after the @ sign, like gmail.com." };
  if (!domain.includes(".")) return { ok: false, error: "The domain needs a dot in it, like gmail.com." };
  if (email.includes("..")) return { ok: false, error: "An email address can't contain two dots in a row." };
  if (local.startsWith(".") || local.endsWith(".")) {
    return { ok: false, error: "An email address can't start or end the name with a dot." };
  }

  if (!EMAIL_RE.test(email)) return { ok: false, error: "That doesn't look like a valid email address." };

  const d = domain.toLowerCase();
  if (DISPOSABLE.has(d)) {
    return { ok: false, error: "Please use a permanent email address — I need to be able to reply." };
  }

  const suggestion = suggestDomain(d);
  // A hint, not an error: someone really can own an address at a domain one
  // letter away from gmail.com, and blocking them would be worse than asking.
  if (suggestion) return { ok: true, hint: `Did you mean ${local}@${suggestion}?` };

  return OK;
}

/* ------------------------------------------------------------------ phone */

/** Digits only, so "(98) 765-43210" and "98765 43210" both validate. */
export const digitsOnly = (s: string) => s.replace(/\D+/g, "");

/**
 * Validates a national number against the selected country's real numbering
 * plan — not just its length. libphonenumber's full metadata knows that Indian
 * mobiles start 6-9, so 1111111111 is rejected where a length check would pass
 * it.
 *
 * Async because the metadata is dynamically imported; see the note at the top.
 */
export async function validatePhone(iso: string, rawNumber: string): Promise<Check> {
  const country = COUNTRY_BY_ISO.get(iso);
  if (!country) return { ok: false, error: "Please choose a country." };

  const national = digitsOnly(rawNumber);
  if (!national) {
    // Distinguish an empty field from one holding "abcdefghij" — telling
    // someone their number is "required" when they just typed one is baffling.
    return {
      ok: false,
      error: rawNumber.trim()
        ? "A phone number can only contain digits."
        : "Phone number is required.",
    };
  }
  if (national.length < 4) return { ok: false, error: "That number is too short." };
  if (national.length > 15) return { ok: false, error: "That number is too long." };

  const { parsePhoneNumberFromString } = await import("libphonenumber-js/max");
  const parsed = parsePhoneNumberFromString(national, iso as never);

  if (!parsed || !parsed.isValid()) {
    return {
      ok: false,
      error: `That isn't a valid ${country.name} number. Check the digits, without the +${country.dial}.`,
    };
  }

  // Landlines are fine — plenty of businesses only have one — but a number
  // that can't receive a call at all is a typo worth catching.
  const type = parsed.getType();
  if (type === "PREMIUM_RATE" || type === "SHARED_COST" || type === "VOICEMAIL") {
    return { ok: false, error: "Please give a number I can actually call you back on." };
  }

  return OK;
}

/** E.164 ("+919876543210") — the format worth storing. Null if unparseable. */
export async function toE164(iso: string, rawNumber: string): Promise<string | null> {
  const { parsePhoneNumberFromString } = await import("libphonenumber-js/max");
  const parsed = parsePhoneNumberFromString(digitsOnly(rawNumber), iso as never);
  return parsed && parsed.isValid() ? parsed.number : null;
}
