<?php
// Report numbers on a small known fixture. `--keep` loads the fixture into
// LEADS_DATA_DIR (e.g. the local .data) and leaves it there for the panel.
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/leads-db.php';
require dirname(__DIR__, 2) . '/leadsforme/reports.php';

$db = leads_db();
$day = (new DateTime('now', new DateTimeZone('Asia/Kolkata')))->format('Y-m-d');
$t = fn(int $min) => gmdate('c', time() - 3600 + $min * 60);   // all within the last hour
$v1 = str_repeat('1', 32);
$v2 = str_repeat('2', 32);
[$s1, $s2, $s3] = [str_repeat('a', 32), str_repeat('b', 32), str_repeat('c', 32)];
$g = '/services/google-ads/';

$db->prepare('INSERT INTO visitors VALUES (?,?,?,?,?,?)')->execute([$v1, $t(0), $t(5), 'IN', 'Google Ads', '/']);
$db->prepare('INSERT INTO visitors VALUES (?,?,?,?,?,?)')->execute([$v2, $t(10), $t(30), 'AE', 'Direct', '/']);
$sess = $db->prepare('INSERT INTO sessions (id, visitor_id, started_at, last_at, landing, channel, device, country) VALUES (?,?,?,?,?,?,?,?)');
$sess->execute([$s1, $v1, $t(0), $t(5), '/', 'Google Ads', 'mobile', 'IN']);
$sess->execute([$s2, $v2, $t(10), $t(12), '/', 'Direct', 'desktop', 'AE']);
$sess->execute([$s3, $v2, $t(25), $t(30), '/', 'Direct', 'desktop', 'AE']);

$db->exec("INSERT INTO leads (created_at, form, name, email, phone, channel, visitor_id, status, value, currency)
    VALUES ('" . $t(5) . "', 'google_ads', 'Won Lead', 'w@x.com', '+911', 'Google Ads', '$v1', 'won', 50000, 'INR')");
$lead = (int) $db->lastInsertId();

$ev = $db->prepare('INSERT INTO events (ts, visitor_id, session_id, type, path, target, label, value, lead_id) VALUES (?,?,?,?,?,?,?,?,?)');
$e = fn(int $m, string $v, string $s, string $type, string $p, ?string $x = null, ?string $l = null, ?int $n = null, ?int $ld = null)
    => $ev->execute([$t($m), $v, $s, $type, $p, $x, $l, $n, $ld]);
$e(0, $v1, $s1, 'page_view', '/');
$e(1, $v1, $s1, 'page_view', $g);
$e(2, $v1, $s1, 'scroll', $g, null, null, 25);
$e(2, $v1, $s1, 'scroll', $g, null, null, 50);
$e(3, $v1, $s1, 'click', $g, 'whatsapp', 'Chat on WhatsApp');
$e(3, $v1, $s1, 'form_start', $g, 'google_ads');
$e(4, $v1, $s1, 'engaged', $g, null, null, 60000);
$e(5, $v1, $s1, 'form_submit', $g, 'google_ads', null, null, $lead);
$e(10, $v2, $s2, 'page_view', '/');
$e(11, $v2, $s2, 'page_view', $g);
$e(12, $v2, $s2, 'page_view', '/');
$e(25, $v2, $s3, 'page_view', '/');
$e(26, $v2, $s3, 'page_view', $g);
$e(27, $v2, $s3, 'form_start', $g, 'google_ads');

$o = report_overview($db, $day, $day);
foreach (['visitors' => 2, 'sessions' => 3, 'wa' => 1, 'call' => 0, 'form_start' => 2, 'form_submit' => 1, 'leads' => 1, 'qualified' => 1, 'won' => 1] as $k => $want) {
    check($o[$k] === $want, "overview $k = " . json_encode($o[$k]) . ", want $want");
}
check(($o['revenue']['INR'] ?? null) == 50000, 'revenue INR wrong');
$ch = array_column($o['by_channel'], null, 'channel');
check($ch['Google Ads']['sessions'] === 1 && $ch['Google Ads']['leads'] === 1 && $ch['Google Ads']['won'] === 1, 'Google Ads channel row wrong');
check($ch['Direct']['sessions'] === 2 && $ch['Direct']['leads'] === 0, 'Direct channel row wrong');

$pages = array_column(report_pages($db, $day, $day), null, 'path');
check($pages[$g]['views'] === 3 && $pages[$g]['visitors'] === 2 && $pages[$g]['wa'] === 1, 'google-ads page counts wrong');
check($pages[$g]['form_start'] === 2 && $pages[$g]['form_submit'] === 1 && $pages[$g]['conv_pct'] === 50.0, 'google-ads conversion wrong');
check($pages[$g]['avg_engaged_s'] === 60 && $pages[$g]['scroll50_pct'] === 50.0, 'google-ads engagement wrong');
check($pages['/']['views'] === 4, 'home views wrong');
check(array_key_first($pages) === '/', 'pages not sorted by views');

$p = report_page($db, $g, $day, $day);
check($p['scroll'][25] === 1 && $p['scroll'][50] === 1 && $p['scroll'][75] === 0, 'page scroll wrong');
check(($p['sources']['Direct'] ?? 0) === 2 && ($p['sources']['Google Ads'] ?? 0) === 1, 'page sources wrong');
check(($p['clicks'][0]['target'] ?? '') === 'whatsapp' && $p['clicks'][0]['n'] === 1, 'page clicks wrong');

$vs = report_visitors($db, $day, $day, 1);
check(count($vs) === 2 && $vs[0]['id'] === $v2, 'visitors list wrong order');
$row1 = array_column($vs, null, 'id')[$v1];
check($row1['sessions'] === 1 && $row1['pages'] === 2 && $row1['lead_id'] === $lead, 'visitor row wrong');

$story = report_visitor($db, $v1);
check($story['visitor']['id'] === $v1 && count($story['sessions']) === 1, 'story sessions wrong');
$types = array_column($story['sessions'][0]['events'], 'type');
check($types[0] === 'page_view' && end($types) === 'form_submit', 'story events not in time order');
check(($story['leads'][0]['id'] ?? 0) === $lead, 'story lead missing');

if (!in_array('--keep', $argv, true)) {
    foreach (['events', 'sessions', 'visitors', 'leads'] as $tb) $db->exec("DELETE FROM $tb");
}
echo "reports ok\n";
