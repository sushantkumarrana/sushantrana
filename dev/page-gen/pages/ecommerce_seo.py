# Ecommerce SEO Services. Copy: 11_Ecommerce_SEO_Services.txt
# Mocks are illustrations tagged "Example": placeholders only, no figures.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

CTA = "Book your free ecommerce SEO audit"

# lucide star and code, local to this page
L.ICON.update({
    "star": '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path>',
    "code": '<path d="m16 18 6-6-6-6"></path><path d="m8 6-6 6 6 6"></path>',
})

TAG_ON = "shrink-0 rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange"
TAG_OFF = "shrink-0 rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted"
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
MONO = "font-family:ui-monospace,SFMono-Regular,Menlo,monospace"
LINE = '<span class="mt-2 block h-2 rounded-full bg-ink/10" aria-hidden="true"{}></span>'


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


def line(width=None):
    return LINE.format(f' style="width:{width}%"' if width else "")


def stars():
    return '<span class="flex gap-0.5 text-orange">' + svg("star", "h-3.5 w-3.5") * 5 + "</span>"


def product_card(name):
    return (f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-6 w-6")}</div>'
            f'<p class="p-3 text-[11px] font-bold leading-tight text-ink">{E(name)}</p></div>')


GHOST = ('<div class="rounded-2xl border border-[var(--color-line)] p-4 opacity-60" aria-hidden="true"><span class="block h-2 w-24 rounded-full bg-ink/10"></span>'
         '<span class="mt-2 block h-3 w-3/4 rounded-full bg-ink/15"></span><span class="mt-2 block h-2 w-full rounded-full bg-ink/10"></span></div>')

# --------------------------------------------------- live buying search demo

serp = figure("Google search", ["Live demo"], (
    f'<label class="block"><span class="{CAP}">Type a product you sell</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<span class="shrink-0 text-sm text-muted">buy</span><input data-mirror="prod" placeholder="running shoes" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Product to preview"/><span class="shrink-0 text-sm text-muted">online</span></span></label>'
    f'<p class="mt-5 {CAP}">Organic result, no cost per click</p>'
    '<div class="mt-2.5 rounded-2xl border border-orange/30 bg-orange/5 p-4"><p class="text-[11px] text-muted">yourstore.com › category</p>'
    '<p class="svc-serp-title mt-1 text-base font-bold leading-snug"><span data-mirror-out="prod" class="svc-cap"></span> | Shop Online at Your Store</p>'
    f'<p class="mt-1 flex items-center gap-2 text-xs text-muted">{stars()}Rating · In stock</p>'
    '<p class="mt-1 text-xs text-body">Your category page, with helpful text and the right products, ranking for a buying search.</p></div>'
    f'<div class="mt-3 grid gap-3">{GHOST * 2}</div>'
    + note("Once a page ranks, it keeps bringing shoppers without paying per click.", "bag")
))

# --------------------------------------------------- "what I optimize" mocks

tree_rows = "".join(
    f'<div class="flex items-center gap-2 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2" style="margin-left:{lvl * 1.25}rem">'
    f'{svg("chev", "h-3.5 w-3.5 shrink-0 text-orange")}<span class="text-xs font-semibold text-ink">{E(t)}</span></div>'
    for lvl, t in [(0, "Home"), (1, "Category"), (2, "Sub-category"), (3, "Product one"), (3, "Product two"), (1, "Buying guides")])

