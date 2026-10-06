"""Builds a new town page from shared/page-template.html and a spec module.
Usage: python3 tools/newtowns/build_town.py guilford
Each spec (tools/newtowns/<slug>.py) defines TOWN (name, accent, hoods, venues, venueMeta,
events, tba, classes, library), PLACES {out|rain|drive: [(name, en, es)]}, and ES {en: es}
for every new blurb/ages/price string. The script writes <slug>/index.html and merges ES
into shared/data-es.js. Re-running overwrites the page (edit the spec, not the page)."""
import json, sys, importlib.util, os, html
ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
slug = sys.argv[1]
spec_path = os.path.join(os.path.dirname(__file__), slug + '.py')
spec = importlib.util.spec_from_file_location('spec', spec_path); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
T = S.TOWN; name = T['display']; url = f'https://ctkidscalendar.com/{slug}/'
tpl = open(os.path.join(ROOT, 'shared', 'page-template.html')).read()
page = (tpl.replace('{{TOWN}}', name).replace('{{URL}}', url).replace('{{ACCENT_HEX}}', T['accent'])
        .replace('{{DOMAIN_DISPLAY}}', f'ctkidscalendar.com/{slug}').replace('{{MONTH_YEAR}}', 'October 2026'))
data = {'name': f'{name} Kids Calendar', 'townLabel': f'{name}, CT', 'url': url, 'email': '', 'instagram': '',
        'calendarThrough': '2026-12-31', 'venues': T['venues'], 'venueMeta': T['venueMeta'], 'hoods': T.get('hoods', []),
        'events': T['events'], 'tba': T.get('tba', []), 'classes': T.get('classes', []), 'library': T.get('library'), 'extraResources': []}
a = page.index('window.TOWN = {'); b = page.index('\n};', a) + 3
page = page[:a] + 'window.TOWN = ' + json.dumps(data, indent=1, ensure_ascii=False) + ';' + page[b:]
esc = lambda s: html.escape(s, quote=True)
def lis(items):
    return ''.join(f'\n            <li><strong>{esc(n)}</strong><span data-es="{esc(es)}">{esc(en)}</span></li>' for n, en, es in items) + '\n          '
for key, marker in [('out', '<!-- <li><strong>Park name</strong><span>One or two lines about it.</span></li> -->'), ('rain', None), ('drive', None)]:
    pass
pa = page.index('<div class="places">')
segs = page[pa:].split('<ul>', 3)  # [before, ul1..., ul2..., ul3...]
out = segs[0]
for i, key in enumerate(['out', 'rain', 'drive']):
    rest = segs[i + 1]; end = rest.index('</ul>')
    out += '<ul>' + lis(S.PLACES[key]) + rest[end:]
page = page[:pa] + out
os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
open(os.path.join(ROOT, slug, 'index.html'), 'w').write(page)
# Spanish strings
p = os.path.join(ROOT, 'shared', 'data-es.js'); js = open(p).read()
ins = ''.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False) + ',\n' for k, v in S.ES.items() if json.dumps(k, ensure_ascii=False) + ':' not in js)
open(p, 'w').write(js.replace('var C={\n', 'var C={\n' + ins, 1))
# check every event/tba/class string has Spanish
allk = set(S.ES) | set()
missing = []
for e in T['events']:
    for f in ('blurb', 'ages', 'price'):
        v = e.get(f)
        if v and v not in S.ES and json.dumps(v, ensure_ascii=False) + ':' not in js: missing.append(v[:50])
for x in T.get('tba', []):
    for f in ('p', 'w'):
        v = x.get(f)
        if v and v not in S.ES and json.dumps(v, ensure_ascii=False) + ':' not in js: missing.append(v[:50])
lib = T.get('library') or {}
if lib.get('desc') and lib['desc'] not in S.ES: missing.append('library desc')
print(f'{slug}: wrote page ({len(T["events"])} events, {len(T.get("tba", []))} cards, {sum(len(v) for v in S.PLACES.values())} places); Spanish added {ins.count(chr(10))}; missing ES: {missing or "none"}')

# keep the "Submit an event" form's town list in step
import re as _re
sp = os.path.join(ROOT, 'shared', 'submit.js'); sj = open(sp).read()
m = _re.search(r'const TOWNS = \[(.*?)\];', sj)
names = _re.findall(r'"([^"]+)"', m.group(1))
if name not in names:
    names = sorted(names + [name])
    sj = sj[:m.start(1)] + ','.join(json.dumps(n) for n in names) + sj[m.end(1):]
    open(sp, 'w').write(sj); print(f'added {name} to the submit form town list')
