(function(){
/* =========================================================================
   CT KIDS CALENDAR — shared engine (bilingual)
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

/* ---------- language ---------- */
let LANG="en";
try{
  const q=new URLSearchParams(location.search).get("lang");
  const saved=localStorage.getItem("ctk-lang");
  LANG=(q==="es"||q==="en")?q:(saved||((navigator.language||"").toLowerCase().startsWith("es")?"es":"en"));
}catch(_){}
const tx=(k,...args)=>{const v=UI[LANG][k];return typeof v==="function"?v(...args):(v!==undefined?v:UI.en[k])};
window.DATA_ES = window.DATA_ES || {};
const DATA_ES = window.DATA_ES;
/* The big shared Spanish dictionary is only downloaded when someone actually switches to Spanish. */
function ensureEs(cb){
  if(window.__ES_LOADED){cb();return}
  const el=document.createElement("script");
  el.src=window.ES_DATA_SRC||"/shared/data-es.js";
  el.onload=()=>cb();el.onerror=()=>cb();
  document.head.appendChild(el);
}
const dx=s=>LANG==="es"&&s&&DATA_ES[s]?DATA_ES[s]:s;

const UI={
en:{
  navBig:"Big days", navCal:"Calendar", navClasses:"Classes", navThings:"Things to do", navRes:"Resources",
  allTowns:"\u2190 All towns", contact:"Contact", suggestTown:"Suggest a town",
  today:"Today", thing:"thing", things:"things", thisWeekend:"This weekend",
  emptyDay:'Nothing on the calendar this day yet. Try <a href="#things">things to do</a> instead.',
  weekendTitle:(a,b)=>a===b?`This weekend, ${a}`:`This weekend, ${a} \u2013 ${b}`,
  shareWeekend:"Share this weekend", shareDayLbl:"Share this day",
  todayPrefix:"Today, ", tomorrowPrefix:"Tomorrow, ",
  bigDay:"Big day", free:"Free", tickets:"Tickets", dropIn:"Drop-in", rsvpSuggested:"RSVP suggested",
  rsvp:"RSVP", signUpAhead:"Sign up ahead", checkFirst:"Check first",
  ages:"Ages", cost:"Cost", where:"Where",
  directions:"Directions", organizerPage:"Organizer's page", shareWithFriend:"Share with a friend", addToCal:"Add to calendar",
  seeOnCal:"See it on the calendar", share:"Share", tba:"TBA", checkForDates:"Check for dates",
  groupFall:"Fall festivals", groupShows:"Shows & performances", groupHw:"Halloween", groupHol:"Holidays",
  noMatchFilters:"Nothing matches those filters this week. Try another age group or neighborhood, or turn off a filter.",
  buildingCal:'We\u2019re still building out this town\u2019s calendar \u2014 check back soon, or <a href="#contact">tell us what\u2019s coming up</a>.',
  catAll:"All", catMusic:"Music", catDance:"Dance", catSwim:"Swim", catMove:"Sports & tumbling",
  catArt:"Art & theater", catBuild:"Build & tinker", catNature:"Nature",
  showingOf:(p,n)=>`Showing ${p} of ${n}`, showAllN:n=>`Show all ${n} classes`, showFewer:"Show fewer", seeClasses:"See classes",
  welcomeTo:b=>`Welcome to ${b}`, thingsWeekendN:n=>`${n} things to do this weekend`,
  knowEvent:e=>`Know an event? ${e}`, moreTowns:"More towns coming to CT Kids Calendar",
  ageAll:"All ages", ageBaby:"Baby", ageToddler:"Toddler", agePreschool:"Preschool", ageBig:"Big kids",
  filterFree:"Free", filterDropin:"Drop-in", filterIndoor:"Indoor", filterBig:"Big days",
  neighborhoodAll:"All neighborhoods",
  weekPrev:"Previous week", weekNext:"Next week",
  copyLink:"Copy link", copied:"Link copied. Paste it anywhere to share.", copyFail:"Couldn\u2019t copy. Press and hold the text to copy it.",
  friendDay:b=>`A friend shared this day with you on ${b}.`, friendWeekend:b=>`A friend shared this weekend\u2019s plans with you on ${b}.`,
  friendClass:b=>`A friend shared this class with you on ${b}.`, friendEvent:(t,b)=>`A friend shared ${t} with you on ${b}.`,
  friendEventGeneric:b=>`A friend shared this event with you on ${b}.`, pastDay:"That day has passed. Here\u2019s what\u2019s coming up instead.",
  langBtn:"Espa\u00f1ol",
  heroH1:'What are we doing <em>today?</em>',
  heroLede:t=>`Storytimes, festivals, classes and things to do for little ones in ${t}, checked and gathered in one place. Tap a day to see what's on.`,
  weekAhead:t=>`The week ahead in ${t}, Conn.`,
  secBigDays:"Big days", bigIntro:"The once-a-year stuff worth planning around: festivals, live shows, Halloween fun and holiday favorites. Tap one to jump to it on the calendar.",
  swipeHw:"Swipe for Halloween and holidays",
  secCalendar:"The calendar", calIntro:"Everything we're tracking, week by week. Narrow it down by age, or show only the free, drop-in or rainy-day stuff.",
  filterAges:"Ages", ageBabies:"Babies", ageToddlers:"Toddlers", agePreschoolF:"Preschool", ageBigKids:"Big kids",
  filterArea:"Area", filterShowOnly:"Show only", filterIndoorLong:"Rainy day (indoors)",
  finePrint:'Holiday closures aren\u2019t always reflected here. Events marked "Check first" are recurring slots we haven\u2019t been able to confirm for every date, so look at the organizer\u2019s page before you head out.',
  secThings:"Things to do anytime", thingsIntro:"No schedule needed. Good for whenever cabin fever hits \u2014 just check each spot's hours before you head out, since not everything opens early.",
  swipeThings:"Swipe for rainy-day spots and short drives",
  getOutside:"Get outside", rainyDay:"Rainy day, indoors", shortDrive:"Worth a short drive",
  secClasses:"Classes & lessons", classesIntro:"Weekly classes worth signing up for, from baby music and first ballet to swim lessons and preschool soccer. Most run in sessions, so check each program's site for start dates and prices.",
  secResources:"Resources for parents", resIntro:"Help with the big things and the everyday things, from pregnancy through the toddler years.",
  today2:"Today", tabToday:"Today", tabBigDays:"Big days", tabCalendar:"Calendar", tabClasses:"Classes", tabToDo:"To do", tabHelp:"Help",
  shareTitle:"Share with a friend", textMsg:"Text message", whatsapp:"WhatsApp", email:"Email", facebook:"Facebook",
  addCalTitle:"Add to your calendar", appleOutlook:"Apple, Outlook or other calendar", googleCal:"Google Calendar", close:"Close",
  footerPart:t=>`${t} Kids Calendar \u00b7 part of <a href="https://ctkidscalendar.com/">CT Kids Calendar</a>`,
  footerChecked:d=>`Schedules last checked ${d} \u00b7 <a href="#privacy">Privacy policy</a>`,
  privacyTitle:"Privacy policy", privacyUpdated:d=>`Effective ${d}`,
  privacyIntro:(t,d)=>`${t} Kids Calendar (${d}) is part of CT Kids Calendar, a free guide to events, classes and resources for families across Connecticut. We keep things simple: this site has no accounts, no advertising trackers and no cookies. We count visits anonymously so we know what's useful. This policy explains the little information that does change hands when you use the site.`,
  privH1:"Information we collect", privP1:"We don't collect personal information through the website itself. You can browse the calendar, classes and resources without telling us who you are, and the site doesn't set cookies.",
  privP2:"To see how many people use the site, we use GoatCounter, a privacy-friendly visit counter. It records which pages are viewed, the website that sent you here (like Instagram), your general location (country and region) and your browser and screen size. It doesn't use cookies, doesn't follow you to other websites, and doesn't collect your name or anything that identifies you personally.",
  privH2:"How we use it", privLi1:"To publish event details we're given, like the name, place, time, ages, price and the organizer's public link.", privLi2:"To talk with businesses and organizations about sponsorship.",
  privP3:"We don't sell, rent or trade your information, and we don't add you to a mailing list without asking.",
  privH3:"Services we rely on", privP4:"A few outside services help run the site, and they may receive basic technical information such as your IP address when your browser connects to them:",
  privGh:'<strong>GitHub Pages</strong> hosts the site. GitHub may keep server logs, including visitor IP addresses, for security. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">GitHub privacy statement</a>.',
  privGf:'<strong>Google Fonts</strong> supplies the site\u2019s typefaces, so your browser requests them from Google. See <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Google\u2019s privacy policy</a>.',
  privGc:'<strong>GoatCounter</strong> counts visits anonymously, as described above. See <a href="https://www.goatcounter.com/help/privacy" target="_blank" rel="noopener">GoatCounter\u2019s privacy policy</a>.',
  privP5:"The site also links to other websites, such as Google Maps, Google Calendar, event organizers and community resources. Those sites have their own privacy practices, which we don't control.",
  privH4:"Children's privacy", privP6:"This site is written for parents and caregivers. It isn't directed at children under 13, and we don't knowingly collect information from them. This site doesn't currently have a way to submit information directly, which further limits this risk.",
  privH5:"Keeping and deleting your information", privP7:"We don't currently have a public contact address, so no emails are being collected yet. This policy will be updated when that changes.",
  privH6:"Changes to this policy", privP8:"If we add something new, like a newsletter sign-up, we'll update this policy first and change the date at the top.",
  backToCal:"Back to the calendar",
},
es:{
  navBig:"D\u00edas especiales", navCal:"Calendario", navClasses:"Clases", navThings:"Qu\u00e9 hacer", navRes:"Recursos",
  allTowns:"\u2190 Todos los pueblos", contact:"Contacto", suggestTown:"Sugerir un pueblo",
  today:"Hoy", thing:"cosa", things:"cosas", thisWeekend:"Este fin de semana",
  emptyDay:'Nada en el calendario para este d\u00eda todav\u00eda. Prueba <a href="#things">qu\u00e9 hacer</a> en su lugar.',
  weekendTitle:(a,b)=>a===b?`Este fin de semana, ${a}`:`Este fin de semana, ${a} \u2013 ${b}`,
  shareWeekend:"Compartir este fin de semana", shareDayLbl:"Compartir este d\u00eda",
  todayPrefix:"Hoy, ", tomorrowPrefix:"Ma\u00f1ana, ",
  bigDay:"D\u00eda especial", free:"Gratis", tickets:"Boletos", dropIn:"Sin inscripci\u00f3n", rsvpSuggested:"RSVP sugerido",
  rsvp:"RSVP", signUpAhead:"Inscripci\u00f3n previa", checkFirst:"Verifica antes",
  ages:"Edades", cost:"Costo", where:"D\u00f3nde",
  directions:"C\u00f3mo llegar", organizerPage:"P\u00e1gina del organizador", shareWithFriend:"Compartir con un amigo", addToCal:"Agregar al calendario",
  seeOnCal:"Ver en el calendario", share:"Compartir", tba:"Pronto", checkForDates:"Ver fechas",
  groupFall:"Festivales de oto\u00f1o", groupShows:"Espect\u00e1culos y funciones", groupHw:"Halloween", groupHol:"Fiestas de fin de a\u00f1o",
  noMatchFilters:"Nada coincide con esos filtros esta semana. Prueba otro grupo de edad o vecindario, o desactiva un filtro.",
  buildingCal:'Todav\u00eda estamos construyendo el calendario de este pueblo \u2014 vuelve pronto, o <a href="#contact">cu\u00e9ntanos qu\u00e9 se viene</a>.',
  catAll:"Todas", catMusic:"M\u00fasica", catDance:"Danza", catSwim:"Nataci\u00f3n", catMove:"Deportes y gimnasia",
  catArt:"Arte y teatro", catBuild:"Construir y crear", catNature:"Naturaleza",
  showingOf:(p,n)=>`Mostrando ${p} de ${n}`, showAllN:n=>`Ver las ${n} clases`, showFewer:"Ver menos", seeClasses:"Ver clases",
  welcomeTo:b=>`Bienvenido a ${b}`, thingsWeekendN:n=>`${n} cosas para hacer este fin de semana`,
  knowEvent:e=>`\u00bfConoces un evento? ${e}`, moreTowns:"M\u00e1s pueblos pr\u00f3ximamente en CT Kids Calendar",
  ageAll:"Todas las edades", ageBaby:"Beb\u00e9s", ageToddler:"Peque\u00f1os", agePreschool:"Preescolar", ageBig:"Ni\u00f1os grandes",
  filterFree:"Gratis", filterDropin:"Sin inscripci\u00f3n", filterIndoor:"Interior", filterBig:"D\u00edas especiales",
  neighborhoodAll:"Todos los vecindarios",
  weekPrev:"Semana anterior", weekNext:"Semana siguiente",
  copyLink:"Copiar enlace", copied:"Enlace copiado. P\u00e9galo donde quieras compartirlo.", copyFail:"No se pudo copiar. Mant\u00e9n presionado el texto para copiarlo.",
  friendDay:b=>`Un amigo comparti\u00f3 este d\u00eda contigo en ${b}.`, friendWeekend:b=>`Un amigo comparti\u00f3 los planes de este fin de semana contigo en ${b}.`,
  friendClass:b=>`Un amigo comparti\u00f3 esta clase contigo en ${b}.`, friendEvent:(t,b)=>`Un amigo comparti\u00f3 ${t} contigo en ${b}.`,
  friendEventGeneric:b=>`Un amigo comparti\u00f3 este evento contigo en ${b}.`, pastDay:"Ese d\u00eda ya pas\u00f3. Esto es lo que sigue.",
  langBtn:"English",
  heroH1:'\u00bfQu\u00e9 hacemos <em>hoy?</em>',
  heroLede:t=>`Cuentacuentos, festivales, clases y cosas que hacer con los m\u00e1s peque\u00f1os en ${t}, verificados y reunidos en un solo lugar. Toca un d\u00eda para ver qu\u00e9 hay.`,
  weekAhead:t=>`La semana en ${t}, Connecticut.`,
  secBigDays:"D\u00edas especiales", bigIntro:"Lo que pasa una vez al a\u00f1o y vale la pena planear: festivales, espect\u00e1culos en vivo, diversi\u00f3n de Halloween y favoritos navide\u00f1os. Toca uno para verlo en el calendario.",
  swipeHw:"Desliza para ver Halloween y las fiestas",
  secCalendar:"El calendario", calIntro:"Todo lo que estamos siguiendo, semana a semana. Filtra por edad, o muestra solo lo gratis, sin inscripci\u00f3n o para d\u00edas de lluvia.",
  filterAges:"Edades", ageBabies:"Beb\u00e9s", ageToddlers:"Peque\u00f1os", agePreschoolF:"Preescolar", ageBigKids:"Ni\u00f1os grandes",
  filterArea:"Zona", filterShowOnly:"Mostrar solo", filterIndoorLong:"D\u00eda de lluvia (interior)",
  finePrint:'Los cierres por d\u00edas festivos no siempre se reflejan aqu\u00ed. Los eventos marcados "Verifica antes" son horarios recurrentes que no hemos podido confirmar para cada fecha, as\u00ed que revisa la p\u00e1gina del organizador antes de salir.',
  secThings:"Qu\u00e9 hacer en cualquier momento", thingsIntro:"No hace falta un horario. Ideal para cuando ataca el aburrimiento \u2014 solo revisa el horario de cada lugar antes de salir, ya que no todos abren temprano.",
  swipeThings:"Desliza para ver lugares para d\u00edas de lluvia y paseos cortos",
  getOutside:"Al aire libre", rainyDay:"D\u00eda de lluvia, interior", shortDrive:"Vale la pena un paseo corto",
  secClasses:"Clases y lecciones", classesIntro:"Clases semanales que vale la pena tomar, desde m\u00fasica para beb\u00e9s y primer ballet hasta nataci\u00f3n y f\u00fatbol preescolar. La mayor\u00eda funciona por sesiones, as\u00ed que revisa el sitio de cada programa para fechas de inicio y precios.",
  secResources:"Recursos para padres", resIntro:"Ayuda con las cosas grandes y las cosas cotidianas, desde el embarazo hasta los a\u00f1os de infancia.",
  today2:"Hoy", tabToday:"Hoy", tabBigDays:"Especiales", tabCalendar:"Calendario", tabClasses:"Clases", tabToDo:"Qu\u00e9 hacer", tabHelp:"Ayuda",
  shareTitle:"Compartir con un amigo", textMsg:"Mensaje de texto", whatsapp:"WhatsApp", email:"Correo", facebook:"Facebook",
  addCalTitle:"Agregar a tu calendario", appleOutlook:"Apple, Outlook u otro calendario", googleCal:"Google Calendar", close:"Cerrar",
  footerPart:t=>`${t} Kids Calendar \u00b7 parte de <a href="https://ctkidscalendar.com/">CT Kids Calendar</a>`,
  footerChecked:d=>`Horarios verificados por \u00faltima vez en ${d} \u00b7 <a href="#privacy">Pol\u00edtica de privacidad</a>`,
  privacyTitle:"Pol\u00edtica de privacidad", privacyUpdated:d=>`Vigente desde ${d}`,
  privacyIntro:(t,d)=>`${t} Kids Calendar (${d}) es parte de CT Kids Calendar, una gu\u00eda gratuita de eventos, clases y recursos para familias en todo Connecticut. Mantenemos las cosas simples: este sitio no tiene cuentas, ni rastreadores publicitarios, ni cookies. Contamos las visitas de forma an\u00f3nima para saber qu\u00e9 es \u00fatil. Esta pol\u00edtica explica la poca informaci\u00f3n que s\u00ed cambia de manos cuando usas el sitio.`,
  privH1:"Informaci\u00f3n que recopilamos", privP1:"No recopilamos informaci\u00f3n personal a trav\u00e9s del sitio web. Puedes navegar el calendario, las clases y los recursos sin decirnos qui\u00e9n eres, y el sitio no instala cookies.",
  privP2:"Para ver cu\u00e1nta gente usa el sitio, usamos GoatCounter, un contador de visitas que respeta la privacidad. Registra qu\u00e9 p\u00e1ginas se ven, el sitio que te envi\u00f3 aqu\u00ed (como Instagram), tu ubicaci\u00f3n general (pa\u00eds y regi\u00f3n) y tu navegador y tama\u00f1o de pantalla. No usa cookies, no te sigue a otros sitios web, y no recopila tu nombre ni nada que te identifique personalmente.",
  privH2:"C\u00f3mo la usamos", privLi1:"Para publicar los detalles de eventos que nos comparten, como el nombre, lugar, hora, edades, precio y el enlace p\u00fablico del organizador.", privLi2:"Para hablar con negocios y organizaciones sobre patrocinios.",
  privP3:"No vendemos, alquilamos ni intercambiamos tu informaci\u00f3n, y no te agregamos a una lista de correo sin preguntarte.",
  privH3:"Servicios en los que nos apoyamos", privP4:"Algunos servicios externos ayudan a operar el sitio, y pueden recibir informaci\u00f3n t\u00e9cnica b\u00e1sica como tu direcci\u00f3n IP cuando tu navegador se conecta a ellos:",
  privGh:'<strong>GitHub Pages</strong> aloja el sitio. GitHub puede conservar registros del servidor, incluyendo direcciones IP de visitantes, por seguridad. Consulta la <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" target="_blank" rel="noopener">declaraci\u00f3n de privacidad de GitHub</a>.',
  privGf:'<strong>Google Fonts</strong> proporciona las tipograf\u00edas del sitio, por lo que tu navegador las solicita a Google. Consulta la <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">pol\u00edtica de privacidad de Google</a>.',
  privGc:'<strong>GoatCounter</strong> cuenta las visitas de forma an\u00f3nima, como se describe arriba. Consulta la <a href="https://www.goatcounter.com/help/privacy" target="_blank" rel="noopener">pol\u00edtica de privacidad de GoatCounter</a>.',
  privP5:"El sitio tambi\u00e9n enlaza a otros sitios web, como Google Maps, Google Calendar, organizadores de eventos y recursos comunitarios. Esos sitios tienen sus propias pr\u00e1cticas de privacidad, que no controlamos.",
  privH4:"Privacidad de los ni\u00f1os", privP6:"Este sitio est\u00e1 escrito para padres y cuidadores. No est\u00e1 dirigido a ni\u00f1os menores de 13 a\u00f1os, y no recopilamos informaci\u00f3n de ellos a sabiendas. Este sitio actualmente no tiene una forma de enviar informaci\u00f3n directamente, lo que limita a\u00fan m\u00e1s este riesgo.",
  privH5:"Conservaci\u00f3n y eliminaci\u00f3n de tu informaci\u00f3n", privP7:"Actualmente no tenemos una direcci\u00f3n de contacto p\u00fablica, as\u00ed que todav\u00eda no se recopilan correos. Esta pol\u00edtica se actualizar\u00e1 cuando eso cambie.",
  privH6:"Cambios a esta pol\u00edtica", privP8:"Si agregamos algo nuevo, como una suscripci\u00f3n a un bolet\u00edn, actualizaremos esta pol\u00edtica primero y cambiaremos la fecha en la parte superior.",
  backToCal:"Volver al calendario",
}
};

const DOW_KEYS=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"];
const DOWL_EN=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];
const DOWL_ES=["domingo","lunes","martes","mi\u00e9rcoles","jueves","viernes","s\u00e1bado"];
const DOW_ES=["dom","lun","mar","mi\u00e9","jue","vie","s\u00e1b"];
const MON_EN=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
const MON_ES=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"];
const DOW=()=>LANG==="es"?DOW_ES:DOW_KEYS;
const DOWL=()=>LANG==="es"?DOWL_ES:DOWL_EN;
const MON=()=>LANG==="es"?MON_ES:MON_EN;

/* ---------- shared, statewide resources (same for every CT town) ---------- */
const HELP = {
  title:{en:"If you're struggling right now",es:"Si est\u00e1s pasando por un momento dif\u00edcil ahora mismo"},
  items:[
    {name:{en:"National Maternal Mental Health Hotline",es:"L\u00ednea Nacional de Salud Mental Materna"}, tel:"18338526262", num:"1-833-852-6262", desc:{en:"Call or text, 24/7, for pregnant and new moms. Free and in English and Spanish.",es:"Llama o env\u00eda un mensaje, 24/7, para mam\u00e1s embarazadas y nuevas. Gratis, en ingl\u00e9s y espa\u00f1ol."}},
    {name:{en:"Postpartum Support International",es:"Postpartum Support International"}, tel:"18009444773", num:"1-800-944-4773", desc:{en:"Helpline for postpartum depression and anxiety, plus free online support groups.",es:"L\u00ednea de ayuda para depresi\u00f3n y ansiedad posparto, adem\u00e1s de grupos de apoyo gratuitos en l\u00ednea."}},
    {name:{en:"Connecticut 2-1-1",es:"Connecticut 2-1-1"}, tel:"211", num:"Dial 2-1-1", desc:{en:"Connects you to local help with food, housing, utilities, childcare and diapers.",es:"Te conecta con ayuda local para comida, vivienda, servicios p\u00fablicos, cuidado infantil y pa\u00f1ales."}},
    {name:{en:"Emergency",es:"Emergencia"}, tel:"911", num:"911", desc:{en:"For any immediate danger to you or your child.",es:"Para cualquier peligro inmediato para ti o tu hijo."}}
  ]
};
const RESOURCES=[
  {for:{en:"Food and nutrition",es:"Comida y nutrici\u00f3n"}, name:{en:"WIC",es:"WIC"}, desc:{en:"Healthy food, formula help and breastfeeding support for pregnant people and kids under 5.",es:"Comida saludable, ayuda con f\u00f3rmula y apoyo de lactancia para personas embarazadas y ni\u00f1os menores de 5 a\u00f1os."}, a:{en:"Find your nearest WIC office",es:"Encuentra tu oficina de WIC m\u00e1s cercana"}, href:"https://portal.ct.gov/DPH/WIC/Find-a-Local-Agency"},
  {for:{en:"Diapers",es:"Pa\u00f1ales"}, name:{en:"The Diaper Bank of Connecticut",es:"The Diaper Bank of Connecticut"}, desc:{en:"Gives out free diapers through partner agencies across the state. Dial 2-1-1 to find the nearest pickup spot.",es:"Reparte pa\u00f1ales gratis a trav\u00e9s de agencias asociadas en todo el estado. Marca 2-1-1 para encontrar el punto de entrega m\u00e1s cercano."}, a:{en:"Visit the Diaper Bank",es:"Visita el Diaper Bank"}, href:"https://www.thediaperbank.org"},
  {for:{en:"Health insurance",es:"Seguro m\u00e9dico"}, name:{en:"HUSKY Health",es:"HUSKY Health"}, desc:{en:"Connecticut's free and low-cost coverage for kids and for pregnant and postpartum moms.",es:"La cobertura gratuita y de bajo costo de Connecticut para ni\u00f1os y para mam\u00e1s embarazadas y posparto."}, a:{en:"Check HUSKY eligibility",es:"Verifica la elegibilidad para HUSKY"}, href:"https://www.huskyhealthct.org"},
  {for:{en:"Development questions",es:"Preguntas sobre el desarrollo"}, name:{en:"Connecticut Birth to Three",es:"Connecticut Birth to Three"}, desc:{en:"Free early-intervention evaluations if you have questions about how your baby or toddler is talking, moving or playing. You don't need a doctor's referral.",es:"Evaluaciones gratuitas de intervenci\u00f3n temprana si tienes preguntas sobre c\u00f3mo habla, se mueve o juega tu beb\u00e9 o ni\u00f1o peque\u00f1o. No necesitas referencia m\u00e9dica."}, a:{en:"Visit Birth to Three",es:"Visita Birth to Three"}, href:"https://www.birth23.org"},
  {for:{en:"Paying for childcare",es:"Pagar el cuidado infantil"}, name:{en:"Care 4 Kids",es:"Care 4 Kids"}, desc:{en:"The state's childcare subsidy program for working families.",es:"El programa estatal de subsidio de cuidado infantil para familias trabajadoras."}, a:{en:"See if you qualify",es:"Ve si calificas"}, href:"https://www.ctcare4kids.com"}
];
const LIBRARY_DEFAULT = {for:{en:"Free, every week",es:"Gratis, cada semana"}, name:{en:"Your local library",es:"Tu biblioteca local"}, desc:{en:"Library cards are free, and most branches host storytimes, Stay & Play and other drop-in programs for little ones.",es:"Las tarjetas de biblioteca son gratuitas, y la mayor\u00eda de las sucursales ofrecen cuentacuentos, Stay & Play y otros programas sin inscripci\u00f3n para los m\u00e1s peque\u00f1os."}, a:{en:"Find your local library",es:"Encuentra tu biblioteca local"}, href:"https://ctstatelibrary.org/find-a-library/"};
const LIB_T = T.library || {};
const LIBRARY = {
  for:{en:LIB_T.for||LIBRARY_DEFAULT.for.en, es:dx(LIB_T.for)||LIBRARY_DEFAULT.for.es},
  name:{en:LIB_T.name||LIBRARY_DEFAULT.name.en, es:dx(LIB_T.name)||LIBRARY_DEFAULT.name.es},
  desc:{en:LIB_T.desc||LIBRARY_DEFAULT.desc.en, es:dx(LIB_T.desc)||LIBRARY_DEFAULT.desc.es},
  a:{en:LIB_T.a||LIBRARY_DEFAULT.a.en, es:dx(LIB_T.a)||LIBRARY_DEFAULT.a.es},
  href:LIB_T.href||LIBRARY_DEFAULT.href
};

/* ---------- helpers ---------- */
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);
const pd=s=>{const[y,m,d]=s.split("-").map(Number);return new Date(y,m-1,d)};
const key=d=>d.getFullYear()+"-"+String(d.getMonth()+1).padStart(2,"0")+"-"+String(d.getDate()).padStart(2,"0");
const addDays=(d,n)=>{const x=new Date(d);x.setDate(x.getDate()+n);return x};
const esc=s=>String(s==null?"":s).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const mins=t=>{const[h,m]=t.split(":").map(Number);return h*60+m};
function fmt(t){let[h,m]=t.split(":").map(Number);const pm=h>=12;h=h%12||12;return (m?`${h}:${String(m).padStart(2,"0")}`:String(h))+(pm?"pm":"am")}
function fmtShort(t){let[h,m]=t.split(":").map(Number);h=h%12||12;return m?`${h}:${String(m).padStart(2,"0")}`:String(h)}
const dLong=d=>`${cap(DOWL()[d.getDay()])} ${MON()[d.getMonth()]} ${d.getDate()}`;
const dMed=d=>`${cap(DOWL()[d.getDay()])}, ${MON()[d.getMonth()]} ${d.getDate()}`;
const dShort=d=>`${DOW()[d.getDay()]} ${MON()[d.getMonth()]} ${d.getDate()}`;
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
  const alsoW=LANG==="es"?"tambi\u00e9n":"also", eachW=LANG==="es"?"c/u":"each", startW=LANG==="es"?"inicio":"start", varyW=LANG==="es"?"var\u00eda, ver anuncio":"vary, see listing";
  if(!times.length)return `${LANG==="es"?"Horarios":"Showtimes"}<small>${varyW}</small>`;
  if(times.length===1)return times[0][1]?`${fmt(times[0][0])}<small>${LANG==="es"?"a":"to"} ${fmt(times[0][1])}</small>`:`${fmt(times[0][0])}<small>${startW}</small>`;
  const dur=mins(times[0][1])-mins(times[0][0]);const same=times.every(t=>mins(t[1])-mins(t[0])===dur);
  return `${fmt(times[0][0])}<small>${alsoW} ${times.slice(1).map(t=>fmtShort(t[0])).join(", ")}${same?` \u00b7 ${dur} min ${eachW}`:""}</small>`;
}
const town=v=>(V[v]&&V[v][2])||TOWN_LABEL;
const addrLine=v=>{const e=V[v]||["",""];return (e[1]?e[1]+", ":"")+town(v).replace(/, CT$/,"")};
const mapUrl=v=>{const e=V[v]||["",""];return "https://www.google.com/maps/search/?api=1&query="+encodeURIComponent(e[0]+", "+(e[1]?e[1]+", ":"")+town(v))};
const hoodName=h=>{const x=HOODS.find(r=>r[0]===h);return x?(LANG==="es"&&x[2]?x[2]:x[1]):""};
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
  if(e.special)tags.push(`<span class="tag special">${tx("bigDay")}</span>`);
  if(e.free)tags.push(`<span class="tag free">${tx("free")}</span>`);
  if(e.ticket)tags.push(`<span class="tag signup">${tx("tickets")}</span>`);
  else if(e.drop&&e.rsvp)tags.push(`<span class="tag drop">${tx("dropIn")}</span><span class="tag signup">${tx("rsvpSuggested")}</span>`);
  else if(e.drop)tags.push(`<span class="tag drop">${tx("dropIn")}</span>`);
  else if(e.rsvp)tags.push(`<span class="tag signup">${tx("rsvp")}</span>`);
  else if(!e.noSignup)tags.push(`<span class="tag signup">${tx("signUpAhead")}</span>`);
  if(e.check)tags.push(`<span class="tag check">${tx("checkFirst")}</span>`);
  const id="ev"+(uid++),k=d?key(d):"";
  const hood=e.hood&&e.hood!=="nearby"?" \u00b7 "+hoodName(e.hood):"";
  return `<li class="ev" data-k="${d?e.id+"|"+k:""}"><details><summary aria-describedby="${id}">
    <span class="ev-time">${timeLabel(o.times)}</span>
    <span><span class="ev-title">${esc(dx(e.t))}</span><span class="ev-place" id="${id}">${esc(place)}${esc(hood)}</span><span class="tags">${tags.join("")}</span></span>
    <span class="evside">${d?`<button class="sharebtn" type="button" data-share-e="${e.id}" data-share-d="${k}" aria-label="${tx("share")}: ${esc(dx(e.t))}">${ICO.share}</button>`:""}<span class="chev" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 12 12"><path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg></span></span>
  </summary>
  <div class="ev-more">
    <dl><dt>${tx("ages")}</dt><dd>${esc(dx(e.ages))}</dd><dt>${tx("cost")}</dt><dd>${esc(dx(e.price))}</dd><dt>${tx("where")}</dt><dd><a href="${mapUrl(e.v)}" target="_blank" rel="noopener">${esc(e.special?place+", "+addrLine(e.v):addrLine(e.v))}</a></dd></dl>
    ${e.blurb?`<p>${esc(dx(e.blurb))}</p>`:""}
    ${e.note?`<p>${esc(dx(e.note))}</p>`:""}
    <div class="ev-actions">
      ${d?`<button class="act primary" type="button" data-share-e="${e.id}" data-share-d="${k}">${ICO.share}${tx("shareWithFriend")}</button>
      <button class="act" type="button" data-cal-e="${e.id}" data-cal-d="${k}">${ICO.cal}${tx("addToCal")}</button>`:""}
      <a class="act" href="${mapUrl(e.v)}" target="_blank" rel="noopener">${ICO.pin}${tx("directions")}</a>
      ${e.src?`<a class="act" href="${e.src}" target="_blank" rel="noopener">${tx("organizerPage")}</a>`:""}
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
  const tEsc=dx(e.t);
  const verb=LANG==="es"?"\u00bfQuieres ir? Encontrado en":"Want to go? Found it on";
  return {title:tEsc,text:`${tEsc} ${LANG==="es"?"en":"at"} ${place}, ${dMed(d)}${t?" "+(LANG==="es"?"a las":"at")+" "+fmt(t[0]):""}. ${verb} ${BRAND}:`,url:`${SITE}#e=${encodeURIComponent(id)}&d=${k}`};
}
function dayShare(d){const n=eventsOn(d).length;const verb=LANG==="es"?"con los m\u00e1s peque\u00f1os":"with little ones";const look=LANG==="es"?"Echa un vistazo en":"Take a look on";return {title:BRAND,text:`${n} ${LANG==="es"?"cosas para hacer":"things to do"} ${verb} ${LANG==="es"?"el":"on"} ${dMed(d)}. ${look} ${BRAND}:`,url:`${SITE}#d=${key(d)}`}}
function weekendDates(){const w=today.getDay();if(w===0)return [today];if(w===6)return [today,addDays(today,1)];const sat=addDays(today,6-w);return [sat,addDays(sat,1)]}
function weekendShare(){const n=weekendDates().reduce((a,d)=>a+eventsOn(d).length,0);const look=LANG==="es"?"Echa un vistazo en":"Take a look on";return {title:BRAND,text:`${n} ${LANG==="es"?"cosas para hacer con los m\u00e1s peque\u00f1os este fin de semana":"things to do with little ones this weekend"}. ${look} ${BRAND}:`,url:`${SITE}#weekend`}}
const sheet=document.getElementById("shareSheet");
function openSheet(sh){
  const full=sh.text+" "+sh.url;
  document.getElementById("sheetPreview").textContent=full;
  document.getElementById("shSms").href="sms:?&body="+encodeURIComponent(full);
  document.getElementById("shWa").href="https://wa.me/?text="+encodeURIComponent(full);
  document.getElementById("shMail").href="mailto:?subject="+encodeURIComponent(sh.title+" (via "+BRAND+")")+"&body="+encodeURIComponent(full);
  document.getElementById("shFb").href="https://www.facebook.com/sharer/sharer.php?u="+encodeURIComponent(sh.url);
  document.getElementById("shCopy").onclick=async()=>{const ok=await copyText(full);closeDlg(sheet);toast(ok?tx("copied"):tx("copyFail"))};
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
  const desc=[dx(e.blurb)||"",tx("ages")+": "+dx(e.ages),tx("cost")+": "+dx(e.price),e.src?e.src:"","","via "+BRAND+": "+link].filter((x,i)=>x||i===4).join("\n");
  let dtS,dtE,gDates;
  if(t){const end=t[1]||addMin(t[0],90);dtS=`DTSTART;TZID=America/New_York:${stamp(d,t[0])}`;dtE=`DTEND;TZID=America/New_York:${stamp(d,end)}`;gDates=`${stamp(d,t[0])}/${stamp(d,end)}`}
  else{const nx=addDays(d,1);dtS=`DTSTART;VALUE=DATE:${key(d).replace(/-/g,"")}`;dtE=`DTEND;VALUE=DATE:${key(nx).replace(/-/g,"")}`;gDates=`${key(d).replace(/-/g,"")}/${key(nx).replace(/-/g,"")}`}
  const now=new Date().toISOString().replace(/[-:]/g,"").replace(/\.\d+/,"");
  const ics=["BEGIN:VCALENDAR","VERSION:2.0",`PRODID:-//${BRAND}//EN`,"CALSCALE:GREGORIAN","METHOD:PUBLISH","BEGIN:VEVENT",`UID:${id}-${k}@${(SITE||"ctkidscalendar.com").replace(/^https?:\/\//,"").replace(/\/$/,"")}`,`DTSTAMP:${now}`,dtS,dtE,`SUMMARY:${icsEsc(dx(e.t))}`,`LOCATION:${icsEsc(where)}`,`DESCRIPTION:${icsEsc(desc)}`,`URL:${link}`,"END:VEVENT","END:VCALENDAR"].join("\r\n");
  const a=document.getElementById("calIcs");a.href="data:text/calendar;charset=utf-8,"+encodeURIComponent(ics);a.setAttribute("download",slug(e.t)+".ics");
  document.getElementById("calGoogle").href="https://calendar.google.com/calendar/render?action=TEMPLATE&text="+encodeURIComponent(dx(e.t))+"&dates="+gDates+"&ctz=America/New_York&details="+encodeURIComponent(desc)+"&location="+encodeURIComponent(where);
  document.getElementById("calPreview").textContent=`${dx(e.t)} \u00b7 ${dMed(d)}${t?" \u00b7 "+fmt(t[0]):""}`;
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
function renderDays(){
  daysEl.innerHTML="";
  for(let i=0;i<7;i++){
    const d=addDays(today,i),n=eventsOn(d).length,b=document.createElement("button");
    b.className="day"+([0,6].includes(d.getDay())?" wkend":"");b.type="button";b.setAttribute("aria-pressed",!wkMode&&i===sel?"true":"false");
    b.innerHTML=`<span class="dow">${i===0?tx("today"):cap(DOW()[d.getDay()])}</span><span class="num">${d.getDate()}</span><span class="cnt">${n}<span class="w"> ${n===1?tx("thing"):tx("things")}</span></span>`;
    b.setAttribute("aria-label",`${dLong(d)}, ${n} ${n===1?tx("thing"):tx("things")}`);
    b.onclick=()=>{sel=i;wkMode=false;renderDays();renderDay()};
    daysEl.appendChild(b);
  }
  wkBtn.setAttribute("aria-pressed",wkMode?"true":"false");
  wkBtn.textContent=tx("thisWeekend");
}
function renderDay(){
  const lbl=document.getElementById("shareDayLabel");
  if(wkMode){
    const ds=weekendDates();
    dayTitle.textContent=tx("weekendTitle",dShort(ds[0]),ds.length>1?dShort(ds[1]):dShort(ds[0]));
    lbl.textContent=tx("shareWeekend");
    dayList.innerHTML=ds.map(d=>{const l=eventsOn(d);return `<li class="wkhead">${dMed(d)} \u00b7 ${l.length}</li>`+(l.length?l.map(o=>row(o,d)).join(""):`<li class="empty">${tx("emptyDay")}</li>`)}).join("");
    return;
  }
  const d=addDays(today,sel),list=eventsOn(d);
  dayTitle.textContent=(sel===0?tx("todayPrefix"):sel===1?tx("tomorrowPrefix"):"")+dLong(d);
  lbl.textContent=tx("shareDayLbl");
  dayList.innerHTML=list.length?list.map(o=>row(o,d)).join(""):`<li class="empty">${tx("emptyDay")}</li>`;
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
  weekTitle.textContent=wk.getMonth()===end.getMonth()?`${MON()[wk.getMonth()]} ${wk.getDate()}\u2013${end.getDate()}`:`${MON()[wk.getMonth()]} ${wk.getDate()} \u2013 ${MON()[end.getMonth()]} ${end.getDate()}`;
  prevB.disabled=wk<=firstWeek;nextB.disabled=wk>=lastWeek;
  let html="",total=0;
  for(let i=0;i<7;i++){
    const d=addDays(wk,i);if(d<today)continue;
    const list=eventsOn(d).filter(o=>pass(o.e));if(!list.length)continue;
    total+=list.length;
    const openIt=!isMobile()||total===list.length||key(d)===forceOpen;
    html+=`<details class="weekday"${openIt?" open":""}><summary><h4><span>${dMed(d)} <span class="n">\u00b7 ${list.length}</span></span></h4></summary><ul class="list">${list.map(o=>row(o,d)).join("")}</ul></details>`;
  }
  weekList.innerHTML=total?html:`<p class="empty">${E.length?tx("noMatchFilters"):tx("buildingCal")}</p>`;
}
prevB.onclick=()=>{wk=addDays(wk,-7);renderWeek()};
nextB.onclick=()=>{wk=addDays(wk,7);renderWeek()};
document.querySelectorAll("[data-age]").forEach(b=>b.onclick=()=>{f.age=b.dataset.age;document.querySelectorAll("[data-age]").forEach(x=>x.setAttribute("aria-pressed",x===b?"true":"false"));renderWeek()});
document.querySelectorAll("[data-toggle]").forEach(b=>b.onclick=()=>{const k=b.dataset.toggle;f[k]=!f[k];b.setAttribute("aria-pressed",f[k]?"true":"false");renderWeek()});
const hoodWrap=document.getElementById("hoodWrap"),hoodSel=document.getElementById("hoodSel");
function renderHoods(){
  if(!HOODS.length){if(hoodWrap)hoodWrap.style.display="none";return}
  hoodSel.innerHTML=HOODS.map(h=>`<option value="${h[0]}"${h[0]===f.hood?" selected":""}>${h[0]==="all"?tx("neighborhoodAll"):(LANG==="es"&&h[2]?h[2]:h[1])}</option>`).join("");
}
if(hoodSel)hoodSel.onchange=()=>{f.hood=hoodSel.value;hoodSel.classList.toggle("on",f.hood!=="all");renderWeek()};

/* ---------- big days ---------- */
const bigEl=document.getElementById("bigList"),bigSection=document.getElementById("bigdays");
function renderBig(){
  const groups={fall:["groupFall",""],shows:["groupShows","shows"],hw:["groupHw","hw"],hol:["groupHol","hol"]};
  const byTitle=new Map();
  E.filter(e=>e.special).forEach(e=>{
    const from=e.when[0].from,last=e.when[e.when.length-1],to=last.to||last.from,cur=byTitle.get(e.t);
    if(cur){cur.to=to>cur.to?to:cur.to;cur.places.push((V[e.v]&&V[e.v][0])||"")}
    else byTitle.set(e.t,{id:e.id,g:e.special,t:e.t,from,to,places:[(V[e.v]&&V[e.v][0])||""]});
  });
  const items=[...byTitle.values()].filter(i=>i.to>=key(today)).sort((a,b)=>a.from<b.from?-1:1);
  if(!items.length&&!TBA.length){if(bigSection)bigSection.style.display="none";return}
  if(bigSection)bigSection.style.display="";
  const andWord=LANG==="es"?" y ":" and ";
  bigEl.innerHTML=Object.entries(groups).map(([g,[lk,c]])=>{
    const dated=items.filter(i=>i.g===g).map(i=>{
      const a=pd(i.from),b=pd(i.to);
      const dd=i.from===i.to?a.getDate():(a.getMonth()===b.getMonth()?`${a.getDate()}\u2013${b.getDate()}`:`${a.getDate()}\u2013${MON()[b.getMonth()]} ${b.getDate()}`);
      return `<li class="bd"><span class="bd-date"><span class="m">${MON()[a.getMonth()]}</span><span class="d">${dd}</span></span>
        <span><strong>${esc(dx(i.t))}</strong><span class="w">${esc([...new Set(i.places)].join(andWord))}</span>
        <span class="rowbtns"><button class="linkbtn" type="button" data-jump="${i.from}">${tx("seeOnCal")}</button><button class="linkbtn" type="button" data-share-e="${i.id}" data-share-d="${i.from}">${tx("share")}</button></span></span></li>`;
    }).join("");
    const tba=TBA.filter(i=>i.g===g).map(i=>`<li class="bd"><span class="bd-date tba"><span class="d">${tx("tba")}</span></span>
        <span><strong>${esc(dx(i.t))}</strong><span class="w">${esc(dx(i.w))}</span><p>${esc(dx(i.p))}</p>
        <a class="linkbtn" href="${i.src}" target="_blank" rel="noopener">${tx("checkForDates")}</a></span></li>`).join("");
    if(!dated&&!tba)return "";
    return `<div class="bdcol${c?" bd"+c:""}"><h3 class="${c}">${tx(lk)}</h3><ol>${dated}${tba}</ol></div>`;
  }).join("");
}
bigEl.addEventListener("click",ev=>{
  const b=ev.target.closest("[data-jump]");if(!b)return;
  const d=pd(b.dataset.jump);forceOpen=b.dataset.jump;wk=monday(d<today?today:d);renderWeek();forceOpen=null;
  document.getElementById("events").scrollIntoView();
});

/* ---------- classes ---------- */
const CCAT_KEYS=[["all","catAll"],["music","catMusic"],["dance","catDance"],["swim","catSwim"],["move","catMove"],["art","catArt"],["build","catBuild"],["nature","catNature"]];
let ccat="all",clOpen=false;
const peek=()=>isMobile()?4:6;
const chipsEl=document.getElementById("classChips"),clEl=document.getElementById("classList"),clSection=document.getElementById("classes");
function renderClasses(){
  if(!CL.length){if(clSection)clSection.style.display="none";return}
  if(clSection)clSection.style.display="";
  const usedCats=new Set(CL.map(c=>c.c));
  chipsEl.innerHTML=CCAT_KEYS.filter(c=>c[0]==="all"||usedCats.has(c[0])).map(c=>`<button class="chip" type="button" data-ccat="${c[0]}" aria-pressed="${c[0]===ccat}">${tx(c[1])}</button>`).join("");
  const all=CL.filter(c=>ccat==="all"||c.c===ccat);
  const P=peek(),collapse=!clOpen&&all.length>P+1;
  const shown=collapse?all.slice(0,P):all;
  clEl.innerHTML=shown.map(c=>{
    const catLbl=tx((CCAT_KEYS.find(x=>x[0]===c.c)||["",""])[1]);
    return `<article class="cls" id="cl-${c.id}">
    <div class="cls-top"><div><span class="ctag ${c.c}">${catLbl}</span><h3>${esc(dx(c.n))}</h3></div>
    <button class="sharebtn" type="button" data-share-c="${c.id}" aria-label="${tx("share")}: ${esc(dx(c.n))}">${ICO.share}</button></div>
    <p>${esc(dx(c.blurb))}</p>
    <div class="meta"><span>${ICO.age}${esc(dx(c.ages))}</span><span>${ICO.pin.replace('width="18" height="18"','width="15" height="15"')}${esc(dx(c.where))}</span></div>
    <div class="links"><a class="act" href="${c.u}" target="_blank" rel="noopener">${tx("seeClasses")}</a></div>
  </article>`}).join("");
  let more="";
  if(collapse)more=`<div class="clmore"><p>${tx("showingOf",P,all.length)}</p><button class="act primary" type="button" data-clmore="open">${tx("showAllN",all.length)}</button></div>`;
  else if(clOpen&&all.length>P+1)more=`<div class="clmore"><button class="act" type="button" data-clmore="close">${tx("showFewer")}</button></div>`;
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
  const cn=dx(c.n),ca=dx(c.ages);
  const found=LANG==="es"?"Encontrado en":"Found it on";
  doShare({title:cn,text:`${LANG==="es"?"Mira esta clase:":"Check out this class:"} ${cn} (${ca}). ${found} ${BRAND}:`,url:`${SITE}#c=${c.id}`});
},true);

