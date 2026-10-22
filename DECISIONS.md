# DECISIONS – Entscheidungsprotokoll

Jede Entscheidung mit ID, Datum, Anlass, Entscheidung und Status. Nur der Orchestrator schreibt hier.

## D-001 · 22.10.2026 · Satzsystem und Layout aus dem Vorprojekt

**Anlass:** Das Buch soll Layout und Form des Lehrbuchs „Ökonomie von Batteriespeichern in Deutschland“ haben.

**Entscheidung:** Das Satzsystem (`07_build/`: Pandoc → Typst, Vorlage `typst/lehrbuch.typst`, Lua-Filter,
Schriften Caladea und Carlito) wird unverändert übernommen. Buchspezifische Angaben stehen nur in
`07_build/buch_config.yaml`. Lieferobjekte werden als PDF gesetzt; DOCX nur als Rückfallebene.

**Status:** beschlossen

## D-002 · 22.10.2026 · Material aus dem Vorprojekt

**Anlass:** Das Vorprojekt hat Strommärkte, Regelreserve, Netzanschluss, EEG und weitere Erlösquellen aus Sicht
eines Batteriespeichers bereits an Primärquellen geprüft (Stand 04.10.2026).

**Entscheidung:** Die Kapitel 2, 3, 11, 12 und 15, das Glossar und 150 Quellen des Vorprojekts liegen unter
`00_input/vorprojekt_bess/` als Hintergrund. Befunde daraus gelten erst nach Nachprüfung in Welle 0 und erhalten
neue Quellen-IDs; Texte werden nicht übernommen, sondern neu geschrieben. Verweise auf das vertrauliche
Erlösgutachten des Vorprojekts werden nicht übernommen.

**Status:** beschlossen

## D-003 · 22.10.2026 · Pandoc-Version im Satz

**Anlass:** Die Probe des Satzsystems (Phase 0) setzte das Formatmuster zunächst mit dem System-Pandoc 3.1.3 der
Umgebung. Dessen Typst-Ausgabe macht aus Tabellen mit Beschriftung keine Typst-Figure: Tabellennummer
(„Tabelle 1.2:“) und Beschriftung über der Tabelle fehlten, die Beschriftung stand zentriert darunter. Das
Referenz-PDF `ansicht/Formatmuster.pdf` zeigt die richtige Form.

**Entscheidung:** `07_build/build.py` (Funktion `pandoc_bin`) nutzt vorrangig das Pandoc aus `pypandoc_binary`
(über `07_build/requirements.txt` installiert; am 22.10.2026 Pandoc 3.9) und greift nur ohne dieses Paket auf ein
System-Pandoc zurück. Layout, Vorlage und Filter bleiben unverändert. Ergebnis: Das Formatmuster wird
seitengleich zum Referenz-PDF gesetzt (5 Seiten, Tabellen 1.1 und 1.2, Abbildung 1.1, alle Kästen).

**Status:** umgesetzt

## D-004 · 22.10.2026 · Arbeitsdatum, Vorabrecherche und Agentenaufruf in Phase 1

**Anlass:** Der Auftrag (Abschnitt 12) erlaubt vor dem Agenda-Vorschlag nur so viel Webrecherche, wie für eine
aktuelle und vollständige Gliederung nötig ist. Seit dem Stand des Vorprojekts (04.10.2026) können sich bewegliche
Themen geändert haben. Die Rollen aus `.claude/agents/` stehen in dieser Sitzung nicht als eigene Subagent-Typen
zur Verfügung.

**Entscheidung:** Arbeitsdatum der Phasen 0 und 1 ist der 22.10.2026. Vier kurze Vorabrecherchen (P1-R Recht,
P1-M Markt und Datenquellen, P1-E Endkunden, P1-S Struktur vergleichbarer Werke und Monitoringbericht) mit je 20–25
Tool-Aufrufen prüfen nur den Status der beweglichen Themen T1–T14 und Ereignisse seit dem 04.10.2026; Notizen unter
`02_research/P1_vorab/`, Quellen-IDs `P1<Kürzel>-<nn>`. Sie ersetzen die Welle 0 nicht. Agenten werden als
allgemeine Agenten mit Verweis auf ihre Rollenbeschreibung beauftragt (`CLAUDE.md` § 7).

**Status:** umgesetzt

