# Link Building Services. Copy: 13_Link_Building_Services.docx
# No numbers beyond the shared hero stats. Mocks are labelled "Example".
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free backlink audit"

# ------------------------------------------------------------ mock helpers
TONE = {"ok": "bg-ink/[0.06] text-ink", "warn": "bg-orange/10 text-orange", "bad": "bg-red-50 text-red-700",
        "hot": "bg-orange text-white", "off": "bg-ink/[0.06] text-muted"}


def tag(text, tone="ok"):
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {TONE[tone]}">{E(text)}</span>'


def rows(items):
    """items = [(title, right_html, sub)]"""
    return '<ul class="grid list-none gap-2.5">' + "".join(
        '<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid min-w-0"><span class="truncate text-sm font-bold text-ink">{E(t)}</span>'
        + (f'<span class="text-xs text-muted">{E(s)}</span>' if s else "") + f'</span>{r}</li>'
        for t, r, s in items) + "</ul>"


def note(text):
    return ('<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg("target", "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def lines(*widths):
    return "".join(f'<span class="mt-2 block h-2 {w} rounded-full bg-ink/10"></span>' for w in widths)


def toggle(pairs, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(label)}</button>'
        for i, (k, label) in enumerate(pairs)) + "</div>"


YES = svg("check", "h-4 w-4 text-orange", 3)
NO = svg("minus", "h-4 w-4 text-muted", 3)

# --------------------------------------------- 01 basics: votes of trust demo
VOTERS = [("Industry news site", False, True), ("Trade association", False, True), ("Relevant blog", True, True), ("Partner website", False, True)]


def voter_rows(rival):
    return rows([(n, tag("Links here", "warn") if (r if rival else y) else tag("No link", "off"), "") for n, y, r in VOTERS])


votes = '<div data-tabs="true">' + figure("Votes of trust", ["Example"], (
    toggle([("you", "Your site"), ("rival", "Competitor")])
    + '<p class="mt-4 text-[10px] font-bold uppercase tracking-wider text-muted">Same kind of content. Trusted sites that link to it:</p>'
    f'<div class="mt-2.5" data-panel="you">{voter_rows(False)}'
    + note("<strong class=\"font-semibold text-ink\">Fewer votes of trust,</strong> so Google has less reason to put you first.")
    + f'</div><div class="mt-2.5" data-panel="rival"{HID}>{voter_rows(True)}'
    + note("<strong class=\"font-semibold text-ink\">More votes of trust,</strong> which is often why they outrank you with similar content.")
    + "</div>")) + "</div>"

# ------------------------------------------------- 03 what I do: tab mocks


def gap_row(name, them, you, head=False):
    if head:
        return ('<li class="flex items-center gap-3 px-4 text-[10px] font-bold uppercase tracking-wider text-muted">'
                '<span class="flex-1">Linking site</span><span class="w-16 text-center">Competitor</span><span class="w-16 text-center">You</span></li>')
    hot = them and not you
    look = "border-orange bg-[#fff7f3]" if hot else "border-[var(--color-line)] bg-white"
    return (f'<li class="flex items-center gap-3 rounded-2xl border {look} px-4 py-3"><span class="flex-1 truncate text-sm font-bold text-ink">{E(name)}</span>'
            f'<span class="grid w-16 place-items-center">{YES if them else NO}</span><span class="grid w-16 place-items-center">{YES if you else NO}</span></li>')


