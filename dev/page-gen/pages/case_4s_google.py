# Case study: 4S Study Abroad (Dubai, UAE) on Google Ads, 1 Apr 2020 - 31 Dec 2024 (19 quarters, INR).
# Numbers: 4s-study-abroad-google-ads-data.json + the case study report Sushant supplied (2026-10-14),
# and his overview screenshot for the same range. Rules: say "enquiries", never revenue or ROAS
# (conversion value was only partly set up). The report's lead-form count (4,883) disagrees with
# the screenshot (7.74k "Submit lead forms"), so it is not used until Sushant confirms which is right.
# Month-by-month screenshots are still to come from Sushant.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
SITE = L.SITE
CTA = "Book your free strategy call"
BAR, LINE = "#ff4d00", "#2f6fdb"

# quarter, cost, impressions, clicks, enquiries (conversions), CTR %, avg CPC, conv rate %, cost per enquiry
Q = [
    ("Q2 2020", 19854.47, 5062, 359, 67.5, 7.09, 55.3, 18.8, 294.14),
    ("Q3 2020", 147524.41, 26580, 2677, 675.0, 10.07, 55.11, 25.21, 218.55),
    ("Q4 2020", 155687.82, 69337, 2947, 976.5, 4.25, 52.83, 33.14, 159.43),
    ("Q1 2021", 234358.79, 50140, 3841, 669.0, 7.66, 61.02, 17.42, 350.31),
    ("Q2 2021", 162651.73, 42090, 3833, 558.0, 9.11, 42.43, 14.56, 291.49),
    ("Q3 2021", 258443.68, 83703, 6472, 1070.0, 7.73, 39.93, 16.53, 241.54),
    ("Q4 2021", 185625.48, 71895, 4800, 705.0, 6.68, 38.67, 14.69, 263.3),
    ("Q1 2022", 223036.43, 105717, 5358, 671.0, 5.07, 41.63, 12.52, 332.39),
    ("Q2 2022", 113547.51, 49484, 2436, 333.0, 4.92, 46.61, 13.67, 340.98),
    ("Q3 2022", 199829.46, 87135, 4191, 1266.0, 4.81, 47.68, 30.21, 157.84),
    ("Q4 2022", 57630.18, 22193, 939, 179.0, 4.23, 61.37, 19.06, 321.96),
    ("Q1 2023", 195364.18, 158097, 3267, 473.0, 2.07, 59.8, 14.48, 413.03),
    ("Q2 2023", 81873.53, 46147, 1522, 153.0, 3.3, 53.79, 10.05, 535.12),
    ("Q3 2023", 122909.4, 46511, 2069, 202.0, 4.45, 59.41, 9.76, 608.46),
    ("Q4 2023", 39377.06, 12519, 611, 59.0, 4.88, 64.45, 9.66, 667.41),
    ("Q1 2024", 46831.33, 13758, 747, 82.0, 5.43, 62.69, 10.98, 571.11),
    ("Q2 2024", 59014.85, 18198, 1153, 197.0, 6.34, 51.18, 17.09, 299.57),
    ("Q3 2024", 90901.85, 31331, 1929, 285.0, 6.16, 47.12, 14.77, 318.95),
    ("Q4 2024", 64227.25, 20528, 1370, 238.0, 6.67, 46.88, 17.37, 269.86),
]
# account totals (the quarterly split misses 0.13% of spend: two campaigns share a name)
SPEND, IMPR, CLICKS, ENQ, CTR, CPC, CR, CPE = 2461996.34, 962447, 50571, 8859, 5.25, 48.68, 16.47, 277.91
assert sum(q[4] for q in Q) == ENQ and round(SPEND / ENQ, 2) == CPE


def inr(v, dp=0):
    """Indian digit grouping: 2461996 -> 24,61,996."""
    whole, _, frac = f"{v:.{dp}f}".partition(".")
    head, tail = whole[:-3], whole[-3:]
    while len(head) > 2:
        tail, head = head[-2:] + "," + tail, head[:-2]
    return "₹" + (head + "," if head else "") + tail + ("." + frac if frac else "")


