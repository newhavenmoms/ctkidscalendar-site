/* CT Kids Calendar — "Submit an event" form.
   One shared pop-up form for the homepage and every town page. Any element with
   [data-submit] opens it (data-submit="class" etc. preselects the type).

   HOW IT SENDS:
   - If WEB3FORMS_KEY is set, the form posts to Web3Forms, which emails the
     submission to the address the key was created for. Free: 250/month.
     Get a key at https://web3forms.com (enter the email, the key arrives by email),
     then paste it below.
   - If no key is set (or the service is unreachable), the form opens the visitor's
     email app with everything filled in, addressed to SUBMIT_TO.
   TOWNS: keep this list in step with the site's towns (tools/newtowns adds new ones). */
(function () {
  const WEB3FORMS_KEY = "303d4e37-2607-4dc4-84b1-8c742c6914bf";               // paste your Web3Forms access key here
  const SUBMIT_TO = "newhavenmoms@gmail.com";
  const TOWNS = ["Branford","Bridgeport","Cheshire","Danbury","Darien","Essex","Fairfield","Farmington","Glastonbury","Greenwich","Guilford","Hamden","Hartford","Madison","Manchester","Middletown","Milford","New Canaan","New Haven","Newtown","Norwalk","Old Saybrook","Ridgefield","Simsbury","Stamford","Stratford","Trumbull","Wallingford","Waterbury","West Hartford","Westport"];

  const T = {
    en: {
      open: "Submit an event", openShort: "Submit", title: "Tell us about it",
      ctaH: "Know about something we're missing?", ctaP: "Events, classes, places to go, or a fix to something we've listed. Send it in and we'll take a look.",
      intro: "Know about an event, class or place we should list? Send it our way. We check every submission before it goes on the calendar.",
      type: "What is it?", tEvent: "An event", tClass: "A class or program", tPlace: "A place to go", tFix: "A correction to something listed",
      town: "Town", townOther: "Another town (tell us below)", choose: "Choose…",
      name: "Name of the event, class or place", when: "Date(s) and time", whenHint: "e.g. Sat Oct 24, 10am–noon",
      where: "Where (place and address)", ages: "Ages", cost: "Cost", costHint: "e.g. Free, $10 per child",
      link: "Link for more info", details: "Details", detailsHint: "What should families know? Registration, what to bring, anything else.",
      you: "Your name (optional)", email: "Your email (optional)", emailHint: "Only used if we have a question about this submission.",
      organizer: "I'm the organizer or work for the host", send: "Send", sending: "Sending…", cancel: "Cancel", close: "Close",
      thanks: "Thank you! We got it.", thanksP: "We'll check the details and add it to the calendar if it's a fit. This usually takes a few days.",
      need: "Please fill in the name, town and details.",
      fail: "Sorry, that didn't go through.", failP: "You can send it by email instead; we've filled everything in for you.",
      almost: "Almost done!", almostP: "Your email app should open with everything filled in. Press send there to finish. If it didn't open, email us at {{TO}}.",
      byEmail: "Send by email", mailNote: "This opens your email app with your submission filled in. Just press send."
    },
    es: {
      open: "Enviar un evento", openShort: "Enviar", title: "Cuéntanos",
      ctaH: "¿Sabes de algo que nos falta?", ctaP: "Eventos, clases, lugares para visitar o una corrección a algo publicado. Envíanoslo y lo revisaremos.",
      intro: "¿Conoces un evento, una clase o un lugar que deberíamos incluir? Envíanoslo. Revisamos cada envío antes de agregarlo al calendario.",
      type: "¿Qué es?", tEvent: "Un evento", tClass: "Una clase o programa", tPlace: "Un lugar para visitar", tFix: "Una corrección a algo publicado",
      town: "Pueblo", townOther: "Otro pueblo (indícalo abajo)", choose: "Elige…",
      name: "Nombre del evento, clase o lugar", when: "Fecha(s) y hora", whenHint: "p. ej. sáb 24 de oct, 10am",
      where: "Dónde (lugar y dirección)", ages: "Edades", cost: "Costo", costHint: "p. ej. Gratis, $10 por niño",
      link: "Enlace para más información", details: "Detalles", detailsHint: "¿Qué deben saber las familias? Inscripción, qué llevar, cualquier otra cosa.",
      you: "Tu nombre (opcional)", email: "Tu correo (opcional)", emailHint: "Solo lo usamos si tenemos una pregunta sobre este envío.",
      organizer: "Soy quien organiza o trabajo para el anfitrión", send: "Enviar", sending: "Enviando…", cancel: "Cancelar", close: "Cerrar",
      thanks: "¡Gracias! Lo recibimos.", thanksP: "Revisaremos los detalles y lo agregaremos al calendario si encaja. Suele tardar unos días.",
      need: "Completa el nombre, el pueblo y los detalles.",
      fail: "Lo sentimos, no se pudo enviar.", failP: "Puedes enviarlo por correo; ya llenamos todo por ti.",
      almost: "¡Casi listo!", almostP: "Tu aplicación de correo debería abrirse con todo ya escrito. Presiona enviar allí para terminar. Si no se abrió, escríbenos a {{TO}}.",
      byEmail: "Enviar por correo", mailNote: "Se abrirá tu aplicación de correo con tu envío ya escrito. Solo presiona enviar."
    }
  };
  const lang = () => { try { return (localStorage.getItem("ctk-lang") || document.documentElement.lang || "en").slice(0, 2) === "es" ? "es" : "en"; } catch (_) { return "en"; } };
  const L = () => T[lang()];
  const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const pageTown = () => (window.TOWN && window.TOWN.townLabel ? window.TOWN.townLabel.replace(/, CT$/, "") : "");
  const track = (n, p) => { try { window.ctkTrack && window.ctkTrack(n, p); } catch (_) {} };

  let dlg = null;
  function build(preset) {
    const l = L(), town = pageTown();
    const opt = (v, txt, sel) => `<option value="${esc(v)}"${sel ? " selected" : ""}>${esc(txt)}</option>`;
    const types = [["event", l.tEvent], ["class", l.tClass], ["place", l.tPlace], ["fix", l.tFix]];
    dlg.innerHTML = `
<form class="sbm" novalidate>
  <div class="sbm-head"><h2>${esc(l.title)}</h2><button type="button" class="sbm-x" data-sbm-close aria-label="${esc(l.close)}">&times;</button></div>
  <p class="sbm-intro">${esc(l.intro)}</p>
  <div class="sbm-grid">
    <label class="full">${esc(l.type)}<select name="type">${types.map(([v, t]) => opt(v, t, v === (preset || "event"))).join("")}</select></label>
    <label>${esc(l.town)} *<select name="town" required>${opt("", l.choose, !town)}${TOWNS.map(t => opt(t, t, t === town)).join("")}${opt("Other", l.townOther, false)}</select></label>
    <label>${esc(l.name)} *<input name="name" required maxlength="200"></label>
    <label>${esc(l.when)}<input name="when" maxlength="200" placeholder="${esc(l.whenHint)}"></label>
    <label>${esc(l.where)}<input name="where" maxlength="200"></label>
    <label>${esc(l.ages)}<input name="ages" maxlength="100"></label>
    <label>${esc(l.cost)}<input name="cost" maxlength="100" placeholder="${esc(l.costHint)}"></label>
    <label class="full">${esc(l.link)}<input name="link" type="url" maxlength="500" placeholder="https://"></label>
    <label class="full">${esc(l.details)} *<textarea name="details" rows="4" required maxlength="3000" placeholder="${esc(l.detailsHint)}"></textarea></label>
    <label>${esc(l.you)}<input name="from" maxlength="100" autocomplete="name"></label>
    <label>${esc(l.email)}<input name="email" type="email" maxlength="200" autocomplete="email"><small>${esc(l.emailHint)}</small></label>
    <label class="full sbm-check"><input type="checkbox" name="organizer" value="yes"> ${esc(l.organizer)}</label>
    <input type="checkbox" name="botcheck" class="sbm-hp" tabindex="-1" autocomplete="off" aria-hidden="true">
  </div>
  <p class="sbm-msg" role="alert" hidden></p>
  <div class="sbm-actions"><button type="button" class="act sbm-cancel" data-sbm-close>${esc(l.cancel)}</button><button type="submit" class="btn sbm-send">${esc(l.send)}</button></div>
  ${WEB3FORMS_KEY ? "" : `<p class="sbm-note">${esc(l.mailNote)}</p>`}
</form>`;
    const form = dlg.querySelector("form");
    form.addEventListener("submit", onSubmit);
    dlg.querySelectorAll("[data-sbm-close]").forEach(b => b.onclick = () => dlg.close());
  }

  function collect(form) {
    const fd = new FormData(form), v = k => (fd.get(k) || "").toString().trim();
    return { type: v("type"), town: v("town"), name: v("name"), when: v("when"), where: v("where"), ages: v("ages"), cost: v("cost"),
             link: v("link"), details: v("details"), from: v("from"), email: v("email"), organizer: v("organizer") ? "yes" : "no", bot: fd.get("botcheck") };
  }
  const subjectOf = d => `[CT Kids Calendar] ${d.type} submission: ${d.name} (${d.town})`;
  const bodyOf = d => [
    `Type: ${d.type}`, `Town: ${d.town}`, `Name: ${d.name}`, `When: ${d.when}`, `Where: ${d.where}`, `Ages: ${d.ages}`,
    `Cost: ${d.cost}`, `Link: ${d.link}`, ``, `Details:`, d.details, ``, `Submitted by: ${d.from || "(not given)"}`,
    `Email: ${d.email || "(not given)"}`, `Organizer: ${d.organizer}`, `Page: ${location.href}`, `Language: ${lang()}`
  ].join("\n");
  const mailtoOf = d => `mailto:${SUBMIT_TO}?subject=${encodeURIComponent(subjectOf(d))}&body=${encodeURIComponent(bodyOf(d))}`;

  function showDone(l, viaEmail) {
    const h = viaEmail ? l.almost : l.thanks, p = viaEmail ? l.almostP.replace("{{TO}}", SUBMIT_TO) : l.thanksP;
    dlg.querySelector("form").innerHTML = `<div class="sbm-head"><h2>${esc(h)}</h2><button type="button" class="sbm-x" data-sbm-close aria-label="${esc(l.close)}">&times;</button></div>
      <p class="sbm-intro">${esc(p)}</p><div class="sbm-actions"><button type="button" class="btn" data-sbm-close>${esc(l.close)}</button></div>`;
    dlg.querySelectorAll("[data-sbm-close]").forEach(b => b.onclick = () => dlg.close());
  }

  async function onSubmit(ev) {
    ev.preventDefault();
    const form = ev.target, l = L(), d = collect(form), msg = form.querySelector(".sbm-msg");
    if (d.bot) return;                                     // spam honeypot
    if (!d.name || !d.town || !d.details) { msg.textContent = l.need; msg.hidden = false; return; }
    msg.hidden = true;
    if (!WEB3FORMS_KEY) { track("submit_event", { method: "email", sub_type: d.type, sub_town: d.town }); location.href = mailtoOf(d); showDone(l, true); return; }
    const btn = form.querySelector(".sbm-send"); btn.disabled = true; btn.textContent = l.sending;
    try {
      const r = await fetch("https://api.web3forms.com/submit", {
        method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({ access_key: WEB3FORMS_KEY, subject: subjectOf(d), from_name: "CT Kids Calendar", replyto: d.email || undefined,
          message: bodyOf(d), type: d.type, town: d.town, event_name: d.name, when: d.when, where: d.where, ages: d.ages, cost: d.cost,
          link: d.link, details: d.details, submitted_by: d.from, email: d.email, organizer: d.organizer, page: location.href })
      });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || j.success === false) throw new Error("send failed");
      track("submit_event", { method: "form", sub_type: d.type, sub_town: d.town });
      showDone(l);
    } catch (_) {
      btn.disabled = false; btn.textContent = l.send;
      msg.innerHTML = `<strong>${esc(l.fail)}</strong> ${esc(l.failP)} <a href="${esc(mailtoOf(d))}">${esc(l.byEmail)}</a>`; msg.hidden = false;
    }
  }

  function open(preset) {
    if (!dlg) { dlg = document.createElement("dialog"); dlg.className = "sbm-dlg"; document.body.appendChild(dlg);
      dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close(); }); }
    build(preset);
    if (dlg.showModal) dlg.showModal(); else dlg.setAttribute("open", "");
    track("submit_open", { sub_type: preset || "event" });
    setTimeout(() => { const f = dlg.querySelector('[name="name"]'); f && f.focus(); }, 30);
  }
  document.addEventListener("click", e => { const b = e.target.closest("[data-submit]"); if (!b) return; e.preventDefault(); open(b.getAttribute("data-submit") || "event"); });
  // label the buttons in the current language (and again after the language toggle)
  function relabel() { document.querySelectorAll("[data-submit-label]").forEach(el => el.textContent = L()[el.getAttribute("data-submit-label")] || el.textContent); document.querySelectorAll("[data-submit-aria]").forEach(el => el.setAttribute("aria-label", L()[el.getAttribute("data-submit-aria")])); }
  document.addEventListener("click", e => { if (e.target.closest("#langBtn")) setTimeout(relabel, 50); });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", relabel); else relabel();
  window.ctkOpenSubmit = open;
})();
