<?php
// Visitors seen in the period, newest first, each opening to their story. Included by ../index.php.
declare(strict_types=1);

$pg = max(1, (int) ($_GET['p'] ?? 1));
$rows = report_visitors($db, $from, $to, $pg);
ob_start(); ?>
<?= nav('visitors', $h, $auth['user']) ?>
<?= $rangeForm('visitors') ?>
<?php if (!$rows): ?>
  <p class="empty">No identified visitors in this period yet.</p>
<?php else: ?>
<div class="scroll"><table class="rep">
  <tr><th>Last seen</th><th>Came first from</th><th>Country</th><th class="n">Visits</th><th class="n">Pages</th><th>Lead</th><th></th></tr>
  <?php foreach ($rows as $r): ?>
  <tr><td><?= $h($ist($r['last_seen'])) ?></td><td><?= $h($r['first_channel'] ?: '—') ?></td><td><?= $h($r['country'] ?: '—') ?></td>
      <td class="n"><?= $num($r['sessions']) ?></td><td class="n"><?= $num($r['pages']) ?></td>
      <td><?= $r['lead_id'] ? '<span class="chip">Lead</span>' : '<span class="muted">—</span>' ?></td>
      <td><a href="?v=visitor&amp;id=<?= $h($r['id']) ?>">Story →</a></td></tr>
  <?php endforeach; ?>
</table></div>
<nav class="pager">
  <?php if ($pg > 1): ?><a href="?v=visitors&amp;<?= $h($rangeQs) ?>&amp;p=<?= $pg - 1 ?>">← Newer</a><?php endif; ?>
  <?php if (count($rows) === REPORT_PAGE_SIZE): ?><a href="?v=visitors&amp;<?= $h($rangeQs) ?>&amp;p=<?= $pg + 1 ?>">Older →</a><?php endif; ?>
</nav>
<?php endif;
page('Visitors', (string) ob_get_clean(), true);
