# Technical SEO Services. Copy: 09_Technical_SEO_Services.txt
# Mocks are illustrations tagged "Example": placeholders only, no figures.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free technical SEO audit"

# lucide smartphone, lock, code and star, local to this page
L.ICON.update({
    "phone2": '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"></rect><path d="M12 18h.01"></path>',
    "lock": '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path>',
    "code": '<path d="m16 18 6-6-6-6"></path><path d="m8 6-6 6 6 6"></path>',
    "star": '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path>',
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


# --------------------------------------------------- crawl > index > rank demo

pipeline = ('<div data-tabs="true">' + figure("How Google reaches your page", ["Example"], (
    toggle([("before", "Before the fix"), ("after", "After the fix")])
    + f'<p class="mt-4 {CAP}">One important page, three steps</p>'
    + '<div class="mt-2.5" data-panel="before">' + rows([
        ("1. Crawl", "Google reads the page", "Reached", True),
        ("2. Index", "A stray noindex tag blocks it", "Blocked", False),
        ("3. Rank", "The page never shows in search", "Not shown", False),
    ]) + note("Great content, but Google cannot store the page, so it cannot rank.", "search")
    + '</div><div class="mt-2.5" data-panel="after" hidden="">' + rows([
        ("1. Crawl", "Google reads the page", "Reached", True),
        ("2. Index", "Tag removed, page stored", "Indexed", True),
        ("3. Rank", "The page can now show in search", "Can rank", True),
    ]) + note("One technical fix unlocks rankings the content already deserved.", "check")
    + "</div>")) + "</div>")

# --------------------------------------------------- "what I fix" mocks


def meter(label, before, after):
    return (f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><p class="flex items-center justify-between text-xs font-bold text-ink">'
            f'<span>{E(label)}</span><span class="{TAG_ON}">Improved</span></p>'
            f'<div class="mt-2.5 grid gap-1.5" aria-hidden="true"><span class="block h-2 rounded-full bg-ink/15" style="width:{before}%"></span>'
            f'<span class="block h-2 rounded-full bg-orange" style="width:{after}%"></span></div></div>')


tree_rows = "".join(
    f'<div class="flex items-center gap-2 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2" style="margin-left:{lvl * 1.25}rem">'
    f'{svg("chev", "h-3.5 w-3.5 shrink-0 text-orange")}<span class="text-xs font-semibold text-ink">{E(t)}</span></div>'
    for lvl, t in [(0, "Home"), (1, "Services"), (2, "Service one"), (2, "Service two"), (1, "Blog"), (2, "Helpful article")])

MOCKS = {
    "crawl": figure("Crawl and index report", ["Example"], rows([
        ("/services/", "Important page", "Indexed", True),
        ("/products/product-one/", "Important page", "Indexed", True),
        ("/search?q=anything", "Internal search results", "Skipped", False),
        ("/tag/old-tag/", "Thin tag page", "Skipped", False),
    ]) + note("Google spends its time on the pages that matter.", "search")),
    "speed": figure("Core Web Vitals", ["Example"], (
        '<div class="flex items-center gap-4 text-[10px] font-bold uppercase tracking-wider text-muted">'
        '<span class="flex items-center gap-1.5"><span class="block h-2 w-4 rounded-full bg-ink/15"></span>Before</span>'
        '<span class="flex items-center gap-1.5"><span class="block h-2 w-4 rounded-full bg-orange"></span>After</span></div>'
        '<div class="mt-3 grid gap-2.5">' + meter("How quickly the page loads", 85, 40) + meter("How fast it responds", 70, 35) + meter("Whether things jump around", 60, 15) + "</div>"
        + note("Shorter bars mean a faster, steadier page.", "zap"))),
    "mobile": figure("Mobile view", ["Example"], (
        '<div class="mx-auto max-w-xs rounded-[28px] border-2 border-[var(--color-line)] bg-white p-3">'
        '<div class="mx-auto h-1.5 w-12 rounded-full bg-ink/15" aria-hidden="true"></div>'
        '<div class="mt-3 rounded-2xl bg-[#fff7f3] p-3"><p class="text-sm font-extrabold text-ink">Your Business</p>'
        '<span class="mt-2 block h-2 rounded-full bg-ink/10" aria-hidden="true"></span><span class="mt-1.5 block h-2 w-3/4 rounded-full bg-ink/10" aria-hidden="true"></span>'
        '<span class="mt-3 block rounded-xl bg-orange py-2 text-center text-xs font-bold text-white">Call now</span></div>'
        '<div class="mt-3 grid grid-cols-2 gap-2" aria-hidden="true"><span class="aspect-square rounded-xl bg-ink/5"></span><span class="aspect-square rounded-xl bg-ink/5"></span></div></div>'
        '<div class="mt-4 flex flex-wrap justify-center gap-2">' + "".join(
            f'<span class="inline-flex items-center gap-1.5 rounded-full bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{svg("check", "h-3 w-3", 3)}{t}</span>'
            for t in ("Readable text", "Easy to tap", "No sideways scrolling")) + "</div>")),
    "structure": figure("Site structure", ["Example"], (
        f'<div class="grid gap-2">{tree_rows}</div>' + note("Every important page is a few clicks from home.", "layers"))),
    "sitemap": figure("Sitemap and robots file", ["Example"], (
        f'<p class="{CAP}">robots.txt</p><div class="mt-2">'
        + code(["User-agent: *", "Disallow: /cart/", "Disallow: /search", "", "Sitemap: https://yourbusiness.com/sitemap.xml"])
        + f'</div><p class="mt-4 {CAP}">sitemap.xml</p><div class="mt-2">'
        + code(["<url><loc>https://yourbusiness.com/</loc></url>", "<url><loc>https://yourbusiness.com/services/</loc></url>"])
        + "</div>")),
    "schema": figure("Schema markup", ["Example"], (
        code(['{ "@type": "Product",', '  "name": "Product one",', '  "aggregateRating": { ... } }'])
        + f'<p class="mt-4 {CAP}">Can show in search as</p>'
        '<div class="mt-2 rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] text-muted">yourbusiness.com</p>'
        '<p class="svc-serp-title mt-1 text-base font-bold">Product one | Your Business</p>'
        '<p class="mt-1 flex items-center gap-2 text-xs text-muted"><span class="flex gap-0.5 text-orange">' + svg("star", "h-3.5 w-3.5") * 5 + '</span>Rating · In stock</p></div>')),
    "errors": figure("Error fixes", ["Example"], rows([
        ("/old-page/", "Still linked, but returns an error", "Redirected", True),
        ("/a/ to /b/ to /c/", "Redirect chain", "Shortened", True),
        ("/page/?ref=home", "Duplicate of /page/", "Canonical set", True),
        ("Broken outbound link", "Points to a page that no longer exists", "Fixed", True),
    ])),
    "security": figure("HTTPS and canonical", ["Example"], (
        '<div class="flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 text-sm text-ink">'
        f'{svg("lock", "h-4 w-4 shrink-0 text-orange")}<span class="truncate">https://yourbusiness.com/page/</span></div>'
        f'<p class="mt-4 {CAP}">In the page head</p><div class="mt-2">'
        + code(['<link rel="canonical"', '      href="https://yourbusiness.com/page/">'])
        + "</div>" + note("One secure address, and one clear version of each page to rank.", "shield"))),
}

TYPES = [
    {"key": "crawl", "name": "Crawling and indexing", "icon": "search",
     "what": "I make sure Google can find and index your important pages, and I stop it from wasting time on pages that do not matter."},
    {"key": "speed", "name": "Site speed and Core Web Vitals", "icon": "gauge",
     "what": "I improve your loading speed and Core Web Vitals, which are the speed and stability scores Google uses when ranking your site."},
    {"key": "mobile", "name": "Mobile friendliness", "icon": "phone2",
     "what": "I make sure your site looks and works well on phones, since that is what Google mainly judges."},
    {"key": "structure", "name": "Site structure and internal links", "icon": "layers",
     "what": "I organize your pages and internal links so both users and Google can move through your site easily."},
    {"key": "sitemap", "name": "Sitemap and robots file", "icon": "file",
     "what": "I set up a clean XML sitemap and a correct robots file, so Google knows what to crawl and what to skip."},
    {"key": "schema", "name": "Schema markup", "icon": "code",
     "what": "I add structured data so Google can better understand your pages and show rich results, which also helps with AI answers."},
    {"key": "errors", "name": "Fixing errors", "icon": "repeat",
     "what": "I fix broken links, wrong redirects and duplicate content that quietly drag down your rankings."},
    {"key": "security", "name": "Security and canonicals", "icon": "shield",
     "what": "I make sure your site uses secure HTTPS and correct canonical tags, so there is no confusion about which page should rank."},
]
for t in TYPES:
    t["mock"] = MOCKS[t["key"]]

leak_box = L.leak_check(
    "Technical health check", "Tick everything that sounds like your website.",
    [("Some of my pages do not show up on Google at all", "Crawl or index problems can hide a page completely."),
     ("My site feels slow, especially on phones", "A slow site loses both rankings and customers."),
     ("Things jump around while my pages load", "Layout shifts are part of Core Web Vitals and frustrate visitors."),
     ("Old links lead to error pages or long redirects", "Broken links and wrong redirects quietly drag rankings down."),
     ("I am not sure my sitemap and robots file are right", "These tell Google what to crawl and what to skip.")],
    ("Nothing ticked yet. A free audit still checks the issues that are hard to spot from the outside.",
     "An issue or two. These are usually the first things I fix on a site.",
     "A hidden technical issue is very likely blocking your rankings. Fixing it often unlocks rankings your content already deserves."),
    CTA, "Issues ticked")

GET = [
    {"icon": "search", "h3": "Complete technical audit report", "p": "A deep check of your site that finds every issue affecting your crawling, indexing, speed and rankings."},
    {"icon": "sliders", "h3": "Issues sorted by priority", "p": "A clear list of issues, sorted so the ones that will move your rankings the most get fixed first."},
    {"icon": "check", "h3": "The fixes themselves", "p": "I do not just hand you a list of problems, I fix them, carefully and without breaking your site."},
    {"icon": "gauge", "h3": "Speed and Core Web Vitals work", "p": "Heavy images, slow code and layout shifts fixed, so your pages are faster for people and stronger in search."},
    {"icon": "code", "h3": "Schema setup", "p": "Structured data that helps Google understand your pages and show rich results."},
    {"icon": "chart", "h3": "Clear reporting", "p": "Simple updates on what was fixed and the impact, plus ongoing monitoring for new issues."},
]

FAQ = [
    ("What is technical SEO?", "Technical SEO is the work that helps search engines crawl, understand and rank your website. It covers things like site speed, mobile friendliness, indexing, site structure and code level details."),
    ("How is technical SEO different from on-page SEO?", "On-page SEO is about your content, keywords and page structure. Technical SEO is about the health of your site itself, making sure Google can reach and read it. Both are needed to rank well."),
    ("What is a technical SEO audit?", "A technical SEO audit is a deep check of your website to find every issue affecting your crawling, indexing, speed and rankings. It gives a clear picture of what is holding your site back."),
    ("What are Core Web Vitals?", "Core Web Vitals are Google's scores for how fast and stable your pages feel to a real user. They look at load speed, response time and layout stability, and they affect your rankings."),
    ("Why is my site not ranking even with good content?", "Often a hidden technical issue is the cause, like slow speed, crawl problems or indexing errors. Good content cannot rank if Google cannot properly reach or understand it."),
    ("How does site speed affect SEO?", "A slow site loses rankings and visitors. Google prefers fast pages, and users leave slow ones, so improving speed helps both your rankings and your sales."),
    ("What are crawling and indexing?", "Crawling is when Google reads your pages, and indexing is when it stores them to show in search. If either fails, your pages will not appear in results at all."),
    ("What is schema markup?", "Schema markup is special code that helps Google understand your pages better. It can lead to rich results in search and also helps your content show up in AI answers."),
    ("Do you fix the issues or just find them?", "I fix them. Many services only hand you a report. I go further and make the actual changes, so your site really improves."),
    ("How long does a technical audit take?", "A full audit usually takes a few days, depending on the size of your site. I then share the findings and a clear plan sorted by priority."),
    ("What tools do you use?", "I use trusted tools like Google Search Console, PageSpeed Insights and professional crawlers to find issues, but the real value is in knowing which fixes actually move rankings."),
    ("Can technical SEO help my ecommerce store?", "Yes, a lot. Large stores often have crawl, speed and duplicate content issues. Fixing these can unlock rankings and sales across many product pages at once."),
    ("Do I need technical SEO if my site is small?", "Even small sites can have speed, mobile or indexing issues that quietly hurt rankings. A quick audit will show whether it is worth the effort for your site."),
    ("Will you break my site while fixing it?", "No. I work carefully and test every change. My goal is to improve your site safely, and I always check that everything still works after each fix."),
    ("What reports will I get?", "You get a clear audit report and simple updates showing what was fixed and the impact, all in plain language."),
    ("How do I get started?", "Just book a free technical SEO audit using the button on this page. I will check your site and show you exactly what is holding your rankings back."),
]

RELATED = [
    ("On-page SEO", "/services/on-page-seo/"),
    ("SEO audit", "/services/seo-audit/"),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
    ("Enterprise SEO", "/services/enterprise-seo/"),
    ("Local SEO", "/services/local-seo/"),
    ("Website maintenance", "/services/website-maintenance/"),
]

PAGE = {
    "path": "/services/technical-seo/",
    "slug": "technical-seo", "thanks": "seo",
    "form_name": "technical_seo",
    "service": "Technical SEO",
    "service_name": "Technical SEO services",
    "thanks_what": "technical SEO audit",
    "category": "Search engine optimization",
    "service_desc": "Technical SEO covering crawling and indexing, site speed and Core Web Vitals, mobile friendliness, site structure and internal links, XML sitemap and robots file, schema markup, error and redirect fixes, HTTPS and canonical tags, with a full audit, the fixes and ongoing monitoring.",
    "audience": "Businesses whose website is not ranking as it should",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What technical SEO includes",
    "offers": GET,
    "title": "Technical SEO Services & Audit | Sushant Rana",
    "og_title": "Technical SEO Services & Audit",
    "og_alt": "Technical SEO services by Sushant Rana",
    "desc": "Technical SEO services that fix crawl and index problems, slow speed and Core Web Vitals holding your rankings back. Book a free technical SEO audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Technical SEO", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Technical SEO", "questions, answered"),
            "body": ["Audits, speed, indexing and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Technical SEO services",
        "h1": ("Technical SEO services that fix what is", "holding your rankings back"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I find and fix the technical issues that stop Google from crawling, understanding and ranking your pages. If you have good content but your website still does not rank, the problem is often hidden in the technical side of your site.',
            "Technical SEO is the foundation that all your other SEO work sits on. If the foundation is broken, even great content and links will struggle. We help businesses of all sizes build a fast, clean and search friendly website.",
        ],
        "cta2": ("See what I fix", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free technical SEO audit",
        "sub": "Tell me about your website and I will run a free technical check.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Website", "fields": [
                {"type": "text", "name": "site", "label": "Website", "req": True, "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "radio", "name": "ranking", "label": "How is your site ranking today?", "req": True,
                 "options": ["Ranking, but stuck", "Dropped recently", "Never ranked well", "New website"]},
                {"type": "select", "name": "platform", "label": "Website platform", "placeholder": "Select your platform",
                 "options": ["WordPress", "WooCommerce", "Other ecommerce platform", "Custom build", "Other", "Not sure"]},
            ]},
            {"label": "Issues", "fields": [
                {"type": "checkbox", "name": "issues", "label": "What worries you most?",
                 "options": ["Pages not on Google", "Slow site", "Core Web Vitals", "Mobile problems", "Errors and redirects", "Schema", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What changed, which pages matter most, what you have tried..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Crawling", "Indexing", "Site speed", "Core Web Vitals", "Mobile friendly", "XML sitemap", "Schema markup", "Redirects", "Canonicals"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What technical SEO is", "and why it matters"),
             "body": ["Technical SEO is the work that helps search engines crawl your site, understand your pages and rank them without any blocks. It covers things like site speed, mobile friendliness, site structure, indexing and code level details.",
                      "This matters because Google cannot rank what it cannot properly reach or understand. Fixing technical issues often unlocks rankings that your content already deserves but was not getting."],
             "bullets": ["Google can reach every important page", "Pages stored and ready to show in search", "A fast, clean site for people and Google"],
             "cta": CTA, "visual": pipeline}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why technical SEO", "is so important"),
                      "body": ["Everything else in SEO sits on top of a healthy site. When the base is right, the rest pays off."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "search", "h3": "No rankings without crawling and indexing", "p": "If Google cannot crawl and index your pages, they simply will not show in search. Fixing this is the first step to any rankings at all."},
                          {"icon": "zap", "h3": "Speed affects rankings and sales", "p": "A slow site loses both rankings and customers. Faster pages rank better and keep more visitors, which means more leads and sales."},
                          {"icon": "phone2", "h3": "Mobile first is the standard", "p": "Google mainly looks at the mobile version of your site. If your site works poorly on phones, your rankings suffer everywhere."},
                          {"icon": "layers", "h3": "It powers all your other SEO", "p": "Content and links work far better on a clean, fast site. Technical SEO is the base that makes everything else pay off."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I fix", "h2": ("The technical issues", "I check and fix"),
                           "body": ["Eight areas that decide whether Google can reach, read and rank your site. Pick one to see what the fix looks like."],
                           "items": TYPES})),
    L.split({"id": "speed", "pill": "The speed factor", "h2": ("Why Core Web Vitals and speed", "matter so much"),
             "body": ["Core Web Vitals are Google's way of measuring how fast and stable your pages feel to a real user. They look at how quickly your page loads, how fast it responds and whether things jump around while loading.",
                      "A slow, jumpy site frustrates visitors and loses rankings and sales. I improve these scores by fixing heavy images, slow code and other issues, which makes your site faster for people and stronger in search."],
             "bullets": ["Heavy images made lighter", "Slow code cleaned up", "Layout that stays still while loading"],
             "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My technical SEO", "process"),
                   "body": ["Five clear stages, from the first audit to ongoing monitoring. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Full technical audit", "short": "Audit", "p": "I run a deep audit of your site to find every issue that is affecting your crawling, indexing, speed and rankings.", "points": ["Crawling and indexing", "Speed and Core Web Vitals", "Structure and code"]},
                       {"h3": "Prioritize by impact", "short": "Prioritize", "p": "I sort the issues so we fix the ones that will move your rankings the most, first. No time is wasted on tiny details.", "points": ["Biggest impact first", "Clear, sorted list", "No time on tiny details"]},
                       {"h3": "Fix and improve", "short": "Fix", "p": "I fix the issues carefully, from speed and mobile to structure and code, without breaking your site.", "points": ["Speed and mobile", "Structure and code", "Careful, safe changes"]},
                       {"h3": "Test and validate", "short": "Test", "p": "I test every fix to make sure it works and that Google can now crawl and read your site the right way.", "points": ["Every fix tested", "Checked in Search Console", "Site still works as before"]},
                       {"h3": "Monitor and report", "short": "Monitor", "p": "I keep watch for new issues and send you clear reports that show what was fixed and the impact.", "points": ["New issues caught early", "What was fixed", "The impact, in plain language"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my technical SEO service"),
                  "body": ["You get a full technical SEO service, from a deep audit to the actual fixes and ongoing monitoring. I do not just hand you a list of problems, I fix them. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Is a hidden technical issue blocking your rankings?",
                                       "p": "Let me run a free technical check on your site. I will show you exactly what is holding you back and how we can fix it. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for technical SEO"),
                  "body": ["The person who finds the issues is the person who fixes them, and explains them in plain words."],
                  "cards": [
                      {"h3": "I fix, not just find", "p": "Many audits end with a long list of problems and no help. I actually make the fixes, so you see real improvement."},
                      {"h3": "Plain language, not jargon", "p": "I explain every issue in simple terms so you understand what is wrong and why the fix matters."},
                      {"h3": "Honest reporting", "p": "I report on what was fixed and the impact in plain language, so you always know the value you are getting."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Websites", "I work with"),
                     "body": "Business websites, ecommerce stores, large content sites and any site that has stopped ranking or was never set up correctly. If you suspect a technical problem is holding you back, I can find and fix it.",
                     "chips": [("Business websites", None), ("Ecommerce stores", None), ("Large content sites", "/services/enterprise-seo/"),
                               ("Sites that stopped ranking", "/services/seo-audit/"), ("Sites never set up correctly", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "technical SEO"),
                     "body": "A healthy site lets your pages, content and links do their job. These are the services that build on it.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to fix your website and", "climb the rankings?"),
               "p": "Let me run a technical check on your site and build a clear plan to fix what is holding you back. The first step is a simple, friendly call.",
               "btn": CTA, "note": "No obligation · Free technical SEO audit"}),
]
