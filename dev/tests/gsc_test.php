<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/gsc.php';
require dirname(__DIR__, 2) . '/leadsforme/reports.php';

$db = leads_db();
$cfg = ['GOOGLE_OAUTH_CLIENT_ID' => 'cid', 'GOOGLE_OAUTH_CLIENT_SECRET' => 'sec', 'GOOGLE_OAUTH_REFRESH_TOKEN' => 'rt'];

// token: refreshed once, then cached
$tokenCalls = 0;
$tok = function ($m, $u, $h, $b) use (&$tokenCalls) {
    $tokenCalls++;
    check($m === 'POST' && $u === 'https://oauth2.googleapis.com/token' && ($b['grant_type'] ?? '') === 'refresh_token' && $b['refresh_token'] === 'rt', 'token request');
    check(in_array('Content-Type: application/x-www-form-urlencoded', $h, true), 'token request not form-encoded');
    return ['code' => 200, 'body' => '{"access_token":"at1","expires_in":3600}'];
};
check(google_access_token($cfg, $tok) === 'at1' && google_access_token($cfg, $tok) === 'at1' && $tokenCalls === 1, 'token not cached');
@unlink(leads_data_dir() . '/google-token.json');
check(google_access_token($cfg, fn() => ['code' => 400, 'body' => '{"error":"invalid_grant","error_description":"reauth related error (invalid_rapt)"}']) === null, 'invalid_grant not null');
check(str_contains((string) @file_get_contents(leads_data_dir() . '/google-token.error'), 'invalid_rapt'), 'token error not recorded');
check(google_access_token([], $tok) === null, 'unconfigured token not null');

// import: paged rows, URL → path
$pages = [
    ['rows' => [['keys' => ['2026-10-26', 'https://sushantrana.com/services/google-ads/', 'google ads expert'], 'clicks' => 2, 'impressions' => 40, 'position' => 8.5],
                ['keys' => ['2026-10-26', 'https://sushantrana.com/', 'sushant rana'], 'clicks' => 3, 'impressions' => 50, 'position' => 5.2]]],
    ['rows' => [['keys' => ['2026-10-27', 'https://sushantrana.com/services/google-ads/', 'google ads expert'], 'clicks' => 1, 'impressions' => 30, 'position' => 9.1]]],
];
$bodies = [];
$api = function ($m, $u, $h, $b) use (&$pages, &$bodies) {
    if (str_contains($u, 'oauth2')) return ['code' => 200, 'body' => '{"access_token":"at2","expires_in":3600}'];
    check(str_contains($u, '/sites/sc-domain%3Asushantrana.com/searchAnalytics/query') && in_array('Authorization: Bearer at2', $h, true), 'gsc request: ' . $u);
    $bodies[] = $b;
    return ['code' => 200, 'body' => json_encode(array_shift($pages) ?? ['rows' => []])];
};
@unlink(leads_data_dir() . '/google-token.json');
$n = gsc_import($db, $cfg, '2026-10-26', '2026-10-27', $api, 2);
check($n === 3 && $bodies[0]['dimensions'] === ['date', 'page', 'query'] && $bodies[1]['startRow'] === 2, 'paging: ' . json_encode($bodies));
check($db->query("SELECT page FROM gsc_daily WHERE query = 'sushant rana'")->fetchColumn() === '/', 'page not a path');
check(gsc_import($db, $cfg, '2026-10-26', '2026-10-27', $api, 2) === 0 && (int) $db->query('SELECT COUNT(*) FROM gsc_daily')->fetchColumn() === 3, 'import not idempotent');

// the page report shows its queries
$p = report_page($db, '/services/google-ads/', '2026-10-26', '2026-10-27');
check(($p['gsc'][0] ?? null) == ['query' => 'google ads expert', 'clicks' => 3, 'impressions' => 70, 'position' => 8.8], 'page gsc: ' . json_encode($p['gsc'] ?? null));

echo "gsc ok\n";
