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

echo "meta ok\n";
