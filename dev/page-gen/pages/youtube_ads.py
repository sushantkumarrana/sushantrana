# YouTube Ads Services. Copy: 05_YouTube_Ads_Services.docx
E, svg, figure, pill = L.E, L.svg, L.figure, L.pill
HID = ' hidden=""'

CTA = "Book your free YouTube Ads strategy call"


def bar(w, tone="bg-ink/10", h="h-2"):
    return f'<span class="block {h} {w} rounded-full {tone}"></span>'


def note(text, icon="target"):
    return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
            f'{svg(icon, "h-4 w-4 shrink-0 text-orange")}<span>{text}</span></p>')


def chips(items):
    return '<div class="flex flex-wrap gap-1.5">' + "".join(
        f'<span class="rounded-full border border-orange/30 bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange">{E(t)}</span>' for t in items) + "</div>"


def player(corner="Skip ad ▸", centre="", progress=None):
    prog = (f'<span class="absolute inset-x-0 bottom-0 h-1 bg-white/10"><span class="block h-1 bg-orange" style="width:{progress}%"></span></span>'
            if progress is not None else "")
    mid = centre or f'<span class="grid h-12 w-12 place-items-center rounded-full bg-orange text-white">{svg("play", "h-6 w-6")}</span>'
    return ('<div class="relative grid aspect-video place-items-center overflow-hidden rounded-2xl bg-[#0a0a0a]">'
            f'{mid}<span class="absolute bottom-3 left-3 rounded bg-white/90 px-2 py-0.5 text-[10px] font-bold text-ink">Ad</span>'
            f'<span class="absolute bottom-3 right-3 rounded bg-black/55 px-3 py-1 text-[11px] font-bold text-white">{E(corner)}</span>{prog}</div>')


def phone(screen):
    """Phone frame, same markup as the Shopify page's mobile mock."""
    return ('<div class="flex justify-center"><div class="w-[clamp(124px,38vw,206px)] shrink-0 [container-type:inline-size]"><div class="relative">'
            '<span aria-hidden="true" class="absolute -left-[1.2cqw] top-[17cqw] h-[7cqw] w-[1.4cqw] rounded-l-full bg-[#2b2b2e]"></span>'
            '<span aria-hidden="true" class="absolute -right-[1.2cqw] top-[34cqw] h-[16cqw] w-[1.4cqw] rounded-r-full bg-[#2b2b2e]"></span>'
            '<div class="relative rounded-[16cqw] p-[1.1cqw] shadow-[0_30px_60px_-25px_rgba(0,0,0,0.65)] bg-[linear-gradient(150deg,#6f6f74_0%,#2f2f33_28%,#17171a_60%,#4a4a4f_100%)]"><div class="rounded-[15cqw] bg-black p-[1.4cqw]">'
            f'<div class="relative aspect-[9/19.5] overflow-hidden rounded-[13.5cqw] bg-white">{screen}</div></div></div></div></div></div>')


def toggle(opts, on=0):
    return '<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">' + "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == on else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-3 py-2 text-xs font-bold transition {"bg-orange text-white" if i == on else "bg-white text-ink hover:text-orange"}">{E(lab)}</button>'
        for i, (k, lab) in enumerate(opts)) + "</div>"


def caption(text):
    return f'<span class="max-w-xs px-6 text-center font-[family-name:var(--font-display)] text-base font-extrabold text-white">{E(text)}</span>'


# --------------------------------------------------- 01 basics: the shape of a video ad

STAGES = [
    ("hook", "Hook", 15, "The first seconds", "Grab attention before the skip button appears."),
    ("story", "Story", 60, "Show and tell", "Show your product, your face and your story."),
    ("action", "Action", 100, "One next step", "Give one clear reason to visit your site."),
]
video_box = '<div data-tabs="true">' + figure("Inside a YouTube ad", ["Example"], (
    toggle([(k, lab) for k, lab, *_ in STAGES])
    + "".join(
        f'<div data-panel="{k}"{HID if i else ""} class="mt-4">{player("Skip ad ▸" if k == "hook" else "Ad", caption(big), pct)}'
        f'<p class="mt-3 text-sm text-body"><strong class="font-semibold text-ink">{E(lab)}.</strong> {E(small)}</p></div>'
        for i, (k, lab, pct, big, small) in enumerate(STAGES))
    + note("I guide the script so the video holds attention and drives action. A good message matters more than expensive production.", "pen"))) + "</div>"

