# Amazon PPC Services. Copy: 06_Amazon_PPC_Services.docx
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free Amazon Ads audit"


def bar(w, tone="bg-ink/10", h="h-2"):
    return f'<span class="block {h} {w} rounded-full {tone}"></span>'


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def tag(text, hot=False):
    tone = "bg-orange/10 text-orange" if hot else "bg-ink/[0.06] text-muted"
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {tone}">{E(text)}</span>'


def rows(items):
    return '<ul class="grid list-none gap-2.5">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid"><span class="text-sm font-bold text-ink">{E(a)}</span><span class="text-xs text-muted">{E(b)}</span></span>{tag(t, hot)}</li>'
        for a, b, t, hot in items) + "</ul>"


def toggle(opts, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-3 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(lab)}</button>'
        for i, (k, lab) in enumerate(opts)) + "</div>"


def box(icon="bag", size="h-12 w-12"):
    return f'<span class="grid {size} shrink-0 place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg(icon, "h-6 w-6")}</span>'


def result(title, sub, top=False):
    if top:
        return (f'<div class="flex items-center gap-3 rounded-2xl border border-orange/30 bg-orange/5 p-3">{box()}'
                f'<span class="grid gap-0.5"><span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored</span>'
                f'<span class="text-sm font-bold text-ink">{title}</span><span class="text-xs text-body">{E(sub)}</span></span></div>')
    return (f'<div class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] p-3 opacity-60">{box()}'
            f'<span class="grid w-full gap-1.5" aria-hidden="true">{bar("w-1/2", "bg-ink/15", "h-3")}{bar("w-3/4")}</span></div>')


# --------------------------------------------------- 01 basics: live Amazon search

search_box = figure("Amazon search results", ["Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type what a shopper searches on Amazon</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="amz" placeholder="steel water bottle" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Amazon search to preview"/></span></label>'
    '<div class="mt-4 grid gap-2.5">'
    + result('Your brand <span data-mirror-out="amz"></span>', "Your product, at the top of page one", True) + result("", "") + result("", "")
    + "</div>" + note("Most shoppers never look past the first page. You only pay when a shopper clicks your ad.", "click")))

# --------------------------------------------------- 03 ad types

brands = ('<div class="rounded-2xl border border-orange/30 bg-orange/5 p-3"><div class="flex items-center gap-3">'
          '<span class="grid h-10 w-10 shrink-0 place-items-center rounded-lg bg-ink text-[10px] font-extrabold text-white">LOGO</span>'
          '<span class="grid"><span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored</span><span class="text-sm font-bold text-ink">Your brand headline</span></span></div>'
          '<div class="mt-3 grid grid-cols-3 gap-2">' + "".join(
              f'<div class="rounded-xl border border-[var(--color-line)] bg-white p-2 text-center"><span class="mx-auto grid aspect-square place-items-center rounded-lg bg-[#fff7f3] text-orange">{svg("bag", "h-5 w-5")}</span>'
              f'<p class="mt-1 text-[10px] font-bold text-ink">{n}</p></div>' for n in ["Product one", "Product two", "Product three"]) + "</div></div>"
          f'<div class="mt-2.5 grid gap-2.5">{result("", "")}</div>')

brand_video = ('<div class="rounded-2xl border border-orange/30 bg-orange/5 p-3"><div class="grid gap-3 sm:grid-cols-2">'
               f'<div class="relative grid aspect-video place-items-center rounded-xl bg-[#0a0a0a]"><span class="grid h-10 w-10 place-items-center rounded-full bg-orange text-white">{svg("play", "h-5 w-5")}</span></div>'
               '<span class="flex flex-col justify-center gap-1"><span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored</span><span class="text-sm font-bold text-ink">Your product in action</span>'
               '<span class="text-xs text-body">A short video that plays right in the search results.</span></span></div></div>'
               f'<div class="mt-2.5 grid gap-2.5">{result("", "")}</div>')

display = ('<div class="rounded-2xl border border-[var(--color-line)] p-3"><div class="flex gap-3">'
           f'<span class="grid h-24 w-24 shrink-0 place-items-center rounded-xl bg-ink/[0.06] text-muted">{svg("bag", "h-8 w-8")}</span>'
           f'<span class="grid w-full content-start gap-1.5" aria-hidden="true">{bar("w-3/4", "bg-ink/15", "h-3")}{bar("w-full")}{bar("w-1/2")}</span></div>'
           f'<div class="mt-3 flex items-center gap-3 rounded-xl border border-orange/30 bg-orange/5 p-3">{box("bag", "h-10 w-10")}'
           '<span class="grid"><span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored</span><span class="text-xs font-bold text-ink">Your product, shown on a product page</span></span></div></div>'
           + note("Also shown to shoppers on other websites, to bring them back.", "repeat"))

