# HubSpot CRM Implementation and Setup Services. Copy: 26_HubSpot_CRM_Setup_Services.docx
# No CRM client is published yet, so there is no client work section.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free HubSpot consultation"

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


def bars(n=5):
    hs = [40, 65, 50, 85, 70, 55][:n]
    return ('<div class="flex h-24 items-end gap-2" aria-hidden="true">'
            + "".join(f'<span class="block flex-1 rounded-t-lg {"bg-orange" if i == 3 else "bg-orange/20"}" style="height:{h}%"></span>' for i, h in enumerate(hs))
            + "</div>")


# --------------------------------------------------- interactive: one lead, first click to closed deal
# The contact record fills up as the lead moves from marketing to sales.

JOURNEY = [  # (tab label, team, event, detail, icon)
    ("Click", "Marketing", "Clicked your ad", "Source saved on the contact", "click"),
    ("Form", "Marketing", "Filled in your website form", "New contact created in HubSpot", "file"),
    ("Email", "Marketing", "Opened your follow up email", "Sent by a workflow, not by hand", "repeat"),
    ("Call", "Sales", "Booked a call with sales", "Deal created, owner assigned", "phone"),
    ("Won", "Sales", "Deal closed", "Full history from the first click", "check"),
]
JOURNEY_NOTES = [
    "The very first click is tracked, so you know which ad or page brought this lead in.",
    "The form fill lands in HubSpot on its own. Nobody types it in, nothing gets lost.",
    "Marketing keeps the lead warm automatically until they are ready to talk.",
    "Sales picks up the lead with everything marketing knows already attached.",
    "Marketing and sales worked from the same record the whole way. That is the alignment.",
]


def journey_panel(i):
    items = ""
    for j, (_, team, ev, det, ic) in enumerate(JOURNEY[: i + 1]):
        cur = j == i
        items += (f'<li class="flex items-center gap-3 rounded-2xl border {"border-orange bg-orange/5" if cur else "border-[var(--color-line)] bg-white"} p-3">'
                  f'<span class="grid h-8 w-8 shrink-0 place-items-center rounded-xl {"bg-orange text-white" if cur else "bg-orange/10 text-orange"}">{svg(ic, "h-4 w-4")}</span>'
                  f'<span class="grid min-w-0 flex-1"><span class="text-sm font-bold text-ink">{E(ev)}</span><span class="text-xs text-muted">{E(det)}</span></span>'
                  f'<span class="rounded-full {"bg-orange/10 text-orange" if team == "Sales" else "bg-ink/[0.06] text-muted"} px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide">{team}</span></li>')
    return (f'<div data-panel="j{i}"{HID if i else ""}><ol class="grid list-none gap-2">{items}</ol>{note(E(JOURNEY_NOTES[i]))}</div>')


journey_box = ('<div data-tabs="true">' + figure("One contact record in HubSpot", ["Example"], (
    '<div class="flex items-center gap-3 border-b border-[var(--color-line)] pb-3"><span class="grid h-10 w-10 place-items-center rounded-full bg-orange/10 text-orange">'
    f'{svg("users", "h-5 w-5")}</span><span><span class="block text-sm font-bold text-ink">Your next customer</span><span class="text-xs text-muted">customer@theirbusiness.com</span></span></div>'
    + '<div class="mt-4">' + label("Follow one lead from first click to closed deal") + "</div>"
    + f'<div class="mt-2.5">{seg([("j" + str(i), j[0]) for i, j in enumerate(JOURNEY)])}</div>'
    + '<div class="mt-4">' + "".join(journey_panel(i) for i in range(len(JOURNEY))) + "</div>")) + "</div>")

# --------------------------------------------------- what I do: one mock per tab

DEAL_STAGES = ["Appointment", "Proposal", "Negotiation", "Closed won"]

