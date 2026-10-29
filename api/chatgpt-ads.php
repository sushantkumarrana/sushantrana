<?php
/**
 * ChatGPT Ads (OpenAI) Conversions API: qualified and won leads.
 * Field names: https://developers.openai.com/ads/conversions-api.md
 */

declare(strict_types=1);
require_once __DIR__ . '/signals.php';

function chatgpt_configured(array $cfg): bool
{
    return ($cfg['OPENAI_ADS_PIXEL_ID'] ?? '') !== '' && ($cfg['OPENAI_ADS_CONVERSIONS_KEY'] ?? '') !== '';
}

/** timestamp_ms must be within the last 7 days. */
function chatgpt_window_days(): int
{
    return 7;
}

function chatgpt_payload(array $signal, array $lead, int $now): array
{
    $user = array_filter([
        'emails_sha256' => ($e = sha_email($lead['email'])) ? [$e] : null,
        'phone_numbers_sha256' => ($p = sha_phone($lead['phone'])) ? [$p] : null,
    ]);
    $data = ['type' => 'customer_action'];
    if ($signal['event'] === 'Won deal') {
        // minor units: 1999.50 USD → 199950
        $data += ['amount' => (int) round((float) $signal['value'] * 100), 'currency' => $signal['currency']];
    }
    $event = array_filter([
        'id' => signal_event_id($signal), 'type' => 'custom',
        'custom_event_name' => strtolower(str_replace(' ', '_', $signal['event'])),
        'timestamp_ms' => $now * 1000, 'action_source' => 'offline', 'oppref' => $lead['oppref'] ?: null,
        'user' => $user ?: null, 'data' => $data,
    ], fn($v) => $v !== null);
    return ['integration_source' => 'sushantrana-panel', 'events' => [$event]];
}

function chatgpt_request(array $signal, array $lead, int $now, array $cfg): array
{
    return ['POST', 'https://bzr.openai.com/v1/events?pid=' . rawurlencode($cfg['OPENAI_ADS_PIXEL_ID']),
        ['Authorization: Bearer ' . $cfg['OPENAI_ADS_CONVERSIONS_KEY']], chatgpt_payload($signal, $lead, $now)];
}
