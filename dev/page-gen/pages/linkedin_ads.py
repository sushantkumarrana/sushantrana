# LinkedIn Ads Services. Copy: 04_LinkedIn_Ads_Services.docx
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free LinkedIn Ads consultation"


def bar(w, tone="bg-ink/10", h="h-2"):
    return f'<span class="block {h} {w} rounded-full {tone}"></span>'


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def chips(items):
    return '<div class="flex flex-wrap gap-1.5">' + "".join(
        f'<span class="rounded-full border border-orange/30 bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange">{E(t)}</span>' for t in items) + "</div>"


def li_post(media, cta="Learn more", head="Your offer for decision makers"):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            '<div class="flex items-center gap-2.5 px-4 py-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-lg bg-ink text-[10px] font-extrabold text-white">YC</span>'
            '<span class="grid"><span class="text-xs font-bold text-ink">Your company</span><span class="text-[10px] text-muted">Promoted</span></span></div>'
            f'<div class="grid gap-1.5 px-4 pb-3" aria-hidden="true">{bar("w-full")}{bar("w-2/3")}</div>{media}'
            '<div class="flex items-center justify-between gap-3 border-t border-[var(--color-line)] bg-[#fff7f3] px-4 py-3">'
            f'<span class="text-xs font-bold text-ink">{E(head)}</span>'
            f'<span class="shrink-0 rounded-full border border-ink px-3 py-1 text-[11px] font-bold text-ink">{E(cta)}</span></div></div>')


IMG = f'<div class="grad-ink-orange grid aspect-video place-items-center text-white">{svg("image", "h-10 w-10", 1.5)}</div>'

# --------------------------------------------------- 01 basics: live job title demo

audience_box = figure("Who sees your ad", ["Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type the job title of your ideal buyer</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("users", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="role" placeholder="operations manager" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Job title to preview"/></span></label>'
    f'<div class="mt-3">{chips(["Job title", "Company", "Industry", "Company size", "Seniority", "Skills"])}</div>'
    f'<div class="mt-4">{li_post(IMG)}</div>'
    + note('<strong class="font-semibold text-ink">Shown in the feed of every</strong> <span data-mirror-out="role"></span> in the industries and company sizes you pick.')))

# --------------------------------------------------- 03 ad types

carousel = ('<div class="grid grid-cols-3 gap-2 px-4 pb-4">' + "".join(
    f'<div class="overflow-hidden rounded-xl border border-[var(--color-line)]"><div class="grad-ink-orange grid aspect-square place-items-center text-white">{svg(ic, "h-6 w-6")}</div>'
    f'<p class="p-2 text-[10px] font-bold text-ink">{n}</p></div>' for n, ic in [("Benefit one", "target"), ("Benefit two", "chart"), ("Benefit three", "shield")]) + "</div>")

lead_gen = figure("Lead Gen Form", ["Example"], (
    '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><p class="text-xs font-bold text-ink">Your company</p>'
    '<p class="mt-1 text-sm font-extrabold text-ink">Get the free guide</p><div class="mt-3 grid gap-2">' + "".join(
        f'<div class="flex items-center justify-between gap-3 rounded-xl border border-[var(--color-line)] px-3 py-2"><span class="grid"><span class="text-[10px] font-semibold uppercase tracking-wide text-muted">{lab}</span>'
        f'<span class="text-xs font-semibold text-ink">{val}</span></span><span class="shrink-0 rounded-full bg-orange/10 px-2 py-0.5 text-[10px] font-bold text-orange">Prefilled</span></div>'
        for lab, val in [("Full name", "Their name"), ("Job title", "Their role"), ("Company", "Their company"), ("Work email", "Their email")])
    + '</div><span class="mt-3 block rounded-xl bg-orange py-2 text-center text-xs font-bold text-white">Submit</span></div>'
    + note("Filled in from their LinkedIn profile, so a busy professional enquires in one tap.", "check")))

message_ad = figure("Message ad", ["Example"], (
    '<div class="rounded-2xl border border-[var(--color-line)] bg-white"><div class="flex items-center gap-2.5 border-b border-[var(--color-line)] px-4 py-3">'
    '<span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange text-[10px] font-extrabold text-white">YC</span>'
    '<span class="grid"><span class="text-xs font-bold text-ink">Your company</span><span class="text-[10px] text-muted">Sponsored · Inbox</span></span></div>'
    f'<div class="p-4"><p class="text-sm font-semibold text-ink">Hi, a personal note for you</p><div class="mt-2 grid gap-1.5" aria-hidden="true">{bar("w-full")}{bar("w-5/6")}{bar("w-2/3")}</div>'
    '<span class="mt-4 inline-flex rounded-full bg-orange px-4 py-1.5 text-xs font-bold text-white">Accept the invite</span></div></div>'))

