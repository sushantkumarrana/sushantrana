# Book a strategy call. Facts from Sushant (2026-10-14): free, 30 minutes,
# Google Meet, booked by form then confirmed on WhatsApp (8289051732).
import json
import re

E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

SITE = L.SITE
CTA = "Book your free strategy call"

_cat = open("api/catalog.php").read()
SERVICES = json.loads(re.search(r"const ALL_SERVICES = (\[.*?\]);", _cat).group(1))
OTHER = re.search(r'const OTHER_SERVICE = "([^"]+)"', _cat).group(1)

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# the call, as a week planner the visitor can click through (illustration)
planner = '<div data-tabs="true">' + figure("Your call", ["Free · 30 min"], (
    '<p class="text-[10px] font-bold uppercase tracking-wider text-muted">Pick a day you prefer</p>'
    '<div class="mt-2.5 grid grid-cols-6 gap-1.5">' + "".join(
        f'<button type="button" data-tab="{d.lower()}" aria-pressed="{"true" if i == 1 else "false"}" data-on="border-orange bg-orange text-white" '
        f'data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" class="rounded-xl border px-1 py-2.5 text-xs font-bold transition '
        f'{"border-orange bg-orange text-white" if i == 1 else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{d}</button>'
        for i, d in enumerate(DAYS))
    + "</div>" + "".join(
        f'<div data-panel="{d.lower()}"{L.HID if i != 1 else ""} class="mt-4 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-4">'
        f'<p class="flex items-center gap-2 text-sm font-bold text-ink">{svg("calendar", "h-4 w-4 text-orange")}{d}, a time that suits you</p>'
        f'<p class="mt-2 flex items-center gap-2 text-sm text-body">{svg("clock", "h-4 w-4 text-orange")}30 minutes</p>'
        f'<p class="mt-2 flex items-center gap-2 text-sm text-body">{svg("video", "h-4 w-4 text-orange")}Google Meet link sent on WhatsApp</p></div>'
        for i, d in enumerate(DAYS))
    + '<p class="mt-4 text-xs text-muted">You tell me the days and times that work in the form. I confirm the exact slot on WhatsApp.</p>')) + "</div>"

COVER = [
    {"icon": "target", "h3": "Your goals", "p": "Where the business is today, where you want it to be, and what a good result looks like for you."},
    {"icon": "chart", "h3": "What is working now", "p": "Your ads, website, SEO and leads as they stand, looked at with the numbers you already have."},
    {"icon": "phone", "h3": "Tracking and follow up", "p": "Whether leads and sales are being counted properly and how quickly enquiries are followed up."},
    {"icon": "layers", "h3": "Clear next steps", "p": "What I would do first and why, so you leave the call knowing your options, whether or not we work together."},
]

FAQ = [
    ("Is the strategy call really free?", "Yes. The call is free and there is no obligation to work together afterwards."),
    ("How long is the call?", "30 minutes, on Google Meet."),
    ("How do I book a time?", "Fill in the short form on this page with the days and times that suit you. I confirm the exact slot on WhatsApp and send the Google Meet link."),
    ("What should I prepare?", "Your website link, access to any numbers you already track, and a short list of what you want to grow. Nothing else is needed."),
    ("Who will I speak to?", "You speak to me, Sushant Rana, directly. Not a sales team."),
    ("Do you take calls with businesses outside India?", "Yes. I work with clients across India, the USA, Canada and Australia, so tell me your time zone in the form and I will fit the call around it."),
    ("What happens after the call?", "If it makes sense to work together, I send a clear plan and a quote. If not, you still keep the advice from the call."),
]

