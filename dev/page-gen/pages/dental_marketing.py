# Dental Marketing Services (industry page). Copy: 20_Dental_Marketing_Services.docx
# No client work: none of the published clients is a dental clinic.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free dental marketing strategy call"

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


# --------------------------------------------------- 01: live Maps demo

maps_demo = figure("Google Maps", ["Example", "Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type what a patient searches</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="q" placeholder="dentist near me" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Search words to preview"/></span></label>'
    '<p class="mt-4 text-[11px] text-muted">Results for <strong class="font-semibold text-ink">&quot;<span data-mirror-out="q"></span>&quot;</strong></p>'
    f'<div class="mt-2">{map_area()}</div>'
    + place_rows("Your Clinic", "Open now · Near you", "Another clinic")
    + '<p class="mt-4 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
    f'{svg("target", "h-4 w-4 shrink-0 text-orange")}Patients pick from the first few clinics they see. That should be yours.</p>'
))

# --------------------------------------------------- 03: what I do (tabs)

TYPES = [
    {"key": "gads", "name": "Google Ads for dentists", "icon": "search",
     "what": "I run ads that show your clinic at the top of Google exactly when people search for a dentist near them.",
     "mock": figure("Search ad", ["Example"], search_ad("yourclinic.com", "Dentist Near You | Your Clinic", "Clear treatments, the reason to choose you and one easy way to book or call.", ["Book appointment", "Treatments", "Call the clinic"]))},
    {"key": "local", "name": "Local SEO and Google Business Profile", "icon": "target",
     "what": "I get your clinic ranking on Google Maps and in the local pack, so nearby patients find you for free.",
     "mock": figure("Local pack", ["Example"], map_area() + place_rows("Your Clinic", "Dentist · Near you", "Another clinic"))},
    {"key": "meta", "name": "Meta Ads for awareness and offers", "icon": "users",
     "what": "I run Facebook and Instagram ads to promote your clinic, your offers and your treatments to local people.",
     "mock": figure("Facebook and Instagram ad", ["Example"], social_ad("Your Clinic", "Your treatment offer", "Shown to people who live near your clinic", "Book now"))},
    {"key": "landing", "name": "High converting landing pages", "icon": "file",
     "what": "I build pages that turn your ad clicks into booked appointments, instead of wasting your budget.",
     "mock": figure("Landing page", ["Example"], landing("Your treatment, explained simply", "Why patients choose your clinic, and one clear next step.", ["Your name", "Phone number", "Preferred day"], "Request appointment"))},
    {"key": "reviews", "name": "Reviews and reputation", "icon": "shield",
     "what": "I help you get more five star reviews and manage your reputation, which is huge for a dental clinic.",
     "mock": figure("Patient reviews", ["Example"], reviews("Patient") + '<p class="mt-3 text-xs text-body">Genuine reviews from real patients, managed and answered.</p>')},
    {"key": "tracking", "name": "Call and booking tracking", "icon": "phone",
     "what": "I track every call and booking so we know exactly which marketing is bringing you patients.",
     "mock": figure("Where patients came from", ["Example"], tracking(
         [("Google Ads", "Phone call", "Booked", True), ("Google Maps", "Booking form", "Booked", True), ("Meta Ads", "Form enquiry", "Enquiry", False), ("Landing page", "Phone call", "Booked", True)],
         "Every call and booking matched to the marketing that brought it."))},
]

# --------------------------------------------------- 04: the patient journey check

