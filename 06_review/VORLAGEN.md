# Vorlagen für Aufträge an Subagents und für Prüfdateien

Diese Vorlagen nutzt der Orchestrator, wenn er Arbeit an Subagents delegiert (CLAUDE.md § 7). Subagents sehen den
Dialog mit dem Auftraggeber nicht; alles, was sie brauchen, steht im Auftrag oder in `CLAUDE.md`. Platzhalter
stehen in ⟨spitzen Klammern⟩. Bewährt hat sich, den Auftrag als Datei im Scratchpad abzulegen und dem Agenten nur
den Pfad zu geben („Lies den Auftrag in … vollständig und führe ihn aus.“). Jeder Auftrag enthält die sechs Punkte
der Delegationsvorlage: Ziel, Abgrenzung, Quellen, Ausgabe, Aufwand, Rückmeldung.

## V1 Kapitelrecherche (Recherche-Agent)

```
⟨Agent⟩-Auftrag ⟨Auftrags-ID, z. B. W2-M1⟩ für Kapitel ⟨n⟩ „⟨Titel⟩“. Arbeitsverzeichnis ⟨Pfad⟩. Arbeitsdatum ⟨TT.MM.JJJJ⟩.
Lies zuerst CLAUDE.md, 01_agenda/AGENDA.md (Kapitel ⟨n⟩), 00_input/WISSENSSTAND_Strommarkt.md (B-⟨…⟩, H-⟨…⟩) und
⟨Vorprojekt-Kapitel in 00_input/vorprojekt_bess/, falls einschlägig⟩.

## Ziel
Belegte Grundlage für die Abschnitte ⟨n.1–n.x⟩: ⟨Fragen, die das Kapitel beantworten muss; welche Zahlen, Normen,
Marktregeln, Daten, Beispiele gebraucht werden⟩. Die Befunde fließen in ⟨Kapitel, Modell M…, Annahmen A-…⟩.

## Abgrenzung
Nicht Teil dieses Auftrags: ⟨Themen anderer Agenten oder Kapitel⟩.

## Quellen
Primärquellen zuerst: ⟨Normen, Festlegungen, Marktregeln, Daten der Netzbetreiber und Börsen, Statistik⟩. Suche
erst breit, dann eng. Belege im Volltext lesen; „Suchauszug“ nur, wenn ein Abruf technisch scheitert. Keine Sperren
umgehen, keine Logins, keine API-Schlüssel.

## Ausgabe (nur diese Datei, kein git)
02_research/K⟨nn⟩_⟨slug⟩/notizen_⟨markt|regulierung|netz|endkunden⟩.md im Format deiner Agentendefinition, mit
Tabelle je Thema (Aussage, Zahl + Einheit bzw. Norm/Festlegung, Markt/Auflösung/Abgrenzung, Stand/Fassung,
Quelle-ID, Qualität A/B/C, Fakt/Schätzung/Annahme, Volltext/Suchauszug), Abweichungen zu Befunden und Hypothesen,
Lücken, Konsequenzen und csv-Block (IDs K⟨nn⟩⟨Kürzel⟩-⟨nn⟩).

## Aufwand
Tool-Budget ⟨10–25⟩ Aufrufe; abbrechen, wenn neue Quellen nichts Neues liefern.

## Rückmeldung
Höchstens 15 Zeilen plus offene Punkte. Wenn das Berechtigungssystem eine Aktion ablehnt, nicht auf anderem Weg
versuchen, sondern melden.
```

## V2 Welle 0: Verifikation der Befunde, Hypothesen und beweglichen Themen