/* ---------- resources ---------- */
function renderResources(){
  const helpEl=document.getElementById("helpList");
  if(helpEl)helpEl.innerHTML=HELP.items.map(h=>`<div><span class="line">${esc(h.name[LANG]||h.name.en)}</span><a class="num" href="tel:${h.tel}">${esc(h.num)}</a><p>${esc(h.desc[LANG]||h.desc.en)}</p></div>`).join("");
  const helpTitle=document.getElementById("helpTitle");
  if(helpTitle)helpTitle.textContent=HELP.title[LANG]||HELP.title.en;
  const list=[...RESOURCES,LIBRARY,...EXTRA_RESOURCES.map(r=>({for:{en:r.for,es:dx(r.for)},name:{en:r.name,es:dx(r.name)},desc:{en:r.desc,es:dx(r.desc)},a:{en:r.a,es:dx(r.a)},href:r.href}))];
  const resEl=document.getElementById("resList");
  if(resEl)resEl.innerHTML=list.map(r=>`<article><span class="for">${esc(r.for[LANG]||r.for.en)}</span><h4>${esc(r.name[LANG]||r.name.en)}</h4><p>${esc(r.desc[LANG]||r.desc.en)}</p><a href="${r.href}" target="_blank" rel="noopener">${esc(r.a[LANG]||r.a.en)}</a></article>`).join("");
}

