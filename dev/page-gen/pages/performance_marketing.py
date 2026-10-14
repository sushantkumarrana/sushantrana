# Performance Marketing Services (pillar for every paid ads page). Copy: 01_Performance_Marketing_Services.docx
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free performance marketing strategy call"


def bar(w, tone="bg-ink/10", h="h-2"):
    return f'<span class="block {h} {w} rounded-full {tone}"></span>'


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def go(label, href):
    return (f'<a href="{href}" class="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-orange transition hover:text-ink">'
            f'{E(label)}{svg("chev", "h-4 w-4")}</a>')


def toggle(opts, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-3 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(lab)}</button>'
        for i, (k, lab) in enumerate(opts)) + "</div>"


def tag(text, hot=False):
    tone = "bg-orange/10 text-orange" if hot else "bg-ink/[0.06] text-muted"
    return f'<span class="shrink-0 rounded-full px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide {tone}">{E(text)}</span>'


def rows(items):
    return '<ul class="grid list-none gap-2.5">' + "".join(
        f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
        f'<span class="grid"><span class="text-sm font-bold text-ink">{E(a)}</span><span class="text-xs text-muted">{E(b)}</span></span>{tag(t, hot)}</li>'
        for a, b, t, hot in items) + "</ul>"


# --------------------------------------------------- 01 basics: old school vs performance

basics_box = '<div data-tabs="true">' + figure("Where your budget goes", ["Example"], (
    toggle([("old", "Old school ads"), ("perf", "Performance marketing")], on=1)
    + '<p class="mt-4 text-[10px] font-bold uppercase tracking-wider text-muted">This month&#x27;s ads</p>'
    + '<div class="mt-2.5" data-panel="old" hidden="">' + rows([
        ("Ad one", "Shown to a wide audience", "Result unknown", False),
        ("Ad two", "Shown to a wide audience", "Result unknown", False),
        ("Ad three", "Shown to a wide audience", "Result unknown", False)])
    + note('<strong class="font-semibold text-ink">A big amount spent,</strong> and you simply hope it works.')
    + '</div><div class="mt-2.5" data-panel="perf">' + rows([
        ("Ad one", "Brought a sale", "More budget", True),
        ("Keyword two", "Brought leads and calls", "Keep running", True),
        ("Audience three", "Clicks, but no sales", "Budget cut", False)])
    + note('<strong class="font-semibold text-ink">You see which ad, keyword and audience brought a sale,</strong> so the budget moves to what works.')
    + "</div>")) + "</div>"

# --------------------------------------------------- 03 channels: one mock per platform


def search_ad():
    return ('<div class="rounded-2xl border border-[var(--color-line)] p-4"><p class="text-[11px] font-bold text-ink">Sponsored</p>'
            '<p class="text-[11px] text-muted">yourbusiness.com</p><p class="svc-serp-title mt-1 text-base font-bold">Your Service In Your City | Call Today</p>'
            '<p class="mt-1 text-xs text-body">Your offer, the reason to choose you and one clear next step.</p>'
            '<div class="mt-3 flex flex-wrap gap-2 text-[11px] font-semibold text-orange"><span>Get a quote</span><span>Our services</span><span>Contact us</span></div></div>')


def social_post(who, sub, media, cta, head="Your headline here"):
    return ('<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
            '<div class="flex items-center gap-2.5 px-4 py-3"><span class="grid h-8 w-8 shrink-0 place-items-center rounded-full bg-orange text-[10px] font-extrabold text-white">YB</span>'
            f'<span class="grid"><span class="text-xs font-bold text-ink">{E(who)}</span><span class="text-[10px] text-muted">{E(sub)}</span></span></div>'
            f'<div class="grid gap-1.5 px-4 pb-3" aria-hidden="true">{bar("w-full")}{bar("w-3/4")}</div>{media}'
            '<div class="flex items-center justify-between gap-3 border-t border-[var(--color-line)] bg-[#fff7f3] px-4 py-3">'
            f'<span class="grid"><span class="text-[10px] uppercase tracking-wider text-muted">yourbusiness.com</span><span class="text-xs font-bold text-ink">{E(head)}</span></span>'
            f'<span class="shrink-0 rounded-lg bg-ink px-3 py-1.5 text-[11px] font-bold text-white">{E(cta)}</span></div></div>')


