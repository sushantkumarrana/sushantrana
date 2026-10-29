<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';

// A database made by the old schema, with one 'contacted' lead.
$path = getenv('LEADS_DATA_DIR') . '/leads.sqlite';
$old = new PDO("sqlite:$path");
$old->exec("CREATE TABLE leads (id INTEGER PRIMARY KEY AUTOINCREMENT, created_at TEXT NOT NULL, form TEXT, name TEXT NOT NULL,
    email TEXT NOT NULL, phone TEXT NOT NULL, business TEXT, service TEXT, enquiry_type TEXT, message TEXT, page TEXT,
    landing_page TEXT, referrer TEXT, channel TEXT, utm_source TEXT, utm_medium TEXT, utm_campaign TEXT, utm_term TEXT,
    utm_content TEXT, gclid TEXT, fbclid TEXT, user_agent TEXT, status TEXT NOT NULL DEFAULT 'new')");
$old->exec("INSERT INTO leads (created_at, name, email, phone, status) VALUES ('" . gmdate('c') . "', 'Old', 'o@x.com', '+911', 'contacted')");
$old = null;

require dirname(__DIR__, 2) . '/api/leads-db.php';
$db = leads_db();

$tables = array_column($db->query("SELECT name FROM sqlite_master WHERE type='table'")->fetchAll(), 'name');
foreach (['leads', 'visitors', 'sessions', 'events', 'page_daily', 'channel_daily'] as $t) check(in_array($t, $tables, true), "table $t missing");

$cols = array_column($db->query('PRAGMA table_info(leads)')->fetchAll(), 'name');
foreach (['journey', 'visitor_id', 'value', 'currency', 'li_fat_id', 'status_at', 'ad_group', 'keyword', 'oppref', 'gbraid', 'wbraid'] as $c) check(in_array($c, $cols, true), "leads.$c missing");
check($db->query("SELECT status FROM leads WHERE name='Old'")->fetchColumn() === 'new', "contacted lead not migrated to new");

check(LEADS_RETENTION_DAYS === 90, 'retention is not 90 days');
check(LEAD_STATUSES === ['new', 'qualified', 'wrong', 'won', 'lost'], 'statuses wrong');
check(LEAD_CURRENCIES === ['INR', 'AED', 'USD', 'EUR', 'GBP', 'CAD', 'CHF'], 'currencies wrong');

// Retention.
$ago = fn(int $days) => gmdate('c', time() - $days * 86400);
$add = $db->prepare("INSERT INTO leads (created_at, name, email, phone, status) VALUES (?, ?, 'a@x.com', '+911', ?)");
$add->execute([$ago(91), 'Old new', 'new']);
$add->execute([$ago(89), 'Recent', 'new']);
$add->execute([$ago(400), 'Old won', 'won']);
$db->prepare("INSERT INTO events (ts, type, path) VALUES (?, 'page_view', '/')")->execute([$ago(91)]);
$db->prepare("INSERT INTO events (ts, type, path) VALUES (?, 'page_view', '/')")->execute([$ago(1)]);
$db->prepare("INSERT INTO visitors (id, first_seen, last_seen) VALUES ('a', ?, ?)")->execute([$ago(120), $ago(91)]);
$db->prepare("INSERT INTO sessions (id, visitor_id, started_at, last_at) VALUES ('s', 'a', ?, ?)")->execute([$ago(91), $ago(91)]);
$old = gmdate('Y-m-d', time() - 100 * 86400);
$db->exec("INSERT INTO ad_clicks VALUES ('OLDCLICK', 'google', '$old', 'c', 'g', 'k')");
$db->exec("INSERT INTO search_terms VALUES ('$old', 'c', 'g', 'old term', 1, 1, 0)");
$db->exec("INSERT INTO gsc_daily VALUES ('$old', '/', 'old query', 1, 1, 1)");
$db->exec("INSERT INTO signals (lead_id, platform, event, created_at, state) VALUES (999999, 'meta', 'Won deal', '" . gmdate('c') . "', 'sent')");
leads_purge();
foreach (['ad_clicks', 'search_terms', 'gsc_daily'] as $tb) check((int) $db->query("SELECT COUNT(*) FROM $tb")->fetchColumn() === 0, "$tb older than 90 days kept");
check((int) $db->query('SELECT COUNT(*) FROM signals WHERE lead_id = 999999')->fetchColumn() === 0, 'signals of a deleted lead kept');
$names = array_column($db->query('SELECT name FROM leads')->fetchAll(), 'name');
check(!in_array('Old new', $names, true), '91-day-old lead kept');
check(in_array('Recent', $names, true), '89-day-old lead deleted');
check(in_array('Old won', $names, true), 'won lead deleted');
check((int) $db->query('SELECT COUNT(*) FROM events')->fetchColumn() === 1, 'old event kept');
check((int) $db->query('SELECT COUNT(*) FROM visitors')->fetchColumn() === 0, 'old visitor kept');
check((int) $db->query('SELECT COUNT(*) FROM sessions')->fetchColumn() === 0, 'old session kept');

echo "db ok\n";