AD_TYPES = [
    {"key": "sp", "name": "Sponsored Products", "icon": "bag",
     "what": "The most common Amazon ad. These promote a single product in search results and on product pages.", "best": "They drive the majority of ad sales for most sellers.",
     "mock": figure("Sponsored Products", ["Example"], '<div class="grid gap-2.5">' + result("Your product", "Top of the Amazon results", True) + result("", "") + result("", "") + "</div>")},
    {"key": "sb", "name": "Sponsored Brands", "icon": "layers",
     "what": "Ads that show your brand logo and several products at the top of search.", "best": "Great for brand awareness and sending shoppers to your store.",
     "mock": figure("Sponsored Brands", ["Example"], brands)},
    {"key": "sbv", "name": "Sponsored Brands Video", "icon": "play",
     "what": "Short video ads in search that grab attention and show your product in action.", "best": "A powerful way to stand out from other listings.",
     "mock": figure("Sponsored Brands Video", ["Example"], brand_video)},
    {"key": "sd", "name": "Sponsored Display", "icon": "repeat",
     "what": "Ads that follow shoppers on and off Amazon, including on product pages and other websites.", "best": "Useful for retargeting and reaching new buyers.",
     "mock": figure("Sponsored Display", ["Example"], display)},
]

# --------------------------------------------------- 04 targeting

flow = ('<ol class="grid list-none gap-2.5">' + "".join(
    f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
    f'<span class="grid"><span class="text-sm font-bold text-ink">{a}</span><span class="text-xs text-muted">{b}</span></span></li>'
    for i, (a, b) in enumerate([("Automatic campaign", "Amazon finds new search terms"), ("Winners spotted", "The terms that bring profitable sales"), ("Manual campaign", "Winners moved in, with full control of bids")], 1)) + "</ol>")

competitor = ('<div class="rounded-2xl border border-[var(--color-line)] p-3"><p class="text-[10px] font-bold uppercase tracking-wide text-muted">A competitor&#x27;s product page</p>'
              f'<div class="mt-2 flex gap-3 opacity-60" aria-hidden="true"><span class="block h-16 w-16 shrink-0 rounded-xl bg-ink/10"></span>'
              f'<span class="grid w-full content-start gap-1.5">{bar("w-3/4", "bg-ink/15", "h-3")}{bar("w-full")}</span></div>'
              f'<div class="mt-3">{result("Your product", "Shown to shoppers who are comparing options", True)}</div></div>')

TARGETING = [
    ("kw", "Keyword targeting", "I find the exact search terms your buyers use and bid on the ones most likely to bring profitable sales.",
     rows([("Search term one", "Brings profitable sales", "Bid up", True), ("Search term two", "New, still learning", "Testing", False), ("Search term three", "Clicks, no sales", "Bid down", False)])),
    ("product", "Product and category targeting", "I place your ads on competitor product pages and in related categories, so you win shoppers who are comparing options.", competitor),
    ("auto", "Automatic and manual campaigns", "I use automatic campaigns to discover new keywords, then move the winners into tight manual campaigns for better control.", flow),
    ("neg", "Negative keywords", "I add negative keywords to stop wasteful clicks on searches that do not convert, which protects your budget and lowers your ACoS.",
     rows([("Search that never converts", "Wasted clicks", "Blocked", True), ("Wrong product type", "Wrong shopper", "Blocked", True), ("Your best search term", "Profitable", "Keep", False)])),
]
t_btns = "".join(
    f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="border-orange bg-orange text-white" data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" '
    f'class="rounded-2xl border px-3 py-2.5 text-left text-xs font-bold transition {"border-orange bg-orange text-white" if i == 0 else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{E(n)}</button>'
    for i, (k, n, _, _) in enumerate(TARGETING))
t_panels = "".join(
    f'<div data-panel="{k}"{HID if i else ""} class="mt-4">{body}<p class="mt-4 text-sm text-body"><strong class="font-semibold text-ink">{E(n)}.</strong> {E(w)}</p></div>'
    for i, (k, n, w, body) in enumerate(TARGETING))
targeting_box = '<div data-tabs="true">' + figure("How your ads find shoppers", ["Example"], f'<div class="grid grid-cols-2 gap-2">{t_btns}</div>{t_panels}') + "</div>"

# --------------------------------------------------- 07 ACoS and TACoS

