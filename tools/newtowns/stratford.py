W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
L="stratford-library"; SRC="https://stratfordlibrary.libcal.com/calendar/events"
B=["baby","toddler","preschool"]
def ev(**k):
    e={"v":L,"free":True,"price":"Free","src":SRC}; e.update(k); return e
T1=[["10:30","11:00"]]
CS="https://www.townofstratford.com/article/2802050"
TOWN={
 "display":"Stratford","accent":"#F6CFA8",
 "venues":{L:["Stratford Library","2203 Main St"],
           "boothe-park":["Boothe Memorial Park","5800 Main St"],
           "town-hall-green":["Stratford Town Hall Green","2725 Main St"]},
 "venueMeta":{L:[None,1],"boothe-park":[None,0],"town-hall-green":[None,0]},
 "events":[
  ev(t="Toddler Time",s=[[1,T1,"2026-10-12","2026-11-23"]],x=["2026-10-26"],ages="Ages 1–2 + caregiver",a=["toddler"],drop=True,
     blurb="Rhymes, songs and stories that build early literacy, in the Children's Program Room. No registration; just drop in. The posted series runs through Nov 23."),
  ev(t="Baby Lapsit",s=[[2,T1,"2026-10-13","2026-12-01"]],x=["2026-10-27","2026-11-24"],ages="Babies (0–18 months) + caregiver",a=["baby"],drop=True,
     blurb="Rhymes, songs, bounces, books and sharing time for babies still in the lap-sitting stage. No registration needed (sign up only if you want reminders)."),
  ev(t="Preschool Storytime",s=[[4,T1,"2026-10-08","2026-12-03"]],x=["2026-10-29","2026-11-26"],ages="Ages 3–5",a=["preschool"],drop=True,
     blurb="Stories, rhymes and a craft for preschoolers. No registration; just drop in. No storytime on Thanksgiving."),
  ev(t="Friday Fun",s=[[5,T1,"2026-10-09","2026-12-04"]],x=["2026-10-30","2026-11-27"],ages="Ages 1–5",a=["toddler","preschool"],drop=True,
     blurb="An end-of-week storytime with books, songs and a take-home craft. No registration; just drop in."),
  ev(t="Trick-or-Treat Storytimes",special="hw",when=D(["2026-10-26","2026-10-27","2026-10-29","2026-10-30"],T1),ages="Babies to age 5",a=B,drop=True,
     blurb="Halloween week, each regular storytime goes trick-or-treating: Toddler Time (Mon Oct 26), Baby Lapsit (Tue Oct 27), Preschool Storytime (Thu Oct 29) and Friday Fun (Fri Oct 30). Costumes welcome."),
  ev(t="Homework Helpers (Grades K–5)",s=[[1,[["16:00","19:00"]],"2026-10-12","2026-12-07"],[2,[["16:00","19:00"]],"2026-10-13","2026-12-08"],[3,[["16:00","17:00"]],"2026-10-14","2026-12-02"],[4,[["18:00","19:00"]],"2026-10-22","2026-12-03"]],
     x=["2026-11-03","2026-11-11","2026-11-25","2026-11-26"],ages="Grades K–5",a=["big"],rsvp=True,
     blurb="Free one-hour homework help in the Children's Department. Sign up for one spot a week; each slot opens for sign-up two weeks ahead and fills fast."),
  ev(t="Homeschool Hangout",when=D(["2026-10-08","2026-11-19"],[["14:00","15:00"]]),ages="Ages 5–12 (homeschool families)",a=["big"],rsvp=True,
     blurb="A meet-up for homeschooled kids and their families. Registration suggested; drop-ins welcome."),
  ev(t="Treehouse Science",when=D(["2026-10-09","2026-11-20"],[["15:30","16:30"]]),ages="Ages 8–12",a=["big"],drop=True,check=True,
     blurb="Hands-on STEAM at the Treehouse table: Snap Circuits (Oct 9) and loom weaving (Nov 20). Spots are limited."),
  ev(t="Sensory Play",when=[W("2026-10-10",[["11:00","12:00"]])],ages="Young children + caregiver",a=["toddler","preschool"],rsvp=True,
     blurb="Hands-on sensory play stations for little ones. Registration required."),
  ev(t="Fall Art",when=D(["2026-10-14","2026-11-18"],[["18:00","19:00"]]),ages="Ages 7–12",a=["big"],rsvp=True,
     blurb="An evening art class: a Halloween village (Oct 14, waitlist only) and a 3-D turkey (Nov 18). Registration required."),
  ev(t="Stop by for Science: Spooky Spiderwebs",special="hw",when=[W("2026-10-20",[["17:30","19:00"]])],ages="Ages 7–12",a=["big"],drop=True,
     blurb="A self-paced, drop-in science activity about spiderwebs."),
  ev(t="Kids Lego Robotics Club",when=[W("2026-10-22",[["14:00","15:00"]]),W("2026-11-12",[["16:00","17:00"]])],ages="Ages 7–12",a=["big"],rsvp=True,
     blurb="Build and code with LEGO Spike kits, funded by a Rotary grant. Registration required."),
  ev(t="Kids Cooking Class",when=[W("2026-10-22",[["15:30","16:30"]])],ages="Ages 8–12",a=["big"],rsvp=True,
     blurb="A hands-on cooking class for kids. Common food allergens are present. Registration required."),
  ev(t="Kids Lego Club",when=[W("2026-10-24",[["11:00","12:00"]])],ages="Ages 5–12",a=["big"],rsvp=True,
     blurb="Build with the library's LEGO collection. Registration required."),
  ev(t="Nutmeg Book Club",when=[W("2026-10-26",[["18:00","19:00"]])],ages="Grades 4–6",a=["big"],rsvp=True,
     blurb="A book club for this year's Nutmeg Award nominees. October's book is Queen of Ocean Parkway. Registration required."),
  ev(t="Crocheting for Kids",when=D(["2026-10-28","2026-11-04"],[["18:00","19:00"]]),ages="Ages 9 and up",a=["big"],rsvp=True,
     blurb="Learn beginner crochet stitches; materials provided. Teens and adults welcome too. Registration required (Oct 28 is waitlist only)."),
  ev(t="Sewing for Kids: Bookmarks",when=[W("2026-11-01",[["14:00","15:00"]])],ages="Ages 7–12",a=["big"],rsvp=True,
     blurb="Sew a fabric bookmark. Only six spots; registration required."),
  ev(t="LEGO Group Build",when=[W("2026-11-03",[["14:00","16:00"]])],ages="Kids of all ages",a=["preschool","big"],drop=True,
     blurb="Spend the Election Day school holiday helping build two Harry Potter LEGO sets. Drop in."),
  ev(t="Little Artists",when=[W("2026-11-21",[["11:00","12:00"]])],ages="Ages 3–7",a=["preschool","big"],rsvp=True,
     blurb="Process art for young artists: it's about exploring materials, not the finished product. Registration required."),
  {"t":"Great Pumpkin Festival","v":"boothe-park","special":"fall","when":[W("2026-10-17",[["12:00","16:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free admission","drop":True,"check":True,"src":CS,
   "blurb":"Stratford's annual fall festival at Boothe Memorial Park, with pumpkin carving, a kids' costume parade and contest, hayrides, face painting and performances. Rain date Oct 18. Times are from past years; check closer to the day."},
  {"t":"Holiday Market & Tree Lighting","v":"town-hall-green","special":"hol","when":[W("2026-11-27",[["14:00","17:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":CS,
   "blurb":"Photos with Santa and Mrs. Claus, free kids' activities like cookie decorating, ornament making and letters to Santa, a holiday market, and the tree lighting at dusk. Times are from last year's schedule (Santa 2–5, lighting 5:30)."},
 ],
 "tba":[{"g":"hol","t":"Stratford Menorah Lighting","w":"Stratford (location to be announced)",
   "p":"Stratford's community menorah lighting is set for Wednesday, Dec 9. The time and place aren't posted yet.","src":CS}],
 "classes":[
  {"id":"little-gym-stratford","c":"move","n":"The Little Gym of Stratford","u":"https://www.thelittlegym.com/connecticut-stratford/",
   "blurb":"Parent-and-child classes, preschool and grade-school gymnastics, and dance, plus camps and Parents' Survival Nights.",
   "ages":"4 months–12 years","where":"475 Hawley Ln"},
 ],
 "library":{"for":"Free, every week","name":"Stratford Library","desc":"Drop-in storytimes four mornings a week (Toddler Time, Baby Lapsit, Preschool Storytime and Friday Fun), free K–5 homework help, LEGO and robotics clubs, art and sewing classes, and free take-home craft and science kits.","a":"See the library's calendar","href":SRC},
}
PLACES={
 "out":[("Boothe Memorial Park","Free and open year-round: gardens, walking paths and a cluster of quirky historic buildings, plus a playground. The museum buildings open on summer weekends.","Gratis y abierto todo el año: jardines, senderos y un conjunto de curiosos edificios históricos, además de un área de juegos. Los museos abren los fines de semana de verano."),
        ("Short Beach Park","A town beach on Long Island Sound with a playground and picnic areas.","Una playa del pueblo en el estrecho de Long Island con área de juegos y zonas de picnic."),
        ("Longbrook Park","A neighborhood park with a splash pad for hot summer days (103 Glendale Rd).","Un parque de barrio con una zona de chorros de agua para los días calurosos de verano (103 Glendale Rd)."),
        ("Roosevelt Forest","Wooded trails and a pond in the north end of town, good for an easy family hike.","Senderos en el bosque y un estanque en el norte del pueblo, ideales para una caminata familiar sencilla.")],
 "rain":[("Stratford Library","A busy children's department with drop-in storytimes most weekday mornings, homework help and free take-home kits.","Un departamento infantil muy activo con cuentacuentos sin inscripción casi todas las mañanas entre semana, ayuda con las tareas y kits gratis para llevar a casa."),
         ("Connecticut Air & Space Museum","Vintage aircraft and aviation history near Sikorsky Airport. Open Saturdays and Sundays 10–4; $5 for kids over 6.","Aviones antiguos e historia de la aviación cerca del aeropuerto Sikorsky. Abre sábados y domingos de 10 a 4; $5 para niños mayores de 6 años."),
         ("National Helicopter Museum","A free little museum at the train station with a real Sikorsky cockpit and a flight simulator. Open Friday–Sunday afternoons from Memorial Day to mid-October.","Un pequeño museo gratis en la estación de tren con una cabina real de Sikorsky y un simulador de vuelo. Abre las tardes de viernes a domingo desde Memorial Day hasta mediados de octubre."),
         ("Ruby and Calvin Fletcher African American History Museum","A free museum of African American history (952 East Broadway). Open Monday, Wednesday, Thursday and Saturday, 10–5.","Un museo gratis de historia afroamericana (952 East Broadway). Abre lunes, miércoles, jueves y sábado, de 10 a 5.")],
 "drive":[("Connecticut's Beardsley Zoo","Connecticut's only zoo, with a rainforest building and a carousel, just over the line in Bridgeport.","El único zoológico de Connecticut, con un edificio de selva tropical y un carrusel, justo al cruzar a Bridgeport."),
          ("Discovery Museum","Hands-on science exhibits and a planetarium in Bridgeport.","Exposiciones de ciencia interactivas y un planetario en Bridgeport."),
          ("Connecticut Audubon Coastal Center","Beach, boardwalk and bird-watching at Milford Point, where the Housatonic meets the Sound.","Playa, pasarela y observación de aves en Milford Point, donde el Housatonic se une al estrecho.")],
}
ES={
 "Ages 1–2 + caregiver":"1–2 años + un adulto",
 "Rhymes, songs and stories that build early literacy, in the Children's Program Room. No registration; just drop in. The posted series runs through Nov 23.":"Rimas, canciones y cuentos que fomentan la lectura temprana, en la sala de programas infantiles. Sin inscripción; solo llega. La serie publicada llega hasta el 23 de nov.",
 "Babies (0–18 months) + caregiver":"Bebés (0–18 meses) + un adulto",
 "Rhymes, songs, bounces, books and sharing time for babies still in the lap-sitting stage. No registration needed (sign up only if you want reminders).":"Rimas, canciones, juegos de rebote, libros y tiempo para compartir para bebés que todavía se sientan en el regazo. No hace falta inscribirse (solo si quieres recordatorios).",
 "Ages 3–5":"3–5 años",
 "Stories, rhymes and a craft for preschoolers. No registration; just drop in. No storytime on Thanksgiving.":"Cuentos, rimas y una manualidad para preescolares. Sin inscripción; solo llega. No hay cuentacuentos el Día de Acción de Gracias.",
 "Ages 1–5":"1–5 años",
 "An end-of-week storytime with books, songs and a take-home craft. No registration; just drop in.":"Un cuentacuentos de fin de semana con libros, canciones y una manualidad para llevar a casa. Sin inscripción; solo llega.",
 "Babies to age 5":"Bebés hasta 5 años",
 "Halloween week, each regular storytime goes trick-or-treating: Toddler Time (Mon Oct 26), Baby Lapsit (Tue Oct 27), Preschool Storytime (Thu Oct 29) and Friday Fun (Fri Oct 30). Costumes welcome.":"En la semana de Halloween, cada cuentacuentos sale a pedir dulces: Toddler Time (lun. 26 de oct.), Baby Lapsit (mar. 27 de oct.), Preschool Storytime (jue. 29 de oct.) y Friday Fun (vie. 30 de oct.). Se pueden traer disfraces.",
 "Grades K–5":"Kínder a 5.º grado",
 "Free one-hour homework help in the Children's Department. Sign up for one spot a week; each slot opens for sign-up two weeks ahead and fills fast.":"Ayuda gratis con las tareas durante una hora en el departamento infantil. Inscríbete en un turno por semana; cada turno se abre dos semanas antes y se llena rápido.",
 "Ages 5–12 (homeschool families)":"5–12 años (familias que educan en casa)",
 "A meet-up for homeschooled kids and their families. Registration suggested; drop-ins welcome.":"Un encuentro para niños educados en casa y sus familias. Se sugiere inscribirse; también se puede llegar sin inscripción.",
 "Ages 8–12":"8–12 años",
 "Hands-on STEAM at the Treehouse table: Snap Circuits (Oct 9) and loom weaving (Nov 20). Spots are limited.":"Actividades STEAM en la mesa Treehouse: Snap Circuits (9 de oct.) y tejido en telar (20 de nov.). Cupo limitado.",
 "Young children + caregiver":"Niños pequeños + un adulto",
 "Hands-on sensory play stations for little ones. Registration required.":"Estaciones de juego sensorial para los más pequeños. Inscripción obligatoria.",
 "Ages 7–12":"7–12 años",
 "An evening art class: a Halloween village (Oct 14, waitlist only) and a 3-D turkey (Nov 18). Registration required.":"Una clase de arte por la tarde: un pueblo de Halloween (14 de oct., solo lista de espera) y un pavo en 3D (18 de nov.). Inscripción obligatoria.",
 "A self-paced, drop-in science activity about spiderwebs.":"Una actividad de ciencia sobre telarañas, sin inscripción y a tu propio ritmo.",
 "Build and code with LEGO Spike kits, funded by a Rotary grant. Registration required.":"Construye y programa con kits LEGO Spike, financiados por una beca del Rotary. Inscripción obligatoria.",
 "A hands-on cooking class for kids. Common food allergens are present. Registration required.":"Una clase práctica de cocina para niños. Habrá alérgenos alimentarios comunes. Inscripción obligatoria.",
 "Ages 5–12":"5–12 años",
 "Build with the library's LEGO collection. Registration required.":"Construye con la colección de LEGO de la biblioteca. Inscripción obligatoria.",
 "Grades 4–6":"4.º a 6.º grado",
 "A book club for this year's Nutmeg Award nominees. October's book is Queen of Ocean Parkway. Registration required.":"Un club de lectura de los libros nominados al premio Nutmeg de este año. El libro de octubre es Queen of Ocean Parkway. Inscripción obligatoria.",
 "Ages 9 and up":"Desde 9 años",
 "Learn beginner crochet stitches; materials provided. Teens and adults welcome too. Registration required (Oct 28 is waitlist only).":"Aprende puntos básicos de crochet; se dan los materiales. También pueden venir adolescentes y adultos. Inscripción obligatoria (el 28 de oct. solo hay lista de espera).",
 "Sew a fabric bookmark. Only six spots; registration required.":"Cose un separador de libros de tela. Solo seis lugares; inscripción obligatoria.",
 "Kids of all ages":"Niños de todas las edades",
 "Spend the Election Day school holiday helping build two Harry Potter LEGO sets. Drop in.":"Pasa el día sin clases de las elecciones ayudando a armar dos sets de LEGO de Harry Potter. Sin inscripción.",
 "Ages 3–7":"3–7 años",
 "Process art for young artists: it's about exploring materials, not the finished product. Registration required.":"Arte de proceso para artistas pequeños: se trata de explorar materiales, no del resultado final. Inscripción obligatoria.",
 "All ages":"Todas las edades",
 "Free admission":"Entrada gratis",
 "Stratford's annual fall festival at Boothe Memorial Park, with pumpkin carving, a kids' costume parade and contest, hayrides, face painting and performances. Rain date Oct 18. Times are from past years; check closer to the day.":"El festival anual de otoño de Stratford en Boothe Memorial Park, con tallado de calabazas, desfile y concurso de disfraces infantiles, paseos en carreta de heno, pintacaritas y presentaciones. Fecha alternativa por lluvia: 18 de oct. El horario es de años anteriores; confírmalo cerca de la fecha.",
 "Photos with Santa and Mrs. Claus, free kids' activities like cookie decorating, ornament making and letters to Santa, a holiday market, and the tree lighting at dusk. Times are from last year's schedule (Santa 2–5, lighting 5:30).":"Fotos con Santa y la Sra. Claus, actividades infantiles gratis como decorar galletas, hacer adornos y escribir cartas a Santa, un mercado navideño y el encendido del árbol al anochecer. El horario es el del año pasado (Santa de 2 a 5, encendido a las 5:30).",
 "Stratford's community menorah lighting is set for Wednesday, Dec 9. The time and place aren't posted yet.":"El encendido comunitario de la menorá de Stratford será el miércoles 9 de dic. La hora y el lugar aún no se han publicado.",
 "Stratford (location to be announced)":"Stratford (lugar por anunciar)",
 "Parent-and-child classes, preschool and grade-school gymnastics, and dance, plus camps and Parents' Survival Nights.":"Clases de padres e hijos, gimnasia para preescolares y escolares, y danza, además de campamentos y noches libres para padres.",
 "4 months–12 years":"4 meses–12 años",
 "Drop-in storytimes four mornings a week (Toddler Time, Baby Lapsit, Preschool Storytime and Friday Fun), free K–5 homework help, LEGO and robotics clubs, art and sewing classes, and free take-home craft and science kits.":"Cuentacuentos sin inscripción cuatro mañanas a la semana (Toddler Time, Baby Lapsit, Preschool Storytime y Friday Fun), ayuda gratis con tareas de kínder a 5.º, clubes de LEGO y robótica, clases de arte y costura, y kits gratis de manualidades y ciencia para llevar a casa.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7): library pages re-read through the calendar's end (Dec 10) ----
for e in TOWN["events"]:
    if e["t"]=="Baby Lapsit": e["x"]=["2026-10-27"]
    if e["t"]=="Toddler Time":
        e["s"]=[[1,T1,"2026-10-12","2026-11-30"]]
        e["blurb"]="Rhymes, songs and stories that build early literacy, in the Children's Program Room. No registration; just drop in. The posted series runs through Nov 30."
    if e["t"]=="Homework Helpers (Grades K–5)":
        e["s"]=[[1,[["16:00","19:00"]],"2026-10-12","2026-12-07"],[2,[["16:00","19:00"]],"2026-10-13","2026-12-08"],[3,[["16:00","17:00"]],"2026-10-14","2026-12-09"],[4,[["18:00","19:00"]],"2026-10-22","2026-12-10"]]
    if e["t"]=="Kids Lego Club": e["when"]=[W("2026-10-24",[["11:00","12:00"]]),W("2026-11-23",[["16:00","17:00"]])]
    if e["t"]=="Stop by for Science: Spooky Spiderwebs":
        e["t"]="Stop by for Science"; e.pop("special",None)
        e["when"]=[W("2026-10-20",[["17:30","19:00"]]),W("2026-11-24",[["17:30","19:00"]])]
        e["blurb"]="A self-paced, drop-in science table: spooky spiderwebs (Oct 20) and popcorn science (Nov 24)."
TOWN["events"].append(ev(t="Charles Dickens' A Christmas Carol",special="hol",when=[W("2026-11-29",[["14:00","15:00"]])],ages="All ages",a=["preschool","big"],drop=True,
   blurb="A holiday performance of A Christmas Carol in the library's Lovell Room."))
ES["Rhymes, songs and stories that build early literacy, in the Children's Program Room. No registration; just drop in. The posted series runs through Nov 30."]="Rimas, canciones y cuentos que fomentan la lectura temprana, en la sala de programas infantiles. Sin inscripción; solo llega. La serie publicada llega hasta el 30 de nov."
ES["A self-paced, drop-in science table: spooky spiderwebs (Oct 20) and popcorn science (Nov 24)."]="Una mesa de ciencia sin inscripción y a tu propio ritmo: telarañas de miedo (20 de oct.) y la ciencia de las palomitas (24 de nov.)."
ES["A holiday performance of A Christmas Carol in the library's Lovell Room."]="Una función navideña de Cuento de Navidad en el Lovell Room de la biblioteca."

# ---- other playbook steps ----
TOWN["tba"]+=[{"g":"hol","t":"Boothe Homestead Christmas","w":"Boothe Memorial Park & Museum, 5800 Main St",
  "p":"The Friends of Boothe Memorial Park decorate the historic homestead for the holidays and open it for tours over the first weekend of December, with Santa photos on Saturday and Sunday afternoons. Small admission; kids under 6 free. This year's dates aren't posted yet.","src":"https://stratfordcrier.com/homestead-for-the-holidays/"}]
TOWN["classes"]+=[
 {"id":"ct-dance-conservatory","c":"dance","n":"Connecticut Dance Conservatory","u":"http://www.ctdanceconservatory.org/general-info.html",
  "blurb":"A dance school with classes by age, a Day of Dance (Nov 8) and a family observation week (Dec 2–7).","ages":"Kids and teens","where":"279 Ferry Blvd"},
 {"id":"turning-pointe","c":"dance","n":"Turning Pointe Dance Academy","u":"https://www.yelp.com/biz/turning-pointe-dance-academy-stratford",
  "blurb":"A neighborhood dance studio on Main Street with children's classes.","ages":"Kids","where":"2420 Main St"},
 {"id":"stratford-rec","c":"move","n":"Stratford Recreation youth programs","u":"https://townofstratford.recdesk.com/Community/Program?category=3",
  "blurb":"About 45 youth classes and sports across fall and winter sessions; browse and register on the town's RecDesk site.","ages":"Kids and teens","where":"Around Stratford"},
]
PLACES["out"]+=[("Stratford Point","Coastal trails, restored dunes and native gardens at the mouth of the Housatonic, run by Connecticut Audubon (1207 Prospect Dr); check open hours.","Senderos costeros, dunas restauradas y jardines nativos en la desembocadura del Housatonic, administrados por Connecticut Audubon (1207 Prospect Dr); consulta el horario.")]
PLACES["rain"]+=[("Obodo Serendipity Books","Stratford's independent bookstore, on the Connecticut Book Trail, with guest-reader storytimes for little kids (3588 Main St).","La librería independiente de Stratford, parte del Connecticut Book Trail, con cuentacuentos de lectores invitados para los más pequeños (3588 Main St).")]
ES.update({
 "The Friends of Boothe Memorial Park decorate the historic homestead for the holidays and open it for tours over the first weekend of December, with Santa photos on Saturday and Sunday afternoons. Small admission; kids under 6 free. This year's dates aren't posted yet.":"Los Friends of Boothe Memorial Park decoran la casa histórica para las fiestas y la abren para visitas el primer fin de semana de diciembre, con fotos con Santa el sábado y el domingo por la tarde. Entrada económica; menores de 6 gratis. Las fechas de este año aún no se han publicado.",
 "Boothe Memorial Park & Museum, 5800 Main St":"Boothe Memorial Park & Museum, 5800 Main St",
 "A dance school with classes by age, a Day of Dance (Nov 8) and a family observation week (Dec 2–7).":"Una escuela de danza con clases por edad, un Day of Dance (8 de nov.) y una semana de observación para familias (2–7 de dic.).",
 "Kids and teens":"Niños y adolescentes",
 "A neighborhood dance studio on Main Street with children's classes.":"Una escuela de danza de barrio en Main Street con clases para niños.",
 "Kids":"Niños",
 "About 45 youth classes and sports across fall and winter sessions; browse and register on the town's RecDesk site.":"Unas 45 clases y deportes juveniles en sesiones de otoño e invierno; consulta e inscríbete en el sitio RecDesk del pueblo.",
 "Around Stratford":"En distintos lugares de Stratford",
})
PLACES["drive"]=[p if p[0]!="Discovery Museum" else ("SHU Discovery Science Center & Planetarium","Hands-on science exhibits and a planetarium in Bridgeport (formerly the Discovery Museum).","Exposiciones de ciencia interactivas y un planetario en Bridgeport (antes Discovery Museum).") for p in PLACES["drive"]]
TOWN["events"].append({"t":"Veterans Day Parade","v":"town-hall-green","when":[W("2026-11-07",[["11:00","12:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":CS,
  "blurb":"Stratford's parade honoring veterans steps off from Town Hall at 11 and heads south on Main Street to Academy Hill. Main Street closes 10:30–12:30. The start time is from past years."})
ES["Stratford's parade honoring veterans steps off from Town Hall at 11 and heads south on Main Street to Academy Hill. Main Street closes 10:30–12:30. The start time is from past years."]="El desfile de Stratford en honor a los veteranos sale del Town Hall a las 11 y baja por Main Street hasta Academy Hill. Main Street cierra de 10:30 a 12:30. La hora de inicio es de años anteriores."

# ---- Stratford Recreation (RecDesk paste, Oct 8) ----
RD="https://townofstratford.recdesk.com/Community/Program?category=3"
TOWN["classes"]=[c for c in TOWN["classes"] if c["id"]!="stratford-rec"]
TOWN["classes"]+=[
 {"id":"strat-mad-science","c":"build","n":"Mad Science (Stratford Rec)","u":RD,
  "blurb":"Six-week after-school science at elementary schools: 2nd Hill Lane (Thursdays, Oct 8–Nov 12, open), Wilcoxson (Fridays, Oct 9–Nov 13) and Nichols (Wednesdays, started Sept 30).","ages":"Grades K–6","where":"Stratford elementary schools"},
 {"id":"strat-kitchen-kids","c":"art","n":"Kitchen Kids! (Stratford Rec)","u":RD,
  "blurb":"A kids' cooking class on Mondays; Fall Session 2 runs Oct 19–Nov 9.","ages":"Grades 2–6","where":"Birdseye Complex kitchen classroom"},
 {"id":"strat-nature-adventures","c":"nature","n":"Nature Adventures @ Roosevelt Forest (Stratford Rec)","u":RD,
  "blurb":"Saturday nature classes in Roosevelt Forest, Oct 24–Nov 14 (grades K–2) and Oct 24–Nov 21 (grades 3–6).","ages":"Grades K–6","where":"Roosevelt Forest"},
 {"id":"strat-audubon","c":"nature","n":"CT Audubon Nature Classes (Stratford Rec)","u":RD,
  "blurb":"One-day Friday nature classes with Connecticut Audubon on Oct 23, Oct 30, Nov 6 and Nov 13; sign up for any or all.","ages":"Grades 2–6","where":"See registration for location"},
 {"id":"strat-sports","c":"move","n":"Youth Basketball, Soccer and Track (Stratford Rec)","u":RD,
  "blurb":"Fall Session 2 clinics: basketball skills on Thursdays (Oct 29–Dec 3), soccer on Wednesdays (Oct 21–Dec 2), each with K–2 and 3–6 groups, plus track and field on Tuesdays for grades 3–6 (Oct 20–Nov 17).","ages":"Grades K–6","where":"Around Stratford"},
 {"id":"strat-tennis","c":"move","n":"Indoor Youth Tennis (Stratford Rec)","u":RD,
  "blurb":"Tuesday indoor tennis for ages 3–5, 5–7 and 7–11, Nov 24–Dec 22. Registration opens Oct 26; classes are tiny (3–10 spots).","ages":"3–11","where":"Around Stratford"},
 {"id":"strat-archery","c":"move","n":"Archery (Stratford Rec)","u":RD,
  "blurb":"Saturday beginner and intermediate archery through Nov 14; a few spots left.","ages":"10 and up","where":"Around Stratford"},
 {"id":"strat-kids-night","c":"move","n":"Kids Night (Parents' Night Out)","u":RD,
  "blurb":"A Friday-night drop-off program for kids on Oct 30, run by Stratford Recreation. Register online; see the listing for times.","ages":"Grades K–5","where":"Stratford Recreation"},
]
ES.update({
 "Six-week after-school science at elementary schools: 2nd Hill Lane (Thursdays, Oct 8–Nov 12, open), Wilcoxson (Fridays, Oct 9–Nov 13) and Nichols (Wednesdays, started Sept 30).":"Ciencia después de clases durante seis semanas en escuelas primarias: 2nd Hill Lane (jueves, 8 de oct.–12 de nov., con lugares), Wilcoxson (viernes, 9 de oct.–13 de nov.) y Nichols (miércoles, empezó el 30 de sept.).",
 "Grades K–6":"Kínder a 6.º grado",
 "Stratford elementary schools":"Escuelas primarias de Stratford",
 "A kids' cooking class on Mondays; Fall Session 2 runs Oct 19–Nov 9.":"Una clase de cocina para niños los lunes; la sesión de otoño 2 va del 19 de oct. al 9 de nov.",
 "Grades 2–6":"2.º a 6.º grado",
 "Birdseye Complex kitchen classroom":"Aula de cocina del Birdseye Complex",
 "Saturday nature classes in Roosevelt Forest, Oct 24–Nov 14 (grades K–2) and Oct 24–Nov 21 (grades 3–6).":"Clases de naturaleza los sábados en Roosevelt Forest, del 24 de oct. al 14 de nov. (kínder–2.º) y del 24 de oct. al 21 de nov. (3.º–6.º).",
 "Roosevelt Forest":"Roosevelt Forest",
 "One-day Friday nature classes with Connecticut Audubon on Oct 23, Oct 30, Nov 6 and Nov 13; sign up for any or all.":"Clases de naturaleza de un día los viernes con Connecticut Audubon el 23 y 30 de oct. y el 6 y 13 de nov.; inscríbete en una o en todas.",
 "See registration for location":"Consulta el lugar al inscribirte",
 "Fall Session 2 clinics: basketball skills on Thursdays (Oct 29–Dec 3), soccer on Wednesdays (Oct 21–Dec 2), each with K–2 and 3–6 groups, plus track and field on Tuesdays for grades 3–6 (Oct 20–Nov 17).":"Clínicas de la sesión de otoño 2: básquetbol los jueves (29 de oct.–3 de dic.) y fútbol los miércoles (21 de oct.–2 de dic.), con grupos de kínder–2.º y 3.º–6.º, además de atletismo los martes para 3.º–6.º (20 de oct.–17 de nov.).",
 "Around Stratford":"En distintos lugares de Stratford",
 "Tuesday indoor tennis for ages 3–5, 5–7 and 7–11, Nov 24–Dec 22. Registration opens Oct 26; classes are tiny (3–10 spots).":"Tenis bajo techo los martes para 3–5, 5–7 y 7–11 años, del 24 de nov. al 22 de dic. La inscripción abre el 26 de oct.; los grupos son muy pequeños (3–10 lugares).",
 "3–11":"3–11 años",
 "Saturday beginner and intermediate archery through Nov 14; a few spots left.":"Tiro con arco para principiantes e intermedios los sábados hasta el 14 de nov.; quedan pocos lugares.",
 "10 and up":"Desde 10 años",
 "A Friday-night drop-off program for kids on Oct 30, run by Stratford Recreation. Register online; see the listing for times.":"Un programa de viernes por la noche para dejar a los niños el 30 de oct., de Stratford Recreation. Inscríbete en línea; consulta el horario en el anuncio.",
 "Grades K–5":"Kínder a 5.º grado",
 "Stratford Recreation":"Stratford Recreation",
})

# ---- patch: stratford-2026-10-08c.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
# Round 3 finishing pass, Oct 8 2026
TH="stratford-town-hall"
TOWN["venues"][TH]=["Stratford Town Hall","2725 Main St"]; TOWN["venueMeta"][TH]=[None,0]
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"]!="Stratford Menorah Lighting"]
TOWN["events"]+=[{"t":"Stratford Menorah Lighting","v":TH,"special":"hol","when":[{"from":"2026-12-09","t":[]}],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://www.townofstratford.com/article/2802050",
  "blurb":"The town's Chanukah menorah lighting with music, dreidels, doughnuts, gelt and a prize for every child. Time and place aren't posted yet (last year: Town Hall at 6pm)."}]
ES_PATCH={"The town's Chanukah menorah lighting with music, dreidels, doughnuts, gelt and a prize for every child. Time and place aren't posted yet (last year: Town Hall at 6pm).":"El encendido de la menorá de Janucá del pueblo con música, dreidels, donas, monedas de chocolate y un premio para cada niño. Hora y lugar aún no publicados (el año pasado: Ayuntamiento a las 6 p. m.)."}

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