```
regulierungs-rechercheur, Auftrag W0-R⟨n⟩. Ziel: die Befunde ⟨B-12 bis B-14, B-16, B-18 bis B-22⟩, die Hypothesen
⟨H-09, H-11, H-25 bis H-36, H-38 bis H-40, H-48 bis H-50, H-53⟩ und die beweglichen Themen ⟨T1, T3–T5, T7, T9, T12,
T14⟩ aus 00_input/WISSENSSTAND_Strommarkt.md am Primärtext prüfen (Stand ⟨TT.MM.JJJJ⟩): geltende Fassung,
Übergangsregeln, laufende Gesetzgebung und Festlegungsverfahren, Ereignisse nach dem 04.10.2026. Für Befunde des
Vorprojekts die URLs aus 00_input/vorprojekt_bess/BESS_QUELLEN_Auswahl.csv nutzen und prüfen, ob die Aussage noch
gilt. Je Punkt ein Urteil: bestätigt / präzisiert / überholt / widerlegt / nicht prüfbar, mit Beleg.
Ausgabe: 02_research/W0_verifikation/notizen_regulierung.md mit Tabelle „Nr. (B/H/T) | Aussage | Befund |
Norm/Festlegung | Stand | Quelle-ID | Qualität | Beleg“, Abschnitt „Bewegliche Themen: Stand und nächstes
Ereignis“, csv-Block (IDs W0R-⟨nn⟩; alte Vorprojekt-ID als Herkunft). Tool-Budget 25–35 Aufrufe. Rückmeldung
höchstens 15 Zeilen, Überholtes und Widerlegtes zuerst.
```
Entsprechend W0-M (markt-rechercheur: B-01 bis B-11, B-14, B-15, B-17, H-12 bis H-22, H-51, H-52, T2, T3, T6, T8,
T11, Datenquellen Abschnitt 14 auf Abrufbarkeit), W0-N (netz-technik-rechercheur: H-01 bis H-08, H-23, H-24, H-37,
H-41, H-42, T13, Systemzahlen) und W0-E (endkunden-rechercheur: H-43 bis H-47, T10, Umlagen und Netzentgelte des
Folgejahres). Höchstens vier Agenten gleichzeitig; Überschneidungen (z. B. B-14 Kapazitätsmarkt: Recht beim
regulierungs-, Ergebnisse beim markt-rechercheur) im Auftrag ausdrücklich abgrenzen.

## V3 Einzelfaktenfrage oder Nachprüfung

```
⟨Agent⟩, Nachprüfung ⟨Thema⟩ (Stand ⟨TT.MM.JJJJ⟩). Buchstand: ⟨Aussage mit Fundstelle, Quelle-ID⟩. Frage: ⟨Ist ein
Ereignis eingetreten / stimmt die Aussage noch / wurde ein neuer Wert veröffentlicht?⟩. Primärquelle: ⟨URL aus
SOURCES.csv⟩. Ausgabe: 02_research/⟨Ordner⟩/notizen_⟨thema⟩.md mit Ergebnis in 2–4 Sätzen, Belegtabelle, „Folgen
für das Buch“ (welche Stelle stimmt, welche nachzuführen ist) und csv-Block für neue Quellen. Tool-Budget 3–10
Aufrufe. Rückmeldung höchstens 8 Zeilen.
```

## V4 Kapitelentwurf (autor)

```
autor, Kapitel ⟨n⟩ „⟨Titel⟩“ (Entwurf). Lies CLAUDE.md, 06_review/LEITFADEN_KAPITEL.md,
07_build/muster/formatmuster.md, die Vorbilder ⟨freigegebene Probekapitel⟩, den Kapitelplan in 01_agenda/AGENDA.md
(Lernziele, Fragen, Tabellen, Abbildungen, Rechenbeispiele), die Notizen 02_research/K⟨nn⟩_⟨slug⟩/*.md,
02_research/SYNTHESE.md (Abschnitt ⟨…⟩), ANNAHMEN.md, DECISIONS.md (⟨D-…⟩) und die Modellwerte
04_models/⟨modell⟩/ergebnisse/⟨lauf-id⟩/kapitelzahlen.md; Abbildungen aus 05_figures/K⟨nn⟩/.
Entscheidungen, die du beachten musst: ⟨Liste⟩. Referenzfälle: ⟨R…⟩. Umfang: Richtwert ⟨n⟩ Wörter, Obergrenze ⟨n⟩.
Ausgabe: 03_chapters/⟨nn⟩_⟨slug⟩.md sowie 06_review/K⟨nn⟩_loesungen_entwurf.md, K⟨nn⟩_glossar_vorschlag.md,
K⟨nn⟩_autor_luecken.md. Kein git. Rückmeldung höchstens 15 Zeilen (Wörter, Quellen, Modellläufe, Lücken).
```

## V5 Faktencheck (faktenpruefer)

