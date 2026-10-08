# Full playbook re-run, Oct 8 2026
FU="fired-up"; YP="youngs-pond"; WALSH="walsh-school"; FUS="https://www.firedupbranford.com/events-1/"
MR="https://branfordct.myrec.com/info/activities/program_details.aspx?ProgramID="
TOWN["venues"].update({FU:["Fired Up! pottery studio","1060 Main St"],YP:["Young's Pond Park (Blackstone Ave lot)","Blackstone Ave"],WALSH:["Walsh Intermediate School","185 Damascus Rd"]})
TOWN["venueMeta"].update({FU:[None,1],YP:[None,0],WALSH:[None,0]})
for e in TOWN["events"]:
    if e["t"]=="Friday Night Movie: Singin' in the Rain": e["when"]=[W("2026-10-16",[["19:00","21:00"]])]
    if e["t"]=="Holiday Parade & Tree Lighting": e["check"]=True
TOWN["events"]+=[
 {"t":"Kids' Cooking with Chef Mary","v":"trapasso","when":[W("2026-10-15",[["16:30","18:30"]]),W("2026-10-28",[["13:45","15:45"]]),W("2026-11-19",[["16:30","18:30"]]),W("2026-12-01",[["16:30","18:30"]]),W("2026-12-17",[["16:30","18:30"]])],"ages":"Ages 6–13","a":["big"],"free":False,"price":"$40–45 residents, $50–55 non-residents","rsvp":True,"src":MR+"30172",
  "blurb":"Hands-on themed cooking: skull pizza and skeleton cupcakes (Oct 15), a half-day session (Oct 28), turkey pasta and Oreo truffles (Nov 19), reindeer quesadillas (Dec 1) and Santa pizza (Dec 17). Register for each class."},
 {"t":"Kids' Insect Walk at Young's Pond","v":YP,"when":[W("2026-10-18",[["14:00","16:00"]])],"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","drop":True,"src":"https://branfordlandtrust.org/learn-about-the-creepy-crawlies-kids-insect-walk-at-youngs-pond/",
  "blurb":"A Branford Land Trust family walk (about 1.5 miles) through Young's Pond and Bob's Woods hunting for creepy crawlies."},
 {"t":"Haunted House LEGO Workshop","v":"trapasso","special":"hw","when":[W("2026-10-28",[["13:45","16:00"]])],"ages":"Ages 5–9","a":["big"],"free":False,"price":"$35 residents, $40 non-residents","rsvp":True,"src":MR+"30224",
  "blurb":"Play-Well's early-release-day workshop: build LEGO haunted houses and engineer traps."},
 {"t":"Dino Design LEGO Workshop","v":"trapasso","when":[W("2026-11-03",[["09:00","12:00"]])],"ages":"Ages 5–9","a":["big"],"free":False,"price":"$35 residents, $40 non-residents","rsvp":True,"src":MR+"30224",
  "blurb":"A no-school Election Day workshop designing LEGO dinosaur habitats."},
 {"t":"Fired Up! Tween Night","v":FU,"when":D(["2026-10-10","2026-11-14","2026-12-12"],[["19:00","21:00"]]),"ages":"Ages 9–13","a":["big"],"free":False,"price":"Pottery price; RSVP","rsvp":True,"check":True,"src":"https://www.firedupbranford.com/studioevents",
  "blurb":"A drop-off pottery-painting night just for tweens."},
 {"t":"Fired Up! Kids-Only Pizza Parties","v":FU,"special":"hw","when":[W("2026-10-24",[["17:00","19:00"]]),W("2026-10-25",[["15:30","17:00"]])],"ages":"Big kids (Oct 24); potty-trained little kids (Oct 25)","a":["preschool","big"],"free":False,"price":"$30","rsvp":True,"check":True,"src":FUS+"little-kids-only-pizza-party-10-25",
  "blurb":"Paint pottery, eat pizza and watch a Halloween movie: Hocus Pocus for big kids (Oct 24) and Muppets Haunted Mansion for little kids (Oct 25). Buy tickets ahead."},
 {"t":"Fired Up! Kids-Only Movie Night","v":FU,"when":D(["2026-11-21","2026-12-12"],[["17:00","19:00"]]),"ages":"Ages 4+ (potty-trained)","a":["preschool","big"],"free":False,"price":"$30","rsvp":True,"src":FUS+"kids-only-movie-night-pizza-party-11-21",
  "blurb":"A parents' night out with pottery painting, pizza and a movie: The Super Mario Galaxy (Nov 21) and Elf (Dec 12)."},
 {"t":"Thanksgiving 5K Kids' Fun Run","v":WALSH,"when":[W("2026-11-26",[["09:00","09:30"]])],"ages":"Ages 1–12","a":["toddler","preschool","big"],"free":False,"price":"$11.19 (more after Nov 1)","rsvp":True,"src":"https://runsignup.com/Race/Info/CT/Branford/BranfordRotaryBC2Thanksgiving5K",
  "blurb":"A kids' fun run at 9 on Thanksgiving morning, before the Rotary 5K (9:10) and 2-mile walk."},
 {"t":"Santa Claus is Coming to Fired Up!","v":FU,"special":"hol","when":[W("2026-11-29",[["09:00","11:00"]])],"ages":"Kids","a":["toddler","preschool","big"],"free":False,"price":"$40 with a pottery piece; $25 siblings","rsvp":True,"src":FUS+"santa-claus-is-coming-to-fired-up-4",
  "blurb":"A one-on-one visit and photos with Santa plus holiday pottery painting. Tickets close Nov 27."},
 {"t":"Holiday Showcase: An Original Musical","v":"legacy","special":"hol","when":[W("2026-12-05",[["10:45","11:05"]])],"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","drop":True,"src":MR+"30189",
  "blurb":"A free 20-minute show by the Legacy Theatre youth class; doors open at 10:30."},
 {"t":"Countdown to Noon","v":FU,"special":"hol","when":[W("2026-12-31",[["11:45","12:15"]])],"ages":"All ages + adult","a":B+["big"],"free":True,"price":"Free (free ticket at checkout)","rsvp":True,"src":FUS+"countdown-to-noon-3",
  "blurb":"Kids make noisemakers and count down to a Noon Year's ball drop at the pottery studio."},
 {"t":"Saturday Storytime","v":"wwml","when":[W("2026-10-24",[["10:30","11:00"]])],"ages":"All ages","a":B,"free":True,"price":"Free","drop":True,"src":"https://www.wwml.org/events",
  "blurb":"Songs and books at the Stony Creek library on the fourth Saturday of the month."},
 {"t":"LEGO Club","v":"wwml","when":[W("2026-10-28",[["16:00","17:00"]])],"ages":"Ages 8+","a":["big"],"free":True,"price":"Free","drop":True,"src":"https://www.wwml.org/events",
  "blurb":"Drop-in LEGO building on the early-release day."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Parks & Rec holiday programs","w":"Around Branford","p":"Every December: Write to Santa, Santa phone calls, a Santa gift delivery by fire truck, candy-cane and Olaf hunts, Santa's Workshop and a Reindeer Route house-decorating map. This year's dates aren't posted yet.","src":MR+"30178"},
 {"g":"fall","t":"Veterans Day Parade","w":"Branford Town Green and Main St","p":"A ceremony on the Green and a parade with Scouts, the high school band and a fife-and-drum corps, usually on the Sunday nearest Nov 11. This year's date isn't posted yet.","src":"https://www.newhavenindependent.org/article/veterans_day_parade_honors_all_who_served"},
]
TOWN["classes"]+=[
 {"id":"bf-play-well","c":"build","n":"Play-Well LEGO workshops","u":MR+"30224","blurb":"LEGO engineering workshops on half days and no-school days at the Community House.","ages":"5–9 years","where":"Joe Trapasso Community House, 46 Church St"},
 {"id":"bf-coder-school","c":"build","n":"theCoderSchool Branford","u":MR+"30399","blurb":"Minecraft, robotics and Python coding sessions in small groups.","ages":"7–13 years","where":"East Main St"},
 {"id":"bf-shoreline-art-music","c":"music","n":"Shoreline School of Art & Music","u":"https://local.zip06.com/branford-ct/shoreline-school-of-art-and-music-203-481-4830","blurb":"Lessons on most instruments plus drawing and painting classes.","ages":"Kids and adults","where":"540 E Main St"},
]
ADD_PLACES["rain"]+=[("Stony Creek Museum","A small village museum of Stony Creek and Thimble Islands history, open weekends 1–4 (84 Thimble Islands Rd).","Un pequeño museo de la historia de Stony Creek y las Thimble Islands, abierto los fines de semana de 1 a 4 (84 Thimble Islands Rd).")]
ES={
 "Ages 6–13":"6–13 años",
 "$40–45 residents, $50–55 non-residents":"$40–45 residentes, $50–55 no residentes",
 "Hands-on themed cooking: skull pizza and skeleton cupcakes (Oct 15), a half-day session (Oct 28), turkey pasta and Oreo truffles (Nov 19), reindeer quesadillas (Dec 1) and Santa pizza (Dec 17). Register for each class.":"Cocina temática práctica: pizza de calavera y cupcakes de esqueleto (15 de oct.), una sesión de medio día (28 de oct.), pasta de pavo y trufas de Oreo (19 de nov.), quesadillas de reno (1 de dic.) y pizza de Santa (17 de dic.). Inscríbete en cada clase.",
 "A Branford Land Trust family walk (about 1.5 miles) through Young's Pond and Bob's Woods hunting for creepy crawlies.":"Una caminata familiar de Branford Land Trust (unas 1.5 millas) por Young's Pond y Bob's Woods en busca de bichos.",
 "Ages 5–9":"5–9 años",
 "$35 residents, $40 non-residents":"$35 residentes, $40 no residentes",
 "Play-Well's early-release-day workshop: build LEGO haunted houses and engineer traps.":"Taller de Play-Well en día de salida temprana: construye casas embrujadas de LEGO y diseña trampas.",
 "A no-school Election Day workshop designing LEGO dinosaur habitats.":"Un taller en el Día de Elecciones, sin escuela, para diseñar hábitats de dinosaurios con LEGO.",
 "Ages 9–13":"9–13 años",
 "Pottery price; RSVP":"Precio de la cerámica; confirma asistencia",
 "A drop-off pottery-painting night just for tweens.":"Una noche de pintura de cerámica solo para preadolescentes, sin padres.",
 "Big kids (Oct 24); potty-trained little kids (Oct 25)":"Niños mayores (24 de oct.); pequeños que ya no usan pañal (25 de oct.)",
 "$30":"$30",
 "Paint pottery, eat pizza and watch a Halloween movie: Hocus Pocus for big kids (Oct 24) and Muppets Haunted Mansion for little kids (Oct 25). Buy tickets ahead.":"Pinta cerámica, come pizza y ve una película de Halloween: Hocus Pocus para los mayores (24 de oct.) y Muppets Haunted Mansion para los pequeños (25 de oct.). Compra los boletos con anticipación.",
 "Ages 4+ (potty-trained)":"4 años o más (sin pañal)",
 "A parents' night out with pottery painting, pizza and a movie: The Super Mario Galaxy (Nov 21) and Elf (Dec 12).":"Una noche libre para los papás con pintura de cerámica, pizza y una película: The Super Mario Galaxy (21 de nov.) y Elf (12 de dic.).",
 "Ages 1–12":"1–12 años",
 "$11.19 (more after Nov 1)":"$11.19 (sube después del 1 de nov.)",
 "A kids' fun run at 9 on Thanksgiving morning, before the Rotary 5K (9:10) and 2-mile walk.":"Una carrera divertida para niños a las 9 la mañana de Acción de Gracias, antes de los 5 km del Rotary (9:10) y la caminata de 2 millas.",
 "$40 with a pottery piece; $25 siblings":"$40 con una pieza de cerámica; $25 hermanos",
 "A one-on-one visit and photos with Santa plus holiday pottery painting. Tickets close Nov 27.":"Una visita individual y fotos con Santa, además de pintura de cerámica navideña. La venta de boletos cierra el 27 de nov.",
 "A free 20-minute show by the Legacy Theatre youth class; doors open at 10:30.":"Un show gratis de 20 minutos de la clase juvenil de Legacy Theatre; las puertas abren a las 10:30.",
 "All ages + adult":"Todas las edades + un adulto",
 "Free (free ticket at checkout)":"Gratis (boleto gratis al pagar)",
 "Kids make noisemakers and count down to a Noon Year's ball drop at the pottery studio.":"Los niños hacen matracas y cuentan hacia atrás hasta la caída de la bola de Año Nuevo al mediodía en el estudio de cerámica.",
 "Songs and books at the Stony Creek library on the fourth Saturday of the month.":"Canciones y libros en la biblioteca de Stony Creek el cuarto sábado del mes.",
 "Drop-in LEGO building on the early-release day.":"Construcción libre con LEGO en el día de salida temprana.",
 "Around Branford":"Por todo Branford",
 "Every December: Write to Santa, Santa phone calls, a Santa gift delivery by fire truck, candy-cane and Olaf hunts, Santa's Workshop and a Reindeer Route house-decorating map. This year's dates aren't posted yet.":"Cada diciembre: cartas a Santa, llamadas de Santa, entrega de regalos de Santa en camión de bomberos, búsquedas de bastones de caramelo y de Olaf, el Taller de Santa y un mapa de casas decoradas Reindeer Route. Las fechas de este año aún no se han publicado.",
 "Branford Town Green and Main St":"Branford Town Green y Main St",
 "A ceremony on the Green and a parade with Scouts, the high school band and a fife-and-drum corps, usually on the Sunday nearest Nov 11. This year's date isn't posted yet.":"Una ceremonia en el Green y un desfile con Scouts, la banda de la preparatoria y un cuerpo de pífanos y tambores, por lo general el domingo más cercano al 11 de nov. La fecha de este año aún no se ha publicado.",
 "LEGO engineering workshops on half days and no-school days at the Community House.":"Talleres de ingeniería con LEGO en días de medio día y sin escuela en el Community House.",
 "Minecraft, robotics and Python coding sessions in small groups.":"Sesiones de programación con Minecraft, robótica y Python en grupos pequeños.",
 "7–13 years":"7–13 años",
 "Lessons on most instruments plus drawing and painting classes.":"Clases de casi todos los instrumentos, además de clases de dibujo y pintura.",
 "Kids and adults":"Niños y adultos",
 "5–9 years":"5–9 años",
}