assert inr(2461996.34) == "₹24,61,996" and inr(277.91, 2) == "₹277.91"

chart = L.journey_chart("4S Study Abroad on Google Ads", ["Q2 2020 to Q4 2024"], [q[0] for q in Q], [
    ("enq", "Enquiries", {"bars": [q[4] for q in Q], "bar_name": "Enquiries", "fmt": lambda v: f"{v:,.0f}" if v == int(v) else f"{v:,.1f}",
                          "aria": "4S Study Abroad Google Ads enquiries by quarter, Q2 2020 to Q4 2024",
                          "note": "Enquiries as Google Ads records them, by quarter. Hover or tap a quarter."}),
    ("cpe", "Cost per enquiry", {"bars": [q[8] for q in Q], "bar_name": "Cost per enquiry", "fmt": lambda v: inr(v),
                                 "note": "Lower is better: ₹159 at the best, ₹667 at the worst, ₹270 by the end of 2024."}),
    ("spend", "Spend", {"bars": [q[1] for q in Q], "bar_name": "Ad spend", "fmt": lambda v: f"₹{v / 100000:.2f}L",
                        "note": "Spend and cost per enquiry move separately: the best results came from structure, not budget."}),
])

# ------------------------------------------------------------------ the challenge
challenge_card = figure("Where the ceiling was", ["Search impression share"], (
    '<div class="grid grid-cols-3 gap-3">' + "".join(
        f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5"><p class="font-[family-name:var(--font-display)] text-xl font-extrabold {c}">{n}</p>'
        f'<p class="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{l}</p></div>'
        for n, l, c in [("12.13%", "Share won", "text-ink"), ("72.76%", "Lost to Ad Rank", "text-orange"), ("15.12%", "Lost to budget", "text-ink")])
    + '</div><p class="mt-4 text-sm text-body">The ceiling on this account was never money. Three quarters of the available searches were lost to ad rank, and only 15% to budget.</p>'))

# ------------------------------------------------------------------ destinations
DEST = [("Canada", 9, 910695.67, 36.99, 18659, 8.23, 3408.87, 267.15), ("Germany", 5, 656653.72, 26.67, 13926, 8.12, 2806.06, 234.01),
        ("United Kingdom", 9, 562356.21, 22.84, 11223, 3.82, 1886.25, 298.13), ("Australia", 8, 128200.16, 5.21, 2368, 3.69, 384.33, 333.57),
        ("Europe, incl. medical", 2, 52625.39, 2.14, 1058, 7.41, 154.0, 341.72), ("Malaysia", 1, 2987.18, 0.12, 84, 10.8, 6.0, 497.86),
        ("Generic and university-specific", 10, 148477.99, 6.03, 3253, 1.7, 213.5, 695.45)]
dest = figure("Spend share and cost per enquiry, by destination", ["19 quarters"], (
    "".join(f'<div class="mt-3 first:mt-0"><div class="flex justify-between gap-3 text-xs font-semibold text-body"><span>{E(n)}</span>'
            f'<span class="text-ink">{share:.2f}% of spend · <span class="{"text-orange" if cpe < CPE else ""}">{inr(cpe)} per enquiry</span></span></div>'
            f'<div class="mt-1.5 h-2.5 overflow-hidden rounded-full bg-ink/[0.06]"><div class="h-full rounded-full" style="width:{share / 36.99 * 100:.1f}%;background:{BAR if cpe < CPE else "#9a9a9a"}"></div></div></div>'
            for n, _, _, share, _, _, _, cpe in DEST)
    + '<details class="mt-5 text-xs text-body"><summary class="cursor-pointer font-semibold text-ink">View as a table</summary><div class="overflow-x-auto">'
      '<table class="mt-2 w-full min-w-[520px]"><thead><tr class="text-left text-muted"><th class="py-1.5 pr-3 font-semibold">Destination</th>'
      '<th class="py-1.5 pr-3 text-right font-semibold">Campaigns</th><th class="py-1.5 pr-3 text-right font-semibold">Spend</th><th class="py-1.5 pr-3 text-right font-semibold">CTR</th>'
      '<th class="py-1.5 pr-3 text-right font-semibold">Enquiries</th><th class="py-1.5 text-right font-semibold">Per enquiry</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><td class="py-1.5 pr-3">{E(n)}</td><td class="py-1.5 pr-3 text-right">{c}</td>'
              f'<td class="py-1.5 pr-3 text-right">{inr(s)}</td><td class="py-1.5 pr-3 text-right">{ctr:.2f}%</td><td class="py-1.5 pr-3 text-right">{e:,.0f}</td>'
              f'<td class="py-1.5 text-right">{inr(cpe, 2)}</td></tr>' for n, c, s, _, _, ctr, e, cpe in DEST)
    + '</tbody></table></div><p class="mt-2 text-muted">Destinations are grouped from campaign names, so read them as indicative.</p></details>'))

