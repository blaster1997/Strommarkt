---
title: "Promptsammlung"
subtitle: "Lehrbuchprojekt „Der Strommarkt in Deutschland“ – Prompts, Leitfäden und Ablauf für Claude Code"
date: "21.10.2026"
kopfzeile-rechts: "Promptsammlung"
inhaltsverzeichnis: true
toc-tiefe: 2
deckblatt-info:
  - "Grundlage: Arbeitsweise, Layout und Erfahrungen des Lehrbuchs „Ökonomie von Batteriespeichern in Deutschland“"
  - "Inhalt: Einrichtung, Startprompt, Freigabe- und Arbeitsprompts je Phase, Steuerungs- und Lernprompts, Lehren aus dem Vorprojekt"
deckblatt-hinweis: "Die Prompts steuern Claude Code als Orchestrator. Das Buch ist keine Rechts-, Steuer- oder Anlageberatung."
---

# So arbeitest du mit dieser Sammlung {.unnumbered}

Das Starter-Kit enthält alles, was das neue Buchprojekt braucht: den Auftrag mit Pflicht-Themenliste von der Physik
des Stroms bis zum Netz, Referenzfällen und Modellen, einen Wissensstand mit 22 im Vorprojekt geprüften Befunden
und 55 Hypothesen, ausgewählte Kapitel, das Glossar und 150 geprüfte Quellen des BESS-Lehrbuchs, die Projektregeln
(`CLAUDE.md`), acht Agentendefinitionen, einen Leitfaden für die Kapitel, Vorlagen für alle Aufträge an Subagents
und das Satzsystem des BESS-Lehrbuchs mit Schriften, sodass das neue Buch genauso aussieht. Diese Sammlung enthält
die Prompts, die du in Claude Code eingibst, in der Reihenfolge des Projekts.

So setzt du sie ein:

- Jeder Prompt steht in einem grauen Block. Kopiere ihn vollständig in eine Nachricht an Claude Code.
- Platzhalter stehen in ⟨spitzen Klammern⟩; ersetze sie vor dem Senden.
- Claude Code arbeitet in Phasen und hält an jedem **STOP** an. Dann prüfst du das Ergebnis (Checkliste im
  vorletzten Kapitel) und gibst mit dem passenden Freigabe-Prompt frei oder verlangst Änderungen.
- Zwischen den STOPs reicht oft ein kurzes „Weiter“. Die ausführlichen Arbeitsprompts brauchst du, wenn du den
  Umfang steuern, Prioritäten setzen oder nach einer Unterbrechung neu ansetzen willst.
- Die Prompts an die Subagents schreibt Claude Code selbst; die Vorlagen dafür stehen in `06_review/VORLAGEN.md`.

# Einrichtung (einmalig)

1. **Repository anlegen:** Lege auf GitHub ein neues, privates Repository an (z. B. `lehrbuch_strommarkt`) und
   kopiere den Inhalt des Ordners `starterkit_strommarkt/` in seine Wurzel (oder entpacke das ZIP). Committe den
   Stand.
2. **Claude Code im Web:** Verbinde das Repository. Wähle eine Umgebung mit Netzwerkzugang, in der Primärquellen
   und Marktdaten erreichbar sind (u. a. gesetze-im-internet.de, recht.bund.de, eur-lex.europa.eu,
   dip.bundestag.de, bundesnetzagentur.de, acer.europa.eu, netztransparenz.de, regelleistung.net, smard.de,
   energy-charts.info, eex.com, transparency.entsoe.eu, marktstammdatenregister.de, destatis.de, PyPI). Als
   Setup-Skript der Umgebung eignet sich `bash 07_build/einrichten.sh`; es installiert Pandoc, Typst und die
   übrigen Python-Pakete. Die Schriften liegen im Kit.
3. **Eigene Unterlagen (optional):** Lege anonymisierte Unterlagen (z. B. Lieferverträge, PPAs, Gutachten,
   Angebote) unter `00_input/vertraulich/` ab (Dateiname neutral, z. B. `U1_ppa_entwurf.pdf`). Die Regeln zur
   Vertraulichkeit stehen in `CLAUDE.md` § 8.
4. **Anpassen vor dem Start (optional):** Prüfe im Auftrag (`00_input/AUFTRAG_Lehrbuch_Strommarkt.md`)
   Leserprofil, Erfolgskriterien, Referenzfälle und Vergleichsmärkte. Alles andere klärt Phase 1.
