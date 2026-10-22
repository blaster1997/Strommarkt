#!/usr/bin/env python3
"""Ergänzt das Feld „kapitel“ im Quellenregister für die angegebenen IDs.

Bearbeitet wird die maßgebliche Definition jeder ID, also die Zeile, die `merge_sources.py` zuletzt liest
(SOURCES_basis.csv, dann die ```csv-Blöcke der Notizen und Modell-READMEs in derselben Reihenfolge).
Danach `python3 sources/merge_sources.py` ausführen.

Aufruf: python3 sources/kapitel_ergaenzen.py <kapitel> <ID> [<ID> …]
"""

from __future__ import annotations

import csv
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BLOCK = re.compile(r"```csv\s*\n(.*?)```", re.S)


def dateien():
    yield ROOT / "sources" / "SOURCES_basis.csv", False
    for p in sorted((ROOT / "02_research").rglob("*.md")) + sorted((ROOT / "04_models").glob("*/README.md")) \
            + sorted((ROOT / "04_models").glob("*/ANNAHMEN_VORSCHLAG.md")):
        yield p, True


def fundstellen(ids):
    """Letzte Fundstelle je ID: (Datei, Zeilentext)."""
    treffer = {}
    for pfad, ist_notiz in dateien():
        text = pfad.read_text(encoding="utf-8")
        bloecke = BLOCK.findall(text) if ist_notiz else [text]
        for block in bloecke:
            for zeile in block.splitlines():
                if not zeile.strip():
                    continue
                try:
                    felder = next(csv.reader(io.StringIO(zeile)))
                except (csv.Error, StopIteration):
                    continue
                if felder and felder[0].strip() in ids:
                    treffer[felder[0].strip()] = (pfad, zeile, felder)
    return treffer


def enthaelt(feld: str, kapitel: str) -> bool:
    teile = [t.strip() for t in re.split(r"[;,]", feld) if t.strip()]
    return any(t == kapitel or t.startswith(kapitel + ".") for t in teile)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    kapitel, ids = sys.argv[1], sys.argv[2:]
    treffer = fundstellen(set(ids))
    for i in ids:
        if i not in treffer:
            print(f"nicht gefunden: {i}")
            continue
        pfad, zeile, felder = treffer[i]
        if len(felder) < 9:
            print(f"übersprungen (weniger als 9 Felder): {i} in {pfad.relative_to(ROOT)}")
            continue
        if enthaelt(felder[8], kapitel):
            print(f"unverändert: {i} ({felder[8]})")
            continue
        felder[8] = f"{felder[8]};{kapitel}" if felder[8].strip() else kapitel
        puffer = io.StringIO()
        csv.writer(puffer, quoting=csv.QUOTE_ALL, lineterminator="").writerow(felder)
        text = pfad.read_text(encoding="utf-8")
        assert text.count(zeile) == 1, f"Zeile für {i} nicht eindeutig in {pfad}"
        pfad.write_text(text.replace(zeile, puffer.getvalue()), encoding="utf-8")
        print(f"ergänzt: {i} → {felder[8]} ({pfad.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