# ------------------------------------------------------------------ campaign types and devices
SPLITS = {
    "type": ("Campaign types", [("Search (40 campaigns)", 98.66, 98.70, inr(277.81, 2)), ("Smart (1)", 0.70, 1.18, inr(165.93, 2)),
                                ("Performance Max (1)", 0.54, 0.12, inr(1199.39, 2)), ("Display (2)", 0.10, 0.0, "no enquiries")],
             "Search did the work. The one Smart campaign brought the cheapest enquiries in the account, 40% below average, on 0.7% of the budget. Performance Max and Display were tests that did not convert."),
    "device": ("Devices", [("Mobile phones", 78.06, 78.83, inr(275.19, 2)), ("Computers", 21.09, 20.39, inr(287.46, 2)), ("Tablets", 0.85, 0.78, inr(303.07, 2))],
               "Mobile took 78% of spend and returned 78.8% of enquiries, at a cost per enquiry 4.3% below computers."),
}


def split_rows(rows):
    return "".join(
        f'<div class="mt-4 first:mt-0"><p class="flex justify-between gap-3 text-sm font-bold text-ink"><span>{E(n)}</span><span class="text-xs font-semibold text-body">{E(cpe)}{" each" if cpe.startswith("₹") else ""}</span></p>' + "".join(
            f'<div class="mt-1.5 flex items-center gap-2"><span class="w-24 shrink-0 text-[11px] font-semibold text-muted">{k}</span>'
            f'<span class="h-2.5 min-w-0 flex-1 overflow-hidden rounded-full bg-ink/[0.06]"><span class="block h-full rounded-full" style="width:{v}%;background:{col}"></span></span>'
            f'<span class="w-12 shrink-0 text-right text-xs font-bold text-ink">{v:.2f}%</span></div>'
            for k, v, col in [("Spend", sp, BAR), ("Enquiries", en, LINE)]) + "</div>"
        for n, sp, en, cpe in rows)


mix = '<div data-tabs="true">' + figure("Where the enquiries came from", ["Share of total"], (
    '<div class="flex flex-wrap gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="rounded-full px-3 py-1.5 text-[11px] font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{v[0]}</button>'
        for i, (k, v) in enumerate(SPLITS.items()))
    + "</div>" + "".join(
        f'<div data-panel="{k}"{L.HID if i else ""} class="mt-5">{split_rows(v[1])}<p class="mt-4 text-xs text-muted">{E(v[2])}</p></div>'
        for i, (k, v) in enumerate(SPLITS.items())))) + "</div>"