IMG = f'<div class="grad-ink-orange grid aspect-video place-items-center text-white">{svg("image", "h-10 w-10", 1.5)}</div>'


def video(label="Skip ad ▸"):
    return ('<div class="relative grid aspect-video place-items-center overflow-hidden rounded-2xl bg-[#0a0a0a]">'
            f'<span class="grid h-12 w-12 place-items-center rounded-full bg-orange text-white">{svg("play", "h-6 w-6")}</span>'
            '<span class="absolute bottom-3 left-3 rounded bg-white/90 px-2 py-0.5 text-[10px] font-bold text-ink">Ad</span>'
            f'<span class="absolute bottom-3 right-3 rounded bg-black/55 px-3 py-1 text-[11px] font-bold text-white">{E(label)}</span></div>')


def product_cards(store="Your store"):
    return ('<div class="grid grid-cols-3 gap-3">' + "".join(
        f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="grid aspect-square place-items-center bg-[#fff7f3] text-orange">{svg("bag", "h-7 w-7")}</div>'
        f'<div class="p-3"><p class="text-[11px] font-bold leading-tight text-ink">{n}</p><p class="mt-1 text-xs font-extrabold text-ink">{pr}</p><p class="text-[10px] text-muted">{store}</p></div></div>'
        for n, pr in [("Product one", "₹1,499"), ("Product two", "₹899"), ("Product three", "₹2,250")]) + "</div>")


amazon_results = ('<div class="grid gap-2.5">' + "".join(
    f'<div class="flex items-center gap-3 rounded-2xl border p-3 {"border-orange/30 bg-orange/5" if i == 0 else "border-[var(--color-line)] opacity-60"}">'
    f'<span class="grid h-12 w-12 shrink-0 place-items-center rounded-xl bg-[#fff7f3] text-orange">{svg("bag", "h-6 w-6")}</span>'
    + (f'<span class="grid gap-1"><span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored</span><span class="text-sm font-bold text-ink">Your product</span>'
       '<span class="text-xs text-body">Top of the Amazon results</span></span>' if i == 0 else
       f'<span class="grid w-full gap-1.5" aria-hidden="true">{bar("w-1/2", "bg-ink/15", "h-3")}{bar("w-3/4")}</span>')
    + "</div>" for i in range(3)) + "</div>")

CHANNELS = [
    ("google", "Google Ads", "search", "/services/google-ads/",
     "Search, Display, Performance Max and remarketing campaigns that capture people at the exact moment they are searching for what you sell.",
     "Great for high intent leads and sales.", figure("Google search ad", ["Example"], search_ad())),
    ("meta", "Meta Ads (Facebook and Instagram)", "image", "/services/meta-ads/",
     "Scroll stopping image and video ads that reach your ideal customer on Facebook and Instagram.",
     "Strong for brand growth, lead generation and ecommerce sales.", figure("Facebook and Instagram feed", ["Example"], social_post("Your business", "Sponsored", IMG, "Learn more"))),
    ("linkedin", "LinkedIn Ads", "users", "/services/linkedin-ads/",
     "The best place to reach decision makers, business owners and specific job roles.",
     "Ideal for B2B services, high value products and hiring campaigns.", figure("LinkedIn feed", ["Example"], social_post("Your company", "Promoted", IMG, "Download", "Your offer for decision makers"))),
    ("youtube", "YouTube Ads", "play", "/services/youtube-ads/",
     "Video ads that tell your story and build trust while people watch content they love.",
     "A smart way to grow awareness and bring warm buyers back to your site.", figure("YouTube video ad", ["Example"], video() + '<p class="mt-3 text-xs text-body">Your story told in seconds, then a reason to visit your site.</p>')),
    ("amazon", "Amazon Ads", "bag", "/services/amazon-ads/",
     "Sponsored Products and Sponsored Brands that push your listings to the top of Amazon search results, so more shoppers find and buy your products.",
     "Built for sellers who want more orders from Amazon.", figure("Amazon search results", ["Example"], amazon_results)),
    ("shopping", "Google Shopping Ads", "layers", "/services/google-shopping-ads/",
     "Product ads with images, prices and reviews that appear right inside Google search.",
     "Perfect for online stores that want ready to buy shoppers.", figure("Google Shopping", ["Example"], '<p class="mb-3 text-[11px] font-bold text-ink">Sponsored products</p>' + product_cards())),
]

