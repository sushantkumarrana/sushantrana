# Education Marketing Services (industry page). Copy: 23_Education_Marketing_Services.docx
# Client work: 4S Study Abroad, Achievers Perfect Career Institute, Touch Abroad (L.PROJECTS facts only).
E, svg, figure, pill, HID = L.E, L.svg, L.figure, L.pill, L.HID

CTA = "Book your free education marketing call"

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


# --------------------------------------------------- 01: the enrolment journey check

JOURNEY = [
    ("Search: we do not show up when students search for our courses", "If you are missing here, they never get as far as comparing you."),
    ("Compare: we have no clear page for each course", "Students compare courses side by side. A focused course page wins that comparison."),
    ("Reviews: our reviews are few or out of date", "Students and parents read reviews before they enrol anywhere."),
    ("Videos: we have no demo class or video to show", "People watch videos before deciding. A free demo or webinar helps them say yes."),
    ("Follow up: counsellors call enquiries back late", "Fast follow up from your counsellors greatly improves admissions."),
]
journey_box = L.leak_check(
    "Enrolment journey check", "Follow a student from search to admission. Tick every step where your institute could be losing them.", JOURNEY,
    ("Nothing ticked. A free call still checks the steps that are hard to see from the inside.",
     "A gap or two. These are the steps I fix first, so students stop slipping away.",
     "Students are likely choosing a competitor before they ever speak to you. This is where your batches start to fill."),
    CTA, "Gaps ticked")

# --------------------------------------------------- 04: admission season planner

SEASONS = [
    ("before", "Before the season", "w-1/2", "I build interest before the season, so students already know your name when they start deciding."),
    ("peak", "During the peak", "w-full", "I scale up hard during the peak, when students are deciding, and capture demand while it is highest."),
    ("after", "After the peak", "w-24", "Demand settles, so spend settles too, instead of staying the same all year."),
]


def season_panel(k):
    _, lab, w, text = next(s for s in SEASONS if s[0] == k)
    flat = ('<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><p class="text-[10px] font-bold uppercase tracking-wider text-muted">Same spend all year</p>'
            '<div class="mt-2 h-2 overflow-hidden rounded-full bg-ink/10" aria-hidden="true"><span class="block h-full w-2/3 rounded-full bg-ink/70"></span></div></div>')
    timed = ('<div class="rounded-2xl border border-orange/30 bg-orange/5 p-3.5"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">Timed to your intake</p>'
             f'<div class="mt-2 h-2 overflow-hidden rounded-full bg-ink/10" aria-hidden="true"><span class="block h-full {w} rounded-full bg-orange"></span></div></div>')
    return f'<div class="mt-4 grid gap-3">{flat}{timed}</div><p class="mt-4 text-sm text-body"><strong class="font-semibold text-ink">{E(lab)}.</strong> {E(text)}</p>'


season_box = pick_demo("Admission season planner", "Pick a point in your intake cycle", [(k, lab) for k, lab, _, _ in SEASONS],
                       season_panel, "Exam results, new sessions and intake deadlines set the rhythm.", "chart")

# --------------------------------------------------- 03: what I do (tabs)

TYPES = [
    {"key": "gads", "name": "Google Ads for courses", "icon": "search",
     "what": "I run ads that show your institute at the top of Google when students search for your courses and coaching.",
     "mock": figure("Search ad", ["Example"], search_ad("yourinstitute.com", "Your Course In Your City | Your Institute", "What the course covers, why students choose you and one easy way to enquire.", ["Course details", "Book a demo class", "Talk to a counsellor"]))},
    {"key": "meta", "name": "Meta Ads for education", "icon": "users",
     "what": "Facebook and Instagram are powerful for education, because I can target students and parents by interest, age and location.",
     "mock": figure("Facebook and Instagram ad", ["Example"], social_ad("Your Institute", "Your next batch starts soon", "Shown to students and parents by interest, age and location", "Enquire now"))},
    {"key": "local", "name": "Local SEO and Google Business Profile", "icon": "target",
     "what": "I help your institute rank locally so nearby students find you for free when they search.",
     "mock": figure("Local pack", ["Example"], map_area() + place_rows("Your Institute", "Coaching centre · Near you", "Another institute"))},
    {"key": "landing", "name": "Course landing pages", "icon": "file",
     "what": "I build focused landing pages for each course that turn clicks into enquiries and applications.",
     "mock": figure("Course landing page", ["Example"], landing("Your course, explained simply", "Who it is for, what students learn and when the next batch starts.", ["Student name", "Phone number", "Course of interest"], "Send my enquiry"))},
    {"key": "crm", "name": "Lead forms and CRM connect", "icon": "layers",
     "what": "I set up lead forms and connect enquiries to your CRM, so your counsellors can follow up fast.",
     "mock": figure("From form to counsellor", ["Example"], steps(["A student fills in a lead form", "The enquiry lands in your CRM", "A counsellor is told straight away", "The student gets a call while still interested"]))},
    {"key": "funnel", "name": "Counselling and webinar funnels", "icon": "play",
     "what": "I set up funnels for free demos, webinars and counselling sessions, which are great for converting students.",
     "mock": figure("Webinar funnel", ["Example"], steps(["Ad invites students to a free demo or webinar", "They register on a simple page", "Reminders bring them to the session", "Counselling turns interest into an admission"]))},
]

