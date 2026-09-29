/* CT Kids Calendar — homepage stats builder.
   Run this (node shared/build-stats.js from the repo root) any time town
   data changes, so the homepage's headline numbers stay accurate.
   It reads window.TOWN out of each town's index.html and writes
   shared/stats.json, which the homepage fetches at runtime.

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
const TOWNS = ['stamford', 'norwalk', 'fairfield', 'ridgefield', 'west-hartford', 'new-haven', 'greenwich', 'darien', 'westport'];

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
