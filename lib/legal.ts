/**
 * Privacy Policy and Terms & Conditions, as prose blocks.
 *
 * ⚠️  These are drafts written to match what this site actually does — the
 *     lead form in components/LeadForm.tsx, the Supabase insert and Resend
 *     email in app/api/lead/route.ts, and the GTM container in app/layout.tsx.
 *     They are NOT legal advice and have not been reviewed by a lawyer. Have
 *     one read them before you rely on them.
 *
 *     Anything wrapped in {{double braces}} renders as a loud yellow highlight
 *     on the live page — those are details only Sushant can supply.
 *
 * Keep them honest: if the data flow in the API route changes, change the
 * "What I collect" and "Who processes your data" sections to match.
 */

import type { Block } from "./prose";

/** Shown at the top of both pages. Bump when you materially change the text. */
export const LEGAL_LAST_UPDATED = "2026-08-11";

export const CONTACT_EMAIL = "me@sushantrana.com";

export const PRIVACY_POLICY: Block[] = [
  {
    t: "p",
    text: "This policy explains what personal information sushantrana.com collects, why it is collected, who processes it, and what you can ask me to do with it. It covers this website only — not the separate agreements or tools used inside a paid engagement, which are dealt with in that engagement's own contract.",
  },
  {
    t: "h2",
    text: "Who is responsible for your data",
  },
  {
    t: "p",
    text: "This site is operated by **Sushant Rana**, an independent business growth consultant trading as a sole proprietor in Chandigarh, India. For the purposes of Indian data protection law I am the person who decides why and how your information is used, and I am the point of contact for any question about it.",
  },
  {
    t: "p",
    text: `You can reach me about anything in this policy at **${CONTACT_EMAIL}**.`,
  },

  { t: "h2", text: "What I collect" },
  {
    t: "h3",
    text: "Information you give me",
  },
  {
    t: "p",
    text: "When you submit the enquiry or consultation form on this site, I collect the fields you fill in:",
  },
  {
    t: "ul",
    items: [
      "**Name, email address and phone number** — required, so I can reply to you.",
      "**Business or website** — optional context about who you are.",
      "**The service you selected** and **whether you want a free consultation or a service enquiry** — so your enquiry reaches me already understood.",
      "**Your message** — optional, and entirely up to you what it contains.",
    ],
  },
  {
    t: "p",
    text: "Please do not put sensitive personal information, financial account details, passwords or client data into the message box. It is a contact form, not a secure channel.",
  },
  {
    t: "h3",
    text: "Information collected automatically",
  },
  {
    t: "p",
    text: "Alongside a form submission I record the page you submitted from, the referring URL, and your browser's user-agent string. This tells me which page produced an enquiry so I know what to write more of. Your IP address is used momentarily to rate-limit the form against spam; it is not written to the database.",
  },
  {
    t: "p",
    text: "Separately, my hosting provider keeps standard server logs (including IP addresses) as part of running and securing the site.",
  },

  { t: "h2", text: "Cookies and analytics" },
  {
    t: "p",
    text: "This site loads **Google Tag Manager**, which in turn may load analytics and advertising tags such as Google Analytics and advertising platform pixels. These set cookies or similar identifiers in your browser and are used to understand how the site is used and to measure marketing performance.",
  },
  {
    t: "ul",
    items: [
      "**Strictly necessary** — needed to serve the site and keep the form working. These cannot be switched off.",
      "**Analytics** — how many people visit, which pages they read, how they arrived.",
      "**Advertising / measurement** — attributing an enquiry back to a campaign, and building remarketing audiences.",
    ],
  },
  {
    t: "p",
    // If a consent banner is ever added to the site, describe it here and link
    // to the preferences control — this paragraph is what a reviewer reads.
    text: "You can block or delete cookies in your browser settings at any time; the site will still work. You can also opt out of Google Analytics specifically using Google's browser add-on.",
  },

  { t: "h2", text: "Why I use it, and on what basis" },
  {
    t: "ul",
    items: [
      "**To answer your enquiry and arrange a call** — because you asked me to, by submitting the form.",
      "**To follow up about the service you selected** — my legitimate interest in responding to a business enquiry, and steps taken at your request before entering a contract.",
      "**To keep the site secure and working** — legitimate interest in preventing spam and abuse.",
      "**To measure marketing performance** — legitimate interest in knowing which pages and campaigns produce enquiries, and consent where the law requires it for cookies.",
    ],
  },
  {
    t: "p",
    text: "I do **not** sell your personal information, and I do not add you to a marketing mailing list from the enquiry form without asking you first.",
  },

  { t: "h2", text: "Who processes your data" },
  {
    t: "p",
    text: "I run a small practice and use established providers rather than building my own infrastructure. Each of these acts as a processor on my instructions:",
  },
  {
    t: "ul",
    items: [
      "**Supabase** — stores enquiry submissions in a private database that is not readable from the browser.",
      "**Resend** — delivers the notification email that tells me an enquiry has arrived.",
      "**Hostinger** — hosts the website and keeps server logs.",
      "**Google (Tag Manager, Analytics, Ads)** — analytics and campaign measurement, as described above.",
    ],
  },
  {
    t: "p",
    text: "Beyond these, I share your information only where I am legally required to, or where you have asked me to.",
  },

  { t: "h2", text: "Where your data is held" },
  {
    t: "p",
    text: "These providers operate globally, so your information may be stored or processed outside India, including in the United States and the European Union. Where that happens I rely on the provider's own contractual safeguards for international transfers.",
  },

  { t: "h2", text: "How long I keep it" },
  {
    t: "p",
    text: "Enquiries are kept for a maximum of **three weeks** from our last contact, after which they are deleted. Records connected to a paid engagement are kept separately, for as long as tax and accounting law requires. You can ask me to delete your enquiry sooner at any time.",
  },

  { t: "h2", text: "Your rights" },
  {
    t: "p",
    text: "You can ask me to:",
  },
  {
    t: "ul",
    items: [
      "**Tell you what I hold** about you, and where it came from.",
      "**Correct** anything that is wrong or out of date.",
      "**Delete** your information, where I have no ongoing legal or contractual reason to keep it.",
      "**Withdraw consent** to marketing or analytics cookies.",
      "**Object to or restrict** a particular use of your information.",
    ],
  },
  {
    t: "p",
    text: `Email **${CONTACT_EMAIL}** and I will respond within 30 days. If you are in India and you are not satisfied with how I have handled your request, you may complain to the Data Protection Board of India. If you are in the UK or EU, you may complain to your national supervisory authority.`,
  },

  { t: "h2", text: "Security" },
  {
    t: "p",
    text: "The site is served over HTTPS. Enquiries are written to a database that the public website key cannot read from — it can only add new rows — so a leaked browser key could not be used to download enquiries. No system is perfectly secure, and I cannot guarantee the security of information while it is in transit to me.",
  },

  { t: "h2", text: "Children" },
  {
    t: "p",
    text: "This is a business-to-business site and is not directed at children. I do not knowingly collect information from anyone under 18. If you believe a child has submitted information through this site, email me and I will delete it.",
  },

  { t: "h2", text: "Links to other sites" },
  {
    t: "p",
    text: "This site links to third-party websites and platforms. Once you follow such a link, this policy no longer applies — the destination site has its own, and I am not responsible for it.",
  },

  { t: "h2", text: "Changes to this policy" },
  {
    t: "p",
    text: "If I change how the site handles personal information, I will update this page and the date at the top. Material changes will be reflected here before the change takes effect.",
  },

  { t: "h2", text: "Contact" },
  {
    t: "p",
    text: `Questions, corrections or deletion requests — email **${CONTACT_EMAIL}** and put "Privacy" in the subject line so it reaches me quickly.`,
  },
];

