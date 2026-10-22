#!/usr/bin/env python3
"""Glossar-Zusammenführung für ein Kapitel (Orchestrator).
Aufruf: python3 glossar_merge.py <kapitelnummer> <vorschlagsdatei> [--schreiben]
"""
import re, sys, csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / '07_build'))
import konfig  # noqa: E402
INTERN = tuple(f'{p}-' for p in (konfig.K.get('interne_id_praefixe') or []))
kap = sys.argv[1]; vorschlag = Path(sys.argv[2]); schreiben = '--schreiben' in sys.argv

def zeilen(tabtext):
    out = []
    for l in tabtext.splitlines():
        if l.startswith('| ') and not l.startswith('| Begriff') and not l.startswith('|---'):
            teile = [c.strip() for c in l.strip().strip('|').split(' | ')]
            if len(teile) >= 3:
                out.append([teile[0], ' | '.join(teile[1:-1]), teile[-1]])
    return out

def key(s):
    s = re.sub(r'\s*/\s*', '/', s.lower())
    for a, b in (('ä','a'),('ö','o'),('ü','u'),('ß','ss')):
        s = s.replace(a, b)
    return s

def kap_merge(a, b):
    nums = set()
    for x in (a + ',' + b).split(','):
        x = x.strip()
        if x: nums.add(x)
    def k(x):
        m = re.match(r'\d+', x); return (int(m.group()) if m else 999, x)
    return ', '.join(sorted(nums, key=k))

g = (ROOT/'GLOSSAR.md').read_text(encoding='utf-8')
kopf, rest = g.split('| Begriff | Erklärung | Kap. |\n|---|---|---|\n', 1)
eintraege = zeilen(rest)
v = vorschlag.read_text(encoding='utf-8')
teile = v.split('**Ergänzungen bestehender Einträge (Vorschlag):**')
neu = zeilen(teile[0])
erg = zeilen(teile[1]) if len(teile) > 1 else []
index = {key(e[0]): i for i, e in enumerate(eintraege)}
bericht = []
# Ergänzungen: bestehende Einträge ersetzen
for b, e, k in erg:
    i = index.get(key(b))
    if i is None:
        bericht.append(f'ERGÄNZUNG ohne Treffer, als neu behandelt: {b}'); neu.append([b, e, k]); continue
    eintraege[i][1] = e; eintraege[i][2] = kap_merge(eintraege[i][2], k)
    bericht.append(f'ergänzt: {b}')
# Neue Einträge einfügen (bestehende Reihenfolge erhalten)
for b, e, k in neu:
    if key(b) in index:
        i = index[key(b)]
        bericht.append(f'BEREITS VORHANDEN (nur Kap. ergänzt): {b}')
        eintraege[i][2] = kap_merge(eintraege[i][2], k); continue
    pos = len(eintraege)
    for j, x in enumerate(eintraege):
        if key(x[0]) > key(b): pos = j; break
    eintraege.insert(pos, [b, e, k]); index = {key(x[0]): i for i, x in enumerate(eintraege)}
    bericht.append(f'neu: {b}')
# Bestehende, im Kapitel verwendete Begriffe (Liste aus dem Vorschlagskopf)
m = re.search(r'\(u\. a\. ([^)]*)\)', teile[0])
if m:
    for b in [x.strip() for x in m.group(1).split(',')]:
        i = index.get(key(b))
        if i is None:
            # Präfixsuche (z. B. „P50/P90“)
            kand = [j for j, x in enumerate(eintraege) if key(x[0]).startswith(key(b))]
            i = kand[0] if kand else None
        if i is None: bericht.append(f'VERWENDET, aber nicht gefunden: {b}'); continue
        eintraege[i][2] = kap_merge(eintraege[i][2], kap)
# Quellen-IDs prüfen
ids = {r['id'] for r in csv.DictReader(open(ROOT/'sources/SOURCES.csv', encoding='utf-8'))}
for b, e, k in eintraege:
    for i in re.findall(r'(?<![A-Za-z0-9-])([A-Z][A-Z0-9]*[A-Z0-9]-\d{1,3}[a-z]?)(?![\d-])', e):
        if re.match(r'^(A|D|P|R|S|L|M|F|N|B)-', i) or i.startswith('A-M') or i.startswith('BK'): continue
        if i not in ids and not i.startswith(INTERN): bericht.append(f'ID nicht im Register: {i} ({b})')
# Alphabetisch sortieren (führende Anführungszeichen und Satzzeichen ignorieren, Umlaute wie Grundbuchstaben)
def sortkey(s):
    s = s.lower().lstrip('„“”"\'»«‚‘’ ')
    for a, b in (('ä','a'),('ö','o'),('ü','u'),('ß','ss')):
        s = s.replace(a, b)
    return re.sub(r'[^0-9a-z ]', '', s)
eintraege.sort(key=lambda x: sortkey(x[0]))
text = kopf + '| Begriff | Erklärung | Kap. |\n|---|---|---|\n' + '\n'.join(f'| {b} | {e} | {k} |' for b, e, k in eintraege) + '\n'
print('\n'.join(bericht)); print('Einträge:', len(eintraege))
if schreiben:
    (ROOT/'GLOSSAR.md').write_text(text, encoding='utf-8'); print('geschrieben')