PAGE = {
    "path": "/contact/book-strategy-call/",
    "slug": "strategy-call",
    "form_name": "strategy_call",
    "service": OTHER,
    "wa_label": "strategy call",
    "enquiry": "consultation",
    "service_name": "Book a strategy call",
    "thanks_what": "strategy call",
    "title": "Book a Free Strategy Call | Sushant Rana",
    "og_title": "Book a Free Strategy Call with Sushant Rana",
    "og_alt": "Book a free 30 minute strategy call with Sushant Rana",
    "desc": "Book a free 30 minute strategy call with Sushant Rana on Google Meet. Tell me your goals, pick a time, and I confirm it on WhatsApp. No obligation.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Contact", "/contact/"), ("Book a strategy call", None)],
    "related": [],
    "faq": {"pill": "Common questions", "h2": ("Strategy call", "questions, answered"), "body": [], "items": FAQ},
    "hero": {
        "pill": "Free strategy call",
        "h1": ("Book a free strategy call,", "30 minutes on Google Meet"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>. Tell me about your business and when you are free, and we will spend 30 minutes on Google Meet looking at your goals, what is working today and what to do next.',
            "Fill in the form, I confirm the time on WhatsApp, and you get the Google Meet link. No obligation and no sales team.",
        ],
        "cta2": ("How the call works", "#process"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("30 min", "Free call")],
    },
    "form": {
        "title": "Book your free strategy call",
        "sub": "Free, 30 minutes on Google Meet. I confirm the time on WhatsApp.",
        "submit": "Request my call",
        "steps": [
            {"label": "Business", "fields": [
                {"type": "select", "name": "service", "label": "What do you want to talk about?", "req": True, "placeholder": "Select a topic",
                 "options": SERVICES + [OTHER]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
                {"type": "textarea", "name": "details", "label": "What do you want to grow?", "placeholder": "Your goals, and what you have tried so far..."},
            ]},
            {"label": "Time", "fields": [
                {"type": "checkbox", "name": "days", "label": "Days that suit you", "req": True, "options": DAYS},
                {"type": "radio", "name": "time", "label": "Time of day", "req": True, "options": ["Morning", "Afternoon", "Evening"]},
                {"type": "select", "name": "timezone", "label": "Your time zone", "req": True, "placeholder": "Select your time zone",
                 "options": ["India (IST)", "UAE (GST)", "UK (GMT/BST)", "US Eastern", "US Central", "US Pacific", "Canada Eastern", "Australia Eastern", "Other"]},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

url = SITE + "/contact/book-strategy-call"
PAGE["graph"] = [
    {"@type": "ContactPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#person"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/og.jpg", "width": 1200, "height": 630},
     "potentialAction": {"@type": "ReserveAction", "name": "Book a free 30 minute strategy call", "target": url + "/"}},
    {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"}, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
]

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Free strategy call", "30 minutes", "Google Meet", "Goals", "Ads", "SEO", "Website", "CRM", "Next steps"]),
    L.split({"id": "call", "pill": "The call", "h2": ("Thirty minutes,", "focused on your business"),
             "body": ["The call is about your business, not a sales pitch. We look at where you are, what you want, and what is getting in the way, using the numbers you already have.",
                      "You leave with a clear picture of your options and what I would do first, whether or not we work together."],
             "bullets": ["Free and with no obligation", "You talk to me directly", "Google Meet, at a time that suits you"],
             "cta": CTA, "visual": planner}, dark=True),
    L.section_bg(
        L.process({"id": "process", "pill": "How it works", "h2": ("From this page", "to your call"),
                   "body": ["Four simple steps. Pick one to follow along."],
                   "steps": [
                       {"h3": "Tell me about you", "short": "Form", "p": "Fill in the short form: your business, what you want to grow, and the days and times that suit you.", "points": ["Two minutes", "Your goals", "Your preferred times"]},
                       {"h3": "Confirm on WhatsApp", "short": "Confirm", "p": "WhatsApp opens with your details filled in. I confirm the exact time there.", "points": ["Details already typed", "Time confirmed", "Google Meet link sent"]},
                       {"h3": "The 30 minute call", "short": "Call", "p": "We meet on Google Meet and go through your goals, what is working, and what is not.", "points": ["Your goals", "Current results", "What is in the way"]},
                       {"h3": "Clear next steps", "short": "Plan", "p": "You leave knowing what to do next. If it makes sense to work together, I send a plan and a quote.", "points": ["Practical next steps", "Plan and quote if needed", "No obligation"]},
                   ]})),
    L.icon_cards({"id": "cover", "pill": "What we cover", "h2": ("What we will talk", "about on the call"),
                  "body": ["Every call is shaped around your business. These are the four things we usually get through."],
                  "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": COVER}),
    L.projects_section(["ourknots", "yalla", "warriors", "4s", "touch", "elixir"], ("Businesses I", "already work with"),
                       "Real brands in India, the UAE, the USA and Canada. Pick one to see what we do for them."),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Let's find your", "next step"), "p": "Tell me about your business and when you are free. I confirm the time on WhatsApp.",
               "btn": CTA, "note": "Free · 30 minutes · Google Meet"}),
]
