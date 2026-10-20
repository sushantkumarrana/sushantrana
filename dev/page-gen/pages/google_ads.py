# Google Ads Management Services. Copy: 02_Google_Ads_Management_Services.docx
# Numbers (hero stats, results, reviews, compare table) wait for Sushant.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free Google Ads audit"

# --------------------------------------------------- interactive visuals

serp = figure("Google search", ["Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type what your buyer searches</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="kw" placeholder="emergency plumber near me" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Search words to preview"/></span></label>'
    '<div class="mt-4 rounded-2xl border border-orange/30 bg-orange/5 p-4">'
    '<p class="text-[11px] font-bold text-ink">Sponsored</p><p class="text-[11px] text-muted">yourbusiness.com</p>'
    '<p class="svc-serp-title mt-1 text-base font-bold leading-snug"><span data-mirror-out="kw" class="svc-cap"></span> | Your Business</p>'
    '<p class="mt-1 text-xs text-body">Ad text written for this exact search, with your offer and one clear next step.</p></div>'
    '<p class="mt-5 text-[10px] font-bold uppercase tracking-wider text-muted">Results without an ad</p>'
    '<div class="mt-2.5 grid gap-3" aria-hidden="true">'
    + '<div class="rounded-2xl border border-[var(--color-line)] p-4 opacity-60"><span class="block h-2 w-24 rounded-full bg-ink/10"></span>'
      '<span class="mt-2 block h-3 w-3/4 rounded-full bg-ink/15"></span><span class="mt-2 block h-2 w-full rounded-full bg-ink/10"></span></div>' * 2
    + '</div><p class="mt-5 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
    f'{svg("target", "h-4 w-4 shrink-0 text-orange")}Your ad shows at the top, only when someone searches words like these.</p>'
))


def tile(icon, name, note=""):
    return (f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3.5 text-center">'
            f'<span class="mx-auto grid h-10 w-10 place-items-center rounded-xl bg-orange/10 text-orange">{svg(icon, "h-5 w-5")}</span>'
            f'<p class="mt-2 text-xs font-bold text-ink">{E(name)}</p></div>')


