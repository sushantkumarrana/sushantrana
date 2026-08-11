import { NextResponse } from "next/server";
import { createClient } from "@supabase/supabase-js";
import { Resend } from "resend";
import { resolveMx, resolve4, resolve6 } from "node:dns/promises";
import {
  ALL_SERVICES,
  ENQUIRY_TYPES,
  ENQUIRY_TYPE_VALUES,
  OTHER_SERVICE,
} from "@/lib/services";
import { COUNTRY_BY_ISO, DEFAULT_COUNTRY } from "@/lib/countries";
import { emailDomain, toE164, validateEmail, validatePhone } from "@/lib/validation";
import { leadEmailHtml, leadEmailText, type LeadEmail } from "@/lib/lead-email";

// Always run on the server, never cached.
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// Where enquiry notifications go. Override with the LEAD_NOTIFY_TO env var
// (useful while me@sushantrana.com is bouncing) without touching code.
const TO = process.env.LEAD_NOTIFY_TO || "me@sushantrana.com";
const FROM = "Sushant Rana Website <leads@sushantrana.com>";

// Simple in-memory throttle. Works because Hostinger runs one persistent
// Node process; it resets on restart, which is fine for basic abuse control.
const hits = new Map<string, number[]>();
const WINDOW_MS = 60_000;
const MAX_PER_WINDOW = 5;

function rateLimited(ip: string) {
  const now = Date.now();
  const recent = (hits.get(ip) ?? []).filter((t) => now - t < WINDOW_MS);
  recent.push(now);
  hits.set(ip, recent);
  if (hits.size > 5000) hits.clear(); // crude cap so the map can't grow forever
  return recent.length > MAX_PER_WINDOW;
}

const clean = (v: unknown, max = 2000) =>
  typeof v === "string" ? v.trim().slice(0, max) : "";

/**
 * Proves the email's domain can actually receive mail, which is the one check
 * the browser cannot make. A domain with no MX record and no address record is
 * not a mailbox — that is a typo or an invention, and the lead would bounce.
 *
 * Fails OPEN: if DNS itself is unreachable or times out, the lead is accepted.
 * Losing a real enquiry to a flaky resolver is far worse than storing one bad
 * address, so only a definitive "this domain does not exist" rejects.
 */
const DNS_BUDGET_MS = 2500;

/** Codes that mean "this name definitively has no such record". Anything else
 *  — SERVFAIL, REFUSED, ETIMEOUT, no network — is our infrastructure failing,
 *  not the visitor mistyping. */
const NO_SUCH_RECORD = new Set(["ENOTFOUND", "NXDOMAIN", "ENODATA"]);

async function domainAcceptsMail(domain: string): Promise<boolean> {
  // One budget for the whole check, and all three lookups in parallel. Doing
  // them in sequence with a timeout each meant an unreachable resolver added
  // three timeouts back to back to every single submission.
  const deadline = new Promise<"timeout">((resolve) =>
    setTimeout(() => resolve("timeout"), DNS_BUDGET_MS)
  );

  const lookups = (async (): Promise<boolean> => {
    const results = await Promise.allSettled([
      resolveMx(domain),
      // No MX is still deliverable: RFC 5321 falls back to the address record.
      resolve4(domain),
      resolve6(domain),
    ]);

    if (results.some((r) => r.status === "fulfilled" && r.value.length > 0)) return true;

    // Reject only when every lookup came back as a definitive "no such record".
    // If even one failed for another reason, we don't actually know, so accept.
    return !results.every(
      (r) =>
        r.status === "rejected" &&
        NO_SUCH_RECORD.has((r.reason as NodeJS.ErrnoException)?.code ?? "")
    );
  })();

  const outcome = await Promise.race([lookups, deadline]);
  return outcome === "timeout" ? true : outcome;
}