5. **Probe des Satzes:** Erster Prompt in der neuen Sitzung (prüft, ob das Layout wie im BESS-Buch gesetzt wird):

```
Führe bash 07_build/einrichten.sh aus und setze dann das Formatmuster:
python3 07_build/build.py 07_build/muster/formatmuster.md
Prüfe das PDF mit python3 07_build/preview.py 07_build/output/formatmuster.pdf
--ziel /tmp/vorschau und zeig mir das Ergebnis. Ändere nichts am Satzsystem.
```

# Start: Phase 0 und Phase 1

Der Startprompt verweist auf den Auftrag; dieser enthält alle Regeln, Phasen und STOPs.

```
Lies 00_input/AUFTRAG_Lehrbuch_Strommarkt.md vollständig und führe Abschnitt 12
aus: Phase 0 (Setup) und Phase 1 (Agenda-Vorschlag). Lies vorher CLAUDE.md,
00_input/WISSENSSTAND_Strommarkt.md, 00_input/vorprojekt_bess/README.md,
06_review/LEITFADEN_KAPITEL.md und 06_review/VORLAGEN.md; die Kapitel des
Vorprojekts mindestens querlesen. Halte jede Entscheidung in DECISIONS.md fest
und den Stand in PROGRESS.md. Setze den Agenda-Vorschlag als PDF, prüfe ihn
visuell und halte dann an (STOP) mit deinen höchstens sieben Rückfragen.
```

Erwartetes Ergebnis: `01_agenda/AGENDA_VORSCHLAG.md` und `.pdf` mit Buchziel, Leserprofil, Lernzielen,
Gliederungsalternativen, empfohlener Gliederung, Abgleich mit der Themenliste, Parametern der Referenzfälle R1–R6,
Umfangs- und Rechercheplan (mit Kennzeichnung der Vorarbeit aus dem Vorprojekt) sowie Rückfragen.

# Freigaben an den STOPs

## Phase 1 → 2: Agenda freigeben

```
Freigabe der Agenda mit folgenden Antworten und Änderungen:
1. ⟨Antwort auf Rückfrage 1⟩
2. ⟨Antwort auf Rückfrage 2⟩
3. ⟨…⟩

Änderungen an der Gliederung: ⟨z. B. Kapitel 13 und 14 zusammenlegen; eigenes
Kapitel zu Gas und CO₂ aufnehmen⟩. Referenzfälle: ⟨Parameter bestätigen oder
ändern⟩. Vergleichsmärkte: ⟨z. B. Großbritannien, Frankreich, Nordeuropa⟩.
Zielumfang: ⟨z. B. 600–700 Seiten für die Kapitel⟩.

Übertrage die Agenda nach 01_agenda/AGENDA.md (mit PDF), trage Teile und
Kapitel in 07_build/buch_config.yaml ein, halte alles in DECISIONS.md fest und
führe Phase 2 aus (Agenten prüfen und schärfen, RESEARCH_PLAN.md mit Welle 0
zuerst). Dann STOP.
```

## Phase 2 → 3: Agenten und Rechercheplan freigeben

```
Freigabe von Agenten und Rechercheplan. Starte Phase 3 mit Welle 0
(Nachprüfung der Befunde des Vorprojekts, der beweglichen Themen und der
Hypothesen am Primärtext, Ereignisse nach dem 04.10.2026 gezielt suchen; je ein
Auftrag für markt-, regulierungs-, netz-technik- und endkunden-rechercheur nach
Vorlage V2). Führe die Ergebnisse zusammen (merge_sources.py, SYNTHESE.md,
ANNAHMEN.md) und berichte mir kurz, welche Befunde überholt und welche
Hypothesen widerlegt wurden. Danach weiter mit den Wellen nach dem
Rechercheplan, den Datensnapshots und Phase 4, ohne auf mich zu warten, bis zum
nächsten STOP (Probekapitel).
```

## Phase 5 → 6: Probekapitel freigeben (Kalibrierung)

