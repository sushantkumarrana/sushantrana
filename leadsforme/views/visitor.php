<?php
// One visitor's story: every visit, every page, every click, and their lead. Included by ../index.php.
declare(strict_types=1);

$id = (string) ($_GET['id'] ?? '');
$s = preg_match('/^[a-f0-9]{32}$/', $id) ? report_visitor($db, $id) : ['visitor' => null];
$clickName = ['whatsapp' => 'WhatsApp', 'call' => 'a phone number', 'email' => 'an email address', 'cta' => 'the button', 'outbound' => 'a link out'];
$say = function (array $e) use ($h, $dur, $clickName): string {
    $page = '<code>' . $h($e['path']) . '</code>';
    return match ($e['type']) {
        'page_view' => "Opened $page",
        'scroll' => 'Scrolled ' . (int) $e['value'] . "% of $page",
        'engaged' => 'Spent ' . $dur(intdiv((int) $e['value'], 1000)) . " on $page",
        'click' => 'Clicked ' . $h($clickName[$e['target']] ?? $e['target']) . ($e['label'] ? ' “' . $h($e['label']) . '”' : '') . " on $page",
        'form_start' => "Started filling the form on $page",
        'form_submit' => "<strong>Sent the form</strong> on $page",
        default => $h($e['type']) . " on $page",
    };
};
ob_start(); ?>
<?= nav('visitors', $h, $auth['user']) ?>
<p><a href="?v=visitors">← All visitors</a></p>
<?php if (!$s['visitor']): ?>
  <p class="empty">This visitor's story is not available. Stories are kept for <?= LEADS_RETENTION_DAYS ?> days.</p>
<?php else: $v = $s['visitor']; ?>
<h1>Visitor from <?= $h($v['country'] ?: 'an unknown country') ?></h1>
<p class="muted">First seen <?= $h($ist($v['first_seen'])) ?> via <?= $h($v['first_channel'] ?: 'unknown') ?> · last seen <?= $h($ist($v['last_seen'])) ?></p>
<?php foreach ($s['leads'] as $l): ?>
  <p><span class="st st-<?= $h($l['status']) ?>"><?= $h($l['status']) ?></span> Lead: <strong><?= $h($l['name']) ?></strong>
     (<?= $h($l['form']) ?>, <?= $h($ist($l['created_at'])) ?>)<?= $l['status'] === 'won' && $l['value'] ? ' · ' . $h($l['currency'] . ' ' . $num($l['value'])) : '' ?>
     · <a href="?v=leads&amp;q=<?= $h(rawurlencode($l['name'])) ?>">open in Leads</a></p>
<?php endforeach; ?>
<?php foreach ($s['sessions'] as $i => $x): $sess = $x['session']; ?>
  <section class="sess">
    <h2>Visit <?= $i + 1 ?> · <?= $h($ist($sess['started_at'])) ?></h2>
    <p class="muted small">From <?= $h($sess['channel'] ?: 'unknown') ?><?= $sess['utm_campaign'] ? ' · campaign ' . $h($sess['utm_campaign']) : '' ?> · landed on <code><?= $h($sess['landing']) ?></code> · <?= $h($sess['device'] ?: '') ?></p>
    <ol class="story">
      <?php foreach ($x['events'] as $e): ?><li><time><?= $h($ist($e['ts'], 'g:i:s a')) ?></time><?= $say($e) ?></li><?php endforeach; ?>
    </ol>
  </section>
<?php endforeach; ?>
<?php endif;
page('Visitor story', (string) ob_get_clean(), true);