export async function POST(req: Request) {
  try {
    const ip =
      req.headers.get("x-forwarded-for")?.split(",")[0]?.trim() ||
      req.headers.get("x-real-ip") ||
      "unknown";

    if (rateLimited(ip)) {
      return NextResponse.json(
        { ok: false, error: "Too many requests. Please try again shortly." },
        { status: 429 }
      );
    }

    const body = await req.json().catch(() => ({}));

    // Honeypot: real users never fill this hidden field.
    if (clean(body.company_website)) {
      // Pretend success so bots don't learn they were caught.
      return NextResponse.json({ ok: true });
    }

    const name = clean(body.name, 120);
    const email = clean(body.email, 200);
    const phone = clean(body.phone, 40);
    const business = clean(body.business, 200);
    const message = clean(body.message, 4000);

    // Allow-list both dropdowns against the shared catalogue rather than
    // storing whatever arrives: the request is client-supplied, so an unknown
    // value means a tampered payload, not a new service.
    const rawService = clean(body.service, 120);
    const service =
      rawService === OTHER_SERVICE || ALL_SERVICES.includes(rawService)
        ? rawService
        : "";

    const rawType = clean(body.enquiryType, 40);
    const enquiryType = ENQUIRY_TYPE_VALUES.includes(rawType) ? rawType : "";

    // Which country's numbering plan the phone should be read against.
    const rawCountry = clean(body.phoneCountry, 2).toUpperCase();
    const phoneCountry = COUNTRY_BY_ISO.has(rawCountry) ? rawCountry : DEFAULT_COUNTRY;

    if (!name || !email || !phone) {
      return NextResponse.json(
        { ok: false, error: "Name, email and phone are required." },
        { status: 400 }
      );
    }

    // Re-run the browser's own checks. The client can be bypassed entirely by
    // posting here directly, so this is where they actually count. `field` lets
    // the form highlight the input that was rejected.
    const emailCheck = validateEmail(email);
    if (!emailCheck.ok) {
      return NextResponse.json(
        { ok: false, field: "email", error: emailCheck.error },
        { status: 400 }
      );
    }

    const phoneCheck = await validatePhone(phoneCountry, phone);
    if (!phoneCheck.ok) {
      return NextResponse.json(
        { ok: false, field: "phone", error: phoneCheck.error },
        { status: 400 }
      );
    }

    // The check the browser can't make: does this domain receive mail at all?
    if (!(await domainAcceptsMail(emailDomain(email)))) {
      return NextResponse.json(
        {
          ok: false,
          field: "email",
          error: `No mail server exists for "${emailDomain(email)}". Please check the spelling.`,
        },
        { status: 400 }
      );
    }

    // Store the number in E.164 so every lead is dialable as-is, regardless of
    // how the visitor spaced or bracketed it.
    const phoneE164 = (await toE164(phoneCountry, phone)) || phone;

    const url = process.env.SUPABASE_URL;
    // Publishable key + an INSERT-only RLS policy = least privilege.
    // Even if this key leaked it could only add rows, never read them.
    const supabaseKey = process.env.SUPABASE_PUBLISHABLE_KEY;
    const resendKey = process.env.RESEND_API_KEY;

    if (!url || !supabaseKey) {
      console.error("[lead] Supabase env vars missing");
      return NextResponse.json(
        { ok: false, error: "Server is not configured. Please email me directly." },
        { status: 500 }
      );
    }

    const supabase = createClient(url, supabaseKey, {
      auth: { persistSession: false },
    });

    const { error } = await supabase.from("leads").insert({
      name,
      email,
      phone: phoneE164,
      business: business || null,
      // Not required server-side even though the form marks it so: a visitor on
      // a cached older bundle would otherwise have their lead rejected outright,
      // which costs far more than a null column.
      service: service || null,
      enquiry_type: enquiryType || null,
      message: message || null,
      source_path: clean(body.sourcePath, 300) || null,
      referrer: clean(req.headers.get("referer"), 300) || null,
      user_agent: clean(req.headers.get("user-agent"), 300) || null,
    });

    if (error) {
      console.error("[lead] insert failed:", error.message);
      return NextResponse.json(
        { ok: false, error: "Could not save your request. Please try again." },
        { status: 500 }
      );
    }

    // The lead is safely stored. Email is best-effort from here — if Resend
    // is down we must NOT tell the visitor it failed, or they'd submit twice.
    if (resendKey) {
      try {
        const typeLabel =
          ENQUIRY_TYPES.find((t) => t.value === enquiryType)?.label ?? "Enquiry";

        const details: LeadEmail = {
          name,
          email,
          phone: phoneE164,
          business,
          service,
          typeLabel,
          enquiryType,
          message,
          sourcePath: clean(body.sourcePath, 300) || "/",
          receivedAt: `${new Date().toLocaleString("en-IN", {
            timeZone: "Asia/Kolkata",
          })} IST`,
        };

        const resend = new Resend(resendKey);
        await resend.emails.send({
          from: FROM,
          to: TO,
          replyTo: email,
          // Service in the subject line so the inbox itself is triageable
          // without opening anything.
          subject: `New ${typeLabel} — ${service || "general"} — ${name}${
            business ? ` (${business})` : ""
          }`,
          // Both parts: a mail with no text alternative scores worse with spam
          // filters, and some clients preview the text version.
          html: leadEmailHtml(details),
          text: leadEmailText(details),
        });
      } catch (mailErr) {
        console.error("[lead] email failed (lead was still saved):", mailErr);
      }
    } else {
      console.warn("[lead] RESEND_API_KEY missing — lead saved, no email sent");
    }

    return NextResponse.json({ ok: true });
  } catch (err) {
    console.error("[lead] unexpected error:", err);
    return NextResponse.json(
      { ok: false, error: "Something went wrong. Please try again." },
      { status: 500 }
    );
  }
}
