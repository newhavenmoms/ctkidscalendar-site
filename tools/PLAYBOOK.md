# Research playbook

How to fill a new town's page, and how to refresh an existing one each season.
It records what actually worked across the first 18 towns, so the next town is
faster. Pair it with:

- `tools/SOURCES.md`: each town's specific sources and when they were last checked (generated: edit `tools/sources-curated.json`, then run `node tools/build-sources-md.js`)
- `node tools/refresh-report.js`: what's stale, ending soon or missing, right now
- `shared/TOWN-TEMPLATE.md`: page setup and the **location rule**

---

## The ground rules

1. **Location rule.** Calendar items (events, classes, Big Days, "date not
   announced yet" cards) must be **in the town**, including its villages. The
   only exceptions are listed in `shared/TOWN-TEMPLATE.md`. Nearby places go only in
   "Worth a short drive."
2. **Verify, don't assume.** Every event needs a source link showing this year's
   date. If last year's date is all you can find, make a "date not announced
   yet" card that says when it *usually* happens.
3. **Watch for stale pages.** Search engines and some calendars serve cached
   copies (we hit February listings in October). Check that the year on the
   page matches.
4. **Watch for same-name towns.** Milford, Middletown, Newtown, Fairfield and
   Greenwich all exist in other states. Look for a 06xxx zip code.
5. **Spanish.** Every new blurb, ages line and price line gets a translation in
   `shared/data-es.js`. Event, place and business names stay in English.

---

## New town: the order that works

Work through these in order. Each step lists where to look and what kinds of
source paid off.

### 1. Library (the backbone: often half of a town's listings)
- Find the platform: **LibCal** (`*.libcal.com`), **LibraryCalendar**
  (`*.librarycalendar.com`), **LibraryMarket**, or **Assabet**.
- LibCal: add the iCal feed to `tools/sources.json` and run the importer.
- LibraryCalendar sites and many others **block automated reading** (Russell,
  Booth). Have the owner open the kids' list view, select all, copy and paste.
  The importer's `--paste` mode handles that text, or Claude can read it
  straight from the chat. This was the single most productive step for
  Middletown and Newtown.
- Note session end dates. Baby and toddler storytimes often run in 4–8 week
  sessions (Booth's ended in October).

### 1a. Library calendars: lessons from the first 18 towns

**Getting the data, by platform**

| Platform | How to tell | What works |
|---|---|---|
| LibCal | `*.libcal.com` | iCal feed via the importer, or paste the filtered list view |
| LibraryMarket / LibraryCalendar (Drupal) | "This event is in the … group" text | Owner pastes the kids-filtered list (Russell, Wallingford, Fairfield, Ferguson, West Hartford) |
| CivicPlus | `calendar.aspx?CID=` | Download the category .ics. Its descriptions are empty, so use it for dates and times only and write blurbs by hand (Norwalk) |
| Others | Anything else | Paste the list view, a few pages at a time |

Ask the owner to filter to children's audiences before pasting.

**Reading the paste (the mistakes we actually made)**

- **Never assume "weekly until December."** Storytimes run in sessions, often 4–8 weeks. If dates stop, the series ends there; list only the dates shown and say "next series not posted yet." Examples: Booth and West Hartford end mid-October; Wallingford, Russell and SoNo end mid-November.
- **Check every expected week for gaps**, and turn gaps into exclusions:
  - Holidays: Columbus Day, Veterans Day, Thanksgiving week, Christmas week.
  - Election Day.
  - Special events taking the slot (Halloween parades, guest performers).
  - Unusual breaks (Trumbull paused storytimes Oct 19–30 for early voting).
- **Thanksgiving:** if a feed lists programs that day, leave them off and say so.
- **Put practical notices in blurbs and the library card:**
  - Construction (Ferguson's Youth Services closure).
  - Parking (Milford's lot closure; West Hartford's free garage).
  - Cancellations.
  - "Full / waitlist."
  - "Families register for the month."
- **Search snippets can be stale.** Twice, snippet-based times were wrong (Russell). The library's own list wins.

**What to include**

- **Include:** storytimes, kids' clubs, after-school programs, holiday and Halloween specials, family concerts and movies, homework help, and caregiver groups for parents of babies.
- **Group many one-off after-school projects at one branch into a single listing** with all dates and themes in the blurb (Fairfield).
- **Leave out:**
  - Adult-only programs.
  - Private room bookings and club meetings.
  - Zoom- or YouTube-only programs, unless the town already lists online classes.
  - Readmobile or pop-up stops without an address.
- **Teen-only programs:** keep existing ones when the paste was filtered to kids (they were filtered out, not cancelled).

### Weekend check (added Oct 5, 2026)

After building or refreshing a town, look at each of the next six weekends on its page. If a weekend has nothing, search the town's Chamber of Commerce events page and its Patch calendar before accepting the gap. Small towns' biggest weekends (craft festivals, Parks & Rec fall series) are often only listed there. Old Saybrook's Arts & Crafts Festival (Oct 3–4) was missed this way.

### 2. Parks & Recreation
- **The seasonal brochure PDF** is the jackpot (Newtown's gave 19 classes in one
  read). Look for "Fall/Winter Program Guide" on the town site.
- **MyRec** (`*.myrec.com`) catalogs list every program, but detail pages often
  put the dates in images. Search snippets of individual program pages often
  carry the live fall table when the page itself reads as a cached copy.
- Town-run Big Days usually live here: Halloween parties, trick-or-treat
  events, tree lightings, egg hunts.

### 3. Big Days (town traditions)
- Search "[town] Halloween 2026", "[town] tree lighting", "[town] holiday
  festival", "[town] fall festival".
- Best sources: the town site, the local paper (Newtown Bee, Patch), the
  chamber of commerce (Middlesex Chamber ran Holiday on Main Street), and the
  local Youth & Family Services (they run Newtown's Holiday Festival).
- Most are annual and fixed to a pattern ("Friday after Thanksgiving," "last
  Saturday before Halloween"). Record the pattern on the card.

### 4. Theaters and family performances
- Big presenting houses with family series: Shubert (New Haven), Ridgefield
  Playhouse, Palace Theatre (Stamford), Toyota Oakdale (Wallingford), Quick
  Center (Fairfield), Westport Country Playhouse.
- **Kid-cast shows** are easy to miss and very local: Crystal Theatre and
  Norwalk Arts Center (Norwalk), Music Theatre of CT, Glastonbury Youth & Family
  Services, Open Arts Alliance (Greenwich), community players (Town Players of
  New Canaan).
- Family theater companies with an annual holiday show: Pantochino (Milford, every
  December at the MAC), Legacy Theatre (Branford).
- Ticket aggregators (Live Nation, SeatGeek) are fine for confirming dates, but
  link the theater's own site.

### 5. Museums and historical societies
- Every town has a historical society; most open on a fixed pattern ("2nd and
  4th Sundays," "summer Sundays"). Record the pattern.
- Check each one's **event calendar** separately: family festivals (Greenwich
  Historical Society's Fall Harvest Festival), holiday open houses, CT Open
  House Day (June).
- Statewide programs to flag each year: **CT Summer at the Museum** (free kids
  plus one adult, July–August) and **CT Open House Day** (a Saturday in June).

### 6. Things to do (places, not dated events)
Cover each category; this is the "rainy day / get outside" backbone.

| Category | Where we found them |
|---|---|
| Parks, playgrounds | Town parks page; note residents-only parks and permit fees (Newtown, Darien) |
| Splash pads | Town site; splashpadatlas.com and mommypoppins lists to discover, then confirm on the town site |
| Farms | CT Grown / ctvisit pick-your-own lists; farm's own site for season dates |
| Rinks | Rink's public-skate page; outdoor rinks open around Thanksgiving |
| Bookstores | **ctbooktrail.org** lists every independent bookstore with its site |
| Toy stores | Yelp/YellowPages to find names, then confirm the store's own site |
| Museums | Town history pages, ctvisit.com listings |
| Libraries | Every branch |

### 7. Bookstore and toy-store events
Indie bookstores often run weekly storytimes (Wesleyan RJ Julia: Sundays 11 am;
Fairfield University Bookstore: Saturdays). Check each store's events page.

### 8. Think outside the box
Farms' fall weekends, nature centers, observatories (Wesleyan's Van Vleck Kids'
Nights through the rec department), mansions with family shows (Wadsworth
Mansion's Nutcracker), and costume sales at youth theaters.

---

## Refresh: when and what

Run `node tools/refresh-report.js` first. It writes `tools/refresh-report.md`
with every "date not announced yet" card (recheck these first), recurring
listings that end soon, category gaps by town, and the thinnest towns.

### Monthly
- Re-import or re-paste library calendars (new sessions).
- Recheck "date not announced yet" cards; most get dates 4–8 weeks out.

### Seasonal checklist

**Late October → winter (Nov–Feb)**
- Holiday Big Days: tree lightings, holiday festivals, Santa visits, holiday
  train shows, Nutcrackers, holiday theater runs, menorah lightings.
- Rinks: outdoor rinks open (Westport PAL Rink at Longshore, Mill River Park);
  Learn to Skate winter sessions; holiday skate events.
- Winter class sessions (rec brochures come out in November/December).
- **School-break programs**: December break, MLK Day, February break camps and
  workshops (libraries, rec departments, museums).
- Indoor play: refresh open-gym and indoor playground hours.
- New Year's: Noon Year's Eve events (children's museums, libraries).
- Extend each town's `calendarThrough` past December 31.

**Late January → spring (Mar–May)**
- Egg hunts, spring festivals, Earth Day, spring rec brochure, spring theater
  (youth productions), farm openings (strawberries in June).

**Late April → summer (Jun–Aug)**
- Summer reading kickoffs, concerts on the green, splash pad openings, beach
  passes and resident rules, summer camps, CT Summer at the Museum, farmers
  markets, CT Open House Day (June).

**Late July → fall (Sep–Oct)**
- Fall rec brochure, library fall sessions, pick-your-own and corn mazes, fall
  festivals, Halloween events (most announced by late September).

---

## Sources added October 2, 2026

New to `SOURCES.md`, grouped by town. Note how each source was read.

- **Branford:** Legacy Theatre (holiday show; times on the tix.com box office);
  Harrison House Museum (summer Saturdays).
- **Cheshire:** Hitchcock-Phillips House (2nd and 4th Sundays; holiday open house
  in mid-December); Norton Brothers Fruit Farm.
- **Fairfield:** Quick Center 2026–27 season announcement (family shows Feb and
  Mar); Fairfield University Bookstore storytimes.
- **Glastonbury:** Youth & Family Services theater page (fall musical); Addison
  Park; Pinwheels Toys; River Bend Bookshop.
- **Greenwich:** Greenwich Historical Society events calendar (fall festival,
  December holiday festival); Greenwich Arts Council events; Open Arts Alliance
  (via Patch); Athena Books; Diane's Books.
- **Middletown:** Russell Library (**paste only**); Middletown Rec on MyRec
  (Kids' Nights at Van Vleck Observatory, Downtown Trick or Treat); Wesleyan
  RJ Julia (Sunday storytime); Wadsworth Mansion public events; General
  Mansfield House; Oddfellows Playhouse; Veterans Memorial Park splash pad.
- **Milford:** Milford Arts Council (Family Pillow Concert); Pantochino (holiday
  musical every December); Mermaid Books.
- **New Canaan:** Town Players (Rudolph); Elm Street Books.
- **New Haven:** McGivney Pilgrimage Center (formerly the Knights of Columbus
  Museum; Christmas crèche exhibit); New Haven Museum; Ralph Walker Rink (new
  operator: Elm City Sports Group); city neighborhood splash pads; Possible
  Futures.
- **Newtown:** C.H. Booth Library (**paste only**); Parks & Rec fall brochure PDF;
  EverWonder (tickets via simpletix); Edmond Town Hall (showare box office);
  Newtown Youth & Family Services (Holiday Festival); Matthew Curtiss House;
  Castle Hill Farm; Halloween on Main.
- **Norwalk:** Crystal Theatre (class show dates are on its homepage); Norwalk
  Arts Center; Music Theatre of CT student productions; Norwalk Historical
  Society; Mill Hill Historic Park.
- **Ridgefield:** Ridgefield Historical Society (Scott House).
- **Stamford:** Stamford History Center; Awesome Toys & Gifts.
- **Wallingford:** Toyota Oakdale Theatre (family shows; check for *Bluey's Big
  Play*); Samuel Parsons House.
- **Westport:** PAL Rink at Longshore; Learn to Skate USA (Parks & Rec); Wakeman
  Town Farm (kids' programs); Westport Country Playhouse family series.
- **West Hartford:** four town splash pads; Playhouse on Park (young-audience
  dates not yet posted).

**Sites that block automated reading** (ask for a paste or work from search
snippets): `*.librarycalendar.com` event pages, `middletownct.gov` calendar,
`ctvisit.com` (very large pages), some `*.myrec.com` detail pages.

### Holiday tags (added Oct 5, 2026)

Major holidays show as a tag on the calendar's day headings. They're listed in `HOL` near the top of the calendar code in `shared/app.js`, with English and Spanish names. The list currently runs through Martin Luther King Jr. Day (Jan 18, 2027). Each fall, add the coming year: Hanukkah, Diwali, Thanksgiving, MLK Day and the Monday holidays move every year, so look the dates up rather than copying last year's.
