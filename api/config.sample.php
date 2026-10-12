<?php
// Copy this file to config.php (same folder) and fill in the values.
// config.php is never served as text: PHP runs it and it outputs nothing,
// and api/.htaccess blocks direct requests to it as well.
return [
    'SUPABASE_URL' => 'https://YOUR-PROJECT.supabase.co',
    // Publishable key + an INSERT-only RLS policy on `leads` and `heartbeat`.
    'SUPABASE_PUBLISHABLE_KEY' => '',
    'RESEND_API_KEY' => '',
    // Where enquiry notifications go.
    'LEAD_NOTIFY_TO' => 'me@sushantrana.com',
];
