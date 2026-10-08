# Full playbook re-run, Oct 8 2026
FH="fairfield-hills"; CVH="cvh-sanctuary"; SHV="sandy-hook-village"; NMS="newtown-middle"
TOWN["venues"].update({FH:["Fairfield Hills","Keating Farm Ave"],CVH:["Catherine Violet Hubbard Animal Sanctuary","8 Commerce Rd"],SHV:["Sandy Hook Village center","Church Hill Rd & Glen Rd, Sandy Hook"],NMS:["Newtown Middle School","11 Queen St"]})
TOWN["venueMeta"].update({FH:[None,0],CVH:[None,0],SHV:[None,0],NMS:[None,0]})
ETH="edmond-town-hall"
TOWN["events"]+=[
 {"t":"Race for Catherine: Kids Kindness Dash","v":FH,"when":[W("2026-10-11",[["08:15","08:45"]])],"ages":"Ages 3–9","a":["preschool","big"],"free":False,"price":"$22.20","rsvp":True,"src":"https://runsignup.com/Race/CT/Newtown/RaceforCatherine",
  "blurb":"A 100-yard kids' dash with a medal and free breakfast, plus adoptable pets on site; the 5K follows at 9. Benefits the Catherine Violet Hubbard Animal Sanctuary."},
 {"t":"Harvest Table Workshop: Kids Cooking","v":ETH,"when":D(["2026-10-13","2026-10-20","2026-10-27","2026-11-10"],[["17:00","18:30"]]),"ages":"Ages 7–11 (ages 12+ at 3pm)","a":["big"],"free":False,"price":"See ticket site","rsvp":True,"check":True,"src":"https://edmondtownhall.org/event/harvesttableworkshop/",
  "blurb":"Chef Robyn Herman teaches knife skills and fall recipes; kids take their food home. Limit 12 per class."},
 {"t":"Scarecrow Contest at Fairfield Hills","v":FH,"special":"fall","when":[{"from":"2026-10-08","to":"2026-10-30","t":[]}],"ages":"All ages","a":B+["big"],"free":True,"price":"Free to visit","drop":True,"src":"https://www.newtown-ct.gov/parks-recreation/pages/7th-annual-scarecrow-contest",
  "blurb":"Families' scarecrows line the Fairfield Hills lamp posts all month. Walk the loop and vote Oct 24–29; the winner is named Oct 30."},
 {"t":"Sandy Hook Halloween Walk","v":SHV,"special":"hw","when":[W("2026-10-24",[["11:00","14:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://www.newtownbee.com/calendar/?event_id=55590&lang=en",
  "blurb":"Costumed trick-or-treating through the Sandy Hook Village shops along Church Hill Rd, Washington Ave, Riverside Rd and Glen Rd. Rain or shine."},
 {"t":"Not So Spooky Anymore","v":CVH,"special":"hw","when":[W("2026-10-24",[["15:00","17:00"]])],"ages":"Kids and families","a":["preschool","big"],"free":False,"price":"$5","rsvp":True,"src":"https://www.cvhfoundation.org/events/",
  "blurb":"Meet the 'spooky' animals up close: live owls, ravens, snakes and tarantulas in the sanctuary's Learning Barn."},
 {"t":"Free Movie: Wicked: For Good","v":ETH,"when":[W("2026-11-15",[["13:00","15:30"]])],"ages":"All ages (PG)","a":["big"],"free":True,"price":"Free (ticket required)","rsvp":True,"src":"https://edmondtownhall.org/event/wickedforgood/",
  "blurb":"A free Sunday matinee in the historic Edmond Town Hall theater; reserve a free ticket online."},
 {"t":"Oliver! (Newtown Stage Company)","v":ETH,"special":"shows","when":[W("2026-11-20",[["19:00","21:30"]]),W("2026-11-21",[["13:00","15:30"],["19:00","21:30"]]),W("2026-11-22",[["13:00","15:30"]])],"ages":"All ages","a":["preschool","big"],"free":False,"price":"See ticket site","rsvp":True,"src":"https://onthestage.tickets/show/newtown-stage-company/6a9e389e4e3e5e9fc544b375",
  "blurb":"A youth musical with a cast of local kids in grades 3–12. End times are estimates."},
 {"t":"Newtown Turkey Trot","v":NMS,"when":[W("2026-11-26",[["07:45","09:00"]])],"ages":"All ages (2.5K walk for families)","a":["big"],"free":False,"price":"$35 through Oct 31, then $45","rsvp":True,"src":"https://runsignup.com/Race/CT/Newtown/NewtownTurkeyTrot",
  "blurb":"Thanksgiving-morning 5K run and 2.5K family walk benefiting the Booth Library."},
 {"t":"Free Movie: The Polar Express","v":ETH,"special":"hol","when":[W("2026-12-20",[["13:00","15:00"]])],"ages":"All ages (G)","a":B+["big"],"free":True,"price":"Free (ticket required)","rsvp":True,"src":"https://edmondtownhall.org/event/free-movie-polar-express/",
  "blurb":"A free holiday matinee at Edmond Town Hall; reserve a free ticket online."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Hawleyville Tree Lighting","w":"Hawleyville Volunteer Fire Co., 34 Hawleyville Rd","p":"Santa photos, free pizza, cocoa, cookies and dancers at the firehouse, on a mid-December Sunday. Last year it was Dec 14 at 5:30. This year's date isn't posted yet.","src":"https://www.newtownbee.com/?p=159738"},
 {"g":"hol","t":"Rotary Pancake Breakfast with Santa","w":"Edmond Town Hall, 45 Main St","p":"Pancakes, Santa from 8:30 and dance performances, usually the first Saturday of December, 8–noon ($7 kids 12 and under). This year's date isn't posted yet.","src":"https://www.newtownbee.com/?p=159744"},
 {"g":"hol","t":"Letters to Santa mailbox at The Toy Tree","w":"The Toy Tree, 32 Church Hill Rd","p":"Drop a letter in Santa's mailbox at the toy store with a stamped, self-addressed envelope and Santa writes back. Last year letters were due Dec 15.","src":"https://www.newtownbee.com/?p=159777"},
 {"g":"hol","t":"Noon Year's Eve at EverWonder","w":"EverWonder Children's Museum, 11 Mile Hill Rd","p":"A morning countdown to noon with a balloon drop, included with museum admission. It has run on Dec 31 in past years; this year's details aren't posted yet.","src":"https://monroe.macaronikid.com/events/657b39fe31ce3b06db4d88ed/-noon-years-eve_-everwonder-newtown"},
]
TOWN["classes"]+=[{"id":"newtown-stage-co","c":"art","n":"Newtown Stage Company youth musicals","u":"https://newtownstageco.com/fall-2026","blurb":"A youth musical-theater company that rehearses and stages two full musicals a year at Edmond Town Hall.","ages":"Grades 3–12","where":"Edmond Town Hall, 45 Main St"}]
REPLACE_PLACES["The Toy Tree"]=("The Toy Tree","A toy store in The Village at Lexington Gardens (32 Church Hill Rd), with a letters-to-Santa mailbox in December.","Una juguetería en The Village at Lexington Gardens (32 Church Hill Rd), con un buzón de cartas a Santa en diciembre.")
ADD_PLACES["out"]+=[("Catherine Violet Hubbard Animal Sanctuary","An animal sanctuary with seasonal family programs, storytimes and animal meet-and-greets (8 Commerce Rd); visit during events.","Un santuario de animales con programas familiares de temporada, cuentacuentos y encuentros con animales (8 Commerce Rd); se visita durante los eventos."),
                    ("Heritage Park","A small village park with a pavilion in the heart of Sandy Hook (7 Glen Rd).","Un pequeño parque con pabellón en el corazón de Sandy Hook (7 Glen Rd).")]
ES={
 "Ages 3–9":"3–9 años","$22.20":"$22.20",
 "A 100-yard kids' dash with a medal and free breakfast, plus adoptable pets on site; the 5K follows at 9. Benefits the Catherine Violet Hubbard Animal Sanctuary.":"Una carrera infantil de 100 yardas con medalla y desayuno gratis, además de mascotas en adopción; los 5K siguen a las 9. A beneficio del Catherine Violet Hubbard Animal Sanctuary.",
 "Ages 7–11 (ages 12+ at 3pm)":"7–11 años (12 años o más a las 3 p. m.)",
 "See ticket site":"Ver el sitio de boletos",
 "Chef Robyn Herman teaches knife skills and fall recipes; kids take their food home. Limit 12 per class.":"La chef Robyn Herman enseña a usar el cuchillo y recetas de otoño; los niños se llevan su comida a casa. Máximo 12 por clase.",
 "Free to visit":"Visita gratis",
 "Families' scarecrows line the Fairfield Hills lamp posts all month. Walk the loop and vote Oct 24–29; the winner is named Oct 30.":"Los espantapájaros de las familias adornan los postes de luz de Fairfield Hills todo el mes. Recorre el circuito y vota del 24 al 29 de oct.; el ganador se anuncia el 30 de oct.",
 "Costumed trick-or-treating through the Sandy Hook Village shops along Church Hill Rd, Washington Ave, Riverside Rd and Glen Rd. Rain or shine.":"A pedir dulces disfrazados por las tiendas de Sandy Hook Village en Church Hill Rd, Washington Ave, Riverside Rd y Glen Rd. Con lluvia o sol.",
 "Kids and families":"Niños y familias","$5":"$5",
 "Meet the 'spooky' animals up close: live owls, ravens, snakes and tarantulas in the sanctuary's Learning Barn.":"Conoce de cerca a los animales 'espeluznantes': búhos, cuervos, serpientes y tarántulas vivos en el Learning Barn del santuario.",
 "All ages (PG)":"Todas las edades (PG)",
 "Free (ticket required)":"Gratis (se requiere boleto)",
 "A free Sunday matinee in the historic Edmond Town Hall theater; reserve a free ticket online.":"Una función gratis el domingo por la tarde en el histórico teatro de Edmond Town Hall; reserva un boleto gratis en línea.",
 "A youth musical with a cast of local kids in grades 3–12. End times are estimates.":"Un musical juvenil con un elenco de niños locales de 3.º a 12.º grado. Las horas de término son aproximadas.",
 "All ages (2.5K walk for families)":"Todas las edades (caminata de 2.5 km para familias)",
 "$35 through Oct 31, then $45":"$35 hasta el 31 de oct., luego $45",
 "Thanksgiving-morning 5K run and 2.5K family walk benefiting the Booth Library.":"Carrera de 5 km y caminata familiar de 2.5 km la mañana de Acción de Gracias, a beneficio de la Booth Library.",
 "All ages (G)":"Todas las edades (G)",
 "A free holiday matinee at Edmond Town Hall; reserve a free ticket online.":"Una función navideña gratis en Edmond Town Hall; reserva un boleto gratis en línea.",
 "Hawleyville Volunteer Fire Co., 34 Hawleyville Rd":"Hawleyville Volunteer Fire Co., 34 Hawleyville Rd",
 "Santa photos, free pizza, cocoa, cookies and dancers at the firehouse, on a mid-December Sunday. Last year it was Dec 14 at 5:30. This year's date isn't posted yet.":"Fotos con Santa, pizza gratis, chocolate, galletas y bailarines en la estación de bomberos, un domingo a mediados de diciembre. El año pasado fue el 14 de dic. a las 5:30. La fecha de este año aún no se ha publicado.",
 "Edmond Town Hall, 45 Main St":"Edmond Town Hall, 45 Main St",
 "Pancakes, Santa from 8:30 and dance performances, usually the first Saturday of December, 8–noon ($7 kids 12 and under). This year's date isn't posted yet.":"Panqueques, Santa desde las 8:30 y presentaciones de baile, por lo general el primer sábado de diciembre, de 8 a mediodía ($7 niños de 12 años o menos). La fecha de este año aún no se ha publicado.",
 "The Toy Tree, 32 Church Hill Rd":"The Toy Tree, 32 Church Hill Rd",
 "Drop a letter in Santa's mailbox at the toy store with a stamped, self-addressed envelope and Santa writes back. Last year letters were due Dec 15.":"Deja una carta en el buzón de Santa de la juguetería con un sobre con estampilla y tu dirección, y Santa te responde. El año pasado las cartas se recibían hasta el 15 de dic.",
 "EverWonder Children's Museum, 11 Mile Hill Rd":"EverWonder Children's Museum, 11 Mile Hill Rd",
 "A morning countdown to noon with a balloon drop, included with museum admission. It has run on Dec 31 in past years; this year's details aren't posted yet.":"Una cuenta regresiva matutina hasta el mediodía con lluvia de globos, incluida con la entrada al museo. Se ha hecho el 31 de dic. en años anteriores; los detalles de este año aún no se han publicado.",
 "A youth musical-theater company that rehearses and stages two full musicals a year at Edmond Town Hall.":"Una compañía juvenil de teatro musical que ensaya y presenta dos musicales completos al año en Edmond Town Hall.",
 "Grades 3–12":"3.º–12.º grado",
}
