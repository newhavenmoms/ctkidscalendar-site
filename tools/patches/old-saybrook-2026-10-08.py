# Full playbook re-run, Oct 8 2026
MR="https://oldsaybrookct.myrec.com/info/activities/program_details.aspx?ProgramID="
KATE="the-kate"; EST="the-estuary"; PRES="the-preserve"; SPR="saybrook-point-resort"; NL="https://actonlibrary.org/wp-content/uploads/2026-NovDec.pdf"; NL1="https://actonlibrary.org/wp-content/uploads/2026-SeptOct.pdf"
TOWN["venues"].update({KATE:["The Kate","300 Main St"],EST:["The Estuary","220 Main St"],PRES:["The Preserve (Ingham Hill Rd lot)","Lot across from 231 Ingham Hill Rd"],SPR:["Saybrook Point Resort & Marina","2 Bridge St"]})
TOWN["venueMeta"].update({KATE:[None,1],EST:[None,1],PRES:[None,0],SPR:[None,1]})
# corrections
for e in TOWN["events"]:
    if e["t"]=="Imaginary Tails with Izzy": e["when"]=[w for w in e["when"] if w["from"]!="2026-12-15"]
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"] not in ("Halloween Trunk or Treat at the Rec","Parks & Rec Fall Fun Series")]
TOWN["events"]+=[
 {"t":"Halloween Trunk or Treat at the Rec","v":"os-rec","special":"hw","when":[W("2026-10-16",[["18:00","20:00"]])],"ages":"Newborn–4th grade","a":B+["big"],"free":True,"price":"Free","drop":True,"src":MR+"11980",
  "blurb":"Decorated trunks, a DJ, games and refreshments behind Town Hall. Families just show up; rain date Sat Oct 17."},
 {"t":"Nature Talk: Bats of Connecticut","v":EST,"when":[W("2026-10-13",[["16:00","17:00"]])],"ages":"All ages","a":["big"],"free":False,"price":"$5 residents, $10 non-residents","rsvp":True,"src":MR+"29823",
  "blurb":"A DEEP Master Wildlife Conservationist's slideshow on Connecticut's bats, with time for questions."},
 {"t":"Nature Talk: Eastern Coyotes","v":EST,"when":[W("2026-11-10",[["16:00","17:00"]])],"ages":"All ages","a":["big"],"free":False,"price":"$5 residents, $10 non-residents","rsvp":True,"src":MR+"29823",
  "blurb":"A slideshow and Q&A about the coyotes that live around Old Saybrook."},
 {"t":"Acoustic Artists Storyteller Series","v":"acton-library","when":D(["2026-10-14","2026-11-18","2026-12-16"],[["18:00","19:00"]]),"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","rsvp":True,"check":True,"src":NL,
  "blurb":"Stories and songs with visuals: Mark Binder (Oct 14), Ramblin' Dan Stevens (Nov 18) and John Calcagni (Dec 16). Registration suggested; end time is an estimate."},
 {"t":"Ballet Spooktacular","v":KATE,"special":"hw","when":D(["2026-10-24","2026-10-25"],[["11:30","12:05"],["13:30","14:05"],["15:30","16:05"]]),"ages":"Ages 4–12","a":["preschool","big"],"free":False,"price":"See box office (860-510-0453)","rsvp":True,"src":"https://www.thekate.org/event/ballet-spooktacular/",
  "blurb":"Eastern Connecticut Ballet's 35-minute Halloween ballet, with characters that are 'fascinating, not frightening,' plus treats."},
 {"t":"Cinderella (Panto Company USA)","v":KATE,"special":"shows","when":[W("2026-11-07",[["13:00","14:00"]])],"ages":"Ages 4–10","a":["preschool","big"],"free":False,"price":"See box office (860-510-0453)","rsvp":True,"src":"https://www.thekate.org/event/cinderella/",
  "blurb":"An hour-long family panto with comedy, audience participation and original songs."},
 {"t":"Walk & Run at The Preserve","v":PRES,"when":[W("2026-11-14",[["09:00","11:30"]])],"ages":"All ages","a":["big"],"free":True,"price":"Free","rsvp":True,"check":True,"src":MR+"29745",
  "blurb":"Walk or run The Preserve's trails at your own pace, with water stops and trail maps. Co-sponsored by Marathon Sports; register ahead."},
 {"t":"Brunch with Santa","v":SPR,"special":"hol","when":[{"from":"2026-11-29","t":[]},{"from":"2026-12-06","t":[]},{"from":"2026-12-13","t":[]}],"ages":"All ages","a":B+["big"],"free":False,"price":"Price not posted yet","rsvp":True,"check":True,"src":"https://www.saybrook.com/dine/special-events/",
  "blurb":"A family brunch with Santa at Saybrook Point on three December Sundays. Times and prices are 'to come'; reservations required."},
 {"t":"Saybrook Starlight Festival","v":"os-main","special":"hol","when":[W("2026-12-05",[["13:00","16:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Mostly free","drop":True,"check":True,"src":"https://www.sayoldsaybrook.com/saybrook-starlight-festival",
  "blurb":"Main Street's holiday afternoon: family fun on the Green, Santa at the gazebo, horse-drawn wagon rides, crafts, a library scavenger hunt, face painting and carolers. Times are from last year's schedule."},
 {"t":"Ornament Decorating","v":"os-rec","special":"hol","when":[W("2026-12-05",[["12:00","12:45"]])],"ages":"Ages 3–12","a":["preschool","big"],"free":False,"price":"$15 residents, $25 non-residents","rsvp":True,"src":MR+"12177",
  "blurb":"Make a keepsake tree ornament during the Starlight Festival."},
 {"t":"Frosty (The Barter Players)","v":KATE,"special":"hol","when":[W("2026-12-06",[["11:00","11:50"],["13:30","14:20"]])],"ages":"Ages 5–11","a":["preschool","big"],"free":False,"price":"See box office (860-510-0453)","rsvp":True,"src":"https://www.thekate.org/event/frosty/",
  "blurb":"A 50-minute Christmas play: a magic hat brings a snowman to life."},
 {"t":"A Letter from Santa","v":"os-rec","special":"hol","when":[{"from":"2026-11-02","to":"2026-12-11","t":[]}],"ages":"Ages 1–12","a":B+["big"],"free":False,"price":"$2 residents, $4 non-residents","rsvp":True,"src":MR+"12003",
  "blurb":"Sign your child up by Dec 11 and Santa mails them a personal letter."},
 {"t":"Holiday Cookie Decorating","v":"os-rec","special":"hol","when":[W("2026-12-12",[["11:00","11:45"],["12:00","12:45"]])],"ages":"Ages 3–12","a":["preschool","big"],"free":False,"price":"$15 residents, $25 non-residents","rsvp":True,"src":MR+"12176",
  "blurb":"Decorate holiday cookies (donated by Pursuit of Pastry) at the Rec, the same morning as the Torchlight Parade."},
 {"t":"Winter Solstice Walk","v":PRES,"special":"hol","when":[W("2026-12-21",[["14:15","16:30"]])],"ages":"Kids over 8 + adults","a":["big"],"free":True,"price":"Free","rsvp":True,"src":MR+"29745",
  "blurb":"A loop through The Preserve ending at the Pequot bog overlook for the solstice sunset. Rain or snow cancels; no dogs."},
 {"t":"Holiday Break Vacation Camp","v":"os-rec","when":D(["2026-12-28","2026-12-29","2026-12-30","2026-12-31"],[["09:00","16:00"]]),"ages":"Grades K–5","a":["big"],"free":False,"price":"$140 residents, $165 non-residents","rsvp":True,"src":MR+"29669",
  "blurb":"Four days of dodgeball, kickball, crafts and games at the Teen Center over winter break."},
 {"t":"Grab & Go Crafts","v":"acton-library","when":[{"from":d,"t":[]} for d in ["2026-10-09","2026-10-16","2026-10-23","2026-10-30","2026-11-06","2026-11-13","2026-11-20","2026-12-04","2026-12-11","2026-12-18"]],"ages":"Kids","a":["preschool","big"],"free":True,"price":"Free","drop":True,"src":NL1,
  "blurb":"A new take-home craft kit in the Children's Room every Friday, while supplies last."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Menorah Lighting on the Town Green","w":"Town Green gazebo, 302 Main St","p":"Chabad of the Shoreline lights a menorah on the Green during Hanukkah, with music and holiday treats. Last year it was Dec 15 at 6pm. This year's date isn't posted yet (Hanukkah is Dec 4–12).","src":"https://www.jewishshoreline.org/Light"},
 {"g":"hol","t":"Hero Tree Lighting","w":"The Kate, 300 Main St","p":"A short tree lighting honoring veterans and service members, the Friday evening before the Starlight Festival. Last year it was Dec 5 at 5:30. This year's date isn't posted yet.","src":"https://www.sayoldsaybrook.com/saybrook-starlight-festival"},
 {"g":"hol","t":"Chamber Elf Hunt","w":"Shops around Old Saybrook","p":"Kids hunt for elves hidden in local shops with a passport, for a prize drawing; the week after Starlight. Last year it ran Dec 7–13. This year's dates aren't posted yet.","src":"https://goschamber.com/december-holiday-events/"},
]
for c in TOWN["classes"]:
    if c["id"]=="ospr-martial-arts": c["blurb"]="Martial arts at New England Rendokan (Walmart Plaza), Nov 2–Dec 16: ages 3–4, 5–7 and 8–12 groups plus a family class. $25 residents, $35 non-residents."
    if c["id"]=="ospr-junior-tennis": c["blurb"]="Thursday lessons at Old Saybrook Swim & Racquet Club, Oct 22–Nov 19: Red Ball (ages 4–7) 4–5pm and Orange Ball (ages 7–10) 5–6pm."
TOWN["classes"]+=[
 {"id":"ospr-nocturnal","c":"nature","n":"Nocturnal Animals (Parks & Rec)","u":MR+"29888","blurb":"Saturday-morning nature class about owls, bats and other night animals, from late October into November. $30 residents.","ages":"3–5 years","where":"308 Main St"},
 {"id":"ospr-little-sports","c":"move","n":"Sports R' Fun and Basketball Skill Builder","u":MR+"29885","blurb":"Saturday sports for little ones: Sports R' Fun for ages 2–4 (Oct 31–Nov 28, $40) and Basketball Skill Builder for grades 1–3 (Nov 14–Dec 12, $25).","ages":"2 years–grade 3","where":"308 Main St"},
 {"id":"ospr-afterschool","c":"art","n":"After-school classes at Goodwin School","u":MR+"12218","blurb":"Zumba Kids (grades 3–4, Mondays from Oct 26) and Creative Craft Corner (grades 5–8, select Wednesdays Nov 4–Dec 16), $25 residents.","ages":"Grades 3–8","where":"Goodwin School"},
]
ADD_PLACES["out"]+=[("The Preserve State Forest","1,000 acres of woods, ponds and trails on the Westbrook and Essex line; free (trailhead lot across from 231 Ingham Hill Rd).","Más de 400 hectáreas de bosque, estanques y senderos en el límite con Westbrook y Essex; gratis (estacionamiento frente al 231 de Ingham Hill Rd)."),
                    ("Kavanagh Park","A town park with a playground and a summer splash pad.","Un parque del pueblo con área de juegos y una zona de chorros en verano.")]
ES={
 "Newborn–4th grade":"Recién nacidos–4.º grado",
 "Decorated trunks, a DJ, games and refreshments behind Town Hall. Families just show up; rain date Sat Oct 17.":"Cajuelas decoradas, DJ, juegos y refrigerios detrás del Ayuntamiento. Las familias solo llegan; fecha en caso de lluvia: sábado 17 de oct.",
 "$5 residents, $10 non-residents":"$5 residentes, $10 no residentes",
 "A DEEP Master Wildlife Conservationist's slideshow on Connecticut's bats, with time for questions.":"Una presentación de un conservacionista de vida silvestre del DEEP sobre los murciélagos de Connecticut, con tiempo para preguntas.",
 "A slideshow and Q&A about the coyotes that live around Old Saybrook.":"Una presentación con preguntas y respuestas sobre los coyotes que viven en Old Saybrook.",
 "Stories and songs with visuals: Mark Binder (Oct 14), Ramblin' Dan Stevens (Nov 18) and John Calcagni (Dec 16). Registration suggested; end time is an estimate.":"Cuentos y canciones con imágenes: Mark Binder (14 de oct.), Ramblin' Dan Stevens (18 de nov.) y John Calcagni (16 de dic.). Se sugiere inscribirse; la hora de término es aproximada.",
 "Ages 4–12":"4–12 años",
 "See box office (860-510-0453)":"Consulta la taquilla (860-510-0453)",
 "Eastern Connecticut Ballet's 35-minute Halloween ballet, with characters that are 'fascinating, not frightening,' plus treats.":"El ballet de Halloween de 35 minutos de Eastern Connecticut Ballet, con personajes 'fascinantes, no aterradores', y dulces.",
 "Ages 4–10":"4–10 años",
 "An hour-long family panto with comedy, audience participation and original songs.":"Una pantomima familiar de una hora con comedia, participación del público y canciones originales.",
 "Walk or run The Preserve's trails at your own pace, with water stops and trail maps. Co-sponsored by Marathon Sports; register ahead.":"Camina o corre por los senderos de The Preserve a tu ritmo, con puestos de agua y mapas. Copatrocinado por Marathon Sports; inscríbete con anticipación.",
 "Price not posted yet":"Precio aún no publicado",
 "A family brunch with Santa at Saybrook Point on three December Sundays. Times and prices are 'to come'; reservations required.":"Un brunch familiar con Santa en Saybrook Point tres domingos de diciembre. Horarios y precios por anunciar; se requiere reservación.",
 "Mostly free":"Casi todo gratis",
 "Main Street's holiday afternoon: family fun on the Green, Santa at the gazebo, horse-drawn wagon rides, crafts, a library scavenger hunt, face painting and carolers. Times are from last year's schedule.":"La tarde navideña de Main Street: diversión familiar en el Green, Santa en el quiosco, paseos en carreta tirada por caballos, manualidades, una búsqueda del tesoro de la biblioteca, pintacaritas y villancicos. El horario es del año pasado.",
 "Ages 3–12":"3–12 años",
 "$15 residents, $25 non-residents":"$15 residentes, $25 no residentes",
 "Make a keepsake tree ornament during the Starlight Festival.":"Haz un adorno navideño de recuerdo durante el Starlight Festival.",
 "Ages 5–11":"5–11 años",
 "A 50-minute Christmas play: a magic hat brings a snowman to life.":"Una obra navideña de 50 minutos: un sombrero mágico le da vida a un muñeco de nieve.",
 "Ages 1–12":"1–12 años",
 "$2 residents, $4 non-residents":"$2 residentes, $4 no residentes",
 "Sign your child up by Dec 11 and Santa mails them a personal letter.":"Inscribe a tu hijo antes del 11 de dic. y Santa le enviará una carta personal por correo.",
 "Decorate holiday cookies (donated by Pursuit of Pastry) at the Rec, the same morning as the Torchlight Parade.":"Decora galletas navideñas (donadas por Pursuit of Pastry) en el centro de recreación, la misma mañana del Torchlight Parade.",
 "Kids over 8 + adults":"Niños mayores de 8 + adultos",
 "A loop through The Preserve ending at the Pequot bog overlook for the solstice sunset. Rain or snow cancels; no dogs.":"Un recorrido por The Preserve que termina en el mirador del pantano Pequot para ver la puesta de sol del solsticio. Se cancela con lluvia o nieve; sin perros.",
 "Grades K–5":"Kínder–5.º grado",
 "$140 residents, $165 non-residents":"$140 residentes, $165 no residentes",
 "Four days of dodgeball, kickball, crafts and games at the Teen Center over winter break.":"Cuatro días de quemados, kickball, manualidades y juegos en el Teen Center durante las vacaciones de invierno.",
 "Kids":"Niños",
 "A new take-home craft kit in the Children's Room every Friday, while supplies last.":"Un nuevo kit de manualidades para llevar a casa en la sala infantil cada viernes, hasta agotar existencias.",
 "Town Green gazebo, 302 Main St":"Quiosco del Town Green, 302 Main St",
 "Chabad of the Shoreline lights a menorah on the Green during Hanukkah, with music and holiday treats. Last year it was Dec 15 at 6pm. This year's date isn't posted yet (Hanukkah is Dec 4–12).":"Chabad of the Shoreline enciende una menorá en el Green durante Janucá, con música y golosinas. El año pasado fue el 15 de dic. a las 6 p. m. La fecha de este año aún no se ha publicado (Janucá es del 4 al 12 de dic.).",
 "The Kate, 300 Main St":"The Kate, 300 Main St",
 "A short tree lighting honoring veterans and service members, the Friday evening before the Starlight Festival. Last year it was Dec 5 at 5:30. This year's date isn't posted yet.":"Un breve encendido del árbol en honor a veteranos y miembros del servicio, el viernes por la tarde antes del Starlight Festival. El año pasado fue el 5 de dic. a las 5:30. La fecha de este año aún no se ha publicado.",
 "Shops around Old Saybrook":"Tiendas de Old Saybrook",
 "Kids hunt for elves hidden in local shops with a passport, for a prize drawing; the week after Starlight. Last year it ran Dec 7–13. This year's dates aren't posted yet.":"Los niños buscan duendes escondidos en tiendas locales con un pasaporte para participar en un sorteo; la semana después de Starlight. El año pasado fue del 7 al 13 de dic. Las fechas de este año aún no se han publicado.",
 "Martial arts at New England Rendokan (Walmart Plaza), Nov 2–Dec 16: ages 3–4, 5–7 and 8–12 groups plus a family class. $25 residents, $35 non-residents.":"Artes marciales en New England Rendokan (Walmart Plaza), del 2 de nov. al 16 de dic.: grupos de 3–4, 5–7 y 8–12 años, además de una clase familiar. $25 residentes, $35 no residentes.",
 "Thursday lessons at Old Saybrook Swim & Racquet Club, Oct 22–Nov 19: Red Ball (ages 4–7) 4–5pm and Orange Ball (ages 7–10) 5–6pm.":"Clases los jueves en Old Saybrook Swim & Racquet Club, del 22 de oct. al 19 de nov.: Red Ball (4–7 años) de 4 a 5 p. m. y Orange Ball (7–10 años) de 5 a 6 p. m.",
 "Saturday-morning nature class about owls, bats and other night animals, from late October into November. $30 residents.":"Clase de naturaleza los sábados por la mañana sobre búhos, murciélagos y otros animales nocturnos, de finales de octubre a noviembre. $30 residentes.",
 "3–5 years":"3–5 años",
 "308 Main St":"308 Main St",
 "Saturday sports for little ones: Sports R' Fun for ages 2–4 (Oct 31–Nov 28, $40) and Basketball Skill Builder for grades 1–3 (Nov 14–Dec 12, $25).":"Deportes los sábados para los pequeños: Sports R' Fun para 2–4 años (31 de oct.–28 de nov., $40) y Basketball Skill Builder para 1.º–3.º grado (14 de nov.–12 de dic., $25).",
 "2 years–grade 3":"2 años–3.º grado",
 "Zumba Kids (grades 3–4, Mondays from Oct 26) and Creative Craft Corner (grades 5–8, select Wednesdays Nov 4–Dec 16), $25 residents.":"Zumba Kids (3.º–4.º grado, lunes desde el 26 de oct.) y Creative Craft Corner (5.º–8.º grado, algunos miércoles del 4 de nov. al 16 de dic.), $25 residentes.",
 "Grades 3–8":"3.º–8.º grado",
}
