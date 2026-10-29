<?php
// Leads (CRM). Included by ../index.php after login; uses its $db, $h, $flash, $auth.
declare(strict_types=1);

/* ---- filters ---- */
$f = [
    'q' => trim((string) ($_GET['q'] ?? '')),
    'channel' => (string) ($_GET['channel'] ?? ''),
    'form' => (string) ($_GET['form'] ?? ''),
    'status' => (string) ($_GET['status'] ?? ''),
    'campaign' => (string) ($_GET['campaign'] ?? ''),
    'from' => (string) ($_GET['from'] ?? ''),
    'to' => (string) ($_GET['to'] ?? ''),
];
$where = [];
$args = [];
if ($f['q'] !== '') {
    $where[] = '(name LIKE ? OR email LIKE ? OR phone LIKE ? OR business LIKE ? OR message LIKE ?)';
    array_push($args, ...array_fill(0, 5, '%' . $f['q'] . '%'));
}
foreach (['channel' => 'channel', 'form' => 'form', 'status' => 'status', 'campaign' => 'utm_campaign'] as $k => $col) {
    if ($f[$k] !== '') { $where[] = "$col = ?"; $args[] = $f[$k]; }
}
$istToUtc = fn(string $d, string $t) => (new DateTime("$d $t", new DateTimeZone(TZ)))->setTimezone(new DateTimeZone('UTC'))->format('c');
if (preg_match('/^\d{4}-\d{2}-\d{2}$/', $f['from'])) { $where[] = 'created_at >= ?'; $args[] = $istToUtc($f['from'], '00:00:00'); }
if (preg_match('/^\d{4}-\d{2}-\d{2}$/', $f['to'])) { $where[] = 'created_at <= ?'; $args[] = $istToUtc($f['to'], '23:59:59'); }
$sqlWhere = $where ? 'WHERE ' . implode(' AND ', $where) : '';

$ist = fn(string $utc) => (new DateTime($utc))->setTimezone(new DateTimeZone(TZ))->format('j M Y, g:i a');
$formLabel = fn(?string $v) => ['consultation' => 'Consultation form', 'shopify_store_development' => 'Shopify form', 'website_maintenance' => 'Maintenance form', 'manual' => 'Added by hand'][$v ?? ''] ?? ($v ?: '—');

/* ---- CSV export (same filters) ---- */
if ($action === 'csv') {
    $st = $db->prepare("SELECT * FROM leads $sqlWhere ORDER BY created_at DESC");
    $st->execute($args);
    header('Content-Type: text/csv; charset=utf-8');
    header('Content-Disposition: attachment; filename="leads-' . date('Y-m-d') . '.csv"');
    $out = fopen('php://output', 'w');
    fwrite($out, "\xEF\xBB\xBF"); // Excel reads UTF-8 with a BOM
    $first = true;
    while ($r = $st->fetch()) {
        $r['created_at'] = $ist($r['created_at']) . ' IST';
        if ($first) { fputcsv($out, array_keys($r), escape: ''); $first = false; }
        // Cells starting with = + - @ would run as formulas in Excel.
        fputcsv($out, array_map(fn($v) => is_string($v) && preg_match('/^[=+\-@]/', $v) && !preg_match('/^\+\d+$/', $v) ? "'$v" : $v, $r), escape: '');
    }
    exit;
}

$page = max(1, (int) ($_GET['p'] ?? 1));
$count = $db->prepare("SELECT COUNT(*) FROM leads $sqlWhere");
$count->execute($args);
$total = (int) $count->fetchColumn();
$st = $db->prepare("SELECT * FROM leads $sqlWhere ORDER BY created_at DESC LIMIT " . PAGE_SIZE . ' OFFSET ' . (($page - 1) * PAGE_SIZE));
$st->execute($args);
$rows = $st->fetchAll();
// what each lead's status told the ad platforms (api/signals.php)
$sigs = [];
if ($rows) {
    $sq = $db->prepare('SELECT * FROM signals WHERE lead_id IN (' . implode(',', array_fill(0, count($rows), '?')) . ') ORDER BY id');
    $sq->execute(array_column($rows, 'id'));
    foreach ($sq->fetchAll() as $sg) $sigs[$sg['lead_id']][] = $sg;
}
$platformName = ['google' => 'Google Ads', 'meta' => 'Meta Ads', 'linkedin' => 'LinkedIn Ads', 'chatgpt' => 'ChatGPT Ads'];

