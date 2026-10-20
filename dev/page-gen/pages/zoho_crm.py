# Zoho CRM Implementation and Setup Services. Copy: 25_Zoho_CRM_Setup_Services.docx
# No CRM client is published yet, so there is no client work section.
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free Zoho CRM consultation"

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


# --------------------------------------------------- interactive pipeline (basics)

STAGES = ["New lead", "Contacted", "Qualified", "Won"]
STAGE_NOTES = [
    "A form fill lands in Zoho on its own, with its source, and is assigned to a salesperson.",
    "A follow up task and reminder are created, so the first call is never forgotten.",
    "The lead is a real opportunity. The next step and its date sit right on the record.",
    "Deal closed. Every call, email and note from first contact is still on the record.",
]


def board_panel(i):
    cols = ""
    for j, st in enumerate(STAGES):
        card = (f'<span class="block rounded-lg border border-orange bg-orange/10 p-2 text-[10px] font-bold leading-tight text-ink">Your next customer</span>'
                if j == i else '<span class="block h-8 rounded-lg bg-ink/[0.06]"></span>')
        cols += (f'<div class="grid content-start gap-1.5 rounded-xl bg-[#fff7f3] p-2"><p class="truncate text-[10px] font-bold uppercase tracking-wide {"text-orange" if j == i else "text-muted"}">{E(st)}</p>'
                 f'{card}<span class="block h-8 rounded-lg bg-ink/[0.06]"></span></div>')
    return f'<div data-panel="s{i}"{HID if i else ""}><div class="grid grid-cols-4 gap-2">{cols}</div>{note(E(STAGE_NOTES[i]))}</div>'


pipeline_box = ('<div data-tabs="true">' + figure("Your Zoho CRM pipeline", ["Example"], (
    label("Move one lead through the pipeline")
    + f'<div class="mt-2.5">{seg([("s" + str(i), s) for i, s in enumerate(STAGES)])}</div>'
    + '<div class="mt-4">' + "".join(board_panel(i) for i in range(len(STAGES))) + "</div>")) + "</div>")

# --------------------------------------------------- what I do: one mock per tab

