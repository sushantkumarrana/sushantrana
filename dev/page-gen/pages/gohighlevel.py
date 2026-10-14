# GoHighLevel Setup and Automation Services. Copy: 27_GoHighLevel_Setup_Services.docx
# No GoHighLevel client is published yet, so there is no client work section.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free GoHighLevel consultation"

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


def flow(trigger, steps):
    """Trigger, then the actions it fires, top to bottom."""
    line = '<span aria-hidden="true" class="mx-auto block h-4 w-0.5 bg-ink/15"></span>'
    out = (f'<div class="flex items-center gap-3 rounded-2xl bg-orange p-3.5 text-white">{svg("zap", "h-5 w-5 shrink-0")}'
           f'<span><span class="block text-[10px] font-bold uppercase tracking-wider text-white/75">When</span><span class="text-sm font-bold">{E(trigger)}</span></span></div>')
    for ic, t in steps:
        out += (line + f'<div class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5">'
                f'<span class="grid h-8 w-8 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-4 w-4")}</span>'
                f'<span class="text-sm font-semibold text-ink">{E(t)}</span></div>')
    return out


def bubble(text, mine=True):
    """One text message. mine = sent by your business."""
    look = "bg-orange text-white" if mine else "bg-ink/[0.06] text-ink"
    pos = "max-width:85%;margin-left:auto" if mine else "max-width:85%"
    return f'<p class="rounded-2xl {look} px-3.5 py-2.5 text-xs font-medium" style="{pos}">{E(text)}</p>'


# --------------------------------------------------- interactive: separate tools vs one system (basics)

TOOLS = [("users", "CRM"), ("layers", "Funnel builder"), ("file", "Email tool"), ("phone", "SMS tool"), ("target", "Booking calendar"), ("shield", "Review tool")]


def tool_tile(ic, name, joined):
    look = "border-orange/30 bg-white" if joined else "border-[var(--color-line)] bg-white opacity-70"
    return (f'<div class="flex items-center gap-2 rounded-2xl border {look} p-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-4 w-4")}</span>'
            f'<span class="text-xs font-bold text-ink">{E(name)}</span></div>')


stack_box = ('<div data-tabs="true">' + figure("Your marketing stack", ["Example"], (
    seg([("apart", "Separate tools"), ("one", "GoHighLevel")])
    + '<div class="mt-4" data-panel="apart">'
    + '<div class="grid grid-cols-2 gap-2.5">' + "".join(tool_tile(ic, n, False) for ic, n in TOOLS) + "</div>"
    + note("Six logins and six bills, and none of them talk to each other. A lead in one tool is invisible to the rest.")
    + '</div><div class="mt-4" data-panel="one" hidden="">'
    + '<div class="rounded-3xl border border-orange bg-orange/5 p-3"><p class="pb-2 text-center font-[family-name:var(--font-display)] text-xs font-extrabold uppercase tracking-widest text-orange">GoHighLevel</p>'
    + '<div class="grid grid-cols-2 gap-2.5">' + "".join(tool_tile(ic, n, True) for ic, n in TOOLS) + "</div></div>"
    + note("One login, one connected system. Every lead, message and booking sits on the same contact.")
    + "</div>")) + "</div>")

# --------------------------------------------------- email + SMS: trigger -> action flows

FLOWS = [
    ("new", "New lead", "A new lead fills in your form", [("phone", "Text them back within seconds"), ("file", "Send a welcome email"), ("layers", "Add them to your pipeline"), ("users", "Alert you or your team")]),
    ("missed", "Missed call", "You miss a call", [("phone", "Text the caller back automatically"), ("users", "Create a call back task"), ("layers", "Save the caller as a lead")]),
    ("quiet", "No reply", "A lead has not replied", [("phone", "Send a follow up text"), ("file", "Send a follow up email"), ("repeat", "Keep following up until they reply or book")]),
]
flows_box = ('<div data-tabs="true">' + figure("Email and SMS workflows", ["Example"], (
    label("Pick a trigger")
    + f'<div class="mt-2.5">{seg([(k, t) for k, t, _, _ in FLOWS])}</div>'
    + "".join(f'<div class="mt-4" data-panel="{k}"{HID if i else ""}>{flow(trig, steps)}</div>' for i, (k, _, trig, steps) in enumerate(FLOWS)))) + "</div>")

