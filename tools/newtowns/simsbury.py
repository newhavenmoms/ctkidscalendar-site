W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
L="simsbury-library"; SRC="https://simsbury.librarycalendar.com/events/month?age_groups%5B72%5D=72"
B=["baby","toddler","preschool"]
def ev(**k):
    e={"v":L,"free":True,"price":"Free","src":SRC}; e.update(k); return e
H=[["16:00","16:30"]]
TOWN={
 "display":"Simsbury","accent":"#C8E8E0",
 "venues":{L:["Simsbury Public Library","725 Hopmeadow St"],
           "hopmeadow":["Hopmeadow Street, Simsbury Center","Hopmeadow St"],
           "flamig":["Flamig Farm","7 Shingle Mill Rd, West Simsbury"]},
 "venueMeta":{L:[None,1],"hopmeadow":[None,0],"flamig":[None,0]},
 "events":[
  ev(t="Books & Bubbles Storytime",when=D(["2026-10-08","2026-10-15","2026-10-22","2026-10-29","2026-10-10","2026-10-12","2026-10-19","2026-10-26"],[["10:30","11:00"]]),ages="Ages 1–5 + caregiver",a=["toddler","preschool"],drop=True,
     blurb="Stories, songs, movement and bubbles, Mondays and Thursdays (plus Saturday, Oct 10). The posted series runs through October; the next one isn't posted yet."),
  ev(t="Born to Read",when=D(["2026-10-13","2026-10-20","2026-10-27"],[["10:00","10:30"]]),ages="Babies not yet walking + caregiver",a=["baby"],drop=True,
     blurb="Rhymes, songs, lap bounces and books for newborns and infants. Stay after for Baby Playgroup."),
  ev(t="Baby Playgroup",when=D(["2026-10-13","2026-10-20","2026-10-27"],[["10:30","11:00"]]),ages="Babies not yet walking + caregiver",a=["baby"],drop=True,
     blurb="Bubbles, social tummy time and conversation with other caregivers, right after Born to Read."),
  ev(t="Music and Movement",when=D(["2026-10-14","2026-10-28"],[["10:30","11:00"]]),ages="Birth–age 6 + caregiver",a=B,drop=True,
     blurb="Sing, dance and play with the parachute."),
  ev(t="Baby Yoga",when=[W("2026-10-09",[["10:00","10:45"]])],ages="9 weeks to crawling + caregiver",a=["baby"],rsvp=True,
     blurb="Songs, rhymes, stretches and simple yoga poses for babies and their grown-ups. Sign up online."),
  ev(t="Toddler Yoga",when=[W("2026-10-09",[["11:00","11:30"]])],ages="Ages 1–3 + caregiver",a=["toddler"],rsvp=True,
     blurb="Fun poses, creative movement and lively songs with your toddler. Sign up online."),
  ev(t="Toddler Art: Halloween Cauldrons",special="hw",when=[W("2026-10-16",[["10:00","11:00"]])],ages="Ages 1–5 + caregiver",a=["toddler","preschool"],drop=True,
     blurb="Make a Halloween cauldron with dot markers, pom-poms, glue and stickers. Drop in."),
  ev(t="Sensory Friendly Storytime",when=[W("2026-10-20",[["10:30","11:00"]])],ages="Ages 1–5 + caregiver",a=["toddler","preschool"],rsvp=True,
     blurb="An inclusive storytime for children with sensory sensitivities, autism or developmental differences. Sign up online."),
  ev(t="Little Leaps",when=[W("2026-10-21",[["10:00","11:00"]])],ages="Ages 1–4 + caregiver",a=["toddler","preschool"],rsvp=True,
     blurb="A creative-movement class exploring rhythm, tempo, levels and opposites: ages 1–2 at 10:00, ages 2–4 at 10:30. Sign up online."),
  ev(t="Bonjour, les mômes! French Time",when=D(["2026-10-23","2026-12-11"],[["10:30","11:15"]]),ages="Birth–age 5 + caregiver",a=B,rsvp=True,
     blurb="Stories, music, movement and props in French (with some English). Sign up online."),
  ev(t="Halloween Storytime & Parade",special="hw",when=[W("2026-10-30",[["10:30","11:00"]])],ages="Birth–age 5 + caregiver",a=B,drop=True,
     blurb="A Halloween storytime, then a costume parade collecting candy at each service desk. Costumes encouraged for kids and parents."),
  ev(t="Chess Club",when=D(["2026-10-14","2026-10-28"],[["16:00","17:00"]]),ages="Grades 2–6",a=["big"],rsvp=True,
     blurb="Learn chess or improve your game. Kids should know how the pieces move. Sign up online."),
  ev(t="Tween Club",when=[W("2026-10-08",[["16:00","16:45"]])],ages="Grades 5–6",a=["big"],rsvp=True,
     blurb="A monthly tween hangout. October: Halloween shrinky dinks. Sign up online."),
  ev(t="Whimsy Workshop",when=D(["2026-10-13","2026-10-27"],H),ages="Grades 3–6",a=["big"],rsvp=True,
     blurb="Decorate a Halloween tote bag (Oct 13, waitlist) or make Halloween squeegee art (Oct 27). Sign up online."),
  ev(t="Build with Dominoes",when=[W("2026-10-22",[["18:00","19:00"]])],ages="Grades K–6",a=["big"],rsvp=True,
     blurb="Build and topple domino creations. Sign up online."),
  ev(t="Kids Book Club",when=[W("2026-10-22",H)],ages="Grades 4–6",a=["big"],rsvp=True,
     blurb="Ms. Katie's new book club, with refreshments. October's book is Miss Mary Is Scary! Sign up online."),
  ev(t="Kids Cooking Club",when=[W("2026-10-26",H)],ages="Grades 3–6 + caregiver",a=["big"],rsvp=True,check=True,
     blurb="Make guacamole and salsa to eat with chips. Waitlist only."),
  ev(t="Kids Halloween Party & Costume Contest",special="hw",when=[W("2026-10-29",H)],ages="Grades K–6",a=["big"],rsvp=True,
     blurb="Compete for funniest, scariest, most creative, fan favorite and best DIY costume. Sign up online."),
  ev(t="Spookulele with the Kinetic Ukes Ensemble",special="hw",when=[W("2026-10-29",[["18:00","20:00"]])],ages="All ages",a=B+["big"],rsvp=True,
     blurb="A family-friendly Halloween ukulele concert with a few thrills and chills. Sign up online."),
  ev(t="Family Photo Shoot",when=[W("2026-11-14",[["10:00","17:00"]]),W("2026-11-15",[["14:00","16:00"]]),W("2026-11-21",[["10:00","17:00"]]),W("2026-11-22",[["14:00","16:00"]])],ages="All ages",a=B+["big"],rsvp=True,
     blurb="The Simsbury Camera Club takes free family portraits for holiday cards. Call the library to sign up."),
  {"t":"Simsbury Celebrates","v":"hopmeadow","special":"hol","when":[W("2026-11-28",[["17:00","20:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://www.simsbury-ct.gov/node/176641",
   "blurb":"Simsbury's holiday night on Hopmeadow Street: a lit-up fire-truck parade, photos with Santa, inflatables, live music (including holiday songs in the library's Children's Room) and fireworks over Simsbury Meadows around 8:15. Times are from past years."},
  {"t":"Halloween at the Farm with Farmer Debbie","v":"flamig","special":"hw","when":[W("2026-10-30",[["10:00","11:00"]])],"ages":"Young children","a":["toddler","preschool"],"free":False,"price":"Tickets required","rsvp":True,"check":True,"src":"https://flamigfarm.yapsody.com/event/index/857093/Halloween-at-The-Farm-with-Farmer-Debbie",
   "blurb":"A Halloween morning at Flamig Farm with Farmer Debbie. Buy tickets ahead; check the farm's listing for details."},
 ],
 "tba":[],
 "classes":[],
 "library":{"for":"Free, every week","name":"Simsbury Public Library","desc":"Books & Bubbles storytimes, Born to Read and a baby playgroup, music and movement, yoga and French for little ones, plus after-school clubs and crafts in the Discovery Center. Many school-age programs fill fast; sign up online.","a":"See children's events","href":SRC},
}
PLACES={
 "out":[("Talcott Mountain State Park","A steep-ish 1.25-mile climb to Heublein Tower and big views of the Farmington Valley. The tower opens through late October.","Una subida algo empinada de 2 km hasta Heublein Tower con grandes vistas del valle de Farmington. La torre abre hasta finales de octubre."),
        ("Simsbury Farms","The town recreation complex, with trails, a playground and outdoor skating in winter.","El complejo recreativo del pueblo, con senderos, área de juegos y patinaje al aire libre en invierno."),
        ("Flamig Farm","A family farm in West Simsbury with farm animals, pony rides and seasonal programs.","Una granja familiar en West Simsbury con animales, paseos en poni y programas de temporada.")],
 "rain":[("Simsbury Public Library","The Discovery Center and Children's Room host storytimes, playgroups and after-school clubs.","El Discovery Center y la sala infantil ofrecen cuentacuentos, grupos de juego y clubes después de clases."),
         ("International Skating Center of Connecticut","An indoor rink complex with public skating sessions; check the schedule before you go.","Un complejo de pistas de hielo techadas con sesiones de patinaje público; consulta el horario antes de ir.")],
 "drive":[("The Children's Museum","Live animals, a planetarium and hands-on exhibits in West Hartford.","Animales vivos, un planetario y exposiciones interactivas en West Hartford."),
          ("McLean Game Refuge","Wooded trails and ponds in Granby, free and quiet.","Senderos en el bosque y estanques en Granby, gratis y tranquilos."),
          ("Hill-Stead Museum","Meadows, gardens, trails and sheep in Farmington, with family events.","Praderas, jardines, senderos y ovejas en Farmington, con eventos familiares.")],
}
ES={
 "Ages 1–5 + caregiver":"1–5 años + un adulto",
 "Stories, songs, movement and bubbles, Mondays and Thursdays (plus Saturday, Oct 10). The posted series runs through October; the next one isn't posted yet.":"Cuentos, canciones, movimiento y burbujas, lunes y jueves (y el sábado 10 de oct.). La serie publicada llega hasta octubre; la siguiente aún no se ha publicado.",
 "Babies not yet walking + caregiver":"Bebés que aún no caminan + un adulto",
 "Rhymes, songs, lap bounces and books for newborns and infants. Stay after for Baby Playgroup.":"Rimas, canciones, juegos en el regazo y libros para recién nacidos y bebés. Quédate después para el Baby Playgroup.",
 "Bubbles, social tummy time and conversation with other caregivers, right after Born to Read.":"Burbujas, tiempo boca abajo con otros bebés y conversación con otros cuidadores, justo después de Born to Read.",
 "Birth–age 6 + caregiver":"0–6 años + un adulto",
 "Sing, dance and play with the parachute.":"Canta, baila y juega con el paracaídas.",
 "9 weeks to crawling + caregiver":"9 semanas hasta gatear + un adulto",
 "Songs, rhymes, stretches and simple yoga poses for babies and their grown-ups. Sign up online.":"Canciones, rimas, estiramientos y posturas de yoga sencillas para bebés y sus adultos. Inscríbete en línea.",
 "Ages 1–3 + caregiver":"1–3 años + un adulto",
 "Fun poses, creative movement and lively songs with your toddler. Sign up online.":"Posturas divertidas, movimiento creativo y canciones animadas con tu niño pequeño. Inscríbete en línea.",
 "Make a Halloween cauldron with dot markers, pom-poms, glue and stickers. Drop in.":"Haz un caldero de Halloween con marcadores de puntos, pompones, pegamento y calcomanías. Sin inscripción.",
 "An inclusive storytime for children with sensory sensitivities, autism or developmental differences. Sign up online.":"Un cuentacuentos inclusivo para niños con sensibilidad sensorial, autismo o diferencias en el desarrollo. Inscríbete en línea.",
 "Ages 1–4 + caregiver":"1–4 años + un adulto",
 "A creative-movement class exploring rhythm, tempo, levels and opposites: ages 1–2 at 10:00, ages 2–4 at 10:30. Sign up online.":"Una clase de movimiento creativo que explora ritmo, tempo, niveles y opuestos: 1–2 años a las 10:00 y 2–4 años a las 10:30. Inscríbete en línea.",
 "Birth–age 5 + caregiver":"0–5 años + un adulto",
 "Stories, music, movement and props in French (with some English). Sign up online.":"Cuentos, música, movimiento y accesorios en francés (con algo de inglés). Inscríbete en línea.",
 "A Halloween storytime, then a costume parade collecting candy at each service desk. Costumes encouraged for kids and parents.":"Un cuentacuentos de Halloween y luego un desfile de disfraces recogiendo dulces en cada mostrador. Se anima a niños y padres a disfrazarse.",
 "Grades 2–6":"2.º a 6.º grado",
 "Learn chess or improve your game. Kids should know how the pieces move. Sign up online.":"Aprende ajedrez o mejora tu juego. Los niños deben saber cómo se mueven las piezas. Inscríbete en línea.",
 "Grades 5–6":"5.º a 6.º grado",
 "A monthly tween hangout. October: Halloween shrinky dinks. Sign up online.":"Una reunión mensual para preadolescentes. Octubre: shrinky dinks de Halloween. Inscríbete en línea.",
 "Grades 3–6":"3.º a 6.º grado",
 "Decorate a Halloween tote bag (Oct 13, waitlist) or make Halloween squeegee art (Oct 27). Sign up online.":"Decora una bolsa de Halloween (13 de oct., lista de espera) o haz arte de Halloween con espátula (27 de oct.). Inscríbete en línea.",
 "Grades K–6":"Kínder a 6.º grado",
 "Build and topple domino creations. Sign up online.":"Construye y derriba creaciones de dominó. Inscríbete en línea.",
 "Grades 4–6":"4.º a 6.º grado",
 "Ms. Katie's new book club, with refreshments. October's book is Miss Mary Is Scary! Sign up online.":"El nuevo club de lectura de Ms. Katie, con refrigerios. El libro de octubre es Miss Mary Is Scary! Inscríbete en línea.",
 "Grades 3–6 + caregiver":"3.º a 6.º grado + un adulto",
 "Make guacamole and salsa to eat with chips. Waitlist only.":"Prepara guacamole y salsa para comer con totopos. Solo lista de espera.",
 "Compete for funniest, scariest, most creative, fan favorite and best DIY costume. Sign up online.":"Compite por el disfraz más gracioso, más aterrador, más creativo, favorito del público y mejor hecho en casa. Inscríbete en línea.",
 "All ages":"Todas las edades",
 "A family-friendly Halloween ukulele concert with a few thrills and chills. Sign up online.":"Un concierto familiar de ukelele de Halloween con algunos sustos. Inscríbete en línea.",
 "The Simsbury Camera Club takes free family portraits for holiday cards. Call the library to sign up.":"El Simsbury Camera Club toma retratos familiares gratis para tarjetas navideñas. Llama a la biblioteca para inscribirte.",
 "Simsbury's holiday night on Hopmeadow Street: a lit-up fire-truck parade, photos with Santa, inflatables, live music (including holiday songs in the library's Children's Room) and fireworks over Simsbury Meadows around 8:15. Times are from past years.":"La noche navideña de Simsbury en Hopmeadow Street: desfile de camiones de bomberos iluminados, fotos con Santa, inflables, música en vivo (incluidas canciones navideñas en la sala infantil de la biblioteca) y fuegos artificiales sobre Simsbury Meadows alrededor de las 8:15. El horario es de años anteriores.",
 "Young children":"Niños pequeños",
 "Tickets required":"Se requieren boletos",
 "A Halloween morning at Flamig Farm with Farmer Debbie. Buy tickets ahead; check the farm's listing for details.":"Una mañana de Halloween en Flamig Farm con Farmer Debbie. Compra boletos con anticipación; consulta los detalles en la página de la granja.",
 "Books & Bubbles storytimes, Born to Read and a baby playgroup, music and movement, yoga and French for little ones, plus after-school clubs and crafts in the Discovery Center. Many school-age programs fill fast; sign up online.":"Cuentacuentos Books & Bubbles, Born to Read y un grupo de juego para bebés, música y movimiento, yoga y francés para los pequeños, además de clubes y manualidades después de clases en el Discovery Center. Muchos programas para escolares se llenan rápido; inscríbete en línea.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7) ----
AB="apple-barn"; SHS="simsbury-historical"; PT="phelps-tavern"; SFL="simsbury-free-library"
TOWN["venues"].update({AB:["Apple Barn, Simsbury Farms","60 Old Farms Rd"],SHS:["Simsbury Historical Society (Ellsworth Visitor Center)","10 Phelps Ln"],PT:["Phelps Tavern Museum","800 Hopmeadow St"],SFL:["Simsbury Free Library","749 Hopmeadow St"]})
TOWN["venueMeta"].update({AB:[None,1],SHS:[None,1],PT:[None,1],SFL:[None,1]})
MR="https://simsburyct.myrec.com/info/activities/program_details.aspx?ProgramID="
SH="https://simsburyhistory.org/events-programs/"
TOWN["events"]+=[
 {"t":"Little Makers Saturdays","v":AB,"when":D(["2026-10-17","2026-11-07","2026-12-12"],[["09:00","11:00"]]),"ages":"Ages 4–7","a":["preschool","big"],"free":False,"price":"$35 per class","rsvp":True,"src":MR+"29026",
  "blurb":"Two one-hour Saturday classes from Simsbury Recreation: Little Chefs (9–10) and Colorful Creations art (10–11, drop-off). Sign up for one or both."},
 {"t":"Murder at 3 Corner Pond: A Colonial Tale","v":SHS,"special":"hw","when":[{"from":"2026-10-22","to":"2026-10-25","t":[]}],"ages":"Check age guidance","a":["big"],"free":False,"price":"Tickets via Playland Productions","check":True,"src":SH,
  "blurb":"A 'spooky fun' play based on the local legend of the Witch of Simsbury, staged in the historical society's Meeting House by Playland Productions. Check times and age guidance when you buy tickets."},
 {"t":"Slate and Sled Painting","v":SHS,"when":[W("2026-11-21",[["10:00","12:00"],["13:00","15:00"]])],"ages":"Check with the society","a":["big"],"free":False,"price":"Materials included; register ahead","rsvp":True,"check":True,"src":SH,
  "blurb":"Paint a slate or a wooden sled, with all materials included. Advance registration and payment required."},
 {"t":"Gingerbread House Display","v":SFL,"special":"hol","when":[{"from":"2026-11-22","to":"2026-11-29","t":[]}],"ages":"All ages","a":B+["big"],"free":True,"price":"Free to view","drop":True,"check":True,"src":MR+"25169",
  "blurb":"Entries in the Simsbury Celebrates gingerbread competition, including a youth category for builders 15 and under, on display for a week. To enter, register by Nov 17 ($15) and drop off Nov 22, 11–12:30."},
 {"t":"Children's Holiday Tea Party","v":PT,"special":"hol","when":[W("2026-12-05",[["14:00","15:30"]])],"ages":"Ages 7 and up + adult","a":["big"],"free":False,"price":"See society","rsvp":True,"check":True,"src":SH,
  "blurb":"A Victorian-style holiday tea at the historic Phelps Tavern. Registration details are coming from the historical society."},
]
TOWN["classes"]+=[
 {"id":"sims-tumble-tots","c":"move","n":"Tumble Tots with Playstrong (Simsbury Rec)","u":MR+"28937",
  "blurb":"Thursday-morning tumbling: Tiny Tots (18 months–3, with a grown-up) and Pre-Tumble (3–5). Six-week Fall 2 session Oct 29–Dec 10, $105.","ages":"18 months–5","where":"Boy Scout Hall, 695 Hopmeadow St"},
 {"id":"sims-little-makers","c":"art","n":"Little Makers (Simsbury Rec)","u":MR+"29007",
  "blurb":"Monday-afternoon cooking (Little Chefs) and art (Colorful Creations) classes at Holcomb Farm, in sessions from Oct 12 and Nov 16, $140.","ages":"4–7","where":"Holcomb Farm"},
 {"id":"sims-mad-science","c":"build","n":"Mad Science After School (Simsbury Rec)","u":MR+"28917",
  "blurb":"Six Monday afternoons of hands-on chemistry ('Crazy Chemworks'), Oct 19–Nov 23, $190.","ages":"Grades K–5","where":"Apple Barn, 60 Old Farms Rd"},
 {"id":"sims-youth-acting","c":"art","n":"Youth Acting (Simsbury Rec)","u":MR+"29082",
  "blurb":"Theatre games, improv, voice and stage skills with Michael Lamb on Fridays (K–2 and 3–6). Fall session Oct 2–Nov 13; watch for winter dates.","ages":"Grades K–6","where":"Apple Barn, 60 Old Farms Rd"},
 {"id":"sims-rec-dance","c":"dance","n":"Fairytale Ballet & Pop Star Jazz (Simsbury Rec)","u":MR+"29029",
  "blurb":"Short Tuesday dance classes for little dancers; the fall session runs through Nov 17.","ages":"3–9","where":"Eno Memorial Hall"},
 {"id":"sims-skating","c":"move","n":"Skating Lessons at Simsbury Farms","u":MR+"25307",
  "blurb":"Sunday learn-to-skate lessons on the covered outdoor rink. The Nov–Dec session is full; session 2 (Dec 27–Jan 24) opens for registration Nov 2. Free rental skates.","ages":"4–18","where":"Simsbury Farms rink"},
 {"id":"gym-training-center","c":"move","n":"Gymnastics Training Center","u":"https://mommypoppins.com/index%2ephp/connecticut-kids/classes-enrichment/best-gymnastics-classes",
  "blurb":"Recreational and competitive gymnastics from toddler classes through grade school.","ages":"Babies–teens","where":"Simsbury"},
]
PLACES["out"]=[p for p in PLACES["out"] if p[0]!="Simsbury Farms"]
PLACES["out"].insert(1,("Simsbury Farms","The town recreation complex at 100 Old Farms Rd: trails, a playground, and a covered outdoor skating rink that opens in mid-November.","El complejo recreativo del pueblo en 100 Old Farms Rd: senderos, área de juegos y una pista de patinaje techada al aire libre que abre a mediados de noviembre."))
PLACES["rain"]+=[("Necker's Toyland","A family-run toy store since 1948, full of hands-on toys, building sets and science kits; closed Tuesdays (1591 Hopmeadow St).","Una juguetería familiar desde 1948, llena de juguetes prácticos, sets de construcción y kits de ciencia; cerrada los martes (1591 Hopmeadow St)."),
                 ("Simsbury Historical Society","The Phelps Tavern Museum and a campus of historic buildings, with family programs and a December holiday market (800 Hopmeadow St).","El Phelps Tavern Museum y un conjunto de edificios históricos, con programas familiares y un mercado navideño en diciembre (800 Hopmeadow St).")]
ES.update({
 "Ages 4–7":"4–7 años",
 "$35 per class":"$35 por clase",
 "Two one-hour Saturday classes from Simsbury Recreation: Little Chefs (9–10) and Colorful Creations art (10–11, drop-off). Sign up for one or both.":"Dos clases de una hora los sábados de Simsbury Recreation: Little Chefs (9–10) y arte Colorful Creations (10–11, sin padres). Inscríbete en una o en las dos.",
 "Check age guidance":"Consulta la guía de edades",
 "Tickets via Playland Productions":"Boletos con Playland Productions",
 "A 'spooky fun' play based on the local legend of the Witch of Simsbury, staged in the historical society's Meeting House by Playland Productions. Check times and age guidance when you buy tickets.":"Una obra 'de miedo divertido' basada en la leyenda local de la Bruja de Simsbury, presentada por Playland Productions en el Meeting House de la sociedad histórica. Consulta horarios y edades al comprar los boletos.",
 "Check with the society":"Consulta con la sociedad",
 "Materials included; register ahead":"Materiales incluidos; inscríbete antes",
 "Paint a slate or a wooden sled, with all materials included. Advance registration and payment required.":"Pinta una pizarra o un trineo de madera, con todos los materiales incluidos. Se requiere inscripción y pago por adelantado.",
 "Free to view":"Gratis para ver",
 "Entries in the Simsbury Celebrates gingerbread competition, including a youth category for builders 15 and under, on display for a week. To enter, register by Nov 17 ($15) and drop off Nov 22, 11–12:30.":"Las casitas del concurso de jengibre de Simsbury Celebrates, con una categoría juvenil para menores de 15 años, en exhibición durante una semana. Para participar, inscríbete antes del 17 de nov. ($15) y entrega tu casita el 22 de nov., de 11 a 12:30.",
 "Ages 7 and up + adult":"Desde 7 años + un adulto",
 "See society":"Consulta con la sociedad",
 "A Victorian-style holiday tea at the historic Phelps Tavern. Registration details are coming from the historical society.":"Un té navideño de estilo victoriano en la histórica Phelps Tavern. La sociedad histórica publicará pronto los detalles de inscripción.",
 "Thursday-morning tumbling: Tiny Tots (18 months–3, with a grown-up) and Pre-Tumble (3–5). Six-week Fall 2 session Oct 29–Dec 10, $105.":"Acrobacia los jueves por la mañana: Tiny Tots (18 meses–3 años, con un adulto) y Pre-Tumble (3–5 años). Sesión de otoño 2 de seis semanas, del 29 de oct. al 10 de dic., $105.",
 "18 months–5":"18 meses–5 años",
 "Boy Scout Hall, 695 Hopmeadow St":"Boy Scout Hall, 695 Hopmeadow St",
 "Monday-afternoon cooking (Little Chefs) and art (Colorful Creations) classes at Holcomb Farm, in sessions from Oct 12 and Nov 16, $140.":"Clases de cocina (Little Chefs) y arte (Colorful Creations) los lunes por la tarde en Holcomb Farm, en sesiones desde el 12 de oct. y el 16 de nov., $140.",
 "4–7":"4–7 años",
 "Six Monday afternoons of hands-on chemistry ('Crazy Chemworks'), Oct 19–Nov 23, $190.":"Seis tardes de lunes de química práctica ('Crazy Chemworks'), del 19 de oct. al 23 de nov., $190.",
 "Theatre games, improv, voice and stage skills with Michael Lamb on Fridays (K–2 and 3–6). Fall session Oct 2–Nov 13; watch for winter dates.":"Juegos teatrales, improvisación, voz y técnica escénica con Michael Lamb los viernes (kínder–2.º y 3.º–6.º). Sesión de otoño del 2 de oct. al 13 de nov.; atento a las fechas de invierno.",
 "Grades K–6":"Kínder a 6.º grado",
 "Short Tuesday dance classes for little dancers; the fall session runs through Nov 17.":"Clases cortas de danza los martes para bailarines pequeños; la sesión de otoño dura hasta el 17 de nov.",
 "3–9":"3–9 años",
 "Sunday learn-to-skate lessons on the covered outdoor rink. The Nov–Dec session is full; session 2 (Dec 27–Jan 24) opens for registration Nov 2. Free rental skates.":"Clases de patinaje los domingos en la pista techada al aire libre. La sesión de nov.–dic. está llena; la sesión 2 (27 de dic.–24 de ene.) abre inscripciones el 2 de nov. Renta de patines gratis.",
 "4–18":"4–18 años",
 "Simsbury Farms rink":"Pista de Simsbury Farms",
 "Recreational and competitive gymnastics from toddler classes through grade school.":"Gimnasia recreativa y competitiva desde clases para niños pequeños hasta primaria.",
 "Babies–teens":"Bebés–adolescentes",
})

# ---- creative places / bookstores / blogs pass (Oct 8) ----
SHS="simsbury-hs"
TOWN["venues"][SHS]=["Simsbury High School Auditorium","34 Farms Village Rd"]; TOWN["venueMeta"][SHS]=[None,1]
TOWN["events"]+=[
 {"t":"Disney's The Little Mermaid (Theatre Guild of Simsbury)","v":SHS,"special":"shows","when":[W("2026-10-09",[["19:30","22:00"]]),W("2026-10-10",[["19:30","22:00"]]),W("2026-10-11",[["14:00","16:30"]]),W("2026-10-17",[["14:00","16:30"],["19:30","22:00"]]),W("2026-10-18",[["14:00","16:30"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"See ticket site","rsvp":True,"check":True,"src":"https://www.theatreguildsimsbury.org/our-season/the-little-mermaid",
  "blurb":"The town's community theater stages the Disney musical. Sunday and Oct 17 matinees are at 2; end times are estimates."},
 {"t":"Family Friendly Haunted Walk Through","v":"flamig","special":"hw","when":D(["2026-10-16","2026-10-17","2026-10-23","2026-10-24"],[["18:00","20:00"]]),"ages":"Ages 3+","a":["preschool","big"],"free":False,"price":"$16 per person + fees","rsvp":True,"src":"https://flamigfarm.yapsody.com/event/index/874655/-Family-Friendly-Haunted-Walk-Through",
  "blurb":"A spooky-character walk through Flamig Farm. The 6–7pm hour is milder, 7–8 scarier. Timed tickets in advance; no strollers; Sunday is the rain date."},
]
TOWN["classes"]+=[
 {"id":"flamig-toddlers","c":"nature","n":"Toddlers on the Farm (Flamig Farm)","u":"https://flamigfarm.yapsody.com",
  "blurb":"Weekday-morning farm sessions with the animals for 2- and 3-year-olds (9:30–10:45). October runs as 4-week sessions ($120), November as 2-week sessions ($60).","ages":"2–3 years","where":"7 Shingle Mill Rd, West Simsbury"},
 {"id":"playhouse-academy-simsbury","c":"art","n":"Playhouse Theatre Academy (Simsbury)","u":"https://www.broadwayworld.com/article/Playhouse-Theatre-Academy-to-Offer-Fall-Classes-20260822",
  "blurb":"Drama and musical-theater classes from age 3: Once Upon a Twist (3–7), Mini-Mainstage (6–8) and a SpongeBob musical class (9–13). Free trial class; 860-523-5900 x16.","ages":"3–13 years","where":"Simsbury"},
]
PLACES["rain"]+=[("FunMax Adventure Park","A big indoor park with trampolines, a ninja course, foam pits, a climbing wall and a multi-level playground for younger kids (Simsbury Commons, 532 Bushy Hill Rd).","Un gran parque techado con trampolines, circuito ninja, fosas de espuma, muro de escalada y un área de juegos de varios niveles para los más pequeños (Simsbury Commons, 532 Bushy Hill Rd)."),
                 ("Gather On Hopmeadow","A creative workshop studio that runs seasonal craft workshops, including kids' and holiday sessions (961 Hopmeadow St).","Un estudio de talleres creativos con talleres de temporada, incluidos talleres para niños y de las fiestas (961 Hopmeadow St).")]
ES.update({
 "See ticket site":"Ver el sitio de boletos",
 "The town's community theater stages the Disney musical. Sunday and Oct 17 matinees are at 2; end times are estimates.":"El teatro comunitario del pueblo presenta el musical de Disney. Las funciones de los domingos y del 17 de oct. por la tarde son a las 2; las horas de término son aproximadas.",
 "Ages 3+":"3 años o más",
 "$16 per person + fees":"$16 por persona + cargos",
 "A spooky-character walk through Flamig Farm. The 6–7pm hour is milder, 7–8 scarier. Timed tickets in advance; no strollers; Sunday is the rain date.":"Un recorrido por Flamig Farm con personajes espeluznantes. De 6 a 7 p. m. es más suave y de 7 a 8, más aterrador. Boletos con horario por adelantado; sin carriolas; el domingo es la fecha en caso de lluvia.",
 "Weekday-morning farm sessions with the animals for 2- and 3-year-olds (9:30–10:45). October runs as 4-week sessions ($120), November as 2-week sessions ($60).":"Sesiones en la granja con los animales entre semana por la mañana para niños de 2 y 3 años (9:30–10:45). En octubre son sesiones de 4 semanas ($120) y en noviembre de 2 semanas ($60).",
 "2–3 years":"2–3 años",
 "Drama and musical-theater classes from age 3: Once Upon a Twist (3–7), Mini-Mainstage (6–8) and a SpongeBob musical class (9–13). Free trial class; 860-523-5900 x16.":"Clases de teatro y teatro musical desde los 3 años: Once Upon a Twist (3–7), Mini-Mainstage (6–8) y una clase del musical de SpongeBob (9–13). Clase de prueba gratis; 860-523-5900 ext. 16.",
 "3–13 years":"3–13 años",
})

# ---- patch: simsbury-2026-10-08b.py ----
ADD_PLACES={'out':[],'rain':[],'drive':[]}; REPLACE_PLACES={}; DROP_PLACES=[]
_ES_before=dict(ES)
# Out and About Mom blog leads (owner request Oct 8): public parks
ADD_PLACES["out"]+=[("Rotary Park Boundless Playground","An accessible 'boundless' playground designed so kids of all abilities can play together (Rotary Park, Weatogue).","Un parque infantil accesible 'boundless', diseñado para que niños de todas las capacidades jueguen juntos (Rotary Park, Weatogue)."),
                    ("Stratton Brook State Park","A state park with an easy, flat rail-trail loop, a pond and picnic areas; good for strollers and bikes.","Un parque estatal con un circuito plano y fácil sobre una antigua vía de tren, un estanque y áreas de picnic; bueno para carriolas y bicicletas.")]

ES.update(globals().get('ES_PATCH', {}))
for _k,_v in ADD_PLACES.items(): PLACES[_k]+=_v
for _k in PLACES: PLACES[_k]=[REPLACE_PLACES.get(p[0],p) for p in PLACES[_k] if p[0] not in DROP_PLACES]
