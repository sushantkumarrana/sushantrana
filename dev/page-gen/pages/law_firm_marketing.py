# Law Firm Marketing Services (industry page). Copy: 24_Law_Firm_Marketing_Services.docx
# Client work: Trust Legal, described only as a website rebuild + maintenance (L.PROJECTS facts).
E, svg, figure, pill, HID = L.E, L.svg, L.figure, L.pill, L.HID

CTA = "Book your free legal marketing call"

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


# --------------------------------------------------- 01: practice area search demo

AREAS = [("family", "Family law", "family lawyer near me"), ("injury", "Personal injury", "personal injury lawyer near me"),
         ("criminal", "Criminal defence", "criminal defence lawyer near me"), ("immigration", "Immigration", "immigration lawyer near me")]
AREA_Q = {k: q for k, _, q in AREAS}


def area_panel(k):
    return (f'<p class="mt-4 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 text-sm text-ink">'
            f'{svg("search", "h-4 w-4 shrink-0 text-muted")}{E(AREA_Q[k])}</p>'
            + place_rows("Your Firm", "Open now · Near you", "Another firm"))


search_demo = pick_demo("When a legal problem hits", "Pick a practice area", [(k, lab) for k, lab, _ in AREAS],
                        area_panel, "People reach out to one of the first firms they trust. That should be yours.", "phone")

# --------------------------------------------------- 03: what I do (tabs)

TYPES = [
    {"key": "gads", "name": "Google Ads for lawyers", "icon": "search",
     "what": "I run ads that put your firm at the top of Google exactly when people search for a lawyer for their specific problem.",
     "mock": figure("Search ad", ["Example"], search_ad("yourfirm.com", "Lawyer For Your Practice Area | Your Firm", "The problem you solve, why clients trust you and one easy way to get in touch.", ["Call the firm", "Practice areas", "Request a consultation"]))},
    {"key": "local", "name": "Local SEO and Google Business Profile", "icon": "target",
     "what": "I help your firm rank on Google Maps and in local search, so nearby clients find you for free.",
     "mock": figure("Local pack", ["Example"], map_area() + place_rows("Your Firm", "Law firm · Near you", "Another firm"))},
    {"key": "landing", "name": "Practice area landing pages", "icon": "file",
     "what": "I build focused pages for each practice area that speak to that client's problem and turn clicks into enquiries.",
     "mock": figure("Practice area page", ["Example"], landing("Your practice area, explained simply", "The problem your client faces, how your firm helps, and one clear next step.", ["Your name", "Phone number", "Briefly, what happened"], "Request a call back"))},
    {"key": "meta", "name": "Meta Ads for awareness", "icon": "users",
     "what": "I run Facebook and Instagram ads to build your firm's presence and reach potential clients in your area.",
     "mock": figure("Facebook and Instagram ad", ["Example"], social_ad("Your Firm", "Legal help, close to you", "Shown to potential clients in your area", "Learn more"))},
    {"key": "reviews", "name": "Reviews and reputation", "icon": "shield",
     "what": "I help you get more genuine reviews and manage your reputation, which is vital when people choose a lawyer.",
     "mock": figure("Client reviews", ["Example"], reviews("Client") + '<p class="mt-3 text-xs text-body">Genuine reviews from real clients, managed and answered.</p>')},
    {"key": "tracking", "name": "Call and intake tracking", "icon": "phone",
     "what": "I track every call and enquiry so we know exactly which marketing is bringing you cases.",
     "mock": figure("Where the cases came from", ["Example"], tracking(
         [("Google Ads", "Phone call", "Signed", True), ("Google Maps", "Phone call", "Consultation", True), ("Meta Ads", "Form enquiry", "Enquiry", False), ("Landing page", "Intake form", "Signed", True)],
         "Every call and enquiry matched to the marketing that brought the case."))},
]

# --------------------------------------------------- 04: the advantage, as a self check

