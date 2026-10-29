<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/cron-daily.php';

$db = leads_db();
$day = '2026-10-20';
$at = fn(string $hhmm) => (new DateTime("$day $hhmm", new DateTimeZone('Asia/Kolkata')))->setTimezone(new DateTimeZone('UTC'))->format('c');
$v = str_repeat('e', 32);
$s = str_repeat('f', 32);
$db->prepare("INSERT INTO sessions (id, visitor_id, started_at, last_at, landing, channel) VALUES (?,?,?,?,'/','Organic search')")->execute([$s, $v, $at('10:00'), $at('10:05')]);
$ev = $db->prepare('INSERT INTO events (ts, visitor_id, session_id, type, path, target, value) VALUES (?,?,?,?,?,?,?)');
foreach ([['10:00', 'page_view', '/', null, null], ['10:01', 'page_view', '/', null, null], ['10:02', 'click', '/', 'whatsapp', null],
          ['10:03', 'scroll', '/', null, 50], ['10:04', 'engaged', '/', null, 4000], ['10:05', 'form_start', '/', 'consultation', null],
          ['23:59', 'page_view', '/', null, null]] as [$t, $type, $p, $x, $n]) {
    $ev->execute([$at($t), $v, $s, $type, $p, $x, $n]);
}
// an event on the next IST day must not count
$ev->execute([(new DateTime('2026-10-21 00:01', new DateTimeZone('Asia/Kolkata')))->setTimezone(new DateTimeZone('UTC'))->format('c'), $v, $s, 'page_view', '/', null, null]);

rollup_day($db, $day);
rollup_day($db, $day); // running twice must not double anything
$r = $db->query("SELECT * FROM page_daily WHERE day = '$day' AND path = '/'")->fetch();
check((int) $r['views'] === 3 && (int) $r['visitors'] === 1 && (int) $r['wa'] === 1, 'page_daily counts wrong: ' . json_encode($r));
check((int) $r['s50'] === 1 && (int) $r['engaged_ms'] === 4000 && (int) $r['engaged_n'] === 1 && (int) $r['form_start'] === 1, 'page_daily detail wrong');
check((int) $db->query("SELECT COUNT(*) FROM page_daily")->fetchColumn() === 1, 'rollup ran twice');
$c = $db->query("SELECT * FROM channel_daily WHERE day = '$day'")->fetch();
check($c['channel'] === 'Organic search' && (int) $c['sessions'] === 1 && (int) $c['wa'] === 1, 'channel_daily wrong: ' . json_encode($c));
$cols = array_column($db->query('PRAGMA table_info(page_daily)')->fetchAll(), 'name');
check(!array_intersect(['visitor_id', 'session_id'], $cols), 'page_daily holds IDs');

// I-4: throttle files older than an hour are deleted
$dir = getenv('LEADS_DATA_DIR');
touch("$dir/t-rate-old", time() - 7200);
touch("$dir/login-fail-old", time() - 7200);
touch("$dir/t-rate-new", time() - 60);
cleanup_temp_files($dir, time());
check(!is_file("$dir/t-rate-old") && !is_file("$dir/login-fail-old") && is_file("$dir/t-rate-new"), 'throttle files not cleaned');

// integrations: with nothing configured every step reports so, nothing throws
$first = cron_integrations($db, [], time(), function () { throw new LogicException('no network in tests'); });
$saved = json_decode((string) file_get_contents(getenv('LEADS_DATA_DIR') . '/integrations.json'), true);
foreach (['search_console', 'meta', 'linkedin', 'chatgpt', 'google_ads_script'] as $k) {
    check(($saved['items'][$k]['state'] ?? '') === 'not configured', "$k not 'not configured': " . json_encode($saved['items'][$k] ?? null));
}
$noNet = fn() => throw new LogicException('no network in tests');
check(cron_integrations($db, ['GOOGLE_ADS_SCRIPT_KEY' => 'k'], time(), $noNet)['google_ads_script']['state'] === 'never ran', 'script never ran');
file_put_contents("$dir/google-ads-script.last", gmdate('c'));
check(cron_integrations($db, ['GOOGLE_ADS_SCRIPT_KEY' => 'k'], time(), $noNet)['google_ads_script']['state'] === 'ok', 'script pull not ok');
// an expired Google login is an error, not "not configured"
$gc = ['GOOGLE_OAUTH_CLIENT_ID' => 'c', 'GOOGLE_OAUTH_CLIENT_SECRET' => 's', 'GOOGLE_OAUTH_REFRESH_TOKEN' => 'r'];
$st = cron_integrations($db, $gc, time(), fn() => ['code' => 400, 'body' => '{"error":"invalid_grant","error_description":"reauth related error (invalid_rapt)"}']);
check($st['search_console']['state'] === 'error' && str_contains($st['search_console']['detail'], 'invalid_rapt'), 'gsc login error: ' . json_encode($st['search_console']));
check(isset($saved['ran_at']) && $first === $saved['items'], 'integrations.json shape');

// a configured integration that fails is reported as an error, the others still run
$st = cron_integrations($db, ['META_ACCESS_TOKEN' => 't', 'META_AD_ACCOUNT_ID' => '1', 'META_DATASET_ID' => 'd'], time(),
    fn() => ['code' => 500, 'body' => '{"error":{"message":"Meta is down"}}']);
check($st['meta']['state'] === 'error' && str_contains($st['meta']['detail'], 'Meta is down'), 'meta error not reported: ' . json_encode($st['meta']));
check($st['linkedin']['state'] === 'not configured', 'linkedin skipped after meta error');

echo "cron ok\n";
