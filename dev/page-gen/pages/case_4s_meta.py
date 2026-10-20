# Case study: 4S Study Abroad (UAE) on Meta Ads, 14 Oct 2024 - 12 Oct 2026.
# Totals, year on year, campaigns and the creative test: the Meta case study report Sushant supplied
# (forest-study-abroad-meta-case-study.md, 2026-10-14). UAE campaigns only: the small India (Noida)
# test campaigns are left out of every number, as the report does.
# Monthly rows: the Ads Manager screenshots he shared (Oct 2024 - Sep 2026; Mar 2025 missing).
# Oct-Dec 2024 were sent inline only, so they are in the chart but not in the proof gallery yet.
# Benchmarks checked 2026-10-14: WordStream 2025 Education & Instruction leads CPL $28.22,
# SuperAds education CPL $21.31. Never claim enrolments, revenue or ROI: Meta has no such data.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
CTA = "Book your free strategy call"
BAR, LINE = "#ff4d00", "#2f6fdb"
USD = 0.27226  # AED is pegged

# month, UAE spend (AED), form leads, WhatsApp conversations, partial (part of the campaign list was off screen)
DATA = [
    ("Oct 2024", 3405.26, 445, 0, False), ("Nov 2024", 2877.35, 303, 0, False), ("Dec 2024", 3426.86, 337, 0, False),
    ("Jan 2025", 3308.91, 356, 0, False), ("Feb 2025", 4465.27, 335, 0, False), ("Mar 2025", None, None, None, False),
    ("Apr 2025", 740.42, 65, 0, False), ("May 2025", 3059.54, 236, 0, False), ("Jun 2025", 3094.91, 259, 0, False),
    ("Jul 2025", 3807.38, 301, 47, False), ("Aug 2025", 5240.85, 318, 174, False), ("Sep 2025", 3752.24, 195, 113, False),
    ("Oct 2025", 4628.08, 276, 113, False), ("Nov 2025", 2427.07, 95, 105, True), ("Dec 2025", 3103.99, 239, 192, False),
    ("Jan 2026", 3002.08, 195, 85, True), ("Feb 2026", 4760.37, 369, 0, False), ("Mar 2026", 1531.19, 176, 146, False),
    ("Apr 2026", 2326.72, 232, 215, False), ("May 2026", 2368.03, 231, 220, False), ("Jun 2026", 1780.80, 142, 153, False),
    ("Jul 2026", 1506.28, 129, 138, False), ("Aug 2026", 1527.43, 124, 214, False), ("Sep 2026", 1314.19, 89, 179, False),
]
MONTHS = [d[0] for d in DATA]
SHOTS = [d[0] for d in DATA if d[1] is not None and not d[0].endswith("2024")]  # 2024 screenshots not saved as files yet
MNUM = {m: i + 1 for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
SLUG = {m: f"{m[4:]}-{MNUM[m[:3]]:02d}" for m in MONTHS}

# report totals (UAE, 24 months)
SPEND, ENQ, CPE = 66496, 7514, 8.79
LEADS, CPL, WA, CPW = 5372, 10.41, 2142, 4.74
# AED 8.79 = spend on form and WhatsApp campaigns / direct enquiries (event and link-click spend left out)
assert LEADS + WA == ENQ and round((LEADS * CPL + WA * CPW) / ENQ, 2) == CPE


def aed(v, dp=0):
    return f"AED {v:,.{dp}f}"


def enq(d):
    return None if d[2] is None or d[4] else d[2] + d[3]


chart = L.journey_chart("4S Study Abroad on Meta", ["Oct 2024 to Sep 2026"], MONTHS, [
    ("enq", "Enquiries", {"bars": [d[2] for d in DATA], "bar_name": "Form leads", "line": [d[3] for d in DATA], "line_name": "WhatsApp conversations",
                          "fmt": lambda v: f"{v:,.0f}", "partial": [d[4] for d in DATA], "aria": "Monthly Meta form leads and WhatsApp conversations, Oct 2024 to Sep 2026",
                          "note": "Form leads and WhatsApp conversations as Meta reports them. No screenshot for March 2025. Hover or tap a month."}),
    ("cpe", "Cost per enquiry", {"bars": [round(d[1] / enq(d), 2) if enq(d) else None for d in DATA], "bar_name": "Cost per enquiry", "fmt": lambda v: f"AED {v:.2f}",
                                 "note": "Spend divided by form leads plus WhatsApp conversations. Lower is better; only months with a complete screenshot."}),
    ("spend", "Spend", {"bars": [d[1] for d in DATA], "bar_name": "Ad spend", "fmt": lambda v: f"AED {v:,.0f}",
                        "note": "About AED 3K a month, coming down in 2026."}),
])

AT_A_GLANCE = [("Ad spend", "AED 66,496"), ("Direct enquiries (form leads + WhatsApp)", "7,514"), ("Cost per direct enquiry", "AED 8.79"),
               ("Instant form leads", "5,372 at AED 10.41"), ("WhatsApp conversations", "2,142 at AED 4.74"), ("Event responses", "176 at AED 0.82"),
               ("Impressions", "3.78M"), ("People reached", "1,151,472"), ("Link clicks", "23,835")]
glance = figure("24 months at a glance", ["UAE campaigns"], (
    '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><table class="w-full border-collapse text-sm"><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="px-3 py-2.5 text-left font-semibold text-ink">{E(k)}</th>'
              f'<td class="px-3 py-2.5 text-right font-bold text-ink">{E(v)}</td></tr>' for k, v in AT_A_GLANCE)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">Meta Ads Manager, 14 Oct 2024 to 12 Oct 2026. Cost per direct enquiry uses the spend on form and WhatsApp campaigns. Form leads, WhatsApp conversations and event responses are counted separately.</p>'))

# ------------------------------------------------------------------ benchmarks (USD, cost per lead)
BENCH = [("WordStream, Education & Instruction (2025)", 28.22, "#9a9a9a"), ("SuperAds, education average", 21.31, "#9a9a9a"),
         ("4S Study Abroad, form leads", round(CPL * USD, 2), BAR)]
assert BENCH[2][1] == 2.83
bench = figure("Cost per lead vs published benchmarks", ["USD"], (
    "".join(f'<div class="mt-4 first:mt-0"><div class="flex justify-between gap-3 text-xs font-semibold text-body"><span>{E(n)}</span><span class="text-ink">${v:.2f}</span></div>'
            f'<div class="mt-1.5 h-3 overflow-hidden rounded-full bg-ink/[0.06]"><div class="h-full rounded-full" style="width:{v / 28.22 * 100:.1f}%;background:{c}"></div></div></div>'
            for n, v, c in BENCH)
    + '<p class="mt-4 text-xs text-muted">AED converted at the pegged 1 AED = 0.27226 USD. Benchmarks are broad datasets, not UAE-only, so read them as a yardstick. Sources: '
      '<a class="underline hover:text-orange" href="https://www.wordstream.com/blog/facebook-ads-benchmarks-2025" target="_blank" rel="noopener">WordStream</a>, '
      '<a class="underline hover:text-orange" href="https://www.superads.ai/facebook-ads-costs/cost-per-lead/education" target="_blank" rel="noopener">SuperAds</a>.</p>'))

# ------------------------------------------------------------------ year on year
YOY = [("Spend", "AED 37,548", "AED 29,877", "-20%"), ("Campaigns with delivery", "11", "16", "+45%"),
       ("Cost per form lead", "AED 11.27", "AED 9.26", "-17.8%"), ("Cost per WhatsApp conversation", "AED 7.27", "AED 4.18", "-42.5%")]
yoy = figure("Year 1 vs year 2", ["UAE"], (
    '<div class="overflow-x-auto"><table class="w-full border-collapse text-sm"><thead><tr class="border-b border-[var(--color-line)] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="py-2 pr-3 text-left font-bold"></th><th class="py-2 pr-3 text-right font-bold">Oct 24 - Oct 25</th><th class="py-2 pr-3 text-right font-bold text-orange">Oct 25 - Oct 26</th><th class="py-2 text-right font-bold">Change</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="py-2.5 pr-3 text-left font-semibold text-ink">{E(k)}</th>'
              f'<td class="py-2.5 pr-3 text-right text-body">{a}</td><td class="py-2.5 pr-3 text-right font-bold text-ink">{b}</td><td class="py-2.5 text-right font-bold text-orange">{c}</td></tr>'
              for k, a, b, c in YOY)
    + "</tbody></table></div>"))

# ------------------------------------------------------------------ campaigns (themes, not raw names)
CAMPS = [("Study in Germany", "Instant form", "1,831 leads", "AED 10.60", "AED 19,400"), ("All UAE locations", "Instant form", "1,082 leads", "AED 6.89", "AED 7,453"),
         ("WhatsApp, Mar 2026 (ABO)", "WhatsApp", "1,306 conversations", "AED 3.65", "AED 4,764"), ("Germany, WhatsApp", "WhatsApp", "836 conversations", "AED 6.43", "AED 5,380"),
         ("Education expo, image", "Instant form", "541 leads", "AED 10.72", "AED 5,798"), ("Schengen, parents", "Instant form", "390 leads", "AED 12.50", "AED 4,874"),
         ("Study in Germany, tailored", "Instant form", "311 leads", "AED 15.40", "AED 4,789"), ("Instant form, Mar 2026 (ABO)", "Instant form", "288 leads", "AED 8.25", "AED 2,376")]
campaigns = figure("The campaigns that carried it", ["24 months"], (
    '<div class="overflow-x-auto"><table class="w-full min-w-[520px] border-collapse text-sm"><thead><tr class="border-b border-[var(--color-line)] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="py-2 pr-3 text-left font-bold">Campaign</th><th class="py-2 pr-3 text-left font-bold">Type</th><th class="py-2 pr-3 text-right font-bold">Results</th>'
    '<th class="py-2 pr-3 text-right font-bold">Per result</th><th class="py-2 text-right font-bold">Spend</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="py-2.5 pr-3 text-left font-semibold text-ink">{E(n)}</th>'
              f'<td class="py-2.5 pr-3 text-body">{t}</td><td class="py-2.5 pr-3 text-right text-body">{r}</td><td class="py-2.5 pr-3 text-right font-bold text-orange">{c}</td>'
              f'<td class="py-2.5 text-right text-body">{s}</td></tr>' for n, t, r, c, s in CAMPS)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">The two biggest form campaigns brought 2,913 leads, 54% of all form leads in the account.</p>'))

# ------------------------------------------------------------------ creative test
TEST = [("Video ads", "AED 11.26", 244), ("Video ads, second set", "AED 10.63", 184), ("Image ads", "AED 25.38", 61)]
creative = figure("Same offer, three creative sets", ["Education Expo 2026"], (
    '<ul class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] {"bg-white" if i < 2 else "bg-[#fff7f3]"} p-4">'
        f'<span class="min-w-0"><span class="block text-sm font-bold text-ink">{E(n)}</span><span class="block text-xs text-muted">{l} leads</span></span>'
        f'<span class="text-right"><span class="block font-[family-name:var(--font-display)] text-xl font-extrabold {"text-ink" if i < 2 else "text-orange"}">{c}</span>'
        f'<span class="block text-[10px] font-semibold uppercase tracking-wider text-muted">Per lead</span></span></li>' for i, (n, c, l) in enumerate(TEST))
    + '</ul><p class="mt-3 text-xs text-muted">Image creative cost 2.3 times more per lead, so the budget moved to video and stayed there.</p>'))

# ------------------------------------------------------------------ milestones (from the monthly screenshots)
MILESTONES = [
    ("Oct 2024", "A strong start", "445 form leads in a month from the Study in Germany and education expo campaigns, at about AED 7.65 per lead."),
    ("Jul 2025", "WhatsApp opens up", "The first WhatsApp conversation campaign for Germany: 47 conversations in its first month, 192 by December."),
    ("Feb 2026", "The creative test", "369 form leads in the Education Expo 2026 push, with video beating image at less than half the cost per lead."),
    ("Mar 2026", "New ABO campaigns", "Separate WhatsApp and instant form campaigns on proven audiences, at AED 2.67 and AED 6.44 per result in their first month."),
    ("Apr - May 2026", "About 15 a day", "447 and 451 direct enquiries a month, about 15 a day, on about AED 2.3K a month."),
    ("Sep 2026", "Cheapest yet", "268 direct enquiries at about AED 4.90 each, on AED 1.3K of UAE spend."),
]
milestones = ('<section class="section" id="milestones" aria-labelledby="milestones-heading">'
              + L.centered_head({"id": "milestones", "pill": "Milestones", "h2": ("The months that", "shaped the account"),
                                 "body": ["The months that changed the account, straight from the monthly screenshots."]})
              + '<ol class="wrap mt-12 grid list-none gap-4 md:grid-cols-2">' + "".join(
                  f'<li data-reveal="true"{L.d(i, per=2)} class="card flex gap-4 p-6"><span class="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-orange/10 font-[family-name:var(--font-display)] text-xs font-extrabold text-orange">{i + 1:02d}</span>'
                  f'<span><span class="block text-[10px] font-bold uppercase tracking-widest text-orange">{E(m)}</span><span class="mt-1 block text-lg font-extrabold text-ink">{E(t)}</span>'
                  f'<span class="mt-1.5 block text-sm text-body">{E(p)}</span></span></li>'
                  for i, (m, t, p) in enumerate(MILESTONES)) + "</ol></section>")

# ------------------------------------------------------------------ proof
ROW = {d[0]: d for d in DATA}


def shot(m):
    slug = SLUG[m]
    srcset = ", ".join(f"/img/{w}/case-studies/4s-study-abroad/meta-{slug}.webp {w}w" for w in (640, 1080, 1920))
    return (f'<a href="/img/1920/case-studies/4s-study-abroad/meta-{slug}.webp" target="_blank" rel="noopener" class="block overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            f'<img alt="4S Study Abroad Meta Ads Manager campaigns view for {m}, campaign names blurred" loading="lazy" decoding="async" width="1920" height="1015" '
            f'class="block h-auto w-full" sizes="(min-width: 1024px) 1100px, 92vw" srcSet="{srcset}" src="/img/1080/case-studies/4s-study-abroad/meta-{slug}.webp"/></a>')


def caption(m):
    d = ROW[m]
    wa = f" · {d[3]} WhatsApp conversations" if d[3] else ""
    part = " · part of the campaign list is off screen, so results shown are a floor" if d[4] else ""
    return f"UAE spend {aed(d[1], 2)} · {d[2]} form leads{wa}{part}"


LAST = len(SHOTS) - 1
proof = ('<section class="section" id="proof" aria-labelledby="proof-heading">'
         + L.centered_head({"id": "proof", "pill": "Proof", "h2": ("Every month, straight from", "Meta Ads Manager"),
                            "body": ["The campaigns view for each month. Campaign names and the ad account are blurred; every number is as Meta reports it. Totals in the screenshots also include a few small test campaigns outside the UAE, which this page leaves out. Pick a month, then click the screenshot to open it full size."]})
         + '<div class="wrap mt-10" data-tabs="true"><div data-reveal="true" class="flex gap-2 overflow-x-auto pb-2">' + "".join(
             f'<button type="button" data-tab="m{SLUG[m]}" aria-pressed="{"true" if i == LAST else "false"}" data-on="border-orange bg-orange text-white" '
             f'data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" class="shrink-0 rounded-full border px-4 py-2 text-xs font-semibold transition '
             f'{"border-orange bg-orange text-white" if i == LAST else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{m}</button>'
             for i, m in enumerate(SHOTS))
         + '</div><div data-reveal="true" style="--d:0.1s" class="mt-6">' + "".join(
             f'<div data-panel="m{SLUG[m]}"{L.HID if i != LAST else ""}>{shot(m)}<p class="mt-3 text-center text-sm text-body"><strong class="font-semibold text-ink">{m}.</strong> {E(caption(m))}</p></div>'
             for i, m in enumerate(SHOTS))
         + "</div></div></section>")

FAQ = [
    ("How much does a study-abroad lead cost on Meta Ads in the UAE?",
     "For 4S Study Abroad, instant form leads averaged AED 10.41 (about USD 2.83) over 24 months. Published education benchmarks are USD 21.31 (SuperAds) and USD 28.22 (WordStream, 2025)."),
    ("Do WhatsApp campaigns work better than lead forms for education?",
     "In this account WhatsApp conversations cost AED 4.74 against AED 10.41 for a form lead, about half. Counsellors also get a warmer start, because the student has already written to them."),
    ("How long before Meta Ads give steady enquiry volume?",
     "Here the second year was cheaper than the first: cost per form lead fell 17.8% and cost per WhatsApp conversation 42.5%, on 20% less spend."),
]

PAGE = {
    "path": "/case-studies/4s-study-abroad/",
    "slug": "case-study",
    "form_name": "case_study",
    "service": "Meta Ads",
    "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "4S Study Abroad Meta Ads case study",
    "thanks_what": "enquiry",
    "title": "4S Study Abroad Meta Ads Case Study | Sushant Rana",
    "og_title": "4S Study Abroad: 7,514 student enquiries at AED 8.79",
    "og_alt": "4S Study Abroad Meta Ads case study by Sushant Rana",
    "desc": "4S Study Abroad on Meta Ads: 7,514 student enquiries at AED 8.79 each over 24 months in Dubai, UAE, from Germany-focused lead forms and WhatsApp.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Meta Ads", "/case-studies/meta-ads/"), ("4S Study Abroad", None)],
    "related": [],
    "faq": {"pill": "Common questions", "h2": ("Meta Ads for education,", "answered"), "body": [], "items": FAQ},
    "hero": {
        "pill": "Case study · Meta Ads · Education",
        "h1": ("4S Study Abroad on Meta:", "7,514 student enquiries at AED 8.79"),
        "intro_html": [
            '<a class="font-semibold text-orange" href="https://www.4sstudyabroad.com/" target="_blank" rel="noopener">4S Study Abroad</a> is a study-abroad and student visa consultancy in Dubai, UAE. Over 24 months, AED 66.5K of Meta spend brought <strong class="font-semibold text-ink">5,372 instant form leads and 2,142 WhatsApp conversations</strong>.',
            "Every number comes from Meta Ads Manager, and the campaigns are still running. Hover the chart to follow it month by month.",
        ],
        "cta_href": "/contact/book-strategy-call/",
        "cta2": ("See what worked", "#approach"),
        "stats": [("7,514", "Student enquiries"), ("AED 8.79", "Per enquiry"), ("AED 4.74", "Per WhatsApp chat"), ("-42.5%", "WhatsApp cost, year on year")],
        "visual": chart,
    },
    "form": {
        "title": "Want this for your education brand?",
        "sub": "Tell me about your business and I will look at your Meta Ads for free.",
        "submit": "Request my free review",
        "steps": [
            {"label": "Business", "fields": [
                {"type": "radio", "name": "business", "label": "What do you offer?", "req": True, "options": ["Study abroad or visas", "Courses or training", "Something else"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["More student enquiries", "Lower cost per lead", "Better quality leads", "Fill an event or intake", "Not sure yet"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Destinations, markets, what you spend, what is not working..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

url = SITE + "/case-studies/4s-study-abroad"
PAGE["graph"] = [
    {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": url + "#article"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/img/1920/case-studies/4s-study-abroad/meta-2026-08.webp"}},
    {"@type": "Article", "@id": url + "#article", "headline": "4S Study Abroad on Meta: 7,514 student enquiries at AED 8.79", "description": PAGE["desc"],
     "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"}, "datePublished": "2026-10-14", "inLanguage": "en",
     "about": {"@type": "Organization", "name": "4S Study Abroad", "url": "https://www.4sstudyabroad.com/",
               "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}}},
    {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"}, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
]

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Meta Ads", "Dubai, UAE", "7,514 enquiries", "AED 8.79 each", "Study in Germany", "WhatsApp", "Video over image", "Still running"]),
    L.split({"id": "challenge", "pill": "The challenge", "h2": ("Steady student enquiries,", "at a cost that works"),
             "body": ["Study abroad is a crowded market in Dubai and across the UAE. Generic \"study abroad\" ads are expensive and pull in people who are not ready to apply.",
                      "4S Study Abroad needed enquiries it could plan around: steady volume for every intake and education expo, at a cost per enquiry a consultancy's margin can carry."],
             "bullets": ["Predictable volume for intakes and expos", "Students and parents, reached separately", "A cost per enquiry the business can live with"],
             "visual": glance}, dark=True),
    L.section_bg(L.icon_cards({"id": "approach", "anchor": "approach", "pill": "What worked", "h2": ("Four decisions behind", "the low cost per enquiry"),
                               "body": ["Each one backed by a number from the account."],
                               "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                                   {"icon": "target", "h3": "Germany first", "p": "Germany and Schengen intent instead of generic study abroad: AED 10.60 per lead at AED 19.4K of spend in the biggest campaign."},
                                   {"icon": "chat", "h3": "Two funnels", "p": "Instant forms and WhatsApp side by side. WhatsApp conversations came in at AED 4.74, about half the cost of a form lead."},
                                   {"icon": "play", "h3": "Creative tested", "p": "Same offer, video against image: AED 11.26 against AED 25.38 per lead. Video won and kept the budget."},
                                   {"icon": "calendar", "h3": "Events as demand", "p": "Expo RSVP campaigns at AED 0.82 per response on tiny budgets, filling education fairs without touching the lead budget."},
                               ]})),
    L.split({"id": "benchmark", "pill": "How cheap is cheap", "h2": ("About 87% below", "education benchmarks"),
             "body": ["Form leads averaged AED 10.41, about USD 2.83. Published Meta benchmarks for education are USD 21.31 (SuperAds) and USD 28.22 (WordStream, 2025).",
                      "All 13 UAE lead form campaigns came in under AED 25.38 a lead; 11 of them under AED 16."],
             "bullets": ["~87% below the SuperAds education average", "~90% below the WordStream education benchmark", "Even the most expensive campaign stayed 68% below the SuperAds average"],
             "visual": bench}),
    L.section_bg(L.split({"id": "yoy", "pill": "Year on year", "h2": ("Spend went down 20%.", "Unit costs went down with it."),
                          "body": ["The second year spent less and got more for each dirham: more WhatsApp campaigns, ABO structures that protected the proven audiences, and video instead of image creative."],
                          "bullets": ["Cost per form lead: AED 11.27 to AED 9.26", "Cost per WhatsApp conversation: AED 7.27 to AED 4.18", "Five more campaigns with delivery"],
                          "visual": yoy}, flip=True)),
    L.split({"id": "campaigns", "pill": "The campaigns", "h2": ("Eight campaigns", "carried the account"),
             "body": ["Germany and Schengen campaigns did the heavy lifting, with a separate campaign for parents, who often make the decision."],
             "bullets": ["1,831 leads from Study in Germany", "1,306 WhatsApp conversations at AED 3.65", "Parents targeted on their own"],
             "visual": campaigns}),
    L.section_bg(L.split({"id": "creative", "pill": "Creative test", "h2": ("Video beat image,", "2.3 times over"),
                          "body": ["In the Education Expo 2026 push the same offer ran as two video sets and one image set. The numbers settled it."],
                          "bullets": ["Video: AED 11.26 and AED 10.63 per lead", "Image: AED 25.38 per lead", "428 of 489 leads came from video"],
                          "visual": creative}, flip=True)),
    milestones,
    L.section_bg(proof),
    L.icon_cards({"id": "next", "pill": "What comes next", "h2": ("Where the account", "goes from here"),
                  "body": ["Meta does not know who enrolled. These are the next steps we recommend."],
                  "cards": [
                      {"icon": "repeat", "h3": "Close the loop", "p": "Feed CRM outcomes back, so campaigns are judged on applications and enrolments, not just enquiries."},
                      {"icon": "users", "h3": "Lookalikes of enrolled students", "p": "Build audiences from students who actually enrolled, not from everyone who filled a form."},
                      {"icon": "pin", "h3": "Beyond Germany", "p": "Take what worked for Germany and Schengen to the next destinations."},
                  ]}),
    L.faq(PAGE["faq"]),
    L.chips_section({"id": "related", "h2": ("More", "case studies"),
                     "body": "More accounts we run, and the services behind this one:",
                     "chips": [("Meta Ads case studies", "/case-studies/meta-ads/"), ("OurKnots on Meta", "/case-studies/ourknots/"),
                               ("Meta Ads management", "/services/meta-ads/"), ("Education marketing", "/industries/education/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want this for your", "education brand?"),
                          "body": ["Tell me about your business and your Meta Ads. I will look at your account and show you where the next gains are, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No commitment"]}),
]