MOCKS = {
    "search": figure("Search ad", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] font-bold text-ink">Sponsored</p>'
        '<p class="text-[11px] text-muted">yourbusiness.com/services</p><p class="svc-serp-title mt-1 text-base font-bold">Your Service In Your City | Call Today</p>'
        '<p class="mt-1 text-xs text-body">Clear offer, the reason to choose you, and a call or enquiry button.</p>'
        '<div class="mt-3 flex flex-wrap gap-2 text-[11px] font-semibold text-orange"><span>Get a quote</span><span>Our services</span><span>Contact us</span></div></div>')),
    "pmax": figure("Performance Max", ["Example"], (
        '<p class="text-center text-[10px] font-bold uppercase tracking-wider text-muted">One campaign, shown across</p>'
        '<div class="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">'
        + tile("search", "Search") + tile("target", "Maps") + tile("play", "YouTube") + tile("file", "Gmail") + tile("image", "Display network")
        + '<div class="grid place-items-center rounded-2xl bg-orange p-3.5 text-center text-xs font-bold text-white">Guided by your data and goals</div></div>')),
    "shopping": figure("Shopping ads", ["Example"], (
        '<p class="text-[11px] font-bold text-ink">Sponsored products</p><div class="mt-3 grid grid-cols-3 gap-3">'
        + "".join(
            f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-7 w-7")}</div>'
            f'<div class="p-3"><p class="text-[11px] font-bold leading-tight text-ink">{n}</p><p class="mt-1 text-xs font-extrabold text-ink">{pr}</p><p class="text-[10px] text-muted">Your store</p></div></div>'
            for n, pr in [("Product one", "₹1,499"), ("Product two", "₹899"), ("Product three", "₹2,250")])
        + '</div><p class="mt-3 text-xs text-body">Image, price and store name, right on the results page.</p>')),
    "display": figure("Display ad", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4" aria-hidden="true"><span class="block h-3 w-1/2 rounded-full bg-ink/15"></span>'
        '<span class="mt-3 block h-2 w-full rounded-full bg-ink/10"></span><span class="mt-2 block h-2 w-5/6 rounded-full bg-ink/10"></span>'
        '<div class="grad-ink-orange mt-4 rounded-xl p-4 text-center"><p class="text-sm font-extrabold text-white">Your banner ad</p>'
        '<p class="mt-1 text-[11px] text-white/75">Shown on websites and apps your audience reads</p>'
        '<span class="mt-3 inline-flex rounded-full bg-white px-3 py-1 text-[10px] font-bold text-ink">Learn more</span></div>'
        '<span class="mt-4 block h-2 w-full rounded-full bg-ink/10"></span><span class="mt-2 block h-2 w-2/3 rounded-full bg-ink/10"></span></div>')),
    "video": figure("YouTube video ad", ["Example"], (
        '<div class="relative grid aspect-video place-items-center overflow-hidden rounded-2xl bg-[#0a0a0a]">'
        f'<span class="grid h-12 w-12 place-items-center rounded-full bg-orange text-white">{svg("play", "h-6 w-6")}</span>'
        '<span class="absolute bottom-3 left-3 rounded bg-white/90 px-2 py-0.5 text-[10px] font-bold text-ink">Ad</span>'
        '<span class="absolute bottom-3 right-3 rounded bg-black/55 px-3 py-1 text-[11px] font-bold text-white">Skip ad ▸</span></div>'
        '<p class="mt-3 text-xs text-body">Your story told in seconds, then a reason to visit your site.</p>')),
    "remarketing": figure("Remarketing", ["Example"], (
        '<ol class="grid list-none gap-3">' + "".join(
            f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
            f'<span class="text-sm font-semibold text-ink">{t}</span></li>'
            for i, t in enumerate(["Someone visits your website", "They leave without buying", "They see your ad on YouTube, Gmail and other sites", "They come back and buy"], 1))
        + '</ol>')),
}

TYPES = [
    ("search", "Search Ads", "search", "Text ads that appear at the top of Google when people search for your keywords.", "Best for capturing high intent leads and sales."),
    ("pmax", "Performance Max", "layers", "A smart campaign that shows your ads across Search, Maps, YouTube, Gmail and the Display network from a single setup.", "Great for wide reach and sales when set up carefully."),
    ("shopping", "Google Shopping Ads", "bag", "Product ads with an image, price and store name that appear right in search.", "Perfect for online stores that want ready to buy shoppers."),
    ("display", "Display Ads", "image", "Banner ads that appear on millions of websites and apps.", "Strong for building brand awareness and staying in front of your audience."),
    ("video", "Video Ads", "play", "Ads that run on YouTube to grow awareness and bring warm viewers back to your site.", "A great way to tell your story."),
    ("remarketing", "Remarketing", "repeat", "Ads that follow up with people who visited your site but did not buy.", "One of the cheapest ways to win back lost sales."),
]

tab_btns = "".join(
    f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" '
    'data-on="border-orange bg-white shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)]" data-off="border-[var(--color-line)] bg-white/60 hover:border-orange" '
    f'class="flex w-full items-center gap-3 rounded-2xl border p-3 text-left text-sm transition sm:p-5 sm:text-base {"border-orange bg-white shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)]" if i == 0 else "border-[var(--color-line)] bg-white/60 hover:border-orange"}">'
    f'<span class="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-5 w-5")}</span>'
    f'<span class="font-[family-name:var(--font-display)] font-extrabold leading-tight text-ink">{E(name)}</span></button>'
    for i, (k, name, ic, _, _) in enumerate(TYPES))
HID = ' hidden=""'
tab_panels = "".join(
    f'<div data-panel="{k}"{HID if i else ""}>{MOCKS[k]}<p class="mt-5 text-body"><strong class="font-semibold text-ink">{E(name)}.</strong> {E(what)}</p>'
    f'<p class="mt-2 text-sm font-semibold text-orange">{E(best)}</p></div>'
    for i, (k, name, _, what, best) in enumerate(TYPES))

