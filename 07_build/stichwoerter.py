#!/usr/bin/env python3
"""Stichwortliste für das Gesamtbuch aus dem Glossar (Phase 7).

Je Glossareintrag ein Stichwort (Begriff ohne Formeln) und seine Suchmuster: der Begriff selbst,
Varianten mit „/“ oder „,“ und Kurzformen in Klammern (z. B. „Stabilisierungs- und Restrukturierungsrahmen
(StaRUG)“ → Muster „Stabilisierungs- und Restrukturierungsrahmen“ und „StaRUG“). Der Lua-Filter markiert damit die Fundstellen im Text
(`stichwort-datei` im YAML-Kopf des Gesamtbuchs); die Vorlage setzt daraus das Verzeichnis.

Aufruf: python3 07_build/stichwoerter.py  → schreibt 07_build/stichwoerter.json
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "07_build"))
import konfig  # noqa: E402
ZIEL = ROOT / "07_build" / "stichwoerter.json"

# Muster, die zu allgemein oder mehrdeutig sind, um Fundstellen sinnvoll zu markieren (buch_config.yaml)
ZU_ALLGEMEIN = set(konfig.K.get("stichwort_zu_allgemein") or [])


def glossar_eintraege() -> list[str]:
    text = (ROOT / "GLOSSAR.md").read_text(encoding="utf-8")
    namen = []
    for zeile in text.splitlines():
        if not zeile.startswith("| ") or zeile.startswith("| Begriff") or zeile.startswith("|---"):
            continue
        namen.append(zeile[2:].split(" | ", 1)[0].strip())
    return namen


def ohne_formeln(s: str) -> str:
    s = re.sub(r"\s*\(\s*\$[^$]*\$\s*\)", "", s)      # „(… $T_A$ …)“ ganz entfernen
    s = re.sub(r"\$[^$]*\$", "", s)
    s = s.replace("**", "").replace("*", "")
    return re.sub(r"\s{2,}", " ", s).strip(" ,;")


def klammer_inhalte(name: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"\(([^()]*)\)", name)]


def hauptteile(name: str) -> list[str]:
    haupt = re.sub(r"\s*\([^()]*\)", "", name).strip()
    teile = []
    for teil in re.split(r"\s*/\s*", haupt):
        stuecke = [s.strip() for s in teil.split(", ")]
        # „Einspeiseleistung, gemeinsame“ oder „Transaktionsgebühr, Anrechnung“: nur der erste Teil;
        # „Einheitenzertifikat, Anlagenzertifikat“: beide (zweiter Teil ein eigenes Kompositum)
        teile.append(stuecke[0])
        for s in stuecke[1:]:
            if s[:1].isupper() and len(s) >= 8 and s not in ZU_ALLGEMEIN:
                teile.append(s)
    return [t for t in teile if t]


def ist_kuerzel(s: str) -> bool:
    return " " not in s and sum(1 for c in s if c.isupper() or c.isdigit()) >= 2 and len(s) <= 8


def kuerzel_passt(kuerzel: str, begriff: str) -> bool:
    """Kurzform passt zum Begriff, wenn ihre Buchstaben in Reihenfolge darin vorkommen und der erste übereinstimmt."""
    buchst = [c.lower() for c in kuerzel if c.isalpha()]
    text = begriff.lower()
    if not buchst or not text or text[0] != buchst[0]:
        return False
    pos = 0
    for c in buchst:
        pos = text.find(c, pos)
        if pos < 0:
            return False
        pos += 1
    return True


def ist_englisch(s: str) -> bool:
    return len(s.split()) >= 2 and not re.search(r"[äöüÄÖÜß§]", s) and s[:1].isalpha()


def muster_von(name: str, hauptbegriffe: set[str], klammer_zaehler: dict[str, int]) -> list[str]:
    muster = list(hauptteile(name))
    for k in klammer_inhalte(name):
        if "/" in k or "§" in k or "Kapitel" in k or len(k) > 40:
            continue
        for teil in re.split(r",\s+|;\s*", k):
            teil = teil.strip()
            for vorsatz in ("kurz ", "auch ", "engl. ", "z. B. "):
                if teil.startswith(vorsatz):
                    teil = teil[len(vorsatz):]
            if not teil or teil in hauptbegriffe:
                continue
            haupt = hauptteile(name)
            if ist_kuerzel(teil):
                if haupt and kuerzel_passt(teil, haupt[0]):
                    muster.append(teil)
            elif ist_englisch(teil) and klammer_zaehler.get(teil, 0) <= 1:
                muster.append(teil)
    gut = []
    for m in muster:
        m = m.strip(" „“\"")
        if not m or len(m) < 3 or len(m.split()) > 4 or m in ZU_ALLGEMEIN:
            continue
        if re.fullmatch(r"[\d.,%–\- ]+", m) or "$" in m:
            continue
        if m not in gut:
            gut.append(m)
    return gut


def main() -> None:
    namen = glossar_eintraege()
    hauptbegriffe = {h for n in namen for h in hauptteile(n)}
    klammer_zaehler: dict[str, int] = {}
    for n in namen:
        for k in klammer_inhalte(n):
            for teil in re.split(r",\s+|;\s*|\s*/\s*", k):
                klammer_zaehler[teil.strip()] = klammer_zaehler.get(teil.strip(), 0) + 1
    eintraege, gesehen = [], set()
    for name in namen:
        wort = ohne_formeln(name)
        if not wort or wort in gesehen:
            continue
        muster = muster_von(name, hauptbegriffe, klammer_zaehler)
        if not muster:
            continue
        gesehen.add(wort)
        eintraege.append({"wort": wort, "muster": muster})
    ZIEL.write_text(json.dumps(eintraege, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"geschrieben: {ZIEL.relative_to(ROOT)} ({len(eintraege)} Stichwörter)")


if __name__ == "__main__":
    main()
