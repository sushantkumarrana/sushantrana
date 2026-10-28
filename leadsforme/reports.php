<?php
/**
 * Report queries for the panel. Dates are IST days (Y-m-d), both ends included.
 * They read the raw tables, which hold the last 90 days (leads_purge);
 * the daily rollups (api/cron-daily.php) keep totals beyond that.
 */

declare(strict_types=1);

/** [from, to] as UTC ISO strings comparable with the stored timestamps. */
function report_range(string $from, string $to): array
{
    $utc = fn(string $d, string $t) => (new DateTime("$d $t", new DateTimeZone('Asia/Kolkata')))->setTimezone(new DateTimeZone('UTC'))->format('c');
    return [$utc($from, '00:00:00'), $utc($to, '23:59:59')];
}

function report_overview(PDO $db, string $from, string $to): array
{
    $r = report_range($from, $to);
    $one = function (string $sql) use ($db, $r): int {
        $st = $db->prepare($sql);
        $st->execute($r);
        return (int) $st->fetchColumn();
    };
    $ev = fn(string $where) => $one("SELECT COUNT(*) FROM events WHERE ts BETWEEN ? AND ? AND $where");
    $leads = "FROM leads WHERE created_at BETWEEN ? AND ?";

    $rev = $db->prepare("SELECT currency, SUM(value) FROM leads WHERE status = 'won' AND created_at BETWEEN ? AND ? GROUP BY currency");
    $rev->execute($r);
    $by = $db->prepare("SELECT channel, COUNT(*) sessions FROM sessions WHERE started_at BETWEEN ? AND ? GROUP BY channel");
    $by->execute($r);
    $lc = $db->prepare("SELECT channel, COUNT(*) leads, SUM(status = 'won') won $leads GROUP BY channel");
    $lc->execute($r);
    $channels = [];
    foreach ($by->fetchAll() as $c) $channels[$c['channel']] = ['channel' => $c['channel'], 'sessions' => (int) $c['sessions'], 'leads' => 0, 'won' => 0];
    foreach ($lc->fetchAll() as $c) {
        $channels[$c['channel']] ??= ['channel' => $c['channel'], 'sessions' => 0, 'leads' => 0, 'won' => 0];
        $channels[$c['channel']]['leads'] = (int) $c['leads'];
        $channels[$c['channel']]['won'] = (int) $c['won'];
    }
    usort($channels, fn($a, $b) => $b['sessions'] <=> $a['sessions'] ?: $b['leads'] <=> $a['leads']);

    return [
        'visitors' => $one('SELECT COUNT(DISTINCT visitor_id) FROM events WHERE ts BETWEEN ? AND ? AND visitor_id IS NOT NULL'),
        'sessions' => $one('SELECT COUNT(*) FROM sessions WHERE started_at BETWEEN ? AND ?'),
        'wa' => $ev("type = 'click' AND target = 'whatsapp'"),
        'call' => $ev("type = 'click' AND target = 'call'"),
        'form_start' => $ev("type = 'form_start'"),
        'form_submit' => $ev("type = 'form_submit'"),
        'leads' => $one("SELECT COUNT(*) $leads"),
        'qualified' => $one("SELECT COUNT(*) $leads AND status IN ('qualified', 'won')"),
        'won' => $one("SELECT COUNT(*) $leads AND status = 'won'"),
        'revenue' => array_map('floatval', $rev->fetchAll(PDO::FETCH_KEY_PAIR)),
        'by_channel' => array_values($channels),
    ];
}

