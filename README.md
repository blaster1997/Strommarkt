# Starter-Kit: Lehrbuch „Der Strommarkt in Deutschland“

Vom Strom selbst bis zum Netz: Physik, Akteure, Großhandel (Terminmarkt, Day-Ahead, Intraday, PPAs),
Bilanzkreise und Regelreserve, Kapazitätsmärkte, EEG und Ausschreibungen, Direktvermarktung, Netz und
Netzentgelte, Endkundenpreis und Regulierung in Deutschland und der EU. Dieses Kit startet ein neues
Claude-Code-Projekt mit derselben Arbeitsweise und demselben Layout wie das Lehrbuch „Ökonomie von
Batteriespeichern in Deutschland“: Phasen mit Freigaben, Orchestrator mit acht Subagents, Schreib-Prüf-Schleife je
Kapitel, Quellen- und Annahmenregister, Rechenmodelle mit Datensnapshots, Satz als PDF über Pandoc und Typst.

## Schnellstart

1. Neues Repository anlegen und den Inhalt dieses Ordners in die Wurzel kopieren; committen.
2. In Claude Code (Web) das Repository öffnen; Umgebung mit Netzwerkzugang zu den Primärquellen, den Datenquellen
   der Netzbetreiber und Börsen und zu PyPI. Der SessionStart-Hook (`.claude/settings.json`) richtet die
   Satzumgebung ein; alternativ `bash 07_build/einrichten.sh` als Setup-Skript der Umgebung.
3. Optional: anonymisierte eigene Unterlagen (Verträge, PPAs, Gutachten) nach `00_input/vertraulich/`.
4. Den Startprompt aus `PROMPTS.md` (Kapitel „Start: Phase 0 und Phase 1“) senden und an jedem STOP mit den
   Freigabe-Prompts weiterarbeiten.

## Inhalt

| Pfad | Zweck |
|---|---|
| `PROMPTS.md` | Promptsammlung: Einrichtung, Startprompt, Freigaben, Arbeits-, Steuerungs- und Lernprompts, Lehren aus dem Vorprojekt |
| `00_input/AUFTRAG_Lehrbuch_Strommarkt.md` | Masterauftrag (Ziel, Phasen, Themenliste A–N, Referenzfälle R1–R6, Modelle M1–M4, Agenten, Regeln) |
| `00_input/WISSENSSTAND_Strommarkt.md` | geprüfte Befunde aus dem Vorprojekt, Hypothesen, bewegliche Themen, Fallkandidaten, vorläufige Gliederung, Datenquellen |
| `00_input/vorprojekt_bess/` | Kapitel 2, 3, 11, 12 und 15, Glossar und 150 geprüfte Quellen des BESS-Lehrbuchs (Hintergrund, vor Verwendung neu prüfen) |
| `CLAUDE.md` | dauerhafte Projektregeln für Orchestrator und Subagents |
| `.claude/agents/` | markt-, regulierungs-, netz-technik-, endkunden-rechercheur, modellierer, autor, faktenpruefer, lektor |
| `.claude/settings.json`, `.claude/hooks/` | SessionStart-Hook für Claude Code im Web |
| `06_review/LEITFADEN_KAPITEL.md` | Schreib-Prüf-Schleife, Umfang, Konventionen |
| `06_review/VORLAGEN.md` | Auftragsvorlagen V1–V16 und Vorlagen der Prüfdateien |
| `07_build/` | Satzsystem mit Vorlage, Filter, Schriften, `buch_config.yaml`, Formatmuster |
| `sources/` | Quellenregister und Skripte |
| `PROGRESS.md`, `DECISIONS.md`, `ANNAHMEN.md`, `GLOSSAR.md` | Statusdateien (Vorlagen) |
| `ansicht/` | PDF-Fassungen von Promptsammlung, Auftrag, Wissensstand und Formatmuster im Buchlayout (zum Lesen; für den Betrieb nicht nötig) |

## Satz prüfen

```bash
bash 07_build/einrichten.sh
python3 07_build/build.py 07_build/muster/formatmuster.md
python3 07_build/preview.py 07_build/output/formatmuster.pdf --ziel /tmp/vorschau
```

Das Buch ist keine Rechts-, Steuer- oder Anlageberatung. Die Schriften Caladea und Carlito stehen unter der SIL
Open Font License 1.1 (`07_build/fonts/`).
