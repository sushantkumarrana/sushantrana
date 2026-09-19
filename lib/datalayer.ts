/**
 * GTM dataLayer events for form submissions.
 *
 * Every lead form on the site calls pushLead() once, after /api/lead confirms
 * the lead was received (never on a failed submit), and before redirecting to
 * its thank-you page. In GTM, trigger on the event name (Custom Event) and read
 * the fields with Data Layer Variables, e.g. `form_name`, `platform`,
 * `user_data.email`.
 *
 * Contact details sit under `user_data` in the shape Google Ads enhanced
 * conversions expects. Keep them out of GA4 event parameters: GA4's terms
 * forbid sending personal data to it.
 *
 * Naming, for every new form: event `lead_<form_name>`, form_name in snake_case
 * matching the thank-you slug, e.g. thank-you-website-maintenance ->
 * website_maintenance.
 */

type Primitive = string | number | boolean | null | undefined;

export function pushLead(
  formName: string,
  fields: Record<string, Primitive | Primitive[]>,
  user: { name?: string; email?: string; phone?: string }
) {
  if (typeof window === "undefined") return;
  const w = window as unknown as { dataLayer?: Record<string, unknown>[] };
  w.dataLayer = w.dataLayer || [];
  w.dataLayer.push({
    event: `lead_${formName}`,
    form_name: formName,
    form_page: window.location.pathname,
    ...Object.fromEntries(
      Object.entries(fields).map(([k, v]) => [k, Array.isArray(v) ? v.join(", ") : v ?? ""])
    ),
    user_data: {
      name: user.name ?? "",
      email: user.email ?? "",
      // E.164-style with the country code, as enhanced conversions expects.
      phone_number: user.phone ?? "",
    },
  });
}
