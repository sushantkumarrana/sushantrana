# Free Website SEO Audit. Copy: 15_Website_SEO_Audit.txt
# No numbers beyond the shared hero stats and L.PROJECTS. Report mocks use word
# ratings only (Good / Needs work), never scores, and are labelled "Example".
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Get your free website SEO audit"

# ------------------------------------------------------------ mock helpers
TONE = {"ok": "bg-ink/[0.06] text-ink", "warn": "bg-orange/10 text-orange", "bad": "bg-red-50 text-red-700",
        "hot": "bg-orange text-white", "off": "bg-ink/[0.06] text-muted"}
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
RATE = {"Good": "ok", "Needs work": "warn", "Missing": "bad", "Ahead": "ok", "Behind": "warn", "Helping": "ok", "Harmful": "bad"}


def tag(text, tone=None):
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {TONE[tone or RATE.get(text, "ok")]}">{E(text)}</span>'


def rows(items):
    """items = [(title, right_html, sub)]"""
    return '<ul class="grid list-none gap-2.5">' + "".join(
        '<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid min-w-0"><span class="truncate text-sm font-bold text-ink">{E(t)}</span>'
        + (f'<span class="text-xs text-muted">{E(s)}</span>' if s else "") + f'</span>{r}</li>'
        for t, r, s in items) + "</ul>"


def rated(items):
    """items = [(area, rating, comment)]"""
    return rows([(a, tag(r), c) for a, r, c in items])


def note(text, icon="target"):
    return ('<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def lines(*widths):
    return "".join(f'<span class="mt-2 block h-2 {w} rounded-full bg-ink/10"></span>' for w in widths)


def numbered(items):
    return '<ol class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
        f'<span class="grid"><span class="text-sm font-semibold text-ink">{E(t)}</span><span class="text-xs text-muted">{E(s)}</span></span></li>'
        for i, (t, s) in enumerate(items, 1)) + "</ol>"


def toggle(pairs, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(label)}</button>'
        for i, (k, label) in enumerate(pairs)) + "</div>"


YES = svg("check", "h-4 w-4 text-orange", 3)
NO = svg("minus", "h-4 w-4 text-muted", 3)

# ----------------------------------------- 01 basics: live audit scope demo
AREAS = ["Technical health", "On page SEO", "Site structure and links", "Backlink profile", "Content gaps", "Competitor comparison", "Mobile and local"]
scope = figure("Your website SEO audit", ["Live demo"], (
    '<label class="block"><span class="' + CAP + '">Type your website</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="site" placeholder="yourbusiness.com" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Website to preview"/></span></label>'
    '<div class="mt-4 rounded-2xl border border-orange/30 bg-orange/5 p-4">'
    f'<p class="{CAP}">Full health check for</p><p class="mt-1 truncate text-base font-extrabold text-ink"><span data-mirror-out="site"></span></p>'
    '<ul class="mt-3 grid list-none gap-1.5">' + "".join(
        f'<li class="flex items-center gap-2 text-xs font-semibold text-ink">{YES}{E(a)}</li>' for a in AREAS)
    + '</ul></div>' + note("<strong class=\"font-semibold text-ink\">Reviewed by hand,</strong> then sorted into a clear list of what to fix, in the right order.")))