# --------------------------------------------------- what I do: one mock per tab

MOCKS = {
    "account": figure("Account setup", ["Example"], (
        label("Set up from the ground up")
        + '<div class="mt-3 grid gap-2.5">' + "".join(
            f'<span class="flex items-center gap-2 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2.5 text-xs font-semibold text-ink">{svg("check", "h-3.5 w-3.5 shrink-0 text-orange", 3)}{t}</span>'
            for t in ["Business details and branding", "Phone number and email sending", "Users and permissions", "Custom fields for your leads", "Lead sources connected"]) + "</div>"
        + note("The right structure and settings for your business before anything else is built."))),
    "pipelines": figure("Pipeline", ["Example"], (
        label("Where every lead stands")
        + '<div class="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">' + "".join(
            f'<div class="grid content-start gap-1.5 rounded-xl bg-[#fff7f3] p-2"><p class="truncate text-[10px] font-bold uppercase tracking-wide {"text-orange" if i == 2 else "text-muted"}">{s}</p>'
            + ('<span class="block rounded-lg border border-orange bg-orange/10 p-2 text-[10px] font-bold leading-tight text-ink">Your next customer</span>' if i == 2 else '<span class="block h-8 rounded-lg bg-ink/[0.06]"></span>')
            + '<span class="block h-8 rounded-lg bg-ink/[0.06]"></span></div>'
            for i, s in enumerate(["New lead", "Contacted", "Booked", "Won"])) + "</div>"
        + note("Leads move stage by stage, and automations fire as they do."))),
    "funnels": figure("Funnel", ["Example"], (
        '<ol class="grid list-none gap-2">' + "".join(
            f'<li class="mx-auto flex w-full items-center justify-between gap-3 rounded-2xl {"bg-orange text-white" if i == 2 else "border border-[var(--color-line)] bg-white text-ink"} px-4 py-3" style="max-width:{w}%">'
            f'<span class="text-sm font-bold">{t}</span><span class="text-[10px] font-semibold uppercase tracking-wide {"text-white/75" if i == 2 else "text-muted"}">{s}</span></li>'
            for i, (t, s, w) in enumerate([("Landing page", "Your offer", 100), ("Lead form", "Details captured", 86), ("Booking page", "Call booked", 72), ("Thank you page", "Next steps", 58)])) + "</ol>"
        + note("Built inside GoHighLevel, so every lead lands straight in your CRM and follow up starts on its own."))),
    "automation": flows_box,
    "calendar": figure("Booking calendar", ["Example"], (
        '<div class="flex items-center justify-between"><p class="text-sm font-bold text-ink">Book a call with Your Business</p>'
        f'<span class="grid h-8 w-8 place-items-center rounded-xl bg-orange/10 text-orange">{svg("target", "h-4 w-4")}</span></div>'
        + '<div class="mt-3 grid grid-cols-3 gap-2">' + "".join(
            f'<span class="rounded-xl border {"border-orange bg-orange text-white" if i == 4 else "border-[var(--color-line)] bg-white text-ink"} py-2 text-center text-xs font-bold">{t}</span>'
            for i, t in enumerate(["9:30", "10:00", "11:30", "1:00", "2:30", "4:00"])) + "</div>"
        + '<div class="mt-4">' + rows([("Booking confirmed", "Added to your calendar", "Automatic", True), ("Reminder sent", "So they show up", "Text and email")]) + "</div>")),
    "missed": figure("Missed call text back", ["Example"], (
        rows([("Missed call", "From a new number", "Just now")])
        + '<div class="mt-4 grid gap-2">'
        + bubble("Hi, sorry we missed your call at Your Business. How can we help?")
        + bubble("Hi, I wanted a quote for next week.", False)
        + bubble("Happy to help. Here is a link to book a time that suits you.")
        + "</div>" + note("The caller gets a reply straight away, so a missed call becomes a saved lead.", "phone"))),
    "reviews": figure("Review request", ["Example"], (
        '<div class="grid gap-2">' + bubble("Thanks for choosing Your Business. Would you leave us a quick review? It helps a lot.") + "</div>"
        + '<div class="mt-4 rounded-2xl border border-[var(--color-line)] bg-white p-4 text-center"><p class="text-2xl tracking-widest text-orange" aria-hidden="true">★★★★★</p>'
        '<p class="mt-1 text-xs font-semibold text-ink">Your customer leaves a review</p></div>'
        + note("Requests go out on their own after each job, so you stop chasing customers by hand.", "shield"))),
    "agency": figure("Agency sub accounts", ["Example"], (
        '<div class="grid place-items-center rounded-2xl bg-orange p-3.5 text-center text-xs font-bold text-white">Your snapshot: funnels, workflows, pipelines</div>'
        + '<span aria-hidden="true" class="mx-auto mt-2 mb-2 block h-5 w-0.5 bg-orange"></span>'
        + '<div class="grid grid-cols-3 gap-2.5">' + "".join(
            f'<div class="rounded-2xl border border-[var(--color-line)] bg-white p-3 text-center"><span class="mx-auto grid h-8 w-8 place-items-center rounded-xl bg-orange/10 text-orange">{svg("users", "h-4 w-4")}</span>'
            f'<p class="mt-2 text-[11px] font-bold text-ink">{t}</p></div>'
            for t in ["Client one", "Client two", "Client three"]) + "</div>"
        + note("Roll the same proven system out to each of your clients in a fraction of the time.", "repeat"))),
}

