# Email Marketing Automation Services. Copy: 29_Email_Automation_Services.docx
# No email client is published yet, so there is no client work section.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free email automation consultation"

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


def email(subject, btn, lines=2):
    """An email in the inbox: sender, subject, a few body lines and a button."""
    body = "".join(f'<span class="mt-2 block h-2 rounded-full bg-ink/10" style="width:{w}%"></span>' for w in [100, 85, 60][:lines])
    return (f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><div class="flex items-center gap-2.5">'
            f'<span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange/10 text-orange">{svg("file", "h-4 w-4")}</span>'
            f'<span class="grid"><span class="text-[11px] text-muted">From: Your Business</span><span class="text-sm font-bold text-ink">{E(subject)}</span></span></div>'
            f'<div aria-hidden="true">{body}</div><span class="mt-3 inline-flex rounded-full bg-orange px-3 py-1.5 text-[11px] font-bold text-white">{E(btn)}</span></div>')


def timeline(items):
    """A sequence: [(when, subject, note)] with a line down the left."""
    out = ""
    for i, (when, subj, sub) in enumerate(items):
        out += (f'<li class="relative flex gap-3 pb-4">'
                + ('<span aria-hidden="true" class="absolute top-8 bottom-0 w-0.5 bg-orange/20" style="left:15px"></span>' if i < len(items) - 1 else "")
                + f'<span class="relative grid h-8 w-8 shrink-0 place-items-center rounded-full {"bg-orange text-white" if i == 0 else "bg-orange/10 text-orange"}">{svg("file", "h-4 w-4")}</span>'
                f'<span class="grid min-w-0 flex-1 rounded-2xl border border-[var(--color-line)] bg-white px-3.5 py-2.5">'
                f'<span class="text-[10px] font-bold uppercase tracking-wider text-orange">{E(when)}</span>'
                f'<span class="text-sm font-bold text-ink">{E(subj)}</span><span class="text-xs text-muted">{E(sub)}</span></span></li>')
    return f'<ol class="grid list-none">{out}</ol>'


# --------------------------------------------------- basics: follow up leak check (dark split)

LEAKS = [
    ("I collect emails but rarely send anything", "A list nobody hears from goes cold."),
    ("New leads get no welcome email", "The moment they are most interested passes in silence."),
    ("Abandoned carts get no reminder", "Shoppers who nearly bought are left to forget you."),
    ("Everyone gets the same email at the same time", "A plain newsletter cannot fit what each person has done."),
]
leak_box = L.leak_check(
    "Follow up leak check", "Tick everything that sounds like your business today.", LEAKS,
    ("Nothing ticked. A free consultation still checks the flows that are easy to overlook.",
     "A gap or two. These are usually the first flows I set up, because they pay back fastest.",
     "You are very likely leaving sales on the table. The right flows could recover them from the audience you already have."),
    CTA, "Gaps ticked")

# --------------------------------------------------- section 04: the right message at the right time

MOMENTS = [
    ("signup", "Signs up", "Someone joins your list", [("Straight away", "Welcome, here is what to expect", "Builds trust from the first email"),
                                                     ("A little later", "The most useful thing we offer", "Starts moving them towards a first purchase"),
                                                     ("Next", "A reason to buy now", "One clear offer")]),
    ("cart", "Leaves cart", "Someone leaves items in their cart", [("Soon after", "You left something behind", "A simple reminder with the items"),
                                                                   ("Next day", "Still thinking it over?", "Answers to common doubts"),
                                                                   ("Last", "Your cart is waiting", "A final nudge, then the flow stops")]),
    ("buys", "Buys", "Someone places an order", [("Straight away", "Thank you for your order", "Confirms and sets expectations"),
                                                 ("After delivery", "How are you finding it?", "Helps them get the most from it"),
                                                 ("Later", "Would you leave a review?", "Reviews and repeat orders")]),
    ("quiet", "Goes quiet", "Someone stops opening or buying", [("First", "We have not heard from you", "A friendly check in"),
                                                                ("Then", "Here is what is new", "A reason to come back"),
                                                                ("Last", "Still want to hear from us?", "Keeps your list healthy")]),
]

