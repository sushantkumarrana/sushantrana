# Case study: Yalla Renovation (Dubai) on Google Ads, 1 Oct 2024 - 30 Sep 2026.
# Numbers: Google Ads account (GST, AED). Totals, campaigns, devices, networks and keywords
# from yala-google-ads-data.json / report Sushant supplied (Codex, 2026-10-14); monthly rows
# from the Overview screenshots he shared (Google rounds cost/impressions/clicks).
# Rules from the brief: never call recorded conversions "qualified leads", no ROAS/revenue,
# keep the methodology footnote. When we took the account over is not known yet: do not claim it.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
CTA = "Book your free strategy call"
BAR, LINE = "#ff4d00", "#2f6fdb"

# month, cost (AED K), impressions (K), recorded conversions, clicks (K)
DATA = [
    ("Oct 2024", 15.4, 80.2, 146.00, 4.72), ("Nov 2024", 15.1, 95.1, 103.00, 4.64), ("Dec 2024", 13.0, 74.9, 61.00, 3.75),
    ("Jan 2025", 14.7, 103, 54.00, 4.46), ("Feb 2025", 16.7, 168, 70.00, 5.63), ("Mar 2025", 26.6, 110, 154.00, 6.42),
    ("Apr 2025", 29.8, 775, 294.00, 18.2), ("May 2025", 17.0, 317, 55.33, 6.71), ("Jun 2025", 34.5, 173, 107.11, 5.1),
    ("Jul 2025", 46.6, 354, 147.51, 7.92), ("Aug 2025", 48.8, 294, 165.39, 10.9), ("Sep 2025", 45.5, 369, 113.96, 8.05),
    ("Oct 2025", 40.8, 247, 72.00, 6.19), ("Nov 2025", 43.9, 159, 81.00, 5.88), ("Dec 2025", 36.9, 185, 55.50, 5.74),
    ("Jan 2026", 47.5, 300, 90.00, 6.58), ("Feb 2026", 40.5, 478, 77.00, 5.75), ("Mar 2026", 77.6, 3300, 171.00, 52.8),
    ("Apr 2026", 91.7, 1810, 326.06, 33.6), ("May 2026", 71.6, 634, 108.99, 12.5), ("Jun 2026", 70.5, 470, 78.95, 4.62),
    ("Jul 2026", 106, 1350, 80.00, 27.2), ("Aug 2026", 109, 257, 87.00, 3.36), ("Sep 2026", 106, 418, 88.00, 3.61),
]
MONTHS = [d[0] for d in DATA]
# the monthly screenshots must add up to the account totals for the period
assert abs(sum(d[3] for d in DATA) - 2786.8) < 0.01 and abs(sum(d[1] for d in DATA) - 1165.5) < 1

