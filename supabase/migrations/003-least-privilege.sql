-- =====================================================================
--  Least privilege for the public API roles.
--
--  The site only ever INSERTs (api/lead.php, api/heartbeat.php, with the
--  publishable key). RLS already blocks reads/updates/deletes, but the
--  default table grants still included TRUNCATE, which RLS does not cover.
--  purge_old_leads() is run by pg_cron as postgres, never over the API.
-- =====================================================================

revoke all on public.leads, public.heartbeat from anon, authenticated;
grant insert on public.leads, public.heartbeat to anon;

revoke execute on function public.purge_old_leads() from public, anon, authenticated;
