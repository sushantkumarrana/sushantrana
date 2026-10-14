# Real Estate Marketing Services (industry page). Copy: 22_Real_Estate_Marketing_Services.docx
# No client work: none of the published clients is a real estate business.
E, svg, figure, pill, HID = L.E, L.svg, L.figure, L.pill, L.HID

CTA = "Book your free real estate marketing call"

# --------------------------------------------------- mock building blocks
# Every mock is an "Example" with placeholder names and no performance figures.

STARS = '<span class="text-xs font-bold text-orange" aria-hidden="true">★★★★★</span>'


def bars(*widths):
    return "".join(f'<span class="mt-2 block h-2 {w} rounded-full bg-ink/10"></span>' for w in widths)


def tag(text, on=True):
    look = "bg-orange/10 text-orange" if on else "bg-ink/[0.06] text-muted"
    return f'<span class="rounded-full {look} px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide">{E(text)}</span>'


def map_area():
    pins = "".join(
        f'<span class="absolute grid h-8 w-8 place-items-center rounded-full {c}" style="left:{x};top:{y}">{svg("target", "h-4 w-4")}</span>'
        for c, x, y in [("bg-orange text-white", "28%", "30%"), ("bg-ink/15 text-white", "62%", "18%"), ("bg-ink/15 text-white", "70%", "58%")])
    return ('<div class="relative aspect-video overflow-hidden rounded-2xl bg-[#fff7f3]" aria-hidden="true">'
            '<span class="absolute inset-x-0 h-2 bg-white" style="top:46%"></span><span class="absolute w-2 bg-white" style="top:0;bottom:0;left:52%"></span>'
            f'{pins}</div>')


def place_rows(you, note, other):
    rows = (f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-orange/30 bg-orange/5 px-4 py-3">'
            f'<span class="grid"><span class="text-sm font-bold text-ink">{E(you)}</span><span class="flex items-center gap-2 text-xs text-muted">{STARS}{E(note)}</span></span>'
            '<span class="rounded-full bg-orange px-3 py-1 text-[11px] font-bold text-white">Call</span></li>')
    rows += (f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3 opacity-60" aria-hidden="true">'
             f'<span class="grid"><span class="text-sm font-bold text-ink">{E(other)}</span><span class="block h-2 w-24 rounded-full bg-ink/10"></span></span></li>') * 2
    return f'<ul class="mt-3 grid list-none gap-2.5">{rows}</ul>'


def search_ad(url, title, text, links):
    return ('<div class="rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] font-bold text-ink">Sponsored</p>'
            f'<p class="text-[11px] text-muted">{E(url)}</p><p class="svc-serp-title mt-1 text-base font-bold">{E(title)}</p>'
            f'<p class="mt-1 text-xs text-body">{E(text)}</p>'
            '<div class="mt-3 flex flex-wrap gap-2 text-[11px] font-semibold text-orange">' + "".join(f"<span>{E(x)}</span>" for x in links) + "</div></div>")


def social_ad(name, head, sub, btn):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            f'<div class="flex items-center gap-2 p-3"><span class="grid h-8 w-8 place-items-center rounded-full bg-orange/10 text-orange">{svg("users", "h-4 w-4")}</span>'
            f'<span class="grid"><span class="text-xs font-bold text-ink">{E(name)}</span><span class="text-[10px] text-muted">Sponsored</span></span></div>'
            f'<div class="grad-ink-orange grid aspect-video place-items-center p-4 text-center"><span><span class="block text-base font-extrabold text-white">{E(head)}</span>'
            f'<span class="mt-1 block text-[11px] text-white/75">{E(sub)}</span></span></div>'
            f'<div class="flex items-center justify-between gap-3 p-3"><span class="text-xs font-semibold text-ink">yourbusiness.com</span>'
            f'<span class="rounded-full bg-orange px-3 py-1 text-[11px] font-bold text-white">{E(btn)}</span></div></div>')


