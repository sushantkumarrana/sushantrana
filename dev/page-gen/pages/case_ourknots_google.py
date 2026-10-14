# Case study: OurKnots on Google Ads, Jan - Sep 2026 (still running).
# Numbers: Google Ads Overview screenshots Sushant shared (one per month):
# "Actual ROAS" column, conversions, cost per conversion, cost (as rounded by Google).
# What changed in the account (campaign types, fixes) is still to come from Sushant;
# do not write any of it until he sends it.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
CTA = "Book your free strategy call"

# month, ROAS %, conversions, cost per conversion (₹), cost (₹)
DATA = [
    ("Jan 2026", 532.68, 16.00, 465, 7450),
    ("Feb 2026", 71.44, 6.00, 2000, 12000),
    ("Mar 2026", 212.88, 8.50, 1070, 9120),
    ("Apr 2026", 382.00, 18.12, 495, 8960),
    ("May 2026", 494.74, 15.38, 593, 9120),
    ("Jun 2026", 287.54, 12.02, 751, 9030),
    ("Jul 2026", 642.78, 25.01, 360, 9010),
    ("Aug 2026", 1197.09, 33.11, 275, 9120),
    ("Sep 2026", 1404.99, 43.91, 206, 9050),
]
MONTHS = [d[0] for d in DATA]
FEB, SEP = DATA[1], DATA[-1]


def rupees(v):
    return f"₹{v / 1000:.2f}K" if v >= 1000 else f"₹{v:.0f}"


chart = L.journey_chart("OurKnots on Google Ads, month by month", ["Jan to Sep 2026"], MONTHS, [
    ("roas", "ROAS", {"bars": [d[1] / 100 for d in DATA], "bar_name": "ROAS", "fmt": lambda v: f"{v:.2f}x", "aria": "Monthly Google Ads ROAS, Jan to Sep 2026",
                      "note": "ROAS as Google Ads reports it in the account's Actual ROAS column. Hover or tap a month for its numbers."}),
    ("conv", "Conversions", {"bars": [d[2] for d in DATA], "bar_name": "Conversions", "fmt": lambda v: f"{v:.2f}",
                             "note": "Google shares credit between ads, so conversions can be fractions."}),
    ("cpa", "Cost per conversion", {"bars": [d[3] for d in DATA], "bar_name": "Cost per conversion", "fmt": rupees,
                                     "note": "Lower is better: from ₹2,000 in February to ₹206 in September."}),
    ("cost", "Spend", {"bars": [d[4] for d in DATA], "bar_name": "Ad spend", "fmt": rupees,
                       "note": "The budget stayed around ₹9K a month the whole time."}),
])

ROWS = [("Ad spend", rupees(FEB[4]), rupees(SEP[4])), ("Conversions", f"{FEB[2]:.2f}", f"{SEP[2]:.2f}"),
        ("Cost per conversion", rupees(FEB[3]), rupees(SEP[3])), ("ROAS", f"{FEB[1] / 100:.2f}x", f"{SEP[1] / 100:.2f}x")]