types_section = (
    '<section class="section" id="types" aria-labelledby="types-heading">'
    + L.centered_head({"id": "types", "pill": "Ad types", "h2": ("The Google Ads campaign types", "I run for you"),
                       "body": ["Google has many campaign types, and each one does a different job. I pick the right mix for your goals and manage them all under one clear strategy. Pick one to see what it looks like."]})
    + f'<div class="wrap mt-12 grid items-start gap-8 lg:grid-cols-2" data-tabs="true"><div data-reveal="true" class="grid grid-cols-2 gap-3 lg:grid-cols-1">{tab_btns}</div>'
    f'<div data-reveal="true" style="--d:0.1s" class="lg:sticky lg:top-24">{tab_panels}</div></div></section>')

LEAKS = [
    ("I am not sure my conversion tracking is right", "Without it you cannot tell which clicks became leads or sales."),
    ("I have never added negative keywords", "Your ads may be paying for searches that will never buy."),
    ("Most of my keywords are on broad match", "The wrong match types let Google show your ad on loosely related searches."),
    ("My ads send people to the home page", "Clicks land on a weak page instead of one built for that search."),
]
leak_box = figure("Budget leak check", ["Self check"], (
    '<div data-leaks="true"><p class="text-sm text-body">Tick everything that sounds like your account.</p><div class="mt-4 grid gap-3">'
    + "".join(
        f'<label class="svc-check"><input type="checkbox" class="sr-only"/><span class="svc-box">{svg("check", "h-3.5 w-3.5", 3)}</span>'
        f'<span><span class="block text-sm font-bold text-ink">{E(t)}</span><span class="mt-0.5 block text-xs text-muted">{E(n)}</span></span></label>'
        for t, n in LEAKS)
    + '</div><div class="mt-5 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-4"><p class="flex items-baseline justify-between text-xs font-semibold uppercase tracking-wide text-muted">'
    '<span>Leaks ticked</span><span class="font-[family-name:var(--font-display)] text-lg font-extrabold text-orange" aria-live="polite"><span data-leak-count="true">0</span> of 4</span></p>'
    '<div class="mt-2 h-2 overflow-hidden rounded-full bg-ink/10" aria-hidden="true"><span data-leak-bar="true" class="block h-full w-0 rounded-full bg-orange transition-[width] duration-300"></span></div>'
    '<p data-leak-msg="0" class="mt-3 text-sm text-body">Nothing ticked yet. A free audit still checks the parts that are hard to see from the dashboard.</p>'
    '<p data-leak-msg="1" hidden="" class="mt-3 text-sm text-body">A leak or two. These are usually the first things I fix when I take over an account.</p>'
    '<p data-leak-msg="2" hidden="" class="mt-3 text-sm text-body">Your budget is very likely leaking. Fixing these first often brings the cost per lead down.</p></div>'
    f'<a href="#contact" class="btn btn-primary mt-5 w-full">{CTA}</a></div>'
))

GET = [
    {"icon": "search", "h3": "Deep keyword research", "p": "I find the exact words your buyers use and study what your competitors are doing, so we target the right searches from day one."},
    {"icon": "pen", "h3": "Ad copy written and tested", "p": "Clear, benefit driven ads, with different versions tested to find the ones that bring the most conversions at the lowest cost."},
    {"icon": "layers", "h3": "Full campaign build", "p": "Campaigns, ad groups and negative keyword lists set up properly, so your budget only goes into searches that can turn into customers."},
    {"icon": "phone", "h3": "Conversion, call and CRM tracking", "p": "Every lead, call and sale is counted correctly with Google Tag Manager, Google Analytics 4 and your CRM, so you know what each click is really worth."},
    {"icon": "sliders", "h3": "Weekly optimization", "p": "Bid management, pausing weak keywords and testing new ads every week. This is where your cost per lead starts to drop."},
    {"icon": "chart", "h3": "Reports in plain language", "p": "Easy to read monthly reports on what you spent and what you earned back, plus landing page advice whenever your page is costing you leads."},
]

