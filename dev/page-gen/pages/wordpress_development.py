# WordPress Website Development Services. Copy: 16_WordPress_Development_Services.txt
# No numbers beyond the shared hero stats and L.PROJECTS. The client projects are
# websites we built and run; never call them WordPress sites. Mocks are "Example".
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Get your free WordPress website quote"

# lucide monitor and smartphone, local to this page
L.ICON.update({
    "monitor": '<rect width="20" height="14" x="2" y="3" rx="2"></rect><line x1="8" x2="16" y1="21" y2="21"></line><line x1="12" x2="12" y1="17" y2="21"></line>',
    "mobile": '<rect width="14" height="20" x="5" y="2" rx="2" ry="2"></rect><path d="M12 18h.01"></path>',
})

# ------------------------------------------------------------ mock helpers
TONE = {"ok": "bg-ink/[0.06] text-ink", "warn": "bg-orange/10 text-orange", "bad": "bg-red-50 text-red-700",
        "hot": "bg-orange text-white", "off": "bg-ink/[0.06] text-muted"}
CAP = "text-[10px] font-bold uppercase tracking-wider text-muted"
MIRROR_IN = "min-w-0 w-full rounded-xl border border-[var(--color-line)] bg-white px-3 py-2 text-sm text-ink outline-none transition focus:border-orange"


def tag(text, tone="ok"):
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {TONE[tone]}">{E(text)}</span>'


def rows(items):
    """items = [(title, right_html, sub)]"""
    return '<ul class="grid list-none gap-2.5">' + "".join(
        '<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid min-w-0"><span class="truncate text-sm font-bold text-ink">{E(t)}</span>'
        + (f'<span class="text-xs text-muted">{E(s)}</span>' if s else "") + f'</span>{r}</li>'
        for t, r, s in items) + "</ul>"


def note(text, icon="target"):
    return ('<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def lines(*widths):
    return "".join(f'<span class="mt-2 block h-2 {w} rounded-full bg-ink/10"></span>' for w in widths)


def toggle(pairs, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex flex-1 items-center justify-center gap-1.5 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{svg(ic, "h-3.5 w-3.5")}{E(label)}</button>'
        for i, (k, label, ic) in enumerate(pairs)) + "</div>"


def browser(body, url="yourbusiness.com"):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="flex items-center gap-1.5 border-b border-[var(--color-line)] px-3 py-2">'
            '<span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span>'
            f'<span class="ml-2 flex-1 truncate rounded-full bg-ink/[0.06] px-3 py-0.5 text-[10px] text-muted">{E(url)}</span></div><div class="p-4">{body}</div></div>')


def btn(text, cls=""):
    return f'<span class="inline-flex rounded-full bg-orange px-3 py-1 text-[10px] font-bold text-white {cls}">{E(text)}</span>'


IMG = f'<span class="grid aspect-[4/3] place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg("image", "h-6 w-6")}</span>'
NAME = '<span data-mirror-out="wpbiz"></span>'
NAV = ('<div class="flex items-center justify-between gap-3" aria-hidden="true"><span class="block h-3 w-16 rounded-full bg-ink/15"></span>'
       '<span class="flex gap-2"><span class="block h-2 w-8 rounded-full bg-ink/10"></span><span class="block h-2 w-8 rounded-full bg-ink/10"></span><span class="block h-2 w-8 rounded-full bg-ink/10"></span></span></div>')


def card_row(n=3):
    return f'<div class="mt-4 grid grid-cols-{n} gap-2" aria-hidden="true">' + (
        f'<span class="rounded-xl border border-[var(--color-line)] p-3"><span class="grid h-6 w-6 place-items-center rounded-lg bg-orange/10 text-orange">{svg("check", "h-3.5 w-3.5", 3)}</span>'
        '<span class="mt-2 block h-2 w-full rounded-full bg-ink/10"></span></span>') * n + "</div>"


