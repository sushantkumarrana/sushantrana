# Meta Ads Services (Facebook and Instagram). Copy: 03_Meta_Ads_Services.docx
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free Meta Ads strategy call"


def bar(w, tone="bg-ink/10", h="h-2"):
    return f'<span class="block {h} {w} rounded-full {tone}"></span>'


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def social_post(media, cta="Learn more", head="Your headline here", sub="Sponsored"):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            '<div class="flex items-center gap-2.5 px-4 py-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange text-[10px] font-extrabold text-white">YB</span>'
            f'<span class="grid"><span class="text-xs font-bold text-ink">Your business</span><span class="text-[10px] text-muted">{E(sub)}</span></span></div>'
            f'<div class="grid gap-1.5 px-4 pb-3" aria-hidden="true">{bar("w-full")}{bar("w-3/4")}</div>{media}'
            '<div class="flex items-center justify-between gap-3 border-t border-[var(--color-line)] bg-[#fff7f3] px-4 py-3">'
            f'<span class="grid"><span class="text-[10px] uppercase tracking-wider text-muted">yourbusiness.com</span><span class="text-xs font-bold text-ink">{E(head)}</span></span>'
            f'<span class="shrink-0 rounded-lg bg-ink px-3 py-1.5 text-[11px] font-bold text-white">{E(cta)}</span></div></div>')


IMG = f'<div class="grad-ink-orange grid aspect-video place-items-center text-white">{svg("image", "h-10 w-10", 1.5)}</div>'
VID = (f'<div class="relative grid aspect-video place-items-center bg-[#0a0a0a]"><span class="grid h-12 w-12 place-items-center rounded-full bg-orange text-white">{svg("play", "h-6 w-6")}</span>'
       '<span class="absolute bottom-3 left-3 rounded bg-black/55 px-2 py-0.5 text-[10px] font-bold text-white">0:15</span></div>')


def phone(screen):
    """Phone frame, same markup as the Shopify page's mobile mock."""
    return ('<div class="flex justify-center"><div class="w-[clamp(124px,38vw,206px)] shrink-0 [container-type:inline-size]"><div class="relative">'
            '<span aria-hidden="true" class="absolute -left-[1.2cqw] top-[17cqw] h-[7cqw] w-[1.4cqw] rounded-l-full bg-[#2b2b2e]"></span>'
            '<span aria-hidden="true" class="absolute -right-[1.2cqw] top-[34cqw] h-[16cqw] w-[1.4cqw] rounded-r-full bg-[#2b2b2e]"></span>'
            '<div class="relative rounded-[16cqw] p-[1.1cqw] shadow-[0_30px_60px_-25px_rgba(0,0,0,0.65)] bg-[linear-gradient(150deg,#6f6f74_0%,#2f2f33_28%,#17171a_60%,#4a4a4f_100%)]"><div class="rounded-[15cqw] bg-black p-[1.4cqw]">'
            f'<div class="relative aspect-[9/19.5] overflow-hidden rounded-[13.5cqw] bg-white">{screen}</div></div></div></div></div></div>')


# --------------------------------------------------- 01 basics: live audience demo

