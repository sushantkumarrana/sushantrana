-- =====================================================================
--  Enforces the retention period promised in the Privacy Policy.
--
--  lib/legal.ts tells visitors their enquiry is deleted "a maximum of
--  three weeks from our last contact". Without this job that sentence is
--  simply untrue — rows would sit in public.leads forever.
--
--  Run once in Supabase -> SQL Editor. Requires the pg_cron extension
--  (Database -> Extensions -> enable "pg_cron").
--
--  IF YOU CHANGE THE PERIOD, change it in lib/legal.ts too. The two must
--  always say the same thing.
-- =====================================================================

create extension if not exists pg_cron;

-- Deletes enquiries older than three weeks.
--
-- Uses created_at, which is the only timestamp on the table. If you later
-- track a "last contacted" date, purge on that instead — the policy says
-- three weeks from LAST CONTACT, which is never earlier than creation, so
-- created_at deletes at or before the promised time. That is the safe
-- direction to be wrong in.
--
-- Leads you want to keep (a live client) should be moved out of this table
-- or given a status the filter below excludes, or they will be deleted.
create or replace function public.purge_old_leads()
returns void
language sql
security definer
set search_path = public
as $$
  delete from public.leads
  where created_at < now() - interval '21 days'
    and status not in ('won');   -- keep converted clients; see note above
$$;

-- Every day at 03:30 UTC (09:00 IST).
select cron.schedule(
  'purge-old-leads',
  '30 3 * * *',
  $$select public.purge_old_leads();$$
);

-- To check it is registered:      select * from cron.job;
-- To remove it:                   select cron.unschedule('purge-old-leads');
-- To run it once by hand:         select public.purge_old_leads();
