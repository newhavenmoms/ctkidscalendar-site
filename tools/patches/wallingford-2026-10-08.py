# Full playbook re-run, Oct 8 2026
YM="wallingford-ymca"; CAT="catalyst-art"; ZION="zion-lutheran"; WSO="choate-colony-hall"; PA="postal-annex"; TH="wallingford-town-hall"
TOWN["venues"].update({YM:["Wallingford Family YMCA","81 S Elm St"],CAT:["Catalyst Art Studio","78 Center St"],ZION:["Zion Lutheran Church","235 Pond Hill Rd"],WSO:["Colony Hall, Choate Rosemary Hall","333 Christian St"],PA:["Postal Annex","61 N Plains Industrial Rd"],TH:["Town Hall & Parade Grounds","45 S Main St"]})
TOWN["venueMeta"].update({YM:[None,1],CAT:[None,1],ZION:[None,0],WSO:[None,1],PA:[None,0],TH:[None,0]})
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"]!="Halloween Happenings"]
CS="https://www.catalystartstudio.com/events-1/"; YG="https://wallingfordymca.org/wp-content/uploads/2026/08/2026-Fall1-Web.pdf"; MR="https://wallingfordct.myrec.com/info/activities/program_details.aspx?ProgramID="
TOWN["events"]+=[
 {"t":"School's-Out Art Camps at Catalyst","v":CAT,"when":D(["2026-10-12","2026-11-03","2026-11-11","2026-12-28","2026-12-29","2026-12-30","2026-12-31"],[["09:00","15:00"]]),"ages":"Ages 5–12","a":["big"],"free":False,"price":"$75 a day ($345 for winter-break week)","rsvp":True,"src":CS+"ages-5-12-winter-break-art-camp",
  "blurb":"Full-day art camps on no-school days (Indigenous Peoples' Day, Election Day, Veterans Day and winter break): a main project, smaller activities, games and a lunch break."},
 {"t":"Y-Cation School-Day-Off Camp","v":YM,"when":D(["2026-10-12","2026-11-03","2026-11-11","2026-12-28","2026-12-29","2026-12-30"],[["07:00","18:00"]]),"ages":"Grades K–8","a":["big"],"free":False,"price":"$75 members, $100 community","rsvp":True,"src":YG,
  "blurb":"Full-day care and camp at the Y on school days off."},
 {"t":"Glow Paint Night: Neon Ghost & Pumpkin","v":CAT,"special":"hw","when":[W("2026-10-16",[["18:00","20:00"]])],"ages":"Ages 6+ (drop-off)","a":["big"],"free":False,"price":"$30 per child","rsvp":True,"src":CS+"glow-paint-night-neon-ghost-pumpkin",
  "blurb":"Kids paint a neon ghost and jack-o'-lantern under blacklight; a nut-free snack is included."},
 {"t":"Zion Scarecrow Festival","v":ZION,"special":"fall","when":[W("2026-10-17",[["10:00","15:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free admission (activities extra)","drop":True,"check":True,"src":"https://allevents.in/wallingford/zion-scarecrow-festival/200030750635912",
  "blurb":"A hayride, kids' games, face painting, build-your-own scarecrow, a bounce house, crafters and live music; proceeds go to Fostering Family Hope."},
 {"t":"Halloween BOO-nanza","v":YM,"special":"hw","when":[W("2026-10-17",[["16:30","19:30"]])],"ages":"Grades K–5","a":["big"],"free":False,"price":"$45 members, $55 community","rsvp":True,"check":True,"src":YG,
  "blurb":"A new drop-off Halloween party at the Y; costumes encouraged."},
 {"t":"Halloween Happenings","v":TH,"special":"hw","when":[W("2026-10-23",[["17:30","20:00"]])],"ages":"All ages (under 12 with an adult)","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://www.wallingfordct.gov/events/2026/10/23/halloween-happenings-2026/",
  "blurb":"Gather at 5:45 at the YMCA (81 S Elm St) for the Goblin Parade at 6:10 along S Elm and Center St, then a party 6:30–8 at Town Hall with crafts, music, games and free treats. No dogs or bikes."},
 {"t":"Wallingford Symphony family concerts","v":WSO,"when":[W("2026-10-25",[["14:00","16:00"]]),{"from":"2026-12-20","t":[]}],"ages":"All ages (18 and under free with an adult)","a":["big"],"free":False,"price":"Kids free with a paying adult","rsvp":True,"check":True,"src":"https://www.wallingfordsymphony.org/tickets",
  "blurb":"A Broadway and Hollywood program (Oct 25 at 2) and Cherished Holiday Classics (Dec 20; time not posted yet)."},
 {"t":"Friday Night Out at the Y","v":YM,"when":[W("2026-10-30",[["18:30","20:30"]])],"ages":"Grades K–5","a":["big"],"free":False,"price":"$30 members, $45 community (up to 2 kids)","rsvp":True,"src":YG,
  "blurb":"A drop-off kids' night at the Y; pre-register 24 hours ahead."},
 {"t":"Halloween Family Fun Day","v":PA,"special":"hw","when":[W("2026-10-31",[["10:00","14:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://allevents.in/wallingford/halloween-family-fun-day/200030786031046",
  "blurb":"The 13th annual: costume contest, trick-or-treating, bounce houses and a basket raffle benefiting the Cook Hill School library."},
 {"t":"Holiday Cookie Decorating","v":"wallingford-rec","when":D(["2026-10-13","2026-11-10","2026-12-08"],[["17:00","18:00"]]),"ages":"Kids (ages not listed)","a":["big"],"free":False,"price":"$30","rsvp":True,"check":True,"src":MR+"30232",
  "blurb":"Decorate four themed cookies to take home: Halloween (Oct 13), Thanksgiving (Nov 10) and Christmas (Dec 8)."},
 {"t":"Parent-Child Winter Deer Countdown Board","v":"wallingford-rec","special":"hol","when":[W("2026-12-04",[["18:30","20:45"]])],"ages":"Ages 8+ with a parent","a":["big"],"free":False,"price":"$30 + $20 supplies","rsvp":True,"src":MR+"30065",
  "blurb":"Parent and child each build a wooden reindeer chalkboard countdown to the holidays."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Downtown Holiday Stroll","w":"Center St and downtown","p":"Wallingford Center's stroll with a Santa sighting, a bonfire at the gazebo, food trucks and roasted chestnuts, the first Friday of December (last year Dec 5, 4–9). This year's date isn't posted yet.","src":"https://www.patch.com/connecticut/wallingford/holiday-stroll-2025-wallingford-here-s-what-know"},
 {"g":"hol","t":"Scuba Santa at the Y","w":"Wallingford Family YMCA","p":"Families help Santa decorate an underwater tree, then swim, have cocoa and cookies, do crafts and an indoor 'snowball' fight. A December date isn't posted yet.","src":"https://wallingfordymca.org/family-time/"},
]
TOWN["classes"]+=[{"id":"wal-catalyst","c":"art","n":"Catalyst Art Studio weekly classes","u":"https://www.catalystartstudio.com/weekly-art-class","blurb":"Weekly kids' art classes by age group, plus camps and parties at the downtown studio.","ages":"4–12 years","where":"78 Center St"}]
ADD_PLACES["rain"]+=[("Catalyst Art Studio","A downtown kids' art studio with weekly classes, no-school-day camps and paint nights (78 Center St).","Un estudio de arte infantil en el centro con clases semanales, campamentos en días sin escuela y noches de pintura (78 Center St).")]
ES={
 "Ages 5–12":"5–12 años",
 "$75 a day ($345 for winter-break week)":"$75 por día ($345 la semana de vacaciones de invierno)",
 "Full-day art camps on no-school days (Indigenous Peoples' Day, Election Day, Veterans Day and winter break): a main project, smaller activities, games and a lunch break.":"Campamentos de arte de día completo en días sin escuela (Día de los Pueblos Indígenas, Día de Elecciones, Día de los Veteranos y vacaciones de invierno): un proyecto principal, actividades más pequeñas, juegos y almuerzo.",
 "Grades K–8":"Kínder–8.º grado",
 "$75 members, $100 community":"$75 miembros, $100 comunidad",
 "Full-day care and camp at the Y on school days off.":"Cuidado y campamento de día completo en el YMCA los días sin escuela.",
 "Ages 6+ (drop-off)":"6 años o más (sin papás)",
 "$30 per child":"$30 por niño",
 "Kids paint a neon ghost and jack-o'-lantern under blacklight; a nut-free snack is included.":"Los niños pintan un fantasma y una calabaza de neón bajo luz negra; incluye un bocadillo sin nueces.",
 "Free admission (activities extra)":"Entrada gratis (actividades con costo)",
 "A hayride, kids' games, face painting, build-your-own scarecrow, a bounce house, crafters and live music; proceeds go to Fostering Family Hope.":"Paseo en carreta, juegos infantiles, pintacaritas, arma tu espantapájaros, brincolín, artesanos y música en vivo; lo recaudado es para Fostering Family Hope.",
 "Grades K–5":"Kínder–5.º grado",
 "$45 members, $55 community":"$45 miembros, $55 comunidad",
 "A new drop-off Halloween party at the Y; costumes encouraged.":"Una nueva fiesta de Halloween sin papás en el YMCA; se recomienda ir disfrazado.",
 "All ages (under 12 with an adult)":"Todas las edades (menores de 12 con un adulto)",
 "Gather at 5:45 at the YMCA (81 S Elm St) for the Goblin Parade at 6:10 along S Elm and Center St, then a party 6:30–8 at Town Hall with crafts, music, games and free treats. No dogs or bikes.":"Reúnete a las 5:45 en el YMCA (81 S Elm St) para el Goblin Parade a las 6:10 por S Elm y Center St, y luego una fiesta de 6:30 a 8 en el Ayuntamiento con manualidades, música, juegos y golosinas gratis. Sin perros ni bicicletas.",
 "All ages (18 and under free with an adult)":"Todas las edades (18 años o menos gratis con un adulto)",
 "Kids free with a paying adult":"Niños gratis con un adulto que paga",
 "A Broadway and Hollywood program (Oct 25 at 2) and Cherished Holiday Classics (Dec 20; time not posted yet).":"Un programa de Broadway y Hollywood (25 de oct. a las 2) y Cherished Holiday Classics (20 de dic.; horario aún no publicado).",
 "$30 members, $45 community (up to 2 kids)":"$30 miembros, $45 comunidad (hasta 2 niños)",
 "A drop-off kids' night at the Y; pre-register 24 hours ahead.":"Una noche para niños sin papás en el YMCA; inscríbete con 24 horas de anticipación.",
 "The 13th annual: costume contest, trick-or-treating, bounce houses and a basket raffle benefiting the Cook Hill School library.":"La 13.ª edición: concurso de disfraces, dulces, brincolines y una rifa de canastas a beneficio de la biblioteca de Cook Hill School.",
 "Kids (ages not listed)":"Niños (edades no indicadas)","$30":"$30",
 "Decorate four themed cookies to take home: Halloween (Oct 13), Thanksgiving (Nov 10) and Christmas (Dec 8).":"Decora cuatro galletas temáticas para llevar a casa: Halloween (13 de oct.), Acción de Gracias (10 de nov.) y Navidad (8 de dic.).",
 "Ages 8+ with a parent":"8 años o más con papá o mamá",
 "$30 + $20 supplies":"$30 + $20 de materiales",
 "Parent and child each build a wooden reindeer chalkboard countdown to the holidays.":"Papá o mamá y su hijo construyen cada uno una pizarra de reno de madera con cuenta regresiva para las fiestas.",
 "Center St and downtown":"Center St y el centro",
 "Wallingford Center's stroll with a Santa sighting, a bonfire at the gazebo, food trucks and roasted chestnuts, the first Friday of December (last year Dec 5, 4–9). This year's date isn't posted yet.":"El paseo de Wallingford Center con aparición de Santa, fogata en el quiosco, camiones de comida y castañas asadas, el primer viernes de diciembre (el año pasado el 5 de dic., de 4 a 9). La fecha de este año aún no se ha publicado.",
 "Wallingford Family YMCA":"Wallingford Family YMCA",
 "Families help Santa decorate an underwater tree, then swim, have cocoa and cookies, do crafts and an indoor 'snowball' fight. A December date isn't posted yet.":"Las familias ayudan a Santa a decorar un árbol bajo el agua y luego nadan, toman chocolate con galletas, hacen manualidades y una pelea de 'bolas de nieve' bajo techo. La fecha de diciembre aún no se ha publicado.",
 "Weekly kids' art classes by age group, plus camps and parties at the downtown studio.":"Clases semanales de arte para niños por grupo de edad, además de campamentos y fiestas en el estudio del centro.",
 "4–12 years":"4–12 años",
}
