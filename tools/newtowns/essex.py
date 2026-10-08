W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
EL="essex-library"; IL="ivoryton-library"
SRC_E="https://www.youressexlibrary.org/"; SRC_T="https://essexct.com/events/category/activity/"
B=["baby","toddler","preschool"]
def ev(v,src,**k):
    e={"v":v,"free":True,"price":"Free","src":src}; e.update(k); return e
TOWN={
 "display":"Essex","accent":"#D6C8EC",
 "hoods":[["essex","Essex Village"],["centerbrook","Centerbrook"],["ivoryton","Ivoryton"]],
 "venues":{EL:["Essex Library","33 West Ave"],IL:["Ivoryton Library","106 Main St, Ivoryton"],
   "essex-fire":["Essex Fire Department","11 Saybrook Rd"],"millrace":["The Millrace Preserve","Ivory St, Ivoryton"],
   "steam-train":["Essex Steam Train & Riverboat","1 Railroad Ave"],"essex-po":["Essex Post Office (parade meeting point)","12 Main St"],
   "brickside":["Brickside Pizza","Ivoryton"],"villages":["Essex, Centerbrook and Ivoryton Main Streets","All three villages"],"ivoryton-village":["Ivoryton Village","Main St, Ivoryton"]},
 "venueMeta":{EL:["essex",1],IL:["ivoryton",1],"essex-fire":["centerbrook",0],"millrace":["ivoryton",0],"steam-train":["centerbrook",1],"essex-po":["essex",0],"brickside":["ivoryton",1],"villages":[None,0],"ivoryton-village":["ivoryton",0]},
 "events":[
  ev(EL,SRC_E,t="Wiggle Worms Story Time",when=D(["2026-10-06","2026-10-13","2026-10-20","2026-10-27"],[["09:30","10:00"],["10:30","11:00"]]),ages="Birth–age 3 + caregiver",a=["baby","toddler"],drop=True,check=True,
     blurb="A play-based music-and-movement storytime with shakers, scarves and stories, then play in the Children's Room. Pick one session; no registration. November dates aren't posted yet."),
  ev(EL,SRC_E,t="Little Learners Story Time",when=D(["2026-10-09","2026-10-23","2026-10-30"],[["10:00","11:00"]]),ages="Ages 2–5",a=["toddler","preschool"],rsvp=True,
     blurb="Themed stories, songs and craft-and-play centers that build kindergarten readiness: firefighters (Oct 9), pumpkin patch (Oct 23) and Halloween costumes (Oct 30)."),
  ev(EL,SRC_E,t="Baby & Toddler Wednesdays",when=D(["2026-10-07","2026-10-14","2026-10-21","2026-10-28"],[["10:00","11:00"]]),ages="Birth–age 4 + caregiver",a=["baby","toddler"],check=True,
     blurb="A different program each week: Sensory Playtime (Oct 7, drop in), Baby Keepsake pumpkin prints (Oct 14), Baby Band (Oct 21) and Baby Playtime (Oct 28). Some need registration."),
  ev(EL,SRC_E,t="Louie Listens",when=[W("2026-10-06",[["17:15","18:00"]])],ages="Kids of all ages",a=["big"],rsvp=True,
     blurb="Sign up for a private 15-minute slot to read to Louie, a licensed therapy dog."),
  ev("essex-fire",SRC_E,t="Essex Touch-A-Truck",special="fall",when=[W("2026-10-10",[["10:00","12:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="Storytime at 10, then climb into fire trucks, police cars, ambulances and public works vehicles and meet the people who drive them. Canceled if it rains."),
  ev(EL,SRC_E,t="STEAM Saturday: Spider Web Slime",special="hw",when=[W("2026-10-10",[["14:30","15:30"]])],ages="Ages 5–12",a=["big"],rsvp=True,
     blurb="Make stretchy spider-web slime and learn the science of non-Newtonian fluids. Wear clothes that can get messy."),
  ev(EL,SRC_E,t="Tween Time: Ramen Taste Test",when=[W("2026-10-23",[["15:30","16:30"]])],ages="Ages 8–12",a=["big"],rsvp=True,
     blurb="Taste ramen flavors from around the world and crown a noodle champion for National Noodle Day."),
  ev("millrace",SRC_E,t="Trek-or-Treat Hike",special="hw",when=[W("2026-10-24",[["11:30","13:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="A short self-guided family hike with Halloween riddles, a treat and a take-home craft, part of the Ivoryton Pumpkin Festival. Canceled if it rains."),
  ev("ivoryton-village",SRC_T,t="Ivoryton Village Pumpkin Festival",special="hw",when=[W("2026-10-24",[])],ages="All ages",a=B+["big"],check=True,
     blurb="Ivoryton's fall festival day, with carved pumpkins and family activities around the village. Check the festival's listing for times."),
  ev(EL,SRC_E,t="Spooky Candles",special="hw",when=[W("2026-10-24",[["14:00","15:00"]])],ages="Ages 8–18",a=["big"],rsvp=True,
     blurb="Decorate festive candles with spooky temporary tattoos. Registration required."),
  ev(EL,SRC_E,t="Trick or Treat at the Library",special="hw",when=[W("2026-10-31",[["09:00","16:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="Come in costume, say the magic words and get a treat (one per child)."),
  ev("essex-po",SRC_E,t="Essex Halloween Parade",special="hw",when=[W("2026-10-31",[["17:30"]])],ages="All ages",a=B+["big"],check=True,
     blurb="The annual costume parade through Essex Village. Families can march with the Essex Library's group (registration required), meeting at the Post Office."),
  ev("villages",SRC_T,t="Scarecrow Contest & FestiFall",special="fall",when=[{"from":"2026-10-01","to":"2026-10-31","t":[]}],ages="All ages",a=B+["big"],
     blurb="All month, scarecrows line the main streets of Essex, Centerbrook and Ivoryton. Stroll, vote for favorites and enjoy fall in the villages."),
  ev("brickside",SRC_T,t="Kids' Spooky Canvas Painting",special="hw",price="$20",free=False,when=[W("2026-10-09",[["12:00"]])],ages="Kids",a=["big"],rsvp=True,check=True,
     blurb="A guided Halloween canvas-painting session for kids at Brickside Pizza."),
  ev("brickside",SRC_T,t="Free Pumpkin Carving",special="hw",when=[W("2026-10-21",[["16:00","18:00"]])],ages="Kids and families",a=["preschool","big"],check=True,
     blurb="Carve a pumpkin to display at the Ivoryton Pumpkin Festival."),
  ev(IL,SRC_T,t="Ivoryton Library Kids' Afternoons",when=[W("2026-10-14",[["16:00","17:00"]]),W("2026-10-21",[["16:00","17:00"]]),W("2026-10-23",[["15:30","16:30"]]),W("2026-11-10",[["15:30","16:30"]]),W("2026-11-24",[["15:30","16:30"]]),W("2026-12-07",[["15:30","16:30"]]),W("2026-12-21",[["15:30","16:30"]])],ages="Kids",a=["preschool","big"],
     blurb="After-school fun at the Ivoryton Library: National Dessert Day (Oct 14), a superhero party (Oct 21), book decorating (Oct 23), Vanilla Cupcake Day (Nov 10), Thanksgiving crafts (Nov 24), a slime party (Dec 7) and the winter solstice (Dec 21)."),
  ev(IL,SRC_T,t="Noon-ish New Year's Eve Party",special="hol",when=[W("2026-12-31",[["11:00","12:00"]])],ages="Young children",a=B,
     blurb="Ring in the new year at noon with the Ivoryton Library."),
  {"t":"North Pole Express","v":"steam-train","special":"hol","when":[W("2026-11-20",[["16:00","20:00"]]),W("2026-11-27",[["14:00","20:00"]]),W("2026-12-23",[["14:00","20:00"]])],
   "s":[[6,[["14:00","20:00"]],"2026-11-21","2026-12-20"],[0,[["14:00","20:00"]],"2026-11-22","2026-12-20"],[2,[["16:00","20:00"]],"2026-12-01","2026-12-22"],[3,[["16:00","20:00"]],"2026-12-02","2026-12-16"],[4,[["16:00","20:00"]],"2026-12-03","2026-12-17"],[5,[["16:00","20:00"]],"2026-12-04","2026-12-18"]],
   "ages":"All ages","a":B+["big"],"free":False,"price":"$60–$70 per coach seat","ticket":True,"check":True,
   "blurb":"A 90-minute evening ride to the North Pole on a vintage train. Departures run every 30 minutes (afternoons and evenings on weekends, evenings on weekdays). Tickets are online only and sell out.","src":"https://essexsteamtrain.com/"},
 ],
 "tba":[{"g":"hol","t":"Trees in the Rigging","w":"Essex waterfront and Main Street",
   "p":"Essex's holiday boat parade and carol stroll, when lighted boats sail past the Connecticut River Museum. Usually the Sunday after Thanksgiving; this year's details aren't posted yet.","src":"https://ctrivermuseum.org/"},
  {"g":"hol","t":"Holiday Train Show at the Connecticut River Museum","w":"Connecticut River Museum, 67 Main St",
   "p":"A big model-train layout with I Spy hunts and a toddler-height layout, usually opening just before Thanksgiving and running into February. Included with admission. This year's dates aren't posted yet.","src":"https://ctrivermuseum.org/"}],
 "classes":[],
 "library":{"for":"Free, every week","name":"Essex Library & Ivoryton Library","desc":"Essex Library runs Wiggle Worms and Little Learners storytimes, baby programs and a Touch-A-Truck; the Ivoryton Library hosts after-school parties and a Noon-ish New Year's Eve.","a":"See the Essex Library calendar","href":SRC_E},
}
PLACES={
 "out":[("Essex Steam Train & Riverboat","Vintage steam-train rides through the Connecticut River valley, with riverboat cruises in season.","Paseos en tren de vapor antiguo por el valle del río Connecticut, con cruceros por el río en temporada."),
        ("Essex Village & the waterfront","A walkable Main Street that ends at the river, with boats, shops and the town dock.","Una Main Street para caminar que termina en el río, con barcos, tiendas y el muelle del pueblo."),
        ("Essex Land Trust preserves","Short, easy trails like The Millrace in Ivoryton, good for little hikers.","Senderos cortos y fáciles como The Millrace en Ivoryton, ideales para pequeños excursionistas.")],
 "rain":[("Connecticut River Museum","Hands-on exhibits about the river, a replica of the first submarine, and a holiday train show in winter.","Exposiciones prácticas sobre el río, una réplica del primer submarino y una exhibición de trenes en invierno."),
         ("Essex Library","Storytimes, baby programs and STEAM Saturdays.","Cuentacuentos, programas para bebés y STEAM Saturdays."),
         ("Ivoryton Library","A small village library with after-school parties and holiday programs.","Una pequeña biblioteca de pueblo con fiestas después de clases y programas festivos."),
         ("Ivoryton Playhouse","A historic village theater; check its season for family-friendly shows.","Un teatro histórico de pueblo; consulta su temporada para funciones familiares.")],
 "drive":[("The Kate (Old Saybrook)","A restored Main Street theater with films and concerts and a free small Katharine Hepburn museum.","Un teatro restaurado en Main Street con películas y conciertos y un pequeño museo gratis de Katharine Hepburn."),
          ("Hammonasset Beach State Park","Connecticut's longest public beach, plus the Meigs Point Nature Center, in Madison.","La playa pública más larga de Connecticut, además del Meigs Point Nature Center, en Madison."),
          ("Bishop's Orchards","Pick-your-own fruit, pumpkins, a farm market and creamery in Guilford.","Frutas para cosechar, calabazas, mercado y heladería en Guilford.")],
}
ES={
 "A play-based music-and-movement storytime with shakers, scarves and stories, then play in the Children's Room. Pick one session; no registration. November dates aren't posted yet.":"Un cuentacuentos de música y movimiento basado en el juego, con maracas, pañuelos y cuentos, y luego juego en la sala infantil. Elige una sesión; sin inscripción. Las fechas de noviembre aún no se han publicado.",
 "Birth–age 3 + caregiver":"0–3 años + un adulto",
 "Themed stories, songs and craft-and-play centers that build kindergarten readiness: firefighters (Oct 9), pumpkin patch (Oct 23) and Halloween costumes (Oct 30).":"Cuentos temáticos, canciones y centros de manualidades y juego que preparan para el kínder: bomberos (9 de oct.), huerto de calabazas (23 de oct.) y disfraces de Halloween (30 de oct.).",
 "Ages 2–5":"2–5 años",
 "A different program each week: Sensory Playtime (Oct 7, drop in), Baby Keepsake pumpkin prints (Oct 14), Baby Band (Oct 21) and Baby Playtime (Oct 28). Some need registration.":"Un programa distinto cada semana: juego sensorial (7 de oct., sin inscripción), huellas de bebé en calabaza (14 de oct.), Baby Band (21 de oct.) y juego para bebés (28 de oct.). Algunos requieren inscripción.",
 "Birth–age 4 + caregiver":"0–4 años + un adulto",
 "Sign up for a private 15-minute slot to read to Louie, a licensed therapy dog.":"Inscríbete para un turno privado de 15 minutos para leerle a Louie, un perro de terapia certificado.",
 "Kids of all ages":"Niños de todas las edades",
 "Storytime at 10, then climb into fire trucks, police cars, ambulances and public works vehicles and meet the people who drive them. Canceled if it rains.":"Cuentacuentos a las 10 y luego súbete a camiones de bomberos, patrullas, ambulancias y vehículos de obras públicas y conoce a quienes los manejan. Se cancela si llueve.",
 "All ages":"Todas las edades",
 "Make stretchy spider-web slime and learn the science of non-Newtonian fluids. Wear clothes that can get messy.":"Haz slime elástico de telaraña y aprende la ciencia de los fluidos no newtonianos. Usa ropa que se pueda ensuciar.",
 "Ages 5–12":"5–12 años",
 "Taste ramen flavors from around the world and crown a noodle champion for National Noodle Day.":"Prueba sabores de ramen de todo el mundo y corona al campeón de los fideos por el Día Nacional del Fideo.",
 "Ages 8–12":"8–12 años",
 "A short self-guided family hike with Halloween riddles, a treat and a take-home craft, part of the Ivoryton Pumpkin Festival. Canceled if it rains.":"Una caminata familiar corta y autoguiada con acertijos de Halloween, un dulce y una manualidad para llevar, como parte del Ivoryton Pumpkin Festival. Se cancela si llueve.",
 "Ivoryton's fall festival day, with carved pumpkins and family activities around the village. Check the festival's listing for times.":"El día del festival de otoño de Ivoryton, con calabazas talladas y actividades familiares por el pueblo. Consulta el anuncio del festival para los horarios.",
 "Decorate festive candles with spooky temporary tattoos. Registration required.":"Decora velas festivas con tatuajes temporales espeluznantes. Inscripción obligatoria.",
 "Ages 8–18":"8–18 años",
 "Come in costume, say the magic words and get a treat (one per child).":"Ven disfrazado, di las palabras mágicas y recibe un dulce (uno por niño).",
 "The annual costume parade through Essex Village. Families can march with the Essex Library's group (registration required), meeting at the Post Office.":"El desfile anual de disfraces por Essex Village. Las familias pueden desfilar con el grupo de la Essex Library (inscripción obligatoria), con punto de encuentro en la oficina de correos.",
 "All month, scarecrows line the main streets of Essex, Centerbrook and Ivoryton. Stroll, vote for favorites and enjoy fall in the villages.":"Todo el mes, espantapájaros adornan las calles principales de Essex, Centerbrook e Ivoryton. Pasea, vota por tus favoritos y disfruta el otoño en los pueblos.",
 "A guided Halloween canvas-painting session for kids at Brickside Pizza.":"Una sesión guiada de pintura de Halloween en lienzo para niños en Brickside Pizza.",
 "Kids":"Niños",
 "Carve a pumpkin to display at the Ivoryton Pumpkin Festival.":"Talla una calabaza para exhibirla en el Ivoryton Pumpkin Festival.",
 "Kids and families":"Niños y familias",
 "After-school fun at the Ivoryton Library: National Dessert Day (Oct 14), a superhero party (Oct 21), book decorating (Oct 23), Vanilla Cupcake Day (Nov 10), Thanksgiving crafts (Nov 24), a slime party (Dec 7) and the winter solstice (Dec 21).":"Diversión después de clases en la Ivoryton Library: Día Nacional del Postre (14 de oct.), una fiesta de superhéroes (21 de oct.), decoración de libros (23 de oct.), Día del Cupcake de Vainilla (10 de nov.), manualidades de Acción de Gracias (24 de nov.), una fiesta de slime (7 de dic.) y el solsticio de invierno (21 de dic.).",
 "Ring in the new year at noon with the Ivoryton Library.":"Recibe el año nuevo al mediodía con la Ivoryton Library.",
 "Young children":"Niños pequeños",
 "A 90-minute evening ride to the North Pole on a vintage train. Departures run every 30 minutes (afternoons and evenings on weekends, evenings on weekdays). Tickets are online only and sell out.":"Un viaje de 90 minutos al Polo Norte en un tren antiguo. Hay salidas cada 30 minutos (tardes y noches los fines de semana, noches entre semana). Los boletos solo se venden en línea y se agotan.",
 "$60–$70 per coach seat":"$60–$70 por asiento en coche",
 "Essex's holiday boat parade and carol stroll, when lighted boats sail past the Connecticut River Museum. Usually the Sunday after Thanksgiving; this year's details aren't posted yet.":"El desfile navideño de barcos y paseo de villancicos de Essex, cuando barcos iluminados pasan frente al Connecticut River Museum. Suele ser el domingo después de Acción de Gracias; los detalles de este año aún no se han publicado.",
 "Essex waterfront and Main Street":"Frente al río y Main Street de Essex",
 "A big model-train layout with I Spy hunts and a toddler-height layout, usually opening just before Thanksgiving and running into February. Included with admission. This year's dates aren't posted yet.":"Una gran maqueta de trenes con juegos de buscar objetos y una maqueta a la altura de los pequeños; suele abrir justo antes de Acción de Gracias y seguir hasta febrero. Incluida con la entrada. Las fechas de este año aún no se han publicado.",
 "Connecticut River Museum, 67 Main St":"Connecticut River Museum, 67 Main St",
 "Essex Library runs Wiggle Worms and Little Learners storytimes, baby programs and a Touch-A-Truck; the Ivoryton Library hosts after-school parties and a Noon-ish New Year's Eve.":"La Essex Library ofrece los cuentacuentos Wiggle Worms y Little Learners, programas para bebés y un Touch-A-Truck; la Ivoryton Library organiza fiestas después de clases y un Noon-ish New Year's Eve.",
 "Free":"Gratis",
 "$20":"$20",
}

# ---- Playbook pass (Oct 4) ----
BH="bushy-hill"
TOWN["venues"][BH]=["Bushy Hill Nature Center","253 Bushy Hill Rd, Ivoryton"]
TOWN["venueMeta"][BH]=["ivoryton",0]
TOWN["venues"]["walnut-main"]=["Walnut St & Main St (parade start)","Ivoryton"]
TOWN["venueMeta"]["walnut-main"]=["ivoryton",0]
PF="https://essexct.recdesk.com/Community/Page?pageId=513"
for e in TOWN["events"]:
    if e["t"]=="Ivoryton Village Pumpkin Festival":
        e["src"]=PF
        e["blurb"]="Ivoryton's fall festival with hayrides, trunk-or-treat, cookie decorating, face painting, live music (5–7 pm) and an evening Pumpkin Stroll of carved pumpkins. Check the town's festival page for the full schedule."
TOWN["events"]+=[
 {"t":"Pumpkin Carving Party at Bushy Hill","v":BH,"special":"hw","when":[W("2026-10-24",[["10:00","12:00"]])],"ages":"All ages","a":["preschool","big"],"src":PF,"check":True,
  "blurb":"Carve a pumpkin to be displayed in the Ivoryton Pumpkin Festival's evening Pumpkin Stroll. All ages and skill levels welcome."},
 {"t":"Ivoryton Costume Parade","v":"walnut-main","special":"hw","when":[W("2026-10-24",[["16:30"]])],"ages":"Kids 12 and under (all welcome)","a":B+["big"],"free":True,"price":"Free","drop":True,"src":PF,"check":True,
  "blurb":"The Pumpkin Festival's costume parade steps off from Walnut and Main Street and winds through the heart of the village."},
]
TOWN["classes"]+=[
 {"id":"bushy-hill","c":"nature","n":"Bushy Hill Nature Center","u":"https://www.bushyhill.org/",
  "blurb":"Outdoor and wilderness education on 700 acres: community workshops, school-vacation days and summer camp, run by Incarnation Center.",
  "ages":"Kids (varies by program)","where":"253 Bushy Hill Rd, Ivoryton"},
 {"id":"natures-playground","c":"nature","n":"Nature's Playground After School","u":"https://incarnationcenter.org/education/natures-playground/",
  "blurb":"An outdoor after-school program with homework help, hiking, farming, fishing and wilderness skills. Buses from Essex and Deep River elementary schools; full days on school vacation days.",
  "ages":"Elementary school","where":"253 Bushy Hill Rd, Ivoryton"},
]
PLACES["rain"].append(("Toys Ahoy!","The village toy store at 43 Main St, with an eclectic mix of toys, games and children's books, and a friendly shop dog.","La juguetería del pueblo en 43 Main St, con una mezcla ecléctica de juguetes, juegos y libros infantiles, y un simpático perro de la tienda."))
PLACES["out"].append(("Bushy Hill Nature Center","700 acres of woods, fields and a lake in Ivoryton, with community workshops and school-vacation programs.","700 acres de bosques, campos y un lago en Ivoryton, con talleres comunitarios y programas en vacaciones escolares."))
ES.update({
 "Ivoryton's fall festival with hayrides, trunk-or-treat, cookie decorating, face painting, live music (5–7 pm) and an evening Pumpkin Stroll of carved pumpkins. Check the town's festival page for the full schedule.":"El festival de otoño de Ivoryton con paseos en carreta de heno, dulces desde los autos, decoración de galletas, pintura de caras, música en vivo (5–7 pm) y un paseo nocturno entre calabazas talladas. Consulta la página del festival para el programa completo.",
 "Carve a pumpkin to be displayed in the Ivoryton Pumpkin Festival's evening Pumpkin Stroll. All ages and skill levels welcome.":"Talla una calabaza para exhibirla en el paseo nocturno de calabazas del Ivoryton Pumpkin Festival. Todas las edades y niveles son bienvenidos.",
 "The Pumpkin Festival's costume parade steps off from Walnut and Main Street and winds through the heart of the village.":"El desfile de disfraces del Pumpkin Festival sale de Walnut y Main Street y recorre el corazón del pueblo.",
 "Kids 12 and under (all welcome)":"Niños de 12 años o menos (todos bienvenidos)",
 "Outdoor and wilderness education on 700 acres: community workshops, school-vacation days and summer camp, run by Incarnation Center.":"Educación al aire libre y en la naturaleza en 700 acres: talleres comunitarios, días de vacaciones escolares y campamento de verano, a cargo de Incarnation Center.",
 "Kids (varies by program)":"Niños (varía según el programa)",
 "253 Bushy Hill Rd, Ivoryton":"253 Bushy Hill Rd, Ivoryton",
 "An outdoor after-school program with homework help, hiking, farming, fishing and wilderness skills. Buses from Essex and Deep River elementary schools; full days on school vacation days.":"Un programa al aire libre después de clases con ayuda con la tarea, caminatas, granja, pesca y habilidades de supervivencia. Autobuses desde las primarias de Essex y Deep River; días completos en vacaciones escolares.",
 "Nature's Playground After School":"Nature's Playground después de clases",
 "Elementary school":"Primaria",
})

# ---- patch: essex-2026-10-08.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
# Full playbook re-run, Oct 8 2026
CRM="ctrm"; ATR="atrium-6-main"; IVP="ivoryton-playhouse"
TOWN["venues"].update({CRM:["Connecticut River Museum","67 Main St"],ATR:["The Atrium at 6 Main","6 Main St, Centerbrook"],IVP:["Ivoryton Playhouse","103 Main St, Ivoryton"]})
TOWN["venueMeta"].update({CRM:[None,1],ATR:[None,1],IVP:[None,1]})
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"] not in ("Trees in the Rigging","Holiday Train Show at the Connecticut River Museum")]
for e in TOWN["events"]:
    if e["t"]=="Ivoryton Village Pumpkin Festival":
        e["blurb"]="Ivoryton's fall festival with hayrides, cookie decorating, face painting, live music (5–7 pm), a trunk-or-treat on the Village Green (5–7 pm) and an evening Pumpkin Stroll of carved pumpkins."
        e["src"]="https://www.ivorytonalliance.org/events"
TOWN["events"]+=[
 {"t":"Holiday Train Show","v":CRM,"special":"hol","when":[{"from":"2026-11-19","to":"2027-01-31","t":[]}],"ages":"All ages","a":B+["big"],"free":False,"price":"Museum admission ($15 adults, $5 ages 6–12, under 5 free)","drop":True,"src":"https://ctrivermuseum.org/events/steve-cryans-33rd-annual-train-show/",
  "blurb":"Steve Cryan's 33rd annual model-train layout on the museum's third floor, with a locomotive scavenger hunt. Open Tuesday–Sunday 10–5; closed Mondays, Thanksgiving and Christmas."},
 {"t":"Trees in the Rigging","v":CRM,"special":"hol","when":[W("2026-11-29",[["12:00","17:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free outdoors; museum admission for inside","drop":True,"check":True,"src":"https://ctrivermuseum.org/events/trees-in-the-rigging-2026/",
  "blurb":"Essex's holiday celebration: a kids' craft in the Boathouse at noon, hot chocolate at 4, a carol parade from Town Hall at 4:30 and a lighted boat parade on the river at 5."},
 {"t":"Playhouse Holiday Jamboree: Christmas Americana","v":IVP,"special":"hol","when":[{"from":"2026-11-19","to":"2026-12-20","t":[]}],"ages":"All ages","a":["big"],"free":False,"price":"$60 adults, $25 students","rsvp":True,"src":"https://www.ivorytonplayhouse.org/our-season/playhouse-holiday-jamboree-2",
  "blurb":"A family-friendly musical revue of American Christmas carols and stories, staged like an old-time radio show. Evenings Thursday–Saturday at 7:30; matinees Wednesday, Thursday, Saturday and Sunday at 2."},
 {"t":"Holiday Princess Jubilee","v":ATR,"special":"hol","when":D(["2026-12-05","2026-12-06"],[["11:00","13:00"]]),"ages":"Ages 2+","a":["toddler","preschool","big"],"free":False,"price":"$89.99 per person","rsvp":True,"src":"https://essexsteamtrain.com/holiday-princess-jubilee/",
  "blurb":"An Essex Steam Train princess brunch with face decorating, snowflake ornaments, letters to Santa, a story and games. No train ride included."},
 {"t":"Ivoryton Illuminations","v":"ivoryton-village","special":"hol","when":[{"from":"2026-12-05","to":"2026-12-31","t":[]}],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://www.ivorytonalliance.org/events",
  "blurb":"Hundreds of thousands of holiday lights switch on in Ivoryton Village on Dec 5 and stay up all month; tune to 101.5 FM for the music. Lighting-night details aren't posted yet."},
 {"t":"Breakfast with Santa","v":ATR,"special":"hol","when":D(["2026-12-12","2026-12-13"],[["09:00","11:00"]]),"ages":"Ages 2+","a":["toddler","preschool","big"],"free":False,"price":"$74.99 per person","rsvp":True,"src":"https://essexsteamtrain.com/experiences-2/breakfast-with-santa/",
  "blurb":"A buffet breakfast where Santa reads a story and visits each table for photos and letters; every child gets a keepsake gift. No train ride included."},
]
TOWN["tba"]+=[{"g":"hol","t":"Ed Pop Magic Show","w":"Essex Town Hall auditorium","p":"The Ivoryton Library's free holiday magic show, with stories and audience participation, usually the Saturday before Christmas. Last year it was Dec 20 at 10 am (registration required). This year's date isn't posted yet.","src":"https://ivorytonlibrary.org/childrens-room/?amp=1"}]
ES_PATCH={
 "Museum admission ($15 adults, $5 ages 6–12, under 5 free)":"Entrada al museo ($15 adultos, $5 de 6–12 años, menores de 5 gratis)",
 "Steve Cryan's 33rd annual model-train layout on the museum's third floor, with a locomotive scavenger hunt. Open Tuesday–Sunday 10–5; closed Mondays, Thanksgiving and Christmas.":"La 33.ª maqueta anual de trenes de Steve Cryan en el tercer piso del museo, con una búsqueda del tesoro de locomotoras. Abre de martes a domingo de 10 a 5; cierra los lunes, Acción de Gracias y Navidad.",
 "Free outdoors; museum admission for inside":"Gratis al aire libre; entrada al museo para el interior",
 "Essex's holiday celebration: a kids' craft in the Boathouse at noon, hot chocolate at 4, a carol parade from Town Hall at 4:30 and a lighted boat parade on the river at 5.":"La celebración navideña de Essex: una manualidad para niños en el Boathouse al mediodía, chocolate caliente a las 4, un desfile con villancicos desde el Ayuntamiento a las 4:30 y un desfile de barcos iluminados en el río a las 5.",
 "$60 adults, $25 students":"$60 adultos, $25 estudiantes",
 "A family-friendly musical revue of American Christmas carols and stories, staged like an old-time radio show. Evenings Thursday–Saturday at 7:30; matinees Wednesday, Thursday, Saturday and Sunday at 2.":"Un espectáculo musical familiar de villancicos e historias navideñas estadounidenses, montado como un programa de radio antiguo. Funciones de jueves a sábado a las 7:30 p. m.; matinés miércoles, jueves, sábado y domingo a las 2.",
 "Ages 2+":"2 años o más",
 "$89.99 per person":"$89.99 por persona",
 "An Essex Steam Train princess brunch with face decorating, snowflake ornaments, letters to Santa, a story and games. No train ride included.":"Un brunch de princesas del Essex Steam Train con decoración de caritas, adornos de copos de nieve, cartas a Santa, un cuento y juegos. No incluye paseo en tren.",
 "Hundreds of thousands of holiday lights switch on in Ivoryton Village on Dec 5 and stay up all month; tune to 101.5 FM for the music. Lighting-night details aren't posted yet.":"Cientos de miles de luces navideñas se encienden en Ivoryton Village el 5 de dic. y se quedan todo el mes; sintoniza 101.5 FM para la música. Los detalles de la noche de encendido aún no se han publicado.",
 "$74.99 per person":"$74.99 por persona",
 "A buffet breakfast where Santa reads a story and visits each table for photos and letters; every child gets a keepsake gift. No train ride included.":"Un desayuno bufé donde Santa lee un cuento y visita cada mesa para fotos y cartas; cada niño recibe un regalo de recuerdo. No incluye paseo en tren.",
 "Ivoryton's fall festival with hayrides, cookie decorating, face painting, live music (5–7 pm), a trunk-or-treat on the Village Green (5–7 pm) and an evening Pumpkin Stroll of carved pumpkins.":"El festival de otoño de Ivoryton con paseos en carreta, decoración de galletas, pintacaritas, música en vivo (5–7 p. m.), dulces desde las cajuelas en el Village Green (5–7 p. m.) y un paseo nocturno entre calabazas talladas.",
 "Essex Town Hall auditorium":"Auditorio del Ayuntamiento de Essex",
 "The Ivoryton Library's free holiday magic show, with stories and audience participation, usually the Saturday before Christmas. Last year it was Dec 20 at 10 am (registration required). This year's date isn't posted yet.":"El show de magia navideño gratis de la Ivoryton Library, con cuentos y participación del público, por lo general el sábado antes de Navidad. El año pasado fue el 20 de dic. a las 10 a. m. (con inscripción). La fecha de este año aún no se ha publicado.",
}

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
