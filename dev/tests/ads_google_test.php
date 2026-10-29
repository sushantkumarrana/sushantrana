<?php
// Storage functions directly; the endpoint's refusals over HTTP on the local preview (port 8091, no api/config.php).
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/ads-store.php';

$db = leads_db();
$now = strtotime('2026-10-29T12:00:00+00:00');

// push: spend twice → still 2 rows; a click fills the matching lead
$spend = [['day' => '2026-10-28', 'platform' => 'google', 'campaign' => 'Search IN', 'ad_group' => 'Google Ads', 'cost' => 1200.5, 'clicks' => 30, 'impressions' => 900, 'currency' => 'INR'],
          ['day' => '2026-10-28', 'platform' => 'google', 'campaign' => 'Search IN', 'ad_group' => 'SEO', 'cost' => 300, 'clicks' => 8, 'impressions' => 200, 'currency' => 'INR']];
ads_store_spend($db, $spend);
ads_store_spend($db, $spend);
check((int) $db->query('SELECT COUNT(*) FROM ad_spend')->fetchColumn() === 2, 'spend duplicated');
$db->exec("INSERT INTO leads (created_at, name, email, phone, gclid, status, value, currency, status_at)
    VALUES ('" . gmdate('c', $now - 86400) . "', 'G', 'g@x.com', '+911', 'GCLID1', 'won', 50000, 'INR', '" . gmdate('c', $now) . "')");
$lead = (int) $db->lastInsertId();
ads_store_clicks($db, [['click_id' => 'GCLID1', 'day' => '2026-10-28', 'campaign' => 'Search IN', 'ad_group' => 'Google Ads', 'keyword' => 'google ads expert']]);
check(ads_backfill_leads($db) === 1, 'backfill count');
$l = $db->query("SELECT utm_campaign, ad_group, keyword FROM leads WHERE id = $lead")->fetch();
check($l === ['utm_campaign' => 'Search IN', 'ad_group' => 'Google Ads', 'keyword' => 'google ads expert'], 'lead not backfilled: ' . json_encode($l));
ads_store_terms($db, [['day' => '2026-10-28', 'campaign' => 'Search IN', 'ad_group' => 'Google Ads', 'term' => 'google ads consultant chandigarh', 'clicks' => 3, 'cost' => 90, 'conversions' => 1]]);
check((int) $db->query('SELECT COUNT(*) FROM search_terms')->fetchColumn() === 1, 'terms not stored');

// pull: the won Google signal, IST time, value; then ack
signal_enqueue($db, $lead);
$pull = google_pull($db, $now);
check(count($pull) === 1 && $pull[0]['gclid'] === 'GCLID1' && $pull[0]['name'] === 'Won deal' && $pull[0]['value'] === 50000.0 && $pull[0]['currency'] === 'INR', 'pull: ' . json_encode($pull));
$queued = $db->query("SELECT created_at FROM signals WHERE platform = 'google'")->fetchColumn();
check($pull[0]['time'] === (new DateTime($queued))->setTimezone(new DateTimeZone('Asia/Kolkata'))->format('Y-m-d H:i:s'), 'pull time is not the status change in IST');
google_ack($db, [$pull[0]['id']], []);
check($db->query("SELECT state FROM signals WHERE platform = 'google'")->fetchColumn() === 'sent', 'ack did not mark sent');
check(google_pull($db, $now) === [], 'sent signal pulled again');

// a click older than 90 days expires; a gbraid-only lead is skipped (the script uploads by gclid)
$db->exec("INSERT INTO leads (created_at, name, email, phone, gclid, status) VALUES ('" . gmdate('c', $now - 91 * 86400) . "', 'Old', 'o@x.com', '+911', 'OLD', 'qualified')");
$old = (int) $db->lastInsertId();
signal_enqueue($db, $old);
$db->exec("INSERT INTO leads (created_at, name, email, phone, gbraid, status) VALUES ('" . gmdate('c', $now) . "', 'App', 'a@x.com', '+911', 'GB1', 'qualified')");
$app = (int) $db->lastInsertId();
signal_enqueue($db, $app);
check(google_pull($db, $now) === [], 'old or gbraid-only lead pulled');
check($db->query("SELECT state FROM signals WHERE lead_id = $old")->fetchColumn() === 'expired', 'old click not expired');
check($db->query("SELECT state FROM signals WHERE lead_id = $app")->fetchColumn() === 'skipped', 'gbraid lead not skipped');

// the endpoint refuses without the key, GET, and huge bodies
$http = function (string $method, string $body = '', array $headers = []): int {
    $ch = curl_init('http://localhost:8091/api/ads-google.php?a=pull');
    curl_setopt_array($ch, [CURLOPT_CUSTOMREQUEST => $method, CURLOPT_RETURNTRANSFER => true, CURLOPT_HTTPHEADER => $headers]
        + ($body !== '' ? [CURLOPT_POSTFIELDS => $body] : []));
    curl_exec($ch);
    return (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
};
check($http('GET') === 405, 'GET not 405');
check($http('POST', '{}', ['X-Key: wrong']) === 403, 'wrong key not 403');
check($http('POST', str_repeat('a', 3 * 1024 * 1024), ['X-Key: wrong']) === 413, 'huge body not 413');

echo "ads google ok\n";