channels_section = L.tabs_showcase({
    "id": "types", "pill": "Channels I run", "h2": ("The paid advertising channels", "I manage for you"),
    "body": ["Every business needs a different mix of platforms. Some do best on Google, some on social media, some on marketplaces. I plan the right mix for your goals and your budget, and I handle each channel end to end. Pick one to see what it looks like."],
    "items": [{"key": k, "name": n, "icon": ic, "what": w, "best": b, "mock": m + go(f"See my {n.split(' (')[0]} service", h)}
              for k, n, ic, h, w, b, m in CHANNELS]})

# --------------------------------------------------- 08 tools + spend check

TOOLS = ["Google Ads", "Meta Ads Manager", "Google Tag Manager", "Google Analytics 4", "Meta Pixel"]
tool_chips = ('<ul class="mt-7 flex list-none flex-wrap gap-2.5">' + "".join(
    f'<li><span class="inline-flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2 font-[family-name:var(--font-display)] text-xs font-semibold text-ink">'
    f'{svg("check", "h-3.5 w-3.5 text-orange", 3)}{E(t)}</span></li>' for t in TOOLS) + "</ul>")

leak_box = L.leak_check(
    "Ad spend check", "Tick everything that sounds like your ads today.",
    [("I do not know my cost per lead or cost per sale", "Without these numbers you cannot tell if your ads are profitable."),
     ("I am not sure my conversion tracking works", "When tracking is broken, it is the first thing I fix."),
     ("I cannot tell which ad or keyword brought a sale", "So the budget cannot move to what works."),
     ("My ads send people to a normal website page", "A focused landing page converts far better."),
     ("My reports talk about clicks and likes, not sales", "Clicks are only the first step.")],
    ("Nothing ticked yet. A free strategy call still checks the parts that are hard to see from the dashboard.",
     "A leak or two. These are usually the first things I fix when I take over an account.",
     "Your budget is very likely leaking. Tracking and landing pages are where I would start."),
    CTA)

# --------------------------------------------------- content

GET = [
    {"icon": "search", "h3": "Keyword and audience research", "p": "Deep research into the exact keywords and audiences that will bring you buyers, plus a look at what your competitors are doing."},
    {"icon": "pen", "h3": "Ad copy and creative planning", "p": "I write the ad copy and plan the creatives, so your images and videos match the message."},
    {"icon": "layers", "h3": "Full campaign build", "p": "Campaigns built properly on the right platforms, with the budget split according to a clear plan."},
    {"icon": "phone", "h3": "Conversion and call tracking", "p": "Every form, call and purchase connected back to the ad that caused it, so we always know what is really working."},
    {"icon": "sliders", "h3": "Optimization, budget and A/B tests", "p": "Weekly optimization, budget management and A/B testing. New ads tested, weak keywords paused and budget moved to the winners."},
    {"icon": "chart", "h3": "Easy to read monthly reports", "p": "Clear reports in plain language that show what you spent and what you earned back."},
]

