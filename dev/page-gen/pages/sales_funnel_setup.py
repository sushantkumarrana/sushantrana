# Sales Funnel Setup Services. Copy: 28_Sales_Funnel_Setup_Services.docx
# No funnel client is published yet, so there is no client work section.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free sales funnel consultation"

# --------------------------------------------------- small mock helpers


def seg(items, on=0):
    """Segmented toggle; items = [(key, label)]. Lives inside a data-tabs box."""
    btns = "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-2 py-2 text-[11px] font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(label)}</button>'
        for i, (k, label) in enumerate(items))
    return f'<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">{btns}</div>'


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def label(text):
    return f'<p class="text-[10px] font-bold uppercase tracking-wider text-muted">{E(text)}</p>'


def row(title, sub="", tag="", hot=False):
    t = (f'<span class="rounded-full {"bg-orange/10 text-orange" if hot else "bg-ink/[0.06] text-muted"} px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide">{E(tag)}</span>' if tag else "")
    s = f'<span class="text-xs text-muted">{E(sub)}</span>' if sub else ""
    return (f'<li class="flex items-center justify-between gap-3 rounded-2xl border {"border-orange/30" if hot else "border-[var(--color-line)]"} bg-white px-4 py-3">'
            f'<span class="grid min-w-0"><span class="text-sm font-bold text-ink">{E(title)}</span>{s}</span>{t}</li>')


def rows(items):
    return '<ul class="grid list-none gap-2.5">' + "".join(row(*it) for it in items) + "</ul>"


ARROW = '<span aria-hidden="true" class="mx-auto mt-2 mb-2 block h-5 w-0.5 bg-orange"></span>'


def page_card(title, lines, btn):
    """A small landing page sketch: headline, a few fields or lines, one button."""
    fields = "".join(f'<span class="flex items-center rounded-xl border border-[var(--color-line)] px-3 py-2 text-[11px] text-muted">{E(f)}</span>' for f in lines)
    return (f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><p class="text-sm font-bold text-ink">{E(title)}</p>'
            f'<div class="mt-3 grid gap-2" aria-hidden="true">{fields}<span class="mt-1 block rounded-full bg-orange py-2 text-center text-[11px] font-bold text-white">{E(btn)}</span></div></div>')


# --------------------------------------------------- basics: website leak check (dark split)

LEAKS = [
    ("Visitors land on my home page and wander", "A normal website lets people browse, get distracted and leave."),
    ("I do not capture details from people who are not ready", "Anyone who leaves without buying is gone for good."),
    ("Nobody follows up after someone shows interest", "Without follow up, warm visitors go cold."),
    ("I do not know how many visitors become customers", "Without that number, adding traffic is a guess, not a plan."),
]
leak_box = L.leak_check(
    "Is your website leaking buyers?", "Tick everything that sounds like your site today.", LEAKS,
    ("Nothing ticked. A free consultation still checks your offer and the path a visitor takes to buy.",
     "A leak or two. A funnel with lead capture and follow up is built to close exactly these.",
     "Your traffic is very likely leaking. A proper funnel could turn far more of the same visitors into customers."),
    CTA)

# --------------------------------------------------- stages: interactive funnel (section 04)

STAGES = [  # key, name, job, page, message, follow up
    ("aware", "Awareness", "Grab attention", "An ad, post or video that stops the scroll", "A clear problem your buyer recognises", "Visitors who show interest are tracked"),
    ("interest", "Interest", "Build interest", "An opt in page with a helpful offer", "Something useful, given in exchange for their details", "Welcome emails start straight away"),
    ("decision", "Decision", "Remove doubts", "A sales page that shows the value", "Answers to objections, proof and a clear offer", "Reminders for people still deciding"),
    ("action", "Action", "Make it simple", "A short checkout or booking page", "One step, one button, nothing in the way", "Confirmation and next steps sent"),
]
WIDTHS = [100, 82, 64, 46]


