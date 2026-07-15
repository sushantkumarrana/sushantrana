/* ==========================================================================
   Sushant Rana — shared behaviour (vanilla JS, no dependencies)
   Interaction engine + rotating-question hero + consultation popup.
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     FORM ENDPOINT — wire your form backend here (Formspree / Basin /
     Make webhook / your own API). Popup + consultation page POST JSON:
     { fullName, email, phone, company, website, service, challenge, source }
     then redirect to thank-you.html. See NOTES.md → "Wiring the form endpoint".
  ------------------------------------------------------------------ */
  var FORM_ENDPOINT = "https://example.com/api/consultation"; // REPLACE: real form endpoint

  var REDUCE = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var CAN_HOVER = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  window.dataLayer = window.dataLayer || [];

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  /* ==================================================================
     1. Sticky header
  ================================================================== */
  function initHeader() {
    var header = document.querySelector(".site-header");
    if (!header) return;
    var update = function () { header.classList.toggle("is-scrolled", window.scrollY > 8); };
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  /* ==================================================================
     2. Desktop nav dropdowns
  ================================================================== */
  function initDropdowns() {
    var items = document.querySelectorAll(".nav__item--dropdown");
    items.forEach(function (item) {
      var toggle = item.querySelector(".nav__toggle");
      if (!toggle) return;
      toggle.addEventListener("click", function () {
        var open = item.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        items.forEach(function (o) { if (o !== item) { o.classList.remove("is-open"); var t = o.querySelector(".nav__toggle"); if (t) t.setAttribute("aria-expanded", "false"); } });
      });
      item.addEventListener("keydown", function (e) {
        if (e.key === "Escape") { item.classList.remove("is-open"); toggle.setAttribute("aria-expanded", "false"); toggle.focus(); }
      });
      item.addEventListener("focusout", function () {
        window.requestAnimationFrame(function () {
          if (!item.contains(document.activeElement)) { item.classList.remove("is-open"); toggle.setAttribute("aria-expanded", "false"); }
        });
      });
    });
    document.addEventListener("click", function (e) {
      items.forEach(function (item) { if (!item.contains(e.target)) { item.classList.remove("is-open"); var t = item.querySelector(".nav__toggle"); if (t) t.setAttribute("aria-expanded", "false"); } });
    });
  }

  /* ==================================================================
     3. Mobile drawer
  ================================================================== */
  function initDrawer() {
    var toggle = document.querySelector(".drawer-toggle");
    var drawer = document.getElementById("mobile-drawer");
    if (!toggle || !drawer) return;
    function setOpen(open) {
      drawer.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      document.body.style.overflow = open ? "hidden" : "";
    }
    toggle.addEventListener("click", function () { setOpen(!drawer.classList.contains("is-open")); });
    drawer.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer.classList.contains("is-open")) { setOpen(false); toggle.focus(); } });
    drawer.querySelectorAll(".drawer__accordion-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var sub = document.getElementById(btn.getAttribute("aria-controls"));
        var open = btn.getAttribute("aria-expanded") === "true";
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        if (sub) sub.classList.toggle("is-open", !open);
      });
    });
  }

  /* ==================================================================
     4. Scroll reveal (IntersectionObserver, graceful fallback)
  ================================================================== */
  function initReveal() {
    var els = document.querySelectorAll(".reveal, .reveal-l, .reveal-r, .reveal-scale, .reveal-blur");
    if (!els.length) return;
    if (REDUCE || !("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("in"); });
      return;
    }
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        var el = e.target;
        var d = el.getAttribute("data-delay");
        if (d) el.style.transitionDelay = d + "ms";
        el.classList.add("in");
        obs.unobserve(el);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
    // Failsafe: if a paint pass was skipped (e.g. tab restored), reveal anything already on-screen.
    window.setTimeout(function () {
      els.forEach(function (el) {
        if (el.classList.contains("in")) return;
        var r = el.getBoundingClientRect();
        if (r.top < (window.innerHeight || 800) && r.bottom > 0) el.classList.add("in");
      });
    }, 1200);
  }

  /* ==================================================================
     5. Number counters (fire once at 40% visible)
  ================================================================== */
  function initCounters() {
    var nums = document.querySelectorAll("[data-count]");
    if (!nums.length) return;
    function fmt(v, dec, comma) {
      var s = dec ? v.toFixed(dec) : String(Math.round(v));
      if (comma) { var p = s.split("."); p[0] = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ","); s = p.join("."); }
      return s;
    }
    function run(el) {
      var target = parseFloat(el.getAttribute("data-count")) || 0;
      var dec = parseInt(el.getAttribute("data-decimals") || "0", 10);
      var pre = el.getAttribute("data-prefix") || "";
      var suf = el.getAttribute("data-suffix") || "";
      var comma = el.getAttribute("data-format") === "comma";
      if (REDUCE) { el.textContent = pre + fmt(target, dec, comma) + suf; return; }
      var dur = 1500, start = null;
      function tick(now) {
        if (start === null) start = now;
        var p = Math.min((now - start) / dur, 1);
        var eased = 1 - Math.pow(1 - p, 3);
        el.textContent = pre + fmt(target * eased, dec, comma) + suf;
        if (p < 1) window.requestAnimationFrame(tick);
        else el.textContent = pre + fmt(target, dec, comma) + suf;
      }
      window.requestAnimationFrame(tick);
    }
    if (!("IntersectionObserver" in window)) { nums.forEach(run); return; }
    var io = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (e) { if (e.isIntersecting) { run(e.target); obs.unobserve(e.target); } });
    }, { threshold: 0.4 });
    nums.forEach(function (el) { io.observe(el); });
  }

  /* ==================================================================
     6. Tabs ([data-tabs] > [data-tab] / [data-panel])
  ================================================================== */
  var TAB_GROUP = 0;
  function initTabs() {
    document.querySelectorAll("[data-tabs]").forEach(function (group) {
      var gi = TAB_GROUP++;
      var tabs = Array.prototype.slice.call(group.querySelectorAll("[data-tab]"));
      var panels = Array.prototype.slice.call(group.querySelectorAll("[data-panel]"));
      tabs.forEach(function (t) {
        var key = t.getAttribute("data-tab");
        var panel = panels.filter(function (p) { return p.getAttribute("data-panel") === key; })[0];
        if (!t.id) t.id = "tab-" + gi + "-" + key;
        if (panel) {
          if (!panel.id) panel.id = "panel-" + gi + "-" + key;
          t.setAttribute("aria-controls", panel.id);
          panel.setAttribute("aria-labelledby", t.id);
          panel.setAttribute("tabindex", "0");
        }
      });
      function activate(key) {
        tabs.forEach(function (t) {
          var on = t.getAttribute("data-tab") === key;
          t.setAttribute("aria-selected", String(on));
          t.setAttribute("tabindex", on ? "0" : "-1");
        });
        panels.forEach(function (p) {
          var hidden = p.getAttribute("data-panel") !== key;
          p.classList.toggle("is-hidden", hidden);
          if (hidden) p.setAttribute("hidden", ""); else p.removeAttribute("hidden");
        });
      }
      tabs.forEach(function (t, i) {
        t.addEventListener("click", function () { activate(t.getAttribute("data-tab")); });
        t.addEventListener("keydown", function (e) {
          if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
          e.preventDefault();
          var dir = e.key === "ArrowRight" ? 1 : -1;
          var next = tabs[(i + dir + tabs.length) % tabs.length];
          next.focus(); activate(next.getAttribute("data-tab"));
        });
      });
      if (tabs[0]) activate(tabs[0].getAttribute("data-tab"));
    });
  }

  /* ==================================================================
     7. Accordion (.acc-trigger toggles next .acc-panel). data-acc-single
        on the .acc container closes siblings.
  ================================================================== */
  function initAccordion() {
    document.querySelectorAll(".acc-trigger").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var panel = btn.nextElementSibling;
        var open = btn.getAttribute("aria-expanded") === "true";
        var group = btn.closest("[data-acc-single]");
        if (group && !open) {
          group.querySelectorAll(".acc-trigger[aria-expanded='true']").forEach(function (other) {
            other.setAttribute("aria-expanded", "false");
            if (other.nextElementSibling) other.nextElementSibling.style.maxHeight = null;
          });
        }
        btn.setAttribute("aria-expanded", open ? "false" : "true");
        if (panel) panel.style.maxHeight = open ? null : panel.scrollHeight + "px";
      });
    });
    window.addEventListener("resize", function () {
      document.querySelectorAll(".acc-trigger[aria-expanded='true']").forEach(function (btn) {
        var p = btn.nextElementSibling; if (p) p.style.maxHeight = p.scrollHeight + "px";
      });
    }, { passive: true });
  }

  /* ==================================================================
     8. FAQ category filter (chips filter [data-acc-cat] items)
  ================================================================== */
  function initFaqCats() {
    var groups = document.querySelectorAll("[data-faq]");
    groups.forEach(function (group) {
      var chips = group.querySelectorAll(".filter-chip[data-cat]");
      var items = group.querySelectorAll("[data-acc-cat]");
      if (!chips.length) return;
      chips.forEach(function (chip) {
        chip.addEventListener("click", function () {
          var key = chip.getAttribute("data-cat");
          chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
          items.forEach(function (it) {
            var show = key === "all" || it.getAttribute("data-acc-cat") === key;
            it.style.display = show ? "" : "none";
          });
        });
      });
    });
  }

  /* ==================================================================
     9. Blog / case-study filter chips
  ================================================================== */
  function initFilter() {
    document.querySelectorAll("[data-filter-group]").forEach(function (group) {
      var chips = group.querySelectorAll(".filter-chip[data-filter]");
      var cards = group.querySelectorAll("[data-cat]");
      if (!chips.length || !cards.length) return;
      chips.forEach(function (chip) {
        chip.addEventListener("click", function () {
          var key = chip.getAttribute("data-filter");
          chips.forEach(function (c) { c.setAttribute("aria-pressed", c === chip ? "true" : "false"); });
          cards.forEach(function (card) {
            var cats = (card.getAttribute("data-cat") || "").split(" ");
            var show = key === "all" || cats.indexOf(key) !== -1;
            card.style.display = show ? "" : "none";
          });
        });
      });
    });
  }

  /* ==================================================================
     10. Tilt (fine pointer, non-reduced-motion only)
  ================================================================== */
  function initTilt() {
    if (REDUCE || !CAN_HOVER) return;
    document.querySelectorAll("[data-tilt]").forEach(function (card) {
      var strength = parseFloat(card.getAttribute("data-tilt")) || 5;
      card.addEventListener("mousemove", function (e) {
        var r = card.getBoundingClientRect();
        var px = (e.clientX - r.left) / r.width - 0.5;
        var py = (e.clientY - r.top) / r.height - 0.5;
        card.style.transform = "perspective(900px) rotateX(" + (-py * strength).toFixed(2) + "deg) rotateY(" + (px * strength).toFixed(2) + "deg)";
      });
      card.addEventListener("mouseleave", function () { card.style.transform = ""; });
    });
  }

  /* ==================================================================
     11. Parallax (throttled, transform only)
  ================================================================== */
  function initParallax() {
    if (REDUCE) return;
    var els = Array.prototype.slice.call(document.querySelectorAll("[data-parallax]"));
    if (!els.length) return;
    var last = 0;
    function onScroll() {
      var now = Date.now(); if (now - last < 16) return; last = now;
      var vh = window.innerHeight;
      els.forEach(function (el) {
        var speed = parseFloat(el.getAttribute("data-parallax")) || 0.12;
        var rect = el.getBoundingClientRect();
        var delta = (rect.top + rect.height / 2) - vh / 2;
        el.style.transform = "translateY(" + (-delta * speed).toFixed(1) + "px)";
      });
    }
    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll, { passive: true });
    onScroll();
  }

  /* ==================================================================
     12. Urgency slot decrement
  ================================================================== */
  function initUrgency() {
    document.querySelectorAll("[data-urgency]").forEach(function (box) {
      var out = box.querySelector("[data-slots-count]");
      var slots = parseInt(box.getAttribute("data-slots") || "3", 10);
      var floor = parseInt(box.getAttribute("data-slots-min") || "1", 10);
      if (!out || REDUCE) return;
      function tick() {
        if (slots <= floor) return;
        if (Math.random() < 0.5) { slots--; out.textContent = String(slots); }
        window.setTimeout(tick, 20000 + Math.random() * 22000);
      }
      window.setTimeout(tick, 22000);
    });
  }

  /* ==================================================================
     13. Live metrics ticker + CRM flow loop
  ================================================================== */
  function initLive() {
    var cells = document.querySelectorAll("[data-live]");
    if (cells.length && !REDUCE) {
      window.setInterval(function () {
        if (document.hidden) return;
        cells.forEach(function (el) {
          var base = parseFloat(el.getAttribute("data-live")) || 0;
          var j = parseFloat(el.getAttribute("data-live-jitter")) || 0;
          var suf = el.getAttribute("data-live-suffix") || "";
          var val = Math.max(0, Math.round(base + (Math.random() * 2 - 1) * j));
          el.textContent = val.toLocaleString("en-IN") + suf;
        });
      }, 2600);
    }
    // CRM board: move the lead card New -> Scored -> Qualified on a loop
    var board = document.querySelector("[data-crm]");
    if (board && !REDUCE) {
      var cols = board.querySelectorAll(".crm-col");
      var lead = board.querySelector("[data-crm-lead]");
      var counter = board.querySelector("[data-crm-count]");
      if (cols.length >= 3 && lead) {
        var stage = 0, processed = parseInt((counter && counter.textContent) || "0", 10) || 0;
        window.setInterval(function () {
          if (document.hidden) return;
          stage = (stage + 1) % 3;
          lead.style.opacity = "0";
          lead.style.transform = "translateY(8px)";
          window.setTimeout(function () {
            cols[stage].querySelector(".crm-slot").appendChild(lead);
            lead.style.opacity = "1";
            lead.style.transform = "none";
            if (stage === 0 && counter) { processed += Math.floor(Math.random() * 3) + 1; counter.textContent = String(processed); }
          }, 320);
        }, 2200);
      }
    }
  }

  /* ==================================================================
     14. Rotating-question hero
  ================================================================== */
  function initHeroRotator() {
    var rotator = document.querySelector(".hero__rotator");
    if (!rotator) return;
    var QUESTIONS = [
      "Why aren’t you getting enough leads?",
      "Why is your ROAS dropping?",
      "Why aren’t your visitors converting?",
      "Why isn’t your business scaling?",
      "Why is your marketing not delivering predictable revenue?"
    ];
    var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    var HOLD = 3200, OUT_MS = 420, index = 0, timer = null;

    function make(text) {
      var el = document.createElement("span");
      el.className = "hero__question";
      el.textContent = text;
      return el;
    }
    function advance() {
      index = (index + 1) % QUESTIONS.length;
      var current = rotator.querySelector(".hero__question");
      var incoming = make(QUESTIONS[index]);
      if (reduce.matches) { rotator.replaceChildren(incoming); incoming.style.opacity = "1"; return; }
      if (current) { current.classList.remove("is-active", "is-in"); current.classList.add("is-out"); window.setTimeout(function () { current.remove(); }, OUT_MS + 40); }
      rotator.appendChild(incoming);
      void incoming.offsetWidth;
      incoming.classList.add("is-in");
    }
    function start() { if (timer) return; if (reduce.matches || document.hidden) return; timer = window.setInterval(advance, HOLD); }
    function stop() { window.clearInterval(timer); timer = null; }
    document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });
    window.addEventListener("focus", start);
    window.addEventListener("pageshow", start);
    if (reduce.addEventListener) reduce.addEventListener("change", function () { stop(); if (!reduce.matches) start(); });
    start();
  }

  /* ==================================================================
     15. Testimonial carousel ([data-carousel])
  ================================================================== */
  function initCarousel() {
    document.querySelectorAll("[data-carousel]").forEach(function (root) {
      var slides = Array.prototype.slice.call(root.querySelectorAll(".carousel__slide"));
      var dotsWrap = root.querySelector(".carousel__dots");
      if (slides.length < 2) { if (slides[0]) slides[0].classList.add("is-active"); return; }
      var i = 0, timer = null;
      var dots = slides.map(function (_, n) {
        var b = document.createElement("button");
        b.className = "carousel__dot";
        b.type = "button";
        b.setAttribute("aria-label", "Show testimonial " + (n + 1));
        b.addEventListener("click", function () { go(n); reset(); });
        if (dotsWrap) dotsWrap.appendChild(b);
        return b;
      });
      function go(n) {
        i = n;
        slides.forEach(function (s, k) { s.classList.toggle("is-active", k === n); s.setAttribute("aria-hidden", String(k !== n)); });
        dots.forEach(function (d, k) { d.classList.toggle("is-active", k === n); if (k === n) d.setAttribute("aria-current", "true"); else d.removeAttribute("aria-current"); });
      }
      function next() { go((i + 1) % slides.length); }
      function start() { if (timer) return; if (REDUCE || document.hidden) return; timer = window.setInterval(next, 5200); }
      function stop() { window.clearInterval(timer); timer = null; }
      function reset() { stop(); start(); }
      root.addEventListener("mouseenter", stop);
      root.addEventListener("mouseleave", start);
      root.addEventListener("focusin", stop);
      root.addEventListener("focusout", start);
      document.addEventListener("visibilitychange", function () { document.hidden ? stop() : start(); });
      window.addEventListener("focus", start);
      var pauseBtn = document.createElement("button");
      pauseBtn.type = "button"; pauseBtn.className = "carousel__pause"; pauseBtn.textContent = "Pause";
      pauseBtn.setAttribute("aria-label", "Pause testimonials");
      pauseBtn.addEventListener("click", function () {
        if (timer) { stop(); pauseBtn.textContent = "Play"; pauseBtn.setAttribute("aria-label", "Play testimonials"); }
        else { start(); pauseBtn.textContent = "Pause"; pauseBtn.setAttribute("aria-label", "Pause testimonials"); }
      });
      if (dotsWrap) dotsWrap.appendChild(pauseBtn);
      go(0); start();
    });
  }

  /* ==================================================================
     16. Before/After slider ([data-baslider] with range input)
  ================================================================== */
  function initBaSlider() {
    document.querySelectorAll("[data-baslider]").forEach(function (root) {
      var before = root.querySelector(".ba-before");
      var handle = root.querySelector(".ba-handle");
      var range = root.querySelector(".ba-range");
      if (!before || !range) return;
      function set(v) {
        before.style.width = v + "%";
        if (handle) handle.style.left = v + "%";
      }
      range.addEventListener("input", function () { set(range.value); });
      set(range.value || 50);
      var ro = new ResizeObserver(function () {
        var pane = before.querySelector(".ba-pane");
        if (pane) pane.style.width = root.clientWidth + "px";
      });
      ro.observe(root);
    });
  }

  /* ==================================================================
     17. Consultation popup — injected once, opened by every CTA
  ================================================================== */
  var SERVICES = [
    "Brand Consulting", "Performance Marketing", "Google Ads", "Meta Ads",
    "TikTok Ads", "LinkedIn Ads", "AI Automation", "CRM Automation",
    "Shopify Development", "WordPress Development", "Wix Studio Development",
    "Webflow Development", "Custom Development", "Complete Business Growth Strategy"
  ];

  function consultFieldsHtml(p) {
    return (
      '<div class="form-grid-2">' +
      '<div class="field"><label for="' + p + '-name">Full Name <span class="req" aria-hidden="true">*</span></label>' +
      '<input type="text" id="' + p + '-name" name="fullName" autocomplete="name" required>' +
      '<p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field"><label for="' + p + '-email">Business Email <span class="req" aria-hidden="true">*</span></label>' +
      '<input type="email" id="' + p + '-email" name="email" autocomplete="email" required>' +
      '<p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field"><label for="' + p + '-phone">Phone Number <span class="req" aria-hidden="true">*</span></label>' +
      '<input type="tel" id="' + p + '-phone" name="phone" autocomplete="tel" inputmode="tel" required>' +
      '<p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field"><label for="' + p + '-company">Company Name</label>' +
      '<input type="text" id="' + p + '-company" name="company" autocomplete="organization">' +
      '<p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field field--full"><label for="' + p + '-website">Website</label>' +
      '<input type="url" id="' + p + '-website" name="website" autocomplete="url" placeholder="https://">' +
      '<p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field field--full"><label for="' + p + '-service">Services Required <span class="req" aria-hidden="true">*</span></label>' +
      '<select id="' + p + '-service" name="service" required><option value="">Select a service</option>' +
      SERVICES.map(function (s) { return '<option value="' + s + '">' + s + "</option>"; }).join("") +
      "</select><p class=\"field__error\" aria-live=\"polite\"></p></div>" +
      '<div class="field field--full"><label for="' + p + '-challenge">Biggest Business Challenge <span class="req" aria-hidden="true">*</span></label>' +
      '<textarea id="' + p + '-challenge" name="challenge" rows="4" required placeholder="Describe your biggest challenge, your current marketing efforts, and what you want to achieve."></textarea>' +
      '<p class="field__error" aria-live="polite"></p></div>' +
      "</div>" +
      '<input type="hidden" name="source" value="" data-source-field>'
    );
  }

  function buildModal() {
    var root = document.createElement("div");
    root.className = "modal-root";
    root.id = "consult-modal";
    root.hidden = true;
    root.innerHTML =
      '<div class="modal__backdrop" data-modal-close></div>' +
      '<div class="modal" role="dialog" aria-modal="true" aria-labelledby="consult-modal-title">' +
      '<button type="button" class="modal__close" data-modal-close aria-label="Close consultation form">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg></button>' +
      '<h2 id="consult-modal-title">Let’s Understand Your Business</h2>' +
      '<p class="modal__subtitle">Tell me about your business and I’ll personally review your requirements before our consultation.</p>' +
      '<form novalidate data-consult-form>' + consultFieldsHtml("cm") +
      '<button type="submit" class="btn btn--primary btn--lg">Book Free Consultation</button>' +
      '<button type="button" class="modal__later" data-modal-close>Maybe Later</button>' +
      "</form></div>";
    document.body.appendChild(root);
    return root;
  }

  function initPopup() {
    var root = buildModal();
    var modal = root.querySelector(".modal");
    var lastTrigger = null;
    var hideTimer = null;
    function focusables() {
      return modal.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])');
    }
    function open(trigger) {
      if (hideTimer) { clearTimeout(hideTimer); hideTimer = null; }
      lastTrigger = trigger || null;
      var src = root.querySelector("[data-source-field]");
      if (src) {
        var page = window.location.pathname.split("/").pop() || "index.html";
        src.value = page + (trigger && trigger.getAttribute("data-cta") ? "#" + trigger.getAttribute("data-cta") : "");
      }
      root.hidden = false;
      window.requestAnimationFrame(function () { window.requestAnimationFrame(function () { root.classList.add("is-visible"); }); });
      document.body.style.overflow = "hidden";
      window.dataLayer.push({ event: "popup_open", source_page: window.location.pathname });
      var f = focusables(); if (f.length) f[0].focus();
      document.addEventListener("keydown", onKeydown);
    }
    function close() {
      root.classList.remove("is-visible");
      document.body.style.overflow = "";
      document.removeEventListener("keydown", onKeydown);
      hideTimer = window.setTimeout(function () { root.hidden = true; hideTimer = null; }, REDUCE ? 0 : 320);
      if (lastTrigger && typeof lastTrigger.focus === "function") lastTrigger.focus();
    }
    function onKeydown(e) {
      if (e.key === "Escape") { close(); return; }
      if (e.key !== "Tab") return;
      var f = focusables(); if (!f.length) return;
      var first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
    root.addEventListener("click", function (e) { if (e.target.closest("[data-modal-close]")) close(); });
    document.addEventListener("click", function (e) {
      var trigger = e.target.closest("[data-popup-open]");
      if (!trigger) return;
      e.preventDefault();
      open(trigger);
    });
    initConsultForm(root.querySelector("[data-consult-form]"));
  }

  /* ==================================================================
     18. Consultation form validation + submit
  ================================================================== */
  function setError(input, message) {
    var field = input.closest(".field");
    if (!field) return;
    field.classList.toggle("has-error", !!message);
    var err = field.querySelector(".field__error");
    if (err) {
      err.textContent = message || "";
      if (!err.id) err.id = (input.id || input.name || "f") + "-error";
      if (message) { input.setAttribute("aria-invalid", "true"); input.setAttribute("aria-describedby", err.id); }
      else { input.removeAttribute("aria-invalid"); input.removeAttribute("aria-describedby"); }
    }
  }
  function validateConsultForm(form) {
    var errors = [];
    var name = form.elements.fullName, email = form.elements.email, phone = form.elements.phone, service = form.elements.service, challenge = form.elements.challenge;
    if (!name.value.trim()) { setError(name, "Please enter your full name."); errors.push("fullName"); } else setError(name, "");
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(email.value.trim())) { setError(email, "Please enter a valid business email address."); errors.push("email"); } else setError(email, "");
    if (phone.value.replace(/\D/g, "").length < 8) { setError(phone, "Please enter a phone number with at least 8 digits."); errors.push("phone"); } else setError(phone, "");
    if (!service.value) { setError(service, "Please select the service you need."); errors.push("service"); } else setError(service, "");
    if (challenge.value.trim().length < 20) { setError(challenge, "Please describe your challenge in at least 20 characters."); errors.push("challenge"); } else setError(challenge, "");
    return errors;
  }
  function initConsultForm(form) {
    if (!form) return;
    var src = form.querySelector("[data-source-field]");
    if (src && !src.value) src.value = window.location.pathname.split("/").pop() || "index.html";
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var errors = validateConsultForm(form);
      if (errors.length) {
        window.dataLayer.push({ event: "form_error", form: "consultation", fields: errors.join(",") });
        var firstInvalid = form.querySelector('[aria-invalid="true"]'); if (firstInvalid) firstInvalid.focus();
        return;
      }
      var submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = "Sending…"; }
      var payload = {};
      ["fullName", "email", "phone", "company", "website", "service", "challenge", "source"].forEach(function (k) { if (form.elements[k]) payload[k] = form.elements[k].value.trim(); });
      window.dataLayer.push({ event: "form_submit", form: "consultation", service: payload.service });
      function done() { window.location.href = "thank-you.html"; }
      try {
        window.fetch(FORM_ENDPOINT, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) }).then(done, done);
        window.setTimeout(done, 2500);
      } catch (err) { done(); }
    });
    Array.prototype.forEach.call(form.querySelectorAll("input, select, textarea"), function (el) {
      el.addEventListener("input", function () { setError(el, ""); });
    });
  }

  /* ==================================================================
     Boot
  ================================================================== */
  ready(function () {
    initHeader();
    initDropdowns();
    initDrawer();
    initReveal();
    initCounters();
    initTabs();
    initAccordion();
    initFaqCats();
    initFilter();
    initTilt();
    initParallax();
    initUrgency();
    initLive();
    initHeroRotator();
    initCarousel();
    initBaSlider();
    initPopup();
    document.querySelectorAll("[data-consult-form-inline]").forEach(initConsultForm);
  });
})();