def landing(head, sub, fields, btn):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="flex items-center gap-1.5 border-b border-[var(--color-line)] px-3 py-2" aria-hidden="true">'
            '<span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span></div>'
            f'<div class="p-4"><p class="text-base font-extrabold leading-snug text-ink">{E(head)}</p><p class="mt-1 text-xs text-body">{E(sub)}</p>'
            '<div class="mt-4 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5">'
            + "".join(f'<span class="mt-2 block rounded-xl border border-[var(--color-line)] bg-white px-4 py-2 text-xs text-muted">{E(f)}</span>' for f in fields)
            + f'<span class="mt-3 block rounded-full bg-orange px-4 py-2.5 text-center text-xs font-bold text-white">{E(btn)}</span></div></div></div>')


def reviews(who):
    cards = "".join(
        f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><p class="flex items-center justify-between gap-3"><span class="text-xs font-bold text-ink">{E(n)}</span>{STARS}</p>'
        f'{bars("w-full", "w-5/6")}</div>' for n in [f"{who} one", f"{who} two", f"{who} three"])
    return f'<div class="grid gap-3" aria-hidden="true">{cards}</div>'


def tracking(rows, foot):
    out = "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid"><span class="text-sm font-bold text-ink">{E(src)}</span><span class="text-xs text-muted">{E(kind)}</span></span>{tag(st, on)}</li>'
        for src, kind, st, on in rows)
    return (f'<ul class="grid list-none gap-2.5">{out}</ul><p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg("target", "h-4 w-4 shrink-0 text-orange")}<span>{E(foot)}</span></p>')


def steps(items):
    return ('<ol class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
        f'<span class="text-sm font-semibold text-ink">{E(t)}</span></li>'
        for i, t in enumerate(items, 1)) + "</ol>")


def pick_demo(title, label, opts, body, foot, icon="target"):
    """Pill buttons that switch a panel. opts = [(key, label)], body(key) -> panel html."""
    btns = "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{E(lab)}</button>'
        for i, (k, lab) in enumerate(opts))
    panels = "".join(f'<div data-panel="{k}"{HID if i else ""}>{body(k)}</div>' for i, (k, _) in enumerate(opts))
    return '<div data-tabs="true">' + figure(title, ["Example"], (
        f'<p class="text-[10px] font-bold uppercase tracking-wider text-muted">{E(label)}</p>'
        f'<div class="mt-2 flex flex-wrap gap-1 rounded-2xl border border-[var(--color-line)] bg-white p-1">{btns}</div>{panels}'
        '<p class="mt-4 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
        f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}{E(foot)}</p>')) + "</div>"


# --------------------------------------------------- 01: location + intent demo

INTENTS = [("buy", "Buy"), ("sell", "Sell"), ("invest", "Invest")]
AREA = '<span data-mirror-out="area" class="svc-cap"></span>'
INTENT_AD = {
    "buy": ("Homes for sale in ", "Listings and projects in the area you want, with one easy way to enquire.", ["View listings", "Book a visit", "Call the agent"]),
    "sell": ("Selling your home in ", "A local agent who knows your market, and a simple way to ask for a valuation.", ["Request a valuation", "How it works", "Call the agent"]),
    "invest": ("Investment property in ", "Projects and plots for buyers who want to invest, explained clearly.", ["See projects", "Download details", "Call the agent"]),
}


def intent_panel(k):
    head, text, links = INTENT_AD[k]
    return ('<div class="mt-4 rounded-2xl border border-orange/30 bg-orange/5 p-4"><p class="text-[11px] font-bold text-ink">Sponsored</p>'
            '<p class="text-[11px] text-muted">yourbusiness.com</p>'
            f'<p class="svc-serp-title mt-1 text-base font-bold leading-snug">{E(head)}{AREA} | Your Agency</p>'
            f'<p class="mt-1 text-xs text-body">{E(text)}</p>'
            '<div class="mt-3 flex flex-wrap gap-2 text-[11px] font-semibold text-orange">' + "".join(f"<span>{E(x)}</span>" for x in links) + "</div></div>")


target_demo = '<div data-tabs="true">' + figure("Right place, right moment", ["Example", "Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type the area you serve</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("target", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="area" placeholder="your city" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Area to preview"/></span></label>'
    '<p class="mt-4 text-[10px] font-bold uppercase tracking-wider text-muted">What are they looking to do?</p>'
    '<div class="mt-2 flex flex-wrap gap-1 rounded-2xl border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{lab}</button>'
        for i, (k, lab) in enumerate(INTENTS)) + "</div>"
    + "".join(f'<div data-panel="{k}"{HID if i else ""}>{intent_panel(k)}</div>' for i, (k, _) in enumerate(INTENTS))
    + '<p class="mt-4 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
    f'{svg("users", "h-4 w-4 shrink-0 text-orange")}Shown to people in your area who are ready to buy, sell or invest.</p>')) + "</div>"

