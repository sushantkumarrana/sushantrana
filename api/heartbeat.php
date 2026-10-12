<?php
/**
 * GET /api/heartbeat.php — writes one row to `heartbeat` so the Supabase Free
 * plan never pauses the project (it pauses after ~7 quiet days, and a paused
 * project drops lead storage to email-only).
 *
 * The Node app used to ping itself every 6 hours. Static hosting has no
 * process, so schedule this URL instead: Hostinger hPanel → Advanced →
 * Cron Jobs → every 6 hours:
 *   curl -s https://sushantrana.com/api/heartbeat.php > /dev/null
 * A 200 also doubles as an uptime probe: site up AND database reachable.
 */

declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$config = is_file(__DIR__ . '/config.php') ? require __DIR__ . '/config.php' : [];
$url = $config['SUPABASE_URL'] ?? getenv('SUPABASE_URL') ?: '';
$key = $config['SUPABASE_PUBLISHABLE_KEY'] ?? getenv('SUPABASE_PUBLISHABLE_KEY') ?: '';

if (!$url || !$key) {
    http_response_code(500);
    exit(json_encode(['ok' => false, 'error' => 'not configured']));
}

// Left open on purpose; abuse is bounded by one write per 55 minutes.
$stamp = sys_get_temp_dir() . '/sr-heartbeat';
if (is_file($stamp) && time() - (int) file_get_contents($stamp) < 55 * 60) {
    exit(json_encode(['ok' => true, 'skipped' => 'throttled']));
}
file_put_contents($stamp, (string) time());

$ch = curl_init(rtrim($url, '/') . '/rest/v1/heartbeat');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => ['Content-Type: application/json', "apikey: $key", "Authorization: Bearer $key", 'Prefer: return=minimal'],
    CURLOPT_POSTFIELDS => json_encode(['source' => 'http']),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 8,
]);
curl_exec($ch);
$code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$ok = $code >= 200 && $code < 300;
http_response_code($ok ? 200 : 500);
echo json_encode($ok ? ['ok' => true, 'pinged' => gmdate('c')] : ['ok' => false, 'error' => 'insert failed']);
