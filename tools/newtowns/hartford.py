W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
SRC="https://programs.hplct.org/events?a=Family%2CYouth"
B=["baby","toddler","preschool"]
DT,AL,BA,CF,DW,PS,RO="hpl-downtown","hpl-albany","hpl-barbour","hpl-campfield","hpl-dwight","hpl-parkst","hpl-ropkins"
def ev(v,**k):
    e={"v":v,"free":True,"price":"Free","src":SRC}; e.update(k); return e
TOWN={
 "display":"Hartford","accent":"#D9C8EE",
 "venues":{DT:["Hartford Public Library, Downtown","500 Main St"],
           AL:["Albany Branch Library","1250 Albany Ave"],
           BA:["Barbour Branch Library","261 Barbour St"],
           CF:["Camp Field Branch Library","30 Campfield Ave"],
           DW:["Dwight Branch Library","7 New Park Ave"],
           PS:["Park Street Library @ the Lyric","603 Park St"],
           RO:["Ropkins Branch Library","1750 Main St"],
           "ctsci":["Connecticut Science Center","250 Columbus Blvd"],
           "hartford-stage":["Hartford Stage","50 Church St"]},
 "venueMeta":{DT:["downtown",1],AL:["northend",1],BA:["northend",1],CF:["southside",1],DW:["southside",1],PS:["southside",1],RO:["northend",1],
              "ctsci":["downtown",1],"hartford-stage":["downtown",1]},
 "hoods":[["downtown","Downtown"],["northend","North End"],["southside","South End & Parkville"]],
 "events":[
  # ---- little ones ----
  ev(DT,t="First Steps in Music",when=D(["2026-10-19","2026-10-26","2026-11-02","2026-11-09","2026-11-16","2026-11-23"],[["11:00","12:00"]]),ages="Babies to preschoolers + caregiver",a=B,rsvp=True,
     blurb="A joyful early-childhood music class in the Downtown Youth Program Room. Registration for each Monday opens at 11 am the Monday before."),
  ev(CF,t="Story Time at Camp Field",when=D(["2026-10-20","2026-10-27","2026-11-03","2026-11-10","2026-11-17","2026-11-24"],[["11:00","11:45"]]),ages="Birth–age 5 + caregiver",a=B,drop=True,
     blurb="Stories, songs and fingerplays every Tuesday morning at the Camp Field Branch."),
  ev(DW,t="Sensory Storytime",when=D(["2026-10-20","2026-11-24"],[["10:00","10:30"]]),ages="Ages 0–5 + caregiver",a=B,drop=True,
     blurb="An adapted storytime for kids of all abilities and sensory needs, ending with bubble time and sensory play."),
  ev(RO,t="Storytime Adventures with Ms. Linda",when=D(["2026-10-27","2026-11-24"],[["09:30","10:15"]]),ages="Ages 2–5 + caregiver",a=["toddler","preschool"],drop=True,
     blurb="An interactive storytime with books, songs, rhymes, music and movement."),
  ev(DT,t="Family Sensory Storytime",when=D(["2026-10-30","2026-11-20","2026-12-04"],[["11:00","12:00"]]),ages="Ages 5 and under + caregiver",a=B,drop=True,
     blurb="A read-along with Ms. Williams: sensory play, stories, music, rhymes and fingerplays."),
  # ---- after school ----
  ev(RO,t="Homework Heroes",s=[[1,[["15:30","16:00"]],"2026-10-12","2026-11-30"],[2,[["15:30","16:00"]],"2026-10-13","2026-11-24"],[3,[["15:30","16:00"]],"2026-10-14","2026-11-04"]],ages="Ages 6–12 (under 12 with a caregiver)",a=["big"],drop=True,
     blurb="After-school help with homework, reading and assignments at the Ropkins Branch."),
  ev(RO,t="Fall Into Creativity",s=[[1,[["15:45","16:15"]],"2026-10-12","2026-11-30"]],ages="Ages 6–12",a=["big"],drop=True,
     blurb="A different hands-on craft with Ms. Linda every Monday at the Ropkins Branch."),
  ev(RO,t="Fall STEM Adventures",s=[[2,[["15:30","16:15"]],"2026-10-13","2026-11-24"]],ages="Ages 6–12",a=["big"],drop=True,
     blurb="Weekly hands-on STEM activities: discover, build and explore."),
  ev(RO,t="Think, Search & Solve!",s=[[3,[["15:30","16:15"]],"2026-10-14","2026-11-25"]],x=["2026-11-11"],ages="Ages 6–12",a=["big"],drop=True,
     blurb="Fall-themed word searches, I Spy puzzles, mazes and other brain teasers."),
  ev(CF,t="Homework Hub",when=D(["2026-10-12","2026-10-14","2026-10-19","2026-10-21","2026-10-26","2026-10-28","2026-11-02","2026-11-06","2026-11-09","2026-11-13","2026-11-16","2026-11-20","2026-11-23","2026-11-27"],[["16:00","17:00"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="Drop-in after-school help with assignments and studying at the Camp Field Branch (Mondays and Wednesdays in October, Mondays and Fridays in November)."),
  ev(CF,t="Craft Corner",when=D(["2026-10-13","2026-10-20","2026-10-27","2026-11-03","2026-11-17"],[["16:00","17:00"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="A new craft every week at the Camp Field Branch."),
  ev(CF,t="Thursday Fun Zone",when=D(["2026-10-08","2026-10-15","2026-10-22","2026-11-05","2026-11-12","2026-11-19"],[["16:00","17:00"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="A different themed activity or craft every Thursday at the Camp Field Branch."),
  ev(CF,t="Builders Club",when=D(["2026-10-26","2026-11-23"],[["16:00","17:00"]]),ages="Ages 5–12",a=["big"],drop=True,
     blurb="A monthly LEGO building challenge."),
  ev(AL,t="Brick Builders & Homework Club",when=D(["2026-10-12","2026-10-19","2026-10-26"],[["15:30","16:30"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="Monday afternoons at the Albany Branch: build with all kinds of building kits, or drop in to do homework and help your friends."),
  ev(AL,t="Crafternoon at Albany",when=D(["2026-10-13","2026-10-20","2026-10-27"],[["15:30","16:30"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="A fun craft every Tuesday at the Albany Branch."),
  ev(AL,t="Quiet Coloring",when=D(["2026-10-14","2026-10-21","2026-10-28"],[["15:30","16:30"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="A relaxing coloring hour at the Albany Branch."),
  ev(AL,t="Makerspace Fridays",when=D(["2026-10-09","2026-10-16","2026-10-23"],[["15:30","16:30"]]),ages="Ages 6–12",a=["big"],drop=True,
     blurb="Use the Albany Branch's makerspace materials to make something cool."),
  ev(DW,t="Decorate Dwight: Rainbows & Rainclouds",when=[W("2026-10-12",[["15:00","16:00"]])],ages="Ages 6–12",a=["big"],drop=True,
     blurb="Make a rainbow or raincloud for the children's area's blue-sky wall."),
  ev(AL,t="Activities with Q+",when=[W("2026-10-15",[["15:30","16:30"]])],ages="Ages 6–12",a=["big"],drop=True,
     blurb="A craft or activity with Norm from Q+."),
  ev(DT,t="Crafternoon Downtown",when=[W("2026-10-21",[["16:00","17:00"]])],ages="Kids",a=["big"],rsvp=True,
     blurb="Seasonal crafts, recycled art and building projects. Please RSVP; supplies are limited."),
  ev(BA,t="Robotics Club",when=D(["2026-10-26","2026-10-27"],[["16:00","17:30"]]),ages="Ages 6–15",a=["big"],rsvp=True,
     blurb="Learn to code and program a robot with the Children's Museum. Registration required."),
  ev(DW,t="Tech Take Apart",when=[W("2026-11-04",[["15:00","16:00"]])],ages="Ages 6–12",a=["big"],drop=True,check=True,
     blurb="Take apart old appliances and electronics with screwdrivers and tools to see how they work."),
  ev(DW,t="Anime Eyes Drawing Tutorial",when=[W("2026-11-09",[["15:00","16:00"]])],ages="Ages 6–12",a=["big"],drop=True,
     blurb="A beginner-friendly lesson in drawing anime-style eyes."),
  ev(DW,t="Native American Paper Ribbon Skirts",when=[W("2026-11-16",[["15:00","16:00"]])],ages="Ages 6–12",a=["big"],drop=True,
     blurb="A paper ribbon-skirt craft for Native American Heritage Month, inspired by What Your Ribbon Skirt Means to Me."),
  ev(DT,t="Mobile Makerspace",when=D(["2026-11-18","2026-11-19"],[["16:00","17:30"]]),ages="Ages 6–12",a=["big"],rsvp=True,
     blurb="The Children's Museum brings 3-D printers, a Chomp Saw and Cricut machines for creative STEM play, Downtown. Registration required."),
  ev(PS,t="Mobile Makerspace",when=D(["2026-12-16","2026-12-17"],[["16:00","17:30"]]),ages="Ages 6–12",a=["big"],rsvp=True,
     blurb="The Children's Museum brings 3-D printers, a Chomp Saw and Cricut machines for creative STEM play at Park Street. Registration required."),
  # ---- holidays ----
  ev(DW,t="Library Trunk or Treat",special="hw",when=[W("2026-10-29",[["15:00","17:00"]])],ages="All ages",a=B+["big"],drop=True,check=True,
     blurb="Indoor trick-or-treat stations with candy, pumpkins and crafts. Costumes encouraged."),
  ev(AL,t="Family-Friendly Halloween Party",special="hw",when=[W("2026-10-29",[["15:00","17:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="Music, candy, pizza and activities for ghouls and goblins of every age."),
  ev(CF,t="Library Spooktacular",special="hw",when=[W("2026-10-29",[["16:00","17:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="Spooky crafts, activities and a special snack. Kids are welcome in costume."),
  ev(CF,t="Veterans Day Family Celebration",when=[W("2026-11-10",[["16:00","17:00"]])],ages="All ages",a=["preschool","big"],drop=True,
     blurb="Make thank-you cards for veterans and enjoy family activities."),
  ev(DW,t="Thanksgiving Hand Turkey Magnets",when=[W("2026-11-23",[["15:00","16:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="The classic handprint turkey, turned into a fridge magnet."),
  ev(CF,t="Thanksgiving Fun Fest",when=[W("2026-11-24",[["16:00","17:00"]])],ages="All ages",a=["preschool","big"],drop=True,
     blurb="A Thanksgiving craft, activities and a special snack."),
  {"t":"Spooktacular at the Science Center","v":"ctsci","special":"hw","when":[W("2026-10-18",[["10:30","14:30"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Included with admission","src":"https://ctvisit.com/events/spooktacular-2",
   "blurb":"Halloween-themed science activities throughout the Connecticut Science Center, included with general admission."},
  {"t":"A Christmas Carol","v":"hartford-stage","special":"hol","when":[{"from":"2026-11-21","to":"2026-12-27","t":[]}],"ages":"School-age kids and up","a":["big"],"free":False,"price":"Tickets vary; 50% off youth tickets at off-peak shows","check":True,"src":"https://www.hartfordstage.org/2026-2027/a-christmas-carol/",
   "blurb":"Hartford Stage's annual ghost-story staging of Dickens, a December tradition. Check the theater's age guidance; some scenes are scary for little ones."},
 ],
 "tba":[],
 "classes":[],
 "library":{"for":"Free, every week","name":"Hartford Public Library","desc":"Eight locations with after-school crafts, STEM and homework help most weekdays (Ropkins, Camp Field and Albany are busiest), weekly storytime at Camp Field, a sensory storytime at Dwight, and a First Steps in Music class Downtown.","a":"See kids' and family programs","href":SRC},
}
PLACES={
 "out":[("Bushnell Park","The downtown park by the State Capitol, home to a 1914 carousel that runs in the warmer months.","El parque del centro junto al Capitolio, con un carrusel de 1914 que funciona en los meses cálidos."),
        ("Elizabeth Park","Famous rose gardens, greenhouses, lawns and a pond on the West Hartford line.","Famosos jardines de rosas, invernaderos, praderas y un estanque en el límite con West Hartford."),
        ("Riverside Park","Riverfront paths, a playground and boat launch along the Connecticut River.","Senderos junto al río, un área de juegos y una rampa para botes a orillas del río Connecticut."),
        ("Keney Park","One of the country's largest city parks, with woods, trails and playing fields in the North End.","Uno de los parques urbanos más grandes del país, con bosques, senderos y canchas en el North End.")],
 "rain":[("Connecticut Science Center","Ten galleries of hands-on science, including KidSpace for children 7 and under, plus a 3-D theater.","Diez galerías de ciencia interactiva, incluido KidSpace para niños de 7 años o menos, y un cine 3D."),
         ("Wadsworth Atheneum Museum of Art","America's oldest public art museum, with family days and art-making activities.","El museo de arte público más antiguo de Estados Unidos, con días familiares y actividades de arte."),
         ("Hartford Public Library, Downtown","The main library on Main Street, with a Youth Program Room and family programs.","La biblioteca principal en Main Street, con una sala de programas juveniles y actividades familiares."),
         ("Mark Twain House & Museum","Tours of the author's ornate home, best for school-age kids.","Recorridos por la elaborada casa del autor, ideales para niños en edad escolar.")],
 "drive":[("The Children's Museum","Live animals, a planetarium and hands-on exhibits in West Hartford.","Animales vivos, un planetario y exposiciones interactivas en West Hartford."),
          ("Dinosaur State Park","Real dinosaur tracks under a geodesic dome, plus trails, in Rocky Hill.","Huellas reales de dinosaurio bajo una cúpula geodésica, además de senderos, en Rocky Hill."),
          ("Lake Compounce","New England's oldest amusement park, in Bristol.","El parque de diversiones más antiguo de Nueva Inglaterra, en Bristol.")],
}
ES={
 "Babies to preschoolers + caregiver":"Bebés a preescolares + un adulto",
 "A joyful early-childhood music class in the Downtown Youth Program Room. Registration for each Monday opens at 11 am the Monday before.":"Una alegre clase de música para la primera infancia en la sala de programas juveniles del Downtown. La inscripción para cada lunes se abre a las 11 am del lunes anterior.",
 "Birth–age 5 + caregiver":"0–5 años + un adulto",
 "Stories, songs and fingerplays every Tuesday morning at the Camp Field Branch.":"Cuentos, canciones y juegos con los dedos todos los martes por la mañana en la sucursal Camp Field.",
 "Ages 0–5 + caregiver":"0–5 años + un adulto",
 "An adapted storytime for kids of all abilities and sensory needs, ending with bubble time and sensory play.":"Un cuentacuentos adaptado para niños de todas las capacidades y necesidades sensoriales, que termina con burbujas y juego sensorial.",
 "Ages 2–5 + caregiver":"2–5 años + un adulto",
 "An interactive storytime with books, songs, rhymes, music and movement.":"Un cuentacuentos interactivo con libros, canciones, rimas, música y movimiento.",
 "Ages 5 and under + caregiver":"Hasta 5 años + un adulto",
 "A read-along with Ms. Williams: sensory play, stories, music, rhymes and fingerplays.":"Lectura con Ms. Williams: juego sensorial, cuentos, música, rimas y juegos con los dedos.",
 "Ages 6–12 (under 12 with a caregiver)":"6–12 años (menores de 12 con un adulto)",
 "After-school help with homework, reading and assignments at the Ropkins Branch.":"Ayuda después de clases con tareas, lectura y trabajos escolares en la sucursal Ropkins.",
 "Ages 6–12":"6–12 años",
 "A different hands-on craft with Ms. Linda every Monday at the Ropkins Branch.":"Una manualidad diferente con Ms. Linda cada lunes en la sucursal Ropkins.",
 "Weekly hands-on STEM activities: discover, build and explore.":"Actividades STEM prácticas cada semana: descubre, construye y explora.",
 "Fall-themed word searches, I Spy puzzles, mazes and other brain teasers.":"Sopas de letras de otoño, juegos de 'veo veo', laberintos y otros acertijos.",
 "Drop-in after-school help with assignments and studying at the Camp Field Branch (Mondays and Wednesdays in October, Mondays and Fridays in November).":"Ayuda sin inscripción después de clases con tareas y estudio en la sucursal Camp Field (lunes y miércoles en octubre, lunes y viernes en noviembre).",
 "A new craft every week at the Camp Field Branch.":"Una manualidad nueva cada semana en la sucursal Camp Field.",
 "A different themed activity or craft every Thursday at the Camp Field Branch.":"Una actividad o manualidad temática diferente cada jueves en la sucursal Camp Field.",
 "Ages 5–12":"5–12 años",
 "A monthly LEGO building challenge.":"Un reto mensual de construcción con LEGO.",
 "Monday afternoons at the Albany Branch: build with all kinds of building kits, or drop in to do homework and help your friends.":"Los lunes por la tarde en la sucursal Albany: construye con todo tipo de kits o ven a hacer la tarea y ayudar a tus amigos.",
 "A fun craft every Tuesday at the Albany Branch.":"Una manualidad divertida cada martes en la sucursal Albany.",
 "A relaxing coloring hour at the Albany Branch.":"Una hora relajante para colorear en la sucursal Albany.",
 "Use the Albany Branch's makerspace materials to make something cool.":"Usa los materiales del makerspace de la sucursal Albany para crear algo genial.",
 "Make a rainbow or raincloud for the children's area's blue-sky wall.":"Haz un arcoíris o una nube de lluvia para la pared de cielo azul del área infantil.",
 "A craft or activity with Norm from Q+.":"Una manualidad o actividad con Norm de Q+.",
 "Kids":"Niños",
 "Seasonal crafts, recycled art and building projects. Please RSVP; supplies are limited.":"Manualidades de temporada, arte con reciclaje y proyectos de construcción. Confirma tu asistencia; los materiales son limitados.",
 "Ages 6–15":"6–15 años",
 "Learn to code and program a robot with the Children's Museum. Registration required.":"Aprende a programar un robot con el Children's Museum. Inscripción obligatoria.",
 "Take apart old appliances and electronics with screwdrivers and tools to see how they work.":"Desarma aparatos y equipos electrónicos viejos con destornilladores y herramientas para ver cómo funcionan.",
 "A beginner-friendly lesson in drawing anime-style eyes.":"Una clase para principiantes sobre cómo dibujar ojos estilo anime.",
 "A paper ribbon-skirt craft for Native American Heritage Month, inspired by What Your Ribbon Skirt Means to Me.":"Una manualidad de falda de listones de papel para el Mes de la Herencia Nativa Americana, inspirada en What Your Ribbon Skirt Means to Me.",
 "The Children's Museum brings 3-D printers, a Chomp Saw and Cricut machines for creative STEM play, Downtown. Registration required.":"El Children's Museum trae impresoras 3D, una sierra Chomp y máquinas Cricut para juego creativo STEM, en el Downtown. Inscripción obligatoria.",
 "The Children's Museum brings 3-D printers, a Chomp Saw and Cricut machines for creative STEM play at Park Street. Registration required.":"El Children's Museum trae impresoras 3D, una sierra Chomp y máquinas Cricut para juego creativo STEM en Park Street. Inscripción obligatoria.",
 "All ages":"Todas las edades",
 "Indoor trick-or-treat stations with candy, pumpkins and crafts. Costumes encouraged.":"Estaciones para pedir dulces bajo techo con caramelos, calabazas y manualidades. Se recomiendan los disfraces.",
 "Music, candy, pizza and activities for ghouls and goblins of every age.":"Música, dulces, pizza y actividades para monstruitos de todas las edades.",
 "Spooky crafts, activities and a special snack. Kids are welcome in costume.":"Manualidades de miedo, actividades y un bocadillo especial. Los niños pueden venir disfrazados.",
 "Make thank-you cards for veterans and enjoy family activities.":"Haz tarjetas de agradecimiento para veteranos y disfruta de actividades familiares.",
 "The classic handprint turkey, turned into a fridge magnet.":"El clásico pavo con la huella de la mano, convertido en un imán para el refrigerador.",
 "A Thanksgiving craft, activities and a special snack.":"Una manualidad de Acción de Gracias, actividades y un bocadillo especial.",
 "Included with admission":"Incluido con la entrada",
 "Halloween-themed science activities throughout the Connecticut Science Center, included with general admission.":"Actividades de ciencia con tema de Halloween en todo el Connecticut Science Center, incluidas con la entrada general.",
 "School-age kids and up":"Niños en edad escolar y mayores",
 "Tickets vary; 50% off youth tickets at off-peak shows":"Precios variables; 50% de descuento en boletos juveniles en funciones de menor demanda",
 "Hartford Stage's annual ghost-story staging of Dickens, a December tradition. Check the theater's age guidance; some scenes are scary for little ones.":"La puesta anual de Hartford Stage de la historia de fantasmas de Dickens, una tradición de diciembre. Consulta la guía de edades del teatro; algunas escenas dan miedo a los más pequeños.",
 "Eight locations with after-school crafts, STEM and homework help most weekdays (Ropkins, Camp Field and Albany are busiest), weekly storytime at Camp Field, a sensory storytime at Dwight, and a First Steps in Music class Downtown.":"Ocho sedes con manualidades, STEM y ayuda con tareas después de clases casi todos los días entre semana (Ropkins, Camp Field y Albany son las más activas), cuentacuentos semanal en Camp Field, un cuentacuentos sensorial en Dwight y la clase First Steps in Music en el Downtown.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7) ----
WA="wadsworth"; BU="bushnell"; BP="bushnell-park"; UL="urban-league"
TOWN["venues"].update({WA:["Wadsworth Atheneum Museum of Art","600 Main St"],BU:["The Bushnell","166 Capitol Ave"],BP:["Bushnell Park","Downtown"],UL:["Urban League of Greater Hartford","140 Woodland St"]})
TOWN["venueMeta"].update({WA:["downtown",1],BU:["downtown",1],BP:["downtown",0],UL:["northend",0]})
WAS="https://www.thewadsworth.org/events/action~agenda/request_format~html/"
BCT="https://www.bushnell.org/education/bushnell-childrens-theatre"
TOWN["events"]+=[
 {"t":"Second Saturdays for Families: Not So Spooky Halloween","v":WA,"special":"hw","when":[W("2026-10-10",[["10:00","14:00"]])],"ages":"Families","a":["preschool","big"],"free":True,"price":"Free admission all day","drop":True,"src":WAS,
  "blurb":"Free museum admission all day, glow-in-the-dark charm bracelets and other autumn crafts, and a magic show by Mr. B. The Hartford Marathon is the same day, so expect downtown road closures."},
 {"t":"Día de Muertos Community Celebration","v":WA,"when":[W("2026-11-01",[["10:00","14:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","rsvp":True,"src":"https://www.thewadsworth.org/events/action~agenda/page_offset~2/request_format~html/",
  "blurb":"Help build a community ofrenda, make incense cones and decorate sugar-skull masks, with ballet folklórico and live mariachi. Registration encouraged. A free sensory-friendly short-film program for ages 8 and up follows at 2 pm."},
 {"t":"Second Saturdays for Families: Monet Moments","v":WA,"when":[W("2026-11-14",[["10:00","15:00"]])],"ages":"Families","a":B+["big"],"free":True,"price":"Free admission all day","drop":True,"src":"https://www.thewadsworth.org/events/action~agenda/page_offset~2/request_format~html/",
  "blurb":"Free admission, an 11 am family tour, flower-bouquet design and hand puppets with the East Lyme Puppetry Project, free popcorn, and New York International Children's Film Festival shorts for little kids and big kids (11–3, the 11 and 12 o'clock shows sensory-friendly)."},
 {"t":"Festival of Lights at the Wadsworth","v":WA,"special":"hol","when":[W("2026-12-07",[["16:30","18:30"]])],"ages":"Families","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://www.thewadsworth.org/events/action~agenda/page_offset~3/request_format~html/",
  "blurb":"A Hanukkah evening with an outdoor menorah lighting and family-friendly crafts."},
 {"t":"Shaun Boothe and the Unauthorized Biography Series","v":BU,"special":"shows","when":D(["2026-10-29","2026-10-30"],[["10:00","11:00"],["12:00","13:00"]]),"ages":"Grades 4–9","a":["big"],"free":False,"price":"$14","rsvp":True,"check":True,"src":BCT,
  "blurb":"A hip-hop biography show from the Bushnell Children's Theatre series. These are school-day shows, but the public can buy tickets from the box office (860-987-5900). The Friday 10 am show is sold out."},
 {"t":"Pete the Cat","v":BU,"special":"shows","when":[W("2026-11-23",[["12:00","13:00"]])],"ages":"Pre-K–grade 3","a":["preschool","big"],"free":False,"price":"$14","rsvp":True,"check":True,"src":BCT,
  "blurb":"The groovy cat's picture books on stage, in the Bushnell Children's Theatre series. The 10 am show is sold out; buy noon tickets from the box office (860-987-5900)."},
 {"t":"A Magical Cirque Christmas","v":BU,"special":"hol","when":[W("2026-11-29",[["16:00","18:00"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Tickets vary","check":True,"src":"https://findingconnecticut.com/the-bushnell-announced-a-magical-cirque-christmas/",
  "blurb":"Cirque acrobats, aerialists and holiday music in a show built for family audiences."},
 {"t":"The Nutmeg Ballet's Nutcracker","v":BU,"special":"hol","when":D(["2026-12-05","2026-12-06"],[]),"ages":"All ages","a":["preschool","big"],"free":False,"price":"Tickets vary","check":True,"src":"https://www.nutmegconservatory.org/nutcracker",
  "blurb":"The Nutmeg Ballet Conservatory's Nutcracker at the Bushnell. Showtimes are on the Bushnell's site."},
 {"t":"Connecticut Ballet's The Nutcracker","v":BU,"special":"hol","when":[W("2026-12-19",[["14:00","16:00"],["18:00","20:00"]]),W("2026-12-20",[["13:00","15:00"],["17:00","19:00"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Tickets vary","src":"https://hartfordsymphony.org/portfolio-items/the-nutcracker-2026/",
  "blurb":"Connecticut Ballet with guest stars from New York City Ballet and American Ballet Theatre, and the Hartford Symphony playing live."},
]
TOWN["tba"]+=[
 {"g":"hw","t":"Urban League Trunk or Treat","w":"Urban League of Greater Hartford, 140 Woodland St",
  "p":"A free trunk-or-treat with a DJ, double-dutch, crafts, prizes and a costume parade, usually the Friday before Halloween, 4–6 pm. This year's date isn't posted yet.","src":"https://www.ulgh.org/events-1/urban-league-trunk-or-treat"},
 {"g":"hol","t":"Bushnell Park Tree Lighting","w":"Bushnell Park, downtown",
  "p":"The mayor lights the city's tree in Bushnell Park, with caroling, hot chocolate and free skating at Winterfest. The last two were on the Sunday after Thanksgiving at 4:30. This year's date isn't posted yet.","src":"https://www.audacy.com/wtic/news/local/second-annual-bushnell-tree-lighting"},
 {"g":"hol","t":"Winterfest at Bushnell Park","w":"Bushnell Park, downtown",
  "p":"Free outdoor skating, free skate rentals and lessons, Santa photos and themed nights, daily 11–8 from Black Friday into January (closed when it rains). 2026 dates aren't posted yet.","src":"https://www.wfsb.com/2025/11/26/winterfest-returns-hartfords-bushnell-park-15th-year/"},
]
TOWN["classes"]+=[
 {"id":"artists-collective","c":"art","n":"The Artists Collective","u":"https://classcub.com/provider/the-artists-collective-hartford-ct",
  "blurb":"Hartford's landmark arts school for young people: dance, music, drama and visual arts, including Saturday School classes.","ages":"6–17","where":"1200 Albany Ave"},
 {"id":"wilson-gray-y","c":"move","n":"Wilson-Gray YMCA Youth & Family Center","u":"https://www.ghymca.org/wilsongray",
  "blurb":"Youth basketball and martial arts, the free Hartford Girls Sports Club, preschool and after-school programs.","ages":"Kids and teens","where":"444 Albany Ave"},
]
PLACES["rain"]=[p for p in PLACES["rain"] if p[0]!="Wadsworth Atheneum Museum of Art"]
PLACES["rain"].insert(1,("Wadsworth Atheneum Museum of Art","America's oldest public art museum. Second Saturdays bring free admission, family tours and art-making; open Wednesday–Sunday.","El museo de arte público más antiguo de Estados Unidos. Los segundos sábados de cada mes hay entrada gratis, recorridos familiares y actividades de arte; abre de miércoles a domingo."))
PLACES["rain"]+=[("Connecticut's Old State House","The 1796 statehouse downtown, with history exhibits for families. Open Tuesday–Saturday, 12–5.","El capitolio de 1796 en el centro, con exposiciones de historia para familias. Abre de martes a sábado, de 12 a 5."),
                 ("The Jumping Frog","A big used bookstore with a children's section (56 Arbor St).","Una gran librería de libros usados con sección infantil (56 Arbor St).")]
ES.update({
 "Families":"Familias",
 "Free admission all day":"Entrada gratis todo el día",
 "Free museum admission all day, glow-in-the-dark charm bracelets and other autumn crafts, and a magic show by Mr. B. The Hartford Marathon is the same day, so expect downtown road closures.":"Entrada gratis al museo todo el día, pulseras de dijes que brillan en la oscuridad y otras manualidades de otoño, y un show de magia de Mr. B. El mismo día es el Maratón de Hartford, así que habrá calles cerradas en el centro.",
 "Help build a community ofrenda, make incense cones and decorate sugar-skull masks, with ballet folklórico and live mariachi. Registration encouraged. A free sensory-friendly short-film program for ages 8 and up follows at 2 pm.":"Ayuda a armar una ofrenda comunitaria, haz conos de incienso y decora máscaras de calavera, con ballet folklórico y mariachi en vivo. Se recomienda inscribirse. A las 2 pm sigue un programa gratis de cortometrajes adaptado a necesidades sensoriales para mayores de 8 años.",
 "Free admission, an 11 am family tour, flower-bouquet design and hand puppets with the East Lyme Puppetry Project, free popcorn, and New York International Children's Film Festival shorts for little kids and big kids (11–3, the 11 and 12 o'clock shows sensory-friendly).":"Entrada gratis, un recorrido familiar a las 11 am, diseño de ramos de flores y títeres de mano con el East Lyme Puppetry Project, palomitas gratis y cortometrajes del New York International Children's Film Festival para niños pequeños y grandes (de 11 a 3; las funciones de las 11 y las 12 están adaptadas a necesidades sensoriales).",
 "A Hanukkah evening with an outdoor menorah lighting and family-friendly crafts.":"Una tarde de Janucá con encendido de la menorá al aire libre y manualidades para toda la familia.",
 "Grades 4–9":"4.º a 9.º grado",
 "$14":"$14",
 "A hip-hop biography show from the Bushnell Children's Theatre series. These are school-day shows, but the public can buy tickets from the box office (860-987-5900). The Friday 10 am show is sold out.":"Un espectáculo biográfico de hip-hop de la serie Bushnell Children's Theatre. Son funciones en horario escolar, pero el público puede comprar boletos en la taquilla (860-987-5900). La función del viernes a las 10 am está agotada.",
 "Pre-K–grade 3":"Prekínder a 3.er grado",
 "The groovy cat's picture books on stage, in the Bushnell Children's Theatre series. The 10 am show is sold out; buy noon tickets from the box office (860-987-5900).":"Los libros del gato más 'groovy' en el escenario, en la serie Bushnell Children's Theatre. La función de las 10 am está agotada; compra boletos para el mediodía en la taquilla (860-987-5900).",
 "Tickets vary":"Precios variables",
 "Cirque acrobats, aerialists and holiday music in a show built for family audiences.":"Acróbatas de circo, artistas aéreos y música navideña en un espectáculo pensado para toda la familia.",
 "The Nutmeg Ballet Conservatory's Nutcracker at the Bushnell. Showtimes are on the Bushnell's site.":"El Cascanueces del Nutmeg Ballet Conservatory en el Bushnell. Los horarios están en el sitio del Bushnell.",
 "Connecticut Ballet with guest stars from New York City Ballet and American Ballet Theatre, and the Hartford Symphony playing live.":"Connecticut Ballet con estrellas invitadas del New York City Ballet y el American Ballet Theatre, y la Hartford Symphony tocando en vivo.",
 "A free trunk-or-treat with a DJ, double-dutch, crafts, prizes and a costume parade, usually the Friday before Halloween, 4–6 pm. This year's date isn't posted yet.":"Un trunk-or-treat gratis con DJ, doble cuerda, manualidades, premios y desfile de disfraces, normalmente el viernes antes de Halloween, de 4 a 6 pm. La fecha de este año aún no se ha publicado.",
 "Urban League of Greater Hartford, 140 Woodland St":"Urban League of Greater Hartford, 140 Woodland St",
 "The mayor lights the city's tree in Bushnell Park, with caroling, hot chocolate and free skating at Winterfest. The last two were on the Sunday after Thanksgiving at 4:30. This year's date isn't posted yet.":"El alcalde enciende el árbol de la ciudad en Bushnell Park, con villancicos, chocolate caliente y patinaje gratis en Winterfest. Los dos últimos fueron el domingo después de Acción de Gracias a las 4:30. La fecha de este año aún no se ha publicado.",
 "Bushnell Park, downtown":"Bushnell Park, en el centro",
 "Free outdoor skating, free skate rentals and lessons, Santa photos and themed nights, daily 11–8 from Black Friday into January (closed when it rains). 2026 dates aren't posted yet.":"Patinaje gratis al aire libre, renta de patines y clases gratis, fotos con Santa y noches temáticas, todos los días de 11 a 8 desde el Black Friday hasta enero (cerrado cuando llueve). Las fechas de 2026 aún no se han publicado.",
 "Hartford's landmark arts school for young people: dance, music, drama and visual arts, including Saturday School classes.":"La emblemática escuela de artes para jóvenes de Hartford: danza, música, teatro y artes visuales, incluidas clases de Saturday School.",
 "6–17":"6–17 años",
 "Kids and teens":"Niños y adolescentes",
 "Youth basketball and martial arts, the free Hartford Girls Sports Club, preschool and after-school programs.":"Básquetbol y artes marciales para jóvenes, el Hartford Girls Sports Club gratis, preescolar y programas después de clases.",
 "Downtown":"Centro",
})

# ---- gap check (Oct 7) ----
PLACES["out"]+=[("City splash pads","Free summer splash pads at Colt Park, Keney Park, Hyland Park, Pope Park North and Goodwin Park.","Zonas de chorros de agua gratis en verano en Colt Park, Keney Park, Hyland Park, Pope Park North y Goodwin Park."),
 ("Winterfest skating at Bushnell Park","Free outdoor skating with free skate rentals and lessons from Black Friday into January (see the date card above).","Patinaje gratis al aire libre con renta de patines y clases gratis desde el Black Friday hasta enero (ver la tarjeta de fecha arriba).")]

# ---- creative places / bookstores / blogs pass (Oct 8) ----
PLACES["rain"]=[p if p[0]!="The Jumping Frog" else ("The Jumping Frog","A rare and used bookstore known for Mark Twain first editions (56 Arbor St). Open by appointment, so call first.","Una librería de libros raros y usados conocida por sus primeras ediciones de Mark Twain (56 Arbor St). Abre con cita, así que llama antes.") for p in PLACES["rain"]]
TOWN["events"]=[dict(e,blurb="Hartford Stage's annual staging of Dickens, Nov 21–Dec 27. A sensory-friendly matinee is Dec 5 at 2pm (open-captioned Dec 6, audio-described Dec 12). Some scenes are scary for little ones.") if e["t"]=="A Christmas Carol" else e for e in TOWN["events"]]
TOWN["classes"]+=[
 {"id":"makerspacect","c":"build","n":"MakerspaceCT","u":"https://classcub.com/provider/makerspacect-hartford-ct",
  "blurb":"A big community makerspace downtown with intro courses (woodworking, CNC, welding) and combat-robotics meetups; free summer STEAM program for teens. Check for youth classes.","ages":"7–17 years","where":"36 Talcott St"},
]
PLACES["drive"]+=[("Barnes & Noble, Blue Back Square","The nearest big bookstore, with a children's section (65 Memorial Rd, West Hartford).","La librería grande más cercana, con sección infantil (65 Memorial Rd, West Hartford).")]
ES.update({
 "Hartford Stage's annual staging of Dickens, Nov 21–Dec 27. A sensory-friendly matinee is Dec 5 at 2pm (open-captioned Dec 6, audio-described Dec 12). Some scenes are scary for little ones.":"La puesta anual de Dickens de Hartford Stage, del 21 de nov. al 27 de dic. Hay una función adaptada sensorialmente el 5 de dic. a las 2 p. m. (con subtítulos el 6 de dic. y con audiodescripción el 12 de dic.). Algunas escenas dan miedo a los más pequeños.",
 "A big community makerspace downtown with intro courses (woodworking, CNC, welding) and combat-robotics meetups; free summer STEAM program for teens. Check for youth classes.":"Un gran makerspace comunitario en el centro con cursos introductorios (carpintería, CNC, soldadura) y encuentros de robótica de combate; programa STEAM gratis en verano para adolescentes. Consulta las clases para jóvenes.",
 "7–17 years":"7–17 años",
})

# ---- patch: hartford-2026-10-08b.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
# Out and About Mom blog leads (owner request Oct 8)
ADD_PLACES["out"]+=[("Goodwin Park","A big city park in the South End with an accessible 'boundless' playground (1192 Maple Ave).","Un gran parque de la ciudad en el South End con un parque infantil accesible 'boundless' (1192 Maple Ave).")]
ADD_PLACES["rain"]+=[("Connecticut Museum of Culture and History","The former Connecticut Historical Society, with hands-on history exhibits for families (1 Elizabeth St).","La antigua Connecticut Historical Society, con exposiciones de historia interactivas para familias (1 Elizabeth St).")]

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