# ------------------------------------------------ 01 basics: device preview
desktop_view = browser(
    NAV + '<div class="mt-4 grid grid-cols-2 items-center gap-4"><div class="min-w-0">'
    f'<p class="truncate text-base font-extrabold leading-tight text-ink">{NAME}</p>' + lines("w-full", "w-2/3")
    + f'<div class="mt-3">{btn("Get a quote")}</div></div>{IMG}</div>' + card_row())
phone_view = (
    '<div class="mx-auto w-full max-w-[236px] rounded-[28px] border-2 border-ink/25 bg-white p-3">'
    '<span class="mx-auto block h-1 w-8 rounded-full bg-ink/15"></span>'
    '<div class="mt-3 flex items-center justify-between" aria-hidden="true"><span class="block h-3 w-16 rounded-full bg-ink/15"></span>'
    '<span class="grid gap-1"><span class="block h-0.5 w-4 bg-ink/70"></span><span class="block h-0.5 w-4 bg-ink/70"></span><span class="block h-0.5 w-4 bg-ink/70"></span></span></div>'
    f'<p class="mt-4 truncate text-base font-extrabold leading-tight text-ink">{NAME}</p>' + lines("w-full", "w-3/4")
    + f'<div class="mt-3">{btn("Get a quote", "w-full justify-center")}</div><div class="mt-3">{IMG}</div>' + card_row(2) + "</div>")

devices = '<div data-tabs="true">' + figure("Your new website", ["Live demo"], (
    f'<label class="block"><span class="{CAP}">Your business name</span><input data-mirror="wpbiz" placeholder="Your Business" class="mt-1.5 {MIRROR_IN}" aria-label="Business name to preview"/></label>'
    f'<div class="mt-4">{toggle([("desktop", "Desktop", "monitor"), ("phone", "Phone", "mobile")])}</div>'
    f'<div class="mt-4" data-panel="desktop">{desktop_view}</div><div class="mt-4" data-panel="phone"{HID}>{phone_view}</div>'
    + note("<strong class=\"font-semibold text-ink\">One site that works on every screen,</strong> built around your brand and easy for you to update."))) + "</div>"