moments_box = ('<div data-tabs="true">' + figure("What each person receives", ["Example"], (
    label("Pick what the person just did")
    + f'<div class="mt-2.5">{seg([(k, t) for k, t, _, _ in MOMENTS])}</div>'
    + "".join(
        f'<div class="mt-4" data-panel="{k}"{HID if i else ""}>'
        f'<div class="flex items-center gap-3 rounded-2xl bg-orange p-3.5 text-white">{svg("zap", "h-5 w-5 shrink-0")}'
        f'<span><span class="block text-[10px] font-bold uppercase tracking-wider text-white/75">Trigger</span><span class="text-sm font-bold">{E(trig)}</span></span></div>'
        f'<div class="mt-4">{timeline(seq)}</div></div>'
        for i, (k, _, trig, seq) in enumerate(MOMENTS)))) + "</div>")

# --------------------------------------------------- what I set up: one mock per flow

MOCKS = {
    "welcome": figure("Welcome sequence", ["Example"], (
        email("Welcome to Your Business", "Start here")
        + '<div class="mt-4">' + timeline([("Email 1", "Welcome and what to expect", "Sent the moment they sign up"),
                                           ("Email 2", "Our story and why we do this", "Builds trust"),
                                           ("Email 3", "Your first offer", "Moves them towards a first purchase")]) + "</div>")),
    "nurture": figure("Lead nurture sequence", ["Example"], (
        timeline([("Week 1", "The problem, explained simply", "Useful, not salesy"),
                  ("Week 2", "How others solved it", "Shows what is possible"),
                  ("Week 3", "Answers to common questions", "Removes doubts"),
                  ("Week 4", "Ready when you are", "One clear next step")])
        + note("Leads warm up over time, so they are ready to buy when the moment comes.", "repeat"))),
    "cart": figure("Abandoned cart email", ["Example"], (
        email("You left something in your cart", "Return to my cart", 1)
        + '<div class="mt-3 flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3">'
        f'<span class="grid h-12 w-12 shrink-0 place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg("bag", "h-6 w-6")}</span>'
        '<span class="grid"><span class="text-sm font-bold text-ink">Product one</span><span class="text-xs text-muted">Still in your cart</span></span></div>'
        + note("Sent automatically to shoppers who left before paying.", "bag"))),
    "post": figure("Post purchase and onboarding", ["Example"], (
        timeline([("After the order", "Thank you, here is what happens next", "A better customer experience"),
                  ("After delivery", "Getting the most from your order", "Onboarding and tips"),
                  ("Later", "How did we do?", "Review request"),
                  ("When it fits", "Time to stock up?", "Encourages a repeat order")]))),
    "winback": figure("Re engagement and win back", ["Example"], (
        email("We miss you at Your Business", "See what is new")
        + '<div class="mt-4 grid grid-cols-2 gap-2.5">'
        + '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3 text-center"><p class="text-[10px] font-bold uppercase tracking-wide text-muted">Quiet subscribers</p><p class="mt-1 text-xs font-semibold text-ink">Woken up</p></div>'
        + '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3 text-center"><p class="text-[10px] font-bold uppercase tracking-wide text-muted">Lapsed customers</p><p class="mt-1 text-xs font-semibold text-ink">Brought back to buy</p></div>'
        + "</div>")),
    "promo": figure("Sales and promo sequence", ["Example"], (
        timeline([("Before launch", "Something is coming", "Builds anticipation"),
                  ("Launch day", "It is live", "The offer, clearly explained"),
                  ("Mid offer", "Your questions, answered", "Removes doubts"),
                  ("Final day", "Last chance", "Drives the final burst of sales")]))),
    "segments": figure("Segmentation", ["Example"], (
        '<div class="grid place-items-center rounded-2xl bg-orange p-3.5 text-center text-xs font-bold text-white">Your email list</div>'
        + '<span aria-hidden="true" class="mx-auto mt-2 mb-2 block h-5 w-0.5 bg-orange"></span>'
        + '<div class="grid grid-cols-2 gap-2.5">' + "".join(
            f'<div class="flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-white p-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-4 w-4")}</span>'
            f'<span class="text-xs font-bold text-ink">{t}</span></div>'
            for ic, t in [("users", "New leads"), ("bag", "First time buyers"), ("repeat", "Repeat customers"), ("gauge", "Gone quiet")]) + "</div>"
        + note("Each group gets emails that actually fit them.", "sliders"))),
}

