/**
 * Blog content, stored as data rather than MDX.
 *
 * The site has no CMS and no MDX pipeline, so a post is a typed array of
 * blocks. That keeps the article page a plain server component, gives the
 * sidebar a table of contents for free (every `h2` becomes an anchor), and
 * means adding a post is one object here — no new route, no new build step.
 *
 * To add a post: append to POSTS, drop a 1600x1000 image at the `img` path,
 * and it appears on /blog, /blog/<slug>, the home page teaser and the sitemap.
 *
 * NOTE: the three articles below are first drafts written to fill the pages.
 * Read them before you publish — they're in your voice but they're not your
 * words, and the numbers in them are illustrative.
 */

import { type Block, headingId, tocOf, wordCount } from "./prose";

export type { Block };
export { headingId };

export type Post = {
  slug: string;
  title: string;
  /** Shown on cards and used as the meta description. Keep under ~160 chars. */
  excerpt: string;
  cat: string;
  /** ISO date — display strings are derived, never stored, so they can't drift. */
  date: string;
  img: string;
  /** Service labels from lib/services.ts. Drives the sidebar's related links. */
  related: string[];
  body: Block[];
};

export const POSTS: Post[] = [
  {
    slug: "revenue-systems-vs-marketing-campaigns",
    title:
      "Revenue Systems vs Marketing Campaigns: Why One Compounds and the Other Expires",
    excerpt:
      "Campaigns end. Systems compound. The structural difference between businesses that grow predictably and businesses that buy growth one month at a time.",
    cat: "Business Strategy",
    date: "2026-06-18",
    img: "/blog/post-1.png",
    related: ["Google Ads", "Meta Ads", "Sales Funnel Setup", "CRM Consulting"],
    body: [
      {
        t: "p",
        text: "Most businesses I meet do not have a marketing problem. They have a **structure** problem that shows up as a marketing problem. Spend goes in, leads come out, and when the spend stops, everything stops with it. Nothing that was built last quarter makes this quarter cheaper.",
      },
      {
        t: "p",
        text: "That is the difference between a campaign and a system. A campaign is a purchase. A system is an asset. Both can produce revenue this month; only one of them produces it more cheaply next month.",
      },
      { t: "h2", text: "What actually separates the two" },
      {
        t: "p",
        text: "The distinction is not budget size or channel choice. I have seen ₹50,000-a-month accounts that behave like systems and ₹50-lakh accounts that behave like a series of disconnected campaigns. What separates them is whether each month's work leaves behind something the next month can use.",
      },
      {
        t: "ul",
        items: [
          "**A campaign optimises for the period.** It is judged on the spend and return inside a date range. When the range closes, the learning usually closes with it.",
          "**A system optimises for the next period.** Every month it hands forward cleaner data, a better-qualified audience, sharper creative, and a shorter path from click to cash.",
          "**A campaign's cost is flat or rising.** You pay the same auction price to reach the same stranger, forever.",
          "**A system's cost curve bends down.** Retargeting pools grow, the CRM learns which leads close, and organic and email start absorbing demand that used to cost money.",
        ],
      },
      { t: "h2", text: "The four layers a revenue system needs" },
      {
        t: "p",
        text: "When I audit an account, I am not really looking at the ads. I am looking for which of these four layers is missing, because growth stalls at the weakest one — not the loudest one.",
      },
      { t: "h3", text: "1. Strategy: the offer and who it is for" },
      {
        t: "p",
        text: "No amount of media buying fixes an offer that a buyer does not want at the price you are asking. Before I touch a campaign I want one sentence: who is this for, what changes for them, and why you rather than the alternative. If that sentence is vague, the ads will be vague and the auction will charge you for the vagueness.",
      },
      { t: "h3", text: "2. Acquisition: paid, organic, and the overlap" },
      {
        t: "p",
        text: "This is the layer everyone treats as the whole job. It is one quarter of it. Its real function in a system is not to generate leads — it is to generate *qualified, attributable* leads that the next two layers can act on.",
      },
      { t: "h3", text: "3. Tracking: knowing what actually happened" },
      {
        t: "p",
        text: "This is where most businesses are quietly broken. If your platform reports 200 conversions and your CRM shows 40 real conversations, you are optimising toward a number that does not exist. Every bid strategy, every budget decision, every creative test downstream of bad tracking is a guess wearing a suit.",
      },
      {
        t: "callout",
        title: "The cheapest fix in marketing",
        text: "Before increasing budget, reconcile one month of platform conversions against your CRM. In most accounts I open, the gap is 30-60%. Closing it changes what the algorithm learns — and that is free performance.",
      },
      { t: "h3", text: "4. Conversion: what happens after the lead arrives" },
      {
        t: "p",
        text: "A lead that waits nine hours for a first response is a different asset from one contacted in five minutes. The follow-up sequence, the routing rules, the reminder before the call — these are marketing, even though nobody in marketing owns them. They are also the parts that compound fastest, because they cost nothing per additional lead.",
      },
      { t: "h2", text: "How to tell which one you have" },
      {
        t: "p",
        text: "Ask four questions. Honest answers take about ten minutes and tell you more than a month of reporting.",
      },
      {
        t: "ol",
        items: [
          "If you paused all paid spend for 30 days, how much revenue would still arrive? If the answer is close to zero, you have campaigns.",
          "Is your cost per qualified lead lower than it was six months ago? If it is flat, nothing is compounding.",
          "Can you name your close rate by source? If not, you are optimising volume, not revenue.",
          "What did last quarter build that this quarter inherits? If the honest answer is 'nothing', that is the finding.",
        ],
      },
      { t: "h2", text: "The uncomfortable part" },
      {
        t: "p",
        text: "Systems are slower to show results. A campaign can show a return in week one. A system often looks worse in month one, because you spend it fixing tracking, rewriting the offer, and building follow-up that nobody sees. Month four is where the two lines cross, and month twelve is where the gap stops being an argument.",
      },
      {
        t: "quote",
        text: "You can rent demand or you can build the machine that captures it. Renting is faster. Building is cheaper every month after the first.",
      },
      {
        t: "p",
        text: "If you are choosing between the two, the deciding question is not which produces more revenue this quarter. It is how many more quarters you intend to be in business.",
      },
    ],
  },
  {
    slug: "lead-quality-over-lead-volume",
    title:
      "Lead Quality Over Lead Volume: The Metric Shift That Changes Everything",
    excerpt:
      "A thousand leads that never answer the phone cost more than a hundred that do. How to rebuild campaigns around qualified conversations instead of form fills.",
    cat: "Marketing",
    date: "2026-06-04",
    img: "/blog/post-2.png",
    related: ["Lead Generation", "Google Ads", "AI Lead Scoring", "Pipeline Management"],
    body: [
      {
        t: "p",
        text: "Cost per lead is the most reassuring bad metric in marketing. It always improves when you ask it to. Widen the targeting, soften the form, add a discount hook — the number falls, the dashboard turns green, and the sales team quietly stops trusting marketing.",
      },
      {
        t: "p",
        text: "The problem is not that CPL is wrong. It is that CPL is a **cost** metric being used as a **quality** metric, and those move in opposite directions more often than anyone admits.",
      },
      { t: "h2", text: "The arithmetic nobody runs" },
      {
        t: "p",
        text: "Two campaigns, same monthly spend. Campaign A produces 500 leads at a low CPL. Campaign B produces 120 at four times the CPL. On the dashboard, A wins decisively.",
      },
      {
        t: "p",
        text: "Now add the two columns nobody puts on the dashboard: what share of each set answers the phone, and what share of those closes. When A's leads connect at 20% and close at 5%, and B's connect at 65% and close at 18%, B produces roughly three times the customers for the same money — and it looked like the loser all quarter.",
      },
      {
        t: "callout",
        title: "Run this on your own numbers",
        text: "Take last quarter by source: leads, connect rate, close rate, average deal value. Multiply them out to cost per customer. The ranking almost never matches the cost-per-lead ranking, and that mismatch is the whole argument.",
      },
      {
        t: "p",
        text: "There is also a cost that never appears anywhere: your sales team's hours. Four hundred unqualified leads is not free — it is a week of somebody's month spent being ignored, plus the morale cost of a pipeline that mostly does not answer.",
      },
      { t: "h2", text: "Why platforms drift toward volume" },
      {
        t: "p",
        text: "Not malice — instruction. If you hand Google or Meta a 'lead' conversion that fires on form submit, you have told the algorithm that all form submits are equally valuable. It will then do exactly what you asked, extremely well: find you the cheapest people who will fill in a form. Cheap form-fillers are not the same population as buyers.",
      },
      {
        t: "p",
        text: "The algorithm is not the problem. The definition you gave it is.",
      },
      { t: "h2", text: "Rebuilding around qualified conversations" },
      { t: "h3", text: "Move the conversion event down the funnel" },
      {
        t: "p",
        text: "Stop optimising to form submit. Optimise to the first event that correlates with revenue — a held sales call, a qualified status in the CRM, a completed application. Send that event back to the platform with offline conversion imports or the conversions API. This single change does more for lead quality than any targeting adjustment.",
      },
      {
        t: "ul",
        items: [
          "**Qualified lead** — meets your basic fit criteria (budget, geography, category). The minimum viable upgrade over raw form fills.",
          "**Connected conversation** — someone actually spoke to them. Strong signal, arrives within days.",
          "**Closed revenue with value** — the real target. Best signal, but slow; use it once volume supports it.",
        ],
      },
      { t: "h3", text: "Add friction on purpose" },
      {
        t: "p",
        text: "Every field you remove raises volume and lowers intent. That trade is sometimes right — and it is a trade, not a free win. Adding budget range, timeline, or a required phone number will cut your lead count and raise your customer count. Do it deliberately, and measure it at the customer line, not the lead line.",
      },
      { t: "h3", text: "Let the copy disqualify" },
      {
        t: "p",
        text: "Ads that state price bands, minimum engagement size, or who this is *not* for will lose you clicks you were going to lose anyway — after you paid for them. Pre-qualifying in the ad is the cheapest filter available.",
      },
      { t: "h3", text: "Feed the negative signal back" },
      {
        t: "p",
        text: "Junk leads are training data. Push your disqualified list back as an exclusion audience and let the platform learn the shape of a bad lead, not just the shape of a good one. Most accounts do the first half of this and never the second.",
      },
      { t: "h2", text: "The metric to put on the wall" },
      {
        t: "p",
        text: "Replace cost per lead with **cost per qualified conversation**, and review it by source. It is harder to calculate, it moves slower, and it will occasionally make a campaign you like look bad. That is precisely why it is worth having.",
      },
      {
        t: "quote",
        text: "Volume is what you report when you cannot yet measure quality. Once you can, nobody asks about volume again.",
      },
    ],
  },
  {
    slug: "practical-ai-automation-without-a-data-team",
    title: "Practical AI Automation for Businesses That Don't Have a Data Team",
    excerpt:
      "You don't need ML engineers. You need five workflows: lead scoring, follow-up, reporting, routing, and reactivation — built on the CRM you already pay for.",
    cat: "AI",
    date: "2026-05-21",
    img: "/blog/post-3.png",
    related: [
      "AI Lead Scoring",
      "Workflow Automation",
      "WhatsApp Automation",
      "Reporting Automation",
    ],
    body: [
      {
        t: "p",
        text: "Almost every 'AI strategy' I am shown by a mid-sized business is a list of tools. Almost every one that works is a list of **decisions that used to wait for a human and no longer do**. The tools are interchangeable. The decisions are the asset.",
      },
      {
        t: "p",
        text: "You do not need a data team for any of what follows. You need the CRM you are already paying for, a workflow tool, and the discipline to build one of these at a time.",
      },
      { t: "h2", text: "1. Lead scoring that runs before anyone opens the CRM" },
      {
        t: "p",
        text: "The highest-value minute in your business is the one right after a lead arrives, and it is usually spent on whoever happens to be at the top of a list. Scoring fixes the ordering.",
      },
      {
        t: "p",
        text: "Start rules-based, not clever: company size, geography, stated budget, the page they converted on, the service they picked. That alone reorders the queue usefully. Once you have a few hundred closed-won and closed-lost records, let a model weight those same fields — it will find combinations your rules missed. Do not start there; you will be modelling noise.",
      },
      {
        t: "callout",
        title: "Order of operations",
        text: "Rules first, model second. A rules-based score you trust beats a model you cannot explain to the person who has to act on it at 9am.",
      },
      { t: "h2", text: "2. Follow-up that does not depend on someone remembering" },
      {
        t: "p",
        text: "Speed to first contact is the most reliably underexploited lever in lead generation, and it is entirely an operations problem. An instant, personal-sounding acknowledgement, a reminder before the call, a nudge after a no-show, and a sequence that stops the moment a human replies.",
      },
      {
        t: "p",
        text: "Where AI genuinely helps is drafting the message with the lead's own context — their industry, the page they came from, the service they selected — so the third follow-up does not read like the first one resent. Where it does not help is deciding to send it. That is a workflow rule, and rules are more reliable than judgement here.",
      },
      { t: "h2", text: "3. Reporting that assembles itself" },
      {
        t: "p",
        text: "If a person spends the first two days of each month rebuilding the same spreadsheet, you are paying a salary for copy and paste. Pull spend from the ad platforms, outcomes from the CRM, join them on a campaign ID you control, and have the summary waiting on Monday.",
      },
      {
        t: "p",
        text: "The AI part is the last inch: a short written read of what changed and what looks anomalous. Useful, but only once the numbers underneath are trustworthy. Automating a report built on broken tracking just distributes the error faster.",
      },
      { t: "h2", text: "4. Routing that matches the lead to the right person" },
      {
        t: "p",
        text: "Round-robin is fair to your team and expensive for you. Route by territory, by service, by deal size, by language — and set an escalation so a high-score lead that sits untouched for an hour goes to someone else automatically. That last rule usually pays for the entire build.",
      },
      { t: "h2", text: "5. Reactivation of the list you already own" },
      {
        t: "p",
        text: "Every business I work with is sitting on a few thousand contacts who did not buy and were never contacted again. This is the cheapest revenue in the building — you paid to acquire them once already.",
      },
      {
        t: "ul",
        items: [
          "Segment on why they went cold: no budget then, wrong timing, lost to a competitor, simply never answered.",
          "Send a reason to come back that matches the segment — not a generic newsletter.",
          "Score the replies and push the warm ones straight into the pipeline with a task attached.",
        ],
      },
      { t: "h2", text: "What to build first" },
      {
        t: "p",
        text: "Not all five. Pick the one where the delay currently costs you the most money — for most businesses that is follow-up speed — and ship it in a fortnight. Measure it for a month. Then build the next.",
      },
      {
        t: "quote",
        text: "Automation does not fix a broken process. It runs the broken process faster and at greater volume. Fix the decision first, then automate it.",
      },
      {
        t: "p",
        text: "The businesses that get value from AI are not the ones with the best models. They are the ones that were honest about which decisions were being made badly, and automated those.",
      },
    ],
  },
];

/** Reverse-chronological — the order every listing uses. */
export const POSTS_BY_DATE: Post[] = [...POSTS].sort((a, b) =>
  b.date.localeCompare(a.date)
);

export const getPost = (slug: string): Post | undefined =>
  POSTS.find((p) => p.slug === slug);

export const CATEGORIES: string[] = [...new Set(POSTS.map((p) => p.cat))];

/** "18 Jun 2026" — fixed en-GB so server and client render the same string. */
export function formatDate(iso: string): string {
  return new Date(`${iso}T00:00:00Z`).toLocaleDateString("en-GB", {
    day: "numeric",
    month: "short",
    year: "numeric",
    timeZone: "UTC",
  });
}

/** 200 wpm over the words we actually render, rounded up to a whole minute. */
export const readingTime = (post: Post): number =>
  Math.max(1, Math.ceil(wordCount(post.body) / 200));

/** The h2s of a post, in order — the table of contents. */
export const tableOfContents = (post: Post) => tocOf(post.body);

/** Two other posts to show under an article. Falls back to newest-first. */
export const relatedPosts = (slug: string, limit = 2): Post[] =>
  POSTS_BY_DATE.filter((p) => p.slug !== slug).slice(0, limit);
