# Local SEO Services. Copy: 08_Local_SEO_Services.txt
# Mocks are illustrations tagged "Example": placeholders only, no figures.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free local SEO audit"

# lucide map-pin and star, local to this page
L.ICON.update({
    "pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path><circle cx="12" cy="10" r="3"></circle>',
    "star": '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path>',
})

TAG_ON = "shrink-0 rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange"
TAG_OFF = "shrink-0 rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted"
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"


def rows(items):
    """[(title, sub, tag, on)] as a list of white rows with a status tag."""
    return '<ul class="grid list-none gap-2.5">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid min-w-0"><span class="text-sm font-bold text-ink">{E(a)}</span><span class="text-xs text-muted">{E(b)}</span></span>'
        f'<span class="{TAG_ON if on else TAG_OFF}">{E(t)}</span></li>' for a, b, t, on in items) + "</ul>"


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}{E(text)}</p>')


def numbered(items):
    return '<ol class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
        f'<span class="text-sm font-semibold text-ink">{E(t)}</span></li>' for i, t in enumerate(items, 1)) + "</ol>"


def stars(cls="h-3.5 w-3.5"):
    return '<span class="flex gap-0.5 text-orange">' + svg("star", cls) * 5 + "</span>"


GHOST = ('<div class="rounded-2xl border border-[var(--color-line)] p-3.5 opacity-60" aria-hidden="true"><span class="block h-3 rounded-full bg-ink/15" style="width:55%"></span>'
         '<span class="mt-2 block h-2 rounded-full bg-ink/10" style="width:80%"></span></div>')

# --------------------------------------------------- live map pack demo

MIRROR_IN = "min-w-0 w-full rounded-xl border border-[var(--color-line)] bg-white px-3 py-2 text-sm text-ink outline-none transition focus:border-orange"
PINS = [(22, 30, False), (68, 22, False), (46, 58, True), (80, 64, False)]
pins = "".join(
    f'<span class="absolute -translate-x-1/2 {"text-orange" if on else "text-muted opacity-30"}" style="left:{x}%;top:{y}%">{svg("pin", "h-8 w-8" if on else "h-5 w-5")}</span>'
    for x, y, on in PINS)
roads = "".join(f'<span class="absolute inset-x-0 h-px bg-ink/10" style="top:{t}%"></span>' for t in (25, 52, 78)) + "".join(
    f'<span class="absolute top-0 bottom-0 bg-ink/10" style="left:{lft}%;width:1px"></span>' for lft in (30, 62))

mappack = figure("Google Maps search", ["Live demo"], (
    '<div class="grid gap-3 sm:grid-cols-2">'
    f'<label class="block"><span class="{CAP}">Your service</span><input data-mirror="svc" placeholder="dentist" class="mt-1.5 {MIRROR_IN}" aria-label="Your service"/></label>'
    f'<label class="block"><span class="{CAP}">Your city</span><input data-mirror="city" placeholder="your city" class="mt-1.5 {MIRROR_IN}" aria-label="Your city"/></label></div>'
    '<p class="mt-4 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 text-sm text-ink">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<span class="truncate"><span data-mirror-out="svc"></span> in <span data-mirror-out="city" class="svc-cap"></span></span></p>'
    f'<div class="relative mt-4 h-44 overflow-hidden rounded-2xl bg-[#fff7f3]" aria-hidden="true">{roads}{pins}</div>'
    f'<p class="mt-4 {CAP}">Top three on the map</p><div class="mt-2.5 grid gap-2.5">'
    '<div class="rounded-2xl border border-orange/30 bg-orange/5 p-3.5"><div class="flex items-start justify-between gap-3"><div class="min-w-0">'
    '<p class="text-sm font-extrabold text-ink">Your Business</p><p class="truncate text-xs text-muted"><span data-mirror-out="svc" class="svc-cap"></span> · <span data-mirror-out="city" class="svc-cap"></span></p></div>'
    f'{svg("pin", "h-5 w-5 shrink-0 text-orange")}</div><div class="mt-2.5 flex flex-wrap gap-2">'
    + "".join(f'<span class="rounded-full border border-[var(--color-line)] bg-white px-3 py-1 text-[11px] font-bold text-ink">{t}</span>' for t in ("Call", "Directions", "Website"))
    + f'</div></div>{GHOST * 2}</div>'
    + note("The top three on the map get a large share of the clicks and calls.", "pin")
))

