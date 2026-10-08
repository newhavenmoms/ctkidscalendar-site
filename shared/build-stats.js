/* CT Kids Calendar — homepage stats builder.
   Run this (node shared/build-stats.js from the repo root) any time town
   data changes, so the homepage's headline numbers stay accurate.
   It reads window.TOWN out of each town's index.html and writes
   shared/stats.json, which the homepage fetches at runtime. Imported events
   (shared/imports/<town>.json, from tools/approve-imports.js) are counted too.

   Definitions used (documented here so a future edit stays consistent):
   - things    = classes.length + events that are NOT a Big Day (e.can.special is unset)
                 i.e. every recurring storytime/class a family could attend weekly.
   - venues    = count of unique venue entries, summed across towns (not deduped
                 across towns, since a family only cares about their own town's list).
   - festivals = events WITH a .special tag (Big Days) + tba.length ("date not
                 announced yet" cards, which also render in the Big Days columns).
*/
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const TOWNS = ['stamford', 'norwalk', 'fairfield', 'ridgefield', 'west-hartford', 'new-haven', 'greenwich', 'darien', 'westport', 'new-canaan', 'cheshire', 'milford', 'trumbull', 'wallingford', 'middletown', 'glastonbury', 'newtown', 'branford', 'guilford', 'old-saybrook', 'essex', 'madison', 'stratford', 'hartford', 'waterbury', 'bridgeport', 'hamden', 'manchester', 'farmington', 'danbury', 'simsbury'];

let things = 0, venues = 0, festivals = 0;

for (const slug of TOWNS) {
  const file = path.join(ROOT, slug, 'index.html');
  const html = fs.readFileSync(file, 'utf8');
  const start = html.indexOf('window.TOWN = {');
  const end = html.indexOf('\n};', start) + 2;
  if (start < 0 || end < 2) throw new Error('window.TOWN block not found in ' + file);
  const TOWN = (function () {
    return eval('(' + html.slice(start, end).replace('window.TOWN = ', '').replace(/;\s*$/, '') + ')');
  })();

  // events published by tools/approve-imports.js live beside the page, not in it
  const importsFile = path.join(ROOT, 'shared', 'imports', slug + '.json');
  if (fs.existsSync(importsFile)) {
    const imp = JSON.parse(fs.readFileSync(importsFile, 'utf8'));
    TOWN.events = TOWN.events.concat(imp.events || []);
    for (const k of Object.keys(imp.venues || {})) if (!TOWN.venues[k]) TOWN.venues[k] = imp.venues[k];
  }

  const classCount = TOWN.classes.length;
  const eventCount = TOWN.events.length;
  const specialCount = TOWN.events.filter(e => e.special).length;
  const tbaCount = (TOWN.tba || []).length;
  const venueCount = Object.keys(TOWN.venues).length;

  things += classCount + (eventCount - specialCount);
  venues += venueCount;
  festivals += specialCount + tbaCount;
}

const stats = {
  towns: TOWNS.length,
  things,
  venues,
  festivals,
  updated: new Date().toISOString().slice(0, 10),
};

fs.writeFileSync(path.join(__dirname, 'stats.json'), JSON.stringify(stats, null, 2) + '\n');
console.log('shared/stats.json written:', stats);

/* ---------- homepage "Big days by county" feed ----------
   Also writes shared/bigdays.json: every upcoming Big Day (events with a
   .special tag) from every town, grouped by county. The same event listed by
   several towns (same title at the same place) appears once, naming every
   town. The homepage fetches this file and hides anything already over. */
const COUNTIES = [
  { id: 'fairfield', en: 'Fairfield County', es: 'Condado de Fairfield',
    towns: ['bridgeport', 'danbury', 'darien', 'fairfield', 'greenwich', 'new-canaan', 'newtown', 'norwalk', 'ridgefield', 'stamford', 'stratford', 'trumbull', 'westport'] },
  { id: 'new-haven', en: 'New Haven County', es: 'Condado de New Haven',
    towns: ['branford', 'cheshire', 'guilford', 'hamden', 'madison', 'milford', 'new-haven', 'wallingford', 'waterbury'] },
  { id: 'hartford', en: 'Hartford County', es: 'Condado de Hartford',
    towns: ['farmington', 'glastonbury', 'hartford', 'manchester', 'simsbury', 'west-hartford'] },
  { id: 'middlesex', en: 'Middlesex County', es: 'Condado de Middlesex',
    towns: ['essex', 'middletown', 'old-saybrook'] },
];
const missing = TOWNS.filter(t => !COUNTIES.some(c => c.towns.includes(t)));
if (missing.length) throw new Error('Add these towns to a county in build-stats.js: ' + missing.join(', '));

// Spanish titles come from the shared dictionary the town pages use
const window_ = {};
new Function('window', fs.readFileSync(path.join(__dirname, 'data-es.js'), 'utf8'))(window_);
const ES = window_.DATA_ES || {};
const slugify = t => t.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const today = new Date().toISOString().slice(0, 10);

