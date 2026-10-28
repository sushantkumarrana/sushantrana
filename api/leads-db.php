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

// Privacy Policy promises deletion within three weeks of last contact.
// Change the policy page too if you change this. 'won' leads are kept.
const LEADS_RETENTION_DAYS = 21;
const LEAD_STATUSES = ['new', 'contacted', 'won', 'lost'];

function leads_data_dir(): string
{
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
            referrer     TEXT,                       -- site that sent the visitor
            channel      TEXT,                       -- Google Ads, Facebook Ads, Organic search …
            utm_source   TEXT, utm_medium TEXT, utm_campaign TEXT, utm_term TEXT, utm_content TEXT,
            gclid        TEXT, fbclid TEXT,
            user_agent   TEXT,
            status       TEXT NOT NULL DEFAULT 'new'
        );
        CREATE INDEX IF NOT EXISTS leads_created_at ON leads (created_at DESC);
        SQL);
    // databases made before the journey column existed
    if (!in_array('journey', array_column($db->query('PRAGMA table_info(leads)')->fetchAll(), 'name'), true)) {
        $db->exec('ALTER TABLE leads ADD COLUMN journey TEXT');
    }
    return $db;
}

function leads_purge(): void
{
    leads_db()->prepare("DELETE FROM leads WHERE status <> 'won' AND created_at < ?")
        ->execute([gmdate('c', time() - LEADS_RETENTION_DAYS * 86400)]);
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
    if (preg_match('/facebook|^fb$|instagram|^ig$|meta/', $src)) return $paid ? 'Facebook Ads' : 'Facebook / Instagram';
    if (!empty($a['fbclid'])) return 'Facebook / Instagram';
    if ($src !== '') return ($paid ? 'Paid' : 'Campaign') . " ($src)";
    if ($ref === '' || str_ends_with($ref, 'sushantrana.com')) return 'Direct';
    if (preg_match('/(^|\.)(google|bing|yahoo|duckduckgo|yandex|baidu|ecosia)\./', $ref)) return 'Organic search';
    if (preg_match('/facebook|instagram|linkedin|twitter|x\.com|t\.co|youtube|pinterest|reddit|whatsapp/', $ref)) return 'Social';
    if (preg_match('/chatgpt|openai|perplexity|claude|gemini|copilot/', $ref)) return 'AI assistant';
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
    ];
    foreach ($cases as [$in, $want]) assert(lead_channel($in) === $want, json_encode($in) . ' -> ' . lead_channel($in));
    echo "lead_channel ok\n";
}
