<?php
/**
 * The ad platforms' own numbers in the panel: daily spend, which Google click
 * came from which campaign / ad group / keyword, and Google search terms.
 * Also the Google side of the signals, which the Google Ads script pulls.
 */

declare(strict_types=1);
require_once __DIR__ . '/signals.php';

function ads_rows(array $rows, array $keys): array
{
    return array_values(array_filter(array_map(function ($r) use ($keys) {
        if (!is_array($r)) return null;
        $out = [];
        foreach ($keys as $k => $type) {
            $v = $r[$k] ?? null;
            $out[$k] = match ($type) {
                'num' => is_numeric($v) ? (float) $v : 0.0,
                'int' => is_numeric($v) ? (int) $v : 0,
                default => is_scalar($v) ? mb_substr(trim((string) $v), 0, 300) : '',
            };
        }
        return preg_match('/^\d{4}-\d{2}-\d{2}$/', $out['day'] ?? '2000-01-01') ? $out : null;
    }, $rows)));
}

function ads_store_spend(PDO $db, array $rows): int
{
    $rows = ads_rows($rows, ['day' => 's', 'platform' => 's', 'campaign' => 's', 'ad_group' => 's', 'cost' => 'num', 'clicks' => 'int', 'impressions' => 'int', 'currency' => 's']);
    $st = $db->prepare('INSERT OR REPLACE INTO ad_spend (day, platform, campaign, ad_group, cost, clicks, impressions, currency) VALUES (?,?,?,?,?,?,?,?)');
    foreach ($rows as $r) $st->execute(array_values($r));
    return count($rows);
}

function ads_store_clicks(PDO $db, array $rows): int
{
    $rows = array_filter(ads_rows($rows, ['click_id' => 's', 'day' => 's', 'campaign' => 's', 'ad_group' => 's', 'keyword' => 's']), fn($r) => $r['click_id'] !== '');
    $st = $db->prepare("INSERT OR REPLACE INTO ad_clicks (click_id, platform, day, campaign, ad_group, keyword) VALUES (?, 'google', ?, ?, ?, ?)");
    foreach ($rows as $r) $st->execute(array_values($r));
    return count($rows);
}

function ads_store_terms(PDO $db, array $rows): int
{
    $rows = ads_rows($rows, ['day' => 's', 'campaign' => 's', 'ad_group' => 's', 'term' => 's', 'clicks' => 'int', 'cost' => 'num', 'conversions' => 'num']);
    $st = $db->prepare('INSERT OR REPLACE INTO search_terms (day, campaign, ad_group, term, clicks, cost, conversions) VALUES (?,?,?,?,?,?,?)');
    foreach ($rows as $r) $st->execute(array_values($r));
    return count($rows);
}

/** Copy campaign / ad group / keyword from Google's click report onto leads that came from those clicks. */
function ads_backfill_leads(PDO $db): int
{
    return $db->exec("UPDATE leads SET
            utm_campaign = COALESCE(NULLIF(utm_campaign, ''), (SELECT campaign FROM ad_clicks c WHERE c.click_id = leads.gclid)),
            ad_group = COALESCE(NULLIF(ad_group, ''), (SELECT ad_group FROM ad_clicks c WHERE c.click_id = leads.gclid)),
            keyword = COALESCE(NULLIF(keyword, ''), (SELECT keyword FROM ad_clicks c WHERE c.click_id = leads.gclid))
        WHERE gclid IN (SELECT click_id FROM ad_clicks) AND (COALESCE(ad_group, '') = '' OR COALESCE(keyword, '') = '' OR COALESCE(utm_campaign, '') = '')");
}

/**
 * Google signals for the script to upload, by gclid, time in IST. Google takes
 * clicks up to 90 days old; gbraid / wbraid leads are skipped (upload is by gclid).
 */
function google_pull(PDO $db, int $now): array
{
    $rows = $db->query("SELECT s.id, s.event, s.value, s.currency, s.created_at, l.gclid, l.created_at AS clicked
        FROM signals s JOIN leads l ON l.id = s.lead_id
        WHERE s.platform = 'google' AND (s.state = 'pending' OR (s.state = 'failed' AND s.tries < 5)) ORDER BY s.id")->fetchAll();
    $mark = $db->prepare('UPDATE signals SET state = ?, detail = ? WHERE id = ?');
    $out = [];
    foreach ($rows as $r) {
        if (($r['gclid'] ?? '') === '') { $mark->execute(['skipped', 'app click (gbraid/wbraid): Google upload is by gclid', $r['id']]); continue; }
        if ($now - strtotime($r['clicked']) > 90 * 86400) { $mark->execute(['expired', 'click older than 90 days', $r['id']]); continue; }
        $out[] = ['id' => (int) $r['id'], 'gclid' => $r['gclid'], 'name' => $r['event'],
            'time' => (new DateTime($r['created_at']))->setTimezone(new DateTimeZone('Asia/Kolkata'))->format('Y-m-d H:i:s'),
            'value' => $r['value'] === null ? null : (float) $r['value'], 'currency' => $r['currency']];
    }
    file_put_contents(leads_data_dir() . '/google-ads-script.last', gmdate('c', $now));
    return $out;
}

/** The script reports what it uploaded. */
function google_ack(PDO $db, array $sent, array $failed): void
{
    $ok = $db->prepare("UPDATE signals SET state = 'sent', sent_at = ?, tries = tries + 1, detail = NULL WHERE id = ? AND platform = 'google'");
    foreach ($sent as $id) if (is_numeric($id)) $ok->execute([gmdate('c'), (int) $id]);
    $bad = $db->prepare("UPDATE signals SET state = 'failed', tries = tries + 1, detail = ? WHERE id = ? AND platform = 'google'");
    foreach ($failed as $f) if (is_array($f) && is_numeric($f['id'] ?? null)) $bad->execute([mb_substr((string) ($f['error'] ?? 'failed'), 0, 300), (int) $f['id']]);
}
