# Landing Page Design Services. Copy: 18_Landing_Page_Design_Services.txt
# No numbers beyond the shared hero stats. Mocks are labelled "Example" or "Live demo".
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Get your free landing page quote"

# lucide star, local to this page
L.ICON.update({
    "star": '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"></path>',
})

# ------------------------------------------------------------ mock helpers
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
MIRROR_IN = "min-w-0 flex-1 bg-transparent text-sm text-ink outline-none"


def note(text, icon="target"):
    return ('<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def lines(*widths):
    return "".join(f'<span class="mt-2 block h-2 {w} rounded-full bg-ink/10"></span>' for w in widths)


def toggle(pairs, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(label)}</button>'
        for i, (k, label) in enumerate(pairs)) + "</div>"


def browser(body, url="yourbusiness.com"):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="flex items-center gap-1.5 border-b border-[var(--color-line)] px-3 py-2">'
            '<span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span>'
            f'<span class="ml-2 flex-1 truncate rounded-full bg-ink/[0.06] px-3 py-0.5 text-[10px] text-muted">{E(url)}</span></div><div class="p-4">{body}</div></div>')


def btn(text, cls=""):
    return f'<span class="inline-flex rounded-full bg-orange px-3 py-1.5 text-[11px] font-bold text-white {cls}">{E(text)}</span>'


def field_box(label):
    return f'<span class="block rounded-lg border border-[var(--color-line)] px-3 py-1.5 text-[10px] text-muted">{E(label)}</span>'


def stars(cls="h-3 w-3"):
    return '<span class="flex gap-0.5 text-orange" aria-hidden="true">' + svg("star", cls) * 5 + "</span>"


def flow(items):
    return '<ol class="grid list-none gap-2.5">' + "".join(
        f'<li class="flex items-center gap-3 rounded-2xl border {"border-orange bg-[#fff7f3]" if hot else "border-[var(--color-line)] bg-white"} p-3.5">'
        f'<span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
        f'<span class="text-sm font-semibold text-ink">{E(t)}</span></li>' for i, (t, hot) in enumerate(items, 1)) + "</ol>"


FORM = f'<div class="mt-3 grid gap-2">{field_box("Your name")}{field_box("Phone or email")}</div>'

# ------------------------------------- 01 basics: homepage vs landing page
NAVLINKS = '<div class="flex flex-wrap gap-1.5" aria-hidden="true">' + "".join(
    f'<span class="rounded-full bg-ink/[0.06] px-2 py-0.5 text-[10px] font-semibold text-muted">{t}</span>'
    for t in ("Home", "About", "Services", "Blog", "Careers", "Gallery", "Contact")) + "</div>"
homepage = browser(
    NAVLINKS + '<p class="mt-4 text-base font-extrabold leading-tight text-ink">Welcome to Your Business</p>' + lines("w-full", "w-5/6")
    + '<div class="mt-3 grid grid-cols-3 gap-2" aria-hidden="true">' + '<span class="block h-10 rounded-lg bg-ink/10"></span>' * 3 + "</div>")
landing = browser(
    '<p class="text-base font-extrabold leading-tight text-ink"><span data-mirror-out="promise" class="svc-cap"></span></p>' + lines("w-5/6")
    + f'<div class="mt-2">{stars()}</div>{FORM}<div class="mt-2">{btn("Claim this offer", "w-full justify-center")}</div>', "yourbusiness.com/offer")

focus = '<div data-tabs="true">' + figure("Where your ad click lands", ["Live demo"], (
    f'<label class="block"><span class="{CAP}">Type what your ad promises</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("pen", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="promise" placeholder="free roof inspection this week" class="{MIRROR_IN}" aria-label="Ad promise to preview"/></span></label>'
    '<div class="mt-4 rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] font-bold text-ink">Sponsored</p><p class="text-[11px] text-muted">yourbusiness.com</p>'
    '<p class="svc-serp-title mt-1 text-base font-bold leading-snug"><span data-mirror-out="promise" class="svc-cap"></span> | Your Business</p></div>'
    f'<p class="mt-4 {CAP}">The click lands on</p><div class="mt-2.5">{toggle([("home", "Your homepage"), ("landing", "A landing page")], 1)}</div>'
    f'<div class="mt-4" data-panel="home"{HID}>{homepage}'
    + note("<strong class=\"font-semibold text-ink\">Many links and many choices,</strong> and the promise from the ad is nowhere to be seen.")
    + f'</div><div class="mt-4" data-panel="landing">{landing}'
    + note("<strong class=\"font-semibold text-ink\">One message, one offer, one action.</strong> The page picks up exactly where the ad left off.")
    + "</div>")) + "</div>"

