<?php
/** LinkedIn Conversions API: qualified and won leads, and ad spend. */

declare(strict_types=1);
require_once __DIR__ . '/signals.php';

function linkedin_configured(array $cfg): bool
{
    return ($cfg['LINKEDIN_ACCESS_TOKEN'] ?? '') !== '' && ($cfg['LINKEDIN_CONVERSION_QUALIFIED'] ?? '') !== ''
        && ($cfg['LINKEDIN_CONVERSION_WON'] ?? '') !== '';
}

function linkedin_window_days(): int
{
    return 90;
}

function linkedin_headers(array $cfg): array
{
    return ['Authorization: Bearer ' . $cfg['LINKEDIN_ACCESS_TOKEN'], 'LinkedIn-Version: ' . (($cfg['LINKEDIN_VERSION'] ?? '') ?: '202603'),
        'X-Restli-Protocol-Version: 2.0.0'];
}

function linkedin_payload(array $signal, array $lead, int $nowMs, array $cfg): array
{
    $rule = $signal['event'] === 'Won deal' ? $cfg['LINKEDIN_CONVERSION_WON'] : $cfg['LINKEDIN_CONVERSION_QUALIFIED'];
    $ids = [];
    if ($e = sha_email($lead['email'])) $ids[] = ['idType' => 'SHA256_EMAIL', 'idValue' => $e];
    if ($lead['li_fat_id']) $ids[] = ['idType' => 'LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID', 'idValue' => $lead['li_fat_id']];
    $body = ['conversion' => "urn:lla:llaPartnerConversion:$rule", 'conversionHappenedAt' => $nowMs,
        'user' => ['userIds' => $ids], 'eventId' => signal_event_id($signal)];
    if ($signal['event'] === 'Won deal') {
        $body['conversionValue'] = ['currencyCode' => $signal['currency'], 'amount' => (string) (0 + $signal['value'])];
    }
    return $body;
}

function linkedin_request(array $signal, array $lead, int $now, array $cfg): array
{
    return ['POST', 'https://api.linkedin.com/rest/conversionEvents', linkedin_headers($cfg), linkedin_payload($signal, $lead, $now * 1000, $cfg)];
}

/** One day's spend per campaign into ad_spend. Returns rows stored; 0 when not configured. */
function linkedin_import_spend(PDO $db, array $cfg, string $day, ?callable $http = null): int
{
    if (($cfg['LINKEDIN_ACCESS_TOKEN'] ?? '') === '' || ($cfg['LINKEDIN_AD_ACCOUNT_ID'] ?? '') === '') return 0;
    $http ??= 'http_json';
    $acct = rawurlencode($cfg['LINKEDIN_AD_ACCOUNT_ID']);
    $get = function (string $url) use ($http, $cfg) {
        $res = $http('GET', $url, linkedin_headers($cfg), null);
        if ($res['code'] !== 200) throw new RuntimeException('LinkedIn: ' . signal_error($res));
        return json_decode($res['body'], true) ?: [];
    };
    [$y, $m, $d] = array_map('intval', explode('-', $day));
    $range = "(start:(year:$y,month:$m,day:$d),end:(year:$y,month:$m,day:$d))";
    $stats = $get("https://api.linkedin.com/rest/adAnalytics?q=analytics&pivot=CAMPAIGN&timeGranularity=DAILY&dateRange=$range"
        . "&accounts=List(urn%3Ali%3AsponsoredAccount%3A$acct)&fields=pivotValues,costInLocalCurrency,clicks,impressions");
    $names = array_column($get("https://api.linkedin.com/rest/adAccounts/$acct/adCampaigns?q=search&fields=id,name")['elements'] ?? [], 'name', 'id');
    $currency = $get("https://api.linkedin.com/rest/adAccounts/$acct")['currency'] ?? '';
    $rows = [];
    foreach ($stats['elements'] ?? [] as $e) {
        $cid = (string) preg_replace('/\D/', '', (string) ($e['pivotValues'][0] ?? ''));
        $rows[] = ['day' => $day, 'platform' => 'linkedin', 'campaign' => $names[$cid] ?? $names[(int) $cid] ?? "Campaign $cid", 'ad_group' => '',
            'cost' => $e['costInLocalCurrency'] ?? 0, 'clicks' => $e['clicks'] ?? 0, 'impressions' => $e['impressions'] ?? 0, 'currency' => $currency];
    }
    require_once __DIR__ . '/ads-store.php';
    return ads_store_spend($db, $rows);
}
