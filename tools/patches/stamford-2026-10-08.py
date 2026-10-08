# Full playbook re-run, Oct 8 2026
JCC="stamford-jcc"; CH="chabad-of-stamford"; STC="stamford-town-center"; REC="stamford-recreation-recreation-star-cent"; PAL="palace-theatre"
LP="latham-park"; COVE="cove-island-pavilion"; HP="harbor-point-square"
TOWN["venues"].update({LP:["Latham Park","Bedford St"],COVE:["Cove Island Park Pavilion","1125 Cove Rd"],HP:["Harbor Point Square","20 Harbor Point Rd"]})
TOWN["venueMeta"].update({LP:[None,0],COVE:[None,0],HP:[None,0]})
TOWN["events"]=[e for e in TOWN["events"] if e["t"]!="Saturday Matinee at Stamford Town Center (Avon on Tour)"]
for e in TOWN["events"]:
    if e["t"]=="Magical Friday Night Halloween Event": e["price"]="$20 per child; pre-register (limit 100)"
TOWN["tba"]=[x for x in TOWN["tba"] if not x["t"].startswith("Heights & Lights")]
J="https://www.stamfordjcc.org/events/2026/"; AV="https://avontheatre.org/movies/avon-on-tour-"; RB="https://www.stamfordrecreation.com/_files/ugd/4367dc_71342bedd5da4161926dc0eba8568d8e.pdf"
TOWN["events"]+=[
 {"t":"Babies, Blocks & Bagels","v":JCC,"when":D(["2026-10-18","2026-11-01"],[["09:30","11:00"]]),"ages":"Birth–3 + caregiver (siblings to 6)","a":["baby","toddler"],"free":False,"price":"Free for members, $25 per family for community","rsvp":True,"src":J+"10/18/early-learning/babies-blocks-bagels/",
  "blurb":"An open-play morning with snacks at the JCC, open to all families."},
 {"t":"Kids' Night Out at the JCC","v":JCC,"when":D(["2026-10-24","2026-11-14","2026-12-12"],[["17:30","21:00"]]),"ages":"Grades K–5","a":["big"],"free":False,"price":"$25 first child, $20 each additional (JCC members only)","rsvp":True,"src":J+"10/24/youth-family/kids-night-out/",
  "blurb":"A members-only drop-off evening with rotating themed activities."},
 {"t":"Tot Shabbat at the JCC","v":JCC,"when":D(["2026-11-13","2026-12-11"],[["17:30","19:00"]]),"ages":"Families with young children","a":["toddler","preschool"],"free":False,"price":"See JCC","rsvp":True,"check":True,"src":J+"11/13/special-events/tot-shabbat-with-rabbi-josh-strom/",
  "blurb":"Songs, blessings, a kosher-style dinner and an art project; Dec 11 is a Chanukah edition with Ori Zaff."},
 {"t":"Halloween Candy Crawl","v":STC,"special":"hw","when":[W("2026-10-25",[["11:00","14:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://stamfordmoms.com/join-us-for-the-stamford-moms-candy-crawl-at-stamford-town-center/",
  "blurb":"Stamford Moms' 5th annual mall trick-or-treat at stores with orange balloons, plus characters, face painting and crafts on Level 4."},
 {"t":"Mighty Makers Saturday Workshops","v":REC,"when":[W("2026-10-24",[["09:00","12:00"]]),W("2026-11-14",[["09:00","12:00"]]),W("2026-12-19",[["09:00","12:00"]])],"ages":"Grades K–4","a":["big"],"free":False,"price":"$50","rsvp":True,"src":RB,
  "blurb":"Saturday-morning workshops at the Star Center: Spooktacular Science (Oct 24), Art Explosion (Nov 14) and a Holiday Make & Take with cookies (Dec 19)."},
 {"t":"Free Holiday Movies (Avon on Tour)","v":STC,"special":"hol","when":[W("2026-11-07",[["13:30","16:00"]]),W("2026-12-04",[["17:30","19:30"]]),W("2026-12-11",[["17:30","19:30"]]),W("2026-12-18",[["17:30","19:30"]])],"ages":"All ages (G/PG)","a":["preschool","big"],"free":True,"price":"Free, first come","drop":True,"src":AV+"the-muppet-christmas-carol/",
  "blurb":"The Avon Theatre's free screenings at Stamford Town Center: The Muppet Christmas Carol (Sat Nov 7, activities 1:30, film 2), then Friday nights The Polar Express (Dec 4), The Grinch (Dec 11) and Elf (Dec 18)."},
 {"t":"Friday Night Kids Club","v":REC,"when":[W("2026-11-13",[["18:00","21:00"]])],"ages":"Grades K–5","a":["big"],"free":False,"price":"$25","rsvp":True,"src":RB,
  "blurb":"A parents' night out at the Star Center with a snack and drink; limit 40."},
 {"t":"Harbor Point Turkey Trot Fun Run","v":HP,"when":[W("2026-11-26",[["08:00","09:30"]])],"ages":"All ages (under 18 with a parent)","a":["preschool","big"],"free":True,"price":"Free (optional raffle)","rsvp":True,"src":"https://www.eventbrite.com/e/15th-annual-harbor-point-5k-turkey-trot-fun-run-tickets-1999388908046",
  "blurb":"An untimed Thanksgiving-morning family 5K; RSVP and waiver online, walk-ups welcome."},
 {"t":"Santa Hay Ride","v":COVE,"special":"hol","when":D(["2026-12-05","2026-12-12"],[["10:00","13:00"],["14:00","16:00"]]),"ages":"All ages (Stamford residents)","a":B+["big"],"free":False,"price":"$8 per rider","rsvp":True,"src":RB,
  "blurb":"The 26th annual hay ride with Santa, who sings and gives each child a treat. Tickets online from Nov 2; no day-of sales."},
 {"t":"Chanukah Festival & Giant Menorah Lighting","v":LP,"special":"hol","when":[W("2026-12-06",[["16:00","17:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","rsvp":True,"src":"https://www.stamfordchabad.org/civicrm/event/info?id=699&reset=1",
  "blurb":"Chabad of Stamford lights 'Fairfield County's largest menorah' with music, latkes, hot cider and chocolate gelt for kids. Register online."},
 {"t":"Heights & Lights","v":"stamford-downtown-bedford-street","special":"hol","when":[W("2026-12-06",[["17:00","19:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://stamford-downtown.com/event/heights-lights/",
  "blurb":"Santa, Rudolph and the Grinch rappel 22 stories down Landmark Square, then fireworks and a procession up Bedford St to the city tree lighting at Latham Park. Time not posted yet (5pm in past years)."},
 {"t":"Menorah Car Parade","v":LP,"special":"hol","when":[W("2026-12-12",[["18:00","19:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://www.stamfordchabad.org/civicrm/event/info?id=701&reset=1",
  "blurb":"Cars topped with menorahs parade from Chabad (770 High Ridge Rd) through Stamford to a giant menorah lighting at Latham Park."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Holiday Wish Express","w":"Stamford Town Center, Level 5","p":"An immersive North Pole walk-through from mid/late November to Dec 24 (it opened Nov 22 last year). Tickets go on sale Oct 13.","src":"https://theholidaywish.com/"},
 {"g":"hol","t":"Shippan Turkey Trot","w":"280 Ocean Dr East, Shippan","p":"A free 4K on Thanksgiving morning at 10 (bring canned food or a donation for Pacific House); costumes encouraged.","src":"https://www.shippantrot.com"},
]
TOWN["classes"]+=[{"id":"stam-hudson-table","c":"art","n":"Hudson Table kids' cooking","u":"https://hudsontable.com/stamford/kids-classes/","blurb":"Hands-on cooking classes and series, from Mommy & Me for ages 2–4 to drop-off classes and an after-school 'Around the World' series for ages 8–14.","ages":"2–14 years","where":"Stamford"}]
ES={
 "Birth–3 + caregiver (siblings to 6)":"0–3 años + un adulto (hermanos hasta 6)",
 "Free for members, $25 per family for community":"Gratis para miembros, $25 por familia para la comunidad",
 "An open-play morning with snacks at the JCC, open to all families.":"Una mañana de juego libre con bocadillos en el JCC, abierta a todas las familias.",
 "Grades K–5":"Kínder–5.º grado",
 "$25 first child, $20 each additional (JCC members only)":"$25 el primer niño, $20 cada uno adicional (solo miembros del JCC)",
 "A members-only drop-off evening with rotating themed activities.":"Una noche sin papás solo para miembros, con actividades temáticas que cambian.",
 "Families with young children":"Familias con niños pequeños","See JCC":"Consulta con el JCC",
 "Songs, blessings, a kosher-style dinner and an art project; Dec 11 is a Chanukah edition with Ori Zaff.":"Canciones, bendiciones, una cena de estilo kosher y un proyecto de arte; el 11 de dic. es una edición de Janucá con Ori Zaff.",
 "Stamford Moms' 5th annual mall trick-or-treat at stores with orange balloons, plus characters, face painting and crafts on Level 4.":"La 5.ª edición del recorrido de dulces de Stamford Moms en las tiendas con globos naranjas del centro comercial, además de personajes, pintacaritas y manualidades en el nivel 4.",
 "$50":"$50",
 "Saturday-morning workshops at the Star Center: Spooktacular Science (Oct 24), Art Explosion (Nov 14) and a Holiday Make & Take with cookies (Dec 19).":"Talleres los sábados por la mañana en el Star Center: Spooktacular Science (24 de oct.), Art Explosion (14 de nov.) y Holiday Make & Take con galletas (19 de dic.).",
 "All ages (G/PG)":"Todas las edades (G/PG)","Free, first come":"Gratis, por orden de llegada",
 "The Avon Theatre's free screenings at Stamford Town Center: The Muppet Christmas Carol (Sat Nov 7, activities 1:30, film 2), then Friday nights The Polar Express (Dec 4), The Grinch (Dec 11) and Elf (Dec 18).":"Funciones gratis del Avon Theatre en Stamford Town Center: The Muppet Christmas Carol (sábado 7 de nov., actividades 1:30, película 2) y luego los viernes por la noche The Polar Express (4 de dic.), The Grinch (11 de dic.) y Elf (18 de dic.).",
 "$25":"$25",
 "A parents' night out at the Star Center with a snack and drink; limit 40.":"Una noche libre para papás en el Star Center con bocadillo y bebida; máximo 40.",
 "All ages (under 18 with a parent)":"Todas las edades (menores de 18 con papá o mamá)",
 "Free (optional raffle)":"Gratis (rifa opcional)",
 "An untimed Thanksgiving-morning family 5K; RSVP and waiver online, walk-ups welcome.":"Unos 5 km familiares sin cronometrar la mañana de Acción de Gracias; confirma y firma el permiso en línea, también se aceptan participantes sin registro.",
 "All ages (Stamford residents)":"Todas las edades (residentes de Stamford)","$8 per rider":"$8 por persona",
 "The 26th annual hay ride with Santa, who sings and gives each child a treat. Tickets online from Nov 2; no day-of sales.":"El 26.º paseo anual en carreta con Santa, que canta y le da una golosina a cada niño. Boletos en línea desde el 2 de nov.; no se venden el mismo día.",
 "Chabad of Stamford lights 'Fairfield County's largest menorah' with music, latkes, hot cider and chocolate gelt for kids. Register online.":"Chabad of Stamford enciende 'la menorá más grande del condado de Fairfield' con música, latkes, sidra caliente y monedas de chocolate para los niños. Inscríbete en línea.",
 "Santa, Rudolph and the Grinch rappel 22 stories down Landmark Square, then fireworks and a procession up Bedford St to the city tree lighting at Latham Park. Time not posted yet (5pm in past years).":"Santa, Rudolph y el Grinch descienden 22 pisos en rapel por Landmark Square, y luego hay fuegos artificiales y un desfile por Bedford St hasta el encendido del árbol en Latham Park. Horario aún no publicado (a las 5 p. m. en años anteriores).",
 "Cars topped with menorahs parade from Chabad (770 High Ridge Rd) through Stamford to a giant menorah lighting at Latham Park.":"Autos con menorás desfilan desde Chabad (770 High Ridge Rd) por Stamford hasta el encendido de una menorá gigante en Latham Park.",
 "Stamford Town Center, Level 5":"Stamford Town Center, nivel 5",
 "An immersive North Pole walk-through from mid/late November to Dec 24 (it opened Nov 22 last year). Tickets go on sale Oct 13.":"Un recorrido inmersivo por el Polo Norte desde mediados o finales de noviembre hasta el 24 de dic. (el año pasado abrió el 22 de nov.). Los boletos salen a la venta el 13 de oct.",
 "280 Ocean Dr East, Shippan":"280 Ocean Dr East, Shippan",
 "A free 4K on Thanksgiving morning at 10 (bring canned food or a donation for Pacific House); costumes encouraged.":"Una carrera gratis de 4 km la mañana de Acción de Gracias a las 10 (trae alimentos enlatados o un donativo para Pacific House); se recomiendan disfraces.",
 "Hands-on cooking classes and series, from Mommy & Me for ages 2–4 to drop-off classes and an after-school 'Around the World' series for ages 8–14.":"Clases y series de cocina práctica, desde Mommy & Me para 2–4 años hasta clases sin papás y una serie después de clases 'Around the World' para 8–14 años.",
 "2–14 years":"2–14 años",
}
