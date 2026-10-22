#!/usr/bin/env python3
"""Führt das Quellenregister sources/SOURCES.csv zusammen.

Quellen: sources/SOURCES_basis.csv (Wissensstand, Fallakten, manuelle Einträge) und alle
```csv-Blöcke in Recherchenotizen unter 02_research/ und in den READMEs der Modelle unter
04_models/ (Kopfzeile gemäß CLAUDE.md §2).
Doppelte IDs: der erste Eintrag gewinnt; Konflikte werden gemeldet.

Aufruf: python3 sources/merge_sources.py
"""

from __future__ import annotations

import csv
import io
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIELDS = ["id", "titel", "herausgeber", "url", "abrufdatum", "stand_der_quelle", "typ",
          "qualität", "kapitel"]
BLOCK = re.compile(r"```csv\s*\n(.*?)```", re.S)


def read_rows(text: str, origin: str):
    reader = csv.DictReader(io.StringIO(text.strip()))
    for row in reader:
        row = {k.strip(): (v or "").strip() for k, v in row.items() if k}
        if not row.get("id"):
            continue
        row["_origin"] = origin
        yield row


def main():
    rows, seen = [], {}
    basis = ROOT / "sources" / "SOURCES_basis.csv"
    rows.extend(read_rows(basis.read_text(encoding="utf-8"), str(basis.relative_to(ROOT))))
    dateien = sorted((ROOT / "02_research").rglob("*.md")) + sorted((ROOT / "04_models").glob("*/README.md")) + sorted((ROOT / "04_models").glob("*/ANNAHMEN_VORSCHLAG.md"))
    for note in dateien:
        for block in BLOCK.findall(note.read_text(encoding="utf-8")):
            rows.extend(read_rows(block, str(note.relative_to(ROOT))))
    # Doppelte IDs: Die später gelesene Zeile ersetzt die frühere (Ersatzzeilen aus Nachrecherchen und
    # Prüfvermerken; Dateien in alphabetischer Folge, Notizen mit Suffix nach der Grundnotiz). Die Position
    # im Register bleibt die der ersten Nennung. Abweichende URLs werden gemeldet.
    out, conflicts, ersetzt = [], [], []
    for row in rows:
        if row["id"] in seen:
            alt = seen[row["id"]]
            if row.get("url") != alt.get("url"):
                conflicts.append((row["id"], alt["_origin"], row["_origin"]))
            if any(row.get(k, "") != alt.get(k, "") for k in FIELDS):
                ersetzt.append((row["id"], alt["_origin"], row["_origin"]))
            out[out.index(alt)] = row
            seen[row["id"]] = row
            continue
        seen[row["id"]] = row
        out.append(row)
    target = ROOT / "sources" / "SOURCES.csv"
    with target.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, quoting=csv.QUOTE_ALL,
                                extrasaction="ignore")
        writer.writeheader()
        for row in out:
            writer.writerow({k: row.get(k, "") for k in FIELDS})
    print(f"{len(out)} Quellen geschrieben nach {target.relative_to(ROOT)}")
    for cid, a, b in ersetzt:
        print(f"ersetzt: {cid} ({a} → {b})")
    for cid, a, b in conflicts:
        print(f"WARNUNG: ID {cid} doppelt mit abweichender URL ({a} / {b})")


if __name__ == "__main__":
    main()
