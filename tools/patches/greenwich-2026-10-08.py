# Full playbook re-run, Oct 8 2026
seen=False; ev=[]
for e in TOWN["events"]:
    if e["t"]=="Fall Harvest Festival":
        if seen: continue
        seen=True
    if e["t"]=="Time Travelers Family Sunday": e["s"][0][3]="2026-12-31"; e["s"][0][4] if len(e["s"][0])>4 else None
    if e["t"]=="Halloween Happenings": e["price"]="$12 per person (ages 3+)"
    if e["t"]=="Days of Play!": e["blurb"]="Outdoor drop-off mornings while schools are closed: scavenger hunts, animal tracking and a plant-themed 'election' on Nov 3. Register ahead."
    ev.append(e)
TOWN["events"]=ev
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"] not in ("Santa's Holiday Village","Holiday Happenings & Movie Night")]
TOWN["classes"]=[c for c in TOWN["classes"] if c["id"]!="bruce-outdoor-arts-festival"]
GBC="greenwich-botanical-center"
TOWN["events"]+=[
 {"t":"Bruce Museum Outdoor Arts Festival","v":"bruce-museum","when":D(["2026-10-10","2026-10-11"],[["10:00","17:00"]]),"ages":"All ages","a":["preschool","big"],"free":False,"price":"$15 (festival and museum); under 5 free","drop":True,"src":"https://brucemuseum.org/events/45th-annual-outdoor-arts-festival/",
  "blurb":"The 45th annual festival with 82 artists, food and a children's drawing contest."},
 {"t":"Museum Movers","v":"bruce-museum","when":[W("2026-10-10",[["11:00","12:00"]])],"ages":"Ages 3–6 + grown-up","a":["preschool"],"free":False,"price":"Included with admission","rsvp":True,"check":True,"src":"https://brucemuseum.org/events/museum-movers-oct-2026/",
  "blurb":"A sensory gallery walk followed by kids' yoga; bring a mat and reserve ahead."},
 {"t":"Halloween Public Skate","v":"dorothy-hamill-rink","special":"hw","when":[W("2026-10-31",[["18:30","20:30"]])],"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free skating; free rental in costume","rsvp":True,"check":True,"src":"https://www.greenwichct.gov/DocumentCenter/View/58759/Halloween-Public-Skate-2026",
  "blurb":"Skate in costume with Halloween music and free candy. Get tickets by QR code or online; skate rental is free if you're in costume."},
 {"t":"Greenwich Alliance Turkey Trot","v":"roger-sherman-baldwin-park","when":[W("2026-11-28",[["09:00","11:00"]])],"ages":"Mini-Trot ages 3–5; 1 mile for kids 6+","a":["preschool","big"],"free":False,"price":"$20 kids, $40 adults","rsvp":True,"src":"https://runscore.runsignup.com/Race/CT/Greenwich/GreenwichAllianceTurkeyTrot",
  "blurb":"A Thanksgiving-weekend Mini-Trot for ages 3–5 (9:00), a 1-mile run (9:30) and a 5K (10:00), benefiting the Greenwich Alliance for Education."},
 {"t":"Santa's Holiday Village","v":"cohen-eastern-civic","special":"hol","when":[W("2026-12-05",[["10:00","12:30"]])],"ages":"All ages (under 1 free)","a":B+["big"],"free":False,"price":"$20 per person ages 2+","rsvp":True,"src":"https://www.greenwichct.gov/2325/Santas-Holiday-Village",
  "blurb":"Parks & Rec's holiday morning with Santa. Tickets go on sale Oct 15 (limit 8 per family) and must be bought ahead."},
 {"t":"The Christmas Owl: Book Signing & Owl Meet-and-Greet","v":GBC,"special":"hol","when":[W("2026-12-06",[["12:00","13:30"]])],"ages":"Families","a":["preschool","big"],"free":False,"price":"$15 non-members; members free","rsvp":True,"src":"https://greenwichbotanicalcenter.org/upcoming_events/the-christmas-owl-book-signing-and-native-owl-meet-greet/",
  "blurb":"Meet live native owls from Ravensbeard Wildlife Center, then hear the author of The Christmas Owl read her picture book about the Rockefeller Center tree owl."},
 {"t":"Holiday Happenings & Movie Night","v":"bendheim-western-civic","special":"hol","when":[W("2026-12-19",[["17:00","19:30"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"$12 per person","rsvp":True,"src":"https://www.greenwichct.gov/2327/Holiday-Happenings-Movie-Night",
  "blurb":"A holiday evening with activities and a movie; tickets go on sale Nov 15 and must be bought ahead."},
]
TOWN["tba"]+=[
 {"g":"hw","t":"Halloween Greet & Treat on Greenwich Ave","w":"Greenwich Ave and side streets","p":"Trick-or-treating at 75+ shops, kids' zones with police and fire trucks and a bubble show, usually the Saturday before Halloween, late morning to early afternoon. This year's date isn't posted yet.","src":"https://greenwichfreepress.com/news/business/greenwich-moms-halloween-greet-treat-returns-to-greenwich-ave-on-oct-26-223109/"},
 {"g":"hol","t":"Chabad Greenwich Chanukah Car Parade & Menorah Lighting","w":"Around Greenwich","p":"Chabad Lubavitch of Greenwich lists a Grand Menorah Car Parade and a concert with a menorah lighting for Chanukah (Dec 4–12), but no dates or places yet.","src":"https://www.chabadgreenwich.org/6712206"},
]
ES={
 "Outdoor drop-off mornings while schools are closed: scavenger hunts, animal tracking and a plant-themed 'election' on Nov 3. Register ahead.":"Mañanas al aire libre sin papás en días sin escuela: búsquedas del tesoro, rastreo de animales y una 'elección' de plantas el 3 de nov. Inscríbete con anticipación.",
 "$12 per person (ages 3+)":"$12 por persona (3 años o más)",
 "$15 (festival and museum); under 5 free":"$15 (festival y museo); menores de 5 gratis",
 "The 45th annual festival with 82 artists, food and a children's drawing contest.":"El 45.º festival anual con 82 artistas, comida y un concurso de dibujo infantil.",
 "Ages 3–6 + grown-up":"3–6 años + un adulto","Included with admission":"Incluido con la entrada",
 "A sensory gallery walk followed by kids' yoga; bring a mat and reserve ahead.":"Un recorrido sensorial por la galería seguido de yoga infantil; trae tapete y reserva con anticipación.",
 "Free skating; free rental in costume":"Patinaje gratis; alquiler gratis si vas disfrazado",
 "Skate in costume with Halloween music and free candy. Get tickets by QR code or online; skate rental is free if you're in costume.":"Patina disfrazado con música de Halloween y dulces gratis. Consigue boletos por código QR o en línea; el alquiler de patines es gratis si vas disfrazado.",
 "Mini-Trot ages 3–5; 1 mile for kids 6+":"Mini-Trot 3–5 años; 1 milla para niños de 6 o más",
 "$20 kids, $40 adults":"$20 niños, $40 adultos",
 "A Thanksgiving-weekend Mini-Trot for ages 3–5 (9:00), a 1-mile run (9:30) and a 5K (10:00), benefiting the Greenwich Alliance for Education.":"Un Mini-Trot para 3–5 años (9:00), una carrera de 1 milla (9:30) y unos 5 km (10:00) el fin de semana de Acción de Gracias, a beneficio de la Greenwich Alliance for Education.",
 "All ages (under 1 free)":"Todas las edades (menores de 1 gratis)",
 "$20 per person ages 2+":"$20 por persona de 2 años o más",
 "Parks & Rec's holiday morning with Santa. Tickets go on sale Oct 15 (limit 8 per family) and must be bought ahead.":"La mañana navideña con Santa de Parks & Rec. Los boletos salen a la venta el 15 de oct. (máximo 8 por familia) y se compran con anticipación.",
 "Families":"Familias","$15 non-members; members free":"$15 no miembros; miembros gratis",
 "Meet live native owls from Ravensbeard Wildlife Center, then hear the author of The Christmas Owl read her picture book about the Rockefeller Center tree owl.":"Conoce búhos nativos vivos de Ravensbeard Wildlife Center y escucha a la autora de The Christmas Owl leer su libro sobre la lechuza del árbol del Rockefeller Center.",
 "$12 per person":"$12 por persona",
 "A holiday evening with activities and a movie; tickets go on sale Nov 15 and must be bought ahead.":"Una tarde navideña con actividades y una película; los boletos salen a la venta el 15 de nov. y se compran con anticipación.",
 "Greenwich Ave and side streets":"Greenwich Ave y calles laterales",
 "Trick-or-treating at 75+ shops, kids' zones with police and fire trucks and a bubble show, usually the Saturday before Halloween, late morning to early afternoon. This year's date isn't posted yet.":"Dulces en más de 75 tiendas, zonas infantiles con patrullas y camiones de bomberos y un show de burbujas, por lo general el sábado antes de Halloween, de media mañana a primera hora de la tarde. La fecha de este año aún no se ha publicado.",
 "Around Greenwich":"Por todo Greenwich",
 "Chabad Lubavitch of Greenwich lists a Grand Menorah Car Parade and a concert with a menorah lighting for Chanukah (Dec 4–12), but no dates or places yet.":"Chabad Lubavitch of Greenwich anuncia un gran desfile de autos con menorás y un concierto con encendido de la menorá para Janucá (del 4 al 12 de dic.), pero aún sin fechas ni lugares.",
}