formulas = ('<div class="mt-7 grid gap-3 sm:grid-cols-2">' + "".join(
    f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><p class="font-[family-name:var(--font-display)] text-lg font-extrabold text-orange">{a}</p>'
    f'<p class="mt-1 text-sm font-semibold text-ink">{b}</p><p class="mt-1 text-xs text-muted">{c}</p></div>'
    for a, b, c in [("ACoS", "Ad spend ÷ ad sales", "Lower means more profit from each ad sale."),
                    ("TACoS", "Ad spend ÷ total sales", "Includes organic sales. The bigger picture number.")]) + "</div>")

leak_box = L.leak_check(
    "Amazon ad account check", "Tick everything that sounds like your account.",
    [("I have never added negative keywords", "Wasteful clicks on searches that do not convert push your ACoS up."),
     ("I only run automatic campaigns", "The winners never move into manual campaigns with proper bid control."),
     ("My campaign structure is messy", "A clean structure is the key to a low ACoS."),
     ("My listing has weak titles, images or few reviews", "Even the best ads struggle when the listing is weak."),
     ("I look at ACoS but never at TACoS", "TACoS shows whether ads grow the whole business.")],
    ("Nothing ticked yet. A free audit still checks the structure, bids and search terms behind your ACoS.",
     "A leak or two. These are usually the first things I fix when I take over an Amazon account.",
     "Your ACoS is very likely higher than it needs to be. Negatives and structure are where I would start."),
    CTA)

GET = [
    {"icon": "search", "h3": "Keyword and competitor research", "p": "The best search terms for your products, and a clear view of what your competitors are doing."},
    {"icon": "layers", "h3": "Campaign build and structure", "p": "A clean campaign structure that is easy to manage and control, which is the key to a low ACoS."},
    {"icon": "sliders", "h3": "Bid management and ACoS control", "p": "Bids adjusted and budget shifted every week to lower your ad cost and grow profitable sales."},
    {"icon": "shield", "h3": "Negative keyword work", "p": "Wasteful searches blocked so your budget only goes to clicks that can convert."},
    {"icon": "file", "h3": "Listing improvement advice", "p": "Clear advice on titles, images and content, because even the best ads struggle if the listing is weak."},
    {"icon": "chart", "h3": "Clear reports", "p": "Reports showing sales, spend, ACoS, TACoS and your best products, plus updates whenever something important changes."},
]

FAQ = [
    ("What is Amazon PPC?", "Amazon PPC is pay per click advertising on Amazon. You pay only when a shopper clicks your ad, and your products get shown at the top of search results and on product pages where buyers can see them."),
    ("What is ACoS?", "ACoS stands for advertising cost of sale. It is the share of your ad sales that you spend on ads. A lower ACoS means you keep more profit from every ad sale."),
    ("How much budget do I need for Amazon ads?", "It depends on your products, your competition and your goals. Some sellers start small and scale up once we find profitable keywords. On our call I will suggest a realistic starting budget."),
    ("What is the difference between Sponsored Products and Sponsored Brands?", "Sponsored Products promote a single product and drive most ad sales. Sponsored Brands show your logo and several products at the top of search and are great for brand awareness."),
    ("Do you optimize my product listings too?", "I review your listings and give clear advice on titles, images and content, because even the best ads struggle if the listing is weak. A strong listing plus good ads is what really grows sales."),
    ("What is the difference between keyword and product targeting?", "Keyword targeting shows your ad when people search certain words. Product targeting places your ad on specific product pages and categories, often your competitors', to win shoppers who are comparing."),
    ("How soon will I see results?", "You can see clicks and sales within the first few days. The first few weeks are used to gather data and cut waste, so a lower ACoS and steady sales usually build from the first month."),
    ("Can you lower my ACoS?", "Yes, this is a big part of my job. I do it by adding negative keywords, adjusting bids, improving campaign structure and moving budget to what actually sells."),
    ("What is the difference between automatic and manual campaigns?", "Automatic campaigns let Amazon find keywords for you and are great for discovery. Manual campaigns give you full control over bids and targeting, which is where the real optimization happens."),
    ("What are negative keywords?", "Negative keywords are searches you do not want to pay for. Adding them stops wasted clicks and lowers your ACoS, which protects your budget."),
    ("Do Amazon ads help my organic ranking?", "Yes. More ad sales send a positive signal to Amazon, which can lift your product in the free search results over time. So your ads help even after they stop."),
    ("What reports will I get?", "You get clear monthly reports showing sales, spend, ACoS, TACoS and your best products, plus updates whenever something important changes."),
    ("Can you work with sellers outside India?", "Yes. I work with Amazon sellers in the US, Canada and other marketplaces, and I can manage your account from anywhere."),
    ("Can you fix my existing Amazon ad account?", "Yes. This is a common request. I audit your account, find the waste and rebuild the structure so your ads become profitable again."),
    ("Do I need good reviews and a strong listing first?", "It helps a lot. Ads bring shoppers, but reviews and a clear listing help turn those clicks into sales. I will point out what to fix first so your ad budget is not wasted."),
    ("How do I get started?", "Just book a free Amazon Ads audit using the button on this page. I will review your account and show you how we can grow your sales and lower your ACoS."),
]

