-- =====================================================================
--  Adds the two lead-form dropdowns to an existing public.leads table.
--
--  Run this once in Supabase -> SQL Editor -> New query -> Run, BEFORE the
--  new form ships. Until these columns exist the API's insert fails and
--  every lead is lost with a 500.
--
--  Safe to re-run: every statement is `if not exists`.
--  (schema.sql already includes these — this file is only for the live
--  table that was created before they were added.)
-- =====================================================================

alter table public.leads add column if not exists service      text;
alter table public.leads add column if not exists enquiry_type text;

comment on column public.leads.service is
  'Service picked in the form dropdown, e.g. ''Google Ads''. Allow-listed against lib/services.ts by the API. Null for leads captured before this column existed.';
comment on column public.leads.enquiry_type is
  '''consultation'' (wants to talk first) or ''service'' (ready to buy). Null for older leads.';

create index if not exists leads_service_idx on public.leads (service);
