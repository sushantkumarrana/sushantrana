/**
 * The enquiry notification email.
 *
 * Written for email clients, not browsers: nested tables for layout, every
 * style inline, no flexbox/grid, no <style> block (Gmail strips it in the
 * mobile app), no web fonts, and a 600px card that Outlook won't break.
 *
 * Every value that came from the form is HTML-escaped before it goes in. The
 * message field is attacker-controlled text arriving in an inbox — unescaped,
 * it would be markup injection straight into what I read every morning.
 */

const ORANGE = "#ff4d00";
const INK = "#0a0a0a";
const BODY = "#2a2a2a";
const MUTED = "#6b6b6b";
const LINE = "#e6e6e6";
const PAGE_BG = "#f4f4f5";

export type LeadEmail = {
  name: string;
  email: string;
  /** E.164, e.g. +919876543210 */
  phone: string;
  business: string;
  service: string;
  /** Human label, e.g. "Free consultation" */
  typeLabel: string;
  /** "consultation" | "service" — drives the badge colour */
  enquiryType: string;
  message: string;
  sourcePath: string;
  receivedAt: string;
};

const esc = (s: string) =>
  s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");

/** Escaped, with newlines preserved as <br> — for the free-text message only. */
const escMultiline = (s: string) => esc(s).replace(/\r?\n/g, "<br />");

/** A label/value row in the details table. */
const row = (label: string, value: string, isLast = false) => `
  <tr>
    <td style="padding:12px 0;${isLast ? "" : `border-bottom:1px solid ${LINE};`}width:96px;vertical-align:top;font:600 12px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${MUTED};text-transform:uppercase;letter-spacing:0.06em;">${label}</td>
    <td style="padding:12px 0;${isLast ? "" : `border-bottom:1px solid ${LINE};`}font:400 15px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${BODY};">${value}</td>
  </tr>`;

/** Bulletproof-ish button: a padded anchor, no background images. */
const button = (href: string, label: string, bg: string, color: string) => `
  <td style="padding-right:8px;">
    <a href="${esc(href)}" style="display:inline-block;padding:11px 18px;border-radius:8px;background:${bg};color:${color};font:600 14px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;text-decoration:none;">${label}</a>
  </td>`;

