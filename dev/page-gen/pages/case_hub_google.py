# Hub: /case-studies/google-ads/. Featured: OurKnots on Google (case_ourknots_google.py).
# Other clients: published facts only (L.PROJECTS).
import runpy

E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
G = runpy.run_path("dev/page-gen/pages/case_ourknots_google.py", init_globals={"L": L})
DATA, rupees = G["DATA"], G["rupees"]
Y = runpy.run_path("dev/page-gen/pages/case_yalla_google.py", init_globals={"L": L})
FG = runpy.run_path("dev/page-gen/pages/case_4s_google.py", init_globals={"L": L})

chart = L.journey_chart("OurKnots on Google Ads", ["Jan to Sep 2026"], [d[0] for d in DATA], [
    ("roas", "ROAS", {"bars": [d[1] / 100 for d in DATA], "bar_name": "ROAS", "fmt": lambda v: f"{v:.2f}x", "aria": "OurKnots Google Ads ROAS by month"}),
    ("cpa", "Cost per conversion", {"bars": [d[3] for d in DATA], "bar_name": "Cost per conversion", "fmt": rupees}),
])

GLANCE = [("OurKnots", "D2C ecommerce", "14.05x", "ROAS, Sep 2026"), ("Elixir Engineering", "Fire safety engineering", "40-45", "Leads a month, SEO + Ads"),
          ("Yalla Renovation", "Home renovation, Dubai", "2,287", "Form submissions, 24 months"), ("Warrior's Cove", "Martial arts academy", "1+ yr", "Leads without a break")]
glance = figure("Google Ads results at a glance", ["Real clients"], (
    '<ul class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-4"><span class="min-w-0">'
        f'<span class="block text-sm font-bold text-ink">{E(n)}</span><span class="block text-xs text-muted">{E(w)}</span></span>'
        f'<span class="text-right"><span class="block font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">{E(v)}</span>'
        f'<span class="block text-[10px] font-semibold uppercase tracking-wider text-muted">{E(l)}</span></span></li>' for n, w, v, l in GLANCE) + "</ul>"))