MOCKS = {
    "keywords": figure("Buying searches, mapped", ["Example"], rows([
        ("“buy product type online”", "Category page", "Mapped", True),
        ("“brand model name”", "Product page", "Mapped", True),
        ("“best product type for your use”", "Buying guide", "Mapped", True),
        ("“product type for kids”", "Sub-category page", "Mapped", True),
    ]) + note("Each buying search points to the page best placed to make the sale.", "search")),
    "category": figure("Category page", ["Example"], (
        '<div class="overflow-hidden rounded-2xl border border-[var(--color-line)]"><p class="truncate border-b border-[var(--color-line)] bg-[#fff7f3] px-4 py-2 text-[11px] text-muted">yourstore.com/product-type/</p>'
        '<div class="p-4"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">H1</p><p class="text-base font-extrabold text-ink">Product Type</p>'
        f'{line()}{line(70)}<p class="mt-2 text-[10px] font-bold uppercase tracking-wider text-orange">Short, helpful intro</p>'
        '<div class="mt-3 grid grid-cols-3 gap-2">' + product_card("Product one") + product_card("Product two") + product_card("Product three") + "</div>"
        '<div class="mt-3 flex flex-wrap gap-2">' + "".join(
            f'<span class="rounded-full border border-[var(--color-line)] px-3 py-1 text-[11px] font-semibold text-ink">{t}</span>' for t in ("Buying guide", "Common questions", "Related categories"))
        + "</div></div></div>")),
    "product": figure("Product page", ["Example"], (
        '<div class="grid grid-cols-2 gap-4"><div class="grid aspect-square place-items-center rounded-2xl bg-[#fff7f3] text-orange">' + svg("image", "h-8 w-8") + "</div>"
        '<div><p class="text-base font-extrabold leading-tight text-ink">Product one, clear descriptive title</p>'
        f'<p class="mt-1.5 flex items-center gap-2 text-[11px] text-muted">{stars()}Reviews</p>{line()}{line(85)}{line(60)}'
        '<span class="mt-3 block rounded-xl bg-orange py-2 text-center text-xs font-bold text-white">Add to cart</span></div></div>'
        '<div class="mt-4 flex flex-wrap gap-2">' + "".join(
            f'<span class="inline-flex items-center gap-1.5 rounded-full bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{svg("check", "h-3 w-3", 3)}{t}</span>'
            for t in ("Unique description", "Size and material", "Care and delivery details")) + "</div>")),
    "structure": figure("Store structure", ["Example"], f'<div class="grid gap-2">{tree_rows}</div>' + note("Shoppers and Google reach every product in a few clicks.", "layers")),
    "technical": figure("Store health fixes", ["Example"], rows([
        ("/product-type/?color=red&sort=price", "Filter URL", "Controlled", True),
        ("/product-one/?variant=2", "Duplicate of /product-one/", "Canonical set", True),
        ("/product-two/", "Out of stock, page kept live", "Related shown", True),
        ("Product one, copied text", "Same as the supplier's site", "Rewritten", True),
    ])),
    "content": figure("Buying guide", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">Guide</p>'
        f'<p class="text-base font-extrabold text-ink">How to choose the right product type</p>{line()}{line(80)}{line(90)}</div>'
        f'<div class="mt-3 mb-3 flex justify-center text-orange" aria-hidden="true"><span style="transform:rotate(90deg)">{svg("chev", "h-6 w-6")}</span></div>'
        '<div class="grid grid-cols-3 gap-2">' + product_card("Product one") + product_card("Product two") + product_card("Product three") + "</div>"
        + note("Shoppers earlier in their search, linked straight to your products.", "file"))),
    "reviews": figure("Reviews and product schema", ["Example"], (
        code(['{ "@type": "Product",', '  "name": "Product one",', '  "offers": { ... },', '  "aggregateRating": { ... } }'])
        + f'<p class="mt-4 {CAP}">Can show in search as</p>'
        '<div class="mt-2 rounded-2xl border border-orange/30 bg-orange/5 p-4"><p class="text-[11px] text-muted">yourstore.com › product-one</p>'
        '<p class="svc-serp-title mt-1 text-base font-bold">Product one | Your Store</p>'
        f'<p class="mt-1 flex items-center gap-2 text-xs text-muted">{stars()}Rating · Reviews · In stock</p></div>')),
}

TYPES = [
    {"key": "keywords", "name": "Product and category keyword research", "icon": "search",
     "what": "I find the exact buying searches for your products and categories, so we target searches that lead to sales."},
    {"key": "category", "name": "Category page SEO", "icon": "layers",
     "what": "I optimize your category pages, which are often your biggest ranking opportunity, with the right keywords and helpful content."},
    {"key": "product", "name": "Product page SEO", "icon": "bag",
     "what": "I improve your product titles, descriptions and details so each product page can rank and convert better."},
    {"key": "structure", "name": "Site structure and navigation", "icon": "sliders",
     "what": "I organize your store so both shoppers and Google can move through it easily, which spreads ranking power."},
    {"key": "technical", "name": "Technical health", "icon": "shield",
     "what": "I fix crawl issues, duplicate content and other technical problems that are common on stores and quietly hurt rankings."},
    {"key": "content", "name": "Content and buying guides", "icon": "file",
     "what": "I add blogs and buying guides that attract shoppers earlier in their journey and link them to your products."},
    {"key": "reviews", "name": "Reviews and schema", "icon": "star",
     "what": "I set up product schema and reviews so your listings can show stars and details in search, which lifts clicks."},
]
for t in TYPES:
    t["mock"] = MOCKS[t["key"]]