GET = [
    {"icon": "target", "h3": "Strategy timed to your seasons", "p": "A plan built around your courses, your students and your intake goals, timed to your admission cycles."},
    {"icon": "search", "h3": "Google and Meta Ads", "p": "Ads at the top of Google when students search for your courses, and Facebook and Instagram ads that reach students and parents."},
    {"icon": "gauge", "h3": "Local SEO", "p": "Your institute ranking locally, so nearby students find you for free when they search."},
    {"icon": "file", "h3": "Course landing pages", "p": "A focused page for each course that turns clicks into enquiries and applications."},
    {"icon": "layers", "h3": "Lead forms and CRM connection", "p": "Enquiries straight into your CRM, so your counsellors can follow up fast."},
    {"icon": "play", "h3": "Counselling and webinar funnels, clear reports", "p": "Funnels for free demos, webinars and counselling sessions, with clear reports on enquiries, admissions and cost per enquiry."},
]

FAQ = [
    ("How do you get student enquiries for my institute?", "I use Google Ads, Meta Ads and local SEO to reach students and parents searching for your courses, then use landing pages and funnels to turn them into enquiries."),
    ("Which channels work best for education?", "Google Ads and Meta Ads work best, with local SEO adding free reach. Meta is strong for reaching students and parents, and Google captures active course searches."),
    ("How much should I spend on marketing?", "It depends on your courses, your area and your intake goals. On our call I will suggest a realistic budget so you get enquiries without overspending."),
    ("How soon will I see enquiries?", "Ads can bring enquiries within days, while SEO builds over a couple of months. Together they give you both fast and lasting results."),
    ("Do you do SEO or ads for education?", "Both. I combine paid ads with local SEO because together they bring more students than either alone, and I balance them to fit your budget and seasons."),
    ("Can you promote a specific course?", "Yes. I can build focused campaigns and landing pages for a single course or program, which works very well during admission drives."),
    ("Do you build landing pages for my courses?", "Yes. I build focused landing pages for each course that turn clicks into enquiries and applications, instead of sending traffic to a busy website."),
    ("Can you run admission season campaigns?", "Yes. I plan and scale your campaigns around your intake cycles, so you capture the most demand exactly when students are deciding."),
    ("Can you connect leads to my CRM?", "Yes. I connect enquiries straight into your CRM or system, so your counsellors can follow up quickly, which greatly improves admissions."),
    ("Do you set up counselling or webinar funnels?", "Yes. I set up funnels for free demos, webinars and counselling sessions, which are some of the best ways to convert students into admissions."),
    ("Can you help study abroad consultants?", "Yes. I help study abroad and career consultants reach the right students and generate quality enquiries for their programs."),
    ("How do you improve lead quality?", "I use clear targeting, honest ad messaging and qualifying questions on forms, so you get serious students rather than random clicks."),
    ("What will my cost per enquiry be?", "It varies by course and area, but my goal is always to lower it over time while keeping quality high. I track it closely so you see the real return."),
    ("What reports will I get?", "You get clear monthly reports showing enquiries, admissions and cost per enquiry, plus updates on the work done."),
    ("How do I get started?", "Just book a free education marketing call using the button on this page. I will look at your courses and show you how to get more students."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("Local SEO", "/services/local-seo/"),
    ("Landing pages", "/services/landing-pages/"),
    ("CRM consulting", None),
    ("Email automation", "/services/email-automation/"),
    ("Sales funnel setup", "/services/sales-funnel-setup/"),
]

PAGE = {
    "path": "/industries/education/",
    "slug": "education-marketing", "thanks": "industry",
    "form_name": "education_marketing",
    "service": "Education Marketing",
    "service_name": "Education marketing services",
    "thanks_what": "education marketing call",
    "category": "Lead generation for education",
    "service_desc": "Education marketing for coaching institutes, colleges, edtech brands and career consultants: Google Ads, Meta Ads, local SEO, course landing pages, lead forms and CRM connection, counselling and webinar funnels and clear reports.",
    "audience": "Coaching institutes, colleges, edtech brands and career consultants",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What education marketing includes",
    "offers": GET,
    "title": "Education Marketing Services for Admissions | Sushant Rana",
    "og_title": "Education Marketing Services for More Admissions",
    "og_alt": "Education marketing services by Sushant Rana",
    "desc": "Education marketing services that bring more student enquiries and admissions with Google Ads, Meta Ads and landing pages. Book a free call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Education", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about education marketing"),
            "body": ["Channels, seasons, budgets and follow up. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Education marketing services",
        "h1": ("Education marketing that brings you more", "student enquiries and admissions"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help coaching institutes, colleges, edtech brands and career consultants get a steady flow of student enquiries and admissions using Google Ads, Meta Ads and landing pages that convert. Do you have great courses but not enough students walking through the door? The problem is usually visibility, not quality.',
            "Students and parents research online before they enrol anywhere. If your institute is not showing up when they search, they choose a competitor. We make sure you are the option they find, trust and sign up with.",
        ],
        "cta2": ("See client work", "#work"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free education marketing call",
        "sub": "Tell me about your courses and I will show you how to bring in more student enquiries.",
        "submit": "Request my free marketing call",
        "company_label": "Institute / brand name",
        "steps": [
            {"label": "Institute", "fields": [
                {"type": "radio", "name": "institute_type", "label": "What best describes you?", "req": True,
                 "options": ["Coaching or test prep", "College or university", "Edtech or online courses", "Career or study abroad consultant", "School"]},
                {"type": "text", "name": "courses", "label": "Courses you want more students for", "placeholder": "For example: test prep, diploma, online course..."},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourinstitute.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "radio", "name": "intake", "label": "When is your next intake?",
                 "options": ["Within a month", "In 1 to 3 months", "Later than 3 months", "Rolling admissions"]},
                {"type": "select", "name": "budget", "label": "Monthly marketing budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L+", "Not decided yet"]},
                {"type": "checkbox", "name": "channels", "label": "What you are interested in",
                 "options": ["Google Ads", "Meta Ads", "Local SEO", "Course landing pages", "CRM and follow up", "Webinar funnels", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your courses, your students, where you enrol from, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Ads for courses", "Meta Ads", "Local SEO", "Course landing pages", "Lead forms", "CRM connect", "Webinar funnels", "Admission seasons"]),
    L.split({"id": "problem", "pill": "The problem", "h2": ("Why great institutes", "still have empty seats"),
             "body": ["Many institutes offer excellent teaching yet still struggle to fill their batches. They depend on word of mouth and old methods, while students and parents have moved online.",
                      "Before enrolling, people search, compare courses, read reviews and watch videos. If your institute is missing from that journey, you lose the student before you ever get a chance to speak to them. I put your courses in front of the right students at the right time."],
             "bullets": ["Students search, compare, read reviews and watch videos", "Missing from that journey means a lost student", "Your courses in front of the right students"],
             "cta": CTA, "visual": journey_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why online marketing works", "so well for education"),
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Students and parents research online", "p": "People look up courses, coaching and colleges online before deciding. Showing up there puts you in front of ready to enrol students."},
                          {"icon": "target", "h3": "You can target by course and location", "p": "I reach the exact students looking for your courses in your area, so your budget goes only to real prospects."},
                          {"icon": "users", "h3": "You fill seats predictably", "p": "Instead of hoping for walk ins, ads and SEO give you a steady, predictable flow of enquiries you can count on."},
                          {"icon": "chart", "h3": "It works around admission seasons", "p": "I can plan and scale your campaigns around your intake cycles, so you capture demand exactly when it peaks."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("How I bring you", "more student enquiries"),
                           "body": ["Six pieces that work together, from the first course search to the counselling call. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.projects_section(["4s", "achievers", "touch"], ("Education brands", "we work with"),
                       "Study abroad, aviation training and career training clients in the UAE, India and Canada. Pick one to see what we do for them."),
    L.split({"id": "seasons", "anchor": "seasons", "pill": "The advantage", "h2": ("Why timing your campaigns", "to admission seasons wins"),
             "body": ["Education runs on cycles. Demand spikes around exam results, new sessions and intake deadlines, then settles. Many institutes miss this and spend the same all year.",
                      "I plan your marketing around these cycles. I build interest before the season, scale up hard during the peak when students are deciding, and capture demand while it is highest. This timing often makes the difference between a full batch and an empty one."],
             "bullets": ["Build interest before the season", "Scale up hard during the peak", "Capture demand while it is highest"],
             "cta": CTA, "visual": season_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the wrong numbers and the people who were only browsing.",
                        "So we connect your ads to your CRM. Each enquiry is saved with the ad it came from, your counsellors mark which students applied or enrolled, and those admissions flow back into Google Ads as conversions. From then on the platform goes after students who enrol, not just forms."],
                  bullets=["Ad click saved with every student enquiry", "Counsellors mark applications and admissions in the CRM", "Admissions sent back to Google Ads", "Reports on cost per admission"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My education marketing", "process"),
                   "body": ["A clear process, not luck. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Discovery and goals", "short": "Discovery", "p": "I learn about your courses, your students and your intake goals, so we focus on the right enquiries.", "points": ["Your courses and students", "Your intake goals", "The right enquiries"]},
                       {"h3": "Strategy", "short": "Strategy", "p": "I plan the right mix of ads, SEO and funnels for your courses and your budget, timed to your seasons.", "points": ["Ads, SEO and funnels", "Planned for your budget", "Timed to your seasons"]},
                       {"h3": "Setup", "short": "Setup", "p": "I build your campaigns, landing pages and lead capture and connect everything to your CRM.", "points": ["Campaigns and landing pages", "Lead capture", "Connected to your CRM"]},
                       {"h3": "Optimize", "short": "Optimize", "p": "I improve your results every week, lowering your cost per enquiry and raising quality.", "points": ["Weekly improvements", "Lower cost per enquiry", "Higher quality"]},
                       {"h3": "Report", "short": "Report", "p": "I send clear reports showing enquiries, admissions and cost per enquiry in plain language.", "points": ["Enquiries and admissions", "Cost per enquiry", "Plain language"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included", "when you work with me"),
                  "body": ["You get a complete, done for you enquiry generation system for your institute. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free marketing call", "h3": "Want to fill your next batch with students?",
                                       "p": "Let me look at your courses and your goals and show you how we can bring you a steady flow of student enquiries. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why education brands", "choose me"),
                  "body": ["You talk to the person running your marketing, and every report is about enquiries, admissions and cost per enquiry."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person running your marketing, with clear answers and fast replies."},
                      {"h3": "Focus on real admissions", "p": "I care about actual enquiries and admissions and your cost per enquiry, not clicks and vanity numbers."},
                      {"h3": "Honest reporting", "p": "I report on enquiries, admissions and cost per enquiry in plain language, so you always know your return."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Education businesses", "I work with"),
                     "body": "I help coaching and test prep institutes, colleges and universities, edtech and online course brands, career and study abroad consultants, and schools. Whether you enrol locally or online, I can bring you more students.",
                     "chips": [("Coaching and test prep", None), ("Colleges and universities", None), ("Edtech and online courses", None),
                               ("Career and study abroad consultants", None), ("Schools", None), ("Local businesses", None)]}),
    L.chips_section({"id": "related", "h2": ("Services behind", "your education marketing"),
                     "body": "The channels, pages and follow up that turn searches into admissions, each with its own page if you want the detail.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to fill", "your batches?"),
               "p": "Let us talk about your courses and your goals and build a marketing plan that brings you a steady flow of student enquiries and admissions.",
               "btn": CTA, "note": "No obligation · Free marketing call"}),
]