FAQ = [
    ("What is performance marketing?", "Performance marketing is paid advertising where you invest in real results such as leads, calls and sales, not just views or clicks. Every part of the campaign is tracked, so you can clearly see the return you are getting on your money."),
    ("How is performance marketing different from normal digital marketing?", "Normal marketing often focuses on awareness and reach. Performance marketing focuses on measurable actions that grow your revenue. In simple words, you pay for outcomes, and every rupee is tracked back to a result."),
    ("Which platforms do you run performance marketing campaigns on?", "I run campaigns on Google Ads, Meta Ads on Facebook and Instagram, LinkedIn Ads, YouTube Ads, Amazon Ads and Google Shopping. I choose the right mix based on your goals, your customers and your budget."),
    ("How much budget do I need to start?", "There is no single answer, because it depends on your industry and your goals. Some clients start small and scale up once we see profit. On our first call, I will suggest a realistic starting budget for your market so you never overspend."),
    ("How soon will I see results?", "Paid ads can start bringing traffic and leads within the first few days. That said, the first two to four weeks are used to gather data and improve the account. Real, stable results usually build from the first month onwards."),
    ("Do you only care about clicks or actual sales?", "I care about sales and leads, not just clicks. Clicks are only the first step. My job is to turn those clicks into real customers and to lower your cost per result over time."),
    ("What is return on ad spend and why does it matter?", "Return on ad spend, or ROAS, tells you how much revenue you earn for every rupee spent on ads. For example, a ROAS of five means you earned five rupees for every one rupee spent. It is one of the clearest ways to measure if your ads are profitable."),
    ("Can you fix my current ads that are not working?", "Yes. This is one of the most common requests I get. I will audit your account, find the leaks that are wasting money, and rebuild the parts that are holding you back. Often the tracking itself is broken, which I fix first."),
    ("Do you work with small businesses or only big brands?", "I work with both. Small and local businesses are welcome, and paid ads can work very well for them when set up carefully. I shape the plan around your size and your budget."),
    ("Will you handle both the strategy and the ad creatives?", "Yes. I plan the full strategy, write the ad copy and guide the creatives so your images and videos match the message. You get a complete service, not just campaign settings."),
    ("How do you track leads and sales from my campaigns?", "I set up proper conversion tracking using tools like Google Tag Manager, Google Analytics 4 and the Meta Pixel. This connects every form, call and purchase back to the ad that caused it, so we always know what is really working."),
    ("Do you provide reports and how often?", "Yes. You get clear monthly reports written in plain language, plus updates whenever something important changes. You will always understand what you spent and what you earned back."),
    ("Can you run ads for my ecommerce store?", "Yes. Ecommerce is a great fit for performance marketing. I use Google Shopping, Performance Max, Meta Ads and Amazon Ads to bring ready to buy shoppers to your products and track every sale."),
    ("Do you charge a fixed fee or a percentage of ad spend?", "It depends on the size and needs of your account. I will explain the options clearly on our call and pick the one that is fair for both of us. There are no hidden charges."),
    ("Is performance marketing better than SEO?", "They do different jobs. Paid ads bring fast results and instant traffic, while SEO builds free long term traffic over time. The best growth usually comes from using both together, and I can guide you on the right balance."),
    ("Do I need a landing page for my paid ads?", "In most cases, yes. A focused landing page converts far better than a normal website page. If your landing page is weak, I will point it out and help you improve it, because it directly affects your cost per lead."),
    ("Can you run campaigns for clients outside India?", "Yes. I work with clients in the US, Canada and other countries. Paid ad platforms are global, so I can manage your account from anywhere and target any market you want to reach."),
    ("What makes you different from a big agency?", "With me, you work directly with the person who builds and runs your ads. There is no junior team and no middleman. You get faster replies, honest reporting and more of your budget going into actual results."),
    ("How do I get started with you?", "Just book a free strategy call using the button on this page. We will talk about your business and your goals, and I will show you how paid ads can grow your leads and sales. No pressure at all."),
]

RELATED = [
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("LinkedIn Ads", "/services/linkedin-ads/"),
    ("YouTube Ads", "/services/youtube-ads/"),
    ("Amazon Ads", "/services/amazon-ads/"),
    ("Google Shopping Ads", "/services/google-shopping-ads/"),
    ("Remarketing", "/services/remarketing/"),
    ("Landing pages", "/services/landing-pages/"),
]

