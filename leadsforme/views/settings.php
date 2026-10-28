<?php
// Settings: stop counting your own visits; check the nightly job. Included by ../index.php.
declare(strict_types=1);

// The cookie is read by site.js on sushantrana.com, so it is shared with the parent domain there.
$host = (string) ($_SERVER['HTTP_HOST'] ?? '');
$cookie = ['path' => '/', 'secure' => $https, 'samesite' => 'Lax'] + (str_ends_with($host, 'sushantrana.com') ? ['domain' => '.sushantrana.com'] : []);
if ($_SERVER['REQUEST_METHOD'] === 'POST' && $csrfOk() && isset($_POST['me'])) {
    $on = $_POST['me'] === 'on';
    setcookie('sr_me', $on ? '1' : '', ['expires' => $on ? time() + 365 * 86400 : time() - 3600] + $cookie);
    header('Location: ./?v=settings');
    exit;
}
$isMe = ($_COOKIE['sr_me'] ?? '') === '1';
$lastFile = leads_data_dir() . '/cron-daily.last';
$last = is_file($lastFile) ? trim((string) file_get_contents($lastFile)) : '';
$csrf = $h($_SESSION['csrf']);
ob_start(); ?>
<?= nav('settings', $h, $auth['user']) ?>
<section class="box" style="max-width:640px">
  <h1>Your own visits</h1>
  <p class="muted">Turn this on in every browser you use, so your own visits and tests do not count. Leads you send still arrive.</p>
  <p><strong><?= $isMe ? 'This browser is not counted.' : 'This browser is counted like any visitor.' ?></strong></p>
  <form method="post"><input type="hidden" name="csrf" value="<?= $csrf ?>">
    <?php if ($isMe): ?><button name="me" value="off">Count me again</button><?php else: ?><button name="me" value="on">This is me, don't count me</button><?php endif; ?>
  </form>
</section>
<section class="box" style="max-width:640px;margin-top:14px">
  <h1>Nightly job</h1>
  <p class="muted">Builds the daily totals and deletes data older than <?= LEADS_RETENTION_DAYS ?> days. Hostinger cron, daily at 02:30 IST:</p>
  <p><code>php ~/domains/sushantrana.com/public_html/api/cron-daily.php</code></p>
  <p><?= $last ? 'Last run: ' . $h($ist($last)) . ' IST' : '<strong>It has not run yet.</strong> Add the cron job in hPanel → Advanced → Cron Jobs.' ?></p>
</section>
<?php
page('Settings', (string) ob_get_clean(), true);