JOURNEY = [
    ("Search: we do not show up for \"dentist near me\"", "If you are not in the first few results or on Maps, the patient books with someone else."),
    ("Trust: our reviews and profile look thin", "Patients trust the clinic whose reviews and profile reassure them."),
    ("Click: our ads send people to the home page", "A clear landing page turns the click into a booking instead of wasting it."),
    ("Book: booking or calling us is not obvious", "If the next step is hard to find, the patient leaves before they book or call."),
    ("Track: we do not know which marketing brought each booking", "Without call and booking tracking you cannot tell what is working."),
]
journey_box = L.leak_check(
    "Patient journey check", "Follow a new patient from search to chair. Tick every step where your clinic could be losing them.", JOURNEY,
    ("Nothing ticked. A free strategy call still checks the steps that are hard to see from the inside.",
     "A gap or two. These are the steps I connect first, so patients stop slipping away.",
     "Patients are likely slipping away at several steps. Connecting the whole journey is how your schedule fills."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "target", "h3": "Strategy for your clinic", "p": "A plan built around your treatments, your area and your budget, focused on the patients you want most."},
    {"icon": "search", "h3": "Google and Meta Ads", "p": "Ads that show your clinic at the top of Google when people search for a dentist, and promote your offers and treatments to local people."},
    {"icon": "gauge", "h3": "Local SEO and Google Business Profile", "p": "Your clinic ranking on Google Maps and in the local pack, so nearby patients find you for free."},
    {"icon": "file", "h3": "High converting landing pages", "p": "Pages that turn your ad clicks into booked appointments, instead of wasting your budget."},
    {"icon": "shield", "h3": "Review and reputation help", "p": "More genuine five star reviews and a reputation you manage, because patients rely on it."},
    {"icon": "chart", "h3": "Call and booking tracking, clear reports", "p": "Every call and booking tracked, with clear reports on calls, bookings and cost per patient in plain language."},
]

