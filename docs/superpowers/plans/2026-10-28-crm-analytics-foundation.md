# CRM + Analytics Foundation Implementation Plan (plan 1 of 3)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** The site records every visitor's story in its own SQLite database, links it to the lead they send, and the `leadsforme` panel shows the CRM (new statuses, deal value, manual leads) plus Overview, Pages, Page detail, Visitors and Visitor story reports, with a consent banner for Europe / UK / Switzerland.

**Architecture:** A small tracker in `assets/js/site.js` batches events to a new `api/t.php`, which stores them in new tables of the existing `leads.sqlite` (outside `public_html`). Report queries live in one PHP file with pure functions, rendered by server-side PHP views in the panel (no JavaScript in the panel, so its CSP stays `default-src 'none'`). A nightly cron script builds daily rollups and enforces 90-day retention.

**Tech Stack:** PHP 8 + PDO SQLite, plain JS (no build), plain CSS, Hostinger cron.

**Spec:** `docs/superpowers/specs/2026-10-28-crm-analytics-design.md`

**Later plans (not in this one):** Plan 2 — ad platforms and Search Console (Google Ads script, Meta CAPI + spend, LinkedIn, ChatGPT Ads, GSC import, campaign report, GTM consent defaults). Plan 3 — lead score and weekly email.

## Before Task 1

The thank-you / journey changes from 28 Oct are still uncommitted in the working tree. Commit them on their own first (`git add -A && git commit -m "One thank-you page per service group; visit journey on every lead"`) so each task below commits only its own files.

## Global Constraints

- No Node, no build step, no new dependencies; PHP 8 + SQLite + plain JS/CSS only (AGENTS.md).
- All new data lives in `leads.sqlite` under `leads_data_dir()`; nothing new under `public_html` holds data.
- Retention: leads 90 days, `won` kept forever; visitors, sessions and raw events 90 days; daily rollup tables hold no visitor or session IDs and are kept.
- Statuses exactly: `new`, `qualified`, `wrong`, `won`, `lost`. Existing `contacted` rows become `new`.
- Deal value only on `won`; currency one of `INR` (default), `AED`, `USD`, `EUR`, `GBP`, `CAD`, `CHF`.
- Consent banner only when the browser time zone is in Europe (`Europe/*`, which includes London and Zurich). Before an answer and after "Decline": events carry no visitor ID and no session ID.
- Never store or send form contents, names, emails or phones in analytics events; never store IP addresses in analytics tables.
- Tracker sends with `navigator.sendBeacon` (fetch `keepalive` fallback), batches of at most 50 events, request body at most 16 KB; `api/t.php` rejects anything larger with HTTP 413.
- Panel keeps its current login, CSRF, security headers and CSP; panel pages render without JavaScript.
- After any change to `assets/js/site.js` or `assets/css/style.css`: `python3 -I dev/sync-layout.py`. Before handing back: `python3 -I dev/seo-audit.py` must end with 0 FAIL.
- Commit locally after each task. Never push: a push to `html-site` is a live deploy and needs Sushant's go-ahead.

## Review Focus

1. A visitor with storage blocked (Safari private, strict settings): the site still works, the tracker sends anonymous events, nothing throws. → Task 3, step "storage blocked".
2. A European visitor who never answers the banner: no visitor ID is ever written to localStorage or sent. → Task 4 test.
3. A lead sent while the tracker is silenced ("this is me" cookie): the lead is still saved and emailed; only analytics is skipped. → Task 5 test.
4. Bots and crawlers hitting `api/t.php` with junk or huge payloads: rejected, nothing stored, no PHP warning. → Task 2 tests.
5. Marking a lead `won` without an amount, or with text in the amount box: the panel refuses with a message and keeps the old status. → Task 6 test.

---

### Task 1: Database schema, statuses and retention

**Files:**
- Modify: `api/leads-db.php`
- Create: `dev/tests/db_test.php`, `dev/tests/bootstrap.php`

