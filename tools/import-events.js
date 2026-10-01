#!/usr/bin/env node
'use strict';
/* CT Kids Calendar — calendar-feed importer (step 1 of 2: make a draft).

   Usage (from the repo root):
     node tools/import-events.js <town>                 fetch every feed listed for <town> in tools/sources.json
     node tools/import-events.js <town> --paste page1.txt,page2.txt   text copied from a LibraryCalendar list page
     node tools/import-events.js <town> --file feed.ics [--source "Library name"]
                                                        use a downloaded .ics file instead of fetching
     Options: --from YYYY-MM-DD  (default: today)   --to YYYY-MM-DD (default: the town's calendarThrough)

   Writes, without touching the live site:
     tools/drafts/<town>.draft.json    the candidate events (each has "keep": true/false)
     tools/drafts/<town>.review.md     a readable, numbered list to check against the source

   Then review, and publish with:  node tools/approve-imports.js <town>   (see tools/README.md) */

const fs = require('fs');
const path = require('path');
const ics = require('./lib/ics');
const { parseLibraryCalendarText } = require('./lib/librarycalendar-text');

const ROOT = path.join(__dirname, '..');
const args = process.argv.slice(2);
const slug = args.find(a => !a.startsWith('--') && !isOptValue(a));
function isOptValue(a) { const i = args.indexOf(a); return i > 0 && args[i - 1].startsWith('--'); }
const opt = name => { const i = args.indexOf('--' + name); return i >= 0 ? args[i + 1] : null; };

if (!slug) { console.error('Usage: node tools/import-events.js <town> [--file feed.ics] [--source "Name"]'); process.exit(1); }

/* ---------- load town data (hand-curated + already-imported) ---------- */
function loadTown(s) {
  const file = path.join(ROOT, s, 'index.html');
  if (!fs.existsSync(file)) throw new Error(`No town page at ${s}/index.html`);
  const html = fs.readFileSync(file, 'utf8');
  const a = html.indexOf('window.TOWN = {'), b = html.indexOf('\n};', a) + 2;
  return eval('(' + html.slice(a, b).replace('window.TOWN = ', '').replace(/;\s*$/, '') + ')');
}
const TOWN = loadTown(slug);
const importsFile = path.join(ROOT, 'shared', 'imports', slug + '.json');
const prior = fs.existsSync(importsFile) ? JSON.parse(fs.readFileSync(importsFile, 'utf8')) : { events: [] };

const config = JSON.parse(fs.readFileSync(path.join(__dirname, 'sources.json'), 'utf8'));
let sources = (config.towns[slug] || []).slice();
if (opt('paste')) {
  const want = opt('source');
  const base = want ? sources.find(s => s.name === want) : sources[0];
  if (!base) { console.error(`No source configured for ${slug} in tools/sources.json.`); process.exit(1); }
  sources = [{ ...base, paste: opt('paste').split(',') }];
} else if (opt('file')) {
  const want = opt('source');
  const base = want ? sources.find(s => s.name === want) : sources[0];
  if (!base) { console.error(`No source ${want ? `"${want}" ` : ''}configured for ${slug} in tools/sources.json.`); process.exit(1); }
  sources = [{ ...base, file: opt('file') }];
}
if (!sources.length) { console.error(`No sources configured for "${slug}" in tools/sources.json.`); process.exit(1); }