# --------------------------------------------------- 03 formats

infeed = ('<div class="grid gap-2.5"><span class="flex items-center gap-2 rounded-full border border-[var(--color-line)] px-3 py-2 text-xs text-muted">'
          f'{svg("search", "h-3.5 w-3.5")}what your buyer searches</span>'
          + "".join(
              f'<div class="flex items-center gap-3 rounded-2xl border p-2 {"border-orange/30 bg-orange/5" if i == 0 else "border-[var(--color-line)] opacity-60"}">'
              + (f'<span class="grad-ink-orange grid h-12 w-24 shrink-0 place-items-center rounded-lg text-white">{svg("play", "h-5 w-5")}</span>'
                 '<span class="grid gap-0.5"><span class="text-sm font-bold text-ink">Your video title</span><span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored · Your channel</span></span>'
                 if i == 0 else
                 f'<span class="block h-12 w-24 shrink-0 rounded-lg bg-ink/10"></span><span class="grid w-full gap-1.5" aria-hidden="true">{bar("w-3/4", "bg-ink/15", "h-3")}{bar("w-1/2")}</span>')
              + "</div>" for i in range(3)) + "</div>")

shorts_screen = (
    '<div class="grad-ink-orange absolute inset-0"></div><div class="relative flex h-full flex-col justify-between p-3 pt-6 text-white">'
    '<p class="text-[9px] font-bold">Shorts</p>'
    f'<span class="mx-auto grid h-10 w-10 place-items-center rounded-full bg-white/10 text-white">{svg("play", "h-5 w-5")}</span>'
    '<div><p class="flex items-center gap-1.5 text-[9px] font-bold"><span class="h-4 w-4 rounded-full bg-white"></span>Your channel · Sponsored</p>'
    '<span class="mt-2 block rounded-full bg-white py-1 text-center text-[9px] font-bold text-ink">Learn more</span></div></div>')

FORMATS = [
    {"key": "skippable", "name": "Skippable in stream ads", "icon": "play",
     "what": "Ads that play before or during a video and can be skipped after a few seconds.", "best": "You mostly pay only when someone watches, so it is very cost effective.",
     "mock": figure("Skippable in stream ad", ["Example"], player("Skip ad ▸"))},
    {"key": "nonskip", "name": "Non skippable ads", "icon": "shield",
     "what": "Short ads that must be watched fully.", "best": "Best when you want to be sure your full message is seen.",
     "mock": figure("Non skippable ad", ["Example"], player("Plays in full"))},
    {"key": "bumper", "name": "Bumper ads", "icon": "zap",
     "what": "Six second ads that deliver a quick, punchy message.", "best": "Great for staying in people's minds and reinforcing your brand.",
     "mock": figure("Bumper ad", ["Example"], player("6 seconds", caption("One quick, memorable message")))},
    {"key": "infeed", "name": "In feed video ads", "icon": "search",
     "what": "Ads that appear in YouTube search results and next to related videos.", "best": "Perfect for reaching people who are actively looking.",
     "mock": figure("In feed video ad", ["Example"], infeed)},
    {"key": "shorts", "name": "Shorts ads", "icon": "layers",
     "what": "Ads that appear inside YouTube Shorts.", "best": "Short video is growing fast here, and attention is high.",
     "mock": figure("Shorts ad", ["Example"], phone(shorts_screen))},
]

# --------------------------------------------------- 04 targeting

steps_list = ('<ol class="grid list-none gap-2.5">' + "".join(
    f'<li class="flex items-center gap-3 rounded-2xl border border-[var(--color-line)] bg-white p-3"><span class="grid h-7 w-7 shrink-0 place-items-center rounded-full bg-orange font-[family-name:var(--font-display)] text-xs font-extrabold text-white">{i}</span>'
    f'<span class="text-sm font-semibold text-ink">{t}</span></li>'
    for i, t in enumerate(["Someone visits your website", "They leave without buying", "They see your video on YouTube", "They come back when they are ready"], 1)) + "</ol>")

