# Adding a new town to CT Kids Calendar

Every town site is one HTML file that (1) sets a `window.TOWN` config object with
that town's content, and (2) loads the two shared files everyone uses:
`/shared/style.css` and `/shared/app.js`. Fix a bug or add a feature once in
those two files, and every town gets it.

## To start a new town

1. Copy `/shared/page-template.html` to `/<town-slug>/index.html`
   (e.g. `/norwalk/index.html`).
2. Find-and-replace every `{{TOWN}}` with the town's display name (e.g. `Norwalk`).
3. Fill in the other `{{...}}` placeholders (see below).
4. Pick an accent color (see "Choosing a color" below) and set it in the
   `:root{ --accent: ... }` block.
5. Fill in the `window.TOWN = {...}` object with real content (see field
   reference below). Empty arrays are fine to start — the page will show
   friendly "still building this" messages instead of looking broken.
6. Write the "Things to do anytime" section by hand (parks, museums, short
   drives) — this one isn't data-driven, just edit the HTML directly using
   the existing `.places` markup as a guide.
7. Add the town as a pin + card on the homepage (`/index.html`): a `<div
   class="tcard soon">` in the `.towngrid`, and a pin in the `.ctmap` SVG
   (copy an existing `<a class="mappin">` block and adjust the coordinates,
   label position, and `href="#card-<slug>"`). Once the town's page is real,
   change its card to `<a class="tcard" href="/<slug>/">` and its map pin's
   `href` to `/<slug>/`.

## `window.TOWN` field reference

```js
window.TOWN = {
  name: "Norwalk Kids Calendar",      // used in the header, share text, footer
  townLabel: "Norwalk, CT",            // fallback location string
  url: "https://ctkidscalendar.com/norwalk/",   // must match the real deployed URL
  email: "hello@ctkidscalendar.com",   // contact address (same for every town, for now)
  instagram: "ctkidscalendar",         // no @ symbol
  calendarThrough: "2026-12-31",       // last date the week-by-week calendar covers

  venues: {
    // short-id: [Display name, street address, "Town, CT" (optional)]
    someLibrary: ["Norwalk Public Library", "1 Belden Ave"],
  },

  venueMeta: {
    // short-id: [neighborhoodKey, indoor(1) / outdoor(0) / null if unknown]
    someLibrary: ["downtown", 1],
  },

  hoods: [
    // [key, "Label"] — leave as [] to hide the neighborhood filter entirely
    ["downtown", "Downtown"],
    ["eastnorwalk", "East Norwalk"],
  ],

  events: [
    // Recurring, same shape as New Haven Moms' event objects:
    // {t:title, v:venueId, ages, a:[age groups], price, free, drop, s:[[dow,[[start,end]],from,until,nth?]]}
    // One-off / date-ranged: {..., special:"fall|hw|hol", when:[{from,to?,t:[[start,end]]}]}
  ],

  tba: [
    // Annual events without a confirmed date yet: {g:"fall|hw|hol", t, w, p, src}
  ],

  classes: [
    // {id, c:category (music|dance|swim|move|art|build|nature), n:name, u:link,
    //  blurb, ages, where}
  ],

  library: null,
  // or: {for:"Free, every week", name:"Norwalk Public Library",
  //      desc:"...", a:"See storytimes", href:"https://..."}

  extraResources: []
  // local additions to the shared statewide list: {for,name,desc,a,href}
};
```

The shared **Resources for moms** section (crisis hotlines, WIC, Diaper Bank,
HUSKY, Birth to Three, Care 4 Kids) is built into `/shared/app.js` and is the
same for every town — it's genuinely statewide. Only the library entry and
any `extraResources` are per-town.

## Choosing a color

Everything else — navy text, cream background, yellow "today"/"free" accent —
is shared and fixed. A town only sets **one** value, `--accent`, a light
pastel used for the hero band and, at low tint, a couple of section
backgrounds. Pick something in the same family as the existing towns (soft,
roughly 80–90% lightness) so contrast with navy text stays consistent without
retesting:

- Stamford `#F3B9A3` (coral)
- Norwalk `#A8E4C9` (mint)
- West Hartford `#F1D48C` (amber)
- Ridgefield `#BFE0B0` (sage)
- Fairfield `#C7CBF2` (periwinkle)

## What's shared vs. per-town

| Shared (`/shared/`)                          | Per-town (each town's `index.html`)         |
|-----------------------------------------------|----------------------------------------------|
| Calendar logic, filters, week/weekend picker  | Events, venues, classes (the `TOWN` object)   |
| Share sheet, "Add to calendar" / ICS export   | Accent color                                  |
| Statewide crisis line + resource list         | Local library, extra local resources          |
| Fonts, layout, buttons, tags, tab bar          | "Things to do anytime" write-up               |
| Acorn logo mark                                | Page title/meta, privacy policy town name     |

## Note on Spanish

New Haven Moms (a separate site, not part of this shared engine) is fully
bilingual. This shared engine launches English-only — the bilingual pattern
is proven and could be added later, but it needs real translated content per
town, which is a separate project once a town's English content is solid.