# ------------------------------------------------- 03 what I build: mocks
MOCKS = {
    "ads": figure("Paid ad landing page", ["Example"], (
        flow([("Google or Meta ad with one promise", False), ("Landing page that repeats the same promise", True), ("Lead or sale", False)])
        + note("The page matches your ad, so more paid clicks turn into leads and sales."))),
    "lead": figure("Lead generation page", ["Example"], browser(
        '<p class="text-base font-extrabold leading-tight text-ink">Your service, with one clear offer</p>' + lines("w-full", "w-2/3")
        + FORM + f'<div class="mt-2">{btn("Get my free quote", "w-full justify-center")}</div>', "yourbusiness.com/quote")),
    "product": figure("Product and sales page", ["Example"], browser(
        f'<div class="grid grid-cols-2 items-center gap-3"><span class="grid aspect-square place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg("bag", "h-8 w-8")}</span>'
        '<div class="min-w-0"><p class="text-sm font-extrabold leading-tight text-ink">Product one</p><ul class="mt-2 grid list-none gap-1">' + "".join(
            f'<li class="flex items-center gap-1.5 text-[11px] text-body">{svg("check", "h-3 w-3 text-orange", 3)}{t}</li>' for t in ("Main benefit", "Second benefit", "Third benefit"))
        + f'</ul><div class="mt-3">{btn("Buy now")}</div></div></div>', "yourbusiness.com/product-one")),
    "event": figure("Event and webinar page", ["Example"], browser(
        '<p class="text-[10px] font-bold uppercase tracking-wider text-orange">Free webinar</p>'
        '<p class="mt-1 text-base font-extrabold leading-tight text-ink">Your workshop title</p>'
        '<div class="mt-3 flex flex-wrap gap-2"><span class="rounded-full bg-ink/[0.06] px-3 py-1 text-[10px] font-bold text-ink">Date and time</span>'
        '<span class="rounded-full bg-ink/[0.06] px-3 py-1 text-[10px] font-bold text-ink">Online</span></div>'
        + FORM + f'<div class="mt-2">{btn("Save my seat", "w-full justify-center")}</div>', "yourbusiness.com/webinar")),
    "app": figure("App and download page", ["Example"], (
        '<div class="flex items-center gap-4"><div class="w-24 shrink-0 rounded-2xl border-2 border-ink/25 bg-white p-2" aria-hidden="true">'
        '<span class="mx-auto block h-1 w-8 rounded-full bg-ink/15"></span><span class="grad-ink-orange mt-2 block h-14 rounded-lg"></span>'
        + lines("w-full", "w-2/3") + '</div><div class="min-w-0 flex-1"><p class="text-base font-extrabold leading-tight text-ink">Your app or free resource</p>'
        + lines("w-full") + f'<div class="mt-3 flex flex-wrap gap-2">{btn("Download")}<span class="inline-flex rounded-full border border-[var(--color-line)] px-3 py-1.5 text-[11px] font-bold text-ink">Get the free guide</span></div></div></div>'
        + note("Built to get more downloads or sign ups."))),
    "click": figure("Click through page", ["Example"], (
        flow([("Someone clicks your ad", False), ("Warm up page builds interest", True), ("They continue to your store or checkout", False)])
        + note("Interest first, then the store, so visitors arrive ready to buy."))),
}

TYPES = [
    ("ads", "Paid ad landing pages", "click", "Pages built to match your Google or Meta ads, so you turn more of your paid clicks into leads and sales."),
    ("lead", "Lead generation pages", "users", "Pages designed to capture enquiries for service businesses, with a clear offer and a simple form."),
    ("product", "Product and sales pages", "bag", "Focused pages that present one product or offer and guide the visitor towards buying."),
    ("event", "Event and webinar pages", "play", "Pages that drive sign ups for your events, webinars and workshops."),
    ("app", "App and download pages", "zap", "Pages built to get more downloads or sign ups for your app or free resource."),
    ("click", "Click through pages", "repeat", "Warm up pages that build interest before sending visitors to your main store or checkout."),
]

# --------------------------------- 04 the secret: landing page anatomy tabs
PARTS = [
    ("headline", "Headline", "A clear headline that matches what the visitor expects from your ad."),
    ("offer", "Offer", "One single goal and a strong offer, with nothing pulling the visitor elsewhere."),
    ("proof", "Proof", "Trust signals near the decision, so the visitor feels safe to act."),
    ("form", "Form", "A simple form that asks only for what you need."),
    ("cta", "CTA", "One clear button that says exactly what happens next."),
]


