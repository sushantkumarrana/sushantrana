import { createClient } from "@supabase/supabase-js";

/**
 * Writes one row to `heartbeat` so Supabase sees database activity.
 *
 * Supabase pauses Free plan projects after roughly 7 days of low activity, and
 * a paused project drops the lead form to email-only delivery.
 *
 * Deliberately NOT done by submitting the real lead form on a timer: that
 * would fill `leads` with fake enquiries and send a notification email every
 * day, which is the fastest way to start ignoring lead emails altogether.
 */

// The site is not on a hosting plan with cron, so the schedule lives inside the
// app (see instrumentation.ts). Shared here because the HTTP route calls this
// too, and neither caller should be able to hammer the table.
const MIN_GAP_MS = 55 * 60 * 1000;

// A paused project can leave the connection hanging. Nobody waits on a
// heartbeat, but a stuck request would still tie up the process.
const DB_BUDGET_MS = 8000;

let lastPing = 0;

export type PingResult =
  | { ok: true; pinged?: string; skipped?: string }
  | { ok: false; error: string };

export async function pingDatabase(source: string): Promise<PingResult> {
  const url = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_PUBLISHABLE_KEY;

  if (!url || !supabaseKey) {
    console.error("[heartbeat] Supabase env vars missing");
    return { ok: false, error: "not configured" };
  }

  const now = Date.now();
  if (now - lastPing < MIN_GAP_MS) return { ok: true, skipped: "throttled" };
  lastPing = now;

  try {
    const supabase = createClient(url, supabaseKey, {
      auth: { persistSession: false },
      global: {
        fetch: (input, init) =>
          fetch(input, { ...init, signal: AbortSignal.timeout(DB_BUDGET_MS) }),
      },
    });

    const { error } = await supabase.from("heartbeat").insert({ source });

    if (error) {
      console.error("[heartbeat] insert failed:", error.message);
      return { ok: false, error: "insert failed" };
    }

    return { ok: true, pinged: new Date().toISOString() };
  } catch (err) {
    console.error("[heartbeat] insert threw:", err);
    return { ok: false, error: "unreachable" };
  }
}
