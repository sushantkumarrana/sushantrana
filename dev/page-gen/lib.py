"""Builds service pages for sushantrana.com from the Shopify page's shell.

Usage: python3 -I lib.py <repo> <spec.py>
The spec module defines PAGE (dict). Output: <repo>/<path>/index.html and the
thank-you page. Shell (head, nav, footer, scripts) is cut from the live
Shopify page so every page shares the same chrome.
"""
import html
import json
import re
import importlib.util
import runpy
import sys
from pathlib import Path

# the shared header/footer stamper (dev/sync-layout.py)
_spec = importlib.util.spec_from_file_location("sync_layout", Path(__file__).resolve().parent.parent / "sync-layout.py")
SYNC = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(SYNC)

SITE = "https://sushantrana.com"
E = html.escape

ICON = {
    "chev": '<path d="m9 18 6-6-6-6"></path>',
    "check": '<path d="M20 6 9 17l-5-5"></path>',
    "plus": '<path d="M5 12h14"></path><path d="M12 5v14"></path>',
    "minus": '<path d="M5 12h14"></path>',
    "target": '<circle cx="12" cy="12" r="10"></circle><circle cx="12" cy="12" r="6"></circle><circle cx="12" cy="12" r="2"></circle>',
    "search": '<path d="m21 21-4.34-4.34"></path><circle cx="11" cy="11" r="8"></circle>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"></path><path d="M16 3.128a4 4 0 0 1 0 7.744"></path><path d="M22 21v-2a4 4 0 0 0-3-3.87"></path><circle cx="9" cy="7" r="4"></circle>',
    "gauge": '<path d="m12 14 4-4"></path><path d="M3.34 19a10 10 0 1 1 17.32 0"></path>',
    "wallet": '<path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"></path><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"></path>',
    "click": '<path d="M14 4.1 12 6"></path><path d="m5.1 8-2.9-.8"></path><path d="m6 12-1.9 2"></path><path d="M7.2 2.2 8 5.1"></path><path d="M9.037 9.69a.498.498 0 0 1 .653-.653l11 4.5a.5.5 0 0 1-.074.949l-4.349 1.041a1 1 0 0 0-.74.739l-1.04 4.35a.5.5 0 0 1-.95.074z"></path>',
    "chart": '<path d="M3 3v16a2 2 0 0 0 2 2h16"></path><path d="M18 17V9"></path><path d="M13 17V5"></path><path d="M8 17v-3"></path>',
    "pen": '<path d="M12 20h9"></path><path d="M16.376 3.622a1 1 0 0 1 3.002 3.002L7.368 18.635a2 2 0 0 1-.855.506l-2.872.838a.5.5 0 0 1-.62-.62l.838-2.872a2 2 0 0 1 .506-.854z"></path>',
    "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"></path><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"></path><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"></path>',
    "phone": '<path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"></path>',
    "sliders": '<path d="M10 5H3"></path><path d="M12 19H3"></path><path d="M14 3v4"></path><path d="M16 17v4"></path><path d="M21 12h-9"></path><path d="M21 19h-5"></path><path d="M21 5h-7"></path><path d="M8 10v4"></path><path d="M8 12H3"></path>',
    "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"></path><path d="M14 2v4a2 2 0 0 0 2 2h4"></path><path d="M10 9H8"></path><path d="M16 13H8"></path><path d="M16 17H8"></path>',
    "play": '<polygon points="6 3 20 12 6 21 6 3"></polygon>',
    "repeat": '<path d="m17 2 4 4-4 4"></path><path d="M3 11v-1a4 4 0 0 1 4-4h14"></path><path d="m7 22-4-4 4-4"></path><path d="M21 13v1a4 4 0 0 1-4 4H3"></path>',
    "bag": '<path d="M6 2 3 6v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V6l-3-4Z"></path><path d="M3 6h18"></path><path d="M16 10a4 4 0 0 1-8 0"></path>',
    "image": '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"></rect><circle cx="9" cy="9" r="2"></circle><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"></path>',
    "zap": '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"></path>',
    "mail": '<rect width="20" height="16" x="2" y="4" rx="2"></rect><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"></path>',
    "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"></path>',
    "pin": '<path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"></path><circle cx="12" cy="10" r="3"></circle>',
    "calendar": '<path d="M8 2v4"></path><path d="M16 2v4"></path><rect width="18" height="18" x="3" y="4" rx="2"></rect><path d="M3 10h18"></path>',
    "video": '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"></path><rect x="2" y="6" width="14" height="12" rx="2"></rect>',
    "clock": '<circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline>',
    "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"></path>',
}


def svg(name, cls, sw=2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" '
            f'class="lucide lucide-{name} {cls}" aria-hidden="true">{ICON[name]}</svg>')


def hl(title, accent):
    """Heading text with its orange tail."""
    return f'{E(title)} <span class="text-orange">{E(accent)}</span>'


def hl_dark(title, accent):
    return f'{E(title)} <span class="text-orange-300">{E(accent)}</span>'


def pill(text, dark=False):
    look = "border border-white/20 bg-white/10 text-orange-300" if dark else "border border-[var(--color-line)] bg-white text-orange"
    return (f'<span class="inline-flex rounded-full px-4 py-1.5 font-[family-name:var(--font-display)] text-xs '
            f'font-bold uppercase tracking-widest {look}">{E(text)}</span>')


def d(i, step=0.05, per=3):
    """Stagger delay attribute for the i-th card in a row of `per`."""
    v = round((i % per) * step, 2)
    return f' style="--d:{v}s"' if v else ""


def bullets(items, dark=False):
    tone = "text-white" if dark else "text-ink"
    li = "".join(
        f'<li class="flex items-start gap-3 {tone}"><span class="mt-0.5 grid h-6 w-6 shrink-0 place-items-center '
        f'rounded-full bg-orange text-white">{svg("check", "h-3.5 w-3.5", 3)}</span><span class="font-medium">{E(t)}</span></li>'
        for t in items)
    return f'<ul class="mt-7 grid list-none gap-3.5">{li}</ul>'


def paras(ps, cls):
    return "".join(f'<p class="{cls}">{E(p)}</p>' for p in ps)


def figure(title, tags, body):
    t = "".join(f'<span class="rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider text-muted">{E(x)}</span>' for x in tags)
    return (f'<figure class="m-0 overflow-hidden rounded-3xl border border-[var(--color-line)] bg-white shadow-[0_30px_70px_-40px_rgba(10,10,10,0.45)]">'
            f'<figcaption class="flex items-center justify-between border-b border-[var(--color-line)] px-5 py-4">'
            f'<span class="font-[family-name:var(--font-display)] text-sm font-bold text-ink">{E(title)}</span>'
            f'<span class="flex items-center gap-2">{t}</span></figcaption><div class="p-5">{body}</div></figure>')


# ------------------------------------------------------------------ sections

DARK_OPEN = ('<section aria-labelledby="{id}-heading" class="relative bg-[#050505] bg-cover bg-center bg-no-repeat " '
             'style="background-image:url(/footer/footer-bg.webp)"><div aria-hidden="true" class="pointer-events-none absolute inset-0 overflow-hidden">'
             '<span class="absolute inset-0 bg-black/45"></span><span class="absolute left-1/2 top-0 h-80 w-[36rem] -translate-x-1/2 rounded-full bg-orange/25 blur-[120px]"></span></div><div class="relative">')