kw_demo = (
    '<label class="block"><span class="text-[10px] font-bold uppercase tracking-wider text-muted">Type what your viewer searches on YouTube</span>'
    '<span class="mt-2 flex items-center gap-2 rounded-full border border-[var(--color-line)] bg-white px-4 py-2.5 transition focus-within:border-orange">'
    f'{svg("search", "h-4 w-4 shrink-0 text-muted")}<input data-mirror="ytkw" placeholder="how to choose a home water filter" '
    'class="min-w-0 flex-1 bg-transparent text-sm text-ink outline-none" aria-label="YouTube search to preview"/></span></label>'
    '<div class="mt-3 flex items-center gap-3 rounded-2xl border border-orange/30 bg-orange/5 p-2">'
    f'<span class="grad-ink-orange grid h-12 w-24 shrink-0 place-items-center rounded-lg text-white">{svg("play", "h-5 w-5")}</span>'
    '<span class="grid gap-0.5"><span class="text-sm font-bold text-ink"><span data-mirror-out="ytkw" class="svc-cap"></span>: watch this first</span>'
    '<span class="text-[10px] font-bold uppercase tracking-wide text-muted">Sponsored · Your channel</span></span></div>')

TARGETING = [
    ("interests", "Interests and topics", "Show your ads to people based on what they are interested in and the topics they watch.",
     chips(["Home and garden", "Fitness", "Business", "Cooking", "Travel"]) + '<p class="mt-2 text-[10px] text-muted">Example interests, picked to match your buyers.</p>'),
    ("keywords", "Keywords and placements", "Target specific search terms and even place your ads on specific channels and videos your audience watches.", kw_demo),
    ("custom", "Custom and remarketing audiences", "Reach people who look like your best customers, and follow up with people who already visited your site but did not buy.", steps_list),
]
t_panels = "".join(
    f'<div data-panel="{k}"{HID if i else ""} class="mt-4">{body}<p class="mt-4 text-sm text-body"><strong class="font-semibold text-ink">{E(n)}.</strong> {E(w)}</p></div>'
    for i, (k, n, w, body) in enumerate(TARGETING))
targeting_box = '<div data-tabs="true">' + figure("Who sees your video", ["Example"], (
    toggle([("interests", "Interests"), ("keywords", "Keywords"), ("custom", "Remarketing")]) + t_panels)) + "</div>"

# --------------------------------------------------- 07 the advantage: video check

leak_box = L.leak_check(
    "YouTube Ads check", "Tick everything that sounds like your video ads today.",
    [("I judge my YouTube ads on views", "Views are only the start. Tracking shows the leads and sales."),
     ("Viewers who do not buy are never followed up", "Remarketing brings them back when they are ready."),
     ("My video takes a while to get to the point", "On skippable ads, the first few seconds decide who keeps watching."),
     ("I think I need an expensive video first", "A clear, honest video often works better than a fancy one."),
     ("My YouTube ads are not linked to conversion tracking", "Without it you can measure views, but not real results.")],
    ("Nothing ticked yet. A free strategy call still checks the targeting, message and tracking behind your video ads.",
     "A gap or two. These are usually the first things I fix so views start turning into customers.",
     "Your video budget is very likely buying views, not customers. Tracking and remarketing are where I would start."),
    CTA, "Gaps ticked")

GET = [
    {"icon": "users", "h3": "Audience research", "p": "Interests, topics, keywords, placements and custom audiences planned around the people likely to care about your offer."},
    {"icon": "pen", "h3": "Video script guidance", "p": "I guide the video and the message so it holds attention and drives action. I can work with a video you already have or advise on a simple one to create."},
    {"icon": "layers", "h3": "Campaign build", "p": "Campaigns built in Google Ads with the right formats for your goal, whether that is awareness, leads or sales."},
    {"icon": "phone", "h3": "Conversion tracking", "p": "Proper tracking set up so we measure real results, not just views."},
    {"icon": "sliders", "h3": "Weekly optimization", "p": "Audiences and videos tested every week, what does not work cut and the winners scaled in a safe and steady way."},
    {"icon": "chart", "h3": "Clear monthly reports", "p": "Plain language reports showing spend, views, actions and results, plus updates on anything important."},
]

