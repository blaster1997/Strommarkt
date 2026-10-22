#!/usr/bin/env python3
"""Build: Markdown → professionell gesetztes PDF.

Standard ist Build v2 (`--engine typst`): Pandoc → Typst mit eigener Vorlage
(`typst/lehrbuch.typst`) → PDF, ohne Word oder LibreOffice. Build v1 (`--engine docx`)
bleibt für Sonderfälle erhalten:

Schritte Build v1
  1. Formatvorlage (reference.docx) mit dokumentspezifischer Kopfzeile erzeugen
  2. Pandoc: Markdown → DOCX mit Lua-Filter (Kästen, Nummerierung, Deckblatt, TOC)
  3. Nachbearbeitung: Kästen, Tabellenlayout, Seitenumbrüche
  4. LibreOffice (UNO): Verzeichnisse aktualisieren, PDF exportieren

Beispiele
  python3 07_build/build.py 01_agenda/AGENDA.md --ziel 01_agenda
  python3 07_build/build.py 03_chapters/04_liquiditaet.md             # → 07_build/output/
  python3 07_build/build.py 07_build/muster/formatmuster.md            # Formatmuster (Layoutprobe)
  python3 07_build/build.py 01_agenda/AGENDA.md --engine docx --nur-docx   # Build v1

Metadaten im YAML-Kopf (Auswahl): title, subtitle, author, date, kopfzeile-links,
kopfzeile-rechts, fusszeile-links, deckblatt-info, deckblatt-hinweis,
inhaltsverzeichnis, toc-tiefe, nummerierung, kapitel-start, h1-neue-seite.
Ohne `kopfzeile-links` im Dokument gilt der Kurztitel aus `07_build/buch_config.yaml`.
Schriften: Caladea und Carlito liegen in `07_build/fonts/` (SIL Open Font License) und werden ohne
Systeminstallation verwendet.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE / "templates"))
from make_reference_docx import build as build_reference  # noqa: E402

sys.path.insert(0, str(HERE))
import konfig  # noqa: E402

SCHRIFTEN = HERE / "fonts"


def standard_metadaten(ordner: Path) -> Path:
    """Metadaten-Datei mit Vorgaben aus der Buchkonfiguration; Angaben im Dokument haben Vorrang."""
    pfad = ordner / "standard_metadaten.json"
    pfad.write_text(json.dumps({"kopfzeile-links": konfig.wert("kurztitel", konfig.wert("titel"))},
                               ensure_ascii=False), encoding="utf-8")
    return pfad


def pandoc_bin() -> str:
    # Vorrang hat das Pandoc aus pypandoc_binary (Version über requirements.txt festgelegt): Ältere
    # System-Pandocs (z. B. 3.1.3) setzen Tabellen mit Beschriftung nicht als Typst-Figure, dann fehlen
    # Tabellennummer und Beschriftung über der Tabelle.
    try:
        import pypandoc  # type: ignore

        return pypandoc.get_pandoc_path()
    except (ImportError, OSError):
        exe = shutil.which("pandoc")
        if exe:
            return exe
        raise


def read_meta(inputs: list[Path]) -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        tpl = Path(tmp) / "meta.tpl"
        tpl.write_text("$meta-json$", encoding="utf-8")
        out = subprocess.run([pandoc_bin(), *map(str, inputs), "-f", "markdown-smart",
                              "--template", str(tpl), "-t", "plain"],
                             check=True, capture_output=True, text=True).stdout
    try:
        return json.loads(out) if out.strip() else {}
    except json.JSONDecodeError:
        return {}


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        return " ".join(as_text(v) for v in value)
    return str(value)


# Pandoc schreibt für \cap das Symbol „sect“, das Typst ab 0.13 nur noch als „inter“ kennt. Ersetzt wird das frei
# stehende Wort (in Formeln steht es zwischen Leerzeichen); im deutschen Text kommt es nicht vor.
def typst_symbole(text: str) -> str:
    return re.sub(r"(?<=\s)sect(?=\s)", "inter", text)


def build_typst(inputs: list[Path], pdf: Path, name: str) -> None:
    """Build v2: Pandoc → Typst → PDF (ohne Word).

    Die .typ-Datei wird vorübergehend im Projektverzeichnis abgelegt, damit relative
    Bildpfade (05_figures/…) aufgelöst werden; Typst-Wurzel ist das Projektverzeichnis.
    """
    import typst  # pip install typst

    typ = ROOT / f".build_{name}.typ"
    with tempfile.TemporaryDirectory() as tmp:
        cmd = [pandoc_bin(), *map(str, inputs), "-f", "markdown-smart", "-t", "typst",
               "--template", str(HERE / "typst" / "lehrbuch.typst"),
               "--lua-filter", str(HERE / "filter" / "lehrbuch.lua"),
               "--metadata-file", str(standard_metadaten(Path(tmp))),
               "--metadata", "lang=de-DE", "-o", str(typ)]
        subprocess.run(cmd, check=True, cwd=str(ROOT))
    typ.write_text(typst_symbole(typ.read_text(encoding="utf-8")), encoding="utf-8")
    schriften = [str(SCHRIFTEN)] if SCHRIFTEN.is_dir() else []
    try:
        _, warnungen = typst.compile_with_warnings(str(typ), output=str(pdf), root=str(ROOT),
                                                   font_paths=schriften)
        for w in warnungen:
            print(f"Typst-Warnung: {w}")
    except typst.TypstError as fehler:
        # häufigste Ursache: Bildpfad falsch (Bilder relativ zum Projektverzeichnis: 05_figures/…)
        sys.exit(f"Satzfehler (Typst) in {name}: {fehler}")
    finally:
        typ.unlink(missing_ok=True)
    print(f"PDF geschrieben: {pdf}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("--name", help="Dateiname ohne Endung (Standard: erste Eingabedatei)")
    ap.add_argument("--ziel", type=Path, default=HERE / "output", help="Ausgabeordner")
    ap.add_argument("--engine", choices=["typst", "docx"], default="typst",
                    help="typst: direkter PDF-Satz (Standard); docx: Build v1 über Word/LibreOffice")
    ap.add_argument("--nur-docx", action="store_true", help="kein PDF erzeugen")
    ap.add_argument("--nur-pdf", action="store_true",
                    help="DOCX nur als temporäres Zwischenprodukt, Ausgabe nur PDF")
    args = ap.parse_args()

    inputs = [p.resolve() for p in args.inputs]
    meta = read_meta(inputs)
    name = args.name or inputs[0].stem
    args.ziel.mkdir(parents=True, exist_ok=True)
    if args.engine == "typst":
        build_typst(inputs, args.ziel / f"{name}.pdf", name)
        return
    pdf = args.ziel / f"{name}.pdf"
    tmp_docx_dir = tempfile.mkdtemp() if args.nur_pdf else None
    docx = (Path(tmp_docx_dir) if tmp_docx_dir else args.ziel) / f"{name}.docx"

    with tempfile.TemporaryDirectory() as tmp:
        ref = Path(tmp) / "reference.docx"
        build_reference(
            ref,
            as_text(meta.get("kopfzeile-links")) or konfig.wert("kurztitel", konfig.wert("titel")),
            as_text(meta.get("kopfzeile-rechts")) or as_text(meta.get("date")),
            as_text(meta.get("fusszeile-links"))
            or (f"Fassung vom {as_text(meta.get('date'))} – keine Rechts-, Steuer- oder Anlageberatung"
                if meta.get("date") else "Keine Rechts-, Steuer- oder Anlageberatung"),
        )
        resource_path = ":".join(sorted({str(p.parent) for p in inputs}
                                        | {str(ROOT / "05_figures"), str(ROOT)}))
        cmd = [pandoc_bin(), *map(str, inputs), "-f", "markdown-smart", "-t", "docx",
               "--reference-doc", str(ref), "--lua-filter", str(HERE / "filter" / "lehrbuch.lua"),
               "--resource-path", resource_path, "--metadata", "lang=de-DE",
               "-o", str(docx)]
        subprocess.run(cmd, check=True)
    subprocess.run([sys.executable, str(HERE / "postprocess_docx.py"), str(docx)], check=True)
    if not args.nur_pdf:
        print(f"DOCX: {docx}")
    if not args.nur_docx:
        subprocess.run(["/usr/bin/python3", str(HERE / "pdf_export.py"), str(docx), str(pdf)],
                       check=True)
    if tmp_docx_dir:
        shutil.rmtree(tmp_docx_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