**Interfaces:**
- Produces:
  - `leads_data_dir(): string` honours env `LEADS_DATA_DIR` when set (tests point it at a temp dir).
  - `const LEADS_RETENTION_DAYS = 90;` `const LEAD_STATUSES = ['new', 'qualified', 'wrong', 'won', 'lost'];` `const LEAD_CURRENCIES = ['INR', 'AED', 'USD', 'EUR', 'GBP', 'CAD', 'CHF'];`
  - `leads` gains columns: `visitor_id TEXT`, `value REAL`, `currency TEXT`, `li_fat_id TEXT`, `status_at TEXT`, `ad_group TEXT`, `keyword TEXT` (+ index on `visitor_id`). Migration also runs `UPDATE leads SET status='new' WHERE status='contacted'`.
  - New tables: `visitors(id TEXT PRIMARY KEY, first_seen TEXT, last_seen TEXT, country TEXT, first_channel TEXT, first_landing TEXT)`, `sessions(id TEXT PRIMARY KEY, visitor_id TEXT, started_at TEXT, last_at TEXT, landing TEXT, channel TEXT, referrer TEXT, utm_source TEXT, utm_medium TEXT, utm_campaign TEXT, device TEXT, country TEXT)`, `events(id INTEGER PRIMARY KEY, ts TEXT, visitor_id TEXT, session_id TEXT, type TEXT, path TEXT, target TEXT, label TEXT, value INTEGER, lead_id INTEGER)`, `page_daily(day TEXT, path TEXT, views INT, visitors INT, engaged_ms INT, engaged_n INT, s25 INT, s50 INT, s75 INT, s90 INT, wa INT, call INT, email INT, form_start INT, form_submit INT, PRIMARY KEY(day, path))`, `channel_daily(day TEXT, channel TEXT, sessions INT, visitors INT, wa INT, call INT, form_start INT, form_submit INT, PRIMARY KEY(day, channel))`. Indexes on `events(ts)`, `events(visitor_id)`, `events(path, ts)`, `sessions(visitor_id)`.
  - `leads_purge(): void` deletes non-won leads older than 90 days and visitors/sessions/events older than 90 days (by `last_seen` / `last_at` / `ts`).
- `dev/tests/bootstrap.php` sets `LEADS_DATA_DIR` to a fresh temp dir and defines `check(bool $ok, string $msg): void` (prints FAIL and exits 1 on false).

- [ ] **Step 1: Write the failing test** `dev/tests/db_test.php`: on a fresh dir, `leads_db()` creates every table above; on a DB created with the old schema (create the old `leads` table by hand, insert one `contacted` row) `leads_db()` adds the new columns and the row becomes `new`; `leads_purge()` removes a `new` lead dated 91 days ago, keeps one dated 89 days ago and a `won` one dated 400 days ago, and removes an event dated 91 days ago. Prints `db ok`.
- [ ] **Step 2: Run** `php dev/tests/db_test.php` — expected: FAIL (missing table `visitors`).
- [ ] **Step 3: Implement** the schema, migration (check `PRAGMA table_info(leads)` per column, like the existing `journey` migration) and purge in `api/leads-db.php`. Keep the `lead_channel` self-check working (`php api/leads-db.php` → `lead_channel ok`).
- [ ] **Step 4: Run** `php dev/tests/db_test.php && php api/leads-db.php` — expected: `db ok` and `lead_channel ok`.
- [ ] **Step 5: Commit** `git add api/leads-db.php dev/tests && git commit -m "Leads DB: analytics tables, new statuses, 90-day retention"`

### Task 2: Tracking endpoint `api/t.php`

**Files:**
- Create: `api/track.php` (storage logic), `api/t.php` (HTTP endpoint), `dev/tests/track_test.php`