WHAT = [
    ("welcome", "Welcome sequences", "users", "The first emails a new lead gets, which build trust and start moving them towards their first purchase."),
    ("nurture", "Lead nurture sequences", "repeat", "A series that educates and warms up leads over time, so they are ready to buy when the moment comes."),
    ("cart", "Abandoned cart recovery", "bag", "Emails that bring back shoppers who left items in their cart, which recovers a large share of lost sales."),
    ("post", "Post purchase and onboarding", "check", "Emails after a purchase that improve the customer experience and encourage repeat orders and reviews."),
    ("winback", "Re engagement and win back", "zap", "Emails that wake up quiet subscribers and bring lapsed customers back to buy again."),
    ("promo", "Sales and promo sequences", "target", "Timed email campaigns for your launches, offers and seasonal promotions that drive a burst of sales."),
    ("segments", "Segmentation", "sliders", "I organize your list into groups so each person gets emails that actually fit them, which greatly lifts your results."),
]

GET = [
    {"icon": "target", "h3": "Email strategy", "p": "The flows that will bring you the most value, mapped to your business and your customer journey."},
    {"icon": "pen", "h3": "Written email flows", "p": "Emails that sound like you and are built to build trust and drive action."},
    {"icon": "zap", "h3": "Full automation setup", "p": "Every flow built in your email tool, with the right triggers so each email sends at the perfect moment."},
    {"icon": "sliders", "h3": "List segmentation", "p": "Your list organized into groups, so the right people get the right emails."},
    {"icon": "layers", "h3": "Store or CRM integration", "p": "Your automation connected to your store or CRM, so it reacts to real customer actions."},
    {"icon": "chart", "h3": "Tracking and ongoing optimization", "p": "Opens, clicks and sales tracked, and your flows improved over time."},
]

FAQ = [
    ("What is email automation?", "Email automation is a set of emails that send themselves based on what a person does, like signing up or leaving a cart. Once built, it runs around the clock without you touching it."),
    ("How is automation different from a newsletter?", "A newsletter is one email sent to everyone at once. Automation sends the right email to each person based on their actions, which feels personal and drives far more sales."),
    ("Do I need email automation?", "If you collect leads or sell online, yes. Automation follows up consistently, which manual effort never does, so it recovers sales you would otherwise lose."),
    ("What are the most important email flows?", "The key ones are a welcome sequence, a lead nurture sequence, abandoned cart recovery, post purchase emails and a win back sequence. I set up the ones that fit your business."),
    ("Can you set up abandoned cart emails?", "Yes. Abandoned cart emails bring back shoppers who left items behind, and they recover a large share of otherwise lost sales for online stores."),
    ("Do you write the emails?", "Yes. I write emails that sound like you and are built to build trust and drive action, not just fill space in an inbox."),
    ("Which email tools do you use?", "I work with popular tools like Mailchimp, Klaviyo and others, as well as email inside GoHighLevel or HubSpot. I will use the one that fits your business best."),
    ("Can you connect it to my store or CRM?", "Yes. I connect your automation to your store or CRM, so it reacts to real customer actions like purchases and sign ups."),
    ("How soon will I see results?", "Some flows, like abandoned cart emails, can start recovering sales within days. Others build value steadily as more people move through them."),
    ("Is email marketing still worth it?", "Yes. Email consistently delivers one of the best returns of any channel, because it sells to people who already know you at almost no cost per email."),
    ("How do you avoid landing in spam?", "I follow good practices for setup, list health and content, and I keep your emails relevant, which all help your emails reach the inbox rather than the spam folder."),
    ("Can you set up segmentation?", "Yes. I organize your list into groups so each person gets emails that fit them, which greatly improves your open rates and sales."),
    ("How do you measure success?", "I track opens, clicks and, most importantly, sales from your emails, so we can see the real value and keep improving your flows."),
    ("What reports will I get?", "You get clear reporting on how your flows are performing, including opens, clicks and revenue, plus updates on the improvements made."),
    ("How do I get started?", "Just book a free email automation consultation using the button on this page. I will look at your business and show you the flows that can grow your sales."),
]