side_ad = figure("Text and dynamic ads", ["Example"], (
    '<div class="flex gap-3" aria-hidden="true"><div class="grid flex-1 gap-3">'
    + ('<div class="rounded-2xl border border-[var(--color-line)] p-3 opacity-60"><span class="flex items-center gap-2"><span class="h-6 w-6 rounded-full bg-ink/15"></span>'
       f'{bar("w-1/2", "bg-ink/15")}</span><span class="mt-2 block">{bar("w-full")}</span><span class="mt-1.5 block">{bar("w-3/4")}</span></div>') * 2
    + '</div><div class="w-24 shrink-0 rounded-2xl border border-orange/30 bg-orange/5 p-3 text-center"><span class="mx-auto block h-8 w-8 rounded-full bg-orange"></span>'
      '<p class="mt-2 text-[10px] font-bold leading-tight text-ink">Your small ad</p><p class="mt-1 text-[9px] text-muted">On the side of LinkedIn</p></div></div>'))

AD_TYPES = [
    {"key": "sponsored", "name": "Sponsored Content", "icon": "image", "what": "Single image or video ads that appear in the LinkedIn feed.", "best": "The most common and flexible format for reaching your audience.",
     "mock": figure("Sponsored Content", ["Example"], li_post(IMG))},
    {"key": "carousel", "name": "Carousel ads", "icon": "layers", "what": "Multiple swipeable cards in one ad.", "best": "Great for telling a story or showing several benefits or services.",
     "mock": figure("Carousel ad", ["Example"], li_post(carousel, "See more"))},
    {"key": "leadgen", "name": "Lead Gen Forms", "icon": "file", "what": "Forms that fill in automatically with the person's LinkedIn details. This makes it very easy for busy professionals to enquire.", "best": "Lifts your lead numbers.",
     "mock": lead_gen},
    {"key": "message", "name": "Message ads", "icon": "pen", "what": "Ads delivered straight to the LinkedIn inbox of your target audience.", "best": "Useful for direct, personal offers and invites.",
     "mock": message_ad},
    {"key": "text", "name": "Text and dynamic ads", "icon": "click", "what": "Smaller ads that appear on the side of LinkedIn.", "best": "A low cost way to stay visible to your audience.",
     "mock": side_ad},
]

# --------------------------------------------------- 04 targeting builder

TARGETING = [
    ("job", "Job title and function", "Reach people by their exact role, such as founder, marketing head or operations manager.", ["Founder", "Marketing head", "Operations manager"]),
    ("company", "Company and industry", "Target specific companies or whole industries that match your best clients.", ["Named companies", "Industries like your best clients"]),
    ("size", "Company size", "Focus on the size of business you serve best, from small firms to large enterprises.", ["Small firms", "Growing companies", "Large enterprises"]),
    ("seniority", "Seniority and skills", "Reach senior decision makers and people with the skills that show they need what you offer.", ["Senior decision makers", "Skills that show the need"]),
]
t_btns = "".join(
    f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="border-orange bg-orange text-white" data-off="border-[var(--color-line)] bg-white text-ink hover:border-orange" '
    f'class="rounded-2xl border px-3 py-2.5 text-left text-xs font-bold transition {"border-orange bg-orange text-white" if i == 0 else "border-[var(--color-line)] bg-white text-ink hover:border-orange"}">{E(n)}</button>'
    for i, (k, n, _, _) in enumerate(TARGETING))
t_panels = "".join(
    f'<div data-panel="{k}"{HID if i else ""} class="mt-4"><p class="text-[10px] font-bold uppercase tracking-wider text-muted">Example audience layer</p>'
    f'<div class="mt-2.5">{chips(ex)}</div><p class="mt-3 text-sm text-body"><strong class="font-semibold text-ink">{E(n)}.</strong> {E(w)}</p></div>'
    for i, (k, n, w, ex) in enumerate(TARGETING))
targeting_box = ('<div data-tabs="true">' + figure("Audience builder", ["Example"], (
    f'<div class="grid grid-cols-2 gap-2">{t_btns}</div>{t_panels}'
    + note("Every layer narrows the audience until only the people who can say yes are left.", "users"))) + "</div>")

