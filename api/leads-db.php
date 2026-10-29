<?php
/**
 * The leads store behind the panel at leadsforme.sushantrana.com.
 *
 * A SQLite file OUTSIDE public_html, so it can never be downloaded:
 *   live:  /home/<user>/leads-data/leads.sqlite
 *   local: <repo>/.data/leads.sqlite (git-ignored)
 * lead.php writes here; leadsforme/ reads it. Both live on the same hosting
 * account, so they share the file without any keys.
 */

declare(strict_types=1);

// Privacy Policy promises deletion within 90 days. Change the policy page
// too if you change this. 'won' leads are kept; visitor stories go too.
const LEADS_RETENTION_DAYS = 90;
const LEAD_STATUSES = ['new', 'qualified', 'wrong', 'won', 'lost'];
const LEAD_CURRENCIES = ['INR', 'AED', 'USD', 'EUR', 'GBP', 'CAD', 'CHF'];

function leads_data_dir(): string
{
    if ($env = getenv('LEADS_DATA_DIR')) return $env;  // dev/tests
    $parts = explode('/domains/', __DIR__, 2);
    $dir = count($parts) === 2 ? $parts[0] . '/leads-data' : dirname(__DIR__) . '/.data';
    if (!is_dir($dir)) mkdir($dir, 0700, true);
    return $dir;
}

function leads_db(): PDO
{
    static $db = null;
    if ($db) return $db;
    $db = new PDO('sqlite:' . leads_data_dir() . '/leads.sqlite', null, null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
    $db->exec('PRAGMA busy_timeout = 5000');
    $db->exec(<<<SQL
        CREATE TABLE IF NOT EXISTS leads (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at   TEXT NOT NULL,              -- UTC, ISO 8601
            form         TEXT,                       -- consultation | shopify_store_development | website_maintenance
            name         TEXT NOT NULL,
            email        TEXT NOT NULL,
            phone        TEXT NOT NULL,
            business     TEXT,
            service      TEXT,
            enquiry_type TEXT,
            message      TEXT,
            page         TEXT,                       -- page the form was sent from
            landing_page TEXT,                       -- first page of the visit
            journey      TEXT,                       -- every page of the visit, in order ("/ > /services/ > …")
            visitor_id   TEXT,                       -- links the visitor's story (events)
            value REAL, currency TEXT,               -- deal amount, set when won
            li_fat_id    TEXT, ad_group TEXT, keyword TEXT,
            status_at    TEXT,                       -- UTC, last status change
            referrer     TEXT,                       -- site that sent the visitor
            channel      TEXT,                       -- Google Ads, Facebook Ads, Organic search …
            utm_source   TEXT, utm_medium TEXT, utm_campaign TEXT, utm_term TEXT, utm_content TEXT,
            gclid        TEXT, fbclid TEXT,
            user_agent   TEXT,
            status       TEXT NOT NULL DEFAULT 'new'
        );
        CREATE INDEX IF NOT EXISTS leads_created_at ON leads (created_at DESC);
        SQL);
    // databases made before these columns existed
    $have = array_column($db->query('PRAGMA table_info(leads)')->fetchAll(), 'name');
    foreach (['journey' => 'TEXT', 'visitor_id' => 'TEXT', 'value' => 'REAL', 'currency' => 'TEXT', 'li_fat_id' => 'TEXT',
              'status_at' => 'TEXT', 'ad_group' => 'TEXT', 'keyword' => 'TEXT',
              'oppref' => 'TEXT', 'gbraid' => 'TEXT', 'wbraid' => 'TEXT'] as $col => $type) {
        if (!in_array($col, $have, true)) $db->exec("ALTER TABLE leads ADD COLUMN $col $type");
    }
    $db->exec("UPDATE leads SET status = 'new' WHERE status = 'contacted'");
    $db->exec(<<<SQL
        CREATE INDEX IF NOT EXISTS leads_visitor ON leads (visitor_id);
        -- the site's own analytics (api/t.php); no IP addresses, no form contents
        CREATE TABLE IF NOT EXISTS visitors (
            id TEXT PRIMARY KEY, first_seen TEXT, last_seen TEXT, country TEXT, first_channel TEXT, first_landing TEXT
        );
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY, visitor_id TEXT, started_at TEXT, last_at TEXT, landing TEXT, channel TEXT, referrer TEXT,
            utm_source TEXT, utm_medium TEXT, utm_campaign TEXT, device TEXT, country TEXT
        );
        CREATE INDEX IF NOT EXISTS sessions_visitor ON sessions (visitor_id);
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY, ts TEXT, visitor_id TEXT, session_id TEXT, type TEXT, path TEXT, target TEXT,
            label TEXT, value INTEGER, lead_id INTEGER
        );
        CREATE INDEX IF NOT EXISTS events_ts ON events (ts);
        CREATE INDEX IF NOT EXISTS events_visitor ON events (visitor_id);
        CREATE INDEX IF NOT EXISTS events_path ON events (path, ts);
        -- daily totals, no visitor or session IDs, kept after the 90 days
        CREATE TABLE IF NOT EXISTS page_daily (
            day TEXT, path TEXT, views INT, visitors INT, engaged_ms INT, engaged_n INT, s25 INT, s50 INT, s75 INT, s90 INT,
            wa INT, call INT, email INT, form_start INT, form_submit INT, PRIMARY KEY (day, path)
        );
        -- what the ad platforms were told (api/signals.php)
        CREATE TABLE IF NOT EXISTS signals (
            id INTEGER PRIMARY KEY, lead_id INT, platform TEXT, event TEXT, value REAL, currency TEXT, created_at TEXT,
            sent_at TEXT, state TEXT, detail TEXT, tries INT DEFAULT 0, UNIQUE (lead_id, platform, event)
        );
        CREATE TABLE IF NOT EXISTS channel_daily (
            day TEXT, channel TEXT, sessions INT, visitors INT, wa INT, call INT, form_start INT, form_submit INT,
            PRIMARY KEY (day, channel)
        );
        SQL);
    return $db;
}

