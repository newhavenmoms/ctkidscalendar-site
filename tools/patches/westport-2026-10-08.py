# Full playbook re-run, Oct 8 2026
EP="earthplace"; MOCA="moca-ct"; Y="westport-ymca"; EPS="https://earthplace.org/event/"; MOS="https://patch.com/connecticut/westport/calendar/event/"
for e in TOWN["events"]:
    if e["t"] in ("Story & Animal Program","Animal Hall Feeding"):
        for r in e["s"]: r[3]="2026-12-31"
    if e["t"]=="Saturday Craft":
        e["t"]="Draw an Animal Friend"; e["s"][0][3]="2026-12-26"; e["src"]=EPS+"draw-an-animal-friend-2/2026-10-10/"
TOWN["classes"]=[c for c in TOWN["classes"] if c["id"] not in ("playhouse-click-clack-moo","playhouse-pinkalicious","playhouse-mutts-gone-nuts","ep-kids-night-out","ep-campfire-fall")]
def ep(t,ws,ages,a,price,blurb,special=None,slug=""):
    e={"t":t,"v":EP,"when":ws,"ages":ages,"a":a,"free":False,"price":price,"rsvp":True,"src":EPS+slug,"blurb":blurb}
    if special: e["special"]=special
    return e
TOWN["events"]+=[
 {"t":"Family Fun Day at MoCA CT","v":MOCA,"when":D(["2026-10-10","2026-11-14","2026-12-12"],[["10:00","12:00"]]),"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","rsvp":True,"check":True,"src":MOS+"20261010/6ff35c1d-d140-49ac-bde3-2735f65bc6bf/family-fun-day-at-moca-ct-october-10",
  "blurb":"Families tour the galleries, make art with museum educators and meet special guests. End time is an estimate; register ahead."},
 ep("Tree ID Walk: Bark, Leaves and Seeds",[W("2026-10-10",[["14:30","15:30"]])],"Ages 3+",["preschool","big"],"$5–8","A family walk learning to identify trees by their bark, leaves and seeds.",slug="tree-id-walk-2026/"),
 {"t":"School Recess Art Camp at MoCA","v":MOCA,"when":D(["2026-10-12","2026-11-03"],[["09:00","12:00"]]),"ages":"Ages 5–10","a":["big"],"free":False,"price":"$75","rsvp":True,"src":MOS+"20261012/06ca8843-fcff-46ec-a100-9a206c26309b/indigenous-peoples-day-columbus-day-school-recess",
  "blurb":"A no-school morning of hands-on art and gallery time (Oct 12 is inspired by Indigenous artistic traditions). Kids must use the bathroom on their own."},
 ep("Kids' Night Out at Earthplace",D(["2026-10-16","2026-11-20","2026-12-11"],[["18:00","21:00"]]),"Ages 4–13 (toilet-trained)",["preschool","big"],"$50 members, $60 non-members","A drop-off night with pizza and live animals: Creepy Critters (Oct 16), Dinosaurs of Today (Nov 20) and Hibernation Station (Dec 11).",slug="kids-night-out-creepy-critters/"),
 {"t":"Family Halloween Spooktacular at the Y","v":Y,"special":"hw","when":[W("2026-10-24",[["15:00","18:00"]])],"ages":"Up to age 12 (under 2 free)","a":B+["big"],"free":False,"price":"$15–20 per child; adults free","rsvp":True,"src":"https://westporty.org/spook/",
  "blurb":"Pumpkin decorating, bounce houses, the rock wall, carnival games, food trucks and a costume parade around the Y grounds. Kids register online."},
 ep("Pumpkin Painting & Carving",D(["2026-10-24","2026-10-25"],[["13:00","15:00"]]),"Families",["preschool","big"],"$30 per table (2 adults + 3 kids, 1 pumpkin)","Paint or carve a pumpkin outdoors with supplies and clean-up provided; extra pumpkins $5.",special="hw",slug="pumpkin-painting-and-carving/2026-10-24/"),
 ep("Full Moon & Bat Hike",[W("2026-10-26",[["18:00","19:00"]])],"Ages 4+",["preschool","big"],"$15–20","An evening hike under the full moon looking for bats.",special="hw",slug="full-moon-bat-hike/"),
 ep("Campfire: Happy OWL-ween",[W("2026-10-30",[["18:30","20:00"]])],"Families",["preschool","big"],"$25–35","Meet nocturnal animals, hear a spooky story and make s'mores; costumes welcome.",special="hw",slug="campfire-happy-owl-ween/"),
 ep("Cozy Campfire",[W("2026-11-14",[["14:00","15:30"]])],"Families",["preschool","big"],"$25–35","Dress warmly and bring a stuffed animal: meet animals up close and make s'mores.",slug="cozy-campfire/"),
 ep("Campfire: Winter Solstice",[W("2026-12-20",[["13:00","14:30"]])],"Families",["preschool","big"],"$25–35","A small craft project, a campfire and a treat for the shortest days of the year.",special="hol",slug="winter-solstice-campfire/"),
 {"t":"Westport PAL Rink public skating","v":"longshore-club-park","special":"hol","when":[{"from":"2026-11-27","to":"2026-12-31","t":[]}],"ages":"All ages","a":["preschool","big"],"free":False,"price":"$6.25 kids 12 and under, $10 adults; rentals $5","drop":True,"check":True,"src":"https://westportct.gov/government/departments-a-z/parks-and-recreation/westport-pal-rink-at-longshore",
  "blurb":"The outdoor rink at Longshore is projected to open Nov 27, weather permitting; daily public skate once it's open."},
]
TOWN["tba"]+=[
 {"g":"hw","t":"Children's Halloween Parade","w":"Main St to Veterans Green and Town Hall, 110 Myrtle Ave","p":"Parks & Rec's weekday-afternoon costume parade with trick-or-treating along Main St and entertainment at Town Hall, best for ages 8 and under. Last year it was Wed Oct 29, meeting at 3:30. This year's date isn't posted yet.","src":"https://www.westportct.gov/Home/Components/News/News/10373/35"},
 {"g":"hol","t":"Wakeman Town Farm Tree Lighting","w":"Wakeman Town Farm, 134 Cross Hwy","p":"A free farm tree lighting with a bonfire, sweets, cocoa and kid musicians, collecting toys and canned goods; the first Friday of December (last year Dec 5, 4–6:30). This year's date isn't posted yet.","src":"https://westportjournal.com/community/westport-ct-tree-lighting-2025/"},
 {"g":"hol","t":"Town Hall Tree Lighting","w":"Westport Town Hall, 110 Myrtle Ave","p":"The Staples Orphenians sing and the Westport Museum serves hot chocolate at the town tree lighting in early December (last year Dec 1 at 5). This year's date isn't posted yet.","src":"https://westportjournal.com/community/westport-ct-tree-lighting-2025/"},
 {"g":"hol","t":"Westport Museum Winter Market","w":"Westport Museum, 25 Avery Pl","p":"Santa photos, a gingerbread village of local buildings, silhouette cutting, a fire and hot chocolate on an early-December Saturday; free (suggested $5). This year's date isn't posted yet.","src":"https://westporthistory.org/event/winter-market-2/"},
 {"g":"hol","t":"The Nutcracker (Westport's Academy of Dance)","w":"Staples High School, 70 North Ave","p":"The 45th annual local Nutcracker, usually the weekend before Christmas (last year Dec 20–21); it often sells out. This year's dates aren't posted yet.","src":"https://patch.com/connecticut/wilton-center-ct/calendar/event/20251220/e1e74916-717d-4539-be9b-1eb4bee4ca7c/westports-academy-of-dance-the-nutcracker"},
 {"g":"hol","t":"Community Menorah Lighting","w":"Compo Acres Shopping Center, 400 Post Rd E","p":"A Hanukkah evening lighting with music, cookies, gelt and dreidels, open to all. Hanukkah is Dec 4–12 this year; the date isn't posted yet.","src":"https://westportjournal.com/community/community-menorah-lighting-ceremonies-herald-hanukkah/"},
]
ES={
 "Families tour the galleries, make art with museum educators and meet special guests. End time is an estimate; register ahead.":"Las familias recorren las galerías, hacen arte con los educadores del museo y conocen invitados especiales. La hora de término es aproximada; inscríbete con anticipación.",
 "Ages 3+":"3 años o más","$5–8":"$5–8",
 "A family walk learning to identify trees by their bark, leaves and seeds.":"Una caminata familiar para aprender a identificar árboles por su corteza, hojas y semillas.",
 "Ages 5–10":"5–10 años","$75":"$75",
 "A no-school morning of hands-on art and gallery time (Oct 12 is inspired by Indigenous artistic traditions). Kids must use the bathroom on their own.":"Una mañana sin escuela de arte práctico y visita a las galerías (el 12 de oct. se inspira en tradiciones artísticas indígenas). Los niños deben ir al baño solos.",
 "Ages 4–13 (toilet-trained)":"4–13 años (sin pañal)",
 "$50 members, $60 non-members":"$50 miembros, $60 no miembros",
 "A drop-off night with pizza and live animals: Creepy Critters (Oct 16), Dinosaurs of Today (Nov 20) and Hibernation Station (Dec 11).":"Una noche sin papás con pizza y animales vivos: Creepy Critters (16 de oct.), Dinosaurs of Today (20 de nov.) y Hibernation Station (11 de dic.).",
 "Up to age 12 (under 2 free)":"Hasta 12 años (menores de 2 gratis)",
 "$15–20 per child; adults free":"$15–20 por niño; adultos gratis",
 "Pumpkin decorating, bounce houses, the rock wall, carnival games, food trucks and a costume parade around the Y grounds. Kids register online.":"Decoración de calabazas, brincolines, el muro de escalada, juegos de feria, camiones de comida y un desfile de disfraces por el YMCA. Los niños se inscriben en línea.",
 "Families":"Familias",
 "$30 per table (2 adults + 3 kids, 1 pumpkin)":"$30 por mesa (2 adultos + 3 niños, 1 calabaza)",
 "Paint or carve a pumpkin outdoors with supplies and clean-up provided; extra pumpkins $5.":"Pinta o talla una calabaza al aire libre con materiales y limpieza incluidos; calabazas extra $5.",
 "Ages 4+":"4 años o más","$15–20":"$15–20",
 "An evening hike under the full moon looking for bats.":"Una caminata nocturna bajo la luna llena en busca de murciélagos.",
 "$25–35":"$25–35",
 "Meet nocturnal animals, hear a spooky story and make s'mores; costumes welcome.":"Conoce animales nocturnos, escucha un cuento de miedo y haz s'mores; se aceptan disfraces.",
 "Dress warmly and bring a stuffed animal: meet animals up close and make s'mores.":"Abrígate y trae un peluche: conoce animales de cerca y haz s'mores.",
 "A small craft project, a campfire and a treat for the shortest days of the year.":"Una pequeña manualidad, una fogata y una golosina para los días más cortos del año.",
 "$6.25 kids 12 and under, $10 adults; rentals $5":"$6.25 niños de 12 años o menos, $10 adultos; alquiler $5",
 "The outdoor rink at Longshore is projected to open Nov 27, weather permitting; daily public skate once it's open.":"Se espera que la pista al aire libre de Longshore abra el 27 de nov., si el clima lo permite; patinaje público diario una vez abierta.",
 "Main St to Veterans Green and Town Hall, 110 Myrtle Ave":"De Main St a Veterans Green y el Ayuntamiento, 110 Myrtle Ave",
 "Parks & Rec's weekday-afternoon costume parade with trick-or-treating along Main St and entertainment at Town Hall, best for ages 8 and under. Last year it was Wed Oct 29, meeting at 3:30. This year's date isn't posted yet.":"El desfile de disfraces de Parks & Rec una tarde entre semana, con dulces por Main St y entretenimiento en el Ayuntamiento, ideal para menores de 8. El año pasado fue el miércoles 29 de oct., reunión a las 3:30. La fecha de este año aún no se ha publicado.",
 "Wakeman Town Farm, 134 Cross Hwy":"Wakeman Town Farm, 134 Cross Hwy",
 "A free farm tree lighting with a bonfire, sweets, cocoa and kid musicians, collecting toys and canned goods; the first Friday of December (last year Dec 5, 4–6:30). This year's date isn't posted yet.":"Un encendido del árbol gratis en la granja con fogata, dulces, chocolate y músicos infantiles, con colecta de juguetes y alimentos enlatados; el primer viernes de diciembre (el año pasado el 5 de dic., de 4 a 6:30). La fecha de este año aún no se ha publicado.",
 "Westport Town Hall, 110 Myrtle Ave":"Ayuntamiento de Westport, 110 Myrtle Ave",
 "The Staples Orphenians sing and the Westport Museum serves hot chocolate at the town tree lighting in early December (last year Dec 1 at 5). This year's date isn't posted yet.":"Los Staples Orphenians cantan y el Westport Museum sirve chocolate caliente en el encendido del árbol del pueblo a principios de diciembre (el año pasado el 1 de dic. a las 5). La fecha de este año aún no se ha publicado.",
 "Westport Museum, 25 Avery Pl":"Westport Museum, 25 Avery Pl",
 "Santa photos, a gingerbread village of local buildings, silhouette cutting, a fire and hot chocolate on an early-December Saturday; free (suggested $5). This year's date isn't posted yet.":"Fotos con Santa, un pueblo de jengibre con edificios locales, siluetas recortadas, fogata y chocolate caliente un sábado a principios de diciembre; gratis (sugerido $5). La fecha de este año aún no se ha publicado.",
 "Staples High School, 70 North Ave":"Staples High School, 70 North Ave",
 "The 45th annual local Nutcracker, usually the weekend before Christmas (last year Dec 20–21); it often sells out. This year's dates aren't posted yet.":"El 45.º Cascanueces local anual, por lo general el fin de semana antes de Navidad (el año pasado el 20 y 21 de dic.); suele agotarse. Las fechas de este año aún no se han publicado.",
 "Compo Acres Shopping Center, 400 Post Rd E":"Compo Acres Shopping Center, 400 Post Rd E",
 "A Hanukkah evening lighting with music, cookies, gelt and dreidels, open to all. Hanukkah is Dec 4–12 this year; the date isn't posted yet.":"Un encendido de Janucá por la tarde con música, galletas, monedas de chocolate y dreidels, abierto a todos. Janucá es del 4 al 12 de dic. este año; la fecha aún no se ha publicado.",
}
