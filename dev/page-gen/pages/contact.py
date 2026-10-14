# Contact page. Facts from Sushant (2026-10-14): WhatsApp/call 8289051732,
# email me@sushantrana.com, city Chandigarh; strategy call = free, 30 min,
# Google Meet, booked by form + WhatsApp. Social links wait for real URLs.
import json
import re

E, svg, figure, pill = L.E, L.svg, L.figure, L.pill

SITE = L.SITE
PHONE_E164 = "+918289051732"
PHONE_SHOW = "+91 82890 51732"
WA = "https://wa.me/918289051732"
EMAIL = "me@sushantrana.com"
CTA = "Send my message"  # hero/modal form title CTA; buttons below name their own action

# services the visitor can pick: the lead API allow-list, plus "not sure"
_cat = open("api/catalog.php").read()
SERVICES = json.loads(re.search(r"const ALL_SERVICES = (\[.*?\]);", _cat).group(1))
OTHER = re.search(r'const OTHER_SERVICE = "([^"]+)"', _cat).group(1)

WAYS = [
    ("chat", "WhatsApp", "Message me directly. Most conversations start here.", "Chat on WhatsApp", WA, ' target="_blank" rel="noopener"'),
    ("phone", "Call", PHONE_SHOW, "Call now", f"tel:{PHONE_E164}", ""),
    ("mail", "Email", EMAIL, "Send an email", f"mailto:{EMAIL}", ""),
    ("calendar", "Strategy call", "Free, 30 minutes on Google Meet.", "Book a strategy call", "/contact/book-strategy-call/", " data-no-popup=\"true\""),
]

ways = (
    '<section class="section" aria-labelledby="ways-heading">'
    + L.centered_head({"id": "ways", "pill": "Ways to reach me", "h2": ("Pick whatever is", "easiest for you"),
                       "body": ["Every message comes straight to me, not to a sales team."]})
    + '<ul class="wrap mt-14 grid list-none gap-5 sm:grid-cols-2 lg:grid-cols-4">' + "".join(
        f'<li class="flex"><div data-reveal="true" class="flex w-full"{L.d(i, per=4)}><article class="card flex w-full flex-col p-7">'
        f'<span class="grid h-12 w-12 place-items-center rounded-2xl bg-orange/10 text-orange">{svg(ic, "h-6 w-6")}</span>'
        f'<h3 class="mt-5 text-xl font-extrabold text-ink">{E(t)}</h3><p class="mt-2.5 break-words text-body">{E(p)}</p>'
        f'<a href="{href}"{attrs} class="btn btn-outline mt-6 w-full">{E(btn)}</a></article></div></li>'
        for i, (ic, t, p, btn, href, attrs) in enumerate(WAYS))
    + '</ul></section>')

where = L.split({"id": "where", "pill": "Where I work from", "h2": ("Based in Chandigarh,", "working with brands abroad"),
                 "body": ["I work from Chandigarh, India, with clients across India, the USA, Canada and Australia. Calls happen on Google Meet, and day to day updates on WhatsApp, so the time difference rarely gets in the way."],
                 "bullets": ["Calls on Google Meet", "Day to day updates on WhatsApp", "One person to talk to, from first call to results"],
                 "visual": figure("Contact details", ["Direct"], (
                     '<ul class="grid list-none gap-3">' + "".join(
                         f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-4">'
                         f'<span class="grid h-10 w-10 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(ic, "h-5 w-5")}</span>'
                         f'<span class="min-w-0"><span class="block text-[10px] font-bold uppercase tracking-wider text-muted">{E(k)}</span>'
                         f'<span class="block break-words text-sm font-semibold text-ink">{v}</span></span></li>'
                         for ic, k, v in [("pin", "City", "Chandigarh, India"),
                                          ("phone", "Call or WhatsApp", f'<a class="hover:text-orange" href="tel:{PHONE_E164}">{PHONE_SHOW}</a>'),
                                          ("mail", "Email", f'<a class="hover:text-orange" href="mailto:{EMAIL}">{EMAIL}</a>'),
                                          ("video", "Calls", "Google Meet")])
                     + "</ul>"))}, dark=True)

