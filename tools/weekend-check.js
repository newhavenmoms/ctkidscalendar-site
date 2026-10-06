#!/usr/bin/env node
'use strict';
/* Weekend check: for each town (or the towns given), count calendar items on each
   of the next N weekends (Sat+Sun) using shared/allevents.json.
   Usage: node tools/weekend-check.js [weeks=6] [town ...]
   Rebuild allevents.json first: node shared/build-stats.js */
const fs=require('fs'),path=require('path');
const A=JSON.parse(fs.readFileSync(path.join(__dirname,'..','shared','allevents.json'),'utf8'));
const args=process.argv.slice(2);const weeks=/^\d+$/.test(args[0]||'')?+args.shift():6;const towns=args.length?args:Object.keys(A.towns);
const pad=n=>String(n).padStart(2,'0'),key=d=>`${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;
const pd=k=>{const[y,m,d]=k.split('-').map(Number);return new Date(y,m-1,d)};
const on=(e,d)=>{const k=key(d);if((e.x||[]).includes(k))return false;
  if((e.s||[]).some(r=>d.getDay()===r[0]&&k>=r[2]&&k<=r[3]&&(!r[4]||Math.ceil(d.getDate()/7)===r[4])))return true;
  return (e.w||[]).some(w=>k>=w.from&&k<=(w.to||w.from))};
const t0=pd(A.updated);const sat=new Date(t0);sat.setDate(t0.getDate()+((6-t0.getDay()+7)%7));
const rows=[];
for(const t of towns){const evs=A.ev.filter(e=>e.tw===t);const out=[];
  for(let i=0;i<weeks;i++){const s=new Date(sat);s.setDate(sat.getDate()+7*i);const u=new Date(s);u.setDate(s.getDate()+1);
    const titles=[...new Set(evs.filter(e=>on(e,s)||on(e,u)).map(e=>e.t))];out.push({wk:key(s),n:titles.length,titles})}
  rows.push({t,out})}
for(const r of rows){console.log(`\n${A.towns[r.t].n}`);for(const w of r.out)console.log(`  ${w.wk}  ${String(w.n).padStart(2)} ${w.n?'':' ← EMPTY'}${w.n>0&&w.n<2?' ← thin':''}  ${w.titles.slice(0,4).join(' · ')}`)}
