# Auto Repair Marketing Services (industry page). Copy: 21_Auto_Repair_Marketing_Services.docx
# No client work: none of the published clients is an auto repair shop.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free auto repair marketing call"

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



# --------------------------------------------------- 01: urgent search demo (pick a problem)

PROBLEMS = [("brakes", "Brakes", "brake repair near me"), ("tyres", "Tyres", "tyre shop near me"),
            ("battery", "Battery", "car battery replacement near me"), ("light", "Warning light", "check engine light near me")]
prob_btns = "".join(
    f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
    f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{E(lab)}</button>'
    for i, (k, lab, _) in enumerate(PROBLEMS))
HID = ' hidden=""'
prob_panels = "".join(
    f'<div data-panel="{k}"{HID if i else ""}><p class="mt-4 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 text-sm text-ink">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}{E(q)}</p>'
    + place_rows("Your Shop", "Open now · Near you", "Another shop") + "</div>"
    for i, (k, _, q) in enumerate(PROBLEMS))
urgent_demo = '<div data-tabs="true">' + figure("When the car breaks down", ["Example"], (
    '<p class="text-[10px] font-bold uppercase tracking-wider text-muted">Pick what went wrong</p>'
    f'<div class="mt-2 flex flex-wrap gap-1 rounded-2xl border border-[var(--color-line)] bg-white p-1">{prob_btns}</div>{prob_panels}'
    '<p class="mt-4 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
    f'{svg("phone", "h-4 w-4 shrink-0 text-orange")}The driver calls one of the top results. That should be your shop.</p>')) + "</div>"

# --------------------------------------------------- 03: what I do (tabs)

TYPES = [
    {"key": "gads", "name": "Google Ads for auto repair", "icon": "search",
     "what": "I run ads that put your shop at the top of Google exactly when drivers search for a repair near them.",
     "mock": figure("Search ad", ["Example"], search_ad("yourshop.com", "Car Repair Near You | Your Shop", "The jobs you do, the reason to choose you and one tap to call.", ["Call the shop", "Our services", "Directions"]))},
    {"key": "local", "name": "Local SEO and Google Business Profile", "icon": "target",
     "what": "I get your shop ranking on Google Maps and in the local pack, so nearby drivers find you for free.",
     "mock": figure("Local pack", ["Example"], map_area() + place_rows("Your Shop", "Auto repair · Near you", "Another shop"))},
    {"key": "meta", "name": "Meta Ads for offers and awareness", "icon": "users",
     "what": "I run Facebook and Instagram ads to promote your services and offers to local drivers.",
     "mock": figure("Facebook and Instagram ad", ["Example"], social_ad("Your Shop", "Your service offer", "Shown to drivers who live near your shop", "Call now"))},
    {"key": "landing", "name": "High converting landing pages", "icon": "file",
     "what": "I build pages that turn your ad clicks into calls and booked jobs, instead of wasting your budget.",
     "mock": figure("Landing page", ["Example"], landing("Your service, done right and nearby", "What you fix, why drivers trust you, and one clear next step.", ["Your name", "Phone number", "Car and problem"], "Request a callback"))},
    {"key": "reviews", "name": "Reviews and reputation", "icon": "shield",
     "what": "I help you get more five star reviews and manage your reputation, which drivers rely on when choosing a shop.",
     "mock": figure("Customer reviews", ["Example"], reviews("Customer") + '<p class="mt-3 text-xs text-body">Genuine reviews from real customers, managed and answered.</p>')},
    {"key": "tracking", "name": "Call tracking", "icon": "phone",
     "what": "I track every call so we know exactly which marketing is bringing cars into your bays.",
     "mock": figure("Where the calls came from", ["Example"], tracking(
         [("Google Ads", "Phone call", "Job booked", True), ("Google Maps", "Phone call", "Job booked", True), ("Meta Ads", "Form enquiry", "Enquiry", False), ("Landing page", "Callback request", "Job booked", True)],
         "Every call matched to the marketing that brought the car in."))},
]

# --------------------------------------------------- 04: the advantage, as a self check