def stage_panel(i):
    _, name, job, page, msg, fu = STAGES[i]
    shape = "".join(
        f'<span class="mx-auto block rounded-xl py-2.5 text-center text-[11px] font-bold uppercase tracking-wide {"bg-orange text-white" if j == i else "bg-orange/10 text-muted"}" style="width:{w}%">{E(STAGES[j][1])}</span>'
        for j, w in enumerate(WIDTHS))
    return (f'<div data-panel="{STAGES[i][0]}"{HID if i else ""}><div class="grid gap-1.5" aria-hidden="true">{shape}</div>'
            f'<p class="mt-4 font-[family-name:var(--font-display)] text-sm font-extrabold text-ink">{E(name)}: {E(job.lower())}</p>'
            '<div class="mt-2.5">' + rows([("Page", page), ("Message", msg), ("Follow up", fu, "Automatic", True)]) + "</div></div>")


stages_box = ('<div data-tabs="true">' + figure("How each stage is built", ["Example"], (
    label("Pick a stage of the funnel")
    + f'<div class="mt-2.5">{seg([(k, n) for k, n, *_ in STAGES])}</div>'
    + '<div class="mt-4">' + "".join(stage_panel(i) for i in range(len(STAGES))) + "</div>")) + "</div>")

# --------------------------------------------------- what I build: one mock per funnel type

MOCKS = {
    "lead": figure("Lead generation funnel", ["Example"], (
        page_card("Free guide for your buyers", ["Your name", "Your email"], "Send me the guide")
        + ARROW + rows([("Guide delivered", "Straight to their inbox", "Automatic", True), ("Nurture emails", "Warming them up towards an enquiry", "Scheduled")]))),
    "webinar": figure("Webinar funnel", ["Example"], (
        page_card("Free live training", ["Your name", "Your email"], "Save my seat")
        + ARROW + rows([("Reminder emails", "So registrants turn up", "Automatic", True), ("Replay and offer", "Follow up after the event", "Scheduled")]))),
    "sales": figure("Sales and VSL funnel", ["Example"], (
        '<div class="relative grid aspect-video place-items-center overflow-hidden rounded-2xl bg-[#0a0a0a]">'
        f'<span class="grid h-12 w-12 place-items-center rounded-full bg-orange text-white">{svg("play", "h-6 w-6")}</span>'
        '<span class="absolute bottom-3 left-3 rounded bg-white/90 px-2 py-0.5 text-[10px] font-bold text-ink">Your sales video</span></div>'
        '<div class="mt-3 grid gap-2" aria-hidden="true"><span class="block h-2 w-full rounded-full bg-ink/10"></span><span class="block h-2 w-5/6 rounded-full bg-ink/10"></span></div>'
        '<span class="mt-4 block rounded-full bg-orange py-2.5 text-center text-xs font-bold text-white">Yes, I want this</span>'
        + note("One page, one message, one button that leads straight to the purchase."))),
    "booking": figure("Application and booking funnel", ["Example"], (
        page_card("Apply to work with us", ["What is your goal?", "What is your budget?", "When do you want to start?"], "Submit application")
        + ARROW + rows([("Good fit", "Sent to your booking calendar", "Qualified", True), ("Not a fit yet", "Sent helpful emails instead", "Nurture")]))),
    "ecom": figure("Ecommerce funnel", ["Example"], (
        rows([("Product one", "Added to cart", "Cart"), ("Add a matching item", "Offered at checkout", "Order bump", True),
              ("One more offer", "Shown after they pay", "Upsell", True), ("Left without paying?", "Cart recovery email sent", "Recovery", True)])
        + note("Strong offers and upsells lift each order, and cart recovery brings back the ones who left.", "bag"))),
    "tripwire": figure("Tripwire funnel", ["Example"], (
        label("Each step grows the customer's value")
        + '<div class="mt-3 flex h-24 items-end gap-3" aria-hidden="true">' + "".join(
            f'<span class="block flex-1 rounded-t-lg {"bg-orange" if i == 2 else "bg-orange/20"}" style="height:{h}%"></span>'
            for i, h in enumerate([30, 60, 90])) + "</div>"
        + '<div class="mt-2 grid grid-cols-3 gap-3">' + "".join(
            f'<span class="text-center text-[10px] font-bold uppercase tracking-wide text-muted">{t}</span>'
            for t in ["Low cost first offer", "Main offer", "Repeat buyer"]) + "</div>"
        + note("A small first yes turns a stranger into a buyer. The bigger offers come after."))),
}

