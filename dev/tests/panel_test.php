<?php
// Panel over HTTP: needs the local preview (port 8091) and a local panel
// login (PANEL_USER / PANEL_PASS, made once with the setup screen). Run:
//   LEADS_DATA_DIR=$PWD/.data PANEL_USER=… PANEL_PASS=… php dev/tests/panel_test.php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/leads-db.php';

$jar = tempnam(sys_get_temp_dir(), 'jar');
$get = function (string $url, ?array $post = null) use ($jar): string {
    $ch = curl_init("http://localhost:8091/leadsforme/$url");
    curl_setopt_array($ch, [CURLOPT_RETURNTRANSFER => true, CURLOPT_COOKIEJAR => $jar, CURLOPT_COOKIEFILE => $jar, CURLOPT_FOLLOWLOCATION => true]
        + ($post ? [CURLOPT_POST => true, CURLOPT_POSTFIELDS => http_build_query($post)] : []));
    return (string) curl_exec($ch);
};
preg_match('/name="csrf" value="([a-f0-9]+)"/', $get(''), $m);
$get('', ['csrf' => $m[1] ?? '', 'user' => getenv('PANEL_USER'), 'pass' => getenv('PANEL_PASS')]);
check(str_contains($get('?v=overview'), 'Overview'), 'could not log in to the local panel');

// A path sent to api/t.php by anyone ends up in the panel's page titles.
$evil = "/</title><meta http-equiv=refresh content='0;url=https://evil.example'>";
leads_db()->prepare("INSERT INTO events (ts, type, path) VALUES (?, 'page_view', ?)")->execute([gmdate('c'), $evil]);
$html = $get('?v=page&r=1&path=' . rawurlencode($evil));
leads_db()->prepare('DELETE FROM events WHERE path = ?')->execute([$evil]);
check(!str_contains($html, '<meta http-equiv=refresh'), 'raw path injected into the page');

echo "panel ok\n";
