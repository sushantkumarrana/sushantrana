<?php
// Field names from https://developers.openai.com/ads/conversions-api.md (checked 29 Oct 2026).
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/chatgpt-ads.php';

$db = leads_db();
$now = 1793300000;
$db->exec("INSERT INTO leads (created_at, name, email, phone, oppref, status, value, currency)
    VALUES ('" . gmdate('c', $now) . "', 'C', ' Op@Example.com', '0091 98765-43210', 'OPP1', 'won', 1999.5, 'USD')");
$id = (int) $db->lastInsertId();
$lead = $db->query("SELECT * FROM leads WHERE id = $id")->fetch();

$p = chatgpt_payload(['lead_id' => $id, 'event' => 'Won deal', 'value' => 1999.5, 'currency' => 'USD'], $lead, $now);
$e = $p['events'][0];
check($e['type'] === 'custom' && $e['custom_event_name'] === 'won_deal' && $e['id'] === "sr-$id-won-deal", 'event identity');
check($e['timestamp_ms'] === $now * 1000 && $e['action_source'] === 'offline' && $e['oppref'] === 'OPP1', 'time / source / oppref');
check($e['user']['emails_sha256'] === [hash('sha256', 'op@example.com')], 'email hash');
check($e['user']['phone_numbers_sha256'] === [hash('sha256', '919876543210')], 'phone hash (no + or leading zeros)');
check($e['data'] === ['type' => 'customer_action', 'amount' => 199950, 'currency' => 'USD'], 'won amount in minor units: ' . json_encode($e['data']));
$q = chatgpt_payload(['lead_id' => $id, 'event' => 'Qualified lead', 'value' => null, 'currency' => null], $lead, $now)['events'][0];
check($q['custom_event_name'] === 'qualified_lead' && $q['data'] === ['type' => 'customer_action'], 'qualified payload');
check(($p['integration_source'] ?? '') === 'sushantrana-panel', 'integration source');

$calls = [];
signal_enqueue($db, $id);
$cfg = ['OPENAI_ADS_PIXEL_ID' => 'px1', 'OPENAI_ADS_CONVERSIONS_KEY' => 'k1'];
signals_send($db, $cfg, function ($m, $u, $h, $b) use (&$calls) { $calls[] = compact('m', 'u', 'h'); return ['code' => 200, 'body' => '{}']; }, $now);
check(($calls[0]['u'] ?? '') === 'https://bzr.openai.com/v1/events?pid=px1' && in_array('Authorization: Bearer k1', $calls[0]['h'], true), 'chatgpt request');
check($db->query("SELECT state FROM signals WHERE lead_id = $id")->fetchColumn() === 'sent', 'chatgpt not sent');

$db->exec("UPDATE signals SET state = 'pending', tries = 0");
signals_send($db, [], fn() => ['code' => 200, 'body' => ''], $now);
check($db->query("SELECT state FROM signals WHERE lead_id = $id")->fetchColumn() === 'pending', 'unconfigured chatgpt not left pending');
check(chatgpt_window_days() === 7, 'chatgpt accepts 7 days');

echo "chatgpt ok\n";
