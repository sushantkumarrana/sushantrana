/** Sushant's WhatsApp business number, in the international format wa.me needs. */
export const WHATSAPP_NUMBER = "918289051732";

/** Opens a WhatsApp chat with the message pre-typed. The visitor still has to
 *  press send — nothing is sent on their behalf. */
export const whatsappUrl = (message: string) =>
  `https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;

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
