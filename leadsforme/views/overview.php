<?php
// Whole-site dashboard. Included by ../index.php after login.
declare(strict_types=1);

$o = report_overview($db, $from, $to);
$money = $o['revenue'] ? implode(' + ', array_map(fn($c, $v) => $c . ' ' . $num($v), array_keys($o['revenue']), $o['revenue'])) : '—';
$maxS = max([1, ...array_column($o['by_channel'], 'sessions')]);
ob_start(); ?>
<?= nav('overview', $h, $auth['user']) ?>
<?= $rangeForm('overview') ?>
<section class="kpis">
  <?php foreach ([
      'Visitors' => $num($o['visitors']), 'Visits' => $num($o['sessions']), 'WhatsApp clicks' => $num($o['wa']),
      'Call clicks' => $num($o['call']), 'Forms started' => $num($o['form_start']), 'Forms sent' => $num($o['form_submit']),
      'Leads' => $num($o['leads']), 'Qualified' => $num($o['qualified']), 'Won' => $num($o['won']), 'Revenue' => $money,
  ] as $label => $value): ?>
    <div class="kpi"><b><?= $h($value) ?></b><span><?= $h($label) ?></span></div>
  <?php endforeach; ?>
</section>
<p class="muted small">Visitors counts people the site may identify (everyone outside Europe, and those in Europe who accepted). Visits, clicks and forms include everyone.</p>

<h2>Where visits and leads came from</h2>
<?php if (!$o['by_channel']): ?>
  <p class="empty">No visits in this period yet.</p>
<?php else: ?>
<div class="scroll"><table class="rep">
  <tr><th>Source</th><th>Visits</th><th class="n">Leads</th><th class="n">Won</th></tr>
  <?php foreach ($o['by_channel'] as $c): ?>
  <tr><td><?= $h($c['channel'] ?: 'Unknown') ?></td><td><?= $bar($c['sessions'], $maxS) . $num($c['sessions']) ?></td>
      <td class="n"><?= $num($c['leads']) ?></td><td class="n"><?= $num($c['won']) ?></td></tr>
  <?php endforeach; ?>
</table></div>
<?php endif;
page('Overview', (string) ob_get_clean(), true);