MOCKS = {
    "setup": figure("Modules and fields", ["Example"], (
        label("Modules switched on for you")
        + '<div class="mt-2.5 flex flex-wrap gap-2">' + "".join(
            f'<span class="rounded-full border border-orange/30 bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{m}</span>'
            for m in ["Leads", "Contacts", "Accounts", "Deals", "Tasks"]) + "</div>"
        + '<div class="mt-4">' + label("Fields that fit your business") + '</div><div class="mt-2.5 grid gap-2">' + "".join(
            f'<div class="flex items-center justify-between gap-3 rounded-xl border border-[var(--color-line)] bg-white px-3 py-2.5"><span class="text-xs font-semibold text-ink">{f}</span>'
            '<span class="block h-2 w-24 rounded-full bg-ink/10" aria-hidden="true"></span></div>'
            for f in ["Lead source", "Service interested in", "City", "Budget range"]) + "</div>")),
    "pipeline": figure("Pipeline stages", ["Example"], (
        label("Your stages, in your words")
        + '<ol class="mt-3 grid list-none gap-2">' + "".join(
            f'<li class="flex items-center gap-3 rounded-2xl border {"border-orange bg-orange/5" if i == 2 else "border-[var(--color-line)] bg-white"} p-3">'
            f'<span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i + 1}</span>'
            f'<span class="text-sm font-semibold text-ink">{s}</span></li>'
            for i, s in enumerate(["New enquiry", "First call done", "Meeting or demo", "Quote sent", "Won or lost"])) + "</ol>"
        + note("Every salesperson knows what each stage means and what has to happen next."))),
    "capture": figure("Lead capture", ["Example"], (
        '<div class="grid grid-cols-2 gap-2.5">' + "".join(
            f'<div class="flex items-center gap-2 rounded-2xl border border-[var(--color-line)] bg-white p-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-4 w-4")}</span>'
            f'<span class="text-xs font-bold text-ink">{t}</span></div>'
            for ic, t in [("file", "Website forms"), ("target", "Ad lead forms"), ("layers", "Landing pages"), ("phone", "Other sources")]) + "</div>"
        + '<span aria-hidden="true" class="mx-auto mt-2 mb-2 block h-5 w-0.5 bg-orange"></span>'
        + rows([("New lead in Zoho CRM", "Source saved, owner assigned", "Automatic", True)]))),
    "automation": figure("Workflow rule", ["Example"], flow("A new lead is created", [
        ("users", "Assign it to the right salesperson"), ("file", "Send the welcome email"),
        ("phone", "Create a call task for today"), ("repeat", "Remind the owner if it is still not contacted")])),
    "email": figure("Contact timeline", ["Example"], (
        '<div class="flex items-center gap-3 border-b border-[var(--color-line)] pb-3"><span class="grid h-10 w-10 place-items-center rounded-full bg-orange/10 text-orange">'
        f'{svg("users", "h-5 w-5")}</span><span><span class="block text-sm font-bold text-ink">Your customer</span><span class="text-xs text-muted">customer@theirbusiness.com</span></span></div>'
        '<div class="mt-3">' + rows([("Email sent: your quote", "From your inbox", "Tracked", True), ("Reply received", "Saved on this contact", "Tracked", True),
                                     ("Follow up email", "Sent automatically", "Scheduled")]) + "</div>")),
    "reports": figure("Sales dashboard", ["Example"], (
        '<div class="grid grid-cols-3 gap-2.5">' + "".join(
            f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3"><p class="text-[10px] font-semibold uppercase tracking-wide text-muted">{t}</p>'
            '<span class="mt-2 block h-3 w-3/4 rounded-full bg-orange/20" aria-hidden="true"></span></div>'
            for t in ["New leads", "Open deals", "Won deals"]) + "</div>"
        + '<div class="mt-4 rounded-2xl border border-[var(--color-line)] p-4">' + label("Pipeline by stage") + f'<div class="mt-3">{bars()}</div></div>'
        + note("Your pipeline, sales and team performance on one screen."))),
    "migration": figure("Data migration", ["Example"], (
        '<div class="grid grid-cols-2 gap-3"><div class="rounded-2xl border border-[var(--color-line)] p-3">' + label("Old spreadsheet")
        + '<div class="mt-2.5 grid gap-1.5" aria-hidden="true">' + '<span class="block h-2.5 rounded bg-ink/10"></span>' * 6 + "</div></div>"
        + '<div class="rounded-2xl border border-orange/30 bg-orange/5 p-3">' + label("Zoho CRM")
        + '<div class="mt-2.5 grid gap-1.5">' + "".join(
            f'<span class="flex items-center gap-1.5 text-[11px] font-semibold text-ink">{svg("check", "h-3.5 w-3.5 shrink-0 text-orange", 3)}{t}</span>'
            for t in ["Columns matched to fields", "Duplicates cleaned up", "Owners assigned", "Nothing left behind"]) + "</div></div></div>"
        + note("Leads and contacts from spreadsheets or another CRM, moved in cleanly and safely."))),
    "training": figure("Team training", ["Example"], (
        label("What your team can do after training")
        + '<div class="mt-3 grid gap-2.5">' + "".join(
            f'<label class="svc-check"><input type="checkbox" class="sr-only"/><span class="svc-box">{svg("check", "h-3.5 w-3.5", 3)}</span>'
            f'<span class="text-sm font-bold text-ink">{t}</span></label>'
            for t in ["Add a new lead", "Move a deal to the next stage", "Log a call and set a reminder", "Read the sales dashboard"]) + "</div>"
        + note("Tick them off. A CRM only works if people use it properly.", "users"))),
}

WHAT = [
    ("setup", "Setup and configuration", "layers", "I set up your Zoho CRM properly from the start, with the right modules, fields and settings for your business."),
    ("pipeline", "Pipeline and stage design", "sliders", "I build your sales pipeline and stages around how you actually sell, so your process is clear and easy to follow."),
    ("capture", "Lead capture setup", "target", "I connect your website forms, ads and other sources so new leads flow straight into your CRM automatically."),
    ("automation", "Automation and workflows", "zap", "I automate follow ups, reminders and tasks, so leads are always contacted on time and nothing is forgotten."),
    ("email", "Email integration", "file", "I connect your email so every message is tracked against the right contact, and I can set up automated emails too."),
    ("reports", "Reports and dashboards", "chart", "I build clear reports and dashboards so you can see your pipeline, sales and team performance at a glance."),
    ("migration", "Data migration", "repeat", "I move your existing leads and contacts from spreadsheets or another CRM into Zoho, cleanly and safely."),
    ("training", "Team training", "users", "I train your team so they actually use the CRM, because a CRM only works if people use it properly."),
]

