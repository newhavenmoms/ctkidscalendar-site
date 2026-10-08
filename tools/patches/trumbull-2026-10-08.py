# Full playbook re-run, Oct 8 2026
TN="tnac"; TNS="https://www.trumbullnatureandartscenter.org/community"
TOWN["venues"][TN]=["Trumbull Nature & Arts Center","7115 Main St"]; TOWN["venueMeta"][TN]=[None,0]
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"]!="Halloween Costume Swap"]
for e in TOWN["events"]:
    if e["t"]=="Trumbull Farmers' Market": e["s"][0][1]=[["16:00","19:00"]]
def tn(t,d,tm,ages,a,price,blurb,special=None):
    e={"t":t,"v":TN,"when":[W(d,tm)],"ages":ages,"a":a,"free":price=="Free","price":price,"rsvp":True,"check":True,"src":TNS,"blurb":blurb}
    if special: e["special"]=special
    return e
TOWN["events"]+=[
 {"t":"Free Halloween Costume Boutique","v":"trumbull-library","special":"hw","when":[W("2026-10-08",[["17:00","19:30"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://trumbull.libcal.com/event/17291716",
  "blurb":"Pick out a free, gently used Halloween costume, with Sustainable Trumbull. First come, first served."},
 tn("Hike Through the Valley","2026-10-17",[["09:45","11:00"]],"All ages",B+["big"],"Free","A guided family hike from the nature center. Register ahead; end time is an estimate.","fall"),
 tn("S'mores and Storytelling Around the Campfire","2026-10-17",[["18:00","19:30"]],"All ages",["preschool","big"],"$20 per family","Campfire stories and s'mores at the nature center. Register ahead; end time is an estimate.","fall"),
 {"t":"Science Adventure Trail (guided)","v":TN,"when":[W("2026-10-18",[["11:00","12:00"],["12:00","13:00"]])],"ages":"Ages 6+","a":["big"],"free":False,"price":"$20 per family","rsvp":True,"check":True,"src":TNS,
  "blurb":"A guided walk along a trail with 10 hands-on science stops; each family gets a tool kit and guide."},
 tn("Interactive Habitats Exhibit and Science Activity","2026-11-08",[["11:00","12:00"]],"Ages 4+",["preschool","big"],"Free","Explore the habitat exhibit, then do a hands-on science activity. Register ahead; also Nov 14."),
 tn("Interactive Habitats Exhibit and Science Activity","2026-11-14",[["11:00","12:00"]],"Ages 4+",["preschool","big"],"Free","Explore the habitat exhibit, then do a hands-on science activity. Register ahead; also Nov 8."),
 tn("Stuffy Animal Crafting","2026-11-21",[["10:00","11:30"]],"Families with kids 9+",["big"],"$20 per family","Sew or craft your own stuffed animal. Register ahead; end time is an estimate."),
 tn("Blue Spruce Holiday Wreath Crafting","2026-12-05",[["10:00","11:30"]],"Families with kids 8+",["big"],"$20 per family","Make a fresh blue spruce holiday wreath to take home. Register ahead; end time is an estimate.","hol"),
 {"t":"Drop-In Story Time","v":"trumbull-library","s":[[4,[["16:00","16:30"]],"2026-10-08","2026-12-17"]],"x":["2026-11-26"],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://trumbull.libcal.com/event/17200831",
  "blurb":"After-school stories for kids and families every Thursday at 4, no sign-up needed."},
 {"t":"Art to Go DIY Bags","v":"fairchild-nichols","when":[{"from":d,"t":[]} for d in ["2026-10-08","2026-10-15","2026-10-22","2026-10-29","2026-11-05","2026-11-12","2026-11-19","2026-12-03"]],"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","drop":True,"src":"https://trumbull.libcal.com/event/17789013",
  "blurb":"A new themed art kit every Thursday at the Nichols branch, to make at the library or take home."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Menorah Lighting at Town Hall","w":"Trumbull Town Hall, 5866 Main St","p":"Chabad Lubavitch's menorah lighting with doughnuts, gelt, dreidels, latkes and a prize for every child, on one night of Hanukkah (Dec 4–12 this year). Last year it was Dec 15 at 6pm. This year's date isn't posted yet.","src":"https://patch.com/connecticut/trumbull/trumbull-hold-menorah-lighting-town-hall"},
 {"g":"hol","t":"Nichols FD Toy Drive & Popcorn Ball Toss","w":"Nichols Fire Department, 100 Shelton Rd","p":"Photos with Santa and the fire truck while the firefighters collect toys for Trumbull Social Services, on a mid-December Saturday. Last year it was Dec 13, 10–noon. This year's date isn't posted yet.","src":"https://www.patch.com/connecticut/trumbull/nichols-fd-host-annual-holiday-toy-drive-popcorn-ball-toss-trumbull"},
]
ADD_PLACES["out"]+=[("Trumbull Nature & Arts Center","Grounds, a playground and trails open dawn to dusk year-round, free, plus a Science Adventure Trail for ages 6+ and seasonal family programs (7115 Main St).","Terrenos, área de juegos y senderos abiertos del amanecer al anochecer todo el año, gratis, además de un Science Adventure Trail para mayores de 6 años y programas familiares de temporada (7115 Main St).")]
ADD_PLACES["rain"]+=[("Kidz Klub at Westfield Trumbull","An indoor play area at the mall with a mini club for little ones and a mega club for bigger kids (5065 Main St); call ahead for hours and prices.","Un área de juegos techada en el centro comercial con un mini club para los pequeños y un mega club para los mayores (5065 Main St); llama antes para confirmar horario y precios.")]
ES={
 "Pick out a free, gently used Halloween costume, with Sustainable Trumbull. First come, first served.":"Escoge un disfraz de Halloween usado y en buen estado, gratis, con Sustainable Trumbull. Por orden de llegada.",
 "A guided family hike from the nature center. Register ahead; end time is an estimate.":"Una caminata familiar guiada desde el centro de naturaleza. Inscríbete con anticipación; la hora de término es aproximada.",
 "$20 per family":"$20 por familia",
 "Campfire stories and s'mores at the nature center. Register ahead; end time is an estimate.":"Cuentos alrededor de la fogata y s'mores en el centro de naturaleza. Inscríbete con anticipación; la hora de término es aproximada.",
 "Ages 6+":"6 años o más",
 "A guided walk along a trail with 10 hands-on science stops; each family gets a tool kit and guide.":"Un recorrido guiado por un sendero con 10 paradas de ciencia práctica; cada familia recibe un kit de herramientas y una guía.",
 "Ages 4+":"4 años o más",
 "Explore the habitat exhibit, then do a hands-on science activity. Register ahead; also Nov 14.":"Explora la exposición de hábitats y luego haz una actividad de ciencia práctica. Inscríbete con anticipación; también el 14 de nov.",
 "Explore the habitat exhibit, then do a hands-on science activity. Register ahead; also Nov 8.":"Explora la exposición de hábitats y luego haz una actividad de ciencia práctica. Inscríbete con anticipación; también el 8 de nov.",
 "Families with kids 9+":"Familias con niños de 9 años o más",
 "Sew or craft your own stuffed animal. Register ahead; end time is an estimate.":"Cose o arma tu propio peluche. Inscríbete con anticipación; la hora de término es aproximada.",
 "Families with kids 8+":"Familias con niños de 8 años o más",
 "Make a fresh blue spruce holiday wreath to take home. Register ahead; end time is an estimate.":"Haz una corona navideña de abeto azul fresco para llevar a casa. Inscríbete con anticipación; la hora de término es aproximada.",
 "After-school stories for kids and families every Thursday at 4, no sign-up needed.":"Cuentos después de clases para niños y familias cada jueves a las 4, sin inscripción.",
 "A new themed art kit every Thursday at the Nichols branch, to make at the library or take home.":"Un nuevo kit de arte temático cada jueves en la sucursal de Nichols, para hacerlo en la biblioteca o llevarlo a casa.",
 "Trumbull Town Hall, 5866 Main St":"Ayuntamiento de Trumbull, 5866 Main St",
 "Chabad Lubavitch's menorah lighting with doughnuts, gelt, dreidels, latkes and a prize for every child, on one night of Hanukkah (Dec 4–12 this year). Last year it was Dec 15 at 6pm. This year's date isn't posted yet.":"El encendido de la menorá de Jabad Lubavitch con donas, monedas de chocolate, dreidels, latkes y un premio para cada niño, en una noche de Janucá (del 4 al 12 de dic. este año). El año pasado fue el 15 de dic. a las 6 p. m. La fecha de este año aún no se ha publicado.",
 "Nichols Fire Department, 100 Shelton Rd":"Departamento de Bomberos de Nichols, 100 Shelton Rd",
 "Photos with Santa and the fire truck while the firefighters collect toys for Trumbull Social Services, on a mid-December Saturday. Last year it was Dec 13, 10–noon. This year's date isn't posted yet.":"Fotos con Santa y el camión de bomberos mientras los bomberos recolectan juguetes para los Servicios Sociales de Trumbull, un sábado a mediados de diciembre. El año pasado fue el 13 de dic., de 10 a mediodía. La fecha de este año aún no se ha publicado.",
}
