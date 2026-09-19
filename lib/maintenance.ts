/**
 * Content for /services/website-maintenance.
 *
 * Package prices and inclusions carry over from the old House Of Web
 * maintenance page (houseofweb.in/website-maintenance-services, archived June
 * 2024). The wording is rewritten, and the old page's USD figures are dropped
 * because two plans listed the same dollar price for different rupee prices.
 *
 * MAINTENANCE_FAQS also feeds FAQPage JSON-LD in the route, so the visible
 * accordion and the structured data can never disagree.
 */

export const CTA_LABEL = "Get a maintenance plan";

export const HERO_STATS = [
  { n: "8+", label: "Years building websites" },
  { n: "50+", label: "Client brands" },
  { n: "3", label: "Plans to pick from" },
  { n: "₹18K", label: "Plans start per year" },
];

export type Plan = {
  name: string;
  hours: string;
  price: string;
  featured?: boolean;
  items: string[];
};

export const PLANS: Plan[] = [
  {
    name: "Essential",
    hours: "7 hours a month",
    price: "₹18,000",
    items: [
      "Monthly backup",
      "Monthly security scan",
      "Disaster recovery",
      "Hosting support",
      "SSL certificate monitoring",
      "Domain expiry alerts",
      "Webmail support",
      "Broken link check and fix",
    ],
  },
  {
    name: "Growth",
    hours: "15 hours a month",
    price: "₹22,000",
    featured: true,
    items: [
      "Two backups a month",
      "Everything in Essential",
      "CMS, plugin and app updates",
      "Basic content and design updates",
      "Google Search Console setup",
      "New page design",
    ],
  },
  {
    name: "Complete",
    hours: "30 hours a month",
    price: "₹44,000",
    items: [
      "Weekly backup",
      "Everything in Growth",
      "Malware scanning and cleanup",
      "Google Analytics setup",
    ],
  },
];

/** The "why it matters" story, told as a timeline across the photo band. */
export const DOWNTIME_STORY = [
  { when: "Day 1", t: "The site launches", d: "Everything works. Nobody signs up for maintenance." },
  { when: "Week 6", t: "A plugin updates", d: "Or a certificate expires. Nobody is watching." },
  { when: "Month 2", t: "Pages break", d: "Forms stop sending. Checkout throws errors." },
  { when: "Every day after", t: "Leads go elsewhere", d: "Visitors leave, and Google notices too." },
];

/** What a plan covers, grouped the way problems actually show up. */
export const COVERAGE = [
  {
    icon: "gauge",
    t: "Performance",
    d: "Loading speed kept in check, dead pages and broken links removed, regular health checks and backups.",
  },
  {
    icon: "shield",
    t: "Security",
    d: "SSL monitoring, outdated software patched before it becomes a way in, and scans for malicious code.",
  },
  {
    icon: "search",
    t: "SEO",
    d: "Content and image optimisation, Search Console watched for errors, so rankings do not slip quietly.",
  },
  {
    icon: "code",
    t: "Development",
    d: "Theme, plugin and app updates, bug fixes, payment gateway issues and product management on ecommerce sites.",
  },
  {
    icon: "palette",
    t: "Design",
    d: "New pages, text and image updates, blog posts and changes to existing sections when the business moves on.",
  },
  {
    icon: "server",
    t: "Domain and hosting",
    d: "Renewals tracked, hosting issues handled with your provider, webmail set up and kept working.",
  },
];

export const UPDATE_POINTS = [
  "CMS, theme, plugin and app updates, tested before they go live",
  "Text, image and price changes whenever the business needs them",
  "New pages and blog posts designed to match the rest of the site",
  "Forms, booking systems and checkouts tested after every change",
];

export const SECURITY_POINTS = [
  "Scheduled backups on every plan",
  "Disaster recovery if anything goes wrong",
  "Malware scanning and cleanup",
  "SSL and domain expiry watched so nothing lapses",
];

export const WHY_CHOOSE = [
  {
    t: "Problems caught early",
    d: "The site is checked on a schedule, so most issues are fixed before a customer ever sees them.",
  },
  {
    t: "One team, whole site",
    d: "Design, code, hosting and SEO sit with the same people, so nothing gets passed between vendors.",
  },
  {
    t: "Priced by the hour you need",
    d: "Pick the monthly hours that fit your site. No paying for an enterprise plan to run a brochure site.",
  },
];

export const RELATED_SERVICES = [
  { label: "Shopify store development", href: "/services/shopify-store-development" },
  { label: "WordPress development", href: "/services/wordpress-development" },
  { label: "Website redesign", href: "/services/website-redesign" },
  { label: "Technical SEO", href: "/services/technical-seo" },
  { label: "Local SEO", href: "/services/local-seo" },
];

