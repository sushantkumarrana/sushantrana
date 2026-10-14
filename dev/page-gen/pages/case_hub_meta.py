# Hub: /case-studies/meta-ads/. Featured: OurKnots (data from case_ourknots.py).
# Other clients: published facts only (L.PROJECTS).
import runpy

E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
OK = runpy.run_path("dev/page-gen/pages/case_ourknots.py", init_globals={"L": L})
DATA, money, roas = OK["DATA"], OK["money"], OK["roas"]
SEP = DATA[-1]
F = runpy.run_path("dev/page-gen/pages/case_4s_meta.py", init_globals={"L": L})

chart = L.journey_chart("OurKnots on Meta", ["Jan 2025 to Sep 2026"], [d[0] for d in DATA], [
    ("rev", "Revenue & spend", {"bars": [d[4] for d in DATA], "bar_name": "Revenue Meta reports", "line": [d[1] for d in DATA], "line_name": "Meta ad spend",
                                "fmt": money, "partial": [d[5] for d in DATA], "aria": "OurKnots Meta revenue and spend by month"}),
    ("roas", "ROAS", {"bars": [roas(d) for d in DATA], "bar_name": "Meta ROAS", "fmt": lambda v: f"{v:.2f}x", "note": "Only months with a complete screenshot are shown."}),
])

GLANCE = [("OurKnots", "D2C ecommerce", "5.13x", "Meta ROAS, Sep 2026"), ("4S Study Abroad", "Overseas education, UAE", "7,514", "Student enquiries, 24 months"),
          ("Yalla Renovation", "Home renovation", "~₹10L", "Monthly Google + Meta budget"), ("Warrior's Cove", "Martial arts academy", "1+ yr", "Leads without a break")]
glance = figure("Meta Ads results at a glance", ["Real clients"], (
    '<ul class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-4"><span class="min-w-0">'
        f'<span class="block text-sm font-bold text-ink">{E(n)}</span><span class="block text-xs text-muted">{E(w)}</span></span>'
        f'<span class="text-right"><span class="block font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">{E(v)}</span>'
        f'<span class="block text-[10px] font-semibold uppercase tracking-wider text-muted">{E(l)}</span></span></li>' for n, w, v, l in GLANCE) + "</ul>"))

