<?php
/**
 * Nightly job (Hostinger cron, 02:30 IST):
 *   php ~/domains/sushantrana.com/public_html/api/cron-daily.php
 * Writes the daily totals for the last two IST days, deletes what is past the
 * 90-day retention, then talks to the ad platforms and Search Console (each
 * one on its own, so one failing does not stop the others). Safe to run more
 * than once a day.
 */

declare(strict_types=1);
require_once __DIR__ . '/leads-db.php';

/** Rebuild page_daily and channel_daily for one IST day (Y-m-d) from the raw tables. */
function rollup_day(PDO $db, string $day): void
{
    $utc = fn(string $t) => (new DateTime("$day $t", new DateTimeZone('Asia/Kolkata')))->setTimezone(new DateTimeZone('UTC'))->format('c');
    $r = [$utc('00:00:00'), $utc('23:59:59')];
    $db->beginTransaction();
    $db->prepare('DELETE FROM page_daily WHERE day = ?')->execute([$day]);
    $db->prepare('DELETE FROM channel_daily WHERE day = ?')->execute([$day]);
    $db->prepare("INSERT INTO page_daily SELECT ?, path,
            SUM(type = 'page_view'), COUNT(DISTINCT CASE WHEN type = 'page_view' THEN visitor_id END),
            COALESCE(SUM(CASE WHEN type = 'engaged' THEN value END), 0), SUM(type = 'engaged'),
            SUM(type = 'scroll' AND value = 25), SUM(type = 'scroll' AND value = 50), SUM(type = 'scroll' AND value = 75), SUM(type = 'scroll' AND value = 90),
            SUM(type = 'click' AND target = 'whatsapp'), SUM(type = 'click' AND target = 'call'), SUM(type = 'click' AND target = 'email'),
            SUM(type = 'form_start'), SUM(type = 'form_submit')
        FROM events WHERE ts BETWEEN ? AND ? GROUP BY path")->execute([$day, ...$r]);
    $db->prepare("INSERT INTO channel_daily SELECT ?, COALESCE(s.channel, 'Unknown'), COUNT(DISTINCT s.id), COUNT(DISTINCT s.visitor_id),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'click' AND e.target = 'whatsapp'),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'click' AND e.target = 'call'),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'form_start'),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'form_submit')
        FROM sessions s WHERE s.started_at BETWEEN ? AND ? GROUP BY s.channel")->execute([$day, ...$r, ...$r, ...$r, ...$r, ...$r]);
    $db->commit();
}

/** Delete per-IP throttle files (api/t.php, panel login) older than an hour. */
function cleanup_temp_files(string $dir, int $now): void
{
    foreach ([...glob("$dir/t-rate-*") ?: [], ...glob("$dir/login-fail-*") ?: []] as $f) {
        if ($now - (int) filemtime($f) > 3600) @unlink($f);
    }
}

/**
 * Send queued signals, import yesterday's Meta and LinkedIn spend and the last
 * 4 days of Search Console, and write each one's state to integrations.json
 * (Settings shows it). States: ok, error, not configured, never ran.
 */
function cron_integrations(PDO $db, array $cfg, int $now, ?callable $http = null): array
{
    require_once __DIR__ . '/gsc.php';
    $http ??= 'http_json';
    $set = fn(array $keys) => !in_array('', array_map(fn($k) => (string) ($cfg[$k] ?? ''), $keys), true);
    $istDay = fn(int $back) => (new DateTime('@' . ($now - $back * 86400)))->setTimezone(new DateTimeZone('Asia/Kolkata'))->format('Y-m-d');
    $at = gmdate('c', $now);
    $sent = signals_send($db, $cfg, $http, $now);
    $signals = function (string $p) use ($sent): string {
        $c = $sent[$p] ?? [];
        return $c ? 'signals: ' . implode(', ', array_map(fn($s, $n) => "$n $s", array_keys($c), $c)) : '';
    };
    $run = function (bool $configured, callable $job) use ($at): array {
        if (!$configured) return ['state' => 'not configured', 'detail' => '', 'at' => $at];
        try {
            [$state, $detail] = $job();
        } catch (Throwable $e) {
            [$state, $detail] = ['error', mb_substr($e->getMessage(), 0, 300)];
        }
        return ['state' => $state, 'detail' => $detail, 'at' => $at];
    };
    $platform = fn(string $p, string $spendKey, callable $import) => $run(
        ("{$p}_configured")($cfg) || $set([$spendKey]),
        function () use ($p, $spendKey, $cfg, $import, $signals, $set) {
            $rows = $set([$spendKey]) ? $import() . ' spend rows' : 'spend not set up';
            $failed = str_contains($signals($p), 'failed');
            return [$failed ? 'error' : 'ok', trim("$rows. " . $signals($p), '. ')];
        });

    $items = [
        'search_console' => $run($set(['GOOGLE_OAUTH_CLIENT_ID', 'GOOGLE_OAUTH_CLIENT_SECRET', 'GOOGLE_OAUTH_REFRESH_TOKEN']), function () use ($db, $cfg, $http, $istDay) {
            if (!google_access_token($cfg, $http)) {
                throw new RuntimeException('Google login failed: ' . (string) @file_get_contents(leads_data_dir() . '/google-token.error'));
            }
            return ['ok', gsc_import($db, $cfg, $istDay(4), $istDay(1), $http) . ' rows'];
        }),
        'meta' => $platform('meta', 'META_AD_ACCOUNT_ID', fn() => meta_import_spend($db, $cfg, $istDay(1), $http)),
        'linkedin' => $platform('linkedin', 'LINKEDIN_AD_ACCOUNT_ID', fn() => linkedin_import_spend($db, $cfg, $istDay(1), $http)),
        'chatgpt' => $run(chatgpt_configured($cfg), function () use ($signals) {
            return [str_contains($signals('chatgpt'), 'failed') ? 'error' : 'ok', $signals('chatgpt')];
        }),
    ];
    $last = leads_data_dir() . '/google-ads-script.last';
    $items['google_ads_script'] = ($cfg['GOOGLE_ADS_SCRIPT_KEY'] ?? '') === ''
        ? ['state' => 'not configured', 'detail' => '', 'at' => null]
        : (is_file($last)
            ? ['state' => 'ok', 'detail' => 'last pull by the Google Ads script', 'at' => trim((string) file_get_contents($last))]
            : ['state' => 'never ran', 'detail' => 'the Google Ads script has not called the panel yet', 'at' => null]);
    file_put_contents(leads_data_dir() . '/integrations.json', json_encode(['ran_at' => $at, 'items' => $items], JSON_PRETTY_PRINT), LOCK_EX);
    return $items;
}

if (PHP_SAPI === 'cli' && realpath($argv[0] ?? '') === __FILE__) {
    $db = leads_db();
    foreach ([1, 2] as $back) {
        rollup_day($db, (new DateTime('now', new DateTimeZone('Asia/Kolkata')))->modify("-$back day")->format('Y-m-d'));
    }
    leads_purge();
    cleanup_temp_files(leads_data_dir(), time());
    cron_integrations($db, is_file(__DIR__ . '/config.php') ? require __DIR__ . '/config.php' : [], time());
    file_put_contents(leads_data_dir() . '/cron-daily.last', gmdate('c'));
    echo "cron-daily ok\n";
} elseif (PHP_SAPI !== 'cli') {
    http_response_code(404);
    exit(1);
}