def anatomy_page(hi):
    def blk(k, inner):
        look = "border-2 border-orange bg-[#fff7f3]" if k == hi else "border border-[var(--color-line)] bg-white opacity-60"
        return f'<div class="rounded-xl {look} p-3">{inner}</div>'
    return browser(
        '<div class="grid gap-2">'
        + blk("headline", '<p class="text-sm font-extrabold leading-tight text-ink">Your headline, matching your ad</p>')
        + blk("offer", '<p class="text-[11px] font-bold text-ink">The one offer</p>' + lines("w-full", "w-2/3"))
        + blk("proof", f'<div class="flex items-center justify-between gap-2">{stars()}<span class="text-[10px] font-semibold text-muted">Reviews and client logos</span></div>')
        + blk("form", f'<div class="grid gap-2">{field_box("Your name")}{field_box("Phone or email")}</div>')
        + blk("cta", btn("Send my enquiry", "w-full justify-center"))
        + "</div>", "yourbusiness.com/offer")


part_btns = '<div class="flex flex-wrap gap-1.5">' + "".join(
    f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white border-orange" data-off="bg-white text-ink border-[var(--color-line)] hover:text-orange" '
    f'class="rounded-full border px-3.5 py-1.5 text-xs font-bold transition {"bg-orange text-white border-orange" if i == 0 else "bg-white text-ink border-[var(--color-line)] hover:text-orange"}">{E(n)}</button>'
    for i, (k, n, _) in enumerate(PARTS)) + "</div>"
anatomy = '<div data-tabs="true">' + figure("Anatomy of a landing page", ["Example"], (
    f'<p class="{CAP}">Pick a part to highlight it</p><div class="mt-2.5">{part_btns}</div>'
    + "".join(
        f'<div class="mt-4" data-panel="{k}"{HID if i else ""}>{anatomy_page(k)}'
        + note(f'<strong class="font-semibold text-ink">{E(n)}.</strong> {E(w)}') + "</div>"
        for i, (k, n, w) in enumerate(PARTS))
    + note("And all of it loads fast, because a slow page loses people before they read a word.", "zap"))) + "</div>"

page_box = '<div class="mt-8">' + L.leak_check(
    "Landing page check", "Tick everything that sounds like the page your ads send people to.",
    [("My ads send people to my home page", "Many links and goals pull visitors away from the one action you want."),
     ("The headline does not match what my ad promised", "Visitors who do not see what they clicked for leave."),
     ("There are no reviews or trust signals near the form", "People hesitate when nothing tells them you are safe to choose."),
     ("The form asks for a lot of details", "Every extra field gives people a reason to give up."),
     ("The page loads slowly on a phone", "Most traffic comes from phones, and slow pages lose it.")],
    ("Nothing ticked. A free quote still covers how to lift results from the traffic you already have.",
     "A weak spot or two. These are the first things I fix on a page that does not convert.",
     "Your page is very likely wasting your ad budget. Let me show you what a proper landing page would change."),
    CTA, "Weak spots ticked") + "</div>"

# ----------------------------------------------------------------- content
GET = [
    {"icon": "pen", "h3": "Conversion focused copy", "p": "The message and the flow written for you, because the words and their order are what really drive conversions."},
    {"icon": "image", "h3": "Clean design", "p": "A clean, focused page that looks professional and guides the visitor towards the action."},
    {"icon": "zap", "h3": "Fast, mobile friendly build", "p": "A page that loads quickly and works perfectly on phones, where most of your traffic comes from."},
    {"icon": "file", "h3": "A simple form", "p": "A short form that asks only for what you need, and can feed your CRM, email tool or spreadsheet."},
    {"icon": "chart", "h3": "Conversion tracking", "p": "Every lead and sale from the page counted correctly, so we can measure and improve results."},
    {"icon": "sliders", "h3": "Ready for testing", "p": "A setup that lets us test headlines, offers and layouts and keep lifting your conversion rate."},
]