```
faktenpruefer, Faktencheck ⟨v1 | Abschlussfaktencheck v2⟩ Kapitel ⟨n⟩ (03_chapters/⟨nn⟩_⟨slug⟩.md) mit
Lösungsentwurf 06_review/K⟨nn⟩_loesungen_entwurf.md. Prüfe vollständig nach deiner Agentendefinition (Beleg, Recht
und Marktregeln, Einheiten und Abgrenzung, Rechnungen, Aktualität, Konsistenz, Vertraulichkeit, rechtliche Grenzen).
Mindestens ⟨15⟩ Stichproben gegen Primärquellen, darunter alle Normzitate, Festlegungen und Preisangaben. Modellwerte
gegen 04_models/⟨…⟩/ergebnisse/⟨lauf-id⟩/ und Stichproben gegen die Datensnapshots in 04_models/daten/ prüfen.
Ausgabe: 06_review/K⟨nn⟩_faktencheck⟨_v2⟩.md. Den Kapiteltext nicht verändern. Tool-Budget ⟨25–40⟩ Aufrufe.
Rückmeldung höchstens 15 Zeilen.
```

## V6 Korrektur (autor)

```
autor, Korrektur Kapitel ⟨n⟩ nach 06_review/K⟨nn⟩_faktencheck⟨…⟩.md ⟨und _lektorat.md⟩. Bearbeite jeden Befund;
dokumentiere je Befund „umgesetzt“ oder „abgelehnt mit Grund“ in 06_review/K⟨nn⟩_korrekturen.md. Halte die
Obergrenze von ⟨n⟩ Wörtern ein (Zählung nach LEITFADEN_KAPITEL.md § 2); gleiche Ergänzungen durch Kürzungen aus,
nie durch Streichen belegter Kernaussagen. Lösungen und Glossarvorschlag mitführen. Kein git.
```

## V7 Lektorat (lektor)

```
lektor, Lektorat Kapitel ⟨n⟩ nach deiner Agentendefinition. Richtwert ⟨n⟩, Obergrenze ⟨n⟩ Wörter. Sprachliche und
formale Korrekturen direkt im Kapitel, inhaltliche als Befund. Ausgabe: 06_review/K⟨nn⟩_lektorat.md mit Matrix
Lernziele × Inhalt × Übungen und Umfang vorher/nachher. Kein git.
```

## V8 Delta-Prüfung nach Änderungen an freigegebenen Kapiteln

```
faktenpruefer, Delta-Prüfung ⟨Anlass, z. B. Erratum, Neulauf M1, neue Umlagen, Gesamtredaktion⟩ für Kapitel
⟨Liste⟩. Geändert wurden: ⟨Liste der Stellen oder git diff ⟨Commit⟩..⟨Commit⟩ -- 03_chapters/⟩. Prüfe nur die
geänderten Stellen und ihre Folgen (Querverweise, gleiche Zahl an anderer Stelle, Lösungen, Glossar, Annahmen) gegen
Quellen und Modelle. Ausgabe: 06_review/⟨Name⟩_deltapruefung.md (Gesamturteil, Befunde mit Schwere, Stichproben).
Tool-Budget ⟨15–30⟩.
```

## V9 Modellauftrag (modellierer)

```
modellierer, Auftrag ⟨M…-Stufe⟩. Ziel: ⟨was das Modell rechnen soll, für welche Kapitel und Referenzfälle⟩.
Eingaben: ⟨Notizen, Annahmen A-…, Entscheidungen D-…, Datensnapshots in 04_models/daten/⟩. Rechenregeln aus Recht
und Marktregeln: ⟨Norm oder Regelwerk, Quelle-ID⟩. Ausgabe: 04_models/⟨modell⟩/ mit README (Ziffern), params/, src/,
tests/, run.py, ergebnisse/⟨Lauf-ID⟩/ mit kapitelzahlen.md; neue Annahmen in ANNAHMEN_VORSCHLAG.md. pytest grün vor
der Rückmeldung. Kein git. Rückmeldung höchstens 15 Zeilen mit Kernzahlen je Referenzfall und Lauf-ID.
```

## V10 Abbildung (modellierer)

