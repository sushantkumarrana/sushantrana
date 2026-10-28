<?php
// Shared setup for dev/tests/*_test.php: a fresh, throwaway leads.sqlite.
// Run a test with:  php dev/tests/<name>_test.php
declare(strict_types=1);

if (!getenv('LEADS_DATA_DIR')) {
    $dir = sys_get_temp_dir() . '/sr-test-' . bin2hex(random_bytes(4));
    mkdir($dir, 0700, true);
    putenv("LEADS_DATA_DIR=$dir");
    register_shutdown_function(fn() => array_map('unlink', glob("$dir/*") ?: []) && @rmdir($dir));
}

function check(bool $ok, string $msg): void
{
    if ($ok) return;
    fwrite(STDERR, "FAIL: $msg\n");
    exit(1);
}