# --------------------------------------------------- 03: what I do (tabs)

TYPES = [
    {"key": "gads", "name": "Google Ads for property", "icon": "search",
     "what": "I run ads that show your properties and services at the top of Google when people search to buy, sell or invest.",
     "mock": figure("Search ad", ["Example"], search_ad("yourbusiness.com", "Apartments In Your Area | Your Agency", "Your listings and projects, why buyers choose you and one easy way to enquire.", ["View listings", "Book a site visit", "Call us"]))},
    {"key": "meta", "name": "Meta Ads for real estate", "icon": "image",
     "what": "Facebook and Instagram are perfect for property, because I can target the right people with strong visuals of your listings and projects.",
     "mock": figure("Facebook and Instagram ad", ["Example"], social_ad("Your Agency", "Your project, shown beautifully", "Strong visuals of your listings, shown to the right people", "Enquire now"))},
    {"key": "local", "name": "Local SEO and Google Business Profile", "icon": "target",
     "what": "I help you rank in your local area so buyers and sellers nearby find you for free.",
     "mock": figure("Local pack", ["Example"], map_area() + place_rows("Your Agency", "Real estate agent · Near you", "Another agency"))},
    {"key": "landing", "name": "High converting landing pages", "icon": "file",
     "what": "I build focused pages for your projects and listings that turn clicks into real enquiries.",
     "mock": figure("Project landing page", ["Example"], landing("Your project, in one clear page", "Location, layouts and what makes it worth a visit, with one clear next step.", ["Your name", "Phone number", "Looking to buy, sell or invest"], "Request details"))},
    {"key": "crm", "name": "Lead capture and CRM connect", "icon": "layers",
     "what": "I connect your leads straight into your CRM or system, so no enquiry is lost and follow up is easy.",
     "mock": figure("From enquiry to follow up", ["Example"], steps(["Someone enquires from an ad or page", "The lead lands in your CRM instantly", "The right agent is told straight away", "Follow up happens fast, nothing is lost"]))},
    {"key": "retarget", "name": "Retargeting", "icon": "repeat",
     "what": "I bring back people who viewed your properties but did not enquire, which is one of the cheapest ways to win more deals.",
     "mock": figure("Retargeting", ["Example"], steps(["Someone views your listing", "They leave without enquiring", "They see your property again on Facebook, Instagram and Google", "They come back and enquire"]))},
]

# --------------------------------------------------- 04: quality, not just numbers