leak_box = L.leak_check(
    "Store check", "Tick everything that sounds like your online store.",
    [("My product descriptions are copied from the supplier", "Thin or duplicate descriptions make product pages hard to rank."),
     ("My category pages are just a grid of products", "Category pages are often your biggest ranking opportunity."),
     ("My filters create a new URL for every color, size and sort", "Endless filter URLs confuse Google and waste crawl budget."),
     ("Out of stock products disappear or show an error", "Handled wrongly, they lose rankings you worked hard to earn."),
     ("I have many near identical product pages", "Similar pages compete with each other for the same searches."),
     ("My listings show no stars or details in search", "Product schema and reviews help your listings stand out.")],
    ("Nothing ticked yet. A free audit still checks the store issues that are hard to see from the front end.",
     "A problem or two. These are usually the first things I fix on a store.",
     "Your store is very likely losing rankings to these problems. Solving them is what separates real ecommerce SEO from basic SEO."),
    CTA, "Problems ticked")

GET = [
    {"icon": "search", "h3": "Product and category keyword research", "p": "The exact buying searches for your products and categories, mapped to the right pages."},
    {"icon": "layers", "h3": "On-page optimization", "p": "Category and product pages optimized with the right keywords, helpful content and unique descriptions."},
    {"icon": "shield", "h3": "Technical fixes", "p": "Crawl, speed, filter and duplicate content issues fixed, and out of stock pages handled properly."},
    {"icon": "file", "h3": "Content and buying guides", "p": "Blogs and guides that attract shoppers earlier and link them to your products."},
    {"icon": "star", "h3": "Product schema and internal linking", "p": "Schema so listings can show stars and details, plus internal links that spread ranking power."},
    {"icon": "chart", "h3": "Clear monthly reports", "p": "Rankings, organic traffic and sales in plain language, plus updates on the work done."},
]

FAQ = [
    ("What is ecommerce SEO?", "Ecommerce SEO is the work that helps your online store rank on Google for buying searches. It focuses on your product pages, category pages and the technical health of your store."),
    ("How is ecommerce SEO different from normal SEO?", "Ecommerce SEO deals with special problems like hundreds of product pages, duplicate content, filters and out of stock items. It also puts a big focus on category and product pages that capture buyers."),
    ("Do I need SEO if I already run paid ads?", "Yes. Ads stop when you stop paying, but SEO keeps bringing buyers for free. Using both together usually lowers your overall cost of getting a sale."),
    ("Should I optimize category pages or product pages?", "Both, but category pages are often the biggest opportunity because they target broad buying searches. I optimize both in the right order for the best gains."),
    ("What about duplicate product descriptions?", "Duplicate descriptions can hurt your rankings. I write unique content for your most important products and handle the rest in a smart way to avoid problems."),
    ("How do you handle out of stock products?", "Out of stock pages can lose valuable rankings if handled wrongly. I manage them so you keep the ranking power and guide shoppers to related products."),
    ("What is the faceted navigation problem?", "Filters on stores can create endless duplicate URLs that confuse Google and waste crawl budget. I control these so your important pages get the attention instead."),
    ("How soon will I see results?", "Ecommerce SEO usually shows movement over two to three months, with bigger gains building over time as your pages gain authority."),
    ("Do reviews help ecommerce SEO?", "Yes. Reviews add fresh content and trust, and with review schema your listings can show stars in search, which lifts clicks and sales."),
    ("Can you do SEO for my Shopify store?", "Yes. I work with Shopify, WooCommerce and other platforms and know the SEO strengths and limits of each one."),
    ("Will you write product descriptions?", "I write or improve descriptions for your most important products so they are unique and helpful, which supports both rankings and sales."),
    ("How do you find product keywords?", "I research the exact words shoppers use before buying, including brand, model and buying phrases, and map them to the right pages."),
    ("Can ecommerce SEO reduce my ad costs?", "Yes. As your organic sales grow, you can rely less on ads for the same revenue, which lowers your overall cost of getting a sale."),
    ("Do you fix technical issues too?", "Yes. Technical health is a big part of ecommerce SEO. I fix crawl, speed and duplicate content issues that hold stores back."),
    ("What reports will I get?", "You get clear monthly reports showing rankings, organic traffic and sales, plus updates on the work done."),
    ("How do I get started?", "Just book a free ecommerce SEO audit using the button on this page. I will review your store and show you how to grow your organic sales."),
]

