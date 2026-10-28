<?php
/**
 * POST /api/t.php — the site's own analytics beacon (site.js track()).
 * Always answers 204 with no body; the visitor never waits on it.
 */

declare(strict_types=1);
header('Cache-Control: no-store');
require __DIR__ . '/track.php';

function done(int $status = 204): never
{
    http_response_code($status);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') done(405);
$raw = file_get_contents('php://input', false, null, 0, 16385);
if ($raw === false || strlen($raw) > 16384) done(413);
$ua = (string) ($_SERVER['HTTP_USER_AGENT'] ?? '');
if (is_bot($ua)) done();

// 120 requests a minute per IP. The file name is a keyed hash that changes daily;
// cron-daily.php deletes these files after an hour.
$file = leads_data_dir() . '/t-rate-' . rate_key($_SERVER['REMOTE_ADDR'] ?? '', gmdate('Y-m-d'));
$hits = array_filter(is_file($file) ? (json_decode((string) file_get_contents($file), true) ?: []) : [], fn($t) => time() - $t < 60);
if (count($hits) >= 120) done(429);
file_put_contents($file, json_encode([...$hits, time()]), LOCK_EX);

$body = json_decode($raw, true);
if (!is_array($body)) done(400);
try {
    track_store(leads_db(), $body, $ua, time());
} catch (Throwable $e) {
    error_log('[t] ' . $e->getMessage());
}
done();
