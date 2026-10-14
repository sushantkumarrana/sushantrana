# Case study: OurKnots on Meta Ads, Jan 2025 - Sep 2026 (campaign still running).
# Every number comes from Sushant's Meta Ads Manager screenshots (campaigns view,
# one per month), summed per month. Never name the agency behind the old PDF.
# Screenshots on the page: campaign names and ad account blurred on request.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
CTA = "Book your free strategy call"

# month, spend, reach, purchases, purchase value, partial?
# partial = some campaign rows were outside the screenshot: purchases/value are a floor.
# None = no screenshot for that month yet.
DATA = [
    ("Jan 2025", 21635.07, 489949, 19, 36684.21, True),
    ("Feb 2025", 32685.18, 164786, 12, 23443.55, False),
    ("Mar 2025", 18846.58, 46913, 15, 21034.40, False),
    ("Apr 2025", 17665.44, 41301, 16, 37627.13, False),
    ("May 2025", None, None, None, None, False),
    ("Jun 2025", 25287.80, 20554, 29, 76426.44, False),
    ("Jul 2025", 32119.90, 26960, 15, 50528.60, False),
    ("Aug 2025", 41487.06, 85473, 40, 74187.60, False),
    ("Sep 2025", 60319.32, 57323, 72, 108791.79, False),
    ("Oct 2025", 65546.27, 33306, 78, 110941.37, True),
    ("Nov 2025", 53654.64, 38523, 34, 62162.53, True),
    ("Dec 2025", 52860.17, 1933859, 15, 23893.50, True),
    ("Jan 2026", 41994.70, 1172071, 39, 73685.50, False),
    ("Feb 2026", 49311.55, 1256588, 51, 128443.75, False),
    ("Mar 2026", 57520.65, 1467805, 70, 181226.05, True),
    ("Apr 2026", 59020.11, 1359800, 70, 209575.00, False),
    ("May 2026", 60229.83, 1074551, 63, 184173.55, False),
    ("Jun 2026", 72996.71, 1379454, 71, 204869.65, False),
    ("Jul 2026", 88333.45, 1450031, 116, 278553.79, False),
    ("Aug 2026", 72770.22, 1306057, 87, 224096.58, False),
    ("Sep 2026", 70614.79, 1176524, 118, 362420.25, False),
]
MONTHS = [d[0] for d in DATA]

# Shopify "Total sales over time" export (Total sales = net sales + shipping + taxes).
# Nov and Dec 2024 come from the export's previous-period columns.
SHOP = [  # month, orders, total sales
    ("Nov 2024", 1, 10.00), ("Dec 2024", 8, 29729.03),
    ("Jan 2025", 24, 47304.21), ("Feb 2025", 10, 20303.55), ("Mar 2025", 25, 86249.15), ("Apr 2025", 21, 54550.13),
    ("May 2025", 20, 50533.90), ("Jun 2025", 28, 57959.34), ("Jul 2025", 15, 24913.56), ("Aug 2025", 41, 76337.90),
    ("Sep 2025", 76, 98924.29), ("Oct 2025", 126, 154384.96), ("Nov 2025", 55, 94024.01), ("Dec 2025", 55, 95326.38),
    ("Jan 2026", 52, 100651.25), ("Feb 2026", 67, 156821.50), ("Mar 2026", 88, 165615.55), ("Apr 2026", 97, 226349.00),
    ("May 2026", 78, 181445.05), ("Jun 2026", 100, 245178.66), ("Jul 2026", 136, 281344.31), ("Aug 2026", 116, 307097.50),
    ("Sep 2026", 152, 383638.35),
]
# Google Ads cost by month (Overview screenshots, rounded by Google); Google ran from Jan 2026.
GSPEND = {"Jan 2026": 7450, "Feb 2026": 12000, "Mar 2026": 9120, "Apr 2026": 8960, "May 2026": 9120,
          "Jun 2026": 9030, "Jul 2026": 9010, "Aug 2026": 9120, "Sep 2026": 9050}
ALL_MONTHS = [m for m, _, _ in SHOP]
META = {d[0]: d for d in DATA}


def total_spend(m):
    d = META.get(m)
    if not d or d[1] is None:
        return None
    return d[1] + GSPEND.get(m, 0)
_MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SLUG = {m: f"20{m[-2:]}-{_MON.index(m[:3]) + 1:02d}" for m in MONTHS}


def money(v):
    if v is None:
        return "–"
    if v >= 100000:
        return f"₹{v / 100000:.2f}L"
    if v >= 1000:
        return f"₹{v / 1000:.1f}K"
    return f"₹{v:.0f}"


def big(v):
    return "–" if v is None else f"{v / 1e6:.2f}M" if v >= 1e6 else f"{v / 1000:.0f}K" if v >= 1000 else str(int(v))


def roas(d):
    return None if d[1] is None or d[5] else d[4] / d[1]


SEP26, FEB25 = DATA[-1], DATA[1]

def blended(m, sales):
    t = total_spend(m)
    return sales / t if t else None


store_chart = L.journey_chart("OurKnots, from the first order", ["Nov 2024 to Sep 2026"], ALL_MONTHS, [
    ("store", "Store sales & ad spend", {"bars": [v for _, _, v in SHOP], "bar_name": "Shopify total sales",
                                         "line": [total_spend(m) for m in ALL_MONTHS], "line_name": "Ad spend, Meta + Google", "fmt": money,
                                         "aria": "OurKnots Shopify total sales and ad spend by month, Nov 2024 to Sep 2026",
                                         "note": "Sales from Shopify. Ad spend from Meta Ads Manager plus Google Ads (Google from Jan 2026). Hover or tap a month."}),
    ("orders", "Orders", {"bars": [o for _, o, _ in SHOP], "bar_name": "Shopify orders", "fmt": lambda v: f"{v:.0f}",
                          "note": "From 1 order in November 2024 to 152 in September 2026."}),
    ("meta", "Meta revenue", {"bars": [META[m][4] if m in META else None for m in ALL_MONTHS], "bar_name": "Revenue Meta reports",
                              "fmt": money, "partial": [META[m][5] if m in META else False for m in ALL_MONTHS]}),
    ("reach", "Reach", {"bars": [META[m][2] if m in META else None for m in ALL_MONTHS], "bar_name": "People reached on Meta", "fmt": big,
                        "note": "Reach jumps from December 2025, when a low cost video awareness campaign started feeding retargeting."}),
    ("blended", "Blended ROAS", {"bars": [blended(m, v) for m, _, v in SHOP], "bar_name": "Store sales ÷ ad spend", "fmt": lambda v: f"{v:.2f}x",
                                 "note": "All Shopify sales divided by all ad spend: the number we actually judge the account on."}),
])


# ------------------------------------------------------------- before / after
ROWS = [("Ad spend", money(FEB25[1]), money(SEP26[1])), ("Purchases", str(FEB25[3]), str(SEP26[3])),
        ("Revenue from Meta", money(FEB25[4]), money(SEP26[4])), ("ROAS", f"{roas(FEB25):.2f}x", f"{roas(SEP26):.2f}x"),
        ("Cost per purchase", money(FEB25[1] / FEB25[3]), money(SEP26[1] / SEP26[3]))]
