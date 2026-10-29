<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/meta.php';

$db = leads_db();
$now = 1793300000;
$db->exec("INSERT INTO leads (created_at, name, email, phone, fbclid, status, value, currency)
    VALUES ('2026-10-29T10:00:00+00:00', 'M', 'Me@Example.com ', '+91 98765-43210', 'FBCLID1', 'won', 50000, 'INR')");
$id = (int) $db->lastInsertId();
$lead = $db->query("SELECT * FROM leads WHERE id = $id")->fetch();

$won = meta_payload(['lead_id' => $id, 'event' => 'Won deal', 'value' => 50000.0, 'currency' => 'INR'], $lead, $now)['data'][0];
check($won['event_name'] === 'Won deal' && $won['event_time'] === $now && $won['action_source'] === 'system_generated', 'meta event basics');
check($won['event_id'] === "sr-$id-won-deal", 'meta event_id');
check($won['user_data']['em'] === [hash('sha256', 'me@example.com')], 'email not normalised and hashed');
check($won['user_data']['ph'] === [hash('sha256', '919876543210')], 'phone not normalised and hashed');
check($won['user_data']['fbc'] === 'fb.1.' . strtotime('2026-10-29T10:00:00+00:00') * 1000 . '.FBCLID1', 'fbc format');
check($won['custom_data']['value'] === 50000.0 && $won['custom_data']['currency'] === 'INR', 'won value');
$q = meta_payload(['lead_id' => $id, 'event' => 'Qualified lead', 'value' => null, 'currency' => null], $lead, $now)['data'][0];
check(!isset($q['custom_data']['value']) && !isset($q['custom_data']['currency']), 'qualified carries a value');
check(!str_contains(json_encode($won), 'Example.com') && !str_contains(json_encode($won), '98765'), 'clear PII in payload');

$cfg = ['META_DATASET_ID' => '123', 'META_ACCESS_TOKEN' => 'tok'];
$calls = [];
$ok = function (string $method, string $url, array $headers, ?array $body) use (&$calls) { $calls[] = compact('method', 'url', 'body'); return ['code' => 200, 'body' => '{"events_received":1}']; };
$sig = fn() => $db->query("SELECT state, detail, tries, sent_at FROM signals WHERE lead_id = $id AND platform = 'meta'")->fetch();

signal_enqueue($db, $id);
$res = signals_send($db, $cfg, $ok, $now);
check(count($calls) === 1 && $calls[0]['method'] === 'POST' && str_starts_with($calls[0]['url'], 'https://graph.facebook.com/v21.0/123/events?access_token=tok'), 'meta request: ' . json_encode($calls));
check($sig()['state'] === 'sent' && $sig()['sent_at'], 'meta not marked sent');
check(($res['meta']['sent'] ?? 0) === 1, 'result counts');

$db->exec("UPDATE signals SET state = 'pending', tries = 0");
signals_send($db, $cfg, fn() => ['code' => 400, 'body' => '{"error":{"message":"Invalid token"}}'], $now);
check($sig()['state'] === 'failed' && $sig()['detail'] === 'Invalid token' && (int) $sig()['tries'] === 1, 'meta 400 not recorded: ' . json_encode($sig()));

$db->exec("UPDATE signals SET state = 'pending', tries = 0");
signals_send($db, $cfg, function () { throw new RuntimeException('timeout'); }, $now);
check($sig()['state'] === 'failed' && str_contains((string) $sig()['detail'], 'timeout'), 'exception not recorded');

$db->exec("UPDATE signals SET state = 'pending', tries = 0");
signals_send($db, ['META_DATASET_ID' => ''], $ok, $now);
check($sig()['state'] === 'skipped' && $sig()['detail'] === 'not configured', 'unconfigured meta not skipped');

$db->exec("UPDATE signals SET state = 'pending', created_at = '" . gmdate('c', $now - 8 * 86400) . "'");
signals_send($db, $cfg, $ok, $now);
check($sig()['state'] === 'expired', 'meta older than 7 days not expired');

// spend import: one ad set row per day, paged
$pages = [
  ['data' => [['campaign_name' => 'Leads IN', 'adset_name' => 'Chandigarh 25-45', 'spend' => '812.40', 'clicks' => '41', 'impressions' => '5200', 'account_currency' => 'INR', 'date_start' => '2026-10-28']],
   'paging' => ['next' => 'https://graph.facebook.com/v21.0/next-page']],
  ['data' => [['campaign_name' => 'Leads IN', 'adset_name' => 'Mohali', 'spend' => '100', 'clicks' => '5', 'impressions' => '700', 'account_currency' => 'INR', 'date_start' => '2026-10-28']]],
];
$urls = [];
$fake = function ($m, $u) use (&$pages, &$urls) { $urls[] = $u; return ['code' => 200, 'body' => json_encode(array_shift($pages))]; };
$n = meta_import_spend($db, ['META_ACCESS_TOKEN' => 'tok', 'META_AD_ACCOUNT_ID' => '555'], '2026-10-28', $fake);
check($n === 2 && str_contains($urls[0], '/act_555/insights?') && str_contains($urls[0], 'level=adset'), 'meta spend import: ' . json_encode($urls));
$r = $db->query("SELECT platform, campaign, ad_group, cost, clicks, currency FROM ad_spend WHERE platform = 'meta' ORDER BY ad_group")->fetchAll();
check(count($r) === 2 && $r[0]['ad_group'] === 'Chandigarh 25-45' && (float) $r[0]['cost'] === 812.4 && $r[0]['currency'] === 'INR', 'meta spend rows: ' . json_encode($r));
$called = false;
check(meta_import_spend($db, ['META_ACCESS_TOKEN' => 'tok'], '2026-10-28', function () use (&$called) { $called = true; return ['code' => 200, 'body' => '{}']; }) === 0 && !$called, 'unconfigured meta spend called out');

echo "meta ok\n";