# --------------------------------------------------- 07 honest advice: fit check

fit_box = L.leak_check(
    "Is LinkedIn right for you?", "Tick everything that is true for your business.",
    [("I sell to other businesses", "LinkedIn is built for reaching business buyers."),
     ("One new client is worth a large amount to me", "Then a higher cost per lead can still give a strong return."),
     ("I know the job titles of the people who buy from me", "That is exactly how LinkedIn lets you target."),
     ("My budget can cover a higher cost per click", "LinkedIn needs more budget than Facebook or Google to gather enough data."),
     ("I want to reach candidates with specific skills", "LinkedIn also works well for recruitment and hiring campaigns.")],
    ("Nothing ticked yet. LinkedIn may not be the best fit, and on the call I will tell you honestly which platform suits you better.",
     "LinkedIn could work for you. Let us check your deal value and budget together on the call.",
     "LinkedIn looks like a strong fit. The next step is the right offer for the right person."),
    CTA, "Fit signs ticked")

GET = [
    {"icon": "target", "h3": "Ideal customer research", "p": "A clear picture of exactly who your ideal buyer is, so we target the right people from the start."},
    {"icon": "users", "h3": "Audience build", "p": "Tight, accurate audiences using LinkedIn's professional targeting, so your budget is not wasted on the wrong people."},
    {"icon": "pen", "h3": "Offer and copywriting", "p": "A strong offer and a clear message, because on LinkedIn the right offer to the right person is what drives leads."},
    {"icon": "file", "h3": "Lead Gen Form setup", "p": "Forms that fill in from the person's profile, so busy professionals can enquire in seconds."},
    {"icon": "sliders", "h3": "Tracking and weekly optimization", "p": "Conversion tracking on leads and lead quality, with audiences, offers and formats improved every week."},
    {"icon": "chart", "h3": "Clear monthly reports", "p": "Plain language reports on spend, leads, cost per lead and results, plus updates on anything important."},
]

FAQ = [
    ("What are LinkedIn Ads?", "LinkedIn Ads are paid ads shown to professionals on LinkedIn. Because people share their real job details, you can target buyers by their role, company and industry, which is ideal for B2B."),
    ("Are LinkedIn Ads good for B2B?", "Yes. LinkedIn is the best platform for B2B, because you can reach the exact decision makers who make buying choices, which you cannot do as precisely anywhere else."),
    ("Why are LinkedIn Ads more expensive than other platforms?", "You are paying to reach high value professionals in a business setting. The cost per lead is higher, but the lead quality is often much higher too, so the return can still be strong."),
    ("How much budget do I need for LinkedIn Ads?", "LinkedIn needs a higher budget than Facebook or Google to gather enough data. On our call I will give you an honest view of the budget you need to see real results."),
    ("What is a Lead Gen Form?", "A Lead Gen Form is a LinkedIn ad form that fills in automatically with the person's professional details. It makes enquiring quick and easy, which brings you more leads."),
    ("Can you target specific job titles and companies?", "Yes. I can target by job title, function, seniority, company, industry and company size, so your ads reach exactly the right people."),
    ("How soon will I see leads?", "You can start getting leads in the first couple of weeks. Because B2B buying takes longer, I focus on lead quality and steady results rather than instant volume."),
    ("Are LinkedIn Ads good for small businesses?", "They can be, if you sell to other businesses and your average deal is valuable. For low value or B2C products, other platforms are usually a better fit, and I will tell you honestly."),
    ("Do you create the ad creatives and copy?", "Yes. I write the copy, craft the offer and guide the creatives so your ads speak clearly to busy professionals."),
    ("Can LinkedIn Ads help with hiring?", "Yes. LinkedIn is excellent for reaching candidates with specific skills and roles, so it works well for recruitment and hiring campaigns."),
    ("What is Sponsored Content?", "Sponsored Content is an ad that appears directly in the LinkedIn feed as a single image, video or carousel. It is the most common and flexible LinkedIn ad format."),
    ("How do you measure success on LinkedIn Ads?", "I track leads, cost per lead and lead quality using conversion tracking, and I focus on the leads that actually turn into real business for you."),
    ("Can you run LinkedIn Ads for clients outside India?", "Yes. I work with clients in the US, Canada and other countries and can target any professional audience you want to reach."),
    ("What reports will I get?", "You get clear monthly reports in plain language showing spend, leads, cost per lead and results, plus updates on anything important."),
    ("How do I get started?", "Just book a free LinkedIn Ads consultation using the button on this page. We will talk about your ideal client and I will show you how LinkedIn can bring you quality leads."),
]

