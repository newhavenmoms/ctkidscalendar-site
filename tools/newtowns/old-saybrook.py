W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
L="acton-library"; SRC="https://actonlibrary.assabetinteractive.com/calendar/"
B=["baby","toddler","preschool"]
def ev(**k):
    e={"v":L,"free":True,"price":"Free","src":SRC}; e.update(k); return e
TOWN={
 "display":"Old Saybrook","accent":"#BFD8EE",
 "venues":{L:["Acton Public Library","60 Old Boston Post Rd"],"os-main":["Main Street to the Town Green","Main St"]},
 "venueMeta":{L:[None,1],"os-main":[None,0]},
 "events":[
  ev(t="Playgroup",s=[[1,[["10:30","11:30"]],"2026-10-05","2026-12-28"]],x=["2026-10-12"],ages="Young children + caregiver",a=B,drop=True,
     blurb="A drop-in, child-led playgroup with activities, sensory materials and toys, a good way for little ones and caregivers to make friends."),
  ev(t="Storytime",s=[[2,[["10:30","11:30"]],"2026-10-06","2026-12-29"]],x=["2026-12-22"],ages="Young children + caregiver",a=B,rsvp=True,
     blurb="Stories, fingerplays, bounces and songs, then free play and bubbles. In October, local Connecticut authors visit for One Book, One Town. Registration requested."),
  ev(t="Sing & Stomp",s=[[5,[["10:30","11:30"]],"2026-10-09","2026-12-18"]],x=["2026-10-16","2026-11-13","2026-11-27"],ages="All ages + grown-ups",a=B,drop=True,
     blurb="A noisy song-and-dance party with bells, shakers, scarves and a parachute, then free play. No registration."),
  ev(t="Tinker Lab",when=D(["2026-10-05","2026-10-19","2026-11-02","2026-11-09","2026-11-23","2026-11-30","2026-12-07","2026-12-14"],[["15:30","16:30"]]),ages="School-age kids",a=["big"],rsvp=True,
     blurb="Imagine, build, code and tinker: marble mazes, Rube Goldberg machines, cardboard construction and coding. Registration required."),
  ev(t="Imaginary Tails with Izzy",when=D(["2026-10-20","2026-10-27","2026-11-10","2026-11-17","2026-11-24","2026-12-01","2026-12-08","2026-12-15"],[["15:30","16:30"]]),ages="Kids practicing reading",a=["big"],
     blurb="Read a favorite book to Izzy, a gentle certified reading dog. Sign up at the Children's Desk for a 10-minute spot."),
  ev(t="Creative Chefs",when=D(["2026-10-07","2026-10-14","2026-10-28"],[["15:30","16:30"]]),ages="Grades 2–6",a=["big"],rsvp=True,check=True,
     blurb="An after-school cooking club where young chefs learn basic skills and new recipes. Registration is for the whole series."),
  ev(t="Great Halloween Costume Swap",special="hw",when=D(["2026-10-08","2026-10-09"],[["15:00","16:30"]]),ages="Kids",a=B+["big"],drop=True,
     blurb="Pick out a Halloween costume for free; you don't need to have donated one. One costume per child."),
  ev(t="Makeup FX Class",special="hw",when=[W("2026-10-17",[["15:00","16:30"]])],ages="All ages",a=["big"],rsvp=True,
     blurb="Learn Halloween and movie special-effects makeup in a hands-on class with Decimated Designs. Registration required."),
  ev(t="Family Paint Night",when=D(["2026-10-21","2026-12-23"],[["18:00","19:30"]]),ages="All ages",a=["preschool","big"],rsvp=True,
     blurb="An evening of painting together as a family. Registration required."),
  ev(t="Pokémon Club",when=D(["2026-10-24","2026-11-21","2026-12-19"],[["14:00","15:00"]]),ages="Ages 6–11",a=["big"],rsvp=True,
     blurb="Learn the card game, do a Pokémon activity and trade talk with other fans. Cards provided. Registration required."),
  ev(t="All Ages Tabletop Game Night",when=D(["2026-10-07","2026-11-25","2026-12-09"],[["18:00","19:45"]]),ages="All ages",a=["preschool","big"],rsvp=True,
     blurb="Card games, board games and more for all ages, with light refreshments."),
  ev(t="Grow N' Glow Terrariums",when=[W("2026-11-14",[["10:30","11:30"]])],ages="Ages 4 and up",a=["preschool","big"],rsvp=True,
     blurb="Build a glow-in-the-dark terrarium with the Old Saybrook Garden Club. Registration required."),
  ev(t="Design Your Own Mug",when=[W("2026-12-08",[["15:00","16:30"],["18:00","19:30"]])],ages="All ages",a=["big"],rsvp=True,
     blurb="Draw your own design on a mug with infusible-ink markers. Registration required."),
  ev(t="Cozy Cookie Decorating",special="hol",when=[W("2026-12-12",[["10:30","11:30"]])],ages="Kids",a=["preschool","big"],rsvp=True,
     blurb="Decorate winter sugar cookies with all the toppings provided. Registration required."),
  ev(t="Season of Books",special="hol",when=[{"from":"2026-12-01","to":"2026-12-31","t":[]}],ages="Young children",a=B,
     blurb="Borrow a stack of wrapped books and unwrap a new bedtime story each night of December."),
  ev(t="Noon Year's Eve Party",special="hol",when=[W("2026-12-31",[["11:00","12:00"]])],ages="Ages 0–10",a=B+["big"],drop=True,
     blurb="Crafts, snacks and a bubble dance party, counting down to a balloon drop at noon. No registration."),
  {"t":"Old Saybrook Torchlight Parade","v":"os-main","special":"hol","when":[W("2026-12-12",[["18:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,
   "blurb":"A beloved holiday tradition: fife and drum corps march by torchlight down Main Street to the Town Green for a carol sing.","src":"https://oldsaybrooktorchlight.com/"},
 ],
 "tba":[],"classes":[],
 "library":{"for":"Free, every week","name":"Acton Public Library","desc":"Drop-in Playgroup on Mondays, Storytime on Tuesdays and Sing & Stomp on Fridays, plus Tinker Lab, a reading dog, Pokémon Club, free Grab & Go craft kits on Fridays and a Noon Year's Eve party.","a":"See the library's calendar","href":SRC},
}
PLACES={
 "out":[("Harvey's Beach","A small, sandy town beach on Long Island Sound.","Una pequeña playa de arena del pueblo en el estrecho de Long Island."),
        ("Saybrook Point & Fort Saybrook Monument Park","Riverside walking paths and history signs where the Connecticut River meets the Sound.","Senderos junto al río y letreros históricos donde el río Connecticut se encuentra con el estrecho.")],
 "rain":[("Acton Public Library","Weekly playgroup, storytime and Sing & Stomp, plus a children's room with toys.","Grupo de juego, cuentacuentos y Sing & Stomp cada semana, además de una sala infantil con juguetes."),
         ("The Kate (Katharine Hepburn Cultural Arts Center)","A restored theater on Main Street with films, concerts and a free small museum about Katharine Hepburn.","Un teatro restaurado en Main Street con películas, conciertos y un pequeño museo gratis sobre Katharine Hepburn."),
         ("Old Saybrook Historical Society","Keeps the 18th-century General William Hart House; check open hours and events.","Cuida la casa General William Hart del siglo XVIII; consulta horarios y eventos.")],
 "drive":[("Essex Steam Train & Riverboat","Vintage steam-train rides along the Connecticut River, including the holiday North Pole Express.","Paseos en tren de vapor antiguo junto al río Connecticut, incluido el North Pole Express navideño."),
          ("Connecticut River Museum","Hands-on river exhibits in Essex, plus a holiday train show from late November.","Exposiciones prácticas sobre el río en Essex, además de una exhibición de trenes navideña desde fines de noviembre."),
          ("Hammonasset Beach State Park","Connecticut's longest public beach, plus the Meigs Point Nature Center's touch tanks and trails, in Madison.","La playa pública más larga de Connecticut, además de los tanques táctiles y senderos del Meigs Point Nature Center, en Madison.")],
}
ES={
 "A drop-in, child-led playgroup with activities, sensory materials and toys, a good way for little ones and caregivers to make friends.":"Un grupo de juego sin inscripción, guiado por los niños, con actividades, materiales sensoriales y juguetes; una buena forma de que pequeños y adultos hagan amigos.",
 "Young children + caregiver":"Niños pequeños + un adulto",
 "Stories, fingerplays, bounces and songs, then free play and bubbles. In October, local Connecticut authors visit for One Book, One Town. Registration requested.":"Cuentos, juegos de dedos, rimas y canciones, y luego juego libre y burbujas. En octubre visitan autores locales de Connecticut por One Book, One Town. Se pide inscribirse.",
 "A noisy song-and-dance party with bells, shakers, scarves and a parachute, then free play. No registration.":"Una ruidosa fiesta de canto y baile con campanas, maracas, pañuelos y un paracaídas, y luego juego libre. Sin inscripción.",
 "All ages + grown-ups":"Todas las edades + adultos",
 "Imagine, build, code and tinker: marble mazes, Rube Goldberg machines, cardboard construction and coding. Registration required.":"Imagina, construye, programa y experimenta: laberintos de canicas, máquinas de Rube Goldberg, construcción con cartón y programación. Inscripción obligatoria.",
 "School-age kids":"Niños en edad escolar",
 "Read a favorite book to Izzy, a gentle certified reading dog. Sign up at the Children's Desk for a 10-minute spot.":"Lee tu libro favorito a Izzy, un tranquilo perro de lectura certificado. Inscríbete en el mostrador infantil para un turno de 10 minutos.",
 "Kids practicing reading":"Niños que practican la lectura",
 "An after-school cooking club where young chefs learn basic skills and new recipes. Registration is for the whole series.":"Un club de cocina después de clases donde los jóvenes chefs aprenden técnicas básicas y recetas nuevas. La inscripción es para toda la serie.",
 "Grades 2–6":"2.º a 6.º grado",
 "Pick up a free craft kit at the library each Friday, while supplies last.":"Recoge un kit de manualidades gratis en la biblioteca cada viernes, hasta agotar existencias.",
 "Kids":"Niños",
 "Pick out a Halloween costume for free; you don't need to have donated one. One costume per child.":"Escoge un disfraz de Halloween gratis; no necesitas haber donado uno. Un disfraz por niño.",
 "Learn Halloween and movie special-effects makeup in a hands-on class with Decimated Designs. Registration required.":"Aprende maquillaje de efectos especiales de Halloween y de cine en una clase práctica con Decimated Designs. Inscripción obligatoria.",
 "All ages":"Todas las edades",
 "An evening of painting together as a family. Registration required.":"Una noche para pintar juntos en familia. Inscripción obligatoria.",
 "Learn the card game, do a Pokémon activity and trade talk with other fans. Cards provided. Registration required.":"Aprende el juego de cartas, haz una actividad de Pokémon y platica con otros fans. Se prestan cartas. Inscripción obligatoria.",
 "Ages 6–11":"6–11 años",
 "Card games, board games and more for all ages, with light refreshments.":"Juegos de cartas, juegos de mesa y más para todas las edades, con bocadillos ligeros.",
 "Build a glow-in-the-dark terrarium with the Old Saybrook Garden Club. Registration required.":"Arma un terrario que brilla en la oscuridad con el Old Saybrook Garden Club. Inscripción obligatoria.",
 "Ages 4 and up":"Desde 4 años",
 "Draw your own design on a mug with infusible-ink markers. Registration required.":"Dibuja tu propio diseño en una taza con marcadores de tinta infusible. Inscripción obligatoria.",
 "Decorate winter sugar cookies with all the toppings provided. Registration required.":"Decora galletas de azúcar invernales con todos los adornos incluidos. Inscripción obligatoria.",
 "Borrow a stack of wrapped books and unwrap a new bedtime story each night of December.":"Llévate una pila de libros envueltos y desenvuelve un cuento nuevo para dormir cada noche de diciembre.",
 "Young children":"Niños pequeños",
 "Crafts, snacks and a bubble dance party, counting down to a balloon drop at noon. No registration.":"Manualidades, bocadillos y una fiesta de baile con burbujas, con cuenta regresiva hasta una lluvia de globos al mediodía. Sin inscripción.",
 "Ages 0–10":"0–10 años",
 "A beloved holiday tradition: fife and drum corps march by torchlight down Main Street to the Town Green for a carol sing.":"Una querida tradición navideña: bandas de pífanos y tambores desfilan con antorchas por Main Street hasta el Town Green para cantar villancicos.",
 "Drop-in Playgroup on Mondays, Storytime on Tuesdays and Sing & Stomp on Fridays, plus Tinker Lab, a reading dog, Pokémon Club, free Grab & Go craft kits on Fridays and a Noon Year's Eve party.":"Grupo de juego sin inscripción los lunes, cuentacuentos los martes y Sing & Stomp los viernes, además de Tinker Lab, un perro de lectura, Pokémon Club, kits de manualidades gratis los viernes y una fiesta de Noon Year's Eve.",
 "Free":"Gratis",
}

# ---- Playbook pass (Oct 4) ----
OSPR="os-rec"; MYREC="https://oldsaybrookct.myrec.com/info/activities/default.aspx"
TOWN["venues"][OSPR]=["Old Saybrook Parks & Recreation","308 Main St"]
TOWN["venueMeta"][OSPR]=[None,1]
TOWN["events"]+=[
 {"t":"'Tis the Season!","v":OSPR,"special":"hol","when":D(["2026-12-05","2026-12-12","2026-12-19","2027-01-02","2027-01-09"],[["09:30","10:30"]]),"ages":"Ages 3–5","a":["preschool"],"free":False,"price":"$30 residents / $40 non-residents (series)","rsvp":True,"src":"https://oldsaybrookct.myrec.com/info/activities/program_details.aspx?ProgramID=11848",
  "blurb":"A month of Saturday holiday celebrations exploring winter traditions through music, art and science. Register for the whole series."},
]
TOWN["tba"].append({"g":"hw","t":"Halloween Trunk or Treat at the Rec","w":"Old Saybrook Parks & Recreation, 308 Main St",
  "p":"Parks & Rec hosts a Trunk or Treat for families with kids in pre-K through grade 4, usually on a late-October Saturday evening. This year's date isn't posted yet.","src":MYREC})
TOWN["classes"]+=[
 {"id":"ospr-soccer-shots","c":"move","n":"Soccer Shots","u":MYREC,
  "blurb":"A 45-minute introduction to dribbling, passing and shooting on Saturday mornings in the fall session. Shin guards required.",
  "ages":"Ages 3–4","where":"Old Saybrook Parks & Recreation, 308 Main St"},
 {"id":"ospr-martial-arts","c":"move","n":"Martial Arts Confidence Course","u":MYREC,
  "blurb":"Martial arts classes grouped by age, from preschoolers to teens, plus an all-ages family class. Check MyRec for the current session.",
  "ages":"Ages 3 and up (by class)","where":"Old Saybrook Parks & Recreation, 308 Main St"},
 {"id":"ospr-junior-tennis","c":"move","n":"Junior Tennis","u":MYREC,
  "blurb":"Red-ball and orange-ball tennis lessons for young players, in multi-week sessions.",
  "ages":"Preschool and elementary","where":"Old Saybrook Parks & Recreation"},
]
PLACES["drive"].append(("Toys Ahoy! (Essex)","A classic village toy store on Main Street in Essex, with toys, games and children's books.","Una clásica juguetería de pueblo en Main Street de Essex, con juguetes, juegos y libros infantiles."))
ES.update({
 "A month of Saturday holiday celebrations exploring winter traditions through music, art and science. Register for the whole series.":"Un mes de celebraciones navideñas los sábados para explorar las tradiciones de invierno con música, arte y ciencia. Inscríbete para toda la serie.",
 "Ages 3–5":"3–5 años",
 "$30 residents / $40 non-residents (series)":"$30 residentes / $40 no residentes (serie)",
 "Parks & Rec hosts a Trunk or Treat for families with kids in pre-K through grade 4, usually on a late-October Saturday evening. This year's date isn't posted yet.":"Parks & Rec organiza un Trunk or Treat para familias con niños de prekínder a 4.º grado, normalmente un sábado por la tarde a fines de octubre. La fecha de este año aún no se ha publicado.",
 "Old Saybrook Parks & Recreation, 308 Main St":"Old Saybrook Parks & Recreation, 308 Main St",
 "A 45-minute introduction to dribbling, passing and shooting on Saturday mornings in the fall session. Shin guards required.":"Una introducción de 45 minutos a regatear, pasar y tirar, los sábados por la mañana en la sesión de otoño. Se requieren espinilleras.",
 "Ages 3–4":"3–4 años",
 "Martial arts classes grouped by age, from preschoolers to teens, plus an all-ages family class. Check MyRec for the current session.":"Clases de artes marciales por edad, de preescolares a adolescentes, además de una clase familiar para todas las edades. Consulta MyRec para la sesión actual.",
 "Ages 3 and up (by class)":"Desde 3 años (según la clase)",
 "Red-ball and orange-ball tennis lessons for young players, in multi-week sessions.":"Clases de tenis con pelota roja y naranja para jugadores jóvenes, en sesiones de varias semanas.",
 "Preschool and elementary":"Preescolar y primaria",
 "Old Saybrook Parks & Recreation":"Old Saybrook Parks & Recreation",
})

# ---- Weekend gap fix (Oct 5) ----
TOWN["tba"].append({"g":"fall","t":"Parks & Rec Fall Fun Series","w":"Atlantic Street Park",
  "p":"A Parks & Rec series of fall activities for families with young kids that kicked off Saturday, Oct 3, at Atlantic Street Park. Upcoming dates aren't posted yet; check Parks & Rec.","src":"https://oldsaybrookct.myrec.com/info/activities/default.aspx"})
PLACES["out"].append(("Clark Community Park","A town park on School House Road with walking trails and seasonal nature walks.","Un parque del pueblo en School House Road con senderos para caminar y caminatas de naturaleza por temporada."))
ES.update({
 "A Parks & Rec series of fall activities for families with young kids that kicked off Saturday, Oct 3, at Atlantic Street Park. Upcoming dates aren't posted yet; check Parks & Rec.":"Una serie de actividades de otoño de Parks & Rec para familias con niños pequeños que comenzó el sábado 3 de octubre en Atlantic Street Park. Las próximas fechas aún no se han publicado; consulta Parks & Rec.",
 "Atlantic Street Park":"Atlantic Street Park",
})

# ---- Weekend check (Oct 5): Patch calendar ----
TOWN["venues"]["goodwin-school"]=["Kathleen E. Goodwin Elementary School","80 Old Boston Post Rd"]
TOWN["venueMeta"]["goodwin-school"]=[None,0]
TOWN["events"].append({"t":"Electrify Your Drive! Free EV Car Show","v":"goodwin-school","when":[W("2026-10-10",[["12:00"]])],"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","drop":True,"check":True,
  "src":"https://patch.com/connecticut/madison-ct/calendar/event/20261010/5fe31ae4-2437-46d6-aba3-7113ba2b61c9/electrify-your-drive-free-ev-car-show-in-old-saybrook",
  "blurb":"A free show of electric cars and trucks in the school parking lot. A fun look for car-loving kids."})
ES.update({"A free show of electric cars and trucks in the school parking lot. A fun look for car-loving kids.":"Una exhibición gratis de autos y camionetas eléctricos en el estacionamiento de la escuela. Ideal para niños a los que les encantan los autos."})

# ---- patch: old-saybrook-2026-10-08.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
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
ES_PATCH={
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

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
