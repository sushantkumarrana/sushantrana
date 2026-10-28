<?php
// One page in detail: sources, scroll depth, what people clicked. Included by ../index.php.
declare(strict_types=1);

$path = (string) ($_GET['path'] ?? '/');
if (!str_starts_with($path, '/')) $path = '/';
$p = report_page($db, $path, $from, $to);
$maxSrc = max([1, ...array_values($p['sources'])]);
$maxScroll = max([1, ...array_values($p['scroll'])]);
$clickName = ['whatsapp' => 'WhatsApp', 'call' => 'Call', 'email' => 'Email', 'cta' => 'Button', 'outbound' => 'Link out'];
ob_start(); ?>
<?= nav('pages', $h, $auth['user']) ?>
<p><a href="?v=pages&amp;<?= $h($rangeQs) ?>">← All pages</a></p>
<h1><?= $h($path) ?> <a class="small" href="https://sushantrana.com<?= $h($path) ?>" target="_blank" rel="noopener">open ↗</a></h1>
<?= $rangeForm('page', ['path' => $path]) ?>
<section class="kpis">
  <?php foreach ([
      'Views' => $num($p['views'] ?? 0), 'Visitors' => $num($p['visitors'] ?? 0), 'Avg. time' => $dur((int) ($p['avg_engaged_s'] ?? 0)),
      'Read half' => ($p['scroll50_pct'] ?? 0) . '%', 'WhatsApp clicks' => $num($p['wa'] ?? 0), 'Call clicks' => $num($p['call'] ?? 0),
      'Forms started' => $num($p['form_start'] ?? 0), 'Forms sent' => $num($p['form_submit'] ?? 0), 'Conversion' => ($p['conv_pct'] ?? 0) . '%',
  ] as $label => $value): ?>
    <div class="kpi"><b><?= $h($value) ?></b><span><?= $h($label) ?></span></div>
  <?php endforeach; ?>
</section>

<h2>Where its visitors came from</h2>
<?php if (!$p['sources']): ?><p class="empty">No identified visits to this page in this period.</p><?php else: ?>
<div class="scroll"><table class="rep"><tr><th>Source</th><th>Visits that saw this page</th></tr>
  <?php foreach ($p['sources'] as $ch => $n): ?><tr><td><?= $h($ch ?: 'Unknown') ?></td><td><?= $bar($n, $maxSrc) . $num($n) ?></td></tr><?php endforeach; ?>
</table></div><?php endif; ?>

<h2>How far people scrolled</h2>
<div class="scroll"><table class="rep"><tr><th>Reached</th><th>Times</th></tr>
  <?php foreach ($p['scroll'] as $depth => $n): ?><tr><td><?= $depth ?>%</td><td><?= $bar($n, $maxScroll) . $num($n) ?></td></tr><?php endforeach; ?>
</table></div>

<h2>What people clicked</h2>
<?php if (!$p['clicks']): ?><p class="empty">No WhatsApp, call, email, button or outbound clicks on this page in this period.</p><?php else: ?>
<div class="scroll"><table class="rep"><tr><th>Kind</th><th>Link or button</th><th class="n">Clicks</th></tr>
  <?php foreach ($p['clicks'] as $c): ?><tr><td><?= $h($clickName[$c['target']] ?? $c['target']) ?></td><td><?= $h($c['label'] ?: '—') ?></td><td class="n"><?= $num($c['n']) ?></td></tr><?php endforeach; ?>
</table></div><?php endif;
page($path, (string) ob_get_clean(), true);
