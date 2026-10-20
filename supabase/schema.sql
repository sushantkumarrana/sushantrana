-- =====================================================================
--  sushantrana.com — leads table
--  Run this once in Supabase → SQL Editor → New query → Run.
-- =====================================================================

create table if not exists public.leads (
  id           uuid primary key default gen_random_uuid(),
  created_at   timestamptz not null default now(),

  name         text not null,
  email        text not null,
  phone        text not null,
  business     text,

  -- what they picked in the two dropdowns on the lead form. Nullable: the API
  -- stores null rather than rejecting a lead that arrives without them.
  service      text,          -- e.g. 'Google Ads' (see lib/services.ts)
  enquiry_type text,          -- 'consultation' | 'service'

  message      text,

  -- context, filled automatically by the API route
  source_path  text,          -- which page the form was opened from
  referrer     text,
  user_agent   text,

  status       text not null default 'new'   -- new | contacted | won | lost
);

create index if not exists leads_created_at_idx on public.leads (created_at desc);
create index if not exists leads_email_idx      on public.leads (email);
create index if not exists leads_status_idx     on public.leads (status);
create index if not exists leads_service_idx    on public.leads (service);

-- ---------------------------------------------------------------------
--  Security: RLS ON. The live project has one policy, "site can submit
--  leads" (INSERT for anon), because api/lead.php uses the publishable
--  key. anon has only the INSERT grant (migrations/003), so the key
--  cannot read, change or delete leads.
-- ---------------------------------------------------------------------
alter table public.leads enable row level security;

-- Belt and braces: make sure the public roles have no direct grants.
revoke all on public.leads from anon, authenticated;
