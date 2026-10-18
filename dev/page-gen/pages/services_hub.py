# Services hub (/services/). Links every indexable service page (the ones in
# sitemap.xml), the industry pages and the case studies. Card copy is cut down
# from each linked page's own meta description; case figures are the ones those
# case studies publish. Keep this list in step with sitemap.xml.
import json
import re

E, svg = L.E, L.svg
SITE = L.SITE
URL = SITE + "/services/"
CTA = "Book your free strategy call"

_cat = open("api/catalog.php").read()
SERVICES = json.loads(re.search(r"const ALL_SERVICES = (\[.*?\]);", _cat).group(1))
OTHER = re.search(r'const OTHER_SERVICE = "([^"]+)"', _cat).group(1)

GROUPS = [
    {"id": "seo", "pill": "SEO", "h2": ("SEO services that get you", "found on Google"),
     "body": ["Rank for the searches your customers already make, from a first audit to technical fixes, content and links."],
     "cards": [
         ("search", "SEO audit", "/services/seo-audit/", "A free audit that shows why your site is not ranking, with a clear and honest action plan."),
         ("gauge", "Technical SEO", "/services/technical-seo/", "Fix the crawl and index problems, slow pages and Core Web Vitals that hold your rankings back."),
         ("file", "On-page SEO", "/services/on-page-seo/", "Titles, headings, content and internal links that help Google understand and rank each page."),
         ("pin", "Local SEO", "/services/local-seo/", "Rank in Google Maps and the local pack, so nearby customers find you first."),
         ("target", "Google Business Profile", "/services/google-business-profile/", "An optimized profile that ranks in the map and brings more calls from local customers."),
         ("bag", "Ecommerce SEO", "/services/ecommerce-seo/", "Product and category pages that rank for buying searches, so shoppers find your store for free."),
         ("layers", "Enterprise SEO", "/services/enterprise-seo/", "Template level fixes and a clear strategy for large websites with thousands of pages."),
         ("repeat", "Link building", "/services/link-building/", "Real, relevant backlinks that grow your authority, built with white hat methods only."),
     ]},
    {"id": "ads", "pill": "Paid ads", "h2": ("Paid ads that bring", "leads and sales"),
     "body": ["Ads on the platforms your buyers use, judged on leads and sales rather than clicks."],
     "cards": [
         ("chart", "Performance marketing", "/services/performance-marketing/", "One paid ads plan across Google, Meta, LinkedIn and more, built to turn ad spend into sales and leads."),
         ("search", "Google Ads", "/services/google-ads/", "Search, Shopping, Performance Max and remarketing that bring ready to buy customers."),
         ("bag", "Google Shopping Ads", "/services/google-shopping-ads/", "Your products, prices and images in front of shoppers, with feed setup and full tracking."),
         ("image", "Meta Ads", "/services/meta-ads/", "Facebook and Instagram ads with smart targeting, strong creatives and full tracking."),
         ("play", "YouTube Ads", "/services/youtube-ads/", "Video ads that grow your brand and bring real sales, not just views."),
         ("users", "LinkedIn Ads", "/services/linkedin-ads/", "Reach decision makers and get B2B leads with precise targeting and lead gen forms."),
         ("wallet", "Amazon Ads", "/services/amazon-ads/", "Sponsored Products, Brands and Display that push your products up and lower your ACoS."),
     ]},
    {"id": "crm", "pill": "CRM and automation", "h2": ("CRM and automation so", "no lead is lost"),
     "body": ["Every lead saved, followed up and tracked to a sale, without your team chasing spreadsheets."],
     "cards": [
         ("sliders", "Zoho CRM", "/services/zoho-crm/", "Set up, customize and automate Zoho CRM, with pipelines, migration and training."),
         ("layers", "HubSpot CRM", "/services/hubspot-crm/", "Pipelines, workflows and migration so marketing and sales work together in HubSpot."),
         ("zap", "GoHighLevel", "/services/gohighlevel/", "Your CRM, funnels, and email and SMS follow up set up to run on autopilot."),
         ("mail", "Email automation", "/services/email-automation/", "Email flows that nurture leads and recover lost sales, with the right message at the right time."),
         ("repeat", "Sales funnel setup", "/services/sales-funnel-setup/", "Pages, copy, automation and tracking that turn strangers into paying customers."),
     ]},
    {"id": "web", "pill": "Websites", "h2": ("Websites built to", "turn visits into enquiries"),
     "body": ["Fast sites and landing pages with tracking in place from day one, and care after launch."],
     "cards": [
         ("pen", "WordPress development", "/services/wordpress-development/", "Fast, SEO ready WordPress websites that are easy to manage yourself, WooCommerce included."),
         ("bag", "Shopify store development", "/services/shopify-store-development/", "New stores, redesigns, themes and migrations, built to convert and handed over in 4 to 6 weeks."),
         ("click", "Landing pages", "/services/landing-pages/", "Landing pages that turn ad clicks into leads and sales, with strong copy and full tracking."),
         ("shield", "Website maintenance", "/services/website-maintenance/", "Backups, updates, security and fixes for WordPress, Shopify, Wix, Webflow and custom sites."),
     ]},
]