PAGE = {
    "path": "/services/performance-marketing/",
    "slug": "performance-marketing",
    "form_name": "performance_marketing",
    "service": "Performance Marketing",
    "service_name": "Performance marketing services",
    "thanks_what": "performance marketing strategy call",
    "category": "Performance marketing",
    "service_desc": "Performance marketing across Google Ads, Meta Ads, LinkedIn Ads, YouTube Ads, Amazon Ads and Google Shopping, with research, ad copy, creative planning, conversion and call tracking, weekly optimization and monthly reporting.",
    "audience": "Businesses that need leads or online sales",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What performance marketing services include",
    "offers": GET,
    "title": "Performance Marketing Services in India | Sushant Rana",
    "og_title": "Performance Marketing Services",
    "og_alt": "Performance marketing services by Sushant Rana",
    "desc": "Performance marketing services that turn ad spend into real sales and leads. Paid ads across Google, Meta, LinkedIn and more. Book a free strategy call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("Performance Marketing", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("Performance marketing", "questions, answered"),
            "body": ["Budgets, platforms, tracking and fees. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "Performance marketing",
        "h1": ("Performance marketing services that", "turn ad spend into real sales"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I plan, run and improve paid ad campaigns built around one clear goal, real business growth. Spending money on ads every month and still not getting enough leads or sales? That is the exact problem we solve. We do not chase likes and empty clicks. Every campaign is judged on the numbers that pay your bills, like qualified leads, sales and return on ad spend.',
            "Whether you are starting your first campaign or trying to rescue ads that have stopped working, we help you get more out of every rupee and every dollar you spend. We work with businesses across India, the UAE, the US and Canada, and I treat your ad budget like it is my own money.",
        ],
        "cta2": ("See client work", "#work"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free performance marketing strategy call",
        "sub": "Tell me about your business and your ads, and I will come to the call with a plan.",
        "submit": "Request my strategy call",
        "steps": [
            {"label": "Ads", "fields": [
                {"type": "radio", "name": "running", "label": "Are you running paid ads now?", "req": True,
                 "options": ["Yes, running now", "Paused or stopped", "Never run them"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
                {"type": "text", "name": "site", "label": "Website", "placeholder": "yourwebsite.com", "attrs": 'inputMode="url" autoComplete="url"'},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["More leads or enquiries", "More online sales", "More phone calls", "Lower cost per result", "Not sure yet"]},
                {"type": "checkbox", "name": "channels", "label": "Channels you are interested in",
                 "options": ["Google Ads", "Meta Ads", "LinkedIn Ads", "YouTube Ads", "Amazon Ads", "Google Shopping", "Not sure"]},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, where you sell it, what is not working today..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

crm = L.crm_section("Google and Meta", CTA, h2=("Your ads only work properly", "when your CRM is connected"),
                    body=["Google and Meta learn from whatever you tell them a conversion is. If the only signal is a form fill, they go and find you more form fills, including the fake numbers and the people who were only browsing.",
                          "So on every account we connect the ads to your CRM. Each lead is saved with where it came from, your sales team updates the lead status, and the qualified leads and sales flow back into Google and Meta as conversions, with their value. From then on the platforms go after buyers, not forms."])
crm = crm.replace("What Google and Meta learns from", "What Google and Meta learn from").replace("Google and Meta sees", "Google and Meta see")

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["Performance marketing", "Google Ads", "Meta Ads", "LinkedIn Ads", "YouTube Ads", "Amazon Ads", "Google Shopping", "Conversion tracking", "Return on ad spend"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What performance marketing", "really means"),
             "body": ["Performance marketing is a type of paid advertising where you only invest in actions that matter to your business. Instead of paying for a vague idea of brand awareness, you pay for measurable results such as clicks, leads, calls, sign ups and sales. Every part of the campaign is tracked, so you always know what you are getting for your money.",
                      "This is very different from old school advertising where you spend a big amount and simply hope it works. With performance marketing, I can see which ad, which keyword and which audience brought you a sale. Then I put more budget behind what works and cut what does not. That is how your results keep getting better month after month."],
             "bullets": ["Pay for clicks, leads, calls, sign ups and sales", "Every ad, keyword and audience tracked", "More budget behind what works, less behind what does not"],
             "cta": CTA, "visual": basics_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why performance marketing is", "worth your money"),
                      "body": ["Most business owners come to me because they want faster and clearer results than they get from other channels. Here is what performance marketing gives you when it is set up the right way."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "zap", "h3": "You get traffic fast", "p": "SEO is powerful, but it takes months to build. Paid ads can put your business in front of ready to buy customers within a day of going live. This makes it perfect for new launches, offers and businesses that need leads right now."},
                          {"icon": "target", "h3": "You reach the right people only", "p": "I can show your ads only to the people who are most likely to buy from you, based on their location, age, interests, job role and even the exact words they type into Google. You stop wasting money on the wrong audience."},
                          {"icon": "chart", "h3": "Everything is measurable", "p": "You will always know your cost per lead, your cost per sale and your return on ad spend. There is no guessing. This clear data helps us make smart decisions and grow your account with confidence."},
                          {"icon": "gauge", "h3": "It scales with your business", "p": "When a campaign is profitable, we can carefully increase the budget and get more of the same result. So as your business grows, your ads can grow with it without losing quality."},
                      ]})
        + channels_section),
    L.projects_section(["ourknots", "yalla", "warriors", "4s", "touch", "elixir"], ("Paid campaigns", "we run right now"),
                       "Real businesses in the UAE, the USA, Canada and India. Pick one to see what we run for them and what it delivers."),
    L.split({"id": "tools", "pill": "Behind the scenes", "h2": ("The tools I use to track", "and grow your results"),
             "body": ["Strong campaigns need strong tracking. I set up and use tools like Google Ads, Meta Ads Manager, Google Tag Manager, Google Analytics 4 and the Meta Pixel to follow every click and conversion. This lets me prove your results and keep improving them with real data, not guesswork.",
                      "Tracking is the part most people skip, and it is the reason so many accounts waste money. Tick what sounds like your ads to see where yours may be leaking."],
             "after": tool_chips, "visual": leak_box}),
    crm,
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My simple and proven", "performance marketing process"),
                   "body": ["Good ad results are not luck. They come from a clear process that I follow on every account. Here is how I take your campaign from an idea to a steady flow of leads and sales."],
                   "steps": [
                       {"h3": "Discovery and goal setting", "short": "Discovery", "p": "First I learn about your business, your customers, your profit margins and your goals. This tells me what a good result looks like for you, so every decision after this points in the right direction.", "points": ["Business and customers", "Profit margins", "What a good result looks like"]},
                       {"h3": "Research and strategy", "short": "Strategy", "p": "I study your market, your competitors and the exact keywords and audiences that will bring you buyers. Then I build a clear plan that shows which platforms to use and how the budget will be split.", "points": ["Market and competitors", "Keywords and audiences", "Platform and budget plan"]},
                       {"h3": "Campaign setup and tracking", "short": "Setup", "p": "I build your campaigns, write the ad copy, plan the creatives and set up proper conversion tracking. Tracking is the part most people skip, and it is the reason so many accounts waste money. I make sure every lead and sale is counted correctly.", "points": ["Campaigns and ad copy", "Creative plan", "Conversion tracking"]},
                       {"h3": "Launch and optimize", "short": "Optimize", "p": "Once live, I watch the numbers closely and improve the account every week. I test new ads, pause weak keywords, fix targeting and shift budget to the winners. This is where your results really start to climb.", "points": ["New ad tests", "Weak keywords paused", "Budget shifted to winners"]},
                       {"h3": "Report and scale", "short": "Scale", "p": "You get clear reports that show what you spent and what you earned back, in plain language. When a campaign is profitable, we scale it up in a safe and steady way.", "points": ["Plain language reports", "Spend versus return", "Safe, steady scaling"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included when", "you work with me"),
                  "body": ["You get a complete, done for you service. I handle the strategy, the setup, the daily work and the reporting, so you can focus on running your business.",
                           "You always have one person who knows your account inside out, and that person is me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free strategy call", "h3": "Ready to get more leads and sales from your ads?",
                                       "p": "Let us look at your business, your goals and your current ads together. I will show you where you are losing money and how we can fix it. There is no pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "over a big agency"),
                  "body": ["When you hire a large agency, your account is often handed to a junior team member while you speak to a salesperson. With me, you work directly with the person who actually builds and manages your campaigns. Nothing gets lost in the middle."],
                  "cards": [
                      {"h3": "You talk to the expert, not a middleman", "p": "Every strategy, every change and every report comes straight from me. You always get clear answers and fast replies."},
                      {"h3": "Your budget goes into ads, not overheads", "p": "A big agency has to cover big office costs. Working with me keeps your money focused on the ads and the results, which means better value for you."},
                      {"h3": "Real numbers, no fluff", "p": "I care about leads, sales and profit, not vanity metrics. My reports are simple and honest, and I will always tell you the truth about what is working."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Industries I run", "performance marketing for"),
                     "body": "I have run paid campaigns for many types of businesses, and I adjust my approach to fit each one. If your business depends on a steady flow of leads or online sales, performance marketing can work for you. If you are not sure, just book a call and I will give you an honest answer.",
                     "chips": [("Ecommerce brands", "/industries/ecommerce/"), ("Healthcare clinics", "/industries/healthcare/"), ("Dental clinics", "/industries/dental/"),
                               ("Real estate", "/industries/real-estate/"), ("Education and coaching", "/industries/education/"), ("Legal firms", "/industries/legal-firms/"),
                               ("Home services", None), ("B2B companies", "/industries/b2b-companies/"), ("Local service businesses", "/industries/local-businesses/")]}),
    L.chips_section({"id": "related", "h2": ("Every channel,", "one plan"),
                     "body": "Each platform has its own page with the detail of how I run it. Pick the one you want to know more about.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Let us grow your business", "together"),
               "p": "You have seen how I work and what I can do. The next step is a simple, friendly chat about your goals. Let us find out if we are the right fit.",
               "btn": CTA, "note": "No obligation · Free strategy call"}),
]
