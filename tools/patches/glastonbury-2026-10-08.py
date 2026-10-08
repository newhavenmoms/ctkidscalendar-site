# Full playbook re-run, Oct 8 2026
ACAD="glas-academy"; SMS="smith-ms"; RBB="river-bend"; GWS="gideon-welles"
MR="https://glastonburyct.myrec.com/info/activities/program_details.aspx?ProgramID="
TOWN["venues"].update({ACAD:["Academy Building","2143 Main St"],SMS:["Smith Middle School running trail","216 Addison Rd"],RBB:["River Bend Bookshop","2400 Main St"],GWS:["Gideon Welles School","1029 Neipsic Rd"]})
TOWN["venueMeta"].update({ACAD:[None,1],SMS:[None,0],RBB:[None,1],GWS:[None,1]})
TOWN["events"]+=[
 {"t":"Halloween House Decorating Map","v":"glas-around","special":"hw","when":[{"from":"2026-10-09","to":"2026-11-01","t":[]}],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":MR+"30271",
  "blurb":"Parks & Rec's first 'Glastonbury Spooktacular' map of decorated houses comes out Oct 9: drive the route and vote for favorites on Facebook Oct 19–Nov 1."},
 {"t":"Goodwill Halloween Hustle 5K & Family Walk","v":SMS,"special":"hw","when":[W("2026-10-18",[["09:00","10:30"]])],"ages":"All ages (family walk)","a":["big"],"free":False,"price":"$33.10 (more after Oct 17)","rsvp":True,"src":"https://runsignup.com/Race/CT/Glastonbury/GoodwillHalloweenHustle5K",
  "blurb":"A costume 5K and family walk with prizes for scariest, funniest and best group, treats at the finish and music."},
 {"t":"Family Paint Night","v":ACAD,"when":D(["2026-11-06","2026-12-04"],[["17:30","19:30"]]),"ages":"Ages 7+ with a parent","a":["big"],"free":False,"price":"$30 for 2 people, up to $75 for 5","rsvp":True,"src":MR+"30210",
  "blurb":"Paint a canvas together with CT Paint Parties: 'Gobble, Gobble' turkeys on Nov 6 and 'Snow Pals' on Dec 4."},
 {"t":"Dreidels & Donuts","v":ACAD,"special":"hol","when":[W("2026-12-04",[["09:00","10:00"],["10:15","11:15"]])],"ages":"Ages 1–5 + caregiver","a":["toddler","preschool"],"free":False,"price":"$10","rsvp":True,"src":MR+"30008",
  "blurb":"A Hanukkah playgroup party with free play, a game, a story, a craft and a snack."},
 {"t":"Kids' Sewing Workshops (Sew This!)","v":ACAD,"when":D(["2026-11-23","2026-11-30","2026-12-07"],[["16:30","17:45"]]),"ages":"Ages 8–14","a":["big"],"free":False,"price":"$35–50, supplies included","rsvp":True,"src":MR+"30183",
  "blurb":"One-day sewing projects: a watercolor floral apron (Nov 23), a striped tote (Nov 30) and a decorate-your-own ugly sweater (Dec 7)."},
 {"t":"Author Story Hour: Stephen Savage","v":RBB,"when":[W("2026-11-27",[["10:30","11:30"]])],"ages":"Ages 3–6","a":["preschool"],"free":True,"price":"Free","drop":True,"src":"https://riverbendbookshop.com/event/2026-11-27/author-story-hour-stephen-savage",
  "blurb":"The author-illustrator of Wide Load on the Road reads at River Bend Bookshop the morning after Thanksgiving; kids go home with a signed copy."},
 {"t":"Vacation Voyagers Break Camp","v":GWS,"when":D(["2026-12-28","2026-12-29","2026-12-30"],[["09:00","15:00"]]),"ages":"Grades K–5","a":["big"],"free":False,"price":"$165 residents","rsvp":True,"src":MR+"30205",
  "blurb":"Three days of games, activities and field trips over December break; before- and after-care available."},
 {"t":"Bingo Bonanza","v":"riverfront-cc","when":[W("2026-12-29",[["13:00","15:00"]])],"ages":"All ages","a":["big"],"free":True,"price":"Free","rsvp":True,"src":MR+"30189",
  "blurb":"Intergenerational family bingo with prizes and refreshments, from Parks & Rec and the Senior Center. Register ahead."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Noon Year's R-E-A-D-O","w":"Welles-Turner Memorial Library, 2407 Main St","p":"The library's Noon Year's Eve bingo-style party for grades K–6 on Dec 31, 11–noon (registration required; it fills). This year's listing isn't posted yet.","src":"https://wtmlib.librarycalendar.com/events/list"},
 {"g":"hol","t":"Stuff a Cruiser Toy Drive","w":"Pinwheels Toys & Games, 60 Hebron Ave","p":"Glastonbury Police park a cruiser at the toy store and collect donated toys, on a late-November Saturday. Last year it was Nov 30, 10–2. This year's date isn't posted yet.","src":"https://glastonburyct.gov/home/showpublisheddocument/46550/638658807207030000"},
]
TOWN["classes"]+=[
 {"id":"glas-music-together","c":"music","n":"Music Together (Little Hands in Harmony)","u":MR+"29970","blurb":"Family music classes at the Riverfront Community Center, plus a three-week 'Jingle Jam' holiday mini-session in December (Tuesdays or Saturdays, $95).","ages":"0–6 years + adult","where":"Riverfront Community Center, 300 Welles St"},
 {"id":"glas-abrakadoodle","c":"art","n":"Abrakadoodle: Myths and Legends","u":MR+"30245","blurb":"A six-week Monday art class, Nov 2–Dec 7: grades K–2 at 4:15 and grades 3–6 at 5:30. $100.","ages":"Grades K–6","where":"Riverfront Community Center, 300 Welles St"},
 {"id":"glas-food-explorers","c":"art","n":"Food Explorers: Holiday Baking","u":MR+"29954","blurb":"Tuesday baking classes Nov 24–Dec 15 making holiday desserts. $90.","ages":"8–14 years","where":"Academy Building, 2143 Main St"},
]
REPLACE_PLACES["Pinwheels Toys & Games"]=("Pinwheels Toys & Games","An independent toy store in Derr Plaza (60 Hebron Ave) with craft kits, plush, LEGO and games for all ages; open daily.","Juguetería independiente en Derr Plaza (60 Hebron Ave) con manualidades, peluches, LEGO y juegos para todas las edades; abre todos los días.")
ADD_PLACES["out"]+=[("Williams Park","A town park with outdoor pond skating in winter when the ice is safe.","Un parque del pueblo con patinaje en el estanque en invierno cuando el hielo es seguro.")]
ADD_PLACES["rain"]+=[("Connecticut Audubon Center at Glastonbury","A nature center with live animals, exhibits and children's programs, open Tuesday–Saturday 10–5 (1361 Main St); call before going.","Un centro de naturaleza con animales vivos, exposiciones y programas infantiles, abierto de martes a sábado de 10 a 5 (1361 Main St); llama antes de ir."),
                     ("Central Rock Gym","An indoor climbing gym with youth programs and kid-friendly walls (Eastern Blvd).","Un gimnasio de escalada techado con programas juveniles y muros para niños (Eastern Blvd).")]
ES={
 "Parks & Rec's first 'Glastonbury Spooktacular' map of decorated houses comes out Oct 9: drive the route and vote for favorites on Facebook Oct 19–Nov 1.":"El primer mapa 'Glastonbury Spooktacular' de casas decoradas de Parks & Rec sale el 9 de oct.: recorre la ruta en auto y vota por tus favoritas en Facebook del 19 de oct. al 1 de nov.",
 "All ages (family walk)":"Todas las edades (caminata familiar)",
 "$33.10 (more after Oct 17)":"$33.10 (sube después del 17 de oct.)",
 "A costume 5K and family walk with prizes for scariest, funniest and best group, treats at the finish and music.":"Una carrera de 5 km con disfraces y caminata familiar, con premios al más aterrador, al más gracioso y al mejor grupo, golosinas en la meta y música.",
 "Ages 7+ with a parent":"7 años o más con papá o mamá",
 "$30 for 2 people, up to $75 for 5":"$30 por 2 personas, hasta $75 por 5",
 "Paint a canvas together with CT Paint Parties: 'Gobble, Gobble' turkeys on Nov 6 and 'Snow Pals' on Dec 4.":"Pinten juntos un lienzo con CT Paint Parties: pavos 'Gobble, Gobble' el 6 de nov. y 'Snow Pals' el 4 de dic.",
 "Ages 1–5 + caregiver":"1–5 años + un adulto",
 "$10":"$10",
 "A Hanukkah playgroup party with free play, a game, a story, a craft and a snack.":"Una fiesta de Janucá del grupo de juego con juego libre, un juego, un cuento, una manualidad y un bocadillo.",
 "Ages 8–14":"8–14 años",
 "$35–50, supplies included":"$35–50, materiales incluidos",
 "One-day sewing projects: a watercolor floral apron (Nov 23), a striped tote (Nov 30) and a decorate-your-own ugly sweater (Dec 7).":"Proyectos de costura de un día: un delantal floral de acuarela (23 de nov.), una bolsa de rayas (30 de nov.) y un suéter feo para decorar (7 de dic.).",
 "Ages 3–6":"3–6 años",
 "The author-illustrator of Wide Load on the Road reads at River Bend Bookshop the morning after Thanksgiving; kids go home with a signed copy.":"El autor e ilustrador de Wide Load on the Road lee en River Bend Bookshop la mañana después de Acción de Gracias; los niños se llevan un ejemplar firmado.",
 "Grades K–5":"Kínder–5.º grado",
 "$165 residents":"$165 residentes",
 "Three days of games, activities and field trips over December break; before- and after-care available.":"Tres días de juegos, actividades y excursiones durante las vacaciones de diciembre; hay cuidado antes y después.",
 "Intergenerational family bingo with prizes and refreshments, from Parks & Rec and the Senior Center. Register ahead.":"Bingo familiar intergeneracional con premios y refrigerios, de Parks & Rec y el Senior Center. Inscríbete con anticipación.",
 "Welles-Turner Memorial Library, 2407 Main St":"Welles-Turner Memorial Library, 2407 Main St",
 "The library's Noon Year's Eve bingo-style party for grades K–6 on Dec 31, 11–noon (registration required; it fills). This year's listing isn't posted yet.":"La fiesta de fin de año al mediodía de la biblioteca, con bingo, para kínder–6.º grado el 31 de dic., de 11 a mediodía (con inscripción; se llena). El anuncio de este año aún no se ha publicado.",
 "Pinwheels Toys & Games, 60 Hebron Ave":"Pinwheels Toys & Games, 60 Hebron Ave",
 "Glastonbury Police park a cruiser at the toy store and collect donated toys, on a late-November Saturday. Last year it was Nov 30, 10–2. This year's date isn't posted yet.":"La policía de Glastonbury estaciona una patrulla en la juguetería y recolecta juguetes donados, un sábado a finales de noviembre. El año pasado fue el 30 de nov., de 10 a 2. La fecha de este año aún no se ha publicado.",
 "Family music classes at the Riverfront Community Center, plus a three-week 'Jingle Jam' holiday mini-session in December (Tuesdays or Saturdays, $95).":"Clases de música en familia en el Riverfront Community Center, además de una minisesión navideña 'Jingle Jam' de tres semanas en diciembre (martes o sábados, $95).",
 "0–6 years + adult":"0–6 años + un adulto",
 "A six-week Monday art class, Nov 2–Dec 7: grades K–2 at 4:15 and grades 3–6 at 5:30. $100.":"Una clase de arte de seis semanas los lunes, del 2 de nov. al 7 de dic.: kínder–2.º grado a las 4:15 y 3.º–6.º grado a las 5:30. $100.",
 "Grades K–6":"Kínder–6.º grado",
 "Tuesday baking classes Nov 24–Dec 15 making holiday desserts. $90.":"Clases de repostería los martes, del 24 de nov. al 15 de dic., para hacer postres navideños. $90.",
 "8–14 years":"8–14 años",
}
