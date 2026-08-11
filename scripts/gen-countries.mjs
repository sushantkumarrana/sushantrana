import { getCountries, getCountryCallingCode } from "libphonenumber-js/max";

const names = new Intl.DisplayNames(["en"], { type: "region" });
const rows = getCountries()
  .map((iso) => ({ iso, dial: getCountryCallingCode(iso), name: names.of(iso) || iso }))
  .filter((r) => r.name !== r.iso)
  .sort((a, b) => a.name.localeCompare(b.name, "en"));

const body = rows.map((r) => `  { iso: "${r.iso}", dial: "${r.dial}", name: ${JSON.stringify(r.name)} },`).join("\n");

process.stdout.write(`/**
 * Every country libphonenumber can validate, with its E.164 calling code.
 *
 * GENERATED — do not hand-edit. Regenerate after a libphonenumber-js upgrade:
 *   node scripts/gen-countries.mjs > lib/countries.ts
 *
 * Written to a file rather than derived at runtime from Intl.DisplayNames on
 * purpose: ICU country names differ slightly between Node and browsers, and a
 * <select> whose option text differs between server and client render is a
 * hydration mismatch.
 */

export type Country = { iso: string; dial: string; name: string };

/** Default selection. India is the home market. */
export const DEFAULT_COUNTRY = "IN";

export const COUNTRIES: Country[] = [
${body}
];

export const COUNTRY_BY_ISO = new Map(COUNTRIES.map((c) => [c.iso, c]));

export const isCountry = (iso: string) => COUNTRY_BY_ISO.has(iso);

/**
 * Flag emoji from an ISO 3166-1 alpha-2 code: each letter maps to its regional
 * indicator symbol. Pure arithmetic, so it is identical on server and client.
 */
export const flagOf = (iso: string) =>
  String.fromCodePoint(...[...iso.toUpperCase()].map((c) => 0x1f1e6 + c.charCodeAt(0) - 65));
`);