MOCKS = {
    "setup": figure("Contact properties", ["Example"], (
        label("Properties set up for your business")
        + '<div class="mt-2.5 grid gap-2">' + "".join(
            f'<div class="flex items-center justify-between gap-3 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2.5"><span class="text-xs font-semibold text-ink">{f}</span>'
            f'<span class="rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold text-orange">{v}</span></div>'
            for f, v in [("Lifecycle stage", "Lead"), ("Lead source", "Website form"), ("Contact owner", "Assigned"), ("Service interested in", "Your service")]) + "</div>"
        + note("The right settings, properties and structure from day one, so the data stays clean."))),
    "pipeline": figure("Deal pipeline", ["Example"], (
        label("Deal stages, in the order you sell")
        + '<div class="mt-3 grid grid-cols-2 gap-2 sm:grid-cols-4">' + "".join(
            f'<div class="grid content-start gap-1.5 rounded-xl bg-[#fff7f3] p-2"><p class="truncate text-[10px] font-bold uppercase tracking-wide {"text-orange" if i == 1 else "text-muted"}">{s}</p>'
            + ('<span class="block rounded-lg border border-orange bg-orange/10 p-2 text-[10px] font-bold leading-tight text-ink">Your deal</span>' if i == 1 else '<span class="block h-8 rounded-lg bg-ink/[0.06]"></span>')
            + '<span class="block h-8 rounded-lg bg-ink/[0.06]"></span></div>'
            for i, s in enumerate(DEAL_STAGES)) + "</div>"
        + note("Every rep can see what stage a deal is in and exactly what has to happen next."))),
    "forms": figure("Website form", ["Example"], (
        '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><p class="text-sm font-bold text-ink">Get in touch</p><div class="mt-3 grid gap-2" aria-hidden="true">'
        + "".join(f'<span class="flex items-center rounded-xl border border-[var(--color-line)] px-3 py-2 text-[11px] text-muted">{f}</span>' for f in ["Name", "Email", "Phone"])
        + '<span class="mt-1 block rounded-full bg-orange py-2 text-center text-[11px] font-bold text-white">Send</span></div></div>'
        + '<span aria-hidden="true" class="mx-auto mt-2 mb-2 block h-5 w-0.5 bg-orange"></span>'
        + rows([("New contact in HubSpot", "Form, page and source saved", "Automatic", True)]))),
    "workflows": figure("Workflow", ["Example"], flow("A contact fills in your form", [
        ("users", "Assign the contact to the right rep"), ("file", "Send the thank you email"),
        ("phone", "Create a call task for the owner"), ("repeat", "Remind the owner if there is no reply")])),
    "sequences": figure("Sales sequence", ["Example"], (
        label("Follow up that sends itself")
        + '<ol class="mt-3 grid list-none gap-2">' + "".join(
            f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3">'
            f'<span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-[10px] font-extrabold text-white">{n}</span>'
            f'<span class="grid"><span class="text-sm font-bold text-ink">{t}</span><span class="text-xs text-muted">{s}</span></span></li>'
            for n, t, s in [("1", "Intro email", "Right after they enquire"), ("2", "Call task", "A reminder for the rep"),
                            ("3", "Follow up email", "If there is still no reply"), ("4", "Last check in", "Then the sequence stops")]) + "</ol>"
        + note("If the prospect replies or books a meeting, the sequence stops on its own.", "zap"))),
    "reports": figure("Sales dashboard", ["Example"], (
        '<div class="grid grid-cols-3 gap-2.5">' + "".join(
            f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3"><p class="text-[10px] font-semibold uppercase tracking-wide text-muted">{t}</p>'
            '<span class="mt-2 block h-3 w-3/4 rounded-full bg-orange/20" aria-hidden="true"></span></div>'
            for t in ["New contacts", "Open deals", "Deals won"]) + "</div>"
        + '<div class="mt-4 rounded-2xl border border-[var(--color-line)] p-4">' + label("Deals by stage") + f'<div class="mt-3">{bars(4)}</div></div>'
        + note("Your pipeline, deals and team performance on one screen."))),
    "migration": figure("Data and integrations", ["Example"], (
        '<div class="grid grid-cols-2 gap-2.5">' + "".join(
            f'<div class="flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-white p-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-4 w-4")}</span>'
            f'<span class="text-xs font-bold text-ink">{t}</span></div>'
            for ic, t in [("file", "Old spreadsheets"), ("layers", "Your website"), ("users", "Your calendar"), ("target", "Ad accounts")]) + "</div>"
        + '<span aria-hidden="true" class="mx-auto mt-2 mb-2 block h-5 w-0.5 bg-orange"></span>'
        + '<div class="grid place-items-center rounded-2xl bg-orange p-3.5 text-center text-xs font-bold text-white">Everything in HubSpot, working together</div>')),
    "training": figure("Team training", ["Example"], (
        label("What your team can do after training")
        + '<div class="mt-3 grid gap-2.5">' + "".join(
            f'<label class="svc-check"><input type="checkbox" class="sr-only"/><span class="svc-box">{svg("check", "h-3.5 w-3.5", 3)}</span>'
            f'<span class="text-sm font-bold text-ink">{t}</span></label>'
            for t in ["Find a contact and see their full history", "Move a deal to the next stage", "Enrol a prospect in a sequence", "Read the sales dashboard"]) + "</div>"
        + note("Tick them off. A CRM only works when people use it.", "users"))),
}

