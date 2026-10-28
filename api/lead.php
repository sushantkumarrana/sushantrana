<?php
/**
 * POST /api/lead.php — every lead form on the site posts here.
 *
 * PHP port of the old Next.js route (app/api/lead/route.ts), same contract:
 * JSON in, {"ok":true} or {"ok":false,"error":..., "field":...} out.
 *
 * Storing (Supabase) and notifying (Resend email) are independent: either one
 * alone still delivers the lead, and only when both fail does the visitor see
 * an error.
 */

declare(strict_types=1);
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

require __DIR__ . '/catalog.php';
require __DIR__ . '/lead-email.php';
require __DIR__ . '/leads-db.php';

$config = is_file(__DIR__ . '/config.php') ? require __DIR__ . '/config.php' : [];
$cfg = fn(string $k) => $config[$k] ?? getenv($k) ?: '';

const FROM = 'Sushant Rana Website <leads@sushantrana.com>';

function reply(array $body, int $status = 200): never
{
    http_response_code($status);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') reply(['ok' => false, 'error' => 'Method not allowed.'], 405);

/* ---- throttle: 5 per minute per IP, kept in the temp dir ---- */
// ponytail: file-per-IP in sys temp; move to the DB if abuse ever outgrows it.
// Last X-Forwarded-For entry: the CDN appends the real client IP; the first
// entries are whatever the visitor sent, so a bot could rotate them.
$xff = array_filter(array_map('trim', explode(',', $_SERVER['HTTP_X_FORWARDED_FOR'] ?? '')));
$ip = end($xff) ?: ($_SERVER['REMOTE_ADDR'] ?? 'unknown');
$hitFile = sys_get_temp_dir() . '/sr-lead-' . md5($ip);
$now = time();
$hits = array_filter(
    is_file($hitFile) ? (json_decode((string) file_get_contents($hitFile), true) ?: []) : [],
    fn($t) => $now - $t < 60
);
$hits[] = $now;
@file_put_contents($hitFile, json_encode(array_values($hits)));
if (count($hits) > 5) reply(['ok' => false, 'error' => 'Too many requests. Please try again shortly.'], 429);

/* ---- input ---- */
$body = json_decode((string) file_get_contents('php://input'), true);
if (!is_array($body)) $body = [];
$clean = fn(string $k, int $max = 2000) => is_string($body[$k] ?? null) ? mb_substr(trim($body[$k]), 0, $max) : '';

// Honeypot: pretend success so bots don't learn they were caught.
if ($clean('company_website') !== '') reply(['ok' => true]);

$name = $clean('name', 120);
$email = $clean('email', 200);
$phone = $clean('phone', 40);
$business = $clean('business', 200);
$message = $clean('message', 4000);
$sourcePath = $clean('sourcePath', 300) ?: '/';
$form = preg_replace('/[^a-z_]/', '', $clean('form', 40));

// First-touch attribution the browser kept since landing (site.js, sr_attr).
$attrIn = is_array($body['attribution'] ?? null) ? $body['attribution'] : [];
$attr = [];
foreach (['landing_page', 'referrer', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid', 'fbclid', 'li_fat_id'] as $k) {
    $attr[$k] = is_string($attrIn[$k] ?? null) ? mb_substr(trim($attrIn[$k]), 0, 300) : '';
}
$channel = lead_channel($attr);
// The visitor's story in the site's own analytics (site.js trackIds), when counted.
$visitorId = preg_match('/^[a-f0-9]{32}$/', (string) ($body['visitorId'] ?? '')) ? $body['visitorId'] : null;

// Pages this visit went through, oldest first (site.js, sr_journey).
$journeyIn = is_array($body['journey'] ?? null) ? $body['journey'] : [];
$journey = mb_substr(implode(' > ', array_map(
    fn($p) => mb_substr(trim($p), 0, 200),
    array_filter(array_slice($journeyIn, -30), 'is_string')
)), 0, 4000);

// Allow-list both dropdowns: an unknown value means a tampered payload.
$service = $clean('service', 120);
if ($service !== OTHER_SERVICE && !in_array($service, ALL_SERVICES, true)) $service = '';
$enquiryType = $clean('enquiryType', 40);
if (!isset(ENQUIRY_TYPES[$enquiryType])) $enquiryType = '';
$country = strtoupper($clean('phoneCountry', 2));
if (!isset(COUNTRY_DIAL[$country])) $country = 'IN';

if ($name === '' || $email === '' || $phone === '') {
    reply(['ok' => false, 'error' => 'Name, email and phone are required.'], 400);
}

/* ---- email: same rules as the browser, plus a DNS check it can't do ---- */
$emailError = validate_email($email);
if ($emailError) reply(['ok' => false, 'field' => 'email', 'error' => $emailError], 400);

$domain = strtolower(substr($email, strrpos($email, '@') + 1));
if (!checkdnsrr($domain, 'MX') && !checkdnsrr($domain, 'A') && !checkdnsrr($domain, 'AAAA')) {
    reply(['ok' => false, 'field' => 'email', 'error' => "No mail server exists for \"$domain\". Please check the spelling."], 400);
}

/* ---- phone ---- */
// ponytail: length check only; the browser already validated the number
// against the country's real numbering plan with libphonenumber. Add a PHP
// libphonenumber port if direct POSTs with junk numbers become a problem.
$national = preg_replace('/\D+/', '', $phone);
if (strlen($national) < 4) reply(['ok' => false, 'field' => 'phone', 'error' => 'That number is too short.'], 400);
if (strlen($national) > 15) reply(['ok' => false, 'field' => 'phone', 'error' => 'That number is too long.'], 400);
$phoneE164 = '+' . COUNTRY_DIAL[$country] . ltrim($national, '0');

/* ---- store ---- */
$typeLabel = ENQUIRY_TYPES[$enquiryType] ?? 'Enquiry';
$received = (new DateTime('now', new DateTimeZone('Asia/Kolkata')))->format('j/n/Y, g:i:s a') . ' IST';

function http_json(string $url, array $headers, array $payload, int $timeout = 8): int
{
    $ch = curl_init($url);
    curl_setopt_array($ch, [
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => array_merge(['Content-Type: application/json'], $headers),
        CURLOPT_POSTFIELDS => json_encode($payload, JSON_UNESCAPED_UNICODE),
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT => $timeout,
    ]);
    curl_exec($ch);
    $code = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    return $code;
}

$stored = false;
$leadId = null;
$url = $cfg('SUPABASE_URL');
$key = $cfg('SUPABASE_PUBLISHABLE_KEY');
if ($url && $key) {
    $code = http_json(rtrim($url, '/') . '/rest/v1/leads', ["apikey: $key", "Authorization: Bearer $key", 'Prefer: return=minimal'], [
        'name' => $name,
        'email' => $email,
        'phone' => $phoneE164,
        'business' => $business ?: null,
        'service' => $service ?: null,
        'enquiry_type' => $enquiryType ?: null,
        'message' => $message ?: null,
        'source_path' => $sourcePath,
        'referrer' => mb_substr($_SERVER['HTTP_REFERER'] ?? '', 0, 300) ?: null,
        'user_agent' => mb_substr($_SERVER['HTTP_USER_AGENT'] ?? '', 0, 300) ?: null,
    ]);
    $stored = $code >= 200 && $code < 300;
    if (!$stored) error_log("[lead] insert failed: HTTP $code");
} else {
    error_log('[lead] Supabase config missing — relying on email');
}

// The panel's own copy, with where the lead came from.
try {
    $nul = fn(string $v) => $v === '' ? null : $v;
    leads_db()->prepare(
        'INSERT INTO leads (created_at, form, name, email, phone, business, service, enquiry_type, message, page,
            landing_page, journey, referrer, channel, utm_source, utm_medium, utm_campaign, utm_term, utm_content, gclid, fbclid, user_agent,
            visitor_id, li_fat_id)
         VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
    )->execute([
        gmdate('c'), $nul($form), $name, $email, $phoneE164, $nul($business), $nul($service), $nul($enquiryType), $nul($message), $sourcePath,
        $nul($attr['landing_page']), $nul($journey), $nul($attr['referrer']), $channel, $nul($attr['utm_source']), $nul($attr['utm_medium']),
        $nul($attr['utm_campaign']), $nul($attr['utm_term']), $nul($attr['utm_content']), $nul($attr['gclid']), $nul($attr['fbclid']),
        mb_substr($_SERVER['HTTP_USER_AGENT'] ?? '', 0, 300) ?: null,
        $visitorId, $nul($attr['li_fat_id']),
    ]);
    $leadId = (int) leads_db()->lastInsertId();
    $stored = true;
    leads_purge();
} catch (Throwable $e) {
    error_log('[lead] panel insert failed: ' . $e->getMessage());
}

/* ---- notify ---- */
$to = $cfg('LEAD_NOTIFY_TO') ?: 'me@sushantrana.com';
$d = compact('name', 'email', 'business', 'service', 'typeLabel', 'enquiryType', 'message', 'sourcePath', 'channel', 'journey') + [
    'landingPage' => $attr['landing_page'],
    'phone' => $phoneE164,
    'receivedAt' => $received,
];

$emailed = false;
$resend = $cfg('RESEND_API_KEY');
if ($resend) {
    $subject = ($stored ? '' : '[NOT SAVED] ') . "New $typeLabel — " . ($service ?: 'general') . " — $name" . ($business ? " ($business)" : '');
    $code = http_json('https://api.resend.com/emails', ["Authorization: Bearer $resend"], [
        'from' => FROM,
        'to' => $to,
        'reply_to' => $email,
        'subject' => $subject,
        'html' => lead_email_html($d),
        'text' => lead_email_text($d),
    ]);
    $emailed = $code >= 200 && $code < 300;
    if (!$emailed) error_log("[lead] email failed: HTTP $code");
} else {
    error_log('[lead] RESEND_API_KEY missing — no email sent');
}

if (!$stored && !$emailed) {
    error_log('[lead] LEAD LOST — not stored, not emailed: ' . json_encode($d, JSON_UNESCAPED_UNICODE));
    reply(['ok' => false, 'error' => "Something went wrong. Please email me directly at $to."], 500);
}

reply(['ok' => true, 'lead' => $leadId]);

/* ------------------------------------------------------------------ */

function validate_email(string $raw): ?string
{
    $email = trim($raw);
    if ($email === '') return 'Email is required.';
    if (preg_match('/\s/', $email)) return "An email address can't contain spaces.";
    if (strlen($email) > 254) return 'That email address is too long.';
    $at = substr_count($email, '@');
    if ($at === 0) return "That's not an email address — it needs an @ sign.";
    if ($at > 1) return 'An email address can only have one @ sign.';
    [$local, $domain] = explode('@', $email);
    if ($local === '') return 'Add the part before the @ sign.';
    if (strlen($local) > 64) return 'The part before the @ is too long.';
    if ($domain === '') return 'Add the part after the @ sign, like gmail.com.';
    if (!str_contains($domain, '.')) return 'The domain needs a dot in it, like gmail.com.';
    if (str_contains($email, '..')) return "An email address can't contain two dots in a row.";
    if (str_starts_with($local, '.') || str_ends_with($local, '.')) return "An email address can't start or end the name with a dot.";
    if (!preg_match('/^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,63}$/', $email)) {
        return "That doesn't look like a valid email address.";
    }
    if (in_array(strtolower($domain), DISPOSABLE_DOMAINS, true)) {
        return 'Please use a permanent email address — I need to be able to reply.';
    }
    return null;
}
