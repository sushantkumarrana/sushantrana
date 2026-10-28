# Enterprise SEO Services. Copy: 12_Enterprise_SEO_Services.txt
# Mocks are illustrations tagged "Example": placeholders only, no figures.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free enterprise SEO consultation"

# lucide code, local to this page
L.ICON.update({
    "code": '<path d="m16 18 6-6-6-6"></path><path d="m8 6-6 6 6 6"></path>',
})

TAG_ON = "shrink-0 rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange"
TAG_OFF = "shrink-0 rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted"
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
MONO = "font-family:ui-monospace,SFMono-Regular,Menlo,monospace"


def rows(items):
    """[(title, sub, tag, on)] as a list of white rows with a status tag."""
    return '<ul class="grid list-none gap-2.5">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid min-w-0"><span class="truncate text-sm font-bold text-ink">{E(a)}</span><span class="text-xs text-muted">{E(b)}</span></span>'
        f'<span class="{TAG_ON if on else TAG_OFF}">{E(t)}</span></li>' for a, b, t, on in items) + "</ul>"


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs font-semibold text-ink">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}{E(text)}</p>')


def code(lines):
    body = "\n".join(E(x) for x in lines)
    return f'<pre class="overflow-x-auto rounded-2xl bg-[#0a0a0a] p-4 text-[11px] leading-relaxed text-white/80" style="{MONO}">{body}</pre>'


def toggle(opts):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{E(label)}</button>'
        for i, (k, label) in enumerate(opts)) + "</div>"


# --------------------------------------------------- one page vs one template demo

TILES = 60
TILE = '<span class="block rounded {}" style="width:1.1rem;height:1.1rem"></span>'


def tiles(lit):
    return ('<div class="flex flex-wrap gap-1.5 rounded-2xl border border-[var(--color-line)] bg-white p-4" aria-hidden="true">'
            + "".join(TILE.format("bg-orange" if i < lit else "bg-ink/10") for i in range(TILES)) + "</div>")


scale = ('<div data-tabs="true">' + figure("One fix, two ways", ["Example"], (
    toggle([("page", "Fix one page"), ("template", "Fix the template")])
    + f'<p class="mt-4 {CAP}">Every page built on your product template</p>'
    + '<div class="mt-2.5" data-panel="page">' + tiles(1)
    + note("One page improved. Every other page on the template keeps the problem.", "file")
    + '</div><div class="mt-2.5" data-panel="template" hidden="">' + tiles(TILES)
    + note("Every page that uses the template improved in a single change.", "zap")
    + "</div>")) + "</div>")

# --------------------------------------------------- "what I do" mocks

tree_rows = "".join(
    f'<div class="flex items-center gap-2 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2" style="margin-left:{lvl * 1.25}rem">'
    f'{svg("chev", "h-3.5 w-3.5 shrink-0 text-orange")}<span class="flex-1 text-xs font-semibold text-ink">{E(t)}</span>'
    f'<span class="{CAP}">{E(n)}</span></div>'
    for lvl, t, n in [(0, "Home", "Hub"), (1, "Section one", "Hub"), (2, "Category", "Template"), (3, "Every product page", "Template"),
                      (1, "Section two", "Hub"), (2, "Every article", "Template")])


def bars(heights):
    return ('<div class="flex h-16 items-end gap-1" aria-hidden="true">'
            + "".join(f'<span class="block flex-1 rounded bg-orange" style="height:{h}%"></span>' for h in heights) + "</div>")