PAGE = {
    "path": "/case-studies/google-ads/", "slug": "case-study", "form_name": "case_study", "service": "Google Ads", "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "Google Ads case studies", "thanks_what": "enquiry",
    "title": "Google Ads Case Studies | Sushant Rana",
    "og_title": "Google Ads Case Studies by Sushant Rana",
    "og_alt": "Google Ads case studies by Sushant Rana",
    "desc": "Real Google Ads results: OurKnots from 0.71x to 14.05x ROAS, Yalla Renovation's 2,287 tracked form leads in Dubai, and more lead generation accounts.",
    "cta": "Book your free strategy call",
    "trail": [("Home", "/"), ("Case Studies", "/case-studies/"), ("Google Ads", None)],
    "related": [],
    "hero": {
        "pill": "Case studies · Google Ads",
        "h1": ("Google Ads case studies,", "with the real numbers"),
        "intro_html": ['Google Ads accounts my team and I run right now, for online stores and lead generation businesses in India, the UAE, Canada and the USA.',
                       "Every result here comes from the client's own ad account. Start with the OurKnots turnaround and Yalla Renovation's lead engine, then the other accounts below."],
        "cta_href": "/contact/book-strategy-call/", "cta2": ("Read the OurKnots story", "#featured"),
        "stats": [("14.05x", "OurKnots ROAS, Sep 2026"), ("₹206", "OurKnots cost per conversion"), ("2,287", "Yalla form submissions"), ("4", "Countries")],
        "visual": glance,
    },
    "form": {"title": "Want results like these?", "sub": "Tell me about your business and I will look at your Google Ads for free.", "submit": "Request my free review",
             "steps": [
                 {"label": "Business", "fields": [
                     {"type": "radio", "name": "business", "label": "What do you sell?", "req": True, "options": ["Online store", "Services", "Something else"]},
                     {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                      "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                     {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'}]},
                 {"label": "Goals", "fields": [
                     {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                      "options": ["More online sales", "More leads", "Better ROAS", "Lower cost per lead", "Not sure yet"]},
                     {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, what you spend, what is not working..."},
                     {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]}]},
             ]},
}
url = SITE + "/case-studies/google-ads"
PAGE["graph"] = [
    {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#person"},
     "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": 1, "url": SITE + "/case-studies/ourknots-google-ads"},
                                                    {"@type": "ListItem", "position": 2, "url": SITE + "/case-studies/yalla-renovation"},
                                                    {"@type": "ListItem", "position": 3, "url": SITE + "/case-studies/4s-study-abroad-google-ads"}]}},
]
PAGE["sections"] = [
    L.hero(PAGE),
    L.featured_case({"id": "featured", "pill": "Featured case study", "h2": ("OurKnots: 0.71x to", "14x on Google Ads"),
                     "body": ["The same ~₹9K monthly budget, made to work harder month after month. Hover the chart for any month."],
                     "name": "OurKnots", "what": "D2C ecommerce · India", "url": "/case-studies/ourknots-google-ads/", "chart": chart,
                     "story": "In February 2026 Google Ads spent ₹12K for 6 conversions at ₹2,000 each. In September 2026 it brought 43.91 conversions at ₹206 each, a 14.05x ROAS on ₹9.05K.",
                     "facts": [("0.71x", "ROAS, Feb 2026"), ("14.05x", "ROAS, Sep 2026"), ("₹206", "Cost per conversion"), ("~₹9K", "Monthly budget")]}),
    L.section_bg(L.featured_case({"id": "yalla", "pill": "Lead generation · UAE", "h2": ("Yalla Renovation: 2,287", "tracked form submissions"),
                                  "body": ["24 months of Search and Performance Max for a Dubai renovation company. Hover the chart for any month."],
                                  "name": "Yalla Renovation", "what": "Home renovation · Dubai", "url": "/case-studies/yalla-renovation/",
                                  "chart": L.journey_chart("Yalla Renovation on Google Ads", ["Oct 2024 to Sep 2026"], Y["MONTHS"], [
                                      ("conv", "Conversions", {"bars": [d[3] for d in Y["DATA"]], "bar_name": "Recorded conversions", "fmt": lambda v: f"{v:,.2f}".replace(".00", ""),
                                                               "aria": "Yalla Renovation Google Ads recorded conversions by month"}),
                                      ("cost", "Spend", {"bars": [d[1] for d in Y["DATA"]], "bar_name": "Ad spend", "fmt": Y["aed_k"]})]),
                                  "story": "12.5M impressions, 254K clicks and 2,287 tracked form submissions in 24 months. One Performance Max campaign brought 67.2% of the forms on 32.8% of the spend.",
                                  "facts": [("12.5M+", "Impressions"), ("254K+", "Clicks"), ("2,287", "Form submissions"), ("+244%", "Recorded conversions")]})),
    L.featured_case({"id": "foursg", "pill": "Lead generation · Education", "h2": ("4S Study Abroad: 8,859", "enquiries at ₹278"),
                     "body": ["19 quarters of Google Ads for a study-abroad consultancy in Dubai, including the bad year. Hover the chart for any quarter."],
                     "name": "4S Study Abroad", "what": "Overseas education · Dubai, UAE", "url": "/case-studies/4s-study-abroad-google-ads/",
                     "chart": L.journey_chart("4S Study Abroad on Google Ads", ["Q2 2020 to Q4 2024"], [q[0] for q in FG["Q"]], [
                         ("enq", "Enquiries", {"bars": [q[4] for q in FG["Q"]], "bar_name": "Enquiries", "fmt": lambda v: f"{v:,.0f}",
                                               "aria": "4S Study Abroad Google Ads enquiries by quarter"}),
                         ("cpe", "Cost per enquiry", {"bars": [q[8] for q in FG["Q"]], "bar_name": "Cost per enquiry", "fmt": lambda v: FG["inr"](v)})]),
                     "story": "₹24.6 lakh of Google Ads brought 8,859 enquiries at ₹277.91 each. After a costly reach experiment in 2023, cost per enquiry fell 59.6% from Q4 2023 to Q4 2024.",
                     "facts": [("8,859", "Enquiries"), ("₹278", "Per enquiry"), ("16.47%", "Click to enquiry"), ("−59.6%", "Q4 23 to Q4 24")]}),
    L.section_bg(L.projects_section(["elixir", "warriors", "touch"], ("More Google Ads accounts", "we run right now"),
                                    "Lead generation for engineering, fitness and training brands. Pick one to see what we run for them.")),
    L.chips_section({"id": "related", "h2": ("More", "case studies"), "body": "The same brands on other channels, and the service behind these results.",
                     "chips": [("Meta Ads case studies", "/case-studies/meta-ads/"), ("Google Ads management", "/services/google-ads/"), ("Google Shopping Ads", "/services/google-shopping-ads/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want results", "like these?"),
                          "body": ["Tell me about your business and your Google Ads. I will look at your account and show you where the next gains are, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No obligation"]}),
]

FAQ = [('Which Google Ads case studies are on this page?', 'OurKnots, a D2C brand that went from a 0.71x to a 14.05x ROAS; Yalla Renovation in Dubai, with 2,287 tracked form submissions in 24 months; and 4S Study Abroad, with 8,859 enquiries at ₹278 each.'), ('Are these real results?', "Yes. Every result comes from the client's own Google Ads account, with screenshots on each case study."), ('Can you look at my Google Ads account?', 'Yes. Fill in the form on this page and I review your account for free, with no obligation.')]
L.add_faq(PAGE, url, ("Google Ads case studies,", "answered"), FAQ)