def split(s, dark=False, flip=False):
    """Text column + a visual column (s['visual'] is raw HTML)."""
    id_ = s["id"]
    hfn = hl_dark if dark else hl
    text_cls = "text-white/80" if dark else "text-body"
    h_cls = "text-white" if dark else "text-ink"
    cta = f'<a href="#contact" class="btn btn-primary mt-9">{E(s["cta"])}</a>' if s.get("cta") else ""
    extra = s.get("after", "")
    D1 = ' style="--d:0.1s"'
    anchor = f' id="{s["anchor"]}"' if s.get("anchor") else ""
    text = (f'<div data-reveal="true" class="{"order-1 lg:order-2" if flip else ""}"{D1 if flip else ""}>{pill(s["pill"], dark)}'
            f'<h2 id="{id_}-heading" class="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold {h_cls}">{hfn(*s["h2"])}</h2>'
            f'{paras(s["body"], "mt-5 max-w-xl " + text_cls)}{bullets(s["bullets"], dark) if s.get("bullets") else ""}{extra}{cta}</div>')
    vis = (f'<div data-reveal="true" class="{"order-2 lg:order-1 " if flip else ""}lg:sticky lg:top-24 lg:self-start"{"" if flip else D1}>'
           f'{s["visual"]}</div>')
    grid = f'<div class="wrap grid items-start gap-14 {"py-20 md:py-28 " if dark else ""}lg:grid-cols-2 svc-split"{anchor}>{text}{vis}</div>'
    if dark:
        return DARK_OPEN.format(id=id_) + grid + "</div></section>"
    return f'<section class="section" aria-labelledby="{id_}-heading">{grid}</section>'


def centered_head(s, dark=False):
    hfn = hl_dark if dark else hl
    if dark:
        return (f'<div class="text-center"><div data-reveal="true">{pill(s["pill"], True)}'
                f'<h2 id="{s["id"]}-heading" class="mx-auto mt-5 max-w-4xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-white">{hfn(*s["h2"])}</h2>'
                f'{paras(s.get("body", []), "mx-auto mt-5 max-w-2xl text-white/75")}</div></div>')
    return (f'<div class="wrap-wide text-center"><div data-reveal="true"><span class="script-label">{E(s["pill"])}</span>'
            f'<h2 id="{s["id"]}-heading" class="mx-auto mt-5 max-w-5xl text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink">{hfn(*s["h2"])}</h2>'
            f'{paras(s.get("body", []), "mx-auto mt-5 max-w-2xl text-lg text-muted")}</div></div>')


def icon_cards(s):
    cols = s.get("cols", "sm:grid-cols-2 lg:grid-cols-3")
    per = 4 if "lg:grid-cols-4" in cols else 3
    items = "".join(
        f'<li class="flex"><div data-reveal="true" class="flex w-full"{d(i, per=per)}><article class="card w-full p-7">'
        f'<span class="grid h-12 w-12 place-items-center rounded-2xl bg-orange/10 text-orange">{svg(c["icon"], "h-6 w-6")}</span>'
        f'<h3 class="mt-5 text-xl font-extrabold text-ink">{E(c["h3"])}</h3><p class="mt-2.5 text-body">{E(c["p"])}</p></article></div></li>'
        for i, c in enumerate(s["cards"]))
    anchor = f'id="{s["anchor"]}" ' if s.get("anchor") else ""
    return (f'<section class="section" {anchor}aria-labelledby="{s["id"]}-heading">{centered_head(s)}'
            f'<ul class="wrap mt-14 grid list-none gap-5 {cols}">{items}</ul>{s.get("after", "")}</section>')


def dark_cards(s):
    items = "".join(
        f'<li class="flex"><div data-reveal="true" class="flex w-full"{d(i, 0.06)}><article class="w-full rounded-3xl border border-white/15 bg-white/[0.06] p-7 backdrop-blur-sm">'
        f'<h3 class="text-xl font-extrabold text-white">{E(c["h3"])}</h3><p class="mt-3 text-white/75">{E(c["p"])}</p></article></div></li>'
        for i, c in enumerate(s["cards"]))
    return (DARK_OPEN.format(id=s["id"]) + f'<div class="wrap py-20 md:py-28">{centered_head(s, True)}'
            f'<ul class="mt-14 grid list-none gap-6 md:grid-cols-3">{items}</ul>{s.get("after", "")}</div></div></section>')


WALKER = None  # filled from the shell (the illustrated character in the process strip)


def process(s):
    steps = s["steps"]
    n = len(steps)
    CUR = ' aria-current="step"'
    edge = f"{50 / n:g}%"
    btns = "".join(
        f'<li class="relative text-center"><button type="button" data-proc-btn="{i}"{CUR if i == 0 else ""} class="group flex w-full flex-col items-center gap-2">'
        f'<span data-proc-dot="true" class="grid h-7 w-7 place-items-center rounded-full border-2 font-[family-name:var(--font-display)] text-xs font-extrabold transition '
        f'{"border-orange bg-orange text-white" if i == 0 else "border-ink/15 bg-white text-muted group-hover:border-orange"}">{i + 1:02d}</span>'
        f'<span data-proc-label="true" class="text-xs font-semibold transition sm:text-sm {"text-ink" if i == 0 else "text-muted group-hover:text-orange"}">{E(st.get("short", st["h3"]))}</span></button></li>'
        for i, st in enumerate(steps))
    cards = "".join(
        f'<li data-proc-card="{i}" class="absolute inset-x-0 top-0 flex lg:relative lg:inset-auto lg:z-auto">'
        f'<article class="w-full rounded-3xl border bg-white p-6 transition-[border-color,box-shadow,transform,opacity] duration-500 '
        f'{"border-orange shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)] lg:-translate-y-2" if i == 0 else "border-[var(--color-line)] lg:opacity-70"}">'
        f'<p class="font-[family-name:var(--font-display)] text-xs font-bold uppercase tracking-widest text-orange">Step {i + 1:02d}</p>'
        f'<h3 class="mt-2 text-lg font-extrabold text-ink">{E(st["h3"])}</h3><p class="mt-2 text-sm text-body">{E(st["p"])}</p>'
        f'<ul class="mt-4 grid list-none gap-1.5">' + "".join(
            f'<li class="flex items-start gap-2 text-xs font-medium text-muted"><span aria-hidden="true" class="mt-1.5 h-1.5 w-1.5 shrink-0 rounded-full bg-orange"></span>{E(b)}</li>'
            for b in st["points"]) + '</ul></article></li>'
        for i, st in enumerate(steps))
    return (f'<section class="section" aria-labelledby="{s["id"]}-heading">{centered_head(s)}'
            f'<div data-process="true" class="relative h-[300vh] lg:h-[340vh]"><div class="sticky top-0 flex min-h-[100dvh] items-center py-10 lg:py-16"><div class="w-full"><div class="wrap">'
            f'<div class="relative overflow-hidden rounded-[32px] border border-[var(--color-line)] bg-white px-6 pb-8 pt-6">{WALKER}'
            f'<ol class="relative mt-2 grid list-none gap-2" style="grid-template-columns:repeat({n},minmax(0,1fr))">'
            f'<span aria-hidden="true" class="absolute top-[13px] h-1 rounded-full bg-ink/10" style="left:{edge};right:{edge}"></span>'
            f'<span aria-hidden="true" data-proc-fill="true" class="absolute top-[13px] h-1 w-0 rounded-full bg-orange transition-[width] duration-300" style="left:{edge}"></span>{btns}</ol></div></div>'
            f'<ol class="wrap relative mt-8 grid h-[300px] list-none grid-cols-1 gap-5 sm:h-[250px] lg:h-auto svc-proc-cols" style="--n:{n}">{cards}</ol></div></div></div></section>')


def chips_section(s):
    items = "".join(
        f'<li><a class="inline-flex rounded-full border border-[var(--color-line)] bg-white px-5 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold text-ink transition hover:border-orange hover:text-orange" href="{href}">{E(t)}</a></li>'
        if href else
        f'<li><span class="inline-flex rounded-full border border-[var(--color-line)] bg-white px-5 py-2.5 font-[family-name:var(--font-display)] text-sm font-semibold text-ink">{E(t)}</span></li>'
        for t, href in s["chips"])
    return (f'<section class="section" aria-labelledby="{s["id"]}-heading"><div class="wrap text-center"><div data-reveal="true">'
            f'<h2 id="{s["id"]}-heading" class="text-2xl font-extrabold text-ink">{hl(*s["h2"])}</h2>'
            f'<p class="mx-auto mt-4 max-w-2xl text-muted">{E(s["body"])}</p>'
            f'<ul class="mt-7 flex list-none flex-wrap justify-center gap-3">{items}</ul></div></div></section>')