export const TERMS: Block[] = [
  {
    t: "p",
    text: "These terms govern your use of sushantrana.com. By browsing the site or submitting the enquiry form you accept them. If you do not accept them, please do not use the site.",
  },
  {
    t: "callout",
    title: "What these terms are not",
    text: "These terms cover the website. They do not govern paid work. Any consulting, marketing or development engagement is governed by a separate written agreement or proposal signed by both of us, and that agreement takes precedence over anything on this page.",
  },

  { t: "h2", text: "Who you are contracting with" },
  {
    t: "p",
    text: `This site is operated by **Sushant Rana**, an independent business growth consultant trading as a sole proprietor in Chandigarh, India. "I", "me" and "my" refer to that business. "You" refers to the person or organisation using the site. Contact: **${CONTACT_EMAIL}**.`,
  },

  { t: "h2", text: "What this website is" },
  {
    t: "p",
    text: "This site describes my services, publishes articles, and lets you request a consultation. Everything on it is provided for general information. It is not an offer capable of acceptance, and it is not professional, legal, financial, tax or investment advice. Do not act on an article here without taking advice suited to your own circumstances.",
  },

  { t: "h2", text: "Enquiries, consultations and bookings" },
  {
    t: "ul",
    items: [
      "Submitting the form is a **request**, not a booking. No engagement exists until I confirm it in writing.",
      "I may decline any enquiry, and I do not have to give a reason.",
      "A free consultation is exactly that — a conversation. It creates no ongoing obligation on either side, and nothing said in it is a deliverable.",
      "You agree that the information you give me is accurate, that the contact details are yours or that you are authorised to use them, and that you are contacting me for a genuine business purpose.",
    ],
  },

  { t: "h2", text: "Fees and paid engagements" },
  {
    t: "p",
    text: "No pricing on this site is a quotation. Fees, scope, timelines, payment terms, media spend handling, cancellation and refunds are all set out in the separate written agreement for that engagement. Where no such agreement exists, no work has been commissioned.",
  },

  { t: "h2", text: "No guarantee of results" },
  {
    t: "p",
    text: "Marketing, advertising and growth outcomes depend on your market, your offer, your pricing, your sales process, your budget, competitor behaviour and the policies of third-party platforms — most of which are outside my control. Case studies, metrics, testimonials and figures shown on this site describe past results for specific businesses. **They are illustrations, not predictions, and they are not a promise of similar results for you.**",
  },

  { t: "h2", text: "Third-party platforms" },
  {
    t: "p",
    text: "Work described on this site depends on platforms operated by others — Google, Meta, LinkedIn, Amazon, Shopify, CRM vendors and similar. Those platforms set their own rules, prices and approval decisions, and can change them, restrict an account or suspend one without notice. I am not responsible for their acts, outages, policy changes or decisions, and you remain responsible for complying with their terms in respect of your own accounts.",
  },

  { t: "h2", text: "Intellectual property" },
  {
    t: "p",
    text: "The content of this site — text, articles, layout, graphics, logos and the design itself — belongs to me or is used with permission, and is protected by copyright and other rights. You may read it, print it and share links to it for your own non-commercial use.",
  },
  {
    t: "p",
    text: "You may not republish, sell, systematically copy or scrape the content, use it to train a machine-learning model, or present it as your own, without my written permission. Quoting a short extract with clear attribution and a link back is welcome.",
  },

  { t: "h2", text: "Acceptable use" },
  {
    t: "p",
    text: "You agree not to use this site to:",
  },
  {
    t: "ul",
    items: [
      "Submit false, spam, automated or abusive enquiries, or anyone else's contact details without their permission.",
      "Attempt to gain unauthorised access to the site, its database, or any system connected to it.",
      "Interfere with the site's operation, including by overloading it or probing it for vulnerabilities.",
      "Upload or transmit anything unlawful, defamatory, infringing or malicious.",
    ],
  },
  {
    t: "p",
    text: "The enquiry form is rate-limited and monitored for abuse. I may block access to the site from any source that breaches this section.",
  },

  { t: "h2", text: "Availability of the site" },
  {
    t: "p",
    text: "I aim to keep the site available but I do not promise it will be uninterrupted or error-free. I may change, suspend or withdraw any part of it, at any time, without notice. Articles are accurate to the best of my knowledge on the date published, and marketing platforms change quickly — an older article may describe something that has since moved on.",
  },

  { t: "h2", text: "Disclaimers and limitation of liability" },
  {
    t: "p",
    text: "The site is provided \"as is\". To the fullest extent permitted by law, I exclude all warranties, express or implied, about its accuracy, completeness, fitness for a particular purpose, or uninterrupted availability.",
  },
  {
    t: "p",
    text: "To the fullest extent permitted by law, I am not liable for any indirect or consequential loss, or for any loss of profit, revenue, business, goodwill, data or anticipated savings, arising from your use of this site or reliance on anything published on it. My total liability arising out of or in connection with this site is limited to INR 10,000 (ten thousand Indian Rupees).",
  },
  {
    t: "p",
    text: "Nothing in these terms excludes or limits liability for fraud, for death or personal injury caused by negligence, or for anything else that cannot lawfully be excluded.",
  },

  { t: "h2", text: "Indemnity" },
  {
    t: "p",
    text: "You agree to indemnify me against claims, losses and reasonable costs arising from your breach of these terms or your misuse of this site.",
  },

  { t: "h2", text: "Privacy" },
  {
    t: "p",
    text: "How I handle personal information submitted through this site is set out in the Privacy Policy, which forms part of these terms.",
  },

  { t: "h2", text: "Changes to these terms" },
  {
    t: "p",
    text: "I may update these terms. The version on this page at the time you use the site is the version that applies, and the date at the top tells you when it last changed. Continuing to use the site after a change means you accept the updated terms.",
  },

  { t: "h2", text: "Governing law and jurisdiction" },
  {
    t: "p",
    text: "These terms, and any dispute arising out of or in connection with them or with this site, are governed by the laws of **India**. The courts at Chandigarh, India — including the High Court of Punjab and Haryana at Chandigarh — shall have exclusive jurisdiction, and both of us submit to that jurisdiction.",
  },

  { t: "h2", text: "Contact" },
  {
    t: "p",
    text: `Questions about these terms — email **${CONTACT_EMAIL}**.`,
  },
];