# screenshots on disk (img/*/case-studies/yalla-renovation/google-YYYY-MM.webp); Jun-Sep 2026 still to come
SHOTS = MONTHS[:20]
MNUM = {m: i + 1 for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
SLUG = {m: f"{m[4:]}-{MNUM[m[:3]]:02d}" for m in MONTHS}


def aed_k(v):
    return f"AED {v:,.1f}K".replace(".0K", "K")


def aed(v):
    return f"AED {v:,.0f}"


def count_k(v):
    return f"{v / 1000:.2f}M" if v >= 1000 else f"{v:,.1f}K".replace(".0K", "K")


chart = L.journey_chart("Yalla Renovation on Google Ads", ["Oct 2024 to Sep 2026"], MONTHS, [
    ("conv", "Conversions", {"bars": [d[3] for d in DATA], "bar_name": "Recorded conversions", "fmt": lambda v: f"{v:,.2f}".replace(".00", ""),
                             "aria": "Google Ads recorded conversions by month, Oct 2024 to Sep 2026",
                             "note": "Conversions as Google Ads records them: mostly form submissions, plus store visits and WhatsApp clicks. Hover or tap a month."}),
    ("cost", "Spend", {"bars": [d[1] for d in DATA], "bar_name": "Ad spend", "fmt": aed_k,
                       "note": "Monthly spend grew from about AED 15K to about AED 106K."}),
    ("clicks", "Clicks", {"bars": [d[4] for d in DATA], "bar_name": "Clicks", "fmt": count_k,
                          "note": "March and April 2026 brought the biggest jumps in clicks."}),
    ("impr", "Impressions", {"bars": [d[2] for d in DATA], "bar_name": "Impressions", "fmt": count_k,
                             "note": "12.5 million impressions in 24 months."}),
])

# ---------------------------------------------------- the period vs the 24 months before
ROWS = [("Impressions", "+1,298%"), ("Recorded conversions", "+244%"), ("Ad spend", "+321%"), ("Cost per conversion", "AED 342 to AED 418")]
versus = figure("Against the 24 months before", ["Google Ads compare"], (
    '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><table class="w-full border-collapse text-sm"><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="px-3 py-2.5 text-left font-semibold text-ink">{k}</th>'
              f'<td class="px-3 py-2.5 text-right font-bold text-ink">{v}</td></tr>' for k, v in ROWS)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">Reach and conversions grew much faster than they had before, and spend grew faster still. Each conversion cost about 22% more. This is a story about scale, and we show the cost of it.</p>'))

# ------------------------------------------------------------------ campaigns
# label, type, cost (AED), form submissions, recorded conversions, cost per conversion, clicks
CAMPS = [
    ("Home renovation", "Performance Max", 381857.16, 1537.49, 1721.49, 221.82, 119160),
    ("Home renovation", "Search", 204509.66, 287.5, 290.5, 704.00, 17345),
    ("Bathroom", "Search", 148259.85, 149.48, 149.48, 991.83, 7314),
    ("Kitchen", "Search", 68973.55, 116.53, 118.53, 581.91, 6258),
    ("Bathroom", "Performance Max", 47731.67, 89.97, 96.97, 492.25, 21586),
    ("Store visits", "Performance Max", 31509.46, 2.0, 303.0, 103.99, 61567),
]
TOTAL_COST, TOTAL_FORMS = 1165484.92, 2287.8
HERO = CAMPS[0]
assert round(HERO[3] / TOTAL_FORMS * 100, 1) == 67.2 and round(HERO[2] / TOTAL_COST * 100, 1) == 32.8


def camp_panel(c):
    name, kind, cost, forms, conv, cpa, clicks = c
    share_cost, share_forms = cost / TOTAL_COST * 100, forms / TOTAL_FORMS * 100
    bars = "".join(
        f'<div class="mt-3"><div class="flex justify-between text-xs font-semibold text-body"><span>{k}</span><span class="text-ink">{v:.1f}%</span></div>'
        f'<div class="mt-1.5 h-2.5 overflow-hidden rounded-full bg-ink/[0.06]"><div class="h-full rounded-full" style="width:{v:.1f}%;background:{col}"></div></div></div>'
        for k, v, col in [("Share of all spend", share_cost, BAR), ("Share of all form submissions", share_forms, LINE)])
    facts = "".join(
        f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5"><p class="font-[family-name:var(--font-display)] text-lg font-extrabold text-orange">{E(n)}</p>'
        f'<p class="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{E(l)}</p></div>'
        for n, l in [(f"{forms:,.2f}".replace(".00", ""), "Form submissions"), (f"{conv:,.2f}".replace(".00", ""), "Recorded conversions"),
                     (aed(cost), "Spend"), (f"AED {cpa:,.2f}", "Cost per conversion")])
    note = (' <span class="text-muted">Most of its conversions are store visits, not forms.</span>' if forms < conv / 2 else "")
    return (f'<p class="text-sm font-bold text-ink">{E(name)} · {E(kind)}</p><p class="mt-1 text-xs text-body">{clicks:,} clicks.{note}</p>'
            f'<div class="mt-4 grid grid-cols-2 gap-3">{facts}</div>{bars}')


campaigns = '<div data-tabs="true">' + figure("Campaigns, side by side", ["24 months"], (
    '<div class="flex gap-2 overflow-x-auto pb-2">' + "".join(
        f'<button type="button" data-tab="c{i}" aria-pressed="{"true" if i == 0 else "false"}" data-on="border-orange bg-orange text-white" '
        f'data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" class="shrink-0 rounded-full border px-3 py-1.5 text-[11px] font-bold transition '
        f'{"border-orange bg-orange text-white" if i == 0 else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{E(c[0])} · {"PMax" if c[1] == "Performance Max" else c[1]}</button>'
        for i, c in enumerate(CAMPS))
    + "</div>" + "".join(f'<div data-panel="c{i}"{L.HID if i else ""} class="mt-4">{camp_panel(c)}</div>' for i, c in enumerate(CAMPS)))) + "</div>"

# ------------------------------------------------------------- devices and networks
SPLITS = {
    "device": ("Devices", [("Mobile phones", 55.2, 73.5, 67.6), ("Computers", 43.6, 15.2, 31.7), ("Tablets", 1.2, 11.3, 0.7)],
               "Mobile brings most of the clicks and conversions. Computers bring 15% of clicks but 32% of conversions. Tablets bring 11% of clicks and almost no conversions, so they are next to check."),
    "network": ("Networks", [("Cross-network (Performance Max)", 43.3, 85.5, 77.3), ("Google Search", 56.7, 14.5, 22.7)],
                "Performance Max carries 77% of recorded conversions on 43% of spend. Part of that is store visits, so Search still does the heavy lifting on form leads from high intent searches."),
}


def split_rows(rows):
    return "".join(
        f'<div class="mt-4 first:mt-0"><p class="text-sm font-bold text-ink">{E(n)}</p>' + "".join(
            f'<div class="mt-1.5 flex items-center gap-2"><span class="w-24 shrink-0 text-[11px] font-semibold text-muted">{k}</span>'
            f'<span class="h-2.5 min-w-0 flex-1 overflow-hidden rounded-full bg-ink/[0.06]"><span class="block h-full rounded-full" style="width:{v}%;background:{col}"></span></span>'
            f'<span class="w-12 shrink-0 text-right text-xs font-bold text-ink">{v}%</span></div>'
            for k, v, col in [("Spend", cost, BAR), ("Clicks", clicks, "#9a9a9a"), ("Conversions", conv, LINE)]) + "</div>"
        for n, cost, clicks, conv in rows)


mix = '<div data-tabs="true">' + figure("Where the results came from", ["Share of total"], (
    '<div class="flex flex-wrap gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="rounded-full px-3 py-1.5 text-[11px] font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{v[0]}</button>'
        for i, (k, v) in enumerate(SPLITS.items()))
    + "</div>" + "".join(
        f'<div data-panel="{k}"{L.HID if i else ""} class="mt-5">{split_rows(v[1])}<p class="mt-4 text-xs text-muted">{E(v[2])}</p></div>'
        for i, (k, v) in enumerate(SPLITS.items())))) + "</div>"

# ------------------------------------------------------------------ keywords
KEYWORDS = [("home renovation", 53862.26, 121.83, 6.01), ("bathroom renovation ideas", 29678.63, 53.03, 6.10),
            ("home renovations contractor", 26985.87, 41.64, 5.96), ("house renovation", 39194.46, 18, 3.94), ('"renovation dubai"', 31398.71, 7, 5.11)]
keywords = figure("Keywords: what each form cost", ["Search"], (
    '<div class="overflow-x-auto"><table class="w-full border-collapse text-sm"><thead><tr class="border-b border-[var(--color-line)] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="py-2 pr-3 text-left font-bold">Keyword</th><th class="py-2 pr-3 text-right font-bold">Spend</th><th class="py-2 pr-3 text-right font-bold">Forms</th><th class="py-2 text-right font-bold">Per form</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="py-2.5 pr-3 text-left font-semibold text-ink">{E(k)}</th>'
              f'<td class="py-2.5 pr-3 text-right text-body">{aed(s)}</td><td class="py-2.5 pr-3 text-right text-body">{f:g}</td>'
              f'<td class="py-2.5 text-right font-bold {"text-orange" if s / f < 1000 else "text-ink"}">{aed(s / f)}</td></tr>' for k, s, f, _ in KEYWORDS)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">Similar click-through rates, very different costs per form. "Home renovation" brought 121.83 forms at about AED 442 each; "renovation dubai" brought 7 at about AED 4,486 each.</p>'))

# ------------------------------------------------------------------ milestones
MILESTONES = [
    ("Oct 2024", "The starting point", "146 recorded conversions on AED 15.4K of spend."),
    ("Apr 2025", "The first big month", "294 conversions and 18.2K clicks, on AED 29.8K."),
    ("Jul - Sep 2025", "Spend steps up", "Budgets moved to AED 45K-49K a month, with 114 to 165 conversions each month."),
    ("Mar 2026", "Reach jumps", "3.3M impressions and 52.8K clicks in a single month."),
    ("Apr 2026", "The record month", "326.06 recorded conversions on AED 91.7K, the most of any month."),
    ("Jun - Sep 2026", "Holding at scale", "AED 70K-109K a month for 79 to 88 conversions a month. The next job is bringing that cost back down."),
]
milestones = ('<section class="section" id="milestones" aria-labelledby="milestones-heading">'
              + L.centered_head({"id": "milestones", "pill": "Milestones", "h2": ("Twenty-four months,", "month by month"),
                                 "body": ["The good months and the expensive ones, as the account recorded them."]})
              + '<ol class="wrap mt-12 grid list-none gap-4 md:grid-cols-2">' + "".join(
                  f'<li data-reveal="true"{L.d(i, per=2)} class="card flex gap-4 p-6"><span class="grid h-12 w-12 shrink-0 place-items-center rounded-2xl bg-orange/10 font-[family-name:var(--font-display)] text-xs font-extrabold text-orange">{i + 1:02d}</span>'
                  f'<span><span class="block text-[10px] font-bold uppercase tracking-widest text-orange">{E(m)}</span><span class="mt-1 block text-lg font-extrabold text-ink">{E(t)}</span>'
                  f'<span class="mt-1.5 block text-sm text-body">{E(p)}</span></span></li>'
                  for i, (m, t, p) in enumerate(MILESTONES)) + "</ol></section>")

# ------------------------------------------------------------------ proof
ROW = {d[0]: d for d in DATA}


def shot(m):
    slug = SLUG[m]
    srcset = ", ".join(f"/img/{w}/case-studies/yalla-renovation/google-{slug}.webp {w}w" for w in (640, 1080, 1920))
    return (f'<a href="/img/1920/case-studies/yalla-renovation/google-{slug}.webp" target="_blank" rel="noopener" class="block overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            f'<img alt="Yalla Renovation Google Ads overview for {m}" loading="lazy" decoding="async" width="1920" height="961" '
            f'class="block h-auto w-full" sizes="(min-width: 1024px) 1100px, 92vw" srcSet="{srcset}" src="/img/1080/case-studies/yalla-renovation/google-{slug}.webp"/></a>')


def caption(m):
    d = ROW[m]
    return f"Spend {aed_k(d[1])} · {count_k(d[2])} impressions · {d[3]:g} conversions · {count_k(d[4])} clicks"


LAST = len(SHOTS) - 1
proof = ('<section class="section" id="proof" aria-labelledby="proof-heading">'
         + L.centered_head({"id": "proof", "pill": "Proof", "h2": ("Every month, straight from", "Google Ads"),
                            "body": ["The account overview for each month, as Google shows it. Pick a month, then click the screenshot to open it full size."]})
         + '<div class="wrap mt-10" data-tabs="true"><div data-reveal="true" class="flex gap-2 overflow-x-auto pb-2">' + "".join(
             f'<button type="button" data-tab="m{SLUG[m]}" aria-pressed="{"true" if i == LAST else "false"}" data-on="border-orange bg-orange text-white" '
             f'data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" class="shrink-0 rounded-full border px-4 py-2 text-xs font-semibold transition '
             f'{"border-orange bg-orange text-white" if i == LAST else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{m}</button>'
             for i, m in enumerate(SHOTS))
         + '</div><div data-reveal="true" style="--d:0.1s" class="mt-6">' + "".join(
             f'<div data-panel="m{SLUG[m]}"{L.HID if i != LAST else ""}>{shot(m)}<p class="mt-3 text-center text-sm text-body"><strong class="font-semibold text-ink">{m}.</strong> {E(caption(m))}</p></div>'
             for i, m in enumerate(SHOTS))
         + "</div></div></section>")

FOOTNOTE = ("Google Ads data, 1 Oct 2024–30 Sept 2026, Gulf Standard Time. Recorded conversions include multiple action types; "
            "form-submission totals are reported separately.")

PAGE = {
    "path": "/case-studies/yalla-renovation/",
    "slug": "case-study",
    "form_name": "case_study",
    "service": "Google Ads",
    "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "Yalla Renovation Google Ads case study",
    "thanks_what": "enquiry",
    "title": "Yalla Renovation Google Ads Case Study | Sushant Rana",
    "og_title": "Yalla Renovation on Google Ads: 2,287 tracked form leads",
    "og_alt": "Yalla Renovation Google Ads case study by Sushant Rana",
    "desc": "Yalla Renovation, Dubai, on Google Ads over 24 months: 12.5M impressions, 254K clicks and 2,287 tracked form submissions from Search and Performance Max.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Google Ads", "/case-studies/google-ads/"), ("Yalla Renovation", None)],
    "related": [],
    "hero": {
        "pill": "Case study · Google Ads",
        "h1": ("Yalla Renovation on Google Ads:", "2,287 tracked form submissions"),
        "intro_html": [
            'Yalla Renovation does home, villa, apartment, kitchen and bathroom renovation in Dubai. Over 24 months, Search and Performance Max brought <strong class="font-semibold text-ink">12.5M impressions, 254K clicks and 2,287 tracked form submissions</strong>.',
            "Every number here comes from the Google Ads account, including the parts that cost more than we would like. Hover the chart to follow it month by month.",
        ],
        "cta_href": "/contact/book-strategy-call/",
        "cta2": ("See the hero campaign", "#campaigns"),
        "stats": [("12.5M+", "Impressions"), ("254K+", "Clicks"), ("2,287", "Tracked form submissions"), ("+244%", "Recorded conversions vs the 24 months before")],
        "visual": chart,
    },
    "form": {
        "title": "Want results like this?",
        "sub": "Tell me about your business and I will look at your Google Ads for free.",
        "submit": "Request my free review",
        "steps": [
            {"label": "Business", "fields": [
                {"type": "radio", "name": "business", "label": "What do you sell?", "req": True, "options": ["Renovation or home services", "Other services", "Online store"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["More leads", "Lower cost per lead", "Better quality leads", "Scale spend", "Not sure yet"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you offer, where, what you spend, what is not working..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

url = SITE + "/case-studies/yalla-renovation"
PAGE["graph"] = [
    {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": url + "#article"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/img/1920/case-studies/yalla-renovation/google-2026-04.webp"}},
    {"@type": "Article", "@id": url + "#article", "headline": "Yalla Renovation on Google Ads: 2,287 tracked form submissions", "description": PAGE["desc"],
     "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"}, "datePublished": "2026-10-14", "inLanguage": "en",
     "about": {"@type": "Organization", "name": "Yalla Renovation", "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}}},
]

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads", "Dubai", "12.5M impressions", "254K clicks", "2,287 form submissions", "Performance Max", "Search"]),
    L.split({"id": "challenge", "pill": "The challenge", "h2": ("More renovation leads,", "without hiding the cost"),
             "body": ["Renovation leads are expensive, and volume the sales team cannot close is wasted money. Yalla Renovation needed steady enquiries across five services: homes, villas, apartments, kitchens and bathrooms.",
                      "Over these 24 months the account reached far more people and recorded far more conversions than in the 24 months before. Spend grew faster than conversions, so each one cost more. Both are on this page."],
             "bullets": ["Impressions up 1,298%", "Recorded conversions up 244%", "Cost per conversion up 22%, from AED 342 to AED 418"],
             "visual": versus}, dark=True),
    L.icon_cards({"id": "strategy", "pill": "The setup", "h2": ("How the account", "is built"),
                  "body": ["Search catches people already looking. Performance Max finds more of them. Each service gets its own campaign, so budgets follow what works."],
                  "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                      {"icon": "search", "h3": "Search by service", "p": "Separate Search campaigns for home, bathroom, kitchen, apartment and villa renovation, plus the brand name."},
                      {"icon": "zap", "h3": "Performance Max", "p": "Home, bathroom and kitchen Performance Max campaigns reach people across Google beyond the search results."},
                      {"icon": "pin", "h3": "Store visits", "p": "A Performance Max campaign for store visits, added in 2026 and measured apart from form leads."},
                      {"icon": "target", "h3": "Conversion tracking", "p": "Lead form submissions are tracked as their own conversion, apart from store visits and WhatsApp clicks."},
                  ]}),
    L.section_bg(L.split({"id": "campaigns", "anchor": "campaigns", "pill": "The hero campaign", "h2": ("One campaign,", "two thirds of the forms"),
                          "body": ["Home Renovation on Performance Max brought 1,537.49 form submissions and 1,721.49 recorded conversions at AED 221.82 each.",
                                   "That is 67.2% of all form submissions in the account, on 32.8% of the spend. Pick another campaign to compare."],
                          "bullets": ["1,537.49 form submissions", "AED 221.82 per recorded conversion", "67.2% of forms on 32.8% of spend"],
                          "visual": campaigns})),
    L.split({"id": "mix", "pill": "Devices and networks", "h2": ("Where the conversions", "actually came from"),
             "body": ["Spend, clicks and conversions do not line up neatly by device or network, and that is where the next savings are.",
                      "Switch between devices and networks to see each share."],
             "bullets": ["Mobile: 73.5% of clicks, 67.6% of conversions", "Computers: 15.2% of clicks, 31.7% of conversions", "Tablets: 11.3% of clicks, 0.7% of conversions"],
             "visual": mix}, flip=True),
    L.section_bg(L.split({"id": "search", "pill": "Search insights", "h2": ("What people searched,", "and what it cost"),
                          "body": ["The most shown Search ad, in the Home Renovation Search campaign, had 304,659 impressions, 15,425 clicks and a 5.06% click-through rate.",
                                   "Searches covered the brand name, kitchen, bathroom, apartment and villa renovation in Dubai, and renovation company and contractor terms. Some keywords bring forms cheaply; others are clicked just as often and bring very few."],
                          "bullets": ["5.06% CTR on the most shown ad", "20.79% CTR on brand searches", "Broad terms like \"renovation dubai\" cost the most per form"],
                          "visual": keywords})),
    milestones,
    L.section_bg(proof),
    '<section class="section" id="measurement" aria-label="How we count">' + L.cta_band({"pill": "How we count", "h3": "What the numbers mean",
                "p": "Recorded conversions (2,786.8) mix form submissions, store visits and WhatsApp clicks, so we lead with the 2,287 tracked form submissions. The account does not yet record which leads became jobs, so we do not claim revenue or ROAS. " + FOOTNOTE,
                "btn": CTA}).replace('href="#contact" class="btn btn-primary"', 'href="/contact/book-strategy-call/" data-no-popup="true" class="btn btn-primary"') + "</section>",
    L.chips_section({"id": "related", "h2": ("More", "case studies"),
                     "body": "More accounts we run, and the service behind this one:",
                     "chips": [("Google Ads case studies", "/case-studies/google-ads/"), ("OurKnots on Google Ads", "/case-studies/ourknots-google-ads/"),
                               ("Google Ads management", "/services/google-ads/"), ("Performance marketing", "/services/performance-marketing/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want a result", "like this?"),
                          "body": ["Tell me about your business and your Google Ads. I will look at your account and show you where the next gains are, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No obligation"]}),
]

FAQ = [('How many leads did Yalla Renovation get from Google Ads?', '2,287 tracked form submissions from 1 Oct 2024 to 30 Sep 2026. Google Ads recorded 2,786.8 conversions in total, which also include store visits and WhatsApp clicks.'), ('Which campaign worked best?', 'Home Renovation on Performance Max: 1,537.49 form submissions, 67.2% of all forms, on 32.8% of the spend, at AED 221.82 per recorded conversion.'), ('Did the cost per conversion go up?', 'Yes. Against the 24 months before, cost per recorded conversion rose about 22%, from AED 342 to AED 418, while recorded conversions grew 244%.'), ('Why does this case study not show ROAS?', 'The account does not yet record which leads became jobs, so we do not claim revenue or ROAS.')]
L.add_faq(PAGE, url, ("Yalla Renovation on Google Ads,", "answered"), FAQ)