RELATED = [
    ("Performance marketing", "/services/performance-marketing/"),
    ("Google Ads", "/services/google-ads/"),
    ("Google Shopping Ads", "/services/google-shopping-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
]

PAGE = {
    "path": "/services/amazon-ads/",
    "slug": "amazon-ads",
    "form_name": "amazon_ads",
    "service": "Amazon Ads",
    "service_name": "Amazon PPC management",
    "thanks_what": "Amazon Ads audit",
    "category": "Marketplace advertising",
    "service_desc": "Amazon PPC management covering Sponsored Products, Sponsored Brands, Sponsored Brands Video and Sponsored Display, with keyword and competitor research, campaign structure, bid management, ACoS and TACoS control, negative keywords, listing advice and reporting.",
    "audience": "Amazon sellers and brands",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What Amazon PPC management includes",
    "offers": GET,
    "title": "Amazon PPC Management Services | Sushant Rana",
    "og_title": "Amazon PPC Management Services",
    "og_alt": "Amazon PPC management services by Sushant Rana",
    "desc": "Amazon PPC management services that push your products to the top and lower your ACoS. Sponsored Products, Brands and Display. Book a free audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Amazon Ads", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Amazon PPC", "questions, answered"),
            "body": ["ACoS, targeting, listings and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Amazon PPC management",
        "h1": ("Amazon PPC services that get your products", "to the top and sell more"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I run Amazon ad campaigns that increase your sales while keeping your ad cost under control. Selling on Amazon but feeling lost in the crowd of other sellers? Amazon PPC is how you rise to the top and get seen by ready to buy shoppers.',
            "Most Amazon shoppers never look past the first page, so if your product is not there, you are missing sales every day. We help sellers across India, the US and Canada win better placement, more orders and a healthier ACoS.",
        ],
        "cta2": ("See ad types", "#types"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free Amazon Ads audit",
        "sub": "Tell me about your products and I will review your Amazon ad account for free.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Store", "fields": [
                {"type": "radio", "name": "running", "label": "Are you running Amazon ads now?", "req": True,
                 "options": ["Yes, running now", "Paused or stopped", "Never run them"]},
                {"type": "select", "name": "marketplace", "label": "Main marketplace", "req": True, "placeholder": "Select a marketplace",
                 "options": ["Amazon.in", "Amazon.com", "Amazon.ca", "Amazon.ae", "Other"]},
                {"type": "select", "name": "products", "label": "Number of products", "placeholder": "Select a range",
                 "options": ["1 - 10", "11 - 50", "51 - 200", "200+"]},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "checkbox", "name": "goals", "label": "What do you want to fix?",
                 "options": ["High ACoS", "Low sales", "New product launch", "Messy campaigns", "Listing advice", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your brand, your best products, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Amazon PPC", "Sponsored Products", "Sponsored Brands", "Sponsored Display", "ACoS", "TACoS", "Negative keywords", "Product targeting"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What Amazon PPC is", "and why it matters"),
             "body": ["Amazon PPC, or pay per click advertising, lets you pay to place your products at the top of Amazon search results and on product pages. You only pay when a shopper clicks your ad.",
                      "This matters because Amazon is where people go when they are ready to buy, not just browse. Good ads put your product in front of these buyers, win sales, and even help push your product higher in the free organic results over time."],
             "bullets": ["Top of search and on product pages", "Pay only when a shopper clicks", "Ad sales help your organic rank too"],
             "cta": CTA, "visual": search_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why Amazon Ads are", "worth your money"),
                      "body": ["Shoppers on Amazon are already in buying mode. Here is what well run ads give you."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "bag", "h3": "You reach buyers ready to purchase", "p": "People on Amazon are already in shopping mode. Your ads reach them at the exact moment they are looking to buy, which brings strong conversion rates."},
                          {"icon": "chart", "h3": "Ads boost your organic rank too", "p": "More ad sales send a positive signal to Amazon, which can lift your product in the free search results as well. So your ads keep working even after you pause them."},
                          {"icon": "wallet", "h3": "You control your ad cost", "p": "With careful bidding and targeting, I keep your ACoS, the share of sales you spend on ads, at a healthy level, so your ads stay profitable."},
                          {"icon": "gauge", "h3": "It scales with your sales", "p": "Once a product is profitable on ads, we can push more budget behind it and grow your orders in a safe, steady way."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "Ad types", "h2": ("The Amazon ad types", "I run for you"),
                           "body": ["Each ad type puts your products in a different spot on Amazon. I use the right mix for your catalog and your goals. Pick one to see what it looks like."],
                           "items": AD_TYPES})),
    L.split({"id": "targeting", "pill": "Targeting", "h2": ("How I target the right", "shoppers on Amazon"),
             "body": ["Good targeting is what keeps your ad cost healthy. I combine four methods so your products show to shoppers who are likely to buy, and not to the ones who never will. Pick one to see how it works."],
             "bullets": ["Keyword targeting", "Product and category targeting", "Automatic and manual campaigns", "Negative keywords"],
             "visual": targeting_box}, dark=True, flip=True),
    L.split({"id": "acos", "pill": "The number that matters", "h2": ("Understanding ACoS and TACoS", "for real profit"),
             "body": ["ACoS, or advertising cost of sale, is the share of your ad sales that you spend on ads. A lower ACoS means more profit from each ad sale, so I work hard to keep it healthy for your margins.",
                      "TACoS, or total advertising cost of sale, looks at your ad spend against your total sales, including organic. This is the bigger picture number I watch to make sure your ads are truly growing your whole business, not just shifting sales around."],
             "after": formulas, "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My Amazon PPC", "process"),
                   "body": ["Five clear stages, from auditing your listings to scaling the products that make money. Pick a stage to follow along."],
                   "steps": [
                       {"h3": "Account and listing audit", "short": "Audit", "p": "I review your account, your products and your listings to see what is working and what is holding back your sales.", "points": ["Account reviewed", "Products and listings checked", "What is holding sales back"]},
                       {"h3": "Keyword and competitor research", "short": "Research", "p": "I study the best keywords and what your competitors are doing, so we target the right searches and products.", "points": ["Best search terms", "Competitor products", "Target list"]},
                       {"h3": "Campaign build and structure", "short": "Build", "p": "I build a clean campaign structure that is easy to manage and control, which is the key to a low ACoS.", "points": ["Clean structure", "Auto and manual campaigns", "Negative keyword lists"]},
                       {"h3": "Bid and ACoS optimization", "short": "Optimize", "p": "I adjust bids, add negatives and shift budget every week to lower your ad cost and grow profitable sales.", "points": ["Weekly bid changes", "New negatives added", "Budget to what sells"]},
                       {"h3": "Reporting and scaling", "short": "Scale", "p": "You get clear reports on sales, spend and ACoS. When a product is profitable, we scale it up carefully.", "points": ["Sales, spend and ACoS", "TACoS tracked", "Careful scaling"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my Amazon PPC service"),
                  "body": ["You get a complete, done for you Amazon advertising service. I handle the strategy, the setup, the daily work and the reporting, and you always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Is your ACoS too high or your sales too low?",
                                       "p": "Let me take a free look at your Amazon ad account. I will show you where money is leaking and how we can grow profitable sales. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why Amazon sellers", "choose me"),
                  "body": ["The person who manages your campaigns is the person you talk to, and success is measured in profit, not just sales."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person who plans and manages your campaigns, with fast replies and clear answers."},
                      {"h3": "Focus on profit, not just sales", "p": "I care about your ACoS and your margins, not only your top line sales, so your growth is real and healthy."},
                      {"h3": "Honest reporting", "p": "I report on sales, spend, ACoS and TACoS in plain language, so you always know what your money is doing."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Amazon sellers", "I work with"),
                     "body": "Private label brands, D2C sellers, resellers and businesses launching new products on Amazon. Whether you have one product or a full catalog, I can build a plan that grows your sales and protects your margins.",
                     "chips": [("Private label brands", None), ("D2C sellers", "/industries/ecommerce/"), ("Resellers", None), ("New product launches", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "Amazon Ads"),
                     "body": "Ecommerce sellers often run Amazon alongside Google Shopping, Google Ads and Meta Ads, with one plan across all of them.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to sell more", "on Amazon?"),
               "p": "Let us look at your products and your ad account together and build a plan that grows profitable sales. The first step is a simple, friendly call.",
               "btn": CTA, "note": "No obligation · Free Amazon Ads audit"}),
]
