'use strict';
/* Minimal iCalendar (.ics) reader for CT Kids Calendar imports.
   Handles: line folding, escaped text, TZID / UTC / all-day dates (converted to
   Connecticut local time), RRULE (DAILY, WEEKLY, MONTHLY by weekday or day),
   EXDATE, RECURRENCE-ID overrides, and STATUS:CANCELLED. */

const TZ = 'America/New_York';

/* ---------- date helpers (dates are 'YYYY-MM-DD' strings, times 'HH:MM') ---------- */
const pad = n => String(n).padStart(2, '0');
const toUTC = d => { const [y, m, dd] = d.split('-').map(Number); return new Date(Date.UTC(y, m - 1, dd)); };
const fromUTC = dt => `${dt.getUTCFullYear()}-${pad(dt.getUTCMonth() + 1)}-${pad(dt.getUTCDate())}`;
const addDays = (d, n) => { const dt = toUTC(d); dt.setUTCDate(dt.getUTCDate() + n); return fromUTC(dt); };
const dow = d => toUTC(d).getUTCDay();
const daysBetween = (a, b) => Math.round((toUTC(b) - toUTC(a)) / 864e5);

const nyFmt = new Intl.DateTimeFormat('en-CA', { timeZone: TZ, year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit', hourCycle: 'h23' });
function nyParts(date) {
  const p = Object.fromEntries(nyFmt.formatToParts(date).map(x => [x.type, x.value]));
  return { date: `${p.year}-${p.month}-${p.day}`, time: `${p.hour}:${p.minute}` };
}
function todayNY() { return nyParts(new Date()).date; }

/* Wall-clock time in some IANA zone -> UTC Date (two-pass offset correction). */
function wallToUTC(y, mo, d, h, mi, tz) {
  let guess = Date.UTC(y, mo - 1, d, h, mi);
  for (let i = 0; i < 2; i++) {
    const f = new Intl.DateTimeFormat('en-US', { timeZone: tz, year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', hourCycle: 'h23' });
    const p = Object.fromEntries(f.formatToParts(new Date(guess)).map(x => [x.type, x.value]));
    const asIf = Date.UTC(+p.year, +p.month - 1, +p.day, +p.hour, +p.minute);
    guess -= asIf - Date.UTC(y, mo - 1, d, h, mi);
  }
  return new Date(guess);
}

const warnings = [];
function parseDateValue(value, params) {
  value = (value || '').trim();
  if (params.VALUE === 'DATE' || /^\d{8}$/.test(value)) {
    return { date: `${value.slice(0, 4)}-${value.slice(4, 6)}-${value.slice(6, 8)}`, time: null };
  }
  const m = value.match(/^(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})?(Z)?$/);
  if (!m) return null;
  const [, y, mo, d, h, mi, , z] = m;
  if (z) return nyParts(new Date(Date.UTC(+y, mo - 1, +d, +h, +mi)));
  const tz = params.TZID;
  if (!tz || /New_York|Eastern|US\/Eastern/i.test(tz)) return { date: `${y}-${mo}-${d}`, time: `${h}:${mi}` };
  try { return nyParts(wallToUTC(+y, +mo, +d, +h, +mi, tz)); }
  catch (e) { warnings.push(`Unknown time zone "${tz}"; treated as Connecticut time.`); return { date: `${y}-${mo}-${d}`, time: `${h}:${mi}` }; }
}

/* ---------- parsing ---------- */
function unfold(text) { return text.replace(/\r\n?/g, '\n').replace(/\n[ \t]/g, ''); }
function unescapeText(v) { return v.replace(/\\n/gi, '\n').replace(/\\([,;\\:])/g, '$1'); }
function parseLine(line) {
  let i = 0, inQ = false;
  for (; i < line.length; i++) { const c = line[i]; if (c === '"') inQ = !inQ; else if (c === ':' && !inQ) break; }
  const head = line.slice(0, i), value = line.slice(i + 1);
  const parts = head.split(';');
  const name = parts.shift().toUpperCase();
  const params = {};
  for (const p of parts) { const j = p.indexOf('='); if (j > 0) params[p.slice(0, j).toUpperCase()] = p.slice(j + 1).replace(/^"|"$/g, ''); }
  return { name, params, value };
}

function parseICS(text) {
  const lines = unfold(text).split('\n');
  const events = [];
  let cur = null, depth = 0;
  for (const raw of lines) {
    const line = raw.trimEnd();
    if (!line) continue;
    if (line === 'BEGIN:VEVENT') { cur = { categories: [], exdates: [] }; depth = 0; continue; }
    if (!cur) continue;
    if (line.startsWith('BEGIN:')) { depth++; continue; }          // e.g. VALARM inside VEVENT
    if (line.startsWith('END:') && line !== 'END:VEVENT') { depth--; continue; }
    if (line === 'END:VEVENT') { if (cur.dtstart) events.push(cur); cur = null; continue; }
    if (depth > 0) continue;
    const { name, params, value } = parseLine(line);
    switch (name) {
      case 'UID': cur.uid = value; break;
      case 'SUMMARY': cur.summary = unescapeText(value).trim(); break;
      case 'DESCRIPTION': cur.description = unescapeText(value); break;
      case 'LOCATION': cur.location = unescapeText(value).trim(); break;
      case 'URL': cur.url = value.trim(); break;
      case 'STATUS': cur.status = value.trim().toUpperCase(); break;
      case 'CATEGORIES': cur.categories.push(...unescapeText(value).split(',').map(s => s.trim()).filter(Boolean)); break;
      case 'DTSTART': cur.dtstart = parseDateValue(value, params); break;
      case 'DTEND': cur.dtend = parseDateValue(value, params); cur.dtendIsDate = !!(cur.dtend && cur.dtend.time === null); break;
      case 'RRULE': cur.rrule = Object.fromEntries(value.split(';').map(kv => kv.split('=')).map(([k, v]) => [k.toUpperCase(), v])); break;
      case 'EXDATE': for (const v of value.split(',')) { const d = parseDateValue(v, params); if (d) cur.exdates.push(d.date); } break;
      case 'RECURRENCE-ID': cur.recurrenceId = (parseDateValue(value, params) || {}).date; break;
      default: if (name.startsWith('X-') && /AUDIENCE|AGE/i.test(name)) cur.categories.push(unescapeText(value).trim());
    }
  }
  return events;
}

/* ---------- recurrence expansion ---------- */
const BYDAY = { SU: 0, MO: 1, TU: 2, WE: 3, TH: 4, FR: 5, SA: 6 };

function ruleDates(start, rule, windowEnd) {
  const freq = (rule.FREQ || '').toUpperCase();
  const interval = +(rule.INTERVAL || 1);
  const until = rule.UNTIL ? parseDateValue(rule.UNTIL, {}).date : null;
  const count = rule.COUNT ? +rule.COUNT : Infinity;
  const stop = until && until < windowEnd ? until : windowEnd;
  const out = [];
  const push = d => { if (d >= start && d <= stop && out.length < count) out.push(d); };
  if (freq === 'DAILY') {
    for (let d = start; d <= stop && out.length < count; d = addDays(d, interval)) push(d);
  } else if (freq === 'WEEKLY') {
    const days = rule.BYDAY ? rule.BYDAY.split(',').map(s => BYDAY[s.slice(-2)]) : [dow(start)];
    let weekStart = addDays(start, -dow(start));
    for (; weekStart <= stop && out.length < count; weekStart = addDays(weekStart, 7 * interval)) {
      for (const wd of days.slice().sort()) push(addDays(weekStart, wd));
    }
  } else if (freq === 'MONTHLY') {
    let [y, m] = start.split('-').map(Number);
    for (let guard = 0; guard < 60 && out.length < count; guard++) {
      const first = `${y}-${pad(m)}-01`;
      if (first > stop) break;
      if (rule.BYDAY) {
        for (const tok of rule.BYDAY.split(',')) {
          const nth = parseInt(tok, 10) || 1, wd = BYDAY[tok.slice(-2)];
          if (nth > 0) { const d = addDays(first, ((wd - dow(first) + 7) % 7) + 7 * (nth - 1)); if (d.slice(0, 7) === first.slice(0, 7)) push(d); }
          else { const last = addDays(`${m === 12 ? y + 1 : y}-${pad(m === 12 ? 1 : m + 1)}-01`, -1); push(addDays(last, -((dow(last) - wd + 7) % 7))); }
        }
      } else {
        const dd = rule.BYMONTHDAY ? +rule.BYMONTHDAY : +start.slice(8);
        const d = `${y}-${pad(m)}-${pad(dd)}`; if (d.slice(5, 7) === pad(m)) push(d);
      }
      m += interval; while (m > 12) { m -= 12; y++; }
    }
  } else {
    warnings.push(`Unsupported repeat rule FREQ=${freq}; only the first date was used.`);
    push(start);
  }
  return out.sort();
}

/* Turn parsed VEVENTs into flat occurrences within [from, to]. */
function occurrences(vevents, from, to) {
  const overrides = new Map();             // uid -> Set(dates replaced by a RECURRENCE-ID event)
  for (const e of vevents) if (e.recurrenceId) { if (!overrides.has(e.uid)) overrides.set(e.uid, new Set()); overrides.get(e.uid).add(e.recurrenceId); }
  const out = [];
  for (const e of vevents) {
    if (!e.dtstart || !e.summary) continue;
    const start = e.dtstart;
    let end = e.dtend || null;
    // all-day DTEND is exclusive
    let spanDays = 0;
    if (end) spanDays = Math.max(0, daysBetween(start.date, end.date) - (start.time === null ? 1 : 0));
    const base = { uid: e.uid, title: e.summary, description: e.description || '', location: e.location || '', url: e.url || '', categories: e.categories, cancelled: e.status === 'CANCELLED' };
    let dates = e.rrule && !e.recurrenceId ? ruleDates(start.date, e.rrule, to) : [start.date];
    const ex = new Set([...(e.exdates || []), ...(!e.recurrenceId && overrides.has(e.uid) ? overrides.get(e.uid) : [])]);
    for (const d of dates) {
      if (ex.has(d)) continue;
      const endDate = addDays(d, spanDays);
      if (endDate < from || d > to) continue;
      out.push({ ...base, date: d, endDate: spanDays ? endDate : null, start: start.time, end: end && end.time && !spanDays ? end.time : null });
    }
  }
  return out;
}

module.exports = { parseICS, occurrences, todayNY, addDays, dow, daysBetween, warnings };