def cta_band(s):
    btn2 = f'<a href="{s["btn2"][1]}" class="btn btn-outline !border-white/30 !text-white">{E(s["btn2"][0])}</a>' if s.get("btn2") else ""
    return (f'<div class="wrap mt-10"><div data-reveal="true"><div class="grad-ink-orange relative overflow-hidden rounded-[36px] p-10 text-center md:p-14">'
            f'<span aria-hidden="true" class="pointer-events-none absolute left-1/2 top-0 h-64 w-64 -translate-x-1/2 rounded-full bg-orange/40 blur-[100px]"></span>'
            f'<div class="relative">{pill(s["pill"], True)}<h3 class="mx-auto mt-5 max-w-3xl text-[clamp(1.4rem,3vw,2.2rem)] font-extrabold text-white">{E(s["h3"])}</h3>'
            f'<p class="mx-auto mt-4 max-w-2xl text-white/75">{E(s["p"])}</p><div class="mt-8 flex flex-wrap justify-center gap-3">'
            f'<a href="#contact" class="btn btn-primary">{E(s["btn"])}</a>{btn2}</div></div></div></div></div>')


def faq(s):
    D5 = ' style="--d:0.05s"'
    items = "".join(
        f'<div data-reveal="true"{D5 if i % 2 else ""}><details class="group overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white">'
        f'<summary class="flex cursor-pointer items-center justify-between gap-4 px-6 py-5 font-[family-name:var(--font-display)] font-semibold text-ink marker:content-[&#x27;&#x27;]">'
        f'<h3 class="text-base font-semibold">{E(q)}</h3><span class="grid h-5 w-5 shrink-0 place-items-center rounded-full bg-ink/5 text-ink transition-transform duration-300 group-open:rotate-45 group-open:bg-orange group-open:text-white">'
        f'{svg("plus", "h-3 w-3", 3)}</span></summary><p class="px-6 pb-6 text-sm text-body">{E(a)}</p></details></div>'
        for i, (q, a) in enumerate(s["items"]))
    return (f'<section class="section" id="faq" aria-labelledby="faq-heading">{centered_head({**s, "id": "faq"})}'
            f'<div class="wrap mt-12 grid gap-4 md:grid-cols-2">{items}</div></section>')


