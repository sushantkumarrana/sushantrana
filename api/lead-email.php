<?php
/**
 * The enquiry notification email (port of lib/lead-email.ts).
 *
 * Written for email clients: nested tables, inline styles, no <style> block,
 * a fluid 600px card. Every form value is HTML-escaped before it goes in.
 */

const E_ORANGE = '#ff4d00';
const E_INK = '#0a0a0a';
const E_BODY = '#2a2a2a';
const E_MUTED = '#6b6b6b';
const E_LINE = '#e6e6e6';
const E_PAGE = '#f4f4f5';
const E_FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif";

function esc(string $s): string
{
    return htmlspecialchars($s, ENT_QUOTES | ENT_HTML5, 'UTF-8');
}

function e_row(string $label, string $value, bool $last = false): string
{
    $border = $last ? '' : 'border-bottom:1px solid ' . E_LINE . ';';
    return '<tr><td style="padding:12px 0;' . $border . 'width:96px;vertical-align:top;font:600 12px/1.5 ' . E_FONT . ';color:' . E_MUTED . ';text-transform:uppercase;letter-spacing:0.06em;">' . $label . '</td>'
        . '<td style="padding:12px 0;' . $border . 'font:400 15px/1.5 ' . E_FONT . ';color:' . E_BODY . ';">' . $value . '</td></tr>';
}

function e_button(string $href, string $label, string $bg, string $color): string
{
    return '<td style="padding-right:8px;"><a href="' . esc($href) . '" style="display:inline-block;padding:11px 18px;border-radius:8px;background:' . $bg . ';color:' . $color . ';font:600 14px/1 ' . E_FONT . ';text-decoration:none;">' . $label . '</a></td>';
}

function lead_email_html(array $d): string
{
    $consult = $d['enquiryType'] === 'consultation';
    $badgeBg = $consult ? 'rgba(255,77,0,0.12)' : 'rgba(10,10,10,0.08)';
    $badgeFg = $consult ? E_ORANGE : E_INK;
    $wa = preg_replace('/\D/', '', $d['phone']);
    $tel = 'tel:' . $d['phone'];
    $f = E_FONT;
    $o = E_ORANGE;
    $ink = E_INK;
    $muted = E_MUTED;
    $body = E_BODY;
    $line = E_LINE;
    $page = E_PAGE;

    $rows = e_row('Email', '<a href="mailto:' . esc($d['email']) . '" style="color:' . $o . ';text-decoration:none;">' . esc($d['email']) . '</a>')
        . e_row('Phone', '<a href="' . esc($tel) . '" style="color:' . $o . ';text-decoration:none;">' . esc($d['phone']) . '</a>')
        . e_row('Business', $d['business'] !== '' ? esc($d['business']) : '<span style="color:' . $muted . ';">&mdash;</span>')
        . e_row('Wants', esc($d['typeLabel']), true);

    $buttons = e_button('mailto:' . $d['email'], 'Reply', $o, '#ffffff')
        . e_button($tel, 'Call', '#f1f1f1', $ink)
        . ($wa ? e_button("https://wa.me/$wa", 'WhatsApp', '#f1f1f1', $ink) : '');

    $msg = $d['message'] !== ''
        ? '<tr><td style="padding:20px 28px 0 28px;"><div style="border-left:3px solid ' . $o . ';background:#faf9f8;border-radius:0 8px 8px 0;padding:14px 16px;">'
          . '<div style="font:600 11px/1 ' . $f . ';color:' . $muted . ';letter-spacing:0.06em;text-transform:uppercase;">Message</div>'
          . '<div style="margin-top:8px;font:400 15px/1.6 ' . $f . ';color:' . $body . ';">' . nl2br(esc($d['message'])) . '</div></div></td></tr>'
        : '';

    $first = esc(explode(' ', $d['name'])[0] ?: 'them');
    $svc = esc($d['service'] ?: 'something not listed');
    $pre = esc($d['service'] ?: 'General enquiry') . ' &middot; ' . esc($d['phone']) . ' &middot; ' . esc($d['email']);
    $received = esc($d['receivedAt']);
    $type = esc($d['typeLabel']);
    $nameE = esc($d['name']);
    $path = esc($d['sourcePath'] ?: '/');

    return <<<HTML
<!doctype html>
<html lang="en"><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width,initial-scale=1" />
<meta name="color-scheme" content="light" /><meta name="supported-color-schemes" content="light" />
<title>New enquiry from {$nameE}</title></head>
<body style="margin:0;padding:0;background:{$page};">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">{$pre}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{$page};">
<tr><td align="center" style="padding:28px 12px;">
<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:#ffffff;border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">
<tr><td style="background:{$ink};padding:22px 28px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td style="font:700 13px/1 {$f};color:#ffffff;letter-spacing:0.12em;text-transform:uppercase;"><span style="color:{$o};">&#9679;</span>&nbsp; New lead</td>
<td align="right" style="font:400 12px/1 {$f};color:rgba(255,255,255,0.55);">{$received}</td>
</tr></table></td></tr>
<tr><td style="height:3px;background:{$o};font-size:0;line-height:0;">&nbsp;</td></tr>
<tr><td style="padding:28px 28px 0 28px;">
<span style="display:inline-block;padding:5px 11px;border-radius:100px;background:{$badgeBg};color:{$badgeFg};font:700 11px/1 {$f};letter-spacing:0.06em;text-transform:uppercase;">{$type}</span>
<h1 style="margin:14px 0 0 0;font:700 26px/1.2 {$f};color:{$ink};">{$nameE}</h1>
<p style="margin:6px 0 0 0;font:400 16px/1.5 {$f};color:{$muted};">wants <strong style="color:{$o};font-weight:600;">{$svc}</strong></p>
</td></tr>
<tr><td style="padding:22px 28px 0 28px;"><table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>{$buttons}</tr></table></td></tr>
<tr><td style="padding:8px 28px 0 28px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{$rows}</table></td></tr>
{$msg}
<tr><td style="padding:22px 28px 26px 28px;"><div style="border-top:1px solid {$line};padding-top:14px;font:400 12px/1.7 {$f};color:{$muted};">
Submitted from <span style="color:{$body};">{$path}</span><br />Reply to this email and it goes straight to {$first}.
</div></td></tr>
</table>
<!--[if mso]></td></tr></table><![endif]-->
<div style="padding:16px 0 0 0;font:400 11px/1.5 {$f};color:#9a9a9a;">sushantrana.com &middot; automated notification</div>
</td></tr></table>
</body></html>
HTML;
}

function lead_email_text(array $d): string
{
    return implode("\n", [
        "NEW LEAD — {$d['typeLabel']}",
        '',
        "Name:     {$d['name']}",
        "Email:    {$d['email']}",
        "Phone:    {$d['phone']}",
        'Business: ' . ($d['business'] ?: '—'),
        'Service:  ' . ($d['service'] ?: '—'),
        "Wants:    {$d['typeLabel']}",
        '',
        'Message:',
        $d['message'] ?: '(none)',
        '',
        'Page:     ' . ($d['sourcePath'] ?: '/'),
        "Received: {$d['receivedAt']}",
    ]);
}