const nowNY = () => new Intl.DateTimeFormat('en-CA', { timeZone: 'America/New_York', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' }).format(new Date());
const FROM = opt('from') || ics.todayNY();
const TO = opt('to') || TOWN.calendarThrough || ics.addDays(FROM, 92);

/* ---------- classification ---------- */
const KID = /\b(story ?times?|stories|story lab|bab(y|ies)|infants?|lapsit|toddlers?|twos|ones\b|preschool(ers)?|pre-?k|kindergarten|kids?|child(ren)?|famil(y|ies)|tweens?|teens?|grades?\s*(k|pre|\d)|elementary|lego|homework|puppet|sensory|playgroup|play ?time|stay (and|&) play|bounce|rhyme|sing-?along|ages?\s*\d)/i;
const ADULT = /\b(adults?( only)?|for grown-?ups|seniors?|18\+|21\+|ages? 18|medicare|retire(ment|es)|tax(es)? (help|prep)|job seekers?|resume|genealogy|family history|trustees|board (of )?(trustees|meeting)|friends of the library meeting|aarp|wine|beer|cocktail)\b/i;
const STRONG_ADULT = /\b(genealogy|family history|ancestry|medicare|estate planning|retirement)\b/i;
const CLOSED = /\b(library closed|closed|closing|closes early|cancell?ed|postponed)\b/i;

function classify(o) {
  const title = o.title, cats = o.categories.join(' '), desc = o.description;
  if (o.cancelled || CLOSED.test(title)) return { kid: false, reason: 'cancelled or closed' };
  const kidTitle = KID.test(title), kidCat = KID.test(cats);
  const adultTitle = ADULT.test(title), adultCat = ADULT.test(cats);
  const kidTitleStrong = KID.test(title.replace(/\bfamil(y|ies)\b/gi, ''));
  if (STRONG_ADULT.test(title + ' ' + desc) && !kidTitleStrong) return { kid: false, reason: 'adult program' };
  if ((adultTitle || adultCat) && !kidTitleStrong) return { kid: false, reason: 'adult program' };
  if (kidTitle || kidCat) return { kid: true, confident: true, reason: kidTitle ? 'kid words in title' : 'kids/family category' };
  if (KID.test(desc) && !ADULT.test(desc)) return { kid: true, confident: false, reason: 'only the description mentions kids' };
  return { kid: false, reason: 'no sign it is for kids' };
}

const AGE_RULES = [
  ['baby', /\b(bab(y|ies)|infants?|lapsit|newborns?|(0|birth)\s*[-–to]+\s*(12|18|24)\s*mo(nths?)?)\b/i],
  ['toddler', /\b(toddlers?|twos|ones|walkers|(12|15|18)\s*[-–]\s*(24|35|36)\s*mo(nths?)?|ages?\s*[12]\s*[-–]\s*[23])\b/i],
  ['preschool', /\b(preschool(ers)?|pre-?k|ages?\s*[2-4]\s*[-–]\s*[5-6]|ages?\s*3\b)/i],
  ['big', /\b(grades?|school[- ]age|k\s*[-–]\s*\d|tweens?|teens?|elementary|ages?\s*(6|7|8|9|10|11|12)|lego|homework|chess|coding|steam|stem|minecraft|d&d|dungeons)\b/i],
];
function groupsFromRange(text) {
  const m = text.match(/\b(?:ages?\s*)?(\d+)\s*(?:[-–]|to)\s*(\d+)\s*(months?|mos?\.?)\b/i);
  if (m) { const lo = +m[1], hi = +m[2], g = []; if (lo < 12) g.push('baby'); if (hi > 12) g.push('toddler'); if (hi > 36) g.push('preschool'); return g; }
  const y = text.match(/\bages?\s*(\d+)\s*(?:[-–]|to)\s*(\d+)\b/i) || text.match(/\bbirth\s*(?:to|[-–])\s*(?:age\s*)?()(\d+)\b/i);
  if (y) { const lo = +(y[1] || 0), hi = +y[2], g = [];
    if (lo < 1) g.push('baby'); if (lo <= 2 && hi >= 1) g.push('toddler'); if (lo <= 5 && hi >= 3) g.push('preschool'); if (hi >= 6) g.push('big'); return g; }
  const gr = text.match(/\bgrades?\s*(pre-?k|k|\d+)/i);
  if (gr) return /pre/i.test(gr[1]) ? ['preschool', 'big'] : ['big'];
  return null;
}
function upTo(text) {
  let m = text.match(/\bup to (\d+)\s*months?\b/i); if (m) return +m[1] > 12 ? ['baby', 'toddler'] : ['baby'];
  m = text.match(/\bup to age (\d+)\b/i); if (m) return groupsFromRange(`ages 0-${m[1]}`);
  return null;
}
function ageGroups(text) {
  const [title] = text.split('\n');
  const r = upTo(title) || groupsFromRange(title) || upTo(text) || groupsFromRange(text);
  if (r && r.length) return { a: r, guessed: false };
  const a = AGE_RULES.filter(([, re]) => re.test(text)).map(([g]) => g);
  return a.length ? { a, guessed: false } : { a: ['toddler', 'preschool', 'big'], guessed: true };
}
function agesLabel(text) {
  if (/\ball ages\b/i.test(text.split('\n')[0])) return 'All ages';
  const t = text.split('\n')[0];
  let u = t.match(/\bup to (\d+\s*months|age \d+)\b/i); if (u) return 'Up to ' + u[1];
  u = t.match(/\b(grades?\s*(?:k|pre-?k|\d+)(?:\s*(?:[-–]|to)\s*\d+)?(?:\s*(?:and up|\+))?|ages?\s*\d+\s*(?:[-–]|to)\s*\d+|ages?\s*\d+\s*(?:and up|\+))\b/i);
  if (u) { const v = u[1].replace(/\s*(?:-|to)\s*(?=\d)/g, '–').replace(/\s+/g, ' '); return (v.charAt(0).toUpperCase() + v.slice(1)).replace(/\b(grades?\s*)k\b/i, '$1K'); }
  const w = text.match(/\b((?:walkers|birth|newborns?|babies|\d+\s*months?)\s*(?:to|[-–])\s*(?:age\s*)?\d+(?:\s*(?:months|years))?)\b/i);
  if (w) { const s = w[1].replace(/\s*-\s*/g, '–').replace(/\s+/g, ' '); return s.charAt(0).toUpperCase() + s.slice(1); }
  const m = text.match(/\b(ages?\s*\d+\s*(?:[-–]\s*\d+|\+|and up)?(?:\s*(?:months|years))?|\d+\s*[-–]\s*\d+\s*months|birth\s*(?:to|[-–])\s*\d+(?:\s*(?:months|years))?|grades?\s*(?:k|pre-?k|\d+)(?:\s*[-–]\s*\d+)?)\b/i);
  if (!m) return null;
  let s = m[1].replace(/\s*-\s*/g, '–').replace(/\s+/g, ' ');
  return s.charAt(0).toUpperCase() + s.slice(1);
}

function cleanText(html) {
  return (html || '').replace(/<br\s*\/?>|<\/p>|<\/li>/gi, '\n').replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&#0?39;|&rsquo;|&lsquo;/g, "'").replace(/&quot;|&ldquo;|&rdquo;/g, '"').replace(/&ndash;/g, '–').replace(/&mdash;/g, '—').replace(/&[a-z]+;/g, ' ')
    .replace(/[ \t]+/g, ' ').replace(/\s*\n\s*/g, '\n').trim();
}
function blurbFrom(desc, max = 260) {
  const sentences = cleanText(desc).replace(/\n+/g, ' ').match(/[^.!?]+[.!?]+(\s|$)|[^.!?]+$/g) || [];
  let out = '';
  for (const s of sentences) { if ((out + s).length > max && out) break; out += s; }
  out = out.trim();
  return out.length > max ? out.slice(0, max - 1).replace(/\s+\S*$/, '') + '…' : out;
}
function editDistance(a, b) {
  const d = Array.from({ length: a.length + 1 }, (_, i) => [i]);
  for (let j = 1; j <= b.length; j++) d[0][j] = j;
  for (let i = 1; i <= a.length; i++) for (let j = 1; j <= b.length; j++)
    d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
  return d[a.length][b.length];
}
const normTitle = t => t.toLowerCase().replace(/\(.*?\)/g, '').replace(/[-–—:]\s*(registration required|register|drop-?in|virtual)\s*$/i, '').replace(/&/g, 'and').replace(/[^a-z0-9]+/g, ' ').trim();

/* ---------- main ---------- */
async function main() {
  const report = { generated: new Date().toISOString(), town: slug, from: FROM, to: TO, sources: [], candidates: [], duplicates: [], skipped: {} };
  const existing = TOWN.events.map(e => ({ e, key: normTitle(e.t), origin: 'hand-curated' }))
    .concat((prior.events || []).map(e => ({ e, key: normTitle(e.t), origin: 'imported from ' + e.imp })));

  for (const src of sources) {
    let text, occ;
    if (src.paste) {
      text = src.paste.map(f => fs.readFileSync(f, 'utf8')).join('\n');
      const all = parseLibraryCalendarText(text);
      if (!all.length) { console.warn(`! ${src.name}: no events found in the pasted text.`); report.sources.push({ name: src.name, error: 'no events found in paste' }); continue; }
      const dates = all.map(o => o.date).sort();
      report.pasteRange = [dates[0], dates[dates.length - 1]];
      occ = all.filter(o => o.date >= FROM && o.date <= TO && !(o.date === ics.todayNY() && (o.end || o.start) < nowNY()));
      report.sources.push({ name: src.name + ' (pasted list)', events: all.length, occurrences: occ.length });
    } else try {
      if (src.file) text = fs.readFileSync(src.file, 'utf8');
      else {
        if (!src.url) { console.warn(`! ${src.name}: no feed URL yet in tools/sources.json — skipped.`); report.sources.push({ name: src.name, error: 'no feed URL configured' }); continue; }
        const res = await fetch(src.url.replace(/^webcal:/, 'https:'), { headers: { 'User-Agent': 'CTKidsCalendarImporter/1.0 (+https://ctkidscalendar.com)' } });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        text = await res.text();
      }
    } catch (err) {
      console.warn(`! ${src.name}: couldn't read the feed (${err.message}). Download it in a browser and use --file.`);
      report.sources.push({ name: src.name, error: err.message }); continue;
    }
    if (!src.paste) {
    if (!/BEGIN:VCALENDAR/.test(text)) { console.warn(`! ${src.name}: that isn't an iCal feed (no BEGIN:VCALENDAR).`); report.sources.push({ name: src.name, error: 'not an iCal feed' }); continue; }

    const vevents = ics.parseICS(text);
    occ = ics.occurrences(vevents, FROM, TO).filter(o => !(o.date === ics.todayNY() && !o.endDate && (o.end || o.start) && (o.end || o.start) < nowNY()));
    report.sources.push({ name: src.name, events: vevents.length, occurrences: occ.length });
    }

    // classify each occurrence; group the kid ones by title
    const groups = new Map();
    for (const o of occ) {
      const c = src.kidsOnly && !CLOSED.test(o.title) && !o.cancelled ? { kid: true, confident: true, reason: 'feed is kids-only' } : classify(o);
      if (!c.kid) { const k = `${o.title} — ${c.reason}`; report.skipped[k] = (report.skipped[k] || 0) + 1; continue; }
      const key = normTitle(o.title);
      if (!groups.has(key)) groups.set(key, { titles: {}, occ: [], confident: c.confident, reason: c.reason });
      const g = groups.get(key);
      g.titles[o.title] = (g.titles[o.title] || 0) + 1; g.occ.push(o);
      g.confident = g.confident && c.confident;
    }

    for (const [key, g] of groups) {
      const title = Object.entries(g.titles).sort((a, b) => b[1] - a[1])[0][0];
      const sample = g.occ[0];
      const text = `${title}\n${sample.categories.join(' ')}\n${cleanText(sample.description)}`;
      const { a, guessed } = ageGroups(text);
      const ages = agesLabel(text);
      const priceM = cleanText(sample.description).match(/\$\s?\d+(?:\.\d{2})?/);
      const noReg = /no (registration|sign[- ]?up)|no need to (register|sign up)|registration (is )?not (required|needed)|drop[- ]?in/i.test(text);
      const rsvp = !noReg && /regist(er|ration)\s*(is\s*)?(required|needed|opens)|must register|sign[- ]?up (is )?required|registration:\s*required/i.test(text);
      const drop = noReg;
      const blurb = blurbFrom(sample.description) || '';
      const where = sample.location && !blurb.includes(sample.location) ? sample.location : '';

      const base = {
        t: title, v: src.venue,
        ages: ages || 'See listing', a, price: priceM ? priceM[0].replace(/\s/g, '') : (src.defaultFree === false ? 'See listing' : 'Free'),
        free: !priceM && src.defaultFree !== false,
        ...(drop ? { drop: true } : {}), ...(rsvp ? { rsvp: true } : {}),
        blurb: (blurb + (where ? ` Room: ${where}.` : '')).trim() || `See the listing for details.`,
        src: sample.url || src.src, imp: src.name,
      };
      if (/hallowe+n|\bboo\b|trick[- ]or[- ]treat|costume parade|spooky/i.test(title)) base.special = 'hw';
      else if (/christmas|hanukk?ah|kwanzaa|santa|holiday (party|celebration|concert)|gingerbread|winter wonderland|tree lighting/i.test(title)) base.special = 'hol';
      const flags = [];
      if (!g.confident) flags.push(g.reason);
      if (guessed) flags.push('age groups guessed');
      if (!ages) flags.push('no age range found');
      if (!blurb) flags.push('no description in feed');

      // split into weekly slots
      const slots = new Map();
      for (const o of g.occ) {
        if (o.endDate) continue; // multi-day spans handled below
        const k = `${ics.dow(o.date)}|${o.start || ''}|${o.end || ''}`;
        if (!slots.has(k)) slots.set(k, []);
        slots.get(k).push(o.date);
      }
      const rules = [], oneOffs = [];
      for (const [k, dates] of slots) {
        const [wd, s, e] = k.split('|'); const ds = [...new Set(dates)].sort();
        const span = ics.daysBetween(ds[0], ds[ds.length - 1]) / 7 + 1;
        if (ds.length >= 3 && s && ds.length / span >= 0.5) rules.push({ wd: +wd, t: e ? [s, e] : [s], from: ds[0], to: ds[ds.length - 1], dates: ds });
        else for (const d of ds) oneOffs.push({ d, t: s ? (e ? [s, e] : [s]) : null });
      }
      // merge rules on the same weekday with the same dates (e.g. 10:15 and 11:00 sessions)
      const merged = [];
      for (const r of rules) {
        const twin = merged.find(m => m.wd === r.wd && m.dates.join() === r.dates.join());
        if (twin) twin.times.push(r.t); else merged.push({ ...r, times: [r.t] });
      }
      const candidates = [];
      if (merged.length) {
        const x = [];
        for (const r of merged) for (let d = r.from; d <= r.to; d = ics.addDays(d, 7)) if (!r.dates.includes(d)) x.push(d);
        candidates.push({ ...base, s: merged.map(r => [r.wd, r.times.sort(), r.from, r.to]), ...(x.length ? { x: [...new Set(x)].sort() } : {}) });
      }
      const timed = oneOffs.sort((p, q) => p.d.localeCompare(q.d));
      if (timed.length) candidates.push({ ...base, when: timed.map(o => ({ from: o.d, t: o.t ? [o.t] : [] })) });
      for (const o of g.occ.filter(o => o.endDate)) candidates.push({ ...base, when: [{ from: o.date, to: o.endDate, t: o.start ? [[o.start, ...(o.end ? [o.end] : [])]] : [] }] });

      // duplicate check against what the town already has
      const dup = existing.filter(x => (x.key === key || (key.length > 8 && editDistance(x.key, key) <= 2)) && x.e.v === src.venue && !(x.origin.startsWith('imported') && x.e.imp === src.name));
      for (const c of candidates) {
        if (dup.length) {
          const cur = dup[0].e;
          const curEnd = (cur.s || []).map(r => r[3]).sort().pop() || (cur.when || []).map(w => w.to || w.from).sort().pop();
          const newEnd = (c.s || []).map(r => r[3]).sort().pop() || (c.when || []).map(w => w.to || w.from).sort().pop();
          report.duplicates.push({ title: c.t, origin: dup[0].origin, note: newEnd && curEnd && newEnd > curEnd ? `feed runs to ${newEnd}, the site stops at ${curEnd} — extend it` : 'already on the site' });
          continue;
        }
        report.candidates.push({ keep: g.confident, flags, event: c });
      }
    }
  }

  report.candidates.forEach((c, i) => { c.n = i + 1; });
  const dir = path.join(__dirname, 'drafts'); fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, `${slug}.draft.json`), JSON.stringify(report, null, 2) + '\n');
  fs.writeFileSync(path.join(dir, `${slug}.review.md`), reviewMarkdown(report));
  const kept = report.candidates.filter(c => c.keep).length;
  console.log(`${slug}: ${report.candidates.length} new candidates (${kept} marked keep), ${report.duplicates.length} already on the site, ${Object.values(report.skipped).reduce((a, b) => a + b, 0)} non-kid dates skipped.`);
  if (ics.warnings.length) console.log('Warnings:\n  ' + [...new Set(ics.warnings)].join('\n  '));
  console.log(`Review: tools/drafts/${slug}.review.md   Publish: node tools/approve-imports.js ${slug}`);
}

