# Round 3 finishing pass, Oct 8 2026
TH="stratford-town-hall"
TOWN["venues"][TH]=["Stratford Town Hall","2725 Main St"]; TOWN["venueMeta"][TH]=[None,0]
TOWN["tba"]=[x for x in TOWN["tba"] if x["t"]!="Stratford Menorah Lighting"]
TOWN["events"]+=[{"t":"Stratford Menorah Lighting","v":TH,"special":"hol","when":[{"from":"2026-12-09","t":[]}],"ages":"All ages","a":B+["big"],"free":True,"price":"Free","drop":True,"check":True,"src":"https://www.townofstratford.com/article/2802050",
  "blurb":"The town's Chanukah menorah lighting with music, dreidels, doughnuts, gelt and a prize for every child. Time and place aren't posted yet (last year: Town Hall at 6pm)."}]
ES_PATCH={"The town's Chanukah menorah lighting with music, dreidels, doughnuts, gelt and a prize for every child. Time and place aren't posted yet (last year: Town Hall at 6pm).":"El encendido de la menorá de Janucá del pueblo con música, dreidels, donas, monedas de chocolate y un premio para cada niño. Hora y lugar aún no publicados (el año pasado: Ayuntamiento a las 6 p. m.)."}
