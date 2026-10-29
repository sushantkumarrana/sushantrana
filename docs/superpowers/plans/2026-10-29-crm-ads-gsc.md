# CRM Plan 2: ad-platform signals, spend, Search Console, consent defaults

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** When Sushant marks a lead `qualified` or `won` in the panel, the ad platform that brought it (Google Ads, Meta, LinkedIn, ChatGPT Ads) is told, with the deal value on `won`; the panel shows each campaign's spend against its leads and revenue, Google Ads search terms, and each page's Search Console queries; Google tags respect the consent banner from the first page load.

**Architecture:** Status changes enqueue rows in a `signals` table (one per platform the lead has a click ID for). Meta, LinkedIn and ChatGPT signals are sent server-to-server right away and retried by the nightly cron; Google signals are pulled nightly by a Google Ads script that Sushant installs in his account, which also pushes spend, click → campaign/ad group/keyword mappings and search terms back to the panel. Search Console and Meta/LinkedIn spend are imported by the nightly cron with tokens kept in `api/config.php`. Every outbound HTTP call goes through one injectable function so tests never hit the network.

**Tech Stack:** PHP 8 + PDO SQLite + curl, plain JS, Google Ads Scripts (JavaScript in the Google Ads UI), Hostinger cron.

**Spec:** `docs/superpowers/specs/2026-10-28-crm-analytics-design.md` (Goals 1, 3, 6, 7; Constraints on platform limits, consent, Google APIs on the server). Plan 1: `docs/superpowers/plans/2026-10-28-crm-analytics-foundation.md` (done, live 29 Oct 2026).

## Global Constraints

- PHP 8 + SQLite + plain JS only, no new dependencies, no build step (AGENTS.md). All data in `leads.sqlite` under `leads_data_dir()`.
- Secrets only in `api/config.php` (git-ignored); `api/config.sample.php` lists every new key with an empty value and a one-line comment.
- A signal is created only for status `qualified` or `won`, only when the lead carries that platform's click ID (`gclid`/`gbraid`/`wbraid` → Google, `fbclid` → Meta, `li_fat_id` → LinkedIn, `oppref` → ChatGPT Ads). `wrong`, `new`, `lost` create nothing. Changing a lead to the same status again creates nothing new.
- Event names on every platform: `Qualified lead` (no value) and `Won deal` (value + currency from the lead).
- Email and phone go to a platform only as SHA-256 of the normalised value (email: trimmed lowercase; phone: digits only with country code), never in clear text, and only to the platform that brought that lead.
- Platform windows: Google 90 days after the click, Meta `event_time` ≤ 7 days old (send at status change, `action_source: "system_generated"`), LinkedIn and ChatGPT sent at status change. A signal still unsent after its window is marked `expired`, not retried.
- Nothing outbound runs when its config keys are empty: the code records `skipped: not configured` and the panel shows it.
- Panel keeps its login, CSRF, CSP `default-src 'none'`, no JavaScript. Machine endpoints (`api/ads-google.php`) authenticate with a long random key from config compared with `hash_equals`, and answer 403 without it.
- After changing `assets/js/site.js`, `assets/css/style.css` or anything stamped into pages: `python3 -I dev/sync-layout.py`. Before handing back: every `dev/tests/*` passes and `python3 -I dev/seo-audit.py` ends with 0 FAIL. Commit locally per task; never push without Sushant's go-ahead.

## Review Focus

1. A lead marked `won`, then `qualified`, then `won` again: each platform gets one `Won deal` (latest value), never two. → Task 2 test.
2. A platform answering 4xx (bad token) or timing out: the panel save still succeeds, the error is shown on the lead, nothing throws. → Task 3 test (fake HTTP returning 400 and throwing).
3. The Google Ads script calling `api/ads-google.php` with a wrong key, a GET instead of POST, or a 5 MB body: 403 / 405 / 413, nothing stored. → Task 6 test.
4. The nightly cron with every integration unconfigured: finishes, writes `cron-daily.last`, logs "not configured" per integration. → Task 9 test.
5. A returning European visitor who declined earlier: on the first page load Google tags are already in `denied` before GTM loads. → Task 11 browser check.

---

### Task 1: Click IDs and channels for every ad platform

**Files:** Modify `assets/js/site.js` (`ATTR_PARAMS` gains `oppref`), `api/lead.php` (attribution keys gain `oppref`, `gbraid`, `wbraid`; stored), `api/leads-db.php` (columns `oppref`, `gbraid`, `wbraid` on `leads`; `lead_channel` rules), `api/track.php` (no change needed beyond `lead_channel`).

