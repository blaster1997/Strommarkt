#!/usr/bin/env python3
"""Setzt das Feld „kapitel“ im Quellenregister auf die Kapitel, die eine ID tatsächlich zitieren.

Zitate zählen im Kapiteltext (`03_chapters/<nn>_*.md`) und in den Lösungen des Kapitels
(`06_review/K<nn>_loesungen_entwurf.md`), nach derselben Regel wie das Quellenverzeichnis des Buchs
(`07_build/buch.py`, Anhang E). IDs, die nur Glossar oder Annahmenverzeichnis belegen, erhalten „Anhang B“ bzw.
„Anhang D“, IDs, die das Buch nicht zitiert, „nicht zitiert“.
Bearbeitet wird die maßgebliche Definition jeder ID (wie `kapitel_ergaenzen.py`); danach
`python3 sources/merge_sources.py` ausführen.

Aufruf: python3 sources/kapitel_abgleichen.py [--schreiben]
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "07_build"))
sys.path.insert(0, str(ROOT / "sources"))

import buch  # noqa: E402
import konfig  # noqa: E402
from kapitel_ergaenzen import fundstellen  # noqa: E402

FELDER = ["id", "titel", "herausgeber", "url", "abrufdatum", "stand_der_quelle", "typ", "qualität", "kapitel"]
NICHT_ZITIERT = "nicht zitiert"


def zeile(felder: list[str]) -> str:
    return ",".join('"' + f.replace('"', '""') + '"' for f in felder)


def belege() -> dict[str, set[int]]:
    kapiteltexte = {n: buch.ohne_yaml(buch.kapiteldatei(n).read_text(encoding="utf-8")) for n in konfig.kapitelnummern()}
    loesungen = []
    for n in konfig.kapitelnummern():
        p = ROOT / "06_review" / f"K{n:02d}_loesungen_entwurf.md"
        if p.exists():
            loesungen.append(f"# Kapitel {n} ·\n" + p.read_text(encoding="utf-8"))
    return buch.zitate_je_kapitel(kapiteltexte, "\n".join(loesungen))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--schreiben", action="store_true", help="Definitionen ändern (sonst nur Bericht)")
    args = ap.parse_args()
    reg = {r["id"]: r for r in csv.DictReader((ROOT / "sources" / "SOURCES.csv").open(encoding="utf-8"))}
    b = belege()
    in_anhang: dict[str, set[str]] = {}
    for buchstabe, text in buch.anhaenge_mit_belegen().items():
        for i in buch.zitierte_ids([text]):
            in_anhang.setdefault(i, set()).add(buchstabe)

    def kapitelfeld(i: str) -> str:
        if i in b:
            return ";".join(str(n) for n in sorted(b[i]))
        if i in in_anhang:
            return ";".join(f"Anhang {x}" for x in sorted(in_anhang[i]))
        return NICHT_ZITIERT

    soll = {i: kapitelfeld(i) for i in reg}
    aendern = {i: s for i, s in soll.items() if reg[i]["kapitel"].strip() != s}
    zitiert = sum(1 for i in reg if i in b)
    print(f"Register: {len(reg)} IDs, davon {zitiert} im Buch zitiert; Kapitelfeld abweichend: {len(aendern)}")
    eigene = tuple(f"{p}-" for p in (konfig.K.get("interne_id_praefixe") or []))
    unbekannt = sorted(i for i in b if i not in reg and not i.startswith(("A-", "D-", "M1-", "M2-", "M3-", "M4-", "P-") + eigene))
    if unbekannt:
        print("zitiert, aber nicht im Register:", ", ".join(unbekannt))
    if not args.schreiben:
        for i in sorted(aendern)[:40]:
            print(f"  {i}: „{reg[i]['kapitel']}“ → „{aendern[i]}“")
        return
    tr = fundstellen(set(aendern))
    je_datei: dict[Path, list[tuple[str, str]]] = {}
    for i, neu_kap in aendern.items():
        pfad, alt, felder = tr[i]
        felder = list(felder) + [""] * (9 - len(felder))
        felder[FELDER.index("kapitel")] = neu_kap
        je_datei.setdefault(pfad, []).append((alt, zeile(felder)))
    for pfad, ersetzungen in je_datei.items():
        text = pfad.read_text(encoding="utf-8")
        for alt, neu in ersetzungen:
            assert text.count(alt) == 1, (pfad, alt[:60])
            text = text.replace(alt, neu)
        pfad.write_text(text, encoding="utf-8")
    print(f"geändert: {len(aendern)} Definitionen in {len(je_datei)} Dateien")


if __name__ == "__main__":
    main()
