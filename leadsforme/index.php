<?php
/**
 * leadsforme.sushantrana.com — private panel for the website's leads.
 *
 * First visit: a one-time setup screen (needs PANEL_SETUP_CODE from
 * api/config.php) where you choose your own username and password. After
 * that: login, then the leads table. Forgot the password? Delete
 * ~/leads-data/panel-auth.json in File Manager and run setup again.
 */

declare(strict_types=1);

require dirname(__DIR__) . '/api/leads-db.php';

$config = is_file(dirname(__DIR__) . '/api/config.php') ? require dirname(__DIR__) . '/api/config.php' : [];
$https = ($_SERVER['HTTPS'] ?? '') === 'on' || ($_SERVER['HTTP_X_FORWARDED_PROTO'] ?? '') === 'https';

header('X-Robots-Tag: noindex, nofollow');
header('X-Frame-Options: DENY');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: no-referrer');
header("Content-Security-Policy: default-src 'none'; style-src 'unsafe-inline'; form-action 'self'; frame-ancestors 'none'; base-uri 'none'");
header('Cache-Control: no-store');

session_name('lfm');
session_set_cookie_params(['lifetime' => 0, 'path' => '/', 'secure' => $https, 'httponly' => true, 'samesite' => 'Strict']);
session_start();

const AUTH_FILE = 'panel-auth.json';
const IDLE_LIMIT = 8 * 3600;
const PAGE_SIZE = 50;
const TZ = 'Asia/Kolkata';

$authPath = leads_data_dir() . '/' . AUTH_FILE;
$auth = is_file($authPath) ? json_decode((string) file_get_contents($authPath), true) : null;
$action = $_GET['a'] ?? '';
$h = fn($v) => htmlspecialchars((string) $v, ENT_QUOTES, 'UTF-8');

if (empty($_SESSION['csrf'])) $_SESSION['csrf'] = bin2hex(random_bytes(16));
$csrfOk = fn() => hash_equals($_SESSION['csrf'], (string) ($_POST['csrf'] ?? ''));

/* ---- login throttle: 5 failures per 15 minutes per IP ---- */
$ip = $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$failFile = leads_data_dir() . '/login-fail-' . md5($ip);
$fails = array_filter(is_file($failFile) ? (json_decode((string) file_get_contents($failFile), true) ?: []) : [], fn($t) => time() - $t < 900);
$locked = count($fails) >= 5;

$error = '';

/* ---- one-time setup ---- */
if (!$auth) {
    $code = (string) ($config['PANEL_SETUP_CODE'] ?? '');
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && $csrfOk() && !$locked) {
        $user = trim((string) ($_POST['user'] ?? ''));
        $pass = (string) ($_POST['pass'] ?? '');
        if ($code === '' || !hash_equals($code, (string) ($_POST['code'] ?? ''))) {
            $fails[] = time();
            file_put_contents($failFile, json_encode(array_values($fails)));
            $error = 'That setup code is not right.';
        } elseif (!preg_match('/^[A-Za-z0-9._@-]{3,60}$/', $user)) {
            $error = 'Username: 3–60 letters, numbers or . _ @ -';
        } elseif (strlen($pass) < 10) {
            $error = 'Password must be at least 10 characters.';
        } elseif ($pass !== (string) ($_POST['pass2'] ?? '')) {
            $error = 'The two passwords do not match.';
        } else {
            file_put_contents($authPath, json_encode(['user' => $user, 'hash' => password_hash($pass, PASSWORD_DEFAULT)]), LOCK_EX);
            chmod($authPath, 0600);
            header('Location: ./');
            exit;
        }
    }
    page('Set up your panel', setup_form($h, $error, $code === '', $locked));
}

/* ---- login / logout ---- */
if ($action === 'logout' && $_SERVER['REQUEST_METHOD'] === 'POST' && $csrfOk()) {
    $_SESSION = [];
    session_destroy();
    header('Location: ./');
    exit;
}

$loggedIn = ($_SESSION['user'] ?? '') === $auth['user'] && time() - ($_SESSION['seen'] ?? 0) < IDLE_LIMIT;
if (!$loggedIn) {
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && $csrfOk()) {
        if ($locked) {
            $error = 'Too many wrong attempts. Try again in 15 minutes.';
        } elseif (hash_equals($auth['user'], (string) ($_POST['user'] ?? '')) && password_verify((string) ($_POST['pass'] ?? ''), $auth['hash'])) {
            @unlink($failFile);
            session_regenerate_id(true);
            $_SESSION['user'] = $auth['user'];
            $_SESSION['seen'] = time();
            header('Location: ./');
            exit;
        } else {
            $fails[] = time();
            file_put_contents($failFile, json_encode(array_values($fails)));
            $error = 'Wrong username or password.';
        }
    }
    page('Sign in', login_form($h, $error));
}
$_SESSION['seen'] = time();