CASES = [
    ("chart", "OurKnots on Meta Ads", "/case-studies/ourknots/", "Meta ROAS from 0.72x to 5.13x, and ₹3.84L of store sales in September 2026."),
    ("chart", "OurKnots on Google Ads", "/case-studies/ourknots-google-ads/", "Google Ads ROAS from 0.71x in February 2026 to 14.05x in September 2026, on the same budget."),
    ("search", "Yalla Renovation on Google Ads", "/case-studies/yalla-renovation/", "2,287 tracked form submissions over 24 months in Dubai, from Search and Performance Max."),
    ("users", "4S Study Abroad on Meta Ads", "/case-studies/4s-study-abroad/", "7,514 student enquiries at AED 8.79 each over 24 months, from lead forms and WhatsApp."),
    ("users", "4S Study Abroad on Google Ads", "/case-studies/4s-study-abroad-google-ads/", "8,859 student enquiries at ₹278 each, with cost per enquiry cut 59.6% after a tough 2023."),
    ("layers", "All Meta Ads case studies", "/case-studies/meta-ads/", "OurKnots, 4S Study Abroad and more Meta Ads lead generation accounts, side by side."),
    ("layers", "All Google Ads case studies", "/case-studies/google-ads/", "OurKnots, Yalla Renovation and more Google Ads lead generation accounts, side by side."),
]

INDUSTRIES = [("Dental clinics", "/industries/dental/"), ("Law firms", "/industries/legal-firms/"), ("Real estate", "/industries/real-estate/"),
              ("Education", "/industries/education/"), ("Auto repair", "/industries/auto-repair/")]

FAQ = [
    ("Which service should I start with?", "It depends on where your leads are leaking. If people cannot find you, start with SEO or Google Ads. If they find you but do not enquire, fix the website or landing page first. If enquiries come in but are not followed up, start with the CRM. On a free strategy call I look at your setup and tell you where to start."),
    ("Can you run several of these services together?", "Yes. Most clients use more than one, for example ads with a landing page, or ads connected to a CRM. One person owning the whole system means nothing falls between two vendors."),
    ("Will I work with you directly?", "Yes. You talk to the same person who plans and runs the work, from the first call to the results."),
    ("Do you work with businesses outside India?", "Yes. I work from Chandigarh, India, with clients across India, the UAE, the USA, Canada and Australia, on Google Meet and WhatsApp."),
    ("Is the strategy call free?", "Yes. The strategy call is free, takes 30 minutes on Google Meet, and comes with no obligation to work together."),
]


def link_cards(items, cols="sm:grid-cols-2 lg:grid-cols-4"):
    """icon_cards markup with the card title as the link."""
    per = 4 if "lg:grid-cols-4" in cols else 3
    return (f'<ul class="wrap mt-14 grid list-none gap-5 {cols}">' + "".join(
        f'<li class="flex"><div data-reveal="true" class="flex w-full"{L.d(i, per=per)}><article class="card w-full p-7">'
        f'<span class="grid h-12 w-12 place-items-center rounded-2xl bg-orange/10 text-orange">{svg(ic, "h-6 w-6")}</span>'
        f'<h3 class="mt-5 text-xl font-extrabold text-ink"><a class="transition hover:text-orange" href="{href}">{E(name)}</a></h3>'
        f'<p class="mt-2.5 text-body">{E(p)}</p></article></div></li>'
        for i, (ic, name, href, p) in enumerate(items)) + "</ul>")


def group(g):
    return (f'<section class="section" id="{g["id"]}" aria-labelledby="{g["id"]}-heading">{L.centered_head(g)}'
            f'{link_cards(g["cards"])}</section>')