**Interfaces:**
- Consumes: Task 1 tables, `lead_channel(array): string`.
- Produces:
  - Request body (JSON): `{"v": string|null, "s": string|null, "tz": string, "ref": string, "attr": {landing_page, utm_source, utm_medium, utm_campaign, gclid, fbclid, li_fat_id}, "e": [{"t": type, "p": path, "x": target, "l": label, "n": int, "lead": int}]}`. `t` ∈ `page_view`, `scroll`, `engaged`, `click`, `form_start`, `form_submit`. For `click`, `x` ∈ `whatsapp`, `call`, `email`, `cta`, `outbound`.
  - `track_store(PDO $db, array $body, string $userAgent, int $now): int` — returns events stored; IDs must match `/^[a-f0-9]{32}$/` or be null; drops unknown types, paths not starting with `/`, labels over 120 chars (truncate), more than 50 events; upserts `visitors` and `sessions` only when `v`/`s` present (session row created from `attr`/`ref` on first sight, `channel` via `lead_channel`).
  - `is_bot(string $ua): bool` — true for empty UA and for `/bot|crawl|spider|slurp|headless|lighthouse|preview|fetch|curl|wget|python|monitor/i`.
  - `tz_country(string $tz): string` — ISO code from a map of the ~40 time zones that cover India, UAE, US, Canada, UK, Switzerland, EU and the rest of the Gulf; `''` when unknown.
  - `device_of(string $ua): string` — `mobile`, `tablet` or `desktop`.
  - `api/t.php`: POST only (405 otherwise), body ≤ 16384 bytes (413), invalid JSON 400, bot UA → 204 with nothing stored, otherwise 204. No cookies, `Cache-Control: no-store`. Rate limit 120 requests per IP per minute using a file counter in `leads_data_dir()` (same pattern as the panel's login throttle); the IP is never written to the DB.
- [ ] **Step 1: Write the failing test** `dev/tests/track_test.php`: a body with `v`, `s` and one `page_view` stores 1 event, 1 visitor, 1 session with `channel` `Google Ads` when `attr.gclid` is set; the same body with `v:null,s:null` stores the event with null IDs and no visitor row; 60 events → 50 stored; `t:"evil"` and `p:"https://x"` are dropped; `v:"../etc"` is treated as null; `is_bot('Googlebot/2.1')` true, a Chrome UA false; `tz_country('Asia/Kolkata') === 'IN'`, `tz_country('Europe/Zurich') === 'CH'`; `device_of` of an iPhone UA is `mobile`. Prints `track ok`.
- [ ] **Step 2: Run** `php dev/tests/track_test.php` — expected: FAIL (`track_store` undefined).
- [ ] **Step 3: Implement** `api/track.php` and `api/t.php`.
- [ ] **Step 4: Run** `php dev/tests/track_test.php` — expected `track ok`. Then with the preview server (`.claude/launch.json` → `sushantrana-html`, port 8091): `curl -s -o /dev/null -w "%{http_code}" -X POST localhost:8091/api/t.php -d "$(head -c 20000 /dev/zero | tr '\0' a)"` → `413`; `curl -s -o /dev/null -w "%{http_code}" localhost:8091/api/t.php` → `405`; a valid body with UA `Googlebot` → `204` and no new row.
- [ ] **Step 5: Commit** `git add api/track.php api/t.php dev/tests/track_test.php && git commit -m "Tracking endpoint api/t.php"`

### Task 3: Tracker in `site.js`

**Files:**
- Modify: `assets/js/site.js` (new block right after the `journey` block; `ATTR_PARAMS` gains `li_fat_id`)

**Interfaces:**
- Consumes: Task 2 request format.
- Produces (inside the site.js IIFE): `track(t, fields)` queues an event; `const visitorId` / `sessionId` (strings or `null` when consent is not granted or storage is blocked); consent state `consent()` → `"granted"` outside Europe, else the stored answer (`localStorage` `sr_consent` = `granted` / `denied`) or `"pending"`. Storage keys: `sr_vid` (`{id, t}` — renewed after 90 days), `sr_sid` (`{id, last}` in sessionStorage-independent localStorage, new id after 30 min idle). Silenced entirely when `document.cookie` has `sr_me=1` or `navigator.webdriver` is true.
- Behaviour: `page_view` on load; `scroll` once per threshold 25/50/75/90; `engaged` with visible milliseconds on `visibilitychange` → hidden and `pagehide`; `click` via one delegated listener: `href` starting `https://wa.me` or `https://api.whatsapp.com` → `whatsapp`, `tel:` → `call`, `mailto:` → `email`, other origin → `outbound`, `.btn` or `[data-consult]` → `cta`, label = trimmed text (≤ 120); `form_start` on the first `input` event inside a form (`x` = `data-form-name` or `consultation`); flush on `pagehide` and every 10 s with `navigator.sendBeacon('/api/t.php', blob)`.
- Storage blocked: every storage access in try/catch; with no storage the tracker sends anonymous events (`v`, `s` null).

- [ ] **Step 1: Verify the failing state**: preview on port 8091, open `/`, then `sqlite3 .data/leads.sqlite "select count(*) from events"` → `0` (or "no such table" if the DB is fresh: run `php -r 'require "api/leads-db.php"; leads_db();'` first).
- [ ] **Step 2: Implement** the tracker.
- [ ] **Step 3: Verify in the browser**: clear storage, open `/` → `/services/` → `/services/google-ads/`, scroll to the bottom, click the WhatsApp link (prevent navigation in the console first), switch tab and back. Expected in SQLite: 1 visitor, 1 session with `landing='/'`, 3 `page_view`, `scroll` rows with values 25/50/75/90 for the Google Ads page, ≥ 1 `engaged` row with `value > 0`, 1 `click` row with `target='whatsapp'`.
- [ ] **Step 4: Verify "storage blocked"**: `grep -n "localStorage\|sessionStorage" assets/js/site.js` and confirm each new call sits inside a `try { } catch { }`; `node --check assets/js/site.js` passes; `/` loads with no console errors (`read_console_messages`, errors only).
- [ ] **Step 5: Verify silencing**: `document.cookie = "sr_me=1; path=/"`, reload, browse 2 pages → no new events. Remove the cookie.
- [ ] **Step 6:** `python3 -I dev/sync-layout.py`, commit `git add assets/js/site.js && git commit -am "First-party tracker"`

### Task 4: Consent banner (Europe / UK / Switzerland)

**Files:**
- Modify: `assets/js/site.js` (banner built by JS, no HTML page edits), `assets/css/style.css` (plain CSS at the bottom, class prefix `consent-`)

**Interfaces:**
- Consumes: Task 3 `consent()`.
- Produces: banner shown when `consent() === "pending"`. Copy (exact): title "Can I count your visit?", body "I use cookies to see which pages help visitors and which ads bring enquiries. Nothing is shared or sold.", buttons "Accept" and "Decline", link "Privacy Policy" → `/privacy-policy/#cookies`. On answer: store `sr_consent`, push to `window.dataLayer` the arguments object of `gtag('consent', 'update', {ad_storage, ad_user_data, ad_personalization, analytics_storage})` with `granted` / `denied`, hide the banner, and on Accept create `sr_vid`/`sr_sid` and send a `page_view` with IDs. Test override: `localStorage.sr_region = "eu"` forces the European path (for previews).
- Banner is a fixed bottom bar, keyboard reachable, `role="dialog"` `aria-label="Cookie consent"`, no horizontal scroll at 360 px, does not cover the WhatsApp float button.

- [ ] **Step 1: Verify the failing state**: with `localStorage.sr_region="eu"` and storage cleared, reload `/` → no banner (not built yet).
- [ ] **Step 2: Implement** banner, consent update, override.
- [ ] **Step 3: Verify**: same setup → banner visible; before answering, `localStorage.sr_vid` is `null` and new events have null `visitor_id`; click Decline → banner gone, still no `sr_vid`, `dataLayer` holds the consent update with `denied`; clear, click Accept → `sr_vid` exists, next events carry it. Without the override (India time zone) → no banner, IDs set. Check at 360 px wide: no horizontal scroll. Remove `sr_region`.
- [ ] **Step 4:** `python3 -I dev/sync-layout.py`, commit `git commit -am "Consent banner for Europe, UK, Switzerland"`

### Task 5: Link visitor stories to leads

**Files:**
- Modify: `assets/js/site.js` (`postLead` sends `visitorId`; after a successful lead, `track('form_submit', {x: formName, lead: id})` then flush before redirect), `api/lead.php` (accept `visitorId` matching `/^[a-f0-9]{32}$/`, store it and `li_fat_id` from `attribution`, return `{"ok":true,"lead":<id>}` with the SQLite insert ID), `dev/tests/lead_test.php`

**Interfaces:**
- Consumes: Task 1 columns, Task 3 `track`, `visitorId`.
- Produces: `leads.visitor_id`, `leads.li_fat_id`; `events` row `form_submit` with `lead_id`.
- [ ] **Step 1: Write the failing test** `dev/tests/lead_test.php`: POSTs to `http://localhost:8091/api/lead.php` (preview running, no `api/config.php`, so no email is sent) a valid lead with `visitorId` = 32 hex chars and `attribution.li_fat_id = "abc"`; asserts the JSON has an integer `lead` and the row has that `visitor_id` and `li_fat_id`; a second POST with `visitorId:"bad"` stores `visitor_id` NULL and still returns `ok`. Prints `lead ok`.
- [ ] **Step 2: Run** `LEADS_DATA_DIR=$PWD/.data php dev/tests/lead_test.php` — expected FAIL (no `lead` in response).
- [ ] **Step 3: Implement.**
- [ ] **Step 4: Run** the test → `lead ok`. Browser check: send the consultation form on `/about/` with `fetch` left real (local, no email config) → thank-you page; SQLite has the lead with `visitor_id` equal to `localStorage.sr_vid` and a `form_submit` event with that `lead_id`. With `sr_me=1` set, sending a lead still works and creates no events.
- [ ] **Step 5:** sync-layout, delete test rows (`rm -rf .data`), commit `git commit -am "Leads carry the visitor ID; form_submit links the story"`

### Task 6: CRM in the panel

**Files:**
- Modify: `leadsforme/index.php` (becomes router + auth + layout), `api/leads-db.php` (status helper)
- Create: `leadsforme/views/leads.php`, `leadsforme/views/lead-new.php`, `leadsforme/.htaccess` rule denying direct `views/` access, `dev/tests/status_test.php`

**Interfaces:**
- Consumes: Task 1 columns and constants.
- Produces:
  - `lead_set_status(PDO $db, int $id, string $status, ?string $value, ?string $currency): ?string` — returns an error message or null; `won` requires a numeric value > 0 and a currency from `LEAD_CURRENCIES`; other statuses clear nothing but set `status_at`; unknown status → error.
  - `lead_add_manual(PDO $db, array $in): int` — required `name` and one of `phone`/`email`; `channel` one of `WhatsApp`, `Telegram`, `Phone call`, `LinkedIn DM`, `Referral`, `Other`; `form` = `manual`.
  - Panel routes: `?v=leads` (default), `?v=lead-new`, plus later views from Task 8. Lead row shows status select with a value box and currency select that apply on Save, and a "Story" link to `?v=visitor&id=<visitor_id>` when present.
- [ ] **Step 1: Write the failing test** `dev/tests/status_test.php`: `won` with value `''` → error "Enter the deal amount to mark this lead won."; `won` with `'abc'` → same error; `won` with `'50000'` + `INR` → null and row has value 50000, currency INR, `status_at` set; `qualified` → null; `'contacted'` → error; `lead_add_manual` without phone and email throws `InvalidArgumentException`. Prints `status ok`.
- [ ] **Step 2: Run** → FAIL.
- [ ] **Step 3: Implement** helpers, split the panel into router + views (keep login, CSRF, headers, CSV export; CSV gains the new columns), status form, manual lead form, the retention note text "Leads older than 90 days are deleted automatically unless marked won."
- [ ] **Step 4: Run** the test → `status ok`. Browser: open `http://localhost:8091/leadsforme/` (the panel's host rule lives in `.htaccess`, which `php -S` ignores), run the one-time setup with a local `PANEL_SETUP_CODE`, log in, add a manual WhatsApp lead, mark it won without an amount → message shown, status unchanged; with 50000 INR → saved.
- [ ] **Step 5:** commit `git commit -am "Panel CRM: statuses, deal value, manual leads"`

### Task 7: Report queries

**Files:**
- Create: `leadsforme/reports.php`, `dev/tests/reports_test.php`

**Interfaces:**
- Consumes: Task 1 tables; rollups from Task 9 for past days plus raw `events` for today (functions read both so they work before the first cron run).
- Produces (all `$from`, `$to` are `Y-m-d` in IST, inclusive):
  - `report_overview(PDO $db, string $from, string $to): array` → `['visitors'=>int,'sessions'=>int,'wa'=>int,'call'=>int,'form_start'=>int,'form_submit'=>int,'leads'=>int,'qualified'=>int,'won'=>int,'revenue'=>['INR'=>float,…],'by_channel'=>[['channel'=>…,'sessions'=>…,'leads'=>…,'won'=>…],…]]`
  - `report_pages(PDO $db, string $from, string $to): array` → rows `['path','views','visitors','avg_engaged_s','scroll50_pct','wa','call','form_start','form_submit','conv_pct']` sorted by views desc.
  - `report_page(PDO $db, string $path, string $from, string $to): array` → the page's row plus `'sources'` (channel → sessions landing or passing through), `'scroll'` (25/50/75/90 counts), `'clicks'` (target+label → count, top 20).
  - `report_visitors(PDO $db, string $from, string $to, int $page): array` → rows `['id','first_seen','last_seen','country','first_channel','sessions','pages','lead_id']`, 50 per page, newest first.
  - `report_visitor(PDO $db, string $id): array` → `['visitor'=>…, 'sessions'=>[['session'=>…, 'events'=>[…]]], 'leads'=>[…]]` with events in time order.
- [ ] **Step 1: Write the failing test** `dev/tests/reports_test.php` with a fixture: 2 visitors, 3 sessions (one Google Ads, two Direct), 7 page views over 2 pages, 1 WhatsApp click on `/services/google-ads/`, 2 form starts, 1 form submit linked to a lead marked won 50000 INR. Assert exact numbers: overview visitors 2, sessions 3, wa 1, form_start 2, form_submit 1, leads 1, won 1, revenue INR 50000; pages report row for `/services/google-ads/` has `wa` 1 and `conv_pct` 50.0 (1 submit / 2 visitors); visitor story for the lead's visitor lists its events in time order and its lead. Prints `reports ok`.
- [ ] **Step 2: Run** → FAIL.
- [ ] **Step 3: Implement.**
- [ ] **Step 4: Run** → `reports ok`.
- [ ] **Step 5:** commit `git add leadsforme/reports.php dev/tests/reports_test.php && git commit -m "Panel report queries"`

### Task 8: Report views

**Files:**
- Create: `leadsforme/views/overview.php`, `pages.php`, `page.php`, `visitors.php`, `visitor.php`
- Modify: `leadsforme/index.php` (nav: Overview, Leads, Pages, Visitors, Settings; date range picker with presets Today, 7 days, 30 days, 90 days, custom; default 30 days)

**Interfaces:**
- Consumes: Task 7 functions; Task 6 router.
- Produces: `?v=overview` (default after login), `?v=pages`, `?v=page&path=…`, `?v=visitors`, `?v=visitor&id=…`. Numbers use `tabular-nums`; bars are CSS widths (no JS, no external files); tables sit in `overflow-x:auto` wrappers so the panel works at 390 px.
- [ ] **Step 1:** load the Task 7 fixture into the local `.data` DB (`LEADS_DATA_DIR=$PWD/.data php dev/tests/reports_test.php --keep` — add a `--keep` flag to the test that leaves the fixture in place).
- [ ] **Step 2: Implement** the views.
- [ ] **Step 3: Verify in the browser** (logged in): overview shows the fixture numbers from Task 7; Pages lists both pages with the WhatsApp click on the Google Ads page; the page detail shows its scroll bars; Visitors lists 2 visitors; the story of the lead's visitor shows its sessions, events in order and the lead. At 390 px wide no page scrolls sideways. Screenshot the overview for Sushant.
- [ ] **Step 4:** `rm -rf .data`, commit `git commit -am "Panel reports: overview, pages, visitors, stories"`

### Task 9: Nightly cron, "this is me", Privacy Policy

**Files:**
- Create: `api/cron-daily.php`, `leadsforme/views/settings.php`, `dev/tests/cron_test.php`
- Modify: `privacy-policy/index.html`, `README.md` (cron line), `llms.txt` only if it quotes retention

**Interfaces:**
- Consumes: Task 1 tables, `leads_purge()`.
- Produces:
  - `rollup_day(PDO $db, string $day): void` — rebuilds `page_daily` and `channel_daily` rows for one IST day from `events`/`sessions` (idempotent: delete then insert).
  - `api/cron-daily.php`: CLI only (exit 1 when not `PHP_SAPI === 'cli'`); rolls up yesterday and the day before, then `leads_purge()`. README cron line: `php ~/domains/sushantrana.com/public_html/api/cron-daily.php` daily at 02:30 IST.
  - Settings view: "This is me" button sets cookie `sr_me=1; Domain=.sushantrana.com; Path=/; Max-Age=31536000; Secure; SameSite=Lax` (and a matching "Count me again" that clears it); shows the cron's last run time (from a file `cron-daily.last` in `leads_data_dir()`).
  - Privacy Policy: section 03 adds the site's own first-party analytics (visitor ID kept 90 days, what is recorded: pages, time, scroll, clicks, form start/send; no form contents; banner for EEA/UK/CH; "Decline" means anonymous counts only) with `id="cookies"`; section 07 changes "a maximum of three weeks" to "a maximum of 90 days"; "Last updated" set to the release date.
- [ ] **Step 1: Write the failing test** `dev/tests/cron_test.php`: fixture events on one day → `rollup_day` gives `page_daily` views and wa equal to raw counts; running it twice gives the same rows; `page_daily` has no visitor or session columns. Prints `cron ok`.
- [ ] **Step 2: Run** → FAIL. **Step 3: Implement** cron, settings, policy text. **Step 4: Run** `php dev/tests/cron_test.php` → `cron ok`; `php api/cron-daily.php` → exit 0; browser: Settings "This is me" sets the cookie (check on `localhost` with `Domain` omitted when the host is not under sushantrana.com); `python3 -I dev/build-llms-full.py`; `python3 -I dev/seo-audit.py` → 0 FAIL.
- [ ] **Step 5:** commit `git commit -am "Nightly rollups and retention, 'this is me', privacy policy"`

### Task 10: Whole-feature check

- [ ] **Step 1:** Run every test: `for t in dev/tests/*_test.php; do php $t || break; done` → each prints its `ok` line (start the preview first for `lead_test.php`).
- [ ] **Step 2:** Browser end to end on the preview: fresh storage → land on `/blog/…` → `/services/google-ads/` → send the Google Ads form → thank-you page. In the panel: the lead appears with its story (3 pages, scroll, the form start and submit), the Overview and Pages counts include it. With `localStorage.sr_region="eu"` repeat with Decline: lead still arrives, story has no visitor ID.
- [ ] **Step 3:** `python3 -I dev/seo-audit.py` → 0 FAIL; check `/` at 360 px for horizontal scroll with the banner shown.
- [ ] **Step 4:** Report to Sushant what changed and what he must do before deploy: add the Hostinger cron line; approve the Privacy Policy wording; deploy the thank-you/journey work first.
