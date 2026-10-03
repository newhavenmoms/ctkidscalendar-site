# Event sources — monthly check list

One place to see where each town's events come from, so re-checking and finding
new events is quick. Update the "Last checked" column whenever a source is reviewed.

## How to use this each month

1. Pick a town and open the **Check regularly** links.
2. Either send Claude the zip and say "monthly check for <town>" (Claude will go
   through these links and report what's new or changed), or paste in anything
   you found yourself.
3. For library calendars with a saved feed link, just say "re-import <town>".
4. Sources under **Worth adding** haven't been used yet — good places to look for
   more events.

Session dates matter: library storytimes often run in 4–8 week sessions, so a
monthly check catches new sessions before the old ones run out.

**Watch for same-name towns.** Research tools keep mixing in other states'
Cheshire, Milford and others. Any address without a Connecticut zip code
(06xxx) is a red flag.

This file is generated. Edit `tools/sources-curated.json` (the hand-picked lists),
then run `node tools/build-sources-md.js`. The "Also cited in your data" lists are
rebuilt from the site itself each time, so they stay accurate as events are added.


---

---

## Branford

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [James Blackstone Memorial Library — events](https://events.blackstonelibrary.org/) | Monthly. No feed link: click Filters → kids' age groups → List, then copy each page (Cmd+A) and paste to Claude. Several storytimes run only on selected weeks. | Sep 30, 2026 (imported Oct–Dec) |
| [Branford Parks & Recreation — programs list](https://branfordct.myrec.com/info/activities/) | Monthly. Check **Annual Special Events** (House Hunt, Goblin Giveaway, parade, Hanukkah, Easter egg hunt) and **Toddler/Youth Programs** (Early Start playgroup, Kids Night Out, swim). Some pages still show last year's details until the town updates them. | Sep 30, 2026 |
| [Willoughby Wallace Memorial Library (Stony Creek)](https://www.wwml.org/events) | Monthly. Mostly adult talks and concerts; watch for the monthly storytime, Collage & Crafts Club and family movies. Its calendar file link (saved in sources.json) may let Claude import it automatically. | Sep 30, 2026 |
| [Branford Land Trust — news & events](https://branfordlandtrust.org/blog/) | Before Thanksgiving and in December: Van Wie Walk (Sunday before Thanksgiving) and New Year's Day hike. | Sep 30, 2026 |
| [Legacy Theatre — tickets](https://www.tix.com/ticket-sales/legacytheatrectcal/6430) | Every couple of months: family series, holiday show ('Tis the Season, Dec 9–20). Don't confuse with Legacy Theatres in Pittsburgh or Las Vegas. | Sep 30, 2026 |
| [Shore Line Trolley Museum — events](https://events.humanitix.com/host/the-shore-line-trolley-museum) | Each season: Pumpkin Patch Trolley (Oct), Santa/holiday trolleys, storytime and sensory-friendly days. East Haven, but a Branford family favorite. | Sep 30, 2026 |
| [Branford Historical Society — events](https://branfordhistoricalsociety.org/events/) | November: holiday open house date. Harrison House tours are summer Saturdays only. | Sep 30, 2026 |

**Also cited in your data** (8 more site(s), busiest first)

- [blackstonelibrary.org](https://www.blackstonelibrary.org/) — 16 event(s)
- [allevents.in](https://allevents.in/branford-ct/all) — 1 event(s)
- [patch.com](https://patch.com/connecticut/branford) — 1 event(s)
- [legacytheatrect.org](https://www.legacytheatrect.org/classes) — 1 class card(s)
- [musicalfolk.com](https://www.musicalfolk.com/OurClasses.html) — 1 class card(s)
- [ymca.org](https://www.ymca.org/locations/soundview-family-ymca) — 1 class card(s)
- [danceunlimitedcrew.com](https://www.danceunlimitedcrew.com/) — 1 class card(s)
- [shiningstarzacrodanceacademyct.com](https://shiningstarzacrodanceacademyct.com/) — 1 class card(s)

---

## Cheshire

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Cheshire Public Library — calendar feed](https://cheshirelibrary.libcal.com/ical_subscribe.php?src=p&cid=1860) | Monthly. Open the link (a calendar file downloads) and send it to Claude, or ask Claude to re-import. Storytimes, STEAM labs, teen programs. | Sep 30, 2026 |
| [Cheshire Parks & Rec, Artsplace, Pool & Youth Services — programs list](https://cheshirect.myrec.com/info/activities/default.aspx) | Monthly, and when new seasons open (Jan, Apr, Sept). One-off events (Halloween Bash, Turkey Hunt, cookie decorating) and class schedules. | Sep 30, 2026 |
| [Same site — facility calendar](https://cheshirect.myrec.com/info/calendar/list.aspx?FacilityID=0&AreaID=0) | Optional skim. Only shows a few days; mostly team practices and rentals. Good for spotting new Youth Services one-offs. | Sep 30, 2026 |
| [Cheshire Historical Society](https://www.cheshirehistory.org/) | Every month or two. House museum open 2nd & 4th Sundays (exceptions are posted as an image on the home page). Spirits Alive cemetery tour each October. | Sep 30, 2026 |
| [Cheshire Land Trust](https://www.cheshirelandtrust.org/) | Before Thanksgiving and in December. Hike dates are in the newsletter PDF and on [Facebook](https://www.facebook.com/CheshireLandTrustCT/) — Claude can't read those, so check by eye. | Sep 30, 2026 |

**Worth adding** (not used yet)

- [Cheshire Public Schools community bulletin board](https://www.cheshire.k12.ct.us/for-parents/community-bulletin-board/) — Flyers for community events (pumpkin patch day, fun runs).
- [Cheshire Patch](https://patch.com/connecticut/cheshire) — Local news roundups of weekend events.

**Don't confuse with**

- Cheshire, **Massachusetts** (cheshirepubliclibrary.org) — a different library with a Tuesday 11am storytime that keeps showing up in research.
- Historical Society of **Cheshire County** — that's Keene, New Hampshire.

**Also cited in your data** (11 more site(s), busiest first)

- [cheshirelibrary.org](https://www.cheshirelibrary.org/events) — 1 event(s)
- [cheshire.k12.ct.us](https://www.cheshire.k12.ct.us/for-parents/community-bulletin-board/) — 1 event(s)
- [oldbishopfarms.com](https://www.oldbishopfarms.com/) — 1 event(s)
- [jbsports.com](https://www.jbsports.com/) — 1 event(s)
- [musicalfolk.com](https://www.musicalfolk.com/Cheshire.html) — 1 class card(s)
- [communityplayatelier.com](https://communityplayatelier.com/programs) — 1 class card(s)
- [catsgymnastics.com](https://www.catsgymnastics.com/) — 1 class card(s)
- [cheshiredancecentre.com](https://www.cheshiredancecentre.com/dances-we-teach) — 1 class card(s)
- [thecoderschool.com](https://www.thecoderschool.com/locations/cheshire/) — 1 class card(s)
- [cheshiresoccerclub.org](https://www.cheshiresoccerclub.org/Default.aspx?tabid=1356669) — 1 class card(s)
- [pack114.org](https://www.pack114.org/) — 1 class card(s)

---

## Darien

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Darien Library — events](https://www.darienlibrary.org/events/upcoming) | Monthly: storytimes, specials, school-break programs. | Oct 3, 2026 |
| [Darien Nature Center](https://www.dariennaturecenter.org/) | Monthly: programs, fall and holiday events. | Oct 3, 2026 |
| [Darien Arts Center — class catalog](https://register.darienarts.org/CourseCatalog/CatalogView.asp?ID=72) | Each season: classes. No public kids' shows in fall 2026. | Oct 3, 2026 |
| [Darien Parks & Recreation](https://www.darienct.gov/202/Parks-Recreation) | Seasonal brochure and town events. | Oct 3, 2026 |
| [Museum of Darien](https://museumofdarien.org/) | Holiday and family events. | Oct 3, 2026 |

**Also cited in your data** (7 more site(s), busiest first)

- [darien-ymca.org](https://darien-ymca.org/child-care/summer-camp/) — 1 event(s), 13 class card(s)
- [newcanaandarienmoms.com](https://newcanaandarienmoms.com/calendar/) — 1 event(s)
- [darienschoolofdance.com](https://darienschoolofdance.com/) — 1 class card(s)
- [dariensoccer.org](https://dariensoccer.org/) — 1 class card(s)
- [darienlittleleague.com](https://www.darienlittleleague.com/) — 1 class card(s)
- [darienyouthlacrosse.org](https://www.darienyouthlacrosse.org/) — 1 class card(s)
- [djfl.org](https://www.djfl.org/) — 1 class card(s)

---

## Fairfield

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Fairfield Public Library (Main + Fairfield Woods)](https://fplct.librarymarket.com/) | Monthly. LibraryMarket: filter Preschool + Children, list view, Paste the kids-filtered list view (blocks automated reading). Last full paste Oct 3. | Oct 3, 2026 |
| [Pequot Library — calendar](https://www.pequotlibrary.org/calendar/) | Monthly (Southport). | Oct 3, 2026 |
| [Fairfield Museum & History Center — events](https://www.fairfieldhistory.org/events-calendar/month/) | Monthly; Halloween on the Green (late Oct). | Oct 3, 2026 |
| [Quick Center for the Arts (Fairfield University)](https://quickcenter.fairfield.edu/) | When the season is announced: family series (Feb and Mar 2027 shows listed). | Oct 3, 2026 |
| [CT Audubon — Fairfield Nature Center](https://ctaudubon.org/locations/the-fairfield-nature-center-and-larsen-sanctuary/) | Each season: programs. | Oct 3, 2026 |
| [Fairfield Parks & Recreation](https://fairfieldct.org/) | Seasonal programs and town events. | Oct 3, 2026 |

**Also cited in your data** (26 more site(s), busiest first)

- [fairfieldtheatreacademy.org](https://fairfieldtheatreacademy.org/classes-2026/) — 23 class card(s)
- [fairfieldareaswimschool.com](https://www.fairfieldareaswimschool.com/springservices) — 5 class card(s)
- [ffldcommunity.com](https://ffldcommunity.com/farmer_s_market/index.php) — 1 event(s), 3 class card(s)
- [fairfieldctmoms.com](https://fairfieldctmoms.com/resources/activities-and-classes/) — 4 class card(s)
- [ctdanceschool.org](https://www.ctdanceschool.org/) — 1 event(s), 2 class card(s)
- [fairfieldskatingclub.com](https://fairfieldskatingclub.com/) — 3 class card(s)
- [cccymca.org](https://cccymca.org/locations/fairfield/swim/) — 3 class card(s)
- [fairfieldpubliclibrary.org](https://fairfieldpubliclibrary.org/children/family-events-and-afterschool-classes/) — 3 class card(s)
- [nstudios.org](https://www.nstudios.org/register.html) — 3 class card(s)
- [edgertoncenter.org](https://edgertoncenter.org/events/sam-the-snowman/) — 2 event(s)
- [wow-swim.com](https://wow-swim.com/) — 2 class card(s)
- [fairfieldskatingclub.org](https://www.fairfieldskatingclub.org/) — 2 class card(s)
- [fairfield.kidstrong.com](https://fairfield.kidstrong.com/) — 2 class card(s)
- [mygym.com](https://www.mygym.com/fairfield) — 2 class card(s)
- [events.fairfield.edu](https://events.fairfield.edu/event/childrens-storytime-in-the-fairfield-forest-1972) — 1 event(s)
- [commerce.fairfieldctchamber.com](https://commerce.fairfieldctchamber.com/events/details/fairfield-harvest-market-fall-2026-6641) — 1 event(s)
- [mofflylifestylemedia.com](https://mofflylifestylemedia.com/fairfield-county-holiday-market-pop-up-guide/) — 1 event(s)
- [ctfairfieldweb.myvscloud.com](https://ctfairfieldweb.myvscloud.com/webtrac/web/search.html?module=AR&type=Camps%20and%20Clinics) — 1 class card(s)
- [creativefamilyrhythms.com](https://www.creativefamilyrhythms.com/music-together-mixed-ages.html?sem0=54068) — 1 class card(s)
- [fairfieldperformingartsstudio.com](https://www.fairfieldperformingartsstudio.com/) — 1 class card(s)
- [breakalegct.com](https://breakalegct.com/) — 1 class card(s)
- [shucommunitytheatre.org](https://shucommunitytheatre.org/) — 1 class card(s)
- [sunnyfieldstudio.net](https://www.sunnyfieldstudio.net/) — 1 class card(s)
- [dvaldaandsirico.com](https://www.dvaldaandsirico.com/) — 1 class card(s)
- [flashpointedance.com](https://www.flashpointedance.com/) — 1 class card(s)
- [bricksandminifigs.com](https://bricksandminifigs.com/fairfield-ct/) — 1 class card(s)

---

## Glastonbury

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Welles-Turner Memorial Library — kids' events list](https://wtmlib.librarycalendar.com/events/list?age_groups%5B59%5D=59&age_groups%5B143%5D=143&age_groups%5B58%5D=58) | Monthly. This link is already filtered to kids' age groups: copy each page and paste to Claude. Session storytimes fill by lottery each September (and likely January); watch for new sessions. | Sep 30, 2026 (imported Oct–Dec) |
| [Glastonbury Parks & Rec — programs list](https://glastonburyct.myrec.com/info/activities/default.aspx?type=activities) | Monthly, and when seasons open (registration days fill fast). Family Programs, Holiday Programs and Pre-School categories: Story Stroll, Santa's Underwater Adventure, Festive Driving Tour, Kids Night Out, playgroup. | Sep 30, 2026 |
| [Santa's Run](https://www.glastonburyct.gov/departments/department-directory-i-z/parks-and-recreation/santa-s-run) | Each October: date and registration (Dec 6 this year). | Sep 30, 2026 |
| [Apple Harvest & Music Festival](https://www.eventbrite.com/e/2026-glastonbury-apple-harvest-and-music-festival-tickets-1994245146918) | Each summer: next year's dates (CT River Valley Chamber). Don't confuse with England's Glastonbury Festival. | Sep 30, 2026 |
| [Historical Society of Glastonbury — events](https://hsgct.org/events/) | Every month or two: Thanksgiving Celebration and other family events. Has a calendar feed (saved in sources.json). | Sep 30, 2026 |
| [Glastonbury farms list (town)](https://www.glastonburyct.gov/departments/department-directory-a-h/health/better-health-initiatives/glastonbury-farms-and-resources) | Each spring and fall: pick-your-own seasons, hayrides, corn mazes. | Sep 30, 2026 |
| [Youth & Family Services — theater productions](https://www.glastonburyct.gov/departments/department-directory-i-z/youth-and-family-services/creative-experiences/theatrical-productions/upcoming-theater-productions-y-fs) | Each season: kid-cast musicals (Charlie Brown, Nov 5–7). | Oct 3, 2026 |

**Worth adding** (not used yet)

**Also cited in your data** (0 more site(s), busiest first)


---

## Greenwich

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Greenwich Library — children](https://www.greenwichlibrary.org/children/) | Monthly; storytimes run by lottery registration. | Oct 3, 2026 |
| [Perrot Library (Old Greenwich) — children's programs](https://perrotlibrary.org/youth-services/current-childrens-programs/) | Monthly. | Oct 3, 2026 |
| [Bruce Museum — events](https://www.brucemuseum.org/events/) | Monthly. | Oct 3, 2026 |
| [Greenwich Historical Society — events](https://greenwichhistory.org/ghs-events/) | Monthly: Fall Harvest Festival (Oct), Holiday Festival (early Dec). | Oct 3, 2026 |
| [Greenwich Arts Council — events](https://www.greenwichartscouncil.org/events) | Monthly: author visits, workshops. | Oct 3, 2026 |
| [Town of Greenwich — special events](https://www.greenwichct.gov/493/Special-Events-Concerts) | Seasonal town events. | Oct 3, 2026 |
| [Greenwich Botanical Center — children's programs](https://greenwichbotanicalcenter.org/childrens-programs/) | Each season. | Oct 3, 2026 |

**Also cited in your data** (18 more site(s), busiest first)

- [greenwichmoms.com](https://www.greenwichmoms.com/) — 2 event(s), 28 class card(s)
- [greenwichymca.org](https://greenwichymca.org/programs/youth/sports-art-enrichment/) — 13 class card(s)
- [ywcagreenwich.org](https://ywcagreenwich.org/) — 3 event(s), 6 class card(s)
- [make-modern.com](https://www.make-modern.com/locations/greenwich) — 6 class card(s)
- [greenwichartsociety.org](https://www.greenwichartsociety.org/) — 5 event(s)
- [greenwichlibrary.libcal.com](https://greenwichlibrary.libcal.com/calendar/events) — 4 event(s), 1 class card(s)
- [gltrust.org](https://gltrust.org/event/go-wild-2026/) — 1 event(s), 3 class card(s)
- [greenwichdancestudio.com](https://greenwichdancestudio.com/) — 4 class card(s)
- [danceadventure.com](https://danceadventure.com/) — 4 class card(s)
- [stsavdance.com](https://www.stsavdance.com/) — 4 class card(s)
- [patch.com](https://patch.com/connecticut/greenwich/calendar/event/20260903/9bee9d3f-0cc8-4feb-9fb0-4ce820439a22/open-arts-alliance-fall-2026-season) — 2 event(s)
- [greenwichfarmersmarketct.com](https://www.greenwichfarmersmarketct.com/) — 1 event(s)
- [cityeventsct.com](https://www.cityeventsct.com/events/og-farmers-market-2026) — 1 event(s)
- [abilis.us](https://www.abilis.us/) — 1 event(s)
- [greenwichtownparty.org](https://www.greenwichtownparty.org/) — 1 event(s)
- [gcyha.net](https://www.gcyha.net/) — 1 class card(s)
- [bgcg.org](https://bgcg.org/what-we-do/after-school-programs/) — 1 class card(s)
- [foodshednetwork.org](https://foodshednetwork.org/) — 1 class card(s)

---

## Middletown

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Russell Library — calendar](https://russelllibrary.librarycalendar.com/) | Monthly. LibraryCalendar: blocks automated reading, so paste the kids-filtered list view. Last full paste Oct 3. | Oct 3, 2026 |
| [City of Middletown calendar](https://middletownct.gov/calendar.aspx?CID=119) | Blocks automated reading; use only if pasted. | Oct 3, 2026 |
| [Middletown Recreation (MyRec)](https://middletownct.myrec.com/info/activities/default.aspx) | Monthly: classes, Van Vleck Kids' Nights, Downtown Trick or Treat. Detail pages often cached; search snippets show live dates. | Oct 3, 2026 |
| [Wesleyan RJ Julia — events](https://rjjulia.com/upcoming-events) | Monthly: Sunday 11am storytime. | Oct 3, 2026 |
| [Wadsworth Mansion — public events](https://www.wadsworthmansion.com/mec-category/public-events/) | Seasonal: Nutcracker (Nov 22), New Year's open house. | Oct 3, 2026 |
| [Oddfellows Playhouse](https://www.oddfellows.org/) | Each season: shows, costume sale (Oct). | Oct 3, 2026 |
| [Middlesex Chamber — Holiday on Main Street](https://www.middlesexchamber.com/holiday-on-main-street/) | Early November: confirm tree lighting dates. | Oct 3, 2026 |

**Also cited in your data** (1 more site(s), busiest first)

- [midymca.org](https://www.midymca.org/) — 1 class card(s)

---

## Milford

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Milford Public Library — calendar](https://milford-pl.libcal.com/calendar/children) | Monthly. LibCal children's calendar: paste the list (or iCal). Parking limited Oct–Dec. | Oct 3, 2026 |
| [Walnut Beach Arts & Business — events](https://walnutbeachartsandbusiness.com/our-events) | Monthly in fall/winter: Boo Fest, Witch Parade, tree lighting. | Sep 29, 2026 |
| [Downtown Milford Business Association](https://downtownmilfordct.com/) | Hall-O-Weekend, farmers market, holiday events. 2026 Hall-O-Weekend schedule not posted yet. | Sep 29, 2026 |
| [Milford Makes — upcoming](https://milfordmakes.org/upcoming/) | Every month or two; mostly adult, occasional free kids' workshops. | Sep 30, 2026 |
| [Milford Recreation (MyRec)](https://milfordct.myrec.com/info/activities/default.aspx) | When seasons open. Classes, adaptive (MAPs) programs. | Sep 29, 2026 |
| [Milford Arts Council (the MAC)](https://milfordarts.org/) | Monthly: Family Pillow Concerts; Pantochino's December musical. | Oct 3, 2026 |
| [Pantochino Productions](http://www.pantochino.com/) | October–November: holiday musical title and dates. | Oct 3, 2026 |

**Don't confuse with**

- Milford, **New Hampshire** — its Pumpkin Festival (milfordpumpkinfestival.org, 'Granite Town') is not ours.

**Also cited in your data** (18 more site(s), busiest first)

- [bridgesct.org](https://bridgesct.org/folks-on-spokes/) — 1 event(s)
- [connecticutfestivals.com](https://connecticutfestivals.com/Milford-CT) — 1 event(s)
- [findarace.com](https://findarace.com/us/events/15th-annual-milford-5k-trick-or-trot-run-walk) — 1 event(s)
- [stores.barnesandnoble.com](https://stores.barnesandnoble.com/store/2240) — 1 event(s)
- [facebook.com](https://www.facebook.com/MilfordLL/) — 1 event(s)
- [ctaudubon.org](https://www.ctaudubon.org/coastal-center-at-milford-point/) — 1 class card(s)
- [musicalfolk.com](https://www.musicalfolk.com/MilfordOrange.html) — 1 class card(s)
- [thegigglingpig.com](https://www.thegigglingpig.com/milford-tgp) — 1 class card(s)
- [gcaofct.com](https://gcaofct.com/milford/schedules/) — 1 class card(s)
- [milfordice.com](https://www.milfordice.com/) — 1 class card(s)
- [leelundstudioofdance.com](https://www.leelundstudioofdance.com/junior-classes) — 1 class card(s)
- [schoolofrock.com](https://www.schoolofrock.com/locations/milford) — 1 class card(s)
- [cccymca.org](https://cccymca.org/locations/woodruff-family-ymca/) — 1 class card(s)
- [milfordcommunityprogram.activityreg.com](https://milfordcommunityprogram.activityreg.com/selectactivity_t2.wcs) — 1 class card(s)
- [app.gostudiopro.com](https://app.gostudiopro.com/online/classes.php?account_id=34044) — 1 class card(s)
- [boysandgirlsclubofmilford.com](https://boysandgirlsclubofmilford.com/enrichment-programs/) — 1 class card(s)
- [pack7milford.org](https://pack7milford.org/aboutus.php) — 1 class card(s)
- [milfordyouthlacrosse.org](https://www.milfordyouthlacrosse.org/signup) — 1 class card(s)

---

## New Canaan

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [New Canaan Library — events](https://www.newcanaanlibrary.org/events/month) | Monthly. | Oct 3, 2026 |
| [New Canaan Nature Center — events](https://newcanaannature.org/events/) | Monthly. | Oct 3, 2026 |
| [Grace Farms — children & families](https://gracefarms.org/events/category/children-families/list) | Monthly. | Oct 3, 2026 |
| [Town Players of New Canaan](https://tpnc.org/) | Each season: Rudolph (Nov 20–Dec 13). | Oct 3, 2026 |
| [New Canaan Chamber — annual events](https://newcanaanchamber.com/annual-events/) | Seasonal: holiday stroll, Halloween. | Oct 3, 2026 |

**Also cited in your data** (25 more site(s), busiest first)

- [newcanaanymca.org](https://newcanaanymca.org/) — 1 event(s), 10 class card(s)
- [newcanaanct.gov](https://www.newcanaanct.gov/) — 6 class card(s)
- [carriagebarn.org](https://carriagebarn.org/) — 2 class card(s)
- [performingartsconservatory.com](https://www.performingartsconservatory.com/) — 2 class card(s)
- [schoolofrock.com](https://www.schoolofrock.com/locations/newcanaan) — 2 class card(s)
- [newcanaandarienmoms.com](https://newcanaandarienmoms.com/calendar/category/family/) — 1 class card(s)
- [nchistory.org](https://nchistory.org/) — 1 class card(s)
- [musicologie.com](https://musicologie.com/locations/new-canaan/) — 1 class card(s)
- [neadance.com](https://neadance.com/) — 1 class card(s)
- [craftykidsnewcanaan.com](https://craftykidsnewcanaan.com/) — 1 class card(s)
- [elmstreetbooks.com](https://elmstreetbooks.com/) — 1 class card(s)
- [campplayland.com](https://campplayland.com/) — 1 class card(s)
- [newcanaansoccer.org](https://newcanaansoccer.org/) — 1 class card(s)
- [newcanaanbaseball.com](https://www.newcanaanbaseball.com/) — 1 class card(s)
- [newcanaanyouthfootball.org](https://www.newcanaanyouthfootball.org/) — 1 class card(s)
- [ncyouthlacrosse.org](https://www.ncyouthlacrosse.org/) — 1 class card(s)
- [newcanaanfieldhockey.com](https://www.newcanaanfieldhockey.com/) — 1 class card(s)
- [newcanaancares.org](https://newcanaancares.org/) — 1 class card(s)
- [newcanaancf.org](https://www.newcanaancf.org/) — 1 class card(s)
- [newcanaanlandtrust.org](https://newcanaanlandtrust.org/) — 1 class card(s)
- [newcanaanmountedtroop.org](https://newcanaanmountedtroop.org/) — 1 class card(s)
- [ncps-k12.org](https://www.ncps-k12.org/) — 1 class card(s)
- [stmarksnewcanaan.org](https://www.stmarksnewcanaan.org/) — 1 class card(s)
- [fpcnc.org](https://fpcnc.org/) — 1 class card(s)
- [umcofnewcanaan.org](https://umcofnewcanaan.org/) — 1 class card(s)

---

## New Haven

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [New Haven Free Public Library (5 branches)](https://nhfpl.libcal.com/calendar) | Monthly. LibCal: filter Ages 0–5, 6–11, Family; paste the list. Last full paste Oct 3. | Oct 3, 2026 |
| [Shubert Theatre — events](https://www.shubert.com/) | Each season: family shows; library workshops tie in. | Oct 3, 2026 |
| [Yale Peabody Museum — events](https://peabody.yale.edu/events) | Monthly. | Oct 3, 2026 |
| [Blessed Michael McGivney Pilgrimage Center (formerly KofC Museum)](https://www.kofcmuseum.org/kms/en/index.html) | November: Christmas crèche exhibit dates. | Oct 3, 2026 |
| [Ralph Walker Rink (Elm City Sports Group)](https://www.ralphwalkericerink.com/public-skate) | October–March: public skate sessions. New operator as of Sep 2026. | Oct 3, 2026 |

**Also cited in your data** (24 more site(s), busiest first)

- [commongroundct.org](https://www.commongroundct.org/calendar/open-farm-day) — 2 event(s), 1 class card(s)
- [creativeartsworkshop.org](https://creativeartsworkshop.org/courses/no-term/art-with-you-and-me/) — 2 event(s), 1 class card(s)
- [cityseed.org](https://www.cityseed.org) — 2 event(s)
- [theshopsatyale.com](https://theshopsatyale.com/chalkart/) — 2 event(s)
- [eventbrite.com](https://www.eventbrite.com/e/2nd-annual-faith-family-fall-festival-tickets-1993959908763) — 2 event(s)
- [nmsnewhaven.org](https://nmsnewhaven.org/music-classes) — 2 class card(s)
- [newhavenballet.org](https://newhavenballet.org/programs-tuition/programs-tuition-childrens/) — 2 class card(s)
- [downtownnewhaven.com](https://www.downtownnewhaven.com/movies) — 1 event(s)
- [barcade.com](https://barcade.com/familyday) — 1 event(s)
- [childrensbuilding.org](https://www.childrensbuilding.org/new-home) — 1 event(s)
- [pebblestoys.com](https://pebblestoys.com/pages/contact) — 1 event(s)
- [trinitynewhaven.org](https://www.trinitynewhaven.org/children-youth-and-family-ministry-events) — 1 event(s)
- [cpcnewhaven.org](https://cpcnewhaven.org/sundays.html) — 1 event(s)
- [britishart.yale.edu](https://britishart.yale.edu/exhibitions-programs/make-time-see-touch-landscapes) — 1 event(s)
- [newhavenmuseum.org](https://www.newhavenmuseum.org/free-first-sunday/) — 1 event(s)
- [visitnewhaven.com](https://visitnewhaven.com/events/new-haven-grand-prix/) — 1 event(s)
- [ctfolk.org](https://www.ctfolk.org/) — 1 event(s)
- [musicalfolk.com](https://www.musicalfolk.com/OurClasses.html) — 1 class card(s)
- [musichavenct.org](https://www.musichavenct.org/) — 1 class card(s)
- [leapforkids.org](https://www.leapforkids.org/swimming) — 1 class card(s)
- [bulldogswimacademy.com](https://bulldogswimacademy.com/) — 1 class card(s)
- [newhavenct.gov](https://www.newhavenct.gov/government/departments-divisions/youth-and-recreation-department/recreation) — 1 class card(s)
- [soccersquirts.com](https://soccersquirts.com/ct/1175-new-haven-preschool-kindergarten-childrens-soccer-classes-activities) — 1 class card(s)
- [yalechildrenstheater.org](https://yalechildrenstheater.org/) — 1 class card(s)

---

## Newtown

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [EverWonder Children's Museum](https://www.everwondermuseum.org/) | Monthly. Story Lab days, early-dismissal programs. | Sep 29, 2026 |
| [C.H. Booth Library](https://www.chboothlibrary.org/) | Monthly. LibCal calendar loads by script, so paste the kids-filtered list view. Baby/toddler sessions end in October. | Oct 2, 2026 |
| [Newtown Parks & Rec — seasonal brochure](https://www.newtown-ct.gov/parks-recreation) | Each season (PDF): classes and town events. | Oct 3, 2026 |
| [Edmond Town Hall — box office](https://edmondtownhall.showare.com/) | Monthly: family shows and kids' workshops. | Oct 3, 2026 |
| [Newtown Youth & Family Services — Holiday Festival](https://www.newtownyouthandfamilyservices.org/) | November: festival tickets (Dec 6). | Oct 3, 2026 |
| [Newtown Historical Society (Matthew Curtiss House)](https://newtownhistory.org/) | Spring and fall open houses. | Oct 3, 2026 |
| [The Newtown Bee](https://www.newtownbee.com/) | Weekly: tree lightings, Halloween, local events. | Oct 3, 2026 |

**Also cited in your data** (7 more site(s), busiest first)

- [chboothlibrary.libcal.com](https://chboothlibrary.libcal.com/calendar?cid=20981&t=d&cal%5B%5D=20981) — 14 event(s)
- [newtowncommunitycenter.org](https://newtowncommunitycenter.org/) — 1 event(s), 1 class card(s)
- [halloweenonmain.com](https://www.halloweenonmain.com/) — 1 event(s)
- [simpletix.com](https://www.simpletix.com/e/jack-o-lantern-jamboree-2026-tickets-295051) — 1 event(s)
- [swct.soccershots.com](https://swct.soccershots.com/) — 1 class card(s)
- [fairfieldcountytennis.net](https://www.fairfieldcountytennis.net/) — 1 class card(s)
- [teamunify.com](https://www.teamunify.com/team/nent/page/home) — 1 class card(s)

---

## Norwalk

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Norwalk Public Library — Main children's (.ics)](https://www.norwalkpl.org/common/modules/iCalendar/iCalendar.aspx?catID=25&feed=calendar) | Monthly. CivicPlus: download .ics and run the importer; descriptions are empty, so write blurbs by hand. | Oct 3, 2026 |
| [Norwalk Public Library — South Norwalk Branch (.ics)](https://www.norwalkpl.org/calendar.aspx) | Monthly. Branch calendar mixes adult and private bookings. | Oct 3, 2026 |
| [Norwalk Recreation & Parks](https://www.norwalkct.gov/) | Seasonal brochure and town events. | Oct 3, 2026 |
| [Stepping Stones Museum for Children](https://www.steppingstonesmuseum.org/) | Monthly. | Oct 3, 2026 |
| [Maritime Aquarium](https://www.maritimeaquarium.org/) | Monthly. | Oct 3, 2026 |
| [Crystal Theatre](https://www.crystaltheatre.org/) | Each season: kid-cast shows (homepage lists dates). | Oct 3, 2026 |
| [Music Theatre of Connecticut — student productions](https://www.musictheatreofct.com/fall-spring-programs) | Each season. | Oct 3, 2026 |
| [Norwalk Historical Society / Mill Hill](https://norwalkhistoricalsociety.org/visit/) | Seasonal events. | Oct 3, 2026 |

**Also cited in your data** (28 more site(s), busiest first)

- [thenorwalkartspace.org](https://www.thenorwalkartspace.org/education) — 9 class card(s)
- [fliphtml5.com](https://fliphtml5.com/qmsjn/kpqu/) — 3 event(s), 4 class card(s)
- [rowayton.org](https://www.rowayton.org/events/upcoming) — 4 event(s)
- [seaport.org](https://www.seaport.org/norwalk-oyster-festival) — 2 event(s), 2 class card(s)
- [stmatthewnorwalk.org](https://stmatthewnorwalk.org/youth-group/) — 3 event(s), 1 class card(s)
- [tumblejungle.com](https://tumblejungle.com/) — 4 class card(s)
- [dev.skyzone.com](https://dev.skyzone.com/norwalk/) — 4 class card(s)
- [stewietheduck.org](https://stewietheduck.org/pricing/) — 3 class card(s)
- [visitnorwalk.org](https://www.visitnorwalk.org/events-in-norwalk/sono-saturday-market/) — 2 event(s)
- [lockwoodmathewsmansion.com](https://lockwoodmathewsmansion.com/event/ghosts-spirits-at-the-mansion/) — 1 event(s), 1 class card(s)
- [ctpridecenter.org](https://www.ctpridecenter.org/caregiver-mixer) — 1 event(s), 1 class card(s)
- [norwalklib.org](https://www.norwalklib.org/calendar.aspx?CID=25) — 1 event(s), 1 class card(s)
- [goldfishswimschool.com](https://goldfishswimschool.com/norwalk/pricing/additional-program/) — 2 class card(s)
- [sonoicehouse.com](https://www.sonoicehouse.com/) — 2 class card(s)
- [norwalk.kidstrong.com](https://norwalk.kidstrong.com/) — 2 class card(s)
- [norwalksymphony.org](https://www.norwalksymphony.org/20262027) — 1 event(s)
- [norwalkartscenter.org](https://www.norwalkartscenter.org/) — 1 event(s)
- [njsa.org](https://njsa.org/) — 1 class card(s)
- [childrenofthesound.com](https://www.childrenofthesound.com/) — 1 class card(s)
- [stewleonards.com](https://www.stewleonards.com/) — 1 class card(s)
- [content.govdelivery.com](https://content.govdelivery.com/accounts/IANORWALK/bulletins/424dc4f) — 1 class card(s)
- [shakespeareonthesound.org](https://www.shakespeareonthesound.org/kids-show) — 1 class card(s)
- [chalkct.com](https://www.chalkct.com/) — 1 class card(s)
- [playhouse-sono.gymdesk.com](https://playhouse-sono.gymdesk.com/) — 1 class card(s)
- [velo-ct.com](https://velo-ct.com/) — 1 class card(s)
- [norwalkacademyofdance.com](https://www.norwalkacademyofdance.com/) — 1 class card(s)
- [thedancecollectivect.com](https://www.thedancecollectivect.com/) — 1 class card(s)
- [justdancestudios.com](https://www.justdancestudios.com/) — 1 class card(s)

---

## Ridgefield

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Ridgefield Library — events](https://ridgefieldlibrary.librarymarket.com/) | Monthly. LibraryMarket: paste the kids-filtered list. | Oct 3, 2026 |
| [Ridgefield Parks & Recreation](https://www.ridgefieldparksandrec.org/) | Seasonal programs and events. | Oct 3, 2026 |
| [The Ridgefield Playhouse](https://ridgefieldplayhouse.org/) | Each season: family series. | Oct 3, 2026 |
| [inRidgefield — events](https://inridgefield.com/) | Monthly: town traditions (Halloween walk, holidays). | Oct 3, 2026 |
| [The Aldrich — Third Saturdays](https://thealdrich.org/) | Monthly. | Oct 3, 2026 |
| [Keeler Tavern Museum — events](https://keelertavernmuseum.org/events/calendar/) | Monthly. | Oct 3, 2026 |
| [Woodcock Nature Center](https://www.woodcocknaturecenter.org/upcomingevents) | Monthly. | Oct 3, 2026 |

**Also cited in your data** (18 more site(s), busiest first)

- [ridgefielddance.org](https://www.ridgefielddance.org/calendar/) — 5 class card(s)
- [actofct.org](https://www.actofct.org/youth-choir) — 4 class card(s)
- [friendsofweirfarm.org](https://friendsofweirfarm.org/events/) — 3 event(s)
- [wayofthesword.org](https://wayofthesword.org/) — 3 class card(s)
- [enchantedgardenstudios.com](https://www.enchantedgardenstudios.com/) — 3 class card(s)
- [ridgefieldschoolofdance.com](https://www.ridgefieldschoolofdance.com/) — 1 event(s), 1 class card(s)
- [ridgefieldacademy.org](https://www.ridgefieldacademy.org/community/parentresources/after-school-enrichment-clubs) — 2 class card(s)
- [littlesproutsplayplace.com](https://www.littlesproutsplayplace.com/) — 2 class card(s)
- [ridgefieldfarmersmarket.org](https://www.ridgefieldfarmersmarket.org/) — 1 event(s)
- [ridgefieldmom.com](https://ridgefieldmom.com/calendar/2026-04-25/) — 1 event(s)
- [ridgefieldpubliclibrary.com](https://www.ridgefieldpubliclibrary.com/children-programs) — 1 event(s)
- [rgoa.org](https://rgoa.org/course/joy-of-art-fall-2026/) — 1 class card(s)
- [landmarkpreschool.org](https://www.landmarkpreschool.org/fun-for-ones) — 1 class card(s)
- [scor.org](https://www.scor.org/Default.aspx?tabid=927299) — 1 class card(s)
- [rbahoops.com](https://rbahoops.com/clinics/) — 1 class card(s)
- [ridgefieldtheaterbarn.org](https://ridgefieldtheaterbarn.org/rtbk-workshops/rtbk-playmakers-lab/) — 1 class card(s)
- [dancefactoryridgefield.com](https://www.dancefactoryridgefield.com/) — 1 class card(s)
- [thelittlegym.com](https://www.thelittlegym.com/ridgefieldct) — 1 class card(s)

---

## Stamford

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Ferguson Library (5 branches)](https://www.fergusonlibrary.org/events/list) | Monthly. Paste the kids-filtered list; storytimes run in monthly sessions with registration. Last full paste Oct 3. | Oct 3, 2026 |
| [Stamford Museum & Nature Center — events](https://www.stamfordmuseum.org/) | Monthly. | Oct 3, 2026 |
| [Mill River Park — kids & family](https://millriverpark.org/events/category/kids-family/) | Monthly; skating season from Thanksgiving. | Oct 3, 2026 |
| [Palace Theatre](https://www.palacestamford.org/) | Each season: family shows. | Oct 3, 2026 |
| [Stamford Downtown — events](https://stamford-downtown.com/) | Seasonal: parade, holiday events. | Oct 3, 2026 |
| [Bartlett Arboretum — events](https://www.bartlettarboretum.org/) | Seasonal. | Oct 3, 2026 |

**Also cited in your data** (28 more site(s), busiest first)

- [chelseapiers.com](https://www.chelseapiers.com/athleticclub-stamford/classes) — 14 class card(s)
- [stamfordjcc.org](https://www.stamfordjcc.org/index.php?mrkrs=Early+Learning+Swim&src=programs) — 10 class card(s)
- [abilis.us](https://www.abilis.us/parent-and-child-classes-fall-2026/) — 5 class card(s)
- [stamfordct.gov](https://www.stamfordct.gov/) — 1 event(s), 3 class card(s)
- [stamfordrecreation.com](https://www.stamfordrecreation.com/) — 2 event(s), 2 class card(s)
- [littlejigz.com](https://www.littlejigz.com/) — 4 class card(s)
- [stamfordmoms.com](https://stamfordmoms.com/stamford-moms-family-fun-day/) — 3 event(s)
- [soundwaters.org](https://soundwaters.org/youth-programs/fall-adventure-series-2/) — 3 class card(s)
- [atozdancestudio.com](https://www.atozdancestudio.com/) — 2 class card(s)
- [curtaincallinc.com](https://www.curtaincallinc.com/) — 2 class card(s)
- [codeninjas.com](https://www.codeninjas.com/locations/en-us/ct/stamford/coding-school-249.html) — 2 class card(s)
- [stamfordchabad.org](https://www.stamfordchabad.org/civicrm/event/info?id=724&reset=1) — 1 event(s)
- [shopstamfordtowncenter.com](https://shopstamfordtowncenter.com/events/) — 1 event(s)
- [heystamford.com](https://www.heystamford.com/event-calendar) — 1 event(s)
- [childrenofthesound.com](https://www.childrenofthesound.com/) — 1 class card(s)
- [penderkeady.com](https://www.penderkeady.com/) — 1 class card(s)
- [balletschoolofstamford.org](https://www.balletschoolofstamford.org/school-schedule) — 1 class card(s)
- [stepsdancestudio.com](https://stepsdancestudio.com/) — 1 class card(s)
- [creativefamilyrhythms.org](https://creativefamilyrhythms.org/) — 1 class card(s)
- [stamfordmusicarts.com](https://stamfordmusicarts.com/) — 1 class card(s)
- [goldfishswimschool.com](https://www.goldfishswimschool.com/stamford/) — 1 class card(s)
- [hvswim.com](https://www.hvswim.com/) — 1 class card(s)
- [sweetblueswim.com](https://sweetblueswim.com/) — 1 class card(s)
- [angellandplay.com](https://angellandplay.com/) — 1 class card(s)
- [templesinaistamford.org](https://www.templesinaistamford.org/school/youth-programs.html) — 1 class card(s)
- [bgcastamford.org](https://www.bgcastamford.org/) — 1 class card(s)
- [germanschoolct.org](https://germanschoolct.org/class-registration/) — 1 class card(s)
- [armelleforkids.com](https://armelleforkids.com/tag/learn-spanish/) — 1 class card(s)

---

## Trumbull

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Trumbull Library — Programs for Little Ones](https://trumbull-ct.gov/760/Programs-For-Little-Ones) | Monthly. Weekly storytimes plus monthly Craft Night, PJ Story Time, Sensory Scientists. | Sep 29, 2026 |
| [Trumbull Library — calendar](https://trumbull.libcal.com/) | Monthly. LibCal: paste the kids-filtered list. Storytimes paused Oct 19–30 for early voting. | Oct 3, 2026 |
| [Trumbull Farmers' Market](https://www.trumbull-ct.gov/1018/Trumbull-Farmers-Market) | Each spring for the new season (ends Oct 15 this year). | Sep 29, 2026 |
| [Trumbull Parks & Recreation (MyRec)](https://trumbullct.myrec.com/info/activities/) | Each season: classes; some programs residents-only. | Oct 3, 2026 |
| [Town of Trumbull — events](https://www.trumbull-ct.gov/169/Events) | Fall Festival, Costume Swap, Tree Lighting dates. Town calendar blocks automated reading. | Oct 3, 2026 |

**Also cited in your data** (0 more site(s), busiest first)


---

## Wallingford

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Wallingford Public Library — upcoming events](https://www.wallingfordlibrary.org/events/upcoming) | Monthly. LibraryCalendar: paste the kids-filtered list view. Weekly storytimes end the week of Nov 16. | Oct 3, 2026 |
| [Wallingford Parks & Recreation (MyRec)](https://wallingfordct.myrec.com/info/activities/default.aspx?type=activities) | Each season: classes and one-day workshops. | Oct 3, 2026 |
| [Toyota Oakdale Theatre](https://www.toyotaoakdaletheatre.com/) | Monthly: family shows (watch for Bluey's Big Play). | Oct 3, 2026 |
| [Wallingford Patch](https://patch.com/connecticut/wallingford) | Celebrate Wallingford, Halloween Happenings, Seasons of Celebration, Holiday Stroll. | Oct 3, 2026 |

**Also cited in your data** (1 more site(s), busiest first)

- [centerforpediatrictherapy.com](https://centerforpediatrictherapy.com/screenings/) — 1 event(s)

---

## West Hartford

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [West Hartford Public Library (Noah Webster, Bishops Corner, Faxon)](https://www.westhartfordlibrary.org/) | Monthly. Paste the kids-filtered list; registered storytime series end mid-October, so check for the next series. Last full paste Oct 3. | Oct 3, 2026 |
| [West Hartford Leisure Services](https://www.westhartfordct.gov/) | Seasonal programs and town events. | Oct 3, 2026 |
| [Elizabeth Park — events](https://elizabethparkct.org/) | Seasonal (approved town-line exception). | Oct 3, 2026 |
| [Noah Webster House](https://noahwebsterhouse.org/) | Seasonal: Hauntings, egg hunt. | Oct 3, 2026 |
| [Playhouse on Park — young audiences](https://playhouseonpark.org/) | When the season posts. | Oct 3, 2026 |

**Also cited in your data** (40 more site(s), busiest first)

- [mandelljcc.org](https://www.mandelljcc.org/index.php?category=AquaticsCenter&link=AquaticsCenterLanding&src=gendocs) — 11 class card(s)
- [westhartfordartleague.squarespace.com](https://westhartfordartleague.squarespace.com/kids-fall-2026-classes) — 8 class card(s)
- [musictogetherwhfv.com](https://musictogetherwhfv.com/classes.aspx) — 6 class card(s)
- [wehamoms.com](https://wehamoms.com/halloweenstrollregistration) — 1 event(s), 2 class card(s)
- [teamplusone.com](https://www.teamplusone.com/kids-martial-arts-west-hartford/) — 3 class card(s)
- [schoolofrock.com](https://www.schoolofrock.com/locations/westhartford) — 3 class card(s)
- [riverbendbookshop.com](https://riverbendbookshop.com/event/2026-10-13/adam-and-makana-wallenta-punk-taco-vol-2-launch-party-and-drawing-workshop) — 2 event(s)
- [thebookclubct.com](https://www.thebookclubct.com/classes) — 2 class card(s)
- [westhartford.recdesk.com](https://westhartford.recdesk.com/Community/Program/Detail?programId=17294) — 2 class card(s)
- [hartfordstitch.com](https://www.hartfordstitch.com/service-page/october-saturday-sewing-club) — 2 class card(s)
- [ywcahartford.org](https://www.ywcahartford.org/programs/childcare/kidslink-before-after-school-program/west-hartford/) — 2 class card(s)
- [thechildrensmuseumct.org](https://www.thechildrensmuseumct.org/full-calendar/) — 2 class card(s)
- [stores.barnesandnoble.com](https://stores.barnesandnoble.com/event/9780062202706-22) — 1 event(s)
- [westhartford.librarymarket.com](https://westhartford.librarymarket.com/events/week/2026/05/27) — 1 event(s)
- [homedepot.com](https://www.homedepot.com/l/West-Hartford/CT/West-Hartford/06110/6210) — 1 event(s)
- [aflct.org](https://www.aflct.org/programs/family-arts-festival-2026/) — 1 event(s)
- [whchamber.com](https://www.whchamber.com/west-hartford-holiday-stroll/) — 1 event(s)
- [whso.org](https://whso.org/rehearsal-schedule/) — 1 event(s)
- [nightfallhartford.org](https://nightfallhartford.org/performances/nightfall2026) — 1 event(s)
- [westpresby.org](https://westpresby.org/) — 1 event(s)
- [westhartfordpride.org](https://westhartfordpride.org/) — 1 event(s)
- [noahwebster.yapsody.com](https://noahwebster.yapsody.com/) — 1 event(s)
- [westhartfordsaf.com](https://www.westhartfordsaf.com/) — 1 event(s)
- [thelittlewanderers.com](https://www.thelittlewanderers.com/) — 1 class card(s)
- [activekids.com](https://www.activekids.com/west-hartford-ct/baseball/baseball-leagues/miracle-league-minor-league-fall-ball-ages-4-11-years-old-2026) — 1 class card(s)
- [wehasoccer.org](https://www.wehasoccer.org/Default.aspx?tabid=746569) — 1 class card(s)
- [westhartfordlittleleague.com](https://www.westhartfordlittleleague.com/Default.aspx?tabid=1931544) — 1 class card(s)
- [junkpotstudio.com](https://junkpotstudio.com/classes/store/youth-camp) — 1 class card(s)
- [westhartfordyoga.com](https://www.westhartfordyoga.com/) — 1 class card(s)
- [pipyogastudio.com](https://www.pipyogastudio.com/about) — 1 class card(s)
- [bethelwesthartford.staging.shulcloud.com](https://bethelwesthartford.staging.shulcloud.com/) — 1 class card(s)
- [ctfamilytheatre.org](https://ctfamilytheatre.org/events/) — 1 class card(s)
- [westhartfordtheater.org](https://www.westhartfordtheater.org/) — 1 class card(s)
- [warhammer.com](https://www.warhammer.com/en-US/store-finder) — 1 class card(s)
- [warhammer-community.com](https://www.warhammer-community.com/en-gb/) — 1 class card(s)
- [angellandplay.com](https://angellandplay.com/) — 1 class card(s)
- [mail.newoldschoolofmusic.com](https://mail.newoldschoolofmusic.com/programs/group-lessons/early-childhood-music-classes) — 1 class card(s)
- [newoldschoolofmusic.com](https://newoldschoolofmusic.com/programs/recitals) — 1 class card(s)
- [bridgefamilycenter.org](https://www.bridgefamilycenter.org/) — 1 class card(s)
- [mygym.com](https://www.mygym.com/westhartford) — 1 class card(s)

---

## Westport

**Check regularly**

| Source | What to look for / how often | Last checked |
|---|---|---|
| [Westport Library — children](https://westportlibrary.org/calendar/category/children/) | Monthly. | Oct 3, 2026 |
| [Wakeman Town Farm](https://wakemantownfarm.org/) | Each season: kids' programs and events. | Oct 3, 2026 |
| [Earthplace](https://earthplace.org/) | Monthly. | Oct 3, 2026 |
| [Westport Country Playhouse — families](https://www.westportplayhouse.org/) | Each season: family series (Pinkalicious, Pete the Cat dates TBA). | Oct 3, 2026 |
| [Westport Museum for History & Culture](https://westportmuseum.org/) | Seasonal. | Oct 3, 2026 |
| [Westport Parks & Rec](https://www.westportct.gov/government/departments-a-z/parks-and-recreation) | Seasonal: PAL Rink, Learn to Skate. | Oct 3, 2026 |

**Also cited in your data** (19 more site(s), busiest first)

- [westporty.org](https://westporty.org/summercamp/) — 15 class card(s)
- [westportmoms.com](https://westportmoms.com/calendar/category/family/month/) — 6 class card(s)
- [mocawestport.org](https://mocawestport.org/) — 6 class card(s)
- [westporthistory.org](https://westporthistory.org/events/) — 3 class card(s)
- [westportdowntown.com](https://westportdowntown.com/westoberfest) — 1 event(s), 1 class card(s)
- [levittpavilion.com](https://levittpavilion.com/) — 2 class card(s)
- [westportjournal.com](https://westportjournal.com/) — 1 event(s)
- [westportsoccer.org](https://www.westportsoccer.org/) — 1 class card(s)
- [westportlittleleague.com](https://www.westportlittleleague.com/) — 1 class card(s)
- [westportpal.org](https://westportpal.org/) — 1 class card(s)
- [westportyouthlacrosse.com](https://www.westportyouthlacrosse.com/) — 1 class card(s)
- [remarkabletheater.org](https://remarkabletheater.org/) — 1 class card(s)
- [westportfarmersmarket.com](https://www.westportfarmersmarket.com/) — 1 class card(s)
- [westportsacademyofdance.com](https://westportsacademyofdance.com/) — 1 class card(s)
- [suzukischools.org](https://suzukischools.org/) — 1 class card(s)
- [westportschoolofmusic.org](https://westportschoolofmusic.org/) — 1 class card(s)
- [thewonder.com](https://www.thewonder.com/) — 1 class card(s)
- [groove-store.com](https://groove-store.com/) — 1 class card(s)
- [barnesandnoble.com](https://www.barnesandnoble.com/) — 1 class card(s)

---