# ------------------------------------------------------------------ the five phases
# year, label, title, spend, enquiries, cost per enquiry, conv rate, paragraphs, warn
PHASES = [
    ("2020", "Phase 1 · Q2 - Q4 2020", "Restart and proof of concept", 323066.7, 1719, 187.94, 28.73,
     ["The account restarted in April 2020, when borders were shut and intakes were being deferred. Spend was raised step by step, from ₹19,854 in Q2 to ₹1,55,688 in Q4, and each step had to keep cost per enquiry in check.",
      "It did better than that: cost per enquiry fell 45.8%, from ₹294.14 to ₹159.43, and conversion rate climbed from 18.80% to 33.14%, the highest of the whole period. Q3 2020 had a 10.07% CTR, also the best on record."], False),
    ("2021", "Phase 2 · 2021", "Scale-up", 841079.68, 3002, 280.17, 15.85,
     ["The biggest investment year: ₹8.41 lakh, and clicks more than tripled to 18,946. Q3 2021 is still the largest quarter by spend and clicks.",
      "Average CPC fell from ₹61.02 in Q1 to ₹38.67 in Q4, a 36.6% cut, while CTR stayed between 6.7% and 9.1%. Broader demand did dilute intent: conversion rate settled at 14.5% to 17.4% and cost per enquiry rose to ₹280 for the year."], False),
    ("2022", "Phase 3 · 2022", "The efficiency peak", 594043.58, 2449, 242.57, 18.95,
     ["Spend was cut 29% against 2021, yet cost per enquiry improved 13.4%. Budget moved out of the weakest destination and time-of-day campaigns and into Canada and Germany.",
      "Q3 2022 is the best quarter of the whole period: 1,266 enquiries at ₹157.84 each and a 30.21% conversion rate, on 22.7% less spend than Q3 2021 for 18.3% more enquiries."], False),
    ("2023", "Phase 4 · 2023", "The reach experiment, and what it cost", 439524.17, 887, 495.52, 11.88,
     ["Q1 2023 pushed for reach: 1,58,097 impressions, the most of any quarter, on about the same spend as Q1 2022. CTR fell to 2.07%, clicks fell 39%, and cost per enquiry rose to ₹413.",
      "It got worse through the year, to ₹667.41 per enquiry and a 9.66% conversion rate in Q4, the weakest quarter on record. Broad match and audience expansion were bought before the quality signals to control them. Spending into a relevance problem made it bigger."], True),
    ("2024", "Phase 5 · 2024", "Rebuild and recovery", 260975.28, 802, 325.41, 15.43,
     ["Spend was cut to its lowest full year, the reach experiment was undone, and budget went back into proven Search campaigns for Canada, Germany and the UK.",
      "Every quality number recovered quarter by quarter: cost per enquiry fell 52.7% from ₹571.11 in Q1 to ₹269.86 in Q4, CPC fell 25.2% and conversion rate rose from 10.98% to 17.37%."], False),
]
phase_btns = "".join(
    f'<button type="button" data-tab="p{y}" aria-pressed="{"true" if i == 0 else "false"}" data-on="border-orange bg-orange text-white" '
    f'data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" class="shrink-0 rounded-full border px-4 py-2 text-xs font-semibold transition '
    f'{"border-orange bg-orange text-white" if i == 0 else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{y}</button>'
    for i, (y, *_rest) in enumerate(PHASES))
phase_panels = "".join(
    f'<div data-panel="p{y}"{L.HID if i else ""}><article class="card p-6 md:p-8">'
    + (f'<span class="inline-block rounded-full bg-orange/10 px-3 py-1 text-[10px] font-bold uppercase tracking-widest text-orange">What went wrong</span>' if warn else "")
    + f'<p class="{"mt-3 " if warn else ""}text-[10px] font-bold uppercase tracking-widest text-orange">{E(lab)}</p><h3 class="mt-1 text-2xl font-extrabold text-ink">{E(t)}</h3>'
    + "".join(f'<p class="mt-3 text-body">{E(p)}</p>' for p in ps)
    + '<div class="mt-5 grid grid-cols-2 gap-3 md:grid-cols-4">' + "".join(
        f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5"><p class="font-[family-name:var(--font-display)] text-lg font-extrabold text-orange">{E(n)}</p>'
        f'<p class="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{l}</p></div>'
        for n, l in [(f"₹{sp / 100000:.2f}L", "Spend"), (f"{en:,}", "Enquiries"), (inr(cpe, 2), "Per enquiry"), (f"{cr:.2f}%", "Conversion rate")])
    + "</div></article></div>"
    for i, (y, lab, t, sp, en, cpe, cr, ps, warn) in enumerate(PHASES))