before_after = figure("Then and now", ["From Google Ads"], (
    '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><table class="w-full border-collapse text-sm">'
    '<thead><tr class="border-b border-[var(--color-line)] bg-[#fff7f3] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="px-3 py-2.5 text-left font-bold">Month</th><th class="px-3 py-2.5 text-right font-bold">Feb 2026</th><th class="px-3 py-2.5 text-right font-bold text-orange">Sep 2026</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="px-3 py-2.5 text-left font-semibold text-ink">{k}</th>'
              f'<td class="px-3 py-2.5 text-right text-body">{a}</td><td class="px-3 py-2.5 text-right font-bold text-ink">{b}</td></tr>' for k, a, b in ROWS)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">Less spend than February, seven times the conversions, and every conversion about ten times cheaper.</p>'))

MILESTONES = [
    ("Jan 2026", "A promising start", "16 conversions at ₹465 each and a 5.33x ROAS in the first month."),
    ("Feb 2026", "The low point", "Spend rose to ₹12K but conversions fell to 6, at ₹2,000 each: a 0.71x ROAS."),
    ("Apr 2026", "Back above 3x", "18.12 conversions at ₹495 each and a 3.82x ROAS, on a smaller ₹8.96K budget."),
    ("Jul 2026", "25 conversions in a month", "25.01 conversions at ₹360 each, a 6.43x ROAS."),
    ("Aug 2026", "Past 10x", "33.11 conversions at ₹275 each and a 11.97x ROAS."),
    ("Sep 2026", "The record month", "43.91 conversions at ₹206 each and a 14.05x ROAS, on ₹9.05K of spend."),
]
milestones = ('<section class="section" id="milestones" aria-labelledby="milestones-heading">'
              + L.centered_head({"id": "milestones", "pill": "Milestones", "h2": ("The road to", "14x on Google"),
                                 "body": ["Same budget all year. These are the months that mattered."]})
              + '<ol class="wrap mt-12 grid list-none gap-4 md:grid-cols-2">' + "".join(
                  f'<li data-reveal="true"{L.d(i, per=2)} class="card flex gap-4 p-6"><span class="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-orange/10 font-[family-name:var(--font-display)] text-xs font-extrabold text-orange">{i + 1:02d}</span>'
                  f'<span><span class="block text-[10px] font-bold uppercase tracking-widest text-orange">{E(m)}</span><span class="mt-1 block text-lg font-extrabold text-ink">{E(t)}</span>'
                  f'<span class="mt-1.5 block text-sm text-body">{E(p)}</span></span></li>'
                  for i, (m, t, p) in enumerate(MILESTONES)) + "</ol></section>")

PAGE = {
    "path": "/case-studies/ourknots-google-ads/",
    "slug": "case-study",
    "form_name": "case_study",
    "service": "Google Ads",
    "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "OurKnots Google Ads case study",
    "thanks_what": "enquiry",
    "title": "OurKnots Google Ads Case Study: 14x ROAS | Sushant Rana",
    "og_title": "OurKnots on Google Ads: 0.71x to 14x ROAS",
    "og_alt": "OurKnots Google Ads case study by Sushant Rana",
    "desc": "How OurKnots went from a 0.71x ROAS on Google Ads in Feb 2026 to 14.05x in Sep 2026 on the same ~₹9K monthly budget, with ₹206 per conversion.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Case Studies", "/case-studies/"), ("Google Ads", "/case-studies/google-ads/"), ("OurKnots", None)],
    "related": [],
    "hero": {
        "pill": "Case study · Google Ads",
        "h1": ("OurKnots on Google Ads:", "0.71x to 14x ROAS"),
        "intro_html": [
            'Google Ads runs alongside Meta for OurKnots, the fabric laces and trims brand. In February 2026 it spent ₹12K for 6 conversions. In September 2026, on a smaller ₹9K budget, it brought <strong class="font-semibold text-ink">43.91 conversions at ₹206 each and a 14.05x ROAS</strong>.',
            "Every number here comes from the Google Ads account, and the campaigns are still running. Hover the chart to follow the turnaround.",
        ],
        "cta_href": "/contact/book-strategy-call/",
        "cta2": ("See the struggle", "#struggle"),
        "stats": [("14.05x", "ROAS, Sep 2026"), ("43.91", "Conversions, Sep 2026"), ("₹206", "Cost per conversion"), ("~₹9K", "Monthly budget")],
        "visual": chart,
    },
    "form": {
        "title": "Want results like this?",
        "sub": "Tell me about your store and I will look at your Google Ads for free.",
        "submit": "Request my free review",
        "steps": [
            {"label": "Business", "fields": [
                {"type": "radio", "name": "business", "label": "What do you sell?", "req": True, "options": ["Online store", "Services", "Something else"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourstore.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["Better ROAS", "Scale spend profitably", "More online sales", "More leads", "Not sure yet"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, what you spend, what is not working..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

url = SITE + "/case-studies/ourknots-google-ads"
PAGE["graph"] = [
    {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": url + "#article"}},
    {"@type": "Article", "@id": url + "#article", "headline": "OurKnots on Google Ads: 0.71x to 14x ROAS", "description": PAGE["desc"],
     "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"}, "datePublished": "2026-10-14", "inLanguage": "en",
     "about": {"@type": "Organization", "name": "OurKnots", "url": "https://ourknots.com"}},
]

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads", "14.05x ROAS", "₹206 per conversion", "43.91 conversions", "~₹9K a month", "Still running"]),
    L.split({"id": "struggle", "anchor": "struggle", "pill": "The real struggle", "h2": ("A good first month,", "then a crash"),
             "body": ["January looked promising at 5.33x. February did not: spend went up to ₹12K and conversions fell to 6, each costing ₹2,000.",
                      "March recovered only to 2.13x, and June slipped back to 2.88x. The turnaround came from making the same budget work harder, not from spending more."],
             "bullets": ["Feb 2026: 0.71x ROAS, ₹2,000 per conversion", "Mar 2026: 2.13x, ₹1,070 per conversion", "Jun 2026: a dip to 2.88x before the climb"],
             "visual": before_after}, dark=True),
    L.section_bg(milestones),
    L.chips_section({"id": "related", "h2": ("More from", "this account"),
                     "body": "Google Ads works alongside Meta for OurKnots. See the other half of the story:",
                     "chips": [("OurKnots on Meta Ads", "/case-studies/ourknots/"), ("Google Ads management", "/services/google-ads/"),
                               ("Google Shopping Ads", "/services/google-shopping-ads/"), ("Performance marketing", "/services/performance-marketing/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want a result", "like this?"),
                          "body": ["Tell me about your store and your Google Ads. I will look at your account and show you where the next gains are, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No obligation"]}),
]

FAQ = [('What ROAS does OurKnots get from Google Ads?', "14.05x in September 2026, up from 0.71x in February 2026, as the account's Actual ROAS column reports it."), ('How much does OurKnots spend on Google Ads?', 'About ₹9K a month. September 2026 was ₹9.05K.'), ('What does a Google Ads conversion cost OurKnots?', '₹206 in September 2026, down from ₹2,000 in February 2026.'), ('Does OurKnots run Meta Ads too?', 'Yes. Google Ads runs alongside Meta Ads, and the OurKnots Meta Ads case study covers the other half of the story.')]
L.add_faq(PAGE, url, ("OurKnots on Google Ads,", "answered"), FAQ)