CHECKS = [
    ("We do not show up when people search for our practice areas", "When the need is urgent, people reach out to one of the first firms they see."),
    ("One general page covers every practice area", "A page for each practice area speaks to that client's problem and turns clicks into enquiries."),
    ("Our reviews are few or out of date", "People rely heavily on reviews when choosing a lawyer."),
    ("Our firm is hard to find on Google Maps", "Nearby clients search the map results first."),
    ("We cannot tell which calls turned into cases", "Without call and intake tracking you cannot see what is bringing you cases."),
]
check_box = L.leak_check(
    "Visibility check", "Tick everything that sounds like your firm today.", CHECKS,
    ("Nothing ticked. A free call still checks the parts that are hard to see from the inside.",
     "A gap or two. These are the first things I fix, so serious clients find you first.",
     "Serious clients are very likely contacting another firm first. This is where your case flow starts to steady."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "target", "h3": "Strategy for your practice areas", "p": "A plan built around your firm, your practice areas and the cases you want most."},
    {"icon": "search", "h3": "Google and Meta Ads", "p": "Ads at the top of Google when people search for a lawyer for their problem, and Facebook and Instagram ads that build your presence locally."},
    {"icon": "gauge", "h3": "Local SEO and Google Business Profile", "p": "Your firm ranking on Google Maps and in local search, so nearby clients find you for free."},
    {"icon": "file", "h3": "Practice area landing pages", "p": "A focused page for each practice area that speaks to that client's problem."},
    {"icon": "shield", "h3": "Review and reputation help", "p": "More genuine reviews and a reputation you manage, because people rely on it when choosing a lawyer."},
    {"icon": "phone", "h3": "Call and intake tracking, clear reports", "p": "Every call and enquiry tracked, with clear reports on calls, enquiries and cost per case in plain language."},
]