MOCKS = {
    "technical": figure("Site-wide technical fixes", ["Example"], rows([
        ("/search?q= pages", "Crawled, but worth nothing", "Blocked", True),
        ("/products/*?sort=", "Endless filter URLs", "Controlled", True),
        ("Article template", "Slow to load on every article", "Faster", True),
        ("/old-section/", "Pages no longer linked", "Reconnected", True),
    ]) + note("Crawl budget goes to the pages that earn traffic.", "search")),
    "templates": figure("Template level fix", ["Example"], (
        f'<p class="{CAP}">Product template, title pattern</p><div class="mt-2">'
        + code(["<title>{Product name} | {Category}", "       | Your Brand</title>", '<h1>{Product name}</h1>'])
        + f'</div><p class="mt-4 {CAP}">Applies to</p><div class="mt-2 flex flex-wrap gap-2">' + "".join(
            f'<span class="inline-flex items-center gap-1.5 rounded-full bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{svg("check", "h-3 w-3", 3)}{t}</span>'
            for t in ("Every product page", "New products, automatically")) + "</div>"
        + note("Change the template once, and every page built on it follows.", "layers"))),
    "architecture": figure("Site architecture", ["Example"], f'<div class="grid gap-2">{tree_rows}</div>' + note("Hubs pass authority down to the pages that matter most.", "layers")),
    "keywords": figure("Keyword strategy by section", ["Example"], rows([
        ("Category one", "Whole cluster of related searches", "Planned", True),
        ("Category two", "Whole cluster of related searches", "Planned", True),
        ("Guides section", "Questions asked before buying", "Planned", True),
        ("Brand pages", "Searches for your brand and products", "Planned", True),
    ])),
    "content": figure("Content gap plan", ["Example"], rows([
        ("Topic one", "A big competitor ranks, you have no page", "Create", True),
        ("Topic two", "Your page is thin", "Expand", True),
        ("Topic three", "Several pages compete", "Merge", True),
        ("Topic four", "Already covered well", "Keep", False),
    ]) + note("Content planned in a format your team can produce at scale.", "file")),
    "reporting": figure("Stakeholder report", ["Example"], (
        '<div class="grid grid-cols-3 gap-2">' + "".join(
            f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3"><p class="text-[10px] font-bold uppercase leading-tight tracking-wider text-muted">{t}</p>'
            f'<div class="mt-2">{bars(h)}</div></div>'
            for t, h in (("Organic traffic", [30, 38, 45, 52, 60, 72]), ("Rankings", [40, 42, 50, 55, 63, 70]), ("Business impact", [25, 30, 40, 48, 58, 66])))
        + '</div><div class="mt-4 rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">For leadership</p>'
        '<p class="mt-1 text-sm font-bold text-ink">What changed, what it is worth, what comes next</p>'
        '<span class="mt-2 block h-2 rounded-full bg-ink/10" aria-hidden="true"></span><span class="mt-2 block h-2 w-2/3 rounded-full bg-ink/10" aria-hidden="true"></span></div>')),
}

TYPES = [
    {"key": "technical", "name": "Large scale technical SEO", "icon": "shield",
     "what": "I fix crawl budget, indexing, speed and structure issues at the level that affects your whole site, not just a few pages."},
    {"key": "templates", "name": "Scalable on-page and templates", "icon": "code",
     "what": "I improve your page templates so a single change lifts every page that uses it, from products to articles."},
    {"key": "architecture", "name": "Site architecture", "icon": "layers",
     "what": "I plan a clean structure and internal linking so authority flows to your most valuable pages across a huge site."},
    {"key": "keywords", "name": "Keyword strategy at scale", "icon": "search",
     "what": "I build a keyword strategy across whole categories and sections, not just a handful of pages."},
    {"key": "content", "name": "Content strategy", "icon": "file",
     "what": "I plan content that can be produced at scale and that fills the gaps where your big competitors are winning."},
    {"key": "reporting", "name": "Reporting for stakeholders", "icon": "chart",
     "what": "I create clear reports that make sense to both marketing teams and senior management, so SEO stays supported."},
]
for t in TYPES:
    t["mock"] = MOCKS[t["key"]]

