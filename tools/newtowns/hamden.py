W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
SRC="https://hamdenlibrary.libcal.com/calendar/programs/"
B=["baby","toddler","preschool"]
MI,BR,WV="hamden-miller","hamden-brundage","hamden-whitneyville"
def ev(v,**k):
    e={"v":v,"free":True,"price":"Free","src":SRC}; e.update(k); return e
TOWN={
 "display":"Hamden","accent":"#E8D2C2",
 "venues":{MI:["Miller Memorial Library","2901 Dixwell Ave"],
           BR:["Brundage Community Branch Library","91 Circular Ave"],
           WV:["Whitneyville Branch Library","125 Carleton St"]},
 "venueMeta":{MI:[None,1],BR:[None,1],WV:[None,1]},
 "events":[
  ev(MI,t="Wonderful Ones Storytime",when=D(["2026-10-19","2026-10-26","2026-11-02","2026-11-09","2026-11-16","2026-12-07","2026-12-14"],[["10:15","11:00"]]),ages="Ages 12–24 months + caregiver",a=["toddler"],rsvp=True,
     blurb="Books, rhymes and music for one-year-olds. Registration recommended; each session opens two weeks ahead and space is limited."),
  ev(MI,t="Time for Twos Storytime",when=D(["2026-10-20","2026-10-27","2026-11-03","2026-11-10","2026-11-17","2026-12-08","2026-12-15"],[["10:15","11:00"]]),ages="Two-year-olds + caregiver",a=["toddler"],rsvp=True,
     blurb="Stories, rhymes, music and play for two-year-olds. Registration recommended; each session opens two weeks ahead and space is limited."),
  ev(MI,t="Preschool Storytime",when=D(["2026-10-08","2026-10-22","2026-10-29","2026-11-05","2026-11-12","2026-11-19","2026-12-03","2026-12-10","2026-12-17"],[["10:45","11:30"]]),ages="Ages 3–5 (younger siblings welcome)",a=["preschool"],drop=True,
     blurb="Stories, projects and activities with Miss Kacie in the Friends Room. Registration appreciated but not required."),
  ev(WV,t="Stay and Play: Fall Edition",when=D(["2026-10-14","2026-11-18"],[["10:30","11:30"]]),ages="Up to age 5 + caregiver",a=B,rsvp=True,
     blurb="Stories, songs and movement, then free play. The Whitneyville meeting room is downstairs (stairs only). Registration recommended."),
  ev(MI,t="Kidding Around Yoga: Un-Spooky Halloween",special="hw",when=[W("2026-10-15",[["10:30","11:30"]])],ages="Preschool and school age + caregiver",a=["preschool","big"],rsvp=True,
     blurb="A not-scary Halloween yoga class for kids and their grown-ups. Registration recommended."),
  ev(BR,t="Fire Safety Storytime",when=[W("2026-10-19",[["11:00","11:45"]])],ages="Preschool and school age",a=["preschool","big"],rsvp=True,
     blurb="A fire-safety storytime at the Brundage Branch. Registration recommended."),
  ev(BR,t="Tween Crafternoon: Spooky Charms",special="hw",when=[W("2026-10-13",[["15:45","16:45"]])],ages="Grades 4–6",a=["big"],rsvp=True,
     blurb="Make spooky charms. Only 12 spots; registration recommended."),
  ev(BR,t="Little Makers: Squishy Pumpkins",when=[W("2026-10-26",[["11:00","11:45"]])],ages="Ages 4 and up (adult help needed)",a=["preschool","big"],rsvp=True,
     blurb="Make a soft pumpkin from stuffing and yarn. Registration recommended."),
  ev(MI,t="Trick or Treat at the Library",special="hw",when=[W("2026-10-31",[["14:30","16:00"]])],ages="Preschool and school age",a=["preschool","big"],drop=True,
     blurb="Creepy crafts and trick-or-treating through the library in costume. No registration."),
 ],
 "tba":[{"g":"hol","t":"Silverbells Tree Lighting","w":"Town Center Park, Dixwell Ave (next to Miller Library)",
   "p":"Hamden's Silverbells celebration: holiday music, cocoa, carols and Santa arriving by fire truck, usually on a weekday evening in early to mid-December, with registration-only cookie and gingerbread workshops later that week. This year's date isn't posted yet.","src":"https://hamdenlibrary.org/?p=23334"}],
 "classes":[],
 "library":{"for":"Free, every week","name":"Hamden Public Library","desc":"Storytimes for ones (Mondays), twos (Tuesdays) and preschoolers (Thursdays) at Miller Memorial Library, plus a monthly Stay and Play at Whitneyville and seasonal crafts at Brundage. Toddler storytimes fill, so register two weeks ahead.","a":"See the library's calendar","href":SRC},
}
PLACES={
 "out":[("Sleeping Giant State Park","Hiking trails up the 'giant,' including the wide Tower Trail to a stone lookout tower.","Senderos para subir al 'gigante', incluido el amplio Tower Trail hasta una torre mirador de piedra."),
        ("Brooksvale Park","A town park with farm animals, a playground, trails and seasonal maple sugaring.","Un parque del pueblo con animales de granja, área de juegos, senderos y elaboración de jarabe de arce en temporada."),
        ("Farmington Canal Heritage Trail","A flat paved trail through Hamden, good for bikes and strollers.","Un sendero plano y pavimentado que atraviesa Hamden, ideal para bicicletas y carriolas."),
        ("Hindinger Farm","A family farm with a pumpkin patch, play area and farm stand in the fall.","Una granja familiar con campo de calabazas, área de juegos y puesto de productos en otoño.")],
 "rain":[("Eli Whitney Museum & Workshop","A hands-on museum of invention with build-it workshops for kids (915 Whitney Ave); check open hours.","Un museo interactivo de inventos con talleres de construcción para niños (915 Whitney Ave); consulta el horario."),
         ("Miller Memorial Library","Hamden's main library, home to storytimes for ones, twos and preschoolers.","La biblioteca principal de Hamden, con cuentacuentos para niños de uno, dos años y preescolares.")],
 "drive":[("Yale Peabody Museum","Dinosaurs, minerals and natural history, free, in New Haven.","Dinosaurios, minerales e historia natural, gratis, en New Haven."),
          ("Lighthouse Point Park","A beach, an 1840s lighthouse and a historic carousel in New Haven.","Una playa, un faro de 1840 y un carrusel histórico en New Haven."),
          ("Connecticut's Beardsley Zoo","Connecticut's only zoo, in Bridgeport.","El único zoológico de Connecticut, en Bridgeport.")],
}
ES={
 "Ages 12–24 months + caregiver":"12–24 meses + un adulto",
 "Books, rhymes and music for one-year-olds. Registration recommended; each session opens two weeks ahead and space is limited.":"Libros, rimas y música para niños de un año. Se recomienda inscribirse; cada sesión se abre dos semanas antes y el cupo es limitado.",
 "Two-year-olds + caregiver":"Niños de dos años + un adulto",
 "Stories, rhymes, music and play for two-year-olds. Registration recommended; each session opens two weeks ahead and space is limited.":"Cuentos, rimas, música y juego para niños de dos años. Se recomienda inscribirse; cada sesión se abre dos semanas antes y el cupo es limitado.",
 "Ages 3–5 (younger siblings welcome)":"3–5 años (hermanos menores bienvenidos)",
 "Stories, projects and activities with Miss Kacie in the Friends Room. Registration appreciated but not required.":"Cuentos, proyectos y actividades con Miss Kacie en el Friends Room. Se agradece la inscripción, pero no es obligatoria.",
 "Up to age 5 + caregiver":"Hasta 5 años + un adulto",
 "Stories, songs and movement, then free play. The Whitneyville meeting room is downstairs (stairs only). Registration recommended.":"Cuentos, canciones y movimiento, y luego juego libre. La sala de Whitneyville está en el piso de abajo (solo escaleras). Se recomienda inscribirse.",
 "Preschool and school age + caregiver":"Preescolares y escolares + un adulto",
 "A not-scary Halloween yoga class for kids and their grown-ups. Registration recommended.":"Una clase de yoga de Halloween que no da miedo para niños y sus adultos. Se recomienda inscribirse.",
 "Preschool and school age":"Preescolares y escolares",
 "A fire-safety storytime at the Brundage Branch. Registration recommended.":"Un cuentacuentos sobre seguridad contra incendios en la sucursal Brundage. Se recomienda inscribirse.",
 "Grades 4–6":"4.º a 6.º grado",
 "Make spooky charms. Only 12 spots; registration recommended.":"Haz dijes de miedo. Solo 12 lugares; se recomienda inscribirse.",
 "Ages 4 and up (adult help needed)":"Desde 4 años (con ayuda de un adulto)",
 "Make a soft pumpkin from stuffing and yarn. Registration recommended.":"Haz una calabaza suave con relleno y estambre. Se recomienda inscribirse.",
 "Creepy crafts and trick-or-treating through the library in costume. No registration.":"Manualidades de miedo y pedir dulces por la biblioteca disfrazados. Sin inscripción.",
 "Hamden's Silverbells celebration: holiday music, cocoa, carols and Santa arriving by fire truck, usually on a weekday evening in early to mid-December, with registration-only cookie and gingerbread workshops later that week. This year's date isn't posted yet.":"La celebración Silverbells de Hamden: música navideña, chocolate caliente, villancicos y Santa llegando en camión de bomberos, normalmente una tarde entre semana a principios o mediados de diciembre, con talleres de galletas y casitas de jengibre (con inscripción) más tarde esa semana. La fecha de este año aún no se ha publicado.",
 "Town Center Park, Dixwell Ave (next to Miller Library)":"Town Center Park, Dixwell Ave (next to Miller Library)",
 "Storytimes for ones (Mondays), twos (Tuesdays) and preschoolers (Thursdays) at Miller Memorial Library, plus a monthly Stay and Play at Whitneyville and seasonal crafts at Brundage. Toddler storytimes fill, so register two weeks ahead.":"Cuentacuentos para niños de un año (lunes), dos años (martes) y preescolares (jueves) en la Miller Memorial Library, además de un Stay and Play mensual en Whitneyville y manualidades de temporada en Brundage. Los cuentacuentos para niños pequeños se llenan, así que inscríbete dos semanas antes.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7) ----
TW="thornton-wilder"; SG="sleeping-giant"
TOWN["venues"].update({TW:["Thornton Wilder Hall, Miller Memorial Cultural Center","2901 Dixwell Ave"],SG:["Sleeping Giant State Park, East Parking","400 Chestnut Ln"]})
TOWN["venueMeta"].update({TW:[None,1],SG:[None,0]})
TOWN["events"]+=[
 {"t":"All Ability Halloween Dance","v":TW,"special":"hw","when":[W("2026-10-16",[["18:30","20:30"]])],"ages":"All ages and abilities","a":["preschool","big"],"free":False,"price":"$5","rsvp":True,"src":"https://hamdenct.myrec.com/info/activities/program_details.aspx?ProgramID=29873",
  "blurb":"Hamden Recreation's inclusive Halloween dance for people of every ability. Register online through Hamden Recreation."},
 {"t":"Geology Hike at Sleeping Giant","v":SG,"when":[W("2026-10-10",[["13:00","15:00"]])],"ages":"Older kids and up (rocky trails)","a":["big"],"free":True,"price":"Free","rsvp":True,"check":True,"src":"https://sgpa.org/program-calendar/",
  "blurb":"A free Sleeping Giant Park Association hike about the park's rocks and how the 'giant' formed. Trails can be uneven; no dogs. SGPA asks hikers to register."},
]
TOWN["tba"]+=[{"g":"hw","t":"Hamden trunk-or-treats","w":"Around Hamden",
  "p":"Most years Hamden has several free trunk-or-treats on late-October Saturdays, including the YMCA's Trunk-or-Treat & Fall Festival at Camp Mountain Laurel (registration required), the Hamden Elks Lodge (175 School St) and Quinnipiac's Boomer's Boo Bash. This year's dates aren't posted yet.","src":"https://thisweekinhamden.substack.com/p/special-edition-halloween-in-hamden-e3a"}]
TOWN["classes"]+=[
 {"id":"new-era-gym","c":"move","n":"New Era Gymnastics","u":"https://www.neweragymnastics.com",
  "blurb":"Co-ed preschool gymnastics, separate boys' and girls' programs, tumbling and ninja classes.","ages":"Preschool–teens","where":"1180 Sherman Ave"},
 {"id":"hamden-rec-swim","c":"swim","n":"Hamden Recreation Swim Lessons","u":"https://hamdenct.myrec.com/info/activities/program_details.aspx?ProgramID=29874",
  "blurb":"Six-week evening swim lessons at the Laura Luzzi Aquatic Center ($80 residents). The fall sessions are full; watch for winter registration.","ages":"Levels 1–2, plus ages 10–16","where":"Hamden High School pool"},
]
PLACES["rain"]=[p for p in PLACES["rain"] if p[0]!="Eli Whitney Museum & Workshop"]
PLACES["rain"].insert(0,("Eli Whitney Museum & Workshop","A hands-on museum of invention where kids build projects to take home. Walk-in visits Saturdays and Sundays 10–3, plus day-long workshops on school vacation days (ages 6–11) (915 Whitney Ave).","Un museo interactivo de inventos donde los niños construyen proyectos para llevar a casa. Visitas sin cita sábados y domingos de 10 a 3, y talleres de día completo en vacaciones escolares (6–11 años) (915 Whitney Ave)."))
PLACES["rain"].append(("Louis Astorino Ice Arena","The town rink at Hamden High School, with public skating and learn-to-skate programs (595 Mix Ave); check the rink's schedule.","La pista municipal en Hamden High School, con patinaje público y clases para aprender a patinar (595 Mix Ave); consulta el horario."))
PLACES["out"]=[p for p in PLACES["out"] if p[0]!="Hindinger Farm"]
PLACES["out"].append(("Hindinger Farm","A family farm stand known for corn and peaches, open May through December, closed Mondays (835 Dunbar Hill Rd).","Un puesto de granja familiar conocido por su maíz y duraznos, abierto de mayo a diciembre, cerrado los lunes (835 Dunbar Hill Rd)."))
TOWN["extraResources"]=[{"for":"Free, ages 0–5","name":"Hamden Family Resource Center","desc":"Free Play and Learn groups for children from birth to 5 and their parents, plus Circle of Security parenting classes, at Church Street School and Ridge Hill School.","a":"Call 203-407-3111","href":"https://www.hamden.org/family-resource-center-frc"}]
ES.update({
 "All ages and abilities":"Todas las edades y capacidades",
 "$5":"$5",
 "Hamden Recreation's inclusive Halloween dance for people of every ability. Register online through Hamden Recreation.":"El baile inclusivo de Halloween de Hamden Recreation para personas de todas las capacidades. Inscríbete en línea con Hamden Recreation.",
 "Older kids and up (rocky trails)":"Niños mayores en adelante (senderos rocosos)",
 "A free Sleeping Giant Park Association hike about the park's rocks and how the 'giant' formed. Trails can be uneven; no dogs. SGPA asks hikers to register.":"Una caminata gratis de la Sleeping Giant Park Association sobre las rocas del parque y cómo se formó el 'gigante'. Los senderos pueden ser irregulares; sin perros. SGPA pide inscribirse.",
 "Around Hamden":"En distintos lugares de Hamden",
 "Most years Hamden has several free trunk-or-treats on late-October Saturdays, including the YMCA's Trunk-or-Treat & Fall Festival at Camp Mountain Laurel (registration required), the Hamden Elks Lodge (175 School St) and Quinnipiac's Boomer's Boo Bash. This year's dates aren't posted yet.":"Casi todos los años Hamden tiene varios trunk-or-treats gratis los sábados de finales de octubre, como el Trunk-or-Treat & Fall Festival del YMCA en Camp Mountain Laurel (con inscripción), el Hamden Elks Lodge (175 School St) y el Boomer's Boo Bash de Quinnipiac. Las fechas de este año aún no se han publicado.",
 "Co-ed preschool gymnastics, separate boys' and girls' programs, tumbling and ninja classes.":"Gimnasia preescolar mixta, programas separados para niños y niñas, acrobacia y clases de ninja.",
 "Preschool–teens":"Preescolar–adolescentes",
 "Six-week evening swim lessons at the Laura Luzzi Aquatic Center ($80 residents). The fall sessions are full; watch for winter registration.":"Clases de natación de seis semanas por la tarde en el Laura Luzzi Aquatic Center ($80 residentes). Las sesiones de otoño están llenas; atento a la inscripción de invierno.",
 "Levels 1–2, plus ages 10–16":"Niveles 1–2, y 10–16 años",
 "Hamden High School pool":"Alberca de Hamden High School",
 "Free, ages 0–5":"Gratis, 0–5 años",
 "Hamden Family Resource Center":"Hamden Family Resource Center",
 "Free Play and Learn groups for children from birth to 5 and their parents, plus Circle of Security parenting classes, at Church Street School and Ridge Hill School.":"Grupos gratis de Juega y Aprende para niños de 0 a 5 años y sus padres, además de clases de crianza Círculo de Seguridad, en Church Street School y Ridge Hill School.",
 "Call 203-407-3111":"Llama al 203-407-3111",
})

# ---- gap check (Oct 7) ----
PLACES["out"]+=[("Villano Park","A neighborhood park with a summer splash pad (260 Mill Rock Rd).","Un parque de barrio con zona de chorros de agua en verano (260 Mill Rock Rd).")]

# ---- creative places / bookstores / blogs pass (Oct 8) ----
QU="qu-mount-carmel"; EW="eli-whitney"
TOWN["venues"].update({QU:["Quinnipiac University, Mount Carmel Quad","275 Mount Carmel Ave"],EW:["Eli Whitney Museum & Workshop","915 Whitney Ave"]})
TOWN["venueMeta"].update({QU:[None,0],EW:[None,1]})
TOWN["events"]+=[
 {"t":"Boomer's Boo Bash","v":QU,"special":"hw","when":[W("2026-10-24",[["10:00","14:00"]])],"ages":"Kids and families","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://local.qu.edu/children-and-families/boomers-boo-bash/",
  "blurb":"Quinnipiac's free Halloween morning on the Mount Carmel quad: activities, prizes, giveaways and candy with Boomer the Bobcat and QU athletes. Rain moves it into the student center."},
]
TOWN["tba"]+=[{"g":"hol","t":"Holiday train display at the Eli Whitney Museum","w":"Eli Whitney Museum & Workshop, 915 Whitney Ave",
  "p":"The museum's A.C. Gilbert/American Flyer toy-train layout opens the day after Thanksgiving and runs into January, free. Last year it opened Nov 28. This year's dates aren't posted yet.","src":"https://cloud.eliwhitney.org/node/4146"}]
PLACES["rain"]+=[("Evan's Toy Shoppe","An independent toy store with toys, games and craft kits near the Eli Whitney Museum (1647 Whitney Ave); call to check hours.","Una juguetería independiente con juguetes, juegos y kits de manualidades cerca del Eli Whitney Museum (1647 Whitney Ave); llama para confirmar el horario."),
                 ("Friends' Second Hand Bookstore","The used-book shop in the basement of Miller Library, with cheap kids' books; open six days a week (2901 Dixwell Ave).","La tienda de libros usados en el sótano de la Miller Library, con libros infantiles baratos; abre seis días a la semana (2901 Dixwell Ave).")]
ES.update({
 "Kids and families":"Niños y familias",
 "Quinnipiac's free Halloween morning on the Mount Carmel quad: activities, prizes, giveaways and candy with Boomer the Bobcat and QU athletes. Rain moves it into the student center.":"La mañana de Halloween gratis de Quinnipiac en el patio de Mount Carmel: actividades, premios, regalos y dulces con Boomer the Bobcat y atletas de QU. Si llueve, se hace en el centro estudiantil.",
 "Eli Whitney Museum & Workshop, 915 Whitney Ave":"Eli Whitney Museum & Workshop, 915 Whitney Ave",
 "The museum's A.C. Gilbert/American Flyer toy-train layout opens the day after Thanksgiving and runs into January, free. Last year it opened Nov 28. This year's dates aren't posted yet.":"La maqueta de trenes de juguete A.C. Gilbert/American Flyer del museo abre el día después de Acción de Gracias y sigue hasta enero, gratis. El año pasado abrió el 28 de nov. Las fechas de este año aún no se han publicado.",
})

# ---- patch: hamden-2026-10-08b.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
# Owner request Oct 8: add Josh's Jungle (source: outandaboutmom.com, May 2015 post)
ADD_PLACES["out"].insert(0,("Josh's Jungle (Town Center Park)","A fully fenced, accessible playground with a soft rubber surface, ramps throughout, lots of slides and climbers, and shady picnic tables; great for toddlers. Free, with a big parking lot (2761 Dixwell Ave, next to Miller Library).","Un parque infantil totalmente cercado y accesible, con superficie de goma suave, rampas por todas partes, muchos toboganes y juegos para trepar, y mesas de picnic con sombra; ideal para los más pequeños. Gratis, con un gran estacionamiento (2761 Dixwell Ave, junto a la Miller Library)."))

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