function loadTown(slug) {
  const html = fs.readFileSync(path.join(ROOT, slug, 'index.html'), 'utf8');
  const start = html.indexOf('window.TOWN = {');
  const end = html.indexOf('\n};', start) + 2;
  const T = eval('(' + html.slice(start, end).replace('window.TOWN = ', '').replace(/;\s*$/, '') + ')');
  const importsFile = path.join(ROOT, 'shared', 'imports', slug + '.json');
  if (fs.existsSync(importsFile)) {
    const imp = JSON.parse(fs.readFileSync(importsFile, 'utf8'));
    T.events = T.events.concat(imp.events || []);
    for (const k of Object.keys(imp.venues || {})) if (!T.venues[k]) T.venues[k] = imp.venues[k];
  }
  T.label = (T.name || slug).replace(/ Kids Calendar$/, '');
  return T;
}

const bigItems = new Map();
for (const county of COUNTIES) {
  for (const slug of county.towns) {
    if (!TOWNS.includes(slug)) continue;
    const T = loadTown(slug);
    for (const e of T.events.filter(x => x.special && x.when && x.when.length)) {
      const from = e.when[0].from, last = e.when[e.when.length - 1], to = last.to || last.from;
      if (to < today) continue;
      const place = (T.venues[e.v] && T.venues[e.v][0]) || '';
      const k = county.id + '|' + e.t + '|' + place;
      const town = { slug, name: T.label, link: `/${slug}/#e=${encodeURIComponent(slugify(e.t) + '--' + e.v)}&d=${from}` };
      const segs = e.when.map(w => [w.from, w.to || w.from]).filter(sg => sg[1] >= today);
      const cur = bigItems.get(k);
      if (cur) {
        if (!cur.towns.some(t => t.slug === slug)) cur.towns.push(town);
        if (from < cur.from) cur.from = from;
        if (to > cur.to) cur.to = to;
        for (const sg of segs) if (!cur.segs.some(x => x[0] === sg[0] && x[1] === sg[1])) cur.segs.push(sg);
        cur.segs.sort((a, b) => a[0] < b[0] ? -1 : 1);
      } else {
        bigItems.set(k, Object.assign({ county: county.id, g: e.special, t: e.t }, ES[e.t] ? { es: ES[e.t] } : {}, { from, to, segs, place, free: !!e.free, towns: [town] }));
      }
    }
  }
}
const bigdays = {
  updated: today,
  counties: COUNTIES.map(({ id, en, es, towns }) => ({ id, en, es, towns: towns.filter(t => TOWNS.includes(t)) })),
  items: [...bigItems.values()].map(i => Object.assign(i, { next: (i.segs[0] || [i.from])[0] })).sort((a, b) => a.next < b.next ? -1 : a.next > b.next ? 1 : a.t.localeCompare(b.t)),
};
fs.writeFileSync(path.join(__dirname, 'bigdays.json'), JSON.stringify(bigdays) + '\n');
console.log('shared/bigdays.json written:', COUNTIES.map(c => `${c.en}: ${bigdays.items.filter(i => i.county === c.id).length}`).join(' · '));

/* ---------- homepage "Near you" master calendar feed ----------
   Also writes shared/allevents.json: every event from every town that still
   has a date today or later, in the same compact schedule format the town
   pages use (s = weekly rules, when = dated runs, x = skipped dates), plus each
   town's center from shared/zips.json for distance. The homepage expands the
   schedules in the browser, so this file stays small. */
const ZIPS = JSON.parse(fs.readFileSync(path.join(__dirname, 'zips.json'), 'utf8'));
const allTowns = {}, allEv = [];
const hasFuture = e => (e.when || []).some(w => (w.to || w.from) >= today) || (e.s || []).some(r => r[3] >= today);
for (const slug of TOWNS) {
  const T = loadTown(slug);
  allTowns[slug] = { n: T.label, ll: ZIPS.towns[slug] || null };
  const VM = T.venueMeta || {};
  for (const e of T.events) {
    if (!hasFuture(e)) continue;
    const v = T.venues[e.v] || [e.v, ''];
    const o = { tw: slug, t: e.t, p: v[0], id: slugify(e.t) + '--' + e.v, a: e.a || [] };
    if (e.free) o.f = 1; if (e.drop) o.d = 1; if (e.special) o.sp = e.special;
    if ((VM[e.v] || [])[1] === 1) o.in = 1;
    if (e.ages) { o.ag = e.ages; if (ES[e.ages]) o.age = ES[e.ages]; }
    if (e.price && !e.free) { o.pr = e.price; if (ES[e.price]) o.pre = ES[e.price]; }
    if (ES[e.t]) o.te = ES[e.t];
    if (e.s) o.s = e.s.filter(r => r[3] >= today);
    if (e.when) o.w = e.when.filter(w => (w.to || w.from) >= today);
    if (e.x) o.x = e.x.filter(k => k >= today);
    if (e.check) o.ck = 1;
    allEv.push(o);
  }
}
fs.writeFileSync(path.join(__dirname, 'allevents.json'), JSON.stringify({ updated: today, towns: allTowns, ev: allEv }) + '\n');
console.log(`shared/allevents.json written: ${allEv.length} events from ${Object.keys(allTowns).length} towns`);