before_after = figure("Then and now", ["From Meta Ads Manager"], (
    '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><table class="w-full border-collapse text-sm">'
    '<thead><tr class="border-b border-[var(--color-line)] bg-[#fff7f3] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="px-3 py-2.5 text-left font-bold">Month</th><th class="px-3 py-2.5 text-right font-bold">Feb 2025</th><th class="px-3 py-2.5 text-right font-bold text-orange">Sep 2026</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="px-3 py-2.5 text-left font-semibold text-ink">{k}</th>'
              f'<td class="px-3 py-2.5 text-right text-body">{a}</td><td class="px-3 py-2.5 text-right font-bold text-ink">{b}</td></tr>' for k, a, b in ROWS)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">A little over twice the spend, almost ten times the purchases and over fifteen times the revenue.</p>'))

# ------------------------------------------------------------------ milestones
MILESTONES = [
    ("Nov 2024", "The first order", "The Shopify store took its very first order. December brought 8 more."),
    ("Feb 2025", "The low point", f"₹32.7K spent across catalogue, engagement and messenger campaigns for {FEB25[3]} purchases worth {money(FEB25[4])}: a {roas(FEB25):.2f}x ROAS."),
    ("Jun 2025", "The first 3x month", f"One focused sale campaign did {money(DATA[5][4])} from {money(DATA[5][1])} of spend, a 3.02x ROAS. July slipped back to 1.57x."),
    ("Sep 2025", "Meta crosses ₹1 lakh in a month", f"{DATA[8][3]} purchases worth {money(DATA[8][4])}, still at a thin 1.80x ROAS as spend climbed to {money(DATA[8][1])}."),
    ("Oct 2025", "The store crosses ₹1 lakh in a month", "126 orders and ₹1.54 lakh of total sales in the Diwali month, the store's first ₹1 lakh month."),
    ("Jan 2026", "₹1 lakh plus, every month", "From January 2026 the store has crossed ₹1 lakh of sales every single month, and Meta alone has reported over ₹1.28 lakh a month since February."),
    ("Jul 2026", "100+ purchases in a month", f"{DATA[18][3]} purchases worth {money(DATA[18][4])} on {money(DATA[18][1])} of spend."),
    ("Sep 2026", "The record month", f"152 orders and ₹3.84 lakh of store sales. Meta reported {SEP26[3]} purchases worth {money(SEP26[4])} at {roas(SEP26):.2f}x, and the best sale campaign returned 9.94x."),
]
milestones = ('<section class="section" id="milestones" aria-labelledby="milestones-heading">'
              + L.centered_head({"id": "milestones", "pill": "Milestones", "h2": ("From one order to", "₹3.84 lakh a month"),
                                 "body": ["Not a straight line. These are the months that mattered."]})
              + '<ol class="wrap mt-12 grid list-none gap-4 md:grid-cols-2">' + "".join(
                  f'<li data-reveal="true"{L.d(i, per=2)} class="card flex gap-4 p-6"><span class="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-orange/10 font-[family-name:var(--font-display)] text-xs font-extrabold text-orange">{i + 1:02d}</span>'
                  f'<span><span class="block text-[10px] font-bold uppercase tracking-widest text-orange">{E(m)}</span><span class="mt-1 block text-lg font-extrabold text-ink">{E(t)}</span>'
                  f'<span class="mt-1.5 block text-sm text-body">{E(p)}</span></span></li>'
                  for i, (m, t, p) in enumerate(MILESTONES)) + "</ol></section>")

# ---------------------------------------------------------------------- proof
SHOTS = [d for d in DATA if d[1] is not None]


def caption(d):
    part = " · part of the campaign list is below the fold, so purchases shown are a floor" if d[5] else ""
    r = f" · ROAS {roas(d):.2f}x" if roas(d) else ""
    return f"Spend {money(d[1])} · {d[3]} purchases · {money(d[4])} revenue{r}{part}"


def shot(d):
    slug = SLUG[d[0]]
    srcset = ", ".join(f"/img/{w}/case-studies/ourknots/meta-{slug}.webp {w}w" for w in (640, 1080, 1920))
    return (f'<a href="/img/1920/case-studies/ourknots/meta-{slug}.webp" target="_blank" rel="noopener" class="block overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            f'<img alt="OurKnots Meta Ads Manager campaigns view for {d[0]}, campaign names blurred" loading="lazy" decoding="async" width="1920" height="1072" '
            f'class="block h-auto w-full" sizes="(min-width: 1024px) 1100px, 92vw" srcSet="{srcset}" src="/img/1080/case-studies/ourknots/meta-{slug}.webp"/></a>')


LAST = len(SHOTS) - 1
proof = ('<section class="section" id="proof" aria-labelledby="proof-heading">'
         + L.centered_head({"id": "proof", "pill": "Proof", "h2": ("Every month, straight from", "Meta Ads Manager"),
                            "body": ["The campaigns view for each month. Campaign names and the ad account are blurred; every number is as Meta reports it. Pick a month, then click the screenshot to open it full size."]})
         + '<div class="wrap mt-10" data-tabs="true"><div data-reveal="true" class="flex gap-2 overflow-x-auto pb-2">' + "".join(
             f'<button type="button" data-tab="{SLUG[d[0]]}" aria-pressed="{"true" if i == LAST else "false"}" data-on="border-orange bg-orange text-white" '
             f'data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" class="shrink-0 rounded-full border px-4 py-2 text-xs font-semibold transition '
             f'{"border-orange bg-orange text-white" if i == LAST else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{d[0]}</button>'
             for i, d in enumerate(SHOTS))
         + '</div><div data-reveal="true" style="--d:0.1s" class="mt-6">' + "".join(
             f'<div data-panel="{SLUG[d[0]]}"{L.HID if i != LAST else ""}>{shot(d)}<p class="mt-3 text-center text-sm text-body"><strong class="font-semibold text-ink">{d[0]}.</strong> {E(caption(d))}</p></div>'
             for i, d in enumerate(SHOTS))
         + "</div></div></section>")

# --------------------------------------------- the store vs what platforms report
SEP_SPEND = SEP26[1] + GSPEND["Sep 2026"]
G_VALUE = 14.0499 * GSPEND["Sep 2026"]  # Google's Actual ROAS x cost
SOURCES = [("Shopify, what the store sold", "₹3.84L", "152 orders"),
           ("Meta reports", money(SEP26[4]), f"{SEP26[3]} purchases"),
           ("Google Ads reports, about", money(G_VALUE), "43.91 conversions"),
           ("Blended ROAS", f"{383638.35 / SEP_SPEND:.2f}x", f"Store sales ÷ {money(SEP_SPEND)} of ad spend")]
sources_box = figure("September 2026, three views", ["Real numbers"], (
    '<ul class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border p-4 {"border-orange bg-[#fff7f3]" if i in (0, 3) else "border-[var(--color-line)] bg-white"}">'
        f'<span class="min-w-0"><span class="block text-[10px] font-bold uppercase tracking-wider text-muted">{E(k)}</span><span class="block text-xs text-body">{E(n)}</span></span>'
        f'<span class="font-[family-name:var(--font-display)] text-xl font-extrabold {"text-orange" if i in (0, 3) else "text-ink"}">{E(v)}</span></li>'
        for i, (k, v, n) in enumerate(SOURCES)) + "</ul>"))