FAQ = [
    ("What are Google Ads?", "Google Ads is Google's paid advertising system. It lets your business appear at the top of Google search results, on YouTube, on Maps and across millions of websites, so you reach people who are looking for what you sell."),
    ("How much budget do I need for Google Ads?", "It depends on your industry and your goals. Some clients start small and scale up once we see profit. On our first call I will suggest a realistic starting budget for your market so you never overspend."),
    ("How soon will I get leads from Google Ads?", "Google Ads can bring traffic and leads within the first few days. The first few weeks are used to gather data and improve the account, so stable results usually build from the first month onwards."),
    ("What is the difference between Google Ads and SEO?", "Google Ads brings instant paid traffic, while SEO builds free traffic slowly over time. Ads are great for fast results, and the best growth usually comes from using both together."),
    ("What is Quality Score and why does it matter?", "Quality Score is Google's rating of how relevant your ad, keyword and landing page are. A higher score lowers your cost per click and improves your ad position, so it saves you money."),
    ("What are negative keywords?", "Negative keywords are searches you do not want to pay for. Adding them stops your ads from showing on the wrong searches, which saves a large part of your budget."),
    ("Do you set up conversion tracking?", "Yes, and it is one of the first things I fix. Without correct tracking you cannot know which clicks turn into leads and sales, so I set this up properly using tools like Google Tag Manager and Google Analytics 4."),
    ("What is Performance Max?", "Performance Max is a smart Google campaign that shows your ads across all of Google from one setup. It works well when it is guided with strong data and clear goals, which is exactly what I do."),
    ("Do I need a CRM to run Google Ads?", "You can run ads without one, but then Google only learns from form fills, good and bad alike. When your CRM sends back which leads were qualified and which became sales, Google Ads bids for more people like your real customers. I connect Zoho, HubSpot or GoHighLevel to your account, or set one up if you do not have a CRM yet."),
    ("Can you run Google Shopping ads for my store?", "Yes. I set up your product feed and run Shopping and Performance Max campaigns that put your products in front of ready to buy shoppers and track every sale."),
    ("Do I need a landing page for Google Ads?", "In most cases a focused landing page converts much better than a normal website page. If your page is weak I will point it out and help you improve it, because it directly affects your cost per lead."),
    ("Will you write the ad copy?", "Yes. I write clear, benefit driven ad copy and test different versions to find the ones that bring the most clicks and conversions at the lowest cost."),
    ("How do you stop my budget from being wasted?", "I add negative keywords, use the right match types, fix tracking, pause weak keywords and send traffic only to strong pages. These steps cut waste and lower your cost per result."),
    ("Can you fix my existing Google Ads account?", "Yes. This is one of the most common requests I get. I audit your account, find the leaks and rebuild the parts that are holding you back."),
    ("Do you manage Google Ads for local businesses?", "Yes. Local businesses do very well on Google Ads when campaigns are set up carefully with the right locations, keywords and call tracking."),
    ("What reports will I get?", "You get clear monthly reports in plain language that show what you spent and what you earned back, plus updates whenever something important changes."),
    ("How do I get started?", "Just book a free Google Ads audit using the button on this page. I will review your business and your account and show you how we can grow your leads and sales."),
]

# ------------------------------------------------ ads + CRM (illustration)

LEADS = [  # (lead, CRM status, sent back to Google?, value)
    ("Lead 1", "Fake number", False, ""),
    ("Lead 2", "Just browsing", False, ""),
    ("Lead 3", "Qualified", True, ""),
    ("Lead 4", "Paid", True, "with sale value"),
]


def lead_rows(crm):
    rows = ""
    for name, status, sent, value in LEADS:
        if crm:
            tag = (f'<span class="rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange">{"Sent " + value if value else "Sent to Google"}</span>'
                   if sent else '<span class="rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted">Not counted</span>')
            mid = f'<span class="text-xs font-semibold text-ink">{status}</span>'
        else:
            tag = '<span class="rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted">1 conversion</span>'
            mid = '<span class="text-xs text-muted">Form filled</span>'
        rows += (f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
                 f'<span class="grid"><span class="text-sm font-bold text-ink">{name}</span>{mid}</span>{tag}</li>')
    return f'<ul class="grid list-none gap-2.5">{rows}</ul>'