FAQ = [
    ("What are YouTube Ads?", "YouTube Ads are video and image ads that run on YouTube. They are managed through Google Ads, so they come with strong targeting and full tracking."),
    ("How much do YouTube Ads cost?", "YouTube is one of the cheaper platforms for reach, and you can often get thousands of views for a small budget. On our call I will suggest a realistic starting budget for your goals."),
    ("Do I need a professional video?", "Not always. A clear, honest video often works better than a fancy one. I guide the script and message, and I can work with a simple video or advise you on creating one."),
    ("How am I charged, per view or per click?", "It depends on the format. With skippable ads you usually pay only when someone watches a good part of your ad or clicks, which keeps your money focused on real interest."),
    ("What is a skippable in stream ad?", "It is an ad that plays before or during a video and can be skipped after a few seconds. You mostly pay only when someone keeps watching, so it is very cost effective."),
    ("What are bumper ads?", "Bumper ads are six second ads that cannot be skipped. They are great for quick, memorable messages that keep your brand in people's minds."),
    ("Can YouTube Ads get me sales or only views?", "They can get you sales when set up with proper tracking and remarketing. Views are only the start, and my job is to turn attention into real customers."),
    ("How do you target the right viewers?", "I use interests, topics, keywords, placements, custom audiences and remarketing, so your ads reach people who are likely to care about your offer."),
    ("Can I retarget people who visited my site?", "Yes. Remarketing on YouTube shows your ads to people who already visited your website, which is one of the cheapest ways to bring back lost buyers."),
    ("How soon will I see results?", "Awareness and views build quickly, often within days. Leads and sales usually build over the first few weeks as we test and improve the account."),
    ("Are YouTube Ads good for small businesses?", "Yes. Because reach is cheap, even small businesses can build strong awareness on YouTube when the targeting and message are right."),
    ("Do you help with the video script?", "Yes. I guide the script and message so your video holds attention and drives action. A good message matters more than expensive production."),
    ("Can you run YouTube Ads for ecommerce?", "Yes. I use video and remarketing to build interest and bring shoppers back to your products, with full tracking of sales."),
    ("What reports will I get?", "You get clear monthly reports in plain language showing spend, views, actions and results, plus updates on anything important."),
    ("How do I get started?", "Just book a free YouTube Ads strategy call using the button on this page. We will talk about your goals and I will show you how YouTube can grow your brand and sales."),
]

RELATED = [
    ("Performance marketing", "/services/performance-marketing/"),
    ("Google Ads", "/services/google-ads/"),
    ("Meta Ads", "/services/meta-ads/"),
    ("LinkedIn Ads", "/services/linkedin-ads/"),
    ("Remarketing", None),
    ("Landing pages", "/services/landing-pages/"),
]

