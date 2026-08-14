import { NextResponse } from "next/server";
import { createClient } from "@supabase/supabase-js";

// Always run on the server, never cached — a cached heartbeat is not a
// heartbeat, it never reaches the database at all.
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

/**
 * Writes one row to `heartbeat` so Supabase sees database activity.
 *
 * Supabase pauses Free plan projects after roughly 7 days of low activity, and
 * a paused project means the lead form falls back to email only. A scheduled
 * GET here from Hostinger's cron keeps the project awake.
 *
 * Deliberately NOT done by submitting the real lead form on a timer: that
 * would fill `leads` with fake enquiries and send a notification email every
 * day, which is the fastest way to start ignoring lead emails altogether.
 *
 * Doubles as an uptime check — a 200 means the app is up AND the database is
 * reachable, which is exactly the pair that has to hold for a lead to be saved.
 */

// Deliberately open, with abuse bounded by the throttle below instead of a
// secret: a shared token is one more thing to set on hPanel and to forget, and
// forgetting it fails silently — the project pauses and nothing says why. The
// worst an attacker achieves here is a handful of empty rows a day.
const MIN_GAP_MS = 55 * 60 * 1000; // 55 min, so an hourly cron is never skipped
let lastPing = 0;

// A paused project can leave the connection hanging. Nobody is waiting on this
// response, but a stuck request would still tie up the process.
const DB_BUDGET_MS = 8000;

export async function GET() {
  const url = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_PUBLISHABLE_KEY;

  if (!url || !supabaseKey) {
    console.error("[heartbeat] Supabase env vars missing");
    return NextResponse.json(
      { ok: false, error: "not configured" },
      { status: 500 }
    );
  }

  const now = Date.now();
  if (now - lastPing < MIN_GAP_MS) {
    // Already pinged recently. Still a 200: the project is awake, which is the
    // question being asked, and a cron that emails on failure shouldn't shout
    // about a duplicate run.
    return NextResponse.json({ ok: true, skipped: "throttled" });
  }
  lastPing = now;

  try {
    const supabase = createClient(url, supabaseKey, {
      auth: { persistSession: false },
      global: {
        fetch: (input, init) =>
          fetch(input, { ...init, signal: AbortSignal.timeout(DB_BUDGET_MS) }),
      },
    });

    const { error } = await supabase
      .from("heartbeat")
      .insert({ source: "cron" });

    if (error) {
      console.error("[heartbeat] insert failed:", error.message);
      return NextResponse.json(
        { ok: false, error: "insert failed" },
        { status: 500 }
      );
    }

    return NextResponse.json({ ok: true, pinged: new Date().toISOString() });
  } catch (err) {
    console.error("[heartbeat] insert threw:", err);
    return NextResponse.json({ ok: false, error: "unreachable" }, { status: 500 });
  }
}
