# Full playbook re-run, Oct 8 2026
GAC="guilford-art-center"; BO="bishops"
TOWN["venues"].update({GAC:["Guilford Art Center","411 Church St"],BO:["Bishop's Orchards (pick-your-own fields)","480 New England Rd"]})
TOWN["venueMeta"].update({GAC:[None,1],BO:[None,0]})
for e in TOWN["events"]:
    if e["t"]=="Time for Twos": e["when"]=[w for w in e["when"] if w["from"]!="2026-10-13"]
    if e["t"]=="Babytime":
        for w in e["when"]:
            if w["from"]=="2026-10-15": w["from"]="2026-10-14"
    if e["t"]=="Junior Chess Class": e["price"]="Free (full; waitlist only)"
GA="https://guilfordartcenter.org/classes/"
TOWN["events"]+=[
 {"t":"Bishop's Fall Festival","v":BO,"special":"fall","when":[{"from":"2026-10-08","to":"2026-11-01","t":[["10:00","17:00"]]}],"ages":"All ages","a":B+["big"],"free":False,"price":"$10–18 all-access (2 and under free)","drop":True,"src":"https://www.bishopsorchards.com/fall-festival",
  "blurb":"A 4-acre corn maze, bounce pads, gem mining, Tire Mountain and pedal karts, plus pick-your-own apples, pears and pumpkins. The Apple Train, Mega Slide and wagon rides run on weekends; cheaper on weekdays."},
 {"t":"CT Spooky Writing Contest","v":"guilford-library","special":"hw","when":[{"from":"2026-10-08","to":"2026-10-31","t":[]}],"ages":"Children's category ages 6–11","a":["big"],"free":True,"price":"Free","src":"https://guilfordfreelibrary.org/events/event/ct-spooky-writing-contest/",
  "blurb":"Write an original spooky story set in Connecticut and submit it online by Oct 31. Winners get a prize and are published in the library's Spooky CT volume."},
 {"t":"Kids' Magical Halloween Workshop","v":GAC,"special":"hw","when":[W("2026-10-24",[["12:30","15:00"]])],"ages":"Ages 5+","a":["preschool","big"],"free":False,"price":"$37.50 + $20 materials","rsvp":True,"src":GA+"kids-magical-halloween-workshop/",
  "blurb":"Clay and mixed-media spooky art: witches, animal familiars, luminaries and potions."},
 {"t":"Day of the Dead Workshop","v":GAC,"special":"hw","when":[W("2026-11-01",[["12:00","14:30"]])],"ages":"Ages 7+","a":["big"],"free":False,"price":"$37.50 + $15 materials","rsvp":True,"src":GA+"mexican-day-of-the-dead-workshop/",
  "blurb":"Make a clay skull luminary and decorate it with jewels, sequins and marigolds."},
 {"t":"Thanksgiving Harvest Baskets Workshop","v":GAC,"when":[W("2026-11-21",[["12:00","14:30"]])],"ages":"Ages 7+","a":["big"],"free":False,"price":"$37.50 + $20 materials","rsvp":True,"src":GA+"thanksgiving-harvest-baskets-workshop/",
  "blurb":"Kids make a clay cornucopia centerpiece with mini pumpkins, acorns and corn, plus a personalized placemat for the holiday table."},
]
TOWN["tba"]+=[
 {"g":"hol","t":"Santa's Workshop","w":"Guilford Community Center, 32 Church St","p":"Parks & Rec's photos with Santa, holiday crafts, pizza and dessert, the same Friday as the tree lighting ($35 per family, register ahead). Last year it was Dec 5, 4–5:30. This year's date isn't posted yet.","src":"https://new.patch.com/connecticut/guilford/calendar/event/20251205/20741e3f-91c3-45b6-a930-8e3ec62d8e1c/santas-workshop"},
 {"g":"hol","t":"Holiday Market at Dudley Farm","w":"Dudley Farm, 2351 Durham Rd, North Guilford","p":"A free market with 30+ artisans in the Munger Barn plus a paper-ornament craft in the decorated farmhouse, the first two weekends of December, 10–2. This year's dates aren't posted yet.","src":"https://ctvisit.com/events/holiday-market-dudley-farm"},
 {"g":"hol","t":"Fire & Ice Menorah Lighting","w":"Guilford Green","p":"Chabad of the Shoreline carves a giant ice menorah and dreidel on the Green, with donuts, cider and free menorahs. It happens during Hanukkah (Dec 4–12 this year); the date isn't posted yet.","src":"https://events.newhavenarts.org/events/fire-ice-menorah-lighting-on-the-guilford-green"},
 {"g":"hol","t":"Drop & Shop Art Workshops","w":"Guilford Art Center, 411 Church St","p":"Kids make art for two hours while parents shop the Holiday Expo ($25 per child, register ahead). Last year: Saturdays Dec 13 and 20, 12–2. This year's dates aren't posted yet.","src":"https://patch.com/connecticut/guilford/calendar/event/20251213/24c1aff4-8c29-402c-bdd1-84a445ccd349/guilford-art-center-helps-parents-check-off-holiday-lists-with-drop-shop-art-workshops"},
]
ES={
 "Free (full; waitlist only)":"Gratis (lleno; solo lista de espera)",
 "$10–18 all-access (2 and under free)":"$10–18 acceso total (2 años o menos gratis)",
 "A 4-acre corn maze, bounce pads, gem mining, Tire Mountain and pedal karts, plus pick-your-own apples, pears and pumpkins. The Apple Train, Mega Slide and wagon rides run on weekends; cheaper on weekdays.":"Un laberinto de maíz de 1.6 hectáreas, colchones inflables, búsqueda de gemas, Tire Mountain y karts de pedales, además de cosecha de manzanas, peras y calabazas. El Apple Train, el Mega Slide y los paseos en carreta funcionan los fines de semana; más barato entre semana.",
 "Children's category ages 6–11":"Categoría infantil 6–11 años",
 "Write an original spooky story set in Connecticut and submit it online by Oct 31. Winners get a prize and are published in the library's Spooky CT volume.":"Escribe un cuento de miedo original ambientado en Connecticut y envíalo en línea antes del 31 de oct. Los ganadores reciben un premio y se publican en el volumen Spooky CT de la biblioteca.",
 "Ages 5+":"5 años o más",
 "$37.50 + $20 materials":"$37.50 + $20 de materiales",
 "Clay and mixed-media spooky art: witches, animal familiars, luminaries and potions.":"Arte espeluznante con barro y técnicas mixtas: brujas, animales mágicos, farolitos y pociones.",
 "Ages 7+":"7 años o más",
 "$37.50 + $15 materials":"$37.50 + $15 de materiales",
 "Make a clay skull luminary and decorate it with jewels, sequins and marigolds.":"Haz un farolito de calavera de barro y decóralo con joyas, lentejuelas y cempasúchil.",
 "Kids make a clay cornucopia centerpiece with mini pumpkins, acorns and corn, plus a personalized placemat for the holiday table.":"Los niños hacen un centro de mesa de cornucopia de barro con minicalabazas, bellotas y maíz, además de un mantelito personalizado para la mesa festiva.",
 "Guilford Community Center, 32 Church St":"Guilford Community Center, 32 Church St",
 "Parks & Rec's photos with Santa, holiday crafts, pizza and dessert, the same Friday as the tree lighting ($35 per family, register ahead). Last year it was Dec 5, 4–5:30. This year's date isn't posted yet.":"Fotos con Santa, manualidades navideñas, pizza y postre de Parks & Rec, el mismo viernes del encendido del árbol ($35 por familia, con inscripción). El año pasado fue el 5 de dic., de 4 a 5:30. La fecha de este año aún no se ha publicado.",
 "Dudley Farm, 2351 Durham Rd, North Guilford":"Dudley Farm, 2351 Durham Rd, North Guilford",
 "A free market with 30+ artisans in the Munger Barn plus a paper-ornament craft in the decorated farmhouse, the first two weekends of December, 10–2. This year's dates aren't posted yet.":"Un mercado gratis con más de 30 artesanos en el Munger Barn y una manualidad de adornos de papel en la casa de la granja decorada, los dos primeros fines de semana de diciembre, de 10 a 2. Las fechas de este año aún no se han publicado.",
 "Guilford Green":"Guilford Green",
 "Chabad of the Shoreline carves a giant ice menorah and dreidel on the Green, with donuts, cider and free menorahs. It happens during Hanukkah (Dec 4–12 this year); the date isn't posted yet.":"Chabad of the Shoreline talla una menorá y un dreidel gigantes de hielo en el Green, con donas, sidra y menorás gratis. Es durante Janucá (del 4 al 12 de dic. este año); la fecha aún no se ha publicado.",
 "Guilford Art Center, 411 Church St":"Guilford Art Center, 411 Church St",
 "Kids make art for two hours while parents shop the Holiday Expo ($25 per child, register ahead). Last year: Saturdays Dec 13 and 20, 12–2. This year's dates aren't posted yet.":"Los niños hacen arte durante dos horas mientras los padres compran en el Holiday Expo ($25 por niño, con inscripción). El año pasado: sábados 13 y 20 de dic., de 12 a 2. Las fechas de este año aún no se han publicado.",
}