TARGETS = ["Age", "Location", "Interests", "Behaviour", "Past actions", "Lookalikes"]
audience_box = figure("Who sees your ad", ["Live demo"], (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Describe your ideal customer</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("users", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="aud" placeholder="homeowners who love interior design" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="Ideal customer to preview"/></span></label>'
    '<div class="mt-3 flex flex-wrap gap-1.5">' + "".join(
        f'<span class="rounded-full border border-orange/30 bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange">{t}</span>' for t in TARGETS)
    + '</div><div class="mt-4">' + social_post(IMG) + '</div>'
    + note('<strong class="font-semibold text-ink">Shown to:</strong> <span data-mirror-out="aud"></span>, on Facebook and Instagram, from one ad manager.', "target")))

# --------------------------------------------------- 03 placements (phone mocks)

feed_screen = (
    '<div class="flex items-center justify-between border-b border-[var(--color-line)] px-3 pb-2 pt-6"><span class="text-[10px] font-extrabold text-ink">Feed</span>'
    f'{bar("w-10", "bg-ink/15")}</div><div class="p-2"><div class="flex items-center gap-1.5"><span class="h-5 w-5 rounded-full bg-orange"></span>'
    '<span class="grid"><span class="text-[9px] font-bold leading-tight text-ink">Your business</span><span class="text-[8px] leading-tight text-muted">Sponsored</span></span></div>'
    f'<div class="grad-ink-orange mt-2 grid aspect-square place-items-center rounded-lg text-white">{svg("image", "h-8 w-8", 1.5)}</div>'
    '<div class="mt-2 flex items-center justify-between rounded-md bg-[#fff7f3] px-2 py-1.5"><span class="text-[8px] font-bold text-ink">Your offer</span>'
    '<span class="rounded bg-ink px-1.5 py-0.5 text-[8px] font-bold text-white">Shop now</span></div>'
    f'<div class="mt-3 grid gap-1.5 opacity-60" aria-hidden="true"><span class="flex items-center gap-1.5"><span class="h-5 w-5 rounded-full bg-ink/15"></span>{bar("w-1/2", "bg-ink/15")}</span>'
    '<span class="block aspect-video rounded-lg bg-ink/10"></span></div></div>')

story_screen = (
    '<div class="grad-ink-orange absolute inset-0"></div><div class="relative flex h-full flex-col justify-between p-3 pt-6 text-white">'
    '<div><div class="grid grid-cols-3 gap-1" aria-hidden="true"><span class="h-0.5 rounded-full bg-white"></span><span class="h-0.5 rounded-full bg-white/50"></span><span class="h-0.5 rounded-full bg-white/50"></span></div>'
    '<p class="mt-2 flex items-center gap-1.5 text-[9px] font-bold"><span class="h-4 w-4 rounded-full bg-white"></span>Your business · Sponsored</p></div>'
    f'<span class="mx-auto grid h-10 w-10 place-items-center rounded-full bg-white/10 text-white">{svg("play", "h-5 w-5")}</span>'
    '<div class="text-center"><p class="text-[11px] font-extrabold leading-tight">Short, punchy video</p>'
    '<span class="mt-2 inline-flex rounded-full bg-white px-3 py-1 text-[9px] font-bold text-ink">Learn more</span></div></div>')

explore_screen = (
    '<div class="border-b border-[var(--color-line)] px-3 pb-2 pt-6"><span class="flex items-center gap-1.5 rounded-full bg-ink/[0.06] px-2 py-1 text-[8px] text-muted">'
    f'{svg("search", "h-3 w-3")}Search</span></div><div class="grid grid-cols-2 gap-1.5 p-2">'
    + '<span class="block aspect-square rounded-md bg-ink/10"></span>' * 2
    + f'<span class="grad-ink-orange relative grid aspect-square place-items-center rounded-md text-white">{svg("bag", "h-5 w-5")}'
      '<span class="absolute left-2 top-2 rounded bg-white/90 px-1 text-[8px] font-bold text-ink">Sponsored</span></span>'
    + '<span class="block aspect-square rounded-md bg-ink/10"></span>' * 3 + '</div>')

PLACEMENTS = [
    {"key": "feeds", "name": "Facebook and Instagram feeds", "icon": "layers",
     "what": "Your ads appear as people scroll through their main feed, which is where most attention and action happens.",
     "mock": figure("Feed placement", ["Example"], phone(feed_screen))},
    {"key": "stories", "name": "Stories and Reels", "icon": "play",
     "what": "Full screen ads between stories and reels. These are perfect for short, punchy video that grabs attention fast.",
     "mock": figure("Stories and Reels placement", ["Example"], phone(story_screen))},
    {"key": "explore", "name": "Explore and Marketplace", "icon": "search",
     "what": "Extra placements that help you reach people while they browse and shop, giving you more chances to be seen.",
     "mock": figure("Explore and Marketplace placement", ["Example"], phone(explore_screen))},
]

# --------------------------------------------------- 04 ad types

carousel = ('<div class="grid grid-cols-3 gap-2 px-4 pb-4">' + "".join(
    f'<div class="overflow-hidden rounded-xl border border-[var(--color-line)]"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-6 w-6")}</div>'
    f'<p class="p-2 text-[10px] font-bold text-ink">{n}</p></div>' for n in ["Product one", "Product two", "Product three"]) + "</div>")

lead_form = figure("Lead form ad", ["Example"], (
    '<div class="rounded-2xl border border-[var(--color-line)] bg-white p-4"><p class="text-xs font-bold text-ink">Your business</p>'
    '<p class="mt-1 text-sm font-extrabold text-ink">Get a free quote</p><div class="mt-3 grid gap-2">' + "".join(
        f'<div class="rounded-xl border border-[var(--color-line)] px-3 py-2"><p class="text-[10px] font-semibold uppercase tracking-wide text-muted">{lab}</p>{bar("mt-1.5 w-1/2", "bg-ink/15")}</div>'
        for lab in ["Full name", "Email", "Phone number"])
    + '</div><span class="mt-3 block rounded-xl bg-orange py-2 text-center text-xs font-bold text-white">Submit</span></div>'
    + note("Filled in right inside Facebook or Instagram, without leaving the app.", "check")))

catalog = figure("Catalog ad", ["Example"], (
    '<p class="text-[11px] font-bold text-ink">From your store catalog</p><div class="mt-3 grid grid-cols-3 gap-3">' + "".join(
        f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-7 w-7")}</div>'
        f'<div class="p-3"><p class="text-[11px] font-bold leading-tight text-ink">{n}</p><p class="text-[10px] text-muted">Shop now</p></div></div>'
        for n in ["Product one", "Product two", "Product three"]) + '</div><p class="mt-3 text-xs text-body">The right products, picked from your catalog for each shopper.</p>'))

retarget = figure("Retargeting", ["Example"], (
    '<ol class="grid list-none gap-3">' + "".join(
        f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3.5"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
        f'<span class="text-sm font-semibold text-ink">{t}</span></li>'
        for i, t in enumerate(["Someone visits your site or engages with your page", "They leave without buying", "They see your ad on Facebook or Instagram", "They come back and buy"], 1))
    + "</ol>"))

AD_TYPES = [
    {"key": "image", "name": "Image ads", "icon": "image", "what": "Simple, clean single image ads that deliver a strong message fast.", "best": "Great for offers and clear promotions.",
     "mock": figure("Image ad", ["Example"], social_post(IMG))},
    {"key": "video", "name": "Video ads", "icon": "play", "what": "Short videos that tell your story, show your product and build trust.", "best": "Video is one of the strongest formats on Meta.",
     "mock": figure("Video ad", ["Example"], social_post(VID, "Watch more"))},
    {"key": "carousel", "name": "Carousel ads", "icon": "layers", "what": "Multiple images or products in one swipeable ad.", "best": "Perfect for showing a range of products or steps.",
     "mock": figure("Carousel ad", ["Example"], social_post(carousel, "Shop now"))},
    {"key": "leadform", "name": "Lead form ads", "icon": "file", "what": "Ads that collect a name, email and phone number right inside Facebook or Instagram, without the person leaving the app.", "best": "Excellent for service businesses.",
     "mock": lead_form},
    {"key": "catalog", "name": "Catalog and collection ads", "icon": "bag", "what": "Product ads pulled from your store catalog that show the right products to the right shoppers.", "best": "Ideal for ecommerce.",
     "mock": catalog},
    {"key": "retargeting", "name": "Retargeting ads", "icon": "repeat", "what": "Ads that follow up with people who visited your site or engaged with your page but did not buy.", "best": "One of the cheapest ways to win back sales.",
     "mock": retarget},
]

# --------------------------------------------------- 07 the secret: creative check

leak_box = L.leak_check(
    "Meta Ads check", "Tick everything that sounds like your ads today.",
    [("I mostly boost posts", "Boosting is a limited option that mostly buys likes, not leads or sales."),
     ("My ads look much like everyone else's", "A boring ad fails even with perfect targeting."),
     ("I have never tested different versions", "Testing many versions is how the winners are found."),
     ("I am not sure the Meta Pixel is set up right", "Without it, Meta cannot learn who your buyers are."),
     ("I am not sure who my ads are reaching", "Wrong targeting sends your money to people who will never buy.")],
    ("Nothing ticked yet. A free strategy call still checks the creatives, targeting and tracking behind your results.",
     "A problem or two. Weak creatives, wrong targeting and broken tracking are the usual reasons Meta Ads do not work.",
     "Your ads are very likely losing money. I would fix the creative and the tracking first."),
    CTA, "Problems ticked")

GET = [
    {"icon": "users", "h3": "Audience research", "p": "I plan who to target using interests, behaviour, location and lookalike audiences based on your best customers."},
    {"icon": "pen", "h3": "Ad copy and creative direction", "p": "Clear, benefit driven copy, and a plan for exactly what your images and videos should show."},
    {"icon": "zap", "h3": "Meta Pixel and event setup", "p": "The Meta Pixel and conversion events set up so every lead and sale is counted correctly."},
    {"icon": "layers", "h3": "Campaign build", "p": "Campaigns built with the right placements and ad types for your goal, whether that is leads or sales."},
    {"icon": "sliders", "h3": "Weekly optimization and retargeting", "p": "Audiences and creatives tested and improved every week, with retargeting to win back people who did not buy."},
    {"icon": "chart", "h3": "Clear monthly reports", "p": "Plain language reports showing spend, leads, sales and return, plus updates whenever something important changes."},
]

FAQ = [
    ("What are Meta Ads?", "Meta Ads are the paid ads that run on Facebook and Instagram. Both platforms share one ad system called Meta, so a single strategy can reach people across both."),
    ("What is the difference between boosting a post and running proper Meta Ads?", "Boosting is a simple, limited option that mostly buys likes. Proper Meta Ads use full targeting, tracking and creative testing to bring real leads and sales. The results are very different."),
    ("How much budget do I need for Facebook and Instagram ads?", "It depends on your goals and your industry. Some clients start small and scale up once we see profit. On our call I will suggest a realistic starting budget for your market."),
    ("How soon will I see results?", "Meta Ads can start bringing leads within the first few days. The first two to four weeks are used to test and learn, so stable results usually build from the first month."),
    ("What is the Meta Pixel and why do I need it?", "The Meta Pixel is a small piece of code on your website that tracks what visitors do. It lets Meta learn who your buyers are and lets you retarget people, which greatly improves your results."),
    ("Can Meta Ads work for ecommerce?", "Yes, very well. I use catalog ads, retargeting and smart audiences to bring ready to buy shoppers to your products and track every sale."),
    ("Can Meta Ads get me leads for a service business?", "Yes. Lead form ads and strong landing pages can bring a steady flow of enquiries for service businesses, often at a low cost per lead."),
    ("Do you create the images and videos?", "I guide and direct your creatives and write the copy. I plan exactly what the images and videos should show, and I can work with your designer or with simple assets you already have."),
    ("What is retargeting on Meta?", "Retargeting shows ads to people who already visited your site or engaged with your page but did not buy. It is one of the cheapest and most profitable types of Meta Ads."),
    ("Why did my previous Facebook ads not work?", "Usually it is one of three reasons: weak creatives, wrong targeting or broken tracking. I check all three, fix the real problem and rebuild the account the right way."),
    ("Which is better for my business, Facebook or Instagram?", "Most businesses do best using both, since they share one system. I let the data decide where your budget performs best, rather than guessing."),
    ("Do you write the ad copy?", "Yes. I write clear, benefit driven copy and test different versions to find the ones that bring the most action."),
    ("How do you target the right audience?", "I use interests, behaviour, location and lookalike audiences based on your best customers. Then I test and refine until we find the audiences that convert."),
    ("Can you run lead form ads?", "Yes. Lead form ads collect contact details right inside Facebook and Instagram, which makes it easy for people to enquire and easy for you to follow up."),
    ("What reports do I get?", "You get clear monthly reports in plain language showing spend, leads, sales and return, plus updates whenever something important changes."),
    ("How do I get started?", "Just book a free Meta Ads strategy call using the button on this page. We will talk about your goals and I will show you how Facebook and Instagram ads can grow your business."),
]

RELATED = [
    ("Performance marketing", "/services/performance-marketing/"),
    ("Google Ads", "/services/google-ads/"),
    ("LinkedIn Ads", "/services/linkedin-ads/"),
    ("YouTube Ads", "/services/youtube-ads/"),
    ("Remarketing", None),
    ("Landing pages", "/services/landing-pages/"),
]

PAGE = {
    "path": "/services/meta-ads/",
    "slug": "meta-ads", "thanks": "paid-ads",
    "form_name": "meta_ads",
    "service": "Meta Ads",
    "service_name": "Meta Ads management",
    "thanks_what": "Meta Ads strategy call",
    "category": "Social media advertising",
    "service_desc": "Meta Ads management for Facebook and Instagram covering feeds, stories, reels, image, video, carousel, lead form, catalog and retargeting ads, with audience research, creative direction, Meta Pixel setup, weekly optimization and monthly reporting.",
    "audience": "Businesses that need leads or online sales",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What Meta Ads management includes",
    "offers": GET,
    "title": "Meta Ads Services, Facebook & Instagram | Sushant Rana",
    "og_title": "Meta Ads Services for Facebook and Instagram",
    "og_alt": "Meta Ads services for Facebook and Instagram by Sushant Rana",
    "desc": "Meta Ads services on Facebook and Instagram that turn scrolls into leads and sales. Smart targeting, strong creatives, full tracking. Book a free call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Meta Ads", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Meta Ads", "questions, answered"),
            "body": ["Budgets, the Meta Pixel, creatives and reporting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Facebook and Instagram ads",
        "h1": ("Meta Ads services that turn Facebook and Instagram", "into a sales machine"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I run Meta Ads that stop the scroll, reach the right people and turn attention into real customers. Want more leads and sales from Facebook and Instagram? That is what we help businesses do every day.',
            "Facebook and Instagram run on the same ad system called Meta, so we manage both from one place with one clear strategy. We run Meta Ads for businesses across India, the UAE, the US and Canada, and I treat your budget like it is my own money.",
        ],
        "cta2": ("See client work", "#work"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free Meta Ads strategy call",
        "sub": "Tell me about your business and I will come to the call with ideas for your ads.",
        "submit": "Request my strategy call",
        "steps": [
            {"label": "Ads", "fields": [
                {"type": "radio", "name": "running", "label": "Are you running Meta Ads now?", "req": True,
                 "options": ["Yes, running ads", "Only boosting posts", "Never run them"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website or Instagram page", "placeholder": "yourwebsite.com"},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["More leads or enquiries", "More online sales", "Win back site visitors", "Brand growth", "Not sure yet"]},
                {"type": "checkbox", "name": "ad_types", "label": "Ad types you are interested in",
                 "options": ["Image", "Video and reels", "Carousel", "Lead forms", "Catalog", "Retargeting", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, who buys it, what has not worked so far..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Facebook ads", "Instagram ads", "Reels", "Stories", "Lead form ads", "Carousel ads", "Catalog ads", "Retargeting", "Meta Pixel"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What Meta Ads are", "and why they matter"),
             "body": ["Meta Ads are the paid ads you see on Facebook and Instagram. Both platforms are owned by Meta and share one powerful ad manager, so a single strategy can reach billions of active users.",
                      "The real power of Meta is its targeting. You can show your ads to people based on their age, location, interests, behaviour and past actions. This means your message reaches the people most likely to buy, not random viewers."],
             "bullets": ["Facebook and Instagram from one ad manager", "Targeting by age, location, interests and behaviour", "Reach people who already know you"],
             "cta": CTA, "visual": audience_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why Meta Ads work so well", "for business growth"),
                      "body": ["When Meta Ads are set up correctly, they can bring a steady flow of leads and sales at a low cost. Here is why so many businesses rely on them."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "users", "h3": "Huge active audience", "p": "Billions of people use Facebook and Instagram every day. Your customers are already there, spending hours scrolling, which gives you plenty of chances to reach them."},
                          {"icon": "target", "h3": "Powerful, precise targeting", "p": "I can target people by interests, behaviour, location and life events, and even reach people who look like your best customers. This keeps your money focused on the right audience."},
                          {"icon": "chart", "h3": "Great for leads and sales", "p": "Meta Ads work for both service businesses that need leads and online stores that need sales. The same system can do both when the strategy is right."},
                          {"icon": "play", "h3": "Visual and video friendly", "p": "Images, videos, reels and carousels grab attention fast. This makes Meta perfect for showing off your product and building trust quickly."},
                      ]})
        + L.tabs_showcase({"id": "placements", "pill": "Placements", "h2": ("Where your Meta Ads", "will appear"),
                           "body": ["Meta shows your ads in many places across Facebook and Instagram. I choose the best placements for your goals and let the system spend where it performs best. Pick one to see it on a phone."],
                           "items": PLACEMENTS})),
    L.tabs_showcase({"id": "types", "pill": "Ad types", "h2": ("The Meta ad types", "I run for you"),
                     "body": ["Different goals need different ad formats. I plan and build the right ones for your business. Pick one to see what it looks like."],
                     "items": AD_TYPES}),
    L.projects_section(["ourknots", "4s", "yalla", "warriors", "touch"], ("Meta Ads accounts", "we run right now"),
                       "Real businesses in the UAE, India, the USA and Canada. Pick one to see what we run for them and what it delivers."),
    L.split({"id": "secret", "pill": "The secret", "h2": ("Why the creative is the most", "important part on Meta"),
             "body": ["On Meta, the image or video you use matters more than almost anything else. A boring ad will fail even with perfect targeting, while a strong scroll stopping ad can bring cheap leads and sales.",
                      "That is why I put so much care into your creatives and copy. I plan a clear message, guide the images and videos, and test many versions to find the ones that truly work. This is often the difference between ads that lose money and ads that make it."],
             "bullets": ["A clear message planned first", "Images and videos guided, not left to chance", "Many versions tested to find the winners"],
             "visual": leak_box}),
    L.crm_section("Meta Ads", CTA),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My Meta Ads", "management process"),
                   "body": ["Five clear stages, from understanding your goals to scaling the ads that make money. Pick a stage to follow along."],
                   "steps": [
                       {"h3": "Goals and audit", "short": "Audit", "p": "I learn your business, your goals and your current results, so I know what a good outcome looks like for you.", "points": ["Business and goals", "Current results reviewed", "What good looks like"]},
                       {"h3": "Audience and creative strategy", "short": "Strategy", "p": "I plan who to target and what to say, then map out the images and videos that will stop the scroll.", "points": ["Who to target", "What to say", "Images and videos mapped"]},
                       {"h3": "Pixel and tracking setup", "short": "Tracking", "p": "I set up the Meta Pixel and conversion tracking so every lead and sale is counted correctly. This is the part most people get wrong.", "points": ["Meta Pixel installed", "Conversion events", "Leads and sales counted"]},
                       {"h3": "Launch and test", "short": "Test", "p": "I launch your campaigns and test different audiences and creatives to quickly find the winners.", "points": ["Campaigns live", "Audiences tested", "Creatives tested"]},
                       {"h3": "Optimize and scale", "short": "Scale", "p": "I improve the account every week and carefully scale the ads that bring profit, so your results keep climbing.", "points": ["Weekly improvements", "Profitable ads scaled", "Steady growth"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my Meta Ads service"),
                  "body": ["You get a complete, done for you service for Facebook and Instagram ads. I handle the strategy, the setup, the testing and the reporting, and you always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free strategy call", "h3": "Want more leads and sales from Facebook and Instagram?",
                                       "p": "Let me look at your business and your goals and show you how Meta Ads can bring you real customers. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for Meta Ads"),
                  "body": ["The person who plans your ads is the person you talk to, and the work starts with the creative, not just the settings."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the same person who plans and runs your ads. Fast replies and clear answers every time."},
                      {"h3": "Creative first approach", "p": "I focus on strong creatives and messaging, which is what really drives results on Meta, instead of only playing with settings."},
                      {"h3": "Honest reporting", "p": "I report on leads, sales and profit in plain language, so you always know what your money is doing."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I run", "Meta Ads for"),
                     "body": "Ecommerce brands, coaches and course creators, healthcare and dental clinics, real estate, local services, restaurants and B2C businesses. If your customers use Facebook or Instagram, and almost everyone does, Meta Ads can work for you.",
                     "chips": [("Ecommerce brands", None), ("Coaches and course creators", "/industries/education/"), ("Healthcare", None),
                               ("Dental clinics", "/industries/dental/"), ("Real estate", "/industries/real-estate/"), ("Local services", None),
                               ("Restaurants", None), ("B2C businesses", None)]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "Meta Ads"),
                     "body": "Meta Ads are one part of a full paid ads plan. These are the channels and pages that work alongside them.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Let us grow your business on", "Facebook and Instagram"),
               "p": "You have seen how I work. The next step is a simple chat about your goals to see if we are the right fit.",
               "btn": CTA, "note": "No obligation · Free strategy call"}),
]