# --------------------------------------------------- "what I do" mocks

MOCKS = {
    "gbp": figure("Google Business Profile", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4"><div class="flex items-start justify-between gap-3"><div>'
        '<p class="text-base font-extrabold text-ink">Your Business</p><p class="text-xs text-muted">Your main category · Your area</p>'
        f'<p class="mt-1 text-xs font-semibold text-orange">Open now</p></div><span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg("pin", "h-5 w-5")}</span></div>'
        '<div class="mt-3 grid grid-cols-3 gap-2">' + "".join(
            f'<span class="rounded-full border border-[var(--color-line)] py-1.5 text-center text-[11px] font-bold text-ink">{t}</span>' for t in ("Call", "Directions", "Website"))
        + '</div><div class="mt-3 grid grid-cols-4 gap-2" aria-hidden="true">'
        + f'<span class="grid aspect-square place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg("image", "h-5 w-5")}</span>' * 4
        + '</div></div><div class="mt-4 flex flex-wrap gap-2">' + "".join(
            f'<span class="inline-flex items-center gap-1.5 rounded-full bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{svg("check", "h-3 w-3", 3)}{t}</span>'
            for t in ("Categories", "Services", "Photos", "Posts", "Details"))
        + "</div>")),
    "keywords": figure("Local searches, mapped", ["Example"], rows([
        ("“your service near me”", "Profile and main service page", "Mapped", True),
        ("“your service in your city”", "City service page", "Mapped", True),
        ("“your service open now”", "Profile hours and services", "Mapped", True),
    ]) + note("Your website and profile shaped around the searches your customers use.", "search")),
    "citations": figure("Name, address, phone check", ["Example"], rows([
        ("Google Business Profile", "Your Business · your address · your phone", "Matches", True),
        ("Directory one", "Your Business · your address · your phone", "Matches", True),
        ("Directory two", "Old phone number", "Fixed", True),
        ("Directory three", "Not listed", "Added", True),
    ]) + note("Same name, address and phone number everywhere.", "check")),
    "reviews": figure("Review flow", ["Example"], numbered([
        "The job is done or the visit is over", "A review link goes to the customer", "They leave a genuine review", "You reply, and it shows on your profile",
    ]) + '<div class="mt-4 rounded-2xl border border-[var(--color-line)] p-4">' + stars()
        + '<span class="mt-2 block h-2 rounded-full bg-ink/10" aria-hidden="true"></span><span class="mt-2 block h-2 rounded-full bg-ink/10" style="width:70%" aria-hidden="true"></span>'
        '<p class="mt-3 rounded-xl bg-[#fff7f3] px-3 py-2 text-xs text-body"><strong class="font-semibold text-ink">Reply from the owner.</strong> Thank you for the kind words.</p></div>'),
    "onpage": figure("City service page", ["Example"], (
        '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><p class="truncate border-b border-[var(--color-line)] bg-[#fff7f3] px-4 py-2 text-[11px] text-muted">yourbusiness.com/your-service-your-city/</p>'
        '<div class="p-4"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">H1</p><p class="text-base font-extrabold text-ink">Your Service in Your City</p>'
        '<span class="mt-2 block h-2 rounded-full bg-ink/10" aria-hidden="true"></span><span class="mt-2 block h-2 rounded-full bg-ink/10" style="width:80%" aria-hidden="true"></span>'
        '<div class="mt-4 grid grid-cols-2 gap-2">' + "".join(
            f'<span class="rounded-xl border border-[var(--color-line)] px-3 py-2 text-[11px] font-semibold text-ink">{t}</span>'
            for t in ("Areas you serve", "Map and address", "Local reviews", "Call button"))
        + "</div></div></div>" + note("Google clearly connects the page to your city and your service.", "pin"))),
    "links": figure("Local links", ["Example"], (
        '<div class="grid grid-cols-3 gap-2">' + "".join(
            f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3 text-center"><span class="mx-auto grid h-9 w-9 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-4 w-4")}</span>'
            f'<p class="mt-2 text-[11px] font-bold leading-tight text-ink">{t}</p></div>'
            for ic, t in (("file", "Local news site"), ("users", "Local business group"), ("layers", "Partner business")))
        + f'</div><div class="mt-3 mb-3 flex justify-center text-orange" aria-hidden="true"><span style="transform:rotate(90deg)">{svg("chev", "h-6 w-6")}</span></div>'
        '<div class="grad-ink-orange rounded-2xl p-4 text-center"><p class="text-sm font-extrabold text-white">yourbusiness.com</p>'
        '<p class="mt-1 text-[11px] text-white/75">More authority in your area</p></div>')),
}

