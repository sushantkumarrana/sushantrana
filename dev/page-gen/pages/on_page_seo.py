# On-Page SEO Services. Copy: 10_On_Page_SEO_Services.txt
# Mocks are illustrations tagged "Example": placeholders only, no figures.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free on-page SEO audit"

# lucide heading, link and code, local to this page
L.ICON.update({
    "heading": '<path d="M6 12h12"></path><path d="M6 20V4"></path><path d="M18 20V4"></path>',
    "link": '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path>',
    "code": '<path d="m16 18 6-6-6-6"></path><path d="m8 6-6 6 6 6"></path>',
})

TAG_ON = "shrink-0 rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange"
TAG_OFF = "shrink-0 rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted"
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
MONO = "font-family:ui-monospace,SFMono-Regular,Menlo,monospace"
MIRROR_IN = "min-w-0 w-full rounded-xl border border-[var(--color-line)] bg-white px-3 py-2 text-sm text-ink outline-none transition focus:border-orange"


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


def snippet(url, title, desc, hot=False):
    look = "border-orange/30 bg-orange/5" if hot else "border-[var(--color-line)] opacity-60"
    return (f'<div class="rounded-2xl border {look} p-4"><p class="truncate text-[11px] text-muted">{E(url)}</p>'
            f'<p class="svc-serp-title mt-1 text-base font-bold leading-snug">{E(title)}</p><p class="mt-1 text-xs text-body">{E(desc)}</p></div>')


# --------------------------------------------------- live Google result preview

serp = figure("Google result preview", ["Live demo"], (
    f'<label class="block"><span class="{CAP}">Type a page title</span>'
    f'<input data-mirror="title" placeholder="Your Service in Your City | Your Business" class="mt-1.5 {MIRROR_IN}" aria-label="Page title to preview"/></label>'
    f'<label class="mt-3 block"><span class="{CAP}">Type a meta description</span>'
    f'<input data-mirror="desc" placeholder="A short summary with your keyword that makes people want to click." class="mt-1.5 {MIRROR_IN}" aria-label="Meta description to preview"/></label>'
    f'<p class="mt-5 {CAP}">How it can look on Google</p>'
    '<div class="mt-2.5 rounded-2xl border border-orange/30 bg-orange/5 p-4"><p class="text-[11px] text-muted">yourbusiness.com › your-page</p>'
    '<p class="svc-serp-title mt-1 text-base font-bold leading-snug"><span data-mirror-out="title"></span></p>'
    '<p class="mt-1 text-xs text-body"><span data-mirror-out="desc"></span></p></div>'
    '<div class="mt-3 grid gap-3" aria-hidden="true">'
    + '<div class="rounded-2xl border border-[var(--color-line)] p-4 opacity-60"><span class="block h-2 w-24 rounded-full bg-ink/10"></span>'
      '<span class="mt-2 block h-3 w-3/4 rounded-full bg-ink/15"></span><span class="mt-2 block h-2 w-full rounded-full bg-ink/10"></span></div>' * 2
    + "</div>" + note("The title is the clickable headline people read before they choose a result.", "search")
))

# --------------------------------------------------- "what I optimize" mocks

outline = "".join(
    f'<div class="flex items-center gap-2 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2" style="margin-left:{lvl * 1.25}rem">'
    f'<span class="{TAG_ON}">{tag}</span><span class="truncate text-xs font-semibold text-ink">{E(t)}</span></div>'
    for lvl, tag, t in [(0, "H1", "Your Service in Your City"), (1, "H2", "What is included"), (1, "H2", "How it works"),
                        (2, "H3", "Step one"), (2, "H3", "Step two"), (1, "H2", "Common questions")])