```
modellierer, Abbildung ⟨Kxx⟩-⟨n⟩: ⟨Inhalt, Datenquelle (Snapshot mit Manifest) oder Lauf-ID, Zeitraum, Auflösung,
Zeitzone⟩. Skript, Daten und Bild unter 05_figures/K⟨nn⟩/, Stil nach 07_build/muster/abbildung_muster.py
(Buchfarben, Carlito, deutsche Zahlen, Achsen mit Einheit, kein Titel und keine Quelle im Bild), dazu ⟨name⟩.md mit
Beschriftung (≤ 30 Wörter) und Quellenzeile.
```

## V11 Konsistenzprüfung je Buchteil (lektor)

```
lektor, Konsistenzprüfung Teil ⟨Nr.⟩ (Kapitel ⟨Liste⟩). Prüfe Begriffe gegen GLOSSAR.md, Leitzahlen und Parameter
der Referenzfälle gegen DECISIONS.md und ANNAHMEN.md, Einheiten (MW/MWh, ct/kWh/€/MWh, Stunde/Viertelstunde),
Querverweise (python3 07_build/querverweise.py), Kästen „Stand“ (gleiches Thema, gleiches Prüfdatum, gleiche
Formulierung), Schreibweisen nach LEITFADEN_KAPITEL.md § 4. Nichts im Text ändern. Ausgabe:
06_review/P7_konsistenz_⟨n⟩.md mit Befunden (Nr. | Kapitel, Zeile | Befund | Schwere | Vorschlag mit Wortwirkung).
```

## V12 Anhänge C, F, G (autor)

