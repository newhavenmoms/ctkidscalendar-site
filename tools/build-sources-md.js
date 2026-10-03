#!/usr/bin/env node
'use strict';
/* Rebuilds tools/SOURCES.md from tools/sources-curated.json (hand-picked sources)
   plus every link the site's data currently cites (via list-sources.js).
   Usage: node tools/build-sources-md.js */
const fs = require('fs'), path = require('path');
const cur = JSON.parse(fs.readFileSync(path.join(__dirname, 'sources-curated.json'), 'utf8'));
const cited = require('./list-sources.js');
const host = u => { try { return new URL(u).hostname.replace(/^www\./, ''); } catch { return ''; } };
const esc = s => String(s || '').replace(/\|/g, '/');
let md = cur.header + '\n\n---\n';
for (const [slug, t] of Object.entries(cur.towns)) {
  md += `\n## ${t.title}\n\n**Check regularly**\n\n`;
  if (t.check.length) {
    md += '| Source | What to look for / how often | Last checked |\n|---|---|---|\n';
    for (const r of t.check) md += `| [${esc(r.name)}](${r.url}) | ${esc(r.how)} | ${esc(r.last)} |\n`;
  } else md += '_None picked yet; start from the cited list below._\n';
  for (const x of t.extras || []) md += '\n' + x + '\n';
  const curatedHosts = new Set(t.check.map(r => host(r.url)));
  const rest = (cited[slug] || []).filter(s => !curatedHosts.has(s.site));
  md += `\n**Also cited in your data** (${rest.length} more site(s), busiest first)\n\n`;
  for (const s of rest) {
    const n = [s.events && `${s.events} event(s)`, s.classes && `${s.classes} class card(s)`].filter(Boolean).join(', ');
    md += `- [${s.site}](${s.links[0]}) — ${n}\n`;
  }
  md += '\n---\n';
}
fs.writeFileSync(path.join(__dirname, 'SOURCES.md'), md);
console.log('tools/SOURCES.md rebuilt: ' + Object.values(cur.towns).reduce((n, t) => n + t.check.length, 0) + ' curated sources across ' + Object.keys(cur.towns).length + ' towns.');