# ------------------------------------------------ 03 what it covers: mocks
MOCKS = {
    "technical": figure("Technical health", ["Example"], rated([
        ("Crawling", "Good", "Google can reach your pages"),
        ("Indexing", "Needs work", "Some key pages are not indexed"),
        ("Site speed", "Needs work", "Heavy images slow the pages down"),
        ("Core Web Vitals", "Needs work", "Layout shifts while loading"),
    ])),
    "onpage": figure("On page SEO", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] text-muted">yourbusiness.com/services</p>'
        '<p class="svc-serp-title mt-1 text-base font-bold leading-snug">Home | Your Business</p>'
        '<p class="mt-1 text-xs text-body">A page title that says nothing about the service on the page.</p></div><div class="mt-4">'
        + rated([("Title", "Needs work", "Vague, no main keyword"), ("Headings", "Good", "One clear H1"),
                 ("Content", "Needs work", "Thin for what buyers want to know"), ("Keywords", "Missing", "The words buyers search are absent")]) + "</div>")),
    "structure": figure("Site structure and links", ["Example"], (
        '<div class="grid gap-2.5">'
        '<div class="rounded-2xl bg-orange px-4 py-2.5 text-center text-xs font-bold text-white">Home</div>'
        '<div class="grid grid-cols-2 gap-2.5">'
        '<div class="rounded-2xl border border-[var(--color-line)] bg-white px-4 py-2.5 text-center text-xs font-bold text-ink">Services</div>'
        '<div class="rounded-2xl border border-[var(--color-line)] bg-white px-4 py-2.5 text-center text-xs font-bold text-ink">Blog</div></div>'
        '<div class="grid grid-cols-2 gap-2.5">'
        '<div class="rounded-2xl border border-[var(--color-line)] bg-white px-4 py-2.5 text-center text-xs text-body">Service pages</div>'
        '<div class="rounded-2xl border border-[var(--color-line)] bg-white px-4 py-2.5 text-center text-xs text-body">Articles</div></div>'
        '<div class="flex items-center justify-between gap-3 rounded-2xl border border-orange bg-[#fff7f3] px-4 py-2.5">'
        '<span class="text-xs font-bold text-ink">Important page, linked from nowhere</span>' + tag("Needs work") + '</div></div>'
        + note("Authority flows through your internal links. Pages left out of the structure struggle to rank."))),
    "backlinks": figure("Backlink profile", ["Example"], rated([
        ("relevantblog.com", "Helping", "Relevant and trusted"),
        ("industrynews.com", "Helping", "Strong and on topic"),
        ("cheap-links.xyz", "Harmful", "Spammy and unrelated"),
    ]) + note("I check whether your links are helping you or holding you back.")),
    "gaps": figure("Content gaps", ["Example"], (
        '<ul class="grid list-none gap-2.5"><li class="flex items-center gap-3 px-4 text-[10px] font-bold uppercase tracking-wider text-muted">'
        '<span class="flex-1">Topic buyers search</span><span class="w-16 text-center">Competitor</span><span class="w-16 text-center">You</span></li>'
        + "".join(
            f'<li class="flex items-center gap-3 rounded-2xl border {"border-orange bg-[#fff7f3]" if them and not you else "border-[var(--color-line)] bg-white"} px-4 py-3">'
            f'<span class="flex-1 truncate text-sm font-bold text-ink">{E(t)}</span><span class="grid w-16 place-items-center">{YES if them else NO}</span>'
            f'<span class="grid w-16 place-items-center">{YES if you else NO}</span></li>'
            for t, them, you in [("Your main service", True, True), ("Service cost guide", True, False), ("Service in your city", True, False), ("How to choose a provider", True, True)])
        + "</ul>" + note("The highlighted topics are your biggest opportunities."))),
    "competitors": figure("Competitor comparison", ["Example"], (
        f'<p class="{CAP}">You compared with your top competitor</p><div class="mt-2.5">'
        + rated([("Technical health", "Ahead", "Your site is cleaner"), ("Content depth", "Behind", "They cover more topics"),
                 ("Backlinks", "Behind", "They have more trusted links"), ("Local presence", "Ahead", "Your profile is stronger")])
        + "</div>" + note("You see exactly where you are behind and how to catch up."))),
    "mobile": figure("Mobile and local", ["Example"], (
        '<div class="flex flex-col gap-4 sm:flex-row sm:items-center">'
        '<div class="mx-auto w-24 shrink-0 rounded-2xl border-2 border-ink/25 bg-white p-2" aria-hidden="true">'
        '<span class="mx-auto block h-1 w-8 rounded-full bg-ink/15"></span><span class="mt-2 block h-10 rounded-lg bg-[#fff7f3]"></span>'
        + lines("w-full", "w-2/3", "w-full") + '<span class="mt-2 block h-4 rounded-full bg-orange"></span></div>'
        + '<div class="min-w-0 flex-1">' + rated([("Mobile layout", "Good", "Easy to read on a phone"), ("Tap targets", "Needs work", "Buttons too close together"),
                 ("Google Business Profile", "Needs work", "Half set up")]) + "</div></div>")),
}

COVERS = [
    ("technical", "Technical health", "gauge", "I check crawling, indexing, site speed and Core Web Vitals, the technical issues that quietly block rankings."),
    ("onpage", "On page SEO", "file", "I review your titles, headings, content and keywords to see where your pages are weak or missing the mark."),
    ("structure", "Site structure and links", "layers", "I look at how your pages are organized and linked, since this affects how well authority flows through your site."),
    ("backlinks", "Backlink profile", "shield", "I review the links pointing to your site to see if they are helping you or holding you back."),
    ("gaps", "Content gaps", "search", "I find the topics and keywords your competitors rank for that you are missing, which are your biggest opportunities."),
    ("competitors", "Competitor comparison", "users", "I compare your site to your top competitors so you can see exactly where you are behind and how to catch up."),
    ("mobile", "Mobile and local", "phone", "I check your mobile experience and, if relevant, your local SEO and Google Business Profile."),
]