PAGE = {
    "path": "/services/youtube-ads/",
    "slug": "youtube-ads", "thanks": "paid-ads",
    "form_name": "youtube_ads",
    "service": "YouTube Ads",
    "service_name": "YouTube Ads management",
    "thanks_what": "YouTube Ads strategy call",
    "category": "Video advertising",
    "service_desc": "YouTube Ads management covering skippable and non skippable in stream ads, bumper ads, in feed video ads and Shorts ads, with audience research, script guidance, conversion tracking, remarketing, weekly optimization and monthly reporting.",
    "audience": "Businesses that want brand growth, leads or online sales from video",
    "countries": ["India", "United Arab Emirates", "United States", "Canada"],
    "offer_name": "What YouTube Ads management includes",
    "offers": GET,
    "title": "YouTube Ads Services That Drive Sales | Sushant Rana",
    "og_title": "YouTube Ads Services That Drive Sales",
    "og_alt": "YouTube Ads services by Sushant Rana",
    "desc": "YouTube Ads services that grow your brand and bring real sales, not just views. Smart targeting, cheap reach and full tracking. Book a free strategy call.",
    "cta": CTA,
    "trail": [("Home", "/"), ("Services", "/services/"), ("YouTube Ads", None)],
    "related": RELATED,
    "faq": {"pill": "Common questions", "h2": ("YouTube Ads", "questions, answered"),
            "body": ["Cost, formats, videos and targeting. If yours is not here, ask me on the call."], "items": FAQ},
    "hero": {
        "pill": "YouTube Ads",
        "h1": ("YouTube Ads services that grow", "your brand and your sales"),
        "intro_html": [
            'I am <strong class="font-semibold text-ink">Sushant Rana</strong>, and my team and I run YouTube Ads that grow your brand and bring real sales, not just views. Want to reach millions of viewers with video and turn them into customers? That is what YouTube Ads can do, and we can set it all up for you.',
            "YouTube is the second largest search engine in the world, and its ads are managed through Google Ads. We run YouTube Ads for businesses across India, the US and Canada.",
        ],
        "cta2": ("See ad formats", "#types"),
        "stats": [("8+", "Years experience"), ("₹50L+", "Ad spend managed"), ("4", "Markets served"), ("4×", "Best B2B ROAS")],
    },
    "form": {
        "title": "Book your free YouTube Ads strategy call",
        "sub": "Tell me about your business and your video, and I will come to the call with a plan.",
        "submit": "Request my strategy call",
        "steps": [
            {"label": "Video", "fields": [
                {"type": "radio", "name": "video", "label": "Do you have a video ad?", "req": True,
                 "options": ["Yes, ready to use", "Raw footage only", "No video yet"]},
                {"type": "radio", "name": "running", "label": "Are you running YouTube Ads now?",
                 "options": ["Yes", "Tried before", "Never"]},
                {"type": "select", "name": "budget", "label": "Monthly ad budget", "req": True, "placeholder": "Select your budget",
                 "options": ["Under ₹50K", "₹50K - 1L", "₹1L - 3L", "₹3L - 5L", "₹5L - 10L", "₹10L+", "Not decided yet"]},
            ]},
            {"label": "Goals", "fields": [
                {"type": "select", "name": "goal", "label": "Main goal", "req": True, "placeholder": "Select your main goal",
                 "options": ["Brand awareness", "More leads", "More online sales", "Bring back site visitors", "Not sure yet"]},
                {"type": "checkbox", "name": "formats", "label": "Formats you are interested in",
                 "options": ["Skippable", "Non skippable", "Bumper", "In feed", "Shorts", "Not sure"]},
                {"type": "text", "name": "site", "label": "Website or YouTube channel", "placeholder": "yourwebsite.com"},
                {"type": "textarea", "name": "details", "label": "Anything I should know?", "placeholder": "What you sell, who your viewers are, what you have tried..."},
                {"type": "select", "name": "source", "label": "How did you hear about me?", "options": ["Google", "Social media", "Referral", "LinkedIn", "Other"]},
            ]},
        ],
    },
}

