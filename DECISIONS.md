# DECISIONS – Entscheidungsprotokoll

Jede Entscheidung mit ID, Datum, Anlass, Entscheidung und Status. Nur der Orchestrator schreibt hier.

## D-001 · TT.MM.JJJJ · Satzsystem und Layout aus dem Vorprojekt

**Anlass:** Das Buch soll Layout und Form des Lehrbuchs „Ökonomie von Batteriespeichern in Deutschland“ haben.

**Entscheidung:** Das Satzsystem (`07_build/`: Pandoc → Typst, Vorlage `typst/lehrbuch.typst`, Lua-Filter,
Schriften Caladea und Carlito) wird unverändert übernommen. Buchspezifische Angaben stehen nur in
`07_build/buch_config.yaml`. Lieferobjekte werden als PDF gesetzt; DOCX nur als Rückfallebene.

**Status:** beschlossen

## D-002 · TT.MM.JJJJ · Material aus dem Vorprojekt

**Anlass:** Das Vorprojekt hat Strommärkte, Regelreserve, Netzanschluss, EEG und weitere Erlösquellen aus Sicht
eines Batteriespeichers bereits an Primärquellen geprüft (Stand 04.10.2026).

**Entscheidung:** Die Kapitel 2, 3, 11, 12 und 15, das Glossar und 150 Quellen des Vorprojekts liegen unter
`00_input/vorprojekt_bess/` als Hintergrund. Befunde daraus gelten erst nach Nachprüfung in Welle 0 und erhalten
neue Quellen-IDs; Texte werden nicht übernommen, sondern neu geschrieben. Verweise auf das vertrauliche
Erlösgutachten des Vorprojekts werden nicht übernommen.

**Status:** beschlossen