# ---------------------------------------- 04 the report: sample report mock
report = '<div data-tabs="true">' + figure("Sample audit report", ["Example"], (
    toggle([("problems", "Main problems"), ("plan", "Action plan")])
    + f'<div class="mt-4" data-panel="problems"><p class="{CAP}">In plain language, with why it matters</p><div class="mt-2.5">'
    + rated([("Technical health", "Needs work", "Key pages are not being indexed"),
             ("On page SEO", "Needs work", "Titles do not match what buyers search"),
             ("Site structure", "Good", "Pages are easy to reach"),
             ("Backlinks", "Good", "No harmful links found"),
             ("Content gaps", "Needs work", "Competitors cover topics you do not")])
    + f'</div></div><div class="mt-4" data-panel="plan"{HID}><p class="{CAP}">Sorted by impact</p><div class="mt-2.5">'
    + numbered([("Fix first", "Get the key pages indexed"), ("Fix next", "Rewrite titles on the main service pages"),
                ("Then", "Write the pages your competitors rank with"), ("Can wait", "Small fixes with little impact")])
    + "</div></div>" + note("<strong class=\"font-semibold text-ink\">No scary numbers.</strong> Just what is wrong, why it matters and what to do first."))) + "</div>"

# ------------------------------------------- 06 the difference: self check
audit_box = L.leak_check(
    "Is your last audit helping?", "Tick everything that sounds like an audit you have had before.",
    [("I ran an automated tool and got a long list of errors", "Tools give every issue the same weight, so the real problems get lost."),
     ("Nobody told me which fix matters most", "Without priorities, time and money go into things that do not move rankings."),
     ("The report felt designed to scare me into buying", "An honest audit tells you what matters and what does not."),
     ("I still do not know why my site is not ranking", "That answer is the whole point of a proper audit.")],
    ("Nothing ticked. A real review by hand still finds the quiet issues tools miss.",
     "Sounds familiar. My audit sorts every issue by impact and explains it in plain language.",
     "You have had the scary report already. Let me give you the honest one, with a plan you can act on."),
    CTA, "Signs ticked")

# ----------------------------------------------------------------- content
GET = [
    {"icon": "file", "h3": "A report you can understand", "p": "A clear report that a normal business owner can actually understand, not a wall of confusing data."},
    {"icon": "search", "h3": "The main problems explained", "p": "The issues that hold your rankings back, explained in plain language with why they matter."},
    {"icon": "target", "h3": "A prioritized action plan", "p": "What to fix first for the biggest impact, so you are never left wondering what to do next."},
    {"icon": "users", "h3": "How you compare", "p": "Where you stand against your top competitors and where your best opportunities are."},
    {"icon": "shield", "h3": "A real review, not a scan", "p": "An audit run with professional tools and real experience, reviewed by hand rather than an instant automated scan."},
    {"icon": "phone", "h3": "An optional walkthrough call", "p": "If you want, a friendly call to walk through the findings and answer your questions, with no pressure to buy anything."},
]

FAQ = [
    ("What is a website SEO audit?", "A website SEO audit is a full health check of your site's search performance. It finds the reasons your site is not ranking well and gives you a clear plan of what to fix."),
    ("Is the audit really free?", "Yes, the audit is free with no obligation. I offer it because it is a genuine way for you to see the value I can bring, whether or not you decide to work with me."),
    ("How long does the audit take?", "It usually takes me a few days to run a proper audit and prepare your report, because I review it by hand rather than sending an instant automated scan."),
    ("What does the audit cover?", "It covers your technical health, on page SEO, site structure, backlinks, content gaps, competitor comparison and your mobile and local presence."),
    ("Will you tell me why I am not ranking?", "Yes. That is the whole point. I find the real reasons your site is held back and explain them clearly, along with what to fix first."),
    ("Do I have to buy anything after the audit?", "No. There is no obligation. You are free to use the action plan yourself. If you want my help to fix things, we can talk, but there is no pressure."),
    ("What do I need to give you?", "Just your website address and a little about your business and goals. If needed, I may ask for access to your Search Console or analytics for a deeper look."),
    ("How is this different from automated audit tools?", "Automated tools spit out generic data and often miss the real issues. My audit adds a real expert's judgement, so you get insight and priorities, not just numbers."),
    ("Will you fix the issues too?", "The audit itself shows you what to fix. If you want me to carry out the fixes, I offer that as a separate service, and we can discuss it after you see the report."),
    ("Can you audit an ecommerce site?", "Yes. I audit online stores too, including the special issues stores face like duplicate content, filters and product page problems."),
    ("Do you check my backlinks?", "Yes. I review your backlink profile to see whether your links are helping you or holding you back, and whether any harmful links need attention."),
    ("Do you compare me to competitors?", "Yes. I compare your site to your top competitors so you can see exactly where you are behind and where your best opportunities are."),
    ("How detailed is the report?", "It is detailed enough to be useful but written in plain language, with the main issues and a prioritized action plan you can actually follow."),
    ("Can this help if my site was doing well but dropped?", "Yes. An audit is one of the best ways to find out why a site lost rankings, so you can fix the cause and recover."),
    ("How do I request my free audit?", "Just fill in the short form using the button on this page with your website and a little about your goals. I will take it from there."),
]