**Interfaces:**
- Produces: `lead_channel()` returns `LinkedIn Ads` when `li_fat_id` is set or `utm_source` matches `linkedin` with a paid medium; `ChatGPT Ads` when `oppref` is set; existing results unchanged otherwise. Leads table columns `oppref TEXT, gbraid TEXT, wbraid TEXT` (migration like Plan 1).
- [ ] **Step 1:** add self-check cases to `api/leads-db.php`: `['li_fat_id'=>'x'] → 'LinkedIn Ads'`, `['utm_source'=>'linkedin','utm_medium'=>'paid'] → 'LinkedIn Ads'`, `['oppref'=>'x'] → 'ChatGPT Ads'`, `['referrer'=>'https://chatgpt.com/'] → 'AI assistant'` (unchanged). Extend `dev/tests/db_test.php` to assert the three new columns. Run `php api/leads-db.php` → FAIL.
- [ ] **Step 2:** implement; run `php api/leads-db.php && php dev/tests/db_test.php` → `lead_channel ok`, `db ok`; `LEADS_DATA_DIR=$PWD/.data php dev/tests/lead_test.php` (preview running) extended to post `attribution.oppref = "op1"` and assert it is stored.
- [ ] **Step 3:** sync-layout, commit "Capture ChatGPT and LinkedIn click IDs; channels for every ad platform".

### Task 2: Signals queue

**Files:** Create `api/signals.php`, `dev/tests/signals_test.php`; modify `api/leads-db.php` (`lead_set_status` calls `signal_enqueue` after a successful update).

**Interfaces:**
- Table `signals(id INTEGER PRIMARY KEY, lead_id INT, platform TEXT, event TEXT, value REAL, currency TEXT, created_at TEXT, sent_at TEXT, state TEXT, detail TEXT, tries INT DEFAULT 0, UNIQUE(lead_id, platform, event))` — `state` ∈ `pending`, `sent`, `failed`, `expired`, `skipped`.
- `signal_platforms(array $lead): array` → subset of `['google', 'meta', 'linkedin', 'chatgpt']` from the click IDs.
- `signal_enqueue(PDO $db, int $leadId): int` — reads the lead; for `qualified` → event `Qualified lead`; for `won` → event `Won deal` with value/currency; upserts one row per platform (`ON CONFLICT(lead_id, platform, event) DO UPDATE SET value, currency, state='pending', tries=0` only if value changed or state is `failed`); returns rows created or changed. Other statuses → 0.
- [ ] **Step 1: failing test** `signals_test.php`: lead with gclid + fbclid marked qualified → 2 rows (`google`,`meta`, `Qualified lead`); marked won 50000 INR → 2 more (`Won deal`, value 50000); won again with same value → 0 changes; won with 60000 → 2 rows updated to 60000 and `pending`; lead with no click IDs → 0; `wrong` → 0. Prints `signals ok`.
- [ ] **Step 2:** run → FAIL. **Step 3:** implement. **Step 4:** run → `signals ok`; `php dev/tests/status_test.php` still `status ok`.
- [ ] **Step 5:** commit "Signals queue for qualified and won leads".

### Task 3: Meta Conversions API

**Files:** Create `api/meta.php`, `dev/tests/meta_test.php`; modify `api/config.sample.php` (`META_DATASET_ID`, `META_ACCESS_TOKEN`, `META_AD_ACCOUNT_ID`), `api/signals.php` (`http_post_json` helper).