$byChannel = $db->query('SELECT channel, COUNT(*) n FROM leads GROUP BY channel ORDER BY n DESC')->fetchAll();
$channels = array_column($byChannel, 'channel');
$campaigns = $db->query('SELECT DISTINCT utm_campaign FROM leads WHERE utm_campaign IS NOT NULL ORDER BY utm_campaign')->fetchAll(PDO::FETCH_COLUMN);
$all = array_sum(array_column($byChannel, 'n'));
$qs = fn(array $over) => http_build_query(array_filter(array_merge(['v' => 'leads'], $f, $over), fn($v) => $v !== '' && $v !== null));
$back = $qs(['p' => $page > 1 ? $page : '']);

ob_start(); ?>
<?= nav('leads', $h, $auth['user']) ?>
<?php if ($flash): ?><p class="err"><?= $h($flash) ?></p><?php endif; ?>

<section class="cards">
  <a class="card<?= $f['channel'] === '' ? ' on' : '' ?>" href="?<?= $h($qs(['channel' => '', 'p' => ''])) ?>"><span><?= $all ?></span>All leads</a>
  <?php foreach ($byChannel as $c): ?>
    <a class="card<?= $f['channel'] === $c['channel'] ? ' on' : '' ?>" href="?<?= $h($qs(['channel' => $c['channel'], 'p' => ''])) ?>"><span><?= (int) $c['n'] ?></span><?= $h($c['channel']) ?></a>
  <?php endforeach; ?>
</section>

<form class="filters" method="get">
  <input type="search" name="q" value="<?= $h($f['q']) ?>" placeholder="Search name, email, phone, message…" aria-label="Search">
  <select name="channel" aria-label="Source"><option value="">All sources</option>
    <?php foreach ($channels as $c): ?><option<?= $f['channel'] === $c ? ' selected' : '' ?>><?= $h($c) ?></option><?php endforeach; ?>
  </select>
  <select name="form" aria-label="Form"><option value="">All forms</option>
    <?php foreach (array_filter($db->query('SELECT DISTINCT form FROM leads ORDER BY form')->fetchAll(PDO::FETCH_COLUMN)) as $v): ?><option value="<?= $v ?>"<?= $f['form'] === $v ? ' selected' : '' ?>><?= $formLabel($v) ?></option><?php endforeach; ?>
  </select>
  <select name="campaign" aria-label="Campaign"><option value="">All campaigns</option>
    <?php foreach ($campaigns as $c): ?><option<?= $f['campaign'] === $c ? ' selected' : '' ?>><?= $h($c) ?></option><?php endforeach; ?>
  </select>
  <select name="status" aria-label="Status"><option value="">Any status</option>
    <?php foreach (LEAD_STATUSES as $s): ?><option<?= $f['status'] === $s ? ' selected' : '' ?>><?= $s ?></option><?php endforeach; ?>
  </select>
  <label>From <input type="date" name="from" value="<?= $h($f['from']) ?>"></label>
  <label>To <input type="date" name="to" value="<?= $h($f['to']) ?>"></label>
  <button>Filter</button>
  <input type="hidden" name="v" value="leads">
  <a href="?v=leads">Reset</a>
  <a class="btn" href="?<?= $h($qs(['a' => 'csv', 'p' => ''])) ?>">Download CSV</a>
  <a class="btn" href="?v=lead-new">Add a lead</a>
</form>

<p class="muted small"><?= $total ?> lead<?= $total === 1 ? '' : 's' ?>. Times in IST. Leads older than <?= LEADS_RETENTION_DAYS ?> days are deleted automatically unless marked won.</p>

<?php if (!$rows): ?>
  <p class="empty">No leads yet<?= $where ? ' for these filters' : '' ?>.</p>
