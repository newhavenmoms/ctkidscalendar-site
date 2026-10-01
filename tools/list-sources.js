#!/usr/bin/env node
'use strict';
/* Lists every source link a town's data currently points to, grouped by website,
   with how many events/classes cite each. Used to keep tools/SOURCES.md complete.
   Usage: node tools/list-sources.js [town]      (no town = all towns) */
const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..');
const TOWNS = ['branford','cheshire','darien','fairfield','glastonbury','greenwich','middletown','milford','new-canaan','new-haven','newtown','norwalk','ridgefield','stamford','trumbull','wallingford','west-hartford','westport'];
function load(slug) {
  const h = fs.readFileSync(path.join(ROOT, slug, 'index.html'), 'utf8');
  const a = h.indexOf('window.TOWN = {'), b = h.indexOf('\n};', a) + 2;
  const T = eval('(' + h.slice(a, b).replace('window.TOWN = ', '').replace(/;\s*$/, '') + ')');
  const imp = path.join(ROOT, 'shared', 'imports', slug + '.json');
  if (fs.existsSync(imp)) T.events = T.events.concat(JSON.parse(fs.readFileSync(imp, 'utf8')).events);
  return T;
}
const host = u => { try { return new URL(u).hostname.replace(/^www\./, ''); } catch { return null; } };
const out = {};
for (const slug of (process.argv[2] ? [process.argv[2]] : TOWNS)) {
  const T = load(slug), sites = {};
  const add = (u, kind) => { const h = host(u); if (!h) return; (sites[h] = sites[h] || { events: 0, classes: 0, links: new Set() })[kind]++; sites[h].links.add(u.split('#')[0]); };
  for (const e of T.events) add(e.src, 'events');
  for (const t of T.tba || []) add(t.src, 'events');
  for (const c of T.classes) add(c.u, 'classes');
  if (T.library && T.library.href) add(T.library.href, 'events');
  out[slug] = Object.entries(sites).sort((x, y) => (y[1].events + y[1].classes) - (x[1].events + x[1].classes))
    .map(([h, s]) => ({ site: h, events: s.events, classes: s.classes, links: [...s.links] }));
}
if (require.main === module) console.log(JSON.stringify(out, null, 1));
module.exports = out;
