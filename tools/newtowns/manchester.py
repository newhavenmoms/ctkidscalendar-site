W=lambda d,t:{"from":d,"t":t}
D=lambda ds,t:[W(d,t) for d in ds]
SRC="https://manchesterpubliclibraryct.events.mylibrary.digital/"
B=["baby","toddler","preschool"]
ML,WB="manchester-library","whiton-library"
def ev(v,**k):
    e={"v":v,"free":True,"price":"Free","src":SRC}; e.update(k); return e
TOWN={
 "display":"Manchester","accent":"#C4D8F0",
 "venues":{ML:["Manchester Public Library (Main)","1041 Main St"],
           WB:["Whiton Branch Library","100 N Main St"],
           "main-st":["Downtown Main Street","903 Main St"],
           "center-church":["Center Congregational Church","11 Center St"]},
 "venueMeta":{ML:[None,1],WB:[None,1],"main-st":[None,0],"center-church":[None,0]},
 "events":[
  ev(WB,t="Storytime @ Whiton Branch",when=D(["2026-10-12","2026-10-19","2026-10-26","2026-11-02","2026-11-09"],[["10:30","11:00"]]),ages="All ages (best for 2–5)",a=["toddler","preschool"],drop=True,
     blurb="Stories, songs and fingerplays at the Whiton Branch on Monday mornings. Dates past Nov 9 aren't posted yet."),
  ev(ML,t="Mother Goose Storytime",when=D(["2026-10-13","2026-10-20","2026-10-27","2026-11-03","2026-11-10"],[["09:30","10:00"]]),ages="Ages 0–24 months + caregiver",a=["baby","toddler"],drop=True,
     blurb="Rhymes, songs and bounces for babies and young toddlers at the Main Library."),
  ev(ML,t="Family Place Parent/Child Workshop",when=D(["2026-10-13","2026-10-20","2026-10-27","2026-11-03","2026-11-10"],[["18:00","19:00"]]),ages="Ages 0–36 months + caregiver (siblings to 5 welcome)",a=["baby","toddler"],rsvp=True,check=True,
     blurb="An evening playgroup with toys, art and local experts on hand to talk with parents. Registration required; call 860-645-0577."),
  ev(ML,t="Storytime at the Main Library",when=D(["2026-10-14","2026-10-15","2026-10-21","2026-10-22","2026-10-28","2026-10-29","2026-11-04","2026-11-05","2026-11-12"],[["10:30","11:00"]]),ages="All ages (best for 2–5)",a=["toddler","preschool"],drop=True,
     blurb="Stories, songs and fingerplays on Wednesday and Thursday mornings. Dates past Nov 12 aren't posted yet."),
  {"t":"Halloween Happenings Downtown","v":"main-st","special":"hw","when":[W("2026-10-24",[["11:00","13:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://www.locable.com/connections/19730-downtown-manchester-special-services-district/events/2026/10/17/513121/halloween-happenings-3/",
   "blurb":"Crafts and bag decorating from 11, then trick-or-treating along Main Street from 11:30 to 1, with games on Purnell Place and a photo booth."},
 ],
 "tba":[{"g":"hol","t":"Manchester Community Tree Lighting","w":"Center Congregational Church, 11 Center St",
   "p":"Santa rides in on a fire truck, then carols, hot cocoa and family activities before the tree is lit around 5:45. Last year it was the Saturday after Thanksgiving. This year's date isn't posted yet.","src":"https://www.manchesterct.gov/Community/Town-Calendar-of-Events/Tree-Lighting-Ceremony-2025"}],
 "classes":[],
 "library":{"for":"Free, every week","name":"Manchester Public Library","desc":"Storytimes at the Main Library on Wednesday and Thursday mornings and at the Whiton Branch on Mondays, Mother Goose for babies on Tuesdays, and a Family Place playgroup for under-3s on Tuesday evenings.","a":"See the library's calendar","href":SRC},
}
PLACES={
 "out":[("Wickham Park","A big park on the East Hartford line with playgrounds, themed gardens, an aviary and trails (parking fee).","Un gran parque en el límite con East Hartford con áreas de juegos, jardines temáticos, un aviario y senderos (se paga estacionamiento)."),
        ("Oak Grove Nature Center","53 acres of woods, a pond and trails, run by the Lutz Children's Museum.","21 hectáreas de bosque, un estanque y senderos, administrados por el Lutz Children's Museum."),
        ("Center Springs Park","A large town park near downtown with a pond, trails and sledding in winter.","Un gran parque cerca del centro con estanque, senderos y lugar para deslizarse en trineo en invierno.")],
 "rain":[("Lutz Children's Museum","A hands-on children's museum with a live-animal room. Open Tuesday–Sunday; $13–14 per child and adult (247 S Main St).","Un museo infantil interactivo con una sala de animales vivos. Abre de martes a domingo; $13–14 por niño y adulto (247 S Main St)."),
         ("Manchester Public Library","Storytimes most weekday mornings and a Family Place playgroup for babies and toddlers.","Cuentacuentos casi todas las mañanas entre semana y un grupo de juego Family Place para bebés y niños pequeños.")],
 "drive":[("Connecticut Science Center","Ten floors of hands-on science, including KidSpace for kids 7 and under, in Hartford.","Diez pisos de ciencia interactiva, incluido KidSpace para niños de 7 años o menos, en Hartford."),
          ("Dinosaur State Park","Real dinosaur tracks under a geodesic dome, plus trails, in Rocky Hill.","Huellas reales de dinosaurio bajo una cúpula geodésica, además de senderos, en Rocky Hill."),
          ("Bushnell Park","Hartford's downtown park, with a 1914 carousel in the warmer months.","El parque del centro de Hartford, con un carrusel de 1914 en los meses cálidos.")],
}
ES={
 "All ages (best for 2–5)":"Todas las edades (ideal para 2–5 años)",
 "Stories, songs and fingerplays at the Whiton Branch on Monday mornings. Dates past Nov 9 aren't posted yet.":"Cuentos, canciones y juegos con los dedos en la sucursal Whiton los lunes por la mañana. Las fechas después del 9 de nov. aún no se han publicado.",
 "Ages 0–24 months + caregiver":"0–24 meses + un adulto",
 "Rhymes, songs and bounces for babies and young toddlers at the Main Library.":"Rimas, canciones y juegos de rebote para bebés y niños pequeños en la biblioteca principal.",
 "Ages 0–36 months + caregiver (siblings to 5 welcome)":"0–36 meses + un adulto (hermanos hasta 5 años bienvenidos)",
 "An evening playgroup with toys, art and local experts on hand to talk with parents. Registration required; call 860-645-0577.":"Un grupo de juego por la tarde con juguetes, arte y expertos locales para conversar con los padres. Inscripción obligatoria; llama al 860-645-0577.",
 "Stories, songs and fingerplays on Wednesday and Thursday mornings. Dates past Nov 12 aren't posted yet.":"Cuentos, canciones y juegos con los dedos los miércoles y jueves por la mañana. Las fechas después del 12 de nov. aún no se han publicado.",
 "All ages":"Todas las edades",
 "Crafts and bag decorating from 11, then trick-or-treating along Main Street from 11:30 to 1, with games on Purnell Place and a photo booth.":"Manualidades y decoración de bolsas desde las 11, y luego a pedir dulces por Main Street de 11:30 a 1, con juegos en Purnell Place y una cabina de fotos.",
 "Santa rides in on a fire truck, then carols, hot cocoa and family activities before the tree is lit around 5:45. Last year it was the Saturday after Thanksgiving. This year's date isn't posted yet.":"Santa llega en un camión de bomberos, y luego hay villancicos, chocolate caliente y actividades familiares antes de encender el árbol alrededor de las 5:45. El año pasado fue el sábado después de Acción de Gracias. La fecha de este año aún no se ha publicado.",
 "Center Congregational Church, 11 Center St":"Center Congregational Church, 11 Center St",
 "Storytimes at the Main Library on Wednesday and Thursday mornings and at the Whiton Branch on Mondays, Mother Goose for babies on Tuesdays, and a Family Place playgroup for under-3s on Tuesday evenings.":"Cuentacuentos en la biblioteca principal los miércoles y jueves por la mañana y en la sucursal Whiton los lunes, Mother Goose para bebés los martes y un grupo de juego Family Place para menores de 3 años los martes por la tarde.",
 "Free":"Gratis",
}

# ---- Full playbook pass (Oct 7) ----
NWP="northwest-park"; LUTZ="lutz"; WALK="mhs-walks"
TOWN["venues"].update({NWP:["Northwest Park","448 Tolland Tpke"],LUTZ:["Lutz Children's Museum","247 S Main St"],WALK:["Manchester historic walks (meeting spot varies)","See listing for each walk"]})
TOWN["venueMeta"].update({NWP:[None,0],LUTZ:[None,1],WALK:[None,0]})
TC="https://www.manchesterct.gov/Community/Town-Calendar-of-Events"
TOWN["events"]+=[
 {"t":"Downtown Scarecrow Festival Kick-Off","v":"main-st","special":"fall","when":[W("2026-10-10",[["10:00","14:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":TC+"/2026-Downtown-Manchester-Scarecrow-Festival-Kick-off",
  "blurb":"More than 40 handmade scarecrows go up along Main Street for the month (through Oct 31). Walk the route and vote for your favorite on Downtown Manchester's Facebook page."},
 {"t":"2nd Saturdays Downtown","v":"main-st","when":D(["2026-10-10","2026-11-14","2026-12-12"],[["10:00","14:00"]]),"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free to browse","drop":True,"check":True,"src":TC+"/2nd-Saturdays-2026",
  "blurb":"Downtown's monthly Saturday of local art, music, food and culture, with family art stations at WORK_SPACE (903 Main St). Times are from last year."},
 {"t":"America 250: Historic Walks","v":WALK,"when":[W("2026-10-10",[["13:00","14:00"]]),W("2026-10-18",[["12:00","13:00"]]),W("2026-11-08",[["12:00","13:00"]]),W("2026-11-14",[["13:00","14:00"]]),W("2026-12-26",[["13:00","14:00"]])],"ages":"All ages","a":["big"],"free":True,"price":"Free","drop":True,"src":TC+"/America-250-Historic-Walks",
  "blurb":"Free one-hour history walks: Bush Hill farm and foliage (Oct 10, 330 Bush Hill Rd), Cheney Homestead (Oct 18, park at 146 Hartford Rd), East Cemetery (Nov 8, Harrison St entrance), the North End (Nov 14, Whiton Library steps) and a Highland Park hike (Dec 26, 670 Spring St). Rain or shine; no dogs."},
 {"t":"Pumpkin Carving at Northwest Park","v":NWP,"special":"fall","when":D(["2026-10-13","2026-10-14"],[["17:00","19:00"]]),"ages":"All ages","a":["preschool","big"],"free":True,"price":"Free","rsvp":True,"check":True,"src":TC+"/Fall-Fest-2026",
  "blurb":"Carve a pumpkin to light up the park and the Fall Fest haunted trail. Registration recommended to reserve a pumpkin."},
 {"t":"Fall Fest","v":NWP,"special":"fall","when":[W("2026-10-16",[["17:00","20:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free admission","drop":True,"src":TC+"/Fall-Fest-2026",
  "blurb":"The town's fall evening at Northwest Park: bounce houses, a haunted trail, trunk-or-treat candy, dance performances, food trucks and vendors."},
 {"t":"Lutz Spooktacular","v":LUTZ,"special":"hw","when":[W("2026-10-24",[["09:30","11:30"]])],"ages":"Young children","a":B+["big"],"free":False,"price":"$5 per child","check":True,"src":"https://lutzmuseum.org/calendar-1",
  "blurb":"Come in costume and trick-or-treat with the museum's animal ambassadors, some of them dressed up too."},
 {"t":"Holiday on Main","v":"main-st","special":"hol","when":[W("2026-11-28",[["10:00","14:00"]])],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"src":"https://www.locable.com/connections/19730-downtown-manchester-special-services-district/events/2026/11/28/513128/holiday-on-main-6/",
  "blurb":"Visit Santa and Mrs. Claus, step into a snow globe and pose in the igloo photo booth downtown."},
]
TOWN["classes"]+=[
 {"id":"goldfish-manchester","c":"swim","n":"Goldfish Swim School","u":"https://goldfishswimschool.com/manchester/",
  "blurb":"Small-group swim lessons in a warm indoor pool, from parent-and-baby classes up to a kids' swim team, plus family swims.","ages":"4 months–12 years","where":"1147 Tolland Tpke"},
 {"id":"silk-city-gym","c":"move","n":"Silk City Gymnastics and Dance","u":"https://silkcitygymnastics.com",
  "blurb":"Parent-and-me and preschool gymnastics, girls' and boys' classes, dance, and trampoline and tumbling.","ages":"18 months–18 years","where":"Manchester"},
 {"id":"manchester-rec-swim","c":"swim","n":"Manchester Recreation Swim Lessons","u":"https://www.manchesterct.gov/Government/Departments/Leisure-Family-and-Recreation-Department/Recreation-Divison/Recreation-Programs/Learn-to-Swim",
  "blurb":"Town swim lessons for Manchester residents, from parent-and-infant classes to Levels 1–6, at the high school pools. Fall sessions run October–December; register online.","ages":"6 months–12 years","where":"Manchester High School pools"},
]
PLACES["rain"]+=[("The Fire Museum","A 1901 wooden firehouse full of antique fire engines in the Cheney mill district (230 Pine St). Open Saturdays 10–4.","Un cuartel de bomberos de madera de 1901 lleno de camiones antiguos en el distrito de los molinos Cheney (230 Pine St). Abre los sábados de 10 a 4."),
                 ("Old Manchester Museum","The historical society's museum of town history, with a one-room-schoolhouse corner (126 Cedar St); call 860-647-9983 for hours.","El museo de historia del pueblo de la sociedad histórica, con un rincón de escuela antigua (126 Cedar St); llama al 860-647-9983 para el horario."),
                 ("Once Upon A Child","A kids' resale shop with gently used toys, books and gear (410 Middle Tpke W).","Una tienda de segunda mano para niños con juguetes, libros y artículos en buen estado (410 Middle Tpke W).")]
PLACES["out"]+=[("Botticello Farms","A big farm stand and pumpkin patch on Hillstown Road, busy every fall weekend (209 Hillstown Rd).","Un gran puesto de granja y campo de calabazas en Hillstown Road, muy concurrido los fines de semana de otoño (209 Hillstown Rd).")]
ES.update({
 "More than 40 handmade scarecrows go up along Main Street for the month (through Oct 31). Walk the route and vote for your favorite on Downtown Manchester's Facebook page.":"Más de 40 espantapájaros hechos a mano se colocan en Main Street durante el mes (hasta el 31 de oct.). Recorre la ruta y vota por tu favorito en la página de Facebook de Downtown Manchester.",
 "Free to browse":"Gratis para pasear",
 "Downtown's monthly Saturday of local art, music, food and culture, with family art stations at WORK_SPACE (903 Main St). Times are from last year.":"El sábado mensual del centro con arte local, música, comida y cultura, con estaciones de arte familiar en WORK_SPACE (903 Main St). El horario es del año pasado.",
 "Free one-hour history walks: Bush Hill farm and foliage (Oct 10, 330 Bush Hill Rd), Cheney Homestead (Oct 18, park at 146 Hartford Rd), East Cemetery (Nov 8, Harrison St entrance), the North End (Nov 14, Whiton Library steps) and a Highland Park hike (Dec 26, 670 Spring St). Rain or shine; no dogs.":"Caminatas gratis de una hora por la historia local: granja y follaje de Bush Hill (10 de oct., 330 Bush Hill Rd), Cheney Homestead (18 de oct., estaciona en 146 Hartford Rd), East Cemetery (8 de nov., entrada de Harrison St), el North End (14 de nov., escalones de la Whiton Library) y una caminata en Highland Park (26 de dic., 670 Spring St). Con lluvia o sol; sin perros.",
 "See listing for each walk":"Ver el lugar de cada caminata",
 "Carve a pumpkin to light up the park and the Fall Fest haunted trail. Registration recommended to reserve a pumpkin.":"Talla una calabaza para iluminar el parque y el sendero embrujado del Fall Fest. Se recomienda inscribirse para apartar una calabaza.",
 "Free admission":"Entrada gratis",
 "The town's fall evening at Northwest Park: bounce houses, a haunted trail, trunk-or-treat candy, dance performances, food trucks and vendors.":"La noche de otoño del pueblo en Northwest Park: brincolines, un sendero embrujado, dulces desde los autos, presentaciones de baile, camiones de comida y vendedores.",
 "Young children":"Niños pequeños",
 "$5 per child":"$5 por niño",
 "Come in costume and trick-or-treat with the museum's animal ambassadors, some of them dressed up too.":"Ven disfrazado a pedir dulces con los animales embajadores del museo, algunos también disfrazados.",
 "Visit Santa and Mrs. Claus, step into a snow globe and pose in the igloo photo booth downtown.":"Visita a Santa y a la Sra. Claus, entra en una bola de nieve gigante y posa en la cabina de fotos del iglú en el centro.",
 "Small-group swim lessons in a warm indoor pool, from parent-and-baby classes up to a kids' swim team, plus family swims.":"Clases de natación en grupos pequeños en una alberca techada y templada, desde clases de papá/mamá y bebé hasta un equipo infantil, además de nado familiar.",
 "4 months–12 years":"4 meses–12 años",
 "Parent-and-me and preschool gymnastics, girls' and boys' classes, dance, and trampoline and tumbling.":"Gimnasia de papá/mamá y yo y preescolar, clases para niñas y niños, danza, y trampolín y acrobacia.",
 "18 months–18 years":"18 meses–18 años",
 "Town swim lessons for Manchester residents, from parent-and-infant classes to Levels 1–6, at the high school pools. Fall sessions run October–December; register online.":"Clases de natación del pueblo para residentes de Manchester, desde clases de papá/mamá y bebé hasta los niveles 1–6, en las albercas de la preparatoria. Las sesiones de otoño van de octubre a diciembre; inscríbete en línea.",
 "6 months–12 years":"6 meses–12 años",
 "Manchester High School pools":"Albercas de Manchester High School",
})

# ---- gap check (Oct 7) ----
PLACES["out"]+=[("Olcott Street Sprayground","A free sprayground open daily 10–8 from late May through Labor Day weekend (121 Olcott St).","Una zona de chorros de agua gratis abierta todos los días de 10 a 8 desde finales de mayo hasta el fin de semana de Labor Day (121 Olcott St).")]

# ---- Manchester Now Fall 2026 guide (PDF, Oct 8) ----
GUIDE="https://www.flipsnack.com/57FF8EB569B/manchester-now-fall-2026"
LL="leisure-labs"; YSB="manchester-ysb"; ECC="manchester-ecc"; CY="community-y"; FAS="firestone"; MHSP="mhs-pools"
TOWN["venues"].update({LL:["Leisure Labs at Mahoney Center","110 Cedar St"],YSB:["Manchester Youth Service Bureau","63 Linden St"],
  ECC:["Early Childhood Center (Northwest Park, Building 1)","448 Tolland Tpke"],CY:["Community Y Rec Center","78 N Main St"],
  FAS:["The Firestone Art Studio & Cafe","1115 Main St"],MHSP:["Manchester High School pools","134 E Middle Tpke"]})
TOWN["venueMeta"].update({LL:[None,1],YSB:[None,1],ECC:[None,1],CY:[None,1],FAS:[None,1],MHSP:[None,1]})
def g(v,**k):
    e={"v":v,"free":True,"price":"Free","src":GUIDE}; e.update(k); return e
NOV26="2026-11-26"
TOWN["events"]+=[
 # little ones
 g(ML,t="Open Playgroup",s=[[5,[["10:00","12:00"]],"2026-10-09","2026-12-18"]],x=["2026-11-27"],ages="Preschool-age children + caregiver",a=["toddler","preschool"],drop=True,check=True,
   blurb="A free Friday-morning playgroup at the new Main Library. Toys are provided; a grown-up stays and supervises."),
 g(ECC,t="Play Pals Drop-In Play Time",s=[[1,[["09:30","11:00"]],"2026-10-12","2026-12-14"]],ages="6 months–4 years + caregiver",a=["baby","toddler","preschool"],drop=True,
   blurb="A free drop-in playgroup where little ones and their grown-ups can play, socialize and meet other families."),
 g(ECC,t="Robin's Mothering Group",s=[[4,[["11:30","13:30"]],"2026-10-08","2026-12-17"]],x=[NOV26],ages="Moms with babies under 1",a=["baby"],drop=True,check=True,
   blurb="A weekly support group for moms of babies under a year old, led by a lactation consultant. The facilitator announces any cancellations."),
 g(ECC,t="Cradle to Crayons Playgroup",s=[[4,[["15:00","16:15"]],"2026-10-15","2026-12-10"]],x=[NOV26],ages="Ages 2–5 + caregiver",a=["toddler","preschool"],check=True,
   blurb="A preschool playgroup that builds the skills kids need for school, with a grown-up alongside."),
 g(LL,t="Start Smart Soccer",when=D(["2026-10-17","2026-10-24","2026-10-31","2026-11-07","2026-11-14"],[["08:30","09:30"]]),ages="Ages 3–5 + parent",a=["preschool"],free=False,price="$65 ($81 non-residents), equipment included",rsvp=True,
   blurb="Parents and kids learn soccer basics together: dribbling, kicking, trapping, passing, shooting and agility. Five Saturday mornings."),
 # school-age
 g(YSB,t="Journey Art & Nature: Build-a-Book",s=[[3,[["15:30","17:00"]],"2026-10-14","2026-12-16"]],x=["2026-11-25"],ages="Grades 4–5",a=["big"],rsvp=True,check=True,
   blurb="Create, write and illustrate your own book inspired by nature and art. An after-school series; register with the Youth Service Bureau."),
 g(LL,t="Glow Art Studio",when=[W("2026-11-06",[["19:00","20:30"]])],ages="Ages 7–12",a=["big"],free=False,price="$10",rsvp=True,
   blurb="Blacklight painting, glowing crafts and neon fun in the dark, for all skill levels."),
 g(LL,t="Sprout Squad: Recycled Gardeners",when=[W("2026-11-07",[["10:00","11:30"]])],ages="Ages 7–12",a=["big"],rsvp=True,check=True,
   blurb="Grow plants in recycled yogurt cups and soda bottles. Kids decorate planters, plant seeds and keep an observation journal."),
 # families
 g(MHSP,t="Weekend Open Swim (IOH Pool)",s=[[6,[["12:00","13:00"]],"2026-10-17","2026-12-12"]],x=["2026-11-28"],ages="All ages",a=B+["big"],free=False,price="Manchester facility pass (residents)",drop=True,
   blurb="Saturday open swim at the high school's indoor pool. There's also open swim Monday and Wednesday 7:30–8:30pm. Pools are closed Nov 11 and Nov 23–28."),
 g(NWP,t="Eastside Farmers Market Fall Pop-Up",special="fall",when=[W("2026-10-14",[["16:00","19:00"]])],ages="All ages",a=B+["big"],price="Free to browse",drop=True,
   blurb="The farmers market's fall pop-up at Northwest Park: 25+ vendors, fall crafts and pumpkin carving. Kids get a $3 voucher for fresh produce."),
 g(LL,t="Drop-In Art Night",s=[[2,[["18:00","20:00"]],"2026-10-13","2026-12-15"]],ages="Kids and families",a=["preschool","big"],drop=True,check=True,
   blurb="A different craft each week: Halloween bats, handprint ghosts, monsters, fall trees, caramel apples, thankful turkeys, snowflakes and more. Also Mondays at Waddell and Wednesdays at Verplanck (Rec Card needed) and Thursdays at the Community Y."),
 g(CY,t="Drop-In Art Night",s=[[4,[["18:00","20:00"]],"2026-10-08","2026-12-17"]],x=[NOV26],ages="Kids and families",a=["preschool","big"],drop=True,check=True,
   blurb="The Thursday edition of the town's weekly drop-in craft night: a new seasonal project each week, from Halloween bats to name snowflakes."),
 g(FAS,t="Paint-Your-Own Pottery: Family Plates",when=[W("2026-10-22",[["17:00","19:00"]])],ages="Ages 2+ with family",a=["toddler","preschool","big"],rsvp=True,check=True,
   blurb="Paint custom dinner plates together as a family at The Firestone. A Youth Service Bureau program; register ahead."),
 g(LL,t="Family Karaoke Night",when=D(["2026-10-23","2026-11-20"],[["19:00","20:30"]]),ages="All ages",a=["preschool","big"],drop=True,check=True,
   blurb="Sing your heart out with family and friends at Leisure Labs."),
 g(LL,t="Brunch & Board Games",when=D(["2026-10-24","2026-11-21"],[["10:00","11:30"]]),ages="All ages",a=["preschool","big"],rsvp=True,
   blurb="Board games with light snacks on a Saturday morning. Registration required."),
 g(LL,t="Friday Movie Night",when=[W("2026-10-30",[["19:00","21:00"]]),W("2026-11-20",[["19:00","21:00"]]),W("2026-12-04",[["19:00","21:00"]])],ages="All ages (PG films)",a=["preschool","big"],drop=True,check=True,
   blurb="Family movies on the big screen in the gym: Hocus Pocus (Oct 30), Matilda (Nov 20) and Home Alone (Dec 4)."),
 g(CY,t="Yoga for Food",when=[W("2026-11-13",[["18:30","19:30"]])],ages="All ages",a=["big"],drop=True,
   blurb="A free community yoga class. Bring a nonperishable food item for the MACC food pantry. No experience needed."),
 g(YSB,t="Family Pie-Making Workshop",when=[W("2026-11-24",[["17:00","19:00"]])],ages="All ages",a=["preschool","big"],rsvp=True,check=True,
   blurb="Make your own apple pie as a family, just in time for Thanksgiving."),
 g(CY,t="Yoga for Toys",special="hol",when=[W("2026-12-04",[["18:30","19:30"]])],ages="All ages",a=["big"],drop=True,
   blurb="A free community yoga class. Bring an unwrapped toy for the Blue Angels and Manchester Police toy drive. No experience needed."),
 g(YSB,t="Family Gingerbread House Competition",special="hol",when=[W("2026-12-17",[["17:00","19:00"]])],ages="Ages 2+ with family",a=["toddler","preschool","big"],rsvp=True,check=True,
   blurb="The 4th annual family gingerbread house contest: build, decorate and enjoy."),
]
TOWN["classes"]+=[
 {"id":"manchester-play-learn","c":"build","n":"Play & Learn (Early Childhood Center)","u":GUIDE,
  "blurb":"Six-week themed classes with stories, crafts and hands-on play. New sessions: About Autumn (Tuesdays 9–10:30, from Oct 27) and About Space (Thursdays 9:30–11, from Oct 29). $36 ($44 non-residents).","ages":"18 months–5 years","where":"448 Tolland Tpke (Northwest Park)"},
 {"id":"manchester-rec-hoops","c":"move","n":"Manchester Rec youth basketball","u":GUIDE,
  "blurb":"Fundamentals of Basketball for ages 6–7 on Saturday mornings from early December, and youth leagues for ages 8–12 (evaluation clinic Nov 13). $35. Free drop-in hoops at Leisure Labs for 12 and under, weekdays 5–6pm (Rec Card).","ages":"6–12 years","where":"Leisure Labs, 110 Cedar St"},
]
TOWN["classes"]=[dict(c,blurb="Town swim lessons from parent-and-infant classes up to Levels 1–6 at the high school pools, $25 per child per session. Manchester residents only; first-timers register in person.") if c["id"]=="manchester-rec-swim" else c for c in TOWN["classes"]]
PLACES["out"]+=[("Charter Oak Park and Union Pond Park skating","Free outdoor ice skating with lights when it's cold enough for safe ice.","Patinaje sobre hielo al aire libre gratis y con iluminación cuando hace suficiente frío para que el hielo sea seguro.")]
PLACES["rain"]=[("Manchester Public Library","The new downtown Main Library (opened Sept 2026, 1041 Main St) has a rooftop garden patio, a Friday-morning playgroup and storytimes most weekday mornings.","La nueva biblioteca principal del centro (abrió en sept. de 2026, 1041 Main St) tiene un patio con jardín en la azotea, un grupo de juego los viernes por la mañana y cuentacuentos casi todas las mañanas entre semana.") if p[0]=="Manchester Public Library" else p for p in PLACES["rain"]]
PLACES["rain"]+=[("The Firestone Art Studio & Cafe","Walk-in pottery, canvas and wood-sign painting seven days a week, with a cafe (1115 Main St).","Pintura de cerámica, lienzos y letreros de madera sin cita los siete días de la semana, con cafetería (1115 Main St).")]
ES.update({
 "Preschool-age children + caregiver":"Niños en edad preescolar + un adulto",
 "A free Friday-morning playgroup at the new Main Library. Toys are provided; a grown-up stays and supervises.":"Un grupo de juego gratis los viernes por la mañana en la nueva biblioteca principal. Hay juguetes; un adulto se queda y supervisa.",
 "6 months–4 years + caregiver":"6 meses–4 años + un adulto",
 "A free drop-in playgroup where little ones and their grown-ups can play, socialize and meet other families.":"Un grupo de juego gratis sin inscripción donde los pequeños y sus adultos pueden jugar, convivir y conocer a otras familias.",
 "Moms with babies under 1":"Mamás con bebés menores de 1 año",
 "A weekly support group for moms of babies under a year old, led by a lactation consultant. The facilitator announces any cancellations.":"Un grupo de apoyo semanal para mamás de bebés menores de un año, dirigido por una consultora de lactancia. La facilitadora avisa de cualquier cancelación.",
 "Ages 2–5 + caregiver":"2–5 años + un adulto",
 "A preschool playgroup that builds the skills kids need for school, with a grown-up alongside.":"Un grupo de juego preescolar que desarrolla las habilidades que los niños necesitan para la escuela, con un adulto a su lado.",
 "Ages 3–5 + parent":"3–5 años + papá o mamá",
 "$65 ($81 non-residents), equipment included":"$65 ($81 no residentes), equipo incluido",
 "Parents and kids learn soccer basics together: dribbling, kicking, trapping, passing, shooting and agility. Five Saturday mornings.":"Padres e hijos aprenden juntos lo básico del fútbol: driblar, patear, controlar, pasar, tirar y agilidad. Cinco sábados por la mañana.",
 "Grades 4–5":"4.º–5.º grado",
 "Create, write and illustrate your own book inspired by nature and art. An after-school series; register with the Youth Service Bureau.":"Crea, escribe e ilustra tu propio libro inspirado en la naturaleza y el arte. Una serie después de clases; inscríbete con el Youth Service Bureau.",
 "Ages 7–12":"7–12 años",
 "$10":"$10",
 "Blacklight painting, glowing crafts and neon fun in the dark, for all skill levels.":"Pintura con luz negra, manualidades que brillan y diversión neón en la oscuridad, para todos los niveles.",
 "Grow plants in recycled yogurt cups and soda bottles. Kids decorate planters, plant seeds and keep an observation journal.":"Cultiva plantas en vasos de yogur y botellas de refresco recicladas. Los niños decoran macetas, siembran semillas y llevan un diario de observación.",
 "Manchester facility pass (residents)":"Pase de instalaciones de Manchester (residentes)",
 "Saturday open swim at the high school's indoor pool. There's also open swim Monday and Wednesday 7:30–8:30pm. Pools are closed Nov 11 and Nov 23–28.":"Nado libre los sábados en la alberca techada de la preparatoria. También hay nado libre los lunes y miércoles de 7:30 a 8:30 p. m. Las albercas cierran el 11 de nov. y del 23 al 28 de nov.",
 "The farmers market's fall pop-up at Northwest Park: 25+ vendors, fall crafts and pumpkin carving. Kids get a $3 voucher for fresh produce.":"El mercado de otoño del mercado de agricultores en Northwest Park: más de 25 vendedores, manualidades de otoño y tallado de calabazas. Los niños reciben un vale de $3 para frutas y verduras frescas.",
 "Kids and families":"Niños y familias",
 "A different craft each week: Halloween bats, handprint ghosts, monsters, fall trees, caramel apples, thankful turkeys, snowflakes and more. Also Mondays at Waddell and Wednesdays at Verplanck (Rec Card needed) and Thursdays at the Community Y.":"Una manualidad distinta cada semana: murciélagos de Halloween, fantasmas con la mano, monstruos, árboles de otoño, manzanas acarameladas, pavos agradecidos, copos de nieve y más. También los lunes en Waddell y los miércoles en Verplanck (se necesita Rec Card) y los jueves en el Community Y.",
 "The Thursday edition of the town's weekly drop-in craft night: a new seasonal project each week, from Halloween bats to name snowflakes.":"La edición de los jueves de la noche semanal de manualidades del pueblo, sin inscripción: un proyecto de temporada nuevo cada semana, desde murciélagos de Halloween hasta copos de nieve con tu nombre.",
 "Ages 2+ with family":"2 años en adelante, en familia",
 "Paint custom dinner plates together as a family at The Firestone. A Youth Service Bureau program; register ahead.":"Pinten juntos platos personalizados en familia en The Firestone. Un programa del Youth Service Bureau; inscríbete con anticipación.",
 "Sing your heart out with family and friends at Leisure Labs.":"Canta con todas tus ganas con familia y amigos en Leisure Labs.",
 "Board games with light snacks on a Saturday morning. Registration required.":"Juegos de mesa con bocadillos ligeros un sábado por la mañana. Inscripción obligatoria.",
 "All ages (PG films)":"Todas las edades (películas PG)",
 "Family movies on the big screen in the gym: Hocus Pocus (Oct 30), Matilda (Nov 20) and Home Alone (Dec 4).":"Películas familiares en la pantalla grande del gimnasio: Hocus Pocus (30 de oct.), Matilda (20 de nov.) y Mi pobre angelito (4 de dic.).",
 "A free community yoga class. Bring a nonperishable food item for the MACC food pantry. No experience needed.":"Una clase de yoga comunitaria gratis. Trae un alimento no perecedero para la despensa de MACC. No se necesita experiencia.",
 "Make your own apple pie as a family, just in time for Thanksgiving.":"Hagan su propio pay de manzana en familia, justo a tiempo para Acción de Gracias.",
 "A free community yoga class. Bring an unwrapped toy for the Blue Angels and Manchester Police toy drive. No experience needed.":"Una clase de yoga comunitaria gratis. Trae un juguete sin envolver para la colecta de juguetes de Blue Angels y la Policía de Manchester. No se necesita experiencia.",
 "The 4th annual family gingerbread house contest: build, decorate and enjoy.":"El 4.º concurso familiar anual de casas de jengibre: construye, decora y disfruta.",
 "Six-week themed classes with stories, crafts and hands-on play. New sessions: About Autumn (Tuesdays 9–10:30, from Oct 27) and About Space (Thursdays 9:30–11, from Oct 29). $36 ($44 non-residents).":"Clases temáticas de seis semanas con cuentos, manualidades y juego práctico. Nuevas sesiones: About Autumn (martes de 9 a 10:30, desde el 27 de oct.) y About Space (jueves de 9:30 a 11, desde el 29 de oct.). $36 ($44 no residentes).",
 "18 months–5 years":"18 meses–5 años",
 "448 Tolland Tpke (Northwest Park)":"448 Tolland Tpke (Northwest Park)",
 "Fundamentals of Basketball for ages 6–7 on Saturday mornings from early December, and youth leagues for ages 8–12 (evaluation clinic Nov 13). $35. Free drop-in hoops at Leisure Labs for 12 and under, weekdays 5–6pm (Rec Card).":"Fundamentos de básquetbol para niños de 6–7 años los sábados por la mañana desde principios de diciembre, y ligas juveniles para 8–12 años (clínica de evaluación el 13 de nov.). $35. Básquetbol libre gratis en Leisure Labs para menores de 12, entre semana de 5 a 6 p. m. (Rec Card).",
 "6–12 years":"6–12 años",
 "Leisure Labs, 110 Cedar St":"Leisure Labs, 110 Cedar St",
 "Town swim lessons from parent-and-infant classes up to Levels 1–6 at the high school pools, $25 per child per session. Manchester residents only; first-timers register in person.":"Clases de natación del pueblo, desde clases de papá/mamá y bebé hasta los niveles 1–6, en las albercas de la preparatoria; $25 por niño por sesión. Solo para residentes de Manchester; quienes se inscriben por primera vez lo hacen en persona.",
})

# ---- creative places / bookstores / blogs pass (Oct 8) ----
PLACES["rain"]+=[
 ("Lava Island","An indoor play park with trampolines, foam pits, slides and a toddler area, open daily 9–9 (Fri–Sat to 10). Kids $16 an hour or $22 all day; adults $8 (169 Hale Rd).","Un parque de juegos techado con trampolines, fosas de espuma, toboganes y área para pequeños, abierto todos los días de 9 a 9 (vie–sáb hasta las 10). Niños $16 la hora o $22 todo el día; adultos $8 (169 Hale Rd)."),
 ("Flight Adventure Park","A big trampoline and inflatable park with a Kidz Zone for under-4s and an arcade; grip socks required (145 Spencer St).","Un gran parque de trampolines e inflables con una Kidz Zone para menores de 4 años y una sala de juegos; se requieren calcetines antideslizantes (145 Spencer St)."),
 ("KidZone","Inflatables, an arcade and a toddler area, Wednesday–Sunday (412B Middle Tpke W). Ages 3+ $18, 2 and under $13.","Inflables, sala de juegos y área para pequeños, de miércoles a domingo (412B Middle Tpke W). 3 años o más $18, 2 años o menos $13."),
 ("Stone Age Rock Gym","An indoor climbing gym open daily, with a kids' climbing club (195 Adams St). Day pass about $15.","Un gimnasio de escalada techado abierto todos los días, con club de escalada para niños (195 Adams St). Pase de un día unos $15."),
 ("Barnes & Noble, Buckland Hills","A big bookstore with a children's section at The Shoppes at Buckland Hills, where there's also a free indoor play area by the food court.","Una gran librería con sección infantil en The Shoppes at Buckland Hills, donde también hay un área de juegos techada gratis junto a la zona de comida."),
]
TOWN["classes"]+=[
 {"id":"code-ninjas-manchester","c":"build","n":"Code Ninjas Manchester","u":"https://reviews.listen360.com/code-ninjas-manchester",
  "blurb":"Kids learn to code by building their own video games, earning belts as they go; after-school sessions and school-break camps.","ages":"7–14 years","where":"388 Middle Tpke W"},
 {"id":"summit-music","c":"music","n":"Summit Music Center","u":"https://thehomeschoolmom.com/local/summit-music-studios",
  "blurb":"One-on-one lessons on most instruments and voice in a downtown music store with 12 teaching studios.","ages":"Kids and teens","where":"421 Main St"},
]
ES.update({
 "Kids learn to code by building their own video games, earning belts as they go; after-school sessions and school-break camps.":"Los niños aprenden a programar creando sus propios videojuegos y ganan cinturones al avanzar; sesiones después de clases y campamentos en vacaciones escolares.",
 "7–14 years":"7–14 años",
 "One-on-one lessons on most instruments and voice in a downtown music store with 12 teaching studios.":"Clases individuales de casi todos los instrumentos y canto en una tienda de música del centro con 12 estudios de enseñanza.",
 "Kids and teens":"Niños y adolescentes",
})