**Interfaces:**
- `http_post_json(string $url, array $headers, array $body, int $timeout = 10): array` → `['code' => int, 'body' => string]`; on curl failure `code` 0 and `body` the error. Tests replace it through `signals_send(PDO $db, array $cfg, ?callable $http = null)`.
- `meta_payload(array $signal, array $lead, int $now): array` → Graph API body: `data[0]` with `event_name` (`Qualified lead` / `Won deal`), `event_time` = `$now`, `action_source` `system_generated`, `event_id` = `"sr-{lead_id}-{event slug}"`, `user_data.em`/`ph` SHA-256 arrays, `user_data.fbc` = `fb.1.{created_at ms}.{fbclid}`, `custom_data.lead_event_source` `sushantrana-panel`, and for `Won deal` `custom_data.value` + `currency`.
- `leadsforme/index.php` calls `signals_send($db, $config)` right after a successful status save (5 s timeout per call), so Meta, LinkedIn and ChatGPT hear at the moment the status changes; any failure is recorded on the signal and never blocks the save or the redirect. Google signals wait for the script (Task 6).
- `signals_send(PDO $db, array $cfg, ?callable $http = null): array` — sends every `pending`/`failed` (tries < 5) signal for configured platforms except `google`: Meta POST `https://graph.facebook.com/v21.0/{META_DATASET_ID}/events?access_token=…`; 2xx → `sent`; else `failed` with the response's message in `detail`; Meta signals whose lead status changed more than 7 days ago → `expired`. Returns counts per state.
- [ ] **Step 1: failing test** `meta_test.php`: payload hashes `Me@Example.com ` to `sha256("me@example.com")` and `+91 98765-43210` to `sha256("919876543210")`; `fbc` format; `Won deal` carries value/currency, `Qualified lead` none; fake HTTP 200 → state `sent`; fake 400 `{"error":{"message":"Invalid token"}}` → `failed`, detail "Invalid token", `lead_set_status` already returned null (save not blocked); fake that throws → `failed`, no exception escapes; empty `META_DATASET_ID` → `skipped`, detail `not configured`. Prints `meta ok`.
- [ ] **Step 2–4:** RED, implement, GREEN.
- [ ] **Step 5:** commit "Meta Conversions API for qualified and won leads".

### Task 4: LinkedIn Conversions API

