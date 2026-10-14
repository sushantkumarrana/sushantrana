# Google Business Profile (GMB) Optimization. Copy: 14_Google_Business_Profile_GMB_Service.txt
# No numbers beyond the shared hero stats. Mocks are labelled "Example" or "Live demo".
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free Google Business Profile audit"

# lucide map-pin, star and message-circle, local to this page
L.ICON.update({
    "pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path><circle cx="12" cy="10" r="3"></circle>',
    "star": '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path>',
    "message": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"></path>',
})

# ------------------------------------------------------------ mock helpers
TONE = {"ok": "bg-ink/[0.06] text-ink", "warn": "bg-orange/10 text-orange", "bad": "bg-red-50 text-red-700",
        "hot": "bg-orange text-white", "off": "bg-ink/[0.06] text-muted"}
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
MIRROR_IN = "min-w-0 w-full rounded-xl border border-[var(--color-line)] bg-white px-3 py-2 text-sm text-ink outline-none transition focus:border-orange"


def tag(text, tone="ok"):
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {TONE[tone]}">{E(text)}</span>'


def rows(items):
    """items = [(title, right_html, sub)]"""
    return '<ul class="grid list-none gap-2.5">' + "".join(
        '<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid min-w-0"><span class="truncate text-sm font-bold text-ink">{E(t)}</span>'
        + (f'<span class="text-xs text-muted">{E(s)}</span>' if s else "") + f'</span>{r}</li>'
        for t, r, s in items) + "</ul>"


def note(text, icon="target"):
    return ('<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def lines(*widths):
    return "".join(f'<span class="mt-2 block h-2 {w} rounded-full bg-ink/10"></span>' for w in widths)


def numbered(items):
    return '<ol class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
        f'<span class="text-sm font-semibold text-ink">{E(t)}</span></li>' for i, t in enumerate(items, 1)) + "</ol>"


def stars(cls="h-3.5 w-3.5"):
    return '<span class="flex gap-0.5 text-orange" aria-hidden="true">' + svg("star", cls) * 5 + "</span>"


def actions(names=("Call", "Directions", "Website")):
    return '<div class="mt-3 grid grid-cols-3 gap-2">' + "".join(
        f'<span class="rounded-full border border-[var(--color-line)] py-1.5 text-center text-[11px] font-bold text-ink">{t}</span>' for t in names) + "</div>"


GHOST = ('<div class="rounded-2xl border border-[var(--color-line)] p-3.5 opacity-60" aria-hidden="true"><span class="block h-3 w-1/2 rounded-full bg-ink/15"></span>'
         '<span class="mt-2 block h-2 w-5/6 rounded-full bg-ink/10"></span></div>')
PHOTO = f'<span class="grid aspect-square place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg("image", "h-5 w-5")}</span>'

# --------------------------------------------- 01 basics: live profile card
profile = figure("Your Google Maps profile", ["Live demo"], (
    '<div class="grid gap-3 sm:grid-cols-2">'
    f'<label class="block"><span class="{CAP}">Business name</span><input data-mirror="biz" placeholder="Your Business" class="mt-1.5 {MIRROR_IN}" aria-label="Business name to preview"/></label>'
    f'<label class="block"><span class="{CAP}">What you do</span><input data-mirror="cat" placeholder="dental clinic" class="mt-1.5 {MIRROR_IN}" aria-label="Business category to preview"/></label></div>'
    '<div class="mt-4 overflow-hidden rounded-2xl border border-orange/30 bg-white">'
    f'<div class="grid grid-cols-3 gap-1.5 bg-[#fff7f3] p-1.5" aria-hidden="true">{PHOTO * 3}</div>'
    '<div class="p-4"><div class="flex items-start justify-between gap-3"><div class="min-w-0">'
    '<p class="text-lg font-extrabold leading-tight text-ink"><span data-mirror-out="biz"></span></p>'
    f'<div class="mt-1 flex items-center gap-2">{stars()}<span class="text-xs text-muted">Reviews</span></div>'
    '<p class="mt-1 truncate text-xs text-muted"><span data-mirror-out="cat" class="svc-cap"></span> · Your area</p>'
    '<p class="mt-1 text-xs font-semibold text-orange">Open now</p></div>'
    f'<span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg("pin", "h-5 w-5")}</span></div>'
    + actions() + '</div></div>'
    + note("This card is often the <strong class=\"font-semibold text-ink\">first thing a local customer sees about you.</strong> A strong one brings calls, directions and visits.", "pin")))