RELATED = [
    ("Performance marketing", "/services/performance-marketing/"),
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("YouTube Ads", "/services/youtube-ads/"),
    ("Lead generation", None),
    ("Landing pages", "/services/landing-pages/"),
]

PAGE = {
    "path": "/services/linkedin-ads/",
    "slug": "linkedin-ads",
    "form_name": "linkedin_ads",
    "service": "LinkedIn Ads",
    "service_name": "LinkedIn Ads management",
    "thanks_what": "LinkedIn Ads consultation",
    "category": "B2B advertising",
    "service_desc": "LinkedIn Ads management for B2B lead generation covering Sponsored Content, carousel ads, Lead Gen Forms, message ads and text ads, with job title, company, industry, company size and seniority targeting, conversion tracking, weekly optimization and monthly reporting.",
    "audience": "B2B companies that sell to other businesses",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What LinkedIn Ads management includes",
    "offers": GET,
    "title": "LinkedIn Ads Services for B2B Leads | Sushant Rana",
    "og_title": "LinkedIn Ads Services for B2B Leads",
    "og_alt": "LinkedIn Ads services for B2B leads by Sushant Rana",
    "desc": "LinkedIn Ads services that reach decision makers and bring high quality B2B leads. Precise targeting, lead gen forms, full tracking. Book a consultation.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("LinkedIn Ads", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("LinkedIn Ads", "questions, answered"),
            "body": ["Cost, targeting, lead quality and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "LinkedIn Ads for B2B",
        "h1": ("LinkedIn Ads services that bring you", "high quality B2B leads"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I run LinkedIn Ads that reach the right professionals and bring you high quality B2B leads. Do you sell to other businesses and want to reach the decision makers who can actually say yes? LinkedIn is the best place to do that, and we can help.',
            "LinkedIn is not the cheapest platform, but for the right business it brings some of the most valuable leads you can get. We run LinkedIn Ads for B2B companies across India, the US and Canada.",
        ],
        "cta2": ("See ad types", "#types"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free LinkedIn Ads consultation",
        "sub": "Tell me about your business and your ideal client, and I will come to the call with a plan.",
        "submit": "Request my consultation",
        "steps": [
            {"label": "Ads", "fields": [
                {"type": "radio", "name": "sell_to", "label": "Who do you sell to?", "req": True,
                 "options": ["Other businesses", "Consumers", "Both"]},
                {"type": "radio", "name": "running", "label": "Have you run LinkedIn Ads before?",
                 "options": ["Yes, running now", "Tried before", "Never"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Buyers", "fields": [
                {"type": "text", "name": "job_titles", "label": "Job titles you want to reach", "req": True, "placeholder": "Founders, HR heads, operations managers..."},
                {"type": "checkbox", "name": "ad_types", "label": "Ad types you are interested in",
                 "options": ["Sponsored Content", "Lead Gen Forms", "Message ads", "Carousel", "Hiring campaigns", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, your typical client, what a new client is worth..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Sponsored Content", "Lead Gen Forms", "Message ads", "Carousel ads", "Job title targeting", "Decision makers", "B2B leads"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What LinkedIn Ads are and", "why they are different"),
             "body": ["LinkedIn Ads are paid ads shown to professionals on the LinkedIn platform. What makes LinkedIn special is that people list their real job title, company, industry and skills, so you can target buyers by exactly what they do for work.",
                      "This is something no other platform can match. If your ideal customer is a specific type of business owner, manager or decision maker, LinkedIn lets you put your message right in front of them."],
             "bullets": ["Target by real job title, company and industry", "Reach the people who approve budgets", "Built for B2B buying"],
             "cta": CTA, "visual": audience_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why LinkedIn Ads are", "perfect for B2B"),
                      "body": ["When you sell to other businesses, LinkedIn gives you something no other platform does: the buyer's real professional details."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "users", "h3": "You reach real decision makers", "p": "You can target the exact people who approve budgets and make buying decisions, instead of hoping your message reaches them."},
                          {"icon": "target", "h3": "Precise professional targeting", "p": "Target by job title, company, industry, company size and seniority. This level of business targeting is unique to LinkedIn."},
                          {"icon": "shield", "h3": "Higher quality leads", "p": "The leads you get from LinkedIn are often more serious and better qualified, because they come from a professional setting."},
                          {"icon": "wallet", "h3": "Great for high value deals", "p": "If one new client is worth a large amount to you, LinkedIn is often the smartest place to spend your ad budget."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "Ad types", "h2": ("The LinkedIn ad types", "I run for you"),
                           "body": ["Each format does a different job, from the feed to the inbox. I pick the ones that fit your offer and your buyer. Pick one to see what it looks like."],
                           "items": AD_TYPES})),
    L.split({"id": "targeting", "pill": "Targeting", "h2": ("How I target the right people", "on LinkedIn"),
             "body": ["The power of LinkedIn is in its targeting. I build a clear picture of your ideal customer and reach them using the options below. Pick one to see how each layer narrows your audience."],
             "bullets": ["Job title and function", "Company and industry", "Company size", "Seniority and skills"],
             "visual": targeting_box}, dark=True, flip=True),
    L.split({"id": "honest", "pill": "Honest advice", "h2": ("Why LinkedIn costs more but", "can still be worth it"),
             "body": ["LinkedIn clicks and leads cost more than most other platforms. Many people see this and stop. That is a mistake for the right business.",
                      "The reason is simple. If one new client is worth a large amount to you, then paying more for a well targeted lead still gives you a strong return. I will always give you honest advice on whether LinkedIn is the right fit for your business and your budget."],
             "visual": fit_box}),
    L.crm_section("LinkedIn Ads", CTA),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My LinkedIn Ads", "process"),
                   "body": ["Five clear stages, from defining your ideal buyer to lowering your cost per lead. Pick a stage to follow along."],
                   "steps": [
                       {"h3": "Goals and ideal customer", "short": "Goals", "p": "I learn your business and define exactly who your ideal buyer is, so we target the right people from the start.", "points": ["Business and goals", "Ideal buyer defined", "Deal value understood"]},
                       {"h3": "Audience build", "short": "Audience", "p": "I build tight, accurate audiences using LinkedIn's professional targeting, so your budget is not wasted on the wrong people.", "points": ["Job titles and functions", "Companies and industries", "Size and seniority"]},
                       {"h3": "Offer and creative", "short": "Offer", "p": "I craft a strong offer and clear message, because on LinkedIn the right offer to the right person is what drives leads.", "points": ["Offer shaped", "Copy written", "Creatives guided"]},
                       {"h3": "Launch and test", "short": "Test", "p": "I launch your campaigns and test audiences, offers and formats to find what brings the best leads.", "points": ["Campaigns live", "Audiences and offers tested", "Formats compared"]},
                       {"h3": "Optimize and report", "short": "Optimize", "p": "I improve the account, lower your cost per lead over time and send you clear reports in plain language.", "points": ["Cost per lead lowered", "Lead quality tracked", "Plain language reports"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my LinkedIn Ads service"),
                  "body": ["You get a complete, done for you LinkedIn Ads service built for B2B lead generation, and you always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free consultation", "h3": "Want to reach decision makers on LinkedIn?",
                                       "p": "Let me learn about your business and your ideal client and show you how LinkedIn Ads can bring you high quality B2B leads. No pressure at all.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for LinkedIn Ads"),
                  "body": ["The person who plans your ads is the person you talk to, and success is measured in clients won, not clicks."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the person who plans and runs your ads, with fast replies and clear answers."},
                      {"h3": "Focus on lead quality, not just volume", "p": "I care about bringing you leads that actually turn into clients, not just cheap clicks."},
                      {"h3": "Honest reporting", "p": "I report on real results in plain language, so you always know what your budget is doing."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I run", "LinkedIn Ads for"),
                     "body": "B2B service providers, software and SaaS companies, consultants, recruitment and staffing firms, and businesses that sell high value products. If you sell to other businesses, LinkedIn can be a strong channel for you.",
                     "chips": [("B2B service providers", None), ("Software and SaaS", None), ("Consultants", None),
                               ("Recruitment and staffing", None), ("High value products", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "LinkedIn Ads"),
                     "body": "LinkedIn often works best as part of a wider paid ads plan, with a landing page built for the offer.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to win more", "B2B clients?"),
               "p": "Let us talk about your ideal customer and build a LinkedIn plan that brings you serious, high quality leads.",
               "btn": CTA, "note": "No obligation · Free consultation"}),
]
