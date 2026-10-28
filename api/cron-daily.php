<?php
/**
 * Nightly job (Hostinger cron, 02:30 IST):
 *   php ~/domains/sushantrana.com/public_html/api/cron-daily.php
 * Writes the daily totals for the last two IST days, then deletes what is
 * past the 90-day retention. Safe to run more than once a day.
 */

declare(strict_types=1);
require_once __DIR__ . '/leads-db.php';

/** Rebuild page_daily and channel_daily for one IST day (Y-m-d) from the raw tables. */
function rollup_day(PDO $db, string $day): void
{
    $utc = fn(string $t) => (new DateTime("$day $t", new DateTimeZone('Asia/Kolkata')))->setTimezone(new DateTimeZone('UTC'))->format('c');
    $r = [$utc('00:00:00'), $utc('23:59:59')];
    $db->beginTransaction();
    $db->prepare('DELETE FROM page_daily WHERE day = ?')->execute([$day]);
    $db->prepare('DELETE FROM channel_daily WHERE day = ?')->execute([$day]);
    $db->prepare("INSERT INTO page_daily SELECT ?, path,
            SUM(type = 'page_view'), COUNT(DISTINCT CASE WHEN type = 'page_view' THEN visitor_id END),
            COALESCE(SUM(CASE WHEN type = 'engaged' THEN value END), 0), SUM(type = 'engaged'),
            SUM(type = 'scroll' AND value = 25), SUM(type = 'scroll' AND value = 50), SUM(type = 'scroll' AND value = 75), SUM(type = 'scroll' AND value = 90),
            SUM(type = 'click' AND target = 'whatsapp'), SUM(type = 'click' AND target = 'call'), SUM(type = 'click' AND target = 'email'),
            SUM(type = 'form_start'), SUM(type = 'form_submit')
        FROM events WHERE ts BETWEEN ? AND ? GROUP BY path")->execute([$day, ...$r]);
    $db->prepare("INSERT INTO channel_daily SELECT ?, COALESCE(s.channel, 'Unknown'), COUNT(DISTINCT s.id), COUNT(DISTINCT s.visitor_id),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'click' AND e.target = 'whatsapp'),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'click' AND e.target = 'call'),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'form_start'),
            (SELECT COUNT(*) FROM events e JOIN sessions x ON x.id = e.session_id WHERE x.channel IS s.channel AND e.ts BETWEEN ? AND ? AND e.type = 'form_submit')
        FROM sessions s WHERE s.started_at BETWEEN ? AND ? GROUP BY s.channel")->execute([$day, ...$r, ...$r, ...$r, ...$r, ...$r]);
    $db->commit();
}

if (PHP_SAPI === 'cli' && realpath($argv[0] ?? '') === __FILE__) {
    $db = leads_db();
    foreach ([1, 2] as $back) {
        rollup_day($db, (new DateTime('now', new DateTimeZone('Asia/Kolkata')))->modify("-$back day")->format('Y-m-d'));
    }
    leads_purge();
    file_put_contents(leads_data_dir() . '/cron-daily.last', gmdate('c'));
    echo "cron-daily ok\n";
} elseif (PHP_SAPI !== 'cli') {
    http_response_code(404);
    exit(1);
}
