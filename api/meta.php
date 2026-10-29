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