WHAT = [
    ("lead", "Lead generation funnels", "target", "Funnels that capture leads with a strong offer, then nurture them into enquiries and sales."),
    ("webinar", "Webinar and event funnels", "users", "Funnels that fill your webinars and events and follow up to turn attendees into buyers."),
    ("sales", "Sales and VSL funnels", "play", "Funnels built around a sales page or video that lead the visitor straight to a purchase."),
    ("booking", "Application and booking funnels", "phone", "Funnels that qualify leads and get them to book a call, perfect for high value services."),
    ("ecom", "Ecommerce funnels", "bag", "Funnels that boost your store's sales with strong offers, upsells and cart recovery."),
    ("tripwire", "Tripwire funnels", "wallet", "Funnels that turn strangers into buyers with a low cost first offer, then grow their value from there."),
]

GET = [
    {"icon": "target", "h3": "Funnel strategy", "p": "Clarity on your offer and your goal, and the right type of funnel mapped to reach it."},
    {"icon": "pen", "h3": "Conversion focused copy", "p": "The message and the offer written to drive action, because they are what really drive results."},
    {"icon": "layers", "h3": "Funnel pages", "p": "Clean pages that focus each visitor on the next step, built on the tool that suits you best."},
    {"icon": "repeat", "h3": "Automated email follow up", "p": "Email and message follow up that keeps working on leads who did not buy right away."},
    {"icon": "chart", "h3": "Tracking setup", "p": "Tracking that shows where people drop off and where the funnel is winning."},
    {"icon": "sliders", "h3": "A plan to test and improve", "p": "Offers, headlines and pages tested over time, so your conversion rate keeps lifting."},
]

FAQ = [
    ("What is a sales funnel?", "A sales funnel is a guided journey that turns a stranger into a customer, one step at a time. Each step is designed to move the visitor closer to buying."),
    ("How is a funnel different from a website?", "A website lets people wander and often leave. A funnel focuses them on one path and one action, which is why it converts far more of your traffic into sales."),
    ("Do I really need a funnel?", "If you want to sell something specific and get more from your traffic, yes. A funnel captures leads and follows up, so you stop losing people who were not ready to buy today."),
    ("What types of funnels are there?", "Common types include lead generation, webinar, sales, application, ecommerce and tripwire funnels. I choose the right type for your offer and your goal."),
    ("How long does it take to build?", "Most funnels take from one to a few weeks depending on the number of pages and the automation. I will give you a clear timeline once I know your offer."),
    ("Do you write the copy?", "Yes. I write conversion focused copy for your funnel, because the message and the offer are what really drive the results."),
    ("Do you set up the automation and email follow up?", "Yes. Follow up is where a lot of sales happen. I set up the email and message sequences that keep working on leads who did not buy right away."),
    ("Which tools do you build funnels on?", "I can build on GoHighLevel, WordPress or a dedicated funnel tool, depending on what suits your business and budget best."),
    ("Can you connect it to my CRM?", "Yes. I connect your funnel to your CRM or system, so leads flow in automatically and your follow up stays organized."),
    ("How soon will I see results?", "A funnel can start converting as soon as traffic hits it. From there, testing and follow up help lift your results over the following weeks."),
    ("Can you A/B test the funnel?", "Yes. I set your funnel up so we can test different offers, headlines and pages, and keep improving your conversion rate over time."),
    ("Do you set up tracking?", "Yes. I set up tracking so we can see exactly where people drop off and where the funnel is winning, then improve from there."),
    ("Can a funnel work for my business?", "Most businesses with a clear offer can benefit from a funnel. On our call I will tell you honestly whether a funnel is right for you and which type fits best."),
    ("What reports will I get?", "You get clear reporting on visitors, conversions and where people drop off, so you can see exactly how your funnel is performing."),
    ("How do I get started?", "Just book a free sales funnel consultation using the button on this page. Tell me about your offer and I will show you how a funnel can grow your sales."),
]

