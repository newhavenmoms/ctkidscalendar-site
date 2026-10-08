# Round 3 finishing pass, Oct 8 2026
CCC="ct-convention-center"; ARENA="peoplesbank-arena"; CO="charter-oak-cc"
TOWN["venues"].update({CCC:["Connecticut Convention Center","100 Columbus Blvd"],ARENA:["PeoplesBank Arena","1 Civic Center Plaza"],CO:["Charter Oak Cultural Center","21 Charter Oak Ave"]})
TOWN["venueMeta"].update({CCC:[None,1],ARENA:[None,1],CO:[None,1]})
CS="https://ctsciencecenter.org/event/"; WA="https://www.thewadsworth.org/event/"
for e in TOWN["events"]:
    if e["t"]=="Festival of Lights at the Wadsworth": e.pop("check",None); e["src"]=WA+"festival-of-lights-2/?instance_id=34552"
    if e["t"]=="Pete the Cat": e["price"]="$14 (box office 860-987-5900); 10am sold out"
TOWN["events"]+=[
 {"t":"Harvest Glow","v":CCC,"special":"fall","when":[W("2026-10-10",[["10:00","19:00"]]),W("2026-10-11",[["10:00","16:00"]])],"ages":"All ages (3 and under free)","a":B+["big"],"free":False,"price":"$10 kids 4–12, $12 adults, plus fee","rsvp":True,"src":"https://hartford.glowgardens.com/",
  "blurb":"The last weekend of an indoor harvest light festival: glowing pumpkin scenes, a corn maze, mini putt and a free train ride. Timed entry."},
 {"t":"Toddler Tuesday at the Science Center","v":"ctsci","when":[W("2026-10-13",[["09:00","13:00"]])],"ages":"Ages 6 and under","a":B,"free":False,"price":"$10 kids, $15 adults","drop":True,"src":CS+"toddler-tuesday-0",
  "blurb":"Special early hours for little ones and their grown-ups."},
 {"t":"Disney Worlds Collide Concert Tour","v":ARENA,"special":"shows","when":[W("2026-11-06",[["19:00","21:30"]])],"ages":"Kids and tweens","a":["big"],"free":False,"price":"See ticket site","rsvp":True,"src":"https://www.peoplesbankarena.com/events/detail/disney-worlds-collide-concert-tour",
  "blurb":"Stars from Descendants, ZOMBIES and Camp Rock in a live concert. Doors at 6."},
 {"t":"Pokémon Day at the Science Center","v":"ctsci","when":[W("2026-11-07",[["10:30","14:30"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Included with admission","drop":True,"src":CS+"pokemon",
  "blurb":"A Pokémon scavenger hunt, card-trading zones, a card-game play lab and special guest Pokémon."},
 {"t":"Science on Screen: WALL-E","v":"ctsci","when":[W("2026-11-07",[["15:00","17:15"]])],"ages":"Families","a":["big"],"free":False,"price":"See Real Art Ways","rsvp":True,"src":CS+"science-screen-wall-e",
  "blurb":"A short talk on robotics by a UConn engineer, then WALL-E."},
 {"t":"New York International Children's Film Festival","v":"wadsworth","when":[W("2026-11-14",[["11:00","16:00"]])],"ages":"Little kids and big kids","a":["preschool","big"],"free":True,"price":"Free admission","drop":True,"src":WA+"film-new-york-international-childrens-film-festival/?instance_id=34521",
  "blurb":"Short-film programs for little kids (11 and 2) and big kids (12 and 3); the earlier two showings are sensory-friendly."},
 {"t":"Holiday Enchantment at the Science Center","v":"ctsci","special":"hol","when":[{"from":"2026-11-14","to":"2026-12-23","t":[]}],"ages":"All ages","a":B+["big"],"free":False,"price":"Included with admission","drop":True,"src":CS+"holiday-enchantment",
  "blurb":"An interactive light floor, a sock-skating rink, winter crafts and holiday science demos, plus Santa 11–3 on most weekends."},
 {"t":"Festival of Trees & Traditions","v":"wadsworth","special":"hol","when":[{"from":"2026-12-03","to":"2026-12-13","t":[]}],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Admission + $5","drop":True,"src":"https://www.thewadsworth.org/events/action~agenda/page_offset~3/request_format~html/",
  "blurb":"The 52nd annual display of decorated trees and wreaths; open Wed–Sun (closed Dec 7–8), 11–5 weekdays and 10–5 weekends."},
 {"t":"Second Saturdays for Families: Winter Wonderland","v":"wadsworth","special":"hol","when":[W("2026-12-12",[["10:00","14:00"]])],"ages":"Families","a":["preschool","big"],"free":True,"price":"Free admission all day","drop":True,"src":WA+"second-saturdays-for-families-winter-wonderland-3/?instance_id=34553",
  "blurb":"Winter celebrations from around the world, with the Japan Society of Greater Hartford and the Mandell JCC."},
]
TOWN["tba"]+=[{"g":"hol","t":"Glow Hartford (holiday edition)","w":"Connecticut Convention Center, 100 Columbus Blvd","p":"A holiday light festival at the Convention Center; last year it ran Nov 21–Dec 23. This year's dates aren't posted yet.","src":"https://www.wfsb.com/2025/11/13/heres-list-connecticut-holiday-festivals-events-2025/"}]
TOWN["classes"]+=[{"id":"charter-oak-city-school","c":"art","n":"City School of the Arts (Charter Oak Cultural Center)","u":"https://charteroakcenter.org/school-of-arts/classes/","blurb":"Free after-school classes in piano, violin, ballet, hip hop, step, martial arts, crafts, singing and cooking; fall showcases the week of Dec 7. Waitlist.","ages":"6–18 years","where":"21 Charter Oak Ave"}]
ADD_PLACES["drive"]+=[("Hartt Community Division, First Steps in Music","Early-childhood music classes at the University of Hartford (200 Bloomfield Ave, West Hartford).","Clases de música para la primera infancia en la University of Hartford (200 Bloomfield Ave, West Hartford).")]
ES_PATCH={
 "$14 (box office 860-987-5900); 10am sold out":"$14 (taquilla 860-987-5900); la función de las 10 está agotada",
 "All ages (3 and under free)":"Todas las edades (3 años o menos gratis)",
 "$10 kids 4–12, $12 adults, plus fee":"$10 niños de 4–12, $12 adultos, más cargo",
 "The last weekend of an indoor harvest light festival: glowing pumpkin scenes, a corn maze, mini putt and a free train ride. Timed entry.":"El último fin de semana de un festival de luces de cosecha bajo techo: escenas de calabazas iluminadas, laberinto de maíz, minigolf y paseo en tren gratis. Entrada con horario.",
 "Ages 6 and under":"6 años o menos","$10 kids, $15 adults":"$10 niños, $15 adultos",
 "Special early hours for little ones and their grown-ups.":"Horario especial temprano para los pequeños y sus adultos.",
 "Kids and tweens":"Niños y preadolescentes","See ticket site":"Ver el sitio de boletos",
 "Stars from Descendants, ZOMBIES and Camp Rock in a live concert. Doors at 6.":"Estrellas de Descendants, ZOMBIES y Camp Rock en concierto. Puertas a las 6.",
 "Included with admission":"Incluido con la entrada",
 "A Pokémon scavenger hunt, card-trading zones, a card-game play lab and special guest Pokémon.":"Una búsqueda del tesoro de Pokémon, zonas de intercambio de cartas, un laboratorio de juego de cartas y Pokémon invitados.",
 "Families":"Familias","See Real Art Ways":"Consulta Real Art Ways",
 "A short talk on robotics by a UConn engineer, then WALL-E.":"Una charla corta sobre robótica de un ingeniero de UConn y luego WALL-E.",
 "Little kids and big kids":"Niños pequeños y mayores","Free admission":"Entrada gratis",
 "Short-film programs for little kids (11 and 2) and big kids (12 and 3); the earlier two showings are sensory-friendly.":"Programas de cortometrajes para niños pequeños (11 y 2) y mayores (12 y 3); las dos primeras funciones están adaptadas sensorialmente.",
 "An interactive light floor, a sock-skating rink, winter crafts and holiday science demos, plus Santa 11–3 on most weekends.":"Un piso de luces interactivo, una pista para patinar en calcetines, manualidades de invierno y demostraciones de ciencia navideña, además de Santa de 11 a 3 casi todos los fines de semana.",
 "Admission + $5":"Entrada + $5",
 "The 52nd annual display of decorated trees and wreaths; open Wed–Sun (closed Dec 7–8), 11–5 weekdays and 10–5 weekends.":"La 52.ª exhibición anual de árboles y coronas decorados; abre de miércoles a domingo (cerrado el 7 y 8 de dic.), de 11 a 5 entre semana y de 10 a 5 los fines de semana.",
 "Free admission all day":"Entrada gratis todo el día",
 "Winter celebrations from around the world, with the Japan Society of Greater Hartford and the Mandell JCC.":"Celebraciones de invierno de todo el mundo, con la Japan Society of Greater Hartford y el Mandell JCC.",
 "Connecticut Convention Center, 100 Columbus Blvd":"Connecticut Convention Center, 100 Columbus Blvd",
 "A holiday light festival at the Convention Center; last year it ran Nov 21–Dec 23. This year's dates aren't posted yet.":"Un festival de luces navideñas en el Convention Center; el año pasado fue del 21 de nov. al 23 de dic. Las fechas de este año aún no se han publicado.",
 "Free after-school classes in piano, violin, ballet, hip hop, step, martial arts, crafts, singing and cooking; fall showcases the week of Dec 7. Waitlist.":"Clases gratis después de la escuela de piano, violín, ballet, hip hop, step, artes marciales, manualidades, canto y cocina; presentaciones de otoño la semana del 7 de dic. Lista de espera.",
 "6–18 years":"6–18 años",
}