FAQ = [
    ("What is a landing page?", "A landing page is a single, focused page built for one goal, like getting a lead or a sale. It removes distractions and guides the visitor towards one clear action."),
    ("How is a landing page different from my homepage?", "Your homepage has many links and goals. A landing page has just one message and one action, which is why it converts far better for ads and offers."),
    ("Why do I need a separate landing page for my ads?", "Sending ad traffic to your homepage wastes clicks. A dedicated landing page matches your ad and focuses the visitor, so you get more leads and sales from the same budget."),
    ("What makes a landing page convert?", "A clear headline, one single goal, a strong offer, trust signals, fast loading and a simple form. I build all of these into your page."),
    ("How long does it take to build?", "Most landing pages take a few days to a couple of weeks depending on the design and copy. I will give you a clear timeline once I know your needs."),
    ("Will my landing page be mobile friendly?", "Yes. Most traffic comes from phones, so every page I build is designed to look and work perfectly on mobile."),
    ("Do you write the copy?", "Yes. I write conversion focused copy, because the words and the message are what really drive results, not just the design."),
    ("Do you set up tracking?", "Yes. I set up conversion tracking so every lead and sale from the page is counted correctly, which lets us measure and improve results."),
    ("Can you A/B test the page?", "Yes. I build your page so we can test different headlines, offers and layouts and keep lifting your conversion rate over time."),
    ("How soon will I see results?", "A landing page can start converting the moment your traffic hits it. From there, testing helps push your results higher over the following weeks."),
    ("Can you connect it to my CRM or email tool?", "Yes. I can connect your form to your CRM, email tool or spreadsheet, so leads flow straight into your system for follow up."),
    ("Can you build on WordPress, Shopify or a page builder?", "Yes. I can build your landing page on WordPress, Shopify or a dedicated landing page tool, depending on what suits you best."),
    ("Will the page load fast?", "Yes. Speed is vital for conversions, so I build your page to load quickly, which also helps with ad quality and rankings."),
    ("What reports will I get?", "You get clear reporting on visits, conversions and conversion rate, so you can see exactly how well the page is performing."),
    ("How do I get started?", "Just request your free landing page quote using the button on this page. Tell me about your offer and I will explain how I can help."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("WordPress development", "/services/wordpress-development/"),
    ("Shopify store development", "/services/shopify-store-development/"),
    ("Website maintenance", "/services/website-maintenance/"),
    ("Lead generation", None),
]

PAGE = {
    "path": "/services/landing-pages/",
    "slug": "landing-pages",
    "form_name": "landing_pages",
    "service": "Landing Pages",
    "service_name": "Landing page design",
    "thanks_what": "landing page quote",
    "category": "Conversion rate optimization",
    "service_desc": "Landing page design and development for paid ads, lead generation, product and sales offers, events and webinars, app downloads and click through pages, with conversion focused copy, a fast mobile build, a simple form, conversion tracking and a setup ready for testing.",
    "audience": "Businesses running paid ads or campaigns that need more leads and sales from their traffic",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What landing page design includes",
    "offers": GET,
    "title": "Landing Page Design Services That Convert | Sushant Rana",
    "og_title": "Landing Page Design Services That Convert",
    "og_alt": "Landing page design services by Sushant Rana",
    "desc": "Landing page design services that turn your ad clicks into leads and sales, with strong copy, clean design and full tracking. Free quote.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Landing Pages", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Landing page", "questions, answered"),
            "body": ["Copy, tracking, testing and timelines. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Landing page design",
        "h1": ("Landing page design that turns your", "clicks into customers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I design high converting landing pages that turn your clicks into real leads and sales, so every rupee you spend works harder. If you are sending ad traffic to a page that just does not convert, a weak landing page can waste your entire ad budget.',
            "A landing page has one job, to get the visitor to take one action. We build focused pages with strong copy, clean design and proper tracking, so you get more results from the same traffic.",
        ],
        "cta2": ("See what makes a page convert", "#anatomy"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Get your free landing page quote",
        "sub": "Tell me about your offer and your traffic, and I will send you a clear quote.",
        "submit": "Request my free quote",
        "steps": [
            {"label": "Traffic", "fields": [
                {"type": "radio", "name": "traffic", "label": "Where will the visitors come from?", "req": True,
                 "options": ["Google Ads", "Meta Ads", "Email or social", "Not running ads yet", "Not sure"]},
                {"type": "select", "name": "page_type", "label": "Type of page", "req": True, "placeholder": "Select a page type",
                 "options": ["Paid ad landing page", "Lead generation page", "Product or sales page", "Event or webinar page", "App or download page", "Click through page", "Not sure"]},
                {"type": "text", "name": "current_page", "label": "Current page, if any", "placeholder": "yourwebsite.com/offer", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Details", "fields": [
                {"type": "checkbox", "name": "needs", "label": "What do you need?",
                 "options": ["Copywriting", "Design", "Tracking", "CRM or email connection", "A/B testing", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Your offer", "placeholder": "What you are promoting, who it is for, where the page should live..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Paid ad landing pages", "Lead generation", "Sales pages", "Webinar pages", "Conversion copy", "Tracking", "A/B testing"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What a landing page is", "and why it matters"),
             "body": ["A landing page is a single, focused page built for one goal, such as getting a lead, a call or a sale. Unlike a normal website page, it removes distractions and guides the visitor towards one clear action.",
                      "This matters because focus wins. When a visitor lands on a page with one message and one offer, they are far more likely to act than on a busy page with many links and choices. This is why landing pages convert so much better."],
             "bullets": ["One message that matches your ad", "One offer, one action", "Every lead and sale tracked"],
             "cta": CTA, "visual": focus}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why a good landing page", "makes you more money"),
                      "body": ["The same traffic, sent to a better page, brings more leads and sales."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "target", "h3": "Focus means higher conversions", "p": "One message and one clear action lead to far more leads and sales than a normal page that pulls people in many directions."},
                          {"icon": "click", "h3": "Perfect for paid ads", "p": "If you run ads, a dedicated landing page stops you wasting your budget. It matches your ad promise and turns more clicks into customers."},
                          {"icon": "zap", "h3": "Faster leads and sales", "p": "A strong landing page can start bringing results the moment your traffic hits it, which makes it perfect for offers and campaigns."},
                          {"icon": "sliders", "h3": "Easy to test and improve", "p": "Because a landing page is focused, it is simple to test different versions and keep pushing your results higher."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I build", "h2": ("The landing pages", "I build for you"),
                           "body": ["Every page is built for one goal. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in TYPES]})),
    L.split({"id": "secret", "anchor": "anatomy", "pill": "The secret", "h2": ("What actually makes", "a landing page convert"),
             "body": ["A landing page is not just a pretty design. It converts because of a few key things working together. A clear headline that matches what the visitor expects, one single goal, a strong offer, trust signals, fast loading and a simple form.",
                      "I build every one of these into your page. I focus on the message and the flow, not just the looks, because that is what actually turns visitors into customers. A beautiful page that does not convert is a waste, and I will not build you one."],
             "after": page_box, "visual": anatomy}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My landing page", "process"),
                   "body": ["Five clear steps, from the one action you want to a page that keeps getting better."],
                   "steps": [
                       {"h3": "Goal and offer", "short": "Goal", "p": "I get clear on the one action you want and the offer that will make people take it.", "points": ["One clear action", "The right offer", "Who the page is for"]},
                       {"h3": "Copy and structure", "short": "Copy", "p": "I write the message and plan the flow, since the words and order are what really drive conversions.", "points": ["Headline that matches the ad", "Message and flow", "Trust signals placed"]},
                       {"h3": "Design", "short": "Design", "p": "I design a clean, focused page that looks professional and guides the visitor towards the action.", "points": ["Clean, focused layout", "Built for mobile", "One clear button"]},
                       {"h3": "Build and tracking", "short": "Build", "p": "I build the page to load fast and set up tracking, so every lead and sale is counted correctly.", "points": ["Fast loading build", "Conversion tracking", "Form connected"]},
                       {"h3": "Test and improve", "short": "Test", "p": "I set the page up so we can test different versions and keep lifting your conversion rate over time.", "points": ["Headline and offer tests", "Layout tests", "Results tracked"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included when", "you work with me"),
                  "body": ["You get a complete, done for you landing page built to convert, not just to look nice. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free quote", "h3": "Are your ads sending traffic to a page that does not convert?",
                                       "p": "Let me look at your offer and your current page and show you how a proper landing page can turn more of your clicks into customers. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for landing pages"),
                  "body": ["Copy and flow first, built by the person you talk to, and set up to keep improving."],
                  "cards": [
                      {"h3": "You work directly with me", "p": "You deal with the person building your page, with clear communication and fast replies."},
                      {"h3": "Conversion first, not just design", "p": "I focus on the copy and flow that actually convert, not just how the page looks."},
                      {"h3": "Built to test and improve", "p": "I set your page up so we can keep testing and lifting results, rather than building it once and forgetting it."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Who needs a high converting", "landing page"),
                     "body": "I build landing pages for businesses running paid ads, service providers who need leads, online stores promoting offers, coaches and course creators, and anyone launching a new product or campaign. If you want more results from your traffic, a landing page can help.",
                     "chips": [("Service providers", None), ("Online stores", None), ("Coaches and course creators", "/industries/education/"),
                               ("Healthcare", None), ("Real estate", "/industries/real-estate/"), ("SaaS", None),
                               ("B2B companies", None), ("New product launches", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "landing pages"),
                     "body": "Landing pages and ads work together, and a well looked after site keeps every page fast.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to turn more clicks", "into customers?"),
               "p": "Let us look at your offer and build a landing page that gets more leads and sales from the traffic you already have.",
               "btn": CTA, "note": "No obligation · Free landing page quote"}),
]