QUALITY = [
    ("Many of our leads never pick up or are not serious", "A flood of cheap leads wastes your time and your money."),
    ("Our ads reach anyone, not people in our areas", "Tight targeting by location and intent is what brings serious buyers and sellers."),
    ("Our ads send people to a busy website, not a project page", "A focused page for each project or listing turns clicks into real enquiries."),
    ("Leads sit in an inbox or spreadsheet before anyone calls", "Fast follow up is often the difference between a deal and a dead lead."),
    ("We never bring back people who viewed our listings", "Retargeting is one of the cheapest ways to win more deals."),
]
quality_box = L.leak_check(
    "Lead quality check", "Tick everything that sounds like your lead flow today.", QUALITY,
    ("Nothing ticked. A free call still checks the parts that are hard to see from the inside.",
     "A gap or two. These are the first things I fix, so more of your leads are worth your time.",
     "You are very likely paying for time wasters. Fixing these is how serious enquiries start to come through."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "target", "h3": "Strategy for your market", "p": "A plan built around your properties, your areas and your ideal buyers and sellers, so we target the right leads."},
    {"icon": "search", "h3": "Google and Meta Ads", "p": "Ads at the top of Google when people search to buy, sell or invest, and strong visuals of your listings on Facebook and Instagram."},
    {"icon": "gauge", "h3": "Local SEO", "p": "Your business ranking in your local area, so buyers and sellers nearby find you for free."},
    {"icon": "file", "h3": "High converting landing pages", "p": "Focused pages for your projects and listings that turn clicks into real enquiries."},
    {"icon": "layers", "h3": "Lead capture, CRM connection and retargeting", "p": "Every lead straight into your CRM so none is lost, and retargeting that brings back people who viewed your properties."},
    {"icon": "chart", "h3": "Clear reports", "p": "Reports on leads, lead quality and cost per lead in plain language."},
]