def faq_schema(url, items):
    """FAQPage node for a page's @graph; the same items must be shown with faq()."""
    return {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"}, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def add_faq(page, url, h2, items):
    """Visible FAQ before the closing form, plus its FAQPage schema."""
    page["sections"].insert(-1, faq({"pill": "Common questions", "h2": h2, "body": [], "items": items}))
    page["graph"].append(faq_schema(url, items))


def contact(s):
    return (f'<section id="contact" class="section"><div class="wrap"><div data-reveal="true"><div class="relative overflow-hidden rounded-[36px] bg-[#050505] bg-cover bg-center p-10 text-center md:p-20" style="background-image:url(/footer/footer-bg.webp)">'
            f'<div class="pointer-events-none absolute inset-0 bg-black/35"></div><div class="pointer-events-none absolute left-1/2 top-0 h-72 w-72 -translate-x-1/2 rounded-full bg-orange/40 blur-[100px]"></div>'
            f'<div class="relative"><h2 class="mx-auto max-w-3xl text-[clamp(2rem,5vw,3.6rem)] text-white">{hl_dark(*s["h2"])}</h2>'
            f'<p class="mx-auto mt-5 max-w-xl text-white/80">{E(s["p"])}</p><a href="#" data-consult="true" class="btn btn-primary mt-9">{E(s["btn"])}</a>'
            f'<p class="mt-5 font-[family-name:var(--font-display)] text-sm font-semibold text-white/70">{E(s["note"])}</p></div></div></div></div></section>')


def marquee(words):
    one = "".join(f'<span class="mx-4 inline-flex items-center gap-4 whitespace-nowrap font-[family-name:var(--font-display)] text-[clamp(0.85rem,1.6vw,1.25rem)] font-bold">{E(w)}<span class="opacity-70">✦</span></span>' for w in words)
    return (f'<div class="py-8" aria-hidden="true"><div class="marquee-nofade overflow-hidden py-2.5 bg-[#0a0a0a] text-white ">'
            f'<div class="marquee__track" style="--dur:55s">{one * 8}</div></div></div>')


def section_bg(inner):
    """The soft grey band the Shopify page wraps its middle sections in."""
    return f'<div class="relative bg-section"><div class="relative z-10">{inner}</div></div>'


# ---------------------------------------------------------------------- form

SELECT_CLS = ("w-full rounded-xl border bg-white px-4 py-2.5 text-ink outline-none transition border-[var(--color-line)] focus:border-orange "
              "appearance-none bg-[length:12px] bg-[right_1rem_center] bg-no-repeat pr-10")
SELECT_STYLE = ('background-image:url(&quot;data:image/svg+xml;utf8,&lt;svg xmlns=&#x27;http://www.w3.org/2000/svg&#x27; viewBox=&#x27;0 0 24 24&#x27; '
                'fill=&#x27;none&#x27; stroke=&#x27;%235a5a5a&#x27; stroke-width=&#x27;3&#x27; stroke-linecap=&#x27;round&#x27; stroke-linejoin=&#x27;round&#x27;&gt;'
                '&lt;path d=&#x27;m6 9 6 6 6-6&#x27;/&gt;&lt;/svg&gt;&quot;)')
INPUT_CLS = "w-full rounded-xl border bg-white px-4 py-2.5 text-ink outline-none transition border-[var(--color-line)] focus:border-orange"
COUNTRY = None  # the full calling-code <select>, cut from the shell
SOURCES = ["Google search", "Instagram", "LinkedIn", "Referral / word of mouth", "Other"]


def label_span(text, req):
    star = ' <span class="text-orange">*</span>' if req else " "
    return f'<span class="mb-1 block text-sm font-semibold text-ink">{E(text)}{star}</span>'


def field(f):
    kind, name, text = f["type"], f["name"], f["label"]
    req = f.get("req", False)
    r = ' data-req="true"' if req else ""
    if kind == "select":
        opts = f'<option value="" selected="">{E(f.get("placeholder", "Select"))}</option>' + "".join(f"<option>{E(o)}</option>" for o in f["options"])
        return (f'<label data-field="{name}"{r}>{label_span(text, req)}<select name="{name}" class="{SELECT_CLS}" style="{SELECT_STYLE}">{opts}</select></label>')
    if kind == "text":
        return (f'<label data-field="{name}"{r}>{label_span(text, req)}<input name="{name}" placeholder="{E(f.get("placeholder", ""))}" '
                f'{f.get("attrs", "")} class="{INPUT_CLS}"/></label>')
    if kind == "textarea":
        return (f'<label data-field="{name}"{r}>{label_span(text, req)}<textarea name="{name}" rows="3" placeholder="{E(f.get("placeholder", ""))}" class="{INPUT_CLS}"></textarea></label>')
    if kind in ("radio", "checkbox"):
        opts = "".join(
            f'<label class="svc-chip"><input type="{kind}" name="{name}" value="{E(o)}" class="sr-only"/><span>{E(o)}</span></label>' for o in f["options"])
        return (f'<div data-field="{name}"{r} role="group" aria-label="{E(text)}">{label_span(text, req)}<div class="flex flex-wrap gap-2">{opts}</div></div>')
    raise ValueError(kind)


def step_form(p, in_modal=False):
    fm = p["form"]
    # site.js turns any button starting "book" / "get your free" into a popup opener
    assert not fm["submit"].lower().startswith(("book", "get your free")), fm["submit"]
    labels = ["Contact"] + [s["label"] for s in fm["steps"]]
    dots = ""
    for i, lab in enumerate(labels):
        on = i == 0
        line = f'<span data-step-line="{i}" class="h-px flex-1 bg-ink/10"></span>' if i < len(labels) - 1 else ""
        dots += (f'<li class="flex flex-1 items-center gap-2"><span data-step-dot="{i}" class="grid h-7 w-7 shrink-0 place-items-center rounded-full text-xs font-bold transition '
                 f'{"bg-orange text-white" if on else "bg-ink/10 text-muted"}"><span data-num="true">{i + 1}</span><span data-tick="true" hidden="">{svg("check", "h-3.5 w-3.5", 3)}</span></span>'
                 f'<span data-step-label="{i}" class="text-xs font-semibold uppercase tracking-wide {"text-ink" if on else "text-muted"}">{E(lab)}</span>{line}</li>')
    contact_step = (
        '<div data-step="0" class="grid gap-3">'
        f'<label data-field="name">{label_span("Full name", True)}<input placeholder="Your name" autoComplete="name" class="{INPUT_CLS}" name="name"/></label>'
        f'<label data-field="email">{label_span("Business email", True)}<input type="email" inputMode="email" autoComplete="email" placeholder="you@company.com" class="{INPUT_CLS}" name="email"/></label>'
        f'<div data-field="phone">{label_span("Phone number", True)}<div data-wrap="true" class="flex overflow-hidden rounded-xl border bg-white transition border-[var(--color-line)] focus-within:border-orange">'
        '<div class="relative shrink-0"><span aria-hidden="true" class="pointer-events-none flex h-full items-center gap-1 border-r border-[var(--color-line)] pl-3 pr-2 ">'
        '<span data-flag="true" class="text-base leading-none">🇮🇳</span><span class="font-medium text-ink">+<span data-dial="true">91</span></span></span>'
        f'{COUNTRY}</div><input type="tel" inputMode="tel" autoComplete="tel-national" placeholder="98765 43210" class="min-w-0 flex-1 bg-transparent px-4 py-2.5 text-ink outline-none" name="phone"/></div></div>'
        f'<label data-field="company">{label_span(fm.get("company_label", "Company / brand name"), True)}<input placeholder="Your business name" autoComplete="organization" class="{INPUT_CLS}" name="company"/></label></div>')
    steps = "".join(
        f'<div data-step="{i + 1}" hidden="" class="grid gap-3">' + "".join(field(f) for f in s["fields"]) + "</div>"
        for i, s in enumerate(fm["steps"]))
    enquiry = f' data-enquiry="{p["enquiry"]}"' if p.get("enquiry") else ""
    return (f'<div class="card p-5 md:p-6" data-step-form="generic" data-form-name="{p["form_name"]}" data-service="{E(p["service"])}" data-thanks="/thank-you-{p.get("thanks", p["slug"])}/"{enquiry}>'
            f'<h2 class="{"pr-10 text-lg" if in_modal else "text-xl"} font-extrabold text-ink">{E(fm["title"])}</h2>'
            f'<p class="mt-1.5 text-sm text-muted">{E(fm["sub"])}</p><ol class="mt-5 flex list-none items-center gap-2">{dots}</ol>'
            '<form noValidate="" data-err="border-red-500" data-ok="border-[var(--color-line)] focus:border-orange" data-wrap-err="border-red-500" '
            'data-wrap-ok="border-[var(--color-line)] focus-within:border-orange" class="mt-5 grid gap-3">'
            '<input tabindex="-1" autoComplete="off" aria-hidden="true" class="absolute left-[-9999px] h-0 w-0 opacity-0" name="website"/>'
            f'{contact_step}{steps}'
            '<p data-form-error="true" hidden="" role="alert" class="rounded-xl bg-red-50 px-4 py-2.5 text-sm font-medium text-red-700"></p>'
            '<div class="mt-2 flex gap-3"><button type="button" data-back="true" hidden="" class="btn btn-outline flex-1">Back</button>'
            '<button type="button" data-next="true" data-label="Next step" class="btn btn-primary flex-1 disabled:opacity-70">Next step</button>'
            f'<button type="submit" data-submit="true" data-label="{E(fm["submit"])}" hidden="" class="btn btn-primary flex-1 disabled:opacity-70">{E(fm["submit"])}</button></div>'
            '<p class="text-center text-xs text-muted">No obligation. Your details stay with me.</p></form></div>')


# ---------------------------------------------------------------------- hero

def breadcrumb(trail):
    items = []
    ld = []
    for i, (name, href) in enumerate(trail):
        ld.append({"@type": "ListItem", "position": i + 1, "name": name, **({"item": SITE + href.rstrip("/") if href != "/" else SITE} if href else {})})
        chev = svg("chev", "h-3.5 w-3.5 shrink-0 opacity-50") if i else ""
        inner = (f'<a class="transition hover:text-orange" href="{href}">{E(name)}</a>' if href else
                 f'<span aria-current="page" class="max-w-[52vw] truncate font-semibold text-ink sm:max-w-none">{E(name)}</span>')
        items.append(f'<li class="flex items-center gap-1">{chev}{inner}</li>')
    js = json.dumps({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": ld}, ensure_ascii=False)
    return (f'<script type="application/ld+json">{js}</script><nav aria-label="Breadcrumb" class="">'
            f'<ol class="flex flex-wrap items-center gap-1 text-xs text-muted">{"".join(items)}</ol></nav>')


def hero(p):
    h = p["hero"]
    stats = ""
    if h.get("stats"):
        cells = "".join(
            f'<div class="bg-[#fff7f3] px-3 py-3.5 text-center"><dt class="sr-only">{E(lab)}</dt><dd><span class="block font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">'
            f'<span class="tabular-nums" data-anim-num="true" data-dur="1300">{E(num)}</span></span><span class="mt-0.5 block text-[10px] font-semibold uppercase leading-tight tracking-wide text-muted">{E(lab)}</span></dd></div>'
            for num, lab in h["stats"])
        stats = f'<div data-reveal="true" class="order-3 lg:col-start-1"><dl class="grid grid-cols-2 gap-px overflow-hidden rounded-2xl border border-[var(--color-line)] bg-[var(--color-line)] sm:grid-cols-4">{cells}</dl></div>'
    main_cta = (f'<a href="{h["cta_href"]}" data-no-popup="true" class="btn btn-primary">{E(p["cta"])}</a>' if h.get("cta_href")
                else f'<a href="#contact" class="btn btn-primary">{E(p["cta"])}</a>')
    right = h.get("visual") or step_form(p)  # case studies show a chart here, the form moves to the end
    return (f'<section class="relative overflow-hidden bg-white" aria-labelledby="hero-heading"><div class="wrap relative z-10 pt-24">{breadcrumb(p["trail"])}</div>'
            '<div class="wrap relative z-10 grid items-start gap-8 py-6 md:py-8 lg:grid-cols-[1.05fr_0.95fr] lg:gap-12">'
            f'<div data-reveal="true" class="order-1">{pill(h["pill"])}'
            f'<h1 id="hero-heading" class="mt-4 text-[clamp(2rem,7vw,2.7rem)] font-extrabold leading-[1.08] text-ink">{hl(*h["h1"])}</h1>'
            + "".join(f'<p class="mt-4 max-w-xl text-body">{x}</p>' for x in h["intro_html"]) +
            f'<div class="mt-6 flex flex-wrap gap-3">{main_cta}'
            f'<a href="{h["cta2"][1]}" class="btn btn-outline">{E(h["cta2"][0])}</a></div></div>'
            f'<div data-reveal="true" class="order-2 lg:row-span-2" style="--d:0.1s">{right}</div>{stats}</div></section>')


# ---------------------------------------------------------------- whole page

def jsonld(p):
    url = SITE + p["path"].rstrip("/")
    if p.get("graph"):  # pages that are not a Service (contact, booking) bring their own
        return json.dumps({"@context": "https://schema.org", "@graph": p["graph"]}, ensure_ascii=False)
    graph = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["desc"], "inLanguage": "en",
         "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": url + "#service"}, "mainEntity": {"@id": url + "#service"},
         "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/og.jpg", "width": 1200, "height": 630},
         "significantLink": [SITE + h.rstrip("/") for _, h in p["related"] if h]},
        {"@type": "Service", "@id": url + "#service", "name": p["service_name"], "serviceType": p["service_name"], "category": p["category"],
         "description": p["service_desc"], "url": url, "provider": {"@id": SITE + "/#person"},
         "areaServed": [{"@type": "Country", "name": c} for c in p["countries"]],
         "audience": {"@type": "BusinessAudience", "name": p["audience"]},
         "availableChannel": {"@type": "ServiceChannel", "serviceUrl": url, "availableLanguage": ["en", "hi"]},
         "hasOfferCatalog": {"@type": "OfferCatalog", "name": p["offer_name"], "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@type": "Service", "name": c["h3"], "description": c["p"]}} for c in p["offers"]]}},
        {"@type": "FAQPage", "@id": url + "#faq", "isPartOf": {"@id": url + "#webpage"}, "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]["items"]]},
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)