function leads_purge(): void
{
    $db = leads_db();
    $cut = gmdate('c', time() - LEADS_RETENTION_DAYS * 86400);
    $db->prepare("DELETE FROM leads WHERE status <> 'won' AND created_at < ?")->execute([$cut]);
    $db->prepare('DELETE FROM events WHERE ts < ?')->execute([$cut]);
    $db->prepare('DELETE FROM sessions WHERE last_at < ?')->execute([$cut]);
    $db->prepare('DELETE FROM visitors WHERE last_seen < ?')->execute([$cut]);
}

const MANUAL_CHANNELS = ['WhatsApp', 'Telegram', 'Phone call', 'LinkedIn DM', 'Referral', 'Other'];

/** Change a lead's status from the panel. Returns an error message, or null when saved.
 *  'won' needs the deal amount: it is what the ad platforms are told the lead was worth. */
function lead_set_status(PDO $db, int $id, string $status, ?string $value, ?string $currency): ?string
{
    if (!in_array($status, LEAD_STATUSES, true)) return 'Unknown status.';
    if ($status === 'won') {
        $amount = preg_replace('/[\s,]/', '', (string) $value);   // "1,00,000" and "1 00 000" are fine
        if (!is_numeric($amount) || !is_finite((float) $amount) || (float) $amount <= 0) return 'Enter the deal amount to mark this lead won.';
        if (!in_array($currency, LEAD_CURRENCIES, true)) return 'Choose the currency of the deal.';
        $db->prepare('UPDATE leads SET status = ?, value = ?, currency = ?, status_at = ? WHERE id = ?')
            ->execute([$status, (float) $amount, $currency, gmdate('c'), $id]);
    } else {
        $db->prepare('UPDATE leads SET status = ?, status_at = ? WHERE id = ?')->execute([$status, gmdate('c'), $id]);
    }
    signal_enqueue($db, $id);
    return null;
}