LEVERS = [
    {"icon": "layers", "h3": "Fewer, stronger campaigns", "p": "In early 2025 a small budget was split across up to eight campaigns at once. Today four sale campaigns and one awareness campaign carry the spend, so Meta can actually learn."},
    {"icon": "image", "h3": "Creative as the main lever", "p": "A steady rhythm of new offer angles, formats and hooks, with tired creative retired before it can push the cost per purchase up."},
    {"icon": "play", "h3": "A cheap awareness layer", "p": "Around ₹3K a month of video awareness reaches over a million people and keeps retargeting audiences full of warm shoppers."},
    {"icon": "chart", "h3": "Decisions on real revenue", "p": "Meta's numbers are checked against Shopify every day, so budget follows money in the bank, not platform reported results alone."},
]

PAGE = {
    "path": "/case-studies/ourknots/",
    "slug": "case-study",
    "form_name": "case_study",
    "service": "Meta Ads",
    "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "OurKnots case study",
    "thanks_what": "enquiry",
    "title": "OurKnots Meta Ads Case Study: 5.13x ROAS | Sushant Rana",
    "og_title": "OurKnots on Meta Ads: from 0.72x to 5.13x ROAS",
    "og_alt": "OurKnots Meta Ads case study by Sushant Rana",
    "desc": "How OurKnots grew from its first order in Nov 2024 to ₹3.84L of store sales in Sep 2026, as Meta ROAS rose from 0.72x to 5.13x. Real data and screenshots.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Case Studies", "/case-studies/"), ("Meta Ads", "/case-studies/meta-ads/"), ("OurKnots", None)],
    "related": [],
    "hero": {
        "pill": "Case study · Meta Ads",
        "h1": ("OurKnots on Meta:", "from 0.72x to 5.13x ROAS"),
        "intro_html": [
            'OurKnots sells fabric laces, borders and trims through its Shopify store, which took its first order in November 2024. In February 2025 its Meta Ads spent ₹32.7K to bring back ₹23.4K. My team and I rebuilt the account month by month, and in September 2026 the store did <strong class="font-semibold text-ink">₹3.84 lakh from 152 orders</strong>, with Meta reporting a 5.13x ROAS.',
            "Sales come from Shopify, ad numbers from Meta Ads Manager and Google Ads, and the campaigns are still running. Hover the chart to follow the journey month by month.",
        ],
        "cta_href": "/contact/book-strategy-call/",
        "cta2": ("See the real struggle", "#struggle"),
        "stats": [("₹3.84L", "Store sales, Sep 2026"), ("152", "Orders, Sep 2026"), ("5.13x", "Meta ROAS, Sep 2026"), ("₹1L+", "Store sales every month in 2026")],
        "visual": store_chart,
    },
    "form": {
        "title": "Want results like this?",
        "sub": "Tell me about your store and I will look at your ads for free.",
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

url = SITE + "/case-studies/ourknots"
PAGE["graph"] = [
    {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": url + "#article"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/img/1920/case-studies/ourknots/meta-2026-09.webp"}},
    {"@type": "Article", "@id": url + "#article", "headline": "OurKnots on Meta: from 0.72x to 5.13x ROAS", "description": PAGE["desc"],
     "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"}, "datePublished": "2026-10-14", "dateModified": "2026-10-14", "inLanguage": "en",
     "image": [SITE + f"/img/1920/case-studies/ourknots/meta-{SLUG[d[0]]}.webp" for d in SHOTS[-4:]],
     "about": {"@type": "Organization", "name": "OurKnots", "url": "https://ourknots.com"}},
]

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Meta Ads", "₹3.62L in Sep 2026", "5.13x ROAS", "118 purchases", "Shopify", "D2C ecommerce", "Still running"]),
    L.split({"id": "struggle", "anchor": "struggle", "pill": "The real struggle", "h2": ("A year of", "thin, unstable returns"),
             "body": ["This did not start as a success story. For most of 2025 the account spent money without a clear engine behind it.",
                      "Catalogue, engagement and messenger campaigns brought reach and chats but very few purchases. Sale pushes for Holi, summer and June worked for a month and faded the next. Even when spend rose to ₹60K a month in September 2025, every rupee returned only about ₹1.80."],
             "bullets": ["Feb 2025: ₹32.7K spent for 12 purchases, a 0.72x ROAS",
                         "Feb 2025: a ₹32K budget split across eight campaigns at once",
                         "Jun 2025 hit 3.02x, then July fell back to 1.57x",
                         "Jan 2026: a post festive dip to 1.75x"],
             "visual": before_after}, dark=True),
    L.split({"id": "truth", "pill": "Meta, Google and the store", "h2": ("Why we judge on", "Shopify, not the ad platforms"),
             "body": ["Add up what Meta and Google each report for September 2026 and you get more than the store actually sold. That is normal: a shopper who clicked a Meta ad and a Google ad before buying is counted by both.",
                      "So the account is judged on Shopify: everything the store sold, divided by everything spent on ads. In September 2026 that blended number was 4.82x."],
             "bullets": ["Meta and Google numbers overlap", "Shopify is the single source of truth", "Budget moves on blended ROAS, not platform ROAS"],
             "visual": sources_box}, flip=True),
    L.icon_cards({"id": "approach", "pill": "What we changed", "h2": ("Four changes that", "turned the account around"),
                  "body": ["No single trick. A simpler account, better creative and decisions made on real revenue."],
                  "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": LEVERS}),
    L.section_bg(milestones + proof),
    L.process({"id": "process", "pill": "The method", "h2": ("How we lift ROAS", "in the first 60 days"),
               "body": ["The same playbook we would run on a new account. The aim of the first 60 days is not a spike, it is a stable, scalable ROAS floor to push budget into."],
               "steps": [
                   {"h3": "Audit and clean base", "short": "Days 0-15", "p": "A full account, pixel, Conversions API and event quality audit. Tracking gaps are fixed first, redundant campaigns are cut, and a daily Shopify versus Meta tracker is set up.", "points": ["Pixel and CAPI audit", "Campaigns consolidated", "Daily revenue tracker"]},
                   {"h3": "Establish the ROAS floor", "short": "Days 15-30", "p": "A lean prospecting and retargeting structure with three to five tested creative angles, left to exit the learning phase cleanly.", "points": ["Lean structure", "3 to 5 creative angles", "Winning offer found"]},
                   {"h3": "Compound the winners", "short": "Days 30-45", "p": "Double down on winning creative and audiences, retire tired ads before costs drift up, and add bundles or threshold offers to raise revenue per order.", "points": ["Winners scaled", "Fatigue caught early", "AOV levers added"]},
                   {"h3": "Scale without breaking", "short": "Days 45-60", "p": "Budget rises in controlled steps on proven campaigns, watching frequency and marginal ROAS, with an always on creative pipeline behind it.", "points": ["Controlled budget steps", "Marginal ROAS watched", "Documented structure"]},
               ]}),
    L.dark_cards({"id": "needle", "pill": "What moved the needle", "h2": ("What made the difference", "in September 2026"),
                  "body": ["The record month, campaign by campaign."],
                  "cards": [
                      {"h3": "One ABO sale campaign at 9.94x", "p": "₹89.1K of purchases from ₹8,965 of spend, the controllable sale campaign that came out of consolidating the old sprawl."},
                      {"h3": "The workhorse at 5.52x", "p": "The core sale campaign drove 44 purchases worth ₹1.32 lakh from ₹24K of spend."},
                      {"h3": "Awareness for ₹3K", "p": "The video awareness campaign reached 1.08 million people for about ₹3K, keeping retargeting full and prospecting cheap."},
                  ]}),
    L.split({"id": "billing", "pill": "How we work with you", "h2": ("Your account,", "your money, full visibility"),
             "body": ["100% of advertising spend is billed directly to your own Meta Ads account. Campaigns run inside your Meta Business Manager, Meta charges your payment method directly, and media spend is never routed, marked up or resold. Our fee is separate from media."],
             "bullets": ["Account ownership: always yours", "Media billing: direct to your Meta account", "Reporting: weekly and monthly, reconciled to revenue",
                         "Creative testing: always on", "Tracking: pixel and CAPI, audited", "First 60 days: stabilise, then scale"],
             "visual": figure("Ad spend billing", ["Confirmed"], (
                 '<ul class="grid list-none gap-3">' + "".join(
                     f'<li class="flex items-start gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-4"><span class="mt-0.5 grid h-6 w-6 shrink-0 place-items-center rounded-full bg-orange text-white">{svg("check", "h-3.5 w-3.5", 3)}</span>'
                     f'<span class="text-sm text-ink">{t}</span></li>'
                     for t in ["<strong class=\"font-semibold\">100% of ad spend</strong> billed to your own Meta Ads account",
                               "Campaigns run in <strong class=\"font-semibold\">your</strong> Business Manager, so you keep full ownership",
                               "Meta charges your card directly. Spend is never marked up or resold",
                               "Our fee is separate from media, every rupee of budget goes to Meta"])
                 + "</ul>"))}, flip=True),
    L.chips_section({"id": "related", "h2": ("More from", "this account"),
                     "body": "OurKnots also runs Google Ads alongside Meta. The services behind these results:",
                     "chips": [("OurKnots on Google Ads", "/case-studies/ourknots-google-ads/"), ("Meta Ads", "/services/meta-ads/"),
                               ("Shopify store development", "/services/shopify-store-development/"), ("Performance marketing", "/services/performance-marketing/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want a result", "like this?"),
                          "body": ["Tell me about your store and your ads. I will look at your account and show you where the next gains are, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No obligation"]}),
]

FAQ = [('What ROAS does OurKnots get from Meta Ads?', 'Meta reported a 5.13x ROAS in September 2026, up from 0.72x in February 2025.'), ('How much does the OurKnots store sell in a month?', '₹3.84 lakh of store sales from 152 orders in September 2026, its record month. The store has crossed ₹1 lakh of sales every month since January 2026.'), ('Why is blended ROAS different from Meta ROAS?', 'Meta and Google both take credit for some of the same orders, so their numbers overlap. The account is judged on Shopify: everything the store sold divided by everything spent on ads, which was 4.82x in September 2026.'), ('Are these numbers real?', 'Yes. Every month is backed by a Meta Ads Manager screenshot on this page, with campaign names and the ad account blurred.')]
L.add_faq(PAGE, url, ("OurKnots on Meta Ads,", "answered"), FAQ)