FAQ = [
    ("How do you get clients for my firm?", "I use Google Ads, local SEO and practice area landing pages to reach people searching for a lawyer, then turn those searches into calls and enquiries for your firm."),
    ("Which channels work best for law firms?", "Google Ads and local SEO usually work best, because they reach people actively looking for legal help. Reviews and a strong profile add important trust."),
    ("Is legal marketing expensive?", "Legal keywords can cost more than average, but a single case is often high value, so the return can be strong. I focus on quality enquiries to keep your cost per case sensible."),
    ("How soon will I see results?", "Google Ads can bring enquiries within days, while local SEO builds over a couple of months. Together they give you both fast and lasting results."),
    ("Do you do legal SEO or ads?", "Both. I combine paid ads with local SEO because together they bring more clients than either alone, and I balance them to fit your budget."),
    ("Can you target a specific practice area?", "Yes. I build focused campaigns and landing pages for each practice area, so you attract the exact type of cases you want."),
    ("Can you help me rank on Google Maps?", "Yes. I optimize your Google Business Profile and local SEO so your firm shows up in the map results when nearby clients search."),
    ("Do you build landing pages for each practice area?", "Yes. I build a focused page for each practice area that speaks to that client's problem and turns clicks into enquiries."),
    ("How do you track calls and enquiries?", "I set up call and intake tracking so we can see exactly which ads and searches are bringing you cases, and improve from there."),
    ("How do reviews help my firm?", "People rely heavily on reviews when choosing a lawyer. I help you get more genuine reviews and manage your reputation to build trust."),
    ("Do you work with solo lawyers?", "Yes. I work with solo lawyers as well as larger firms, and I tailor the plan and budget to fit your size and goals."),
    ("Can you handle a competitive practice area?", "Yes. Competitive areas need sharper targeting and stronger pages, which is exactly where careful marketing makes the biggest difference."),
    ("What will my cost per case be?", "It varies by practice area and location, but my goal is always to lower it over time while keeping quality high. I track it closely so you see the real return."),
    ("What reports will I get?", "You get clear monthly reports showing calls, enquiries and cost per case, plus updates on the work done."),
    ("How do I get started?", "Just book a free legal marketing call using the button on this page. I will look at your firm and show you how to bring in more clients."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Local SEO", "/services/local-seo/"),
    ("Google Business Profile", "/services/google-business-profile/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("Landing pages", "/services/landing-pages/"),
    ("CRM consulting", None),
]

PAGE = {
    "path": "/industries/legal-firms/",
    "slug": "law-firm-marketing", "thanks": "industry",
    "form_name": "law_firm_marketing",
    "service": "Law Firm Marketing",
    "service_name": "Law firm marketing services",
    "thanks_what": "legal marketing call",
    "category": "Lead generation for law firms",
    "service_desc": "Law firm marketing for solo lawyers and firms: Google Ads, local SEO and Google Business Profile, practice area landing pages, Meta Ads, review and reputation help, call and intake tracking and clear reports.",
    "audience": "Law firms and lawyers",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What law firm marketing includes",
    "offers": GET,
    "title": "Law Firm Marketing Services for More Clients | Sushant Rana",
    "og_title": "Law Firm Marketing Services for More Clients",
    "og_alt": "Law firm marketing services by Sushant Rana",
    "desc": "Law firm marketing services that bring quality clients with Google Ads, local SEO and landing pages built around your practice areas. Book a free call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Legal Firms", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about law firm marketing"),
            "body": ["Channels, costs, practice areas and tracking. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Law firm marketing services",
        "h1": ("Law firm marketing that brings you", "more quality clients"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help law firms and individual lawyers get a steady stream of quality clients using Google Ads, local SEO and landing pages built around your practice areas. Does your firm rely on referrals and word of mouth, with case flow that goes up and down?',
            "When someone needs a lawyer, they search online and reach out to one of the first firms they trust. We make sure that firm is yours, so you spend less time chasing work and more time practising law.",
        ],
        "cta2": ("Check your visibility", "#advantage"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free legal marketing call",
        "sub": "Tell me about your firm and I will show you how to bring in more of the clients you want.",
        "submit": "Request my free marketing call",
        "company_label": "Firm name",
        "steps": [
            {"label": "Firm", "fields": [
                {"type": "radio", "name": "firm_size", "label": "Firm size", "req": True,
                 "options": ["Solo lawyer", "Small firm", "Multi lawyer firm"]},
                {"type": "checkbox", "name": "practice_areas", "label": "Practice areas you want more cases in",
                 "options": ["Family law", "Personal injury", "Criminal defence", "Corporate", "Immigration", "Property law", "Other"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourfirm.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "budget", "label": "Monthly marketing budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "checkbox", "name": "channels", "label": "What you are interested in",
                 "options": ["Google Ads", "Local SEO and Maps", "Practice area pages", "Meta Ads", "Reviews", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your firm, your location, the cases you want most, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads for lawyers", "Local SEO", "Google Maps", "Google Business Profile", "Practice area pages", "Meta Ads", "Reviews", "Intake tracking"]),
    L.split({"id": "problem", "pill": "The problem", "h2": ("Why good firms still have", "unsteady case flow"),
             "body": ["Many skilled lawyers depend on referrals and their reputation, which is valuable but unpredictable. Some months are busy and others are worryingly quiet.",
                      "The reality is that most people now search online the moment they need legal help. If your firm is not visible when they search, they contact a competitor instead. I fix this by making your firm easy to find and easy to trust exactly when clients are looking."],
             "bullets": ["People search the moment they need legal help", "They contact one of the first firms they trust", "Your firm easy to find and easy to trust"],
             "cta": CTA, "visual": search_demo}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why online marketing works", "so well for law firms"),
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Clients search when they need help", "p": "People look for a lawyer online the moment a legal problem hits. Showing up there puts you in front of clients who are ready to act."},
                          {"icon": "wallet", "h3": "Legal cases are high value", "p": "One good case can be worth a lot, so even a higher cost per lead can bring a strong return when the marketing is done right."},
                          {"icon": "target", "h3": "You can target by practice area", "p": "I reach people looking for your specific practice areas in your location, so your budget goes only to relevant clients."},
                          {"icon": "repeat", "h3": "It builds a predictable pipeline", "p": "Instead of relying only on referrals, steady marketing gives you a reliable flow of enquiries every month."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("How I bring you", "more clients"),
                           "body": ["Six pieces that work together, from the urgent search to the signed client. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.split({"id": "advantage", "anchor": "advantage", "pill": "The advantage", "h2": ("Why high intent and high value", "make legal marketing powerful"),
             "body": ["Legal searches are different from most. When someone searches for a lawyer, the need is urgent and real, and a single case can be worth a great deal to your firm.",
                      "This combination of high intent and high value makes being visible so powerful. By putting your firm at the top of search for your practice areas and backing it with strong reviews, I help you win serious clients before your competitors even get a look. In legal marketing, visibility at the right moment is everything."],
             "bullets": ["High intent: the need is urgent and real", "High value: one case can be worth a great deal", "Top of search, backed by strong reviews"],
             "visual": check_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a call or a form fill, it goes and finds you more of those, including wrong numbers and people who were only asking around.",
                        "So we connect your ads to your CRM. Each call and enquiry is saved with the ad it came from, your intake team marks which ones became consultations and signed clients, and those flow back into Google Ads as conversions. From then on the platform goes after real cases, not just enquiries."],
                  bullets=["Ad click saved with every call and enquiry", "Intake team marks consultations and signed clients in the CRM", "Signed clients sent back to Google Ads", "Reports on cost per case"]),
    L.projects_section(["trust"], ("Legal clients", "we work with"),
                       "Trust Legal, a law firm in New Delhi. We rebuilt their website from scratch and look after its maintenance and technical care."),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My law firm marketing", "process"),
                   "body": ["A clear process, not luck. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Discovery and goals", "short": "Discovery", "p": "I learn about your firm, your practice areas and the cases you want most, so we focus your marketing correctly.", "points": ["Your firm and practice areas", "The cases you want most", "Your goals"]},
                       {"h3": "Strategy", "short": "Strategy", "p": "I plan the right mix of ads, local SEO and pages for your areas, your location and your budget.", "points": ["Ads, local SEO and pages", "Planned for your location", "Planned for your budget"]},
                       {"h3": "Setup", "short": "Setup", "p": "I build your campaigns, practice area pages and profile, and set up call and intake tracking.", "points": ["Campaigns and profile", "Practice area pages", "Call and intake tracking"]},
                       {"h3": "Optimize", "short": "Optimize", "p": "I improve your results every week, lowering your cost per case and raising lead quality.", "points": ["Weekly improvements", "Lower cost per case", "Higher lead quality"]},
                       {"h3": "Report", "short": "Report", "p": "I send clear reports showing calls, enquiries and cost per case in plain language.", "points": ["Calls and enquiries", "Cost per case", "Plain language"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included", "when you work with me"),
                  "body": ["You get a complete, done for you client generation system for your firm. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free marketing call", "h3": "Want a steady flow of quality cases?",
                                       "p": "Let me look at your firm and your practice areas and show you how we can bring you more of the clients you want. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why law firms", "choose me"),
                  "body": ["You talk to the person running your marketing, and every report is about calls, enquiries and cost per case."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person running your marketing, with clear answers and fast replies."},
                      {"h3": "Focus on real cases", "p": "I care about actual enquiries and signed clients and your cost per case, not clicks and vanity numbers."},
                      {"h3": "Honest reporting", "p": "I report on calls, enquiries and cost per case in plain language, so you always know your return."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Law firms", "I work with"),
                     "body": "I help solo lawyers and multi lawyer firms across practice areas such as family law, personal injury, criminal defence, corporate, immigration and property law. Whatever your focus, I can bring you more of the right clients.",
                     "chips": [("Solo lawyers", None), ("Multi lawyer firms", None), ("Family law", None), ("Personal injury", None), ("Criminal defence", None),
                               ("Corporate", None), ("Immigration", None), ("Property law", None), ("Local businesses", None)]}),
    L.chips_section({"id": "related", "h2": ("Services behind", "your law firm marketing"),
                     "body": "The channels, pages and intake follow up that bring cases in, each with its own page if you want the detail.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to grow", "your practice?"),
               "p": "Let us talk about your firm and your practice areas and build a marketing plan that brings you a steady flow of quality clients.",
               "btn": CTA, "note": "No obligation · Free marketing call"}),
]