FAQ = [
    ("How do you get me real estate leads?", "I use Google Ads, Meta Ads and local SEO to reach people looking to buy, sell or invest, then use landing pages and qualification to turn them into serious enquiries."),
    ("Which channels work best for real estate?", "Google Ads and Meta Ads usually work best, with local SEO adding free reach. Meta is especially strong because property is visual and its targeting is powerful."),
    ("Are the leads quality or just time wasters?", "My focus is quality. I use tight targeting and qualification so the leads that reach you are serious buyers and sellers, not a flood of curious clicks."),
    ("How much should I spend on marketing?", "It depends on your market, your price points and your goals. On our call I will suggest a realistic budget so you get quality leads without overspending."),
    ("How soon will I see leads?", "Google and Meta Ads can bring enquiries within days, while SEO builds over a couple of months. Together they give you both fast and lasting results."),
    ("Do you do real estate SEO or ads?", "Both. I combine paid ads with local SEO because together they bring more and better leads than either one alone, and I balance them to fit your budget."),
    ("Can you promote a specific project or apartment?", "Yes. I can build focused campaigns and landing pages for a single project, launch or listing, which works very well for developers."),
    ("Do you build landing pages for my listings?", "Yes. I build focused landing pages for your projects and listings that turn clicks into real enquiries, instead of sending traffic to a busy website."),
    ("Can you connect leads to my CRM?", "Yes. I connect your leads straight into your CRM or system, so no enquiry is lost and your team can follow up quickly."),
    ("How do you handle lead follow up?", "I make sure leads flow into your CRM instantly and can set up automated follow up, since fast follow up is often the difference between a deal and a dead lead."),
    ("Do you work with developers?", "Yes. I work with developers and builders to promote projects and launches, and I can scale campaigns up during key sales periods."),
    ("Can you retarget interested buyers?", "Yes. Retargeting brings back people who viewed your properties but did not enquire, which is one of the cheapest ways to win more deals."),
    ("What will my cost per lead be?", "It varies by market and property type, but my goal is always to lower it over time while keeping lead quality high. I track it closely so you see the real return."),
    ("What reports will I get?", "You get clear monthly reports showing leads, lead quality and cost per lead, plus updates on the work done."),
    ("How do I get started?", "Just book a free real estate marketing call using the button on this page. I will look at your market and show you how to get quality leads."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("Local SEO", "/services/local-seo/"),
    ("Landing pages", "/services/landing-pages/"),
    ("Remarketing", "/services/remarketing/"),
    ("CRM consulting", "/services/crm-consulting/"),
]

PAGE = {
    "path": "/industries/real-estate/",
    "slug": "real-estate-marketing",
    "form_name": "real_estate_marketing",
    "service": "Real Estate Marketing",
    "service_name": "Real estate marketing services",
    "thanks_what": "real estate marketing call",
    "category": "Lead generation for real estate",
    "service_desc": "Real estate lead generation for agents, brokers and developers: Google Ads, Meta Ads, local SEO, high converting landing pages, lead capture and CRM connection, retargeting and clear reports.",
    "audience": "Real estate agents, brokers and developers",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What real estate marketing includes",
    "offers": GET,
    "title": "Real Estate Lead Generation Services | Sushant Rana",
    "og_title": "Real Estate Lead Generation Services",
    "og_alt": "Real estate lead generation services by Sushant Rana",
    "desc": "Real estate lead generation services for agents and developers: quality buyer and seller leads from Google Ads, Meta Ads, local SEO and landing pages.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Industries", "/industries/"), ("Real Estate", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about real estate marketing"),
            "body": ["Channels, lead quality, budgets and follow up. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Real estate lead generation",
        "h1": ("Real estate marketing that brings you", "ready buyers and sellers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help real estate agents, brokers and developers get a steady flow of quality buyer and seller leads using Google Ads, Meta Ads, local SEO and landing pages that actually convert. Are you tired of chasing cold leads or paying for enquiries that never turn into deals?',
            "In real estate, the deal usually goes to whoever the buyer or seller finds and trusts first. We make sure that is you, with marketing that brings serious leads to your pipeline, not just curious clickers.",
        ],
        "cta2": ("Check your lead quality", "#quality"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free real estate marketing call",
        "sub": "Tell me about your market and I will show you how to bring in quality buyer and seller leads.",
        "submit": "Request my free marketing call",
        "company_label": "Agency / company name",
        "steps": [
            {"label": "Business", "fields": [
                {"type": "radio", "name": "business_type", "label": "What best describes you?", "req": True,
                 "options": ["Agent or realtor", "Broker or agency", "Developer or builder", "Other"]},
                {"type": "checkbox", "name": "leads", "label": "Leads you want more of",
                 "options": ["Buyers", "Sellers", "Investors", "A project launch", "Commercial spaces"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "budget", "label": "Monthly marketing budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "checkbox", "name": "channels", "label": "What you are interested in",
                 "options": ["Google Ads", "Meta Ads", "Local SEO", "Landing pages", "CRM and follow up", "Retargeting", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your areas, your projects or listings, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads for property", "Meta Ads", "Local SEO", "Project landing pages", "Lead capture", "CRM connect", "Retargeting"]),
    L.split({"id": "problem", "pill": "The problem", "h2": ("Why good agents still struggle", "for quality leads"),
             "body": ["Many agents and developers have great properties but still fight for good leads. They rely on referrals and old contacts, or they buy cheap leads that turn out to be time wasters.",
                      "Today, almost every buyer and seller starts online. They search, browse and compare before they ever call. If your marketing is not reaching them at the right moment with the right message, you lose them to another agent. I fix this by putting you in front of serious buyers and sellers when they are ready to act."],
             "bullets": ["Buyers and sellers start online", "The right message at the right moment", "Serious leads, ready to act"],
             "cta": CTA, "visual": target_demo}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why online marketing works", "so well for real estate"),
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Buyers and sellers search online first", "p": "People look for property and agents online before doing anything else. Showing up there puts you in front of ready to act leads."},
                          {"icon": "target", "h3": "You can target by location and intent", "p": "I reach people in the exact areas you serve who are actively looking to buy, sell or invest, so your budget is not wasted."},
                          {"icon": "shield", "h3": "You get quality, not just quantity", "p": "The goal is serious leads, not a pile of curious clicks. Good targeting and qualification bring you people who are ready to talk business."},
                          {"icon": "repeat", "h3": "It builds a predictable pipeline", "p": "Instead of feast and famine, steady marketing gives you a reliable flow of enquiries you can count on every month."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("How I bring you", "more property leads"),
                           "body": ["Six pieces that work together, from the first search to the follow up call. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.split({"id": "quality", "anchor": "quality", "pill": "The difference", "h2": ("Why I focus on quality leads,", "not just numbers"),
             "body": ["It is easy to generate a lot of cheap leads that never turn into deals. That just wastes your time and your money. The real goal is serious buyers and sellers who are ready to talk.",
                      "So I focus on quality. I use tight targeting and smart qualification so the leads that reach you are the ones worth your time. A smaller number of serious enquiries will always beat a flood of time wasters, and that is what I aim for."],
             "bullets": ["Tight targeting by area and intent", "Smart qualification before the lead reaches you", "Serious enquiries over a flood of time wasters"],
             "visual": quality_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the wrong numbers and the people who were only curious.",
                        "So we connect your ads to your CRM. Each enquiry is saved with the ad it came from, your team marks which leads were serious and which booked a site visit, and those leads flow back into Google Ads as conversions. From then on the platform goes after serious buyers and sellers, not just forms."],
                  bullets=["Ad click saved with every enquiry", "Your team marks serious leads and site visits in the CRM", "Qualified leads sent back to Google Ads", "Reports on cost per qualified lead"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My real estate marketing", "process"),
                   "body": ["A clear process, not luck. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Discovery and goals", "short": "Discovery", "p": "I learn about your properties, your areas and your ideal buyers and sellers, so we target the right leads.", "points": ["Your properties and areas", "Your ideal buyers and sellers", "Your goals"]},
                       {"h3": "Strategy", "short": "Strategy", "p": "I plan the right mix of ads, SEO and pages for your market and your budget.", "points": ["Ads, SEO and pages", "Planned for your market", "Planned for your budget"]},
                       {"h3": "Setup", "short": "Setup", "p": "I build your campaigns, landing pages and lead capture, and connect everything to your CRM.", "points": ["Campaigns and landing pages", "Lead capture", "Connected to your CRM"]},
                       {"h3": "Optimize", "short": "Optimize", "p": "I improve your results every week, lowering your cost per lead and raising lead quality.", "points": ["Weekly improvements", "Lower cost per lead", "Higher lead quality"]},
                       {"h3": "Report", "short": "Report", "p": "I send clear reports showing leads, quality and cost per lead in plain language.", "points": ["Leads and quality", "Cost per lead", "Plain language"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included", "when you work with me"),
                  "body": ["You get a complete, done for you lead generation system for your real estate business. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free marketing call", "h3": "Want a steady flow of serious property leads?",
                                       "p": "Let me look at your market and your goals and show you how we can bring you quality buyer and seller leads. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why real estate businesses", "choose me"),
                  "body": ["You talk to the person running your marketing, and every report is about lead quality and cost per lead."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person running your marketing, with clear answers and fast replies."},
                      {"h3": "Focus on serious leads", "p": "I care about quality enquiries and closed deals, not just clicks and vanity numbers."},
                      {"h3": "Honest reporting", "p": "I report on leads, quality and cost per lead in plain language, so you always know your return."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Real estate businesses", "I work with"),
                     "body": "I help individual agents and realtors, brokers and agencies, property developers and builders, and teams selling apartments, plots or commercial spaces. Whether you sell one project or many, I can bring you quality leads.",
                     "chips": [("Agents and realtors", None), ("Brokers and agencies", None), ("Developers and builders", None), ("Apartments", None), ("Plots", None),
                               ("Commercial spaces", None), ("Local businesses", "/industries/local-businesses/")]}),
    L.chips_section({"id": "related", "h2": ("Services behind", "your real estate marketing"),
                     "body": "The channels, pages and follow up that bring serious leads in, each with its own page if you want the detail.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to fill your pipeline", "with quality leads?"),
               "p": "Let us talk about your market and your goals and build a marketing plan that brings you serious buyers and sellers every month.",
               "btn": CTA, "note": "No obligation · Free marketing call"}),
]