phases = ('<section class="section" id="phases" aria-labelledby="phases-heading">'
          + L.centered_head({"id": "phases", "pill": "Five phases", "h2": ("Nineteen quarters,", "five chapters"),
                             "body": ["Not a straight line: a restart, a scale-up, a peak, a mistake and a rebuild. Pick a year."]})
          + f'<div class="wrap mt-10" data-tabs="true"><div data-reveal="true" class="flex gap-2 overflow-x-auto pb-2">{phase_btns}</div>'
          f'<div data-reveal="true" style="--d:0.1s" class="mt-6">{phase_panels}</div></div></section>')

# ------------------------------------------------------------------ recovery, Q4 2023 vs Q4 2024
REC = [("Spend", inr(39377), inr(64227), "+63.1%"), ("Clicks", "611", "1,370", "+124.2%"), ("CTR", "4.88%", "6.67%", "+36.7%"),
       ("Average CPC", "₹64.45", "₹46.88", "−27.3%"), ("Enquiries", "59", "238", "+303.4%"), ("Cost per enquiry", "₹667.41", "₹269.86", "−59.6%")]
recovery = figure("Q4 2023 against Q4 2024", ["Same quarter, a year apart"], (
    '<div class="overflow-x-auto"><table class="w-full border-collapse text-sm"><thead><tr class="border-b border-[var(--color-line)] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="py-2 pr-3 text-left font-bold"></th><th class="py-2 pr-3 text-right font-bold">Q4 2023</th><th class="py-2 pr-3 text-right font-bold text-orange">Q4 2024</th><th class="py-2 text-right font-bold">Change</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="py-2.5 pr-3 text-left font-semibold text-ink">{k}</th>'
              f'<td class="py-2.5 pr-3 text-right text-body">{a}</td><td class="py-2.5 pr-3 text-right font-bold text-ink">{b}</td><td class="py-2.5 text-right font-bold text-orange">{c}</td></tr>'
              for k, a, b, c in REC)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">Four quarters after its worst result, the account was beating its own 19-quarter average of ₹277.91.</p>'))

# ------------------------------------------------------------------ proof
overview = (
    '<section class="section" id="proof" aria-labelledby="proof-heading">'
    + L.centered_head({"id": "proof", "pill": "Proof", "h2": ("Straight from", "the Google Ads account"),
                       "body": ["The account overview for the whole period, as Google shows it. Click the screenshot to open it full size."]})
    + '<div class="wrap mt-10" data-reveal="true"><a href="/img/1920/case-studies/4s-study-abroad/google-overview-2020-2024.webp" target="_blank" rel="noopener" '
      'class="block overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><img alt="4S Study Abroad Google Ads overview, 1 Apr 2020 to 31 Dec 2024: ₹2.46M cost, ₹278 cost per conversion, 50.6K clicks" '
      'loading="lazy" decoding="async" width="1920" height="961" class="block h-auto w-full" sizes="(min-width: 1024px) 1100px, 92vw" '
      'srcSet="' + ", ".join(f"/img/{w}/case-studies/4s-study-abroad/google-overview-2020-2024.webp {w}w" for w in (640, 1080, 1920))
    + '" src="/img/1080/case-studies/4s-study-abroad/google-overview-2020-2024.webp"/></a>'
      '<p class="mt-3 text-center text-sm text-body"><strong class="font-semibold text-ink">1 Apr 2020 - 31 Dec 2024.</strong> Cost ₹2.46M · cost per conversion ₹278 · 50.6K clicks</p></div></section>')

# ------------------------------------------------------------------ data appendix + method
appendix = (
    '<section class="section" id="data" aria-labelledby="data-heading">'
    + L.centered_head({"id": "data", "pill": "The data", "h2": ("Every quarter,", "in one table"),
                       "body": ["All figures in INR, the account currency, on Gulf Standard Time."]})
    + '<div class="wrap mt-10" data-reveal="true"><details class="card p-5 text-sm text-body md:p-6"><summary class="cursor-pointer font-semibold text-ink">Show all 19 quarters</summary>'
      '<div class="mt-4 overflow-x-auto"><table class="w-full min-w-[720px] border-collapse"><caption class="pb-2 text-left text-xs text-muted">4S Study Abroad Google Ads by quarter, Q2 2020 to Q4 2024</caption>'
      '<thead><tr class="border-b border-[var(--color-line)] text-[10px] font-bold uppercase tracking-wider text-muted">'
    + "".join(f'<th scope="col" class="py-2 pr-3 {"text-left" if i == 0 else "text-right"} font-bold">{h}</th>'
              for i, h in enumerate(["Quarter", "Spend", "Impressions", "Clicks", "CTR", "Avg CPC", "Enquiries", "Conv. rate", "Per enquiry"]))
    + "</tr></thead><tbody>"
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="py-2 pr-3 text-left font-semibold text-ink">{q[0]}</th>'
              + "".join(f'<td class="py-2 pr-3 text-right">{v}</td>' for v in
                        [inr(q[1]), f"{q[2]:,}", f"{q[3]:,}", f"{q[5]:.2f}%", inr(q[6], 2), f"{q[4]:,.1f}".replace(".0", ""), f"{q[7]:.2f}%", inr(q[8], 2)])
              + "</tr>" for q in Q)
    + "</tbody></table></div></details></div></section>")