def meta(p):
    url = SITE + p["path"]
    t, ds = E(p["title"]), E(p["desc"])
    og = E(p["og_title"])
    return (f'<title>{t}</title><link rel="stylesheet" href="/assets/css/style.css"/><meta name="description" content="{ds}"/>'
            '<meta name="robots" content="index, follow"/><meta name="googlebot" content="index, follow, max-image-preview:large, max-snippet:-1"/>'
            f'\n<link rel="canonical" href="{url}"/><meta property="og:title" content="{og}"/><meta property="og:description" content="{ds}"/>'
            f'<meta property="og:url" content="{url}"/><meta property="og:site_name" content="Sushant Rana"/><meta property="og:locale" content="en_US"/>'
            '<meta property="og:image" content="https://sushantrana.com/og.jpg"/><meta property="og:image:width" content="1200"/><meta property="og:image:height" content="630"/>'
            f'<meta property="og:image:alt" content="{E(p["og_alt"])}"/><meta property="og:type" content="website"/><meta name="twitter:card" content="summary_large_image"/>'
            f'<meta name="twitter:title" content="{og}"/><meta name="twitter:description" content="{ds}"/><meta name="twitter:image" content="https://sushantrana.com/og.jpg"/>')


def load_shell(repo):
    global WALKER, COUNTRY
    s = (repo / "services/shopify-store-development/index.html").read_text()
    i = s.find("<div data-proc-walk")
    WALKER = s[i:s.find('<ol class="relative mt-2', i)]
    i = s.find('<select aria-label="Country calling code"')
    COUNTRY = s[i:s.find("</select>", i) + 9]
    return s


def build(repo, p):
    shell = load_shell(repo)
    head_start = shell.find("<title>")
    head_end = shell.find('<meta name="twitter:image"')
    head_end = shell.find("/>", head_end) + 2
    top = shell[:head_start] + meta(p) + shell[head_end:shell.find('<main id="main">')]
    # page graph: the first ld+json after <body>
    gi = top.find('<script type="application/ld+json">', top.find("<body>"))
    ge = top.find("</script>", gi) + 9
    top = top[:gi] + f'<script type="application/ld+json">{jsonld(p)}</script>' + top[ge:]

    tail = shell[shell.find("</main>") + 7:]
    mi = tail.find('<div data-modal="quote"')
    me = tail.find('<button data-back-to-top')
    modal = (f'<div data-modal="quote" hidden="" class="modal fixed inset-0 z-[100] grid place-items-center p-4" role="dialog" aria-modal="true" aria-label="{E(p["form"]["title"])}">'
             '<div data-modal-close="true" class="absolute inset-0 bg-black/55 backdrop-blur-sm"></div>'
             '<div data-modal-panel="true" data-lenis-prevent="true" class="relative max-h-[calc(100dvh-2rem)] w-full max-w-md touch-pan-y overflow-y-auto overscroll-contain rounded-[28px]">'
             '<button type="button" aria-label="Close" data-modal-close="true" class="absolute right-4 top-4 z-10 grid h-9 w-9 place-items-center rounded-full bg-black/5 text-ink transition hover:bg-black/10">'
             '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-x h-4 w-4" aria-hidden="true"><path d="M18 6 6 18"></path><path d="m6 6 12 12"></path></svg></button>'
             f'{step_form(p, in_modal=True)}</div></div>\n')
    tail = tail[:mi] + modal + tail[me:]
    tail = re.sub(r'(<a href="#contact" data-consult="true" class="btn btn-primary w-full">)[^<]*(</a>)', lambda m: m.group(1) + E(p["cta"]) + m.group(2), tail)

    body = '<main id="main">' + "".join(p["sections"]) + "</main>"
    # long CTA labels must wrap on small phones instead of widening the page
    body = re.sub(r'class="btn (?!svc-wrap)', 'class="btn svc-wrap ', body).replace("svc-wrap btn-primary svc-wrap", "svc-wrap btn-primary")
    out = repo / p["path"].strip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SYNC.stamp(top + body + tail, p["path"]))
    return out


WHATSAPP = "918289051732"


# One thank-you page per service group (GA4 gets one lead event per group:
# /thank-you-paid-ads/ → lead_paid_ads). slug → (title, WhatsApp fallback label).
THANKS_GROUPS = {
    "paid-ads": ("Paid ads", "paid ads"),
    "seo": ("SEO", "SEO"),
    "website": ("Website development", "website"),
    "crm-automation": ("CRM and automation", "CRM and automation"),
    "industry": ("Industry marketing", "marketing"),
}


def build_thanks(repo, p):
    """Thank-you page that opens WhatsApp with the lead's answers (site.js, data-wa-generic).
    A spec with "thanks" points its form at a shared group page and builds that page."""
    t = (repo / "thank-you-case-study/index.html").read_text()
    slug = p.get("thanks", p["slug"])
    if slug in THANKS_GROUPS:
        (title, label), (back, back_name), form = THANKS_GROUPS[slug], ("/services/", "all services"), slug.replace("-", "_")
    else:
        back, back_name = p.get("thanks_back", (p["path"], p["service_name"]))  # shared thank-you pages link to the hub
        title, label, form = back_name, p.get("wa_label", p["service"]), p["form_name"]
    t = re.sub(r"<title>[^<]*</title>", f"<title>Thank you | {E(title)} | Sushant Rana</title>", t)
    t = re.sub(r'data-wa-generic="[^"]*" data-wa-number="[^"]*" data-service="[^"]*"',
               f'data-wa-generic="{form}" data-wa-number="{WHATSAPP}" data-service="{E(label)}"', t, count=1)
    t = t.replace('href="/case-studies/">Case studies</a>', f'href="{back}">{E(back_name)}</a>', 1)
    assert f'data-wa-generic="{form}"' in t and f'href="{back}"' in t
    out = repo / f"thank-you-{slug}" / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(SYNC.stamp(t, f"/thank-you-{slug}/"))
    return out


# ------------------------------------------------------- shared widgets
# Reusable interactive blocks. google_ads.py shows the hand-built versions.

HID = ' hidden=""'
TAB_ON = "border-orange bg-white shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)]"
TAB_OFF = "border-[var(--color-line)] bg-white/60 hover:border-orange"


def default_mock(it):
    """Plain illustration card for a tab that has no hand-built mock."""
    return figure(it["name"], [it.get("tag", "What you get")], (
        f'<div class="grid place-items-center rounded-2xl bg-[#fff7f3] py-10 text-orange">{svg(it["icon"], "h-12 w-12", 1.5)}</div>'
        f'<p class="mt-4 text-sm text-body">{E(it["what"])}</p>'))


def tabs_showcase(s):
    """Section 03 style: tab buttons on one side, a mock + text per tab.
    s = {id, pill, h2: (a, b), body: [..], anchor?, items: [{key, name, icon, what, best?, mock?}]}"""
    items = s["items"]
    btns = "".join(
        f'<button type="button" data-tab="{it["key"]}" aria-pressed="{"true" if i == 0 else "false"}" data-on="{TAB_ON}" data-off="{TAB_OFF}" '
        f'class="flex w-full items-center gap-3 rounded-2xl border p-3 text-left text-sm transition sm:p-5 sm:text-base {TAB_ON if i == 0 else TAB_OFF}">'
        f'<span class="grid h-9 w-9 shrink-0 place-items-center rounded-xl bg-orange/10 text-orange">{svg(it["icon"], "h-5 w-5")}</span>'
        f'<span class="font-[family-name:var(--font-display)] font-extrabold leading-tight text-ink">{E(it["name"])}</span></button>'
        for i, it in enumerate(items))
    panels = "".join(
        f'<div data-panel="{it["key"]}"{HID if i else ""}>{it.get("mock") or default_mock(it)}'
        f'<p class="mt-5 text-body"><strong class="font-semibold text-ink">{E(it["name"])}.</strong> {E(it["what"])}</p>'
        + (f'<p class="mt-2 text-sm font-semibold text-orange">{E(it["best"])}</p>' if it.get("best") else "") + "</div>"
        for i, it in enumerate(items))
    anchor = s.get("anchor", s["id"])
    return (f'<section class="section" id="{anchor}" aria-labelledby="{s["id"]}-heading">' + centered_head(s)
            + f'<div class="wrap mt-12 grid items-start gap-8 lg:grid-cols-2" data-tabs="true"><div data-reveal="true" class="grid grid-cols-2 gap-3 lg:grid-cols-1">{btns}</div>'
            f'<div data-reveal="true" style="--d:0.1s" class="lg:sticky lg:top-24">{panels}</div></div></section>')


