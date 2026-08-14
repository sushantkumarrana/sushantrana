import { NextResponse } from "next/server";
import { pingDatabase } from "@/lib/heartbeat";

// Always run on the server, never cached — a cached heartbeat is not a
// heartbeat, it never reaches the database at all.
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

/**
 * Manual and external entry point to the heartbeat.
 *
 * The app pings itself on a timer (see instrumentation.ts), so this route is
 * not what keeps the project awake day to day. It stays because it is the only
 * way to check that mechanism from outside, and because it doubles as an uptime
 * probe: a 200 means the app is up AND the database is reachable, which is
 * exactly the pair that has to hold for a lead to be saved.
 *
 * Left open deliberately, with abuse bounded by the throttle inside
 * pingDatabase rather than a secret: a shared token is one more thing to set
 * and to forget, and forgetting it fails silently.
 */
export async function GET() {
  const result = await pingDatabase("http");
  return NextResponse.json(result, { status: result.ok ? 200 : 500 });
}
