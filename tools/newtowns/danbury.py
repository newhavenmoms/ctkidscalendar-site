W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
L="danbury-library"; SRC="https://danburylibrary.events.mylibrary.digital/"
B=["baby","toddler","preschool"]
def ev(**k):
    e={"v":L,"free":True,"price":"Free","src":SRC}; e.update(k); return e
RAIL="https://ctvisit.com/events/ride-husking-bee-pumpkin-patch-train-1"
TOWN={
 "display":"Danbury","accent":"#F2C9D7",
 "venues":{L:["Danbury Library","170 Main St"],
           "rail":["Danbury Railway Museum","120 White St"]},
 "venueMeta":{L:[None,1],"rail":[None,0]},
 "events":[
  ev(t="Baby & Me Sign Language",when=D(["2026-10-08","2026-10-15","2026-10-22","2026-10-29"],[["11:00","11:45"]]),ages="Babies and toddlers + caregiver",a=["baby","toddler"],drop=True,check=True,
     blurb="Learn simple baby signs together through songs and play."),
  ev(t="Baby Lapsit Storytime",when=D(["2026-10-13","2026-10-20","2026-10-27"],[["11:00","11:45"]]),ages="Babies + caregiver",a=["baby"],drop=True,
     blurb="Rhymes, songs and board books for the littlest listeners."),
  ev(t="Music & Movement for Babies",when=D(["2026-11-03","2026-11-10","2026-11-17"],[["11:00","11:45"]]),ages="Babies + caregiver",a=["baby"],drop=True,check=True,
     blurb="A November series of songs, movement and play for babies and their grown-ups."),
  ev(t="All Ages Storytime",when=[W("2026-10-14",[["15:00","15:45"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="An after-school storytime for the whole family."),
  ev(t="One Book One Community: If You Give a Mouse a Cookie",when=[W("2026-10-17",[["11:00","12:00"]])],ages="Ages 0–12",a=B+["big"],drop=True,check=True,
     blurb="A family celebration of this year's One Book One Community picture book."),
  ev(t="Drop-in Sensory Play",when=[W("2026-10-26",[["11:00","12:00"]])],ages="Ages 0–5 + caregiver",a=B,drop=True,
     blurb="Sensory bins and hands-on play for little ones. (The Oct 19 session is cancelled.)"),
  ev(t="Caregiver and Me French Classes",when=D(["2026-11-12","2026-11-19","2026-12-03","2026-12-10","2026-12-17"],[["16:30","17:15"]]),ages="Ages 0–5 + caregiver",a=B,rsvp=True,check=True,
     blurb="Songs, stories and play in French for young children and their grown-ups."),
  ev(t="Sing-Along and Stories: A Concert for All Ages",when=[W("2026-12-08",[["14:00","15:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="A family concert of songs and stories."),
  ev(t="Speedcubing Club",s=[[2,[["17:30","18:30"]],"2026-10-13","2026-12-29"]],ages="School age and teens",a=["big"],rsvp=True,check=True,
     blurb="Learn to solve the Rubik's Cube, then get faster, every Tuesday."),
  ev(t="Bilingual Medical Kids Workshop",when=D(["2026-10-13","2026-10-20","2026-10-27"],[["17:00","18:00"]]),ages="Ages 6–12",a=["big"],rsvp=True,check=True,
     blurb="A three-week bilingual workshop where kids explore health and medicine."),
  ev(t="Kids Cooking Class",when=D(["2026-10-13","2026-10-19","2026-11-16"],[["16:00","17:00"]]),ages="Ages 6–12 and teens",a=["big"],rsvp=True,check=True,
     blurb="Chocolate-chip dippers (Oct 13), pumpkin granola cups (Oct 19, full) and gingerbread French toast (Nov 16). Registration required."),
  ev(t="Mario Kart Madness",when=[W("2026-10-10",[["11:00","12:00"]])],ages="Ages 6–12 and teens",a=["big"],drop=True,check=True,
     blurb="Race friends in Mario Kart on the big screen."),
  ev(t="Read to Sydney",when=[W("2026-10-14",[["16:00","17:00"]])],ages="Ages 6–12",a=["big"],rsvp=True,check=True,
     blurb="Practice reading aloud to Sydney, a friendly therapy dog. The first of 12 sessions running through May; see the library's calendar for later dates."),
  ev(t="Fall Slime Series",when=D(["2026-10-14","2026-10-21","2026-10-28"],[["16:30","17:30"]]),ages="Ages 6–12 and teens",a=["big"],rsvp=True,check=True,
     blurb="Three weeks of slime-making."),
  ev(t="Homework Help",s=[[4,[["16:00","18:00"]],"2026-10-15","2026-12-17"]],x=["2026-11-26"],ages="Ages 6–12",a=["big"],drop=True,check=True,
     blurb="Free after-school homework help on Thursdays, running through May with holiday breaks."),
  ev(t="Beyond the Breed: Exploring Dog DNA",when=[W("2026-10-15",[["18:00","19:00"]])],ages="Families, kids and teens",a=["big"],drop=True,check=True,
     blurb="Learn what dog DNA tests reveal about breeds and behavior."),
  ev(t="LEGO Free Play",when=[W("2026-10-26",[["16:00","17:00"]])],ages="Ages 6–12",a=["big"],drop=True,
     blurb="Free building with the library's LEGO. The first of seven sessions through April; see the library's calendar for later dates."),
  ev(t="Paper Flower Crafting",when=[W("2026-11-02",[["16:00","17:00"]])],ages="All ages",a=["preschool","big"],rsvp=True,check=True,
     blurb="Make paper flowers in a bilingual craft workshop."),
  ev(t="Community Ofrenda: A Día de los Muertos Celebration",when=[W("2026-11-04",[["17:00","18:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="Help build a community ofrenda and celebrate Día de los Muertos."),
  ev(t="Diwali Celebration",when=[W("2026-11-14",[["11:00","12:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="A family celebration of the festival of lights."),
  ev(t="R.I. Pirate Guy's Pirate Adventure!",when=[W("2026-12-28",[["15:00","16:00"]])],ages="Ages 6–12",a=["preschool","big"],drop=True,
     blurb="A pirate-themed show for the winter break."),
  ev(t="WIRED UP!",when=[W("2026-12-29",[["15:00","16:00"]])],ages="Ages 6–12",a=["big"],drop=True,check=True,
     blurb="A family performance for the winter break."),
  ev(t="Sewing Small Stuffies",when=[W("2026-12-30",[["15:00","16:00"]])],ages="Ages 6–12",a=["big"],rsvp=True,check=True,
     blurb="Sew a small stuffed toy over the winter break."),
  ev(t="Winter Magic & Melodies with Joy Blooms",when=[W("2026-12-30",[["17:30","18:30"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="A winter-break family concert."),
  {"t":"Husking Bee Pumpkin Patch Train","v":"rail","special":"fall","when":[{"from":d,"t":[["11:00","16:00"]]} for d in ["2026-10-10","2026-10-11","2026-10-17","2026-10-18","2026-10-24","2026-10-25","2026-10-31","2026-11-01"]],
   "ages":"All ages (under 2 free)","a":B+["big"],"free":False,"price":"$20 ($25 twilight trains)","rsvp":True,"src":RAIL,
   "blurb":"A 20-minute ride in a 1920s coach to the railyard pumpkin patch, where every rider picks a free pumpkin and gets cider and cookies. Trains hourly 11–3, plus a 6:30 twilight train on Saturdays and a Storytime Express on Saturday mornings. Reservations recommended."},
 ],
 "tba":[
  {"g":"hw","t":"Halloween on the Green","w":"CityCenter Danbury Green, 1 Ives St",
   "p":"Danbury's free Halloween afternoon with a kids' costume parade and contest, goodie bags for the first 800 costumed kids, music and vendors. Usually the last Saturday in October, 1–4 pm. This year's date isn't posted yet.","src":"https://danbury.macaronikid.com/events/66fff33da04af54b6afc6cd1/-32nd-annual-halloween-on-the-green--citycenter-danbury-green"},
  {"g":"hol","t":"Light the Lights","w":"CityCenter Danbury Green, 1 Ives St",
   "p":"Danbury lights its 40-foot tree on an early-December Saturday afternoon, with Santa arriving by fire truck, performances and a holiday market. This year's date isn't posted yet.","src":"https://danbury.macaronikid.com/articles/6750f8c84fd31f69acdd13e3/danburys-light-the-lights_-saturday-december-7"},
  {"g":"hol","t":"Santa trains at the Danbury Railway Museum","w":"Danbury Railway Museum, 120 White St",
   "p":"The museum runs its Santa trains from late November through December. This year's dates aren't posted yet.","src":"https://ctvisit.com/events/ride-vintage-train-visit-santa-claus-all-aboard-snow-clipper-first-gift-express-2"},
 ],
 "classes":[],
 "library":{"for":"Free, every week","name":"Danbury Library","desc":"Baby sign language, lapsit and music classes, French for little ones, a weekly Speedcubing Club and Thursday homework help, plus cooking classes, slime and LEGO for school-age kids, and winter-break shows.","a":"See the library's calendar","href":SRC},
}
PLACES={
 "out":[("Tarrywile Park & Mansion","Over 700 acres of trails, ponds and meadows around a historic mansion, free to explore.","Más de 280 hectáreas de senderos, estanques y praderas alrededor de una mansión histórica, gratis para explorar."),
        ("Danbury Railway Museum","Climb aboard vintage railcars and locomotives in the old railyard, with model trains inside.","Sube a vagones y locomotoras antiguas en el viejo patio ferroviario, con trenes a escala adentro."),
        ("Rogers Park","A big city park with playgrounds, a pond and walking paths.","Un gran parque de la ciudad con áreas de juegos, un estanque y senderos.")],
 "rain":[("Danbury Library","The downtown library, with baby classes, homework help and after-school clubs.","La biblioteca del centro, con clases para bebés, ayuda con tareas y clubes después de clases."),
         ("Danbury Ice Arena","An indoor rink with public skating; check the schedule before you go.","Una pista de hielo techada con patinaje público; consulta el horario antes de ir."),
         ("Danbury Fair Mall","A big indoor mall with a double-decker carousel, handy on a rainy day.","Un gran centro comercial techado con un carrusel de dos pisos, útil en días de lluvia.")],
 "drive":[("Squantz Pond State Park","A lakeside beach and trails in New Fairfield.","Una playa junto al lago y senderos en New Fairfield."),
          ("Putnam Memorial State Park","Revolutionary War encampment ruins, a museum and trails in Redding.","Ruinas de un campamento de la Guerra de Independencia, un museo y senderos en Redding."),
          ("Weir Farm National Historical Park","A painter's farm and studio with free art kits for kids, on the Ridgefield–Wilton line.","La granja y estudio de un pintor con kits de arte gratis para niños, entre Ridgefield y Wilton.")],
}
ES={
 "Babies and toddlers + caregiver":"Bebés y niños pequeños + un adulto",
 "Learn simple baby signs together through songs and play.":"Aprendan juntos señas sencillas para bebés con canciones y juegos.",
 "Babies + caregiver":"Bebés + un adulto",
 "Rhymes, songs and board books for the littlest listeners.":"Rimas, canciones y libros de cartón para los más pequeños.",
 "A November series of songs, movement and play for babies and their grown-ups.":"Una serie de noviembre con canciones, movimiento y juego para bebés y sus adultos.",
 "All ages":"Todas las edades",
 "An after-school storytime for the whole family.":"Un cuentacuentos después de clases para toda la familia.",
 "Ages 0–12":"0–12 años",
 "A family celebration of this year's One Book One Community picture book.":"Una celebración familiar del libro ilustrado de One Book One Community de este año.",
 "Ages 0–5 + caregiver":"0–5 años + un adulto",
 "Sensory bins and hands-on play for little ones. (The Oct 19 session is cancelled.)":"Cajas sensoriales y juego práctico para los pequeños. (La sesión del 19 de oct. está cancelada.)",
 "Songs, stories and play in French for young children and their grown-ups.":"Canciones, cuentos y juego en francés para niños pequeños y sus adultos.",
 "A family concert of songs and stories.":"Un concierto familiar de canciones y cuentos.",
 "School age and teens":"Escolares y adolescentes",
 "Learn to solve the Rubik's Cube, then get faster, every Tuesday.":"Aprende a resolver el cubo de Rubik y luego hazlo más rápido, todos los martes.",
 "Ages 6–12":"6–12 años",
 "A three-week bilingual workshop where kids explore health and medicine.":"Un taller bilingüe de tres semanas donde los niños exploran la salud y la medicina.",
 "Ages 6–12 and teens":"6–12 años y adolescentes",
 "Chocolate-chip dippers (Oct 13), pumpkin granola cups (Oct 19, full) and gingerbread French toast (Nov 16). Registration required.":"Galletas de chispas de chocolate para mojar (13 de oct.), vasitos de granola de calabaza (19 de oct., lleno) y pan francés de jengibre (16 de nov.). Inscripción obligatoria.",
 "Race friends in Mario Kart on the big screen.":"Compite con tus amigos en Mario Kart en la pantalla grande.",
 "Practice reading aloud to Sydney, a friendly therapy dog. The first of 12 sessions running through May; see the library's calendar for later dates.":"Practica la lectura en voz alta con Sydney, una amigable perra de terapia. Es la primera de 12 sesiones hasta mayo; consulta el calendario de la biblioteca para las siguientes fechas.",
 "Three weeks of slime-making.":"Tres semanas para hacer slime.",
 "Free after-school homework help on Thursdays, running through May with holiday breaks.":"Ayuda gratis con las tareas los jueves después de clases, hasta mayo con pausas en días festivos.",
 "Families, kids and teens":"Familias, niños y adolescentes",
 "Learn what dog DNA tests reveal about breeds and behavior.":"Descubre lo que revelan las pruebas de ADN de perros sobre razas y comportamiento.",
 "Free building with the library's LEGO. The first of seven sessions through April; see the library's calendar for later dates.":"Construcción libre con los LEGO de la biblioteca. Es la primera de siete sesiones hasta abril; consulta el calendario de la biblioteca para las siguientes fechas.",
 "Make paper flowers in a bilingual craft workshop.":"Haz flores de papel en un taller bilingüe de manualidades.",
 "Help build a community ofrenda and celebrate Día de los Muertos.":"Ayuda a armar una ofrenda comunitaria y celebra el Día de los Muertos.",
 "A family celebration of the festival of lights.":"Una celebración familiar de la fiesta de las luces.",
 "A pirate-themed show for the winter break.":"Un espectáculo de piratas para las vacaciones de invierno.",
 "A family performance for the winter break.":"Una función familiar para las vacaciones de invierno.",
 "Sew a small stuffed toy over the winter break.":"Cose un pequeño peluche durante las vacaciones de invierno.",
 "A winter-break family concert.":"Un concierto familiar en las vacaciones de invierno.",
 "All ages (under 2 free)":"Todas las edades (menores de 2 gratis)",
 "$20 ($25 twilight trains)":"$20 ($25 trenes al atardecer)",
 "A 20-minute ride in a 1920s coach to the railyard pumpkin patch, where every rider picks a free pumpkin and gets cider and cookies. Trains hourly 11–3, plus a 6:30 twilight train on Saturdays and a Storytime Express on Saturday mornings. Reservations recommended.":"Un paseo de 20 minutos en un vagón de los años 20 hasta el campo de calabazas del patio ferroviario, donde cada pasajero elige una calabaza gratis y recibe sidra y galletas. Trenes cada hora de 11 a 3, más un tren al atardecer a las 6:30 los sábados y un Storytime Express los sábados por la mañana. Se recomienda reservar.",
 "Danbury's free Halloween afternoon with a kids' costume parade and contest, goodie bags for the first 800 costumed kids, music and vendors. Usually the last Saturday in October, 1–4 pm. This year's date isn't posted yet.":"La tarde gratis de Halloween de Danbury con desfile y concurso de disfraces infantiles, bolsas de regalo para los primeros 800 niños disfrazados, música y vendedores. Normalmente el último sábado de octubre, de 1 a 4 pm. La fecha de este año aún no se ha publicado.",
 "CityCenter Danbury Green, 1 Ives St":"CityCenter Danbury Green, 1 Ives St",
 "Danbury lights its 40-foot tree on an early-December Saturday afternoon, with Santa arriving by fire truck, performances and a holiday market. This year's date isn't posted yet.":"Danbury enciende su árbol de 12 metros un sábado por la tarde a principios de diciembre, con Santa llegando en camión de bomberos, presentaciones y un mercado navideño. La fecha de este año aún no se ha publicado.",
 "The museum runs its Santa trains from late November through December. This year's dates aren't posted yet.":"El museo ofrece sus trenes de Santa desde finales de noviembre hasta diciembre. Las fechas de este año aún no se han publicado.",
 "Danbury Railway Museum, 120 White St":"Danbury Railway Museum, 120 White St",
 "Baby sign language, lapsit and music classes, French for little ones, a weekly Speedcubing Club and Thursday homework help, plus cooking classes, slime and LEGO for school-age kids, and winter-break shows.":"Lenguaje de señas para bebés, clases de regazo y música, francés para los pequeños, un club semanal de Speedcubing y ayuda con tareas los jueves, además de clases de cocina, slime y LEGO para escolares, y funciones en las vacaciones de invierno.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7) ----
CC="citycenter-green"; DHS="danbury-high"
TOWN["venues"].update({CC:["CityCenter Danbury Green","1 Ives St"],DHS:["Danbury High School Auditorium","43 Clapboard Ridge Rd"]})
TOWN["venueMeta"].update({CC:[None,0],DHS:[None,1]})
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"] not in ("Halloween on the Green","Light the Lights")]
TOWN["events"]+=[
 {"t":"Halloween on the Green","v":CC,"special":"hw","when":[W("2026-10-31",[["13:00","16:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://citycenterdanbury.com/event/halloween-on-the-green-2/",
  "blurb":"Danbury's free Halloween afternoon: a kids' costume parade with prizes for most original, scariest and cutest, goodie bags for the first 800 costumed kids, music, a photo booth and vendors. Rain moves it to Patriot Garage level 4."},
 {"t":"Light the Lights Winter Festival","v":CC,"special":"hol","when":[W("2026-12-05",[["16:00","19:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://citycenterdanbury.com/",
  "blurb":"Danbury lights its 40-foot tree on the CityCenter Green, with Santa arriving by fire truck, holiday performances and a holiday market."},
 {"t":"Danbury Music Centre's The Nutcracker","v":DHS,"special":"hol","when":[W("2026-12-11",[["19:30","21:30"]]),W("2026-12-12",[["15:00","17:00"]]),W("2026-12-13",[["15:00","17:00"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Tickets on sale Nov 1","check":True,"src":"https://danburymusiccentre.org/program/nutcracker-ballet/",
  "blurb":"Danbury's community Nutcracker, danced by local kids, teens and adults with a live orchestra. Tickets go on sale Nov 1."},
]
TOWN["classes"]+=[
 {"id":"gym-spectrum","c":"move","n":"Gymnastic Spectrum","u":"https://danbury.macaronikid.com/directory/5859628c4ba41260f7536afa/gymnastic-spectrum",
  "blurb":"Non-competitive recreational and preschool gymnastics with trampolines and a foam pit, plus ninja classes.","ages":"Preschool–teens","where":"69 Kenosia Ave Ext"},
 {"id":"dmc-strings","c":"music","n":"Danbury Centre Strings (Danbury Music Centre)","u":"https://danburymusiccentre.org/",
  "blurb":"A free strings program for school-age kids, September through May, from the Danbury Music Centre.","ages":"School age","where":"256 Main St"},
 {"id":"danbury-ice-lts","c":"move","n":"Learn to Skate at Danbury Ice Arena","u":"https://ctvisit.com/listings/danbury-ice-arena",
  "blurb":"Learn-to-skate classes for all ages and abilities, plus public skating sessions; see the arena's monthly schedule.","ages":"All ages","where":"1 Independence Way"},
]
PLACES["rain"]=[p for p in PLACES["rain"] if p[0]!="Danbury Ice Arena"]
PLACES["rain"]+=[("Danbury Ice Arena","An indoor rink with public skating and learn-to-skate classes (1 Independence Way); check the monthly schedule.","Una pista de hielo techada con patinaje público y clases para aprender a patinar (1 Independence Way); consulta el horario mensual."),
                 ("Military Museum of Southern New England","More than 25 tanks and military vehicles outside and thousands of artifacts inside, on Park Avenue near the mall. Kids can climb into the vehicles on summer Open Turret Days; winter hours are shorter.","Más de 25 tanques y vehículos militares afuera y miles de objetos adentro, en Park Avenue cerca del centro comercial. En los Open Turret Days de verano los niños pueden subirse a los vehículos; en invierno el horario es más corto."),
                 ("Danbury Museum & Historical Society","Downtown history museum in Huntington Hall, open Wednesday–Saturday, 12–4 (43 Main St).","Museo de historia en el centro, en Huntington Hall, abierto de miércoles a sábado, de 12 a 4 (43 Main St)."),
                 ("The Booksmiths Shoppe","An independent bookstore on the Connecticut Book Trail (100 Reserve Rd).","Una librería independiente del Connecticut Book Trail (100 Reserve Rd)."),
                 ("LEGO Store, Danbury Fair","Build-your-own-minifigure and Pick & Build walls inside the Danbury Fair mall.","Estaciones para armar tu propia minifigura y muros de Pick & Build dentro del centro comercial Danbury Fair.")]
ES.update({
 "Danbury's free Halloween afternoon: a kids' costume parade with prizes for most original, scariest and cutest, goodie bags for the first 800 costumed kids, music, a photo booth and vendors. Rain moves it to Patriot Garage level 4.":"La tarde gratis de Halloween de Danbury: desfile de disfraces infantiles con premios al más original, el más aterrador y el más tierno, bolsas de regalo para los primeros 800 niños disfrazados, música, cabina de fotos y vendedores. Si llueve, se muda al nivel 4 del Patriot Garage.",
 "Danbury lights its 40-foot tree on the CityCenter Green, with Santa arriving by fire truck, holiday performances and a holiday market.":"Danbury enciende su árbol de 12 metros en el CityCenter Green, con Santa llegando en camión de bomberos, presentaciones navideñas y un mercado navideño.",
 "Tickets on sale Nov 1":"Boletos a la venta desde el 1 de nov.",
 "Danbury's community Nutcracker, danced by local kids, teens and adults with a live orchestra. Tickets go on sale Nov 1.":"El Cascanueces comunitario de Danbury, bailado por niños, adolescentes y adultos de la zona con orquesta en vivo. Los boletos salen a la venta el 1 de nov.",
 "Non-competitive recreational and preschool gymnastics with trampolines and a foam pit, plus ninja classes.":"Gimnasia recreativa y preescolar no competitiva con trampolines y fosa de espuma, además de clases de ninja.",
 "Preschool–teens":"Preescolar–adolescentes",
 "A free strings program for school-age kids, September through May, from the Danbury Music Centre.":"Un programa gratis de instrumentos de cuerda para niños en edad escolar, de septiembre a mayo, del Danbury Music Centre.",
 "School age":"Edad escolar",
 "Learn-to-skate classes for all ages and abilities, plus public skating sessions; see the arena's monthly schedule.":"Clases para aprender a patinar para todas las edades y niveles, además de sesiones de patinaje público; consulta el horario mensual de la pista.",
})

# ---- gap check (Oct 7) ----
PLACES["out"]+=[("Lake Kenosia Park","A lakeside city park with a summer splash pad, playground and fields.","Un parque junto al lago con zona de chorros de agua en verano, área de juegos y campos.")]
PLACES["rain"]=[p if p[0]!="LEGO Store, Danbury Fair" else ("LEGO Store, Danbury Fair","A LEGO toy store with build-your-own-minifigure and Pick & Build walls, inside the Danbury Fair mall.","Una tienda de juguetes LEGO con estaciones para armar tu propia minifigura y muros de Pick & Build, dentro del centro comercial Danbury Fair.") for p in PLACES["rain"]]

# ---- creative places / bookstores / blogs pass (Oct 8) ----
EH="elmwood-hall"; STEW="stew-leonards"
TOWN["venues"].update({EH:["Elmwood Hall","10 Elmwood Pl"],STEW:["Stew Leonard's Danbury","99 Federal Rd"]})
TOWN["venueMeta"].update({EH:[None,1],STEW:[None,0]})
TOWN["events"]+=[
 {"t":"Pumpkin Palooza at Stew Leonard's","v":STEW,"special":"fall","when":D(["2026-10-10","2026-10-11"],[["11:00","17:00"]]),"ages":"All ages","a":B+["big"],"free":False,"price":"Free painting with a pumpkin purchase","drop":True,"check":True,"src":"https://allevents.in/danbury/stew-leonards-in-danbury-pumpkin-palooza/100001999695808995",
  "blurb":"Buy a pumpkin and paint it for free under the Garden Shop tent."},
 {"t":"Grandparent & Me Card-Making Workshop","v":EH,"when":[W("2026-10-20",[["14:30","15:30"]])],"ages":"Ages 6+ with a grandparent or guardian 60+","a":["big"],"free":True,"price":"Free","rsvp":True,"check":True,"src":"https://citycenterdanbury.com/event/flcb-workshop/",
  "blurb":"Kids and grandparents make handmade greeting cards together with Kim McCormack of Creative Curiosity. 15 kids max; the listing gives two different start times, so confirm when you register."},
]
PLACES["rain"]=[p if p[0]!="Danbury Fair Mall" else ("Danbury Fair Mall","A big indoor mall with a double-decker carousel, the Kid's Klub play area and a Barnes & Noble, handy on a rainy day.","Un gran centro comercial techado con un carrusel de dos pisos, el área de juegos Kid's Klub y un Barnes & Noble, útil en días de lluvia.") for p in PLACES["rain"]]
PLACES["rain"]+=[("Jumpz Trampoline Sports","Trampolines, foam pits, a ninja course, laser tag and a Junior Jumpz area for ages 5 and under, Wednesday–Sunday (21 Prindle Ln). From $17 for 30 minutes; toddlers $12.","Trampolines, fosas de espuma, circuito ninja, láser tag y el área Junior Jumpz para niños de 5 años o menos, de miércoles a domingo (21 Prindle Ln). Desde $17 por 30 minutos; pequeños $12."),
                 ("Thrillz High-Flying Adventure Park","Ninja-style obstacles over airbags (48-inch minimum height), a VR coaster and laser tag, Wednesday–Sunday (5 Prindle Ln).","Obstáculos estilo ninja sobre colchones de aire (estatura mínima de 48 pulgadas), una montaña rusa de realidad virtual y láser tag, de miércoles a domingo (5 Prindle Ln)."),
                 ("Xtreme Play Adrenaline Park","A ropes course, rock wall, bumper cars, laser tag and mini bowling (38 Mill Plain Rd). Open Wednesday–Sunday afternoons and evenings.","Circuito de cuerdas, muro de escalada, carritos chocones, láser tag y miniboliche (38 Mill Plain Rd). Abre de miércoles a domingo por la tarde y noche.")]
ES.update({
 "Free painting with a pumpkin purchase":"Pintura gratis al comprar una calabaza",
 "Buy a pumpkin and paint it for free under the Garden Shop tent.":"Compra una calabaza y píntala gratis bajo la carpa del Garden Shop.",
 "Ages 6+ with a grandparent or guardian 60+":"6 años o más con un abuelo o tutor de 60 años o más",
 "Kids and grandparents make handmade greeting cards together with Kim McCormack of Creative Curiosity. 15 kids max; the listing gives two different start times, so confirm when you register.":"Niños y abuelos hacen tarjetas a mano junto con Kim McCormack de Creative Curiosity. Máximo 15 niños; el anuncio da dos horas de inicio distintas, así que confírmalo al inscribirte.",
})
