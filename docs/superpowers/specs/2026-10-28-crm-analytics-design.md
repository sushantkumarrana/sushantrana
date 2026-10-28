# Lead CRM + first-party analytics for sushantrana.com — design

Status: draft for Sushant's approval (28 Oct 2026). Approach A, chosen by Sushant.

## Intent

One private place, the existing panel at `leadsforme.sushantrana.com`, where Sushant sees every lead and every visitor's story, and from which the ad platforms learn which leads were good. Today leads arrive by email and sit in a small panel with no link to what the visitor did, GA4 records 0 key events, and no ad platform is told which leads turned into money. The point is to know which pages, campaigns and keywords bring leads that close, and to feed that back so the ads find more of them.

Only for sushantrana.com. Used mostly on a laptop; it must still work on a phone a few days a month.

## Goals

1. **CRM.** Every lead in one table: name, phone, email, business, form answers, then source, medium, campaign, ad group, keyword (or Meta ad set / ad), click IDs, landing page, journey, linked visitor story, lead score. Leads from WhatsApp, Telegram, phone, LinkedIn DMs and referrals are added by hand with their source.
2. **Status and value.** Statuses `new`, `qualified` (Sushant's "OK"), `wrong`, `won`, `lost`. `won` asks for the deal amount and currency, entered when the deal closes.
3. **Signals back to the ads.** When a lead from an ad becomes `qualified` or `won`, the panel sends a "Qualified lead" or "Won deal" (with value) conversion to the platform that brought it: Google Ads, Meta (Facebook + Instagram), LinkedIn, ChatGPT Ads. `wrong` sends nothing.
4. **Visitor stories.** Each visitor gets a browser ID kept 90 days, so all visits of one person join into one story: pages in order, time and scroll on each, every click (WhatsApp, call, email, CTA buttons, outbound links), form started, form sent. When they send a form, the story attaches to the lead.
5. **Site dashboard.** For any date range: visitors, sessions, WhatsApp clicks, call clicks, form starts, forms sent, leads, qualified, won, revenue, split by channel.
6. **Per-page report.** For every page (35, 50 or more): visitors, where they came from, average engaged time, scroll depth, WhatsApp / call clicks from that page, form starts and sends, conversion rate, plus the Search Console queries, impressions, clicks and position for that page.
7. **Campaign report.** Spend per campaign (and ad group / ad set) from Google Ads, Meta and LinkedIn next to leads, qualified, won and revenue from the CRM: cost per lead, cost per won deal, ROAS. Google Ads search terms per ad group as an aggregated table.
8. **Lead score.** Each lead marked hot / warm / cold from what the visitor did before sending the form.
9. **Weekly email.** Every Monday morning (IST): last week's visitors, leads, qualified, won, revenue, spend, top pages and campaigns.
10. **Clean numbers.** Bots and Sushant's own visits do not count.

## Non-goals (v1)

- Session recordings and heatmaps. Microsoft Clarity can be added later for free.
- More than one website, client access, or a mobile app.
- Replacing GA4 or GTM. They stay; the panel's numbers should roughly agree with GA4.
- Search term per individual lead. Google does not expose it per click; v1 shows search terms per ad group instead.

## Anti-goals (would be a failure even if it works)

- The site gets slower. The tracker must be small, send with `navigator.sendBeacon`, and never block rendering.
- Visitors in Europe, the UK or Switzerland are tracked before they agree.
- A `wrong` lead, or a lead with no click ID for that platform, is ever sent as a conversion.
- Names, emails or phone numbers end up in analytics events, GA4 or the dataLayer analytics payloads. Hashed email/phone go only to the ad platform that brought that lead.
- Leads or stories leak: the panel stays behind its login, the data stays outside `public_html`.

## Constraints

- Hostinger shared hosting: PHP 8 + SQLite (the existing `api/leads-db.php` database outside `public_html`), cron jobs available, no Node, no build step (AGENTS.md).
- Site code is plain HTML/CSS/JS; tracking lives in `assets/js/site.js`, run `dev/sync-layout.py` after changing it.
- Traffic is small today (~230 sessions in 90 days), so SQLite is enough; design for up to ~50k events a day without changes.
- Retention (Sushant's decision): leads 90 days, `won` leads kept forever; visitor stories and raw events 90 days. Daily totals without IDs may be kept longer. Privacy Policy and `LEADS_RETENTION_DAYS` change from 21 days to 90.
- Consent (Sushant's decision): a banner only for visitors in the EEA, UK and Switzerland. They are tracked with an ID only after "Accept"; on "Decline" only anonymous counts are recorded. The banner also sets Google Consent Mode v2 for those visitors. Everyone else gets no banner; the Privacy Policy explains what is recorded. (Not legal advice; India's DPDP rules are still coming into force.)
- Platform limits (checked 28 Oct 2026, verify again when building):
  - Google Ads accepts offline conversions up to 90 days after the click. gclid / gbraid / wbraid are already captured in `sr_attr`.
  - Meta Conversions API: `event_time` at most 7 days in the past, so send at the moment the status changes. Match on `fbc` (from fbclid, already captured) plus hashed email and phone.
  - LinkedIn Conversions API needs `li_fat_id` (captured from the URL, not stored today) plus hashed email; its first-party cookie lasts about 7 days, so read it from the landing URL. Needs a LinkedIn developer app with Conversions API access, approved by LinkedIn.
  - ChatGPT Ads has a pixel and a Conversions API; offline/CRM uploads are invite-only (LiveRamp / OpenAI rep). v1 captures its click ID and UTMs and sends server events if Sushant gets access; otherwise the pixel alone.
- Google APIs on the server: service-account keys are blocked by the sushantrana.com org policy, so cron jobs use Sushant's own OAuth client ("Claude GSC", project `sushantrana-gsc`) with a stored refresh token. The Workspace forced a re-login (`invalid_rapt`) on 28 Oct; Sushant must exempt this internal app from Google Cloud session control in Workspace Admin, or the nightly jobs will stop every time it expires.

## Approaches considered

| | Approach | Trade-off |
|---|---|---|
| **A (chosen)** | Grow the existing `leadsforme` PHP + SQLite panel into the CRM; the site records its own events; cron jobs exchange data with GSC and the ad platforms. | Most to build. Everything in one place, visitor stories join leads directly, no monthly fee, fits the current stack and login. |
| B | Off-the-shelf: GoHighLevel or HubSpot for the CRM, Clarity or PostHog for analytics. | Fast, mature, recordings for free. Data split across tools, stories not joined to leads, weak LinkedIn / ChatGPT signals, ~$97/month for GoHighLevel. |
| C | Own CRM + self-hosted Matomo for tracking. | Ready visitor log and consent. Heavy on shared hosting, needs MySQL, two systems to keep in sync. |

Sushant picked A because the needs are specific (stories tied to leads, WhatsApp and call clicks, won deals sent back to four ad platforms) and the traffic is small.

## How it works (decided)

### Recording what visitors do
- `site.js` gives each visitor a random ID (`sr_vid`, localStorage, 90 days) and a session ID (new after 30 minutes idle). It reuses the existing `sr_attr` (first-touch source, 90 days) and `sr_journey`.
- Events: `page_view`, `scroll` (25/50/75/90%), `engaged_time` (sent on `pagehide`/`visibilitychange`), `click` (tel:, wa.me / WhatsApp, mailto:, CTA buttons, outbound links, with the link text and target), `form_start` (first input in a form), `form_submit` (with the lead ID returned by `api/lead.php`).
- Sent in small batches to a new endpoint `api/t.php` with `sendBeacon`. The endpoint validates and caps the payload, drops known bots, rate-limits by IP, stores no IP address (country only, from the request), and never stores form contents.
- New capture: `li_fat_id` and any ChatGPT Ads click ID from the landing URL go into `sr_attr`, and `api/lead.php` stores them.
- Sushant's own visits: a "this is me" switch in the panel sets a cookie that makes the tracker stay silent on that browser.

### Consent
- The tracker decides "EEA / UK / Switzerland" from the browser time zone (`Europe/*`, plus the UK and Swiss zones) with no network call, and shows a small banner there. Before an answer, and after "Decline", it sends anonymous counts only (page views, clicks) with no visitor or session ID.
- The banner also drives Google Consent Mode v2 through the dataLayer, so GA4, Google Ads and the Meta pixel respect the same answer.

### CRM
- The existing `leads` table gains: visitor ID, status (new/qualified/wrong/won/lost), deal value and currency, lead score, Meta ad set / ad, LinkedIn and ChatGPT click IDs, Google ad group and keyword, and a log of which conversions were sent where and when.
- Google campaign / ad group / keyword come two ways: ValueTrack parameters in the Google Ads tracking template, and the nightly Google Ads script's `click_view` lookup by gclid. Meta, LinkedIn and ChatGPT use URL parameter templates (`utm_campaign={{campaign.name}}` etc.) that Sushant sets once in each ad account.
- Manual leads: a form in the panel with source (WhatsApp, Telegram, phone, LinkedIn DM, referral, other), same statuses.
- The lead row opens to the full visitor story timeline.

### Signals back to the ads
- **Google Ads:** a Google Ads script that Sushant installs once in the account runs nightly. It pulls `qualified` and `won` conversions from a secret panel URL and uploads them as offline conversions (by gclid / gbraid / wbraid), pushes campaign / ad group / keyword spend and the gclid → campaign / ad group / keyword mapping back to the panel, and pushes ad-group search terms. No Google Ads API developer token is needed.
- **Meta:** Conversions API call from PHP at the moment the status changes (`action_source: system_generated`), with dataset ID and system-user token in `api/config.php`. Spend from the Marketing API nightly.
- **LinkedIn:** Conversions API call at status change. Spend from the Marketing API nightly, once LinkedIn approves API access.
- **ChatGPT Ads:** Conversions API at status change if access is granted; until then the pixel on the thank-you pages only.
- Each send is logged with its result. Failed sends retry nightly while still inside the platform's window, and the lead shows the error.

### Reports in the panel
- Overview, Pages, Page detail, Visitors (list + story), Leads (CRM), Campaigns, Settings (integrations, "this is me", exports).
- Search Console page × query data imported nightly for the last 3 days (GSC data lags 2–3 days) with the stored OAuth refresh token.
- Daily rollup tables so the reports stay fast; raw events purged after 90 days.
- Weekly email via the existing Resend setup, Monday 09:00 IST, from a cron job.
- The panel works on laptop first, and its tables scroll sideways on a phone instead of breaking.

## Calls made in writing this (Sushant to check)

- Added a `lost` status (qualified but did not buy) next to Sushant's OK / wrong / won. Today's `contacted` leads become `new`.
- Deal value has a currency picker (INR default, AED, USD, others), because clients pay in several currencies and every platform needs the currency.
- "Qualified lead" is sent with no value; only "Won deal" carries the amount.
- WhatsApp and call clicks are counted and shown in the visitor story, but are not leads until Sushant adds them by hand, since a click carries no name or number.
- EEA / UK / Switzerland is detected from the browser time zone. A few non-EU `Europe/*` zones (Türkiye, Russia) will also see the banner; that errs on the safe side.

## Left to the builder

- Exact SQLite schema, indexes and rollup tables.
- Lead score rules and thresholds (start simple: pages viewed, service and pricing pages seen, engaged time, return visits; tunable in Settings).
- Charting: a small self-hosted library or plain SVG. The panel's CSP is `default-src 'none'`, so nothing loads from a CDN.
- Panel layout and navigation, keeping the current login, CSRF and security headers.
- Order of the work. Suggested: tracker + `t.php` + tables → CRM fields and statuses → reports → consent banner + Privacy Policy → Google Ads script → Meta → LinkedIn → ChatGPT → lead score → weekly email.

## Sushant's one-time setup (outside the code)

1. Deploy the pending thank-you / journey changes first; this design builds on them.
2. Workspace Admin: exempt the "Claude GSC" OAuth app from Google Cloud session control.
3. Google Ads: add the ValueTrack tracking template and install the script the builder provides.
4. Meta: create a Conversions API dataset and a system-user token; set URL parameters on all ads.
5. LinkedIn: create a developer app and apply for Conversions API / Advertising API access; set UTM templates.
6. ChatGPT Ads: create the pixel and a Conversions key in Ads Manager; ask OpenAI for offline conversions access.
7. Approve the updated Privacy Policy text (90-day retention, what is recorded, the banner).