JUMP = " · ".join(f'<a class="font-semibold text-orange" href="#{g["id"]}">{E(g["pill"])}</a>' for g in GROUPS)

PAGE = {
    "path": "/services/",
    "slug": "services",
    "form_name": "services",
    "service": OTHER,
    "wa_label": "services page",
    "enquiry": "service",
    "service_name": "Services",
    "title": "Services: Ads, SEO, CRM and Websites | Sushant Rana",
    "og_title": "Services by Sushant Rana",
    "og_alt": "Services by Sushant Rana, business growth consultant",
    "desc": "All of Sushant Rana's services in one place: SEO, Google and Meta Ads, CRM and automation, and websites, for businesses in India, the UAE, the USA and beyond.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", None)],
    "related": [],
    "hero": {
        "pill": "Services",
        "h1": ("Ads, SEO, CRM and websites,", "run as one system"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, a business growth consultant in Chandigarh, India. I run SEO, paid ads, CRM and automation, and websites for service businesses and online stores in India, the UAE, the USA, Canada and Australia, and you work with me directly.',
            "Pick a service below to see how I work, or book a free 30 minute strategy call and I will tell you where to start.",
            f"Jump to: {JUMP}",
        ],
        "cta2": ("See the case studies", "#cases"),
    },
    "form": {
        "title": "Tell me what you need",
        "sub": "Three quick steps. I reply within one business day.",
        "submit": "Send my enquiry",
        "steps": [
            {"label": "Need", "fields": [
                {"type": "select", "name": "service", "label": "Which service do you need?", "req": True, "placeholder": "Select a service",
                 "options": SERVICES + [OTHER]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "textarea", "name": "details", "label": "What do you want to grow?", "req": True, "placeholder": "What your business does, and what you want more of"},
                {"type": "radio", "name": "reply", "label": "Best way to reply", "options": ["WhatsApp", "Phone call", "Email"]},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": L.SOURCES},
            ]},
        ],
    },
}

PAGE["graph"] = [
    {"@type": "CollectionPage", "@id": URL + "#webpage", "url": URL, "name": PAGE["title"], "description": PAGE["desc"], "inLanguage": "en",
     "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": SITE + "/#person"}, "mainEntity": {"@id": URL + "#services"},
     "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/og.jpg", "width": 1200, "height": 630}},
    {"@type": "ItemList", "@id": URL + "#services", "name": "Services by Sushant Rana", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "url": SITE + href}
        for i, (_, name, href, _) in enumerate(c for g in GROUPS for c in g["cards"])]},
    L.faq_schema(URL, FAQ),
]

PAGE["sections"] = [
    L.hero(PAGE),
    group(GROUPS[0]),
    L.section_bg(group(GROUPS[1])),
    group(GROUPS[2]),
    L.section_bg(group(GROUPS[3])),
    L.dark_cards({"id": "how", "pill": "How I work", "h2": ("One person behind", "every service"),
                  "body": ["Whichever service you start with, the way I work stays the same."],
                  "cards": [
                      {"h3": "You work directly with me", "p": "You talk to the same person who plans and runs the work. Fast replies and clear answers every time."},
                      {"h3": "Ads connected to your CRM", "p": "Qualified leads and sales flow back into Google and Meta as conversions, so the ads go after buyers, not form fills."},
                      {"h3": "Honest reporting", "p": "Reports on leads, sales and cost per result in plain language, so you always know what your money is doing."},
                  ]}),
    ('<section class="section" id="cases" aria-labelledby="cases-heading">'
     + L.centered_head({"id": "cases", "pill": "Case studies", "h2": ("Real results from", "client accounts"),
                        "body": ["Numbers taken from the ad accounts themselves, month by month."]})
     + link_cards(CASES, "sm:grid-cols-2 lg:grid-cols-3") + "</section>"),
    L.chips_section({"id": "industries", "h2": ("Industries I", "work with"),
                     "body": "Pages for the industries I work with most, with the services that fit each one.", "chips": INDUSTRIES}),
    L.faq({"pill": "Common questions", "h2": ("Questions about", "my services"), "body": [], "items": FAQ}),
    L.contact({"h2": ("Not sure where", "to start?"), "p": "Tell me about your business and I will suggest the service that fits, or a mix of them.",
               "btn": CTA, "note": "No obligation · Free 30 minute strategy call"}),
]
