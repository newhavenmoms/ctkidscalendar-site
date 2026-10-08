W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
SRC="https://www.farmingtonlibraries.org/events"
B=["baby","toddler","preschool"]
FL,BL="farmington-library","barney-library"
def ev(v,**k):
    e={"v":v,"free":True,"price":"Free","src":SRC}; e.update(k); return e
TOWN={
 "display":"Farmington","accent":"#DCEBC4",
 "venues":{FL:["Farmington Library","6 Monteith Dr"],
           BL:["Barney Library","71 Main St"],
           "flt":["Farmington Land Trust property","Location sent at registration"],
           "hill-stead":["Hill-Stead Museum","35 Mountain Rd"]},
 "venueMeta":{FL:[None,1],BL:[None,1],"flt":[None,0],"hill-stead":[None,0]},
 "events":[
  # ---- little ones ----
  ev(FL,t="Toddler Time",s=[[4,[["09:30","10:00"]],"2026-10-08","2026-11-19"]],ages="Ages 2–3 + caregiver",a=["toddler"],drop=True,
     blurb="Dance, sing, move and play while building early literacy skills. Drop in."),
  ev(FL,t="Bite Sized Science",s=[[4,[["10:30","11:00"]],"2026-10-08","2026-11-19"]],ages="Preschoolers + caregiver",a=["preschool"],drop=True,
     blurb="A story plus a simple experiment or project exploring early science ideas."),
  ev(FL,t="Tots and Tunes",s=[[5,[["09:30","10:00"]],"2026-10-09","2026-12-18"]],x=["2026-11-27"],ages="Little kids + caregiver",a=["toddler","preschool"],drop=True,
     blurb="A high-energy music-and-movement class that starts with a story. Drop in."),
  ev(FL,t="Wonderful Ones",when=D(["2026-10-13","2026-10-20","2026-10-27","2026-11-03","2026-11-17"],[["09:30","10:15"]]),ages="One-year-olds + caregiver",a=["toddler"],drop=True,
     blurb="A drop-in storytime of books, music and movement just for one-year-olds."),
  ev(BL,t="Movers and Groovers",s=[[2,[["10:00","10:45"]],"2026-10-13","2026-12-29"]],ages="Little kids + caregiver",a=["toddler","preschool"],drop=True,
     blurb="A lively story and dancing in the Barney Library's Hoppin Gallery, every Tuesday."),
  ev(FL,t="Baby & Me Storytime",when=D(["2026-10-14","2026-10-28","2026-11-04","2026-11-11","2026-11-18"],[["09:30","10:00"]]),ages="Babies not yet walking + caregiver",a=["baby"],drop=True,
     blurb="A storytime for babies who aren't walking on their own yet. Drop in."),
  ev(FL,t="Bouncing Bookworms Storytime",when=D(["2026-10-14","2026-10-21","2026-10-28","2026-11-04","2026-11-11","2026-11-18"],[["10:30","11:15"]]),ages="Toddlers + caregiver",a=["toddler"],rsvp=True,check=True,
     blurb="A sensory storytime built around movement and sensory exploration. Currently full; check for openings."),
  ev(BL,t="Celebrate the Season",when=D(["2026-10-14","2026-11-18","2026-12-16"],[["10:00","10:45"]]),ages="Ages 3–5 + caregiver",a=["preschool"],rsvp=True,
     blurb="Seasonal stories and a hands-on craft at the Barney Library, once a month. Registration required."),
  ev(FL,t="Baby Steps Support Group",when=D(["2026-10-08","2026-10-22","2026-11-12"],[["10:30","11:30"]]),ages="Parents and caregivers of infants",a=["baby"],drop=True,
     blurb="A support group for parents and caregivers of infants. Babies welcome."),
  ev(FL,t="Firefighter Storytime",when=[W("2026-10-08",[["10:00","11:00"]])],ages="Ages 0–5 + caregiver",a=B,rsvp=True,check=True,
     blurb="A Fire Prevention Week storytime. Waitlist only."),
  ev(FL,t="PJ Storytime",when=[W("2026-10-13",[["18:00","18:30"]])],ages="Families",a=B,drop=True,
     blurb="Wear pajamas and bring blankets and plushies to a cozy bedtime storytime. Drop in."),
  ev(BL,t="We Play Wednesday",when=[W("2026-10-28",[["09:30","11:00"]])],ages="Young children + caregiver",a=B,drop=True,
     blurb="The Hoppin Gallery turns into a playroom: kids play while grown-ups chat."),
  ev(FL,t="Halloween Stories & Crafts",special="hw",when=[W("2026-10-31",[["10:30","11:30"]])],ages="Ages 2–5",a=["toddler","preschool"],drop=True,
     blurb="Not-so-spooky stories and songs, then a Halloween craft. Costumes welcome; drop in."),
  ev(FL,t="Math Storytime",when=D(["2026-11-02","2026-12-07"],[["18:00","18:45"]]),ages="Young children + caregiver",a=["toddler","preschool"],drop=True,
     blurb="Stories, rhymes and music built on early math ideas, ending with play time with math toys. Drop in."),
  ev(FL,t="Preschool Storytime",when=[W("2026-11-09",[["09:30","10:30"]])],ages="Ages 3–5",a=["preschool"],drop=True,check=True,
     blurb="A drop-in preschool storytime. Several fall dates were cancelled, so check that it's on before you go."),
  ev(FL,t="Baby's Morning Out Playgroup",when=D(["2026-11-09","2026-12-14"],[["10:00","11:00"]]),ages="Babies 0–12 months + caregiver",a=["baby"],drop=True,
     blurb="A playgroup for caregivers and infants, run by UConn."),
  ev(FL,t="Bilingual Spanish Storytime",when=[W("2026-11-10",[["18:00","18:30"]])],ages="Ages 3–6 (all welcome)",a=["preschool","big"],rsvp=True,
     blurb="Songs, rhymes and stories in Spanish and English. Registration required."),
  ev(FL,t="Weekend Wiggles!",when=[W("2026-11-21",[["09:30","10:00"]])],ages="Little kids + caregiver",a=["toddler","preschool"],drop=True,
     blurb="A Saturday music-and-movement class with a story and parachute time at the end. Drop in."),
  # ---- school-age ----
  ev(FL,t="Homeschool Curiosity Club",s=[[4,[["15:00","16:00"]],"2026-10-08","2026-11-19"]],ages="Homeschooled tweens",a=["big"],rsvp=True,check=True,
     blurb="Questions, investigations and answers for homeschooled tweens. Waitlist only."),
  ev(FL,t="Adaptive Storytime",when=D(["2026-10-14","2026-10-21","2026-11-04","2026-11-11"],[["18:00","19:00"]]),ages="Neurodiverse kids ages 3–10 + family",a=["preschool","big"],rsvp=True,check=True,
     blurb="A small-group storytime for families of neurodiverse children. Waitlist only."),
  ev(FL,t="Tinkering Tweens",when=D(["2026-10-14","2026-11-11"],[["17:00","18:00"]]),ages="Tweens",a=["big"],rsvp=True,
     blurb="STEAM projects in the Maker Space with the 3-D printer and Cricut: magical potion bottles (Oct 14) and solar-system lights (Nov 11). Registration required."),
  ev("flt",t="Nature Explorers with the Farmington Land Trust",when=D(["2026-10-10","2026-11-14","2026-12-12"],[["11:00","12:15"]]),ages="Grades K–3",a=["big"],rsvp=True,check=True,
     blurb="Outdoor nature exploration on Land Trust property with the library. Currently full; check for openings."),
  ev(FL,t="Halloween Costume Swap",special="hw",when=[W("2026-10-17",[["14:00","16:00"]])],ages="All ages",a=B+["big"],drop=True,
     blurb="Pick out a new-to-you costume donated by the community. No donation needed to take one."),
  ev(FL,t="Family Dinner Movie Theater",when=D(["2026-10-19","2026-11-16","2026-12-21"],[["17:30","19:30"]]),ages="Families",a=["preschool","big"],rsvp=True,
     blurb="Bring your dinner and watch a free movie on the big screen, the third Monday of each month. Registration required."),
  ev(FL,t="Pokémon Club",when=D(["2026-10-20","2026-11-17"],[["16:30","17:30"]]),ages="Grades K–12",a=["big"],rsvp=True,
     blurb="Trade Pokémon cards and do a Pokémon-themed activity, once a month. Registration required."),
  ev(BL,t="Afterschool LEGO Club",when=D(["2026-10-26","2026-11-30"],[["15:45","16:30"]]),ages="Ages 8–12",a=["big"],rsvp=True,check=True,
     blurb="Build and code with LEGO SPIKE Prime at the Barney Library. Currently full."),
  ev(FL,t="Magical Makers",when=D(["2026-10-27","2026-11-24"],[["17:00","18:00"]]),ages="Kids",a=["big"],rsvp=True,check=True,
     blurb="A magical story and a craft to match: witch's cauldrons and clay familiars (Oct 27) and hot-air balloons (Nov 24). Registration required; October is full."),
  ev(FL,t="Mad Science Mania",special="hw",when=[W("2026-10-28",[["18:00","19:00"]])],ages="Ages 4–12",a=["preschool","big"],rsvp=True,check=True,
     blurb="A costume party meets mad science: a craft, trick-or-treating around the library and an experiment. Currently full."),
  ev(BL,t="Craft Hour: Pumpkin Watercolors",when=[W("2026-10-29",[["15:00","16:00"]])],ages="Kids",a=["big"],rsvp=True,
     blurb="Paint pumpkin watercolors at the Barney Library's every-other-month craft hour. Registration required."),
  ev(FL,t="Turkey Apples",when=[W("2026-11-07",[["10:00","10:30"]])],ages="Grades K–6",a=["big"],rsvp=True,check=True,
     blurb="Turn an apple into a turkey to take home. Waitlist only."),
  ev(BL,t="Barney Kids Book Club",when=D(["2026-11-09","2026-12-14"],[["15:45","16:30"]]),ages="Grades K–4",a=["big"],rsvp=True,
     blurb="No assigned reading: a read-aloud with Miss Amy and a themed craft or activity after school. Registration required."),
  ev(BL,t="Tellabration!",when=[W("2026-11-16",[["14:00","15:00"]])],ages="Preschool and elementary",a=["preschool","big"],rsvp=True,
     blurb="The Barney Library's annual afternoon of live storytelling. Registration required."),
  ev(FL,t="Culinary Kids Club: Pancakes!",when=[W("2026-11-18",[["18:00","19:00"]])],ages="Grades 3–6",a=["big"],rsvp=True,
     blurb="Learn to make pancakes. Dietary restrictions can't be accommodated. Registration required."),
  {"t":"Halloween on the Hill","v":"hill-stead","special":"hw","when":[W("2026-10-31",[["12:00","16:00"]])],"ages":"All ages","a":B+["big"],"free":False,"price":"$5 per person (ages 2+), $20 per carload","rsvp":True,"src":"https://ctvisit.com/events/halloween-hill-2",
   "blurb":"Follow the Pond Loop for treats and surprises, take a hayride and slingshot a pumpkin to feed the sheep. Costumes encouraged; pre-registration requested."},
 ],
 "tba":[],
 "classes":[],
 "library":{"for":"Free, every week","name":"Farmington Libraries","desc":"Two libraries (Farmington Library on Monteith Drive and Barney Library on Main Street) with drop-in toddler, baby and music storytimes most weekday mornings, Movers and Groovers every Tuesday, monthly family dinner movies, and maker and LEGO clubs. Popular programs fill fast.","a":"See the libraries' calendar","href":SRC},
}
PLACES={
 "out":[("Hill-Stead Museum grounds","152 acres of meadows, a sunken garden and walking trails around a Colonial Revival house, plus sheep to visit.","62 hectáreas de praderas, un jardín hundido y senderos alrededor de una casa de estilo Colonial Revival, además de ovejas para visitar."),
        ("Farmington River Trail","A flat paved rail trail along the river, good for bikes, scooters and strollers.","Un sendero plano y pavimentado junto al río, ideal para bicicletas, patinetas y carriolas."),
        ("Winding Trails","A recreation area with a swimming lake in summer and cross-country skiing and trails in winter (passes required).","Un área recreativa con un lago para nadar en verano y esquí de fondo y senderos en invierno (se requiere pase).")],
 "rain":[("Farmington Library","The main library on Monteith Drive, with a Maker Space and a busy children's program room.","La biblioteca principal en Monteith Drive, con un Maker Space y una sala de programas infantiles muy activa."),
         ("Barney Library","A small historic library on Main Street whose Hoppin Gallery hosts music, play mornings and crafts.","Una pequeña biblioteca histórica en Main Street cuya Hoppin Gallery acoge música, mañanas de juego y manualidades."),
         ("Stanley-Whitman House","A 1720 house and living-history museum with colonial demonstrations and seasonal programs; check open hours.","Una casa de 1720 y museo de historia viva con demostraciones coloniales y programas de temporada; consulta el horario.")],
 "drive":[("The Children's Museum","Live animals, a planetarium and hands-on exhibits in West Hartford.","Animales vivos, un planetario y exposiciones interactivas en West Hartford."),
          ("New Britain Museum of American Art","An art museum with family days and kid-friendly galleries in New Britain.","Un museo de arte con días familiares y galerías para niños en New Britain."),
          ("Lake Compounce","New England's oldest amusement park, in Bristol.","El parque de diversiones más antiguo de Nueva Inglaterra, en Bristol.")],
}
ES={
 "Ages 2–3 + caregiver":"2–3 años + un adulto",
 "Dance, sing, move and play while building early literacy skills. Drop in.":"Baila, canta, muévete y juega mientras desarrollas la lectura temprana. Sin inscripción.",
 "Preschoolers + caregiver":"Preescolares + un adulto",
 "A story plus a simple experiment or project exploring early science ideas.":"Un cuento y un experimento o proyecto sencillo para explorar ideas básicas de ciencia.",
 "Little kids + caregiver":"Niños pequeños + un adulto",
 "A high-energy music-and-movement class that starts with a story. Drop in.":"Una clase muy activa de música y movimiento que empieza con un cuento. Sin inscripción.",
 "One-year-olds + caregiver":"Niños de un año + un adulto",
 "A drop-in storytime of books, music and movement just for one-year-olds.":"Un cuentacuentos sin inscripción con libros, música y movimiento solo para niños de un año.",
 "A lively story and dancing in the Barney Library's Hoppin Gallery, every Tuesday.":"Un cuento animado y baile en la Hoppin Gallery de la Barney Library, todos los martes.",
 "Babies not yet walking + caregiver":"Bebés que aún no caminan + un adulto",
 "A storytime for babies who aren't walking on their own yet. Drop in.":"Un cuentacuentos para bebés que todavía no caminan solos. Sin inscripción.",
 "Toddlers + caregiver":"Niños pequeños + un adulto",
 "A sensory storytime built around movement and sensory exploration. Currently full; check for openings.":"Un cuentacuentos sensorial basado en el movimiento y la exploración sensorial. Por ahora está lleno; consulta si hay lugares.",
 "Ages 3–5 + caregiver":"3–5 años + un adulto",
 "Seasonal stories and a hands-on craft at the Barney Library, once a month. Registration required.":"Cuentos de temporada y una manualidad en la Barney Library, una vez al mes. Inscripción obligatoria.",
 "Parents and caregivers of infants":"Padres y cuidadores de bebés",
 "A support group for parents and caregivers of infants. Babies welcome.":"Un grupo de apoyo para padres y cuidadores de bebés. Los bebés son bienvenidos.",
 "Ages 0–5 + caregiver":"0–5 años + un adulto",
 "A Fire Prevention Week storytime. Waitlist only.":"Un cuentacuentos de la Semana de Prevención de Incendios. Solo lista de espera.",
 "Families":"Familias",
 "Wear pajamas and bring blankets and plushies to a cozy bedtime storytime. Drop in.":"Ven en pijama y trae cobijas y peluches a un acogedor cuentacuentos antes de dormir. Sin inscripción.",
 "Young children + caregiver":"Niños pequeños + un adulto",
 "The Hoppin Gallery turns into a playroom: kids play while grown-ups chat.":"La Hoppin Gallery se convierte en sala de juegos: los niños juegan mientras los adultos conversan.",
 "Ages 2–5":"2–5 años",
 "Not-so-spooky stories and songs, then a Halloween craft. Costumes welcome; drop in.":"Cuentos y canciones que no dan mucho miedo, y luego una manualidad de Halloween. Se pueden traer disfraces; sin inscripción.",
 "Stories, rhymes and music built on early math ideas, ending with play time with math toys. Drop in.":"Cuentos, rimas y música basados en ideas matemáticas básicas, que terminan con juego con juguetes de matemáticas. Sin inscripción.",
 "Ages 3–5":"3–5 años",
 "A drop-in preschool storytime. Several fall dates were cancelled, so check that it's on before you go.":"Un cuentacuentos para preescolares sin inscripción. Se cancelaron varias fechas de otoño, así que confirma antes de ir.",
 "Babies 0–12 months + caregiver":"Bebés de 0–12 meses + un adulto",
 "A playgroup for caregivers and infants, run by UConn.":"Un grupo de juego para cuidadores y bebés, a cargo de UConn.",
 "Ages 3–6 (all welcome)":"3–6 años (todos son bienvenidos)",
 "Songs, rhymes and stories in Spanish and English. Registration required.":"Canciones, rimas y cuentos en español e inglés. Inscripción obligatoria.",
 "A Saturday music-and-movement class with a story and parachute time at the end. Drop in.":"Una clase de música y movimiento los sábados con un cuento y juego con paracaídas al final. Sin inscripción.",
 "Homeschooled tweens":"Preadolescentes educados en casa",
 "Questions, investigations and answers for homeschooled tweens. Waitlist only.":"Preguntas, investigaciones y respuestas para preadolescentes educados en casa. Solo lista de espera.",
 "Neurodiverse kids ages 3–10 + family":"Niños neurodiversos de 3–10 años + familia",
 "A small-group storytime for families of neurodiverse children. Waitlist only.":"Un cuentacuentos en grupo pequeño para familias de niños neurodiversos. Solo lista de espera.",
 "Tweens":"Preadolescentes",
 "STEAM projects in the Maker Space with the 3-D printer and Cricut: magical potion bottles (Oct 14) and solar-system lights (Nov 11). Registration required.":"Proyectos STEAM en el Maker Space con la impresora 3D y la Cricut: botellas de pociones mágicas (14 de oct.) y luces del sistema solar (11 de nov.). Inscripción obligatoria.",
 "Grades K–3":"Kínder a 3.er grado",
 "Outdoor nature exploration on Land Trust property with the library. Currently full; check for openings.":"Exploración de la naturaleza al aire libre en terrenos del Land Trust con la biblioteca. Por ahora está lleno; consulta si hay lugares.",
 "All ages":"Todas las edades",
 "Pick out a new-to-you costume donated by the community. No donation needed to take one.":"Elige un disfraz donado por la comunidad. No hace falta donar para llevarte uno.",
 "Bring your dinner and watch a free movie on the big screen, the third Monday of each month. Registration required.":"Trae tu cena y mira una película gratis en pantalla grande, el tercer lunes de cada mes. Inscripción obligatoria.",
 "Grades K–12":"Kínder a 12.º grado",
 "Trade Pokémon cards and do a Pokémon-themed activity, once a month. Registration required.":"Intercambia cartas de Pokémon y haz una actividad temática, una vez al mes. Inscripción obligatoria.",
 "Ages 8–12":"8–12 años",
 "Build and code with LEGO SPIKE Prime at the Barney Library. Currently full.":"Construye y programa con LEGO SPIKE Prime en la Barney Library. Por ahora está lleno.",
 "Kids":"Niños",
 "A magical story and a craft to match: witch's cauldrons and clay familiars (Oct 27) and hot-air balloons (Nov 24). Registration required; October is full.":"Un cuento mágico y una manualidad a juego: calderos de bruja y animales de arcilla (27 de oct.) y globos aerostáticos (24 de nov.). Inscripción obligatoria; octubre está lleno.",
 "Ages 4–12":"4–12 años",
 "A costume party meets mad science: a craft, trick-or-treating around the library and an experiment. Currently full.":"Una fiesta de disfraces con ciencia loca: una manualidad, pedir dulces por la biblioteca y un experimento. Por ahora está lleno.",
 "Paint pumpkin watercolors at the Barney Library's every-other-month craft hour. Registration required.":"Pinta calabazas en acuarela en la hora de manualidades bimestral de la Barney Library. Inscripción obligatoria.",
 "Grades K–6":"Kínder a 6.º grado",
 "Turn an apple into a turkey to take home. Waitlist only.":"Convierte una manzana en un pavo para llevar a casa. Solo lista de espera.",
 "Grades K–4":"Kínder a 4.º grado",
 "No assigned reading: a read-aloud with Miss Amy and a themed craft or activity after school. Registration required.":"Sin lectura asignada: Miss Amy lee en voz alta y luego hay una manualidad o actividad temática después de clases. Inscripción obligatoria.",
 "Preschool and elementary":"Preescolar y primaria",
 "The Barney Library's annual afternoon of live storytelling. Registration required.":"La tarde anual de narración en vivo de la Barney Library. Inscripción obligatoria.",
 "Grades 3–6":"3.º a 6.º grado",
 "Learn to make pancakes. Dietary restrictions can't be accommodated. Registration required.":"Aprende a hacer panqueques. No se pueden atender restricciones alimentarias. Inscripción obligatoria.",
 "$5 per person (ages 2+), $20 per carload":"$5 por persona (desde 2 años), $20 por auto",
 "Follow the Pond Loop for treats and surprises, take a hayride and slingshot a pumpkin to feed the sheep. Costumes encouraged; pre-registration requested.":"Recorre el Pond Loop en busca de dulces y sorpresas, da un paseo en carreta de heno y lanza una calabaza con una resortera para alimentar a las ovejas. Se recomiendan los disfraces; se pide inscripción previa.",
 "Two libraries (Farmington Library on Monteith Drive and Barney Library on Main Street) with drop-in toddler, baby and music storytimes most weekday mornings, Movers and Groovers every Tuesday, monthly family dinner movies, and maker and LEGO clubs. Popular programs fill fast.":"Dos bibliotecas (Farmington Library en Monteith Drive y Barney Library en Main Street) con cuentacuentos sin inscripción para niños pequeños, bebés y de música casi todas las mañanas entre semana, Movers and Groovers todos los martes, películas familiares mensuales con cena y clubes de maker y LEGO. Los programas populares se llenan rápido.",
 "Free":"Gratis",
 "Location sent at registration":"Ubicación enviada al inscribirse",
}