CHECKS = [
    ("We do not show up when drivers search for a repair near them", "A driver with car trouble calls one of the top results, fast."),
    ("We are not in the Google Maps results", "Ranking in the map results is one of the best ways to win local repair jobs."),
    ("Our reviews are few or out of date", "Drivers rely heavily on reviews when choosing a shop they can trust."),
    ("Our ads send drivers to the home page", "A focused page turns the click into a call or a booked job."),
    ("We cannot tell which calls came from which marketing", "Without call tracking you cannot see what brings cars into your bays."),
]
check_box = L.leak_check(
    "Local search check", "Tick everything that sounds like your shop today.", CHECKS,
    ("Nothing ticked. A free call still checks the parts that are hard to see from the inside.",
     "A gap or two. These are the first things I fix, so the urgent calls start coming to you.",
     "Urgent jobs are very likely going to the shop down the road. This is where your bays start to fill."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "target", "h3": "Strategy for your shop", "p": "A plan built around your services, your area and your budget, focused on the jobs you want most."},
    {"icon": "search", "h3": "Google and Meta Ads", "p": "Ads that put your shop at the top of Google when drivers search for a repair, and promote your services and offers to local drivers."},
    {"icon": "gauge", "h3": "Local SEO and Google Business Profile", "p": "Your shop ranking on Google Maps and in the local pack, so nearby drivers find you for free."},
    {"icon": "file", "h3": "Landing pages", "p": "Pages that turn your ad clicks into calls and booked jobs, instead of wasting your budget."},
    {"icon": "shield", "h3": "Review and reputation help", "p": "More genuine five star reviews and a reputation you manage, because drivers rely on it."},
    {"icon": "phone", "h3": "Call tracking and clear reports", "p": "Every call tracked, with clear reports on calls, jobs and cost per customer in plain language."},
]