**Files:** Create `api/linkedin.php`, `dev/tests/linkedin_test.php`; config keys `LINKEDIN_ACCESS_TOKEN`, `LINKEDIN_AD_ACCOUNT_ID`, `LINKEDIN_CONVERSION_QUALIFIED`, `LINKEDIN_CONVERSION_WON` (rule IDs), `LINKEDIN_VERSION` (default `202603`, set to LinkedIn's current version when building).

**Interfaces:**
- `linkedin_payload(array $signal, array $lead, int $nowMs): array` → body for `POST https://api.linkedin.com/rest/conversionEvents`: `conversion` = `urn:lla:llaPartnerConversion:{rule id}`, `conversionHappenedAt` = `$nowMs`, `user.userIds` = `[{idType: SHA256_EMAIL, idValue}, {idType: LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID, idValue: li_fat_id}]`, `eventId` = `sr-{lead_id}-{slug}`, `conversionValue {currencyCode, amount}` only for `Won deal` (amount as a string).
- Headers: `Authorization: Bearer …`, `LinkedIn-Version: {LINKEDIN_VERSION}`, `X-Restli-Protocol-Version: 2.0.0`. Wired into `signals_send`.
- [ ] **Steps:** failing test (payload shape, headers, 201 → sent, 401 → failed with message, unconfigured → skipped) → implement → `linkedin ok` → commit "LinkedIn Conversions API".

### Task 5: ChatGPT Ads Conversions API

**Files:** Create `api/chatgpt-ads.php`, `dev/tests/chatgpt_test.php`; config keys `OPENAI_ADS_PIXEL_ID`, `OPENAI_ADS_CONVERSIONS_KEY`.

**Interfaces:**
- `chatgpt_payload(array $signal, array $lead, int $now): array` → `{events: [{event_name, event_id: "sr-{lead_id}-{slug}", event_time: $now, oppref, user_data: {em: sha256}, value?, currency?}]}` for `POST https://bzr.openai.com/v1/events?pid={OPENAI_ADS_PIXEL_ID}` with `Authorization: Bearer {OPENAI_ADS_CONVERSIONS_KEY}`. Before building, check OpenAI's Ads developer docs (developers.openai.com/ads) for the exact field names and adjust the test to them; ledger the result.
- [ ] **Steps:** failing test (payload, 2xx → sent, unconfigured → skipped) → implement → `chatgpt ok` → commit "ChatGPT Ads Conversions API".

### Task 6: Google Ads exchange endpoint and script

**Files:** Create `api/ads-google.php`, `api/ads-store.php` (storage functions), `dev/google-ads-script.js` (pasted by Sushant into Google Ads → Tools → Scripts), `dev/tests/ads_google_test.php`; config `GOOGLE_ADS_SCRIPT_KEY` (64 hex chars); tables `ad_spend(day, platform, campaign, ad_group, cost REAL, clicks INT, impressions INT, currency TEXT, PRIMARY KEY(day, platform, campaign, ad_group))`, `ad_clicks(click_id TEXT PRIMARY KEY, platform TEXT, day TEXT, campaign TEXT, ad_group TEXT, keyword TEXT)`, `search_terms(day, campaign, ad_group, term, clicks INT, cost REAL, conversions REAL, PRIMARY KEY(day, campaign, ad_group, term))`.

**Interfaces:**
- `POST api/ads-google.php?a=pull` (header `X-Key`) → JSON `{conversions: [{gclid|gbraid|wbraid, name, time: "Y-m-d H:i:s+0530", value, currency, id}]}` for Google signals `pending`/`failed` and click ≤ 90 days old (older → `expired`).
- `POST api/ads-google.php?a=ack` body `{sent: [id…], failed: [{id, error}]}` → updates states.
- `POST api/ads-google.php?a=push` body `{spend: […], clicks: […], terms: […]}` → `ads_store_spend/clicks/terms(PDO, array): int` upserts; then `ads_backfill_leads(PDO): int` copies campaign/ad group/keyword from `ad_clicks` onto leads with that gclid where empty.
- Limits: POST only (405), body ≤ 2 MB (413), key mismatch or empty config key → 403, invalid JSON → 400.
- Script (`dev/google-ads-script.js`): `main()` → pull, upload via `AdsApp.bulkUploads().newCsvUpload(['Google Click ID','Conversion Name','Conversion Time','Conversion Value','Conversion Currency'], {moneyInMicros: false, timeZone: 'Asia/Kolkata'}).forOfflineConversions()`, `apply()`, ack; then GAQL reports for yesterday (`campaign`/`ad_group` metrics, `click_view` for yesterday, `search_term_view` for the last 7 days) and push. Constants at the top: `PANEL_URL`, `KEY`. The two conversion actions ("Qualified lead", "Won deal", source "Import from clicks") are created by Sushant in Google Ads.
- [ ] **Step 1: failing test** `ads_google_test.php` (functions called directly, plus the endpoint over HTTP on the preview): wrong key → 403; GET → 405; 3 MB → 413; push of 2 spend rows twice → 2 rows; push of a click for a lead's gclid → lead gets campaign/ad group/keyword; pull lists a pending Google `Won deal` with value and IST time; a 91-day-old click → `expired`, not listed; ack moves states. Prints `ads google ok`.
- [ ] **Steps 2–4:** RED, implement, GREEN; `node --check dev/google-ads-script.js`.
- [ ] **Step 5:** commit "Google Ads exchange endpoint and script".

### Task 7: Meta and LinkedIn spend import

**Files:** Modify `api/meta.php` (`meta_import_spend(PDO, array $cfg, string $day, ?callable $http): int` via `GET /v21.0/act_{id}/insights?level=adset&time_range=…&fields=campaign_name,adset_name,spend,clicks,impressions,account_currency`), `api/linkedin.php` (`linkedin_import_spend(...)` via `adAnalytics` finder, pivot CAMPAIGN), add `http_get_json` beside `http_post_json`; tests extend `meta_test.php` / `linkedin_test.php` with fake responses → rows in `ad_spend` with platform `meta` / `linkedin`; unconfigured → 0 and no call.
- [ ] **Steps:** RED → implement → GREEN → commit "Meta and LinkedIn spend import".

### Task 8: Search Console import

**Files:** Create `api/google-oauth.php`, `api/gsc.php`, `dev/tests/gsc_test.php`; config `GOOGLE_OAUTH_CLIENT_ID`, `GOOGLE_OAUTH_CLIENT_SECRET`, `GOOGLE_OAUTH_REFRESH_TOKEN`, `GSC_SITE` (default `sc-domain:sushantrana.com`); table `gsc_daily(day, page, query, clicks INT, impressions INT, position REAL, PRIMARY KEY(day, page, query))`.

**Interfaces:**
- `google_access_token(array $cfg, ?callable $http): ?string` — POST `https://oauth2.googleapis.com/token` (`grant_type=refresh_token`); caches the token in `leads_data_dir()/google-token.json` until 60 s before expiry; returns null and logs `invalid_grant` details on failure (the Workspace re-login case).
- `gsc_import(PDO, array $cfg, string $from, string $to, ?callable $http): int` — `searchAnalytics/query` with dimensions `date,page,query`, rowLimit 25000, paged with `startRow`; stores page as a path (`/services/google-ads/`).
- `report_page()` (Plan 1, `leadsforme/reports.php`) gains `'gsc' => [['query','clicks','impressions','position'],…]` top 20 for the range.
- [ ] **Steps:** failing test (token refresh and cache, `invalid_grant` → null, paged import of 3 fake rows, URL → path, report_page returns them) → implement → `gsc ok` → commit "Search Console import".

### Task 9: Nightly cron wiring and integration status

**Files:** Modify `api/cron-daily.php` (after rollups: `signals_send`, `meta_import_spend` and `linkedin_import_spend` for yesterday, `gsc_import` for the last 4 days; each in its own try/catch; a status line per integration written to `leads_data_dir()/integrations.json`), `leadsforme/views/settings.php` (table: integration, configured yes/no, last result, last run).
- [ ] **Step 1: failing test** in `cron_test.php`: with an empty config the cron functions run, return, and `integrations.json` holds `not configured` for google_oauth, meta, linkedin, chatgpt, google_ads_script (last pull time). **Steps 2–4:** RED, implement, GREEN. **Step 5:** commit "Cron runs signals and imports; Settings shows integration status".

### Task 10: Campaigns report and lead signal log

**Files:** Modify `leadsforme/reports.php` (`report_campaigns(PDO, string $from, string $to): array` → rows `platform, campaign, cost, currency, clicks, leads, qualified, won, revenue, cpl, cost_per_won, roas`, matching leads to spend by platform + `utm_campaign`/Google campaign name; `report_terms(PDO, from, to): array` top 100 terms), create `leadsforme/views/campaigns.php`, add "Campaigns" to the nav, lead detail shows its signals (platform, event, state, detail, sent_at), page detail shows the GSC table.
- [ ] **Step 1: failing test** `reports_test.php` gains a fixture: Google campaign "Search IN" spend ₹10,000, 2 leads (1 won ₹50,000) → cpl 5000, cost_per_won 10000, roas 5.0; Meta campaign with spend and no leads → leads 0, cpl null. **Steps 2–4:** RED, implement, GREEN; browser check of `?v=campaigns` at 1280 and 390 px with the fixture (`--keep`). **Step 5:** commit "Campaigns report, search terms, signal log".

### Task 11: Consent Mode defaults before GTM

**Files:** Create `includes/consent-default.html` (one inline `<script data-consent-default>`), modify `dev/sync-layout.py` (insert or replace that script immediately before the GTM `<script>` in `<head>`), `privacy-policy/index.html` (restore "and Google tags are told not to use cookies" in the banner bullet), `dev/seo-audit.py` only if it flags the new script.

**Interfaces:**
- The snippet defines `window.dataLayer`, a `gtag` shim, and pushes `gtag('consent','default',{ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',analytics_storage:'denied',wait_for_update:500,region:[EEA + GB + CH ISO codes]})`; then reads `localStorage.sr_consent` (try/catch) and, if set, pushes `gtag('consent','update', …)` with that answer, so returning visitors are correct before GTM loads. Region list: AT BE BG HR CY CZ DK EE FI FR DE GR HU IE IT LV LT LU MT NL PL PT RO SK SI ES SE IS LI NO GB CH.
- [ ] **Step 1: failing check:** `grep -c 'data-consent-default' index.html` → 0. **Step 2:** implement and run `python3 -I dev/sync-layout.py`; every page with GTM has exactly one snippet, placed before GTM (`python3 -I` one-liner asserting order on all pages). **Step 3:** browser: with `localStorage.sr_consent='denied'` and `sr_region='eu'`, reload `/` → `dataLayer` holds the default and the denied update before the `gtm.js` event; seo-audit 0 FAIL. **Step 4:** commit "Consent Mode defaults before GTM".

### Task 12: Whole check and Sushant's setup list

- [ ] Run every `dev/tests/*_test.php` and `node dev/tests/consent_zone_test.js`; seo-audit 0 FAIL.
- [ ] Browser on the preview: mark a fixture lead with gclid + fbclid `won` → panel shows two signals (Google `pending`, Meta `skipped: not configured` locally); Settings shows every integration "not configured"; Campaigns page renders.
- [ ] Final whole-branch review as in Plan 1, then hand Sushant the setup list: Google Ads conversion actions + script + `GOOGLE_ADS_SCRIPT_KEY`; Meta dataset + system-user token + ad account; LinkedIn developer app approval + token + conversion rules; ChatGPT Ads pixel + conversions key; Google OAuth refresh token for GSC (and the Workspace session-control exemption); the URL tracking templates on Meta/LinkedIn/ChatGPT ads (`utm_source`, `utm_medium=paid`, `utm_campaign={{campaign.name}}`, `utm_content={{adset.name}}`).