MOCKS = {
    "audit": figure("Backlink audit", ["Example"], rows([
        ("relevantblog.com", tag("Helping"), "Relevant and trusted"),
        ("industrynews.com", tag("Helping"), "Strong and on topic"),
        ("tradeassociation.org", tag("Missing", "warn"), "Your competitors have it, you do not"),
        ("cheap-links.xyz", tag("Harmful", "bad"), "Spammy and unrelated"),
    ])),
    "gap": figure("Competitor link gap", ["Example"], (
        '<ul class="grid list-none gap-2.5">' + gap_row("", 0, 0, True)
        + gap_row("Industry news site", True, False) + gap_row("Relevant blog", True, True)
        + gap_row("Trade association", True, False) + gap_row("Local directory", True, True) + "</ul>"
        + note("The highlighted sites link to your competitor and not to you. Those are the targets."))),
    "guest": figure("Guest post", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[10px] font-bold uppercase tracking-wider text-muted">Relevant industry website · Guest article</p>'
        '<p class="mt-1 text-base font-bold leading-snug text-ink">A genuinely useful article written for their readers</p>'
        + lines("w-full", "w-5/6") +
        '<p class="mt-3 text-xs text-body">...as the team at <span class="font-semibold text-orange underline">Your Business</span> explains in their guide...</p>'
        + lines("w-full", "w-2/3") + '</div>'
        + note("Authority from the link, plus readers who click through to you."))),
    "insert": figure("Link insertion", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4"><div class="flex items-center justify-between gap-3">'
        '<p class="text-[10px] font-bold uppercase tracking-wider text-muted">Existing article on a trusted site</p>' + tag("Link added", "warn") + '</div>'
        + lines("w-full", "w-5/6", "w-full") +
        '<p class="mt-3 text-xs text-body">An existing sentence on the topic now points readers to '
        '<span class="rounded bg-orange/10 px-1 font-semibold text-orange underline">yourbusiness.com/guide</span>, right where it fits.</p>'
        + lines("w-3/4") + '</div>'
        + note("The page already has readers and trust. Your link sits inside content that is relevant to you."))),
    "pr": figure("Digital PR", ["Example"], (
        '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><div class="bg-[#0a0a0a] px-4 py-2.5 text-xs font-extrabold uppercase tracking-wider text-white">Industry news</div>'
        '<div class="p-4"><p class="text-base font-bold leading-snug text-ink">A story on a news or industry site</p>' + lines("w-full", "w-5/6") +
        '<div class="mt-3 flex flex-wrap gap-2">' + tag("Mentions Your Business", "warn") + tag("Links to yourbusiness.com", "warn") + '</div></div></div>'
        + note("Mentions and links from news and industry sites are some of the strongest you can get."))),
    "disavow": figure("Toxic link cleanup", ["Example"], (
        '<div class="rounded-2xl bg-[#0a0a0a] p-4 text-xs leading-relaxed text-white/80"><p class="text-white/60"># Links we ask Google to ignore</p>'
        '<p>domain:cheap-links.xyz</p><p>domain:spam-directory.example</p></div>'
        '<div class="mt-4">' + rows([("Harmful links found", tag("Step 1", "off"), "From the backlink audit"),
                                     ("Removal requested", tag("Step 2", "off"), "Asked the site owner first"),
                                     ("Disavowed", tag("Step 3", "hot"), "Google told to ignore the rest")]) + '</div>')),
}

WORK = [
    ("audit", "Backlink audit", "search", "I review your current links to see what is helping, what is missing and whether any harmful links need to be dealt with."),
    ("gap", "Competitor link gap", "users", "I study the links your competitors have that you do not, so we target the ones that will help you most."),
    ("guest", "Guest posting", "pen", "I earn links through quality articles on real, relevant websites, which brings both authority and referral traffic."),
    ("insert", "Link insertions", "layers", "I place your links inside existing, relevant content on trusted sites, which can be a natural and effective way to build authority."),
    ("pr", "Digital PR and mentions", "zap", "I earn mentions and links from news and industry sites, which are some of the strongest links you can get."),
    ("disavow", "Disavowing toxic links", "shield", "If harmful links are dragging you down, I identify them and help remove or disavow them to protect your rankings."),
]

# ------------------------------------------------ 04 white hat: risk check
risk_box = L.leak_check(
    "Risky link check", "Tick everything that sounds like your site.",
    [("Someone offered me hundreds of links for a small fee", "Cheap bulk links are usually spammy and can get your site penalized."),
     ("My links come from sites unrelated to my business", "Unrelated links pass little value and can look unnatural to Google."),
     ("My rankings jumped, then dropped suddenly", "Spammy links can boost you for a while and then wipe out your rankings."),
     ("I have never checked who links to my site", "Harmful links can sit there quietly and drag your rankings down.")],
    ("Nothing ticked. A free backlink audit still checks for harmful links you cannot see from the outside.",
     "A risk or two. These are the first things I look at in a backlink audit.",
     "Your link profile may be at risk. Let me check it before it costs you rankings."),
    CTA, "Risks ticked")