FAQ = [
    ("How do you get more customers for my shop?", "I use Google Ads and local SEO to put your shop at the top when drivers search for a repair near them, then turn those clicks and calls into booked jobs."),
    ("Which channels work best for auto repair?", "Google Ads and local SEO work best, because they reach drivers who need a repair right now. Meta Ads and reviews add strong support."),
    ("How much should I spend on marketing?", "It depends on your area, competition and goals. On our call I will suggest a realistic budget for your market so you get results without overspending."),
    ("How soon will I see results?", "Google Ads can bring calls within days, while local SEO builds over a couple of months. Together they give you both fast and lasting results."),
    ("Do you do local SEO for auto shops?", "Yes. I optimize your Google Business Profile and local SEO so your shop ranks on Google Maps when nearby drivers search."),
    ("Can you get me on Google Maps?", "Yes. Ranking in the map results is one of the best ways to win local repair jobs, and it is a core part of what I do for auto shops."),
    ("How do you track calls?", "I set up call tracking so we can see exactly which ads and searches are bringing cars into your bays, and improve from there."),
    ("Can you fill my slow days?", "Yes. Steady marketing keeps a flow of customers coming in, which helps smooth out the quiet periods that used to hurt your income."),
    ("Do you build landing pages for my shop?", "Yes. I build focused pages that turn your ad clicks into calls and booked jobs, which lowers your cost per customer."),
    ("How do reviews help my shop?", "Drivers rely heavily on reviews when choosing a shop. I help you get more genuine five star reviews and manage your reputation."),
    ("Do you work with multiple locations?", "Yes. I can run marketing for shops with several locations, setting up profiles and campaigns for each one."),
    ("Can you help a new shop?", "Yes. For a new shop, ads and local SEO are one of the fastest ways to get known and start bringing in cars."),
    ("What services can you promote?", "I can promote any of your services, from general repair and tyres to brakes, servicing and specialty work, and focus on the jobs you want most."),
    ("What reports will I get?", "You get clear monthly reports showing calls, jobs and cost per customer, plus updates on the work done."),
    ("How do I get started?", "Just book a free auto repair marketing call using the button on this page. I will look at your shop and show you how to bring in more customers."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Local SEO", "/services/local-seo/"),
    ("Google Business Profile", "/services/google-business-profile/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("Landing pages", "/services/landing-pages/"),
    ("Lead generation", "/services/lead-generation/"),
]

PAGE = {
    "path": "/industries/auto-repair/",
    "slug": "auto-repair-marketing",
    "form_name": "auto_repair_marketing",
    "service": "Auto Repair Marketing",
    "service_name": "Auto repair marketing services",
    "thanks_what": "auto repair marketing call",
    "category": "Digital marketing for auto repair shops",
    "service_desc": "Auto repair marketing for shops and garages: Google Ads, local SEO and Google Business Profile, Meta Ads, landing pages, review and reputation help, call tracking and clear reports.",
    "audience": "Auto repair shops and garages",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What auto repair marketing includes",
    "offers": GET,
    "title": "Auto Repair Marketing Services for More Cars | Sushant Rana",
    "og_title": "Auto Repair Marketing Services for More Cars",
    "og_alt": "Auto repair marketing services by Sushant Rana",
    "desc": "Auto repair marketing services that keep your bays full. Google Ads and local SEO that turn local searches into booked jobs. Book a free marketing call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Industries", "/industries/"), ("Auto Repair", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about auto repair marketing"),
            "body": ["Channels, budgets, timelines and tracking. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Auto repair marketing services",
        "h1": ("Auto repair marketing that", "keeps your bays full"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help auto repair shops get a steady flow of local customers using Google Ads and local SEO that put you at the top when drivers need help. Do you run a great repair shop but still have slow days with empty bays? The best mechanics do not always get the most cars, the most visible ones do.',
            "When a car has a problem, the driver searches for a shop near them and calls one of the first they see. We make sure that shop is yours, so your bays stay full and your slow days disappear.",
        ],
        "cta2": ("See why it works", "#advantage"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free auto repair marketing call",
        "sub": "Tell me about your shop and I will show you how to bring in more local customers.",
        "submit": "Request my free marketing call",
        "company_label": "Shop / garage name",
        "steps": [
            {"label": "Shop", "fields": [
                {"type": "radio", "name": "running", "label": "Are you running ads for your shop now?", "req": True,
                 "options": ["Yes, running now", "Paused or stopped", "Never run them"]},
                {"type": "checkbox", "name": "jobs", "label": "Jobs you want more of",
                 "options": ["General repair", "Tyres and wheels", "Brakes", "Servicing and oil change", "Body and collision", "Specialty work"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourshop.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "budget", "label": "Monthly marketing budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "checkbox", "name": "channels", "label": "What you are interested in",
                 "options": ["Google Ads", "Local SEO and Maps", "Meta Ads", "Landing pages", "Reviews", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your shop, your area, how many locations, which days are slow..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads for auto repair", "Local SEO", "Google Maps", "Google Business Profile", "Meta Ads", "Landing pages", "Reviews", "Call tracking"]),
    L.split({"id": "problem", "pill": "The problem", "h2": ("Why good shops", "still have slow days"),
             "body": ["Plenty of skilled shops sit with empty bays while a competitor down the road is busy. Usually the difference is not the work, it is who shows up first when a driver searches for help.",
                      "Car trouble is urgent. When something goes wrong, the driver grabs their phone, searches for a repair shop near them and calls one of the top results. If you are not showing up there, you are handing those customers to the shop that is."],
             "bullets": ["Drivers search the moment something goes wrong", "They call one of the top results", "Your shop put at the top when they search"],
             "cta": CTA, "visual": urgent_demo}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why online marketing works", "so well for auto shops"),
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Drivers search when they need you", "p": "People look for a repair shop near them the moment they have a problem. Showing up there puts you in front of ready to book customers."},
                          {"icon": "users", "h3": "Local competition is tough", "p": "Many shops compete for the same drivers. Good marketing makes sure you are the one they call, not the one they scroll past."},
                          {"icon": "target", "h3": "It brings ready customers", "p": "Ads and local SEO reach people who need a repair right now, which means high intent customers, not tyre kickers."},
                          {"icon": "repeat", "h3": "It fills your slow days", "p": "With steady marketing, you can keep your bays busy even during the quiet periods that used to hurt your income."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("How I bring you", "more customers"),
                           "body": ["Six pieces that work together, from the urgent search to the booked job. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.split({"id": "advantage", "anchor": "advantage", "pill": "The advantage", "h2": ("Why being top of local search", "wins the job"),
             "body": ["Auto repair is different from most businesses because the need is urgent. A driver with a problem is not going to research for days, they call fast and go with a shop they can trust that is close by.",
                      "This is a huge advantage for you if you show up first. By putting your shop at the top of local search and backing it with strong reviews, I help you win the job before your competitors even get a look. Speed and visibility are everything in this business, and I give you both."],
             "bullets": ["Top of local search when the need is urgent", "Strong reviews that earn trust fast", "Close by, easy to call"],
             "visual": check_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a call or a form fill, it goes and finds you more of those, including wrong numbers and people who were only asking around.",
                        "So we connect your ads to your CRM. Each call and enquiry is saved with the ad it came from, your service desk marks which ones became booked jobs, and those jobs flow back into Google Ads as conversions. From then on the platform goes after drivers who book, not just callers."],
                  bullets=["Ad click saved with every call and enquiry", "Service desk marks booked jobs in the CRM", "Booked jobs sent back to Google Ads", "Reports on cost per booked job"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My auto repair marketing", "process"),
                   "body": ["A clear process, not luck. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Shop audit and goals", "short": "Audit", "p": "I learn about your shop, your services and your goals, so we focus on the jobs you want most.", "points": ["Your shop and services", "The jobs you want most", "Your goals"]},
                       {"h3": "Strategy", "short": "Strategy", "p": "I plan the right mix of ads and local SEO for your area and your budget.", "points": ["Ads and local SEO", "Planned for your area", "Planned for your budget"]},
                       {"h3": "Setup", "short": "Setup", "p": "I build your campaigns, profile and landing pages and set up call tracking.", "points": ["Campaigns and profile", "Landing pages", "Call tracking"]},
                       {"h3": "Optimize", "short": "Optimize", "p": "I improve your results every week, lowering your cost per customer and bringing in more jobs.", "points": ["Weekly improvements", "Lower cost per customer", "More jobs"]},
                       {"h3": "Report", "short": "Report", "p": "I send you clear reports showing calls, jobs and cost per customer in plain language.", "points": ["Calls and jobs", "Cost per customer", "Plain language"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included", "when you work with me"),
                  "body": ["You get a complete, done for you customer generation system for your shop. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free marketing call", "h3": "Want to keep your bays full all week?",
                                       "p": "Let me look at your shop and your area and show you exactly how we can bring you more local customers. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why auto shops", "choose me"),
                  "body": ["You talk to the person running your marketing, and every report is about calls, jobs and cost per customer."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person running your marketing, with clear answers and fast replies."},
                      {"h3": "Focus on booked jobs", "p": "I care about actual calls and jobs and your cost per customer, not clicks and vanity numbers."},
                      {"h3": "Honest reporting", "p": "I report on calls, jobs and cost per customer in plain language, so you always know your return."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Auto shops", "I work with"),
                     "body": "I help general repair shops, tyre and wheel shops, body and collision shops, oil change and quick service centres, and specialty and multi location garages. Whatever you fix, I can bring you more of the right customers.",
                     "chips": [("General repair shops", None), ("Tyre and wheel shops", None), ("Body and collision shops", None), ("Oil change and quick service", None),
                               ("Specialty and multi location garages", None), ("Automobile", "/industries/automobile/"), ("Local businesses", "/industries/local-businesses/")]}),
    L.chips_section({"id": "related", "h2": ("Services behind", "your auto repair marketing"),
                     "body": "The channels and pages that bring cars in, each with its own page if you want the detail.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to fill", "your bays?"),
               "p": "Let us talk about your shop and your area and build a marketing plan that keeps a steady flow of customers coming through your doors.",
               "btn": CTA, "note": "No obligation · Free marketing call"}),
]