def leak_check(title, intro, items, msgs, cta, unit="Leaks ticked"):
    """Self check: items = [(statement, why)], msgs = (none, some, most)."""
    n = len(items)
    return figure(title, ["Self check"], (
        f'<div data-leaks="true"><p class="text-sm text-body">{E(intro)}</p><div class="mt-4 grid gap-3">'
        + "".join(
            f'<label class="svc-check"><input type="checkbox" class="sr-only"/><span class="svc-box">{svg("check", "h-3.5 w-3.5", 3)}</span>'
            f'<span><span class="block text-sm font-bold text-ink">{E(t)}</span><span class="mt-0.5 block text-xs text-muted">{E(w)}</span></span></label>'
            for t, w in items)
        + '</div><div class="mt-5 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-4"><p class="flex items-baseline justify-between text-xs font-semibold uppercase tracking-wide text-muted">'
        f'<span>{E(unit)}</span><span class="font-[family-name:var(--font-display)] text-lg font-extrabold text-orange" aria-live="polite"><span data-leak-count="true">0</span> of {n}</span></p>'
        '<div class="mt-2 h-2 overflow-hidden rounded-full bg-ink/10" aria-hidden="true"><span data-leak-bar="true" class="block h-full w-0 rounded-full bg-orange transition-[width] duration-300"></span></div>'
        + "".join(f'<p data-leak-msg="{i}"{HID if i else ""} class="mt-3 text-sm text-body">{E(m)}</p>' for i, m in enumerate(msgs))
        + f'</div><a href="#contact" class="btn btn-primary svc-wrap mt-5 w-full">{E(cta)}</a></div>'))


# ---- ads + CRM ("ads only work properly when the CRM is connected")

CRM_LEADS = [("Lead 1", "Fake number", None), ("Lead 2", "Just browsing", None), ("Lead 3", "Qualified", "Sent to {p}"), ("Lead 4", "Paid", "Sent with sale value")]


def crm_box(platform):
    def rows(crm):
        out = ""
        for name, status, sent in CRM_LEADS:
            if crm:
                tag = (f'<span class="rounded-full bg-orange/10 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-orange">{E(sent.format(p=platform))}</span>' if sent
                       else '<span class="rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted">Not counted</span>')
                mid = f'<span class="text-xs font-semibold text-ink">{status}</span>'
            else:
                tag = '<span class="rounded-full bg-ink/[0.06] px-2.5 py-1 text-[10px] font-bold uppercase tracking-wide text-muted">1 conversion</span>'
                mid = '<span class="text-xs text-muted">Form filled</span>'
            out += (f'<li class="flex items-center justify-between gap-3 rounded-2xl border border-[var(--color-line)] bg-white px-4 py-3">'
                    f'<span class="grid"><span class="text-sm font-bold text-ink">{name}</span>{mid}</span>{tag}</li>')
        return f'<ul class="grid list-none gap-2.5">{out}</ul>'

    def verdict(strong, text):
        return (f'<p class="mt-4 flex items-start gap-2 rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] px-4 py-3 text-xs text-body">'
                f'{svg("target", "h-4 w-4 shrink-0 text-orange")}<span><strong class="font-semibold text-ink">{strong}</strong> {text}</span></p>')

    toggle = "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="flex-1 rounded-full px-4 py-2 text-xs font-bold transition {"bg-orange text-white" if i else "bg-white text-ink hover:text-orange"}">{label}</button>'
        for i, (k, label) in enumerate([("without", "Without CRM"), ("with", "With CRM connected")]))
    return ('<div data-tabs="true">' + figure(f"What {platform} learns from", ["Example"], (
        f'<div class="flex gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">{toggle}</div>'
        '<p class="mt-4 text-[10px] font-bold uppercase tracking-wider text-muted">Four leads from this week&#x27;s ads</p>'
        f'<div class="mt-2.5" data-panel="without" hidden="">{rows(False)}'
        + verdict(f"{E(platform)} sees 4 equal conversions,", "so it chases more form fills, including the junk ones.")
        + f'</div><div class="mt-2.5" data-panel="with">{rows(True)}'
        + verdict(f"{E(platform)} sees the 2 leads that mattered,", "so it goes after more people like your real customers.")
        + "</div>")) + "</div>")


CRM_LINKS = [("Zoho CRM", "/services/zoho-crm/"), ("HubSpot CRM", "/services/hubspot-crm/"), ("GoHighLevel", "/services/gohighlevel/")]


def crm_section(platform, cta, h2=None, body=None, bullets=None):
    links = ('<ul class="mt-7 flex list-none flex-wrap gap-2.5">' + "".join(
        f'<li><a class="inline-flex rounded-full border border-[var(--color-line)] bg-white px-4 py-2 font-[family-name:var(--font-display)] text-xs font-semibold text-ink transition hover:border-orange hover:text-orange" href="{h}">{t}</a></li>'
        for t, h in CRM_LINKS) + "</ul>")
    return split({"id": "crm", "pill": "Ads + CRM", "h2": h2 or (f"{platform} only works properly", "when your CRM is connected"),
                  "body": body or [f"{platform} learns from whatever you tell it a conversion is. If the only signal is a form fill, it goes and finds you more form fills, including the fake numbers and the people who were only browsing.",
                                   f"So on every account we connect the ads to your CRM. Each lead is saved with where it came from, your sales team updates the lead status, and the qualified leads and sales flow back into {platform} as conversions, with their value. From then on the platform goes after buyers, not forms."],
                  "bullets": bullets or ["Ad click saved with every lead", "Lead status synced from Zoho, HubSpot or GoHighLevel", "Qualified leads and sales sent back as conversions", "Reports on cost per qualified lead and cost per sale"],
                  "after": links, "cta": cta, "visual": crm_box(platform)}, dark=True)


# ---- client work: ONLY facts already published on the live home page
# (client feedback block). Never add a number here that is not on the site.