WHAT = [
    ("setup", "Setup and onboarding", "layers", "I set up your HubSpot account properly from the start, with the right settings, properties and structure for your business."),
    ("pipeline", "Pipeline and deal stage design", "sliders", "I build your sales pipeline and deal stages around how you actually sell, so your process is clear and easy to follow."),
    ("forms", "Forms and lead capture", "target", "I connect your website forms and lead sources so new contacts flow straight into HubSpot automatically."),
    ("workflows", "Workflows and automation", "zap", "I build workflows that automate follow ups, tasks and reminders, so leads are always handled on time."),
    ("sequences", "Email and sequences", "file", "I set up your email and sales sequences, so prospects get timely, consistent follow up without manual effort."),
    ("reports", "Reports and dashboards", "chart", "I build clear dashboards so you can see your pipeline, deals and team performance at a glance."),
    ("migration", "Data migration and integrations", "repeat", "I move your existing data into HubSpot cleanly and connect the other tools you use, so everything works together."),
    ("training", "Team training", "users", "I train your team so they actually use HubSpot properly, because a CRM only works when people use it."),
]

LEAKS = [
    ("Marketing and sales use separate tools", "Leads fall through the gap between the two."),
    ("Sales does not hear about new leads in time", "By the time someone calls, the chance is often gone."),
    ("Sales calls without the lead's history", "Nobody can see which ad, page or email brought the lead in."),
    ("Follow up depends on someone remembering", "Without workflows, good leads quietly go cold."),
]
leak_box = L.leak_check(
    "Marketing and sales gap check", "Tick everything that sounds like your business today.", LEAKS,
    ("Nothing ticked. A free consultation still checks the hand off points that are easy to miss.",
     "A gap or two. Closing these is the first thing a proper HubSpot setup does.",
     "Leads are very likely falling between marketing and sales. Aligning them often brings more deals from the leads you already have."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "layers", "h3": "Setup and onboarding", "p": "The right settings, properties and structure for your business, set up properly from the start."},
    {"icon": "sliders", "h3": "Pipeline design", "p": "A sales pipeline and deal stages built around how you actually sell."},
    {"icon": "target", "h3": "Lead capture", "p": "Website forms and lead sources flowing straight into HubSpot, with no manual entry."},
    {"icon": "zap", "h3": "Workflows, email and sequences", "p": "Follow ups, tasks, reminders and sales sequences that run on their own, so leads never go cold."},
    {"icon": "chart", "h3": "Dashboards", "p": "Your pipeline, deals and team performance at a glance."},
    {"icon": "users", "h3": "Migration, integrations and training", "p": "Your data moved in cleanly, your other tools connected, and a team that knows how to use HubSpot."},
]