function report_pages(PDO $db, string $from, string $to): array
{
    $st = $db->prepare("SELECT path,
            SUM(type = 'page_view') views,
            COUNT(DISTINCT CASE WHEN type = 'page_view' THEN visitor_id END) visitors,
            AVG(CASE WHEN type = 'engaged' THEN value END) engaged_ms,
            COUNT(DISTINCT CASE WHEN type = 'scroll' AND value >= 50 THEN visitor_id END) s50,
            SUM(type = 'click' AND target = 'whatsapp') wa,
            SUM(type = 'click' AND target = 'call') call,
            SUM(type = 'form_start') form_start,
            SUM(type = 'form_submit') form_submit
        FROM events WHERE ts BETWEEN ? AND ? GROUP BY path ORDER BY views DESC, path");
    $st->execute(report_range($from, $to));
    return array_map(function ($r) {
        $visitors = (int) $r['visitors'];
        return [
            'path' => $r['path'], 'views' => (int) $r['views'], 'visitors' => $visitors,
            'avg_engaged_s' => (int) round(((float) $r['engaged_ms']) / 1000),
            'scroll50_pct' => $visitors ? round((int) $r['s50'] / $visitors * 100, 1) : 0.0,
            'wa' => (int) $r['wa'], 'call' => (int) $r['call'], 'form_start' => (int) $r['form_start'], 'form_submit' => (int) $r['form_submit'],
            'conv_pct' => $visitors ? round((int) $r['form_submit'] / $visitors * 100, 1) : 0.0,
        ];
    }, $st->fetchAll());
}

function report_page(PDO $db, string $path, string $from, string $to): array
{
    $r = report_range($from, $to);
    $row = current(array_filter(report_pages($db, $from, $to), fn($p) => $p['path'] === $path)) ?: ['path' => $path, 'views' => 0];

    $src = $db->prepare("SELECT s.channel, COUNT(DISTINCT s.id) FROM events e JOIN sessions s ON s.id = e.session_id
        WHERE e.path = ? AND e.type = 'page_view' AND e.ts BETWEEN ? AND ? GROUP BY s.channel ORDER BY 2 DESC");
    $src->execute([$path, ...$r]);
    $sc = $db->prepare("SELECT value, COUNT(*) FROM events WHERE path = ? AND type = 'scroll' AND ts BETWEEN ? AND ? GROUP BY value");
    $sc->execute([$path, ...$r]);
    $scroll = array_fill_keys([25, 50, 75, 90], 0);
    foreach ($sc->fetchAll(PDO::FETCH_KEY_PAIR) as $n => $c) if (isset($scroll[(int) $n])) $scroll[(int) $n] = (int) $c;
    $cl = $db->prepare("SELECT target, label, COUNT(*) n FROM events WHERE path = ? AND type = 'click' AND ts BETWEEN ? AND ?
        GROUP BY target, label ORDER BY n DESC LIMIT 20");
    $cl->execute([$path, ...$r]);

    return $row + [
        'sources' => array_map('intval', $src->fetchAll(PDO::FETCH_KEY_PAIR)),
        'scroll' => $scroll,
        'clicks' => array_map(fn($c) => ['target' => $c['target'], 'label' => $c['label'], 'n' => (int) $c['n']], $cl->fetchAll()),
    ];
}

const REPORT_PAGE_SIZE = 50;

function report_visitors(PDO $db, string $from, string $to, int $page): array
{
    $st = $db->prepare("SELECT v.id, v.first_seen, v.last_seen, v.country, v.first_channel,
            (SELECT COUNT(*) FROM sessions s WHERE s.visitor_id = v.id) sessions,
            (SELECT COUNT(*) FROM events e WHERE e.visitor_id = v.id AND e.type = 'page_view') pages,
            (SELECT MAX(l.id) FROM leads l WHERE l.visitor_id = v.id) lead_id
        FROM visitors v WHERE v.last_seen >= ? AND v.first_seen <= ?
        ORDER BY v.last_seen DESC LIMIT " . REPORT_PAGE_SIZE . ' OFFSET ' . (max(1, $page) - 1) * REPORT_PAGE_SIZE);
    $st->execute(report_range($from, $to));
    return array_map(fn($r) => ['sessions' => (int) $r['sessions'], 'pages' => (int) $r['pages'],
        'lead_id' => $r['lead_id'] === null ? null : (int) $r['lead_id']] + $r, $st->fetchAll());
}

function report_visitor(PDO $db, string $id): array
{
    $v = $db->prepare('SELECT * FROM visitors WHERE id = ?');
    $v->execute([$id]);
    $s = $db->prepare('SELECT * FROM sessions WHERE visitor_id = ? ORDER BY started_at');
    $s->execute([$id]);
    $e = $db->prepare('SELECT ts, session_id, type, path, target, label, value, lead_id FROM events WHERE visitor_id = ? ORDER BY ts, id');
    $e->execute([$id]);
    $events = [];
    foreach ($e->fetchAll() as $row) $events[$row['session_id']][] = $row;
    $l = $db->prepare('SELECT id, created_at, name, form, status, value, currency FROM leads WHERE visitor_id = ? ORDER BY created_at');
    $l->execute([$id]);
    return [
        'visitor' => $v->fetch() ?: null,
        'sessions' => array_map(fn($sess) => ['session' => $sess, 'events' => $events[$sess['id']] ?? []], $s->fetchAll()),
        'leads' => array_map(fn($r) => ['id' => (int) $r['id']] + $r, $l->fetchAll()),
    ];
}