/**
 * Platforms shown in the "Every platform" grid and offered in the form.
 * Logos are simple-icons SVGs (CC0) in /public/logos/platforms/, recoloured to
 * each brand's hex. A missing file falls back to an icon tile.
 */
export const PLATFORMS: { name: string; logos: string[] }[] = [
  { name: "WordPress", logos: ["wordpress"] },
  { name: "WooCommerce", logos: ["woocommerce"] },
  { name: "Shopify", logos: ["shopify"] },
  { name: "Wix", logos: ["wix"] },
  { name: "Wix Studio", logos: ["wix"] },
  { name: "Squarespace", logos: ["squarespace"] },
  { name: "Webflow", logos: ["webflow"] },
  { name: "Framer", logos: ["framer"] },
  // No Magento logo yet (simple-icons dropped it). Upload
  // /public/logos/platforms/magento.svg, then set logos: ["magento"].
  { name: "Magento", logos: [] },
  { name: "BigCommerce", logos: ["bigcommerce"] },
  { name: "Joomla", logos: ["joomla"] },
  { name: "Drupal", logos: ["drupal"] },
  { name: "Ghost", logos: ["ghost"] },
  { name: "HubSpot CMS", logos: ["hubspot"] },
  { name: "Custom HTML", logos: ["html5"] },
  { name: "React and Next.js", logos: ["react", "nextdotjs"] },
  { name: "AI-built sites", logos: [] },
];

/* ------------------------------------------------------------ enquiry form */

export const FORM_PROBLEMS = [
  "Site is down or not loading",
  "Slow loading",
  "Hacked or showing malware",
  "Errors or broken pages",
  "Forms, checkout or payments not working",
  "Plugin, app or theme updates",
  "Content or design changes",
  "SEO or Google issues",
  "Domain, hosting or email issues",
  "Nothing broken, just want it looked after",
];

export const FORM_REASONS = [
  "Something is broken right now",
  "Regular upkeep so nothing breaks",
  "My old developer is no longer available",
  "I need ongoing changes and updates",
  "Just exploring options",
];

export const FORM_ACCESS = [
  { key: "domain", q: "Domain login" },
  { key: "hosting", q: "Hosting login" },
  { key: "backend", q: "Website admin login" },
] as const;

export const ACCESS_ANSWERS = ["Yes", "No", "Not sure"];

export type Faq = { q: string; a: string };

/**
 * Grouped for the page; flattened for FAQPage JSON-LD. Questions follow what
 * people actually search on Google ("People also ask") and ask ChatGPT about
 * website maintenance.
 */
