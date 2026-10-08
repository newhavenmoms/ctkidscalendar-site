# Full playbook re-run, Oct 8 2026
DNC="darien-nature-center"; DAC="darien-arts-center"; MOD="museum-of-darien"; DHS="darien-hs"
TOWN["venues"][DHS]=["Darien High School cross-country trail","80 High School Ln"]; TOWN["venueMeta"][DHS]=[None,0]
TOWN["venues"]["darien-community-association"]=["Darien Community Association","274 Middlesex Rd"]
for e in TOWN["events"]:
    if e["t"]=="Scary Stories to Tell in the Dark": e["check"]=True
    if e["t"]=="An Old Fashion Holiday": e["check"]=True
N="https://www.dariennaturecenter.org/"
TOWN["events"]+=[
 {"t":"Animal Room Grand Opening","v":DNC,"when":[W("2026-10-17",[["10:00","12:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"See listing","drop":True,"check":True,"src":N+"the-animal-room",
  "blurb":"Tour the Nature Center's new Animal Room, meet the animals and have s'mores."},
 {"t":"Early Dismissal at the Nature Center","v":DNC,"when":[W("2026-10-22",[["14:00","15:30"]]),W("2026-10-23",[["14:00","15:30"]])],"ages":"Grades K–5 (drop-off)","a":["big"],"free":False,"price":"See registration","rsvp":True,"check":True,"src":N+"early-dismissal",
  "blurb":"Early-release afternoons: a hike and campfire (Oct 22) and hands-on time with reptiles, mammals and birds (Oct 23)."},
 {"t":"Pumpkin Decorating at the Nature Center","v":DNC,"special":"hw","when":D(["2026-10-27","2026-10-28"],[["15:00","16:30"]]),"ages":"All ages + adult","a":B+["big"],"free":False,"price":"$35 per family members, $45 non-members","rsvp":True,"src":N+"pumpkin-decorating",
  "blurb":"Come in costume for a costume scavenger hunt, s'mores, photos with the animals and pumpkin decorating."},
 {"t":"CRAFTLAB: Tours and Tricorn Hats","v":MOD,"when":[W("2026-11-03",[["11:00","13:00"]])],"ages":"Kids + adult","a":["preschool","big"],"free":False,"price":"$10","drop":True,"src":"https://museumofdarien.org/product/craftlab-tours-and-tricorn-hats-on-election-day/",
  "blurb":"An Election Day tour of the 1736 homestead about how kids lived 250 years ago, then kids make a tricorn hat."},
 {"t":"Overstuffed Turkey Trot & 1-Mile Fun Run","v":DHS,"when":[W("2026-11-27",[["10:00","11:30"]])],"ages":"All ages (5 and under free)","a":["preschool","big"],"free":False,"price":"$30 ages 6–12, $45+ adults","rsvp":True,"src":"https://runsignup.com/Race/CT/Darien/DarienDepotOverstuffed",
  "blurb":"The day after Thanksgiving: a 1-mile fun run/walk at 10 and a 5K at 10:30, benefiting The Depot youth center. Snow date Nov 28."},
 {"t":"The Nutcracker (Darien Arts Center)","v":DAC,"special":"hol","when":[W("2026-12-05",[["15:00","17:00"],["18:00","20:00"]]),W("2026-12-06",[["12:00","14:00"],["15:00","17:00"]]),W("2026-12-12",[["15:00","17:00"],["18:00","20:00"]]),W("2026-12-13",[["12:00","14:00"],["15:00","17:00"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"See ticket site","rsvp":True,"src":"https://register.darienarts.org/CourseCatalog/Tickets/EventView.asp?EventID=100",
  "blurb":"The arts center's full-length Nutcracker, danced by academy students ages 5–18. End times are estimates."},
]
TOWN["tba"]+=[
 {"g":"hw","t":"DCA Halloween Parade","w":"Post Rd, from the Darien Fire Station (848 Post Rd)","p":"Kids in costume parade along Post Road and trick-or-treat at the shops, usually the Friday morning before Halloween at 10. This year's date isn't posted yet.","src":"https://darienite.com/dca-annual-halloween-parade-coming-friday-oct-29-downtown-267862"},
 {"g":"hol","t":"Tree Lighting with Santa at Darien Sport Shop","w":"Darien Sport Shop back lot, Post Rd","p":"Santa arrives by fire truck, with music, cocoa and candy canes, the Sunday after Thanksgiving, 4:30–5:30. Letters to Santa can be dropped off into December. This year's date isn't posted yet.","src":"https://patch.com/connecticut/darien/calendar/event/20251129/ffc5d697-e674-4cf4-96b0-e4ab34a3bd0d/spirit-of-the-season-launch-in-darien"},
 {"g":"hol","t":"Town Hanukkah Celebration","w":"Grove Street Plaza","p":"Crafts, treats, PJ Library books, latkes and a menorah lighting at 6pm on one night of Hanukkah (Dec 4–12 this year); bring a toy or food donation. This year's date isn't posted yet.","src":"https://patch.com/connecticut/darien/details-dariens-hanukkah-celebration"},
 {"g":"hol","t":"Lit Tree Lane Stroll","w":"Darien Library, 1441 Post Rd","p":"Decorated trees fill the library from the Friday after Thanksgiving into January, with an opening-night stroll, music and a kids' craft. Last year it opened Nov 28.","src":"https://www.darienlibrary.org/littreelane"},
]
TOWN["classes"]+=[{"id":"dnc-snowbirds","c":"nature","n":"Snowbirds Winter Break Camp","u":N+"vacation-programs","blurb":"A nature preschool camp Dec 14–17 for twos and ages 3–6; membership required.","ages":"2–6 years","where":"120 Brookside Rd"}]
ES={
 "See listing":"Ver el anuncio",
 "Tour the Nature Center's new Animal Room, meet the animals and have s'mores.":"Recorre la nueva Animal Room del centro de naturaleza, conoce a los animales y come s'mores.",
 "Grades K–5 (drop-off)":"Kínder–5.º grado (sin papás)","See registration":"Ver la inscripción",
 "Early-release afternoons: a hike and campfire (Oct 22) and hands-on time with reptiles, mammals and birds (Oct 23).":"Tardes de salida temprana: caminata y fogata (22 de oct.) y tiempo práctico con reptiles, mamíferos y aves (23 de oct.).",
 "All ages + adult":"Todas las edades + un adulto",
 "$35 per family members, $45 non-members":"$35 por familia miembros, $45 no miembros",
 "Come in costume for a costume scavenger hunt, s'mores, photos with the animals and pumpkin decorating.":"Ven disfrazado a una búsqueda del tesoro de disfraces, s'mores, fotos con los animales y decoración de calabazas.",
 "Kids + adult":"Niños + un adulto","$10":"$10",
 "An Election Day tour of the 1736 homestead about how kids lived 250 years ago, then kids make a tricorn hat.":"Un recorrido en el Día de Elecciones por la casa de 1736 sobre cómo vivían los niños hace 250 años; luego los niños hacen un tricornio.",
 "All ages (5 and under free)":"Todas las edades (5 años o menos gratis)",
 "$30 ages 6–12, $45+ adults":"$30 de 6–12 años, desde $45 adultos",
 "The day after Thanksgiving: a 1-mile fun run/walk at 10 and a 5K at 10:30, benefiting The Depot youth center. Snow date Nov 28.":"El día después de Acción de Gracias: una carrera/caminata divertida de 1 milla a las 10 y unos 5 km a las 10:30, a beneficio del centro juvenil The Depot. Fecha en caso de nieve: 28 de nov.",
 "See ticket site":"Ver el sitio de boletos",
 "The arts center's full-length Nutcracker, danced by academy students ages 5–18. End times are estimates.":"El Cascanueces completo del centro de artes, bailado por estudiantes de 5 a 18 años. Las horas de término son aproximadas.",
 "Post Rd, from the Darien Fire Station (848 Post Rd)":"Post Rd, desde la estación de bomberos de Darien (848 Post Rd)",
 "Kids in costume parade along Post Road and trick-or-treat at the shops, usually the Friday morning before Halloween at 10. This year's date isn't posted yet.":"Los niños desfilan disfrazados por Post Road y piden dulces en las tiendas, por lo general el viernes por la mañana antes de Halloween a las 10. La fecha de este año aún no se ha publicado.",
 "Darien Sport Shop back lot, Post Rd":"Estacionamiento trasero de Darien Sport Shop, Post Rd",
 "Santa arrives by fire truck, with music, cocoa and candy canes, the Sunday after Thanksgiving, 4:30–5:30. Letters to Santa can be dropped off into December. This year's date isn't posted yet.":"Santa llega en camión de bomberos, con música, chocolate y bastones de caramelo, el domingo después de Acción de Gracias, de 4:30 a 5:30. Las cartas a Santa se reciben hasta diciembre. La fecha de este año aún no se ha publicado.",
 "Grove Street Plaza":"Grove Street Plaza",
 "Crafts, treats, PJ Library books, latkes and a menorah lighting at 6pm on one night of Hanukkah (Dec 4–12 this year); bring a toy or food donation. This year's date isn't posted yet.":"Manualidades, golosinas, libros de PJ Library, latkes y el encendido de la menorá a las 6 p. m. en una noche de Janucá (del 4 al 12 de dic. este año); trae un juguete o alimento para donar. La fecha de este año aún no se ha publicado.",
 "Darien Library, 1441 Post Rd":"Darien Library, 1441 Post Rd",
 "Decorated trees fill the library from the Friday after Thanksgiving into January, with an opening-night stroll, music and a kids' craft. Last year it opened Nov 28.":"Árboles decorados llenan la biblioteca desde el viernes después de Acción de Gracias hasta enero, con un paseo de inauguración, música y una manualidad para niños. El año pasado abrió el 28 de nov.",
 "A nature preschool camp Dec 14–17 for twos and ages 3–6; membership required.":"Un campamento de naturaleza preescolar del 14 al 17 de dic. para niños de 2 y de 3–6 años; requiere membresía.",
 "2–6 years":"2–6 años",
}
