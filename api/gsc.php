<?php
/** Search Console queries per page, imported nightly into gsc_daily. */

declare(strict_types=1);
require_once __DIR__ . '/google-oauth.php';

/** Import days $from..$to (Y-m-d). Returns rows stored; 0 when not configured. */
function gsc_import(PDO $db, array $cfg, string $from, string $to, ?callable $http = null, int $rowLimit = 25000): int
{
    $http ??= 'http_json';
    $token = google_access_token($cfg, $http);
    if (!$token) return 0;
    $site = ($cfg['GSC_SITE'] ?? '') ?: 'sc-domain:sushantrana.com';
    $url = 'https://www.googleapis.com/webmasters/v3/sites/' . rawurlencode($site) . '/searchAnalytics/query';
    $st = $db->prepare('INSERT OR REPLACE INTO gsc_daily (day, page, query, clicks, impressions, position) VALUES (?,?,?,?,?,?)');
    $stored = 0;
    for ($start = 0; ; $start += $rowLimit) {
        $res = $http('POST', $url, ["Authorization: Bearer $token"],
            ['startDate' => $from, 'endDate' => $to, 'dimensions' => ['date', 'page', 'query'], 'rowLimit' => $rowLimit, 'startRow' => $start]);
        if ($res['code'] !== 200) throw new RuntimeException('Search Console: ' . signal_error($res));
        $rows = (json_decode($res['body'], true) ?: [])['rows'] ?? [];
        foreach ($rows as $r) {
            [$day, $page, $query] = $r['keys'];
            $st->execute([$day, (parse_url($page, PHP_URL_PATH) ?: '/'), $query, (int) $r['clicks'], (int) $r['impressions'], (float) $r['position']]);
            $stored++;
        }
        if (count($rows) < $rowLimit) return $stored;
    }
}
