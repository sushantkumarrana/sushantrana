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
    // One-time code for leadsforme.sushantrana.com: the first visit asks for
    // it before you choose your panel username and password.
    'PANEL_SETUP_CODE' => '',

    // Meta Conversions API (Events Manager → dataset) and Marketing API spend (system-user token with ads_read)
    'META_DATASET_ID' => '',
    'META_ACCESS_TOKEN' => '',
    'META_AD_ACCOUNT_ID' => '',          // digits only, without "act_"

    // LinkedIn Conversions API + ad analytics (developer app with Conversions API access)
    'LINKEDIN_ACCESS_TOKEN' => '',
    'LINKEDIN_AD_ACCOUNT_ID' => '',          // digits only
    'LINKEDIN_CONVERSION_QUALIFIED' => '',   // conversion rule id for "Qualified lead"
    'LINKEDIN_CONVERSION_WON' => '',         // conversion rule id for "Won deal"
    'LINKEDIN_VERSION' => '202603',          // LinkedIn-Version header (YYYYMM)

    // ChatGPT Ads (OpenAI Ads Manager → Conversions): pixel id and a Conversions API key
    'OPENAI_ADS_PIXEL_ID' => '',
    'OPENAI_ADS_CONVERSIONS_KEY' => '',

    // Google Ads script (dev/google-ads-script.js) ↔ api/ads-google.php: same long random key in both
    'GOOGLE_ADS_SCRIPT_KEY' => '',
];