```
Freigabe der Probekapitel mit dieser Kalibrierung:
- Tiefe: ⟨passt / tiefer bei … / knapper bei …⟩
- Physik und Technik: ⟨so lassen / mehr Anschauung / weniger⟩
- Umfang: ⟨Richtwert = Agenda-Wörter × 1,3, Obergrenze × 1,4 bestätigen oder
  ändern⟩
- Stil: ⟨z. B. mehr Abbildungen aus realen Daten; weniger Normzitate im
  Fließtext; mehr Verweise zwischen den Märkten⟩
- Prüfschleife: ⟨vollständig beibehalten / Abschlussfaktencheck nur bei Kapiteln
  mit Rechtsänderungen⟩

Halte die Kalibrierung als Entscheidung fest, ergänze
06_review/LEITFADEN_KAPITEL.md (Vorbilder: die beiden Probekapitel) und starte
Phase 6 mit Teil ⟨I⟩. Nach jedem Teil ein kurzer Statusbericht, kein STOP außer
bei grundlegenden Widersprüchen.
```

## Phase 6 → 7: Gesamtredaktion freigeben

```
Phase 7 ist freigegeben. Arbeitspakete: Konsistenzprüfung (Skripte und Lektoren
je Buchteil, Einheiten und Zeitangaben), Vereinheitlichung der Kästen „Stand“,
Glossar mit englischen Entsprechungen, Anhänge C, F und G, Register abgleichen,
Stichwortverzeichnis, Gesamtbuch als PDF (DOCX nur als Rückfallebene),
Prüfliste vor Drucklegung mit Nachprüfung der beweglichen Themen und der
Jahreswerte, Abschlussbericht mit offenen Punkten und Empfehlungen. Halte die
Wortgrenzen ein und lass jede inhaltliche Änderung an freigegebenen Kapiteln per
Delta-Prüfung prüfen.
```

# Arbeitsprompts je Phase

## Phase 3: Recherche und Daten

Welle für einen Buchteil starten (wenn du die Reihenfolge selbst steuern willst):

```
Starte die Recherche für Teil ⟨II⟩ (Kapitel ⟨4–8⟩) nach RESEARCH_PLAN.md: 2–4
Agenten parallel, je 10–25 Tool-Aufrufe, Aufträge nach Vorlage V1 in
06_review/VORLAGEN.md. Danach Notizen prüfen (Stichproben am Primärtext),
Register zusammenführen, SYNTHESE.md und ANNAHMEN.md nachführen. Kurzbericht:
neue Befunde, Widersprüche, Lücken.
```

Marktdaten für Modelle und Abbildungen beschaffen:

```
Lege die Datensnapshots für M1 und M2 an (Vorlage V16): Day-Ahead-Preise DE-LU,
Last, Einspeisung Wind an Land, Wind auf See und Solar, Marktwerte, reBAP, für
⟨2019 bis heute⟩, in der Auflösung der Quelle. Nur frei zugängliche Endpunkte,
keine API-Schlüssel. Prüfe die Jahresmittel gegen eine zweite Quelle und
berichte Abweichungen.
```

Nachrecherche bei Lücken:

```
In SYNTHESE.md sind für Kapitel ⟨n⟩ folgende Lücken offen: ⟨Liste⟩. Prüfe,
welche sich mit Primärquellen schließen lassen, und beauftrage höchstens zwei
Agenten (Vorlage V3). Was nicht belegbar ist, bleibt als [LÜCKE: …] stehen.
```

## Phase 4: Modelle

```
Baue die Modelle nach Abschnitt 4.2 des Auftrags in dieser Reihenfolge: M1
(Merit Order und Kraftwerkseinsatz), M2 (Erneuerbare: Marktwerte, Förderung,
PPA), M3 (Beschaffung und Risiko), M4 (Netz und Endkundenpreis). Je Modell ein
Auftrag an den modellierer (Vorlage V9), Markt- und Rechtsregeln nur aus Notizen
mit Primärbeleg, Daten nur aus Snapshots mit Manifest, pytest grün, Lauf-IDs und
kapitelzahlen.md für die Referenzfälle R1–R6. Vergleiche M1 mit den realen
Day-Ahead-Preisen, prüfe die Kernzahlen mit einer Handrechnung und berichte
kurz.
```

## Phase 5: Probekapitel

```
Schreibe die zwei Probekapitel ⟨6 „Day-Ahead-Markt und Marktkopplung“ und 17
„Direktvermarktung und negative Preise“⟩ in der vollen Schleife: autor →
faktenpruefer → autor → lektor → Abschlussfaktencheck. Setze beide als PDF,
prüfe sie visuell und lege sie mir mit einer kurzen Einschätzung zu Tiefe,
Umfang und offenen Punkten vor (STOP).
```

