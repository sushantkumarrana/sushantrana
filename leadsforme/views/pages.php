<?php
// Every page of the site with its visits, attention and actions. Included by ../index.php.
declare(strict_types=1);

$rows = report_pages($db, $from, $to);
$maxV = max([1, ...array_column($rows, 'views')]);
ob_start(); ?>
<?= nav('pages', $h, $auth['user']) ?>
<?= $rangeForm('pages') ?>
<?php if (!$rows): ?>
  <p class="empty">No page views in this period yet.</p>
<?php else: ?>
<div class="scroll"><table class="rep">
  <tr><th>Page</th><th>Views</th><th class="n">Visitors</th><th class="n">Avg. time</th><th class="n">Read half</th>
      <th class="n">WhatsApp</th><th class="n">Calls</th><th class="n">Forms started</th><th class="n">Forms sent</th><th class="n">Conversion</th></tr>
  <?php foreach ($rows as $r): ?>
  <tr><td><a href="?v=page&amp;path=<?= $h(rawurlencode($r['path'])) ?>&amp;<?= $h($rangeQs) ?>"><?= $h($r['path']) ?></a></td>
      <td><?= $bar($r['views'], $maxV) . $num($r['views']) ?></td><td class="n"><?= $num($r['visitors']) ?></td>
      <td class="n"><?= $dur($r['avg_engaged_s']) ?></td><td class="n"><?= $r['scroll50_pct'] ?>%</td>
      <td class="n"><?= $num($r['wa']) ?></td><td class="n"><?= $num($r['call']) ?></td>
      <td class="n"><?= $num($r['form_start']) ?></td><td class="n"><?= $num($r['form_submit']) ?></td><td class="n"><?= $r['conv_pct'] ?>%</td></tr>
  <?php endforeach; ?>
</table></div>
<p class="muted small">Read half: visitors who scrolled at least halfway. Conversion: forms sent ÷ visitors.</p>
<?php endif;
page('Pages', (string) ob_get_clean(), true);
