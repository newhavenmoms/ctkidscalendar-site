/* CT Kids Calendar: Google Analytics 4 with Consent Mode v2.
   ------------------------------------------------------------
   1. Paste your GA4 Measurement ID below (Admin > Data streams > your web stream).
   2. Nothing else to change: every page loads this file.
   Until a visitor taps "Allow", analytics cookies stay off (analytics_storage
   denied) and Google only receives cookieless pings. Advertising storage,
   ad user data and ad personalization are always denied. */
(function () {
  var GA_ID = "G-BG5T3421T5"; // <-- your Measurement ID
  if (!/^G-[A-Z0-9]{6,}$/.test(GA_ID) || GA_ID === "G-XXXXXXXXXX") return; // not set up yet: do nothing

  var KEY = "ctk-consent"; // "granted" | "denied", kept in this browser only
  var saved = null;
  try { saved = localStorage.getItem(KEY); } catch (_) {}

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag("consent", "default", {
    analytics_storage: saved === "granted" ? "granted" : "denied",
    ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied",
    wait_for_update: 500
  });
  gtag("set", "ads_data_redaction", true);
  gtag("js", new Date());

  // Which town page this is ("home" on the homepage), sent with every hit.
  var seg = location.pathname.split("/").filter(Boolean)[0] || "home";
  gtag("config", GA_ID, { page_town: seg, allow_google_signals: false, allow_ad_personalization_signals: false });

  var s = document.createElement("script");
  s.async = true; s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_ID);
  document.head.appendChild(s);

  /* ---------- tracking helper + the clicks we care about ---------- */
  function track(name, params) { gtag("event", name, Object.assign({ page_town: seg }, params || {})); }
  window.ctkTrack = track;
  var txt = function (el) { return (el && el.textContent || "").replace(/\s+/g, " ").trim().slice(0, 100); };
  document.addEventListener("click", function (ev) {
    var t = ev.target.closest ? ev.target : ev.target.parentElement; if (!t) return;
    var el;
    if ((el = t.closest("#langBtn"))) return track("language_switch", { to: document.documentElement.lang === "es" ? "en" : "es" });
    if ((el = t.closest("#homeBig a"))) { var li = el.closest("li"); return track("big_day_click", { event_title: txt(el), place: txt(li && li.querySelector(".w")), from: "homepage" }); }
    if ((el = t.closest("[data-cal-e]"))) return track("add_to_calendar_open", { event_title: el.dataset.calE });
    if ((el = t.closest("[data-share-e],[data-share-c],[data-share-d]"))) return track("share_open", { item: el.dataset.shareE || el.dataset.shareC || el.dataset.shareD });
    if ((el = t.closest("[data-ccat]"))) return track("class_filter", { category: el.dataset.ccat });
    if ((el = t.closest("[data-jump]"))) return track("see_on_calendar", { item: txt(el.closest("li,article,.bd") || el) });
    if ((el = t.closest(".places a"))) return track("place_click", { place: txt(el), link_url: el.href });
    if ((el = t.closest(".cls a"))) { var card = el.closest(".cls"); return track("class_click", { class_name: txt(card && card.querySelector("h3,h4")), link_url: el.href }); }
  }, true);

  /* ---------- the consent notice ---------- */
  var T = {
    en: { msg: "We use cookies for analytics.", yes: "Accept", no: "Decline", more: "Privacy", label: "Cookies" },
    es: { msg: "Usamos cookies para an\u00e1lisis.", yes: "Aceptar", no: "Rechazar", more: "Privacidad", label: "Cookies" }
  };
  var box = null;
  function lang() { return document.documentElement.lang === "es" ? "es" : "en"; }
  function policyHref() { return document.getElementById("privacy") ? "#privacy" : "/#privacy"; }
  function paint() {
    if (!box) return; var L = T[lang()];
    box.setAttribute("aria-label", L.label);
    box.innerHTML = '<p>' + L.msg + ' <a href="' + policyHref() + '">' + L.more + '</a></p>' +
      '<div class="ctk-cc-btns"><button type="button" data-cc="denied">' + L.no + '</button><button type="button" data-cc="granted" class="yes">' + L.yes + '</button></div>';
  }
  function choose(v) {
    try { localStorage.setItem(KEY, v); } catch (_) {}
    gtag("consent", "update", { analytics_storage: v });
    if (v === "denied") { // remove any GA cookies already set on this domain
      document.cookie.split(";").forEach(function (c) {
        var n = c.split("=")[0].trim();
        if (/^_ga/.test(n)) ["", "; domain=." + location.hostname.replace(/^www\./, "")].forEach(function (d) {
          document.cookie = n + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + d;
        });
      });
    }
    hide();
  }
  function show() {
    if (box) return;
    var css = document.createElement("style");
    css.textContent = ".ctk-cc{position:fixed;z-index:9999;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));max-width:max-content;margin:0 auto;display:flex;align-items:center;gap:12px;flex-wrap:wrap;justify-content:space-between;background:var(--card,#fff);color:var(--ink,#1d2b4f);border:1.5px solid var(--ink,#1d2b4f);padding:10px 12px;font:14px/1.35 var(--sans,system-ui,sans-serif)}" +
      ".ctk-cc p{margin:0}.ctk-cc a{color:inherit;text-underline-offset:3px}.ctk-cc-btns{display:flex;gap:8px}" +
      ".ctk-cc button{font:600 .72rem/1 var(--mono,ui-monospace,monospace);letter-spacing:.06em;text-transform:uppercase;padding:9px 12px;border:1.5px solid var(--ink,#1d2b4f);background:var(--card,#fff);color:var(--ink,#1d2b4f);cursor:pointer}" +
      ".ctk-cc button.yes{background:var(--ink,#1d2b4f);color:#fff}.ctk-cc button:focus-visible{outline:3px solid var(--marigold,#FFD166);outline-offset:2px}";
    document.head.appendChild(css);
    box = document.createElement("div"); box.className = "ctk-cc"; box.setAttribute("role", "region");
    box.addEventListener("click", function (e) { var b = e.target.closest("[data-cc]"); if (b) choose(b.dataset.cc); });
    paint(); document.body.appendChild(box);
    new MutationObserver(paint).observe(document.documentElement, { attributes: true, attributeFilter: ["lang"] });
  }
  function hide() { if (box) { box.remove(); box = null; } }
  // "Cookie settings" links in the privacy policy reopen the notice
  document.addEventListener("click", function (e) { var c = e.target.closest && e.target.closest("[data-cookie-settings]"); if (c) { e.preventDefault(); show(); } });
  if (saved !== "granted" && saved !== "denied") {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", show); else show();
  }
})();