## Phase 6: Kapitel schreiben

Teil bearbeiten (Standardfall):

```
Bearbeite Teil ⟨III⟩ (Kapitel ⟨9–12⟩) in der Schreib-Prüf-Schleife nach
06_review/LEITFADEN_KAPITEL.md, höchstens fünf Agenten gleichzeitig. Je Kapitel
nach der Freigabe: Glossar, Lösungen, Register und Annahmen übernehmen, PDF
setzen, D-Entscheidung, PROGRESS.md, Commit. Am Ende des Teils ein Statusbericht
(Wörter, offene Lücken, Befunde).
```

Kapitel freigeben, wenn der Abschlussfaktencheck vorliegt:

```
Setze die Auflagen aus 06_review/K⟨nn⟩_faktencheck_v2.md um (mittel und höher
vollständig, niedrig soweit die Wortgrenze reicht), prüfe die Änderungen selbst,
übernimm Glossar, Lösungen und Quellen und gib Kapitel ⟨n⟩ frei (D-Entscheidung,
PDF, PROGRESS.md).
```

Neue Modellwerte oder Daten in fertige Kapitel übernehmen:

```
Nach dem Neulauf ⟨Lauf-ID⟩ bzw. dem neuen Datensnapshot ⟨Name⟩ stimmen Werte in
den Kapiteln ⟨Liste⟩ nicht mehr. Ermittle alle betroffenen Stellen (Text,
Tabellen, Abbildungen, Lösungen, Annahmen), lass sie vom autor nachführen und
anschließend per Delta-Prüfung (Vorlage V8) prüfen. Archivwerte nur noch
gekennzeichnet.
```

## Phase 7: Gesamtredaktion und Build

Konsistenzprüfung:

```
Führe die Konsistenzprüfung aus: python3 07_build/querverweise.py,
offene_punkte.py, Konsistenzprüfung je Buchteil durch lektor (Vorlage V11),
Parameter der Referenzfälle gegen DECISIONS.md, Einheiten (MW/MWh, ct/kWh,
Stunde/Viertelstunde) buchweit. Setze die Befunde um (Delta-Prüfung für
inhaltliche Änderungen) und berichte.
```

Verzeichnisse und Anhänge:

```
Erstelle die Anhänge C (Abkürzungen), F (Formelsammlung) und G (Modellhandbuch)
mit Vorlage V12, das Glossar mit englischen Entsprechungen (V15) und die
Stichwortliste (python3 07_build/stichwoerter.py). Gleiche das Register ab:
python3 sources/kapitel_abgleichen.py --schreiben und python3
sources/merge_sources.py.
```

Prüfliste vor Drucklegung und Nachprüfung:

```
Erstelle die Prüfliste vor Drucklegung (Vorlage V13) aus den Kästen „Stand“.
Vereinheitliche widersprüchliche Kästen, soweit die Wortgrenzen es erlauben, und
lass die dringendsten beweglichen Themen und die Jahreswerte (Umlagen,
Netzentgelte, Stromsteuer) am Primärtext nachprüfen (Vorlage V3). Was offen
bleibt, steht in der Prüfliste mit Termin und betroffenen Rechnungen.
```

Gesamtbuch und Abschlussbericht:

```
Setze das Gesamtbuch mit python3 07_build/buch.py (Stand, Datenstand und
Rechtsstand vorher in 07_build/buch_config.yaml eintragen), prüfe es visuell
(Deckblatt, Teile, Kapitelköpfe, Tabellen, Abbildungen, Anhänge,
Stichwortverzeichnis), erzeuge die DOCX-Rückfallebene und schreibe den
Abschlussbericht (Lieferobjekte, Gesamtredaktion, Qualitätsstand, offen vor
Drucklegung, Empfehlungen; Anlagen Prüfliste, Verifikationsliste, Lückenliste).
Setze den Bericht als PDF, committe Buch-PDF, DOCX und Bericht und schick mir
die Dateien.
```

# Steuerungsprompts (jederzeit)

Stand abfragen:

```
Wo stehen wir? Bitte kurz: abgeschlossene Schritte, laufende Agenten, nächster
STOP, offene Entscheidungen für mich.
```

Nach Unterbrechung oder neuer Sitzung weitermachen:

```
Lies CLAUDE.md, PROGRESS.md und die letzten Einträge in DECISIONS.md, prüfe git
status und git log und setze die Arbeit an der Stelle fort, an der sie stehen
geblieben ist. Starte keine Agenten doppelt.
```