leak_box = L.leak_check(
    "Scale check", "Tick everything that sounds like your website.",
    [("SEO fixes on my site are made one page at a time", "On a large site, the biggest gains come from the template behind many pages."),
     ("The same SEO issue shows up on many pages", "A repeated issue usually points to one template that needs one fix."),
     ("Google crawls lots of pages that do not matter", "Crawl budget spent on low value pages is not spent on your best ones."),
     ("SEO changes wait a long time for sign off", "Recommendations that are easy to understand and approve get live faster."),
     ("Leadership cannot see what SEO is worth", "Without clear reporting, SEO loses the support it needs."),
     ("We lost traffic after a release or redesign", "Large sites often lose traffic due to template or technical issues.")],
    ("Nothing ticked yet. A free consultation still looks for the template level wins that are easy to miss.",
     "A few signs. These are usually where the first template level wins are.",
     "Your site is very likely leaving traffic on the table at scale. The right template fix can lift thousands of pages at once."),
    CTA, "Signs ticked")

GET = [
    {"icon": "search", "h3": "Deep technical and content audit", "p": "A full review of your large site that finds the patterns and template issues affecting the most pages."},
    {"icon": "sliders", "h3": "A prioritized roadmap", "p": "Every fix sorted by impact, so your time and budget go to the work that moves the needle."},
    {"icon": "code", "h3": "Template level fixes", "p": "Changes planned at the template and technical level, so each one improves many pages at once."},
    {"icon": "layers", "h3": "Architecture and internal linking plans", "p": "A clean structure that sends authority to your most valuable pages across the whole site."},
    {"icon": "file", "h3": "Scalable keyword and content strategy", "p": "Keywords planned across whole sections, and content your teams can produce at scale."},
    {"icon": "chart", "h3": "Stakeholder ready reporting", "p": "Traffic, rankings and business impact reported in language both teams and leadership can act on."},
]

FAQ = [
    ("What is enterprise SEO?", "Enterprise SEO is SEO for large websites with thousands of pages, many teams and complex systems. It focuses on template level and pattern level work rather than fixing pages one by one."),
    ("How is enterprise SEO different from normal SEO?", "Normal SEO often fixes single pages. Enterprise SEO works at scale, where one template fix can improve thousands of pages, and where technical complexity and team approvals matter much more."),
    ("What counts as a large website?", "There is no exact line, but sites with thousands of pages, large catalogs or lots of content usually need an enterprise approach because their scale changes how SEO works."),
    ("Why does scale change SEO so much?", "At scale, small mistakes repeat across the whole site and small wins multiply. The focus moves from individual pages to the patterns and templates behind them."),
    ("What are template level fixes?", "A template is the design used by many pages, like all product pages or all articles. Fixing SEO issues in a template improves every page that uses it in one change."),
    ("How do you handle thousands of pages?", "I focus on the patterns and templates that affect the most pages, and on technical issues like crawl budget and indexing, so my work scales across your whole site."),
    ("Do you work with our in-house team?", "Yes. Enterprise SEO needs teamwork. I work with your marketing, content and development teams, and I make changes easy to understand and approve."),
    ("How long does it take to see results?", "Enterprise sites can see meaningful gains within a few months once template and technical fixes go live, and results keep growing as the strategy rolls out."),
    ("Can you handle multiple locations or languages?", "Yes. I can plan and manage SEO for multi location and multi language sites, including the technical setup that helps each version rank in the right place."),
    ("How do you report to management?", "I create clear reports that show traffic, rankings and business impact in language that both marketing teams and senior leaders can act on."),
    ("What tools do you use?", "I use enterprise grade crawlers, Google Search Console and analytics tools, but the real value is in knowing which large scale fixes actually move the needle."),
    ("Can you fix a big site that lost traffic?", "Yes. Large sites often lose traffic due to template or technical issues. I find the cause, fix it at scale and work to recover your rankings."),
    ("Do you do the work or just advise?", "Both. I create the strategy and roadmap and work hands on with your teams to get the changes live, rather than just handing over a report."),
    ("What reports will I get?", "You get clear reports showing traffic, rankings and the impact of the work at scale, made to suit both your team and your leadership."),
    ("How do I get started?", "Just book a free enterprise SEO consultation using the button on this page. I will review your site and show you the biggest opportunities to grow."),
]

