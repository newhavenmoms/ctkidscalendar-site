#!/usr/bin/env node
'use strict';
/* Refresh report — what needs attention across all towns.
   Usage:  node tools/refresh-report.js            (writes tools/refresh-report.md)
           node tools/refresh-report.js --days 45  (look-ahead window, default 30)
   Sections:
     1. Thinnest towns (fewest listings in the next 60 days)
     2. "Date not announced yet" cards to recheck
     3. Recurring listings that end soon (new sessions to look for)
     4. Coverage gaps by category (what to search for next; see tools/PLAYBOOK.md)
     5. calendarThrough dates that need extending */
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..');
const TOWNS = fs.readdirSync(ROOT).filter(d => d !== 'shared' && d !== 'tools' && fs.existsSync(path.join(ROOT, d, 'index.html')) && fs.readFileSync(path.join(ROOT, d, 'index.html'), 'utf8').includes('window.TOWN = {')).sort();
const argDays = process.argv.indexOf('--days');
const SOON = argDays > -1 ? parseInt(process.argv[argDays + 1], 10) : 30;

const pad = n => String(n).padStart(2, '0');
const key = d => `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
const add = (d, n) => { const x = new Date(d); x.setDate(x.getDate() + n); return x; };
const today = new Date(); const T0 = key(today), TSOON = key(add(today, SOON)), T60 = key(add(today, 60));
const fmt = k => { const [y, m, d] = k.split('-').map(Number); return new Date(y, m - 1, d).toLocaleDateString('en-US', { month: 'short', day: 'numeric' }); };

function load(slug) {
  const h = fs.readFileSync(path.join(ROOT, slug, 'index.html'), 'utf8');
  const a = h.indexOf('window.TOWN = {'), b = h.indexOf('\n};', a) + 2;
  const T = eval('(' + h.slice(a, b).replace('window.TOWN = ', '').replace(/;\s*$/, '') + ')');
  const imp = path.join(ROOT, 'shared', 'imports', slug + '.json');
  if (fs.existsSync(imp)) {
    const j = JSON.parse(fs.readFileSync(imp, 'utf8'));
    T.events = T.events.concat(j.events || []);
    for (const k of Object.keys(j.venues || {})) if (!T.venues[k]) T.venues[k] = j.venues[k];
  }
  const pa = h.indexOf('<div class="places">'), pb = h.indexOf('</section>', pa);
  T._places = (h.slice(pa, pb).match(/<li><strong[^>]*>[\s\S]*?<\/li>/g) || []).map(s => s.replace(/<[^>]+>/g, ' ').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim());
  T._label = (T.name || slug).replace(/ Kids Calendar$/, '');
  return T;
}

// does an event have any occurrence between a and b (inclusive keys)?
function inWindow(e, a, b) {
  if (e.when) return e.when.some(w => (w.to || w.from) >= a && w.from <= b);
  if (e.s) return e.s.some(r => r[3] >= a && r[2] <= b);
  return false;
}

const CATS = [
  ['Library programs', (T, all) => T.events.some(e => /librar/i.test((T.venues[e.v] || [''])[0]))],
  ['Parks & Rec programs', (T, all) => /parks? ?(&|and) ?rec|recreation/i.test(all)],
  ['Theater / family shows', (T, all) => T.events.some(e => e.special === 'shows') || /theat|playhouse/i.test(all)],
  ['Museum / historical society', (T, all) => /museum|historical society|history center/i.test(T._places.join(' '))],
  ['Farm', (T, all) => /farm|orchard/i.test(T._places.join(' '))],
  ['Ice skating', (T, all) => /skat|rink/i.test(all)],
  ['Splash pad', (T, all) => /splash|spray|sprinkler/i.test(T._places.join(' '))],
  ['Bookstore', (T, all) => /book(s|store|shop)\b/i.test(T._places.join(' '))],
  ['Toy store', (T, all) => /\btoy/i.test(T._places.join(' '))],
  ['Halloween Big Day', (T) => T.events.some(e => e.special === 'hw') || (T.tba || []).some(x => x.g === 'hw')],
  ['Holiday Big Day', (T) => T.events.some(e => e.special === 'hol') || (T.tba || []).some(x => x.g === 'hol')],
];

// Categories we searched for and confirmed don't exist in town (keeps them out of the gaps list).
const KNOWN_NONE = JSON.parse(fs.readFileSync(path.join(__dirname, 'known-none.json'), 'utf8'));
const rows = [], tbaOut = [], endingOut = [], gapOut = [], throughOut = [];
for (const slug of TOWNS) {
  const T = load(slug);
  const all = [JSON.stringify(T.events.map(e => [e.t, (T.venues[e.v] || [''])[0], e.blurb || ''])), JSON.stringify(T.classes.map(c => [c.n, c.where, c.blurb || ''])), T._places.join(' ')].join(' ');
  const upcoming = T.events.filter(e => inWindow(e, T0, T60)).length;
  rows.push({ slug, label: T._label, upcoming, classes: T.classes.length, places: T._places.length, tba: (T.tba || []).length });

  for (const x of T.tba || []) tbaOut.push(`| ${T._label} | ${x.t} | ${x.w || ''} | ${x.src ? `[source](${x.src})` : ''} |`);

  for (const e of T.events) {
    if (!e.s) continue;
    const end = e.s.map(r => r[3]).sort().pop();
    if (end >= T0 && end <= TSOON) endingOut.push(`| ${T._label} | ${e.t} | ${(T.venues[e.v] || [''])[0]} | ${fmt(end)} | ${e.src ? `[source](${e.src})` : ''} |`);
  }

  const none = (KNOWN_NONE[slug] || {});
  const missing = CATS.filter(([n, test]) => !test(T, all) && !none[n]).map(([n]) => n);
  const confirmed = Object.keys(none);
  if (missing.length || confirmed.length) gapOut.push(`| ${T._label} | ${missing.join(', ') || '—'} | ${confirmed.map(k => k + ' (' + none[k] + ')').join('; ') || '—'} |`);

  if (T.calendarThrough && T.calendarThrough <= T60) throughOut.push(`- ${T._label}: calendar runs through ${fmt(T.calendarThrough)} — extend it and add the next season's events.`);
}