Weniger Prüfaufwand (bewusste Abwägung):

```
Für die Kapitel ⟨Liste⟩ reicht ein Faktencheck mit anschließender Korrektur; den
Abschlussfaktencheck nur, wenn der erste Faktencheck einen kritischen oder hohen
Befund hatte oder Rechtsstände geändert wurden. Halte das als Entscheidung fest.
```

Neue Unterlage einarbeiten:

```
Ich habe ⟨Datei⟩ unter 00_input/vertraulich/ abgelegt (Unterlage ⟨U2⟩,
anonymisiert). Analysiere sie nach Vorlage V14, schlag vor, wo sie im Buch
hilft, und warte auf meine Freigabe, welche Zahlen verwendet werden dürfen.
```

Erratum an einem freigegebenen Kapitel:

```
In Kapitel ⟨n⟩ ist ⟨Aussage⟩ falsch bzw. veraltet (Beleg: ⟨Quelle⟩). Korrigiere
die Stelle und alle Folgestellen (andere Kapitel, Lösungen, Glossar, Annahmen),
lass die Änderung per Delta-Prüfung prüfen und halte das Erratum in DECISIONS.md
fest.
```

Neues Ereignis im Markt oder in der Regulierung (z. B. Beschluss, Festlegung,
Ausschreibungsergebnis):

```
Am ⟨TT.MM.JJJJ⟩ wurde ⟨Ereignis, z. B. das EEG 2027 beschlossen⟩. Prüfe es am
Primärtext (Vorlage V3), ermittle alle betroffenen Kapitel, Kästen „Stand“,
Rechnungen und Annahmen und schlag mir vor, was nachzuführen ist. Nach meiner
Freigabe nachführen und per Delta-Prüfung prüfen lassen.
```

Jahreswerte nachführen (jährlich ab Oktober, wenn die ÜNB die Umlagen des
Folgejahres veröffentlichen):

```
Führe die Jahreswerte für ⟨JJJJ⟩ nach: Umlagen nach EnFG und KWKG,
Offshore-Netzumlage, Aufschlag für besondere Netznutzung,
Übertragungsnetzentgelte und Zuschüsse, Stromsteuer, Höchstwerte der
Ausschreibungen. Erst am Primärtext prüfen (Vorlage V3), dann M4 neu rechnen
und die Kapitel per Delta-Prüfung nachführen.
```

Wenn ein Agent an Berechtigungen scheitert:

```
Welche Aktion wurde abgelehnt, von welchem Agenten, und wofür wird sie
gebraucht? Versuche es nicht auf anderem Weg; ich entscheide über die Freigabe.
```

# Lernprompts (für dich als Leser)

Das Buch soll dir helfen, den Strommarkt zu verstehen. Diese Prompts nutzt du, wenn Kapitel fertig sind; sie
ändern nichts am Buch.

Kapitel in eigenen Worten erklären lassen:

```
Erkläre mir Kapitel ⟨n⟩ auf einer Seite: die fünf wichtigsten Zusammenhänge,
eine Zahl mit Quelle je Zusammenhang und wie das Kapitel mit den Kapiteln davor
und danach zusammenhängt. Nur aus dem freigegebenen Kapiteltext, nichts Neues.
```

Zusammenhänge zwischen den Märkten zeigen:

```
Zeig mir am Beispiel ⟨eines sonnigen Sonntags im Mai / einer Dunkelflaute im
Januar⟩, wie Terminmarkt, Day-Ahead, Intraday, Ausgleichsenergie, Regelreserve,
Redispatch, Marktprämie und Endkundenpreis zusammenwirken. Nutze nur Aussagen
und Zahlen aus dem Buch mit Kapitelverweis.
```

Selbsttest:

```
Stell mir zehn Fragen zu Teil ⟨II⟩, gemischt aus Rechnen, Erklären und
Bewerten. Warte nach jeder Frage auf meine Antwort und korrigiere sie mit
Verweis auf das Kapitel.
```

# Dateien des Starter-Kits

