#!/usr/bin/env node
'use strict';
/* Adds website links to the "Things to do anytime" lists on every town page.

   Links live in one place: shared/place-links.json
     { "links": { "Place Name": "https://…", "town-slug|Place Name": "https://…" } }
   A "town|Name" key overrides the plain name for that one town (useful when two
   towns use the same name for different places). Only add links that have been
   checked; places without their own website simply stay as plain text.

   Usage: node tools/link-places.js            (all towns; safe to re-run)
          node tools/link-places.js --report   (also list places still without a link) */

const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..');
const { links } = JSON.parse(fs.readFileSync(path.join(ROOT, 'shared', 'place-links.json'), 'utf8'));
const report = process.argv.includes('--report');
const decode = s => s.replace(/&amp;/g, '&').replace(/&#39;|&rsquo;/g, "'").replace(/&quot;/g, '"').replace(/<[^>]+>/g, '').trim();
const esc = s => s.replace(/&/g, '&amp;').replace(/"/g, '&quot;');

let total = 0, linked = 0; const missing = {};
for (const slug of fs.readdirSync(ROOT)) {
  const file = path.join(ROOT, slug, 'index.html');
  if (!fs.existsSync(file) || slug === 'shared' || slug === 'tools') continue;
  let html = fs.readFileSync(file, 'utf8');
  const a = html.indexOf('<div class="places">');
  if (a < 0) continue;
  const b = html.indexOf('</section>', a);
  let section = html.slice(a, b);
  section = section.replace(/<strong([^>]*)>([\s\S]*?)<\/strong>/g, (whole, attrs, inner) => {
    total++;
    // undo any earlier link so changes to the map (fixed or removed URLs) take effect
    let es = (attrs.match(/data-es="([^"]*)"/) || [])[1];
    const m = inner.match(/^<a href="[^"]*"[^>]*?(?: data-es="([^"]*)")?[^>]*>([\s\S]*)<\/a>$/);
    if (m) { inner = m[2]; if (m[1]) es = m[1]; }
    const name = decode(inner);
    const url = links[`${slug}|${name}`] || links[name];
    const esAttr = es ? ` data-es="${es}"` : '';
    if (!url) { (missing[slug] = missing[slug] || []).push(name); return `<strong${esAttr}>${inner}</strong>`; }
    linked++;
    return `<strong><a href="${esc(url)}" target="_blank" rel="noopener"${esAttr}>${inner}</a></strong>`;
  });
  html = html.slice(0, a) + section + html.slice(b);
  fs.writeFileSync(file, html);
}
console.log(`Linked ${linked} of ${total} "Things to do" entries.`);
if (report) for (const [t, names] of Object.entries(missing).sort()) console.log(`  ${t}: ${names.join(' · ')}`);
