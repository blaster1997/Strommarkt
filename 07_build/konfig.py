#!/usr/bin/env python3
"""Liest die Buchkonfiguration `07_build/buch_config.yaml`.

Alle buchspezifischen Angaben des Satzsystems (Titel, Teile und Kapitel, Deckblatt, Stand, vertrauliche
Unterlagen, Stichwort-Ausnahmen) stehen dort; die Skripte lesen sie über dieses Modul.
"""

from __future__ import annotations

from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
PFAD = HERE / "buch_config.yaml"


def laden() -> dict:
    with PFAD.open(encoding="utf-8") as datei:
        return yaml.safe_load(datei) or {}


K = laden()


def teile() -> list[tuple[str, str, list[int]]]:
    """(Nummer, Titel, Kapitelnummern) je Teil des Buchs."""
    return [(str(t["nr"]), str(t["titel"]), [int(n) for n in t["kapitel"]]) for t in K.get("teile", [])]


def kapitelnummern() -> list[int]:
    return [n for _, _, nummern in teile() for n in nummern]


def kapitel_anzahl() -> int:
    nummern = kapitelnummern()
    return max(nummern) if nummern else 0


def wert(schluessel: str, standard: str = "") -> str:
    v = K.get(schluessel)
    return standard if v is None else str(v)


def vertraulich() -> dict[str, tuple[str, str]]:
    """ID → (Eintrag im Quellenverzeichnis, Stand) für vertrauliche Unterlagen."""
    return {str(v["id"]): (str(v.get("eintrag", "")), str(v.get("stand", ""))) for v in (K.get("vertraulich") or [])}
