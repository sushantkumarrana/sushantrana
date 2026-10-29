<?php
// Needs the local preview (.claude/launch.json → sushantrana-html, port 8091)
// and no api/config.php, so nothing is emailed. Run:
//   LEADS_DATA_DIR=$PWD/.data php dev/tests/lead_test.php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/leads-db.php';

function post_lead(array $body): array
{
    $ch = curl_init('http://localhost:8091/api/lead.php');
    curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => ['Content-Type: application/json'], CURLOPT_POSTFIELDS => json_encode($body)]);
    $out = json_decode((string) curl_exec($ch), true);
    return is_array($out) ? $out : [];
}

$base = ['name' => 'Lead Test', 'email' => 'leadtest@gmail.com', 'phone' => '9876543210', 'phoneCountry' => 'IN',
    'form' => 'google_ads', 'sourcePath' => '/services/google-ads/', 'journey' => ['/', '/services/google-ads/']];
$vid = str_repeat('d', 32);

$res = post_lead($base + ['visitorId' => $vid, 'attribution' => ['landing_page' => '/', 'li_fat_id' => 'abc', 'oppref' => 'op1', 'gbraid' => 'gb1']]);
check(($res['ok'] ?? false) === true && is_int($res['lead'] ?? null), 'no lead id in response: ' . json_encode($res));
$row = leads_db()->query('SELECT visitor_id, li_fat_id, oppref, gbraid FROM leads WHERE id = ' . $res['lead'])->fetch();
check($row['oppref'] === 'op1' && $row['gbraid'] === 'gb1', 'oppref / gbraid not stored');
check($row['visitor_id'] === $vid, 'visitor_id not stored');
check($row['li_fat_id'] === 'abc', 'li_fat_id not stored');

$res2 = post_lead($base + ['visitorId' => 'bad']);
check(($res2['ok'] ?? false) === true, 'lead with a bad visitor id refused');
check(leads_db()->query('SELECT visitor_id FROM leads WHERE id = ' . (int) ($res2['lead'] ?? 0))->fetchColumn() === null, 'bad visitor id stored');

leads_db()->exec("DELETE FROM leads WHERE email = 'leadtest@gmail.com'");
echo "lead ok\n";