# ---- Full playbook pass (Oct 7) ----
SWH="stanley-whitman"; UM="unionville-museum"
TOWN["venues"]["flt"]=["Farmington Land Trust","119 Coppermine Rd, Unionville"]
TOWN["venues"].update({SWH:["Stanley-Whitman House","37 High St"],UM:["Unionville Museum","15 School St, Unionville"]})
TOWN["venueMeta"].update({SWH:[None,0],UM:[None,1]})
SWP="https://www.s-wh.org/programs"
TOWN["events"]+=[
 {"t":"Ghost Walk Tours","v":SWH,"special":"hw","when":[W("2026-10-17",[["13:00","16:00"]])],"ages":"School-age kids and up","a":["big"],"free":False,"price":"About $20–25 (last year)","rsvp":True,"check":True,"src":SWP,
  "blurb":"Guided ghost-story walks at 1, 2 and 3 pm from the Stanley-Whitman House's Memento Mori Cemetery. Buy tickets through the museum."},
 {"t":"Unionville Walking Tours","v":UM,"when":[W("2026-10-17",[["13:30","14:30"],["15:00","16:00"]])],"ages":"All ages","a":["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://unionvillemuseum.org",
  "blurb":"Free walking tours of downtown Unionville and how urban renewal changed it, starting at the Unionville Museum. No RSVP; rain date Oct 18."},
 {"t":"The Nutcracker: Land of the Sweets","v":"hill-stead","special":"hol","when":[W("2026-11-14",[["14:00","15:00"],["16:00","17:00"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"Tickets required","check":True,"src":"https://events.humanitix.com/the-nutcracker-land-of-the-sweets",
  "blurb":"Ballet Hartford dances a one-hour Nutcracker at Hill-Stead, a short version that suits little ones."},
 {"t":"Colonial Thanksgiving","v":SWH,"when":[W("2026-11-14",[["12:00","15:00"]])],"ages":"All ages","a":["big"],"free":False,"price":"See museum","check":True,"src":SWP,
  "blurb":"Historian Dennis Picard shows how colonial families cooked and celebrated the harvest, at the 1720 Whitman Tavern."},
 {"t":"Candlelight Tours: Christmas in Farmington","v":SWH,"special":"hol","when":[W("2026-12-12",[["19:00","21:00"]])],"ages":"School-age kids and up","a":["big"],"free":False,"price":"About $20–25 (last year)","rsvp":True,"check":True,"src":SWP,
  "blurb":"The museum's 20th annual candlelit holiday tours of historic Farmington."},
]
TOWN["classes"]+=[
 {"id":"farmington-rec","c":"move","n":"Farmington Recreation programs","u":"https://patch.com/connecticut/farmington/parent-s-guide-after-school-activities-farmington",
  "blurb":"Town classes and youth sports by season; register through Farmington Recreation (860-675-2540).","ages":"Preschool–teens","where":"Around Farmington"},
 {"id":"farmington-martial-arts","c":"move","n":"Farmington Martial Arts","u":"https://fmamembers.com",
  "blurb":"Martial arts classes for kids at a range of ages, focused on confidence, discipline and self-defense.","ages":"Kids and teens","where":"Farmington"},
 {"id":"fv-dance-music","c":"music","n":"Farmington Valley Dance & Music School","u":"https://farmingtonvalleydanceandmusicllc.org/farmington-music-lessons/",
  "blurb":"Music lessons and dance classes for kids.","ages":"Kids and teens","where":"Farmington"},
 {"id":"farmington-sports-arena","c":"move","n":"Farmington Sports Arena","u":"https://fsasports.com",
  "blurb":"An indoor sports arena with youth leagues, clinics and instruction.","ages":"Kids and teens","where":"Farmington"},
]
PLACES["rain"]+=[("Unionville Museum","A free local history museum, open Wednesdays, Saturdays and Sundays 2–4 during exhibits (15 School St, Unionville).","Un museo gratis de historia local, abierto miércoles, sábados y domingos de 2 a 4 durante las exposiciones (15 School St, Unionville).")]
PLACES["out"]=[p if p[0]!="Hill-Stead Museum grounds" else ("Hill-Stead Museum grounds","152 acres of meadows, a sunken garden, woodland trails and a sheep farm, free to explore daily 7:30–5:30.","62 hectáreas de praderas, un jardín hundido, senderos en el bosque y una granja de ovejas, gratis para explorar todos los días de 7:30 a 5:30.") for p in PLACES["out"]]
PLACES["out"].append(("Farmington Land Trust","Trails and open space across town, with a small barn and family programs at 119 Coppermine Rd in Unionville.","Senderos y espacios abiertos por todo el pueblo, con un pequeño granero y programas familiares en 119 Coppermine Rd, Unionville."))
ES.update({
 "School-age kids and up":"Niños en edad escolar y mayores",
 "About $20–25 (last year)":"Unos $20–25 (el año pasado)",
 "Guided ghost-story walks at 1, 2 and 3 pm from the Stanley-Whitman House's Memento Mori Cemetery. Buy tickets through the museum.":"Caminatas guiadas con historias de fantasmas a la 1, 2 y 3 pm desde el Memento Mori Cemetery de la Stanley-Whitman House. Compra boletos con el museo.",
 "Free walking tours of downtown Unionville and how urban renewal changed it, starting at the Unionville Museum. No RSVP; rain date Oct 18.":"Caminatas gratis por el centro de Unionville y cómo lo cambió la renovación urbana, desde el Unionville Museum. Sin reservación; fecha alternativa por lluvia: 18 de oct.",
 "Tickets required":"Se requieren boletos",
 "Ballet Hartford dances a one-hour Nutcracker at Hill-Stead, a short version that suits little ones.":"Ballet Hartford baila un Cascanueces de una hora en Hill-Stead, una versión corta ideal para los más pequeños.",
 "See museum":"Consulta con el museo",
 "Historian Dennis Picard shows how colonial families cooked and celebrated the harvest, at the 1720 Whitman Tavern.":"El historiador Dennis Picard muestra cómo cocinaban y celebraban la cosecha las familias coloniales, en la Whitman Tavern de 1720.",
 "The museum's 20th annual candlelit holiday tours of historic Farmington.":"Los 20.º recorridos navideños anuales a la luz de las velas por el Farmington histórico, del museo.",
 "Town classes and youth sports by season; register through Farmington Recreation (860-675-2540).":"Clases del pueblo y deportes juveniles por temporada; inscríbete con Farmington Recreation (860-675-2540).",
 "Preschool–teens":"Preescolar–adolescentes",
 "Around Farmington":"En distintos lugares de Farmington",
 "Martial arts classes for kids at a range of ages, focused on confidence, discipline and self-defense.":"Clases de artes marciales para niños de varias edades, enfocadas en la confianza, la disciplina y la defensa personal.",
 "Kids and teens":"Niños y adolescentes",
 "Music lessons and dance classes for kids.":"Clases de música y danza para niños.",
 "An indoor sports arena with youth leagues, clinics and instruction.":"Un centro deportivo techado con ligas juveniles, clínicas y clases.",
 "119 Coppermine Rd, Unionville":"119 Coppermine Rd, Unionville",
})

# ---- gap check (Oct 7) ----
PLACES["out"]+=[("Westwoods Recreational Complex splash pad","A new splash pad (opened 2026) beside Westwoods Golf Course, for summer days (14 Westwoods Dr).","Una nueva zona de chorros de agua (abierta en 2026) junto al Westwoods Golf Course, para los días de verano (14 Westwoods Dr).")]

# ---- Farmington Recreation (MyRec), read Oct 8 ----
MR="https://farmingtonct.myrec.com/info/activities/program_details.aspx?ProgramID="
STG="staples-green"; FHS="farmington-hs"
TOWN["venues"].update({STG:["Staples House Green","1554 Farmington Ave"],FHS:["Farmington High School","10 Monteith Dr"]})
TOWN["venueMeta"].update({STG:[None,0],FHS:[None,0]})
TOWN["events"]+=[
 {"t":"Farmington Fall Festival","v":STG,"special":"hw","when":[W("2026-10-24",[["13:00","16:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free (bring a food-pantry donation)","drop":True,"src":MR+"29975",
  "blurb":"Crafts, games, trick-or-treat tables and sensory-friendly activities, hosted by Farmington Recreation and the libraries. Bring a nonperishable item for the Farmington Food Pantry."},
 {"t":"MPower Youth Running Festival","v":FHS,"when":[W("2026-11-08",[["09:15","11:30"]])],"ages":"Ages 2–14","a":["toddler","preschool","big"],"free":False,"price":"$11.60 fun run, $22.20 mile, $32.80 5K","rsvp":True,"src":"https://runsignup.com/Race/Info/CT/Farmington/MPower5K",
  "blurb":"A kids-only running festival on closed courses: a quarter-mile fun run for ages 2–8 (9:15), a 1-mile for ages 5–14 (9:30) and a 5K for ages 6–14 (10:30). Mile and 5K prices go up after Nov 1."},
]
TOWN["classes"]=[c for c in TOWN["classes"] if c["id"]!="farmington-rec"]
TOWN["classes"]+=[
 {"id":"farm-tumble-bunnies","c":"move","n":"Tumble Bunnies (Farmington Rec)","u":MR+"29843",
  "blurb":"Saturday-morning gymnastics in the Union School gym. The late-fall session runs Oct 24–Dec 5 (no class Nov 28); age 2 with a parent, ages 3–6 on their own. $119 ($129 non-residents).","ages":"2–6 years","where":"Union School, 173 School St, Unionville"},
 {"id":"farm-nebt-ballet","c":"dance","n":"Ballet with New England Ballet Theatre","u":MR+"29999",
  "blurb":"Sunday-afternoon ballet and tap, Oct 18–Nov 22: Tiny Twirls (18 months–3 with a caregiver, $99) and Petite Pirouettes (ages 7–13, $119). Little Leaps (3–6) is full.","ages":"18 months–13 years","where":"1928 Rec Studio, Town Hall"},
 {"id":"farm-jukido","c":"move","n":"Jukido Youth Self-Defense","u":MR+"29986",
  "blurb":"Jujutsu-, judo- and aikido-based self-defense with anti-bullying skills, Friday evenings. Next session Nov 6–20 ($74; $84 non-residents).","ages":"5 years and up","where":"1928 Rec Studio, Town Hall"},
 {"id":"farm-badminton","c":"move","n":"Youth Badminton Clinics","u":MR+"29885",
  "blurb":"Monday and Wednesday clinics with a national-level player, beginner to advanced. Fall session 2 runs Oct 21–Nov 18. $199 ($219 non-residents).","ages":"5–17 years","where":"Irving Robbins Middle School gym"},
 {"id":"farm-tennis","c":"move","n":"Youth Tennis Clinics (indoor)","u":MR+"29855",
  "blurb":"Sunday-afternoon indoor clinics with a USPTA pro, Nov 15–Dec 20 (no class Nov 29). Ages 4–5 $59; older groups $119. Bring a racket.","ages":"4–15 years","where":"Irving Robbins Middle School gym"},
 {"id":"farm-rec-basketball","c":"move","n":"Farmington Rec Youth Basketball","u":MR+"29928",
  "blurb":"Winter basketball for Farmington residents and students, Dec 5–Feb 13: clinic-style for grades K–1, weekly practice and Saturday games for grades 2–8. $129. Some grades are already full; wait list available.","ages":"Grades K–8","where":"West District School and other town gyms"},
 {"id":"farm-ski-club","c":"move","n":"Rec Ski Club at Ski Sundown","u":MR+"29977",
  "blurb":"Five weekly winter ski trips by bus from school for Farmington Public Schools students. Registration for 2026–27 opens Oct 13; lift, lesson and rental costs are paid separately.","ages":"Grades 3–8","where":"Ski Sundown (bus from school)"},
]
ES.update({
 "Free (bring a food-pantry donation)":"Gratis (trae una donación para la despensa)",
 "Crafts, games, trick-or-treat tables and sensory-friendly activities, hosted by Farmington Recreation and the libraries. Bring a nonperishable item for the Farmington Food Pantry.":"Manualidades, juegos, mesas para pedir dulces y actividades adaptadas sensorialmente, organizadas por Farmington Recreation y las bibliotecas. Trae un alimento no perecedero para la despensa de Farmington.",
 "Ages 2–14":"2–14 años",
 "$11.60 fun run, $22.20 mile, $32.80 5K":"$11.60 carrera divertida, $22.20 la milla, $32.80 los 5K",
 "A kids-only running festival on closed courses: a quarter-mile fun run for ages 2–8 (9:15), a 1-mile for ages 5–14 (9:30) and a 5K for ages 6–14 (10:30). Mile and 5K prices go up after Nov 1.":"Un festival de carreras solo para niños en rutas cerradas: una carrera divertida de un cuarto de milla para 2–8 años (9:15), una milla para 5–14 años (9:30) y unos 5K para 6–14 años (10:30). Los precios de la milla y los 5K suben después del 1 de nov.",
 "Saturday-morning gymnastics in the Union School gym. The late-fall session runs Oct 24–Dec 5 (no class Nov 28); age 2 with a parent, ages 3–6 on their own. $119 ($129 non-residents).":"Gimnasia los sábados por la mañana en el gimnasio de Union School. La sesión de fin de otoño va del 24 de oct. al 5 de dic. (sin clase el 28 de nov.); niños de 2 años con papá o mamá, de 3–6 años solos. $119 ($129 no residentes).",
 "2–6 years":"2–6 años",
 "Union School, 173 School St, Unionville":"Union School, 173 School St, Unionville",
 "Sunday-afternoon ballet and tap, Oct 18–Nov 22: Tiny Twirls (18 months–3 with a caregiver, $99) and Petite Pirouettes (ages 7–13, $119). Little Leaps (3–6) is full.":"Ballet y tap los domingos por la tarde, del 18 de oct. al 22 de nov.: Tiny Twirls (18 meses–3 años con un adulto, $99) y Petite Pirouettes (7–13 años, $119). Little Leaps (3–6) está lleno.",
 "18 months–13 years":"18 meses–13 años",
 "1928 Rec Studio, Town Hall":"Estudio de recreación 1928, Town Hall",
 "Jujutsu-, judo- and aikido-based self-defense with anti-bullying skills, Friday evenings. Next session Nov 6–20 ($74; $84 non-residents).":"Defensa personal basada en jujutsu, judo y aikido con habilidades contra el acoso, los viernes por la tarde. Próxima sesión del 6 al 20 de nov. ($74; $84 no residentes).",
 "5 years and up":"5 años en adelante",
 "Monday and Wednesday clinics with a national-level player, beginner to advanced. Fall session 2 runs Oct 21–Nov 18. $199 ($219 non-residents).":"Clínicas los lunes y miércoles con un jugador de nivel nacional, de principiante a avanzado. La sesión 2 de otoño va del 21 de oct. al 18 de nov. $199 ($219 no residentes).",
 "5–17 years":"5–17 años",
 "Irving Robbins Middle School gym":"Gimnasio de Irving Robbins Middle School",
 "Sunday-afternoon indoor clinics with a USPTA pro, Nov 15–Dec 20 (no class Nov 29). Ages 4–5 $59; older groups $119. Bring a racket.":"Clínicas bajo techo los domingos por la tarde con un profesional de la USPTA, del 15 de nov. al 20 de dic. (sin clase el 29 de nov.). 4–5 años $59; grupos mayores $119. Trae raqueta.",
 "4–15 years":"4–15 años",
 "Winter basketball for Farmington residents and students, Dec 5–Feb 13: clinic-style for grades K–1, weekly practice and Saturday games for grades 2–8. $129. Some grades are already full; wait list available.":"Básquetbol de invierno para residentes y estudiantes de Farmington, del 5 de dic. al 13 de feb.: estilo clínica para K–1.º grado, práctica semanal y partidos los sábados para 2.º–8.º grado. $129. Algunos grados ya están llenos; hay lista de espera.",
 "Grades K–8":"Kínder–8.º grado",
 "West District School and other town gyms":"West District School y otros gimnasios del pueblo",
 "Five weekly winter ski trips by bus from school for Farmington Public Schools students. Registration for 2026–27 opens Oct 13; lift, lesson and rental costs are paid separately.":"Cinco salidas semanales a esquiar en invierno, en autobús desde la escuela, para estudiantes de las escuelas públicas de Farmington. La inscripción 2026–27 abre el 13 de oct.; el pase, las clases y el alquiler se pagan aparte.",
 "Grades 3–8":"3.º–8.º grado",
 "Ski Sundown (bus from school)":"Ski Sundown (autobús desde la escuela)",
})

# ---- creative places / bookstores / blogs pass (Oct 8) ----
PLACES["rain"]+=[("Farmington Library Used Bookstore","The Friends' used-book shop inside the main library, restocked weekly and open library hours; kids' books are cheap (6 Monteith Dr).","La tienda de libros usados de los Amigos dentro de la biblioteca principal, con nuevos títulos cada semana y abierta en el horario de la biblioteca; los libros infantiles son baratos (6 Monteith Dr).")]
PLACES["out"]+=[("Farmington Miniature Golf & Ice Cream Parlor","Landscaped mini golf next to an old-fashioned ice cream parlor on Route 4 (1048 Farmington Ave); seasonal, so call 860-677-0118 before going late in the fall.","Minigolf con jardines junto a una heladería de estilo antiguo en la Ruta 4 (1048 Farmington Ave); es de temporada, así que llama al 860-677-0118 antes de ir a finales del otoño."),
                ("Riverfront Miniature Golf & Ice Cream","Mini golf overlooking the Farmington River in Unionville (218 River Rd); seasonal.","Minigolf con vista al río Farmington en Unionville (218 River Rd); de temporada.")]
PLACES["drive"]+=[("The Perfect Toy","An independent toy store in Avon (290 W Main St).","Una juguetería independiente en Avon (290 W Main St)."),
                  ("The Claypen","Paint-your-own pottery in West Hartford (997 Farmington Ave).","Pinta tu propia cerámica en West Hartford (997 Farmington Ave)."),
                  ("Barnes & Noble, Westfarms","A new bookstore (opened July 2026) inside Westfarms mall, on the West Hartford side.","Una librería nueva (abrió en julio de 2026) dentro del centro comercial Westfarms, del lado de West Hartford.")]
TOWN["classes"]+=[
 {"id":"codersschool-farmington","c":"build","n":"theCoderSchool Farmington","u":"https://classcub.com/provider/thecoderschool-farmington-hartford-ct",
  "blurb":"Coding coaching two kids to a coach, plus group classes in block coding, Minecraft, Roblox and Python. Some fall classes are also offered through Farmington Continuing Ed.","ages":"6–17 years","where":"1051 Farmington Ave"},
]
ES.update({
 "Coding coaching two kids to a coach, plus group classes in block coding, Minecraft, Roblox and Python. Some fall classes are also offered through Farmington Continuing Ed.":"Clases de programación con un instructor por cada dos niños, además de clases grupales de programación por bloques, Minecraft, Roblox y Python. Algunas clases de otoño también se ofrecen por medio de Farmington Continuing Ed.",
 "6–17 years":"6–17 años",
})

# ---- patch: drop-childrens-museum-2026-10-08.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
DROP_PLACES.append("The Children's Museum")  # closed permanently (WFSB, Feb 4 2026)

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