TYPES = [
    {"key": "gbp", "name": "Google Business Profile optimization", "icon": "pin",
     "what": "I fully optimize your Google Business Profile, the free listing that powers your place in the map results.", "best": "This is the single biggest lever in local SEO."},
    {"key": "keywords", "name": "Local keyword targeting", "icon": "search",
     "what": "I find the exact local searches your customers use and shape your website and profile around them."},
    {"key": "citations", "name": "Citations and listings", "icon": "layers",
     "what": "I list your business on trusted directories with the same name, address and phone number everywhere.", "best": "This builds trust with Google."},
    {"key": "reviews", "name": "Review strategy", "icon": "star",
     "what": "I set up a simple system to get more genuine reviews and to respond to them.", "best": "This lifts both trust and rankings."},
    {"key": "onpage", "name": "Local on-page SEO", "icon": "file",
     "what": "I optimize your website pages for your city and services, so Google clearly connects you to your area."},
    {"key": "links", "name": "Local link building", "icon": "click",
     "what": "I earn mentions and links from local and relevant sites, which strengthens your authority in your area."},
]
for t in TYPES:
    t["mock"] = MOCKS[t["key"]]

leak_box = L.leak_check(
    "Profile health check", "Tick everything that sounds like your Google Business Profile.",
    [("My profile has one category, or I am not sure it is right", "Categories decide which searches your profile can show up for."),
     ("I have not added my services and recent photos", "A thin profile gives Google and customers little reason to pick you."),
     ("I have not posted on my profile in months", "A well kept, active profile is what earns calls and visits."),
     ("My name, address or phone differs on some sites", "Details that do not match weaken the trust Google gives your listing."),
     ("I do not ask customers for reviews", "Reviews build trust with customers and help your rankings.")],
    ("Nothing ticked yet. A free audit still checks your profile, listings and map rankings in detail.",
     "A gap or two. These are usually the first things I fix on a profile.",
     "Your profile is very likely holding you back on the map. Fixing it is often the fastest way to more calls and visits."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "pin", "h3": "Google Business Profile optimization", "p": "The right categories, services, photos, posts and details, and a profile that is kept active."},
    {"icon": "search", "h3": "Local keyword research", "p": "The exact local searches your customers use, built into your website and your profile."},
    {"icon": "layers", "h3": "Citation building", "p": "Your business listed on trusted directories with the same name, address and phone number everywhere."},
    {"icon": "star", "h3": "Review strategy", "p": "A simple system to get more genuine reviews and to respond to them, which lifts trust and rankings."},
    {"icon": "file", "h3": "Local on-page SEO and content", "p": "Pages optimized for your city and services, plus helpful local content that answers what your customers search for."},
    {"icon": "chart", "h3": "Clear monthly reports", "p": "Map rankings, calls, clicks and profile activity in plain language, plus updates on the work done."},
]

FAQ = [
    ("What is local SEO?", "Local SEO is the work that helps your business show up when people search for a service near them. It focuses on Google Maps, the local pack and searches with near me in them."),
    ("How is local SEO different from normal SEO?", "Normal SEO tries to rank a website across a wide area. Local SEO focuses on your city and nearby area, and it puts a big focus on your Google Business Profile, map rankings and reviews."),
    ("What is Google Business Profile?", "Google Business Profile is the free listing that shows your business on Google Maps and in the local pack. Optimizing it is the most important part of local SEO."),
    ("How soon will I see results?", "Local SEO often shows movement within a few weeks, especially after profile and citation work. Stronger, stable results usually build over two to three months."),
    ("What is the local pack?", "The local pack is the group of top three businesses shown on the map at the top of local search results. It gets a large share of clicks and calls, so ranking there is very valuable."),
    ("What are citations and NAP?", "Citations are mentions of your business on directories and other sites. NAP means your name, address and phone number. Keeping these the same everywhere builds trust with Google."),
    ("How important are reviews for local SEO?", "Very important. Reviews build trust with customers and help your rankings. I set up a simple system to get more genuine reviews and to respond to them."),
    ("Can you rank me for near me searches?", "Yes. Near me searches are a core part of local SEO. By optimizing your profile, website and listings for your area, I help you appear for these searches."),
    ("Do you work with multi location businesses?", "Yes. I can manage local SEO for businesses with several branches, setting up and optimizing a profile and local pages for each location."),
    ("Do I need a website for local SEO?", "A website helps a lot and is recommended, but even without one, a strong Google Business Profile can bring calls and visits. I will advise on the best path for your situation."),
    ("How do you track local rankings?", "I track where you appear on the map for your key searches, along with calls and clicks from your profile, and I share this in clear reports."),
    ("Can local SEO help a service area business?", "Yes. If you travel to customers rather than having a shopfront, I can set up your profile as a service area business and target the areas you cover."),
    ("What reports will I get?", "You get clear monthly reports showing map rankings, calls, clicks and profile activity, plus updates on the work done."),
    ("Can you fix a suspended Google Business Profile?", "In many cases yes. I review why the profile was suspended, fix the cause and guide the reinstatement process to get you back on the map."),
    ("Do you work with businesses outside India?", "Yes. Local SEO is based on location, so I can help local businesses in the US, Canada and other places rank in their own city and area."),
    ("How do I get started?", "Just book a free local SEO audit using the button on this page. I will review your local presence and show you how to get found by more nearby customers."),
]