WHAT = [
    ("account", "Full account setup", "layers", "I set up your GoHighLevel account properly from the ground up, with the right structure and settings for your business."),
    ("pipelines", "Pipelines and CRM", "sliders", "I build your pipelines and CRM around how you sell, so you always know where every lead stands."),
    ("funnels", "Funnels and landing pages", "file", "I build funnels and landing pages inside GoHighLevel that capture leads and turn clicks into enquiries and sales."),
    ("automation", "Email and SMS automation", "zap", "I create workflows that follow up with leads by email and text automatically, so no one is forgotten."),
    ("calendar", "Calendars and booking", "target", "I set up booking calendars so leads can schedule calls or appointments with you directly."),
    ("missed", "Missed call text back", "phone", "I set up automatic text replies to missed calls, so a missed call never turns into a lost customer."),
    ("reviews", "Reputation and reviews", "shield", "I set up review requests and reputation tools to help you collect more five star reviews on autopilot."),
    ("agency", "Agency sub accounts", "users", "If you run an agency, I set up sub accounts and snapshots so you can roll out systems to your own clients quickly."),
]

LEAKS = [
    ("New leads wait hours for a reply", "The business that responds first usually wins the customer."),
    ("Missed calls do not get a call back", "Every missed call can be a customer who rings the next business."),
    ("Follow up stops after one try", "Most leads need more than one nudge before they reply or book."),
    ("My follow up is done by hand", "Manual follow up is always too slow and never fully consistent."),
]
leak_box = L.leak_check(
    "Speed to lead check", "Tick everything that sounds like your business today.", LEAKS,
    ("Nothing ticked. A free consultation still checks the hand offs where leads quietly slip away.",
     "A slow spot or two. These are the first things I automate in GoHighLevel.",
     "Leads are very likely going to faster competitors. Instant, automated follow up often turns the same leads into far more customers."),
    CTA, "Slow spots ticked")

GET = [
    {"icon": "layers", "h3": "Full account setup", "p": "Your GoHighLevel account built from the ground up, with the right structure and settings."},
    {"icon": "sliders", "h3": "Pipelines, CRM and funnels", "p": "Pipelines built around how you sell, plus funnels and landing pages that capture leads."},
    {"icon": "zap", "h3": "Email and SMS automation", "p": "Workflows that follow up by email and text automatically, so no one is forgotten."},
    {"icon": "phone", "h3": "Calendars and missed call text back", "p": "Leads book with you directly, and missed calls get an instant text reply."},
    {"icon": "shield", "h3": "Reputation tools", "p": "Review requests that go out on their own, so you collect more five star reviews."},
    {"icon": "users", "h3": "Agency sub accounts", "p": "For agencies, sub accounts and snapshots so you can roll systems out to your own clients."},
]