# ------------------------------------------------- 03 what I do: tab mocks
MOCKS = {
    "setup": figure("Setup and verification", ["Example"], (
        numbered(["Profile created with your correct details", "Verification by postcard, phone, email or video", "Verified and showing on the map"])
        + note("I guide you through verification so your profile goes live correctly."))),
    "optimize": figure("Profile optimization", ["Example"], rows([
        ("Categories", tag("Complete", "warn"), "Primary and extra categories researched"),
        ("Services", tag("Complete", "warn"), "Every service you offer listed"),
        ("Description", tag("Complete", "warn"), "Clear, written for your customers"),
        ("Hours", tag("Complete", "warn"), "Including holiday hours"),
        ("Attributes", tag("Complete", "warn"), "The extra details buyers look for"),
    ])),
    "photos": figure("Photos and Google posts", ["Example"], (
        f'<p class="{CAP}">Photos</p><div class="mt-2 grid grid-cols-4 gap-2" aria-hidden="true">{PHOTO * 4}</div>'
        f'<p class="mt-4 {CAP}">Latest post</p>'
        '<div class="mt-2 rounded-2xl border border-[var(--color-line)] p-4"><div class="flex items-center justify-between gap-3">'
        '<p class="text-sm font-bold text-ink">This month&#x27;s offer</p>' + tag("Offer", "warn") + '</div>'
        + lines("w-full", "w-2/3") +
        '<span class="mt-3 inline-flex rounded-full bg-orange px-3 py-1 text-[10px] font-bold text-white">Learn more</span></div>'
        + note("Regular posts and fresh photos keep the profile active."))),
    "qa": figure("Questions and answers", ["Example"], (
        '<div class="grid gap-2.5">'
        '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><p class="' + CAP + '">Question from a customer</p>'
        '<p class="mt-1 text-sm font-bold text-ink">Do you take walk in appointments?</p></div>'
        '<div class="rounded-2xl border border-orange/30 bg-orange/5 p-4"><p class="' + CAP + '">Answer from the business</p>'
        '<p class="mt-1 text-sm text-body">A clear, helpful answer, so the buyer does not have to call and ask.</p></div></div>'
        + note("Buyers get clear, helpful information right away.", "message"))),
    "reviews": figure("Reviews and replies", ["Example"], (
        numbered(["A happy customer gets a simple review link", "They leave a genuine review", "Your business replies"])
        + '<div class="mt-4 rounded-2xl border border-[var(--color-line)] p-4">'
        f'<div class="flex items-center justify-between gap-3"><p class="text-sm font-bold text-ink">A customer</p>{stars()}</div>' + lines("w-full", "w-3/4")
        + '<div class="mt-3 rounded-xl bg-[#fff7f3] p-3"><p class="text-[11px] font-bold text-ink">Reply from Your Business</p>' + lines("w-5/6") + '</div></div>')),
    "ranking": figure("Local ranking", ["Example"], (
        '<p class="flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 text-sm text-ink">'
        f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<span class="truncate">your service near me</span></p>'
        f'<p class="mt-4 {CAP}">Top three on the map</p><div class="mt-2.5 grid gap-2.5">'
        '<div class="rounded-2xl border border-orange/30 bg-orange/5 p-3.5"><div class="flex items-start justify-between gap-3"><div class="min-w-0">'
        f'<p class="text-sm font-extrabold text-ink">Your Business</p><div class="mt-1">{stars("h-3 w-3")}</div></div>{svg("pin", "h-5 w-5 shrink-0 text-orange")}</div></div>'
        f'{GHOST * 2}</div>' + note("The right signals and content for the searches your customers use.", "pin"))),
    "insights": figure("Insights and suspension fixes", ["Example"], (
        rows([("Calls", tag("Tracked", "warn"), "From your profile"),
              ("Direction requests", tag("Tracked", "warn"), "People heading to you"),
              ("Website clicks", tag("Tracked", "warn"), "Visits from your profile")])
        + f'<p class="mt-4 {CAP}">If your profile is suspended</p><div class="mt-2.5">'
        + rows([("Suspension reviewed", tag("Step 1", "off"), "Why it happened"),
                ("Cause fixed", tag("Step 2", "off"), "The problem put right"),
                ("Reinstatement requested", tag("Step 3", "hot"), "Back on the map")]) + "</div>")),
}