/* ---------- ticker ---------- */
function renderTicker(){
  const items=[tx("welcomeTo",BRAND)];
  const wkN=weekendDates().reduce((a,d)=>a+eventsOn(d).length,0);
  if(wkN)items.push(tx("thingsWeekendN",wkN));
  const soon=key(addDays(today,21)),seen=new Set();
  E.filter(e=>e.special).forEach(e=>{const w=e.when[0];if(w.from>=key(today)&&w.from<=soon&&!seen.has(e.t)){seen.add(e.t);items.push(`${dx(e.t)} \u00b7 ${dShort(pd(w.from))}`)}});
  if(EMAIL)items.push(tx("knowEvent",EMAIL));
  if(T.instagram)items.push("@"+T.instagram.replace(/^@/,""));
  if(items.length<3)items.push(tx("moreTowns"));
  const one=items.map(t=>`<span>${esc(t)}</span>`).join("");
  const tt=document.getElementById("tickerTrack");if(tt)tt.innerHTML=one+one;
}

/* ---------- language switching ---------- */
function applyStaticI18n(){
  document.documentElement.lang=LANG;
  const townName=TOWN_LABEL.replace(/, CT$/,"");
  document.querySelectorAll("[data-i18n]").forEach(el=>{
    const k=el.dataset.i18n;
    if(UI.en[k]!==undefined)el.innerHTML=tx(k);
  });
  document.querySelectorAll("[data-i18n-aria]").forEach(el=>{
    const k=el.dataset.i18nAria;
    if(UI.en[k]!==undefined)el.setAttribute("aria-label",tx(k));
  });
  document.querySelectorAll("[data-i18n-town]").forEach(el=>{
    const k=el.dataset.i18nTown;
    if(UI.en[k]!==undefined)el.innerHTML=tx(k,townName);
  });
  document.querySelectorAll("[data-i18n-date]").forEach(el=>{
    const k=el.dataset.i18nDate,d=el.dataset.dateVal;
    if(UI.en[k]!==undefined)el.innerHTML=tx(k,d);
  });
  document.querySelectorAll("[data-es]").forEach(el=>{
    if(el.dataset.enOrig===undefined)el.dataset.enOrig=el.textContent;
    el.textContent=LANG==="es"?el.dataset.es:el.dataset.enOrig;
  });
  const priTitle=document.getElementById("privIntro");
  if(priTitle)priTitle.innerHTML=tx("privacyIntro",townName,priTitle.dataset.domain);
  const lb=document.getElementById("langBtn");
  if(lb){
    const full=lb.querySelector(".full"),shortEl=lb.querySelector(".short");
    if(full)full.textContent=tx("langBtn");
    if(shortEl)shortEl.textContent=LANG==="es"?"EN":"ES";
    lb.setAttribute("aria-label",LANG==="es"?"Switch to English":"Cambiar a espa\u00f1ol");
  }
}
function reRenderAll(){
  renderHoods();renderDays();renderDay();renderWeek();renderBig();renderClasses();renderTicker();renderResources();applyStaticI18n();
}
const langBtn=document.getElementById("langBtn");
if(langBtn)langBtn.onclick=()=>{LANG=LANG==="es"?"en":"es";try{localStorage.setItem("ctk-lang",LANG)}catch(_){}reRenderAll();if(LANG==="es"&&!window.__ES_LOADED)ensureEs(reRenderAll)};

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