FAQ = [
    ("How do you get more patients for my clinic?", "I use a mix of Google Ads, local SEO and high converting landing pages to put your clinic in front of people searching for a dentist and turn them into booked appointments."),
    ("Which channels work best for dentists?", "Google Ads and local SEO usually work best, because they reach people actively looking for a dentist near them. Meta Ads and reviews add strong support."),
    ("How much should a dental clinic spend on marketing?", "It depends on your area, your competition and your goals. On our call I will suggest a realistic budget for your market so you get results without overspending."),
    ("How soon will I see new patients?", "Google Ads can bring enquiries within days, while local SEO builds over a couple of months. Together they give you both fast and lasting results."),
    ("Do you do dental SEO or dental ads?", "Both. I combine local SEO and paid ads because together they bring more patients than either one alone, and I balance them to fit your budget."),
    ("Can you help me rank on Google Maps?", "Yes. I optimize your Google Business Profile and local SEO so your clinic shows up in the map results when nearby patients search."),
    ("How do you track new patient calls?", "I set up call and booking tracking so we can see exactly which ads and searches are bringing you patients, and improve from there."),
    ("Can you target high value treatments like implants?", "Yes. I can build campaigns aimed at patients looking for implants, cosmetic work and other high value treatments, not just routine check ups."),
    ("Do you build landing pages for my clinic?", "Yes. I build focused landing pages that turn your ad clicks into booked appointments, which greatly lowers your cost per patient."),
    ("How do reviews help my clinic?", "Reviews build trust and strongly affect whether people choose you. I help you get more genuine reviews and manage your reputation."),
    ("Do you work with multi location practices?", "Yes. I can run marketing for practices with several locations, setting up profiles and campaigns for each one."),
    ("Can you help a brand new clinic?", "Yes. For a new clinic, ads and local SEO are one of the fastest ways to get known and start filling your schedule."),
    ("What will my cost per patient be?", "It varies by treatment and area, but my goal is always to lower it over time. I track it closely so you can see the real return on your spend."),
    ("What reports will I get?", "You get clear monthly reports showing calls, bookings and cost per patient, plus updates on the work done."),
    ("How do I get started?", "Just book a free dental marketing strategy call using the button on this page. I will look at your clinic and show you how to get more patients."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Local SEO", "/services/local-seo/"),
    ("Google Business Profile", "/services/google-business-profile/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("Landing pages", "/services/landing-pages/"),
    ("Lead generation", None),
]

PAGE = {
    "path": "/industries/dental/",
    "slug": "dental-marketing",
    "form_name": "dental_marketing",
    "service": "Dental Marketing",
    "service_name": "Dental marketing services",
    "thanks_what": "dental marketing strategy call",
    "category": "Digital marketing for dental clinics",
    "service_desc": "Dental marketing for clinics and practices: Google Ads, local SEO and Google Business Profile, Meta Ads, high converting landing pages, review and reputation help, call and booking tracking and clear reports.",
    "audience": "Dental clinics and practices",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What dental marketing includes",
    "offers": GET,
    "title": "Dental Marketing Services for More Patients | Sushant Rana",
    "og_title": "Dental Marketing Services for More Patients",
    "og_alt": "Dental marketing services by Sushant Rana",
    "desc": "Dental marketing services that bring new patients with Google Ads, local SEO and high converting landing pages. Book a free dental marketing call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Dental", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about dental marketing"),
            "body": ["Channels, budgets, timelines and tracking. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Dental marketing services",
        "h1": ("Dental marketing that fills your chairs", "with new patients"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help dental clinics get a steady flow of new patients using Google Ads, local SEO and landing pages that actually convert. If you are a great dentist with too many empty slots in your schedule, the problem is almost never your dentistry, it is that not enough new patients know about you.',
            "Being a skilled dentist is not enough on its own. Patients search online first, and if your clinic is not showing up, they book with someone else. We make sure you are the clinic they find and choose.",
        ],
        "cta2": ("See the patient journey", "#journey"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free dental marketing strategy call",
        "sub": "Tell me about your clinic and I will show you how to bring in more new patients.",
        "submit": "Request my free strategy call",
        "company_label": "Clinic / practice name",
        "steps": [
            {"label": "Clinic", "fields": [
                {"type": "radio", "name": "running", "label": "Are you running ads for your clinic now?", "req": True,
                 "options": ["Yes, running now", "Paused or stopped", "Never run them"]},
                {"type": "checkbox", "name": "treatments", "label": "Treatments you want more patients for",
                 "options": ["Check ups and cleaning", "Implants", "Cosmetic dentistry", "Orthodontics", "Emergency visits", "Other"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourclinic.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "budget", "label": "Monthly marketing budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "checkbox", "name": "channels", "label": "What you are interested in",
                 "options": ["Google Ads", "Local SEO and Maps", "Meta Ads", "Landing pages", "Reviews", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your clinic, your area, how many locations, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads for dentists", "Local SEO", "Google Maps", "Google Business Profile", "Meta Ads", "Landing pages", "Reviews", "Call tracking"]),
    L.split({"id": "problem", "pill": "The problem", "h2": ("Why great dentists", "still have empty chairs"),
             "body": ["Most dentists are excellent at what they do, yet still struggle to keep their schedule full. The reason is simple, they rely on word of mouth and hope, while newer patients are all searching online.",
                      "When someone needs a dentist today, they search on Google or Maps and pick from the first few clinics they see. If you are not there, you lose that patient. I fix this by making your clinic easy to find and easy to book."],
             "bullets": ["Patients search on Google and Maps first", "They choose from the first few clinics they see", "Your clinic made easy to find and easy to book"],
             "cta": CTA, "visual": maps_demo}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why online marketing works", "so well for dentists"),
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Patients search online first", "p": "People look for a dentist near them on Google before they ever call. Showing up there puts you in front of ready to book patients."},
                          {"icon": "users", "h3": "Local competition is fierce", "p": "There are many clinics competing for the same patients. Good marketing makes sure you are the one they choose, not the one they scroll past."},
                          {"icon": "repeat", "h3": "It brings predictable patients", "p": "Instead of waiting and hoping, ads and SEO give you a steady, predictable flow of new patient enquiries."},
                          {"icon": "wallet", "h3": "You can win high value treatments", "p": "Smart targeting helps you attract patients for higher value treatments like implants and cosmetic work, not just check ups."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("How I get you", "more new patients"),
                           "body": ["Six pieces that work together, from the first search to the booked appointment. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.split({"id": "journey", "anchor": "journey", "pill": "The journey", "h2": ("How I turn a search", "into a booked appointment"),
             "body": ["Getting a new patient is a journey, and I make sure your clinic wins at every step. It starts when someone searches for a dentist, sees your clinic at the top, and trusts you because of your reviews and profile.",
                      "From there, they click through to a clear landing page and book or call. I connect all of these steps, from the search to the booked appointment, so you do not lose patients along the way. This full journey approach is what turns marketing spend into a full schedule."],
             "bullets": ["Search: your clinic at the top", "Trust: reviews and a strong profile", "Click: a clear landing page", "Book: a call or a booked appointment"],
             "visual": journey_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the wrong numbers and the people who were only browsing.",
                        "So we connect your ads to your CRM. Each enquiry is saved with the ad it came from, your front desk marks which patients booked an appointment, and those bookings flow back into Google Ads as conversions. From then on the platform goes after patients who book, not just forms."],
                  bullets=["Ad click saved with every patient enquiry", "Front desk marks booked appointments in the CRM", "Booked appointments sent back to Google Ads", "Reports on cost per booked patient"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My dental marketing", "process"),
                   "body": ["A clear process, not luck. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Clinic audit and goals", "short": "Audit", "p": "I learn about your clinic, your treatments and your goals, so we focus on the patients you want most.", "points": ["Your clinic and treatments", "The patients you want most", "Your goals"]},
                       {"h3": "Strategy", "short": "Strategy", "p": "I plan the right mix of ads, local SEO and pages for your area and your budget.", "points": ["Ads, local SEO and pages", "Planned for your area", "Planned for your budget"]},
                       {"h3": "Setup", "short": "Setup", "p": "I build your campaigns, profile and landing pages and set up call and booking tracking.", "points": ["Campaigns and profile", "Landing pages", "Call and booking tracking"]},
                       {"h3": "Optimize", "short": "Optimize", "p": "I improve your results every week, lowering your cost per patient and bringing more bookings.", "points": ["Weekly improvements", "Lower cost per patient", "More bookings"]},
                       {"h3": "Report", "short": "Report", "p": "I send you clear reports showing calls, bookings and cost per patient in plain language.", "points": ["Calls and bookings", "Cost per patient", "Plain language"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included", "when you work with me"),
                  "body": ["You get a complete, done for you patient generation system for your clinic. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free strategy call", "h3": "Want a steady flow of new patients?",
                                       "p": "Let me look at your clinic and your area and show you exactly how we can fill your schedule with new patients. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why dentists", "choose me"),
                  "body": ["You talk to the person running your marketing, and every report is about bookings and cost per patient."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person running your marketing, with clear answers and fast replies."},
                      {"h3": "Focus on booked patients", "p": "I care about actual bookings and cost per patient, not clicks and vanity numbers."},
                      {"h3": "Honest reporting", "p": "I report on calls, bookings and cost per patient in plain language, so you always know your return."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Dental clinics", "I work with"),
                     "body": "I help general dentists, cosmetic and implant clinics, orthodontists and multi location dental practices. Whether you are a new clinic or an established one wanting to grow, I can bring you more of the patients you want.",
                     "chips": [("General dentists", None), ("Cosmetic and implant clinics", None), ("Orthodontists", None), ("Multi location practices", None),
                               ("New clinics", None), ("Healthcare", None), ("Local businesses", None)]}),
    L.chips_section({"id": "related", "h2": ("Services behind", "your dental marketing"),
                     "body": "The channels and pages that bring patients in, each with its own page if you want the detail.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to fill", "your schedule?"),
               "p": "Let us talk about your clinic and your goals and build a marketing plan that brings you a steady flow of new patients.",
               "btn": CTA, "note": "No obligation · Free strategy call"}),
]
