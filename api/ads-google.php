<?php
/**
 * POST /api/ads-google.php?a=pull|ack|push — the Google Ads script's only door
 * into the panel (dev/google-ads-script.js). Header X-Key must equal
 * GOOGLE_ADS_SCRIPT_KEY in api/config.php.
 */

declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
require __DIR__ . '/ads-store.php';

function out(int $status, array $body = []): never
{
    http_response_code($status);
    echo json_encode($body ?: ['ok' => $status === 200]);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') out(405);
$raw = file_get_contents('php://input', false, null, 0, 2 * 1024 * 1024 + 1);
if ($raw === false || strlen($raw) > 2 * 1024 * 1024) out(413);
$config = is_file(__DIR__ . '/config.php') ? require __DIR__ . '/config.php' : [];
$key = (string) ($config['GOOGLE_ADS_SCRIPT_KEY'] ?? '');
if ($key === '' || !hash_equals($key, (string) ($_SERVER['HTTP_X_KEY'] ?? ''))) out(403);
$body = json_decode($raw, true);
if (!is_array($body)) out(400);

$db = leads_db();
switch ($_GET['a'] ?? '') {
    case 'pull':
        out(200, ['conversions' => google_pull($db, time())]);
    case 'ack':
        google_ack($db, (array) ($body['sent'] ?? []), (array) ($body['failed'] ?? []));
        out(200);
    case 'push':
        $n = ['spend' => ads_store_spend($db, (array) ($body['spend'] ?? [])), 'clicks' => ads_store_clicks($db, (array) ($body['clicks'] ?? [])),
            'terms' => ads_store_terms($db, (array) ($body['terms'] ?? []))];
        $n['leads'] = ads_backfill_leads($db);
        out(200, ['ok' => true, 'stored' => $n]);
    default:
        out(400);
}
