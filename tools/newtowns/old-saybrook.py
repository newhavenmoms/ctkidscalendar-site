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