export function leadEmailHtml(d: LeadEmail): string {
  const isConsult = d.enquiryType === "consultation";
  const badgeBg = isConsult ? "rgba(255,77,0,0.12)" : "rgba(10,10,10,0.08)";
  const badgeFg = isConsult ? ORANGE : INK;

  // wa.me wants digits only, no plus.
  const waNumber = d.phone.replace(/\D/g, "");
  const telHref = `tel:${d.phone}`;

  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<meta name="color-scheme" content="light" />
<meta name="supported-color-schemes" content="light" />
<title>New enquiry from ${esc(d.name)}</title>
</head>
<body style="margin:0;padding:0;background:${PAGE_BG};">

<!-- Preheader: the grey line Gmail shows next to the subject in the list.
     Hidden in the body itself by the zero size + hidden overflow. -->
<div style="display:none;max-height:0;overflow:hidden;opacity:0;">
  ${esc(d.service || "General enquiry")} &middot; ${esc(d.phone)} &middot; ${esc(d.email)}
</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:${PAGE_BG};">
<tr><td align="center" style="padding:28px 12px;">

  <!--[if mso]>
  <table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td>
  <![endif]-->

  <!-- Fluid card: width:100% + max-width, NOT width:600px. A fixed-width child
       stretches the parent table, so max-width:100% would then resolve against
       600px and the card would overflow a 360px phone instead of shrinking.
       Outlook desktop ignores max-width, hence the mso ghost table above. -->
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:#ffffff;border-radius:14px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,0.08);">

    <!-- header -->
    <tr>
      <td style="background:${INK};padding:22px 28px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr>
            <td style="font:700 13px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:#ffffff;letter-spacing:0.12em;text-transform:uppercase;">
              <span style="color:${ORANGE};">&#9679;</span>&nbsp; New lead
            </td>
            <td align="right" style="font:400 12px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:rgba(255,255,255,0.55);">
              ${esc(d.receivedAt)}
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <!-- orange rule under the header -->
    <tr><td style="height:3px;background:${ORANGE};font-size:0;line-height:0;">&nbsp;</td></tr>

    <!-- headline -->
    <tr>
      <td style="padding:28px 28px 0 28px;">
        <span style="display:inline-block;padding:5px 11px;border-radius:100px;background:${badgeBg};color:${badgeFg};font:700 11px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;letter-spacing:0.06em;text-transform:uppercase;">
          ${esc(d.typeLabel)}
        </span>
        <h1 style="margin:14px 0 0 0;font:700 26px/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${INK};">
          ${esc(d.name)}
        </h1>
        <p style="margin:6px 0 0 0;font:400 16px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${MUTED};">
          wants <strong style="color:${ORANGE};font-weight:600;">${esc(d.service || "something not listed")}</strong>
        </p>
      </td>
    </tr>

    <!-- actions -->
    <tr>
      <td style="padding:22px 28px 0 28px;">
        <table role="presentation" cellpadding="0" cellspacing="0" border="0">
          <tr>
            ${button(`mailto:${d.email}`, "Reply", ORANGE, "#ffffff")}
            ${button(telHref, "Call", "#f1f1f1", INK)}
            ${waNumber ? button(`https://wa.me/${waNumber}`, "WhatsApp", "#f1f1f1", INK) : ""}
          </tr>
        </table>
      </td>
    </tr>

    <!-- details -->
    <tr>
      <td style="padding:8px 28px 0 28px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
          ${row("Email", `<a href="mailto:${esc(d.email)}" style="color:${ORANGE};text-decoration:none;">${esc(d.email)}</a>`)}
          ${row("Phone", `<a href="${esc(telHref)}" style="color:${ORANGE};text-decoration:none;">${esc(d.phone)}</a>`)}
          ${row("Business", d.business ? esc(d.business) : `<span style="color:${MUTED};">&mdash;</span>`)}
          ${row("Wants", esc(d.typeLabel), true)}
        </table>
      </td>
    </tr>

    <!-- message -->
    ${
      d.message
        ? `<tr>
      <td style="padding:20px 28px 0 28px;">
        <div style="border-left:3px solid ${ORANGE};background:#faf9f8;border-radius:0 8px 8px 0;padding:14px 16px;">
          <div style="font:600 11px/1 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${MUTED};letter-spacing:0.06em;text-transform:uppercase;">Message</div>
          <div style="margin-top:8px;font:400 15px/1.6 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${BODY};">${escMultiline(d.message)}</div>
        </div>
      </td>
    </tr>`
        : ""
    }

    <!-- meta -->
    <tr>
      <td style="padding:22px 28px 26px 28px;">
        <div style="border-top:1px solid ${LINE};padding-top:14px;font:400 12px/1.7 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:${MUTED};">
          Submitted from <span style="color:${BODY};">${esc(d.sourcePath || "/")}</span><br />
          Reply to this email and it goes straight to ${esc(d.name.split(" ")[0] || "them")}.
        </div>
      </td>
    </tr>

  </table>

  <!--[if mso]></td></tr></table><![endif]-->

  <div style="padding:16px 0 0 0;font:400 11px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif;color:#9a9a9a;">
    sushantrana.com &middot; automated notification
  </div>

</td></tr>
</table>
</body>
</html>`;
}

/**
 * Plain-text alternative. Not optional: a mail with no text part scores worse
 * with spam filters, and some clients still render it in previews.
 */
export function leadEmailText(d: LeadEmail): string {
  return [
    `NEW LEAD — ${d.typeLabel}`,
    ``,
    `Name:     ${d.name}`,
    `Email:    ${d.email}`,
    `Phone:    ${d.phone}`,
    `Business: ${d.business || "—"}`,
    `Service:  ${d.service || "—"}`,
    `Wants:    ${d.typeLabel}`,
    ``,
    `Message:`,
    d.message || "(none)",
    ``,
    `Page:     ${d.sourcePath || "/"}`,
    `Received: ${d.receivedAt}`,
  ].join("\n");
}
