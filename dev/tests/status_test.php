<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/leads-db.php';

$db = leads_db();
$db->exec("INSERT INTO leads (created_at, name, email, phone) VALUES ('" . gmdate('c') . "', 'A', 'a@x.com', '+911')");
$id = (int) $db->lastInsertId();
$row = fn() => $db->query("SELECT status, value, currency, status_at FROM leads WHERE id = $id")->fetch();
$need = 'Enter the deal amount to mark this lead won.';

check(lead_set_status($db, $id, 'won', '', 'INR') === $need, 'won without amount accepted');
check(lead_set_status($db, $id, 'won', 'abc', 'INR') === $need, 'won with text amount accepted');
check($row()['status'] === 'new', 'status changed by a refused update');
check(lead_set_status($db, $id, 'won', '50000', 'XYZ') !== null, 'unknown currency accepted');
check(lead_set_status($db, $id, 'won', '50000', 'INR') === null, 'valid won refused');
$r = $row();
check($r['status'] === 'won' && (float) $r['value'] === 50000.0 && $r['currency'] === 'INR' && $r['status_at'], 'won not saved');
check(lead_set_status($db, $id, 'qualified', null, null) === null && $row()['status'] === 'qualified', 'qualified refused');
check(lead_set_status($db, $id, 'contacted', null, null) !== null, 'old status accepted');

try {
    lead_add_manual($db, ['name' => 'B', 'channel' => 'WhatsApp']);
    check(false, 'manual lead without phone or email accepted');
} catch (InvalidArgumentException) {
}
$m = lead_add_manual($db, ['name' => 'C', 'phone' => '+91 98765', 'channel' => 'Telegram', 'message' => 'Asked about SEO']);
$mr = $db->query("SELECT form, channel, status FROM leads WHERE id = $m")->fetch();
check($mr['form'] === 'manual' && $mr['channel'] === 'Telegram' && $mr['status'] === 'new', 'manual lead wrong: ' . json_encode($mr));
try {
    lead_add_manual($db, ['name' => 'D', 'phone' => '1', 'channel' => 'Pigeon']);
    check(false, 'unknown channel accepted');
} catch (InvalidArgumentException) {
}

echo "status ok\n";