WORK = [
    ("setup", "Full setup and verification", "shield", "If you do not have a profile, I set it up and guide the verification so your business appears on the map correctly."),
    ("optimize", "Complete profile optimization", "sliders", "I optimize every part of your profile, including categories, services, description, hours and attributes, so Google fully understands your business."),
    ("photos", "Photos and Google posts", "image", "I add strong photos and regular posts, which keep your profile active and make it more attractive to customers."),
    ("qa", "Questions and answers", "message", "I manage the questions and answers on your profile so buyers get clear, helpful information right away."),
    ("reviews", "Review generation and responses", "star", "I set up a simple system to get more genuine reviews and to respond to them, which lifts both trust and rankings."),
    ("ranking", "Local ranking optimization", "pin", "I use the right signals and content so your profile ranks higher for the searches your customers use."),
    ("insights", "Insights and suspension fixes", "chart", "I track your profile insights and, if your profile is suspended, I work to get it reinstated."),
]

# ------------------------------------------- 06 the difference: self check
forgotten_box = L.leak_check(
    "Forgotten profile check", "Tick everything that sounds like your profile.",
    [("I claimed my profile once and have not touched it since", "A half filled, never updated profile is ignored by Google and customers."),
     ("Some categories, services, hours or description are missing", "Google cannot show you for searches it does not fully understand."),
     ("I have not added photos or posts in a long time", "Fresh photos and posts keep a profile active, which Google and customers reward."),
     ("Reviews come in slowly, and some have no reply", "Reviews and replies build trust and help your ranking."),
     ("Customer questions on my profile go unanswered", "Buyers with no answer often call the business next door instead.")],
    ("Nothing ticked. A free audit still compares your profile with your competitors and shows what is holding it back.",
     "A gap or two. These are usually the first things I fix on a profile.",
     "Your profile is very likely being ignored. Bringing it back to life is often the fastest way to more calls and visits."),
    CTA, "Gaps ticked")

# ----------------------------------------------------------------- content
GET = [
    {"icon": "shield", "h3": "Profile setup and verification", "p": "Your profile set up with the right details and verified, so your business appears on the map correctly."},
    {"icon": "sliders", "h3": "Full optimization", "p": "Categories, services, description, hours and attributes completed, so Google fully understands your business."},
    {"icon": "image", "h3": "Photos and posts", "p": "Strong photos and regular posts that keep your profile active and attractive to customers."},
    {"icon": "message", "h3": "Questions and answers", "p": "The questions on your profile managed, so buyers get clear, helpful information right away."},
    {"icon": "star", "h3": "A review system", "p": "A simple way to get more genuine reviews and respond to them, which lifts trust and rankings."},
    {"icon": "pin", "h3": "Local ranking work", "p": "The right signals and content so your profile ranks higher for the searches your customers use."},
    {"icon": "chart", "h3": "Clear reports", "p": "Calls, clicks, map rankings and profile activity, reported in plain language."},
]

FAQ = [
    ("What is a Google Business Profile?", "Google Business Profile is the free listing that shows your business on Google Maps and in the local pack. It shows your details, photos, reviews and more, and it drives local calls and visits."),
    ("Is Google Business Profile the same as Google My Business?", "Yes. Google My Business is the old name. Google renamed it to Google Business Profile, but many people still call it GMB. It is the same free listing."),
    ("Is a Google Business Profile free?", "Yes, the profile itself is completely free. My service is about optimizing and managing it so it actually brings you customers, which most free profiles fail to do."),
    ("How does a Google Business Profile help my business?", "It helps people find you on the map, read your reviews, call you and get directions. A strong profile can bring a steady flow of local customers with no ad cost."),
    ("How do I get my profile verified?", "Google verifies your business through methods like a postcard, phone, email or video. I guide you through the process so your profile goes live correctly."),
    ("How important are reviews for my profile?", "Very important. Reviews build trust with customers and help your ranking. I set up a simple system to get more genuine reviews and to respond to them."),
    ("Can you optimize my existing profile?", "Yes. Most profiles are only half set up. I complete and optimize every part so it ranks better and attracts more customers."),
    ("What are Google posts?", "Google posts are short updates you can add to your profile, like offers or news. They keep your profile active, which Google and customers both like."),
    ("How soon will I see results?", "You often see more calls and clicks within a few weeks of proper optimization, with stronger map rankings building over a couple of months."),
    ("Can you fix a suspended Google Business Profile?", "In many cases yes. I review why it was suspended, fix the cause and guide the reinstatement process to get you back on the map."),
    ("Do I need a website to use a Google Business Profile?", "No, but a website helps a lot. Even without one, a strong profile can bring calls and visits. I will advise the best path for your situation."),
    ("What categories should I choose?", "The right categories help Google show you for the correct searches. I research and pick the best primary and extra categories for your business."),
    ("How do you increase my calls?", "I optimize your profile, add strong content and reviews, and improve your local ranking, so more people find you and take action."),
    ("Can you manage multiple locations?", "Yes. I can set up and optimize a separate profile for each of your locations so every branch shows up correctly on the map."),
    ("What reports will I get?", "You get clear monthly reports showing calls, clicks, map rankings and profile activity, plus updates on the work done."),
    ("How do I get started?", "Just book a free Google Business Profile audit using the button on this page. I will review your profile and show you how to get more local customers."),
]

