#!/usr/bin/env python3
"""Gesamtbuch als PDF (Phase 7): Titel, Teile, Kapitel und Deckblatt aus `07_build/buch_config.yaml`.

Setzt die Kapitel in ihren Teilen und die Anhänge A–H zu einem Dokument zusammen und übergibt es
an die Pipeline von build.py (Pandoc → Typst, Vorlage und Lua-Filter unverändert, Buchmodus über die
Metadaten `buch` und `stichwort-datei`).

Anhänge: A Lösungen (03_chapters/anhang_loesungen.md), B Glossar (GLOSSAR.md, optional mit englischen
Entsprechungen aus 07_build/glossar_englisch.csv), C Abkürzungen (03_chapters/anhang_abkuerzungen.md),
D Annahmenverzeichnis (aus ANNAHMEN.md erzeugt), E Quellenverzeichnis (aus sources/SOURCES.csv, nur im Buch
zitierte Quellen; vertrauliche Unterlagen und `ohne_herausgeber` nach buch_config.yaml), F Formelsammlung
(03_chapters/anhang_formeln.md), G Modellhandbuch (03_chapters/anhang_modelle.md), H Stichwortverzeichnis
(von der Vorlage aus den Marken des Lua-Filters gesetzt).

Aufruf:
  python3 07_build/buch.py                      # Gesamtbuch → 07_build/output/<dateiname>.pdf
  python3 07_build/buch.py --kapitel 1 2 --name probe   # Probesatz mit ausgewählten Kapiteln
  python3 07_build/buch.py --nur-markdown       # nur das zusammengesetzte Markdown schreiben
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402
import konfig  # noqa: E402

KAPITEL = ROOT / "03_chapters"

TEILE = konfig.teile()

# Quellen, die im Verzeichnis ohne Herausgeber und URL erscheinen (Vertraulichkeit, CLAUDE.md § 8)
OHNE_HERAUSGEBER = set(konfig.K.get("ohne_herausgeber") or [])
# Vertrauliche Unterlagen des Auftraggebers: im Buch nur unter ihrer Bezeichnung, ohne Titel, Herausgeber und URL
VERTRAULICH = konfig.vertraulich()

ID = r"[A-Z][A-Z0-9]*-[0-9]{2,3}[a-z]?"



def _q(s: str) -> str:
    """Zeichenkette als YAML-Skalar in doppelten Anführungszeichen (JSON ist gültiges YAML)."""
    return json.dumps(s, ensure_ascii=False)


def buch_yaml() -> str:
    k = konfig.K
    zeilen = ["---",
              f"title: {_q(konfig.wert('titel'))}",
              f"subtitle: {_q(konfig.wert('untertitel'))}",
              f"date: {_q('Stand ' + konfig.wert('stand'))}",
              f"kopfzeile-links: {_q(konfig.wert('kurztitel', konfig.wert('titel')))}",
              "nummerierung: kapitelweise",
              "kolumnentitel: kapitel",
              "inhaltsverzeichnis: true",
              "toc-tiefe: 2",
              "buch: true",
              'stichwort-datei: "07_build/stichwoerter.json"']
    if k.get("deckblatt_info"):
        zeilen.append("deckblatt-info:")
        zeilen += [f"  - {_q(str(z))}" for z in k["deckblatt_info"]]
    if k.get("fusszeile_links"):
        zeilen.append(f"fusszeile-links: {_q(konfig.wert('fusszeile_links'))}")
    if k.get("deckblatt_hinweis"):
        zeilen.append(f"deckblatt-hinweis: {_q(konfig.wert('deckblatt_hinweis'))}")
    zeilen.append("---")
    return "\n".join(zeilen) + "\n"


def ohne_yaml(text: str) -> str:
    if text.startswith("---"):
        ende = text.find("\n---", 3)
        if ende > 0:
            return text[ende + 4:].lstrip("\n")
    return text


def kapiteldatei(nr: int) -> Path:
    treffer = sorted(KAPITEL.glob(f"{nr:02d}_*.md"))
    if not treffer:
        sys.exit(f"Kapitel {nr} fehlt in {KAPITEL}")
    return treffer[0]


def typst(code: str) -> str:
    return f"\n```{{=typst}}\n{code}\n```\n"


def teilseite(nr: str, titel: str) -> str:
    # Klasse .teil: im Satz Überschrift mit Label <teil> (Teilseite, eigener Eintrag im Inhaltsverzeichnis),
    # im DOCX eine nicht nummerierte Überschrift erster Ebene
    return f"\n# Teil {nr} – {titel} {{.unnumbered .teil}}\n"


def anhang_kopf(buchstabe: str, titel: str) -> str:
    return f"\n# Anhang {buchstabe} · {titel} {{.unnumbered .anhang}}\n" + typst(f'#anhang-buchstabe.update("{buchstabe}")')


def ueberschriften_tiefer(text: str, toc_ebene: int = 2) -> str:
    """Alle Überschriften um eine Ebene tiefer; neue Ebene `toc_ebene` bleibt im Inhaltsverzeichnis."""
    zeilen, im_code = [], False
    for z in text.splitlines():
        if z.startswith("```"):
            im_code = not im_code
        if not im_code and re.match(r"^#{1,5} ", z):
            z = "#" + z
            if z.startswith("#" * toc_ebene + " ") and "{.unnumbered}" in z:
                z = z.replace("{.unnumbered}", "{.unnumbered .toc}")
        zeilen.append(z)
    return "\n".join(zeilen)


# --- Anhang A: Lösungen --------------------------------------------------------------------------
def anhang_loesungen() -> str:
    text = ohne_yaml((KAPITEL / "anhang_loesungen.md").read_text(encoding="utf-8"))
    return ueberschriften_tiefer(text)


# --- Anhang B: Glossar ---------------------------------------------------------------------------
def anhang_glossar() -> str:
    text = ohne_yaml((ROOT / "GLOSSAR.md").read_text(encoding="utf-8"))
    text = re.sub(r"^# Glossar \{\.unnumbered\}\s*", "", text, flags=re.M)
    englisch = {}
    pfad = HERE / "glossar_englisch.csv"
    if pfad.exists():
        for r in csv.DictReader(pfad.open(encoding="utf-8")):
            if r.get("englisch", "").strip():
                englisch[r["begriff"].strip()] = r["englisch"].strip()
    if not englisch:
        return text
    zeilen = []
    for z in text.splitlines():
        if z.startswith("| Begriff | Erklärung | Kap. |"):
            z = "| Begriff | Englisch | Erklärung | Kap. |"
        elif z.startswith("|---|---|---|"):
            z = "|---|---|---|---|"
        elif z.startswith("| "):
            teile = z[2:-2].split(" | ")
            if len(teile) >= 3:
                begriff = teile[0]
                z = "| " + " | ".join([begriff, englisch.get(begriff, "–")] + teile[1:]) + " |"
        zeilen.append(z)
    return "\n".join(zeilen)


# --- Anhang D: Annahmenverzeichnis ----------------------------------------------------------------
def anhang_annahmen() -> str:
    text = (ROOT / "ANNAHMEN.md").read_text(encoding="utf-8")
    aus = [
        "Das Verzeichnis enthält alle Annahmen, auf die sich Text, Rechenbeispiele und Modelle stützen; im Text "
        "verweisen die IDs darauf (z. B. „A-009“). Typ: F = auf Fakt gestützt (Quelle), S = Schätzung (Herleitung), "
        "A = Annahme (Begründung). Low, Mid und High bezeichnen niedrigen, mittleren und hohen Zahlenwert. "
        "A-001 bis A-099 sind übergreifende Annahmen, A-M1 bis A-M4 Modellannahmen, A-Kxx Annahmen einzelner "
        f"Kapitel. Stand {konfig.wert('stand')}.",
        "",
    ]
    kopf: list[str] | None = None
    for z in text.splitlines():
        if z.startswith("# "):
            continue
        m = re.match(r"^(#{2,3}) (.*)$", z)
        if m:
            titel = re.sub(r"\s*\((IDs|übernommen)[^)]*\)", "", m.group(2)).strip()
            ebene = "##" if m.group(1) == "##" else "###"
            aus += ["", f"{ebene} {titel} {{.unnumbered .toc}}" if ebene == "##" else f"{ebene} {titel} {{.unnumbered}}", ""]
            kopf = None
            continue
        if z.startswith("| ID |"):
            kopf = [c.strip() for c in z.strip().strip("|").split(" | ")]
            continue
        if z.startswith("|---"):
            continue
        if z.startswith("| A-") and kopf:
            zellen = [c.strip() for c in z.strip().strip("|").split(" | ")]
            if len(zellen) != len(kopf):
                zellen = zellen[: len(kopf) - 1] + [" | ".join(zellen[len(kopf) - 1:])]
            werte = dict(zip(kopf, zellen))
            aid, name = werte.get("ID", ""), ohne_pruefvermerke(werte.get("Annahme", ""))
            typ = werte.get("Typ", "")
            aus.append(f"**{aid} · {name}** ({'Typ ' + typ if typ else 'ohne Typ'})  ")
            for feld in kopf:
                if feld in ("ID", "Annahme", "Typ", "Status"):
                    continue
                inhalt = ohne_pruefvermerke(werte.get(feld, "").strip())
                if inhalt and inhalt not in ("–", "-"):
                    aus.append(f"*{feld}:* {inhalt}  ")
            aus.append("")
    return "\n".join(aus)


# --- Anhang E: Quellenverzeichnis ------------------------------------------------------------------
def zitierte_ids(texte: list[str]) -> set[str]:
    ids = set()
    for t in texte:
        for m in re.finditer(r"\[([^\]]+)\]", t):
            inhalt = m.group(1)
            ids.update(re.findall(ID, inhalt))
            for pre, von, bis in re.findall(r"([A-Z][A-Z0-9]*-)(\d{2,3}) bis -?(?:[A-Z][A-Z0-9]*-)?(\d{2,3})", inhalt):
                for n in range(int(von), int(bis) + 1):
                    ids.add(f"{pre}{n:0{len(von)}d}")
    return ids


def datum_de(s: str) -> str:
    """ISO-Daten des Registers im Buchformat: 2026-09-28 → 28.09.2026, 2025-04 → 04/2025."""
    s = re.sub(r"\b(\d{4})-(\d{2})-(\d{2})\b", r"\3.\2.\1", s)
    return re.sub(r"\b(\d{4})-(\d{2})\b", r"\2/\1", s)


# Arbeitsvermerke im Register (wer wie geprüft hat, lokale Dateien), die nicht ins gedruckte Verzeichnis gehören.
INTERN = re.compile(r"Orchestrator|Faktencheck|\bAgent\b|WebFetch|curl|HTTP \d|sources/|Seitenbilder|https?://|"
                    r"PDF gelesen|Abrufwerkzeug|Prüfvermerk|Publications-Office|Volltext|Textauszug|vollständig gelesen")


def _teile(s: str) -> list[str]:
    """Trennt an „;“ außerhalb von Klammern."""
    teile, tiefe, start = [], 0, 0
    for i, z in enumerate(s):
        tiefe += {"(": 1, ")": -1}.get(z, 0)
        if z == ";" and tiefe == 0:
            teile.append(s[start:i])
            start = i + 1
    teile.append(s[start:])
    return [x.strip() for x in teile if x.strip()]


def ohne_arbeitsvermerke(s: str) -> str:
    def klammer(m: re.Match) -> str:
        teile = [x for x in _teile(m.group(2)) if not INTERN.search(x)]
        return f"{m.group(1)}({'; '.join(teile)})" if teile else ""
    s = re.sub(r"(\s*)\(([^()]*)\)", klammer, s)
    return "; ".join(x for x in _teile(s) if not INTERN.search(x))


# Prüfvermerke im Annahmenverzeichnis (Faktencheck, Lektorat, Orchestrator): im Druck weglassen bzw. neutral fassen.
PRUEF = re.compile(r"Faktencheck|Orchestrator|Lektorat|Prüfvermerk|Prüferrechnung|\bAgent\b|HTTP \d{3}")


def ohne_pruefvermerke(s: str) -> str:
    """Vermerke zum Prüfweg weglassen; Setzungen des Orchestrators als „Setzung der Autoren“."""
    s = re.sub(r"(nach )?(?:Vorgabe|Entscheidung) (?:des )?Orchestrators?", lambda m: (m.group(1) or "") + "Setzung der Autoren", s)
    s = re.sub(r",? (?:präzisiert |geändert )?nach Faktencheck K\d\d(?: v\d)?(?:,? (?:Befund|Nr\.) \d+(?: und \d+)?)?", "", s)
    s = re.sub(r",? Prüfvermerk Nr\. \d+(?: und \d+)?", "", s)
    s = re.sub(r"K\d\d-Prüfvermerk(?: Nr\. \d+)?, ", "", s)
    s = re.sub(r", Volltext nach Prüfvermerk", "", s)
    s = re.sub(r"Ablesung im Faktencheck K\d\d(?: v\d)?, ", "", s)
    s = re.sub(r", im Faktencheck K\d\d(?: v\d)? nachvollzogen", "", s)
    def klammer(m: re.Match) -> str:
        teile = [x for x in _teile(m.group(2)) if not PRUEF.search(x)]
        return f"{m.group(1)}({'; '.join(teile)})" if teile else ""

    for _ in range(3):
        neu = re.sub(r"(\s*)\(([^()]*)\)", klammer, s)
        if neu == s:
            break
        s = neu
    return "; ".join(x for x in _teile(s) if not PRUEF.search(x))


def zitate_je_kapitel(kapiteltexte: dict[int, str], loesungen: str) -> dict[str, set[int]]:
    """Kapitel, die eine Quellen-ID zitieren (Kapiteltext und Lösungen des Kapitels)."""
    belege: dict[str, set[int]] = {}
    for n, t in kapiteltexte.items():
        for i in zitierte_ids([t]):
            belege.setdefault(i, set()).add(n)
    for m in re.finditer(r"^#+ Kapitel (\d+) ·.*?(?=^#+ Kapitel \d+ ·|\Z)", loesungen, flags=re.M | re.S):
        for i in zitierte_ids([m.group(0)]):
            belege.setdefault(i, set()).add(int(m.group(1)))
    return belege


def anhaenge_mit_belegen() -> dict[str, str]:
    """Anhänge, deren Belege ebenfalls ins Quellenverzeichnis gehören (Buchstabe → Text)."""
    return {"B": (ROOT / "GLOSSAR.md").read_text(encoding="utf-8"),
            "D": (ROOT / "ANNAHMEN.md").read_text(encoding="utf-8")}


def anhang_quellen(kapiteltexte: dict[int, str], loesungen: str, anhaenge: dict[str, str] | None = None) -> str:
    reg = {r["id"]: r for r in csv.DictReader((ROOT / "sources" / "SOURCES.csv").open(encoding="utf-8"))}
    belege = zitate_je_kapitel(kapiteltexte, loesungen)
    in_anhang: dict[str, set[str]] = {}
    for buchstabe, text in (anhaenge or {}).items():
        for i in zitierte_ids([text]):
            in_anhang.setdefault(i, set()).add(buchstabe)
    ids = sorted(i for i in set(belege) | set(in_anhang) if i in reg)

    def schluessel(i: str):
        m = re.match(r"([A-Z][A-Z0-9]*?)(\d*)([A-Z]?)-(\d+)", i)
        return (m.group(1), int(m.group(2) or 0), m.group(3), int(m.group(4))) if m else (i, 0, "", 0)

    aus = [
        "Das Verzeichnis nennt alle im Buch zitierten Quellen mit ihrem Kürzel, wie es im Text in eckigen Klammern "
        f"steht. Qualität: A = Primärquelle ({konfig.wert('qualitaet_a', 'Gesetz, Gericht, Behörde')}), B = anerkannte "
        "Sekundärquelle, C = Fachmedien und Anbieterangaben. „Abruf“ nennt den Tag des Zugriffs, „Stand“ den Stand "
        "der Quelle, „Kap.“ die Kapitel, die sie zitieren (Text oder Lösungen), „Anhang B“ und „Anhang D“ Belege nur im "
        "Glossar oder im Annahmenverzeichnis. "
        + (konfig.wert("vertraulich_hinweis") + " " if konfig.wert("vertraulich_hinweis") else "")
        + f"Erfasst sind {len(ids)} Quellen.",
        "",
    ]
    for i in sorted(ids, key=schluessel):
        r = reg[i]
        titel = re.sub(r", Volltext(?: S\. [\d–]+)?", "", r["titel"].strip())
        herausgeber = ohne_arbeitsvermerke(r["herausgeber"].strip())
        url = r["url"].strip()
        if i in OHNE_HERAUSGEBER:
            herausgeber, url = "", ""
        ist_vertraulich = i in VERTRAULICH
        if ist_vertraulich:
            titel, herausgeber, url = VERTRAULICH[i][0], "", ""
        teile = []
        if herausgeber:
            teile.append(f"{herausgeber}:")
        teile.append(f"{titel}.")
        meta = []
        if ist_vertraulich:
            if VERTRAULICH[i][1]:
                meta.append(f"Stand {VERTRAULICH[i][1]}")
        elif r.get("stand_der_quelle", "").strip():
            stand = ohne_arbeitsvermerke(datum_de(r["stand_der_quelle"].strip()))
            if stand:
                meta.append(f"Stand {stand}")
        if r.get("abrufdatum", "").strip() and not ist_vertraulich:
            meta.append(f"Abruf {datum_de(r['abrufdatum'].strip())}")
        if r.get("qualität", "").strip():
            meta.append(f"Qualität {r['qualität'].strip()}")
        if i in belege:
            meta.append("Kap. " + ", ".join(str(n) for n in sorted(belege[i])))
        elif i in in_anhang:
            meta.append("Anhang " + ", ".join(sorted(in_anhang[i])))
        zeile = f"**[{i}]** " + " ".join(teile)
        if meta:
            zeile += " (" + "; ".join(meta) + ")"
        if url.startswith("http"):
            zeile += f" <{url}>"
        aus.append(zeile.replace("$", "\\$") + "\n")
    return "\n".join(aus)


def kompakt(text: str) -> str:
    """Verzeichnisse (D, E) in kleinerer Groteskschrift, ohne Blocksatz."""
    return (typst("#[\n#set text(font: sans, size: 9pt)\n#set par(justify: false, leading: 0.5em, spacing: 0.75em)")
            + "\n" + text + "\n" + typst("]"))


def optionaler_anhang(datei: str) -> str | None:
    p = KAPITEL / datei
    if not p.exists():
        return None
    return ueberschriften_tiefer(ohne_yaml(p.read_text(encoding="utf-8")))


def zusammensetzen(kapitel: list[int]) -> str:
    teile = [buch_yaml()]
    vorwort = KAPITEL / "vorwort.md"
    if vorwort.exists():
        teile.append(ohne_yaml(vorwort.read_text(encoding="utf-8")))
    kapiteltexte: dict[int, str] = {}
    for nr_teil, titel, nummern in TEILE:
        auswahl = [n for n in nummern if n in kapitel]
        if not auswahl:
            continue
        teile.append(teilseite(nr_teil, titel))
        for n in auswahl:
            t = ohne_yaml(kapiteldatei(n).read_text(encoding="utf-8"))
            kapiteltexte[n] = t
            teile.append("\n" + t + "\n")
    loesungen = anhang_loesungen()
    teile += [anhang_kopf("A", "Lösungen der Übungen"), loesungen]
    teile += [anhang_kopf("B", "Glossar"), anhang_glossar()]
    abk = optionaler_anhang("anhang_abkuerzungen.md")
    if abk:
        teile += [anhang_kopf("C", "Abkürzungen"), abk]
    teile += [anhang_kopf("D", "Annahmenverzeichnis"), kompakt(anhang_annahmen())]
    teile += [anhang_kopf("E", "Quellenverzeichnis"), kompakt(anhang_quellen(kapiteltexte, loesungen, anhaenge_mit_belegen()))]
    form = optionaler_anhang("anhang_formeln.md")
    if form:
        teile += [anhang_kopf("F", "Formelsammlung"), form]
    mod = optionaler_anhang("anhang_modelle.md")
    if mod:
        teile += [anhang_kopf("G", "Modellhandbuch M1–M4"), mod]
    teile += [anhang_kopf("H", "Stichwortverzeichnis"), typst("#stichwortverzeichnis()"),
              "::: {.nur-docx}\nDas Stichwortverzeichnis mit Seitenzahlen enthält die PDF-Fassung des Buchs.\n:::\n"]
    return "\n".join(teile)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kapitel", type=int, nargs="*", default=konfig.kapitelnummern())
    ap.add_argument("--name", default=konfig.wert("dateiname", "Lehrbuch"))
    ap.add_argument("--ziel", type=Path, default=HERE / "output")
    ap.add_argument("--nur-markdown", action="store_true")
    args = ap.parse_args()
    md = zusammensetzen(args.kapitel)
    args.ziel.mkdir(parents=True, exist_ok=True)
    (HERE / "output").mkdir(parents=True, exist_ok=True)
    md_pfad = HERE / "output" / f"{args.name}.md"
    md_pfad.write_text(md, encoding="utf-8")
    print(f"Markdown geschrieben: {md_pfad.relative_to(ROOT)} ({len(md):,} Zeichen)".replace(",", "."))
    if args.nur_markdown:
        return
    build.build_typst([md_pfad], args.ziel / f"{args.name}.pdf", args.name)


if __name__ == "__main__":
    main()
