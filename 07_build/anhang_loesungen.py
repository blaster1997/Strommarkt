#!/usr/bin/env python3
"""Erzeugt 03_chapters/anhang_loesungen.md aus den freigegebenen Lösungsentwürfen in 06_review/.

Aufruf:
    python3 07_build/anhang_loesungen.py 06 18      # Kapitelnummern, deren Lösungen freigegeben sind

Quelle je Kapitel: 06_review/K<nn>_loesungen_entwurf.md. Das Skript
- übernimmt den Titel des Kapitels unverändert aus dem YAML-Kopf von 03_chapters/<nn>_*.md,
- streicht die internen Vorbemerkungen zwischen „## Kapitel“ und der ersten Übungsüberschrift,
- stuft die Überschriften ein (## Kapitel → #, ### Übung → ##, #### → ###) und nimmt sie von der
  automatischen Nummerierung aus ({.unnumbered}).
Tabellen, Formeln und Quellenzeilen bleiben unverändert.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "07_build"))
import konfig  # noqa: E402

ZIEL = ROOT / "03_chapters" / "anhang_loesungen.md"

KOPF = """---
title: "Anhang A · Lösungen zu den Übungen"
subtitle: {untertitel}
date: "{datum}"
kopfzeile-rechts: "Anhang A · Lösungen"
inhaltsverzeichnis: true
toc-tiefe: 1
deckblatt-hinweis: {hinweis}
---

Die Lösungen zeigen Rechenwege und Begründungen zu den Übungen der Kapitel. Zahlen, Quellen und
Annahmen folgen dem jeweiligen Kapitel; wo eine Lösung zusätzliche Angaben nutzt, ist das vermerkt.

"""


def kapiteltitel(nr: str) -> str:
    datei = next((ROOT / "03_chapters").glob(f"{nr}_*.md"))
    text = datei.read_text(encoding="utf-8")
    m = re.search(r'^title:\s*"(.*)"', text, flags=re.M)
    titel = m.group(1) if m else f"Kapitel {int(nr)}"
    return titel                      # „Kapitel n · Titel“ wie im Kapitelkopf (Titel enthalten teils Doppelpunkte)


def abschnitt(nr: str) -> str:
    quelle = ROOT / "06_review" / f"K{nr}_loesungen_entwurf.md"
    zeilen = quelle.read_text(encoding="utf-8").splitlines()
    aus, vorspann = [], False
    for z in zeilen:
        if re.match(r"^## Kapitel \d+\s*$", z):
            aus.append(f"# {kapiteltitel(nr)} {{.unnumbered}}")
            vorspann = True                           # interne Vorbemerkungen bis zur ersten Übung
            continue
        if vorspann and not z.startswith("#"):
            continue
        if z.startswith("#"):
            vorspann = False
            stufe = len(z) - len(z.lstrip("#"))
            text = z[stufe:].strip()
            if "{.unnumbered}" not in text:
                text += " {.unnumbered}"
            aus.append("#" * max(stufe - 1, 1) + " " + text)
            continue
        aus.append(z)
    return "\n".join(aus).strip() + "\n"


def main(nummern: list[str]) -> None:
    import datetime as dt
    teile = [KOPF.format(datum=dt.date.today().strftime("%d.%m.%Y"),
                         untertitel=json.dumps(konfig.wert("titel"), ensure_ascii=False),
                         hinweis=json.dumps(konfig.wert("hinweis_kurz", "Keine Rechts-, Steuer- oder Anlageberatung."),
                                            ensure_ascii=False))]
    for i, nr in enumerate(sorted(nummern, key=int)):
        if i:
            teile.append("\n<!-- neue-seite -->\n\n")
        teile.append(abschnitt(nr.zfill(2)))
    ZIEL.write_text("".join(teile), encoding="utf-8")
    print(f"geschrieben: {ZIEL.relative_to(ROOT)} (Kapitel {', '.join(nummern)})")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main(sys.argv[1:])