hub = ('<div class="grid grid-cols-3 gap-2">' + "".join(
    f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3 text-center"><span class="mx-auto grid h-9 w-9 place-items-center rounded-xl bg-orange/10 text-orange">{svg("file", "h-4 w-4")}</span>'
    f'<p class="mt-2 text-[11px] font-bold leading-tight text-ink">{t}</p></div>' for t in ("Blog post", "Related service", "Home page"))
    + f'</div><div class="mt-3 mb-3 flex justify-center text-orange" aria-hidden="true"><span style="transform:rotate(90deg)">{svg("chev", "h-6 w-6")}</span></div>'
    '<div class="grad-ink-orange rounded-2xl p-4 text-center"><p class="text-sm font-extrabold text-white">Your most important page</p>'
    '<p class="mt-1 text-[11px] text-white/75">Linked with clear, descriptive anchor text</p></div>')

MOCKS = {
    "keywords": figure("Keyword map", ["Example"], rows([
        ("/", "Your brand and main service", "Mapped", True),
        ("/services/service-one/", "Service one in your city", "Mapped", True),
        ("/blog/how-to-choose/", "How to choose service one", "Mapped", True),
        ("/services/service-one-old/", "Same search as service one", "Merged", False),
    ]) + note("One page, one clear search, no pages competing with each other.", "search")),
    "titles": figure("Title and description", ["Example"], (
        f'<p class="{CAP}">Before</p><div class="mt-2">' + snippet("yourbusiness.com", "Home", "Welcome to our website. We offer many services.") + "</div>"
        f'<p class="mt-4 {CAP}">After</p><div class="mt-2">'
        + snippet("yourbusiness.com › your-service", "Your Service in Your City | Your Business", "What you offer, who it is for and one clear reason to click. Book online today.", True) + "</div>")),
    "headings": figure("Heading structure", ["Example"], f'<div class="grid gap-2">{outline}</div>' + note("One H1, then H2s and H3s in a clear order.", "heading")),
    "content": figure("Content against search intent", ["Example"], (
        '<p class="rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3 text-sm text-ink">'
        f'<span class="{CAP} block">The search</span>“how to choose service one”</p>'
        f'<p class="mt-4 {CAP}">What the searcher wants to know</p><div class="mt-2.5">' + rows([
            ("What it is and who it suits", "Covered in the opening section", "Answered", True),
            ("What to compare", "A clear, simple checklist", "Answered", True),
            ("Common mistakes", "Added during optimization", "Added", True),
            ("The next step", "A clear call to action", "Answered", True),
        ]) + "</div>")),
    "links": figure("Internal links", ["Example"], hub),
    "images": figure("Images and URLs", ["Example"], rows([
        ("/page?id=123", "Becomes /your-service-your-city/", "Clean URL", True),
        ("IMG_0042.jpg", "Becomes your-service-team.webp", "Renamed", True),
        ("Alt text: empty", "Becomes: Your team at work on your service", "Described", True),
        ("Large image file", "Compressed for faster loading", "Lighter", True),
    ])),
    "schema": figure("Schema markup", ["Example"], (
        code(['{ "@type": "FAQPage",', '  "mainEntity": [{', '    "@type": "Question",', '    "name": "Your common question?" }] }'])
        + f'<p class="mt-4 {CAP}">Can show in search as</p>'
        '<div class="mt-2 rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] text-muted">yourbusiness.com</p>'
        '<p class="svc-serp-title mt-1 text-base font-bold">Your Service in Your City | Your Business</p>'
        '<div class="mt-2 grid gap-1.5">' + "".join(
            f'<p class="flex items-center justify-between rounded-xl border border-[var(--color-line)] px-3 py-2 text-xs font-semibold text-ink">{t}{svg("chev", "h-3.5 w-3.5 text-muted")}</p>'
            for t in ("Your common question?", "Another common question?")) + "</div></div>")),
}