<?php else: ?>
<div class="table">
  <div class="row head"><div>Received</div><div>Lead</div><div>Project</div><div>Came from</div><div>Campaign</div><div>Status</div></div>
  <?php foreach ($rows as $r): ?>
  <details class="row-wrap">
    <summary class="row">
      <div><?= $h($ist($r['created_at'])) ?></div>
      <div><strong><?= $h($r['name']) ?></strong><br><span class="muted"><?= $h($r['email']) ?> · <?= $h($r['phone']) ?></span></div>
      <div><?= $h($r['service'] ?: '—') ?><br><span class="muted"><?= $h($formLabel($r['form'])) ?> · <?= $h($r['page']) ?></span></div>
      <div><span class="chip"><?= $h($r['channel']) ?></span></div>
      <div><?= $r['utm_campaign'] ? '<strong>' . $h($r['utm_campaign']) . '</strong>' : '<span class="muted">—</span>' ?><?php if ($r['utm_content'] || $r['utm_term']): ?><br><span class="muted"><?= $h(implode(' · ', array_filter([$r['utm_content'], $r['utm_term']]))) ?></span><?php endif; ?></div>
      <div><span class="st st-<?= $h($r['status']) ?>"><?= $h($r['status']) ?></span><?php if ($r['status'] === 'won' && $r['value']): ?><br><span class="muted"><?= $h($r['currency'] . ' ' . number_format((float) $r['value'])) ?></span><?php endif; ?></div>
    </summary>
    <div class="detail">
      <dl>
        <?php foreach ([
            'Business / website' => $r['business'], 'Enquiry type' => $r['enquiry_type'], 'Sent from page' => $r['page'],
            'First page of visit' => $r['landing_page'], 'Pages this visit' => $r['journey'] ?? null, 'Referrer' => $r['referrer'], 'utm_source' => $r['utm_source'],
            'utm_medium' => $r['utm_medium'], 'utm_campaign' => $r['utm_campaign'], 'utm_term' => $r['utm_term'],
            'utm_content' => $r['utm_content'], 'Ad group' => $r['ad_group'], 'Keyword' => $r['keyword'], 'Google click ID (gclid)' => $r['gclid'],
            'Facebook click ID (fbclid)' => $r['fbclid'], 'LinkedIn click ID' => $r['li_fat_id'], 'ChatGPT click ID (oppref)' => $r['oppref'] ?? null,
            'Device' => $r['user_agent'],
        ] as $k => $v): if ($v === null || $v === '') continue; ?>
          <dt><?= $h($k) ?></dt><dd><?= $h($v) ?></dd>
        <?php endforeach; ?>
      </dl>
      <?php if ($r['message']): ?><div class="msg"><?= nl2br($h($r['message'])) ?></div><?php endif; ?>
      <?php if ($sigs[$r['id']] ?? null): ?>
      <div class="scroll"><table class="rep"><tr><th>Told</th><th>Event</th><th>State</th><th>Sent</th></tr>
        <?php foreach ($sigs[$r['id']] as $sg): ?>
        <tr><td><?= $h($platformName[$sg['platform']] ?? $sg['platform']) ?></td><td><?= $h($sg['event']) ?><?= $sg['value'] !== null ? ' · ' . $h($sg['currency'] . ' ' . number_format((float) $sg['value'])) : '' ?></td>
            <td><?= $h($sg['state']) ?><?= $sg['detail'] ? '<br><span class="muted">' . $h($sg['detail']) . '</span>' : '' ?></td><td><?= $sg['sent_at'] ? $h($ist($sg['sent_at'])) : '—' ?></td></tr>
        <?php endforeach; ?>
      </table></div>
      <?php endif; ?>
      <div class="actions">
        <a class="btn" href="mailto:<?= $h($r['email']) ?>">Email</a>
        <a class="btn" href="tel:<?= $h($r['phone']) ?>">Call</a>
        <a class="btn" href="https://wa.me/<?= $h(preg_replace('/\D/', '', $r['phone'])) ?>" target="_blank" rel="noopener">WhatsApp</a>
        <?php if ($r['visitor_id']): ?><a class="btn" href="?v=visitor&amp;id=<?= $h($r['visitor_id']) ?>">Story</a><?php endif; ?>
        <form method="post" class="inline">
          <input type="hidden" name="csrf" value="<?= $h($_SESSION['csrf']) ?>">
          <input type="hidden" name="id" value="<?= (int) $r['id'] ?>">
          <input type="hidden" name="back" value="<?= $h($back) ?>">
          <label>Status <select name="status"><?php foreach (LEAD_STATUSES as $s): ?><option<?= $r['status'] === $s ? ' selected' : '' ?>><?= $s ?></option><?php endforeach; ?></select></label>
          <label>Deal amount (for won) <input name="value" inputmode="decimal" size="9" value="<?= $h($r['value'] !== null ? (string) (0 + $r['value']) : '') ?>"></label>
          <label>Currency <select name="currency"><?php foreach (LEAD_CURRENCIES as $c): ?><option<?= ($r['currency'] ?: 'INR') === $c ? ' selected' : '' ?>><?= $c ?></option><?php endforeach; ?></select></label>
          <button>Save</button>
        </form>
      </div>
    </div>
  </details>
  <?php endforeach; ?>
</div>
<?php if ($total > PAGE_SIZE): ?>
  <nav class="pager">
    <?php if ($page > 1): ?><a href="?<?= $h($qs(['p' => $page - 1])) ?>">← Newer</a><?php endif; ?>
    <span class="muted">Page <?= $page ?> of <?= (int) ceil($total / PAGE_SIZE) ?></span>
    <?php if ($page * PAGE_SIZE < $total): ?><a href="?<?= $h($qs(['p' => $page + 1])) ?>">Older →</a><?php endif; ?>
  </nav>
<?php endif; ?>
<?php endif;
page('All leads', (string) ob_get_clean(), true);

