/*
 * sushantrana.com — every interactive behaviour on the static site.
 *
 * The HTML already contains every state (menus, popups, all form steps, all
 * tab panels), closed with the `hidden` attribute. This file only flips
 * attributes and classes; the animations themselves live in style.css.
 * No build step, no framework: edit and upload.
 */
(() => {
  "use strict";

  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduced = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const split = (s) => (s || "").split(/\s+/).filter(Boolean);
  const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));

  /* ---- where this visitor came from (sent with every lead) ----
   * Kept from the first page of the visit for 90 days; a new ad click or
   * campaign link replaces it, so the lead is credited to the latest one. */
  const ATTR_KEY = "sr_attr";
  const ATTR_PARAMS = ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "gclid", "gbraid", "wbraid", "fbclid"];
  const attribution = (() => {
    let saved = null;
    try {
      saved = JSON.parse(localStorage.getItem(ATTR_KEY) || "null");
    } catch {
      /* storage blocked: attribute this page view only */
    }
    if (saved && Date.now() - saved.t > 90 * 864e5) saved = null;
    const q = new URLSearchParams(location.search);
    const tagged = ATTR_PARAMS.some((k) => q.get(k));
    const ref = document.referrer && new URL(document.referrer).host !== location.host ? document.referrer : "";
    if (saved && !tagged) return saved;
    const a = { t: Date.now(), landing_page: location.pathname + location.search, referrer: ref };
    ATTR_PARAMS.forEach((k) => q.get(k) && (a[k] = q.get(k)));
    a.gclid = a.gclid || a.gbraid || a.wbraid || "";
    try {
      localStorage.setItem(ATTR_KEY, JSON.stringify(a));
    } catch {
      /* fine: still sent with a form on this page */
    }
    return a;
  })();

  /** Replace one class set with another. */
  const cls = (el, add, remove) => {
    split(remove).forEach((c) => el.classList.remove(c));
    split(add).forEach((c) => el.classList.add(c));
  };
  /** Elements carry their two looks as data-on / data-off class strings. */
  const swap = (el, on) => cls(el, on ? el.dataset.on : el.dataset.off, on ? el.dataset.off : el.dataset.on);

  /** Runs fn once when el scrolls into view (same trigger as the old
   *  useInViewport hook: 10% visible, 5% bottom margin). */
  const onView = (el, fn) => {
    if (!("IntersectionObserver" in window)) return fn(el);
    const io = new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) {
          io.disconnect();
          fn(el);
        }
      },
      { rootMargin: "0px 0px -5% 0px", threshold: 0.1 }
    );
    io.observe(el);
  };

  /** Show / hide with the CSS exit animation (.closing) before `hidden`. */
  const show = (el) => {
    clearTimeout(el._t);
    el.classList.remove("closing");
    el.hidden = false;
  };
  const hide = (el, ms = 200) => {
    if (el.hidden) return;
    if (reduced) return void (el.hidden = true);
    el.classList.add("closing");
    clearTimeout(el._t);
    el._t = setTimeout(() => {
      el.hidden = true;
      el.classList.remove("closing");
    }, ms);
  };
  /** Restart a one-shot CSS animation class. */
  const replay = (el, c) => {
    if (reduced) return;
    el.classList.remove(c);
    void el.offsetWidth;
    el.classList.add(c);
  };

  /* ------------------------------------------------------ smooth scroll */

  let lenis = null;
  if (!reduced && window.Lenis) {
    lenis = new window.Lenis({
      duration: 1.1,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });
    const loop = (t) => {
      lenis.raf(t);
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }
  const lockScroll = (on) => {
    document.body.style.overflow = on ? "hidden" : "";
    if (lenis) on ? lenis.stop() : lenis.start();
  };

  /* ---------------------------------------------------- reveal on scroll */

  $$("[data-reveal], [data-reveal-words], [data-slide], [data-grow-group]").forEach((el) =>
    onView(el, () => el.classList.add("is-in"))
  );

  /* -------------------------------------------------------- count-ups */

  const countUp = (el, target, render, dur) => {
    if (reduced) return void (el.textContent = render(target));
    el.textContent = render(0);
    onView(el, () => {
      const t0 = performance.now();
      const tick = (t) => {
        const p = Math.min(1, (t - t0) / dur);
        el.textContent = render(target * (1 - Math.pow(1 - p, 3)));
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  };

  $$("[data-count]").forEach((el) => {
    const d = el.dataset;
    const dec = +d.dec || 0;
    countUp(el, +d.count, (n) => `${d.prefix || ""}${n.toFixed(dec)}${d.suffix || ""}`, +d.dur || 1400);
  });

  // "72%" counts to 72, "4.2x" to 4.2, "₹1,499" keeps its prefix and grouping.
  $$("[data-anim-num]").forEach((el) => {
    const m = /^([^\d]*)([\d,]+(?:\.\d+)?)(.*)$/.exec(el.textContent.trim());
    if (!m) return;
    const [, pre, digits, post] = m;
    const dec = digits.includes(".") ? digits.split(".")[1].length : 0;
    const grouped = digits.includes(",");
    const fmt = (n) =>
      grouped
        ? n.toLocaleString("en-IN", { minimumFractionDigits: dec, maximumFractionDigits: dec })
        : n.toFixed(dec);
    countUp(el, Number(digits.replace(/,/g, "")), (n) => pre + fmt(n) + post, +el.dataset.dur || 1300);
  });

  /* --------------------------------------------------------------- nav */

  const navRoot = $("[data-nav-root]");
  if (navRoot) {
    const bar = $("[data-nav]", navRoot);
    const logo = $("img[data-on]", bar);
    let scrolled = null;
    const onScroll = () => {
      const s = scrollY > 120;
      if (s === scrolled) return;
      scrolled = s;
      swap(bar, s);
      if (logo) swap(logo, s);
    };
    addEventListener("scroll", onScroll, { passive: true });
    onScroll();

    // desktop dropdowns + mega panel
    let openKey = null;
    let timer = 0;
    const panelsOf = (k) => $$("[data-dd-panel]", navRoot).filter((p) => p.dataset.ddPanel === k);
    const btnOf = (k) => $$("[data-dd-btn]", navRoot).find((b) => b.dataset.ddBtn === k);
    const setOpen = (k) => {
      if (k === openKey) return;
      if (openKey) {
        panelsOf(openKey).forEach((p) => hide(p));
        const b = btnOf(openKey);
        b.setAttribute("aria-expanded", "false");
        swap(b, false);
      }
      openKey = k;
      if (k) {
        panelsOf(k).forEach(show);
        const b = btnOf(k);
        b.setAttribute("aria-expanded", "true");
        swap(b, true);
      }
    };
    const hoverOpen = (k) => {
      clearTimeout(timer);
      setOpen(k);
    };
    const hoverClose = () => {
      clearTimeout(timer);
      timer = setTimeout(() => setOpen(null), 130);
    };

    $$("[data-dd]", navRoot).forEach((li) => {
      const k = li.dataset.dd;
      li.addEventListener("mouseenter", () => hoverOpen(k));
      const b = $("[data-dd-btn]", li);
      b.addEventListener("click", () => setOpen(openKey === k ? null : k));
      b.addEventListener("focus", () => setOpen(k));
    });
    $$("[data-dd-panel]", navRoot).forEach((p) => {
      if (p.closest("[data-dd]")) return; // flat menus live inside their <li>
      p.addEventListener("mouseenter", () => hoverOpen(p.dataset.ddPanel));
      p.addEventListener("mouseleave", hoverClose);
    });
    navRoot.addEventListener("mouseleave", hoverClose);

    // mobile drawer
    const toggle = $("[data-mobile-toggle]", navRoot);
    const drawer = $("[data-mobile-menu]", navRoot);
    const setMobile = (on) => {
      toggle.setAttribute("aria-expanded", String(on));
      if (on) return show(drawer);
      hide(drawer);
      $$("[data-acc-btn]", drawer).forEach((b) => {
        b.setAttribute("aria-expanded", "false");
        $("[data-acc-panel]", b.closest("[data-acc-group]")).classList.remove("open");
      });
    };
    toggle.addEventListener("click", () => setMobile(drawer.hidden));

    addEventListener("keydown", (e) => {
      if (e.key !== "Escape") return;
      setOpen(null);
      setMobile(false);
    });
  }

  /* -------------------------------------------------------- accordions */

  $$("[data-acc-btn]").forEach((b) =>
    b.addEventListener("click", () => {
      const item = b.closest("[data-acc-group]");
      const open = b.getAttribute("aria-expanded") !== "true";
      const group = item.dataset.accGroup;
      // a named group (the mobile menu) keeps one section open at a time;
      // a bare data-acc-group (FAQ items) opens independently
      if (open && group && group !== "true") {
        $$(`[data-acc-group="${group}"]`).forEach((o) => {
          if (o === item) return;
          $("[data-acc-btn]", o).setAttribute("aria-expanded", "false");
          $("[data-acc-panel]", o).classList.remove("open");
        });
      }
      b.setAttribute("aria-expanded", String(open));
      $("[data-acc-panel]", item).classList.toggle("open", open);
    })
  );

  /* ------------------------------------------------------ tabs, filters */

  const own = (box, sel, attr) => $$(sel, box).filter((el) => el.closest(attr) === box);

  $$("[data-tabs]").forEach((box) => {
    const tabs = own(box, "[data-tab]", "[data-tabs]");
    const panels = own(box, "[data-panel]", "[data-tabs]");
    tabs.forEach((t) =>
      t.addEventListener("click", () => {
        if (t.getAttribute("aria-pressed") === "true") return;
        tabs.forEach((o) => {
          const on = o === t;
          o.setAttribute("aria-pressed", String(on));
          swap(o, on);
          $$("[data-acc-panel]", o).forEach((p) => p.classList.toggle("open", on));
        });
        panels.forEach((p) => {
          const on = p.dataset.panel === t.dataset.tab;
          p.hidden = !on;
          if (on) replay(p, p.dataset.anim === "pop" ? "pop-in" : "tab-in");
        });
      })
    );
  });

  $$("[data-filters]").forEach((box) => {
    const btns = $$("[data-filter]", box);
    btns.forEach((b) =>
      b.addEventListener("click", () => {
        const f = b.dataset.filter;
        btns.forEach((o) => {
          o.setAttribute("aria-pressed", String(o === b));
          swap(o, o === b);
        });
        $$("[data-tag]", box).forEach((c) => {
          const on = f === "all" || c.dataset.tag === f;
          const was = !c.hidden;
          c.hidden = !on;
          if (on && !was) replay(c, "card-in");
        });
      })
    );
  });

  /* ----------------------------------------------- rotating hero question */

  const rot = $("[data-rotate]");
  if (rot && !reduced) {
    const items = $$(":scope > span", rot);
    let i = 0;
    setInterval(() => {
      const cur = items[i];
      i = (i + 1) % items.length;
      const next = items[i];
      cur.classList.add("rot-out");
      setTimeout(() => {
        cur.hidden = true;
        cur.classList.remove("rot-out");
        next.classList.add("rot-pre");
        next.hidden = false;
        void next.offsetWidth;
        next.classList.remove("rot-pre");
      }, 550);
    }, 4400);
  }

  /* ------------------------------------- automation demo: deal hopping */

  $$("[data-deal-board]").forEach((board) => {
    const deals = $$("[data-deal]", board);
    let stage = 0;
    if (reduced || deals.length < 2) return;
    onView(board, () =>
      setInterval(() => {
        const from = deals[stage];
        stage = (stage + 1) % deals.length;
        const to = deals[stage];
        const a = from.getBoundingClientRect();
        from.hidden = true;
        to.hidden = false;
        const b = to.getBoundingClientRect();
        // FLIP: start where the old card was, then let the transition settle it
        to.style.transition = "none";
        to.style.transform = `translate(${a.left - b.left}px, ${a.top - b.top}px)`;
        void to.offsetWidth;
        to.style.transition = "";
        to.style.transform = "";
      }, 1600)
    );
  });

  /* ------------------------------------------------ footer glow, to-top */

  $$("[data-glow]").forEach((el) =>
    el.addEventListener("mousemove", (e) => {
      const r = el.getBoundingClientRect();
      el.style.setProperty("--mx", `${e.clientX - r.left}px`);
      el.style.setProperty("--my", `${e.clientY - r.top}px`);
    })
  );

  const toTop = $("[data-back-to-top]");
  if (toTop) {
    let on = false;
    const sync = () => {
      const s = scrollY > 600;
      if (s === on) return;
      on = s;
      s ? show(toTop) : hide(toTop);
    };
    addEventListener("scroll", sync, { passive: true });
    sync();
    toTop.addEventListener("click", () =>
      lenis ? lenis.scrollTo(0) : scrollTo({ top: 0, behavior: "smooth" })
    );
  }

  /* ================================================================ forms */

  /* ---- validation (same rules as lib/validation.ts) ---- */

  const EMAIL_RE = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,63}$/;
  const DISPOSABLE = new Set([
    "10minutemail.com", "20minutemail.com", "33mail.com", "guerrillamail.com",
    "guerrillamail.info", "guerrillamail.net", "sharklasers.com", "grr.la",
    "mailinator.com", "mailinator.net", "trashmail.com", "trashmail.net",
    "temp-mail.org", "tempmail.com", "tempmailo.com", "tempr.email",
    "throwawaymail.com", "yopmail.com", "yopmail.net", "getnada.com",
    "nada.email", "dispostable.com", "maildrop.cc", "fakeinbox.com",
    "spamgourmet.com", "mytemp.email", "moakt.com", "emailondeck.com",
    "mohmal.com", "inboxbear.com", "burnermail.io", "tempinbox.com",
    "mailnesia.com", "spam4.me", "byom.de", "discard.email", "spambog.com",
    "einrot.com", "harakirimail.com", "tmail.ws", "linshiyouxiang.net",
  ]);
  const COMMON_DOMAINS = [
    "gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.in", "yahoo.co.uk",
    "hotmail.com", "hotmail.co.uk", "outlook.com", "live.com", "msn.com",
    "icloud.com", "me.com", "aol.com", "proton.me", "protonmail.com",
    "zoho.com", "rediffmail.com", "gmx.com", "mail.com", "yandex.com",
  ];

  function editDistance(a, b, max = 2) {
    if (Math.abs(a.length - b.length) > max) return max + 1;
    let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      const cur = [i];
      let best = i;
      for (let j = 1; j <= b.length; j++) {
        const v = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        cur[j] = v;
        if (v < best) best = v;
      }
      if (best > max) return max + 1;
      prev = cur;
    }
    return prev[b.length];
  }

  function suggestDomain(d) {
    if (COMMON_DOMAINS.includes(d)) return null;
    let best = null;
    let bestDist = 3;
    for (const c of COMMON_DOMAINS) {
      const dist = editDistance(d, c);
      if (dist < bestDist) {
        bestDist = dist;
        best = c;
      }
    }
    return bestDist <= 2 ? best : null;
  }

  function validateEmail(raw) {
    const email = raw.trim();
    if (!email) return { ok: false, error: "Email is required." };
    if (/\s/.test(email)) return { ok: false, error: "An email address can't contain spaces." };
    if (email.length > 254) return { ok: false, error: "That email address is too long." };
    const at = email.split("@").length - 1;
    if (at === 0) return { ok: false, error: "That's not an email address — it needs an @ sign." };
    if (at > 1) return { ok: false, error: "An email address can only have one @ sign." };
    const [local, domain] = email.split("@");
    if (!local) return { ok: false, error: "Add the part before the @ sign." };
    if (local.length > 64) return { ok: false, error: "The part before the @ is too long." };
    if (!domain) return { ok: false, error: "Add the part after the @ sign, like gmail.com." };
    if (!domain.includes(".")) return { ok: false, error: "The domain needs a dot in it, like gmail.com." };
    if (email.includes("..")) return { ok: false, error: "An email address can't contain two dots in a row." };
    if (local.startsWith(".") || local.endsWith("."))
      return { ok: false, error: "An email address can't start or end the name with a dot." };
    if (!EMAIL_RE.test(email)) return { ok: false, error: "That doesn't look like a valid email address." };
    const d = domain.toLowerCase();
    if (DISPOSABLE.has(d))
      return { ok: false, error: "Please use a permanent email address — I need to be able to reply." };
    const s = suggestDomain(d);
    if (s) return { ok: true, hint: `Did you mean ${local}@${s}?` };
    return { ok: true };
  }

  // libphonenumber is 250 kB, so it only loads once someone uses a phone field.
  let lpn = null;
  const loadPhoneLib = () =>
    (lpn ||= new Promise((res, rej) => {
      const s = document.createElement("script");
      s.src = "/assets/vendor/libphonenumber-max.js";
      s.onload = () => res(window.libphonenumber);
      s.onerror = rej;
      document.head.appendChild(s);
    }));

  async function validatePhone(select, raw) {
    const opt = select.selectedOptions[0];
    if (!opt) return { ok: false, error: "Please choose a country." };
    const national = raw.replace(/\D+/g, "");
    if (!national)
      return { ok: false, error: raw.trim() ? "A phone number can only contain digits." : "Phone number is required." };
    if (national.length < 4) return { ok: false, error: "That number is too short." };
    if (national.length > 15) return { ok: false, error: "That number is too long." };
    let lib;
    try {
      lib = await loadPhoneLib();
    } catch {
      return { ok: true }; // the server checks again; never block a lead on a CDN hiccup
    }
    const p = lib.parsePhoneNumberFromString(national, select.value);
    if (!p || !p.isValid())
      return {
        ok: false,
        error: `That isn't a valid ${opt.dataset.name} number. Check the digits, without the +${opt.dataset.dial}.`,
      };
    if (["PREMIUM_RATE", "SHARED_COST", "VOICEMAIL"].includes(p.getType()))
      return { ok: false, error: "Please give a number I can actually call you back on." };
    return { ok: true };
  }

  /* ---- field messages and borders ---- */

  const MS = {
    idle: "border-[var(--color-line)] hover:border-orange",
    open: "border-orange",
    invalid: "border-red-500",
  };

  const box = (form, f) => $(`[data-field="${f}"]`, form);

  function mark(form, f, bad) {
    const b = box(form, f);
    if (!b) return;
    const multi = $("[data-multi]", b);
    if (multi) {
      multi.dataset.invalid = bad ? "1" : "";
      return paintMulti(multi);
    }
    const wrap = $("[data-wrap]", b);
    const el = wrap || $("input:not([type=hidden]), select, textarea", b);
    if (el && !(el.type === "radio" || el.type === "checkbox")) {
      const [err, ok] = wrap ? [form.dataset.wrapErr, form.dataset.wrapOk] : [form.dataset.err, form.dataset.ok];
      cls(el, bad ? err : ok, bad ? ok : err);
    }
    const input = $("input:not([type=hidden]):not([type=radio]):not([type=checkbox]), select, textarea", b);
    if (input) bad ? input.setAttribute("aria-invalid", "true") : input.removeAttribute("aria-invalid");
  }

  /** Error (red) or hint (orange) line under a field; no message clears it. */
  function note(form, f, msg, hint = false) {
    const b = box(form, f);
    if (!b) return;
    let p = $(":scope > [data-note]", b);
    if (!msg) {
      if (p) p.remove();
      return mark(form, f, false);
    }
    if (!p) {
      p = document.createElement("p");
      p.dataset.note = "";
      b.appendChild(p);
    }
    const mt = form.closest('[data-step-form="maintenance"]') ? "mt-1.5" : "mt-1";
    p.className = `${mt} text-xs font-medium ${hint ? "text-orange" : "text-red-600"}`;
    hint ? p.removeAttribute("role") : p.setAttribute("role", "alert");
    p.textContent = msg;
    mark(form, f, !hint);
  }

  const formError = (form, msg) => {
    const p = $("[data-form-error]", form);
    p.textContent = msg || "";
    p.hidden = !msg;
  };

  const clearAll = (form) => {
    $$("[data-note]", form).forEach((p) => p.remove());
    $$("[data-field]", form).forEach((b) => mark(form, b.dataset.field, false));
    formError(form, null);
  };

  const checkEmail = (form, input) => {
    if (!input.value.trim()) return true;
    const r = validateEmail(input.value);
    note(form, "email", r.ok ? r.hint : r.error, r.ok);
    return r.ok;
  };

  const checkPhone = async (form, input, select) => {
    if (!input.value.trim()) return true;
    const r = await validatePhone(select, input.value);
    note(form, "phone", r.ok ? null : r.error);
    return r.ok;
  };

  /** Country picker: repaint flag + dial code over the native select. */
  function wireCountry(select, onChange) {
    const wrap = select.parentElement;
    const paint = () => {
      const o = select.selectedOptions[0];
      $("[data-flag]", wrap).textContent = o.dataset.flag;
      $("[data-dial]", wrap).textContent = o.dataset.dial;
    };
    select.addEventListener("change", () => {
      paint();
      if (onChange) onChange();
    });
    select._paint = paint;
    paint();
  }

  const dialOf = (select) => select.selectedOptions[0].dataset.dial;

  /** Grey placeholder text until a real option is picked. */
  $$("[data-placeholder-select]").forEach((s) => {
    const paint = () => s.classList.toggle("text-muted", !s.value);
    s.addEventListener("change", paint);
    s._paint = paint;
  });

  const busyBtn = (btn, busy, text) => {
    btn.disabled = busy;
    btn.textContent = busy ? text : btn.dataset.label;
  };

  /* ---- GTM dataLayer (same shape as lib/datalayer.ts) ---- */

  function pushLead(formName, fields, user) {
    window.dataLayer = window.dataLayer || [];
    const flat = {};
    for (const [k, v] of Object.entries(fields)) flat[k] = Array.isArray(v) ? v.join(", ") : v ?? "";
    window.dataLayer.push({
      event: `lead_${formName}`,
      form_name: formName,
      form_page: location.pathname,
      ...flat,
      user_data: { name: user.name || "", email: user.email || "", phone_number: user.phone || "" },
    });
  }

  async function postLead(payload, form) {
    const res = await fetch("/api/lead.php", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...payload, form, attribution, sourcePath: location.pathname }),
    });
    const data = await res.json().catch(() => ({}));
    return { ok: res.ok && data.ok, data };
  }

  const NETWORK = "Network problem. Please check your connection and retry.";
  const saveLead = (key, value) => {
    try {
      sessionStorage.setItem(key, JSON.stringify(value));
    } catch {
      /* storage blocked: the thank-you page falls back to a generic message */
    }
  };

  /* ---- the consultation form (popup + blog sidebar) ---- */

  $$("form[data-lead-form]").forEach((form) => {
    const el = form.elements;
    const select = $("[data-country]", form);
    const btn = $("button[type=submit]", form);
    let busy = false;

    wireCountry(select, () => {
      note(form, "phone", null);
      if (el.phone.value.trim()) checkPhone(form, el.phone, select);
    });
    el.name.addEventListener("input", () => note(form, "name", null));
    el.email.addEventListener("input", () => note(form, "email", null));
    el.email.addEventListener("blur", () => checkEmail(form, el.email));
    el.phone.addEventListener("input", () => note(form, "phone", null));
    el.phone.addEventListener("blur", () => checkPhone(form, el.phone, select));
    el.service.addEventListener("change", () => note(form, "service", null));

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (busy) return;
      busy = true;
      busyBtn(btn, true, "Checking…");
      formError(form, null);

      const fd = new FormData(form);
      const str = (k) => String(fd.get(k) || "");
      const name = str("name").trim();
      const done = () => {
        busy = false;
        busyBtn(btn, false);
      };

      const missing = {};
      if (!name) missing.name = "Please tell me your name.";
      if (!str("email").trim()) missing.email = "Email is required.";
      if (!str("phone").trim()) missing.phone = "Phone number is required.";
      if (!str("service")) missing.service = "Please choose a service.";
      if (Object.keys(missing).length) {
        Object.entries(missing).forEach(([f, m]) => note(form, f, m));
        return done();
      }

      const [okE, okP] = await Promise.all([checkEmail(form, el.email), checkPhone(form, el.phone, select)]);
      if (!okE || !okP) return done();

      try {
        const { ok, data } = await postLead({
          name,
          email: str("email"),
          phone: str("phone"),
          phoneCountry: select.value,
          business: fd.get("business"),
          service: str("service"),
          enquiryType: str("enquiryType"),
          message: fd.get("message"),
          company_website: str("company_website"),
        }, "consultation");
        if (!ok) {
          const msg = data.error || "Could not send. Please try again.";
          data.field === "email" || data.field === "phone" ? note(form, data.field, msg) : formError(form, msg);
          return done();
        }
        pushLead(
          "consultation",
          { enquiry_type: str("enquiryType"), service: str("service"), business: str("business"), message: str("message") },
          { name, email: str("email"), phone: `+${dialOf(select)}${str("phone").replace(/\D/g, "")}` }
        );
        location.href = "/thank-you-consultation/";
      } catch {
        formError(form, NETWORK);
        done();
      }
    });
  });

  /* ---- multi-select dropdowns (maintenance form) ---- */

  function paintMulti(ms) {
    const btn = $("[data-multi-btn]", ms);
    const open = btn.getAttribute("aria-expanded") === "true";
    cls(btn, ms.dataset.invalid ? MS.invalid : open ? MS.open : MS.idle, `${MS.invalid} ${MS.open} ${MS.idle}`);
    const vals = ms._vals || [];
    const text = $("[data-multi-text]", ms);
    text.textContent =
      vals.length === 0 ? ms.dataset.placeholder : vals.length === 1 ? vals[0] : `${vals[0]} +${vals.length - 1} more`;
    cls(text, vals.length ? "text-ink" : "text-muted", vals.length ? "text-muted" : "text-ink");
  }

  $$("[data-multi]").forEach((ms) => {
    const btn = $("[data-multi-btn]", ms);
    const list = $("[data-multi-list]", ms);
    ms._vals = [];
    const setOpen = (on) => {
      list.hidden = !on;
      btn.setAttribute("aria-expanded", String(on));
      paintMulti(ms);
    };
    ms._close = () => setOpen(false);
    btn.addEventListener("click", () => setOpen(list.hidden));
    // keep click order, the way the React version listed the picks
    list.addEventListener("change", (e) => {
      const v = e.target.value;
      ms._vals = e.target.checked ? [...ms._vals, v] : ms._vals.filter((x) => x !== v);
      paintMulti(ms);
      ms.dispatchEvent(new Event("multichange", { bubbles: true }));
    });
    document.addEventListener("mousedown", (e) => {
      if (!list.hidden && !ms.contains(e.target)) setOpen(false);
    });
    // capture phase, so Escape closes this list without also closing the popup
    document.addEventListener(
      "keydown",
      (e) => {
        if (e.key === "Escape" && !list.hidden) {
          e.stopPropagation();
          setOpen(false);
        }
      },
      true
    );
    ms._reset = () => {
      ms._vals = [];
      ms.dataset.invalid = "";
      setOpen(false);
    };
  });

  /* ---- three-step forms (Shopify quote, website maintenance) ---- */

  const STEP_CLS = {
    dotOn: "bg-orange text-white",
    dotOff: "bg-ink/10 text-muted",
    labelOn: "text-ink",
    labelOff: "text-muted",
    lineOn: "bg-orange",
    lineOff: "bg-ink/10",
  };

  const SHOPIFY_KEY = "shopify-lead";
  const MAINT_KEY = "maintenance-lead";

  $$("[data-step-form]").forEach((root) => {
    const kind = root.dataset.stepForm;
    const form = $("form", root);
    const el = form.elements;
    const select = $("[data-country]", form);
    const steps = $$("[data-step]", form);
    const back = $("[data-back]", form);
    const next = $("[data-next]", form);
    const submit = $("[data-submit]", form);
    const stepNames = (form.dataset.steps || "").split("|");
    const ticks = root.hasAttribute("data-ticks");
    let step = 0;
    let busy = false;

    const go = (n) => {
      step = n;
      steps.forEach((s) => (s.hidden = +s.dataset.step !== n));
      $$("[data-step-dot]", root).forEach((d) => {
        const i = +d.dataset.stepDot;
        cls(d, i <= n ? STEP_CLS.dotOn : STEP_CLS.dotOff, i <= n ? STEP_CLS.dotOff : STEP_CLS.dotOn);
        if (ticks) {
          $("[data-num]", d).hidden = i < n;
          $("[data-tick]", d).hidden = i >= n;
        }
      });
      $$("[data-step-label]", root).forEach((l) => {
        const on = +l.dataset.stepLabel <= n;
        cls(l, on ? STEP_CLS.labelOn : STEP_CLS.labelOff, on ? STEP_CLS.labelOff : STEP_CLS.labelOn);
      });
      $$("[data-step-line]", root).forEach((l) => {
        const on = +l.dataset.stepLine < n;
        cls(l, on ? STEP_CLS.lineOn : STEP_CLS.lineOff, on ? STEP_CLS.lineOff : STEP_CLS.lineOn);
      });
      const num = $("[data-step-num]", root);
      if (num) {
        num.textContent = n + 1;
        $("[data-step-name]", root).textContent = stepNames[n];
      }
      back.hidden = n === 0;
      next.hidden = n === steps.length - 1;
      submit.hidden = n !== steps.length - 1;
    };

    wireCountry(select, () => note(form, "phone", null));

    // Any edit clears that field's error and the form-level one.
    const clearOn = (name, field = name) => {
      const input = el[name];
      if (!input) return;
      const ev = input.tagName === "SELECT" || input instanceof RadioNodeList ? "change" : "input";
      (input instanceof RadioNodeList ? Array.from(input) : [input]).forEach((i) =>
        i.addEventListener(ev, () => {
          note(form, field, null);
          formError(form, null);
        })
      );
    };

    const val = (k) => (el[k] ? String(el[k].value || "") : "");

    /* -- per-form rules -- */

    const shopify = {
      async validate(n) {
        if (n === 0) {
          const errs = {};
          if (!val("name").trim()) errs.name = "Please tell me your name.";
          if (!val("company").trim()) errs.company = "Please add your business or brand name.";
          const e = validateEmail(val("email"));
          if (!e.ok) errs.email = e.error;
          const p = await validatePhone(select, val("phone"));
          if (!p.ok) errs.phone = p.error;
          ["name", "company", "email", "phone"].forEach((f) => note(form, f, errs[f] || null));
          return !Object.keys(errs).length;
        }
        if (n === 1 && (!val("service") || !val("platform") || !val("revenue"))) {
          formError(form, "Please answer the required questions.");
          return false;
        }
        return true;
      },
      busyNext: true,
      finalCheck() {
        if (!val("timeline") || !val("budget")) {
          formError(form, "Please pick a timeline and a budget range.");
          return false;
        }
        return true;
      },
      payload() {
        const message = [
          `What they need: ${val("service")}`,
          `Current platform: ${val("platform")}`,
          `Monthly revenue: ${val("revenue")}`,
          val("products") && `Number of products: ${val("products")}`,
          `Timeline: ${val("timeline")}`,
          `Budget: ${val("budget")}`,
          val("source") && `Heard about me via: ${val("source")}`,
          val("details") && `\nProject notes:\n${val("details")}`,
        ]
          .filter(Boolean)
          .join("\n");
        return {
          name: val("name"),
          email: val("email"),
          phone: val("phone"),
          phoneCountry: select.value,
          business: val("company"),
          service: "Shopify Store Development",
          enquiryType: "service",
          message,
          company_website: val("website"),
        };
      },
      success() {
        const dial = dialOf(select);
        const f = (k) => val(k);
        pushLead(
          "shopify_store_development",
          {
            company: f("company"), service: f("service"), platform: f("platform"), revenue: f("revenue"),
            products: f("products"), timeline: f("timeline"), budget: f("budget"), source: f("source"), details: f("details"),
          },
          { name: f("name"), email: f("email"), phone: `+${dial}${f("phone").replace(/\D/g, "")}` }
        );
        saveLead(SHOPIFY_KEY, {
          name: f("name"), company: f("company"), email: f("email"), phone: `+${dial} ${f("phone")}`,
          service: f("service"), platform: f("platform"), revenue: f("revenue"), products: f("products"),
          timeline: f("timeline"), budget: f("budget"), details: f("details"),
        });
        location.href = "/thank-you-shopify-store-development/";
      },
      // a rejected email or phone goes back to step 1, next to the field
      fieldStep: 0,
      sending: "Sending…",
    };

    const multi = (name) => $(`[data-multi] input[name="${name}"]`, form)?.closest("[data-multi]");
    const picks = (name) => (multi(name) ? multi(name)._vals : []);
    const ACCESS = [
      ["domain", "Domain"],
      ["hosting", "Hosting"],
      ["backend", "Backend"],
    ];
    const access = (k) => {
      const c = $(`input[name="access-${k}"]:checked`, form);
      return c ? c.value : "";
    };
    const accessText = () => ACCESS.map(([k, label]) => `${label} login: ${access(k)}`).join(", ");

    const maintenance = {
      async validate(n) {
        if (n === 0) {
          const errs = {};
          if (!val("platform")) errs.platform = "Pick the platform your site runs on.";
          if (!picks("problems").length) errs.problems = "Pick at least one.";
          if (!picks("reasons").length) errs.reason = "Pick at least one reason.";
          ["platform", "problems", "reason"].forEach((f) => note(form, f, errs[f] || null));
          return !Object.keys(errs).length;
        }
        if (n === 1) {
          const ok = ACCESS.every(([k]) => access(k));
          note(form, "access", ok ? null : "Please answer all three.");
          return ok;
        }
        return true;
      },
      async finalCheck() {
        const errs = {};
        if (!val("name").trim()) errs.name = "Please tell me your name.";
        const e = validateEmail(val("email"));
        if (!e.ok) errs.email = e.error;
        const p = await validatePhone(select, val("phone"));
        if (!p.ok) errs.phone = p.error;
        ["name", "email", "phone"].forEach((f) => note(form, f, errs[f] || null));
        return !Object.keys(errs).length;
      },
      payload() {
        const plan = val("plan");
        const message = [
          val("site") && `Website: ${val("site")}`,
          `Platform: ${val("platform")}`,
          `Problems: ${picks("problems").join(", ")}`,
          `Why maintenance: ${picks("reasons").join(", ")}`,
          plan && `Plan picked on the page: ${plan}`,
          `Access: ${accessText()}`,
        ]
          .filter(Boolean)
          .join("\n");
        return {
          name: val("name"),
          email: val("email"),
          phone: val("phone"),
          phoneCountry: select.value,
          business: val("site"),
          service: "Website Maintenance",
          enquiryType: "service",
          message,
          company_website: val("honeypot"),
        };
      },
      success() {
        const dial = dialOf(select);
        pushLead(
          "website_maintenance",
          {
            website: val("site"), platform: val("platform"), problems: picks("problems"), reasons: picks("reasons"),
            plan: val("plan"), domain_login: access("domain"), hosting_login: access("hosting"), backend_login: access("backend"),
          },
          { name: val("name"), email: val("email"), phone: `+${dial}${val("phone").replace(/\D/g, "")}` }
        );
        saveLead(MAINT_KEY, {
          name: val("name"), email: val("email"), phone: `+${dial} ${val("phone")}`, website: val("site"),
          platform: val("platform"), problems: picks("problems").join(", "), reason: picks("reasons").join(", "),
          plan: val("plan"), access: accessText(),
        });
        location.href = "/thank-you-website-maintenance/";
      },
      fieldStep: null,
      sending: "Sending…",
    };

    const rules = kind === "shopify" ? shopify : maintenance;

    if (kind === "shopify") {
      ["name", "email", "phone", "company", "service", "platform", "revenue", "timeline", "budget"].forEach((n) => clearOn(n));
    } else {
      ["platform", "name", "email", "phone"].forEach((n) => clearOn(n));
      ACCESS.forEach(([k]) => clearOn(`access-${k}`, "access"));
      form.addEventListener("multichange", (e) => {
        const name = $("input", e.target).name;
        note(form, name === "problems" ? "problems" : "reason", null);
        formError(form, null);
      });
    }

    next.addEventListener("click", async () => {
      if (busy) return;
      if (rules.busyNext && step === 0) {
        busy = true;
        busyBtn(next, true, "Checking…");
        const ok = await rules.validate(step);
        busy = false;
        busyBtn(next, false);
        if (ok) go(step + 1);
        return;
      }
      if (await rules.validate(step)) go(step + 1);
    });
    back.addEventListener("click", () => go(step - 1));

    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      if (busy) return;
      // Enter inside an earlier step means "Next", not "send".
      if (step < steps.length - 1) return next.click();
      if (kind === "shopify" && !(await rules.finalCheck())) return;
      busy = true;
      busyBtn(submit, true, rules.sending);
      formError(form, null);
      const done = () => {
        busy = false;
        busyBtn(submit, false);
      };
      if (kind === "maintenance" && !(await rules.finalCheck())) return done();

      try {
        const { ok, data } = await postLead(
          rules.payload(),
          kind === "shopify" ? "shopify_store_development" : "website_maintenance"
        );
        if (!ok) {
          const msg = data.error || "Could not send. Please try again.";
          if (data.field === "email" || data.field === "phone") {
            if (rules.fieldStep !== null) go(rules.fieldStep);
            note(form, data.field, msg);
          } else formError(form, msg);
          return done();
        }
        rules.success();
      } catch {
        formError(form, NETWORK);
        done();
      }
    });

    // Opening a popup starts the form fresh, like the old remount did.
    root._reset = (plan) => {
      form.reset();
      clearAll(form);
      $$("[data-multi]", form).forEach((m) => m._reset());
      $$("[data-placeholder-select]", form).forEach((s) => s._paint && s._paint());
      if (select._paint) select._paint();
      if (el.plan) el.plan.value = plan || "";
      busy = false;
      busyBtn(submit, false);
      busyBtn(next, false);
      go(0);
    };

    go(0);
  });

  /* -------------------------------------------------------------- popups */

  const modal = $("[data-modal]");
  if (modal) {
    const quote = modal.dataset.modal === "quote";
    const open = (plan) => {
      const f = $("[data-step-form]", modal);
      if (f && f._reset) f._reset(plan);
      show(modal);
      lockScroll(true);
    };
    const close = () => {
      if (modal.hidden) return;
      hide(modal);
      lockScroll(false);
    };

    // Capture phase, same triggers as the React popups.
    document.addEventListener(
      "click",
      (e) => {
        const t = e.target.closest("a, button");
        if (!t || t.closest("[data-modal-panel]")) return;
        const href = t.getAttribute("href") || "";
        const txt = (t.textContent || "").trim().toLowerCase();
        const hit =
          t.hasAttribute("data-consult") ||
          href === "#contact" ||
          href.startsWith("/contact") ||
          txt.startsWith("book") ||
          (quote && (t.hasAttribute("data-quote") || txt.startsWith("get your free")));
        if (!hit) return;
        e.preventDefault();
        e.stopPropagation();
        open(t.dataset.plan);
      },
      true
    );
    $$("[data-modal-close]", modal).forEach((c) => c.addEventListener("click", close));
    addEventListener("keydown", (e) => e.key === "Escape" && close());
  }

  /* ------------------------------------------------ Shopify product cards */

  const inr = (n) => `₹${n.toLocaleString("en-IN")}`;
  const ADD = {
    idle: "bg-orange text-white",
    adding: "bg-orange-600 text-white",
    added: "bg-[#15803d] text-white",
    disabled: "cursor-not-allowed bg-ink/10 text-muted",
  };
  const ALL_ADD = Object.values(ADD).join(" ");

  /** Add → Adding… → Added → back, like a real AJAX add (nothing is sent). */
  function addCycle(btn, onDone) {
    const text = $("[data-add-text]", btn);
    const tick = $("[data-check]", btn);
    const set = (state, label) => {
      cls(btn, ADD[state], ALL_ADD);
      text.textContent = label;
      tick.hidden = state !== "added";
    };
    btn._busy = true;
    set("adding", "Adding…");
    setTimeout(() => {
      set("added", "Added");
      setTimeout(() => {
        btn._busy = false;
        set("idle", btn.dataset.idle);
        onDone();
      }, 1500);
    }, 900);
    return set;
  }

  $$("[data-pack-card]").forEach((card) => {
    const packs = JSON.parse(card.dataset.packs);
    const btns = $$("[data-pack]", card);
    const pick = (i) => {
      btns.forEach((b, j) => {
        b.setAttribute("aria-pressed", String(i === j));
        swap(b, i === j);
      });
      $("[data-total]", card).textContent = inr(packs[i].total);
      $("[data-unit]", card).textContent = inr(packs[i].unit);
    };
    btns.forEach((b, i) => b.addEventListener("click", () => pick(i)));
    const add = $("[data-add]", card);
    add.addEventListener("click", () => !add._busy && addCycle(add, () => pick(0)));
  });

  $$("[data-colour-card]").forEach((card) => {
    const names = JSON.parse(card.dataset.colours);
    const price = +card.dataset.price;
    const mrp = +card.dataset.mrp;
    const swatches = $$("[data-colour]", card);
    const stepper = $("[data-stepper]", card);
    const add = $("[data-add]", card);
    let qty = 1;

    const paintQty = () => {
      $("[data-qty]", card).textContent = qty;
      $("[data-price-now]", card).textContent = inr(price * qty);
      $("[data-price-mrp]", card).textContent = inr(mrp * qty);
    };
    const pick = (i) => {
      swatches.forEach((s, j) => {
        s.setAttribute("aria-pressed", String(i === j));
        swap(s, i === j);
      });
      $("[data-colour-name]", card).textContent = i === null ? "Pick a colour" : names[i];
      swap(stepper, i !== null);
      add.disabled = i === null;
      if (!add._busy) {
        cls(add, i === null ? ADD.disabled : ADD.idle, ALL_ADD);
        $("[data-add-text]", add).textContent = i === null ? "Pick a colour" : add.dataset.idle;
      }
    };
    swatches.forEach((s, i) => s.addEventListener("click", () => pick(i)));
    $$("[data-qty-step]", card).forEach((b) =>
      b.addEventListener("click", () => {
        qty = clamp(qty + +b.dataset.qtyStep, 1, 9);
        paintQty();
      })
    );
    add.addEventListener("click", () => {
      if (add._busy || add.disabled) return;
      addCycle(add, () => {
        qty = 1;
        paintQty();
        pick(null);
      });
    });
  });

  /* ---------------------------------------- Shopify scroll walkthrough */

  const PROC = {
    dotOn: "border-orange bg-orange text-white",
    dotOff: "border-ink/15 bg-white text-muted group-hover:border-orange",
    labelOn: "text-ink",
    labelOff: "text-muted group-hover:text-orange",
    cardOn: "border-orange shadow-[0_26px_60px_-30px_rgba(255,77,0,0.5)] lg:-translate-y-2",
    cardOff: "border-[var(--color-line)] lg:opacity-70",
  };

  $$("[data-process]").forEach((wrap) => {
    const cards = $$("[data-proc-card]", wrap);
    const btns = $$("[data-proc-btn]", wrap);
    const tools = $$("[data-tool]", wrap);
    const walker = $("[data-walker]", wrap);
    const walk = $("[data-proc-walk]", wrap);
    const fill = $("[data-proc-fill]", wrap);
    const n = cards.length;
    const mq = matchMedia("(max-width: 1023px)");
    let progress = 0;
    let active = -1;
    let stopWalk = 0;
    let frame = 0;

    // Phone layout: the cards are a deck on one spot, the active one on top.
    const stack = () =>
      cards.forEach((li, i) => {
        if (!mq.matches) return li.removeAttribute("style");
        const o = i - active;
        li.style.zIndex = 40 - Math.abs(o);
        li.style.transform =
          o >= 0
            ? `translateY(${Math.min(o, 3) * 9}px) scale(${1 - Math.min(o, 3) * 0.025})`
            : `translateY(${o * 24}px) scale(${1 + o * 0.02})`;
        li.style.opacity = o < 0 ? 0 : 1;
        li.style.transition = "transform 550ms cubic-bezier(0.16,1,0.3,1), opacity 400ms ease";
      });

    const render = () => {
      walk.style.transform = `translateX(calc(${progress} * (100% - 130px)))`;
      fill.style.width = `calc(${progress} * 75%)`;
      const a = clamp(Math.floor(progress * n), 0, n - 1);
      if (a === active) return;
      active = a;
      btns.forEach((b, i) => {
        a === i ? b.setAttribute("aria-current", "step") : b.removeAttribute("aria-current");
        const dot = $("[data-proc-dot]", b);
        const label = $("[data-proc-label]", b);
        cls(dot, i <= a ? PROC.dotOn : PROC.dotOff, i <= a ? PROC.dotOff : PROC.dotOn);
        cls(label, i === a ? PROC.labelOn : PROC.labelOff, i === a ? PROC.labelOff : PROC.labelOn);
      });
      cards.forEach((li, i) => {
        const art = li.firstElementChild;
        cls(art, i === a ? PROC.cardOn : PROC.cardOff, i === a ? PROC.cardOff : PROC.cardOn);
      });
      tools.forEach((t, i) => (t.style.display = i === a ? "" : "none"));
      stack();
    };

    const onScroll = () => {
      if (frame) return;
      frame = requestAnimationFrame(() => {
        frame = 0;
        const r = wrap.getBoundingClientRect();
        const travel = r.height - innerHeight;
        if (travel <= 0) return;
        progress = clamp(-r.top / travel, 0, 1);
        if (!reduced) walker.classList.add(walker.dataset.walkCls);
        clearTimeout(stopWalk);
        stopWalk = setTimeout(() => walker.classList.remove(walker.dataset.walkCls), 220);
        render();
      });
    };

    btns.forEach((b, i) =>
      b.addEventListener("click", () => {
        progress = i / (n - 1);
        render();
      })
    );
    mq.addEventListener("change", stack);
    addEventListener("scroll", onScroll, { passive: true });
    addEventListener("resize", onScroll);
    render();
    onScroll();
  });

  /* ---------------------------------------------- prices in local money */

  const inrEls = $$("[data-inr]");
  if (inrEls.length) {
    const EUR = ["Amsterdam", "Athens", "Berlin", "Bratislava", "Brussels", "Dublin", "Helsinki", "Lisbon",
      "Ljubljana", "Luxembourg", "Madrid", "Malta", "Monaco", "Paris", "Riga", "Rome", "Tallinn", "Vienna",
      "Vilnius", "Zagreb"];
    const CAD = ["Toronto", "Vancouver", "Edmonton", "Winnipeg", "Halifax", "St_Johns", "Regina", "Montreal",
      "Moncton", "Whitehorse", "Yellowknife", "Iqaluit"];
    const ZONES = {
      "Asia/Kolkata": "INR", "Asia/Calcutta": "INR", "Asia/Dubai": "AED", "Asia/Riyadh": "SAR",
      "Asia/Qatar": "QAR", "Asia/Kuwait": "KWD", "Asia/Bahrain": "BHD", "Asia/Muscat": "OMR",
      "Asia/Singapore": "SGD", "Europe/London": "GBP", "Pacific/Auckland": "NZD", "Africa/Johannesburg": "ZAR",
    };
    EUR.forEach((c) => (ZONES[`Europe/${c}`] = "EUR"));
    CAD.forEach((c) => (ZONES[`America/${c}`] = "CAD"));

    const tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
    const currency = ZONES[tz] || (tz.startsWith("Australia/") ? "AUD" : "USD");
    const nice = (n) => (n >= 1000 ? Math.round(n / 10) * 10 : n >= 100 ? Math.round(n / 5) * 5 : Math.round(n));

    if (currency !== "INR") {
      fetch("https://open.er-api.com/v6/latest/INR")
        .then((r) => r.json())
        .then((d) => {
          const rate = d && d.result === "success" ? d.rates[currency] : 0;
          if (!rate) return;
          const convert = (digits, compact) => {
            const amount = Number(digits.replace(/,/g, "")) * (compact ? 1000 : 1);
            return new Intl.NumberFormat("en", {
              style: "currency",
              currency,
              maximumFractionDigits: 0,
              notation: compact && amount * rate >= 10000 ? "compact" : "standard",
            }).format(nice(amount * rate));
          };
          inrEls.forEach((el) => {
            el.textContent = el.dataset.inr.replace(/₹(\d+(?:,\d+)*)(K)?/g, (_, d, k) => convert(d, !!k));
          });
          $$('[data-price-note="inr"]').forEach((n) => (n.hidden = true));
          $$('[data-price-note="foreign"]').forEach((n) => (n.hidden = false));
          $$("[data-cur]").forEach((n) => (n.textContent = currency));
        })
        .catch(() => {
          /* offline or rate limit: rupee prices stay, which is still correct */
        });
    }
  }

  /* ------------------------------------- thank-you pages → WhatsApp */

  const wa = $("[data-wa-thanks]");
  if (wa) {
    const shop = wa.dataset.waThanks === "shopify";
    const key = shop ? SHOPIFY_KEY : MAINT_KEY;
    const delay = +wa.dataset.delay;
    let lead = null;
    try {
      const raw = sessionStorage.getItem(key);
      if (raw) lead = JSON.parse(raw);
      // Shopify clears at once; maintenance keeps it until the hand-off.
      if (shop) sessionStorage.removeItem(key);
    } catch {
      /* malformed or blocked: generic message */
    }

    const line = (label, v) => (v ? `${label}: ${v}` : null);
    const message = shop
      ? lead && lead.name
        ? [
            "Hi Sushant, I just requested a Shopify store quote on sushantrana.com.",
            "",
            line("Name", lead.name), line("Business", lead.company), line("Email", lead.email),
            line("Phone", lead.phone), line("What I need", lead.service), line("Current platform", lead.platform),
            line("Monthly revenue", lead.revenue), line("Products", lead.products), line("Timeline", lead.timeline),
            line("Budget", lead.budget), lead.details ? `\nNotes: ${lead.details}` : null,
          ].filter((l) => l !== null).join("\n")
        : "Hi Sushant, I just requested a Shopify store quote on your website and would like to talk about my store."
      : lead && lead.name
        ? [
            "Hi Sushant, I just sent a website maintenance request on sushantrana.com.",
            "",
            line("Name", lead.name), line("Email", lead.email), line("Phone", lead.phone),
            line("Website", lead.website), line("Platform", lead.platform), line("Problems", lead.problems),
            line("Why maintenance", lead.reason), line("Plan", lead.plan), line("Access", lead.access),
          ].filter((l) => l !== null).join("\n")
        : "Hi Sushant, I just sent a website maintenance request on your website and would like to talk about my site.";

    const number = shop ? "918289051732" : "919501110124";
    const url = `https://wa.me/${number}?text=${encodeURIComponent(message)}`;
    $$("[data-wa-link]", wa).forEach((a) => {
      a.href = url;
      a.hidden = false;
    });

    // ?preview=1 holds the page so it can be checked without the bounce.
    const preview = new URLSearchParams(location.search).has("preview");
    if (!shop) {
      $$("[data-auto]", wa).forEach((n) => (n.hidden = false));
      $$("[data-manual]", wa).forEach((n) => (n.hidden = true));
      const ring = $("[data-ring]", wa);
      if (ring) ring.classList.add("run");
    }
    if (shop && preview) return;

    let left = Math.round(delay / 1000);
    const paint = () => {
      $$("[data-left]", wa).forEach((n) => (n.textContent = left));
      $$("[data-sec]", wa).forEach((n) => (n.textContent = left === 1 ? "second" : "seconds"));
    };
    paint();
    setInterval(() => {
      left = Math.max(0, left - 1);
      paint();
    }, 1000);
    if (!preview)
      setTimeout(() => {
        try {
          sessionStorage.removeItem(key);
        } catch {
          /* ignore */
        }
        location.href = url;
      }, delay);
  }
})();
