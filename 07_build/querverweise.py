#!/usr/bin/env python3
"""Querverweisprüfung für das Gesamtbuch (Phase 7, Konsistenzprüfung).

Ermittelt je Kapitel die nummerierten Abschnitte (H2, H3), Tabellen („Table:“-Beschriftungen), Abbildungen
(Bildabsätze) und Übungen und prüft alle Verweise der Form „Abschnitt 14.3“, „Tabelle 15.6“, „Abbildung 9.2“,
„Übung 25.3“, „Lösung 12.4“ und „Kapitel 27“ in Kapiteln, Lösungen und Vorwort auf ein existierendes Ziel.
Ausgabe: Liste der Verweise ohne Ziel (Datei, Zeile, Verweis, Kontext).

Aufruf: python3 07_build/querverweise.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "07_build"))
import konfig  # noqa: E402

MAX_KAPITEL = konfig.kapitel_anzahl()
KAP = ROOT / "03_chapters"


def struktur(nr: int, text: str) -> dict:
    abschnitte, tabellen, abbildungen, uebungen = set(), 0, 0, set()
    h2 = h3 = 0
    im_code = in_uebungen = False
    for z in text.splitlines():
        if z.startswith("```"):
            im_code = not im_code
            continue
        if im_code:
            continue
        if z.startswith("## ") and "{.unnumbered" not in z:
            h2 += 1
            h3 = 0
            abschnitte.add(f"{nr}.{h2}")
        elif z.startswith("### ") and "{.unnumbered" not in z:
            h3 += 1
            abschnitte.add(f"{nr}.{h2}.{h3}")
        s = z.lstrip("> ").strip()
        if s.startswith("Table:"):
            tabellen += 1
        if re.match(r"^!\[.+\]\(.+\)", s):
            abbildungen += 1
        for m in re.finditer(r"\*\*Übung (\d+)\.(\d+)", z):
            uebungen.add(f"{m.group(1)}.{m.group(2)}")
        if z.startswith("## Übungen"):
            in_uebungen = True
        elif z.startswith("## "):
            in_uebungen = False
        if in_uebungen:
            m = re.match(r"^(\d+)\. ", z)
            if m:
                uebungen.add(f"{nr}.{m.group(1)}")
    return {
        "abschnitt": abschnitte,
        "tabelle": {f"{nr}.{i}" for i in range(1, tabellen + 1)},
        "abbildung": {f"{nr}.{i}" for i in range(1, abbildungen + 1)},
        "uebung": uebungen,
    }


def main() -> None:
    kapitel = {}
    texte = {}
    for p in sorted(KAP.glob("[0-9][0-9]_*.md")):
        nr = int(p.name[:2])
        t = p.read_text(encoding="utf-8")
        texte[p.name] = t
        kapitel[nr] = struktur(nr, t)
    for extra in ("anhang_loesungen.md", "vorwort.md"):
        if (KAP / extra).exists():
            texte[extra] = (KAP / extra).read_text(encoding="utf-8")
    muster = [
        ("abschnitt", r"Abschnitt(?:e|en)? (\d{1,2})\.(\d{1,2})(?:\.(\d{1,2}))?"),
        ("tabelle", r"Tabellen? (\d{1,2})\.(\d{1,2})"),
        ("abbildung", r"Abbildung(?:en)? (\d{1,2})\.(\d{1,2})"),
        ("uebung", r"Übung(?:en)? (\d{1,2})\.(\d{1,2})"),
        ("uebung", r"Lösung(?:en)? (\d{1,2})\.(\d{1,2})"),
    ]
    fehler = 0
    for name, t in texte.items():
        for i, z in enumerate(t.splitlines(), 1):
            if z.startswith(("Table:", "> Table:")) and name != "anhang_loesungen.md":
                pass
            for art, rx in muster:
                for m in re.finditer(rx, z):
                    davor = z[max(0, m.start() - 40):m.start()]
                    if re.search(r"(Kapitelzahlen|kapitelzahlen[^ ]*|Lauf M4-\S+|Taxonomie-|Verordnung \(EU\) \S+|Anlage \d+,?)\W*$", davor):
                        continue
                    k = int(m.group(1))
                    if k not in kapitel:
                        continue
                    ziel = f"{m.group(1)}.{m.group(2)}" + (f".{m.group(3)}" if art == "abschnitt" and m.lastindex and m.lastindex >= 3 and m.group(3) else "")
                    if ziel not in kapitel[k][art]:
                        fehler += 1
                        a = max(0, m.start() - 60)
                        print(f"{name}:{i}: {m.group(0)} → kein Ziel | …{z[a:m.end() + 40]}…")
            for m in re.finditer(r"Kapitel (\d{1,2})\b", z):
                if int(m.group(1)) > MAX_KAPITEL or int(m.group(1)) == 0:
                    fehler += 1
                    print(f"{name}:{i}: {m.group(0)} → kein Kapitel")
    print(f"Verweise ohne Ziel: {fehler}")


if __name__ == "__main__":
    main()
