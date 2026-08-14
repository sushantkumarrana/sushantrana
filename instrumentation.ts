/**
 * Runs once when a Next.js server instance starts.
 *
 * The heartbeat schedule lives here because this site is deployed as a
 * Hostinger Node.js Web App, and that product has no Cron Jobs feature — it is
 * only offered on classic shared hosting. Rather than depend on SSH crontab
 * (which does not survive a redeploy) or an external pinger, the always-on Node
 * process schedules its own ping.
 */
export async function register() {
  // Only the Node runtime can reach the database, and only production should
  // write rows — otherwise every local `next dev` pollutes the table.
  if (process.env.NEXT_RUNTIME !== "nodejs") return;
  if (process.env.NODE_ENV !== "production") return;

  const { pingDatabase } = await import("@/lib/heartbeat");

  const EVERY_6_HOURS = 6 * 60 * 60 * 1000;

  // Ping shortly after boot, not during it: `register` has to finish before the
  // server accepts requests, so nothing slow belongs on this path. A restart
  // therefore also refreshes the 7-day inactivity clock on its own.
  setTimeout(() => void pingDatabase("boot"), 15_000).unref();

  // unref so the timer can never be the reason a process refuses to exit.
  setInterval(() => void pingDatabase("interval"), EVERY_6_HOURS).unref();

  console.log("[heartbeat] scheduled every 6h");
}
