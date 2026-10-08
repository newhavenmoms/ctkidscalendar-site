W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
L="guilford-library"; SRC="https://guilfordfreelibrary.org/events/audience/children/"
B=["baby","toddler","preschool"]
def ev(**k):
    e={"v":L,"free":True,"price":"Free","src":SRC}; e.update(k); return e
TOWN={
 "display":"Guilford","accent":"#F3D9A4",
 "venues":{L:["Guilford Free Library","67 Park St"],"guilford-green":["Guilford Green","Downtown Guilford"]},
 "venueMeta":{L:[None,1],"guilford-green":[None,0]},
 "events":[
  ev(t="Paws & Read",s=[[1,[["16:00","17:00"]],"2026-10-05","2026-12-28"],[2,[["16:00","17:00"]],"2026-10-06","2026-12-29"],[3,[["16:00","17:00"]],"2026-10-07","2026-12-30"],[4,[["16:15","17:15"]],"2026-10-08","2026-12-31"]],
     ages="Kids practicing reading",a=["big"],check=True,blurb="Kids read aloud to a friendly therapy dog: Theo on Mondays and Wednesdays, Oliver on Tuesdays and Newman on Thursdays."),
  ev(t="Time for Twos",when=D(["2026-10-06","2026-10-13","2026-10-20","2026-10-27","2026-11-03","2026-11-17","2026-11-24"],[["10:00","10:45"]]),ages="Age 2 + caregiver",a=["toddler"],rsvp=True,
     blurb="A Tuesday-morning storytime just for two-year-olds and their grown-ups. Registration required."),
  ev(t="Sunshine Storytime",when=D(["2026-10-07","2026-10-14","2026-10-21","2026-10-28","2026-11-04","2026-11-11"],[["10:00","10:45"]]),ages="Ages 3 and up",a=["preschool"],rsvp=True,
     blurb="A Wednesday-morning preschool storytime with stories, songs and a craft. The fall series ends November 11."),
  ev(t="Babytime",when=D(["2026-10-08","2026-10-15","2026-10-22","2026-10-29","2026-11-05"],[["09:30","10:30"]]),ages="Babies + caregiver",a=["baby"],rsvp=True,
     blurb="Songs, rhymes and play for babies and their grown-ups on Thursday mornings. The fall series ends November 5."),
  ev(t="One on Ones",when=D(["2026-10-19","2026-10-26","2026-11-02","2026-11-09","2026-11-16","2026-11-23"],[["09:30","10:30"]]),ages="Toddlers + caregiver",a=["toddler"],rsvp=True,
     blurb="A six-week Monday-morning series for little ones and a caregiver. Registration required."),
  ev(t="Storytime with Hesch",when=D(["2026-10-05","2026-11-02","2026-12-07"],[["10:30","11:15"]]),ages="Young children + family",a=B,drop=True,
     blurb="A monthly musical storytime with guest performer Hesch."),
  ev(t="Storytime with Mimi",when=D(["2026-10-08","2026-11-05","2026-12-03"],[["11:00","11:45"]]),ages="Young children + family",a=B,drop=True,
     blurb="A monthly guest storytime with Mimi on Thursday mornings."),
  ev(t="Storytime with Aaron",when=D(["2026-10-23","2026-11-27","2026-12-18"],[["10:30","11:15"]]),ages="Young children + family",a=B,drop=True,
     blurb="A monthly Friday-morning guest storytime with Aaron."),
  ev(t="Lego Club",when=D(["2026-10-13","2026-11-10","2026-12-08"],[["16:00","17:00"]]),ages="School-age kids",a=["big"],
     blurb="A monthly after-school LEGO building club."),
  ev(t="Junior Chess Class",when=D(["2026-10-21","2026-10-28","2026-11-04","2026-11-11","2026-11-18"],[["16:15","17:30"]]),ages="Ages 5–10",a=["big"],rsvp=True,
     blurb="Learn and practice chess in a weekly after-school class for young players. Registration required."),
  ev(t="Loeb's Weekend Wildlife",when=[W("2026-10-24",[["11:00","12:00"]]),W("2026-11-07",[["11:00","12:00"]])],ages="Kids and families",a=["preschool","big"],
     blurb="Weekend nature programs: Awesome Hawks on Oct 24 and Preparing for Winter on Nov 7."),
  ev(t="Haunted Gingerbread Houses",special="hw",when=[W("2026-10-14",[])],ages="Kids",a=["big"],rsvp=True,check=True,
     blurb="Build a spooky gingerbread house for Halloween. Check the library calendar for the time and registration."),
  {"t":"Spooktacular on the Green","v":"guilford-green","special":"hw","when":[W("2026-10-25",[["14:00","16:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,
   "blurb":"The town's annual Halloween afternoon of family fun on the Green, run by Guilford Parks & Rec. Costumes encouraged. If it rains, it moves to the Guilford Community Center (32 Church St).","src":"https://www.guilfordparkrec.com/newslist.php"},
  ev(t="Trick-or-Treat Storytime",special="hw",when=[W("2026-10-27",[["16:00","16:45"]])],ages="Ages 4–6",a=["preschool"],
     blurb="A Halloween storytime for young kids. Costumes welcome."),
  ev(t="History Comes Alive: History of Halloween",special="hw",when=[W("2026-10-29",[["16:15","17:15"]])],ages="Ages 8–11",a=["big"],rsvp=True,
     blurb="Where Halloween traditions came from, told through hands-on history."),
  ev(t="All Ages Board Game Night",when=D(["2026-10-28","2026-11-25","2026-12-30"],[["17:30","20:00"]]),ages="All ages",a=["preschool","big"],drop=True,
     blurb="A monthly evening of board games for the whole family."),
  ev(t="Tellabration!",when=[W("2026-11-20",[["16:30","17:30"]])],ages="Families",a=["preschool","big"],
     blurb="A family storytelling celebration, part of the worldwide Tellabration storytelling night."),
  ev(t="Meet Lauren Tarshis, Author of I Survived",special="shows",when=[W("2026-11-21",[["14:00","16:00"]])],ages="Kids 7 and up",a=["big"],rsvp=True,
     blurb="The bestselling author of the I Survived series visits the library. Registration required."),
 ],
 "tba":[{"g":"hol","t":"Holiday Tree Lighting & Luminaria","w":"Guilford Green",
   "p":"Guilford lights its tree on the Green each December, usually alongside the Guilford Foundation's luminaria. This year's date isn't posted yet.","src":"https://www.ci.guilford.ct.us/"}],
 "classes":[],
 "library":{"for":"Free, every week","name":"Guilford Free Library","desc":"Storytimes for babies, twos and preschoolers in fall series, monthly guest storytimes, reading-dog visits four days a week, chess, LEGO and family game nights.","a":"See the library's calendar","href":SRC},
}
PLACES={
 "out":[("Guilford Green","One of New England's largest town greens, with big trees, open lawns and shops and cafés all around.","Uno de los parques centrales más grandes de Nueva Inglaterra, con árboles grandes, amplio césped y tiendas y cafés alrededor."),
        ("Jacobs Beach","The town beach on Long Island Sound, with calm water, a playground and a view of the salt marsh.","La playa del pueblo en el estrecho de Long Island, con agua tranquila, parque infantil y vista a la marisma."),
        ("Chaffinch Island Park","A rocky shoreline park with short trails, picnic spots and great views of the Sound.","Un parque costero rocoso con senderos cortos, lugares para picnic y lindas vistas del estrecho."),
        ("Westwoods Trails","Miles of wooded trails with rock formations and a lake, including short loops for little legs.","Kilómetros de senderos en el bosque con formaciones rocosas y un lago, incluidos circuitos cortos para piernas pequeñas."),
        ("Bishop's Orchards","A six-generation family farm: pick-your-own fruit in season, pumpkins, a farm market and a creamery.","Una granja familiar de seis generaciones: frutas para cosechar en temporada, calabazas, mercado y heladería."),
        ("Dudley Farm Museum","A 19th-century farm museum in North Guilford with barns, animals, gardens and seasonal family events.","Un museo granja del siglo XIX en North Guilford con graneros, animales, huertos y eventos familiares de temporada.")],
 "rain":[("Guilford Free Library","Storytimes most weekdays, reading-dog visits and a big children's room.","Cuentacuentos casi todos los días entre semana, visitas de perros de lectura y una gran sala infantil."),
         ("Henry Whitfield State Museum","Connecticut's oldest house (1639), a stone museum with exhibits about early Guilford. Check seasonal hours.","La casa más antigua de Connecticut (1639), un museo de piedra con exposiciones sobre los inicios de Guilford. Consulta el horario de temporada."),
         ("Breakwater Books","An independent bookstore on the Green with a well-loved children's section.","Una librería independiente junto al Green con una sección infantil muy querida.")],
 "drive":[("Hammonasset Beach State Park","Connecticut's longest public beach, plus the Meigs Point Nature Center's touch tanks and trails, just over the line in Madison.","La playa pública más larga de Connecticut, además de los tanques táctiles y senderos del Meigs Point Nature Center, en Madison."),
          ("Essex Steam Train & Riverboat","Vintage steam-train rides along the Connecticut River, including the holiday North Pole Express.","Paseos en tren de vapor antiguo junto al río Connecticut, incluido el North Pole Express navideño."),
          ("Lyman Orchards","Pick-your-own apples and pumpkins, a corn maze and fall weekend activities in Middlefield.","Manzanas y calabazas para cosechar, laberinto de maíz y actividades de fin de semana en otoño en Middlefield.")],
}
ES={
 "Kids read aloud to a friendly therapy dog: Theo on Mondays and Wednesdays, Oliver on Tuesdays and Newman on Thursdays.":"Los niños leen en voz alta a un amigable perro de terapia: Theo los lunes y miércoles, Oliver los martes y Newman los jueves.",
 "Kids practicing reading":"Niños que practican la lectura",
 "A Tuesday-morning storytime just for two-year-olds and their grown-ups. Registration required.":"Un cuentacuentos los martes por la mañana solo para niños de dos años y sus adultos. Inscripción obligatoria.",
 "Age 2 + caregiver":"2 años + un adulto",
 "A Wednesday-morning preschool storytime with stories, songs and a craft. The fall series ends November 11.":"Un cuentacuentos preescolar los miércoles por la mañana con cuentos, canciones y una manualidad. La serie de otoño termina el 11 de noviembre.",
 "Ages 3 and up":"Desde 3 años",
 "Songs, rhymes and play for babies and their grown-ups on Thursday mornings. The fall series ends November 5.":"Canciones, rimas y juego para bebés y sus adultos los jueves por la mañana. La serie de otoño termina el 5 de noviembre.",
 "Babies + caregiver":"Bebés + un adulto",
 "A six-week Monday-morning series for little ones and a caregiver. Registration required.":"Una serie de seis semanas los lunes por la mañana para los más pequeños y un adulto. Inscripción obligatoria.",
 "Toddlers + caregiver":"Niños pequeños + un adulto",
 "A monthly musical storytime with guest performer Hesch.":"Un cuentacuentos musical mensual con el artista invitado Hesch.",
 "Young children + family":"Niños pequeños + familia",
 "A monthly guest storytime with Mimi on Thursday mornings.":"Un cuentacuentos mensual con la invitada Mimi los jueves por la mañana.",
 "A monthly Friday-morning guest storytime with Aaron.":"Un cuentacuentos mensual los viernes por la mañana con el invitado Aaron.",
 "A monthly after-school LEGO building club.":"Un club mensual de construcción con LEGO después de clases.",
 "School-age kids":"Niños en edad escolar",
 "Learn and practice chess in a weekly after-school class for young players. Registration required.":"Aprende y practica ajedrez en una clase semanal después de clases para jugadores jóvenes. Inscripción obligatoria.",
 "Ages 5–10":"5–10 años",
 "Weekend nature programs: Awesome Hawks on Oct 24 and Preparing for Winter on Nov 7.":"Programas de naturaleza los fines de semana: halcones el 24 de octubre y preparación para el invierno el 7 de noviembre.",
 "Kids and families":"Niños y familias",
 "Build a spooky gingerbread house for Halloween. Check the library calendar for the time and registration.":"Construye una casita de jengibre espeluznante para Halloween. Consulta el calendario de la biblioteca para la hora y la inscripción.",
 "Kids":"Niños",
 "The town's annual Halloween afternoon of family fun on the Green. Costumes encouraged.":"La tarde anual de Halloween del pueblo, con diversión familiar en el Green. Se recomiendan disfraces.",
 "All ages":"Todas las edades",
 "A Halloween storytime for young kids. Costumes welcome.":"Un cuentacuentos de Halloween para los más pequeños. Se aceptan disfraces.",
 "Ages 4–6":"4–6 años",
 "Where Halloween traditions came from, told through hands-on history.":"De dónde vienen las tradiciones de Halloween, contado con historia práctica.",
 "Ages 8–11":"8–11 años",
 "A monthly evening of board games for the whole family.":"Una noche mensual de juegos de mesa para toda la familia.",
 "A family storytelling celebration, part of the worldwide Tellabration storytelling night.":"Una celebración familiar de narración, parte de la noche mundial de cuentos Tellabration.",
 "Families":"Familias",
 "The bestselling author of the I Survived series visits the library. Registration required.":"La autora superventas de la serie I Survived visita la biblioteca. Inscripción obligatoria.",
 "Kids 7 and up":"Niños desde 7 años",
 "Guilford lights its tree on the Green each December, usually alongside the Guilford Foundation's luminaria. This year's date isn't posted yet.":"Guilford enciende su árbol en el Green cada diciembre, normalmente junto con las luminarias de la Guilford Foundation. La fecha de este año aún no se ha publicado.",
 "Guilford Green":"Guilford Green",
 "Storytimes for babies, twos and preschoolers in fall series, monthly guest storytimes, reading-dog visits four days a week, chess, LEGO and family game nights.":"Cuentacuentos para bebés, niños de dos años y preescolares en series de otoño, cuentacuentos mensuales con invitados, visitas de perros de lectura cuatro días a la semana, ajedrez, LEGO y noches de juegos en familia.",
 "Free":"Gratis",
}

# ---- Playbook pass (Oct 4): classes, museums, farm, bookstore/toy stores ----
DF="dudley-farm"
TOWN["venues"][DF]=["Dudley Farm Museum","2351 Durham Rd, North Guilford"]
TOWN["venueMeta"][DF]=[None,0]
TOWN["events"]+=[
 {"t":"Raptors of Connecticut","v":DF,"when":[W("2026-10-10",[["11:00","12:00"]])],"ages":"Kids and families","a":["preschool","big"],"src":"https://dudleyfarm.com/events/","check":True,
  "blurb":"Meet some of Connecticut's birds of prey in a family program at the Dudley Farm."},
 {"t":"Dudley Farm Harvest Day","v":DF,"special":"fall","when":[W("2026-10-17",[["10:00","14:00"]])],"ages":"All ages","a":B+["big"],"src":"https://dudleyfarm.com/events/",
  "blurb":"The farm museum's annual family harvest festival. Rain date October 24."},
 {"t":"Guilford Farmers' Market at the Dudley Farm","v":DF,"s":[[6,[["09:30","12:30"]],"2026-10-10","2026-10-31"]],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://visitnewhaven.com/events/guilfords-farmers-market-at-the-dudley-farm/",
  "blurb":"Local produce and handmade crafts on the grounds of a farm kept as it was in 1900. Saturdays through October 31."},
]
TOWN["classes"]+=[
 {"id":"gpr-preschool-gym","c":"move","n":"Preschool Gym: Lil' Movers, Tumbling & Stumbling, Movers & Shakers","u":"https://www.guilfordparkrec.com/",
  "blurb":"Long-running Guilford Parks & Rec classes on mats, beams and rings: parent-and-child Lil' Movers for 18 months–3, Tumbling & Stumbling for 3–5 and Movers & Shakers for 5–7. Offered most seasons; check the current brochure for days and fees.",
  "ages":"18 months–7 years (by class)","where":"Nathanael B. Greene Community Center, 32 Church St"},
 {"id":"gpr-martial-arts","c":"move","n":"Kids' Martial Arts","u":"https://www.guilfordparkrec.com/",
  "blurb":"A Parks & Rec martial arts class for young kids covering motor skills, tumbling, basic kicks, pad work and games, with a separate class for older belts. Check the current brochure.",
  "ages":"Ages 3–9 (kids class)","where":"Nathanael B. Greene Community Center, 32 Church St"},
 {"id":"limelite-guilford","c":"dance","n":"Limelite Dance Studio","u":"https://www.limelitedancestudio.com/",
  "blurb":"A dance studio with classes from 18 months through adult and performance teams for ages 5–18. The 2026–27 schedule is posted.",
  "ages":"18 months–adult","where":"17 Water St (also in Madison)"},
 {"id":"guilford-art-center","c":"art","n":"Guilford Art Center","u":"https://www.guilfordartcenter.org/",
  "blurb":"A community art school with classes and workshops for kids alongside its adult studios. Check the catalog for current sessions.",
  "ages":"Kids (varies by class)","where":"Guilford Art Center"},
]
PLACES["out"]=[p if p[0]!="Jacobs Beach" else ("Jacobs Beach","The town beach on Long Island Sound, with calm water, a splash pad and a new playground with shade structures.","La playa del pueblo en el estrecho de Long Island, con agua tranquila, una zona de chorros de agua y un parque infantil nuevo con sombra.") for p in PLACES["out"]]
PLACES["out"]=[p if p[0]!="Dudley Farm Museum" else ("Dudley Farm Museum","A farm museum in North Guilford kept as it was around 1900, with barns, gardens, a Saturday farmers' market through October and a fall Harvest Day.","Un museo granja en North Guilford conservado como era hacia 1900, con graneros, huertos, mercado de agricultores los sábados hasta octubre y un Harvest Day en otoño.") for p in PLACES["out"]]
PLACES["rain"]=[p for p in PLACES["rain"] if p[0] not in ("Henry Whitfield State Museum","Breakwater Books")]
PLACES["rain"]+=[
 ("Henry Whitfield State Museum","Connecticut's oldest house (1639) is closed for restoration in 2026, but the visitor center's archaeology exhibit is open weekdays 10–4, and there's a StoryWalk and pollinator garden outside. Kids 5 and under free.","La casa más antigua de Connecticut (1639) está cerrada por restauración en 2026, pero la exposición de arqueología del centro de visitantes abre entre semana de 10 a 4, y afuera hay un StoryWalk y un jardín de polinizadores. Menores de 5 años gratis."),
 ("Guilford's historic house museums","The Hyland House, the Thomas Griswold House and the Medad Stone Tavern open seasonally for tours and events; check each museum's schedule.","La Hyland House, la Thomas Griswold House y la Medad Stone Tavern abren por temporada para visitas y eventos; consulta el horario de cada museo."),
 ("Breakwater Books","An independent bookstore on the Green (81 Whitfield St) with a dedicated children's room.","Una librería independiente junto al Green (81 Whitfield St) con una sala dedicada a los niños."),
 ("The Purple Bear","An independent toy store on the Green (63 Whitfield St) with free gift wrapping.","Una juguetería independiente junto al Green (63 Whitfield St) con envoltura de regalo gratis."),
 ("Jordie's Toy Shoppe","A toy store at Guilford Commons (1100 Village Walk).","Una juguetería en Guilford Commons (1100 Village Walk)."),
]
ES.update({
 "Meet some of Connecticut's birds of prey in a family program at the Dudley Farm.":"Conoce algunas aves rapaces de Connecticut en un programa familiar en la Dudley Farm.",
 "The farm museum's annual family harvest festival. Rain date October 24.":"El festival familiar anual de la cosecha del museo granja. Fecha en caso de lluvia: 24 de octubre.",
 "Local produce and handmade crafts on the grounds of a farm kept as it was in 1900. Saturdays through October 31.":"Productos locales y artesanías en los terrenos de una granja conservada como en 1900. Los sábados hasta el 31 de octubre.",
 "Long-running Guilford Parks & Rec classes on mats, beams and rings: parent-and-child Lil' Movers for 18 months–3, Tumbling & Stumbling for 3–5 and Movers & Shakers for 5–7. Offered most seasons; check the current brochure for days and fees.":"Clases de larga trayectoria de Guilford Parks & Rec con colchonetas, barras y aros: Lil' Movers con un adulto para 18 meses–3 años, Tumbling & Stumbling para 3–5 y Movers & Shakers para 5–7. Se ofrecen casi todas las temporadas; consulta el folleto actual para días y precios.",
 "Preschool Gym: Lil' Movers, Tumbling & Stumbling, Movers & Shakers":"Gimnasia preescolar: Lil' Movers, Tumbling & Stumbling, Movers & Shakers",
 "18 months–7 years (by class)":"18 meses–7 años (según la clase)",
 "Nathanael B. Greene Community Center, 32 Church St":"Nathanael B. Greene Community Center, 32 Church St",
 "A Parks & Rec martial arts class for young kids covering motor skills, tumbling, basic kicks, pad work and games, with a separate class for older belts. Check the current brochure.":"Una clase de artes marciales de Parks & Rec para niños pequeños con motricidad, volteretas, patadas básicas, trabajo con almohadillas y juegos, y otra clase para cinturones más avanzados. Consulta el folleto actual.",
 "Kids' Martial Arts":"Artes marciales para niños",
 "Ages 3–9 (kids class)":"3–9 años (clase infantil)",
 "A dance studio with classes from 18 months through adult and performance teams for ages 5–18. The 2026–27 schedule is posted.":"Una escuela de danza con clases desde los 18 meses hasta adultos y equipos de presentación para 5–18 años. El horario 2026–27 ya está publicado.",
 "18 months–adult":"18 meses–adultos",
 "17 Water St (also in Madison)":"17 Water St (también en Madison)",
 "A community art school with classes and workshops for kids alongside its adult studios. Check the catalog for current sessions.":"Una escuela comunitaria de arte con clases y talleres para niños además de sus talleres para adultos. Consulta el catálogo para las sesiones actuales.",
 "Kids (varies by class)":"Niños (varía según la clase)",
})

ES.update({"The town's annual Halloween afternoon of family fun on the Green, run by Guilford Parks & Rec. Costumes encouraged. If it rains, it moves to the Guilford Community Center (32 Church St).":"La tarde anual de Halloween del pueblo, con diversión familiar en el Green, organizada por Guilford Parks & Rec. Se recomiendan disfraces. Si llueve, se traslada al Guilford Community Center (32 Church St)."})

# ---- patch: guilford-2026-10-08.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
# Full playbook re-run, Oct 8 2026
GAC="guilford-art-center"; BO="bishops"
TOWN["venues"].update({GAC:["Guilford Art Center","411 Church St"],BO:["Bishop's Orchards (pick-your-own fields)","480 New England Rd"]})
TOWN["venueMeta"].update({GAC:[None,1],BO:[None,0]})
for e in TOWN["events"]:
    if e["t"]=="Time for Twos": e["when"]=[w for w in e["when"] if w["from"]!="2026-10-13"]
    if e["t"]=="Babytime":
        for w in e["when"]:
            if w["from"]=="2026-10-15": w["from"]="2026-10-14"
    if e["t"]=="Junior Chess Class": e["price"]="Free (full; waitlist only)"
GA="https://guilfordartcenter.org/classes/"
TOWN["events"]+=[
 {"t":"Bishop's Fall Festival","v":BO,"special":"fall","when":[{"from":"2026-10-08","to":"2026-11-01","t":[["10:00","17:00"]]}],"ages":"All ages","a":B+["big"],"free":False,"price":"$10–18 all-access (2 and under free)","drop":True,"src":"https://www.bishopsorchards.com/fall-festival",
  "blurb":"A 4-acre corn maze, bounce pads, gem mining, Tire Mountain and pedal karts, plus pick-your-own apples, pears and pumpkins. The Apple Train, Mega Slide and wagon rides run on weekends; cheaper on weekdays."},
 {"t":"CT Spooky Writing Contest","v":"guilford-library","special":"hw","when":[{"from":"2026-10-08","to":"2026-10-31","t":[]}],"ages":"Children's category ages 6–11","a":["big"],"free":True,"price":"Free","src":"https://guilfordfreelibrary.org/events/event/ct-spooky-writing-contest/",
  "blurb":"Write an original spooky story set in Connecticut and submit it online by Oct 31. Winners get a prize and are published in the library's Spooky CT volume."},
 {"t":"Kids' Magical Halloween Workshop","v":GAC,"special":"hw","when":[W("2026-10-24",[["12:30","15:00"]])],"ages":"Ages 5+","a":["preschool","big"],"free":False,"price":"$37.50 + $20 materials","rsvp":True,"src":GA+"kids-magical-halloween-workshop/",
  "blurb":"Clay and mixed-media spooky art: witches, animal familiars, luminaries and potions."},
 {"t":"Day of the Dead Workshop","v":GAC,"special":"hw","when":[W("2026-11-01",[["12:00","14:30"]])],"ages":"Ages 7+","a":["big"],"free":False,"price":"$37.50 + $15 materials","rsvp":True,"src":GA+"mexican-day-of-the-dead-workshop/",
  "blurb":"Make a clay skull luminary and decorate it with jewels, sequins and marigolds."},
 {"t":"Thanksgiving Harvest Baskets Workshop","v":GAC,"when":[W("2026-11-21",[["12:00","14:30"]])],"ages":"Ages 7+","a":["big"],"free":False,"price":"$37.50 + $20 materials","rsvp":True,"src":GA+"thanksgiving-harvest-baskets-workshop/",
  "blurb":"Kids make a clay cornucopia centerpiece with mini pumpkins, acorns and corn, plus a personalized placemat for the holiday table."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Santa's Workshop","w":"Guilford Community Center, 32 Church St","p":"Parks & Rec's photos with Santa, holiday crafts, pizza and dessert, the same Friday as the tree lighting ($35 per family, register ahead). Last year it was Dec 5, 4–5:30. This year's date isn't posted yet.","src":"https://new.patch.com/connecticut/guilford/calendar/event/20251205/20741e3f-91c3-45b6-a930-8e3ec62d8e1c/santas-workshop"},
 {"g":"hol","t":"Holiday Market at Dudley Farm","w":"Dudley Farm, 2351 Durham Rd, North Guilford","p":"A free market with 30+ artisans in the Munger Barn plus a paper-ornament craft in the decorated farmhouse, the first two weekends of December, 10–2. This year's dates aren't posted yet.","src":"https://ctvisit.com/events/holiday-market-dudley-farm"},
 {"g":"hol","t":"Fire & Ice Menorah Lighting","w":"Guilford Green","p":"Chabad of the Shoreline carves a giant ice menorah and dreidel on the Green, with donuts, cider and free menorahs. It happens during Hanukkah (Dec 4–12 this year); the date isn't posted yet.","src":"https://events.newhavenarts.org/events/fire-ice-menorah-lighting-on-the-guilford-green"},
 {"g":"hol","t":"Drop & Shop Art Workshops","w":"Guilford Art Center, 411 Church St","p":"Kids make art for two hours while parents shop the Holiday Expo ($25 per child, register ahead). Last year: Saturdays Dec 13 and 20, 12–2. This year's dates aren't posted yet.","src":"https://patch.com/connecticut/guilford/calendar/event/20251213/24c1aff4-8c29-402c-bdd1-84a445ccd349/guilford-art-center-helps-parents-check-off-holiday-lists-with-drop-shop-art-workshops"},
]
ES_PATCH={
 "Free (full; waitlist only)":"Gratis (lleno; solo lista de espera)",
 "$10–18 all-access (2 and under free)":"$10–18 acceso total (2 años o menos gratis)",
 "A 4-acre corn maze, bounce pads, gem mining, Tire Mountain and pedal karts, plus pick-your-own apples, pears and pumpkins. The Apple Train, Mega Slide and wagon rides run on weekends; cheaper on weekdays.":"Un laberinto de maíz de 1.6 hectáreas, colchones inflables, búsqueda de gemas, Tire Mountain y karts de pedales, además de cosecha de manzanas, peras y calabazas. El Apple Train, el Mega Slide y los paseos en carreta funcionan los fines de semana; más barato entre semana.",
 "Children's category ages 6–11":"Categoría infantil 6–11 años",
 "Write an original spooky story set in Connecticut and submit it online by Oct 31. Winners get a prize and are published in the library's Spooky CT volume.":"Escribe un cuento de miedo original ambientado en Connecticut y envíalo en línea antes del 31 de oct. Los ganadores reciben un premio y se publican en el volumen Spooky CT de la biblioteca.",
 "Ages 5+":"5 años o más",
 "$37.50 + $20 materials":"$37.50 + $20 de materiales",
 "Clay and mixed-media spooky art: witches, animal familiars, luminaries and potions.":"Arte espeluznante con barro y técnicas mixtas: brujas, animales mágicos, farolitos y pociones.",
 "Ages 7+":"7 años o más",
 "$37.50 + $15 materials":"$37.50 + $15 de materiales",
 "Make a clay skull luminary and decorate it with jewels, sequins and marigolds.":"Haz un farolito de calavera de barro y decóralo con joyas, lentejuelas y cempasúchil.",
 "Kids make a clay cornucopia centerpiece with mini pumpkins, acorns and corn, plus a personalized placemat for the holiday table.":"Los niños hacen un centro de mesa de cornucopia de barro con minicalabazas, bellotas y maíz, además de un mantelito personalizado para la mesa festiva.",
 "Guilford Community Center, 32 Church St":"Guilford Community Center, 32 Church St",
 "Parks & Rec's photos with Santa, holiday crafts, pizza and dessert, the same Friday as the tree lighting ($35 per family, register ahead). Last year it was Dec 5, 4–5:30. This year's date isn't posted yet.":"Fotos con Santa, manualidades navideñas, pizza y postre de Parks & Rec, el mismo viernes del encendido del árbol ($35 por familia, con inscripción). El año pasado fue el 5 de dic., de 4 a 5:30. La fecha de este año aún no se ha publicado.",
 "Dudley Farm, 2351 Durham Rd, North Guilford":"Dudley Farm, 2351 Durham Rd, North Guilford",
 "A free market with 30+ artisans in the Munger Barn plus a paper-ornament craft in the decorated farmhouse, the first two weekends of December, 10–2. This year's dates aren't posted yet.":"Un mercado gratis con más de 30 artesanos en el Munger Barn y una manualidad de adornos de papel en la casa de la granja decorada, los dos primeros fines de semana de diciembre, de 10 a 2. Las fechas de este año aún no se han publicado.",
 "Guilford Green":"Guilford Green",
 "Chabad of the Shoreline carves a giant ice menorah and dreidel on the Green, with donuts, cider and free menorahs. It happens during Hanukkah (Dec 4–12 this year); the date isn't posted yet.":"Chabad of the Shoreline talla una menorá y un dreidel gigantes de hielo en el Green, con donas, sidra y menorás gratis. Es durante Janucá (del 4 al 12 de dic. este año); la fecha aún no se ha publicado.",
 "Guilford Art Center, 411 Church St":"Guilford Art Center, 411 Church St",
 "Kids make art for two hours while parents shop the Holiday Expo ($25 per child, register ahead). Last year: Saturdays Dec 13 and 20, 12–2. This year's dates aren't posted yet.":"Los niños hacen arte durante dos horas mientras los padres compran en el Holiday Expo ($25 por niño, con inscripción). El año pasado: sábados 13 y 20 de dic., de 12 a 2. Las fechas de este año aún no se han publicado.",
}

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
