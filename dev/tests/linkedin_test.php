<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/linkedin.php';

$db = leads_db();
$now = 1793300000;
$db->exec("INSERT INTO leads (created_at, name, email, phone, li_fat_id, status, value, currency)
    VALUES ('" . gmdate('c', $now) . "', 'L', 'Li@Example.com', '+911', 'LIFAT1', 'won', 2500, 'USD')");
$id = (int) $db->lastInsertId();
$lead = $db->query("SELECT * FROM leads WHERE id = $id")->fetch();
$cfg = ['LINKEDIN_ACCESS_TOKEN' => 'tok', 'LINKEDIN_CONVERSION_QUALIFIED' => '111', 'LINKEDIN_CONVERSION_WON' => '222', 'LINKEDIN_VERSION' => '202603'];

$won = linkedin_payload(['lead_id' => $id, 'event' => 'Won deal', 'value' => 2500.0, 'currency' => 'USD'], $lead, $now * 1000, $cfg);
check($won['conversion'] === 'urn:lla:llaPartnerConversion:222' && $won['conversionHappenedAt'] === $now * 1000, 'conversion urn / time');
check($won['eventId'] === "sr-$id-won-deal", 'eventId');
$ids = array_column($won['user']['userIds'], 'idValue', 'idType');
check($ids['SHA256_EMAIL'] === hash('sha256', 'li@example.com') && $ids['LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID'] === 'LIFAT1', 'user ids');
check($won['conversionValue'] === ['currencyCode' => 'USD', 'amount' => '2500'], 'won value: ' . json_encode($won['conversionValue'] ?? null));
$q = linkedin_payload(['lead_id' => $id, 'event' => 'Qualified lead', 'value' => null, 'currency' => null], $lead, $now * 1000, $cfg);
check($q['conversion'] === 'urn:lla:llaPartnerConversion:111' && !isset($q['conversionValue']), 'qualified payload');

$calls = [];
signal_enqueue($db, $id);
signals_send($db, $cfg, function ($m, $u, $h, $b) use (&$calls) { $calls[] = compact('m', 'u', 'h'); return ['code' => 201, 'body' => '']; }, $now);
check(count($calls) === 1 && $calls[0]['u'] === 'https://api.linkedin.com/rest/conversionEvents', 'linkedin url');
check(in_array('Authorization: Bearer tok', $calls[0]['h'], true) && in_array('LinkedIn-Version: 202603', $calls[0]['h'], true)
    && in_array('X-Restli-Protocol-Version: 2.0.0', $calls[0]['h'], true), 'linkedin headers: ' . json_encode($calls[0]['h']));
$state = fn() => $db->query("SELECT state, detail FROM signals WHERE lead_id = $id")->fetch();
check($state()['state'] === 'sent', 'linkedin not sent');

$db->exec("UPDATE signals SET state = 'pending', tries = 0");
signals_send($db, $cfg, fn() => ['code' => 401, 'body' => '{"message":"Invalid access token","status":401}'], $now);
check($state()['state'] === 'failed' && $state()['detail'] === 'Invalid access token', 'linkedin 401: ' . json_encode($state()));

$db->exec("UPDATE signals SET state = 'pending', tries = 0");
signals_send($db, ['LINKEDIN_ACCESS_TOKEN' => 'tok'], fn() => ['code' => 201, 'body' => ''], $now);
check($state()['state'] === 'pending' && $state()['detail'] === 'not configured', 'linkedin without conversion rules not left pending');

// spend import: analytics per campaign, names and currency looked up
$fake = function ($m, $u) {
    if (str_contains($u, '/adAnalytics')) return ['code' => 200, 'body' => json_encode(['elements' => [
        ['pivotValues' => ['urn:li:sponsoredCampaign:901'], 'costInLocalCurrency' => '45.20', 'clicks' => 12, 'impressions' => 3000]]])];
    if (str_contains($u, '/adCampaigns')) return ['code' => 200, 'body' => json_encode(['elements' => [['id' => 901, 'name' => 'B2B leads US']]])];
    if (preg_match('#/adAccounts/777$#', $u)) return ['code' => 200, 'body' => json_encode(['currency' => 'USD'])];
    return ['code' => 404, 'body' => '{}'];
};
$n = linkedin_import_spend($db, ['LINKEDIN_ACCESS_TOKEN' => 'tok', 'LINKEDIN_AD_ACCOUNT_ID' => '777'], '2026-10-28', $fake);
$r = $db->query("SELECT day, campaign, cost, clicks, currency FROM ad_spend WHERE platform = 'linkedin'")->fetch();
check($n === 1 && $r == ['day' => '2026-10-28', 'campaign' => 'B2B leads US', 'cost' => 45.2, 'clicks' => 12, 'currency' => 'USD'], 'linkedin spend: ' . json_encode($r));
check(linkedin_import_spend($db, ['LINKEDIN_ACCESS_TOKEN' => 'tok'], '2026-10-28', $fake) === 0, 'unconfigured linkedin spend imported');

echo "linkedin ok\n";