export const FAQ_GROUPS: { h: string; items: Faq[] }[] = [
  {
    h: "The basics",
    items: [
      {
        q: "What is website maintenance?",
        a: "Website maintenance is the regular work that keeps a live website secure, fast and correct: backups, software and plugin updates, security checks, bug fixes, broken link repairs and content changes. It is to a website what servicing is to a car.",
      },
      {
        q: "Why does my website need a maintenance plan?",
        a: "Software, plugins, browsers and search engines keep changing. Without regular care a site slows down, breaks or becomes an easy target for hackers. A plan keeps it updated, backed up and working, with someone already responsible when something goes wrong.",
      },
      {
        q: "What is included in website maintenance services?",
        a: "Every plan includes backups, security scans, disaster recovery, hosting and webmail support, SSL and domain monitoring, and broken link fixes. Higher plans add CMS and plugin updates, content and design changes, new pages, Search Console and Analytics setup, and malware cleanup.",
      },
      {
        q: "What happens if I do not maintain my website?",
        a: "Outdated plugins and themes are the most common way sites get hacked. Unmaintained sites also slow down, show errors after browser or platform updates, lose forms and payments without anyone noticing, and slowly drop in Google rankings.",
      },
      {
        q: "How often should a website be maintained?",
        a: "Backups and security checks should run at least monthly, and weekly for busy or ecommerce sites. Plugin and platform updates are best applied as they release, after testing. A full health check of speed, SEO and broken links every month keeps small problems small.",
      },
      {
        q: "Can I maintain my website myself?",
        a: "You can handle simple text changes yourself. Updates, backups, security and fixing what breaks after an update need technical knowledge and time. Most business owners find a plan costs less than the hours, and the risk, of doing it alone.",
      },
      {
        q: "What is the difference between website maintenance and website support?",
        a: "Maintenance is planned, preventive work like updates, backups and checks. Support is fixing a problem after it appears. Every plan here covers both, so you do not pay separately when something breaks.",
      },
    ],
  },
  {
    h: "Cost and plans",
    items: [
      {
        q: "How much does website maintenance cost in India?",
        a: "Plans start at ₹18,000 a year for 7 hours of work a month, with a 15 hour plan at ₹22,000 and a 30 hour plan at ₹44,000 a year. Clients in India pay 18% GST on top. Very large or complex sites may need a custom quote.",
      },
      {
        q: "How much does website maintenance cost per month?",
        a: "Billed yearly, the plans work out to roughly ₹1,500, ₹1,830 and ₹3,670 a month, depending on how many hours of work your site needs each month.",
      },
      {
        q: "What is a website AMC?",
        a: "AMC stands for Annual Maintenance Contract. It is a yearly agreement where one team takes care of your website's upkeep for a fixed price, instead of you paying for each fix separately. All three plans here are AMCs.",
      },
      {
        q: "Which plan should I choose?",
        a: "A small business site with few changes is usually fine on Essential. If you update content often or run a CMS with many plugins or apps, pick Growth. Ecommerce stores and high-traffic sites suit Complete.",
      },
      {
        q: "Are hosting and domain charges included?",
        a: "No. Hosting and domain renewals are paid to your provider and stay in your name. The plan covers managing them: tracking renewal dates, handling hosting issues with the provider and keeping SSL and webmail working.",
      },
    ],
  },
  {
    h: "Platforms",
    items: [
      {
        q: "Which platforms and CMS do you maintain?",
        a: "WordPress, WooCommerce, Shopify, Wix, Wix Studio, Squarespace, Webflow, Framer, Magento, BigCommerce, Joomla, Drupal, Ghost and HubSpot CMS, plus custom HTML, React and Next.js sites and sites built with AI tools.",
      },
      {
        q: "Do Wix, Squarespace, Shopify or Webflow websites need maintenance?",
        a: "Yes, though less of it. The platform takes care of hosting and core security, but content, SEO settings, speed, forms, integrations, apps, domains and broken links are still yours to look after. Those are exactly what the plans cover.",
      },
      {
        q: "What does WordPress maintenance include?",
        a: "Core, theme and plugin updates tested before they go live, PHP version checks, database cleanup, backups, malware scanning, speed work and fixing anything an update breaks. WordPress needs the most regular care of any CMS because of its plugins.",
      },
      {
        q: "What does Shopify store maintenance include?",
        a: "Theme updates, app reviews and leftover app code cleanup, product and collection uploads, speed work, broken link and image fixes, checkout and payment checks, and design changes to sections and pages.",
      },
      {
        q: "Do you maintain Webflow and Framer websites?",
        a: "Yes. That covers CMS collection updates, new pages built with your existing components, interaction and layout fixes on new screen sizes, form and integration checks, SEO settings and publishing changes safely.",
      },
      {
        q: "Do you maintain custom HTML, React or vibe-coded websites?",
        a: "Yes. Sites built by hand or with AI tools such as Lovable, Bolt, v0, Replit or Cursor still need dependency and security updates, bug fixes, deployment and hosting care, and someone who can read and safely change the code.",
      },
      {
        q: "Can you move my website to another platform?",
        a: "Yes. Moving between platforms, for example Wix to WordPress or WooCommerce to Shopify, is a separate project. Tell me on the call and I will quote it alongside the maintenance plan.",
      },
    ],
  },
  {
    h: "Security, speed and SEO",
    items: [
      {
        q: "What if my site gets hacked or goes down?",
        a: "The site is restored from the latest clean backup, the cause is found and fixed, and security is tightened so it does not happen again. Disaster recovery is part of every plan.",
      },
      {
        q: "How often is my website backed up?",
        a: "Monthly on Essential, twice a month on Growth and weekly on Complete. Hosted platforms like Shopify and Wix are backed up at the content level where the platform allows it.",
      },
      {
        q: "Can you make my slow website faster?",
        a: "Yes. Speed work covers image compression, removing unused plugins, apps and scripts, caching, and fixing whatever the Core Web Vitals report flags. Keeping it fast after that is part of the monthly checks.",
      },
      {
        q: "Does website maintenance help SEO?",
        a: "Yes. Google favours fast, secure, error-free sites. Fixing broken links and 404 errors, keeping SSL valid, improving speed and watching Search Console for problems all protect the rankings you already have.",
      },
    ],
  },
  {
    h: "Working together",
    items: [
      {
        q: "Do you maintain websites you did not build?",
        a: "Yes. Every new site starts with a health check, so any existing problems are found and listed before the plan begins.",
      },
      {
        q: "Will I keep ownership and admin access to my website?",
        a: "Yes. Your website, domain, hosting and accounts stay in your name. I work through the access you give and you can remove it at any time.",
      },
      {
        q: "How do I request changes to my website?",
        a: "Send the change on WhatsApp or email with the page and what should change. It is worked into your monthly hours and you are told when it is live.",
      },
    ],
  },
];

export const MAINTENANCE_FAQS: Faq[] = FAQ_GROUPS.flatMap((g) => g.items);