FAQ = [
    ("What is HubSpot?", "HubSpot is an all in one platform that brings your CRM, marketing, sales and service together. It keeps all your leads and customers in one place and helps you manage them from first contact to closed deal."),
    ("Is HubSpot free?", "HubSpot's core CRM is free, so you can start without a big cost. It also offers paid tools with more power, and I will help you choose only what you actually need."),
    ("Is HubSpot good for small business?", "Yes. You can start with the free CRM and add tools as you grow. It is user friendly and scales well, which makes it a strong fit for small and growing businesses."),
    ("Can you set it up for me?", "Yes. I handle the full setup, from onboarding and pipelines to automation and training, so you get a working system without the headache of doing it yourself."),
    ("Can you design pipelines and deal stages?", "Yes. I build your pipeline and deal stages around how you actually sell, so your process is clear and your team knows exactly what to do next."),
    ("Can you connect my website forms?", "Yes. I connect your website forms and lead sources so new contacts flow straight into HubSpot automatically, with no manual entry."),
    ("Can you automate follow ups with workflows?", "Yes. I build workflows that automate follow ups, tasks and reminders, so leads are always handled on time and nothing goes cold."),
    ("Can you set up email sequences?", "Yes. I set up email and sales sequences so your prospects get timely, consistent follow up without you doing it by hand."),
    ("Can you migrate my data?", "Yes. I move your existing leads and contacts into HubSpot cleanly and safely, so you start with all your data in one place."),
    ("Can you integrate HubSpot with my other tools?", "Yes. I connect HubSpot with the other tools you use, such as your website, calendar or ad accounts, so everything works together."),
    ("Will you train my team?", "Yes. I train your team so they actually use HubSpot properly, because a CRM only delivers results when people use it well."),
    ("How long does the setup take?", "It depends on how complex your process is, but most setups take from a few days to a couple of weeks. I will give you a clear timeline after our first talk."),
    ("Can you build reports and dashboards?", "Yes. I build clear dashboards so you can see your pipeline, deals and team performance at a glance."),
    ("Do you provide ongoing support?", "Yes. I stay available after setup to help with changes and improvements, so your HubSpot keeps working as your business grows."),
    ("How is HubSpot different from Zoho?", "Both are strong CRMs. HubSpot is known for ease of use and connecting marketing and sales, while Zoho is very affordable and flexible. I can help you pick the right one for your needs."),
    ("How do I get started?", "Just book a free HubSpot consultation using the button on this page. I will learn how you work and show you how a proper setup can grow your sales."),
]

RELATED = [
    ("Zoho CRM", "/services/zoho-crm/"),
    ("GoHighLevel", "/services/gohighlevel/"),
    ("CRM consulting", None),
    ("Sales funnel setup", "/services/sales-funnel-setup/"),
    ("Email automation", "/services/email-automation/"),
    ("Lead generation", None),
    ("Google Ads", "/services/google-ads/"),
    ("LinkedIn Ads", "/services/linkedin-ads/"),
]

