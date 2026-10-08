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
| Indoor play, climbing, roller rinks | Mommy Poppins indoor-play guide, ctvisit.com listings; confirm on the venue's site |
| Creative studios, coding, music, drama | Patch "parent's guide to after-school activities" articles, classcub.com, Macaroni Kid directories |
| Museums | Town history pages, ctvisit.com listings |
| Libraries | Every branch |

### 7. Bookstore and toy-store events
Indie bookstores often run weekly storytimes (Wesleyan RJ Julia: Sundays 11 am;
Fairfield University Bookstore: Saturdays). Check each store's events page.

### 7b. Creative places, indoor play and mom blogs (added Oct 8)
Don't stop at "no bookstore / no toy store" after one list check. For every town:
- **Chains count:** Barnes & Noble (storytimes and author visits; the event pages load by script, so check the town's Macaroni Kid edition for dates), LEGO Store build events, comic and game shops (thecardshopfinder.com lists Pokémon/Magic shops by town), and the library Friends' used-book shop (often in the library basement).
- **Creative places:** paint-your-own pottery, kids' art and workshop studios, coding/STEM schools (Code Ninjas, theCoderSchool, Snapology), music schools, drama academies, community theater (family musicals), kids' cooking.
- **Indoor play:** trampoline and adventure parks (Urban Air, Lava Island, Jumpz, FunMax), climbing gyms, roller rinks, play cafés, mall play areas. Mommy Poppins' "indoor play spaces in CT" guide (updated Feb 2026) and ctvisit.com listings are the fastest finders. Confirm address and town; many are just over a town line.
- **Mom blogs and family-event sites:** find the Macaroni Kid edition that names the town in its coverage list (Hartford covers Simsbury and the Farmington Valley; Southbury covers Waterbury; Danbury has its own; manchester.macaronikid.com is New Hampshire). Their calendars return 403 to automated reading, so ask the owner to paste them. Also: town-specific newsletters (This Week in Hamden on Substack, Farmington Valley Community on beehiiv), farm ticket pages (Flamig Farm on Yapsody), KidsWannaGo (often stale; mis-tags), Mommy Poppins (good for places, stale for dates).
- Confirm every event from a blog on the host's own site, and record dead ends in `known-none.json` with the reason (e.g., Waterbury's Barnes & Noble closed Jan 2026).

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

### Submissions form (added Oct 5, 2026)

Every page has a "Submit an event" button and footer link that open a shared form (`shared/submit.js`). Submissions go to newhavenmoms@gmail.com through Web3Forms once its access key is pasted into `WEB3FORMS_KEY` at the top of that file; until then the form opens the visitor's email app, pre-filled. `build_town.py` adds each new town to the form's town list. Treat submissions like any other lead: verify against the organizer's own page before adding, and note the source.

### Schools page (added Oct 6, 2026; renamed Oct 7, 2026)

`/schools/` is linked from the homepage menu ("Schools" / "Escuelas"; menu order is Español, Schools, Submit an event) and currently shows a "Coming soon" card (English/Spanish). It's marked noindex and kept out of the sitemap until it launches; when real content goes up, remove the robots meta tag and add it to sitemap.xml.

The page used to live at `/school/`. That folder now holds only a small redirect page that sends visitors (and any `?query` or `#anchor`) on to `/schools/`. Keep it so old links keep working, and keep it out of the sitemap. If the site moves to a host with server-side redirects (Netlify `_redirects`, Cloudflare Pages, etc.), add a 301 from `/school/` to `/schools/` there as well.

### Nine new towns (added Oct 7, 2026)

Stratford, Hartford, Waterbury, Bridgeport, Hamden, Manchester, Farmington, Danbury and Simsbury, built with `tools/newtowns/<town>.py` + `build_town.py` like the others. Lessons:

- **LibCal can be read without a paste.** The calendar page itself loads by JavaScript, but its list endpoint returns the events: `https://<lib>.libcal.com/ajax/calendar/list?c=-1&date=0000-00-00&perpage=35&page=1&audience=<id>&cats=&inc=0`. Keep `perpage` at 35 or less (bigger pages get cut off) and page through. Audience IDs are in the raw data: Bridgeport 7093 (ages 0–5) and 7094 (6–11); Hamden 4605 (preschool) and 3367 (school age). Fetching many pages quickly hits a rate limit, so pace it.
- **Paste-only calendars:** LibraryCalendar (Farmington, Simsbury), Communico (Hartford, `programs.hplct.org`) and mylibrary.digital (Danbury, Manchester). mylibrary.digital list views show **start times only**, so Danbury and Manchester end times are estimates; the events are marked "check." The importer's paste parser (`tools/lib/librarycalendar-text.js`) handled the Farmington and Simsbury pastes directly.
- **Big cities, thin pages.** Hartford, Hamden and Manchester came out thin because their libraries carry most of the kids' calendar and the cities' Big Days are mostly undated so far. Hartford especially needs a second pass: Wadsworth Atheneum family days, the Bushnell's family shows, the city tree lighting.
- **Same-name trap: Waterbury, Vermont** (River of Light parade, "Waterbury Roundabout"). Bridgeport, West Virginia also showed up for rinks.
- **Weekend check (Oct 7):** Patch calendars for Hartford, Hamden, Manchester and Simsbury had nothing kid-focused or were stale. The gaps are recorded in `SOURCES.md` as accepted for now.
- **Map pins** for the new towns were placed from `shared/zips.json` town centers using a fit of the existing pins, then nudged apart by hand around Hartford (Farmington, Hartford, Simsbury).

**Full playbook pass (also Oct 7):** The first build of these nine covered only the library, Big Days and a few places. A second pass went through every step: Parks & Rec, theaters, museum and historical-society calendars, bookstores and toy stores, farms, rinks and splash pads, and the Chamber/Patch weekend check. Don't skip it: it roughly doubled the events on the thinnest towns and filled the classes sections. What worked:
- **MyRec catalogs** (`<town>ct.myrec.com/info/activities/default.aspx`) list program names; ask the reader for each program's `program_details.aspx?ProgramID=` link, then read each one for sessions, ages and fees (Simsbury, Hamden).
- **RecDesk** (Stratford) and **Flipsnack** guides (Manchester) don't render outside a browser, so ask the owner for a paste or a PDF. Last year's PDF guide often sits at a predictable town-site path and shows the pattern.
- **Museum agenda views** page through cleanly (the Wadsworth's `events/action~agenda/page_offset~N/`; the Mattatuck's `calendar/list/`).
- **The Bushnell Children's Theatre** school-day shows are open to the public ($14 by phone), so list them.
- Same-name traps again: Waterbury VT (discoverwaterbury.com) and Manchester NH (Wonderland Books and Toys).
- Record categories confirmed absent in `tools/known-none.json` so the refresh report stops flagging them.

**Owner-supplied sources (Oct 8):** WebFetch refuses URLs that haven't appeared in a search result or a message. When a town's Rec catalog (MyRec, RecDesk) won't open, ask the owner to send the link in a message; after that it reads normally (Farmington MyRec). Open each `program_details.aspx?ProgramID=` page for sessions, fees and seats, and skip sessions that have ended or meet out of town. Seasonal guides that only exist as image flipbooks (Manchester Now) need the owner's PDF. Its extracted text has gaps between letters and jumbled columns, so check each day/date pair against a calendar before using it. Keep the extracted text in tools/pastes/, not the PDF.
