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
ES={
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
