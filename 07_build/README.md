# Build: Markdown → PDF

Alle Lieferobjekte des Lehrbuchprojekts (Agenda, Kapitel, Berichte, Gesamtbuch) werden aus Markdown mit einer
gemeinsamen Pipeline gesetzt und als **PDF** ausgeliefert. Das Satzsystem ist aus dem Lehrbuch „Ökonomie von
Batteriespeichern in Deutschland“ übernommen; Layout, Kästen, Tabellen- und Abbildungsstil sind unverändert.
Ergebnis: Deckblatt, Inhaltsverzeichnis, Kopf- und Fußzeile mit lebendem Kolumnentitel, nummerierte Überschriften,
Tabellen und Abbildungen, Quellenzeilen, farbige Kästen, Formeln, PDF-Lesezeichen; im Gesamtbuch Teilseiten,
Anhänge A–H und Stichwortverzeichnis.

## Einrichtung

```bash
bash 07_build/einrichten.sh      # installiert die Python-Pakete aus requirements.txt (idempotent)
```

Die Schriften Caladea und Carlito liegen in `fonts/` (SIL Open Font License 1.1) und werden ohne
Systeminstallation verwendet.

## Aufruf

```bash
python3 07_build/build.py 01_agenda/AGENDA.md --ziel 01_agenda
python3 07_build/build.py 03_chapters/04_liquiditaet.md            # Einzelkapitel → 07_build/output/
python3 07_build/buch.py                                           # Gesamtbuch nach buch_config.yaml
python3 07_build/buch.py --kapitel 1 2 --name probe                # Probesatz mit ausgewählten Kapiteln
python3 07_build/preview.py 07_build/output/<datei>.pdf --ziel /tmp/vorschau   # Kontaktbögen zur Sichtprüfung
python3 07_build/build.py 07_build/output/<name>.md --engine docx --nur-docx --name <name>  # DOCX-Rückfallebene
```

## Buchkonfiguration

`buch_config.yaml` ist die einzige Stelle für buchspezifische Angaben: Titel, Untertitel, Kurztitel (Kopfzeile),
Dateiname, Stand, Daten- und Rechtsstand, Teile mit Kapitelnummern, Deckblattzeilen, Fußzeile, vertrauliche
Unterlagen für das Quellenverzeichnis, Stichwort-Ausnahmen. Nach der Agenda-Freigabe Teile und Kapitel eintragen,
vor jedem Gesamtbuch die Datumsangaben.

## Pipeline (Standard, `--engine typst`)

1. Pandoc setzt Markdown nach Typst. Der Lua-Filter `filter/lehrbuch.lua` wandelt Kästen (GitHub-Alert-Syntax) in
   `#kasten(...)`, berechnet Spaltenbreiten, setzt das deutsche Dezimalkomma in Formeln, markiert Quellenzeilen
   unter Tabellen und Abbildungen, setzt Stichwortmarken und bereitet die Metadaten für Deckblatt und Nummerierung
   auf.
2. Die Vorlage `typst/lehrbuch.typst` enthält das **gesamte Layout** (Farben, Schriften, Überschriften,
   Kapitelkopf, Kästen, Tabellenstil, Beschriftungen, Kopf- und Fußzeile, Deckblatt, Inhaltsverzeichnis,
   Stichwortverzeichnis). Layoutänderungen nur dort.
3. Typst (Python-Paket `typst`) erzeugt das PDF direkt; kein Word, kein LibreOffice.

Die temporäre `.typ`-Datei liegt während des Satzes im Projektverzeichnis, damit Bildpfade (`05_figures/…`)
aufgelöst werden; sie wird danach gelöscht. Fehlt ein Bild, bricht der Build mit „Satzfehler (Typst)“ und dem
gesuchten Pfad ab.

## Hilfsskripte

| Skript | Zweck |
|---|---|
| `anhang_loesungen.py <nn> …` | Lösungsanhang aus `06_review/K<nn>_loesungen_entwurf.md` |
| `glossar_merge.py <n> <vorschlag> [--schreiben]` | Glossarvorschlag eines Kapitels ins Glossar übernehmen |
| `stichwoerter.py` | Stichwortliste aus dem Glossar (`stichwoerter.json`) |
| `querverweise.py` | Verweise auf Abschnitte, Tabellen, Abbildungen und Übungen ohne Ziel |
| `offene_punkte.py` | Lückenliste, Verifikationsliste, Wortlaut der Kästen „Stand“ (Phase 7) |
| `preview.py` | Kontaktbögen eines PDFs |
| `muster/formatmuster.md`, `muster/abbildung_muster.py` | Beispiel aller Satzelemente und einer Abbildung |

## Build v1 (Rückfallebene, `--engine docx`)

`templates/make_reference_docx.py` (Formatvorlage) → Pandoc DOCX mit demselben Lua-Filter → `postprocess_docx.py`
(Kästen, Tabellenlayout); PDF-Export über LibreOffice (`pdf_export.py`) nur, wenn LibreOffice mit UNO vorhanden
ist. Nur nutzen, wenn eine bearbeitbare Word-Datei ausdrücklich verlangt wird (`--nur-docx`).

## Markdown-Konventionen (Kurzfassung, verbindlich siehe CLAUDE.md § 5)

- YAML-Kopf: `title`, `subtitle`, `date`, `kopfzeile-rechts`; optional `deckblatt-info`, `deckblatt-hinweis`,
  `inhaltsverzeichnis: true`, `toc-tiefe`, `nummerierung: kapitelweise`, `kapitel-start`, `h1-neue-seite: true`,
  `kolumnentitel: kapitel`.
- Kästen: `> [!NOTE]` / `[!TIP]` / `[!IMPORTANT]` / `[!WARNING]` / `[!BEISPIEL]` / `[!STAND]` / `[!DEFINITION]`,
  erste Zeile mit fettem Titel (z. B. `**Hier Fachleute einbinden:**`).
- Tabellen mit `Table: Titel` darunter, danach eine Zeile `Quelle: … (Stand TT.MM.JJJJ).`.
- Formeln in LaTeX-Syntax; Dezimalkomma als `{,}`. Seitenumbruch: `<!-- neue-seite -->`. Dollarzeichen maskieren.