PAGE["sections"] = [
    L.hero(PAGE),
    L.marquee(["YouTube Ads", "Skippable ads", "Bumper ads", "In feed video", "Shorts ads", "Video remarketing", "Script guidance"]),
    L.split({"id": "basics", "pill": "The basics", "h2": ("What YouTube Ads are", "and why they matter"),
             "body": ["YouTube Ads are video and image ads that run on YouTube. They are managed through Google Ads, which means they come with the same powerful targeting and tracking.",
                      "Billions of hours of video are watched on YouTube every day. This gives your business a huge, engaged audience and one of the cheapest ways to get in front of people using video."],
             "bullets": ["Run through Google Ads, with its targeting and tracking", "A huge, engaged audience", "One of the cheapest ways to reach people with video"],
             "cta": CTA, "visual": video_box}, dark=True),
    L.section_bg(
        L.icon_cards({"id": "why", "pill": "Why it works", "h2": ("Why YouTube Ads are", "so powerful"),
                      "body": ["Video reaches people while they watch content they love, and with Google behind it, every view can be targeted and tracked."],
                      "cols": "sm:grid-cols-2 lg:grid-cols-4", "cards": [
                          {"icon": "users", "h3": "A massive audience", "p": "Almost everyone watches YouTube. Whatever your business, your customers are spending time there every single day."},
                          {"icon": "wallet", "h3": "Cheap views", "p": "You can often reach thousands of viewers for a small budget. This makes YouTube one of the most cost effective ways to build awareness."},
                          {"icon": "target", "h3": "Powerful targeting", "p": "Because YouTube runs on Google Ads, you can target by interests, keywords, topics and even people who visited your site."},
                          {"icon": "play", "h3": "Video builds trust fast", "p": "People trust what they can see and hear. Video lets you show your product, your face and your story, which builds trust far quicker than text."},
                      ]})
        + L.tabs_showcase({"id": "types", "pill": "Ad formats", "h2": ("The YouTube ad formats", "I run for you"),
                           "body": ["Each format suits a different goal, from a six second reminder to a full story. I pick the mix that fits your message. Pick one to see what it looks like."],
                           "items": FORMATS})),
    L.split({"id": "targeting", "pill": "Targeting", "h2": ("How I reach", "the right viewers"),
             "body": ["Views only matter when they come from the right people. I combine three kinds of targeting so your video reaches people who are likely to care about your offer. Pick one to see how it works."],
             "bullets": ["Interests and topics", "Keywords and placements", "Custom and remarketing audiences"],
             "visual": targeting_box}, dark=True, flip=True),
    L.split({"id": "advantage", "pill": "The advantage", "h2": ("Why video builds trust faster", "than any other ad"),
             "body": ["Text and images can tell people about your business, but video lets them see and feel it. When a person watches you explain your product, hears your voice and sees real results, trust builds much faster.",
                      "This is why YouTube Ads are so strong for growing a brand and warming up buyers. Even people who do not buy right away will remember you, and remarketing brings them back when they are ready."],
             "visual": leak_box}),
    L.crm_section("YouTube Ads", CTA),
    L.section_bg(
        L.process({"id": "process", "pill": "How I work", "h2": ("My YouTube Ads", "process"),
                   "body": ["Five clear stages, from choosing the goal to scaling the videos that work. Pick a stage to follow along."],
                   "steps": [
                       {"h3": "Goals and audit", "short": "Goals", "p": "I learn your business and your goals, so I know whether we are aiming for awareness, leads or sales.", "points": ["Business and goals", "Awareness, leads or sales", "Current results reviewed"]},
                       {"h3": "Audience and message", "short": "Message", "p": "I plan who to target and what your video should say, and I guide the script so it holds attention and drives action.", "points": ["Who to target", "What the video says", "Script guidance"]},
                       {"h3": "Setup and tracking", "short": "Setup", "p": "I build your campaigns and set up proper tracking, so we can measure real results and not just views.", "points": ["Campaigns built", "Conversion tracking", "Remarketing lists"]},
                       {"h3": "Launch and test", "short": "Test", "p": "I launch and test different audiences and videos to find the combinations that perform best.", "points": ["Campaigns live", "Audiences tested", "Videos compared"]},
                       {"h3": "Optimize and scale", "short": "Scale", "p": "I improve the account, cut what does not work and scale the winners in a safe and steady way.", "points": ["Weak parts cut", "Winners scaled", "Steady growth"]},
                   ]})),
    L.icon_cards({"id": "get", "pill": "What you get", "h2": ("What is included in", "my YouTube Ads service"),
                  "body": ["You get a complete, done for you YouTube Ads service. I handle the strategy, the targeting, the setup and the reporting, and you always work directly with me."],
                  "cards": GET,
                  "after": L.cta_band({"pill": "Free strategy call", "h3": "Want to reach millions of viewers on YouTube?",
                                       "p": "Let me look at your business and your goals and show you how YouTube Ads can grow your brand and your sales. No pressure and no obligation.",
                                       "btn": CTA})}),
    L.dark_cards({"id": "choose", "pill": "Why me", "h2": ("Why businesses choose me", "for YouTube Ads"),
                  "body": ["The person who plans your ads is the person you talk to, and success is measured in leads and sales, not view counts."],
                  "cards": [
                      {"h3": "You work directly with the expert", "p": "You talk to the same person who plans and runs your ads, with clear answers and fast replies."},
                      {"h3": "Focus on real results", "p": "I care about leads and sales, not just view counts, and I set up proper tracking to prove it."},
                      {"h3": "Honest reporting", "p": "I report on what matters in plain language, so you always know what your budget is doing."},
                  ]}),
    L.chips_section({"id": "who", "h2": ("Businesses I run", "YouTube Ads for"),
                     "body": "Ecommerce brands, coaches and course creators, local services, healthcare, real estate and any business that can tell a good story on video. If you have something to show, YouTube can work for you.",
                     "chips": [("Ecommerce brands", None), ("Coaches and course creators", "/industries/education/"), ("Local services", None),
                               ("Healthcare", None), ("Real estate", "/industries/real-estate/")]}),
    L.chips_section({"id": "related", "h2": ("Services that pair with", "YouTube Ads"),
                     "body": "YouTube works best alongside search, social and remarketing, so viewers who remember you can find you again.", "chips": RELATED}),
    L.faq(PAGE["faq"]),
    L.contact({"h2": ("Ready to grow", "with video?"),
               "p": "Let us talk about your goals and build a YouTube plan that gets you seen, remembered and chosen by more customers.",
               "btn": CTA, "note": "No obligation · Free strategy call"}),
]