RELATED = [
    ("Landing pages", "/services/landing-pages/"),
    ("GoHighLevel", "/services/gohighlevel/"),
    ("Email automation", "/services/email-automation/"),
    ("Zoho CRM", "/services/zoho-crm/"),
    ("HubSpot CRM", "/services/hubspot-crm/"),
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
]

PAGE = {
    "path": "/services/sales-funnel-setup/",
    "slug": "sales-funnel-setup",
    "form_name": "sales_funnel_setup",
    "service": "Sales Funnel Setup",
    "service_name": "Sales funnel setup",
    "thanks_what": "sales funnel consultation",
    "category": "Conversion funnel design",
    "service_desc": "Sales funnel setup covering lead generation, webinar, sales and VSL, application and booking, ecommerce and tripwire funnels, with funnel strategy, conversion focused copy, funnel pages, automated email follow up, tracking and testing.",
    "audience": "Businesses selling a clear offer that want more sales from their traffic",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What sales funnel setup includes",
    "offers": GET,
    "title": "Sales Funnel Setup Services That Convert | Sushant Rana",
    "og_title": "Sales Funnel Setup Services That Convert",
    "og_alt": "Sales funnel setup services by Sushant Rana",
    "desc": "Sales funnel setup services: I design and build funnels that turn strangers into paying customers, with pages, copy, automation and tracking.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Sales funnel setup", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about sales funnels"),
            "body": ["Funnel types, copy, tools, timelines and tracking. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Sales funnel setup",
        "h1": ("Sales funnel setup that turns strangers", "into paying customers"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I design and build sales funnels that guide people step by step, from first click to paying customer, so more of your traffic turns into sales. '
            "If you are sending traffic to your website and hoping people buy, remember that hope is not a strategy, and a normal website is not built to sell.",
            "A sales funnel is a path you design on purpose. Every step is built to move the visitor closer to buying, with the right message and the right follow up. We build the whole thing for you, pages, copy and automation included.",
        ],
        "cta2": ("See funnel types", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free sales funnel consultation",
        "sub": "Tell me about your offer and I will show you how a funnel can grow your sales.",
        "submit": "Request my free consultation",
        "steps": [
            {"label": "Your offer", "fields": [
                {"type": "radio", "name": "offer_type", "label": "What do you sell?", "req": True,
                 "options": ["A service", "Coaching or consulting", "A course or digital product", "Physical products", "Other"]},
                {"type": "radio", "name": "current_funnel", "label": "Do you have a funnel today?", "req": True,
                 "options": ["Yes, but it is not converting", "Just a website", "Nothing yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "problem", "label": "Main problem", "req": True, "placeholder": "Select your main problem",
                 "options": ["Traffic but few sales", "Leads are not followed up", "My offer is not clear", "Not sure which funnel I need", "Not sure yet"]},
                {"type": "checkbox", "name": "funnel_types", "label": "Funnels you are interested in",
                 "options": ["Lead generation", "Webinar", "Sales or VSL", "Application or booking", "Ecommerce", "Tripwire", "Not sure"]},
                {"type": "select", "name": "tool", "label": "Preferred tool", "placeholder": "Select a tool",
                 "options": ["GoHighLevel", "WordPress", "A dedicated funnel tool", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Your offer, where your traffic comes from, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Lead funnels", "Webinar funnels", "VSL funnels", "Booking funnels", "Ecommerce funnels", "Tripwire funnels", "Email follow up", "Tracking"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What a sales funnel is", "and why it matters"),
             "body": ["A sales funnel is a guided journey that takes a stranger and turns them into a customer, one step at a time. Instead of dropping people on a busy website, it leads them through a clear path towards one action.",
                      "This matters because a normal website lets people wander and leave. A funnel focuses them. Each step warms them up, builds trust and removes doubts, so far more of your visitors end up buying instead of bouncing away."],
             "bullets": ["One clear path towards one action", "Details captured before people leave", "Follow up that warms visitors into buyers"],
             "cta": CTA, "visual": leak_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why you need one", "h2": ("Why a sales funnel beats", "a normal website"),
                      "body": ["A website shows people around. A funnel walks them to the sale. Here is the difference."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "shield", "h3": "It stops leaking leads", "p": "A funnel captures contact details early and follows up, so the people who are not ready to buy today are not lost forever."},
                          {"icon": "click", "h3": "It guides buyers step by step", "p": "Instead of leaving people to figure it out, a funnel leads them through a clear path that makes buying easy."},
                          {"icon": "zap", "h3": "It automates the selling", "p": "With follow up built in, a funnel keeps selling for you around the clock, even while you sleep."},
                          {"icon": "chart", "h3": "It makes revenue predictable", "p": "When you know how many visitors turn into customers, you can scale your traffic with confidence and grow on purpose."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I build", "h2": ("The sales funnels", "I build for you"),
                           "body": ["Each funnel type does a different job. I choose the right one for your offer and your goal. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WHAT]})),
    L.split({"id": "stages", "pill": "The stages", "h2": ("How each stage of your funnel", "is built to convert"),
             "body": ["A good funnel guides people through clear stages. First it grabs attention and creates awareness. Then it builds interest with a helpful offer. Next it drives the decision by removing doubts and showing value. Finally it makes taking action simple and easy.",
                      "I design each stage on purpose, with the right page, message and follow up at every step. Nothing is left to chance. This is why a proper funnel converts so much better than just sending traffic to a page and hoping."],
             "bullets": ["Awareness: grab attention", "Interest: a helpful offer", "Decision: remove doubts, show value", "Action: simple and easy"],
             "cta": CTA, "visual": stages_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My sales funnel", "process"),
                   "body": ["A funnel that sells starts with a clear offer. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Strategy and offer", "short": "Strategy", "p": "I get clear on your offer and your goal, then map the right type of funnel to reach it.", "points": ["Your offer, sharpened", "Your goal, defined", "The right funnel type"]},
                       {"h3": "Map the funnel", "short": "Map", "p": "I plan every step and page, so the whole journey is designed to guide the visitor towards buying.", "points": ["Every step planned", "Every page planned", "One clear path"]},
                       {"h3": "Build the pages", "short": "Build", "p": "I build your funnel pages with strong copy and clean design that focus each visitor on the next step.", "points": ["Conversion focused copy", "Clean design", "One next step per page"]},
                       {"h3": "Automation and follow up", "short": "Follow up", "p": "I set up the email and message follow up that keeps working on leads who did not buy right away.", "points": ["Email follow up", "Message follow up", "Leads kept warm"]},
                       {"h3": "Test and optimize", "short": "Optimize", "p": "I set up tracking and test the funnel so we can keep lifting your conversion rate over time.", "points": ["Tracking set up", "Offers and pages tested", "Conversion rate lifted"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included when", "you work with me"),
                  "body": ["You get a complete, done for you sales funnel that is ready to turn traffic into customers. I build on the tool that suits you best. You work directly with me throughout."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Ready to turn more of your traffic into sales?",
                                       "p": "Let me look at your offer and your goals and show you how a proper sales funnel can turn more visitors into customers. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for funnels"),
                  "body": ["Funnels built to convert and to keep improving, by the person you talk to."],
                  "cards": [
                      {"h3": "You work directly with me", "p": "You deal with the person building your funnel, with clear communication and fast replies."},
                      {"h3": "Conversion first", "p": "I focus on the offer, copy and follow up that actually convert, not just pretty pages."},
                      {"h3": "Built to test and grow", "p": "I set your funnel up so we can keep testing and improving, rather than building it once and forgetting it."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Who needs", "a sales funnel"),
                     "body": "Coaches and consultants, service businesses, course creators, online stores and anyone selling a clear offer. If you want more sales from your traffic, a funnel can help you get there.",
                     "chips": [("Coaches and consultants", None), ("Service businesses", "/industries/local-businesses/"), ("Course creators", "/industries/education/"),
                               ("Online stores", "/industries/ecommerce/"), ("Anyone selling a clear offer", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "your funnel"),
                     "body": "A funnel earns more when the traffic feeding it and the CRM catching its leads are handled alongside it.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to build a funnel", "that sells?"),
               "p": "Let us look at your offer and your goals and build a sales funnel that turns more of your visitors into paying customers.",
               "btn": CTA, "note": "No obligation · Free sales funnel consultation"}),
]