RECON = [("Conversions", "8,859.00", "8,859.00", "100.00%"), ("Clicks", "50,521", "50,571", "99.90%"),
         ("Impressions", "9,60,425", "9,62,447", "99.79%"), ("Spend", "₹24,58,689", "₹24,61,996", "99.87%")]
method = figure("Quarterly sums against account totals", ["Reconciliation"], (
    '<div class="overflow-x-auto"><table class="w-full border-collapse text-sm"><thead><tr class="border-b border-[var(--color-line)] text-[10px] font-bold uppercase tracking-wider text-muted">'
    '<th class="py-2 pr-3 text-left font-bold"></th><th class="py-2 pr-3 text-right font-bold">Quarterly sum</th><th class="py-2 pr-3 text-right font-bold">Account total</th><th class="py-2 text-right font-bold">Match</th></tr></thead><tbody>'
    + "".join(f'<tr class="border-b border-[var(--color-line)] last:border-0"><th scope="row" class="py-2.5 pr-3 text-left font-semibold text-ink">{k}</th>'
              f'<td class="py-2.5 pr-3 text-right text-body">{a}</td><td class="py-2.5 pr-3 text-right text-body">{b}</td><td class="py-2.5 text-right font-bold text-ink">{c}</td></tr>'
              for k, a, b, c in RECON)
    + "</tbody></table></div>"
    '<p class="mt-3 text-xs text-muted">Two campaigns share a name, so one drops out of the quarterly split: ₹3,307, or 0.13% of spend. Campaign, device and account totals match Google Ads exactly.</p>'))

FAQ = [
    ("What was the cost per lead for this education Google Ads account?", "₹277.91 per enquiry across 19 quarters, improving to ₹269.86 in the final quarter, Q4 2024."),
    ("How many leads did the campaigns generate?", "8,859 enquiries from 50,571 clicks, a 16.47% click-to-enquiry rate."),
    ("Which destination market performed best?", "Germany, at ₹234.01 per enquiry with an 8.12% CTR, on the second-largest budget."),
    ("Does Google Ads work for study-abroad consultancies?", "It did here, with the account split by destination and tuned for ad relevance rather than reach. Conversion rate peaked at 33.14% in Q4 2020."),
    ("What is the biggest mistake in education PPC?", "Buying reach to fix a relevance problem. In 2023 this account had its highest quarterly impressions and, by the end of the year, its worst cost per enquiry."),
]

