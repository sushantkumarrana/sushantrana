<?php
declare(strict_types=1);
require __DIR__ . '/bootstrap.php';
require dirname(__DIR__, 2) . '/api/signals.php';

$db = leads_db();
$lead = function (array $cols) use ($db): int {
    $cols += ['created_at' => gmdate('c'), 'name' => 'S', 'email' => 's@x.com', 'phone' => '+911'];
    $db->prepare('INSERT INTO leads (' . implode(',', array_keys($cols)) . ') VALUES (' . rtrim(str_repeat('?,', count($cols)), ',') . ')')
        ->execute(array_values($cols));
    return (int) $db->lastInsertId();
};
$rows = fn(int $id) => $db->query("SELECT platform, event, value, currency, state FROM signals WHERE lead_id = $id ORDER BY event, platform")->fetchAll();

check(signal_platforms(['gclid' => 'g', 'fbclid' => 'f', 'li_fat_id' => '', 'oppref' => null]) === ['google', 'meta'], 'platforms from click ids');
check(signal_platforms(['wbraid' => 'w', 'oppref' => 'o', 'li_fat_id' => 'l']) === ['google', 'linkedin', 'chatgpt'], 'gbraid/wbraid/oppref/li_fat_id');

$id = $lead(['gclid' => 'g1', 'fbclid' => 'f1']);
check(lead_set_status($db, $id, 'qualified', null, null) === null, 'qualified refused');
$r = $rows($id);
check(count($r) === 2 && $r[0]['event'] === 'Qualified lead' && $r[0]['value'] === null && $r[0]['state'] === 'pending', 'qualified signals: ' . json_encode($r));

lead_set_status($db, $id, 'won', '50000', 'INR');
$won = array_values(array_filter($rows($id), fn($x) => $x['event'] === 'Won deal'));
check(count($won) === 2 && (float) $won[0]['value'] === 50000.0 && $won[0]['currency'] === 'INR', 'won signals: ' . json_encode($won));

$db->exec("UPDATE signals SET state = 'sent' WHERE lead_id = $id");
lead_set_status($db, $id, 'qualified', null, null);
lead_set_status($db, $id, 'won', '50000', 'INR');
check(count($rows($id)) === 4 && !array_filter($rows($id), fn($x) => $x['state'] !== 'sent'), 'same status again created or reset signals');

lead_set_status($db, $id, 'won', '60000', 'INR');
$won = array_values(array_filter($rows($id), fn($x) => $x['event'] === 'Won deal'));
check((float) $won[0]['value'] === 60000.0 && $won[0]['state'] === 'pending' && count($rows($id)) === 4, 'new value not re-queued: ' . json_encode($won));

$none = $lead([]);
lead_set_status($db, $none, 'won', '1000', 'INR');
check($rows($none) === [], 'lead without click ids got signals');
$wrong = $lead(['gclid' => 'g2']);
lead_set_status($db, $wrong, 'wrong', null, null);
check($rows($wrong) === [], 'wrong lead got signals');

echo "signals ok\n";
