/* BIONUT — site behaviour (no dependencies) */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* Sticky header state */
  var header = document.querySelector(".site-header");
  function onScroll() { if (header) header.classList.toggle("scrolled", window.scrollY > 12); }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobile menu */
  var toggle = document.querySelector(".menu-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("menu-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && document.body.classList.contains("menu-open")) {
        document.body.classList.remove("menu-open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth > 1120) { document.body.classList.remove("menu-open"); toggle.setAttribute("aria-expanded", "false"); }
    });
  }

  /* Reveal on scroll + count-up */
  function countUp(el) {
    var target = parseFloat(el.getAttribute("data-count").replace(/,/g, ""));
    var hasComma = el.getAttribute("data-count").indexOf(",") > -1;
    var fmt = function (n) { var s = Math.round(n).toString(); return hasComma ? s.replace(/\B(?=(\d{3})+(?!\d))/g, ",") : s; };
    if (reduce) { el.firstChild.nodeValue = fmt(target); return; }
    var start = null, dur = 1400;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.firstChild.nodeValue = fmt(target * eased);
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var targets = document.querySelectorAll(".reveal, [data-count]");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var t = en.target;
        if (t.hasAttribute("data-count")) countUp(t); else t.classList.add("in");
        io.unobserve(t);
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    targets.forEach(function (t) {
      if (t.hasAttribute("data-count")) t.firstChild.nodeValue = "0";
      io.observe(t);
    });
  } else {
    targets.forEach(function (t) { t.classList.add("in"); });
  }

  /* World map interactions */
  var map = document.querySelector(".world-map");
  if (map) {
    var tip = document.querySelector(".map-tip");
    var wrap = map.closest(".map-wrap");
    var buttons = document.querySelectorAll(".market-list button");
    function setActive(code, show) {
      map.querySelectorAll(".active").forEach(function (n) { n.classList.remove("active"); });
      buttons.forEach(function (b) { b.classList.toggle("active", b.dataset.code === code); });
      if (!code) { if (tip) tip.classList.remove("show"); return; }
      map.querySelectorAll('[data-code="' + code + '"]').forEach(function (n) { n.classList.add("active"); });
      if (tip && show) {
        var pin = map.querySelector('.pin[data-code="' + code + '"]');
        if (pin) {
          var vb = map.viewBox.baseVal, r = map.getBoundingClientRect();
          var x = (pin.cx.baseVal.value - vb.x) / vb.width * r.width;
          var y = (pin.cy.baseVal.value - vb.y) / vb.height * r.height;
          tip.textContent = pin.getAttribute("data-name");
          tip.style.left = x + "px"; tip.style.top = y + "px";
          tip.classList.add("show");
        }
      }
    }
    map.querySelectorAll("[data-code]").forEach(function (n) {
      n.addEventListener("mouseenter", function () { setActive(n.dataset.code, true); });
      n.addEventListener("mouseleave", function () { setActive(null); });
    });
    buttons.forEach(function (b) {
      b.addEventListener("mouseenter", function () { setActive(b.dataset.code, true); });
      b.addEventListener("focus", function () { setActive(b.dataset.code, true); });
      b.addEventListener("mouseleave", function () { setActive(null); });
      b.addEventListener("blur", function () { setActive(null); });
      b.addEventListener("click", function () { setActive(b.dataset.code, true); });
    });
    if (wrap && !reduce) {
      var routes = map.querySelectorAll(".route");
      routes.forEach(function (p) {
        var len = p.getTotalLength();
        p.style.strokeDasharray = len; p.style.strokeDashoffset = len;
      });
      var mio = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return;
        routes.forEach(function (p, i) {
          p.style.transition = "stroke-dashoffset 1.6s cubic-bezier(.2,.7,.2,1) " + (i * 0.12) + "s";
          p.style.strokeDashoffset = "0";
          p.addEventListener("transitionend", function () { p.style.strokeDasharray = ""; p.style.strokeDashoffset = ""; p.style.transition = ""; }, { once: true });
        });
        mio.disconnect();
      }, { threshold: 0.3 });
      mio.observe(wrap);
    }
  }

  /* Product gallery */
  var main = document.querySelector(".pd-main");
  if (main) {
    var mainPic = main.querySelector("picture");
    document.querySelectorAll(".pd-thumbs button").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var src = btn.querySelector("picture").cloneNode(true);
        var img = src.querySelector("img");
        img.alt = btn.getAttribute("data-alt") || img.alt;
        img.removeAttribute("loading");
        mainPic.replaceWith(src); mainPic = src;
        document.querySelectorAll(".pd-thumbs button").forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
      });
    });
  }

  /* Enquiry form: prefill + mailto composition */
  var form = document.querySelector("#enquiry");
  if (form) {
    var params = new URLSearchParams(window.location.search);
    var p = params.get("product");
    if (p) { var sel = form.querySelector("#f-product"); if (sel && sel.querySelector('option[value="' + p + '"]')) sel.value = p; }
    var c = params.get("cert");
    if (c) { var msg = form.querySelector("#f-message"); if (msg && !msg.value) msg.value = form.getAttribute("data-cert-text").replace("%s", c); }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll("[required]").forEach(function (inp) {
        var valid = inp.value.trim() !== "" && (inp.type !== "email" || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(inp.value.trim()));
        inp.closest(".field").classList.toggle("invalid", !valid);
        if (!valid) ok = false;
      });
      var out = form.querySelector(".form-msg");
      if (!ok) { out.textContent = form.getAttribute("data-required"); return; }
      out.textContent = "";
      var lines = [];
      form.querySelectorAll("[data-label]").forEach(function (inp) {
        var v = inp.tagName === "SELECT" ? inp.options[inp.selectedIndex].text : inp.value.trim();
        if (v) lines.push(inp.getAttribute("data-label") + ": " + v);
      });
      var company = form.querySelector("#f-company").value.trim();
      var subject = form.getAttribute("data-subject") + (company ? " — " + company : "");
      window.location.href = "mailto:" + form.getAttribute("data-to") + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(lines.join("\n"));
    });
  }
})();