def verdict(text, strong):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg("target", "h-4 w-4 shrink-0 text-orange")}<span><strong class="font-semibold text-ink">{strong}</strong> {text}</span></p>')


CRM_TOGGLE = "".join(
    f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
    f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i else "bg-white text-ink hover:text-orange"}">{label}</button>'
    for i, (k, label) in enumerate([("without", "Without CRM"), ("with", "With CRM connected")]))

crm_box = (
    '<div data-tabs="true">' + figure("What Google Ads learns from", ["Example"], (
        f'<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">{CRM_TOGGLE}</div>'
        '<p class="mt-4 text-[10px] font-bold uppercase tracking-wider text-muted">Four leads from this week\'s ads</p>'
        f'<div class="mt-2.5" data-panel="without" hidden="">{lead_rows(False)}'
        + verdict("so it bids for more form fills, including the junk ones.", "Google sees 4 equal conversions,")
        + f'</div><div class="mt-2.5" data-panel="with">{lead_rows(True)}'
        + verdict("so it bids for more people like your real customers.", "Google sees the 2 leads that mattered,")
        + "</div>")) + "</div>")

CRMS = [("Zoho CRM", "/services/zoho-crm/"), ("HubSpot CRM", "/services/hubspot-crm/"), ("GoHighLevel", "/services/gohighlevel/")]
crm_links = ('<ul class="mt-7 flex list-none flex-wrap gap-2.5">' + "".join(
    f'<li><a class="inline-flex rounded-full border border-[var(--color-line)] bg-white px-4 py-2 font-[family-name:var(--font-display)] text-xs font-semibold text-ink transition hover:border-orange hover:text-orange" href="{h}">{t}</a></li>'
    for t, h in CRMS) + "</ul>")

# ------------------------------------------------- projects (published facts only)
# Every fact below is already on the live home page (client feedback block).
# Real Google Ads dashboard screenshots go in "dashboard" once Sushant sends them.

PROJECTS = [
    {"key": "yalla", "name": "Yalla Renovation", "what": "Home renovation", "where": "Dubai, UAE", "img": "yalla-renovation-website",
     "channels": ["Google Ads", "Meta Ads"], "case": "/case-studies/yalla-renovation/",
     "facts": [("~₹10L", "Monthly Google and Meta budget"), ("Leads", "Judged on site visits booked")],
     "story": "Renovation leads are expensive, and volume the sales team cannot close is wasted money. We run Google and Meta as one budget and judge it on leads that turn into site visits, so the team spends its time on real homeowners and villa owners."},
    {"key": "warriors", "name": "Warrior's Cove", "what": "Martial arts academy", "where": "Minnesota, USA", "img": "warriors-cove-website",
     "channels": ["Google Ads", "Meta Ads"],
     "facts": [("1+ yr", "Leads coming in without a break"), ("2", "Gyms: Minneapolis and Saint Paul")],
     "story": "Membership enquiries are the lifeblood of the business. We have kept Google Ads and Meta Ads delivering leads continuously for over a year, run from India, with clear reporting and changes flagged before they have to ask."},
    {"key": "touch", "name": "Touch Abroad", "what": "Career training", "where": "Ontario, Canada", "img": "touch-abroad-website",
     "channels": ["Website", "Google Ads", "Meta Ads"],
     "facts": [("2 yrs", "Working together"), ("1", "Owner for the site and the ads")],
     "story": "We built the website and have run the Google Ads and Meta Ads that fill enquiries for their PSW and skill based programmes ever since. One person owning both means nothing falls between two vendors, and every intake starts with a full list of people to call."},
    {"key": "elixir", "name": "Elixir Engineering", "what": "Fire safety engineering", "where": "India", "img": "elixir-engineering-website",
     "channels": ["SEO", "Google Ads"],
     "facts": [("40-45", "Leads every month, SEO and Ads"), ("SEO + Ads", "Ads cover what SEO has not reached")],
     "story": "Fire safety maintenance, Form B audits, training and repairs are hard to find online. SEO got several target keywords ranking, and Google Ads covers the searches SEO has not reached yet."},
]