PAGE = {
    "path": "/services/hubspot-crm/",
    "slug": "hubspot-crm",
    "form_name": "hubspot_crm",
    "service": "HubSpot CRM",
    "service_name": "HubSpot CRM implementation and setup",
    "thanks_what": "HubSpot consultation",
    "category": "CRM implementation",
    "service_desc": "HubSpot CRM implementation covering setup and onboarding, pipeline and deal stage design, forms and lead capture, workflows and automation, email and sales sequences, dashboards, data migration, integrations and team training.",
    "audience": "Businesses that want marketing and sales working as one system",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What HubSpot CRM implementation includes",
    "offers": [{"h3": n, "p": w} for _, n, _, w in WHAT],
    "title": "HubSpot CRM Implementation & Setup Services | Sushant Rana",
    "og_title": "HubSpot CRM Implementation & Setup Services",
    "og_alt": "HubSpot CRM implementation and setup services by Sushant Rana",
    "desc": "HubSpot CRM implementation services: I set up and automate HubSpot so marketing and sales work together. Pipelines, workflows, migration, training.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("HubSpot CRM", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about HubSpot"),
            "body": ["Cost, setup, workflows, data and training. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "HubSpot CRM implementation",
        "h1": ("HubSpot CRM setup that aligns", "your marketing and sales"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I set up, customize and automate HubSpot so your marketing and sales work as one system, and every lead is captured and followed up. '
            "If your marketing and sales feel disconnected, with leads slipping between them, HubSpot fixes that when it is set up right.",
            "HubSpot is one of the most powerful all in one platforms, but it only pays off when it fits how you work. We build your HubSpot around your process, automate the busywork and give you a clear view of your whole pipeline.",
        ],
        "cta2": ("See what I set up", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free HubSpot consultation",
        "sub": "Tell me how your marketing and sales work today and I will show you what a proper setup looks like.",
        "submit": "Request my free consultation",
        "steps": [
            {"label": "Your setup", "fields": [
                {"type": "radio", "name": "current_crm", "label": "What do you use to track leads today?", "req": True,
                 "options": ["Spreadsheets or notes", "HubSpot already", "Another CRM", "Nothing yet"]},
                {"type": "radio", "name": "team_size", "label": "How many people will use HubSpot?", "req": True,
                 "options": ["Just me", "2 - 5", "6 - 15", "16 - 50", "50+"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "problem", "label": "Main problem", "req": True, "placeholder": "Select your main problem",
                 "options": ["Marketing and sales are disconnected", "Leads get lost or go cold", "Follow up is slow or manual", "No clear view of the pipeline",
                             "Team does not use our CRM", "Moving from another CRM", "Not sure yet"]},
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Setup", "Pipelines", "Forms", "Workflows", "Sequences", "Dashboards", "Migration", "Integrations", "Training"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "How you sell, where leads come from, what is going wrong today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["HubSpot setup", "Deal pipelines", "Forms", "Workflows", "Sales sequences", "Dashboards", "Integrations", "Team training"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What HubSpot is", "and why it matters"),
             "body": ["HubSpot is an all in one platform that brings your CRM, marketing, sales and customer service together in one place. Its core CRM is free, and it grows with powerful tools as your needs grow.",
                      "This matters because most businesses run their marketing and sales in separate tools that do not talk to each other. Leads fall through the gaps. HubSpot connects everything, so a lead is tracked from the first click all the way to a closed deal, with nothing lost in between."],
             "bullets": ["CRM, marketing, sales and service in one place", "A free core CRM to start with", "Every lead tracked from first click to closed deal"],
             "cta": CTA, "visual": journey_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why HubSpot", "h2": ("Why HubSpot is", "a great choice"),
                      "body": ["HubSpot is built to keep marketing and sales on the same page. Here is why it is a strong fit."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "wallet", "h3": "A powerful free CRM to start", "p": "HubSpot's core CRM is free, so you can start organizing your leads and sales without a big upfront cost, then add tools as you grow."},
                          {"icon": "layers", "h3": "Marketing and sales in one place", "p": "Your ads, forms, emails, pipeline and deals all live together, so your marketing and sales teams finally work from the same information."},
                          {"icon": "zap", "h3": "Strong automation and workflows", "p": "HubSpot can automate follow ups, tasks and emails with easy to build workflows, which saves hours and stops leads going cold."},
                          {"icon": "gauge", "h3": "Easy to use and scale", "p": "HubSpot is known for being user friendly, and it scales from a small team to a large operation without needing to switch systems."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The HubSpot CRM implementation work", "I do for you"),
                           "body": ["Everything a working HubSpot needs, from the first setting to a trained team. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WHAT]})),
    L.split({"id": "value", "pill": "The real value", "h2": ("Why aligning marketing and sales", "wins more deals"),
             "body": ["The biggest reason leads are lost is that marketing and sales are not connected. Marketing brings in a lead, sales never hears about it in time, and the chance is gone.",
                      "HubSpot closes that gap. When it is set up right, every lead flows from marketing straight to sales with the full history attached, and automation makes sure it is followed up fast. This alignment often brings more deals from the leads you already have, which is where the real value lies."],
             "visual": leak_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the fake numbers and the people who were only browsing.",
                        "HubSpot already knows which of those leads became real deals. So when we set it up, the ad click is saved on every contact, your team moves deals through the pipeline as they work them, and HubSpot sends the qualified leads and closed deals back to Google Ads as conversions, with their value. From then on your ads go after buyers, not forms."],
                  bullets=["Ad click saved on every HubSpot contact", "Deal stages kept up to date by your sales team", "Qualified leads and closed deals sent back to Google Ads", "Reports on cost per qualified lead and cost per deal"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My HubSpot", "setup process"),
                   "body": ["A HubSpot that fits comes from understanding how your marketing and sales work first. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Discovery", "short": "Discovery", "p": "I learn how your marketing and sales work, where leads come from and what is going wrong today.", "points": ["How marketing and sales work", "Where leads come from", "What is going wrong"]},
                       {"h3": "Design", "short": "Design", "p": "I plan your pipeline, properties and workflows so HubSpot matches how your business actually runs.", "points": ["Pipeline and deal stages", "Properties that fit", "Workflows planned"]},
                       {"h3": "Build and automate", "short": "Build", "p": "I build the CRM, set up lead capture and create the workflows and sequences that automate follow up.", "points": ["CRM built", "Lead capture live", "Workflows and sequences"]},
                       {"h3": "Integrate and migrate", "short": "Integrate", "p": "I connect your other tools and move your existing data in cleanly, so everything lives in one place.", "points": ["Tools connected", "Data moved in cleanly", "One place for everything"]},
                       {"h3": "Train and support", "short": "Train", "p": "I train your team and stay available afterwards, so HubSpot keeps working as your business grows.", "points": ["Team training", "Help after setup", "Changes as you grow"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my HubSpot service"),
                  "body": ["You get a complete, done for you HubSpot setup that fits your business and is ready to use. I explain everything in simple terms. You work directly with me throughout."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Want your marketing and sales working as one?",
                                       "p": "Let me look at how you work today and show you how a properly set up HubSpot can capture every lead and close more deals. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for HubSpot"),
                  "body": ["A HubSpot your team actually uses, set up by the person you talk to."],
                  "cards": [
                      {"h3": "Built around how you work", "p": "I set up HubSpot to fit your real process, not a generic template, so your team actually uses it."},
                      {"h3": "Explained in plain language", "p": "I keep things simple and beginner friendly, so you understand and control your own system."},
                      {"h3": "Done for you, with support", "p": "I handle the whole setup and stay available afterwards, so you are never left stuck."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I set up", "HubSpot for"),
                     "body": "Sales and marketing teams, B2B companies, agencies, consultants and growing businesses. If you want your marketing and sales working together, HubSpot is a strong choice.",
                     "chips": [("Sales and marketing teams", None), ("B2B companies", None), ("Agencies", None), ("Consultants", None),
                               ("Growing businesses", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "HubSpot"),
                     "body": "HubSpot earns more when the leads feeding it and the follow up coming out of it are handled alongside it.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to connect your", "marketing and sales?"),
               "p": "Let us look at how you work today and build a HubSpot setup that captures every lead, automates your follow up and helps you close more deals.",
               "btn": CTA, "note": "No obligation · Free HubSpot consultation"}),
]