PROJECTS = {
    "yalla": {"name": "Yalla Renovation", "what": "Home renovation", "where": "Dubai, UAE", "img": "yalla-renovation-website", "channels": ["Google Ads", "Meta Ads"],
              "case": "/case-studies/yalla-renovation/",
              "facts": [("~₹10L", "Monthly Google and Meta budget"), ("Visits", "Every lead judged on site visits")],
              "story": "Renovation leads are expensive, and volume the sales team cannot close is wasted money. We run Google and Meta as one budget and judge it on leads that turn into site visits, so the team spends its time on real homeowners and villa owners."},
    "warriors": {"name": "Warrior's Cove", "what": "Martial arts academy", "where": "Minnesota, USA", "img": "warriors-cove-website", "channels": ["Google Ads", "Meta Ads"],
                 "facts": [("1+ yr", "Leads coming in without a break"), ("2", "Gyms: Minneapolis and Saint Paul")],
                 "story": "Membership enquiries are the lifeblood of the business. We have kept Google Ads and Meta Ads delivering leads continuously for over a year, run from India, with clear reporting and changes flagged before they have to ask."},
    "touch": {"name": "Touch Abroad", "what": "Career training", "where": "Ontario, Canada", "img": "touch-abroad-website", "channels": ["Website", "Google Ads", "Meta Ads"],
              "facts": [("2 yrs", "Working together"), ("1", "Owner for the site and the ads")],
              "story": "We built the website and have run the Google Ads and Meta Ads that fill enquiries for their PSW and skill based programmes ever since. One person owning both means nothing falls between two vendors, and every intake starts with a full list of people to call."},
    "elixir": {"name": "Elixir Engineering", "what": "Fire safety engineering", "where": "India", "img": "elixir-engineering-website", "channels": ["SEO", "Google Ads"],
               "facts": [("40-45", "Leads every month, SEO and Ads"), ("SEO + Ads", "Ads cover what SEO has not reached")],
               "story": "Fire safety maintenance, Form B audits, training and repairs are hard to find online. SEO got several target keywords ranking, and Google Ads covers the searches SEO has not reached yet."},
    "4s": {"name": "4S Study Abroad", "what": "Overseas education", "where": "UAE and India", "img": "4s-study-abroad-website", "channels": ["Meta Ads"], "case": "/case-studies/4s-study-abroad/",
           "facts": [("~15", "Student enquiries every day"), ("AED 3K", "Monthly Meta Ads budget")],
           "story": "For more than a year their Meta Ads have delivered roughly 15 student enquiries a day on about AED 3,000 a month. Counsellors can plan their week because the pipeline does not collapse between campaigns, and anything that starts to slip is flagged early."},
    "achievers": {"name": "Achievers Perfect Career Institute", "what": "Aviation training", "where": "Chandigarh, India", "img": "achievers-perfect-career-institute-website", "channels": ["Website", "SEO"],
                  "facts": [("Up", "Admissions across North India"), ("HP", "Himachal Pradesh, now the top source")],
                  "story": "Students searching for aviation and career training across North India were not finding the institute. We rebuilt the website and the online presence so they show up and make sense when someone compares institutes, and admissions increased across the region."},
    "bazayan": {"name": "Bazayan.ch", "what": "Pharmaceutical B2B", "where": "Switzerland", "img": "bazayan-website", "channels": ["B2B website"],
                "facts": [("Static", "Old site, dated and barely visited"), ("Clicks", "Buyers find the API range in a few")],
                "story": "A static, dated website is a poor first impression for a pharmaceutical API supplier. We replaced it with a modern B2B site that lays out the API portfolio clearly, so buyers understand what they supply within a few clicks."},
    "trust": {"name": "Trust Legal", "what": "Legal services", "where": "New Delhi, India", "img": "trust-legal-website", "channels": ["Website", "Maintenance"],
              "facts": [("2 yrs", "Maintenance and technical care"), ("Rebuilt", "Website rebuilt from scratch")],
              "story": "A law firm cannot afford a website that breaks or looks neglected. We rebuilt theirs from scratch and have handled maintenance and every technical requirement for two years: an issue is raised, it gets fixed, and they get back to their clients."},
    # Meta figures: Meta Ads Manager screenshots (see pages/case_ourknots.py)
    "ourknots": {"name": "OurKnots", "what": "D2C ecommerce", "where": "India", "img": "ourknots-website", "channels": ["Shopify", "Meta Ads", "Google Ads"],
                 "facts": [("₹3.84L", "Store sales, Sep 2026"), ("5.13x", "Meta ROAS, up from 0.72x")],
                 "story": "A range of laces, trims and wedding accessories with no online sales at all. We built the Shopify store, then turned its ads around: from a 0.72x Meta ROAS in February 2025 to 152 orders and ₹3.84 lakh of store sales in September 2026.",
                 "case": "/case-studies/ourknots/"},
}


def shot(p):
    widths = [384, 640, 750, 828, 1080, 1200, 1920]
    srcset = ", ".join(f'/img/{w}/clients/{p["img"]}.webp {w}w' for w in widths)
    return (f'<div class="overflow-hidden rounded-2xl border border-[var(--color-line)] bg-white"><div class="flex items-center gap-1.5 border-b border-[var(--color-line)] px-3 py-2" aria-hidden="true">'
            '<span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span><span class="h-2 w-2 rounded-full bg-ink/15"></span></div>'
            f'<img alt="{E(p["name"])} website, a {E(p["what"].lower())} client of Sushant Rana" loading="lazy" decoding="async" width="1400" height="765" '
            f'class="block h-auto w-full" sizes="(min-width: 1024px) 560px, 92vw" srcSet="{srcset}" src="/img/1200/clients/{p["img"]}.webp"/></div>')


def projects_section(keys, h2, body):
    """Tabs of client projects. keys pick from PROJECTS; h2 = (a, b)."""
    ps = [dict(PROJECTS[k], key=k) for k in keys]
    btns = "".join(
        f'<button type="button" data-tab="{p["key"]}" aria-pressed="{"true" if i == 0 else "false"}" data-on="{TAB_ON}" data-off="{TAB_OFF}" '
        f'class="w-full rounded-2xl border p-3 text-left transition sm:p-5 {TAB_ON if i == 0 else TAB_OFF}">'
        f'<span class="block font-[family-name:var(--font-display)] text-sm font-extrabold text-ink sm:text-base">{E(p["name"])}</span>'
        f'<span class="mt-0.5 block text-xs text-muted">{E(p["what"])} · {E(p["where"])}</span></button>'
        for i, p in enumerate(ps))
    panels = "".join(
        f'<div data-panel="{p["key"]}"{HID if i else ""}><article class="card overflow-hidden p-5 md:p-6">{shot(p)}'
        '<div class="mt-5 flex flex-wrap gap-2">' + "".join(
            f'<span class="rounded-full border border-orange/30 bg-orange/10 px-3 py-1 text-[11px] font-semibold text-orange">{E(c)}</span>' for c in p["channels"]) + '</div>'
        f'<h3 class="mt-4 text-xl font-extrabold text-ink">{E(p["name"])}</h3><p class="text-sm text-muted">{E(p["what"])} · {E(p["where"])}</p>'
        '<div class="mt-4 grid grid-cols-2 gap-3">' + "".join(
            f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5"><p class="font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">{E(n)}</p>'
            f'<p class="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{E(l)}</p></div>' for n, l in p["facts"]) + '</div>'
        f'<p class="mt-4 text-body">{E(p["story"])}</p>'
        + (f'<a href="{p["case"]}" class="btn btn-outline mt-5">Read the case study</a>' if p.get("case") else "")
        + '</article></div>'
        for i, p in enumerate(ps))
    return ('<section class="section" id="work" aria-labelledby="work-heading">'
            + centered_head({"id": "work", "pill": "Client work", "h2": h2, "body": [body]})
            + f'<div class="wrap mt-12 grid items-start gap-8 lg:grid-cols-[1.05fr_0.95fr]" data-tabs="true">'
            f'<div data-reveal="true" class="grid grid-cols-2 gap-3 lg:order-2 lg:grid-cols-1 lg:self-start">{btns}</div>'
            f'<div data-reveal="true" style="--d:0.1s" class="lg:order-1">{panels}</div></div></section>')



# ------------------------------------------------------------ journey chart
# One y-axis per view (bars and line share the unit). Hover/focus a month for
# its numbers; partial months are striped, missing months are left empty.

BAR, LINE = "#ff4d00", "#2f6fdb"  # validated pair (dataviz validate_palette.js)


def _nice(v):
    if v <= 0:
        return 1
    mag = 10 ** (len(str(int(v))) - 1)
    for m in (1, 1.5, 2, 2.5, 3, 4, 5, 6, 8, 10):
        if v <= m * mag:
            return m * mag
    return 10 * mag