RELATED = [
    ("Google Business Profile", "/services/google-business-profile/"),
    ("On-page SEO", "/services/on-page-seo/"),
    ("Link building", "/services/link-building/"),
    ("SEO audit", "/services/seo-audit/"),
    ("Technical SEO", "/services/technical-seo/"),
    ("Google Ads", "/services/google-ads/"),
]

PAGE = {
    "path": "/services/local-seo/",
    "slug": "local-seo",
    "form_name": "local_seo",
    "service": "Local SEO",
    "service_name": "Local SEO services",
    "thanks_what": "local SEO audit",
    "category": "Search engine optimization",
    "service_desc": "Local SEO covering Google Business Profile optimization, local keyword targeting, citations and listings, review strategy, local on-page SEO, local link building and monthly reporting on map rankings, calls and clicks.",
    "audience": "Local businesses that want more calls, visits and bookings from their area",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What local SEO includes",
    "offers": GET,
    "title": "Local SEO Services That Get You Found | Sushant Rana",
    "og_title": "Local SEO Services That Get You Found",
    "og_alt": "Local SEO services by Sushant Rana",
    "desc": "Local SEO services that help you rank in Google Maps and the local pack, so nearby customers find you first. Book a free local SEO audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Local SEO", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Local SEO", "questions, answered"),
            "body": ["Profiles, reviews, rankings and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Local SEO services",
        "h1": ("Local SEO services that get your business found", "by nearby customers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help local businesses show up in the top spots on Google, so nearby customers choose you first. When people search for a service near them, they usually pick from the first few results on the map.',
            "Local SEO is one of the best investments a local business can make, because the people searching are close by and ready to act. We help clinics, shops, service businesses and multi location brands get found and get more calls, visits and bookings.",
        ],
        "cta2": ("See client work", "#work"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free local SEO audit",
        "sub": "Tell me about your business and I will review your local presence for free.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Business", "fields": [
                {"type": "radio", "name": "gbp", "label": "Do you have a Google Business Profile?", "req": True,
                 "options": ["Yes, set up", "Yes, but not optimized", "No or not sure"]},
                {"type": "text", "name": "area", "label": "City or area you serve", "req": True, "placeholder": "Your city or area"},
                {"type": "select", "name": "locations", "label": "Number of locations", "placeholder": "Select",
                 "options": ["One location", "2 to 5 locations", "6 or more locations", "Service area, no shopfront"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Google Business Profile", "Map rankings", "Reviews", "Citations", "Local pages", "Suspended profile", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you do, the areas you cover, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Business Profile", "Local pack", "Google Maps", "Near me searches", "Citations", "Reviews", "Local pages", "Local links"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What local SEO is", "and why it matters"),
             "body": ["Local SEO is the work that helps your business appear when people search for a service near them, such as a dentist near me or a plumber in your city. It focuses on Google Maps, the local pack of top results, and the map area that shows above the normal results.",
                      "This matters because most local searches lead to a call or a visit very soon after. If you are not in those top local results, your competitors are getting those customers instead of you."],
             "bullets": ["Found on Google Maps and in the local pack", "Shown for near me and city searches", "Searchers who call or visit soon after"],
             "cta": CTA, "visual": mappack}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why local SEO is perfect", "for local business"),
                      "body": ["The people searching are close by and ready to act. That is what makes local search so valuable."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Near me searches are huge", "p": "Every day people search for services near them and act fast. Ranking well for these searches puts you in front of buyers at the perfect moment."},
                          {"icon": "pin", "h3": "The local pack gets the clicks", "p": "The map area with the top three businesses gets a large share of the clicks and calls. Getting into that pack can transform your enquiries."},
                          {"icon": "target", "h3": "You reach high intent buyers", "p": "Local searchers are usually ready to buy, book or visit soon. This means the leads you get are warm and close to a decision."},
                          {"icon": "star", "h3": "Reviews build instant trust", "p": "Strong reviews on your profile make people choose you over others. I help you get more reviews and show them off."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The local SEO work", "I do for you"),
                           "body": ["Six parts that work together to get you into the map results and keep you there. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.projects_section(["elixir", "achievers"], ("SEO work for", "real businesses"),
                       "Businesses in India where SEO is part of what we do. Pick one to see the work and what it delivered."),
    L.split({"id": "lever", "pill": "The big lever", "h2": ("Why your Google Business Profile is", "the heart of local SEO"),
             "body": ["Your Google Business Profile is the free listing that decides whether you show up in the map and local pack. It is the most powerful tool in local SEO, and most businesses never set it up properly.",
                      "I fully optimize your profile with the right categories, services, photos, posts and details, and I keep it active. A strong, well kept profile is often the fastest way to more calls and visits from local searches."],
             "bullets": ["The right categories and services", "Fresh photos and posts", "Details kept complete and active"],
             "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My local SEO", "process"),
                   "body": ["Five clear stages, from the first audit to monthly reports. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Local audit", "short": "Audit", "p": "I check your current rankings, your Google Business Profile and your listings to find the gaps that are holding you back.", "points": ["Current map rankings", "Google Business Profile check", "Listings and gaps"]},
                       {"h3": "Profile and on-page optimization", "short": "Optimize", "p": "I optimize your profile and your website pages for your city and services, so Google knows exactly where and what you serve.", "points": ["Profile optimized", "City and service pages", "Local keywords in place"]},
                       {"h3": "Citations and consistency", "short": "Citations", "p": "I fix and build listings so your business details match everywhere, which is a key trust signal for local ranking.", "points": ["Wrong listings fixed", "New listings built", "Same details everywhere"]},
                       {"h3": "Reviews and content", "short": "Reviews", "p": "I build your review flow and add helpful local content that answers what your customers search for.", "points": ["Review flow set up", "Replies to reviews", "Helpful local content"]},
                       {"h3": "Tracking and reporting", "short": "Reporting", "p": "I track your map rankings, calls and clicks and send you clear reports in plain language.", "points": ["Map rankings tracked", "Calls and clicks tracked", "Plain language reports"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my local SEO service"),
                  "body": ["You get a complete, done for you local SEO service focused on getting you more calls, visits and bookings from your area. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Want more local customers finding you on Google?",
                                       "p": "Let me take a free look at your local presence and your Google Business Profile. I will show you exactly what is holding you back. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why local businesses", "choose me"),
                  "body": ["The person doing the work is the person you talk to, and every report is about calls, visits and bookings."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person doing the work, with clear answers and fast replies, not a call center."},
                      {"h3": "Focus on real enquiries", "p": "I care about calls, visits and bookings, not just rankings on a screen. Real business is the goal."},
                      {"h3": "Honest reporting", "p": "I report on rankings, calls and clicks in plain language, so you always know the value you are getting."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Local businesses", "I work with"),
                     "body": "Dental and healthcare clinics, salons and spas, restaurants, law firms, real estate offices, home service providers and multi location businesses. If your customers come from your local area, local SEO can grow your enquiries.",
                     "chips": [("Dental clinics", "/industries/dental/"), ("Healthcare clinics", None), ("Salons and spas", None),
                               ("Restaurants", None), ("Law firms", "/industries/legal-firms/"), ("Real estate offices", "/industries/real-estate/"),
                               ("Home services", None), ("Local businesses", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "local SEO"),
                     "body": "Local rankings go further when your profile, your pages and your links are handled together.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to get found by", "more local customers?"),
               "p": "Let us look at your local presence together and build a plan that brings you more calls, visits and bookings from your area.",
               "btn": CTA, "note": "No obligation · Free local SEO audit"}),
]