TYPES = [
    {"key": "keywords", "name": "Keyword research and mapping", "icon": "search",
     "what": "I find the right keywords for each page and map them so every page targets clear, non competing searches."},
    {"key": "titles", "name": "Title tags and meta descriptions", "icon": "pen",
     "what": "I write titles and descriptions that include your keywords and make people want to click from the search results."},
    {"key": "headings", "name": "Headings and structure", "icon": "heading",
     "what": "I set up a clean H1 and H2 structure so both Google and readers can follow your page easily."},
    {"key": "content", "name": "Content optimization", "icon": "file",
     "what": "I improve your content so it fully answers what the searcher wants, which is what Google rewards most."},
    {"key": "links", "name": "Internal linking", "icon": "link",
     "what": "I link your pages together in a smart way, which spreads authority and helps Google find and rank your important pages."},
    {"key": "images", "name": "Image and URL optimization", "icon": "image",
     "what": "I optimize your images, alt text and page URLs so nothing on the page is left holding back your rankings."},
    {"key": "schema", "name": "Schema markup", "icon": "code",
     "what": "I add structured data so Google understands your pages better and can show rich results and AI answers."},
]
for t in TYPES:
    t["mock"] = MOCKS[t["key"]]

leak_box = L.leak_check(
    "Page check", "Pick one page that should rank better, then tick everything that is true for it.",
    [("The title does not include the search it should rank for", "The title is one of the clearest signals of what a page is about."),
     ("Another of my pages targets the same keyword", "Pages that compete with each other make it harder for either to rank."),
     ("It repeats a keyword instead of answering the question", "Google rewards the page that fully answers what the searcher wants."),
     ("It has no clear H1, or several of them", "A clean heading structure helps Google and readers follow the page."),
     ("Few of my other pages link to it", "Internal links help Google find the page and pass authority to it."),
     ("Its images have no alt text", "Alt text helps Google understand images and helps accessibility.")],
    ("Nothing ticked yet. A free audit still checks the details that are easy to miss on your own pages.",
     "A gap or two. These are usually quick fixes, and some of the fastest wins in SEO.",
     "This page is very likely held back by on-page issues. Fixing them often moves it up without needing anything else."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "search", "h3": "Keyword research and mapping", "p": "The right keyword and search intent for each page, so your pages target clear, non competing searches."},
    {"icon": "pen", "h3": "Title and meta writing", "p": "Titles and descriptions that include your keywords and make people want to click."},
    {"icon": "heading", "h3": "Heading structure", "p": "A clean H1 and H2 structure that both Google and readers can follow."},
    {"icon": "file", "h3": "Content optimization", "p": "Content improved so it fully answers what the searcher wants, in your own voice."},
    {"icon": "link", "h3": "Internal linking, images and URLs", "p": "Smart internal links, optimized images and alt text, clean URLs and schema setup."},
    {"icon": "chart", "h3": "Clear reports", "p": "Rankings, traffic and the on-page work done, in plain language, plus updates on progress."},
]

FAQ = [
    ("What is on-page SEO?", "On-page SEO is the work done on your own pages to help them rank, such as the content, titles, headings, images and internal links. It tells Google what your page is about."),
    ("What is the difference between on-page and off-page SEO?", "On-page SEO is about your own pages and content. Off-page SEO is about signals from outside your site, mainly backlinks. Both are needed for strong rankings."),
    ("What is the difference between on-page and technical SEO?", "On-page SEO focuses on content and page elements. Technical SEO focuses on the health of your site, like speed and indexing. They work together as a complete SEO plan."),
    ("What are title tags and meta descriptions?", "The title tag is the clickable headline shown in search results, and the meta description is the short summary below it. Good ones include your keyword and encourage people to click."),
    ("How important are headings for SEO?", "Very important. A clear H1 and H2 structure helps Google understand your page and helps readers follow it. Good headings often improve both rankings and time on page."),
    ("What is keyword mapping?", "Keyword mapping means giving each page its own clear keyword and search intent, so your pages do not compete with each other and each one targets the right searches."),
    ("What is search intent?", "Search intent is what the person really wants when they search. Matching your page to that intent is the most important part of ranking today, more than repeating keywords."),
    ("How does internal linking help?", "Internal links connect your pages and pass authority between them. They help Google find your important pages and can lift the rankings of the pages you link to."),
    ("Do you rewrite my content?", "I improve and expand your content where needed so it fully answers the searcher and includes the right keywords naturally. I keep your voice and message intact."),
    ("How soon will I see results?", "On-page changes often show movement within a few weeks, which makes it one of the faster parts of SEO. Bigger gains build over a couple of months."),
    ("What is image alt text?", "Alt text is a short description of an image that helps Google understand it and helps accessibility. It is a small but useful on-page ranking signal."),
    ("Do you add schema markup?", "Yes. I add structured data so Google understands your pages better and can show rich results, which also helps your content appear in AI answers."),
    ("How is on-page SEO different from writing blogs?", "Blogs are new content you create. On-page SEO is optimizing any page, new or old, so it ranks. I often improve your existing pages first, since that brings quick wins."),
    ("Can on-page SEO fix a page that dropped in rankings?", "Often yes. A page can drop when its content no longer matches what searchers want. I refresh and re-optimize it to win back its position."),
    ("What reports will I get?", "You get clear reports showing rankings, traffic and the on-page work done, in plain language, plus updates on progress."),
    ("How do I get started?", "Just book a free on-page SEO audit using the button on this page. I will review your key pages and show you how to help them rank."),
]