/* ---- changes ---- */
$db = leads_db();
leads_purge();
$flash = (string) ($_SESSION['flash'] ?? '');
unset($_SESSION['flash']);
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $csrfOk() && isset($_POST['status'])) {
    $err = lead_set_status($db, (int) ($_POST['id'] ?? 0), (string) $_POST['status'], (string) ($_POST['value'] ?? ''), (string) ($_POST['currency'] ?? ''));
    if ($err) $_SESSION['flash'] = $err;
    header('Location: ./?' . (string) ($_POST['back'] ?? ''));
    exit;
}
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $csrfOk() && $action === 'lead-new') {
    try {
        lead_add_manual($db, $_POST);
        header('Location: ./?v=leads');
    } catch (InvalidArgumentException $e) {
        $_SESSION['flash'] = $e->getMessage();
        $_SESSION['draft'] = array_intersect_key($_POST, array_flip(['name', 'email', 'phone', 'business', 'service', 'message', 'channel']));
        header('Location: ./?v=lead-new');
    }
    exit;
}

/* ---- views (views/*.php, each ends with page()) ---- */
$view = (string) ($_GET['v'] ?? 'leads');
if (!preg_match('/^[a-z-]+$/', $view) || !is_file(__DIR__ . "/views/$view.php")) $view = 'leads';
require __DIR__ . "/views/$view.php";


/* ------------------------------------------------------------------ */

function setup_form(callable $h, string $error, bool $noCode, bool $locked): string
{
    if ($noCode) {
        return '<div class="box"><h1>Panel not ready</h1><p>Add <code>PANEL_SETUP_CODE</code> to <code>api/config.php</code> on the server, then reload this page.</p></div>';
    }
    $csrf = $h($_SESSION['csrf']);
    $err = $locked ? '<p class="err">Too many wrong attempts. Try again in 15 minutes.</p>' : ($error ? '<p class="err">' . $h($error) . '</p>' : '');
    return <<<HTML
<form class="box" method="post" autocomplete="off">
  <h1>Create your login</h1>
  <p class="muted">This screen shows only once. Choose the username and password you will use to open your leads.</p>
  $err
  <input type="hidden" name="csrf" value="$csrf">
  <label>Setup code<input name="code" required autocomplete="off"></label>
  <label>Username<input name="user" required autocomplete="username"></label>
  <label>Password (10+ characters)<input type="password" name="pass" required minlength="10" autocomplete="new-password"></label>
  <label>Password again<input type="password" name="pass2" required minlength="10" autocomplete="new-password"></label>
  <button>Create login</button>
</form>
HTML;
}

function login_form(callable $h, string $error): string
{
    $csrf = $h($_SESSION['csrf']);
    $err = $error ? '<p class="err">' . $h($error) . '</p>' : '';
    return <<<HTML
<form class="box" method="post">
  <h1>Leads</h1>
  <p class="muted">Sign in to see your website's leads.</p>
  $err
  <input type="hidden" name="csrf" value="$csrf">
  <label>Username<input name="user" required autofocus autocomplete="username"></label>
  <label>Password<input type="password" name="pass" required autocomplete="current-password"></label>
  <button>Sign in</button>
</form>
HTML;
}

function nav(string $active, callable $h, string $user): string
{
    $links = '';
    foreach (['leads' => 'Leads'] as $v => $label) {
        $links .= '<a href="?v=' . $v . '"' . ($v === $active ? ' class="on" aria-current="page"' : '') . ">$label</a>";
    }
    $csrf = $h($_SESSION['csrf']);
    $u = $h($user);
    return <<<HTML
<header class="top">
  <nav class="tabs"><strong>sushantrana.com</strong>$links</nav>
  <div><span class="muted">$u</span> · <form method="post" action="?a=logout" style="display:inline"><input type="hidden" name="csrf" value="$csrf"><button type="submit" class="linkbtn">Sign out</button></form></div>
</header>
HTML;
}