| Baustein | Datei und Zweck |
|---|---|
| Auftrag | `00_input/` `AUFTRAG_Lehrbuch_Strommarkt.md`: Masterauftrag mit Ziel, Phasen und STOPs, Pflicht-Themenliste A–N, Referenzfällen R1–R6, Modellen M1–M4, Agenten, Quellenregeln, Didaktik, Struktur, Stil, Satz und Vertraulichkeit |
| Wissensstand | `00_input/` `WISSENSSTAND_Strommarkt.md`: geprüfte Befunde B-01 bis B-22 aus dem Vorprojekt, Hypothesen H-01 bis H-55, bewegliche Themen T1–T14, Fallkandidaten, vorläufige Gliederung, Datenquellen, offene Fragen |
| Vorprojekt | `00_input/` `vorprojekt_bess/`: Kapitel 2, 3, 11, 12 und 15 des BESS-Lehrbuchs, Glossar und 150 geprüfte Quellen mit Regeln zur Verwendung |
| Projektregeln | `CLAUDE.md`: dauerhafte Regeln für Orchestrator und Subagents |
| Agenten | `.claude/agents/`: markt-, regulierungs-, netz-technik- und endkunden-rechercheur, modellierer, autor, faktenpruefer, lektor |
| Start-Hook | `.claude/settings.json` und `.claude/hooks/`: richtet die Satzumgebung in Claude Code im Web ein |
| Leitfaden | `06_review/` `LEITFADEN_KAPITEL.md`: Schreib-Prüf-Schleife, Umfang, Konventionen, Schreibweisen, Erfahrungen des Vorprojekts |
| Vorlagen | `06_review/VORLAGEN.md`: Auftragsvorlagen V1–V16 für Subagents und Vorlagen der Prüfdateien |
| Satzsystem | `07_build/`: Pandoc → Typst mit Vorlage, Filter, Schriften, `buch_config.yaml`, Formatmuster und Hilfsskripten |
| Quellenregister | `sources/`: Register mit Skripten zum Zusammenführen und Abgleichen |
| Statusdateien | `PROGRESS.md`, `DECISIONS.md`, `ANNAHMEN.md`, `GLOSSAR.md` (Vorlagen) |
| Promptsammlung | `PROMPTS.md`: diese Sammlung |
| Ansicht | `ansicht/`: diese Sammlung, Auftrag, Wissensstand und Formatmuster als PDF im Buchlayout |

Table: Inhalt des Starter-Kits

Quelle: Starter-Kit (Stand 21.10.2026).

| Befehl | Wirkung |
|---|---|
| `python3 07_build/build.py <datei>.md` | Einzeldokument als PDF (Kapitel, Agenda, Bericht) |
| `python3 07_build/buch.py` | Gesamtbuch mit Teilen und Anhängen A–H |
| `python3 07_build/preview.py <pdf> --ziel <ordner>` | Kontaktbögen zur Sichtprüfung |
| `python3 07_build/anhang_loesungen.py <nn> …` | Lösungsanhang aus den Lösungsentwürfen |
| `python3 07_build/glossar_merge.py <n> <vorschlag> --schreiben` | Glossarvorschlag eines Kapitels übernehmen |
| `python3 sources/merge_sources.py` | Quellenregister aus den csv-Blöcken der Notizen |
| `python3 sources/kapitel_abgleichen.py --schreiben` | Kapitelfeld des Registers auf die zitierenden Kapitel setzen |
| `python3 07_build/stichwoerter.py` | Stichwortliste aus dem Glossar |
| `python3 07_build/querverweise.py` | Verweise ohne Ziel finden |
| `python3 07_build/offene_punkte.py` | Lücken, Verifikationsliste, Kästen „Stand“ |

Table: Werkzeuge des Satzsystems

Quelle: Starter-Kit (Stand 21.10.2026).

# Checkliste für dich an jedem STOP

- **Agenda (Phase 1):** Deckt die Gliederung alles ab, was du verstehen willst, von der Physik bis zum Netz? Sind
  die Märkte vollständig (Termin, Day-Ahead, Intraday, Ausgleichsenergie, Regelreserve, Kapazität, PPA,
  Herkunftsnachweise)? Sind die Referenzfälle realistisch und decken sie Verbraucher, Erzeuger und Speicher ab?
  Sind die Vergleichsmärkte die richtigen? Stimmt die Tiefe bei Physik und Recht?
- **Agenten und Rechercheplan (Phase 2):** Beginnt die Recherche mit der Nachprüfung der Befunde des Vorprojekts
  und der beweglichen Themen? Sind die Aufträge der vier Rechercheure klar abgegrenzt? Sind die Datenquellen für
  die Modelle frei zugänglich?