LEAKS = [
    ("My leads live in spreadsheets, inboxes and notes", "There is no single place that shows every lead and where it stands."),
    ("Some leads never get a second follow up", "Lost follow ups are lost sales, even when the lead was a good one."),
    ("Nobody is reminded when to call back", "Follow up depends on someone remembering, which is when leads slip."),
    ("I cannot see my pipeline at a glance", "You do not know what is closing this month or which lead is stuck."),
]
leak_box = L.leak_check(
    "Follow up leak check", "Tick everything that sounds like your business today.", LEAKS,
    ("Nothing ticked. A free consultation still checks the parts of your process that are easy to miss.",
     "A leak or two. These are the first things a proper Zoho setup closes.",
     "Leads are very likely slipping through. Fixing follow up often brings more sales from the leads you already have."),
    CTA)

GET = [
    {"icon": "layers", "h3": "Setup and configuration", "p": "The right modules, fields and settings for your business, set up properly from the start."},
    {"icon": "sliders", "h3": "Pipeline design", "p": "A sales pipeline and stages built around how you actually sell, clear and easy to follow."},
    {"icon": "zap", "h3": "Lead capture and automation", "p": "Website forms, ads and other sources flowing straight in, with follow ups, reminders and tasks automated."},
    {"icon": "file", "h3": "Email integration", "p": "Every message tracked against the right contact, with automated emails where they help."},
    {"icon": "chart", "h3": "Reports and dashboards", "p": "Your pipeline, sales and team performance at a glance."},
    {"icon": "users", "h3": "Data migration and team training", "p": "Your existing data moved in cleanly, and a team that knows how to use the CRM properly."},
]

FAQ = [
    ("What is Zoho CRM?", "Zoho CRM is a system that keeps all your leads and customers in one place, tracks every conversation and helps you manage sales from first contact to closed deal."),
    ("Why do I need a CRM?", "Without a CRM, leads get lost and follow ups are forgotten, which means lost sales. A CRM keeps everything organized so nothing slips and you close more deals."),
    ("Is Zoho CRM good for small business?", "Yes. Zoho CRM is powerful but affordable, which makes it a great fit for small and growing businesses that want serious features without a huge cost."),
    ("Can you set it up for me?", "Yes. I handle the full setup, from configuration and pipelines to automation and training, so you get a working CRM without the headache of doing it yourself."),
    ("Can you customize the pipelines and fields?", "Yes. I shape your pipeline, stages and fields around how you actually sell, so the CRM matches your real process instead of forcing you to change."),
    ("Can you connect my website and ad leads?", "Yes. I connect your website forms, ads and other sources so new leads flow straight into your CRM automatically, with no manual entry."),
    ("Can you automate follow ups?", "Yes. I set up automation for follow ups, reminders and tasks, so leads are always contacted on time and nothing is forgotten."),
    ("Can you migrate my data from spreadsheets or another CRM?", "Yes. I move your existing leads and contacts into Zoho cleanly and safely, so you start with all your data in one place."),
    ("Will you train my team?", "Yes. I train your team so they actually use the CRM properly, because a CRM only delivers results when people use it."),
    ("How long does the setup take?", "It depends on how complex your process is, but most setups take from a few days to a couple of weeks. I will give you a clear timeline after our first talk."),
    ("Is Zoho CRM affordable?", "Yes. Zoho is known for offering strong features at a reasonable price, and I will help you choose the right plan for your needs."),
    ("Can it send emails automatically?", "Yes. I connect your email and can set up automated emails and sequences, so leads get timely, consistent follow up without manual effort."),
    ("Can you build reports and dashboards?", "Yes. I build clear reports and dashboards so you can see your pipeline, sales and team performance at a glance."),
    ("Do you provide ongoing support?", "Yes. I stay available after setup to help with changes, questions and improvements, so your CRM keeps working as your business grows."),
    ("Is my data safe in Zoho CRM?", "Zoho follows strong security practices to protect your data. I also set up your account correctly with the right access controls for your team."),
    ("How do I get started?", "Just book a free Zoho CRM consultation using the button on this page. I will learn how you work and show you how a proper setup can grow your sales."),
]

RELATED = [
    ("HubSpot CRM", "/services/hubspot-crm/"),
    ("GoHighLevel", "/services/gohighlevel/"),
    ("CRM consulting", None),
    ("Sales funnel setup", "/services/sales-funnel-setup/"),
    ("Email automation", "/services/email-automation/"),
    ("Lead generation", None),
    ("Google Ads", "/services/google-ads/"),
]