RELATED = [
    ("Google Shopping Ads", "/services/google-shopping-ads/"),
    ("Technical SEO", "/services/technical-seo/"),
    ("On-page SEO", "/services/on-page-seo/"),
    ("Ecommerce websites", "/services/ecommerce-website/"),
    ("Link building", "/services/link-building/"),
    ("Content SEO", "/services/content-seo/"),
]

PAGE = {
    "path": "/services/ecommerce-seo/",
    "slug": "ecommerce-seo",
    "form_name": "ecommerce_seo",
    "service": "Ecommerce SEO",
    "service_name": "Ecommerce SEO services",
    "thanks_what": "ecommerce SEO audit",
    "category": "Search engine optimization",
    "service_desc": "Ecommerce SEO covering product and category keyword research, category and product page SEO, store structure and navigation, technical health, content and buying guides, reviews and product schema, internal linking and monthly reporting on rankings, organic traffic and sales.",
    "audience": "Online stores that want more organic sales",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What ecommerce SEO includes",
    "offers": GET,
    "title": "Ecommerce SEO Services for Online Stores | Sushant Rana",
    "og_title": "Ecommerce SEO Services for Online Stores",
    "og_alt": "Ecommerce SEO services by Sushant Rana",
    "desc": "Ecommerce SEO services that rank your product and category pages for buying searches, so shoppers find your store for free. Book a free audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Ecommerce SEO", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Ecommerce SEO", "questions, answered"),
            "body": ["Products, categories, filters and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Ecommerce SEO services",
        "h1": ("Ecommerce SEO services that bring free buyers", "to your online store"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I help online stores grow their organic sales month after month. Ecommerce SEO gets your product and category pages ranking on Google, so ready to buy shoppers find you for free, without you paying for every single click.',
            "Paid ads stop the moment you stop paying, but SEO keeps bringing buyers long after the work is done. We help Shopify, WooCommerce and other online stores turn Google into a steady sales channel.",
        ],
        "cta2": ("See what I optimize", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free ecommerce SEO audit",
        "sub": "Tell me about your store and I will review it for free.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Store", "fields": [
                {"type": "text", "name": "site", "label": "Store website", "req": True, "placeholder": "yourstore.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "radio", "name": "platform", "label": "Store platform", "req": True,
                 "options": ["Shopify", "WooCommerce", "Other platform", "Not sure"]},
                {"type": "select", "name": "products", "label": "Number of products", "placeholder": "Select",
                 "options": ["Under 50", "50 to 500", "500 to 5,000", "More than 5,000", "Not sure"]},
            ]},
            {"label": "Goals", "fields": [
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Category pages", "Product pages", "Keyword research", "Technical issues", "Buying guides", "Reviews and schema", "Not sure"]},
                {"type": "radio", "name": "ads", "label": "Are you running paid ads now?", "options": ["Yes", "No", "Paused"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, your best categories, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Category pages", "Product pages", "Buying searches", "Faceted navigation", "Duplicate content", "Out of stock pages", "Buying guides", "Product schema"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What ecommerce SEO is", "and why it matters"),
             "body": ["Ecommerce SEO is the work that helps your online store rank on Google for the searches people use when they want to buy. It focuses on your category pages, product pages and the overall health of your store.",
                      "This matters because most shoppers start on Google. If your products show up for buying searches, you get free, high intent traffic that keeps coming, which lowers how much you need to spend on ads."],
             "bullets": ["Found for the searches people use to buy", "Free traffic that keeps coming", "Less money spent on ads"],
             "cta": CTA, "visual": serp}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why ecommerce SEO is", "a smart investment"),
                      "body": ["Ads rent attention. SEO builds a sales channel your store owns."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "users", "h3": "Free buyers who keep coming", "p": "Once your pages rank, they bring shoppers every day without paying per click. This traffic keeps working for you long term."},
                          {"icon": "wallet", "h3": "Less dependence on paid ads", "p": "Strong SEO reduces how much you rely on ads. Many stores use SEO to lower their overall cost of getting a sale."},
                          {"icon": "bag", "h3": "Category and product pages capture buyers", "p": "These pages target the exact searches people use before buying, so they attract shoppers who are ready to purchase."},
                          {"icon": "chart", "h3": "Results grow over time", "p": "Unlike ads, SEO builds up. The work you do now keeps paying off and compounds month after month."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I optimize", "h2": ("The ecommerce SEO work", "I do for you"),
                           "body": ["Seven parts of your store that decide whether shoppers find your products on Google. Pick one to see what it looks like."],
                           "items": TYPES})),
    L.split({"id": "challenge", "pill": "The challenge", "h2": ("The special problems of ecommerce SEO", "and how I solve them"),
             "body": ["Online stores face SEO problems that normal websites do not. You often have thin or duplicate product descriptions, hundreds of similar pages, filters that create endless URLs, and out of stock products that lose their rankings.",
                      "I know how to handle all of these. I write unique content where it matters, control the filter and duplicate page issues, and manage out of stock pages so you do not lose the rankings you worked hard to earn. Solving these problems is what separates real ecommerce SEO from basic SEO."],
             "bullets": ["Unique content where it matters", "Filter and duplicate pages under control", "Out of stock pages that keep their rankings"],
             "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My ecommerce SEO", "process"),
                   "body": ["Five clear stages, from the store audit to monthly reports. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Store audit", "short": "Audit", "p": "I check your store's rankings, structure and technical health to find the biggest opportunities and problems.", "points": ["Current rankings", "Store structure", "Technical health"]},
                       {"h3": "Keyword and structure plan", "short": "Plan", "p": "I map buying keywords to your categories and products and plan a clean structure for growth.", "points": ["Buying keywords mapped", "Categories and products", "Structure for growth"]},
                       {"h3": "Optimize categories and products", "short": "Optimize", "p": "I optimize your most valuable pages first, since these bring the fastest gains in sales.", "points": ["Most valuable pages first", "Category pages", "Product pages"]},
                       {"h3": "Technical fixes and content", "short": "Fixes", "p": "I fix technical issues and add content and links that support your product pages.", "points": ["Technical issues fixed", "Buying guides and blogs", "Links to product pages"]},
                       {"h3": "Track and report", "short": "Report", "p": "I track rankings, traffic and sales and send you clear reports in plain language.", "points": ["Rankings tracked", "Organic traffic and sales", "Plain language reports"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my ecommerce SEO service"),
                  "body": ["You get a complete, done for you ecommerce SEO service focused on growing your organic sales. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Want more sales without paying for every click?",
                                       "p": "Let me take a free look at your store and show you the biggest SEO opportunities to grow your organic sales. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why online stores", "choose me"),
                  "body": ["The person who plans your store's SEO is the person you talk to, and every report is about rankings, traffic and sales."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person doing the work, with clear answers and fast replies."},
                      {"h3": "I understand ecommerce problems", "p": "I know how to handle duplicate content, filters and out of stock pages, which most basic SEO misses."},
                      {"h3": "Honest reporting", "p": "I report on rankings, traffic and sales in plain language, so you always know what you are getting."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Online stores", "I work with"),
                     "body": "Shopify stores, WooCommerce stores and other ecommerce platforms across many product categories. If you sell products online, ecommerce SEO can grow your free sales.",
                     "chips": [("Shopify stores", "/services/shopify-store-development/"), ("WooCommerce stores", "/services/wordpress-development/"),
                               ("Other ecommerce platforms", "/services/ecommerce-website/"), ("Ecommerce brands", "/industries/ecommerce/")]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "ecommerce SEO"),
                     "body": "Online stores grow fastest when SEO, Shopping ads and a healthy store are handled together.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to grow your store", "with free traffic?"),
               "p": "Let us look at your store together and build an SEO plan that brings ready to buy shoppers to your products every day.",
               "btn": CTA, "note": "No obligation · Free ecommerce SEO audit"}),
]