- **Probekapitel (Phase 5):** Tiefe, Umfang, Lesbarkeit, Abbildungen aus realen Daten, Rechenbeispiele,
  Praxis-Checks; Einheiten und Zeitangaben sauber; Normzitate korrekt und nicht zu dicht; Zusammenhänge zu
  anderen Märkten sichtbar; Layout wie im BESS-Buch.
- **Statusberichte (Phase 6):** Lücken, die du mit eigenen Unterlagen schließen kannst; Widersprüche, die eine
  Entscheidung brauchen; neue Ereignisse, die nachgeführt werden müssen.
- **Abschluss (Phase 7):** Prüfliste vor Drucklegung, Jahreswerte, Verifikationsliste der Belege, empfohlene
  Modellläufe, Stellen „Hier Fachleute einbinden“.

# Lehren aus dem Vorprojekt

Das BESS-Lehrbuch entstand in diesem Ablauf zwischen dem 27.09. und dem 04.10.2026: 26 Kapitel in neun Teilen,
844 Seiten mit Anhängen A–H, 1.081 erfasste Quellen, davon 614 im Buch belegt, vier Modelle mit 488 Tests. Daraus
folgen einige Empfehlungen, die in `CLAUDE.md` und im Leitfaden bereits berücksichtigt sind:

1. **Probekapitel ernst nehmen.** Tiefe und Umfang erst nach den Probekapiteln festlegen; danach gelten
   Wortgrenzen streng. Plane je Kapitel 5–10 % Reserve unter der Obergrenze ein, sonst kostet jede spätere
   Korrektur Kürzungen an anderer Stelle.
2. **Rechts- und Marktstände früh und einheitlich datieren.** Kästen „Stand“ mit Prüfdatum, Fundstelle, Status
   und nächstem Ereignis; gleiche Themen in allen Kapiteln gleich formulieren. Die Prüfliste vor Drucklegung von
   Anfang an in `PROGRESS.md` sammeln. Im Strommarkt ändern sich Regeln im Monatstakt.
3. **Welle 0 zuerst.** Befunde und Hypothesen am Primärtext prüfen, bevor geschrieben wird; im Vorprojekt hat das
   mehrere falsche Ausgangsannahmen früh korrigiert.
4. **Einheiten und Zeitauflösung prüfen.** Die häufigsten inhaltlichen Fehler im Vorprojekt betrafen MW und MWh,
   Stunden und Viertelstunden (seit dem 01.10.2025 am Day-Ahead-Markt) sowie Zählweisen (z. B. negative Stunden).
   Jede Zahl braucht ihre Abgrenzung.
5. **Modellwerte nur mit Lauf-ID, Daten nur als Snapshot.** Nach jedem Neulauf alle Kapitel mit Werten des Modells
   per Delta-Prüfung nachführen; alte Läufe als Archiv kennzeichnen. Quellenzeilen mit Modellwerten tragen das
   Datum der Lauf-ID.
6. **Eine Quelle der Wahrheit je Verzeichnis.** Glossar, Annahmen und Register pflegt nur der Orchestrator;
   Agenten liefern Vorschläge und csv-Blöcke. Das Stichwortverzeichnis entsteht aus dem Glossar.
7. **Suchauszüge kennzeichnen.** Was nur als Suchauszug vorliegt, landet automatisch auf der Verifikationsliste;
   gesperrte Seiten (z. B. epexspot.com für automatisierte Abrufe) werden nicht umgangen, sondern über andere
   Primärquellen belegt.
8. **Höchstens fünf Agenten gleichzeitig, Aufträge als Datei.** Lange Aufträge als Datei im Scratchpad ablegen
   und den Agenten nur den Pfad geben; Rückmeldungen kurz, Details in Dateien.
9. **Satzfallen.** Unmaskierte Dollarzeichen, falsche Bildpfade, überbreite Tabellen und Überschriften, die mit
   „1. “ beginnen, sind die häufigsten Satzfehler; das Formatmuster zeigt die richtige Form.
10. **Berechtigungen und Vertraulichkeit.** Lehnt das System eine Aktion eines Agenten ab, nicht umgehen, sondern
    dem Auftraggeber melden. Vertrauliche Unterlagen nur unter ihrer Bezeichnung und mit Fundstelle; Verwendung
    der Zahlen ausdrücklich freigeben lassen.
