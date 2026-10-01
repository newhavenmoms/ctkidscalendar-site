# Calendar-feed importer

Pulls kids' and family events from library (and other) calendar feeds, turns
them into CT Kids Calendar events, and lets you review them before anything
goes live. Imported events are stored apart from the hand-checked data in each
town page, so re-running an import never overwrites your curated events.

Needs Node 18 or newer. Run everything from the repo root.

## One-time setup: add a feed

1. Open the library's events calendar (the `calendarPage` link in
   `tools/sources.json`).
2. Find its **Subscribe** / **iCal** / **Add to calendar** button for the whole
   calendar (not a single event) and copy the link.
   - **LibCal** (Cheshire, Milford, Trumbull): the Subscribe button on the
     calendar gives a link like
     `https://xxx.libcal.com/ical_subscribe.php?src=p&cid=1234&k=abcdef`.
     If it lets you choose a category such as Children or Kids, do that and set
     `"kidsOnly": true` for that source.
   - **LibraryCalendar** (Blackstone, Welles-Turner, Russell) and other sites:
     look for the same kind of iCal or "subscribe" link. If a site only offers
     .ics files for single events, the importer can't use it; let Claude know.
3. Paste it into that library's `"url"` in `tools/sources.json`.

## Each time: import, review, publish

```
node tools/import-events.js cheshire        # 1. make a draft (changes nothing on the site)
open tools/drafts/cheshire.review.md        # 2. read the numbered list, click the links
node tools/approve-imports.js cheshire      # 3. publish everything marked ✅
node shared/build-stats.js                  # 4. refresh the homepage numbers
```

In step 3 you can be choosy:
- `--only 1,4,7` publishes exactly those numbers (including ⬜ ones).
- `--skip 3,5` publishes the ✅ items except those.
- `--dry` shows what would happen without changing anything.

If a site blocks the download, open the feed link in your browser, save the
.ics file, and use it directly:

```
node tools/import-events.js cheshire --file ~/Downloads/feed.ics
```

## What the importer does for you

- **Keeps only kids' and family events.** It skips adult programs, closures
  and cancellations, and lists what it skipped at the bottom of the review.
  Anything it's unsure about (for example, only the description mentions kids)
  is marked ⬜ so it won't publish unless you include it.
- **Turns repeated dates into weekly schedules**, with the skipped weeks
  listed, and combines same-morning sessions like 10:15 and 11:00 into one
  listing.
- **Checks for duplicates** against what's already on the site. If the feed
  shows a program you already list running later than the site does (a new
  session), the review tells you to extend it.
- **Refreshes instead of piling up.** Publishing again replaces that source's
  previous import, so run it monthly to pick up new sessions.
- **Fills in ages, age filters, price, registration and drop-in** from the
  listing text. Anything it had to guess is flagged ⚠️ in the review.

## Good to know

- Imported events are English-only for now. The Spanish view shows them in
  English until translations are added.
- Imported events have no "Check first" tag, because they come from the
  organizer's own calendar. Still give the review a quick read: feeds sometimes
  include staff-only or members-only items.
- Files: `tools/sources.json` (feeds), `tools/drafts/` (review files, safe to
  delete), `shared/imports/<town>.json` + `.js` (published imports; the `.js`
  is generated, don't edit it).
- `tools/fixtures/test-feed.ics` is a made-up test feed for checking the
  importer. Don't publish from it:
  `node tools/import-events.js cheshire --file tools/fixtures/test-feed.ics`
