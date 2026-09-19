/** Sushant's WhatsApp business number, in the international format wa.me needs. */
export const WHATSAPP_NUMBER = "918289051732";

/** Opens a WhatsApp chat with the message pre-typed. The visitor still has to
 *  press send — nothing is sent on their behalf. */
export const whatsappUrl = (message: string, number = WHATSAPP_NUMBER) =>
  `https://wa.me/${number}?text=${encodeURIComponent(message)}`;

/** Number that website maintenance enquiries go to. */
export const MAINTENANCE_WHATSAPP = "919501110124";

/** sessionStorage key for the last maintenance enquiry (same reasoning as
 *  SHOPIFY_LEAD_KEY below). */
export const MAINTENANCE_LEAD_KEY = "maintenance-lead";

export type MaintenanceLead = {
  name: string;
  email: string;
  phone: string;
  website: string;
  platform: string;
  problems: string;
  reason: string;
  plan: string;
  access: string;
};

export function maintenanceLeadMessage(lead: Partial<MaintenanceLead> | null): string {
  if (!lead?.name) {
    return "Hi Sushant, I just sent a website maintenance request on your website and would like to talk about my site.";
  }
  const line = (label: string, value?: string) => (value ? `${label}: ${value}` : null);
  return [
    "Hi Sushant, I just sent a website maintenance request on sushantrana.com.",
    "",
    line("Name", lead.name),
    line("Email", lead.email),
    line("Phone", lead.phone),
    line("Website", lead.website),
    line("Platform", lead.platform),
    line("Problems", lead.problems),
    line("Why maintenance", lead.reason),
    line("Plan", lead.plan),
    line("Access", lead.access),
  ]
    .filter((l) => l !== null)
    .join("\n");
}

/** sessionStorage key holding the last Shopify enquiry, handed from the form to
 *  the thank-you page. Session storage rather than a query string: these are
 *  the visitor's own contact details and they have no business sitting in a URL
 *  that ends up in history, logs or a referrer header. */
export const SHOPIFY_LEAD_KEY = "shopify-lead";

export type ShopifyLead = {
  name: string;
  company: string;
  email: string;
  phone: string;
  service: string;
  platform: string;
  revenue: string;
  products: string;
  timeline: string;
  budget: string;
  details: string;
};

/** The message the visitor lands in WhatsApp with. */
export function shopifyLeadMessage(lead: Partial<ShopifyLead> | null): string {
  if (!lead?.name) {
    return "Hi Sushant, I just requested a Shopify store quote on your website and would like to talk about my store.";
  }
  const line = (label: string, value?: string) => (value ? `${label}: ${value}` : null);
  return [
    `Hi Sushant, I just requested a Shopify store quote on sushantrana.com.`,
    "",
    line("Name", lead.name),
    line("Business", lead.company),
    line("Email", lead.email),
    line("Phone", lead.phone),
    line("What I need", lead.service),
    line("Current platform", lead.platform),
    line("Monthly revenue", lead.revenue),
    line("Products", lead.products),
    line("Timeline", lead.timeline),
    line("Budget", lead.budget),
    lead.details ? `\nNotes: ${lead.details}` : null,
  ]
    .filter((l) => l !== null)
    .join("\n");
}
