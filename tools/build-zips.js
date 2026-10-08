#!/usr/bin/env node
'use strict';
/* One-time / occasional: builds shared/zips.json from the open "zipcodes" npm
   dataset (US Census ZCTA centroids).
     node tools/build-zips.js /path/to/zipcodes/package
   Output: { zips: { "06901": [lat, lng], ... }, towns: { stamford: [lat, lng], ... } }
   Includes every Connecticut ZIP plus any ZIP within 30 miles of a town we cover,
   so families just over the NY/MA/RI line can search too. Town centers are the
   average of that town's own ZIP centroids. Re-run after adding a town. */
const fs = require('fs'), path = require('path');
const pkg = process.argv[2];
if (!pkg) { console.error('Usage: node tools/build-zips.js <path-to-zipcodes-package>'); process.exit(1); }
const Z = Object.values(require(path.resolve(pkg)).codes);
const ROOT = path.join(__dirname, '..');
const TOWNS = fs.readdirSync(ROOT).filter(d => fs.existsSync(path.join(ROOT, d, 'index.html')) && !['shared', 'tools', 'school', 'schools'].includes(d));
const nameOf = slug => slug.split('-').map(w => w[0].toUpperCase() + w.slice(1)).join(' ');
const r2 = x => Math.round(x * 1e4) / 1e4;
const towns = {};
for (const slug of TOWNS) {
  const zs = Z.filter(z => z.state === 'CT' && z.city.toLowerCase() === nameOf(slug).toLowerCase());
  if (!zs.length) { console.warn('! no ZIPs found for', slug, '— add its center by hand'); continue; }
  towns[slug] = [r2(zs.reduce((s, z) => s + z.latitude, 0) / zs.length), r2(zs.reduce((s, z) => s + z.longitude, 0) / zs.length)];
}
const mi = (a, b) => { const R = 3958.8, t = Math.PI / 180, dLa = (b[0] - a[0]) * t, dLo = (b[1] - a[1]) * t;
  const h = Math.sin(dLa / 2) ** 2 + Math.cos(a[0] * t) * Math.cos(b[0] * t) * Math.sin(dLo / 2) ** 2; return 2 * R * Math.asin(Math.sqrt(h)); };
const centers = Object.values(towns);
const zips = {};
for (const z of Z) {
  if (z.latitude == null) continue;
  const ll = [r2(z.latitude), r2(z.longitude)];
  if (z.state === 'CT' || centers.some(c => mi(c, ll) <= 30)) zips[z.zip] = ll;
}
fs.writeFileSync(path.join(ROOT, 'shared', 'zips.json'), JSON.stringify({ source: 'zipcodes npm package (US Census ZCTA centroids)', zips, towns }) + '\n');
console.log(`shared/zips.json: ${Object.keys(zips).length} ZIPs, ${Object.keys(towns).length} town centers`);