rows.sort((a, b) => a.upcoming - b.upcoming);
const md = [
  `# Refresh report — ${today.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}`,
  '', `Generated by \`node tools/refresh-report.js\`. "Soon" means the next ${SOON} days. How to act on each section: \`tools/PLAYBOOK.md\`.`, '',
  '## 1. Thinnest towns (events in the next 60 days)', '',
  '| Town | Upcoming events | Classes | Things to do | Unannounced cards |', '|---|---|---|---|---|',
  ...rows.map(r => `| ${r.label} | ${r.upcoming} | ${r.classes} | ${r.places} | ${r.tba} |`), '',
  `## 2. "Date not announced yet" cards to recheck (${tbaOut.length})`, '',
  'Most of these get dates 4–8 weeks ahead. When one is announced, turn it into a real event.', '',
  '| Town | Card | Where | Source |', '|---|---|---|---|', ...tbaOut, '',
  `## 3. Recurring listings ending in the next ${SOON} days (${endingOut.length})`, '',
  'Look for the next session (new dates, new times) before these run out.', '',
  '| Town | Listing | Venue | Ends | Source |', '|---|---|---|---|---|', ...(endingOut.length ? endingOut : ['| — | Nothing ending soon | | | |']), '',
  '## 4. Coverage gaps by category', '',
  '"Still to search" = nothing found yet. When a search confirms a town truly has none, add it to tools/known-none.json so it stops showing up here.', '',
  '| Town | Still to search | Confirmed none in town |', '|---|---|---|', ...gapOut, '',
  '## 5. Calendar end dates', '', ...(throughOut.length ? throughOut : ['All towns run at least 60 days ahead.']), '',
].join('\n');
fs.writeFileSync(path.join(__dirname, 'refresh-report.md'), md);
console.log(`tools/refresh-report.md written — ${tbaOut.length} unannounced cards, ${endingOut.length} listings ending in ${SOON} days, ${gapOut.length} towns with category gaps.`);
