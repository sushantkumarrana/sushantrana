<?php
/** Meta (Facebook + Instagram) Conversions API: qualified and won leads, and ad spend. */

declare(strict_types=1);
require_once __DIR__ . '/signals.php';

const META_GRAPH = 'https://graph.facebook.com/v21.0';

function meta_configured(array $cfg): bool
{
    return ($cfg['META_DATASET_ID'] ?? '') !== '' && ($cfg['META_ACCESS_TOKEN'] ?? '') !== '';
}

/** Meta takes server events up to 7 days old. */
function meta_window_days(): int
{
    return 7;
}

function meta_payload(array $signal, array $lead, int $now): array
{
    $user = array_filter([
        'em' => ($e = sha_email($lead['email'])) ? [$e] : null,
        'ph' => ($p = sha_phone($lead['phone'])) ? [$p] : null,
        'fbc' => $lead['fbclid'] ? 'fb.1.' . strtotime($lead['created_at']) * 1000 . '.' . $lead['fbclid'] : null,
    ]);
    $custom = ['lead_event_source' => 'sushantrana-panel', 'event_source' => 'crm'];
    if ($signal['event'] === 'Won deal') $custom += ['value' => (float) $signal['value'], 'currency' => $signal['currency']];
    return ['data' => [[
        'event_name' => $signal['event'], 'event_time' => $now, 'action_source' => 'system_generated',
        'event_id' => signal_event_id($signal), 'user_data' => $user, 'custom_data' => $custom,
    ]]];
}

function meta_request(array $signal, array $lead, int $now, array $cfg): array
{
    $url = META_GRAPH . '/' . rawurlencode($cfg['META_DATASET_ID']) . '/events?access_token=' . rawurlencode($cfg['META_ACCESS_TOKEN']);
    return ['POST', $url, [], meta_payload($signal, $lead, $now)];
}

/** Yesterday's (or any day's) spend per ad set into ad_spend. Returns rows stored; 0 when not configured. */
function meta_import_spend(PDO $db, array $cfg, string $day, ?callable $http = null): int
{
    if (($cfg['META_ACCESS_TOKEN'] ?? '') === '' || ($cfg['META_AD_ACCOUNT_ID'] ?? '') === '') return 0;
    $http ??= 'http_json';
    $url = META_GRAPH . '/act_' . rawurlencode($cfg['META_AD_ACCOUNT_ID']) . '/insights?' . http_build_query([
        'level' => 'adset', 'time_range' => json_encode(['since' => $day, 'until' => $day]), 'limit' => 500,
        'fields' => 'campaign_name,adset_name,spend,clicks,impressions,account_currency', 'access_token' => $cfg['META_ACCESS_TOKEN']]);
    $rows = [];
    for ($page = 0; $url && $page < 20; $page++) {
        $res = $http('GET', $url, [], null);
        if ($res['code'] !== 200) throw new RuntimeException('Meta insights: ' . signal_error($res));
        $j = json_decode($res['body'], true) ?: [];
        foreach ($j['data'] ?? [] as $r) {
            $rows[] = ['day' => $r['date_start'] ?? $day, 'platform' => 'meta', 'campaign' => $r['campaign_name'] ?? '', 'ad_group' => $r['adset_name'] ?? '',
                'cost' => $r['spend'] ?? 0, 'clicks' => $r['clicks'] ?? 0, 'impressions' => $r['impressions'] ?? 0, 'currency' => $r['account_currency'] ?? ''];
        }
        $url = $j['paging']['next'] ?? null;
    }
    require_once __DIR__ . '/ads-store.php';
    return ads_store_spend($db, $rows);
}
