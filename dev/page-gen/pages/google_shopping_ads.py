# Google Shopping Ads Services. Copy: 07_Google_Shopping_Ads_Services.docx
# No crm_section: Shopping sells products in a store, so the "CRM sends qualified leads back" story does not fit.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free Google Shopping audit"


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def tag(text, hot=False):
    tone = "bg-orange/10 text-orange" if hot else "bg-ink/[0.06] text-muted"
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {tone}">{E(text)}</span>'


def rows(items, hot):
    return '<ul class="grid list-none gap-2.5">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">{E(a)}</span><span class="text-sm font-semibold text-ink">{E(b)}</span></span>{tag(t, hot)}</li>'
        for a, b, t in items) + "</ul>"


def toggle(opts, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-3 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(lab)}</button>'
        for i, (k, lab) in enumerate(opts)) + "</div>"


def card(title_html, price, store="Your store"):
    return (f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-7 w-7")}</div>'
            f'<div class="p-3"><p class="text-[11px] font-bold leading-tight text-ink">{title_html}</p><p class="mt-1 text-xs font-extrabold text-ink">{price}</p><p class="text-[10px] text-muted">{store}</p></div></div>')


def tile(icon, name):
    return (f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3.5 text-center">'
            f'<span class="mx-auto grid h-10 w-10 place-items-center rounded-xl bg-orange/10 text-orange">{svg(icon, "h-5 w-5")}</span>'
            f'<p class="mt-2 text-xs font-bold text-ink">{E(name)}</p></div>')


# --------------------------------------------------- 01 basics: live Shopping results

shop_box = figure("Google search", ["Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type what a shopper searches</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="shop" placeholder="running shoes for men" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Product search to preview"/></span></label>'
    '<p class="mt-4 text-[11px] font-bold text-ink">Sponsored products</p><div class="mt-2.5 grid grid-cols-3 gap-3">'
    + card('<span data-mirror-out="shop" class="svc-cap"></span>', "₹1,499") + card("Product two", "₹899") + card("Product three", "₹2,250")
    + "</div>" + note('<strong class="font-semibold text-ink">Image, price and store name,</strong> seen before the click. Merchant Center holds the product data, Google Ads runs the campaign.', "bag")))

# --------------------------------------------------- 03 how it works: weak vs strong feed

WEAK = [("Title", "Item 4471", "Unclear"), ("Product type", "Not set", "Missing"), ("Image", "Small, dark photo", "Poor"), ("Details", "Size and colour left out", "Incomplete")]
STRONG = [("Title", "Brand, product and key feature", "Clear"), ("Product type", "The right category", "Correct"), ("Image", "Clear photo on a clean background", "Strong"), ("Details", "Size, colour and material filled in", "Complete")]
feed_box = '<div data-tabs="true">' + figure("One product in your feed", ["Example"], (
    toggle([("weak", "Weak feed"), ("strong", "Strong feed")], on=1)
    + f'<div class="mt-4" data-panel="weak" hidden="">{rows(WEAK, False)}'
    + note('<strong class="font-semibold text-ink">Google guesses,</strong> and shows the product for the wrong searches.')
    + f'</div><div class="mt-4" data-panel="strong">{rows(STRONG, True)}'
    + note('<strong class="font-semibold text-ink">Google understands the product,</strong> and matches it to the right searches.')
    + "</div>")) + "</div>"

# --------------------------------------------------- 04 campaign types

CAMPAIGNS = [
    {"key": "standard", "name": "Standard Shopping", "icon": "sliders",
     "what": "Classic Shopping campaigns that give you full control over which products show and how much you bid.", "best": "Best for careful, hands on management.",
     "mock": figure("Standard Shopping", ["Example"], (
         '<div class="grid gap-2.5">' + "".join(
             f'<div class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3"><span class="grid"><span class="text-sm font-bold text-ink">{g}</span>'
             f'<span class="text-xs text-muted">{s}</span></span>{tag(t, hot)}</div>'
             for g, s, t, hot in [("Best sellers", "Product group", "Bid higher", True), ("New arrivals", "Product group", "Testing", False), ("Low margin items", "Product group", "Bid lower", False)])
         + "</div>" + note("You decide which products show and what each group is worth.", "sliders")))},
    {"key": "pmax", "name": "Performance Max for retail", "icon": "layers",
     "what": "A smart campaign that shows your products across Search, Shopping, YouTube, Gmail and Display from one setup.", "best": "Powerful for sales when guided with strong data.",
     "mock": figure("Performance Max", ["Example"], (
         '<p class="text-center text-[10px] font-bold uppercase tracking-wider text-muted">Your products, shown across</p><div class="mt-3 grid grid-cols-2 gap-3 sm:grid-cols-3">'
         + tile("search", "Search") + tile("bag", "Shopping") + tile("play", "YouTube") + tile("file", "Gmail") + tile("image", "Display")
         + '<div class="grid place-items-center rounded-2xl bg-orange p-3.5 text-center text-xs font-bold text-white">Guided by your feed and data</div></div>'))},
    {"key": "remarketing", "name": "Shopping remarketing", "icon": "repeat",
     "what": "Showing your products again to people who viewed them but did not buy.", "best": "One of the cheapest ways to win back lost sales.",
     "mock": figure("Shopping remarketing", ["Example"], (
         '<ol class="grid list-none gap-3">' + "".join(
             f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
             f'<span class="text-sm font-semibold text-ink">{t}</span></li>'
             for i, t in enumerate(["A shopper views your product", "They leave without buying", "They see that product again on Google", "They come back and buy"], 1)) + "</ol>"))},
]