RELATED = [
    ("GoHighLevel", "/services/gohighlevel/"),
    ("Sales funnel setup", "/services/sales-funnel-setup/"),
    ("Zoho CRM", "/services/zoho-crm/"),
    ("HubSpot CRM", "/services/hubspot-crm/"),
    ("WhatsApp automation", None),
    ("Ecommerce SEO", "/services/ecommerce-seo/"),
    ("Google Shopping Ads", "/services/google-shopping-ads/"),
]

PAGE = {
    "path": "/services/email-automation/",
    "slug": "email-automation", "thanks": "crm-automation",
    "form_name": "email_automation",
    "service": "Email Automation",
    "service_name": "Email marketing automation",
    "thanks_what": "email automation consultation",
    "category": "Email marketing automation",
    "service_desc": "Email marketing automation covering welcome, lead nurture, abandoned cart, post purchase, win back and promo sequences, list segmentation, store or CRM integration, tracking and ongoing optimization.",
    "audience": "Businesses that collect leads or sell online",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What email marketing automation includes",
    "offers": [{"h3": n, "p": w} for _, n, _, w in WHAT],
    "title": "Email Marketing Automation Services | Sushant Rana",
    "og_title": "Email Marketing Automation Services",
    "og_alt": "Email marketing automation services by Sushant Rana",
    "desc": "Email marketing automation services: I set up flows that nurture leads and recover lost sales while you sleep, with the right message at the right time.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Email automation", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about email automation"),
            "body": ["Flows, tools, spam, results and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Email marketing automation",
        "h1": ("Email automation that turns leads into sales", "while you sleep"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I set up email automation that follows up with your leads and customers automatically, so you nurture relationships and recover lost sales without lifting a finger. '
            "If you collect leads and email addresses but never quite follow up the way you should, that is money left on the table.",
            "Email is still one of the highest returning channels in marketing, but only when it is automated and timed well. We build the email flows that send the right message at the right moment, so your leads keep moving towards a sale on their own.",
        ],
        "cta2": ("See the flows I build", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free email automation consultation",
        "sub": "Tell me about your leads and customers and I will show you the flows that could grow your sales.",
        "submit": "Request my free consultation",
        "steps": [
            {"label": "Your list", "fields": [
                {"type": "radio", "name": "email_tool", "label": "Which email tool do you use?", "req": True,
                 "options": ["Mailchimp", "Klaviyo", "GoHighLevel", "HubSpot", "Another tool", "None yet"]},
                {"type": "radio", "name": "business_type", "label": "What kind of business are you?", "req": True,
                 "options": ["Online store", "Service business", "Coach or course creator", "SaaS", "Other"]},
                {"type": "radio", "name": "list_size", "label": "How big is your email list?",
                 "options": ["Under 1,000", "1,000 - 10,000", "10,000+", "Not sure"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "problem", "label": "Main problem", "req": True, "placeholder": "Select your main problem",
                 "options": ["Leads are not followed up", "Abandoned carts are not recovered", "Customers do not come back", "We only send newsletters", "Emails land in spam", "Not sure yet"]},
                {"type": "checkbox", "name": "flows", "label": "Flows you are interested in",
                 "options": ["Welcome", "Lead nurture", "Abandoned cart", "Post purchase", "Win back", "Promo", "Segmentation", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, where your leads come from, what you send today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Welcome sequences", "Lead nurture", "Abandoned cart", "Post purchase", "Win back", "Promo sequences", "Segmentation"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What email automation is", "and why it matters"),
             "body": ["Email automation is a set of emails that send themselves based on what a person does, such as signing up, buying, or leaving items in a cart. Once it is built, it runs around the clock without you touching it.",
                      "This matters because manual follow up never happens consistently. Leads go cold and sales are lost. Automation makes sure every lead and customer gets the right emails at the right time, every single time, which brings you more sales from the audience you already have."],
             "bullets": ["Emails that send themselves", "Triggered by what each person does", "Running around the clock"],
             "cta": CTA, "visual": leak_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why email automation is", "so powerful"),
                      "body": ["Email sells to people who already know you. Automation makes sure it happens every time."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "repeat", "h3": "It nurtures leads automatically", "p": "Most leads are not ready to buy right away. Automation keeps warming them up until they are, without you chasing them."},
                          {"icon": "bag", "h3": "It recovers lost sales", "p": "Automated emails bring back people who abandoned a cart or went quiet, recovering sales you would otherwise lose."},
                          {"icon": "users", "h3": "It builds relationships at scale", "p": "You can stay in touch with thousands of people in a personal way, all automatically, which builds trust and repeat business."},
                          {"icon": "wallet", "h3": "It delivers a high return", "p": "Email is known for one of the best returns of any channel, because it sells to people who already know you, at almost no cost per email."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I set up", "h2": ("The email flows", "I build for you"),
                           "body": ["Each flow handles one moment in your customer's journey. I set up the ones that fit your business. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WHAT]})),
    L.split({"id": "value", "pill": "The real value", "h2": ("Why the right message at the right time", "wins"),
             "body": ["Sending everyone the same email at the same time does not work well. What works is sending the right message based on what each person has actually done.",
                      "That is exactly what automation does. Someone who just signed up gets a welcome. Someone who left a cart gets a reminder. Someone who has gone quiet gets a win back. Each person gets the email that fits their moment, which feels personal and drives far more sales than a plain newsletter ever could."],
             "bullets": ["Signs up: a welcome", "Leaves a cart: a reminder", "Buys: a thank you and a review request", "Goes quiet: a win back"],
             "cta": CTA, "visual": moments_box}),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My email automation", "process"),
                   "body": ["Flows that earn start with knowing your customer journey. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Strategy and mapping", "short": "Strategy", "p": "I map out which email flows will bring you the most value, based on your business and your customer journey.", "points": ["Your customer journey", "Highest value flows first", "A clear flow map"]},
                       {"h3": "Write the emails", "short": "Write", "p": "I write emails that sound like you and are built to build trust and drive action, not just fill an inbox.", "points": ["Your voice", "Built to build trust", "Built to drive action"]},
                       {"h3": "Set up flows and triggers", "short": "Build", "p": "I build the automations in your email tool, with the right triggers so each email sends at the perfect moment.", "points": ["Flows built in your tool", "The right triggers", "Perfect timing"]},
                       {"h3": "Integrate and segment", "short": "Integrate", "p": "I connect your store or CRM and organize your list, so the right people get the right emails.", "points": ["Store or CRM connected", "List segmented", "Right email, right person"]},
                       {"h3": "Test and optimize", "short": "Optimize", "p": "I track opens, clicks and sales and keep improving your flows to lift your results over time.", "points": ["Opens and clicks tracked", "Sales tracked", "Flows improved"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my email automation service"),
                  "body": ["You get a complete, done for you email automation setup that keeps working for you every day. You work directly with me throughout."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Are you leaving sales on the table with poor follow up?",
                                       "p": "Let me look at your leads and customers and show you the email flows that could recover lost sales and grow your revenue. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for email automation"),
                  "body": ["Flows written to sell and set up to improve, by the person you talk to."],
                  "cards": [
                      {"h3": "You work directly with me", "p": "You deal with the person building your flows, with clear communication and fast replies."},
                      {"h3": "Written to sell, not just to send", "p": "I focus on emails that build trust and drive sales, based on what each person actually does."},
                      {"h3": "Set up to improve over time", "p": "I track and optimize your flows, so your email automation keeps getting better and earning more."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I set up", "email automation for"),
                     "body": "Online stores, service businesses, coaches and course creators and SaaS companies. If you collect leads or make sales online, email automation can grow your revenue.",
                     "chips": [("Online stores", None), ("Service businesses", None), ("Coaches and course creators", "/industries/education/"),
                               ("SaaS companies", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "email automation"),
                     "body": "Email automation earns more when the leads feeding it and the systems it reacts to are handled alongside it.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to turn your list", "into sales?"),
               "p": "Let us look at your leads and customers and build email automation that nurtures them and recovers lost sales, all on autopilot.",
               "btn": CTA, "note": "No obligation · Free email automation consultation"}),
]
