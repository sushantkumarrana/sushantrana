<?php
// Ad spend next to the leads and deals it brought, and Google search terms. Included by ../index.php.
declare(strict_types=1);

$rows = report_campaigns($db, $from, $to);
$terms = report_terms($db, $from, $to);
$platformName = ['google' => 'Google Ads', 'meta' => 'Meta Ads', 'linkedin' => 'LinkedIn Ads', 'chatgpt' => 'ChatGPT Ads'];
$money = fn(?float $v, ?string $cur) => $v === null ? '—' : trim(($cur ?? '') . ' ' . number_format($v));
$gCur = current(array_filter(array_column(array_filter($rows, fn($r) => $r['platform'] === 'google'), 'currency'))) ?: '';
ob_start(); ?>
<?= nav('campaigns', $h, $auth['user']) ?>
<?= $rangeForm('campaigns') ?>
<?php if (!$rows): ?>
  <p class="empty">No ad spend or ad leads in this period. Spend arrives nightly once the ad accounts are connected (Settings → Integrations).</p>
<?php else: ?>
<div class="scroll"><table class="rep">
  <tr><th>Campaign</th><th class="n">Spend</th><th class="n">Clicks</th><th class="n">Leads</th><th class="n">Qualified</th><th class="n">Won</th>
      <th class="n">Revenue</th><th class="n">Cost per lead</th><th class="n">Cost per won</th><th class="n">ROAS</th></tr>
  <?php foreach ($rows as $r): ?>
  <tr><td><a href="?v=leads&amp;campaign=<?= $h(rawurlencode($r['campaign'])) ?>"><?= $h($r['campaign']) ?></a><br><span class="muted small"><?= $h($platformName[$r['platform']] ?? $r['platform']) ?></span></td>
      <td class="n"><?= $h($money($r['cost'], $r['currency'])) ?></td><td class="n"><?= $num($r['clicks']) ?></td>
      <td class="n"><?= $num($r['leads']) ?></td><td class="n"><?= $num($r['qualified']) ?></td><td class="n"><?= $num($r['won']) ?></td>
      <td class="n"><?= $h($money($r['revenue'] ?: null, $r['currency'])) ?></td><td class="n"><?= $h($money($r['cpl'], $r['currency'])) ?></td>
      <td class="n"><?= $h($money($r['cost_per_won'], $r['currency'])) ?></td><td class="n"><?= $r['roas'] === null ? '—' : $h($r['roas'] . '×') ?></td></tr>
  <?php endforeach; ?>
</table></div>
<p class="muted small">Leads match a campaign by their utm_campaign (Google: from the click report). ROAS: won revenue ÷ spend, in the ad account's currency.</p>
<?php endif; ?>

<h2>Google search terms</h2>
<?php if (!$terms): ?>
  <p class="empty">No search terms in this period. The Google Ads script sends the last 7 days each night.</p>
<?php else: ?>
<div class="scroll"><table class="rep">
  <tr><th>Search term</th><th>Campaign</th><th class="n">Clicks</th><th class="n">Cost</th><th class="n">Google conversions</th></tr>
  <?php foreach ($terms as $t): ?>
  <tr><td><?= $h($t['term']) ?></td><td><?= $h($t['campaign']) ?></td><td class="n"><?= $num($t['clicks']) ?></td>
      <td class="n"><?= $h($money($t['cost'], $gCur)) ?></td><td class="n"><?= $h((string) (0 + $t['conversions'])) ?></td></tr>
  <?php endforeach; ?>
</table></div>
<?php endif;
page('Campaigns', (string) ob_get_clean(), true);