# --------------------------------------------------- 05 the secret: feed check

leak_box = L.leak_check(
    "Product feed check", "Tick everything that sounds like your store.",
    [("My product titles are short or unclear", "Google uses titles to decide which searches show your products."),
     ("Some products are disapproved in Merchant Center", "Disapprovals can quietly kill your sales."),
     ("My product images are poor quality", "People shop with their eyes, so a weak image loses the click."),
     ("Product types or details are missing", "Incomplete data sends your products to the wrong searches."),
     ("Most of the work so far has been changing bids", "Bids cannot fix a weak feed.")],
    ("Nothing ticked yet. A free audit still checks your Merchant Center and feed for problems that are hard to spot.",
     "A gap or two. Feed fixes like these are usually the first thing I do on a Shopping account.",
     "Your feed is very likely holding your sales back. That is where I would start."),
    CTA, "Feed gaps ticked")

GET = [
    {"icon": "shield", "h3": "Merchant Center setup", "p": "Google Merchant Center set up or fixed, with your account and products approved and healthy."},
    {"icon": "file", "h3": "Product feed optimization", "p": "Clear, keyword rich titles, correct product types, strong images and complete details."},
    {"icon": "layers", "h3": "Campaign build and structure", "p": "A clean structure that separates your products in a smart way, so we can control bids and spend."},
    {"icon": "sliders", "h3": "Bid management", "p": "Bids adjusted, wasted spend cut and budget pushed to your best selling products every week."},
    {"icon": "check", "h3": "Disapproved products fixed", "p": "I find the cause, fix the feed or settings and get your products approved and selling again."},
    {"icon": "chart", "h3": "Tracking and monthly reports", "p": "Conversion tracking on every sale, and clear reports showing sales, spend, return and your best products."},
]

FAQ = [
    ("What are Google Shopping Ads?", "Google Shopping Ads are product ads that appear in Google search with an image, price and store name. They help online stores reach shoppers who are ready to buy."),
    ("What is Google Merchant Center?", "Google Merchant Center is the tool that stores all your product information, like titles, prices and images. Google reads this to decide when and where to show your Shopping Ads."),
    ("Do I need a product feed?", "Yes. The product feed is the file that lists all your products and their details. It is the engine behind Shopping Ads, and I set it up and optimize it for you."),
    ("How are Shopping Ads different from Search Ads?", "Search Ads are text ads that use keywords. Shopping Ads use your product feed and show an image and price. Shopping is usually better for selling products, while Search is better for services."),
    ("How much budget do I need for Shopping Ads?", "It depends on your products and competition. Some stores start small and scale up once we find winning products. On our call I will suggest a realistic starting budget."),
    ("Why is the product feed so important?", "Google uses your feed to decide which searches show your products. Clear titles and good images bring better placement and cheaper sales, while a weak feed holds your account back."),
    ("What is the difference between Standard Shopping and Performance Max?", "Standard Shopping gives you more control over products and bids. Performance Max is a smart campaign that reaches across all of Google from one setup. I choose the right mix for your goals."),
    ("How soon will I see results?", "Shopping Ads can bring traffic and sales within the first few days. The first few weeks are used to gather data and cut waste, so strong results usually build from the first month."),
    ("Can you fix my disapproved products?", "Yes. Product disapprovals are common and can quietly kill your sales. I find the cause, fix the feed or settings and get your products approved and selling again."),
    ("Do you optimize my product titles and images?", "Yes. I improve your titles, product types and image quality inside the feed, because these directly affect which searches show your products and how many people click."),
    ("What is ROAS for Shopping Ads?", "ROAS, or return on ad spend, tells you how much revenue you earn for every rupee spent. For Shopping, a strong ROAS is one of the clearest signs your store is growing profitably."),
    ("Can you handle a store with many products?", "Yes. I structure large catalogs in a smart way so we can control spend and push budget to your best sellers, even with hundreds of products."),
    ("Do you work with Shopify and WooCommerce stores?", "Yes. I work with Shopify, WooCommerce and other platforms, and I can connect your store to Merchant Center using the right feed method."),
    ("What reports will I get?", "You get clear monthly reports showing sales, spend, return and your best products, plus updates whenever something important changes."),
    ("Can you fix my existing Shopping account?", "Yes. I audit your Merchant Center and campaigns, fix the feed and rebuild the structure so your Shopping Ads become profitable again."),
    ("How do I get started?", "Just book a free Google Shopping audit using the button on this page. I will review your store and feed and show you how we can grow your sales."),
]

