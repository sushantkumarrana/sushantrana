<?php
/**
 * Signals: what the ad platforms are told when a lead is marked qualified or won.
 *
 * lead_set_status() queues one row per platform the lead carries a click ID
 * for; signals_send() (panel save, nightly cron) delivers Meta, LinkedIn and
 * ChatGPT ones; the Google Ads script pulls the Google ones (api/ads-google.php).
 */

declare(strict_types=1);
require_once __DIR__ . '/leads-db.php';

const SIGNAL_EVENTS = ['qualified' => 'Qualified lead', 'won' => 'Won deal'];

/** Platforms this lead can be reported to, from the click IDs it arrived with. */
function signal_platforms(array $lead): array
{
    $has = fn(string ...$keys) => (bool) array_filter($keys, fn($k) => ($lead[$k] ?? '') !== '' && $lead[$k] !== null);
    return array_keys(array_filter([
        'google' => $has('gclid', 'gbraid', 'wbraid'),
        'meta' => $has('fbclid'),
        'linkedin' => $has('li_fat_id'),
        'chatgpt' => $has('oppref'),
    ]));
}

/** Queue the lead's current status for every platform that brought it. Returns rows created or changed. */
function signal_enqueue(PDO $db, int $leadId): int
{
    $st = $db->prepare('SELECT * FROM leads WHERE id = ?');
    $st->execute([$leadId]);
    $lead = $st->fetch();
    $event = $lead ? (SIGNAL_EVENTS[$lead['status']] ?? null) : null;
    if (!$event) return 0;
    $won = $lead['status'] === 'won';
    $value = $won ? (float) $lead['value'] : null;
    $currency = $won ? $lead['currency'] : null;

    $changed = 0;
    $find = $db->prepare('SELECT * FROM signals WHERE lead_id = ? AND platform = ? AND event = ?');
    foreach (signal_platforms($lead) as $platform) {
        $find->execute([$leadId, $platform, $event]);
        $row = $find->fetch();
        if (!$row) {
            $db->prepare("INSERT INTO signals (lead_id, platform, event, value, currency, created_at, state) VALUES (?,?,?,?,?,?,'pending')")
                ->execute([$leadId, $platform, $event, $value, $currency, gmdate('c')]);
            $changed++;
        } elseif ($row['state'] === 'failed' || ($won && ((float) $row['value'] !== $value || $row['currency'] !== $currency))) {
            // a new deal amount is news for the platform; a failed send gets another go
            $db->prepare("UPDATE signals SET value = ?, currency = ?, state = 'pending', tries = 0, detail = NULL WHERE id = ?")
                ->execute([$value, $currency, $row['id']]);
            $changed++;
        }
    }
    return $changed;
}