# ------------------------------------- 05 quality beats quantity: the scale
dots = "".join('<span class="h-2 w-2 rounded-full bg-ink/15"></span>' for _ in range(100))


def checks(items, tone):
    return '<ul class="mt-3 grid list-none gap-1.5">' + "".join(
        f'<li class="flex items-center gap-2 text-xs font-semibold {tone}">{YES if tone == "text-ink" else NO}{E(t)}</li>' for t in items) + "</ul>"


scale = figure("One strong link vs a hundred weak ones", ["Example"], (
    '<div class="grid gap-3 sm:grid-cols-2">'
    '<div class="rounded-2xl border-2 border-orange bg-[#fff7f3] p-4">'
    f'<span class="grid h-10 w-10 place-items-center rounded-xl bg-orange text-white">{svg("shield", "h-5 w-5")}</span>'
    '<p class="mt-3 text-sm font-extrabold text-ink">One link from a trusted, relevant site</p>'
    + checks(["Relevant to your business", "Real traffic", "Sits inside useful content"], "text-ink") + '</div>'
    '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4">'
    f'<div class="flex flex-wrap gap-1" aria-hidden="true">{dots}</div>'
    '<p class="mt-3 text-sm font-extrabold text-ink">A hundred weak links</p>'
    + checks(["Unrelated sites", "No real visitors", "Penalty risk"], "text-muted") + '</div></div>'
    + note("<strong class=\"font-semibold text-ink\">The single strong link wins,</strong> and it is far safer.")))

# ----------------------------------------------------------------- content
GET = [
    {"icon": "search", "h3": "Backlink audit", "p": "A review of your current links: what is helping, what is missing and whether any harmful links need to be dealt with."},
    {"icon": "users", "h3": "Competitor link gap analysis", "p": "The links your competitors have that you do not, so we target the ones that will help you most."},
    {"icon": "target", "h3": "A clear strategy", "p": "A plan for which types of links and which sites will help you most, based on relevance and quality."},
    {"icon": "layers", "h3": "Quality link placements", "p": "Real links from real, relevant websites, earned through white hat methods only."},
    {"icon": "shield", "h3": "Toxic link cleanup where needed", "p": "Harmful links identified and removed or disavowed, so they stop dragging your rankings down."},
    {"icon": "chart", "h3": "Clear reports", "p": "The new links built, your authority and your rankings, reported in plain language."},
]

FAQ = [
    ("What is link building?", "Link building is the work of getting other websites to link to yours. Each quality link acts as a vote of trust that helps Google rank your site higher."),
    ("Why do backlinks matter for SEO?", "Backlinks are one of Google's top ranking signals. Quality links raise your site's authority and help your pages rank, often more than any other single factor."),
    ("Are all backlinks good?", "No. Links from trusted, relevant sites help you, but spammy or unrelated links can hurt your rankings. Quality and relevance matter far more than quantity."),
    ("What is a white hat link?", "A white hat link is one earned through safe, honest methods on a real, relevant website. These links are safe from penalties and they last, unlike cheap spammy links."),
    ("What is guest posting?", "Guest posting is writing a quality article for another relevant website, which includes a link back to your site. It builds authority and can bring referral traffic too."),
    ("How many links do I need?", "There is no magic number. One strong, relevant link is worth more than a hundred weak ones. I focus on quality and relevance, not big counts."),
    ("How do you find link opportunities?", "I study your competitors' links, your industry and trusted relevant sites to find the best places to earn links that will actually lift your rankings."),
    ("Are the links permanent?", "I aim for links that are placed to last on real, established sites. No one can promise a link stays forever, but quality placements are far more stable than cheap ones."),
    ("Can bad links hurt my site?", "Yes. Spammy or unnatural links can lower your rankings or trigger a penalty. This is exactly why I only use safe white hat methods."),
    ("What is a disavow?", "A disavow tells Google to ignore certain harmful links pointing at your site. If toxic links are hurting you, I identify them and help remove or disavow them."),
    ("How soon will I see results?", "Link building is a longer term investment. You usually see rankings improve over a couple of months as the new links gain value and trust."),
    ("Do you guarantee rankings?", "No honest SEO can guarantee exact rankings, because Google alone decides. What I promise is safe, quality links and steady, real improvement over time."),
    ("How do you measure link quality?", "I look at the trust and authority of the site, how relevant it is to you, its real traffic and where the link sits. Relevance and trust matter most."),
    ("Can you remove toxic links?", "Yes. I audit your link profile, find harmful links and help remove or disavow them so they stop dragging your rankings down."),
    ("What reports will I get?", "You get clear reports showing the new links built, your authority and your rankings, plus updates on the progress in plain language."),
    ("How do I get started?", "Just book a free backlink audit using the button on this page. I will review your link profile and show you how to grow your authority safely."),
]