function page(string $title, string $body, bool $wide = false): never
{
    $cls = $wide ? 'wide' : 'narrow';
    echo <<<HTML
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>$title · Leads</title>
<style>
:root{--ink:#0a0a0a;--body:#3a3a3a;--muted:#777;--line:#e6e3df;--bg:#f6f4f1;--card:#fff;--o:#ff4d00;--o-soft:rgba(255,77,0,.1)}
@media (prefers-color-scheme:dark){:root{--ink:#f2f0ed;--body:#d6d2cc;--muted:#9a958e;--line:#2c2a27;--bg:#121110;--card:#1b1a18;--o-soft:rgba(255,77,0,.18)}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--body);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
a,.linkbtn{color:var(--o)}.linkbtn{background:none;border:0;padding:0;font:inherit;cursor:pointer}.muted{color:var(--muted)}.small{font-size:13px}main{margin:0 auto;padding:24px 16px}
main.narrow{max-width:420px;padding-top:12vh}main.wide{max-width:1200px}
h1{color:var(--ink);font-size:22px;margin:0 0 6px}
.box{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:28px;display:grid;gap:14px}
label{display:grid;gap:6px;font-size:13px;font-weight:600;color:var(--ink)}
input,select{font:inherit;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;min-width:0}
input:focus,select:focus,button:focus-visible,a:focus-visible,summary:focus-visible{outline:2px solid var(--o);outline-offset:2px}
button,.btn{font:600 14px/1 system-ui,sans-serif;background:var(--o);color:#fff;border:0;border-radius:10px;padding:11px 16px;cursor:pointer;text-decoration:none;display:inline-block}
.err{background:var(--o-soft);color:var(--o);border-radius:8px;padding:10px 12px;margin:0;font-weight:600}
code{background:var(--o-soft);padding:1px 5px;border-radius:5px}
.top{display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap;margin-bottom:18px;color:var(--ink)}
.cards{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px;color:var(--body);text-decoration:none;font-size:13px;display:grid;min-width:110px}
.card span{font-size:22px;font-weight:700;color:var(--ink)}.card.on{border-color:var(--o);box-shadow:0 0 0 1px var(--o)}
.filters{display:flex;flex-wrap:wrap;gap:8px;align-items:end;margin-bottom:10px}
.filters input[type=search]{flex:1 1 240px}.filters label{font-weight:500}
.table{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.row{display:grid;grid-template-columns:140px 1.4fr 1.2fr 1fr 1fr 96px;gap:12px;padding:12px 16px;align-items:start;font-size:14px}
.head{font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);border-bottom:1px solid var(--line)}
.row-wrap{border-bottom:1px solid var(--line)}.row-wrap:last-child{border-bottom:0}
summary.row{cursor:pointer;list-style:none}summary.row::-webkit-details-marker{display:none}summary.row:hover{background:var(--o-soft)}
.row strong{color:var(--ink)}
.chip{display:inline-block;background:var(--o-soft);color:var(--o);font-weight:600;font-size:12px;border-radius:100px;padding:3px 9px}
.st{display:inline-block;font-size:12px;font-weight:700;text-transform:uppercase;border-radius:6px;padding:3px 8px;background:var(--line);color:var(--ink)}
.st-new{background:var(--o);color:#fff}.st-qualified{background:#2563c9;color:#fff}.st-won{background:#1f8a4c;color:#fff}.st-wrong,.st-lost{opacity:.6}
.tabs{display:flex;gap:14px;align-items:center;flex-wrap:wrap}.tabs a{color:var(--body);text-decoration:none;font-weight:600}.tabs a.on{color:var(--o)}
.detail{padding:4px 16px 18px}
dl{display:grid;grid-template-columns:200px 1fr;gap:6px 14px;margin:0 0 12px;font-size:14px}dt{color:var(--muted)}dd{margin:0;word-break:break-word;color:var(--ink)}
.msg{white-space:normal;background:var(--bg);border-left:3px solid var(--o);border-radius:0 8px 8px 0;padding:12px 14px;margin-bottom:12px}
.actions{display:flex;gap:8px;flex-wrap:wrap;align-items:end}.inline{display:flex;gap:8px;align-items:end}.inline label{font-weight:500}
.empty{background:var(--card);border:1px dashed var(--line);border-radius:14px;padding:40px;text-align:center}
.pager{display:flex;gap:16px;justify-content:center;margin-top:16px}
@media (max-width:820px){.row{grid-template-columns:1fr 1fr}.head{display:none}dl{grid-template-columns:1fr}dt{margin-top:6px}}
</style></head><body><main class="$cls">$body</main></body></html>
HTML;
    exit;
}
