/* ==========================================================================
   Sushant Rana — v3 motion engine
   Lenis smooth scroll · GSAP ScrollTrigger · SplitType · lazy Three.js hero
   Plus the live consultation popup (Supabase Edge Function).
   ========================================================================== */
(function () {
  "use strict";

  /* ------------------------------------------------------------------
     FORM ENDPOINT — Supabase Edge Function (saves lead + emails notification)
     Payload: { fullName, email, phone, company, website, service, challenge, source }
  ------------------------------------------------------------------ */
  var FORM_ENDPOINT = "https://mrviteqvzqmejauiftpp.supabase.co/functions/v1/consultation";

  var REDUCE = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var FINE = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var DESKTOP = window.matchMedia("(min-width: 1024px)").matches;

  window.dataLayer = window.dataLayer || [];
  document.documentElement.classList.remove("no-js");

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }

  /* ==================================================================
     1. Smooth scroll (Lenis) + GSAP wiring
  ================================================================== */
  var lenis = null;
  function initScroll() {
    var gsap = window.gsap;
    if (gsap && window.ScrollTrigger) gsap.registerPlugin(window.ScrollTrigger);
    if (REDUCE || !window.Lenis) return;
    lenis = new window.Lenis({ duration: 1.05, smoothWheel: true, lerp: 0.11 });
    function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
    requestAnimationFrame(raf);
    if (window.ScrollTrigger) {
      lenis.on("scroll", window.ScrollTrigger.update);
      window.ScrollTrigger.refresh();
    }
    // anchor links go through Lenis
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener("click", function (e) {
        var id = a.getAttribute("href");
        if (!id || id === "#") return;
        var t = document.querySelector(id);
        if (!t) return;
        e.preventDefault();
        lenis.scrollTo(t, { offset: -80 });
      });
    });
  }

  /* ==================================================================
     2. Scroll reveals + headline split
  ================================================================== */
  function initReveal() {
    var gsap = window.gsap;
    var els = document.querySelectorAll("[data-reveal]");
    if (!gsap || !window.ScrollTrigger || REDUCE) {
      els.forEach(function (el) { el.style.opacity = 1; el.style.transform = "none"; });
      return;
    }
    els.forEach(function (el) {
      var delay = parseFloat(el.getAttribute("data-reveal-delay") || "0");
      gsap.to(el, {
        opacity: 1, y: 0, duration: 0.9, ease: "power3.out", delay: delay,
        scrollTrigger: { trigger: el, start: "top 88%", once: true }
      });
    });

    // stagger groups
    document.querySelectorAll("[data-stagger]").forEach(function (group) {
      var kids = group.children;
      gsap.set(kids, { opacity: 0, y: 26 });
      gsap.to(kids, {
        opacity: 1, y: 0, duration: 0.75, ease: "power3.out", stagger: 0.07,
        scrollTrigger: { trigger: group, start: "top 85%", once: true }
      });
    });

    // Headline reveal — per-line fade + rise. Deliberately NOT an overflow:hidden
    // mask: with a tight display line-height that clips descenders and gradient text.
    if (window.SplitType) {
      document.querySelectorAll("[data-split]").forEach(function (h) {
        var st = new window.SplitType(h, { types: "lines", lineClass: "split-line" });
        gsap.set(st.lines, { opacity: 0, y: 34 });
        gsap.to(st.lines, {
          opacity: 1, y: 0, duration: 1, ease: "power3.out", stagger: 0.09,
          scrollTrigger: { trigger: h, start: "top 92%", once: true }
        });
      });
    }

    // chart bars in dashboards
    document.querySelectorAll(".dash").forEach(function (d) {
      window.ScrollTrigger.create({ trigger: d, start: "top 80%", once: true, onEnter: function () { d.classList.add("is-in"); } });
    });

    // timeline active state
    document.querySelectorAll(".tl").forEach(function (step) {
      window.ScrollTrigger.create({
        trigger: step, start: "top 70%", end: "bottom 40%",
        onEnter: function () { step.classList.add("is-active"); },
        onEnterBack: function () { step.classList.add("is-active"); }
      });
    });
  }

  /* ==================================================================
     3. Counters
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
      var start = null, dur = 1600;
      function tick(now) {
        if (start === null) start = now;
        var p = Math.min((now - start) / dur, 1);
        el.textContent = pre + fmt(target * (1 - Math.pow(1 - p, 3)), dec, comma) + suf;
        if (p < 1) requestAnimationFrame(tick);
        else el.textContent = pre + fmt(target, dec, comma) + suf;
      }
      requestAnimationFrame(tick);
    }
    if (!("IntersectionObserver" in window)) { nums.forEach(run); return; }
    var io = new IntersectionObserver(function (es, o) {
      es.forEach(function (e) { if (e.isIntersecting) { run(e.target); o.unobserve(e.target); } });
    }, { threshold: 0.4 });
    nums.forEach(function (n) { io.observe(n); });
  }

  /* ==================================================================
     4. Header, mega menu, drawer
  ================================================================== */
  function initHeader() {
    var header = document.querySelector(".header");
    if (header) {
      var upd = function () { header.classList.toggle("is-scrolled", window.scrollY > 10); };
      upd(); window.addEventListener("scroll", upd, { passive: true });
    }
    var items = document.querySelectorAll(".nav__item--has-mega");
    items.forEach(function (item) {
      var trig = item.querySelector(".nav__trigger");
      if (!trig) return;
      trig.addEventListener("click", function () {
        var open = item.classList.toggle("is-open");
        trig.setAttribute("aria-expanded", open ? "true" : "false");
        items.forEach(function (o) { if (o !== item) { o.classList.remove("is-open"); var t = o.querySelector(".nav__trigger"); if (t) t.setAttribute("aria-expanded", "false"); } });
      });
      item.addEventListener("keydown", function (e) { if (e.key === "Escape") { item.classList.remove("is-open"); trig.setAttribute("aria-expanded", "false"); trig.focus(); } });
      item.addEventListener("focusout", function () {
        requestAnimationFrame(function () { if (!item.contains(document.activeElement)) { item.classList.remove("is-open"); trig.setAttribute("aria-expanded", "false"); } });
      });
    });
    document.addEventListener("click", function (e) {
      items.forEach(function (item) { if (!item.contains(e.target)) { item.classList.remove("is-open"); var t = item.querySelector(".nav__trigger"); if (t) t.setAttribute("aria-expanded", "false"); } });
    });

    var burger = document.querySelector(".burger");
    var drawer = document.getElementById("drawer");
    if (burger && drawer) {
      var setOpen = function (open) {
        drawer.classList.toggle("is-open", open);
        burger.setAttribute("aria-expanded", open ? "true" : "false");
        burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
        document.body.style.overflow = open ? "hidden" : "";
        if (lenis) open ? lenis.stop() : lenis.start();
      };
      burger.addEventListener("click", function () { setOpen(!drawer.classList.contains("is-open")); });
      drawer.addEventListener("click", function (e) { if (e.target.closest("a")) setOpen(false); });
      document.addEventListener("keydown", function (e) { if (e.key === "Escape" && drawer.classList.contains("is-open")) { setOpen(false); burger.focus(); } });
      drawer.querySelectorAll(".drawer__acc").forEach(function (btn) {
        btn.addEventListener("click", function () {
          var sub = document.getElementById(btn.getAttribute("aria-controls"));
          var open = btn.getAttribute("aria-expanded") === "true";
          btn.setAttribute("aria-expanded", open ? "false" : "true");
          if (sub) sub.classList.toggle("is-open", !open);
        });
      });
    }
  }

  /* ==================================================================
     5. Cursor + magnetic buttons (fine pointer only)
  ================================================================== */
  function initCursor() {
    if (!FINE || REDUCE) return;
    var dot = document.createElement("div"); dot.className = "cursor-dot";
    var ring = document.createElement("div"); ring.className = "cursor-ring";
    dot.setAttribute("aria-hidden", "true"); ring.setAttribute("aria-hidden", "true");
    document.body.appendChild(ring); document.body.appendChild(dot);
    var mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
    document.addEventListener("mousemove", function (e) {
      mx = e.clientX; my = e.clientY;
      dot.style.transform = "translate3d(" + mx + "px," + my + "px,0)";
    }, { passive: true });
    (function loop() {
      rx += (mx - rx) * 0.16; ry += (my - ry) * 0.16;
      ring.style.transform = "translate3d(" + rx + "px," + ry + "px,0)";
      requestAnimationFrame(loop);
    })();
    var SEL = "a, button, .chip, .ind, .tool, input, select, textarea";
    document.addEventListener("mouseover", function (e) { if (e.target.closest(SEL)) ring.classList.add("is-active"); });
    document.addEventListener("mouseout", function (e) { if (e.target.closest(SEL)) ring.classList.remove("is-active"); });

    // magnetic buttons
    var mags = Array.prototype.slice.call(document.querySelectorAll("[data-magnetic]"));
    var tick = false;
    document.addEventListener("mousemove", function (e) {
      if (tick) return; tick = true;
      requestAnimationFrame(function () {
        tick = false;
        mags.forEach(function (b) {
          var r = b.getBoundingClientRect();
          if (r.bottom < -80 || r.top > innerHeight + 80) return;
          var dx = e.clientX - (r.left + r.width / 2);
          var dy = e.clientY - (r.top + r.height / 2);
          var dist = Math.max(Math.abs(dx) - r.width / 2, Math.abs(dy) - r.height / 2);
          if (dist < 70) {
            var pull = 1 - Math.max(dist, 0) / 70;
            b.style.transform = "translate(" + dx * 0.22 * pull + "px," + dy * 0.22 * pull + "px)";
          } else if (b.style.transform) { b.style.transform = ""; }
        });
      });
    }, { passive: true });
  }

  /* ==================================================================
     6. Hero 3D — lazy, desktop only, progressive enhancement
  ================================================================== */
  function initHero3D() {
    var mount = document.getElementById("hero-3d");
    if (!mount || REDUCE || !DESKTOP) return;
    // don't punish slow connections
    var conn = navigator.connection;
    if (conn && (conn.saveData || /2g/.test(conn.effectiveType || ""))) return;

    import("../vendor/three.module.js").then(function (THREE) {
      var w = mount.clientWidth, h = mount.clientHeight;
      var renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true, powerPreference: "high-performance" });
      renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
      renderer.setSize(w, h);
      mount.appendChild(renderer.domElement);

      var scene = new THREE.Scene();
      var camera = new THREE.PerspectiveCamera(50, w / h, 0.1, 100);
      camera.position.z = 9;

      var accent = new THREE.Color("#5B7CFA");
      var accent2 = new THREE.Color("#A855F7");

      scene.add(new THREE.AmbientLight(0xffffff, 0.55));
      var l1 = new THREE.DirectionalLight(accent, 2.6); l1.position.set(-5, 4, 6); scene.add(l1);
      var l2 = new THREE.DirectionalLight(accent2, 2.2); l2.position.set(6, -3, 4); scene.add(l2);

      var group = new THREE.Group(); scene.add(group);
      var geos = [
        new THREE.IcosahedronGeometry(1.15, 0),
        new THREE.TorusGeometry(0.85, 0.28, 16, 60),
        new THREE.OctahedronGeometry(1.0, 0),
        new THREE.SphereGeometry(0.72, 32, 32)
      ];
      // Background ambience only: small, translucent, pushed to the periphery
      // and well behind the content plane so it never competes with the copy.
      var mat = new THREE.MeshStandardMaterial({
        color: 0x1a2040, metalness: 0.8, roughness: 0.28,
        transparent: true, opacity: 0.42
      });
      var wire = new THREE.MeshBasicMaterial({ color: accent, wireframe: true, transparent: true, opacity: 0.14 });

      var meshes = [];
      var spots = [[-6.2, 2.4, -6], [6.0, 1.8, -7], [-5.2, -2.6, -5], [5.6, -2.4, -6.5], [0.4, 3.4, -9]];
      spots.forEach(function (p, i) {
        var g = geos[i % geos.length];
        var m = new THREE.Mesh(g, i % 2 === 0 ? mat : wire);
        m.position.set(p[0], p[1], p[2]);
        m.scale.setScalar(0.34 + (i % 3) * 0.1);
        m.userData.spin = 0.0016 + i * 0.0007;
        m.userData.baseY = p[1];
        m.userData.phase = i * 1.3;
        group.add(m); meshes.push(m);
      });

      var tx = 0, ty = 0, cx = 0, cy = 0;
      window.addEventListener("mousemove", function (e) {
        tx = (e.clientX / innerWidth - 0.5); ty = (e.clientY / innerHeight - 0.5);
      }, { passive: true });

      var t = 0, running = true;
      function render() {
        if (!running) return;
        requestAnimationFrame(render);
        t += 0.01;
        cx += (tx - cx) * 0.04; cy += (ty - cy) * 0.04;
        group.rotation.y = cx * 0.5;
        group.rotation.x = cy * 0.32;
        meshes.forEach(function (m) {
          m.rotation.x += m.userData.spin;
          m.rotation.y += m.userData.spin * 1.3;
          m.position.y = m.userData.baseY + Math.sin(t + m.userData.phase) * 0.22;
        });
        renderer.render(scene, camera);
      }
      render();
      mount.classList.add("is-ready");

      // pause when hero is off-screen / tab hidden
      var hero = mount.closest(".hero") || mount;
      if ("IntersectionObserver" in window) {
        new IntersectionObserver(function (es) {
          es.forEach(function (e) { if (e.isIntersecting && !running) { running = true; render(); } else if (!e.isIntersecting) { running = false; } });
        }, { threshold: 0.01 }).observe(hero);
      }
      document.addEventListener("visibilitychange", function () {
        if (document.hidden) running = false;
        else if (!running) { running = true; render(); }
      });

      window.addEventListener("resize", function () {
        w = mount.clientWidth; h = mount.clientHeight;
        camera.aspect = w / h; camera.updateProjectionMatrix(); renderer.setSize(w, h);
      }, { passive: true });
    }).catch(function () { /* 3D is a bonus — silently skip */ });
  }

  /* ==================================================================
     7. Consultation popup (Supabase-backed)
  ================================================================== */
  var SERVICES = [
    "Brand Strategy", "Performance Marketing", "Google Ads", "Meta Ads",
    "AI Automation", "CRM Systems", "Web Development", "Analytics & Tracking",
    "Funnels & CRO", "Complete Growth System"
  ];

  function fields(p) {
    return (
      '<div class="form-grid-2">' +
      '<div class="field"><label for="' + p + '-name">Full Name <span class="req">*</span></label><input type="text" id="' + p + '-name" name="fullName" autocomplete="name" required><p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field"><label for="' + p + '-email">Business Email <span class="req">*</span></label><input type="email" id="' + p + '-email" name="email" autocomplete="email" required><p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field"><label for="' + p + '-phone">Phone <span class="req">*</span></label><input type="tel" id="' + p + '-phone" name="phone" autocomplete="tel" inputmode="tel" required><p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field"><label for="' + p + '-company">Company</label><input type="text" id="' + p + '-company" name="company" autocomplete="organization"><p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field field--full"><label for="' + p + '-website">Website</label><input type="url" id="' + p + '-website" name="website" placeholder="https://"><p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field field--full"><label for="' + p + '-service">What do you need? <span class="req">*</span></label><select id="' + p + '-service" name="service" required><option value="">Select a service</option>' +
      SERVICES.map(function (s) { return '<option value="' + s + '">' + s + "</option>"; }).join("") +
      '</select><p class="field__error" aria-live="polite"></p></div>' +
      '<div class="field field--full"><label for="' + p + '-challenge">Biggest growth challenge <span class="req">*</span></label><textarea id="' + p + '-challenge" name="challenge" rows="4" required placeholder="Where is growth stuck right now, what have you tried, and what does success look like?"></textarea><p class="field__error" aria-live="polite"></p></div>' +
      "</div>" +
      '<input type="hidden" name="source" value="" data-source-field>'
    );
  }

  function initPopup() {
    var root = document.createElement("div");
    root.className = "modal-root"; root.id = "consult-modal"; root.hidden = true;
    root.innerHTML =
      '<div class="modal__backdrop" data-modal-close></div>' +
      '<div class="modal" role="dialog" aria-modal="true" aria-labelledby="consult-title">' +
      '<button type="button" class="modal__close" data-modal-close aria-label="Close">' +
      '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg></button>' +
      '<h2 id="consult-title">Let’s map your revenue system</h2>' +
      '<p class="modal__subtitle">Tell me where growth is stuck. I review every enquiry personally before we talk.</p>' +
      '<form novalidate data-consult-form>' + fields("cm") +
      '<button type="submit" class="btn btn--primary btn--lg">Book Strategy Call</button>' +
      '<button type="button" class="modal__later" data-modal-close>Maybe later</button>' +
      "</form></div>";
    document.body.appendChild(root);

    var modal = root.querySelector(".modal");
    var last = null, hideTimer = null;
    function focusables() { return modal.querySelectorAll('a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled])'); }
    function open(trigger) {
      if (hideTimer) { clearTimeout(hideTimer); hideTimer = null; }
      last = trigger || null;
      var src = root.querySelector("[data-source-field]");
      if (src) src.value = (location.pathname.split("/").pop() || "index.html") + (trigger && trigger.getAttribute("data-cta") ? "#" + trigger.getAttribute("data-cta") : "");
      root.hidden = false;
      requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add("is-visible"); }); });
      document.body.style.overflow = "hidden";
      if (lenis) lenis.stop();
      window.dataLayer.push({ event: "popup_open", source_page: location.pathname });
      var f = focusables(); if (f.length) f[0].focus();
      document.addEventListener("keydown", onKey);
    }
    function close() {
      root.classList.remove("is-visible");
      document.body.style.overflow = "";
      if (lenis) lenis.start();
      document.removeEventListener("keydown", onKey);
      hideTimer = window.setTimeout(function () { root.hidden = true; hideTimer = null; }, REDUCE ? 0 : 320);
      if (last && last.focus) last.focus();
    }
    function onKey(e) {
      if (e.key === "Escape") { close(); return; }
      if (e.key !== "Tab") return;
      var f = focusables(); if (!f.length) return;
      var first = f[0], lastEl = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); lastEl.focus(); }
      else if (!e.shiftKey && document.activeElement === lastEl) { e.preventDefault(); first.focus(); }
    }
    root.addEventListener("click", function (e) { if (e.target.closest("[data-modal-close]")) close(); });
    document.addEventListener("click", function (e) {
      var t = e.target.closest("[data-popup-open]");
      if (!t) return;
      e.preventDefault(); open(t);
    });
    initForm(root.querySelector("[data-consult-form]"));
  }

  function setError(input, msg) {
    var field = input.closest(".field"); if (!field) return;
    field.classList.toggle("has-error", !!msg);
    var err = field.querySelector(".field__error");
    if (err) {
      err.textContent = msg || "";
      if (!err.id) err.id = (input.id || input.name || "f") + "-error";
      if (msg) { input.setAttribute("aria-invalid", "true"); input.setAttribute("aria-describedby", err.id); }
      else { input.removeAttribute("aria-invalid"); input.removeAttribute("aria-describedby"); }
    }
  }

  function initForm(form) {
    if (!form) return;
    var src = form.querySelector("[data-source-field]");
    if (src && !src.value) src.value = location.pathname.split("/").pop() || "index.html";
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var el = form.elements, errs = [];
      if (!el.fullName.value.trim()) { setError(el.fullName, "Please enter your name."); errs.push("fullName"); } else setError(el.fullName, "");
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(el.email.value.trim())) { setError(el.email, "Enter a valid business email."); errs.push("email"); } else setError(el.email, "");
      if (el.phone.value.replace(/\D/g, "").length < 8) { setError(el.phone, "Enter a phone number with at least 8 digits."); errs.push("phone"); } else setError(el.phone, "");
      if (!el.service.value) { setError(el.service, "Pick what you need."); errs.push("service"); } else setError(el.service, "");
      if (el.challenge.value.trim().length < 20) { setError(el.challenge, "A sentence or two helps me prepare (20+ characters)."); errs.push("challenge"); } else setError(el.challenge, "");
      if (errs.length) {
        window.dataLayer.push({ event: "form_error", form: "consultation", fields: errs.join(",") });
        var bad = form.querySelector('[aria-invalid="true"]'); if (bad) bad.focus();
        return;
      }
      var btn = form.querySelector('button[type="submit"]');
      if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      var payload = {};
      ["fullName", "email", "phone", "company", "website", "service", "challenge", "source"].forEach(function (k) { if (el[k]) payload[k] = el[k].value.trim(); });
      window.dataLayer.push({ event: "form_submit", form: "consultation", service: payload.service });
      function done() { location.href = "thank-you.html"; }
      try {
        window.fetch(FORM_ENDPOINT, { method: "POST", keepalive: true, headers: { "Content-Type": "application/json" }, body: JSON.stringify(payload) }).then(done, done);
        window.setTimeout(done, 2500);
      } catch (err) { done(); }
    });
    form.querySelectorAll("input, select, textarea").forEach(function (i) {
      i.addEventListener("input", function () { setError(i, ""); });
    });
  }

  /* ==================================================================
     Boot
  ================================================================== */
  ready(function () {
    initScroll();
    initHeader();
    initReveal();
    initCounters();
    initCursor();
    initPopup();
    initHero3D();
    document.querySelectorAll("[data-consult-form-inline]").forEach(initForm);
  });
})();