RELATED = [
    ("Performance marketing", "/services/performance-marketing/"),
    ("Google Ads", "/services/google-ads/"),
    ("Amazon Ads", "/services/amazon-ads/"),
    ("Remarketing", None),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
    ("Ecommerce websites", None),
]

PAGE = {
    "path": "/services/google-shopping-ads/",
    "slug": "google-shopping-ads", "thanks": "paid-ads",
    "form_name": "google_shopping_ads",
    "service": "Google Shopping Ads",
    "service_name": "Google Shopping Ads management",
    "thanks_what": "Google Shopping audit",
    "category": "Shopping advertising",
    "service_desc": "Google Shopping Ads management covering Merchant Center setup, product feed optimization, Standard Shopping, Performance Max for retail and Shopping remarketing, with bid management, disapproval fixes, conversion tracking and monthly reporting.",
    "audience": "Online stores that sell physical products",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What Google Shopping Ads management includes",
    "offers": GET,
    "title": "Google Shopping Ads Services | Sushant Rana",
    "og_title": "Google Shopping Ads Services",
    "og_alt": "Google Shopping Ads services by Sushant Rana",
    "desc": "Google Shopping Ads services that put your products, prices and images in front of ready to buy shoppers. Feed setup, full tracking. Book a free audit.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Google Shopping Ads", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Google Shopping Ads", "questions, answered"),
            "body": ["Merchant Center, feeds, budgets and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Google Shopping Ads",
        "h1": ("Google Shopping Ads services that put your products", "in front of buyers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I set up and manage Shopping campaigns that bring ready to buy shoppers to your store. Google Shopping Ads show your product image, price and store name right in the search results, so shoppers can see what you sell before they even click.',
            "Shopping Ads are one of the best channels for ecommerce, because the shopper already knows the product and the price when they click. We run Google Shopping for online stores across India, the US and Canada.",
        ],
        "cta2": ("See campaign types", "#types"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free Google Shopping audit",
        "sub": "Tell me about your store and I will review your feed and campaigns for free.",
        "submit": "Request my free audit",
        "steps": [
            {"label": "Store", "fields": [
                {"type": "radio", "name": "platform", "label": "Your store platform", "req": True,
                 "options": ["Shopify", "WooCommerce", "Other", "Not sure"]},
                {"type": "radio", "name": "running", "label": "Are you running Shopping ads now?",
                 "options": ["Yes, running now", "Paused or stopped", "Never run them"]},
                {"type": "text", "name": "site", "label": "Store website", "req": True, "placeholder": "yourstore.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "select", "name": "products", "label": "Number of products", "placeholder": "Select a range",
                 "options": ["1 - 50", "51 - 200", "201 - 1,000", "1,000+"]},
                {"type": "checkbox", "name": "fix", "label": "What do you need help with?",
                 "options": ["Merchant Center setup", "Feed optimization", "Disapproved products", "Campaign build", "Performance Max", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, your best products, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Google Shopping", "Merchant Center", "Product feed", "Performance Max", "Shopping remarketing", "Disapproved products", "ROAS"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What Google Shopping Ads are", "and how they sell"),
             "body": ["Google Shopping Ads are product ads that appear at the top of Google search with an image, a price and your store name. They are powered by two tools working together, Google Merchant Center, which holds your product information, and Google Ads, which runs the campaigns.",
                      "Because the shopper sees the product and price before clicking, the clicks you get are more likely to turn into sales. This makes Shopping one of the highest value channels for any online store."],
             "bullets": ["Image, price and store name in search", "Merchant Center plus Google Ads", "Clicks from shoppers who already know the price"],
             "cta": CTA, "visual": shop_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why Google Shopping Ads are", "great for ecommerce"),
                      "body": ["Shopping puts the product itself in front of the shopper. Here is why that works so well for online stores."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "image", "h3": "Your products are seen, not just read", "p": "Shopping Ads show a real photo of your product. People shop with their eyes, so a clear image gets far more attention than a plain text ad."},
                          {"icon": "target", "h3": "High buyer intent", "p": "Shopping Ads appear when people are searching for a product to buy. These are warm shoppers who are close to a purchase."},
                          {"icon": "wallet", "h3": "The price is shown upfront", "p": "Because the price is visible before the click, the people who click are already comfortable with your pricing. This means better quality clicks and less wasted spend."},
                          {"icon": "chart", "h3": "Strong return for online stores", "p": "When the feed and campaigns are set up well, Shopping often gives one of the best returns on ad spend for ecommerce."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "Campaign types", "h2": ("The Shopping campaign types", "I run"),
                           "body": ["Each campaign type gives a different balance of control and reach. I pick the right mix for your store. Pick one to see how it works."],
                           "items": CAMPAIGNS})),
    L.split({"id": "how", "pill": "How it works", "h2": ("How Google Shopping", "actually works"),
             "body": ["Shopping Ads do not use keywords the way Search Ads do. Instead, Google reads your product feed, which is a file that lists all your products with their titles, images, prices and details. Google then decides which searches to show your products for, based on that feed.",
                      "This is why the feed is the real engine behind Shopping. A clean, well written feed leads to better placement and cheaper sales. A messy feed holds your whole account back, no matter how much you spend."],
             "bullets": ["No keywords, the feed decides", "Titles, images, prices and details", "A clean feed means better placement"],
             "visual": feed_box}, dark=True, flip=True),
    L.split({"id": "secret", "pill": "The secret", "h2": ("Why the product feed is", "the most important part"),
             "body": ["Most Shopping accounts fail because of a weak product feed, not a weak budget. If your product titles are unclear or your images are poor, Google shows your products for the wrong searches and your sales suffer.",
                      "I spend real time getting your feed right. This means clear, keyword rich titles, correct product types, strong images and complete details. A strong feed is the single biggest thing that lifts your Shopping results."],
             "visual": leak_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My Google Shopping", "process"),
                   "body": ["Five clear stages, from a healthy Merchant Center to scaling the products that sell. Pick a stage to follow along."],
                   "steps": [
                       {"h3": "Merchant Center setup", "short": "Setup", "p": "I set up or fix your Google Merchant Center and make sure your account and products are approved and healthy.", "points": ["Account set up or fixed", "Products approved", "Store connected"]},
                       {"h3": "Product feed optimization", "short": "Feed", "p": "I improve your product titles, types, images and details, because the feed is what decides where your products show.", "points": ["Clear titles", "Correct product types", "Strong images and details"]},
                       {"h3": "Campaign build and structure", "short": "Build", "p": "I build a clean campaign structure that separates your products in a smart way, so we can control bids and spend.", "points": ["Smart product groups", "Bid control", "Conversion tracking"]},
                       {"h3": "Bid and priority optimization", "short": "Optimize", "p": "I adjust bids, cut wasted spend and push budget to your best selling products every week.", "points": ["Weekly bid changes", "Wasted spend cut", "Best sellers pushed"]},
                       {"h3": "Reporting and scaling", "short": "Scale", "p": "You get clear reports on sales, spend and return. When a set of products is profitable, we scale it up carefully.", "points": ["Sales, spend and return", "Best products", "Careful scaling"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my Google Shopping service"),
                  "body": ["You get a complete, done for you Google Shopping service. I handle the feed, the setup, the daily work and the reporting, and you always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free audit", "h3": "Want more sales from your online store?",
                                       "p": "Let me look at your store and your product feed and show you how Google Shopping can bring ready to buy shoppers. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why online stores", "choose me"),
                  "body": ["The person who manages your feed and campaigns is the person you talk to, and the work starts with the feed, not just the bids."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person who builds and runs your campaigns and manages your feed, with clear answers and fast replies."},
                      {"h3": "Feed first approach", "p": "I focus on getting your product feed right, which is what really drives Shopping results, instead of only changing bids."},
                      {"h3": "Honest reporting", "p": "I report on sales, spend and return in plain language, so you always know what your budget is doing."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Online stores", "I work with"),
                     "body": "I run Google Shopping for Shopify stores, WooCommerce stores and other ecommerce platforms, across many product categories. If you sell physical products online, Shopping Ads can grow your sales.",
                     "chips": [("Ecommerce brands", None), ("Shopify stores", None), ("WooCommerce stores", None), ("Other ecommerce platforms", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "Google Shopping"),
                     "body": "Online stores often run Shopping alongside Google Ads, Amazon and remarketing, with a store and SEO built to convert the clicks.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to grow", "your online store?"),
               "p": "Let us look at your products and your feed together and build a Shopping plan that brings ready to buy shoppers to your store.",
               "btn": CTA, "note": "No obligation · Free Google Shopping audit"}),
]