/* ---------- structured data (Event JSON-LD, for search rich results; always English) ---------- */
function injectEventSchema(){
  const items=[];
  E.filter(e=>!e.special).forEach(e=>{
    for(let i=0;i<45;i++){
      const d=addDays(today,i);
      const o=eventsOn(d).find(x=>x.e.t===e.t&&x.e.v===e.v);
      if(o){
        const t=o.times[0];
        items.push({
          "@type":"Event","name":e.t,"startDate":key(d)+(t?"T"+t[0]:""),
          "endDate":(t&&t[1])?key(d)+"T"+t[1]:undefined,
          "eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled",
          "location":V[e.v]?{"@type":"Place","name":V[e.v][0],"address":addrLine(e.v)}:undefined,
          "description":e.blurb||e.t,"isAccessibleForFree":!!e.free,"url":SITE+"#e="+encodeURIComponent(e.id)+"&d="+key(d)
        });
        break;
      }
    }
  });
  E.filter(e=>e.special).forEach(e=>{
    (e.when||[]).forEach(w=>{
      if(w.from>=key(today)){
        const t=w.t&&w.t[0];
        items.push({
          "@type":"Event","name":e.t,"startDate":w.from+(t?"T"+t[0]:""),
          "endDate":(w.to&&w.to!==w.from)?w.to:((t&&t[1])?w.from+"T"+t[1]:undefined),
          "eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled",
          "location":V[e.v]?{"@type":"Place","name":V[e.v][0],"address":addrLine(e.v)}:undefined,
          "description":e.blurb||e.t,"isAccessibleForFree":!!e.free,"url":SITE+"#e="+encodeURIComponent(e.id)+"&d="+w.from
        });
      }
    });
  });
  if(!items.length)return;
  const ld={"@context":"https://schema.org","@graph":items};
  const s=document.createElement('script');s.type='application/ld+json';s.textContent=JSON.stringify(ld);document.head.appendChild(s);
}