def chart_view(months, view):
    """view: {bars, bar_name, line?, line_name?, fmt, partial?, note?}; values may be None."""
    bars, line = view["bars"], view.get("line")
    fmt = view["fmt"]
    partial = view.get("partial") or [False] * len(months)
    top = _nice(max([v for v in bars if v] + [v for v in (line or []) if v] + [1]) * 1.05)
    n = len(months)
    grid = "".join(
        f'<span class="absolute left-0 right-0 border-t border-[var(--color-line)]" style="bottom:{q * 25}%"></span>'
        f'<span class="absolute -left-1 -translate-x-full text-[9px] font-semibold text-muted" style="bottom:calc({q * 25}% - 6px)">{E(fmt(top * q / 4))}</span>'
        for q in range(5))
    cols = ""
    for i, m in enumerate(months):
        b = bars[i]
        lv = line[i] if line else None
        edge = ' data-edge="l"' if i < 3 else ' data-edge="r"' if i >= n - 3 else ""
        tip = f'<span class="block font-bold">{E(m)}</span>'
        if b is None and lv is None:
            tip += '<span class="block text-white/70">No data yet</span>'
        if b is not None:
            tip += f'<span class="block"><span style="color:#ffb08f">■</span> {E(view["bar_name"])}: {E(fmt(b))}{" (partial)" if partial[i] else ""}</span>'
        if lv is not None:
            tip += f'<span class="block"><span style="color:#9dbcf2">■</span> {E(view["line_name"])}: {E(fmt(lv))}</span>'
        bar = (f'<span class="absolute bottom-0 left-[18%] right-[18%] rounded-t {"svc-partial" if partial[i] else ""}" style="height:{b / top * 100:.2f}%;background:{BAR}"></span>'
               if b else "")
        cols += (f'<div class="svc-col relative h-full flex-1" tabindex="0"{edge} aria-label="{E(m)}">{bar}'
                 f'<span class="svc-tip">{tip}</span></div>')
    svg = ""
    if line:
        segs, cur = [], []
        for i, v in enumerate(line):
            if v is None:
                if cur:
                    segs.append(cur)
                cur = []
            else:
                cur.append(f"{(i + 0.5) / n * 1000:.1f},{1000 - v / top * 1000:.1f}")
        if cur:
            segs.append(cur)
        svg = ('<svg class="pointer-events-none absolute inset-0 h-full w-full" viewBox="0 0 1000 1000" preserveAspectRatio="none" aria-hidden="true">'
               + "".join(f'<polyline points="{" ".join(sg)}" fill="none" stroke="{LINE}" stroke-width="2.5" vector-effect="non-scaling-stroke" stroke-linejoin="round"/>' for sg in segs)
               + "</svg>")
    ticks = "".join(
        f'<span class="min-w-0 flex-1 text-center text-[9px] font-semibold text-muted">{E(m) if (i % 3 == 0 or i == n - 1) else ""}</span>'
        for i, m in enumerate(months))
    legend = (f'<span class="flex items-center gap-1.5"><span class="h-2.5 w-3 rounded-sm" style="background:{BAR}"></span>{E(view["bar_name"])}</span>'
              + (f'<span class="flex items-center gap-1.5"><span class="h-0.5 w-4 rounded" style="background:{LINE}"></span>{E(view["line_name"])}</span>' if line else "")
              + ('<span class="flex items-center gap-1.5"><span class="svc-partial h-2.5 w-3 rounded-sm" style="background:#ff4d00"></span>Partial month</span>' if any(partial) else ""))
    rows = "".join(
        f'<tr class="border-b border-[var(--color-line)] last:border-0"><td class="py-1.5 pr-3">{E(m)}</td><td class="py-1.5 pr-3 text-right">{E(fmt(bars[i])) if bars[i] is not None else "–"}{" *" if partial[i] else ""}</td>'
        + (f'<td class="py-1.5 text-right">{E(fmt(line[i])) if line[i] is not None else "–"}</td>' if line else "") + "</tr>"
        for i, m in enumerate(months))
    table = (f'<details class="mt-4 text-xs text-body"><summary class="cursor-pointer font-semibold text-ink">View as a table</summary>'
             f'<table class="mt-2 w-full"><thead><tr class="text-left text-muted"><th class="py-1.5 pr-3 font-semibold">Month</th>'
             f'<th class="py-1.5 pr-3 text-right font-semibold">{E(view["bar_name"])}</th>'
             + (f'<th class="py-1.5 text-right font-semibold">{E(view["line_name"])}</th>' if line else "")
             + f'</tr></thead><tbody>{rows}</tbody></table>'
             + ('<p class="mt-2 text-muted">* Partial: part of that month&#x27;s campaign list was outside the screenshot.</p>' if any(partial) else "")
             + "</details>")
    note = f'<p class="mt-3 text-xs text-muted">{E(view["note"])}</p>' if view.get("note") else ""
    return (f'<div class="flex flex-wrap gap-x-4 gap-y-1 text-[11px] font-semibold text-muted">{legend}</div>'
            f'<div class="relative ml-10 mt-5 h-56 sm:h-64" role="img" aria-label="{E(view.get("aria", view["bar_name"]))}">{grid}'
            f'<div class="absolute inset-0 flex">{cols}</div>{svg}</div>'
            f'<div class="ml-10 mt-2 flex">{ticks}</div>{note}{table}')


def journey_chart(title, tags, months, views):
    """views: [(key, tab label, view dict)] - tabs switch views, one axis each."""
    tabs = "".join(
        f'<button type="button" data-tab="{k}" aria-pressed="{"true" if i == 0 else "false"}" data-on="bg-orange text-white" data-off="bg-white text-ink hover:text-orange" '
        f'class="rounded-full px-3 py-1.5 text-[11px] font-bold transition {"bg-orange text-white" if i == 0 else "bg-white text-ink hover:text-orange"}">{E(label)}</button>'
        for i, (k, label, _) in enumerate(views))
    panels = "".join(f'<div data-panel="{k}"{HID if i else ""} class="mt-4">{chart_view(months, v)}</div>' for i, (k, _, v) in enumerate(views))
    return ('<div data-tabs="true">' + figure(title, tags, (
        f'<div class="flex flex-wrap gap-1 rounded-full border border-[var(--color-line)] bg-white p-1">{tabs}</div>{panels}')) + "</div>")


def form_section(p, s):
    """The step form, inline near the end of a page (case studies keep the hero for proof)."""
    return (f'<section class="section" id="form" aria-labelledby="form-heading"><div class="wrap grid items-start gap-14 lg:grid-cols-2 svc-split">'
            f'<div data-reveal="true">{pill(s["pill"])}<h2 id="form-heading" class="mt-5 text-[clamp(1.8rem,4vw,3.1rem)] font-extrabold text-ink">{hl(*s["h2"])}</h2>'
            f'{paras(s["body"], "mt-5 max-w-xl text-body")}{bullets(s["bullets"]) if s.get("bullets") else ""}'
            f'<a href="/contact/book-strategy-call/" data-no-popup="true" class="btn btn-outline mt-9">Book a strategy call instead</a></div>'
            f'<div data-reveal="true" style="--d:0.1s">{step_form(p)}</div></div></section>')



def featured_case(s):
    """Big card for a channel hub: chart + facts + link to the full case study.
    s = {id, pill, h2, body, name, what, url, facts: [(num, label)], story, chart}"""
    facts = "".join(
        f'<div class="rounded-2xl border border-[var(--color-line)] bg-[#fff7f3] p-3.5"><p class="font-[family-name:var(--font-display)] text-xl font-extrabold text-orange">{E(n)}</p>'
        f'<p class="mt-0.5 text-[10px] font-semibold uppercase tracking-wider text-muted">{E(l)}</p></div>' for n, l in s["facts"])
    return (f'<section class="section" id="{s["id"]}" aria-labelledby="{s["id"]}-heading">' + centered_head(s)
            + f'<div class="wrap mt-12 grid items-start gap-8 lg:grid-cols-2 svc-split"><div data-reveal="true">{s["chart"]}</div>'
            f'<div data-reveal="true" style="--d:0.1s"><article class="card p-6 md:p-8">{pill(s["what"])}'
            f'<h3 class="mt-4 text-2xl font-extrabold text-ink">{E(s["name"])}</h3><p class="mt-3 text-body">{E(s["story"])}</p>'
            f'<div class="mt-5 grid grid-cols-2 gap-3">{facts}</div>'
            f'<a href="{s["url"]}" class="btn btn-primary mt-6">Read the full case study</a></article></div></div></section>')


if __name__ == "__main__":
    repo = Path(sys.argv[1])
    load_shell(repo)  # the spec's sections need WALKER and COUNTRY
    spec = runpy.run_path(sys.argv[2], init_globals={"L": sys.modules[__name__]})
    page = spec["PAGE"]
    print(build(repo, page))
    print(build_thanks(repo, page))
