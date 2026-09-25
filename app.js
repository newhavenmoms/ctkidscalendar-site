(function(){
/* =========================================================================
   CT KIDS CALENDAR — shared engine
   Every town page defines `window.TOWN = {...}` BEFORE loading this file.
   See /shared/TOWN-TEMPLATE.md for the full shape and a worked example.
   ========================================================================= */
const T = window.TOWN || {};
const BRAND = T.name || "CT Kids Calendar";
const SITE = T.url || "";
const EMAIL = T.email || "";
const TOWN_LABEL = T.townLabel || "";
const V = T.venues || {};
const E = (T.events || []).slice();
const TBA = T.tba || [];
const VM = T.venueMeta || {};
const HOODS = (T.hoods || []).slice(); // [] hides the neighborhood filter
const CL = (T.classes || []).slice();
const EXTRA_RESOURCES = T.extraResources || []; // town-specific add-ons to the shared resource list
const U = T.calendarThrough || "2026-12-31"; // last date the week-by-week calendar covers

/* ---------- shared, statewide resources (same for every CT town) ---------- */
const HELP = {
  title:"If you're struggling right now",
  items:[
    {name:"National Maternal Mental Health Hotline", tel:"18338526262", num:"1-833-852-6262", desc:"Call or text, 24/7, for pregnant and new moms. Free and in English and Spanish."},
    {name:"Postpartum Support International", tel:"18009444773", num:"1-800-944-4773", desc:"Helpline for postpartum depression and anxiety, plus free online support groups."},
    {name:"Connecticut 2-1-1", tel:"211", num:"Dial 2-1-1", desc:"Connects you to local help with food, housing, utilities, childcare and diapers."},
    {name:"Emergency", tel:"911", num:"911", desc:"For any immediate danger to you or your child."}
  ]
};
const RESOURCES=[
  {for:"Food and nutrition", name:"WIC", desc:"Healthy food, formula help and breastfeeding support for pregnant people and kids under 5.", a:"Find your nearest WIC office", href:"https://portal.ct.gov/DPH/WIC/Find-a-Local-Agency"},
  {for:"Diapers", name:"The Diaper Bank of Connecticut", desc:"Gives out free diapers through partner agencies across the state. Dial 2-1-1 to find the nearest pickup spot.", a:"Visit the Diaper Bank", href:"https://www.thediaperbank.org"},
  {for:"Health insurance", name:"HUSKY Health", desc:"Connecticut's free and low-cost coverage for kids and for pregnant and postpartum moms.", a:"Check HUSKY eligibility", href:"https://www.huskyhealthct.org"},
  {for:"Development questions", name:"Connecticut Birth to Three", desc:"Free early-intervention evaluations if you have questions about how your baby or toddler is talking, moving or playing. You don't need a doctor's referral.", a:"Visit Birth to Three", href:"https://www.birth23.org"},
  {for:"Paying for childcare", name:"Care 4 Kids", desc:"The state's childcare subsidy program for working families.", a:"See if you qualify", href:"https://www.ctcare4kids.com"}
];
const LIBRARY = T.library || {for:"Free, every week", name:"Your local library", desc:"Library cards are free, and most branches host storytimes, Stay & Play and other drop-in programs for little ones.", a:"Find your local library", href:"https://ctstatelibrary.org/find-a-library/"};

/* ---------- helpers ---------- */
const DOW=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
const DOWL=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
const MON=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);
const pd=s=>{const[y,m,d]=s.split("-").map(Number);return new Date(y,m-1,d)};
const key=d=>d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0");
const addDays=(d,n)=>{const x=new Date(d);x.setDate(x.getDate()+n);return x};
const esc=s=>String(s==null?"":s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const mins=t=>{const[h,m]=t.split(":").map(Number);return h*60+m};
function fmt(t){let[h,m]=t.split(":").map(Number);const pm=h>=12;h=h%12||12;return (m?`${h}:${String(m).padStart(2,"0")}`:String(h))+(pm?"pm":"am")}
function fmtShort(t){let[h,m]=t.split(":").map(Number);h=h%12||12;return m?`${h}:${String(m).padStart(2,"0")}`:String(h)}
const dLong=d=>`${DOWL[d.getDay()]} ${MON[d.getMonth()]} ${d.getDate()}`;
const dMed=d=>`${DOWL[d.getDay()]}, ${MON[d.getMonth()]} ${d.getDate()}`;
const dShort=d=>`${DOW[d.getDay()]} ${MON[d.getMonth()]} ${d.getDate()}`;
function occursOn(sc,d){const[dow,,from,until,nth]=sc;if(d.getDay()!==dow)return false;const k=key(d);if(k<from||k>until)return false;if(nth)return Math.ceil(d.getDate()/7)===nth;return true}
function eventsOn(d){
  const out=[],k=key(d);
  E.forEach(e=>{
    if(e.s)e.s.forEach(sc=>{if(occursOn(sc,d))out.push({e,times:sc[1]})});
    if(e.when)e.when.forEach(w=>{if(k>=w.from&&k<=(w.to||w.from))out.push({e,times:w.t})});
  });
  const m=new Map();
  out.forEach(o=>{const kk=o.e.t+o.e.v;if(m.has(kk))m.get(kk).times=m.get(kk).times.concat(o.times);else m.set(kk,{e:o.e,times:o.times.slice()})});
  const st=o=>o.times.length?mins(o.times[0][0]):9999;
  return [...m.values()].map(o=>{o.times.sort((a,b)=>mins(a[0])-mins(b[0]));return o}).sort((a,b)=>st(a)-st(b));
}
function timeLabel(times){
  if(!times.length)return `Showtimes<small>vary, see listing</small>`;
  if(times.length===1)return times[0][1]?`${fmt(times[0][0])}<small>to ${fmt(times[0][1])}</small>`:`${fmt(times[0][0])}<small>start</small>`;
  const dur=mins(times[0][1])-mins(times[0][0]);const same=times.every(t=>mins(t[1])-mins(t[0])===dur);
  return `${fmt(times[0][0])}<small>also ${times.slice(1).map(t=>fmtShort(t[0])).join(", ")}${same?` · ${dur} min each`:""}</small>`;
}
const town=v=>(V[v]&&V[v][2])||TOWN_LABEL;
const addrLine=v=>{const e=V[v]||["",""];return (e[1]?e[1]+", ":"")+town(v).replace(/, CT$/,"")};
const mapUrl=v=>{const e=V[v]||["",""];return "https://www.google.com/maps/search/?api=1&query="+encodeURIComponent(e[0]+", "+(e[1]?e[1]+", ":"")+town(v))};
const hoodName=h=>{const x=HOODS.find(r=>r[0]===h);return x?x[1]:""};
const slug=t=>t.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/[^a-z0-9]+/g,"-").replace(/^-|-$/g,"");
E.forEach(e=>{e.id=slug(e.t)+"--"+e.v;const m=VM[e.v]||["nearby",null];e.hood=m[0];e.indoor=m[1]});
const EMAP=new Map(E.map(e=>[e.id,e]));
const ICO={
  share:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v12M7 8l5-5 5 5"></path><path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"></path></svg>',
  pin:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6.1-7-11a7 7 0 0 1 14 0c0 4.9-7 11-7 11z"></path><circle cx="12" cy="10" r="2.5"></circle></svg>',
  cal:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3"></rect><path d="M3 10h18M8 3v4M16 3v4M12 13v5M9.5 15.5h5"></path></svg>',
  age:'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="7" r="4"></circle><path d="M5 21a7 7 0 0 1 14 0"></path></svg>'
};

/* ---------- one event row ---------- */
let uid=0;
function row(o,d){
  const e=o.e,place=(V[e.v]&&V[e.v][0])||"",tags=[];
  if(e.special)tags.push(`<span class="tag special">Big day</span>`);
  if(e.free)tags.push(`<span class="tag free">Free</span>`);
  if(e.ticket)tags.push(`<span class="tag signup">Tickets</span>`);
  else if(e.drop&&e.rsvp)tags.push(`<span class="tag drop">Drop-in</span><span class="tag signup">RSVP suggested</span>`);
  else if(e.drop)tags.push(`<span class="tag drop">Drop-in</span>`);
  else if(e.rsvp)tags.push(`<span class="tag signup">RSVP</span>`);
  else if(!e.noSignup)tags.push(`<span class="tag signup">Sign up ahead</span>`);
  if(e.check)tags.push(`<span class="tag check">Check first</span>`);
  const id="ev"+(uid++),k=d?key(d):"";
  const hood=e.hood&&e.hood!=="nearby"?" · "+hoodName(e.hood):"";
  return `<li class="ev" data-k="${d?e.id+"|"+k:""}"><details><summary aria-describedby="${id}">
    <span class="ev-time">${timeLabel(o.times)}</span>
    <span><span class="ev-title">${esc(e.t)}</span><span class="ev-place" id="${id}">${esc(place)}${esc(hood)}</span><span class="tags">${tags.join("")}</span></span>
    <span class="evside">${d?`<button class="sharebtn" type="button" data-share-e="${e.id}" data-share-d="${k}" aria-label="Share: ${esc(e.t)}">${ICO.share}</button>`:""}<span class="chev" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg></span></span>
  </summary>
  <div class="ev-more">
    <dl><dt>Ages</dt><dd>${esc(e.ages)}</dd><dt>Cost</dt><dd>${esc(e.price)}</dd><dt>Where</dt><dd><a href="${mapUrl(e.v)}" target="_blank" rel="noopener">${esc(e.special?place+", "+addrLine(e.v):addrLine(e.v))}</a></dd></dl>
    ${e.blurb?`<p>${esc(e.blurb)}</p>`:""}
    ${e.note?`<p>${esc(e.note)}</p>`:""}
    <div class="ev-actions">
      ${d?`<button class="act primary" type="button" data-share-e="${e.id}" data-share-d="${k}">${ICO.share}Share with a friend</button>
      <button class="act" type="button" data-cal-e="${e.id}" data-cal-d="${k}">${ICO.cal}Add to calendar</button>`:""}
      <a class="act" href="${mapUrl(e.v)}" target="_blank" rel="noopener">${ICO.pin}Directions</a>
      ${e.src?`<a class="act" href="${e.src}" target="_blank" rel="noopener">Organizer's page</a>`:""}
    </div>
  </div></details></li>`;
}

/* ---------- toast, dialogs ---------- */
const toastEl=document.getElementById("toast");let toastT;
function toast(msg){if(!toastEl)return;toastEl.textContent=msg;toastEl.hidden=false;clearTimeout(toastT);toastT=setTimeout(()=>toastEl.hidden=true,4500)}
function openDlg(el){if(!el)return;if(el.showModal)el.showModal();else el.setAttribute("open","")}
function closeDlg(el){if(!el)return;if(el.close)el.close();else el.removeAttribute("open")}
document.querySelectorAll("dialog.sheet").forEach(dl=>{
  dl.addEventListener("click",ev=>{if(ev.target===dl||ev.target.closest("[data-close]"))closeDlg(dl)});
});
async function copyText(t){try{await navigator.clipboard.writeText(t);return true}catch(_){const a=document.createElement("textarea");a.value=t;document.body.appendChild(a);a.select();let ok=false;try{ok=document.execCommand("copy")}catch(__){}a.remove();return ok}}

/* ---------- sharing ---------- */
function firstTime(e,d){const o=eventsOn(d).find(x=>x.e.id===e.id);return o&&o.times.length?o.times[0]:null}
function eventShare(id,k){
  const e=EMAP.get(id);if(!e)return null;const d=pd(k),t=firstTime(e,d),place=(V[e.v]&&V[e.v][0])||"";
  return {title:e.t,text:`${e.t} at ${place}, ${dMed(d)}${t?" at "+fmt(t[0]):""}. Want to go? Found it on ${BRAND}:`,url:`${SITE}#e=${encodeURIComponent(id)}&d=${k}`};
}
function dayShare(d){return {title:BRAND,text:`${eventsOn(d).length} things to do with little ones on ${dMed(d)}. Take a look on ${BRAND}:`,url:`${SITE}#d=${key(d)}`}}
function weekendDates(){const w=today.getDay();if(w===0)return [today];if(w===6)return [today,addDays(today,1)];const sat=addDays(today,6-w);return [sat,addDays(sat,1)]}
function weekendShare(){const n=weekendDates().reduce((a,d)=>a+eventsOn(d).length,0);return {title:BRAND,text:`${n} things to do with little ones this weekend. Take a look on ${BRAND}:`,url:`${SITE}#weekend`}}
const sheet=document.getElementById("shareSheet");
function openSheet(sh){
  const full=sh.text+" "+sh.url;
  document.getElementById("sheetPreview").textContent=full;
  document.getElementById("shSms").href="sms:?&body="+encodeURIComponent(full);
  document.getElementById("shWa").href="https://wa.me/?text="+encodeURIComponent(full);
  document.getElementById("shMail").href="mailto:?subject="+encodeURIComponent(sh.title+" (via "+BRAND+")")+"&body="+encodeURIComponent(full);
  document.getElementById("shFb").href="https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(sh.url);
  document.getElementById("shCopy").onclick=async()=>{const ok=await copyText(full);closeDlg(sheet);toast(ok?"Link copied. Paste it anywhere to share.":"Couldn't copy. Press and hold the text to copy it.")};
  openDlg(sheet);
}
async function doShare(sh){
  if(!sh)return;
  if(navigator.share){try{await navigator.share(sh);return}catch(err){if(err&&err.name==="AbortError")return}}
  openSheet(sh);
}

/* ---------- add to calendar ---------- */
const calSheet=document.getElementById("calSheet");
const icsEsc=s=>String(s).replace(/\\/g,"\\\\").replace(/;/g,"\\;").replace(/,/g,"\\,").replace(/\n/g,"\\n");
const stamp=(d,t)=>key(d).replace(/-/g,"")+"T"+t.replace(":","")+"00";
function addMin(t,m){const x=mins(t)+m;return String(Math.floor(x/60)%24).padStart(2,"0")+":"+String(x%60).padStart(2,"0")}
function openCal(id,k){
  const e=EMAP.get(id);if(!e)return;const d=pd(k),t=firstTime(e,d),place=(V[e.v]&&V[e.v][0])||"";
  const where=place+", "+((V[e.v]&&V[e.v][1])?V[e.v][1]+", ":"")+town(e.v);
  const link=`${SITE}#e=${encodeURIComponent(id)}&d=${k}`;
  const desc=[e.blurb||"","Ages: "+e.ages,"Cost: "+e.price,e.src?e.src:"","","via "+BRAND+": "+link].filter((x,i)=>x||i===4).join("\n");
  let dtS,dtE,gDates;
  if(t){const end=t[1]||addMin(t[0],90);dtS=`DTSTART;TZID=America/New_York:${stamp(d,t[0])}`;dtE=`DTEND;TZID=America/New_York:${stamp(d,end)}`;gDates=`${stamp(d,t[0])}/${stamp(d,end)}`}
  else{const nx=addDays(d,1);dtS=`DTSTART;VALUE=DATE:${key(d).replace(/-/g,"")}`;dtE=`DTEND;VALUE=DATE:${key(nx).replace(/-/g,"")}`;gDates=`${key(d).replace(/-/g,"")}/${key(nx).replace(/-/g,"")}`}
  const now=new Date().toISOString().replace(/[-:]/g,"").replace(/\.\d+/,"");
  const ics=["BEGIN:VCALENDAR","VERSION:2.0",`PRODID:-//${BRAND}//EN`,"CALSCALE:GREGORIAN","METHOD:PUBLISH","BEGIN:VEVENT",`UID:${id}-${k}@${(SITE||"ctkidscalendar.com").replace(/^https?:\/\//,"").replace(/\/$/,"")}`,`DTSTAMP:${now}`,dtS,dtE,`SUMMARY:${icsEsc(e.t)}`,`LOCATION:${icsEsc(where)}`,`DESCRIPTION:${icsEsc(desc)}`,`URL:${link}`,"END:VEVENT","END:VCALENDAR"].join("\r\n");
  const a=document.getElementById("calIcs");a.href="data:text/calendar;charset=utf-8,"+encodeURIComponent(ics);a.setAttribute("download",slug(e.t)+".ics");
  document.getElementById("calGoogle").href="https://calendar.google.com/calendar/render?action=TEMPLATE&text="+encodeURIComponent(e.t)+"&dates="+gDates+"&ctz=America/New_York&details="+encodeURIComponent(desc)+"&location="+encodeURIComponent(where);
  document.getElementById("calPreview").textContent=`${e.t} · ${dMed(d)}${t?" · "+fmt(t[0]):""}`;
  openDlg(calSheet);
}

/* ---------- global clicks ---------- */
document.addEventListener("click",ev=>{
  const s=ev.target.closest("[data-share-e]");
  if(s){ev.preventDefault();ev.stopPropagation();doShare(eventShare(s.dataset.shareE,s.dataset.shareD));return}
  const c=ev.target.closest("[data-cal-e]");
  if(c){ev.preventDefault();ev.stopPropagation();openCal(c.dataset.calE,c.dataset.calD);return}
},true);

/* ---------- hero: this week & weekend ---------- */
const today=new Date();today.setHours(0,0,0,0);
const daysEl=document.getElementById("days"),dayList=document.getElementById("dayList"),dayTitle=document.getElementById("dayTitle");
const wkBtn=document.getElementById("weekendBtn");
let sel=0,wkMode=false;
const emptyDayMsg=`Nothing on the calendar this day yet. Try <a href="#things">things to do</a> instead.`;
function renderDays(){
  daysEl.innerHTML="";
  for(let i=0;i<7;i++){
    const d=addDays(today,i),n=eventsOn(d).length,b=document.createElement("button");
    b.className="day"+([0,6].includes(d.getDay())?" wkend":"");b.type="button";b.setAttribute("aria-pressed",!wkMode&&i===sel?"true":"false");
    b.innerHTML=`<span class="dow">${i===0?"Today":cap(DOW[d.getDay()])}</span><span class="num">${d.getDate()}</span><span class="cnt">${n}<span class="w"> ${n===1?"thing":"things"}</span></span>`;
    b.setAttribute("aria-label",`${dLong(d)}, ${n} events`);
    b.onclick=()=>{sel=i;wkMode=false;renderDays();renderDay()};
    daysEl.appendChild(b);
  }
  wkBtn.setAttribute("aria-pressed",wkMode?"true":"false");
}
function renderDay(){
  const lbl=document.getElementById("shareDayLabel");
  if(wkMode){
    const ds=weekendDates();
    dayTitle.textContent=ds.length>1?`This weekend, ${dShort(ds[0])} – ${dShort(ds[1])}`:"This weekend, "+dShort(ds[0]);
    lbl.textContent="Share this weekend";
    dayList.innerHTML=ds.map(d=>{const l=eventsOn(d);return `<li class="wkhead">${dMed(d)} · ${l.length}</li>`+(l.length?l.map(o=>row(o,d)).join(""):`<li class="empty">${emptyDayMsg}</li>`)}).join("");
    return;
  }
  const d=addDays(today,sel),list=eventsOn(d);
  dayTitle.textContent=(sel===0?"Today, ":sel===1?"Tomorrow, ":"")+dLong(d);
  lbl.textContent="Share this day";
  dayList.innerHTML=list.length?list.map(o=>row(o,d)).join(""):`<li class="empty">${emptyDayMsg}</li>`;
}
wkBtn.onclick=()=>{wkMode=!wkMode;if(!wkMode)sel=0;renderDays();renderDay()};
document.getElementById("shareDay").onclick=()=>doShare(wkMode?weekendShare():dayShare(addDays(today,sel)));

/* ---------- full calendar ---------- */
const weekList=document.getElementById("weekList"),weekTitle=document.getElementById("weekTitle");
const prevB=document.getElementById("prevWeek"),nextB=document.getElementById("nextWeek");
const monday=d=>{const x=new Date(d);x.setDate(x.getDate()-((x.getDay()+6)%7));return x};
const firstWeek=monday(today),lastWeek=monday(pd(U));
let wk=new Date(firstWeek),forceOpen=null;
const f={age:"all",hood:"all",free:false,dropin:false,indoor:false,special:false};
const isMobile=()=>window.matchMedia("(max-width:760px)").matches;
function pass(e){
  if(f.age!=="all"&&!e.a.includes(f.age))return false;
  if(f.hood!=="all"&&e.hood!==f.hood)return false;
  if(f.free&&!e.free)return false;
  if(f.dropin&&!e.drop)return false;
  if(f.indoor&&e.indoor!==1)return false;
  if(f.special&&!e.special)return false;
  return true;
}
function renderWeek(){
  const end=addDays(wk,6);
  weekTitle.textContent=wk.getMonth()===end.getMonth()?`${MON[wk.getMonth()]} ${wk.getDate()}–${end.getDate()}`:`${MON[wk.getMonth()]} ${wk.getDate()} – ${MON[end.getMonth()]} ${end.getDate()}`;
  prevB.disabled=wk<=firstWeek;nextB.disabled=wk>=lastWeek;
  let html="",total=0;
  for(let i=0;i<7;i++){
    const d=addDays(wk,i);if(d<today)continue;
    const list=eventsOn(d).filter(o=>pass(o.e));if(!list.length)continue;
    total+=list.length;
    const openIt=!isMobile()||total===list.length||key(d)===forceOpen;
    html+=`<details class="weekday"${openIt?" open":""}><summary><h4><span>${dMed(d)} <span class="n">· ${list.length}</span></span></h4></summary><ul class="list">${list.map(o=>row(o,d)).join("")}</ul></details>`;
  }
  weekList.innerHTML=total?html:`<p class="empty">${E.length?"Nothing matches those filters this week. Try another age group or neighborhood, or turn off a filter.":"We're still building out this town's calendar &mdash; check back soon, or <a href='#contact'>tell us what's coming up</a>."}</p>`;
}
prevB.onclick=()=>{wk=addDays(wk,-7);renderWeek()};
nextB.onclick=()=>{wk=addDays(wk,7);renderWeek()};
document.querySelectorAll("[data-age]").forEach(b=>b.onclick=()=>{f.age=b.dataset.age;document.querySelectorAll("[data-age]").forEach(x=>x.setAttribute("aria-pressed",x===b?"true":"false"));renderWeek()});
document.querySelectorAll("[data-toggle]").forEach(b=>b.onclick=()=>{const k=b.dataset.toggle;f[k]=!f[k];b.setAttribute("aria-pressed",f[k]?"true":"false");renderWeek()});
const hoodWrap=document.getElementById("hoodWrap"),hoodSel=document.getElementById("hoodSel");
function renderHoods(){
  if(!HOODS.length){if(hoodWrap)hoodWrap.style.display="none";return}
  hoodSel.innerHTML=HOODS.map(h=>`<option value="${h[0]}"${h[0]===f.hood?" selected":""}>${h[1]}</option>`).join("");
}
if(hoodSel)hoodSel.onchange=()=>{f.hood=hoodSel.value;hoodSel.classList.toggle("on",f.hood!=="all");renderWeek()};

/* ---------- big days ---------- */
const bigEl=document.getElementById("bigList"),bigSection=document.getElementById("bigdays");
function renderBig(){
  const groups={fall:["Fall festivals",""],hw:["Halloween","hw"],hol:["Holidays","hol"]};
  const byTitle=new Map();
  E.filter(e=>e.special).forEach(e=>{
    const from=e.when[0].from,last=e.when[e.when.length-1],to=last.to||last.from,cur=byTitle.get(e.t);
    if(cur){cur.to=to>cur.to?to:cur.to;cur.places.push((V[e.v]&&V[e.v][0])||"")}
    else byTitle.set(e.t,{id:e.id,g:e.special,t:e.t,from,to,places:[(V[e.v]&&V[e.v][0])||""]});
  });
  const items=[...byTitle.values()].filter(i=>i.to>=key(today)).sort((a,b)=>a.from<b.from?-1:1);
  if(!items.length&&!TBA.length){if(bigSection)bigSection.style.display="none";return}
  if(bigSection)bigSection.style.display="";
  bigEl.innerHTML=Object.entries(groups).map(([g,[lk,c]])=>{
    const dated=items.filter(i=>i.g===g).map(i=>{
      const a=pd(i.from),b=pd(i.to);
      const dd=i.from===i.to?a.getDate():(a.getMonth()===b.getMonth()?`${a.getDate()}–${b.getDate()}`:`${a.getDate()}–${MON[b.getMonth()]} ${b.getDate()}`);
      return `<li class="bd"><span class="bd-date"><span class="m">${MON[a.getMonth()]}</span><span class="d">${dd}</span></span>
        <span><strong>${esc(i.t)}</strong><span class="w">${esc([...new Set(i.places)].join(" and "))}</span>
        <span class="rowbtns"><button class="linkbtn" type="button" data-jump="${i.from}">See it on the calendar</button><button class="linkbtn" type="button" data-share-e="${i.id}" data-share-d="${i.from}">Share</button></span></span></li>`;
    }).join("");
    const tba=TBA.filter(i=>i.g===g).map(i=>`<li class="bd"><span class="bd-date tba"><span class="d">TBA</span></span>
        <span><strong>${esc(i.t)}</strong><span class="w">${esc(i.w)}</span><p>${esc(i.p)}</p>
        <a class="linkbtn" href="${i.src}" target="_blank" rel="noopener">Check for dates</a></span></li>`).join("");
    if(!dated&&!tba)return "";
    return `<div class="bdcol${c?" bd"+c:""}"><h3 class="${c}">${lk}</h3><ol>${dated}${tba}</ol></div>`;
  }).join("");
}
bigEl.addEventListener("click",ev=>{
  const b=ev.target.closest("[data-jump]");if(!b)return;
  const d=pd(b.dataset.jump);forceOpen=b.dataset.jump;wk=monday(d<today?today:d);renderWeek();forceOpen=null;
  document.getElementById("events").scrollIntoView();
});

/* ---------- classes ---------- */
const CCATS=[["all","All"],["music","Music"],["dance","Dance"],["swim","Swim"],["move","Sports & tumbling"],["art","Art & theater"],["build","Build & tinker"],["nature","Nature"]];
let ccat="all",clOpen=false;
const peek=()=>isMobile()?4:6;
const chipsEl=document.getElementById("classChips"),clEl=document.getElementById("classList"),clSection=document.getElementById("classes");
function renderClasses(){
  if(!CL.length){if(clSection)clSection.style.display="none";return}
  if(clSection)clSection.style.display="";
  const usedCats=new Set(CL.map(c=>c.c));
  chipsEl.innerHTML=CCATS.filter(c=>c[0]==="all"||usedCats.has(c[0])).map(c=>`<button class="chip" type="button" data-ccat="${c[0]}" aria-pressed="${c[0]===ccat}">${c[1]}</button>`).join("");
  const all=CL.filter(c=>ccat==="all"||c.c===ccat);
  const P=peek(),collapse=!clOpen&&all.length>P+1;
  const shown=collapse?all.slice(0,P):all;
  clEl.innerHTML=shown.map(c=>{
    const catLbl=(CCATS.find(x=>x[0]===c.c)||["",""])[1];
    return `<article class="cls" id="cl-${c.id}">
    <div class="cls-top"><div><span class="ctag ${c.c}">${catLbl}</span><h3>${esc(c.n)}</h3></div>
    <button class="sharebtn" type="button" data-share-c="${c.id}" aria-label="Share: ${esc(c.n)}">${ICO.share}</button></div>
    <p>${esc(c.blurb)}</p>
    <div class="meta"><span>${ICO.age}${esc(c.ages)}</span><span>${ICO.pin.replace('width="18" height="18"','width="15" height="15"')}${esc(c.where)}</span></div>
    <div class="links"><a class="act" href="${c.u}" target="_blank" rel="noopener">See classes</a></div>
  </article>`}).join("");
  let more="";
  if(collapse)more=`<div class="clmore"><p>Showing ${P} of ${all.length}</p><button class="act primary" type="button" data-clmore="open">Show all ${all.length} classes</button></div>`;
  else if(clOpen&&all.length>P+1)more=`<div class="clmore"><button class="act" type="button" data-clmore="close">Show fewer</button></div>`;
  let m=document.getElementById("clMore");if(!m){m=document.createElement("div");m.id="clMore";clEl.after(m)}
  m.innerHTML=more;
}
if(chipsEl)chipsEl.addEventListener("click",ev=>{const b=ev.target.closest("[data-ccat]");if(!b)return;ccat=b.dataset.ccat;clOpen=false;renderClasses()});
if(clSection)clSection.addEventListener("click",ev=>{
  const b=ev.target.closest("[data-clmore]");if(!b)return;
  if(b.dataset.clmore==="open"){clOpen=true;renderClasses();const n=clEl.children[peek()];if(n)n.querySelector("h3").setAttribute("tabindex","-1"),n.querySelector("h3").focus({preventScroll:true})}
  else{clOpen=false;renderClasses();clSection.scrollIntoView()}
});
document.addEventListener("click",ev=>{
  const b=ev.target.closest("[data-share-c]");if(!b)return;
  ev.preventDefault();ev.stopPropagation();
  const c=CL.find(x=>x.id===b.dataset.shareC);if(!c)return;
  doShare({title:c.n,text:`Check out this class: ${c.n} (${c.ages}). Found it on ${BRAND}:`,url:`${SITE}#c=${c.id}`});
},true);

/* ---------- resources ---------- */
(function renderResources(){
  const helpEl=document.getElementById("helpList");
  if(helpEl)helpEl.innerHTML=HELP.items.map(h=>`<div><span class="line">${esc(h.name)}</span><a class="num" href="tel:${h.tel}">${esc(h.num)}</a><p>${esc(h.desc)}</p></div>`).join("");
  const list=[...RESOURCES,LIBRARY,...EXTRA_RESOURCES];
  const resEl=document.getElementById("resList");
  if(resEl)resEl.innerHTML=list.map(r=>`<article><span class="for">${esc(r.for)}</span><h4>${esc(r.name)}</h4><p>${r.desc}</p><a href="${r.href}" target="_blank" rel="noopener">${esc(r.a)}</a></article>`).join("");
})();

/* ---------- ticker ---------- */
function renderTicker(){
  const items=[`Welcome to ${BRAND}`];
  const wkN=weekendDates().reduce((a,d)=>a+eventsOn(d).length,0);
  if(wkN)items.push(`${wkN} things to do this weekend`);
  const soon=key(addDays(today,21)),seen=new Set();
  E.filter(e=>e.special).forEach(e=>{const w=e.when[0];if(w.from>=key(today)&&w.from<=soon&&!seen.has(e.t)){seen.add(e.t);items.push(`${e.t} · ${dShort(pd(w.from))}`)}});
  if(EMAIL)items.push(`Know an event? ${EMAIL}`);
  if(T.instagram)items.push("@"+T.instagram.replace(/^@/,""));
  if(items.length<3)items.push("More towns coming to CT Kids Calendar");
  const one=items.map(t=>`<span>${esc(t)}</span>`).join("");
  const tt=document.getElementById("tickerTrack");if(tt)tt.innerHTML=one+one;
}

/* ---------- mobile tab bar ---------- */
(function(){
  const tabs=[...document.querySelectorAll(".tabbar a")],ids=tabs.map(t=>t.dataset.tab);
  const setActive=id=>tabs.forEach(t=>t.setAttribute("aria-current",t.dataset.tab===id?"true":"false"));
  setActive("today");
  if(!("IntersectionObserver" in window))return;
  const seen=new Map();
  const io=new IntersectionObserver(es=>{
    es.forEach(e=>seen.set(e.target.id,e.isIntersecting?e.intersectionRatio:0));
    let best=null,bv=0;ids.forEach(id=>{const v=seen.get(id)||0;if(v>bv){bv=v;best=id}});
    if(best)setActive(best);
  },{threshold:[0,.1,.25,.5],rootMargin:"-30% 0px -50% 0px"});
  ids.forEach(id=>{const el=document.getElementById(id);if(el)io.observe(el)});
})();

/* ---------- resize: re-collapse/re-expand at breakpoint ---------- */
(function(){const mq=window.matchMedia("(max-width:760px)");let last=mq.matches;
  const re=()=>{if(mq.matches!==last){last=mq.matches;renderWeek();renderClasses()}};
  if(mq.addEventListener)mq.addEventListener("change",re);else if(mq.addListener)mq.addListener(re);
  window.addEventListener("resize",re);})();

/* ---------- initial render ---------- */
renderHoods();renderDays();renderDay();renderWeek();renderBig();renderClasses();renderTicker();

/* ---------- links: shared events, days, weekend ---------- */
function handleHash(){
  const h=location.hash.slice(1);
  if(h.startsWith("c=")){const id=h.slice(2);ccat="all";clOpen=true;renderClasses();const el=document.getElementById("cl-"+id);if(el){el.classList.add("flash");setTimeout(()=>el.scrollIntoView({block:"center"}),60);toast(`A friend shared this class with you on ${BRAND}.`)}return}
  if(h==="weekend"){wkMode=true;renderDays();renderDay();document.getElementById("today").scrollIntoView();toast(`A friend shared this weekend's plans with you on ${BRAND}.`);return}
  if(!/^(e|d)=/.test(h))return;
  const q=new URLSearchParams(h),k=q.get("d");if(!k||!/^\d{4}-\d{2}-\d{2}$/.test(k))return;
  const d=pd(k),id=q.get("e");
  if(d<today){toast("That day has passed. Here's what's coming up instead.");document.getElementById("today").scrollIntoView();return}
  const diff=Math.round((d-today)/864e5);
  if(!id&&diff<7){sel=diff;wkMode=false;renderDays();renderDay();document.getElementById("today").scrollIntoView();toast(`A friend shared this day with you on ${BRAND}.`);return}
  forceOpen=k;wk=monday(d);renderWeek();forceOpen=null;
  const tgt=id?document.querySelector(`#weekList .ev[data-k="${CSS.escape(id+"|"+k)}"]`):null;
  if(tgt){tgt.querySelector("details").open=true;tgt.classList.add("flash");setTimeout(()=>tgt.scrollIntoView({block:"center"}),60);const e=EMAP.get(id);toast(`A friend shared ${e?e.t:"this event"} with you on ${BRAND}.`)}
  else{document.getElementById("events").scrollIntoView();if(!id)toast(`A friend shared this day with you on ${BRAND}.`)}
}
handleHash();
window.addEventListener("hashchange",handleHash);
})();
