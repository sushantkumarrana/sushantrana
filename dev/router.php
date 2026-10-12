<?php
// Local preview only: `php -S` with Apache-like 404 handling.
$root = $_SERVER['DOCUMENT_ROOT'];
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$file = $root . $path;
if (is_file($file)) return false;
if (is_dir($file)) {
    if (substr($path, -1) !== '/') { header("Location: $path/", true, 301); return true; }
    if (is_file("$file/index.html") || is_file("$file/index.php")) return false;
}
http_response_code(404);
readfile("$root/404.html");