/* ---------- review report ---------- */
const DAYS = ['Sundays', 'Mondays', 'Tuesdays', 'Wednesdays', 'Thursdays', 'Fridays', 'Saturdays'];
const fmtD = d => new Date(d + 'T12:00:00Z').toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
const fmtT = t => { if (!t) return ''; let [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'pm' : 'am'; h = h % 12 || 12; return `${h}${m ? ':' + String(m).padStart(2, '0') : ''}${ap}`; };
const fmtTimes = ts => ts.map(t => t.length > 1 ? `${fmtT(t[0])}–${fmtT(t[1])}` : fmtT(t[0])).join(' & ');
function schedule(e) {
  const parts = [];
  for (const r of e.s || []) parts.push(`${DAYS[r[0]]} ${fmtTimes(r[1])}, ${fmtD(r[2])}–${fmtD(r[3])}`);
  if (e.x) parts.push(`skips ${e.x.map(fmtD).join(', ')}`);
  for (const w of e.when || []) parts.push(`${fmtD(w.from)}${w.to ? '–' + fmtD(w.to) : ''}${w.t.length ? ' ' + fmtTimes(w.t) : ' (all day)'}`);
  return parts.join('; ');
}
function reviewMarkdown(r) {
  let md = `# Import review: ${r.town}\n\nGenerated ${r.generated.slice(0, 16).replace('T', ' ')} UTC for ${r.from} to ${r.to}.\n\n`;
  md += `Sources: ${r.sources.map(s => s.error ? `${s.name} (not read: ${s.error})` : `${s.name} (${s.occurrences} dates)`).join('; ')}\n\n`;
  md += `Check each item against its link. Items marked ✅ will be published; ⬜ won't, unless you include them.\n`;
  md += `Publish all ✅: \`node tools/approve-imports.js ${r.town}\`  ·  Pick exactly: \`--only 1,4,7\`  ·  Drop some: \`--skip 3,5\`\n\n## New events (${r.candidates.length})\n\n`;
  for (const c of r.candidates) {
    const e = c.event;
    md += `**${c.n}. ${c.keep ? '✅' : '⬜'} ${e.t}** — ${schedule(e)}\n`;
    md += `   ${e.special ? `🎃 Big day (${{ hw: 'Halloween', hol: 'Holidays', fall: 'Fall' }[e.special]}) · ` : ''}Ages: ${e.ages} (${e.a.join(', ')}) · ${e.price}${e.rsvp ? ' · registration' : ''}${e.drop ? ' · drop-in' : ''}\n`;
    md += `   ${e.blurb}\n   ${e.src}\n`;
    if (c.flags.length) md += `   ⚠️ ${c.flags.join('; ')}\n`;
    md += '\n';
  }
  md += `## Already on the site (${r.duplicates.length})\n\n` + (r.duplicates.map(d => `- ${d.title} (${d.origin}): ${d.note}`).join('\n') || '- none') + '\n\n';
  const sk = Object.entries(r.skipped).sort((a, b) => b[1] - a[1]);
  md += `## Skipped as not for kids (${sk.length} titles)\n\n` + (sk.map(([k, n]) => `- ${k}${n > 1 ? ` (${n} dates)` : ''}`).join('\n') || '- none') + '\n';
  return md;
}

main().catch(err => { console.error(err); process.exit(1); });