PAGE = {
    "path": "/case-studies/meta-ads/", "slug": "case-study", "form_name": "case_study", "service": "Meta Ads", "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "Meta Ads case studies", "thanks_what": "enquiry",
    "title": "Meta Ads Case Studies | Sushant Rana",
    "og_title": "Meta Ads Case Studies by Sushant Rana",
    "og_alt": "Meta Ads case studies by Sushant Rana",
    "desc": "Real Meta Ads results: OurKnots from 0.72x to 5.13x ROAS, 4S Study Abroad's 7,514 student enquiries at AED 8.79, and more lead generation accounts.",
    "cta": "Book your free strategy call",
    "trail": [("Home", "/"), ("Case Studies", "/case-studies/"), ("Meta Ads", None)],
    "related": [],
    "hero": {
        "pill": "Case studies · Meta Ads",
        "h1": ("Meta Ads case studies,", "with the real numbers"),
        "intro_html": ['Facebook and Instagram accounts my team and I run right now, for online stores and lead generation businesses in India, the UAE, Canada and the USA.',
                       "Every result here comes from the client's own ad account. Start with the full OurKnots story, then the other accounts below."],
        "cta_href": "/contact/book-strategy-call/", "cta2": ("Read the OurKnots story", "#featured"),
        "stats": [("₹3.84L", "OurKnots store sales, Sep 2026"), ("5.13x", "OurKnots Meta ROAS"), ("~15", "4S enquiries a day"), ("4", "Countries")],
        "visual": glance,
    },
    "form": {"title": "Want results like these?", "sub": "Tell me about your business and I will look at your Meta Ads for free.", "submit": "Request my free review",
             "steps": [
                 {"label": "Business", "fields": [
                     {"type": "radio", "name": "business", "label": "What do you sell?", "req": True, "options": ["Online store", "Services", "Something else"]},
                     {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                      "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                     {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'}]},
                 {"label": "Goals", "fields": [
                     {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                      "options": ["More online sales", "More leads", "Better ROAS", "Scale spend profitably", "Not sure yet"]},
                     {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, what you spend, what is not working..."},
                     {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]}]},
             ]},
}
url = SITE + "/case-studies/meta-ads"
PAGE["graph"] = [
    {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#person"},
     "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": 1, "url": SITE + "/case-studies/ourknots"},
                                                    {"@type": "ListItem", "position": 2, "url": SITE + "/case-studies/4s-study-abroad"}]}},
]
PAGE["sections"] = [
    L.hero(PAGE),
    L.featured_case({"id": "featured", "pill": "Featured case study", "h2": ("OurKnots: from 0.72x", "to 5.13x on Meta"),
                     "body": ["The full journey of a D2C laces and trims brand, from its first order to ₹3.84 lakh a month. Hover the chart for any month."],
                     "name": "OurKnots", "what": "D2C ecommerce · India", "url": "/case-studies/ourknots/", "chart": chart,
                     "story": "In February 2025 the account spent ₹32.7K to bring back ₹23.4K. By September 2026 Meta reported 118 purchases worth ₹3.62 lakh, and the store sold ₹3.84 lakh in the month.",
                     "facts": [("0.72x", "Meta ROAS, Feb 2025"), ("5.13x", "Meta ROAS, Sep 2026"), ("152", "Store orders, Sep 2026"), ("20", "Monthly screenshots")]}),
    L.section_bg(L.featured_case({"id": "foursa", "pill": "Lead generation · UAE", "h2": ("4S Study Abroad: 7,514", "student enquiries at AED 8.79"),
                                  "body": ["24 months of Meta Ads for a study-abroad consultancy. Hover the chart for any month."],
                                  "name": "4S Study Abroad", "what": "Overseas education · UAE", "url": "/case-studies/4s-study-abroad/",
                                  "chart": L.journey_chart("4S Study Abroad on Meta", ["Oct 2024 to Sep 2026"], F["MONTHS"], [
                                      ("enq", "Enquiries", {"bars": [d[2] for d in F["DATA"]], "bar_name": "Form leads", "line": [d[3] for d in F["DATA"]], "line_name": "WhatsApp conversations",
                                                            "fmt": lambda v: f"{v:,.0f}", "partial": [d[4] for d in F["DATA"]], "aria": "4S Study Abroad monthly form leads and WhatsApp conversations"})]),
                                  "story": "AED 66.5K of Meta spend brought 5,372 form leads and 2,142 WhatsApp conversations. In year two, cost per WhatsApp conversation fell 42.5% on 20% less spend.",
                                  "facts": [("7,514", "Student enquiries"), ("AED 8.79", "Per enquiry"), ("AED 4.74", "Per WhatsApp chat"), ("-42.5%", "WhatsApp cost, year on year")]})),
    L.projects_section(["yalla", "warriors", "touch"], ("More Meta Ads accounts", "we run right now"),
                       "Lead generation for renovation, fitness and training brands. Pick one to see what we run for them."),
    L.chips_section({"id": "related", "h2": ("More", "case studies"), "body": "The same brands on other channels, and the service behind these results.",
                     "chips": [("Google Ads case studies", "/case-studies/google-ads/"), ("Meta Ads management", "/services/meta-ads/"), ("Performance marketing", "/services/performance-marketing/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want results", "like these?"),
                          "body": ["Tell me about your business and your Meta Ads. I will look at your account and show you where the next gains are, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No obligation"]}),
]

FAQ = [('Which Meta Ads case studies are on this page?', 'OurKnots, a D2C laces and trims brand that went from a 0.72x to a 5.13x Meta ROAS, and 4S Study Abroad, a study-abroad consultancy in Dubai with 7,514 student enquiries at AED 8.79 each.'), ('Are these real results?', "Yes. Every result comes from the client's own ad account, with monthly screenshots on each case study."), ('Can you look at my Meta Ads account?', 'Yes. Fill in the form on this page and I review your account for free, with no obligation.')]
L.add_faq(PAGE, url, ("Meta Ads case studies,", "answered"), FAQ)