# ------------------------------------------------- 03 what I build: mocks
MOCKS = {
    "business": figure("Business website", ["Example"], browser(
        NAV + '<p class="mt-4 text-base font-extrabold leading-tight text-ink">Your service, explained clearly</p>' + lines("w-full", "w-5/6")
        + f'<div class="mt-3 flex flex-wrap gap-2">{btn("Get a quote")}<span class="inline-flex rounded-full border border-[var(--color-line)] px-3 py-1 text-[10px] font-bold text-ink">Call us</span></div>'
        + '<div class="mt-4 flex flex-wrap gap-2">' + "".join(tag(t) for t in ("Reviews", "Services", "Contact")) + "</div>")),
    "custom": figure("Custom design", ["Example"], (
        '<div class="grid grid-cols-2 gap-3">'
        '<div class="rounded-2xl border border-[var(--color-line)] p-3 opacity-60"><p class="' + CAP + '">Generic template</p>'
        '<span class="mt-3 block aspect-[4/3] rounded-xl bg-ink/10"></span>' + lines("w-full", "w-2/3") + '</div>'
        '<div class="rounded-2xl border-2 border-orange bg-[#fff7f3] p-3"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">Built for your brand</p>'
        '<span class="grad-ink-orange mt-3 grid aspect-[4/3] place-items-center rounded-xl text-xs font-extrabold text-white">Your Business</span>'
        + lines("w-full", "w-2/3") + '</div></div>' + note("Designed around your brand, so your site stands out from your competitors."))),
    "builder": figure("Page builder editing", ["Example"], (
        '<div class="flex gap-3"><div class="grid w-16 shrink-0 content-start gap-2">'
        + "".join(f'<span class="rounded-lg border border-[var(--color-line)] bg-white px-2 py-1.5 text-center text-[10px] font-bold text-ink">{t}</span>' for t in ("Heading", "Text", "Image", "Button"))
        + '</div><div class="min-w-0 flex-1 rounded-2xl border border-[var(--color-line)] p-3">'
        '<div class="rounded-lg border-2 border-orange p-2"><p class="text-sm font-extrabold text-ink">Edit this heading</p></div>'
        + lines("w-full", "w-5/6") + f'<div class="mt-3">{btn("Save")}</div></div></div>'
        + note("Click, type, save. Easy for you to edit and update later."))),
    "woo": figure("WooCommerce store", ["Example"], (
        '<div class="grid grid-cols-3 gap-3">' + "".join(
            f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-6 w-6")}</div>'
            f'<div class="p-3"><p class="text-[11px] font-bold leading-tight text-ink">{n}</p><span class="mt-2 block h-4 rounded-full bg-orange"></span></div></div>'
            for n in ("Product one", "Product two", "Product three"))
        + '</div><div class="mt-4 grid grid-cols-3 gap-2">' + "".join(
            f'<span class="rounded-full {"bg-orange text-white" if i == 2 else "bg-ink/[0.06] text-ink"} py-1.5 text-center text-[11px] font-bold">{t}</span>'
            for i, t in enumerate(("Cart", "Checkout", "Paid"))) + "</div>"
        + note("Products, payments and a smooth checkout that is built to sell.", "bag"))),
    "landing": figure("Landing page", ["Example"], browser(
        '<p class="text-base font-extrabold leading-tight text-ink">One offer, one clear headline</p>' + lines("w-5/6")
        + '<div class="mt-3 grid gap-2">' + '<span class="block h-7 rounded-lg border border-[var(--color-line)]"></span>' * 2
        + f'{btn("Send my enquiry", "w-full justify-center py-2")}</div>', "yourbusiness.com/offer")
        + note("Focused pages for your campaigns and offers. No menu, one goal.")),
    "redesign": figure("Website redesign", ["Example"], (
        '<div class="grid grid-cols-2 gap-3">'
        '<div class="rounded-2xl border border-[var(--color-line)] p-3"><p class="' + CAP + '">Before</p>'
        '<div class="mt-3 grid gap-1.5 opacity-50" aria-hidden="true"><span class="block h-3 w-full bg-ink/15"></span><span class="block h-2 w-full bg-ink/10"></span>'
        '<span class="block h-2 w-3/4 bg-ink/10"></span><span class="block h-8 w-full bg-ink/10"></span></div>'
        '<ul class="mt-3 grid list-none gap-1 text-[11px] text-muted"><li>Dated look</li><li>Slow to load</li><li>Hard to use on a phone</li></ul></div>'
        '<div class="rounded-2xl border-2 border-orange bg-[#fff7f3] p-3"><p class="text-[10px] font-bold uppercase tracking-wider text-orange">After</p>'
        '<div class="mt-3"><span class="block h-3 w-2/3 rounded-full bg-ink/15"></span>' + lines("w-full")
        + f'<div class="mt-2">{btn("Get a quote")}</div></div>'
        '<ul class="mt-3 grid list-none gap-1 text-[11px] font-semibold text-ink"><li>Fresh, modern design</li><li>Fast loading</li><li>Built to bring enquiries</li></ul></div></div>'
        + note("We keep what already works and improve both the look and the results."))),
    "speed": figure("Speed and SEO setup", ["Example"], rows([
        ("Fast loading pages", tag("Built in", "warn"), "Light images and clean code"),
        ("Mobile friendly", tag("Built in", "warn"), "Works on phones, tablets and computers"),
        ("Titles and descriptions", tag("Set up", "warn"), "Every page ready to be found"),
        ("Clean page structure", tag("Set up", "warn"), "Clear headings Google can read"),
        ("Tracking", tag("Set up", "warn"), "Forms and enquiries counted"),
    ])),
}

BUILD = [
    ("business", "Business websites", "file", "Clean, professional websites that build trust and turn visitors into enquiries and customers."),
    ("custom", "Custom WordPress design", "pen", "Designs built around your brand, not generic templates, so your site stands out from your competitors."),
    ("builder", "Elementor and page builder sites", "sliders", "Sites built with page builders so they are easy for you to edit and update yourself later."),
    ("woo", "WooCommerce online stores", "bag", "Full online stores on WordPress with products, payments and a smooth checkout that is built to sell."),
    ("landing", "Landing pages", "target", "Focused, high converting landing pages for your campaigns and offers."),
    ("redesign", "Website redesign", "repeat", "A fresh, modern redesign of your old site that improves both looks and results."),
    ("speed", "Speed and SEO setup", "zap", "I build your site to load fast and come SEO ready, so it is set up to rank from the start."),
]