proj_btns = "".join(
    f'<button type="button" data-tab="{p["key"]}" aria-pressed="{"true" if i == 0 else "false"}" '
    'data-on="border-orange bg-white shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)]" data-off="border-[var(--color-line)] bg-white/60 hover:border-orange" '
    f'class="w-full rounded-2xl border p-3 text-left transition sm:p-5 {"border-orange bg-white shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)]" if i == 0 else "border-[var(--color-line)] bg-white/60 hover:border-orange"}">'
    f'<span class="block font-[family-name:var(--font-display)] text-sm font-extrabold text-ink sm:text-base">{E(p["name"])}</span>'
    f'<span class="mt-0.5 block text-xs text-muted">{E(p["what"])} · {E(p["where"])}</span></button>'
    for i, p in enumerate(PROJECTS))


def shot(p):
    widths = [384, 640, 750, 828, 1080, 1200, 1920]
    srcset = ", ".join(f'/img/{w}/clients/{p["img"]}.webp {w}w' for w in widths)
    return (f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="flex items-center gap-1.5 border-b border-[var(--color-line)] px-3 py-2" aria-hidden="true">'
            '<span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span></div>'
            f'<img alt="{E(p["name"])} website, a {E(p["what"].lower())} client whose ads Sushant Rana runs" loading="lazy" decoding="async" width="1400" height="765" '
            f'class="block h-auto w-full" sizes="(min-width: 1024px) 560px, 92vw" srcSet="{srcset}" src="/img/1200/clients/{p["img"]}.webp"/></div>')


proj_panels = "".join(
    f'<div data-panel="{p["key"]}"{HID if i else ""}><article class="card overflow-hidden p-5 md:p-6">{shot(p)}'
    '<div class="mt-5 flex flex-wrap gap-2">' + "".join(
        f'<span class="rounded-full border border-orange/30 bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{E(c)}</span>' for c in p["channels"]) + '</div>'
    f'<h3 class="mt-4 text-xl font-extrabold text-ink">{E(p["name"])}</h3><p class="text-sm text-muted">{E(p["what"])} · {E(p["where"])}</p>'
    '<div class="mt-4 grid grid-cols-2 gap-3">' + "".join(
        f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5"><p class="font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">{E(n)}</p>'
        f'<p class="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{E(l)}</p></div>' for n, l in p["facts"]) + '</div>'
    f'<p class="mt-4 text-body">{E(p["story"])}</p>'
    + (f'<a href="{p["case"]}" class="btn btn-outline mt-5">Read the case study</a>' if p.get("case") else "") + '</article></div>'
    for i, p in enumerate(PROJECTS))

projects_section = (
    '<section class="section" id="work" aria-labelledby="work-heading">'
    + L.centered_head({"id": "work", "pill": "Client work", "h2": ("Google Ads accounts", "we run right now"),
                       "body": ["Real businesses in Dubai, the USA, Canada and India. Pick one to see what we run for them and what it delivers."]})
    + f'<div class="wrap mt-12 grid items-start gap-8 lg:grid-cols-[1.05fr_0.95fr]" data-tabs="true">'
    f'<div data-reveal="true" class="grid grid-cols-2 gap-3 lg:order-2 lg:grid-cols-1 lg:self-start">{proj_btns}</div>'
    f'<div data-reveal="true" style="--d:0.1s" class="lg:order-1">{proj_panels}</div></div></section>')

RELATED = [
    ("Google Shopping Ads", "/services/google-shopping-ads/"),
    ("Remarketing", None),
    ("YouTube Ads", "/services/youtube-ads/"),
    ("Landing pages", "/services/landing-pages/"),
    ("Performance marketing", "/services/performance-marketing/"),
    ("Local SEO", "/services/local-seo/"),
]