RELATED = [
    ("Technical SEO", "/services/technical-seo/"),
    ("On page SEO", "/services/on-page-seo/"),
    ("Link building", "/services/link-building/"),
    ("Content SEO", "/services/content-seo/"),
    ("Local SEO", "/services/local-seo/"),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
]

PAGE = {
    "path": "/services/seo-audit/",
    "slug": "seo-audit",
    "form_name": "seo_audit",
    "service": "SEO Audit",
    "service_name": "Website SEO audit",
    "thanks_what": "website SEO audit",
    "category": "Search engine optimization",
    "service_desc": "A free website SEO audit reviewed by hand, covering technical health, on page SEO, site structure and internal links, backlinks, content gaps, competitor comparison and mobile and local SEO, delivered as a plain language report with a prioritized action plan.",
    "audience": "Businesses with a website that is not getting the rankings or traffic it should",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What the free website SEO audit includes",
    "offers": GET,
    "title": "Free Website SEO Audit Report | Sushant Rana",
    "og_title": "Free Website SEO Audit Report",
    "og_alt": "Free website SEO audit by Sushant Rana",
    "desc": "Get a free website SEO audit that shows exactly why you are not ranking, with a clear, honest action plan. No jargon and no obligation.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("SEO Audit", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Website SEO audit", "questions, answered"),
            "body": ["What it covers, how long it takes and what happens after. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Free website SEO audit",
        "h1": ("Get a free website SEO audit that shows", "exactly why you are not ranking"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I will run a free audit of your website that shows exactly what is holding your rankings back and what to fix first. If you feel your site should rank higher but do not know what is wrong, a proper SEO audit gives you the answer.',
            "This is not an automated report full of scary numbers. It is a clear, honest review from a real SEO, with a simple action plan you can actually use, whether you work with me or not.",
        ],
        "cta2": ("See a sample report", "#report"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Get your free website SEO audit",
        "sub": "Tell me about your website and goals. I will review it by hand and send you a clear report.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Website", "fields": [
                {"type": "text", "name": "site", "label": "Website", "req": True, "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "radio", "name": "situation", "label": "Where does your site stand today?", "req": True,
                 "options": ["Never ranked well", "Rankings dropped", "Ranking, want more", "New website", "Not sure"]},
                {"type": "select", "name": "site_type", "label": "Type of website", "req": True, "placeholder": "Select your website type",
                 "options": ["Small business site", "Large site", "Online store", "Other"]},
            ]},
            {"label": "Goals", "fields": [
                {"type": "checkbox", "name": "worries", "label": "Anything you already suspect?",
                 "options": ["Technical issues", "Weak pages", "Backlinks", "Content gaps", "Competitors", "Mobile", "Local SEO", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Your goals", "placeholder": "What you sell, who you want to reach, the searches you want to rank for..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Technical health", "On page SEO", "Site structure", "Backlinks", "Content gaps", "Competitor comparison", "Mobile and local"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What a website SEO audit is", "and what it finds"),
             "body": ["A website SEO audit is a full health check of your site's search performance. It looks at the technical side, the content, the structure, the links and how you compare to your competitors.",
                      "The goal is simple. It finds the exact reasons your site is not ranking as well as it should, and it gives you a clear list of what to fix, in the right order."],
             "bullets": ["Reviewed by a real SEO, not a scan", "Every issue sorted by impact", "Free, with no obligation"],
             "cta": CTA, "visual": scope}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why you need one", "h2": ("Why every business should get", "an SEO audit"),
                      "body": ["Guessing is expensive. An audit shows you what is really going on before you spend another rupee."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "Find the hidden problems", "p": "Most sites have quiet issues that block rankings without the owner ever knowing. An audit brings them into the light."},
                          {"icon": "target", "h3": "Know why you are not ranking", "p": "Instead of guessing, you get real answers about what is holding your site back and what is costing you traffic."},
                          {"icon": "file", "h3": "Get a clear action plan", "p": "You leave with a simple, prioritized list of fixes, so you know exactly what to do next for the biggest impact."},
                          {"icon": "wallet", "h3": "Stop wasting money", "p": "An audit stops you spending on the wrong things. You focus your time and budget only on what will actually move your rankings."},
                      ]})
        + L.tabs_showcase({"id": "covers", "anchor": "types", "pill": "What it covers", "h2": ("What my website SEO audit", "covers"),
                           "body": ["Seven areas, each checked by hand. Pick one to see the kind of thing the audit finds."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in COVERS]})),
    L.split({"id": "report", "anchor": "report", "pill": "The report", "h2": ("What you get in your", "free audit report"),
             "body": ["You get a clear report that a normal business owner can actually understand, not a wall of confusing data. I explain the main problems in plain language and why they matter.",
                      "Most importantly, you get a prioritized action plan. I tell you what to fix first for the biggest impact, so you are never left wondering what to do next. This is real value you can use straight away."],
             "bullets": ["Main problems in plain language", "Why each one matters", "What to fix first, next and later"],
             "cta": CTA, "visual": report}, dark=True, flip=True),
    L.projects_section(["elixir", "achievers"], ("SEO work for", "real businesses"),
                       "Two businesses in India whose SEO we run. Pick one to see what the work changed for them."),
    L.split({"id": "difference", "pill": "The difference", "h2": ("Why my audit", "is different"),
             "body": ["Many free audits are just automated reports designed to scare you into buying. Mine is different. It is a real review from an experienced SEO, written in plain language with honest advice.",
                      "I sort the issues by impact, tell you the truth about what matters and what does not, and give you a plan you can act on even if you never hire me. That is how I earn your trust."],
             "visual": audit_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How it works", "h2": ("How the free audit", "works"),
                   "body": ["Four simple steps, from the short form to a friendly walkthrough if you want one."],
                   "steps": [
                       {"h3": "You request it", "short": "Request", "p": "You fill in the short form with your website and a little about your business and goals.", "points": ["Your website address", "Your business and goals", "Nothing to pay"]},
                       {"h3": "I analyze your site", "short": "Analyze", "p": "I run a full audit of your website using professional tools and my own experience, not just an automated scan.", "points": ["Professional tools", "Reviewed by hand", "Compared with competitors"]},
                       {"h3": "I send your report", "short": "Report", "p": "I send you a clear report with the main issues and a prioritized action plan in plain language.", "points": ["Main issues explained", "Prioritized action plan", "Plain language"]},
                       {"h3": "We discuss it", "short": "Discuss", "p": "If you want, we jump on a friendly call to walk through the findings and answer your questions. No pressure to buy anything.", "points": ["Optional call", "Your questions answered", "No pressure to buy"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "your free audit"),
                  "body": ["Real value you can use straight away, whether you work with me or not. You always deal directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Want to know exactly why you are not ranking?",
                                       "p": "Request your free website SEO audit and I will show you the real reasons your site is not performing, with a clear plan to fix it. No obligation at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses trust", "my audits"),
                  "body": ["An honest review from the person who would do the work, with no pressure attached."],
                  "cards": [
                      {"h3": "A real expert, not a tool", "p": "You get a review from an experienced SEO, not just an automated scan that misses the real issues."},
                      {"h3": "Honest and clear", "p": "I explain everything in plain language and tell you the truth, even if the answer is that only a few small fixes are needed."},
                      {"h3": "No pressure", "p": "The audit is genuinely helpful with no obligation. You can act on it yourself or work with me, the choice is yours."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Who this audit", "is for"),
                     "body": "Any business that has a website but is not getting the rankings or traffic it wants. Whether you have a small business site, a large site or an online store, the audit will show you where you stand and what to do next.",
                     "chips": [("Local businesses", "/industries/local-businesses/"), ("Ecommerce stores", "/industries/ecommerce/"), ("B2B companies", "/industries/b2b-companies/"),
                               ("SaaS", "/industries/saas/"), ("Healthcare", "/industries/healthcare/"), ("Education", "/industries/education/"),
                               ("Real estate", "/industries/real-estate/"), ("Legal firms", "/industries/legal-firms/")]}),
    L.chips_section({"id": "related", "h2": ("Where the audit", "leads next"),
                     "body": "The audit shows what to fix. These are the services that fix it, if you want my help.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to find out what is", "holding you back?"),
               "p": "Request your free website SEO audit today and get a clear, honest picture of your SEO and a simple plan to improve it.",
               "btn": CTA, "note": "No obligation · Reviewed by hand"}),
]
