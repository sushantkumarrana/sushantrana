import { NextResponse } from "next/server";
import { createClient } from "@supabase/supabase-js";
import { Resend } from "resend";

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

    if (!name || !email || !phone) {
      return NextResponse.json(
        { ok: false, error: "Name, email and phone are required." },
        { status: 400 }
      );
    }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return NextResponse.json(
        { ok: false, error: "That email address doesn't look right." },
        { status: 400 }
      );
    }

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
      phone,
      business: business || null,
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
        const resend = new Resend(resendKey);
        await resend.emails.send({
          from: FROM,
          to: TO,
          replyTo: email,
          subject: `New enquiry — ${name}${business ? ` (${business})` : ""}`,
          text: [
            `Name:     ${name}`,
            `Email:    ${email}`,
            `Phone:    ${phone}`,
            `Business: ${business || "—"}`,
            ``,
            `Message:`,
            message || "(none)",
            ``,
            `Page:     ${clean(body.sourcePath) || "/"}`,
            `Received: ${new Date().toLocaleString("en-IN", { timeZone: "Asia/Kolkata" })} IST`,
          ].join("\n"),
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