RELATED = [
    ("Local SEO", "/services/local-seo/"),
    ("Website SEO audit", "/services/seo-audit/"),
    ("On page SEO", "/services/on-page-seo/"),
    ("Link building", "/services/link-building/"),
    ("Google Ads", "/services/google-ads/"),
    ("Landing pages", "/services/landing-pages/"),
]

PAGE = {
    "path": "/services/google-business-profile/",
    "slug": "google-business-profile",
    "form_name": "google_business_profile",
    "service": "Google Business Profile",
    "service_name": "Google Business Profile optimization",
    "thanks_what": "Google Business Profile audit",
    "category": "Local search engine optimization",
    "service_desc": "Google Business Profile (GMB) optimization covering setup and verification, full profile optimization, photos and Google posts, questions and answers, review generation and responses, local ranking work, insights and suspension fixes, with plain language reports.",
    "audience": "Local businesses that want more calls, directions and visits",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What Google Business Profile optimization includes",
    "offers": GET,
    "title": "Google Business Profile (GMB) Optimization | Sushant Rana",
    "og_title": "Google Business Profile (GMB) Optimization",
    "og_alt": "Google Business Profile optimization service by Sushant Rana",
    "desc": "Google Business Profile optimization so you rank in the map, get more calls and win more local customers. Book a free profile audit with me.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Google Business Profile", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Google Business Profile", "questions, answered"),
            "body": ["Verification, reviews, suspensions and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Google Business Profile",
        "h1": ("Google Business Profile optimization that gets you", "more calls and customers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I optimize your Google Business Profile so you show up in the map, build trust and turn searches into calls and visits. Your profile decides whether local customers find you on Google Maps and call you first, and most businesses never set it up properly.',
            "Your Google Business Profile, once called Google My Business, is a free listing with a huge impact on local sales. We help clinics, shops, restaurants and service businesses get the most out of it.",
        ],
        "cta2": ("See what I do", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free Google Business Profile audit",
        "sub": "Tell me about your business and I will review your profile for free.",
        "submit": "Request my free profile audit",
        "steps": [
            {"label": "Profile", "fields": [
                {"type": "radio", "name": "has_profile", "label": "Do you have a Google Business Profile?", "req": True,
                 "options": ["Yes, verified", "Yes, not verified", "It is suspended", "No profile yet", "Not sure"]},
                {"type": "text", "name": "profile_link", "label": "Business name or Google Maps link", "placeholder": "Your business name or Maps link"},
                {"type": "select", "name": "locations", "label": "Number of locations", "req": True, "placeholder": "Select locations",
                 "options": ["1 location", "2 to 5 locations", "6 or more locations"]},
            ]},
            {"label": "Needs", "fields": [
                {"type": "checkbox", "name": "work", "label": "What do you need help with?",
                 "options": ["Setup and verification", "Full optimization", "Photos and posts", "Reviews", "Map rankings", "Suspension fix", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you do, your area, your main competitors..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Business Profile", "Map pack", "Verification", "Photos and posts", "Reviews", "Local rankings", "Suspension fixes"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What Google Business Profile is", "and why it matters"),
             "body": ["Google Business Profile is the free business listing that shows up on Google Maps and in the local pack, the group of top businesses shown for local searches. It was earlier known as Google My Business, so many people still call it GMB.",
                      "This matters because it is often the first thing a local customer sees about you. A strong profile can bring calls, directions and visits every day, while a weak one lets your competitors take those customers instead."],
             "bullets": ["Shown on Google Maps and in the local pack", "Free, with no ad cost", "Calls, directions and visits tracked"],
             "cta": CTA, "visual": profile}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why your Google Business Profile", "is so powerful"),
                      "body": ["For local searches, your profile often matters more than your website."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "pin", "h3": "It powers the map pack", "p": "Your profile decides whether you appear in the top three businesses on the map. That spot gets a large share of local calls and clicks."},
                          {"icon": "wallet", "h3": "It is free but high value", "p": "There is no ad cost. A well optimized profile brings customers for free, which makes it one of the best returns in all of marketing."},
                          {"icon": "phone", "h3": "It drives real actions", "p": "People use your profile to call you, get directions and visit your website. These are real, ready to buy actions, not just views."},
                          {"icon": "star", "h3": "Reviews build instant trust", "p": "Your star rating and reviews sit right on your profile. Strong reviews make people choose you over the business next door."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The Google Business Profile work", "I do for you"),
                           "body": ["Seven parts that turn a forgotten listing into a steady source of calls. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WORK]})),
    L.split({"id": "difference", "pill": "The difference", "h2": ("Why an active profile", "beats a forgotten one"),
             "body": ["Most businesses claim their profile once and then forget it. It sits half filled and never updated, so Google and customers both ignore it.",
                      "I treat your profile as a living part of your marketing. I keep it complete, fresh and active with posts, photos and reviews. This is often the single fastest way to more calls and visits from local searches, and it is exactly what your competitors are not doing."],
             "visual": forgotten_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My Google Business Profile", "process"),
                   "body": ["Five clear steps, from the first audit to monthly reports on calls and map rankings."],
                   "steps": [
                       {"h3": "Profile audit", "short": "Audit", "p": "I review your current profile against your competitors to find what is missing and what is holding you back.", "points": ["Your profile reviewed", "Competitor profiles compared", "Gaps and blockers listed"]},
                       {"h3": "Full optimization", "short": "Optimize", "p": "I complete and optimize every part of your profile so it is accurate, rich and ready to rank.", "points": ["Categories and services", "Description, hours and attributes", "Accurate and complete"]},
                       {"h3": "Content and photos", "short": "Content", "p": "I add photos and posts and keep the profile active, which Google and customers both reward.", "points": ["Strong photos", "Regular Google posts", "Questions answered"]},
                       {"h3": "Reviews system", "short": "Reviews", "p": "I set up your review flow and response process to build trust and improve your ranking.", "points": ["Simple review requests", "Genuine reviews only", "Every review answered"]},
                       {"h3": "Track and report", "short": "Report", "p": "I track your calls, clicks and map rankings and send you clear reports in plain language.", "points": ["Calls and clicks", "Map rankings", "Plain language reports"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in my", "Google Business Profile service"),
                  "body": ["You get a complete, done for you service to turn your profile into a steady source of local customers. You always work directly with me."],
                  "cols": "sm:grid-cols-2 lg:grid-cols-4",
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Want more calls from Google Maps?",
                                       "p": "Let me take a free look at your Google Business Profile. I will show you exactly what is holding it back and how we can get you more local customers. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why local businesses", "choose me"),
                  "body": ["Real actions, honest reports and the person doing the work on the other end of the phone."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person doing the work, with clear answers and fast replies, not a call center."},
                      {"h3": "Focus on calls and visits", "p": "I care about real actions like calls, directions and visits, not just how your profile looks."},
                      {"h3": "Honest reporting", "p": "I report on calls, clicks and rankings in plain language, so you always know the value you are getting."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Local businesses", "I work with"),
                     "body": "I optimize profiles for dental and healthcare clinics, salons and spas, restaurants, law firms, real estate offices, home service providers and multi location businesses. If your customers come from your local area, this service can grow your calls and visits.",
                     "chips": [("Dental clinics", "/industries/dental/"), ("Healthcare clinics", "/industries/healthcare/"), ("Salons and spas", None),
                               ("Restaurants", None), ("Law firms", "/industries/legal-firms/"), ("Real estate offices", "/industries/real-estate/"),
                               ("Home service providers", None), ("Multi location businesses", None), ("Local businesses", "/industries/local-businesses/")]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "your Google Business Profile"),
                     "body": "Your profile and local SEO work together, and a strong website makes every profile visit count.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to win more", "local customers?"),
               "p": "Let us look at your Google Business Profile together and build a plan that brings you more calls, directions and visits from your area.",
               "btn": CTA, "note": "No obligation · Free profile audit"}),
]