PAGE = {
    "path": "/services/zoho-crm/",
    "slug": "zoho-crm",
    "form_name": "zoho_crm",
    "service": "Zoho CRM",
    "service_name": "Zoho CRM implementation and setup",
    "thanks_what": "Zoho CRM consultation",
    "category": "CRM implementation",
    "service_desc": "Zoho CRM implementation covering setup and configuration, pipeline and stage design, lead capture, automation and workflows, email integration, reports and dashboards, data migration and team training.",
    "audience": "Businesses with leads to manage and sales to close",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What Zoho CRM implementation includes",
    "offers": [{"h3": n, "p": w} for _, n, _, w in WHAT],
    "title": "Zoho CRM Implementation & Setup Services | Sushant Rana",
    "og_title": "Zoho CRM Implementation & Setup Services",
    "og_alt": "Zoho CRM implementation and setup services by Sushant Rana",
    "desc": "Zoho CRM implementation services: I set up, customize and automate Zoho CRM so you stop losing leads. Pipelines, automation, migration and training.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Zoho CRM", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Frequently asked questions", "about Zoho CRM"),
            "body": ["Setup, cost, data, automation and training. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Zoho CRM implementation",
        "h1": ("Zoho CRM setup that organizes your leads", "and grows your sales"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I set up, customize and automate Zoho CRM so every lead is captured, followed up and turned into more business. '
            "If your leads are scattered across spreadsheets, your inbox and sticky notes, some are slipping through the cracks, and that is costing you sales.",
            "A CRM only helps if it is set up around how you actually work. We build your Zoho CRM to fit your sales process, automate the boring follow up, and give you a clear view of your pipeline, so nothing gets forgotten and more deals get closed.",
        ],
        "cta2": ("See what I set up", "#types"),
        "stats": [("8+", "Years experience"), ("4", "Markets served"), ("100%", "Accounts you own"), ("1", "Point of contact")],
    },
    "form": {
        "title": "Book your free Zoho CRM consultation",
        "sub": "Tell me how you handle leads today and I will show you what a proper setup looks like.",
        "submit": "Request my free consultation",
        "steps": [
            {"label": "Your setup", "fields": [
                {"type": "radio", "name": "current_crm", "label": "What do you use to track leads today?", "req": True,
                 "options": ["Spreadsheets or notes", "Zoho CRM already", "Another CRM", "Nothing yet"]},
                {"type": "radio", "name": "team_size", "label": "How many people will use the CRM?", "req": True,
                 "options": ["Just me", "2 - 5", "6 - 15", "16 - 50", "50+"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "problem", "label": "Main problem", "req": True, "placeholder": "Select your main problem",
                 "options": ["Leads get lost or forgotten", "Follow up is slow or manual", "No clear view of the pipeline", "Team does not use our CRM", "Moving from another CRM", "Not sure yet"]},
                {"type": "checkbox", "name": "needs", "label": "What do you need help with?",
                 "options": ["Setup", "Pipelines", "Lead capture", "Automation", "Email", "Reports", "Migration", "Training"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "How you sell, where leads come from, what is going wrong today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Zoho CRM setup", "Pipelines", "Lead capture", "Workflows", "Email integration", "Dashboards", "Data migration", "Team training"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What a CRM does", "and why you need one"),
             "body": ["A CRM, or customer relationship management system, is one place to store all your leads and customers, track every conversation and manage your sales from first contact to closed deal.",
                      "Without one, leads get lost, follow ups are forgotten and you never really know what is happening in your pipeline. Zoho CRM fixes this by keeping everything organized in one place, so your team always knows who to contact and when, and no opportunity slips away."],
             "bullets": ["Every lead and customer in one place", "Every conversation tracked", "A clear pipeline from first contact to closed deal"],
             "cta": CTA, "visual": pipeline_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why Zoho", "h2": ("Why Zoho CRM is", "a great choice"),
                      "body": ["Zoho CRM gives small and growing businesses serious features without a huge cost. Here is why it is a strong fit."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "wallet", "h3": "Powerful but affordable", "p": "Zoho CRM gives you serious features at a price that works for small and growing businesses, which makes it great value."},
                          {"icon": "layers", "h3": "Part of a full ecosystem", "p": "Zoho connects with email, marketing, books, desk and many other tools, so your whole business can run in one connected system."},
                          {"icon": "sliders", "h3": "Flexible and customizable", "p": "Zoho can be shaped around your exact sales process, fields and stages, rather than forcing you to change how you work."},
                          {"icon": "zap", "h3": "Built in automation", "p": "Zoho can automate follow ups, reminders and tasks, so your team spends less time on admin and more time selling."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "What I do", "h2": ("The Zoho CRM implementation work", "I do for you"),
                           "body": ["Everything a working CRM needs, from the first setting to a trained team. Pick one to see what it looks like."],
                           "items": [{"key": k, "name": n, "icon": ic, "what": w, "mock": MOCKS[k]} for k, n, ic, w in WHAT]})),
    L.split({"id": "value", "pill": "The real value", "h2": ("Why a good setup means", "no lead falls through"),
             "body": ["The biggest leak in most businesses is not lead generation, it is follow up. Leads come in and then get forgotten, and those lost follow ups are lost sales.",
                      "A properly set up Zoho CRM closes that leak. Every lead is captured, assigned and followed up automatically, with reminders so nothing slips. This single change often brings more sales from the leads you already have, without spending a rupee more on marketing. That is the real value of doing the setup right."],
             "visual": leak_box}),
    L.crm_section("Google Ads", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                  body=["Google Ads learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the fake numbers and the people who were only browsing.",
                        "Your Zoho CRM is the one place that knows which leads were real. So when we set it up, the ad click is saved with every lead, your team updates the lead status as they work it, and Zoho sends the qualified leads and sales back to Google Ads as conversions, with their value. From then on your ads go after buyers, not forms."],
                  bullets=["Ad click saved with every lead in Zoho", "Lead status kept up to date by your sales team", "Qualified leads and sales sent back to Google Ads", "Reports on cost per qualified lead and cost per sale"]),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My Zoho CRM", "setup process"),
                   "body": ["A CRM that fits comes from understanding how you sell first. Pick a stage to follow along, or read all five below."],
                   "steps": [
                       {"h3": "Discovery", "short": "Discovery", "p": "I learn how you sell, where your leads come from and what is going wrong today, so the setup fits your real process.", "points": ["How you sell today", "Where leads come from", "What is going wrong"]},
                       {"h3": "Design pipelines and fields", "short": "Design", "p": "I plan your pipeline, stages and fields, so the CRM matches how your business actually works.", "points": ["Pipeline and stages", "Fields that fit", "Matches your process"]},
                       {"h3": "Build and automate", "short": "Build", "p": "I build the CRM, set up lead capture and automate your follow ups, reminders and tasks.", "points": ["CRM built", "Lead capture live", "Follow ups automated"]},
                       {"h3": "Integrate and migrate", "short": "Integrate", "p": "I connect your email and tools and move your existing data in cleanly, so everything is in one place.", "points": ["Email connected", "Tools connected", "Data moved in cleanly"]},
                       {"h3": "Train and support", "short": "Train", "p": "I train your team and stay available to help, so the CRM keeps working for you long after setup.", "points": ["Team training", "Help after setup", "Changes as you grow"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my Zoho CRM service"),
                  "body": ["You get a complete, done for you Zoho CRM setup that fits your business and is ready to use from day one. I explain everything in simple terms, so you always understand your own system. You work directly with me throughout."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Tired of losing leads and chasing follow ups?",
                                       "p": "Let me look at how you work today and show you how a properly set up Zoho CRM can capture every lead and close more sales. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for Zoho CRM"),
                  "body": ["A CRM your team actually uses, set up by the person you talk to."],
                  "cards": [
                      {"h3": "Built around how you work", "p": "I set up your CRM to fit your real sales process, not a generic template, so your team actually uses it."},
                      {"h3": "Explained in plain language", "p": "I keep things simple and beginner friendly, so you understand and control your own system without needing a manual."},
                      {"h3": "Done for you, with support", "p": "I handle the whole setup and stay available afterwards, so you are never left stuck on your own."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I set up", "Zoho CRM for"),
                     "body": "Sales teams, service businesses, agencies, consultants and small to mid sized companies. If you have leads to manage and sales to close, a well built CRM will help you do it better.",
                     "chips": [("Sales teams", None), ("Service businesses", None), ("Agencies", None), ("Consultants", None),
                               ("Small to mid sized companies", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "Zoho CRM"),
                     "body": "A CRM earns more when the leads feeding it and the follow up coming out of it are handled alongside it.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to stop", "losing leads?"),
               "p": "Let us look at how you work today and build a Zoho CRM that captures every lead, automates your follow up and helps you close more sales.",
               "btn": CTA, "note": "No obligation · Free Zoho CRM consultation"}),
]