/* ---------- initial render ---------- */
renderHoods();renderDays();renderDay();renderWeek();renderBig();renderClasses();renderTicker();renderResources();applyStaticI18n();injectEventSchema();
if(LANG==="es"&&!window.__ES_LOADED)ensureEs(reRenderAll);

/* ---------- links: shared events, days, weekend ---------- */
function handleHash(){
  const h=location.hash.slice(1);
  if(h.startsWith("c=")){const id=h.slice(2);ccat="all";clOpen=true;renderClasses();const el=document.getElementById("cl-"+id);if(el){el.classList.add("flash");setTimeout(()=>el.scrollIntoView({block:"center"}),60);toast(tx("friendClass",BRAND))}return}
  if(h==="weekend"){wkMode=true;renderDays();renderDay();document.getElementById("today").scrollIntoView();toast(tx("friendWeekend",BRAND));return}
  if(!/^(e|d)=/.test(h))return;
  const q=new URLSearchParams(h),k=q.get("d");if(!k||!/^\d{4}-\d{2}-\d{2}$/.test(k))return;
  const d=pd(k),id=q.get("e");
  if(d<today){toast(tx("pastDay"));document.getElementById("today").scrollIntoView();return}
  const diff=Math.round((d-today)/864e5);
  if(!id&&diff<7){sel=diff;wkMode=false;renderDays();renderDay();document.getElementById("today").scrollIntoView();toast(tx("friendDay",BRAND));return}
  forceOpen=k;wk=monday(d);renderWeek();forceOpen=null;
  const tgt=id?document.querySelector(`#weekList .ev[data-k="${CSS.escape(id+"|"+k)}"]`):null;
  if(tgt){tgt.querySelector("details").open=true;tgt.classList.add("flash");setTimeout(()=>tgt.scrollIntoView({block:"center"}),60);const e=EMAP.get(id);toast(e?tx("friendEvent",dx(e.t),BRAND):tx("friendEventGeneric",BRAND))}
  else{document.getElementById("events").scrollIntoView();if(!id)toast(tx("friendDay",BRAND))}
}
handleHash();
window.addEventListener("hashchange",handleHash);
})();