FAQ = [
    ("What is GoHighLevel?", "GoHighLevel is an all in one platform that combines a CRM, funnels, email and SMS automation, booking calendars and reputation tools in one place, so you can run your marketing and follow up from one system."),
    ("What tools can GoHighLevel replace?", "It can replace your separate CRM, funnel builder, email tool, SMS tool, booking calendar and review tool. This usually saves money and stops your systems being scattered."),
    ("Is GoHighLevel good for agencies?", "Yes. It is built with agencies in mind. I can set up sub accounts and snapshots so you can roll out ready made systems to your own clients quickly."),
    ("Can you set it up for me?", "Yes. I handle the full setup, from your account and funnels to automation and training, so you get a working system without the technical headache."),
    ("Can you build funnels in GoHighLevel?", "Yes. I build funnels and landing pages inside GoHighLevel that capture leads and turn clicks into enquiries and sales."),
    ("Can you set up email and SMS automation?", "Yes. I create workflows that follow up with leads by both email and text automatically, which reaches people far better than email alone."),
    ("What is missed call text back?", "It is an automatic text sent when you miss a call, so the caller instantly gets a reply. This simple feature turns missed calls into saved leads."),
    ("Can you set up booking calendars?", "Yes. I set up calendars so leads can book calls or appointments with you directly, and get automatic reminders so they show up."),
    ("Can you set up my pipelines?", "Yes. I build your pipelines and CRM around how you sell, so you always know exactly where each lead stands."),
    ("Can you set up sub accounts for my agency?", "Yes. I set up sub accounts and reusable snapshots so you can deliver complete systems to your clients in a fraction of the time."),
    ("Can you migrate me from another tool?", "Yes. I can move your contacts and rebuild your key systems inside GoHighLevel, so you switch over without losing your data or your workflows."),
    ("Will you train me or my team?", "Yes. I train you and your team so you can run the system with confidence, and I keep things simple and easy to follow."),
    ("How long does the setup take?", "It depends on how much you need built, but most setups take from a few days to a couple of weeks. I will give you a clear timeline after our first talk."),
    ("Can it handle reviews and reputation?", "Yes. I set up automatic review requests and reputation tools so you collect more five star reviews without chasing customers by hand."),
    ("Do you provide ongoing support?", "Yes. I stay available after setup to help with changes and improvements, so your system keeps running smoothly."),
    ("How do I get started?", "Just book a free GoHighLevel consultation using the button on this page. I will look at how you handle leads and show you how to put it on autopilot."),
]

RELATED = [
    ("Zoho CRM", "/services/zoho-crm/"),
    ("HubSpot CRM", "/services/hubspot-crm/"),
    ("Sales funnel setup", "/services/sales-funnel-setup/"),
    ("Email automation", "/services/email-automation/"),
    ("WhatsApp automation", "/services/whatsapp-automation/"),
    ("Lead generation", "/services/lead-generation/"),
    ("Google Business Profile", "/services/google-business-profile/"),
]