```
autor, Anhänge C (Abkürzungen), F (Formelsammlung) und G (Modellhandbuch M1–M4). Grundlagen: Kapitel 1–⟨n⟩,
GLOSSAR.md, ANNAHMEN.md, README der Modelle. Keine neuen Zahlen, keine neuen Quellen; nur IDs, die die Kapitel
zitieren. Format nach CLAUDE.md § 5: YAML-Kopf, keine H1, Abschnitte `# … {.unnumbered}`, Pipe-Tabellen mit
`Table:` und Quellenzeile. Formeln wörtlich aus den Kapiteln mit Fundstelle. Ausgabe:
03_chapters/anhang_abkuerzungen.md, anhang_formeln.md, anhang_modelle.md und 06_review/P7_anhaenge_CFG.md
(Auswahlregeln, Zweifelsfälle, Widersprüche, Vorschläge). Kein git.
```

## V13 Prüfliste vor Drucklegung (regulierungs-rechercheur oder autor)

```
Ziel: Der Auftraggeber soll vor dem Druck wissen, welche Aussagen an einem Rechts- oder Marktstand hängen, der sich
bald ändern kann, wann das geschieht und welche Zahlen dann neu zu rechnen sind. Eingaben:
06_review/P7_stand_kaesten.md (alle Kästen „Stand“), PROGRESS.md (offene Punkte), DECISIONS.md, ANNAHMEN.md.
Keine Webabrufe, keine neuen Fakten. Ausgabe: 06_review/P7_pruefliste_drucklegung.md mit Tabelle „Nr. | Thema |
Stand im Buch | Nächstes Ereignis (Datum) | Betroffene Kapitel | Was neu zu prüfen oder zu rechnen ist (A-IDs,
Modelle)“, nach Datum sortiert, und Abschnitt „Widersprüche und Lücken in den Stand-Kästen“. Jahreswerte
(Umlagen, Netzentgelte, Steuersätze, Höchstwerte) gesondert mit Veröffentlichungstermin auflisten.
```

## V14 Analyse einer vertraulichen Unterlage (autor oder Recherche-Agent, ohne Web)

```
Analyse der Unterlage ⟨U1⟩ (00_input/vertraulich/⟨Datei⟩). Vertraulich nach CLAUDE.md § 8: keine Namen, keine
Hinweise auf Vertragspartner, Gutachter, Netzbetreiber, Standort, Projektnummer oder Dateinamen in die Ausgabe
übernehmen; nicht versuchen, Beteiligte zu identifizieren; keine Webabrufe. Ziel: Struktur, Zahlen mit Fundstelle
(Tab., Kap.), Methodik, Annahmen, Prüfpunkte (Plausibilität, Einheiten, Stichtage, Marktregeln, Lücken) und Eignung
als Fallbeispiel. Ausgabe: 02_research/00_unterlagen/⟨U1⟩_analyse.md.
```

## V15 Glossar mit englischen Entsprechungen (Orchestrator oder autor)

```
Für jeden Eintrag in GLOSSAR.md die gebräuchliche englische Entsprechung (Fachsprache des europäischen
Strommarkts, der Netzkodizes und der Börsen; bei deutschen Rechtsinstituten ohne Entsprechung eine erklärende
Übersetzung in Klammern). Ausgabe: 07_build/glossar_englisch.csv mit Spalten "begriff","englisch"; Schlüssel exakt
wie der Begriff im Glossar.
```

## V16 Datensnapshot für die Modelle (modellierer)

```
modellierer, Datensnapshot ⟨Bezeichnung⟩. Reihen: ⟨z. B. Day-Ahead-Preise DE-LU, Last, Einspeisung Wind und Solar,
Marktwerte, reBAP⟩; Zeitraum ⟨…⟩; Auflösung ⟨Stunde/Viertelstunde⟩. Quellen und Endpunkte aus
02_research/⟨…⟩/notizen_markt.md (Abschnitt „Datenquellen für die Modelle“). Nur frei zugängliche Endpunkte, keine
API-Schlüssel, keine Registrierung. Speicherung in UTC als CSV oder Parquet unter 04_models/daten/⟨JJJJMMTT⟩_⟨name⟩/
mit MANIFEST.md (Quelle, Endpunkt, Abrufdatum, SHA-256, Zeitraum, Auflösung, Zeitzone, Lizenz, Lücken und
Umstellungstage). Plausibilitätsprüfung: Anzahl Zeitschritte je Tag (92, 96 oder 100 Viertelstunden an
Umstellungstagen), fehlende Werte, Ausreißer, Abgleich von Jahresmitteln mit einer zweiten Quelle. Kein git.
```

## Vorlagen für Prüfdateien

### Faktencheck (`06_review/<Kxx>_faktencheck.md`)
```
# Faktencheck <Kxx> · Version <n> · TT.MM.JJJJ
## Gesamturteil (freigabefähig ja/nein; kritisch / hoch / mittel / niedrig)
## Befunde
| Nr. | Fundstelle | Aussage im Text | Befund | Schwere | Beleg/Prüfung | Korrekturvorschlag |
## Nicht prüfbare Aussagen (Grund)
## Stichproben gegen Primärquellen
```

### Lektorat (`06_review/<Kxx>_lektorat.md`)
```
# Lektorat <Kxx> · TT.MM.JJJJ
## Gesamturteil
## Matrix Lernziele × Inhalt × Übungen
## Befunde (Nr. | Fundstelle | Befund | Art | Schwere | Vorschlag)
## Direkt vorgenommene Korrekturen
## Umfang (Wörter vorher/nachher, Grenze)
```

### Korrekturen (`06_review/<Kxx>_korrekturen.md`)
```
# Korrekturen <Kxx> · TT.MM.JJJJ
| Befund (Datei, Nr.) | Umsetzung | Stelle | Wortwirkung |
## Abgelehnt (Befund | Grund)
## Umfang (Wörter, Grenze)
```

### Lösungsentwurf (`06_review/<Kxx>_loesungen_entwurf.md`)
```
## Kapitel <n>

### Übung <n>.1
Rechenweg, Ergebnis mit Einheit, Quellen- und A-IDs wie im Kapitel.
```

### Glossarvorschlag (`06_review/<Kxx>_glossar_vorschlag.md`)
```
| Begriff | Erklärung | Kap. |
|---|---|---|
| Ausgleichsenergie | … [Quelle-ID] | <n> |

**Ergänzungen bestehender Einträge (Vorschlag):**

| Begriff | Erklärung | Kap. |
|---|---|---|

**Englische Entsprechungen:**

| Begriff | englisch |
|---|---|
| Ausgleichsenergie | imbalance energy |
```

### Lücken des Autors (`06_review/<Kxx>_autor_luecken.md`)
```
| Nr. | Fundstelle | Platzhalter | Was fehlt | Vorschlag (Agent, Quelle, Modell) |
```