PAGE = {
    "path": "/case-studies/4s-study-abroad-google-ads/",
    "slug": "case-study",
    "form_name": "case_study",
    "service": "Google Ads",
    "wa_label": "case study",
    "thanks_back": ("/case-studies/", "Case studies"),
    "service_name": "4S Study Abroad Google Ads case study",
    "thanks_what": "enquiry",
    "title": "4S Study Abroad Google Ads Case Study | Sushant Rana",
    "og_title": "4S Study Abroad on Google Ads: 8,859 enquiries at ₹278",
    "og_alt": "4S Study Abroad Google Ads case study by Sushant Rana",
    "desc": "4S Study Abroad on Google Ads, Apr 2020 to Dec 2024: 8,859 student enquiries at ₹278 each, and cost per enquiry cut 59.6% after a tough 2023.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Google Ads", "/case-studies/google-ads/"), ("4S Study Abroad", None)],
    "related": [],
    "faq": {"pill": "Common questions", "h2": ("Google Ads for education,", "answered"), "body": [], "items": FAQ},
    "hero": {
        "pill": "Case study · Google Ads · Education",
        "h1": ("4S Study Abroad on Google Ads:", "8,859 enquiries at ₹278"),
        "intro_html": [
            '<a class="font-semibold text-orange" href="https://www.4sstudyabroad.com/" target="_blank" rel="noopener">4S Study Abroad</a> is an overseas education consultancy in Dubai, UAE, placing students in Canada, the UK, Germany, Australia and Europe. Over 19 quarters, ₹24.6 lakh of Google Ads brought <strong class="font-semibold text-ink">8,859 enquiries at ₹277.91 each</strong>.',
            "It was not a straight line, and the bad year is on this page too. Every number comes from the Google Ads account.",
        ],
        "cta_href": "/contact/book-strategy-call/",
        "cta2": ("See the five phases", "#phases"),
        "stats": [("8,859", "Enquiries"), ("₹278", "Per enquiry"), ("16.47%", "Click to enquiry"), ("−59.6%", "Cost per enquiry, Q4 23 to Q4 24")],
        "visual": chart,
    },
    "form": {
        "title": "Want this for your education brand?",
        "sub": "Tell me about your business and I will look at your Google Ads for free.",
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
                 "options": ["More student enquiries", "Lower cost per lead", "Better quality leads", "Fill an intake", "Not sure yet"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Destinations, markets, what you spend, what is not working..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

url = SITE + "/case-studies/4s-study-abroad-google-ads"
PAGE["graph"] = [
    {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "mainEntity": {"@id": url + "#article"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/img/1920/case-studies/4s-study-abroad/google-overview-2020-2024.webp"}},
    {"@type": "Article", "@id": url + "#article", "headline": "4S Study Abroad on Google Ads: 8,859 enquiries at ₹278", "description": PAGE["desc"],
     "author": {"@id": SITE + "/#person"}, "publisher": {"@id": SITE + "/#person"}, "datePublished": "2026-10-14", "inLanguage": "en",
     "about": {"@type": "Organization", "name": "4S Study Abroad", "url": "https://www.4sstudyabroad.com/",
               "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}}},
    {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"}, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
]

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads", "Dubai, UAE", "8,859 enquiries", "₹278 each", "Canada", "Germany", "UK", "19 quarters"]),
    L.split({"id": "challenge", "pill": "The challenge", "h2": ("A decision,", "not a purchase"),
             "body": ["Nobody buys a degree in one visit. A student fills in a form, a counsellor follows up, and the placement closes offline weeks or months later. The only thing Google Ads can count is the enquiry.",
                      "Demand is seasonal around the September and January intakes, every destination is its own auction, and big consultancy networks and universities bid on the same searches."],
             "bullets": ["Four destination markets to fill", "A cost per enquiry the counsellors can convert", "Through a pandemic and every change to Google's campaign types"],
             "visual": challenge_card}, dark=True),
    L.section_bg(L.split({"id": "destinations", "pill": "Destination first", "h2": ("One campaign set", "per destination"),
                          "body": ["Instead of one catch-all campaign, each destination got its own campaigns, budgets and bids. Canada, Germany and the UK took 86.5% of spend and brought 91.3% of enquiries.",
                                   "Germany was the efficiency winner, Canada the volume engine. Generic and university-specific campaigns were the leak: 6% of spend, 2.4% of enquiries, at ₹695 each."],
                          "bullets": ["Germany: ₹234.01 per enquiry, 8.12% CTR", "Canada: 38% of enquiries at ₹267.15", "Generic terms: 2.5 times the average cost"],
                          "visual": dest})),
    L.split({"id": "mix", "pill": "Channels and devices", "h2": ("Search did the work,", "mostly on phones"),
             "body": ["Search took 98.66% of spend and brought 98.7% of enquiries. The automated formats ran as small, controlled tests.",
                      "Switch between campaign types and devices to see each share."],
             "bullets": ["Smart: ₹165.93 per enquiry, the cheapest in the account", "Performance Max: 11 enquiries, no value signal to learn from", "Display: zero enquiries, so it was stopped"],
             "visual": mix}, flip=True),
    L.section_bg(phases),
    L.split({"id": "recovery", "pill": "The recovery", "h2": ("From the worst quarter", "to better than average"),
             "body": ["The like-for-like test: the same quarter, a year apart. More spend, but far more enquiries for it, and each one cost less than half as much."],
             "bullets": ["Enquiries up 303.4%", "Cost per enquiry down 59.6%", "Conversion rate back to 17.37%"],
             "visual": recovery}, dark=True),
    L.icon_cards({"id": "lessons", "pill": "What the data proves", "h2": ("Six lessons from", "nineteen quarters"),
                  "body": ["What held true across the whole account, good years and bad."],
                  "cards": [
                      {"icon": "layers", "h3": "Structure beat budget", "p": "The best quarter, Q3 2022, used 22.7% less money than the biggest-spending one and brought more enquiries at ₹157.84 each."},
                      {"icon": "target", "h3": "Concentration is correct", "p": "The top 10 campaigns took 84.6% of spend and returned 90% of enquiries. 31 of 76 campaigns were left switched off."},
                      {"icon": "phone", "h3": "Mobile is the market", "p": "78.06% of spend, 78.83% of enquiries, and a cost per enquiry 4.3% below computers."},
                      {"icon": "gauge", "h3": "Relevance, not money", "p": "72.76% of searches lost to ad rank and only 15.12% to budget. More budget would not have fixed it."},
                      {"icon": "zap", "h3": "Automation needs a signal", "p": "Smart brought the cheapest enquiries, ₹165.93. Performance Max, with no value data to learn from, cost ₹1,199.39 each."},
                      {"icon": "calendar", "h3": "Plan for seasons", "p": "Q3 is the strongest quarter for conversion (25.2% in 2020, 30.2% in 2022). Budgets that build into intakes beat flat monthly pacing."},
                  ]}),
    L.section_bg(overview),
    appendix,
    L.section_bg(L.split({"id": "method", "pill": "How we count", "h2": ("Where the numbers", "come from"),
                          "body": ["Everything is read from the Google Ads account for 1 April 2020 to 31 December 2024, with paused and removed campaigns included. 2020 covers nine months only.",
                                   "Enquiries are the Google Ads conversions column, mostly lead form submissions. Conversion value was only partly set up, so we do not quote revenue or ROAS. Destination groups come from campaign names."],
                          "visual": method}, flip=True)),
    L.faq(PAGE["faq"]),
    L.chips_section({"id": "related", "h2": ("More", "case studies"),
                     "body": "The same client on Meta, and more accounts we run:",
                     "chips": [("4S Study Abroad on Meta", "/case-studies/4s-study-abroad/"), ("Google Ads case studies", "/case-studies/google-ads/"),
                               ("Google Ads management", "/services/google-ads/"), ("Education marketing", "/industries/education/")]}),
    L.form_section(PAGE, {"pill": "Your turn", "h2": ("Want this for your", "education brand?"),
                          "body": ["Tell me about your business and your Google Ads. I will look at your account and show you where the money is actually going, for free."],
                          "bullets": ["Free account review", "You talk to me directly", "No obligation"]}),
]
