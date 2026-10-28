<?php
/**
 * Storage for the site's own analytics (site.js → api/t.php).
 *
 * One request is a batch of up to 50 events from one page. Visitor and
 * session IDs come only after consent (or outside Europe); without them the
 * events are stored as anonymous counts. No IP addresses, no form contents.
 */

declare(strict_types=1);
require_once __DIR__ . '/leads-db.php';

const TRACK_TYPES = ['page_view', 'scroll', 'engaged', 'click', 'form_start', 'form_submit'];
const TRACK_MAX_EVENTS = 50;

function track_store(PDO $db, array $body, string $userAgent, int $now): int
{
    $id = fn($v) => is_string($v) && preg_match('/^[a-f0-9]{32}$/', $v) ? $v : null;
    $str = fn($v, int $max) => is_string($v) ? mb_substr(trim($v), 0, $max) : '';
    // whole numbers that fit an int, else null (a huge float would warn when cast)
    $int = fn($v) => is_int($v) || (is_string($v) && $v !== '') ? (($i = filter_var($v, FILTER_VALIDATE_INT)) === false ? null : $i) : null;
    $vid = $id($body['v'] ?? null);
    $sid = $vid ? $id($body['s'] ?? null) : null;
    $ts = gmdate('c', $now);
    $country = tz_country($str($body['tz'] ?? '', 64));

    $events = [];
    foreach (array_slice(is_array($body['e'] ?? null) ? $body['e'] : [], 0, TRACK_MAX_EVENTS) as $e) {
        if (!is_array($e) || !in_array($e['t'] ?? '', TRACK_TYPES, true)) continue;
        $path = $str($e['p'] ?? '', 300);
        if (!str_starts_with($path, '/')) continue;
        $events[] = [$ts, $vid, $sid, $e['t'], $path, $str($e['x'] ?? '', 120), $str($e['l'] ?? '', 120), $int($e['n'] ?? null), $int($e['lead'] ?? null)];
    }
    if (!$events) return 0;

    $db->beginTransaction();
    if ($vid) {
        $clean = fn($a) => is_array($a) ? array_map(fn($v) => $str($v, 300), $a) : [];
        $attr = $clean($body['attr'] ?? null) + ['referrer' => ''];   // first touch, kept 90 days: the visitor's first channel
        $cur = isset($body['cur']) ? $clean($body['cur']) : $attr;     // how this visit arrived: the session's channel
        $cur['referrer'] = $str($body['ref'] ?? '', 300);
        $channel = lead_channel($cur);
        $landing = ($attr['landing_page'] ?? '') ?: $events[0][4];
        $db->prepare('INSERT INTO visitors (id, first_seen, last_seen, country, first_channel, first_landing) VALUES (?,?,?,?,?,?)
            ON CONFLICT(id) DO UPDATE SET last_seen = excluded.last_seen')
            ->execute([$vid, $ts, $ts, $country, lead_channel($attr['referrer'] !== '' ? $attr : $attr + $cur), $landing]);
        if ($sid) {
            $db->prepare('INSERT INTO sessions (id, visitor_id, started_at, last_at, landing, channel, referrer, utm_source, utm_medium,
                    utm_campaign, device, country) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                ON CONFLICT(id) DO UPDATE SET last_at = excluded.last_at')
                ->execute([$sid, $vid, $ts, $ts, $events[0][4], $channel, $cur['referrer'] ?: null, ($cur['utm_source'] ?? '') ?: null,
                    ($cur['utm_medium'] ?? '') ?: null, ($cur['utm_campaign'] ?? '') ?: null, device_of($userAgent), $country]);
        }
    }
    $ins = $db->prepare('INSERT INTO events (ts, visitor_id, session_id, type, path, target, label, value, lead_id) VALUES (?,?,?,?,?,?,?,?,?)');
    foreach ($events as $row) $ins->execute($row);
    $db->commit();
    return count($events);
}

/** Name of the per-IP throttle file: keyed with a secret that is never stored with it and a new key every day. */
function rate_key(string $ip, string $day): string
{
    $file = leads_data_dir() . '/t-salt';
    if (!is_file($file)) file_put_contents($file, bin2hex(random_bytes(32)), LOCK_EX);
    return hash_hmac('sha256', "$day|$ip", (string) file_get_contents($file));
}

function is_bot(string $ua): bool
{
    return trim($ua) === '' || (bool) preg_match('/bot|crawl|spider|slurp|headless|lighthouse|preview|fetch|curl|wget|python|monitor/i', $ua);
}

function device_of(string $ua): string
{
    if (preg_match('/ipad|tablet/i', $ua) || (str_contains($ua, 'Android') && !str_contains($ua, 'Mobile'))) return 'tablet';
    return preg_match('/mobile|iphone|android/i', $ua) ? 'mobile' : 'desktop';
}

/** Country from the browser's time zone; the server never looks at the IP. */
function tz_country(string $tz): string
{
    static $map = [
        'Asia/Kolkata' => 'IN', 'Asia/Calcutta' => 'IN', 'Asia/Dubai' => 'AE', 'Asia/Muscat' => 'OM', 'Asia/Qatar' => 'QA',
        'Asia/Bahrain' => 'BH', 'Asia/Kuwait' => 'KW', 'Asia/Riyadh' => 'SA', 'Asia/Karachi' => 'PK', 'Asia/Dhaka' => 'BD',
        'Asia/Kathmandu' => 'NP', 'Asia/Singapore' => 'SG', 'Asia/Colombo' => 'LK', 'Australia/Sydney' => 'AU',
        'Australia/Melbourne' => 'AU', 'Pacific/Auckland' => 'NZ', 'America/New_York' => 'US', 'America/Chicago' => 'US',
        'America/Denver' => 'US', 'America/Phoenix' => 'US', 'America/Los_Angeles' => 'US', 'America/Anchorage' => 'US',
        'Pacific/Honolulu' => 'US', 'America/Toronto' => 'CA', 'America/Vancouver' => 'CA', 'America/Edmonton' => 'CA',
        'America/Winnipeg' => 'CA', 'America/Halifax' => 'CA', 'America/Nassau' => 'BS', 'Europe/London' => 'GB',
        'Europe/Dublin' => 'IE', 'Europe/Zurich' => 'CH', 'Europe/Berlin' => 'DE', 'Europe/Paris' => 'FR',
        'Europe/Amsterdam' => 'NL', 'Europe/Madrid' => 'ES', 'Europe/Rome' => 'IT', 'Europe/Vienna' => 'AT',
        'Europe/Brussels' => 'BE', 'Europe/Stockholm' => 'SE', 'Europe/Warsaw' => 'PL', 'Europe/Lisbon' => 'PT',
        'Europe/Helsinki' => 'FI', 'Europe/Copenhagen' => 'DK', 'Europe/Oslo' => 'NO', 'Europe/Istanbul' => 'TR',
    ];
    return $map[$tz] ?? '';
}
