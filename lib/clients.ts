/**
 * Client work shown on /about and referenced by that page's JSON-LD.
 *
 * One source of truth on purpose: the visible cards and the `mentions` array in
 * the structured data are generated from this list, so schema can never claim a
 * client the page does not actually show.
 *
 * `url` is the client's own website and is intentionally nullable — a guessed
 * domain would be a fabricated citation and a broken outbound link, so the
 * "Visit website" link only renders for domains that are confirmed.
 *
 * The card image is a screenshot of the client's own website, served from
 * /public/clients/<slug>-website.png. Missing files fall back to the
 * placeholder box rather than a broken image, so screenshots can be dropped in
 * later without touching this file.
 */
export type Client = {
  slug: string;
  /** Shown on the card. Short forms are fine — set `fullName` alongside so the
   *  full legal name still reaches the structured data and the caption. */
  name: string;
  fullName?: string;
  url: string | null;
  location: string;
  industry: string;
  services: string[];
  summary: string;
  /** Short, factual outcome. Omitted where there is no verified number. */
  result?: string;
};

export const CLIENTS: Client[] = [
  {
    slug: "yalla-renovation",
    name: "Yalla Renovation",
    url: "https://www.yallarenovation.com/",
    location: "Dubai, United Arab Emirates",
    industry: "Home & villa renovation",
    services: ["Google Ads", "Meta Ads"],
    summary:
      "Paid acquisition for a Dubai home, apartment, office and villa renovation company, run across Google Ads and Meta Ads as a single budget and judged on leads the sales team could actually convert.",
    result: "₹10 lakh monthly ad budget managed, delivering convertible leads from Google and Meta",
  },
  {
    slug: "4s-study-abroad",
    name: "4S Study Abroad",
    url: "https://www.4sstudyabroad.com/",
    location: "Dubai, UAE and India",
    industry: "Overseas education consulting",
    services: ["Google Ads", "Meta Ads"],
    summary:
      "Student enquiry generation for an overseas education consultancy operating out of the UAE and India, held at a steady daily volume for over a year rather than spiking and collapsing with each campaign.",
    result: "Around 15 leads per day sustained for the past year on roughly AED 3,000 a month in Meta Ads",
  },
  {
    slug: "achievers-perfect-career-institute",
    name: "APCI",
    fullName: "Achievers Perfect Career Institute",
    url: "https://achieversperfectcareer.com/",
    location: "Chandigarh, India",
    industry: "Aviation & career training institute",
    services: ["Website development", "SEO", "Online presence"],
    summary:
      "Built the website and online presence for Achievers Perfect Career Institute (APCI), Chandigarh, so students searching for aviation and career training in North India could find and evaluate it.",
    result: "Increased admissions across North India, with Himachal Pradesh the strongest source",
  },
  {
    slug: "ourknots",
    name: "OurKnots",
    url: "https://ourknots.com/",
    location: "India",
    industry: "D2C ethnic laces, trims and accessories",
    services: ["Shopify store development", "D2C brand building", "Performance marketing"],
    summary:
      "Built the Shopify store and the D2C brand around it, covering laces, trims, neck patches and wedding accessories, then scaled the storefront from no sales at all to a steady monthly run rate.",
    result: "From zero sales to ₹3 lakh per month on Shopify",
  },
  {
    slug: "warriors-cove",
    name: "Warrior's Cove",
    url: "https://warriorscove.com/",
    location: "Minneapolis and Saint Paul, Minnesota, USA",
    industry: "Mixed martial arts & Jiu-Jitsu academy",
    services: ["Google Ads", "Meta Ads", "Lead generation"],
    summary:
      "Membership enquiries for a Minnesota mixed martial arts and Jiu-Jitsu academy with gyms in Minneapolis and Saint Paul, delivered continuously through Google Ads and Meta Ads.",
    result: "Over one year of continuous lead delivery",
  },
  {
    slug: "bazayan",
    name: "Bazayan.ch",
    url: "https://bazayan.ch/",
    location: "Switzerland",
    industry: "Pharmaceutical API supply (B2B)",
    services: ["Website development", "B2B web design"],
    summary:
      "Replaced a static, low-traffic website with a modern B2B site for a Swiss pharmaceutical API supplier. The rebuild made the API portfolio clear to read and easy to navigate, which is what its online presence had been missing.",
    result: "Static site replaced with a modern, clearer website and a stronger online presence",
  },
  {
    slug: "touch-abroad",
    name: "Touch Abroad",
    url: "https://touchabroad.ca/",
    location: "Mississauga, Ontario, Canada",
    industry: "Career training & education consulting",
    services: ["Website development", "Google Ads", "Meta Ads"],
    summary:
      "A two-year engagement with a Mississauga-based education consultant covering the website build and the ongoing Google Ads and Meta Ads that fill enquiries for their PSW and skill-based programmes.",
    result: "Two years of continuous website and paid media work",
  },
  {
    slug: "trust-legal",
    name: "Trust Legal",
    url: "https://trustlegal.in/",
    location: "New Delhi, India",
    industry: "Law firm",
    services: ["Website development", "Website maintenance", "Technical support"],
    summary:
      "Rebuilt the firm's website from scratch and have handled maintenance and every technical requirement for the business for the last two years.",
    result: "Two years of ongoing website maintenance",
  },
  {
    slug: "elixir-engineering",
    name: "Elixir Engineering",
    url: "https://www.elixirengg.com/",
    location: "India",
    industry: "Fire safety systems engineering",
    services: ["SEO", "Google Ads"],
    summary:
      "Search visibility and paid search for a fire safety engineering company that handles system maintenance, Form B audits, training and repairs. Multiple target keywords now rank on Google, with Google Ads carrying the intent SEO does not reach yet.",
    result: "40–45 leads per month from SEO and Google Ads",
  },
];
