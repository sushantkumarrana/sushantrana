/**
 * Single source of truth for the service catalogue.
 *
 * Three things read from here and must never drift apart:
 *   - the Services mega menu in the nav
 *   - the "Which service?" dropdown on every lead form
 *   - the Quick links panel in the blog sidebar
 *
 * Slugs are what /services/<slug> resolves to. Anything without a real page
 * yet lands on the services catch-all, which renders the "coming soon" shell.
 */

export type ServiceGroup = {
  /** Heading shown in the nav column, the <optgroup> label, and the sidebar. */
  heading: string;
  items: string[];
};

export const SERVICE_GROUPS: ServiceGroup[] = [
  {
    heading: "Performance Marketing",
    items: [
      "Google Ads",
      "Meta Ads",
      "LinkedIn Ads",
      "YouTube Ads",
      "Google Shopping Ads",
      "Amazon Ads",
      "Lead Generation",
      "Remarketing",
    ],
  },
  {
    heading: "SEO Services",
    items: [
      "Local SEO",
      "Technical SEO",
      "Ecommerce SEO",
      "Enterprise SEO",
      "SEO Audit",
      "Link Building",
      "Content SEO",
    ],
  },
  {
    heading: "Website Development",
    items: [
      "WordPress Development",
      "Ecommerce Website",
      "Landing Pages",
      "Website Redesign",
      "Website Maintenance",
    ],
  },
  {
    heading: "CRM Solutions",
    items: [
      "Zoho CRM",
      "HubSpot CRM",
      "GoHighLevel",
      "Sales Funnel Setup",
      "Pipeline Management",
      "Email Automation",
      "Reporting Dashboard",
      "CRM Consulting",
    ],
  },
  {
    heading: "AI Automation",
    items: [
      "AI Lead Scoring",
      "WhatsApp Automation",
      "AI Assistants",
      "Workflow Automation",
      "Reporting Automation",
    ],
  },
];

/** The last option in the dropdown, for anyone whose need isn't listed. */
export const OTHER_SERVICE = "Something else / not sure yet";

export const serviceSlug = (s: string) =>
  s
    .toLowerCase()
    .replace(/&/g, "and")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-|-$/g, "");

/** Flat list of every valid service label — used to validate what the API gets. */
export const ALL_SERVICES: string[] = SERVICE_GROUPS.flatMap((g) => g.items);

/**
 * Maps a URL path back to a service label so a form opened on
 * /services/google-ads can preselect "Google Ads" instead of making the
 * visitor find it again in a 33-item dropdown.
 *
 * Returns "" when the path isn't a service page, which the form reads as
 * "no preselection" — never as an invalid value.
 */
export function serviceFromPath(pathname: string): string {
  const m = /^\/services\/([^/?#]+)/.exec(pathname);
  if (!m) return "";
  const slug = m[1].toLowerCase();
  return ALL_SERVICES.find((s) => serviceSlug(s) === slug) ?? "";
}

/** What the visitor wants from me. Stored alongside the service on each lead. */
export const ENQUIRY_TYPES = [
  {
    value: "consultation",
    label: "Free consultation",
    hint: "Talk it through with me first",
  },
  {
    value: "service",
    label: "Service enquiry",
    hint: "I want you to run this for me",
  },
] as const;

export type EnquiryType = (typeof ENQUIRY_TYPES)[number]["value"];

export const ENQUIRY_TYPE_VALUES: string[] = ENQUIRY_TYPES.map((t) => t.value);
