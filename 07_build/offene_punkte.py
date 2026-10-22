#!/usr/bin/env python3
"""Erzeugt die Listen offener Punkte für den Abschlussbericht (Phase 7) aus Kapiteln und Register.

- `06_review/P7_luecken.md`: alle Marken [LÜCKE: …] mit Kapitel und Abschnitt
- `06_review/P7_verifikationsliste.md`: zitierte Belege, die nur als Suchauszug, nur mit Titel oder nicht
  vollständig gelesen vorliegen (vor dem Druck am Volltext zu prüfen)
- `06_review/P7_stand_kaesten.md`: Wortlaut aller Kästen „Stand“ je Kapitel (Grundlage der Prüfliste vor
  Drucklegung)

Aufruf: python3 07_build/offene_punkte.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import buch  # noqa: E402
import konfig  # noqa: E402

KAPITEL = konfig.kapitelnummern()
STAND = konfig.wert("stand")
BEREICH = f"{KAPITEL[0]}–{KAPITEL[-1]}" if KAPITEL else "–"

REVIEW = ROOT / "06_review"
VERIFIKATION = re.compile(r"Suchauszug|nur Titel|nicht gelesen|nicht lesbar|nicht abrufbar")


def abschnitte(text: str, kapitel: int) -> list[tuple[int, str]]:
    """(Zeilenindex, Abschnittsnummer) je nummerierter Überschrift, wie der Satz sie zählt."""
    zaehler = [0, 0, 0]
    aus, im_code = [], False
    for i, z in enumerate(text.splitlines()):
        if z.startswith("```"):
            im_code = not im_code
        if im_code:
            continue
        m = re.match(r"^(#{1,4}) (.*)$", z)
        if not m or "unnumbered" in m.group(2):
            continue
        ebene = len(m.group(1))
        if ebene == 1:
            zaehler = [0, 0, 0]
            continue
        zaehler[ebene - 2] += 1
        for j in range(ebene - 1, 3):
            zaehler[j] = 0
        aus.append((i, ".".join([str(kapitel)] + [str(x) for x in zaehler[: ebene - 1]])))
    return aus


def abschnitt_von(zeile: int, liste: list[tuple[int, str]]) -> str:
    nr = ""
    for i, n in liste:
        if i <= zeile:
            nr = n
        else:
            break
    return nr


def zelle(s: str) -> str:
    return s.replace("|", "/").replace("\n", " ").strip()


def kopf(titel: str, untertitel: str) -> list[str]:
    return ["---", f'title: "{titel}"', f'subtitle: "{untertitel}"', f'date: "{STAND}"',
            f'kopfzeile-rechts: "{titel}"', "---", ""]


def luecken() -> int:
    aus = kopf("Lücken im Buch", "Anlage zum Abschlussbericht Phase 7")
    aus += [f"Alle Marken [LÜCKE: …] der Kapitel {BEREICH}; erzeugt mit `07_build/offene_punkte.py`. Eine Lücke heißt: Für die",
            "Aussage fehlt ein belastbarer Beleg; das Buch nennt sie, statt eine Zahl zu erfinden.", "",
            "| Kap. | Abschnitt | Lücke |", "|---|---|---|"]
    n = 0
    for k in KAPITEL:
        text = buch.ohne_yaml(buch.kapiteldatei(k).read_text(encoding="utf-8"))
        liste = abschnitte(text, k)
        gesehen = set()
        for i, z in enumerate(text.splitlines()):
            for m in re.finditer(r"\[LÜCKE:\s*([^\]]+)\]", z):
                eintrag = m.group(1).strip()
                if eintrag in gesehen or eintrag in ("…", "..."):
                    continue
                gesehen.add(eintrag)
                aus.append(f"| {k} | {abschnitt_von(i, liste)} | {zelle(eintrag)} |")
                n += 1
    aus += ["", "Table: Lücken je Kapitel", "", f"Quelle: Kapitel {BEREICH} (Stand {STAND}); {n} Einträge."]
    (REVIEW / "P7_luecken.md").write_text("\n".join(aus) + "\n", encoding="utf-8")
    return n


def verifikationsliste() -> int:
    kapiteltexte = {k: buch.ohne_yaml(buch.kapiteldatei(k).read_text(encoding="utf-8")) for k in KAPITEL}
    loesungen = "\n".join(f"# Kapitel {k} ·\n" + p.read_text(encoding="utf-8")
                          for k in KAPITEL if (p := REVIEW / f"K{k:02d}_loesungen_entwurf.md").exists())
    belege = buch.zitate_je_kapitel(kapiteltexte, loesungen)
    zeilen = []
    for r in csv.DictReader((ROOT / "sources" / "SOURCES.csv").open(encoding="utf-8")):
        if r["id"] not in belege:
            continue
        felder = " ".join([r["typ"], r["stand_der_quelle"], r["titel"], r["herausgeber"]])
        vermerk = sorted(set(m.group(0) for m in VERIFIKATION.finditer(felder)))
        if not vermerk:
            continue
        titel = r["titel"].strip()
        if len(titel) > 110:
            titel = titel[:107].rstrip() + " …"
        zeilen.append((r["qualität"], r["id"], titel, ", ".join(vermerk),
                       ", ".join(str(k) for k in sorted(belege[r["id"]]))))
    rang = {"A": 0, "B": 1, "B/C": 2, "C": 3}
    zeilen.sort(key=lambda z: (rang.get(z[0], 9), z[1]))
    aus = kopf("Verifikationsliste", "Anlage zum Abschlussbericht Phase 7")
    aus += ["Zitierte Belege, die nur als Suchauszug, nur mit Titel oder nicht vollständig gelesen vorliegen; vor dem",
            "Druck am Volltext zu prüfen, Qualität A zuerst. Erzeugt mit `07_build/offene_punkte.py` aus",
            "`sources/SOURCES.csv` (Felder Typ, Stand, Titel, Herausgeber).", "",
            "| Qual. | ID | Titel | Vermerk | Kap. |", "|---|---|---|---|---|"]
    aus += [f"| {q} | {i} | {zelle(t)} | {v} | {k} |" for q, i, t, v, k in zeilen]
    aus += ["", "Table: Belege mit Prüfbedarf", "", f"Quelle: Quellenregister (Stand {STAND}); {len(zeilen)} Einträge."]
    (REVIEW / "P7_verifikationsliste.md").write_text("\n".join(aus).replace("$", "\\$") + "\n", encoding="utf-8")
    return len(zeilen)


def stand_kaesten() -> int:
    aus = kopf("Kästen „Stand“", "Arbeitsgrundlage der Prüfliste vor Drucklegung")
    aus += [f"Wortlaut aller Kästen „Stand“ der Kapitel {BEREICH}, erzeugt mit `07_build/offene_punkte.py`.", ""]
    n = 0
    for k in KAPITEL:
        text = buch.ohne_yaml(buch.kapiteldatei(k).read_text(encoding="utf-8"))
        liste = abschnitte(text, k)
        zeilen = text.splitlines()
        i = 0
        while i < len(zeilen):
            if zeilen[i].startswith("> [!STAND]"):
                block = []
                j = i + 1
                while j < len(zeilen) and zeilen[j].startswith(">"):
                    block.append(zeilen[j][1:].strip())
                    j += 1
                n += 1
                aus += [f"## Kapitel {k}, Abschnitt {abschnitt_von(i, liste) or '–'} {{.unnumbered}}", "",
                        " ".join(x for x in block if x), ""]
                i = j
            else:
                i += 1
    (REVIEW / "P7_stand_kaesten.md").write_text("\n".join(aus) + "\n", encoding="utf-8")
    return n


def main() -> None:
    print(f"Lücken: {luecken()}; Verifikationsliste: {verifikationsliste()}; Kästen „Stand“: {stand_kaesten()}")


if __name__ == "__main__":
    main()