PAGE = {
    "path": "/services/google-ads/",
    "slug": "google-ads",
    "form_name": "google_ads",
    "service": "Google Ads",
    "service_name": "Google Ads management",
    "thanks_what": "Google Ads audit",
    "category": "Pay per click advertising",
    "service_desc": "Google Ads management covering Search, Performance Max, Shopping, Display, YouTube video and remarketing campaigns, with keyword research, ad copy, conversion tracking, weekly optimization and monthly reporting.",
    "audience": "Businesses that need leads or online sales",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What Google Ads management includes",
    "offers": GET,
    "title": "Google Ads Management Services | Sushant Rana",
    "og_title": "Google Ads Management Services",
    "og_alt": "Google Ads management services by Sushant Rana",
    "desc": "Google Ads management that brings ready to buy customers, not just clicks. Search, Shopping, Performance Max and remarketing. Book a free audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Google Ads", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Google Ads management", "questions, answered"),
            "body": ["Budgets, timelines, tracking and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Google Ads management",
        "h1": ("Google Ads management services that", "bring ready to buy customers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I build and manage Google Ads campaigns that bring you real leads and sales, not just clicks. Every part of your account is set up to get the most value from your budget.',
            "Whether you are new to Google Ads or your current campaigns are burning money, we can help you turn Google into a steady source of customers, for businesses across India, the UAE, the US and Canada.",
        ],
        "cta2": ("See client work", "#work"),
        # same figures as the live home page
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free Google Ads audit",
        "sub": "Tell me about your business and I will review your account for free.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Account", "fields": [
                {"type": "radio", "name": "running", "label": "Are you running Google Ads now?", "req": True,
                 "options": ["Yes, running now", "Paused or stopped", "Never run them"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["More leads or enquiries", "More online sales", "More phone calls", "More store visits", "Not sure yet"]},
                {"type": "checkbox", "name": "campaigns", "label": "Campaigns you are interested in",
                 "options": ["Search", "Performance Max", "Shopping", "Display", "YouTube", "Remarketing", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, where you sell it, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Search ads", "Performance Max", "Shopping", "Display", "YouTube", "Remarketing", "Conversion tracking"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What Google Ads can do", "for your business"),
             "body": ["Google Ads puts your business in front of people at the exact moment they are searching for your product or service. This is the most powerful type of buyer intent, because the person is already looking for what you offer.",
                      "Unlike SEO, which builds over months, Google Ads can start bringing traffic and leads on the same day your campaign goes live. This makes it perfect for new offers, launches and any business that needs customers now."],
             "bullets": ["Shown only to people searching for what you sell", "Live and bringing traffic on day one", "Every click, lead and sale tracked"],
             "cta": CTA, "visual": serp}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why Google Ads is one of", "the best ways to grow"),
                      "body": ["Google Ads is popular for a reason. When it is managed well, it gives you fast, clear and profitable results."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "target", "h3": "You reach high intent buyers", "p": "Your ads only show to people who are actively searching for what you sell. These are warm buyers, not random visitors, which means better quality leads."},
                          {"icon": "wallet", "h3": "You stay in control of the budget", "p": "You decide how much to spend per day and per month. I make sure that budget goes only into the keywords and audiences that bring results."},
                          {"icon": "click", "h3": "You only pay for clicks", "p": "In most campaigns you pay only when someone clicks your ad, not when it is shown. This keeps your money focused on real interest."},
                          {"icon": "chart", "h3": "Everything is measurable", "p": "You will always know your cost per click, your cost per lead and your return on ad spend. There is no guessing, only clear numbers."},
                      ]})
        + types_section),
    projects_section,
    L.split({"id": "waste", "pill": "The real problem", "h2": ("Why most Google Ads accounts", "waste money"),
             "body": ["Many business owners tell me their Google Ads just do not work. In most cases the account was set up in a rush and never fixed. The most common leaks are broken conversion tracking, no negative keywords, the wrong keyword match types and sending clicks to a weak page.",
                      "When I take over an account, I fix these problems first. Very often this alone brings down the cost per lead and starts turning a losing account into a profitable one."],
             "visual": leak_box}),
    L.split({"id": "crm", "pill": "Ads + CRM", "h2": ("Google Ads only works properly", "when your CRM is connected"),
             "body": ["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the fake numbers and the people who were only browsing.",
                      "So on every account we connect the ads to your CRM. The click is saved with each lead, your sales team updates the lead status, and the qualified leads and sales flow back into Google Ads as conversions, with their value. From then on Google bids for buyers, not for forms."],
             "bullets": ["Click ID saved with every lead", "Lead status synced from Zoho, HubSpot or GoHighLevel", "Qualified leads and sales sent back as conversions", "Reports on cost per qualified lead and cost per sale"],
             "after": crm_links, "cta": CTA, "visual": crm_box}, dark=True),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My Google Ads", "management process"),
                   "body": ["Good results come from a clear process, not luck. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Audit and goals", "short": "Audit", "p": "I study your business, your goals and your current account. This tells me what a good result looks like and where money is being wasted.", "points": ["Business and goal review", "Current account audit", "Where money is leaking"]},
                       {"h3": "Keyword and competitor research", "short": "Research", "p": "I find the exact keywords your buyers use and study what your competitors are doing, so we target the right searches from day one.", "points": ["Buyer keyword list", "Competitor ad review", "Negative keyword list"]},
                       {"h3": "Campaign build and tracking", "short": "Build", "p": "I build your campaigns, write the ad copy, add negative keywords and set up proper conversion tracking so every lead and sale is counted correctly.", "points": ["Campaigns and ad copy", "Conversion and call tracking", "CRM connected to Google Ads"]},
                       {"h3": "Weekly optimization", "short": "Optimize", "p": "I improve the account every week by pausing weak keywords, testing new ads and adjusting bids. This is where your cost per lead starts to drop.", "points": ["Bid adjustments", "New ad tests", "Weak keywords paused"]},
                       {"h3": "Reporting and scaling", "short": "Scale", "p": "You get clear reports in plain language. When a campaign is profitable, I scale it up in a safe and steady way.", "points": ["Plain language reports", "Spend versus return", "Steady, safe scaling"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my Google Ads service"),
                  "body": ["You get a complete, done for you Google Ads service. I handle the strategy, the setup, the daily work and the reporting, and you always talk to me directly."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Is your Google Ads budget being wasted?",
                                       "p": "Let me take a free look at your account. I will show you exactly where money is leaking and how we can fix it. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for Google Ads"),
                  "body": ["The person who plans your account is the person you talk to, and every report is about leads, sales and profit."],
                  "cards": [
                      {"h3": "You work directly with me", "p": "No middleman and no account manager relaying your notes. The person accountable for your ads is the same person you talk to."},
                      {"h3": "Your budget goes into ads, not overheads", "p": "Working with me keeps your money focused on results instead of big agency office costs, which means better value for you."},
                      {"h3": "Honest reporting, real numbers", "p": "I report on leads, sales and profit, not vanity metrics. You always know the truth about what is working."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I run", "Google Ads for"),
                     "body": "Ecommerce stores, local service businesses, clinics, property, education, law firms, home services and B2B companies. If your business needs leads or online sales, Google Ads can work for you.",
                     "chips": [("Ecommerce stores", None), ("Local businesses", None), ("Healthcare", None),
                               ("Dental clinics", "/industries/dental/"), ("Real estate", "/industries/real-estate/"), ("Education", "/industries/education/"),
                               ("Legal firms", "/industries/legal-firms/"), ("Home services", None), ("B2B companies", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "Google Ads"),
                     "body": "Ads earn more when the landing page, the follow up and the other channels are handled alongside them.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to get more", "from Google Ads?"),
               "p": "Let us look at your goals and your account together and build a plan that brings real customers. The first step is a simple, friendly call.",
               "btn": CTA, "note": "No obligation · Free account audit"}),
]