# ------------------------------------------- 06 the difference: self check
site_box = L.leak_check(
    "Is your website costing you?", "Tick everything that sounds like your current website.",
    [("It takes a while to load, especially on a phone", "Slow pages lose visitors before they ever read your offer."),
     ("It looks fine but brings very few enquiries", "A site that just sits there is not guiding visitors towards taking action."),
     ("SEO was never set up when it was built", "Without a search friendly base, the site quietly misses traffic."),
     ("I need a developer for every small change", "You should be able to update your own content and pages."),
     ("I am stuck on a platform I cannot easily move away from", "Your website should be fully yours, to move or change when you want.")],
    ("Nothing ticked. A free quote still covers how to make your next site faster and easier to find.",
     "A gap or two. These are exactly what I build into a site from the start.",
     "Your website is very likely costing you traffic and sales. Let me show you what a fast, SEO ready site would change."),
    CTA, "Issues ticked")

# ----------------------------------------------------------------- content
GET = [
    {"icon": "pen", "h3": "Custom design", "p": "A clean, modern layout built around your brand that guides visitors towards taking action."},
    {"icon": "layers", "h3": "Mobile friendly development", "p": "A site that works well on phones, tablets and computers, with everything working smoothly."},
    {"icon": "zap", "h3": "Fast loading speed", "p": "Speed built in from the start, because a fast site keeps visitors happy and ranks better on Google."},
    {"icon": "search", "h3": "Basic on page SEO setup", "p": "Your pages set up the right way so the site is ready to be found from day one."},
    {"icon": "phone", "h3": "Contact forms and tracking", "p": "Forms that send enquiries to you, with tracking so you can see what the site brings in."},
    {"icon": "users", "h3": "A simple handover", "p": "I show you how to manage your site, so you can update it yourself with confidence."},
]

FAQ = [
    ("Why should I choose WordPress?", "WordPress is flexible, easy to manage and great for SEO. You fully own your site, you can update it yourself, and it can grow with your business over time."),
    ("Can I update the website myself?", "Yes. I build your site so you can edit content, add pages and update images on your own. I also show you how during the handover."),
    ("How long does it take to build a website?", "It depends on the size and features, but most business websites take a few weeks. I will give you a clear timeline once I understand your needs."),
    ("Will my website be mobile friendly?", "Yes. Every site I build works well on phones, tablets and computers, since most visitors and Google both look at the mobile version first."),
    ("Will my website be fast?", "Yes. I build speed into the site from the start, because a fast site keeps visitors happy and ranks better on Google."),
    ("Is WordPress good for SEO?", "Yes. WordPress has a strong SEO foundation, and I set up your site the right way so it is ready to rank from day one."),
    ("Do you use Elementor or custom code?", "I use the right tool for your needs. Page builders like Elementor make it easy for you to edit later, while custom work is used where it adds real value."),
    ("Can you build an online store?", "Yes. I build online stores on WordPress using WooCommerce, with products, payments and a smooth checkout that is designed to sell."),
    ("Can you redesign my existing website?", "Yes. I can give your old site a fresh, modern redesign that improves both its look and its results, while keeping what already works."),
    ("Do you provide the content?", "I can guide your content and help shape it, and I can arrange writing if needed. Good content matters a lot, so I make sure your pages are clear and helpful."),
    ("What about hosting and domain?", "I will guide you on choosing good hosting and a domain, and I can handle the setup for you so everything is done properly."),
    ("Will you train me to use the site?", "Yes. During handover I show you how to manage your site, so you feel confident making updates on your own."),
    ("Do you provide maintenance after launch?", "Yes. I offer website maintenance as a separate service to keep your site updated, secure and running smoothly after launch."),
    ("Is WordPress secure?", "WordPress is secure when it is set up and maintained properly. I follow good practices during the build and can keep it secure with ongoing maintenance."),
    ("What do I get when the site is done?", "You get a complete, working website that you own and can manage, along with a handover so you know how to use it."),
    ("How do I get started?", "Just request your free WordPress quote using the button on this page. Tell me about your business and I will explain how I can help."),
]

