<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/track.php';

$db = leads_db();
$now = time();
$chrome = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36';
$iphone = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';
$vid = str_repeat('a', 32);
$sid = str_repeat('b', 32);
$count = fn(string $t) => (int) $db->query("SELECT COUNT(*) FROM $t")->fetchColumn();

$body = ['v' => $vid, 's' => $sid, 'tz' => 'Asia/Kolkata', 'ref' => '',
    'attr' => ['landing_page' => '/services/google-ads/', 'gclid' => 'g1'],
    'e' => [['t' => 'page_view', 'p' => '/services/google-ads/']]];
check(track_store($db, $body, $chrome, $now) === 1, 'one page_view not stored');
check($count('visitors') === 1 && $count('sessions') === 1, 'visitor/session not created');
check($db->query("SELECT channel FROM sessions")->fetchColumn() === 'Google Ads', 'session channel not Google Ads');
check($db->query("SELECT country FROM visitors")->fetchColumn() === 'IN', 'visitor country not IN');

$anon = ['v' => null, 's' => null, 'tz' => 'Europe/Berlin', 'e' => [['t' => 'page_view', 'p' => '/']]];
check(track_store($db, $anon, $chrome, $now) === 1, 'anonymous event not stored');
check($count('visitors') === 1, 'anonymous event created a visitor');
check($db->query("SELECT COUNT(*) FROM events WHERE visitor_id IS NULL AND session_id IS NULL")->fetchColumn() == 1, 'anonymous event has IDs');

$many = ['v' => $vid, 's' => $sid, 'e' => array_fill(0, 60, ['t' => 'scroll', 'p' => '/', 'n' => 50])];
check(track_store($db, $many, $chrome, $now) === 50, 'more than 50 events stored');

$bad = ['v' => '../etc', 's' => $sid, 'e' => [['t' => 'evil', 'p' => '/'], ['t' => 'click', 'p' => 'https://x'], ['t' => 'click', 'p' => '/', 'x' => 'whatsapp', 'l' => str_repeat('w', 300)]]];
check(track_store($db, $bad, $chrome, $now) === 1, 'bad events not dropped');
check($db->query("SELECT visitor_id FROM events WHERE type='click'")->fetchColumn() === null, 'bad visitor id kept');
check(mb_strlen((string) $db->query("SELECT label FROM events WHERE type='click'")->fetchColumn()) === 120, 'label not cut to 120');

check(is_bot('Googlebot/2.1 (+http://www.google.com/bot.html)') && is_bot('') && !is_bot($chrome), 'is_bot wrong');
check(tz_country('Asia/Kolkata') === 'IN' && tz_country('Europe/Zurich') === 'CH' && tz_country('Mars/Base') === '', 'tz_country wrong');
check(device_of($iphone) === 'mobile' && device_of($chrome) === 'desktop', 'device_of wrong');

// I-5: numbers too big for an int are dropped, with no PHP warning
set_error_handler(fn($no, $msg) => throw new ErrorException($msg));
check(track_store($db, ['e' => [['t' => 'scroll', 'p' => '/huge', 'n' => 1e30, 'lead' => '99999999999999999999']]], $chrome, $now) === 1, 'huge number event not stored');
restore_error_handler();
check($db->query("SELECT value, lead_id FROM events WHERE path = '/huge'")->fetch() == ['value' => null, 'lead_id' => null], 'huge numbers kept');

// I-6: a visit is credited to how this visit arrived (cur), the visitor to the first ad click (attr)
$v3 = str_repeat('3', 32);
track_store($db, ['v' => $v3, 's' => str_repeat('4', 32), 'attr' => ['gclid' => 'old'], 'e' => [['t' => 'page_view', 'p' => '/']]], $chrome, $now);
track_store($db, ['v' => $v3, 's' => str_repeat('5', 32), 'attr' => ['gclid' => 'old'], 'cur' => [], 'ref' => 'https://www.google.com/',
    'e' => [['t' => 'page_view', 'p' => '/']]], $chrome, $now);
check($db->query("SELECT channel FROM sessions WHERE id = '" . str_repeat('5', 32) . "'")->fetchColumn() === 'Organic search', 'returning organic visit credited to the old ad');
check($db->query("SELECT first_channel FROM visitors WHERE id = '$v3'")->fetchColumn() === 'Google Ads', 'visitor first channel lost');

// I-4: the rate-limit key is not a plain hash of the IP, and changes every day
check(rate_key('203.0.113.7', '2026-10-28') !== md5('203.0.113.7'), 'rate key is md5(IP)');
check(rate_key('203.0.113.7', '2026-10-28') !== rate_key('203.0.113.7', '2026-10-29'), 'rate key does not rotate');
check(rate_key('203.0.113.7', '2026-10-28') === rate_key('203.0.113.7', '2026-10-28'), 'rate key not stable within a day');

echo "track ok\n";
