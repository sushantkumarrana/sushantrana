/**
 * Client feedback shown on the homepage carousel and the Shopify service page.
 *
 * Each entry is tied to a real project from lib/clients.ts and uses only the
 * facts published there: services, locations and the stated results. No
 * figure appears here that the client list does not already carry.
 *
 * They are written from those project outcomes, not transcribed from a review
 * platform or an email, and the page says so beside them. Before treating any
 * of them as a verbatim quote, send it to the client for approval and replace
 * the text with their own words. Never add Review or AggregateRating schema for
 * these.
 *
 * `name` is the project, not a person. Individual client names are left out on
 * purpose.
 */
export type Testimonial = {
  /** Sector label shown above the quote. */
  industry: string;
  quote: string;
  /** Project name, e.g. "OurKnots". */
  name: string;
  /** What was delivered and where, e.g. "Shopify store · India". */
  company: string;
};

export const TESTIMONIALS: Testimonial[] = [
  {
    industry: "D2C ecommerce",
    name: "OurKnots",
    company: "Shopify store and D2C brand · India",
    quote:
      "We came to Sushant with a product range of laces, trims and wedding accessories and no online sales at all. He built the Shopify store, shaped the brand around it and then ran the marketing that brought buyers in. The store went from zero to around ₹3 lakh a month, and the best part is that it is steady revenue, not a one-off spike from a sale.",
  },
  {
    industry: "Home renovation",
    name: "Yalla Renovation",
    company: "Google Ads and Meta Ads · Dubai",
    quote:
      "Renovation leads are expensive, and most agencies hand you volume that the sales team cannot close. Sushant runs our Google and Meta spend as one budget of around ₹10 lakh a month and judges it on leads we can actually convert into site visits. Our team spends its time on real homeowners and villa owners now, not on chasing numbers that never pick up.",
  },
  {
    industry: "Overseas education",
    name: "4S Study Abroad",
    company: "Meta Ads lead generation · UAE and India",
    quote:
      "What we needed was consistency. For more than a year our Meta Ads have delivered roughly 15 student enquiries every day on a budget of about AED 3,000 a month. Counsellors can plan their week because the pipeline does not collapse between campaigns, and Sushant flags anything that starts to slip before it becomes a problem.",
  },
  {
    industry: "Aviation training",
    name: "Achievers Perfect Career Institute",
    company: "Website, SEO and online presence · Chandigarh",
    quote:
      "Students were searching for aviation and career training across North India and simply not finding us. Sushant rebuilt our website and our online presence so we show up and make sense when someone compares institutes. Admissions increased across the region, and Himachal Pradesh has become our strongest source of new students.",
  },
  {
    industry: "Martial arts academy",
    name: "Warrior's Cove",
    company: "Google Ads and Meta Ads · Minnesota, USA",
    quote:
      "We run gyms in Minneapolis and Saint Paul, and membership enquiries are the lifeblood of the business. Sushant has kept Google Ads and Meta Ads delivering leads continuously for over a year, from India, without us ever feeling the time difference. Reporting is clear, and when something needs to change he tells us before we have to ask.",
  },
  {
    industry: "Pharmaceutical B2B",
    name: "Bazayan.ch",
    company: "B2B website rebuild · Switzerland",
    quote:
      "Our old website was static, dated and barely visited, which is a poor first impression for a pharmaceutical API supplier. Sushant replaced it with a modern B2B site that lays out our API portfolio clearly and is easy to navigate. Buyers can now understand what we supply within a few clicks, which is exactly what our online presence was missing.",
  },
  {
    industry: "Career training",
    name: "Touch Abroad",
    company: "Website, Google Ads and Meta Ads · Ontario, Canada",
    quote:
      "Sushant has worked with us for two years. He built the website and has run the Google Ads and Meta Ads that fill enquiries for our PSW and skill-based programmes ever since. Having one person own both the site and the ads means nothing falls between two vendors, and every intake starts with a full list of people to call.",
  },
  {
    industry: "Legal services",
    name: "Trust Legal",
    company: "Website rebuild and maintenance · New Delhi",
    quote:
      "A law firm cannot afford a website that breaks or looks neglected. Sushant rebuilt ours from scratch and has handled maintenance and every technical requirement for the last two years. We raise an issue, it gets fixed, and we get back to our clients. That reliability is worth more to us than any redesign.",
  },
  {
    industry: "Fire safety engineering",
    name: "Elixir Engineering",
    company: "SEO and Google Ads · India",
    quote:
      "We handle fire safety maintenance, Form B audits, training and repairs, and none of it is easy to find online. Sushant got several of our target keywords ranking on Google and uses Google Ads to cover the searches SEO has not reached yet. Between the two we now receive 40 to 45 leads every month.",
  },
];