/** A lead that came in by WhatsApp, Telegram, a call, a LinkedIn DM or a referral. Returns its id. */
function lead_add_manual(PDO $db, array $in): int
{
    $s = fn(string $k, int $max) => mb_substr(trim((string) ($in[$k] ?? '')), 0, $max);
    if ($s('name', 120) === '') throw new InvalidArgumentException('Enter a name.');
    if ($s('phone', 40) === '' && $s('email', 200) === '') throw new InvalidArgumentException('Enter a phone number or an email.');
    if (!in_array($in['channel'] ?? '', MANUAL_CHANNELS, true)) throw new InvalidArgumentException('Choose where the lead came from.');
    $db->prepare("INSERT INTO leads (created_at, form, name, email, phone, business, service, message, channel, status)
        VALUES (?, 'manual', ?, ?, ?, ?, ?, ?, ?, 'new')")
        ->execute([gmdate('c'), $s('name', 120), $s('email', 200), $s('phone', 40), $s('business', 200) ?: null,
            $s('service', 120) ?: null, $s('message', 4000) ?: null, $in['channel']]);
    return (int) $db->lastInsertId();
}

/**
 * Where the visitor came from, from what the browser remembered on landing.
 * Click IDs beat UTMs: Google and Meta add them to ad clicks automatically.
 */
function lead_channel(array $a): string
{
    $src = strtolower($a['utm_source'] ?? '');
    $med = strtolower($a['utm_medium'] ?? '');
    $paid = (bool) preg_match('/cpc|ppc|paid|ads?$|display|social_paid/', $med);
    $ref = strtolower((string) parse_url($a['referrer'] ?? '', PHP_URL_HOST));

    if (!empty($a['gclid']) || ($paid && str_contains($src, 'google'))) return 'Google Ads';
    if (!empty($a['oppref'])) return 'ChatGPT Ads';
    if (!empty($a['li_fat_id']) || ($paid && str_contains($src, 'linkedin'))) return 'LinkedIn Ads';
    if (preg_match('/facebook|^fb$|instagram|^ig$|meta/', $src)) return $paid ? 'Facebook Ads' : 'Facebook / Instagram';
    if (!empty($a['fbclid'])) return 'Facebook / Instagram';
    if ($src !== '') return ($paid ? 'Paid' : 'Campaign') . " ($src)";
    if ($ref === '' || str_ends_with($ref, 'sushantrana.com')) return 'Direct';
    if (preg_match('/(^|\.)(google|bing|yahoo|duckduckgo|yandex|baidu|ecosia)\./', $ref)) return 'Organic search';
    // AI first: "chatgpt.com" contains "t.co"
    if (preg_match('/chatgpt|openai|perplexity|claude|gemini|copilot/', $ref)) return 'AI assistant';
    if (preg_match('/facebook|instagram|linkedin|twitter|x\.com|t\.co|youtube|pinterest|reddit|whatsapp/', $ref)) return 'Social';
    return "Referral ($ref)";
}

// Self-check: php api/leads-db.php
if (PHP_SAPI === 'cli' && realpath($argv[0] ?? '') === __FILE__) {
    $cases = [
        [['gclid' => 'x'], 'Google Ads'],
        [['utm_source' => 'google', 'utm_medium' => 'cpc'], 'Google Ads'],
        [['utm_source' => 'facebook', 'utm_medium' => 'paid'], 'Facebook Ads'],
        [['fbclid' => 'x'], 'Facebook / Instagram'],
        [['utm_source' => 'ig', 'utm_medium' => 'social'], 'Facebook / Instagram'],
        [['utm_source' => 'newsletter'], 'Campaign (newsletter)'],
        [['referrer' => 'https://www.google.com/'], 'Organic search'],
        [['referrer' => 'https://www.linkedin.com/feed'], 'Social'],
        [['referrer' => 'https://example.org/x'], 'Referral (example.org)'],
        [[], 'Direct'],
        [['li_fat_id' => 'x'], 'LinkedIn Ads'],
        [['utm_source' => 'linkedin', 'utm_medium' => 'paid'], 'LinkedIn Ads'],
        [['oppref' => 'x'], 'ChatGPT Ads'],
        [['referrer' => 'https://chatgpt.com/'], 'AI assistant'],
    ];
    foreach ($cases as [$in, $want]) assert(lead_channel($in) === $want, json_encode($in) . ' -> ' . lead_channel($in));
    echo "lead_channel ok\n";
}

require_once __DIR__ . '/signals.php';  // lead_set_status() queues the ad-platform signals