booking_teaser = L.cta_band({"pill": "Prefer to talk first?", "h3": "Book a free 30 minute strategy call",
                             "p": "Tell me about your business, pick a day and time that suits you, and we confirm it on WhatsApp. The call itself is on Google Meet.",
                             "btn": "Book a strategy call"}).replace(
    'href="#contact" class="btn btn-primary">Book a strategy call', 'href="/contact/book-strategy-call/" data-no-popup="true" class="btn btn-primary">Book a strategy call')

FAQ = [
    ("How quickly will you reply?", "I reply personally within one business day, usually sooner. WhatsApp is the fastest way to reach me."),
    ("Is the first conversation free?", "Yes. The first conversation and the strategy call are free, with no obligation to work together."),
    ("Do you work with businesses outside India?", "Yes. I work with clients across India, the USA, Canada and Australia, on Google Meet and WhatsApp."),
    ("Can I just message you on WhatsApp?", f"Yes. Message me on WhatsApp at {PHONE_SHOW} and I will pick it up from there."),
    ("What should I tell you in my first message?", "What your business does, what you want to grow, and what you have tried so far. A link to your website helps too."),
]

PAGE = {
    "path": "/contact/",
    "slug": "contact",
    "form_name": "contact",
    "service": OTHER,
    "wa_label": "contact form",
    "enquiry": "consultation",
    "service_name": "Contact",
    "thanks_what": "message",
    "title": "Contact Sushant Rana | Call, WhatsApp or Email",
    "og_title": "Contact Sushant Rana",
    "og_alt": "Contact Sushant Rana, business growth consultant",
    "desc": "Contact Sushant Rana by WhatsApp, call or email, or send a message here. Based in Chandigarh, working with brands in India, the USA, Canada and Australia.",
    "cta": "Send me a message",
    "trail": [("Home", "/"), ("Contact", None)],
    "related": [],
    "faq": {"pill": "Common questions", "h2": ("Before you", "get in touch"), "body": [], "items": FAQ},
    "hero": {
        "pill": "Contact",
        "h1": ("Let's talk about", "growing your business"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>. Send me a message with the form, or reach me directly on WhatsApp, by phone or by email. Every message comes to me, and I reply personally within one business day, usually sooner.',
            f'Call or WhatsApp: <a class="font-semibold text-orange" href="tel:{PHONE_E164}">{PHONE_SHOW}</a> · Email: <a class="font-semibold text-orange break-words" href="mailto:{EMAIL}">{EMAIL}</a>',
        ],
        "cta2": ("Chat on WhatsApp", WA),
    },
    "form": {
        "title": "Send me a message",
        "sub": "Three quick steps. I reply within one business day.",
        "submit": "Send message",
        "steps": [
            {"label": "Topic", "fields": [
                {"type": "select", "name": "service", "label": "What can I help with?", "req": True, "placeholder": "Select a service",
                 "options": SERVICES + [OTHER]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Message", "fields": [
                {"type": "textarea", "name": "details", "label": "Your message", "req": True, "placeholder": "What does your business do, and what do you want to grow?"},
                {"type": "radio", "name": "reply", "label": "Best way to reply", "options": ["WhatsApp", "Phone call", "Email"]},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

url = SITE + "/contact"
PAGE["graph"] = [
    {"@type": "ContactPage", "@id": url + "#webpage", "url": url, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#person"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/og.jpg", "width": 1200, "height": 630}},
    {"@type": "Person", "@id": SITE + "/#person", "name": "Sushant Rana", "email": EMAIL, "telephone": PHONE_E164,
     "address": {"@type": "PostalAddress", "addressLocality": "Chandigarh", "addressCountry": "IN"},
     "contactPoint": {"@type": "ContactPoint", "contactType": "sales", "telephone": PHONE_E164, "email": EMAIL, "availableLanguage": ["en", "hi"]}},
    {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"}, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ]},
]

PAGE["sections"] = [
    L.hero(PAGE),
    ways,
    where,
    L.section_bg('<section class="section" aria-label="Book a strategy call">' + booking_teaser + "</section>"),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready when", "you are"), "p": "Send a message, book a call or just say hello on WhatsApp.",
               "btn": "Send me a message", "note": "Reply within one business day · Chandigarh, India"}),
]
