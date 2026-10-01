'use strict';
/* Reads text copied from a LibraryCalendar (LibraryMarket) events list page —
   the calendar system used by Blackstone (Branford), Welles-Turner (Glastonbury)
   and Russell (Middletown) libraries — and returns occurrences in the same shape
   as lib/ics.js, so the importer treats a paste exactly like a calendar feed.

   Each event in the copied text looks like:
     This event is in the "Youth" group          (0+ lines)
     <short teaser title>
     <event title>
     Friday, October 2, 2026 at 11:00am - 11:30am
     <Room> at <Library name>
     Program Type: / <types>
     Age Group: / <groups>
     <description…>
     Registration Required / Waitlist / Cancelled  (optional status lines) */

const MONTHS = { january: 1, february: 2, march: 3, april: 4, may: 5, june: 6, july: 7, august: 8, september: 9, october: 10, november: 11, december: 12 };
const DATE_RE = /^(?:Sunday|Monday|Tuesday|Wednesday|Thursday|Friday|Saturday),\s+([A-Za-z]+)\s+(\d{1,2}),\s+(\d{4})\s+at\s+(\d{1,2}:\d{2}\s*[ap]m)(?:\s*[-–]\s*(\d{1,2}:\d{2}\s*[ap]m))?/i;
const STATUS_RE = /^(registration (open|required|closed|full|not required)|waitlist|cancell?ed|full|closing|in person|online|upcoming|offsite event|no registration (is )?needed)$/i;
const GROUP_RE = /^This event is in the ".*" group$/i;
// the second, detailed copy of each event on some LibraryCalendar sites starts with a bare month abbreviation ("Oct")
const STOP_RE = /^(closed for |all day|pagination$|current page|page\d|next page|last page|connect with us|disclaimer\(s\)|library branch:|(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)$|[a-z]{3}\d{1,2}\d{4}[a-z]{3}$)/i;

const pad = n => String(n).padStart(2, '0');
function to24(t) {
  const m = t.trim().toLowerCase().match(/^(\d{1,2}):(\d{2})\s*([ap])m$/);
  if (!m) return null;
  let h = +m[1] % 12; if (m[3] === 'p') h += 12;
  return `${pad(h)}:${m[2]}`;
}

function parseLibraryCalendarText(text) {
  const lines = text.replace(/\r/g, '').split('\n').map(l => l.replace(/\u200b/g, '').trim());
  const dateIdx = [];
  lines.forEach((l, i) => { if (DATE_RE.test(l)) dateIdx.push(i); });
  const out = [];
  dateIdx.forEach((di, n) => {
    const m = lines[di].match(DATE_RE);
    const month = MONTHS[m[1].toLowerCase()];
    if (!month) return;
    const date = `${m[3]}-${pad(month)}-${pad(+m[2])}`;
    // the block runs until the next event's teaser line (two lines above its date) or a stop line
    const nextDi = n + 1 < dateIdx.length ? dateIdx[n + 1] : lines.length + 2;
    let end = nextDi - 2;
    while (end > di && GROUP_RE.test(lines[end - 1])) end--;
    const block = [];
    for (let i = di + 1; i < end; i++) { if (STOP_RE.test(lines[i])) break; block.push(lines[i]); }
    const location = block[0] || '';
    const field = name => { const i = block.findIndex(l => l.toLowerCase() === name); return i >= 0 ? block[i + 1] || '' : ''; };
    const types = field('program type:'), ages = field('age group:');
    const ageIdx = block.findIndex(l => l.toLowerCase() === 'age group:');
    const rest = block.slice(ageIdx >= 0 ? ageIdx + 2 : 1);
    const status = rest.filter(l => STATUS_RE.test(l));
    let desc = rest.filter(l => l && !STATUS_RE.test(l) && !GROUP_RE.test(l) && !/:$/.test(l)).join(' ').trim();
    if (/\.\.\.$/.test(desc)) desc = desc.replace(/[^.!?]*\.\.\.$/, '').trim();   // drop the cut-off last sentence
    let title = lines[di - 1], url = '';
    const link = title.match(/^\[(.+)\]\((https?:[^)]+)\)$/);          // markdown-style paste
    if (link) { title = link[1]; url = link[2]; }
    const full = /\s*-\s*program full\s*$/i.test(title);
    title = title.replace(/\s*-\s*program full\s*$/i, '');
    out.push({
      uid: `paste-${date}-${to24(m[4])}-${title}`, title,
      description: desc + (status.length ? ' ' + status.join('. ') + '.' : ''),
      location: location.replace(/\s+at\s+.*$/i, ''), url, full,
      categories: [ages, types].filter(Boolean),
      cancelled: status.some(s => /cancel/i.test(s)) || /^cancell?ed/i.test(title),
      date, endDate: null, start: to24(m[4]), end: m[5] ? to24(m[5]) : null,
    });
  });
  return out;
}

module.exports = { parseLibraryCalendarText };