RELATED = [
    ("Technical SEO", "/services/technical-seo/"),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
    ("On-page SEO", "/services/on-page-seo/"),
    ("SEO audit", "/services/seo-audit/"),
    ("Content SEO", None),
    ("Reporting dashboards", None),
]

PAGE = {
    "path": "/services/enterprise-seo/",
    "slug": "enterprise-seo", "thanks": "seo",
    "form_name": "enterprise_seo",
    "service": "Enterprise SEO",
    "service_name": "Enterprise SEO services",
    "thanks_what": "enterprise SEO consultation",
    "category": "Search engine optimization",
    "service_desc": "Enterprise SEO for large websites covering large scale technical SEO, template level on-page fixes, site architecture and internal linking, keyword and content strategy at scale, work with in-house teams and stakeholder ready reporting.",
    "audience": "Large brands, big ecommerce stores, publishers and SaaS companies with large websites",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What enterprise SEO includes",
    "offers": GET,
    "title": "Enterprise SEO Services for Large Sites | Sushant Rana",
    "og_title": "Enterprise SEO Services for Large Sites",
    "og_alt": "Enterprise SEO services by Sushant Rana",
    "desc": "Enterprise SEO services for large websites with thousands of pages, using template level fixes and a clear strategy. Book a free consultation.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Enterprise SEO", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Enterprise SEO", "questions, answered"),
            "body": ["Scale, templates, teams and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Enterprise SEO services",
        "h1": ("Enterprise SEO services that grow traffic", "across large websites"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I run enterprise SEO that grows traffic across large, complex websites in a smart and scalable way. If you run a large website with thousands of pages and its SEO is not living up to its size, it needs a very different approach from a small site.',
            "On a large site, one clever fix can improve thousands of pages at once. We help big brands, large stores and content heavy sites unlock the traffic their size deserves.",
        ],
        "cta2": ("See what I do", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free enterprise SEO consultation",
        "sub": "Tell me about your website and I will review it for free.",
        "submit": "Request my free consultation",
        "steps": [
            {"label": "Website", "fields": [
                {"type": "text", "name": "site", "label": "Website", "req": True, "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "radio", "name": "site_type", "label": "What kind of site is it?", "req": True,
                 "options": ["Large brand site", "Ecommerce store", "Publisher or content site", "SaaS", "Multi location or language"]},
                {"type": "select", "name": "pages", "label": "Roughly how many pages?", "req": True, "placeholder": "Select",
                 "options": ["1,000 to 10,000", "10,000 to 100,000", "More than 100,000", "Not sure"]},
            ]},
            {"label": "Goals", "fields": [
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Technical SEO at scale", "Templates", "Site architecture", "Keyword strategy", "Content strategy", "Stakeholder reporting", "Traffic recovery"]},
                {"type": "checkbox", "name": "teams", "label": "Teams you have in-house", "options": ["Marketing", "Content", "Development", "None yet"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your platform, recent changes, what leadership wants to see..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Template level fixes", "Crawl budget", "Indexing at scale", "Site architecture", "Internal linking", "Keyword strategy", "Content at scale", "Stakeholder reporting"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What enterprise SEO is", "and why it is different"),
             "body": ["Enterprise SEO is SEO for large websites, usually those with thousands or even millions of pages, many teams and complex systems. It is not just bigger SEO, it is a different way of working.",
                      "On a large site you cannot fix pages one by one. You have to work at the template level, plan at scale and work with several teams to get changes live. Done right, the results can be huge because every improvement is multiplied across many pages."],
             "bullets": ["Work at the template level", "Plans built for scale", "Changes live with your teams"],
             "cta": CTA, "visual": scale}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it is different", "h2": ("Why large websites need", "a special SEO approach"),
                      "body": ["Size changes the rules. What works page by page on a small site does not work across thousands of pages."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "layers", "h3": "Scale changes everything", "p": "With thousands of pages, small mistakes repeat across the whole site and small wins multiply. The focus shifts from single pages to patterns and templates."},
                          {"icon": "sliders", "h3": "More technical complexity", "p": "Large sites have crawl budget limits, complex code and many moving parts. Technical SEO becomes far more important and more challenging."},
                          {"icon": "users", "h3": "Many stakeholders and approvals", "p": "Changes often need sign off from several teams. Part of my job is making SEO easy to understand and approve, so good ideas actually get live."},
                          {"icon": "zap", "h3": "Template level impact", "p": "Fixing one page template can improve thousands of pages instantly. This is the biggest advantage of enterprise SEO when it is done well."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The enterprise SEO work", "I do for you"),
                           "body": ["Six parts of SEO planned for the size of your site. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.split({"id": "advantage", "pill": "The advantage", "h2": ("Why one fix can improve", "thousands of pages"),
             "body": ["The real power of enterprise SEO is leverage. On a small site, fixing a title tag helps one page. On a large site, fixing a title tag in a template can help thousands of pages in a single change.",
                      "This is why I focus on finding the patterns and template level issues that hold back your whole site. The right fix here can bring a jump in traffic that no amount of single page work could match."],
             "bullets": ["Patterns found across the whole site", "Template issues fixed once", "Every page on the template lifted"],
             "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My enterprise SEO", "process"),
                   "body": ["Five clear stages, from the deep audit to reporting leadership can act on. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Deep audit and priorities", "short": "Audit", "p": "I audit your large site to find the patterns and template issues that affect the most pages, then sort them by impact.", "points": ["Patterns across the site", "Template issues", "Sorted by impact"]},
                       {"h3": "Template and technical fixes", "short": "Templates", "p": "I plan fixes at the template and technical level, so each change improves many pages at once.", "points": ["Template changes", "Technical fixes", "Many pages per change"]},
                       {"h3": "Scalable content and structure", "short": "Content", "p": "I plan content and internal linking that can grow with your site and fill your biggest gaps.", "points": ["Content gaps filled", "Internal linking plan", "Built to grow"]},
                       {"h3": "Work with your teams", "short": "Teams", "p": "I work closely with your marketing, content and development teams to get the changes live smoothly.", "points": ["Marketing and content", "Development", "Changes easy to approve"]},
                       {"h3": "Measure and report", "short": "Report", "p": "I track traffic and rankings at scale and report in a way that both teams and leadership can act on.", "points": ["Traffic at scale", "Rankings at scale", "Reports leadership can act on"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my enterprise SEO service"),
                  "body": ["You get senior, hands on SEO for your large website, from strategy to the actual work. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Is your large website underperforming in search?",
                                       "p": "Let me review your site and show you the template level opportunities that could lift thousands of pages at once. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why large brands choose me", "for enterprise SEO"),
                  "body": ["Senior attention on the fixes that matter, and reporting that keeps SEO supported."],
                  "cards": [
                      {"h3": "Direct senior expertise", "p": "You work directly with an experienced SEO, not a junior handed a huge account. The strategy and the key work come from me."},
                      {"h3": "Process and priorities", "p": "I focus on the template and pattern level fixes that move the needle, so your time and budget go to high impact work."},
                      {"h3": "Reporting leaders understand", "p": "I report in clear language that makes the value of SEO obvious to your leadership and easy to support."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Large websites", "I work with"),
                     "body": "Large brands, big ecommerce stores, publishers, SaaS companies and multi location or multi language sites. If your site has thousands of pages, enterprise SEO can unlock its full potential.",
                     "chips": [("Large brands", None), ("Big ecommerce stores", None), ("Publishers", None),
                               ("SaaS companies", None), ("Multi location sites", "/services/local-seo/"), ("Multi language sites", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "enterprise SEO"),
                     "body": "Large sites need the technical, content and reporting sides handled as one plan.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to unlock your", "large website's potential?"),
               "p": "Let us look at your site and its templates together and build an enterprise SEO plan that grows traffic across thousands of pages.",
               "btn": CTA, "note": "No obligation · Free enterprise SEO consultation"}),
]