PAGE = {
    "path": "/services/gohighlevel/",
    "slug": "gohighlevel",
    "form_name": "gohighlevel",
    "service": "GoHighLevel",
    "service_name": "GoHighLevel setup and automation",
    "thanks_what": "GoHighLevel consultation",
    "category": "CRM and marketing automation",
    "service_desc": "GoHighLevel setup covering full account setup, pipelines and CRM, funnels and landing pages, email and SMS automation, booking calendars, missed call text back, reputation and review tools, and agency sub accounts and snapshots.",
    "audience": "Local service businesses, coaches, consultants, clinics and marketing agencies",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What GoHighLevel setup includes",
    "offers": [{"h3": n, "p": w} for _, n, _, w in WHAT],
    "title": "GoHighLevel Setup & Automation Services | Sushant Rana",
    "og_title": "GoHighLevel Setup & Automation Services",
    "og_alt": "GoHighLevel setup and automation services by Sushant Rana",
    "desc": "GoHighLevel setup services: I set up your CRM, funnels, and email and SMS follow up on autopilot, so you capture and close more leads.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("GoHighLevel", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about GoHighLevel"),
            "body": ["Tools, automation, agencies and setup time. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "GoHighLevel setup",
        "h1": ("GoHighLevel setup that runs your marketing", "and follow up on autopilot"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I build your GoHighLevel account so your marketing, follow up and bookings run on autopilot. '
            "If you are juggling separate tools for your CRM, funnels, emails and texts and still losing leads, GoHighLevel brings it all into one system, and we set it up for you.",
            "GoHighLevel is a favourite of agencies and service businesses because it replaces a whole stack of tools. But it is powerful, and the setup is where most people get stuck. We handle that for you, so you get all the benefits without the headache.",
        ],
        "cta2": ("See what I set up", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free GoHighLevel consultation",
        "sub": "Tell me how you handle leads today and I will show you how to put it on autopilot.",
        "submit": "Request my free consultation",
        "steps": [
            {"label": "Your setup", "fields": [
                {"type": "radio", "name": "current_crm", "label": "What do you use today?", "req": True,
                 "options": ["Separate tools", "GoHighLevel already", "A CRM only", "Nothing yet"]},
                {"type": "radio", "name": "business_type", "label": "What kind of business are you?", "req": True,
                 "options": ["Local service business", "Coach or consultant", "Clinic", "Marketing agency", "Other"]},
                {"type": "radio", "name": "team_size", "label": "How many people will use it?",
                 "options": ["Just me", "2 - 5", "6 - 15", "16 - 50", "50+"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "problem", "label": "Main problem", "req": True, "placeholder": "Select your main problem",
                 "options": ["Leads are not followed up fast enough", "Missed calls turn into lost customers", "Too many separate tools", "Not enough reviews",
                             "Need sub accounts for my clients", "Moving from another tool", "Not sure yet"]},
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Account setup", "Pipelines", "Funnels", "Email and SMS", "Calendars", "Missed call text back", "Reviews", "Sub accounts"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "Where leads come from, how you follow up today, what is going wrong..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["GoHighLevel setup", "Pipelines", "Funnels", "Email and SMS", "Booking calendars", "Missed call text back", "Reviews", "Agency sub accounts"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What GoHighLevel is", "and why it matters"),
             "body": ["GoHighLevel, often called GHL, is an all in one platform that combines a CRM, funnels and landing pages, email and SMS automation, booking calendars, pipelines and reputation tools in one place.",
                      "This matters because most businesses pay for and juggle many separate tools that do not talk to each other. GoHighLevel replaces that whole stack with one connected system, which saves money and, more importantly, makes sure no lead is missed."],
             "bullets": ["CRM, funnels, email, SMS and calendars in one system", "One connected place for every lead", "Fewer tools to pay for and juggle"],
             "cta": CTA, "visual": stack_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why GoHighLevel", "h2": ("Why GoHighLevel is", "so powerful"),
                      "body": ["GoHighLevel is built for fast, automated follow up. Here is why it works so well."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "layers", "h3": "Everything in one place", "p": "Your CRM, funnels, emails, texts, calendars and pipelines all live in one system, so nothing is scattered and nothing is lost."},
                          {"icon": "phone", "h3": "Powerful email and SMS automation", "p": "GoHighLevel can follow up by both email and text automatically, which reaches leads far more effectively than email alone."},
                          {"icon": "zap", "h3": "Great for instant lead follow up", "p": "It can respond to new leads in seconds, and speed is often what decides whether a lead becomes a customer."},
                          {"icon": "users", "h3": "Built for service businesses and agencies", "p": "With booking, pipelines and reputation tools built in, it fits local businesses, coaches and agencies perfectly."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The GoHighLevel setup work", "I do for you"),
                           "body": ["Everything a working GoHighLevel account needs, from the first setting to agency snapshots. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WHAT]})),
    L.split({"id": "value", "pill": "The real value", "h2": ("Why instant, automated follow up", "wins more leads"),
             "body": ["Most leads are lost simply because no one followed up fast enough. The business that responds first usually wins the customer, and manual follow up is always too slow.",
                      "GoHighLevel solves this. It can text and email a new lead within seconds, reply to missed calls automatically, and keep following up until they respond or book. This instant, automated follow up often turns the same number of leads into far more customers, which is the real power of a good GoHighLevel setup."],
             "visual": leak_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the fake numbers and the people who were only browsing.",
                        "GoHighLevel sees what happens after the form: who replied, who booked and who paid. So when we set it up, the ad click is saved with every lead, your pipeline stages update as leads book and buy, and those qualified leads and sales are sent back to Google Ads as conversions, with their value. From then on your ads go after buyers, not forms."],
                  bullets=["Ad click saved with every lead in GoHighLevel", "Pipeline stages update as leads book and buy", "Bookings and sales sent back to Google Ads", "Reports on cost per booking and cost per sale"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My GoHighLevel", "setup process"),
                   "body": ["A setup that fixes your real gaps starts with how you handle leads today. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Discovery", "short": "Discovery", "p": "I learn how you get and handle leads today and where you are losing them, so the setup fixes your real gaps.", "points": ["Where leads come from", "How you follow up today", "Where leads are lost"]},
                       {"h3": "Design", "short": "Design", "p": "I plan your pipelines, funnels and automation so GoHighLevel matches how your business runs.", "points": ["Pipelines planned", "Funnels mapped", "Automation designed"]},
                       {"h3": "Build and automate", "short": "Build", "p": "I build your account, funnels and workflows and set up your email, SMS and missed call text back.", "points": ["Account and funnels", "Email and SMS workflows", "Missed call text back"]},
                       {"h3": "Integrate", "short": "Integrate", "p": "I connect your lead sources, calendars and other tools so everything flows into one system.", "points": ["Lead sources connected", "Calendars connected", "One system for everything"]},
                       {"h3": "Train and support", "short": "Train", "p": "I train you and your team and stay available afterwards, so the system keeps working for you.", "points": ["Training for you and your team", "Help after setup", "Changes as you grow"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my GoHighLevel service"),
                  "body": ["You get a complete, done for you GoHighLevel setup that runs your marketing and follow up automatically. I explain everything simply, and you work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Want your lead follow up running on autopilot?",
                                       "p": "Let me look at how you handle leads today and show you how GoHighLevel can capture and follow up with every one automatically. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for GoHighLevel"),
                  "body": ["A GoHighLevel setup built for speed to lead, by the person you talk to."],
                  "cards": [
                      {"h3": "I handle the hard part", "p": "GoHighLevel is powerful but complex to set up. I do the heavy lifting so you get the benefits without the frustration."},
                      {"h3": "Built around fast follow up", "p": "I focus your setup on speed to lead and automated follow up, which is what actually turns leads into customers."},
                      {"h3": "Explained simply, with support", "p": "I keep things beginner friendly and stay available afterwards, so you are never left confused or stuck."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I set up", "GoHighLevel for"),
                     "body": "Local service businesses, coaches and consultants, clinics and, importantly, marketing agencies that want to deliver systems to their own clients. If you want your lead handling on autopilot, GoHighLevel is a strong fit.",
                     "chips": [("Local service businesses", "/industries/local-businesses/"), ("Coaches and consultants", None), ("Clinics", "/industries/healthcare/"),
                               ("Dental clinics", "/industries/dental/"), ("Auto repair shops", "/industries/auto-repair/"), ("Marketing agencies", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "GoHighLevel"),
                     "body": "GoHighLevel earns more when the leads feeding it and the pages they land on are handled alongside it.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to put your", "follow up on autopilot?"),
               "p": "Let us look at how you handle leads today and build a GoHighLevel setup that captures and follows up with every lead automatically.",
               "btn": CTA, "note": "No obligation · Free GoHighLevel consultation"}),
]
