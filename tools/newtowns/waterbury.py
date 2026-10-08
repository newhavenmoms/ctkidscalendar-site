W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
L="bronson-library"; SRC="https://www.bronsonlibrary.org/kidprograms"
B=["baby","toddler","preschool"]
def ev(**k):
    e={"v":L,"free":True,"price":"Free","src":SRC}; e.update(k); return e
T1=[["10:30","11:00"]]
MATT="https://www.mattmuseum.org/?p=32793"
TOWN={
 "display":"Waterbury","accent":"#CDE8D6",
 "venues":{L:["Silas Bronson Library","267 Grand St"],
           "matt":["Mattatuck Museum","144 W Main St"]},
 "venueMeta":{L:[None,1],"matt":[None,1]},
 "events":[
  ev(t="Toddlers, Tales and Tunes",s=[[2,T1,"2026-10-13","2026-11-24"]],ages="Ages 6 and under + caregiver",a=B,drop=True,
     blurb="Stories, songs and rhymes in the Picture Book Room, every Tuesday morning."),
  ev(t="Wonderful Wednesday Stories",s=[[3,T1,"2026-10-14","2026-11-25"]],x=["2026-11-11"],ages="Young children + caregiver",a=B,drop=True,
     blurb="A weekly Wednesday-morning storytime in the Picture Book Room."),
  ev(t="Story Nook Thursdays",s=[[4,T1,"2026-10-08","2026-11-19"]],ages="Young children + caregiver",a=B,drop=True,
     blurb="A weekly Thursday-morning storytime in the Children's Room."),
  ev(t="KidZone Coding Club",s=[[2,[["16:30","17:30"]],"2026-10-13","2026-11-24"]],ages="Ages 7–12 (beginners)",a=["big"],check=True,
     blurb="Beginner coding for kids in the library's Computer Classroom, Tuesday afternoons."),
  ev(t="You Can Call Me Trixie",when=[W("2026-10-10",[["11:00","12:00"]])],ages="Ages 4–11",a=["preschool","big"],check=True,
     blurb="A Saturday-morning program for kids in the Children's Room. See the library's page for details."),
  ev(t="Third Thursday Tales",when=D(["2026-10-15","2026-11-19"],[["18:00","19:00"]]),ages="Ages 3–10",a=["preschool","big"],drop=True,
     blurb="An evening storytime in the Picture Book Room, once a month."),
  ev(t="Where in the Library Is Silas the Cat?",when=D(["2026-10-15","2026-11-19"],[["10:00","17:00"]]),ages="Ages 2 and up",a=["toddler","preschool","big"],drop=True,check=True,
     blurb="An all-day seek-and-find in the KidZone: track down Silas the Cat hiding somewhere in the library. Come any time the library is open."),
  ev(t="Fourth Friday Fun Factory",when=D(["2026-10-23","2026-11-27"],[["15:00","16:00"]]),ages="Ages 3–12",a=["preschool","big"],drop=True,
     blurb="A Friday-afternoon activity hour in the Children's Room, once a month."),
  ev(t="Waterbury Witch and Wizard Day",special="hw",when=[W("2026-10-31",[["11:00","15:00"]])],ages="Kids of all ages",a=B+["big"],drop=True,check=True,
     blurb="A Halloween-day celebration of witches and wizards with the library's Mardi Gross festivities. Costumes welcome; check the library's page for the lineup."),
  ev(t="Sleepy Hollow Story Time & Craft",when=[W("2026-11-13",[["15:00","16:00"]])],ages="Kids",a=["preschool","big"],drop=True,
     blurb="A Legend of Sleepy Hollow story and a craft in the Children's Room."),
  {"t":"Chess Lessons at the Mattatuck","v":"matt","when":D(["2026-10-17","2026-10-24","2026-10-31"],[["10:30","13:00"]]),"ages":"All ages and skill levels","a":["big"],"free":True,"price":"Free","rsvp":True,"src":MATT,
   "blurb":"Free Saturday chess lessons at the museum for every age and skill level. Registration required."},
  {"t":"Free Admission Day at the Mattatuck","v":"matt","when":[W("2026-10-10",[["11:00","17:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":MATT,
   "blurb":"Free admission to the museum's galleries of Connecticut art and history, on the second Saturday of the month."},
  {"t":"School's Out Day Camp: Mixed Media Medicine","v":"matt","when":[W("2026-10-12",[["09:30","15:30"]])],"ages":"School-age kids","a":["big"],"free":False,"price":"$50 ($35 members)","rsvp":True,"check":True,"src":MATT,
   "blurb":"A full day of art-making at the museum on the Columbus Day school holiday, with early drop-off from 8 and late pick-up until 5. Registration required."},
 ],
 "tba":[{"g":"hol","t":"Waterbury Tree Lighting","w":"Waterbury Green, downtown",
   "p":"Waterbury lights its tree on the Green each year after Thanksgiving, with choirs including the Waterbury PAL Choir, crafts, photos and hot cocoa. Last year it was the Saturday after Thanksgiving. This year's date isn't posted yet.","src":"https://thewaterburytimes.com/2025/11/29/waterbury-tree-lighting-ceremony-2025/"}],
 "classes":[],
 "library":{"for":"Free, every week","name":"Silas Bronson Library","desc":"Storytimes three mornings a week (Toddlers, Tales and Tunes on Tuesdays, Wonderful Wednesday Stories and Story Nook Thursdays), a beginner coding club, a monthly evening storytime and Friday Fun Factory, and Saturday movies.","a":"See children's programs","href":SRC},
}
PLACES={
 "out":[("Hamilton Park","A big city park with a splash pad, playgrounds and a pond (110 Hamilton Park Rd).","Un gran parque de la ciudad con zona de chorros de agua, áreas de juegos y un estanque (110 Hamilton Park Rd)."),
        ("Fulton Park","A large city park on the east side with a splash pad and room to run.","Un gran parque de la ciudad en el lado este con zona de chorros de agua y espacio para correr."),
        ("Waterbury Green","The downtown green, home to the city's holiday tree lighting.","El parque del centro, donde se enciende el árbol navideño de la ciudad.")],
 "rain":[("Silas Bronson Library","The downtown library's KidZone and Picture Book Room host storytimes three mornings a week.","El KidZone y la sala de libros ilustrados de la biblioteca del centro ofrecen cuentacuentos tres mañanas a la semana."),
         ("Mattatuck Museum","Connecticut art and Waterbury history, with kids' programs and school-holiday camps. Open Tuesday–Sunday; free on the second Saturday of the month.","Arte de Connecticut e historia de Waterbury, con programas infantiles y campamentos en días sin clases. Abre de martes a domingo; gratis el segundo sábado de cada mes."),
         ("Palace Theater","Waterbury's restored 1922 theater, with a Broadway series and family shows. Use its 'Family-Friendly' filter to find kids' shows.","El teatro restaurado de 1922 de Waterbury, con una serie de Broadway y espectáculos familiares. Usa su filtro 'Family-Friendly' para encontrar funciones infantiles.")],
 "drive":[("Lake Compounce","New England's oldest amusement park, in Bristol, with fall weekends and a holiday lights season.","El parque de diversiones más antiguo de Nueva Inglaterra, en Bristol, con fines de semana de otoño y temporada de luces navideñas."),
          ("Quassy Amusement Park","A small, kid-friendly amusement park and waterpark on Lake Quassapaug in Middlebury (summer season).","Un pequeño parque de diversiones y acuático para niños junto al lago Quassapaug en Middlebury (temporada de verano)."),
          ("White Memorial Conservation Center","Nature trails, boardwalks and a nature museum in Litchfield.","Senderos naturales, pasarelas y un museo de naturaleza en Litchfield.")],
}
ES={
 "Ages 6 and under + caregiver":"Hasta 6 años + un adulto",
 "Stories, songs and rhymes in the Picture Book Room, every Tuesday morning.":"Cuentos, canciones y rimas en la sala de libros ilustrados, todos los martes por la mañana.",
 "Young children + caregiver":"Niños pequeños + un adulto",
 "A weekly Wednesday-morning storytime in the Picture Book Room.":"Un cuentacuentos semanal los miércoles por la mañana en la sala de libros ilustrados.",
 "A weekly Thursday-morning storytime in the Children's Room.":"Un cuentacuentos semanal los jueves por la mañana en la sala infantil.",
 "Ages 7–12 (beginners)":"7–12 años (principiantes)",
 "Beginner coding for kids in the library's Computer Classroom, Tuesday afternoons.":"Programación para principiantes en el aula de computadoras de la biblioteca, los martes por la tarde.",
 "Ages 4–11":"4–11 años",
 "A Saturday-morning program for kids in the Children's Room. See the library's page for details.":"Un programa para niños el sábado por la mañana en la sala infantil. Consulta la página de la biblioteca para más detalles.",
 "Ages 3–10":"3–10 años",
 "An evening storytime in the Picture Book Room, once a month.":"Un cuentacuentos por la tarde en la sala de libros ilustrados, una vez al mes.",
 "Ages 2 and up":"Desde 2 años",
 "An all-day seek-and-find in the KidZone: track down Silas the Cat hiding somewhere in the library. Come any time the library is open.":"Un juego de búsqueda todo el día en el KidZone: encuentra al gato Silas escondido en algún lugar de la biblioteca. Ven en cualquier momento mientras la biblioteca esté abierta.",
 "Ages 3–12":"3–12 años",
 "A Friday-afternoon activity hour in the Children's Room, once a month.":"Una hora de actividades el viernes por la tarde en la sala infantil, una vez al mes.",
 "Kids of all ages":"Niños de todas las edades",
 "A Halloween-day celebration of witches and wizards with the library's Mardi Gross festivities. Costumes welcome; check the library's page for the lineup.":"Una celebración de brujas y magos el día de Halloween con las festividades Mardi Gross de la biblioteca. Se pueden traer disfraces; consulta el programa en la página de la biblioteca.",
 "Kids":"Niños",
 "A Legend of Sleepy Hollow story and a craft in the Children's Room.":"Un cuento de la leyenda de Sleepy Hollow y una manualidad en la sala infantil.",
 "All ages and skill levels":"Todas las edades y niveles",
 "Free Saturday chess lessons at the museum for every age and skill level. Registration required.":"Clases de ajedrez gratis los sábados en el museo para todas las edades y niveles. Inscripción obligatoria.",
 "All ages":"Todas las edades",
 "Free admission to the museum's galleries of Connecticut art and history, on the second Saturday of the month.":"Entrada gratis a las galerías de arte e historia de Connecticut del museo, el segundo sábado de cada mes.",
 "School-age kids":"Niños en edad escolar",
 "$50 ($35 members)":"$50 ($35 para miembros)",
 "A full day of art-making at the museum on the Columbus Day school holiday, with early drop-off from 8 and late pick-up until 5. Registration required.":"Un día completo de arte en el museo el día sin clases de Columbus Day, con entrada temprana desde las 8 y recogida tarde hasta las 5. Inscripción obligatoria.",
 "Waterbury lights its tree on the Green each year after Thanksgiving, with choirs including the Waterbury PAL Choir, crafts, photos and hot cocoa. Last year it was the Saturday after Thanksgiving. This year's date isn't posted yet.":"Waterbury enciende su árbol en el Green cada año después de Acción de Gracias, con coros como el Waterbury PAL Choir, manualidades, fotos y chocolate caliente. El año pasado fue el sábado después de Acción de Gracias. La fecha de este año aún no se ha publicado.",
 "Waterbury Green, downtown":"Waterbury Green, en el centro",
 "Storytimes three mornings a week (Toddlers, Tales and Tunes on Tuesdays, Wonderful Wednesday Stories and Story Nook Thursdays), a beginner coding club, a monthly evening storytime and Friday Fun Factory, and Saturday movies.":"Cuentacuentos tres mañanas a la semana (Toddlers, Tales and Tunes los martes, Wonderful Wednesday Stories y Story Nook Thursdays), un club de programación para principiantes, un cuentacuentos mensual por la tarde, el Friday Fun Factory y películas los sábados.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7) ----
RS="riverside-cemetery"; MC="https://www.mattmuseum.org/calendar/list/"
TOWN["venues"][RS]=["Riverside Cemetery","496 Riverside St"]; TOWN["venueMeta"][RS]=[None,0]
TOWN["events"]+=[
 {"t":"Family Fun Day: Halloween Spooktacular","v":"matt","special":"hw","when":[W("2026-10-31",[["13:00","17:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":MC,
  "blurb":"A free Halloween family afternoon at the Mattatuck Museum. Costumes welcome."},
 {"t":"School's Out Day Camps at the Mattatuck","v":"matt","when":D(["2026-11-03","2026-11-11"],[["08:00","17:00"]]),"ages":"School-age kids","a":["big"],"free":False,"price":"$50 ($35 members)","rsvp":True,"src":MC,
  "blurb":"Full-day art camps on school holidays: photography and scrapbooking (Election Day, Nov 3) and Fractured Fairytales (Veterans Day, Nov 11). Drop-off from 8, pick-up by 5. Registration required."},
 {"t":"Kids' Art Workshop: The World I Painted","v":"matt","when":[W("2026-11-07",[["12:00","13:00"]])],"ages":"Kids","a":["big"],"free":False,"price":"See museum","rsvp":True,"check":True,"src":MC,
  "blurb":"A hands-on painting workshop for kids at the Mattatuck Museum. Check the museum's calendar for ages and price."},
 {"t":"Spirits Alive at Riverside","v":RS,"special":"fall","when":[W("2026-10-17",[["13:00","15:30"]])],"ages":"Older kids and up","a":["big"],"free":False,"price":"$20","rsvp":True,"check":True,"src":"https://ctvisit.com/events/spirits-alive-riverside",
  "blurb":"Costumed 'spirits' tell the stories of Waterbury people buried at historic Riverside Cemetery. Walking tours leave every 20 minutes from 1 to 2:40, with an all-access tour at 3:15."},
]
TOWN["tba"]+=[{"g":"hw","t":"YMCA Trunk-or-Treat at Riverside Cemetery","w":"Riverside Cemetery, 496 Riverside St",
  "p":"The Waterbury YMCA's free trunk-or-treat and festival, with haunted trails and decorated cars, usually on a mid-to-late-October Saturday afternoon. This year's date isn't posted yet.","src":"https://mommypoppins.com/connecticut-kids/event/events/waterbury-ymca-trunk-or-treat-and-festival"}]
TOWN["classes"]+=[
 {"id":"dynamite-gym","c":"move","n":"Dynamite Academy of Gymnastics","u":"https://mommypoppins.com/connecticut-kids/directory/classes/dynamite-academy-of-gymnastics",
  "blurb":"Gymnastics classes including caregiver-and-toddler classes and therapeutic gymnastics for kids with autism and other developmental differences.","ages":"Toddlers–young adults","where":"130 Scott Rd, Building 4"},
 {"id":"waterbury-ymca","c":"swim","n":"YMCA of Waterbury","u":"https://mommypoppins.com/connecticut-kids/indoor-activities/indoor-swimming-pools-in-new-haven-county",
  "blurb":"Indoor pool with swim lessons and open swim downtown; kids under 8 swim with an adult in the water. Check current schedules with the Y.","ages":"All ages","where":"136 W Main St"},
]
PLACES["rain"]+=[("Waterbury recreation centers","The city's rec centers (River-Baldwin, Chase Park House, North End and William Tracy Park House) run after-school programs; call 203-574-8292.","Los centros recreativos de la ciudad (River-Baldwin, Chase Park House, North End y William Tracy Park House) ofrecen programas después de clases; llama al 203-574-8292.")]
ES.update({
 "A free Halloween family afternoon at the Mattatuck Museum. Costumes welcome.":"Una tarde familiar gratis de Halloween en el Mattatuck Museum. Se pueden traer disfraces.",
 "Full-day art camps on school holidays: photography and scrapbooking (Election Day, Nov 3) and Fractured Fairytales (Veterans Day, Nov 11). Drop-off from 8, pick-up by 5. Registration required.":"Campamentos de arte de día completo en días sin clases: fotografía y scrapbooking (día de elecciones, 3 de nov.) y Fractured Fairytales (Día de los Veteranos, 11 de nov.). Entrada desde las 8 y recogida antes de las 5. Inscripción obligatoria.",
 "See museum":"Consulta con el museo",
 "A hands-on painting workshop for kids at the Mattatuck Museum. Check the museum's calendar for ages and price.":"Un taller práctico de pintura para niños en el Mattatuck Museum. Consulta el calendario del museo para edades y precio.",
 "Older kids and up":"Niños mayores en adelante",
 "$20":"$20",
 "Costumed 'spirits' tell the stories of Waterbury people buried at historic Riverside Cemetery. Walking tours leave every 20 minutes from 1 to 2:40, with an all-access tour at 3:15.":"'Espíritus' disfrazados cuentan las historias de habitantes de Waterbury enterrados en el histórico Riverside Cemetery. Los recorridos a pie salen cada 20 minutos de 1 a 2:40, con un recorrido accesible a las 3:15.",
 "The Waterbury YMCA's free trunk-or-treat and festival, with haunted trails and decorated cars, usually on a mid-to-late-October Saturday afternoon. This year's date isn't posted yet.":"El trunk-or-treat y festival gratis del YMCA de Waterbury, con senderos embrujados y autos decorados, normalmente un sábado por la tarde de mediados o finales de octubre. La fecha de este año aún no se ha publicado.",
 "Riverside Cemetery, 496 Riverside St":"Riverside Cemetery, 496 Riverside St",
 "Gymnastics classes including caregiver-and-toddler classes and therapeutic gymnastics for kids with autism and other developmental differences.":"Clases de gimnasia, incluidas clases de niño pequeño con su cuidador y gimnasia terapéutica para niños con autismo y otras diferencias en el desarrollo.",
 "Toddlers–young adults":"Niños pequeños–jóvenes adultos",
 "Indoor pool with swim lessons and open swim downtown; kids under 8 swim with an adult in the water. Check current schedules with the Y.":"Alberca techada con clases de natación y nado libre en el centro; los menores de 8 años nadan con un adulto en el agua. Consulta los horarios actuales con el Y.",
})

# ---- creative places / bookstores / blogs pass (Oct 8) ----
PLACES["rain"]+=[
 ("Roller Magic","Waterbury's roller rink, with family skate sessions most Wednesday, Friday, Saturday and Sunday, themed skate nights and an arcade (60 Harvester Rd). Admission about $8.50–13 plus $5 skate rental; check the rink's schedule.","La pista de patinaje sobre ruedas de Waterbury, con sesiones familiares casi todos los miércoles, viernes, sábados y domingos, noches temáticas y sala de juegos (60 Harvester Rd). Entrada de unos $8.50–13 más $5 por el alquiler de patines; consulta el horario de la pista."),
 ("Urban Air Adventure Park","An indoor trampoline and adventure park, open afternoons on weekdays and all day on weekends (425 Bank St). Passes about $16–40.","Un parque techado de trampolines y aventura, abierto por las tardes entre semana y todo el día los fines de semana (425 Bank St). Pases de unos $16–40."),
 ("Laser Planet","Laser tag plus a Little Dipper play space for kids up to about 5, open Thursday–Sunday (2457 East Main St); call ahead.","Láser tag y el área de juegos Little Dipper para niños de hasta unos 5 años, abierto de jueves a domingo (2457 East Main St); llama antes."),
 ("Lakewood Lanes","Bowling, including glow-in-the-dark Galaxy bowling (694 Lakewood Rd).","Boliche, incluido el boliche Galaxy que brilla en la oscuridad (694 Lakewood Rd)."),
 ("Fascia's Chocolates","A local chocolate factory with tours and kids' Young Chocolatier parties (44 Chase River Rd).","Una fábrica de chocolate local con recorridos y fiestas Young Chocolatier para niños (44 Chase River Rd)."),
 ("Richie's Comic Cabana","A comic shop with comics and Pokémon and Magic cards (96 Store Ave). Open Tuesday–Sunday; call ahead.","Una tienda de cómics con cómics y cartas de Pokémon y Magic (96 Store Ave). Abre de martes a domingo; llama antes."),
]
TOWN["classes"]+=[
 {"id":"snapology-waterbury","c":"build","n":"Snapology of Waterbury","u":"https://www.snapology.com/connecticut-waterbury/?p=31",
  "blurb":"LEGO-based robotics, coding and STEAM workshops and school-break camps. One-day workshops from $49; check the schedule for new dates.","ages":"4–14 years","where":"425 Bank St"},
 {"id":"seven-angels-classes","c":"art","n":"Seven Angels Theatre classes","u":"https://mommypoppins.com/connecticut-kids/indoor-activities/25-things-to-do-in-waterbury-the-brass-city",
  "blurb":"Theater classes and workshops for young performers at Waterbury's professional theater, plus a summer theater camp.","ages":"7–18 years","where":"1 Plank Rd"},
]
ES.update({
 "LEGO-based robotics, coding and STEAM workshops and school-break camps. One-day workshops from $49; check the schedule for new dates.":"Talleres de robótica, programación y STEAM con LEGO y campamentos en vacaciones escolares. Talleres de un día desde $49; consulta el calendario para nuevas fechas.",
 "4–14 years":"4–14 años",
 "Theater classes and workshops for young performers at Waterbury's professional theater, plus a summer theater camp.":"Clases y talleres de teatro para jóvenes artistas en el teatro profesional de Waterbury, además de un campamento de teatro en verano.",
 "7–18 years":"7–18 años",
})