RELATED = [
    ("Landing pages", "/services/landing-pages/"),
    ("Website maintenance", "/services/website-maintenance/"),
    ("Website redesign", None),
    ("Ecommerce website", None),
    ("Technical SEO", "/services/technical-seo/"),
    ("On page SEO", "/services/on-page-seo/"),
]

PAGE = {
    "path": "/services/wordpress-development/",
    "slug": "wordpress-development", "thanks": "website",
    "form_name": "wordpress_development",
    "service": "WordPress Development",
    "service_name": "WordPress website development",
    "thanks_what": "WordPress website quote",
    "category": "Website development",
    "service_desc": "WordPress website development covering business websites, custom design, Elementor and page builder sites, WooCommerce stores, landing pages, redesigns, and speed and SEO setup, with a handover so you can manage the site yourself.",
    "audience": "Businesses that need a fast, professional website they can manage themselves",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What WordPress website development includes",
    "offers": GET,
    "title": "WordPress Website Development Services | Sushant Rana",
    "og_title": "WordPress Website Development Services",
    "og_alt": "WordPress website development services by Sushant Rana",
    "desc": "I build fast, SEO ready WordPress websites that look great and are easy for you to manage yourself. Custom design, WooCommerce and more.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("WordPress Development", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("WordPress development", "questions, answered"),
            "body": ["Timelines, editing, hosting and what happens after launch. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "WordPress development",
        "h1": ("WordPress website development that looks great and", "actually performs"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I design and develop WordPress websites that not only look good but also load quickly, rank well and turn visitors into customers. If you want a site that looks professional, loads fast and is easy to update yourself, that is exactly what we build.',
            "WordPress powers a huge part of the web because it is flexible, owner friendly and great for SEO. We build sites that you fully own and can easily manage, without being stuck depending on anyone.",
        ],
        "cta2": ("See websites we built", "#work"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Get your free WordPress website quote",
        "sub": "Tell me about your business and the site you need, and I will send you a clear quote.",
        "submit": "Request my free quote",
        "steps": [
            {"label": "Project", "fields": [
                {"type": "radio", "name": "project", "label": "What do you need?", "req": True,
                 "options": ["New website", "Redesign", "Online store", "Landing page", "Not sure"]},
                {"type": "select", "name": "size", "label": "Roughly how many pages?", "req": True, "placeholder": "Select a size",
                 "options": ["1 to 5 pages", "6 to 15 pages", "16 or more pages", "Not sure yet"]},
                {"type": "text", "name": "site", "label": "Current website, if any", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Details", "fields": [
                {"type": "checkbox", "name": "features", "label": "Features you need",
                 "options": ["Contact forms", "Bookings", "Online store", "Memberships", "Blog", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you do, sites you like, when you need it live..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Custom WordPress design", "Elementor", "WooCommerce", "Landing pages", "Redesigns", "Speed", "SEO ready"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What I build", "with WordPress"),
             "body": ["I build custom WordPress websites for businesses, from simple service sites to full online stores. Every site is designed around your brand and your goals, not squeezed into a generic template.",
                      "The best part is that you stay in control. WordPress is easy to manage, so you can update your own content, add pages and make small changes without needing a developer every time."],
             "bullets": ["Designed around your brand", "Works on every screen", "Easy for you to update"],
             "cta": CTA, "visual": devices}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why WordPress", "h2": ("Why WordPress is a smart choice", "for your website"),
                      "body": ["Flexible, owner friendly and great for SEO, which is why so much of the web runs on it."],
                      "cards": [
                          {"icon": "shield", "h3": "You own and control it", "p": "Your site is fully yours. You are not locked into a closed platform, and you can move or change it whenever you want."},
                          {"icon": "pen", "h3": "Easy to update yourself", "p": "You can edit content, add pages and update images on your own, which saves you time and money over the long run."},
                          {"icon": "search", "h3": "Great for SEO", "p": "WordPress is built in a way that search engines love, which gives your site a strong base to rank well from day one."},
                          {"icon": "layers", "h3": "Endless flexibility", "p": "With the right setup and plugins, WordPress can do almost anything, from bookings to online stores to memberships."},
                          {"icon": "chart", "h3": "It grows with you", "p": "As your business grows, your site can grow too, adding new features and pages without starting over."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I build", "h2": ("The WordPress services", "I offer"),
                           "body": ["From a simple service site to a full online store. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in BUILD]})),
    L.projects_section(["bazayan", "trust", "achievers", "touch"], ("Websites we have", "built and run"),
                       "Real businesses in Switzerland, India and Canada. Pick one to see what we built and what it changed for them."),
    L.split({"id": "difference", "pill": "The difference", "h2": ("Fast and SEO ready", "from day one"),
             "body": ["Many websites are built to look nice but load slowly and ignore SEO, which quietly costs the owner traffic and sales. I do it differently.",
                      "I build speed and SEO into the site from the start, not as an afterthought. A fast, search friendly site keeps visitors happy, ranks better on Google and turns more of them into customers. This is the difference between a website that just sits there and one that actually brings you business."],
             "visual": site_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My WordPress development", "process"),
                   "body": ["Five clear steps, from the first conversation to a site you can run yourself."],
                   "steps": [
                       {"h3": "Discovery and planning", "short": "Plan", "p": "I learn your business, your goals and what you need from the site, then plan the pages and features.", "points": ["Your business and goals", "Pages planned", "Features agreed"]},
                       {"h3": "Design", "short": "Design", "p": "I design a clean, modern layout that matches your brand and guides visitors towards taking action.", "points": ["Built around your brand", "Clean, modern layout", "Clear path to action"]},
                       {"h3": "Development", "short": "Build", "p": "I build the site to be fast, mobile friendly and easy to manage, with everything working smoothly.", "points": ["Fast loading", "Mobile friendly", "Easy to manage"]},
                       {"h3": "Content and SEO setup", "short": "SEO", "p": "I set up your content, basic SEO and tracking so the site is ready to be found and to grow.", "points": ["Content in place", "Basic SEO set up", "Tracking installed"]},
                       {"h3": "Testing, launch and handover", "short": "Launch", "p": "I test everything, launch your site and show you how to manage it, so you feel confident using it.", "points": ["Everything tested", "Site launched", "Handover and training"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included when", "you work with me"),
                  "body": ["You get a complete, done for you WordPress website that is ready to work for your business. You always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free quote", "h3": "Ready for a website that works as hard as you do?",
                                       "p": "Tell me about your business and your goals, and I will show you how I can build a WordPress site that looks great, loads fast and brings you customers. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for WordPress"),
                  "body": ["A site built for speed and search, by the person you actually talk to, that you can run yourself."],
                  "cards": [
                      {"h3": "You work directly with me", "p": "You deal with the person actually building your site, with clear communication and no middleman."},
                      {"h3": "Built for speed and SEO", "p": "I build sites that load fast and are ready to rank, not just pretty sites that sit idle."},
                      {"h3": "You stay in control", "p": "I hand over a site you can manage yourself and show you how, so you are never stuck depending on anyone."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I build", "websites for"),
                     "body": "I build WordPress websites for service businesses, clinics, consultants, local shops, startups and online stores across many industries. If you need a website that looks professional and performs, I can build it for you.",
                     "chips": [("Service businesses", None), ("Clinics", None), ("Consultants", None),
                               ("Local shops", None), ("Startups", None), ("Online stores", None),
                               ("Education", "/industries/education/"), ("Legal firms", "/industries/legal-firms/"), ("B2B companies", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "your new website"),
                     "body": "A new site does more when it is looked after, focused pages back up your campaigns and the SEO keeps building.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to build your", "new website?"),
               "p": "Let us talk about your business and your goals and build a WordPress site that looks professional, loads fast and brings you customers.",
               "btn": CTA, "note": "No obligation · Free website quote"}),
]