RELATED = [
    ("On page SEO", "/services/on-page-seo/"),
    ("Technical SEO", "/services/technical-seo/"),
    ("Website SEO audit", "/services/seo-audit/"),
    ("Content SEO", None),
    ("Local SEO", "/services/local-seo/"),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
]

PAGE = {
    "path": "/services/link-building/",
    "slug": "link-building",
    "form_name": "link_building",
    "service": "Link Building",
    "service_name": "Link building services",
    "thanks_what": "backlink audit",
    "category": "Search engine optimization",
    "service_desc": "White hat link building covering backlink audits, competitor link gap analysis, guest posting, link insertions, digital PR, toxic link cleanup and disavows, with clear progress reports.",
    "audience": "Businesses that want higher rankings and authority on Google",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What link building includes",
    "offers": GET,
    "title": "Link Building Services (White Hat) | Sushant Rana",
    "og_title": "Link Building Services (White Hat)",
    "og_alt": "White hat link building services by Sushant Rana",
    "desc": "I build real, high quality backlinks that grow your authority and rankings, using safe white hat methods only. Book a free backlink audit with me.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Link Building", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Link building", "questions, answered"),
            "body": ["Safety, quality, timelines and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Link building services",
        "h1": ("Link building services that build", "real authority and rankings"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I build real, high quality links from trusted websites that grow your authority and push your pages up the rankings. If you have good content that still will not rank on page one, the missing piece is often backlinks.',
            "Backlinks are one of Google's strongest ranking signals, but only when they are safe and relevant. We use white hat methods only, so your links help you now and keep you safe from penalties later.",
        ],
        "cta2": ("See the link work", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free backlink audit",
        "sub": "Tell me about your site and I will review your link profile for free.",
        "submit": "Request my backlink audit",
        "steps": [
            {"label": "Website", "fields": [
                {"type": "text", "name": "site", "label": "Website", "req": True, "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "radio", "name": "built_before", "label": "Have you built links before?", "req": True,
                 "options": ["Yes, with an agency", "Yes, ourselves", "Never", "Not sure"]},
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["Rank higher for key pages", "Catch up with a competitor", "Recover from a ranking drop", "Clean up bad links", "Not sure yet"]},
            ]},
            {"label": "Needs", "fields": [
                {"type": "checkbox", "name": "work", "label": "What do you need help with?",
                 "options": ["Backlink audit", "Competitor link gap", "Guest posting", "Link insertions", "Digital PR", "Toxic link cleanup", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your main competitors, the pages you want to rank, past link work..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["White hat links", "Backlink audit", "Competitor link gap", "Guest posting", "Link insertions", "Digital PR", "Toxic link cleanup"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What link building is", "and why it matters"),
             "body": ["Link building is the work of getting other websites to link to yours. Each quality link acts like a vote of trust that tells Google your site is a reliable source worth ranking.",
                      "This matters because backlinks remain one of the top ways Google decides who ranks. If your competitors have stronger links, they often outrank you even with similar content. Good link building closes that gap."],
             "bullets": ["Real links from trusted, relevant sites", "White hat methods only", "Every new link tracked and reported"],
             "cta": CTA, "visual": votes}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why backlinks are so powerful", "for rankings"),
                      "body": ["Links are still one of the clearest signals Google uses to decide who deserves the top spots."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "chart", "h3": "Links are a top ranking signal", "p": "Google treats links as votes of trust. Quality links to your pages are one of the clearest ways to lift your rankings."},
                          {"icon": "shield", "h3": "They build authority and trust", "p": "Links from respected sites raise your whole site's authority, which helps all your pages rank better, not just the linked one."},
                          {"icon": "users", "h3": "They bring referral traffic", "p": "A good link on a relevant site also sends real visitors to you, so you get customers as well as ranking power."},
                          {"icon": "target", "h3": "They help you beat competitors", "p": "Often the only thing between you and the top spot is a stronger link profile. Closing that gap is how you overtake them."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The link building work", "I do for you"),
                           "body": ["Every link is earned on a real, relevant site. Pick one to see what the work looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WORK]})),
    L.split({"id": "whitehat", "pill": "The right way", "h2": ("Why I only build", "safe, white hat links"),
             "body": ["There are two kinds of link building. The wrong kind uses cheap, spammy links that can boost you for a while and then get you penalized, sometimes wiping out your rankings overnight.",
                      "I only use white hat methods, which means real links from real, relevant websites. This approach is slower than buying bulk links, but it is safe and it lasts. I will never put your site at risk for a quick result."],
             "visual": risk_box}),
    L.split({"id": "quality", "pill": "The real rule", "h2": ("Why quality beats quantity", "every time"),
             "body": ["Many people ask how many links they can get. That is the wrong question. One strong link from a trusted, relevant site is worth more than a hundred weak ones.",
                      "So I focus on relevance and quality, not big numbers. A smaller set of powerful, relevant links will lift your rankings far more safely than a pile of low value ones ever could."],
             "bullets": ["Relevance to your business first", "Trusted sites with real traffic", "Links placed inside useful content"],
             "visual": scale}, dark=True, flip=True),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My link building", "process"),
                   "body": ["Four clear steps, from finding the gaps to reporting on the links we earn."],
                   "steps": [
                       {"h3": "Backlink audit and gap", "short": "Audit", "p": "I review your links and compare them to your competitors to find the biggest opportunities and any risks.", "points": ["Your current links reviewed", "Competitor links compared", "Risks and opportunities listed"]},
                       {"h3": "Strategy and targets", "short": "Strategy", "p": "I plan which types of links and which sites will help you most, based on relevance and quality.", "points": ["Link types that suit you", "Target sites picked for relevance", "Quality before quantity"]},
                       {"h3": "Outreach and placement", "short": "Outreach", "p": "I reach out and earn placements on real, relevant sites, focusing on links that pass real value.", "points": ["Outreach to real sites", "Guest posts and insertions", "Links that pass real value"]},
                       {"h3": "Monitor and report", "short": "Report", "p": "I track your new links, your authority and your rankings, and report clearly on the progress.", "points": ["New links tracked", "Authority and rankings tracked", "Clear progress reports"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in my", "link building service"),
                  "body": ["You get a complete, done for you link building service that grows your authority the safe way. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Want stronger links that actually move rankings?",
                                       "p": "Let me run a free backlink audit and show you where your link profile is weak and how we can close the gap on your competitors. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for link building"),
                  "body": ["Safe methods, relevant links and honest reports from the person doing the work."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person planning and doing the work, with clear answers and fast replies."},
                      {"h3": "Safe, white hat only", "p": "I never use risky, spammy links. Your rankings are protected for the long term, not put at risk for a quick win."},
                      {"h3": "Quality and honest reporting", "p": "I focus on relevant, quality links and report on them honestly, so you always know the real value you are getting."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I build", "links for"),
                     "body": "Any business with good content that is being outranked by sites with stronger links, from online stores and local businesses to B2B and SaaS companies.",
                     "chips": [("Ecommerce stores", None), ("Local businesses", None), ("B2B companies", None),
                               ("SaaS", None), ("Healthcare", None), ("Education", "/industries/education/"),
                               ("Real estate", "/industries/real-estate/"), ("Legal firms", "/industries/legal-firms/")]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "link building"),
                     "body": "Links work best when the pages they point to are technically sound and well optimized.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to build", "real authority?"),
               "p": "Let us review your backlinks together and build a safe, quality link plan that lifts your rankings and closes the gap on your competitors.",
               "btn": CTA, "note": "No obligation · Free backlink audit"}),
]
