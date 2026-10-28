<?php
// Add a lead that came in outside the website. Included by ../index.php after login.
declare(strict_types=1);

$d = $_SESSION['draft'] ?? [];
unset($_SESSION['draft']);
$val = fn(string $k) => $h((string) ($d[$k] ?? ''));
ob_start(); ?>
<?= nav('leads', $h, $auth['user']) ?>
<form class="box" method="post" action="?a=lead-new" style="max-width:560px">
  <h1>Add a lead</h1>
  <p class="muted">For enquiries that came by WhatsApp, Telegram, a call, a LinkedIn message or a referral.</p>
  <?php if ($flash): ?><p class="err"><?= $h($flash) ?></p><?php endif; ?>
  <input type="hidden" name="csrf" value="<?= $h($_SESSION['csrf']) ?>">
  <label>Came from <select name="channel" required>
    <?php foreach (MANUAL_CHANNELS as $c): ?><option<?= ($d['channel'] ?? '') === $c ? ' selected' : '' ?>><?= $h($c) ?></option><?php endforeach; ?>
  </select></label>
  <label>Name <input name="name" required value="<?= $val('name') ?>"></label>
  <label>Phone <input name="phone" inputmode="tel" value="<?= $val('phone') ?>"></label>
  <label>Email <input name="email" type="email" value="<?= $val('email') ?>"></label>
  <label>Business <input name="business" value="<?= $val('business') ?>"></label>
  <label>Service <input name="service" value="<?= $val('service') ?>"></label>
  <label>Notes <textarea name="message" rows="4" style="font:inherit;border:1px solid var(--line);border-radius:10px;padding:10px 12px;background:var(--card);color:var(--ink)"><?= $val('message') ?></textarea></label>
  <button>Save lead</button>
  <a href="?v=leads">Cancel</a>
</form>
<?php
page('Add a lead', (string) ob_get_clean(), true);
