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
        } elseif ($won && $row['state'] === 'sent' && ((float) $row['value'] !== $value || $row['currency'] !== $currency)) {
            // the platform already counted this deal; sending it again would count it twice
            $db->prepare('UPDATE signals SET detail = ? WHERE id = ?')->execute(
                ["amount changed to $currency " . number_format((float) $value) . ' after it was sent: change it in the ad platform', $row['id']]);
            $changed++;
        } elseif ($row['state'] === 'failed' || ($won && $row['state'] === 'pending' && ((float) $row['value'] !== $value || $row['currency'] !== $currency))) {
            // not delivered yet: a new deal amount replaces the old one; a failed send gets another go
            $db->prepare("UPDATE signals SET value = ?, currency = ?, state = 'pending', tries = 0, detail = NULL WHERE id = ?")
                ->execute([$value, $currency, $row['id']]);
            $changed++;
        }
    }
    return $changed;
}

/** One HTTP call with a JSON body (or none). Never throws: curl errors come back as code 0. */
function http_json(string $method, string $url, array $headers = [], ?array $body = null, int $timeout = 10): array
{
    // a form body when the caller says so (OAuth token endpoint), JSON otherwise
    $form = in_array('Content-Type: application/x-www-form-urlencoded', $headers, true);
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_CUSTOMREQUEST => $method,
        CURLOPT_HTTPHEADER => array_merge($form ? ['Accept: application/json'] : ['Content-Type: application/json', 'Accept: application/json'], $headers),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => $timeout,
    ] + ($body !== null ? [CURLOPT_POSTFIELDS => $form ? http_build_query($body) : json_encode($body, JSON_UNESCAPED_UNICODE)] : []));
    $out = curl_exec($ch);
    $res = ['code' => (int) curl_getinfo($ch, CURLINFO_HTTP_CODE), 'body' => $out === false ? curl_error($ch) : (string) $out];
    curl_close($ch);
    return $res;
}

function sha_email(?string $email): ?string
{
    $e = strtolower(trim((string) $email));
    return $e === '' ? null : hash('sha256', $e);
}

function sha_phone(?string $phone): ?string
{
    // digits with the country code, no "+" and no leading zeros ("0091…" → "91…")
    $d = ltrim(preg_replace('/\D/', '', (string) $phone), '0');
    return $d === '' ? null : hash('sha256', $d);
}

/** "qualified-lead" / "won-deal": stable per lead and event, so platforms can de-duplicate. */
function signal_event_id(array $signal): string
{
    return 'sr-' . $signal['lead_id'] . '-' . strtolower(str_replace(' ', '-', $signal['event']));
}

/**
 * Deliver pending (and failed, fewer than 5 tries) signals for Meta, LinkedIn and
 * ChatGPT Ads. Each platform file defines {p}_configured($cfg), {p}_window_days()
 * and {p}_request($signal, $lead, $now, $cfg) → [method, url, headers, body].
 * Returns counts per platform and state. Never throws. With $leadId (panel
 * save) only that lead's pending signals go; retries are the nightly job's.
 */
function signals_send(PDO $db, array $cfg, ?callable $http = null, ?int $now = null, ?int $leadId = null): array
{
    $http ??= 'http_json';
    $now ??= time();
    $counts = [];
    $todo = $db->query("SELECT s.*, l.created_at AS lead_created_at FROM signals s JOIN leads l ON l.id = s.lead_id
        WHERE s.platform <> 'google' AND " . ($leadId === null ? "(s.state = 'pending' OR (s.state = 'failed' AND s.tries < 5))" : "s.state = 'pending' AND s.lead_id = " . $leadId) . ' ORDER BY s.id')->fetchAll();
    $save = $db->prepare('UPDATE signals SET state = ?, detail = ?, tries = ?, sent_at = ? WHERE id = ?');
    $leadQ = $db->prepare('SELECT * FROM leads WHERE id = ?');
    foreach ($todo as $sig) {
        $p = $sig['platform'];
        $tries = (int) $sig['tries'];
        if (function_exists("{$p}_window_days") && $now - strtotime($sig['created_at']) > ("{$p}_window_days")() * 86400) {
            $state = 'expired';
            $detail = 'older than the platform accepts';
        } elseif (!function_exists("{$p}_configured") || !("{$p}_configured")($cfg)) {
            // stays queued: it goes out once the keys are in api/config.php (until the window above closes)
            $state = 'pending';
            $detail = 'not configured';
        } else {
            $leadQ->execute([$sig['lead_id']]);
            $lead = $leadQ->fetch();
            $tries++;
            try {
                [$method, $url, $headers, $body] = ("{$p}_request")($sig, $lead, $now, $cfg);
                $res = $http($method, $url, $headers, $body);
                $ok = $res['code'] >= 200 && $res['code'] < 300;
                $state = $ok ? 'sent' : 'failed';
                $detail = $ok ? null : signal_error($res);
            } catch (Throwable $e) {
                $state = 'failed';
                $detail = mb_substr($e->getMessage(), 0, 300);
            }
        }
        $save->execute([$state, $detail, $tries, $state === 'sent' ? gmdate('c', $now) : null, $sig['id']]);
        $counts[$p][$detail === 'not configured' ? 'not configured' : $state] = ($counts[$p][$detail === 'not configured' ? 'not configured' : $state] ?? 0) + 1;
    }
    return $counts;
}

/** The platform's own error message, or the start of the response. */
function signal_error(array $res): string
{
    $j = json_decode($res['body'], true);
    $msg = $j['error']['message'] ?? $j['message'] ?? $j['error'] ?? null;
    return mb_substr(is_string($msg) ? $msg : "HTTP {$res['code']}: " . $res['body'], 0, 300);
}

foreach (['meta', 'linkedin', 'chatgpt-ads'] as $platformFile) {
    if (is_file(__DIR__ . "/$platformFile.php")) require_once __DIR__ . "/$platformFile.php";
}
