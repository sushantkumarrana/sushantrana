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
