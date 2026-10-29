<?php
/**
 * An access token for Google APIs (Search Console) from Sushant's own OAuth
 * client and refresh token in api/config.php. Service-account keys are blocked
 * by the sushantrana.com org policy, so this is the server's only way in.
 */

declare(strict_types=1);
require_once __DIR__ . '/signals.php';

function google_access_token(array $cfg, ?callable $http = null): ?string
{
    foreach (['GOOGLE_OAUTH_CLIENT_ID', 'GOOGLE_OAUTH_CLIENT_SECRET', 'GOOGLE_OAUTH_REFRESH_TOKEN'] as $k) {
        if (($cfg[$k] ?? '') === '') return null;
    }
    $cache = leads_data_dir() . '/google-token.json';
    $c = is_file($cache) ? json_decode((string) file_get_contents($cache), true) : null;
    if (is_array($c) && ($c['expires_at'] ?? 0) > time() + 60) return $c['access_token'];

    $http ??= 'http_json';
    $res = $http('POST', 'https://oauth2.googleapis.com/token', ['Content-Type: application/x-www-form-urlencoded'], [
        'grant_type' => 'refresh_token', 'client_id' => $cfg['GOOGLE_OAUTH_CLIENT_ID'],
        'client_secret' => $cfg['GOOGLE_OAUTH_CLIENT_SECRET'], 'refresh_token' => $cfg['GOOGLE_OAUTH_REFRESH_TOKEN']]);
    $j = json_decode($res['body'], true) ?: [];
    if ($res['code'] !== 200 || empty($j['access_token'])) {
        // invalid_grant / invalid_rapt: the Workspace wants a new login (Settings shows this)
        file_put_contents(leads_data_dir() . '/google-token.error', gmdate('c') . ' ' . mb_substr($res['body'], 0, 500));
        return null;
    }
    file_put_contents($cache, json_encode(['access_token' => $j['access_token'], 'expires_at' => time() + (int) ($j['expires_in'] ?? 3600)]), LOCK_EX);
    @unlink(leads_data_dir() . '/google-token.error');
    return $j['access_token'];
}
