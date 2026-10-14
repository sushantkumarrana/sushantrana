# SEO + GEO + AEO + AI Search Readiness audit — sushantrana.com

Audit date: 15 Oct 2026. Environment: local repo (`html-site`, uncommitted) served by `php -S localhost:8090 dev/router.php`.
Rules: `SEO-RULES.md`, `SEO_LAUNCH_CHECKLIST.md`, `GEO_AEO_AIO_CHECKLIST.md`. Automated gate: `python3 -I dev/seo-audit.py`.
This file is hidden from visitors (`.htaccess` blocks every `.md`).

## Executive result: CONDITIONAL GO

Code-level crawlability, indexability, canonicals, sitemap, schema, answer-first intros, mobile layout and internal links pass on all 47 indexable pages.
Before launch: the owner decisions below (training crawlers, Search Console AI setting, Bing). Everything that needs the live site or the owner's accounts is NOT TESTED.

## Findings

| Priority | URL | Area | Check | Evidence | File | Fix | Test run | Status | Owner |
|---|---|---|---|---|---|---|---|---|---|
| P1 | all 47 | GEO (entity) | Official profile links | Footer Instagram/YouTube link to `https://www.instagram.com/`, `https://www.youtube.com/` | includes/footer.html | Removed both on Sushant's request (15 Oct); only LinkedIn stays | seo-audit.py | PASS (fixed) | Claude |
| P1 | all 47 | GEO (entity) | LinkedIn link | Footer linked `https://www.linkedin.com/`; the real profile was already in About schema `sameAs` | includes/footer.html | Pointed to `linkedin.com/in/sushant-kumar-rana-030879114`, re-stamped with sync-layout.py | seo-audit.py | PASS (fixed) | Claude |
| P1 | /case-studies/ | SEO/GEO | Hub page | Breadcrumbs of every case study link to a noindex "coming soon" placeholder | case-studies/index.html | Build the case studies hub | seo-audit.py | FAIL (open) | Claude, on approval |
| P1 | robots.txt | AIO | Training vs search crawlers | GPTBot, CCBot, Google-Extended, anthropic-ai, cohere-ai (training) are allowed together with search crawlers | robots.txt | Owner decides training policy; search crawlers (Googlebot, Bingbot, OAI-SearchBot) stay allowed | blocked() check in seo-audit.py | NOT TESTED (owner decision) | Sushant |
| P1 | site | AIO | Google AI inclusion setting | Needs Search Console → Settings → Search generative AI | - | Check, do not change without owner | - | NOT TESTED | Sushant |
| P1 | site | AIO | Bing Webmaster Tools + sitemap | Needs Bing account | - | Add site, submit sitemap.xml | - | NOT TESTED | Sushant |
| P1 | 47 | SEO | Live HTTP 200, headers, X-Robots-Tag | Needs the deployed site | .htaccess | `curl -I` each URL after deploy | - | NOT TESTED | Claude after push |
| P2 | /about/ vs / | GEO (entity) | jobTitle | "Project Manager & Business Growth Consultant" (About) vs "Business Growth Consultant" (Home) | about/index.html, index.html | Pick one title | seo-audit.py | WARN | Sushant |
| P2 | / | AEO | H1 | H1 holds all rotating questions ("Why aren't you getting enough leads? Why is your ROAS dropping? ...") | index.html | Optional: keep one question in the H1, rotate the rest outside it | manual | OPEN | Sushant |
| P2 | case studies | GEO | Client permission | Client names, logos and screenshots are public | case-studies/* | Confirm each client is happy to be named | - | NOT TESTED | Sushant |
| P2 | site | AEO | FAQPage schema | Google stopped showing FAQ rich results (May 2026); 39 pages keep FAQPage only where the FAQ is visible | - | No schema-only FAQs; add FAQs only where they help visitors | seo-audit.py (schema questions must be visible) | PASS | - |
| P2 | /llms.txt | AIO | llms.txt | Optional, not used by Google; kept because it is maintained with every new page | llms.txt | Keep updated or drop; not a launch item | - | N/A | - |

## Passed on every indexable page (seo-audit.py, 47 pages)

Unique title and description, one H1, self canonical with trailing slash, index/follow, OG tags, valid JSON-LD, BreadcrumbList (all but home),
FAQPage only with visible questions, Article on blog posts, answer-first intro under the H1, no nosnippet / AI-only meta tags,
images WebP with alt and size, no broken or redirecting internal links, no orphan pages, sitemap = indexable pages,
robots.txt allows Googlebot, Bingbot and OAI-SearchBot and does not block CSS/JS/images. 360px: no horizontal scroll (browser check, all 47).
Business entity: Person + ProfessionalService on home (Chandigarh, phone, email, countries served), Person + ContactPoint on contact.

## URL inventory

| URL | Type | Index | Canonical OK | H1 (intent served) | Schema | Visible proof |
|---|---|---|---|---|---|---|
| / | Home | index | PASS | Why aren’t you getting enough leads?Why is your ROAS dropping?Why aren | Person, ProfessionalService, WebSite | case/results |
| /about/ | About | index | PASS | Sushant Rana, building revenue systems since 2017 | AboutPage, BreadcrumbList, FAQPage, Person | case/results |
| /services/shopify-store-development/ | Service | index | PASS | Shopify store development that starts selling on first day | BreadcrumbList, FAQPage, Service | case/results |
| /services/website-maintenance/ | Service | index | PASS | Website maintenance that keeps your site fast, secure and up to date | BreadcrumbList, FAQPage, Service | case/results |
| /services/google-ads/ | Service | index | PASS | Google Ads management services that bring ready to buy customers | BreadcrumbList, FAQPage, Service | case/results |
| /blog/ | Hub | index | PASS | Thinking you can use | BreadcrumbList, CollectionPage | case/results |
| /blog/will-my-shopify-store-look-different/ | Blog | index | PASS | Will My Store Look Different From Other Shopify Sites? | BlogPosting, BreadcrumbList | case/results |
| /blog/revenue-systems-vs-marketing-campaigns/ | Blog | index | PASS | Revenue Systems vs Marketing Campaigns: Why One Compounds and the Othe | BlogPosting, BreadcrumbList | case/results |
| /blog/lead-quality-over-lead-volume/ | Blog | index | PASS | Lead Quality Over Lead Volume: The Metric Shift That Changes Everythin | BlogPosting, BreadcrumbList | case/results |
| /blog/practical-ai-automation-without-a-data-team/ | Blog | index | PASS | Practical AI Automation for Businesses That Don't Have a Data Team | BlogPosting, BreadcrumbList | case/results |
| /privacy-policy/ | Policy | index | PASS | Privacy Policy | BreadcrumbList | case/results |
| /terms-and-conditions/ | Policy | index | PASS | Terms & Conditions | BreadcrumbList | case/results |
| /services/amazon-ads/ | Service | index | PASS | Amazon PPC services that get your products to the top and sell more | BreadcrumbList, FAQPage, Service | case/results |
| /industries/auto-repair/ | Industry | index | PASS | Auto repair marketing that keeps your bays full | BreadcrumbList, FAQPage, Service | case/results |
| /industries/dental/ | Industry | index | PASS | Dental marketing that fills your chairs with new patients | BreadcrumbList, FAQPage, Service | case/results |
| /services/ecommerce-seo/ | Service | index | PASS | Ecommerce SEO services that bring free buyers to your online store | BreadcrumbList, FAQPage, Service | case/results |
| /industries/education/ | Industry | index | PASS | Education marketing that brings you more student enquiries and admissi | BreadcrumbList, FAQPage, Service | case/results |
| /services/email-automation/ | Service | index | PASS | Email automation that turns leads into sales while you sleep | BreadcrumbList, FAQPage, Service | case/results |
| /services/enterprise-seo/ | Service | index | PASS | Enterprise SEO services that grow traffic across large websites | BreadcrumbList, FAQPage, Service | case/results |
| /services/gohighlevel/ | Service | index | PASS | GoHighLevel setup that runs your marketing and follow up on autopilot | BreadcrumbList, FAQPage, Service | case/results |
| /services/google-business-profile/ | Service | index | PASS | Google Business Profile optimization that gets you more calls and cust | BreadcrumbList, FAQPage, Service | case/results |
| /services/google-shopping-ads/ | Service | index | PASS | Google Shopping Ads services that put your products in front of buyers | BreadcrumbList, FAQPage, Service | case/results |
| /services/hubspot-crm/ | Service | index | PASS | HubSpot CRM setup that aligns your marketing and sales | BreadcrumbList, FAQPage, Service | case/results |
| /services/landing-pages/ | Service | index | PASS | Landing page design that turns your clicks into customers | BreadcrumbList, FAQPage, Service | case/results |
| /industries/legal-firms/ | Industry | index | PASS | Law firm marketing that brings you more quality clients | BreadcrumbList, FAQPage, Service | case/results |
| /services/link-building/ | Service | index | PASS | Link building services that build real authority and rankings | BreadcrumbList, FAQPage, Service | case/results |
| /services/linkedin-ads/ | Service | index | PASS | LinkedIn Ads services that bring you high quality B2B leads | BreadcrumbList, FAQPage, Service | case/results |
| /services/local-seo/ | Service | index | PASS | Local SEO services that get your business found by nearby customers | BreadcrumbList, FAQPage, Service | case/results |
| /services/meta-ads/ | Service | index | PASS | Meta Ads services that turn Facebook and Instagram into a sales machin | BreadcrumbList, FAQPage, Service | case/results |
| /services/on-page-seo/ | Service | index | PASS | On-page SEO services that turn your pages into ranking machines | BreadcrumbList, FAQPage, Service | case/results |
| /services/performance-marketing/ | Service | index | PASS | Performance marketing services that turn ad spend into real sales | BreadcrumbList, FAQPage, Service | case/results |
| /industries/real-estate/ | Industry | index | PASS | Real estate marketing that brings you ready buyers and sellers | BreadcrumbList, FAQPage, Service | case/results |
| /services/sales-funnel-setup/ | Service | index | PASS | Sales funnel setup that turns strangers into paying customers | BreadcrumbList, FAQPage, Service | case/results |
| /services/seo-audit/ | Service | index | PASS | Get a free website SEO audit that shows exactly why you are not rankin | BreadcrumbList, FAQPage, Service | case/results |
| /services/technical-seo/ | Service | index | PASS | Technical SEO services that fix what is holding your rankings back | BreadcrumbList, FAQPage, Service | case/results |
| /services/wordpress-development/ | Service | index | PASS | WordPress website development that looks great and actually performs | BreadcrumbList, FAQPage, Service | case/results |
| /services/youtube-ads/ | Service | index | PASS | YouTube Ads services that grow your brand and your sales | BreadcrumbList, FAQPage, Service | case/results |
| /services/zoho-crm/ | Service | index | PASS | Zoho CRM setup that organizes your leads and grows your sales | BreadcrumbList, FAQPage, Service | case/results |
| /contact/ | Contact | index | PASS | Let's talk about growing your business | BreadcrumbList, ContactPage, FAQPage, Person | case/results |
| /contact/book-strategy-call/ | Contact | index | PASS | Book a free strategy call, 30 minutes on Google Meet | BreadcrumbList, ContactPage, FAQPage | case/results |
| /case-studies/ourknots/ | Case study | index | PASS | OurKnots on Meta: from 0.72x to 5.13x ROAS | Article, BreadcrumbList, FAQPage | screenshots |
| /case-studies/ourknots-google-ads/ | Case study | index | PASS | OurKnots on Google Ads: 0.71x to 14x ROAS | Article, BreadcrumbList, FAQPage | case/results |
| /case-studies/yalla-renovation/ | Case study | index | PASS | Yalla Renovation on Google Ads: 2,287 tracked form submissions | Article, BreadcrumbList, FAQPage | screenshots |
| /case-studies/4s-study-abroad/ | Case study | index | PASS | 4S Study Abroad on Meta: 7,514 student enquiries at AED 8.79 | Article, BreadcrumbList, FAQPage | screenshots |
| /case-studies/4s-study-abroad-google-ads/ | Case study | index | PASS | 4S Study Abroad on Google Ads: 8,859 enquiries at ₹278 | Article, BreadcrumbList, FAQPage | screenshots |
| /case-studies/meta-ads/ | Hub | index | PASS | Meta Ads case studies, with the real numbers | BreadcrumbList, CollectionPage, FAQPage | case/results |
| /case-studies/google-ads/ | Hub | index | PASS | Google Ads case studies, with the real numbers | BreadcrumbList, CollectionPage, FAQPage | case/results |

## Follow-up

- Launch day: push, then `curl -I` every sitemap URL (expect 200, no X-Robots-Tag), fetch live robots.txt and sitemap.xml, PageSpeed Insights on home, a service page and a case study.
- Week 1: Search Console (sitemap, URL Inspection on 5 URLs, generative AI setting), Bing Webmaster Tools (sitemap, AI Performance when it appears).
- Day 30/60: GSC Generative AI performance report, Bing AI Performance, a fixed list of 10 buyer questions checked in Google AI Mode, ChatGPT search and Copilot (date, cited URL, accuracy).