RELATED = [
    ("Technical SEO", "/services/technical-seo/"),
    ("Link building", "/services/link-building/"),
    ("SEO audit", "/services/seo-audit/"),
    ("Content SEO", None),
    ("Local SEO", "/services/local-seo/"),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
]

PAGE = {
    "path": "/services/on-page-seo/",
    "slug": "on-page-seo", "thanks": "seo",
    "form_name": "on_page_seo",
    "service": "On-Page SEO",
    "service_name": "On-page SEO services",
    "thanks_what": "on-page SEO audit",
    "category": "Search engine optimization",
    "service_desc": "On-page SEO covering keyword research and mapping, title tags and meta descriptions, heading structure, content optimization for search intent, internal linking, image and URL optimization, schema markup and clear reporting.",
    "audience": "Businesses with pages that should rank but do not",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What on-page SEO includes",
    "offers": GET,
    "title": "On-Page SEO Services That Rank | Sushant Rana",
    "og_title": "On-Page SEO Services That Rank",
    "og_alt": "On-page SEO services by Sushant Rana",
    "desc": "On-page SEO services that help Google understand and rank your pages, from titles and headings to content and internal links. Book a free audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("On-Page SEO", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("On-page SEO", "questions, answered"),
            "body": ["Titles, intent, content and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "On-page SEO services",
        "h1": ("On-page SEO services that turn your pages into", "ranking machines"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I optimize the content and the elements on your own pages so Google clearly understands them and ranks them for the right searches. If you have pages that should rank but just sit on page two or three of Google, on-page SEO is often the missing piece.',
            "On-page SEO is the part of SEO you have full control over, and it usually gives some of the fastest wins. We help businesses tune their pages so they climb the rankings and turn more visitors into customers.",
        ],
        "cta2": ("See what I optimize", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free on-page SEO audit",
        "sub": "Tell me about your website and I will review your key pages for free.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Pages", "fields": [
                {"type": "text", "name": "site", "label": "Website", "req": True, "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "radio", "name": "ranking", "label": "Where do your key pages rank today?", "req": True,
                 "options": ["Page one, not the top", "Page two or three", "Not ranking at all", "Not sure"]},
                {"type": "select", "name": "pages", "label": "How many pages need work?", "placeholder": "Select",
                 "options": ["1 to 10 pages", "11 to 50 pages", "51 to 200 pages", "More than 200 pages", "Not sure"]},
            ]},
            {"label": "Goals", "fields": [
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Keyword mapping", "Titles and meta", "Headings", "Content", "Internal links", "Images and URLs", "Schema", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Which pages matter most, the searches you want to win, what you have tried..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Keyword mapping", "Title tags", "Meta descriptions", "Headings", "Search intent", "Content", "Internal links", "Alt text", "Schema markup"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What on-page SEO is", "and why it matters"),
             "body": ["On-page SEO is the work you do on your own pages to help them rank, such as the content, the titles, the headings, the images and the internal links. It tells Google exactly what your page is about and why it deserves to rank.",
                      "This matters because even a great page will struggle if Google cannot clearly understand it. Good on-page SEO connects your page to the searches your customers use, which lifts your rankings and your traffic."],
             "bullets": ["Every page matched to the right search", "Titles people want to click", "Content that fully answers the searcher"],
             "cta": CTA, "visual": serp}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why on-page SEO", "gives fast wins"),
                      "body": ["It is the part of SEO you control completely, which is why it so often moves first."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "target", "h3": "It tells Google what your page is about", "p": "Clear titles, headings and content help Google match your page to the right searches. This is the base of every ranking."},
                          {"icon": "sliders", "h3": "You are in full control", "p": "Unlike links, which depend on others, on-page SEO is fully in your hands. That means faster changes and faster results."},
                          {"icon": "chart", "h3": "It lifts rankings for your keywords", "p": "Tuning your pages for the right keywords and search intent often moves you up the results without needing anything else."},
                          {"icon": "click", "h3": "Better pages convert more", "p": "Good on-page work also improves the experience for visitors, so more of them turn into leads and sales."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I optimize", "h2": ("The on-page elements", "I optimize for you"),
                           "body": ["Seven parts of every page that decide how well it ranks. Pick one to see what the work looks like."],
                           "items": TYPES})),
    L.split({"id": "intent", "pill": "The real key", "h2": ("Why matching search intent", "beats stuffing keywords"),
             "body": ["Old SEO was about repeating a keyword many times. That does not work today and can even hurt you. What Google really wants is a page that fully answers what the searcher is looking for.",
                      "So when I optimize a page, I focus on search intent, which means understanding what the person actually wants and making sure your page gives it clearly. This is the difference between a page that ranks and one that gets ignored."],
             "bullets": ["What the searcher actually wants", "Answered clearly on the page", "Keywords used naturally, not stuffed"],
             "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My on-page SEO", "process"),
                   "body": ["Five clear stages, from the first page review to reports. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "On-page audit", "short": "Audit", "p": "I review your pages to find what is missing, what is weak and what is quietly holding your rankings back.", "points": ["What is missing", "What is weak", "What holds rankings back"]},
                       {"h3": "Keyword research and mapping", "short": "Keywords", "p": "I match the right keyword and search intent to each page, so we target the correct searches.", "points": ["One keyword per page", "Search intent matched", "No pages competing"]},
                       {"h3": "Optimize your pages", "short": "Optimize", "p": "I improve titles, headings, content, images and links across your key pages, one by one.", "points": ["Titles and headings", "Content and images", "Key pages first"]},
                       {"h3": "Strengthen internal links", "short": "Links", "p": "I connect your pages with smart internal links so authority flows to the pages that matter most.", "points": ["Links to key pages", "Clear anchor text", "Authority where it counts"]},
                       {"h3": "Track and report", "short": "Report", "p": "I track your rankings and traffic and send clear reports that show the movement and the impact.", "points": ["Rankings tracked", "Traffic tracked", "Plain language reports"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my on-page SEO service"),
                  "body": ["You get a complete, done for you on-page SEO service that gets your pages ready to rank. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Are your pages not ranking as they should?",
                                       "p": "Let me take a free look at your key pages. I will show you exactly what is holding them back and how we can fix it. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for on-page SEO"),
                  "body": ["The person who reviews your pages is the person who improves them, and every report is about rankings and traffic."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person doing the work, with clear answers and fast replies."},
                      {"h3": "Intent first, not keyword stuffing", "p": "I focus on matching search intent, which is what actually ranks pages today, not outdated tricks."},
                      {"h3": "Honest reporting", "p": "I report on rankings and traffic in plain language, so you always know the value you are getting."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Websites", "I work with"),
                     "body": "Business websites, service sites, ecommerce stores and blogs across many industries. If you have pages that should rank but do not, on-page SEO can turn them around.",
                     "chips": [("Business websites", None), ("Service businesses", None), ("Ecommerce stores", None), ("Blogs", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "on-page SEO"),
                     "body": "Well tuned pages go further on a healthy site with strong links and fresh content.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to get your pages", "ranking?"),
               "p": "Let us look at your key pages together and build a plan to lift them up the results and bring you more traffic.",
               "btn": CTA, "note": "No obligation · Free on-page SEO audit"}),
]
