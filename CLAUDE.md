# CLAUDE.md – Projektregeln „Der Strommarkt in Deutschland“

Diese Regeln gelten dauerhaft für den Orchestrator und alle Subagents. Sie fassen die Abschnitte 6, 7 und 9–11
des Auftrags (`00_input/AUFTRAG_Lehrbuch_Strommarkt.md`) zusammen und übernehmen die Arbeitsweise, das Layout und
die Erfahrungen des Vorprojekts (Lehrbuch „Ökonomie von Batteriespeichern in Deutschland“).

## 1 Projekt in Kürze

- **Buch:** Deutschsprachiges Lehrbuch (Niveau berufsbegleitender Master / Professional) zum Strommarkt in
  Deutschland, vom Strom als physikalischem Gut über Großhandel, Systemsicherheit, Kapazität, Förderung und Netz bis
  zum Endkundenpreis, mit Rechtsrahmen in Deutschland und der EU. Fokus Deutschland, europäische Einordnung.
- **Leser:** wirtschaftlich versiert (Investor, Geschäftsführung, Finanzierung, Beratung), kennt einzelne Segmente
  aus Speicherinvestitionen, ist aber weder Energietechniker noch Energierechtler.
- **Konsequenz:** Quellenqualität, Datierung (Daten- und Rechtsstand) und die Trennung von Fakt, Schätzung und
  Annahme haben Vorrang vor Umfang und Eleganz.
- **Eingaben (`00_input/`, nie verändern):** Auftrag, Wissensstand (Ausgangshypothese, nicht Wahrheit), Material des
  Vorprojekts unter `00_input/vorprojekt_bess/` (Abschnitt 9), optional vertrauliche Unterlagen unter
  `00_input/vertraulich/` (Abschnitt 8).
- **Referenzfälle:** R1 Haushalt; R2 Industriekunde mit strukturierter Beschaffung; R3 Windpark an Land mit
  EEG-Zuschlag und Direktvermarktung; R4 Solarpark mit PPA; R5 Gaskraftwerk (Spark Spread, Absicherung,
  Regelreserve, Kapazitätsmarkt); R6 Batteriespeicher (Anschluss an das Vorprojekt). Die Parameter legt die
  Agenda-Freigabe fest (D-Entscheidung, A-IDs).
- **Vergleichsmärkte:** nach Phase 1 festlegen (Vorschlag: Großbritannien, Frankreich, Nordeuropa).
- **Verbindliche Gliederung:** `01_agenda/AGENDA.md` (nach Freigabe); Teile und Kapitel zusätzlich in
  `07_build/buch_config.yaml`. Rechercheaufträge: `02_research/RESEARCH_PLAN.md`.
- **Phasen:** 0 Setup → 1 Agenda (STOP) → 2 Agenten/Rechercheplan (STOP) → 3 Recherche → 4 Modelle →
  5 Probekapitel (STOP) → 6 alle Kapitel → 7 Gesamtredaktion/Build. Keine spätere Phase ohne Freigabe. Status in
  `PROGRESS.md`, Entscheidungen in `DECISIONS.md`.

## 2 Quellen- und Qualitätsregeln

1. **Rangfolge:** Gesetze, Verordnungen und EU-Rechtsakte in amtlicher Fassung, Gesetzesmaterialien, Festlegungen
   und Beschlüsse der BNetzA, Entscheidungen von ACER, EU-Kommission und Gerichten → Daten und Veröffentlichungen
   der Netzbetreiber und Börsen (netztransparenz.de, regelleistung.net, SMARD, energy-charts, EEX, EPEX SPOT,
   ENTSO-E-Transparenzplattform), amtliche Statistik (Destatis, AGEB, Marktstammdatenregister), Monitoringberichte
   von BNetzA und Bundeskartellamt → anerkannte Studien (Fraunhofer, FfE, Agora Energiewende, EWI, DIW,
   Öko-Institut, IEA, ACER-Marktberichte, Ember) → Kanzlei- und Fachmedien → Anbieter- und Marketingseiten (nur
   Einordnung, nie einzige Quelle für eine Zahl).
2. **Zugang:** Kostenpflichtige Datenbanken, Börsendaten hinter Bezahlschranken und Normenkommentare sind meist nicht
   zugänglich. Dann frei veröffentlichte Primärdaten, Normtext und Gesetzesbegründung nutzen und die Lücke benennen.
   Nie Inhalte aus nicht gelesenen Quellen wiedergeben.
3. **Datierung:** Jede Zahl mit Einheit, Stand-Datum und Quelle; jede Rechtsaussage mit Norm (Paragraf, Absatz,
   Satz, Nummer) und Fassung bzw. Aktenzeichen und Datum. Regulatorisch bewegliche Themen ausdrücklich kennzeichnen
   (Kasten „Stand“) und vor Verwendung neu prüfen; Liste in `00_input/WISSENSSTAND_Strommarkt.md`, Abschnitt 11
   (u. a. EEG 2027 und Differenzverträge, Ausschreibungen, Kapazitätsmarkt nach StromVKG, AgNes,
   Netzanschlusspaket, Regelreserveprodukte, § 13k, § 14a und § 14c EnWG, MiSpeL, Preisgrenzen, Gebotszone,
   Umlagen und Stromsteuer, EU-ETS und ETS 2, EU-Strommarktreform, Ablösung von StromNZV, StromNEV und ARegV).
4. **Kennzeichnung:** Fakt (mit Quelle) / Schätzung (mit Herleitung) / Annahme (mit Begründung). Annahmen zentral
   in `ANNAHMEN.md` (ID `A-xxx`, Modellannahmen `A-M1-xx` usw., Kapitelannahmen `A-Kxx-xx`), im Text mit ID.
5. **Ebenen und Einheiten nie vermischen:** Leistung (MW, GW) und Energie (MWh, TWh); elektrisch und thermisch
   (MW_el, MWh_th); Stunden- und Viertelstundenwerte (eine Viertelstunde mit 100 MW sind 25 MWh); Base, Peak und
   Profil; Handelstag und Liefertag; MEZ und MESZ; Gebotszone (DE-LU); Großhandels- und Endkundenpreis; netto und
   brutto (Umsatzsteuer); ct/kWh und €/MWh (1 ct/kWh = 10 €/MWh); nominal und real (mit Basisjahr); installierte
   Leistung, gesicherte Leistung und Erzeugung; Brutto- und Nettoerzeugung; €/MW je Zeitraum bei Leistungsprodukten
   („€/MW je 4-h-Block“, „€/MW/a“).
6. **Preise und Erlöse nie ohne Kontext:** Markt, Gebotszone, Lieferperiode, Auflösung, Zeitraum, Mittelwert oder
   mengengewichtet, brutto oder netto, real oder nominal, Quelle und Methode.
7. **Keine erfundenen Zahlen, Quellen, Normen, Aktenzeichen, Entscheidungen oder Zitate.** Wenn nichts Belastbares zu
   finden ist: Lücke benennen (`[LÜCKE: …]`).
8. **Widersprüche nicht glätten:** beide Werte mit Quelle nennen und den Grund erklären (Stichtag, Definition,
   Auflösung, Abgrenzung, Methodik, Region).
9. **Zitate:** Inhalte in eigenen Worten; wörtliche Zitate nur kurz und selten.
10. **Quellenregister:** `sources/SOURCES.csv` mit den Spalten
    `id,titel,herausgeber,url,abrufdatum,stand_der_quelle,typ,qualität,kapitel` (alle Felder in doppelten
    Anführungszeichen; Qualität A = Primärquelle, B = anerkannte Sekundärquelle, C = Fachmedien/Anbieter). Agenten
    liefern Quellen als csv-Block in ihrer Notiz (IDs `<Kapitel-ID><Kürzel>-<nn>`, Kürzel M Markt, R Regulierung,
    N Netz und Technik, E Endkunden); der Orchestrator führt mit `python3 sources/merge_sources.py` zusammen. Im
    Text: Quellenkürzel in eckigen Klammern, z. B. [K06M-03].
11. **Rechtliche Grenzen:** Keine Rechts-, Steuer- oder Anlageberatung. Stellen, an denen Rechtsanwalt für
    Energierecht, Steuerberater, Wirtschaftsprüfer oder Fachanwalt für Bank- und Kapitalmarktrecht nötig sind, als
    Kasten „Hier Fachleute einbinden“ markieren. „Fachanwalt für …“ nur mit einer Bezeichnung nach der
    Fachanwaltsordnung, sonst „Rechtsanwalt für …“ (es gibt keinen Fachanwalt für Energierecht).
12. **Unternehmen und Ereignisse:** nur mit öffentlich zugänglichen, datierten Quellen; Unternehmen nur so benennen,
    wie die Quelle es tut; keine Spekulation über Motive oder Marktmissbrauch; laufende Verfahren als laufend
    kennzeichnen.

## 3 Didaktisches Kapiteldesign (Backward Design + Bloom)

Erst Lernziele, dann Nachweis (Übungen), dann Inhalt. Jedes Kapitel folgt dieser Vorlage:

1. Lernziele (2–4, messbare Bloom-Verben, aufsteigend bis „bewerten“/„entwerfen“; nie „verstehen“ oder „kennen“)
2. Warum das für Investoren und Marktteilnehmer zählt (3–5 Sätze) mit Marktkompass (Tabelle der berührten Ebenen:
   Physik und Technik, Großhandel, System und Netz, Förderung, Regulierung, Endkundenpreis)
3. Kerninhalt in Fließtext mit Formeln, Tabellen, Abbildungen (aus realen Daten, wo möglich)
4. Rechenbeispiel am Referenzfall, Schritt für Schritt, reproduzierbar aus `04_models/` (Lauf-ID)
5. Praxis-Check: Checkliste oder Prüffragen für Daten, Verträge, Prognosen, Angebote, Due Diligence
6. Typische Fehler und Fallstricke
7. Zusammenfassung (5–8 Kernaussagen)
8. Übungen: 3–6 Aufgaben (Rechnen, Bewerten, Entscheiden), Lösungen in `06_review/<Kxx>_loesungen_entwurf.md`;
   den Anhang erzeugt der Orchestrator (`python3 07_build/anhang_loesungen.py <nn> …`)
9. Quellen des Kapitels und „Stand“-Vermerk

Schreib-Prüf-Schleife je Kapitel: `autor` → `faktenpruefer` (Befundliste mit Schweregrad, prüft nur gegen Text und
Quellen) → `autor` korrigiert → `lektor` → Abschlussfaktencheck → Orchestrator gibt frei. Befundlisten nach
`06_review/<Kxx>_*.md`. Einzelheiten und Erfahrungen: `06_review/LEITFADEN_KAPITEL.md`.

## 4 Stil

Deutsch, sachlich, klar, für wirtschaftlich versierte Leser ohne energietechnische oder juristische Ausbildung.
Fachbegriffe beim ersten Auftreten erklären und in `GLOSSAR.md` übernehmen; englische Entsprechungen, wo der Markt
englische Begriffe nutzt (Day-Ahead, Intraday, Gate Closure, Clearing), sammelt der Orchestrator in
`07_build/glossar_englisch.csv` (das Gesamtbuch setzt daraus eine Spalte im Glossar). Physik nur so weit, wie sie für Märkte
und Netz nötig ist. Überwiegend Fließtext; Tabellen für Vergleiche und Zahlen; Aufzählungen nur für Checklisten.
Jede Zahl mit Einheit, Stand und Quelle. Formeln mit Variablenerklärung. Keine Werbesprache, keine Füllsätze.
Einordnungen, die kein Befund sind, als „Einordnung“ oder „Einschätzung“ kennzeichnen.

## 5 Formatierung (verbindlich – „immer professionell formatieren“)

Jedes Lieferobjekt (Agenda, Kapitel, Buch, Berichte) wird aus Markdown mit `07_build/build.py` gesetzt und als
**PDF** ausgeliefert (Pandoc → Typst, ohne Word; `--engine docx` nur als Rückfallebene); das Gesamtbuch mit
`07_build/buch.py`. Vor Übergabe visuell prüfen (`07_build/preview.py`). Ein vollständiges Beispiel aller
Elemente steht in `07_build/muster/formatmuster.md`.

**Markdown-Konventionen**

- YAML-Kopf je Datei: `title`, `subtitle`, `date`, `kopfzeile-rechts`; Kapiteldateien zusätzlich
  `kapitel-start: <n>`, `nummerierung: kapitelweise` (Muster: `title: "Kapitel 6 · Day-Ahead-Markt und
  Marktkopplung"`, `kopfzeile-rechts: "Kapitel 6 · Stand TT.MM.JJJJ"`). Überschriften nicht von Hand
  nummerieren – das macht der Filter (`{.unnumbered}` für Ausnahmen).
- Kästen in GitHub-Alert-Syntax, Titel fett in der ersten Zeile:
  `> [!NOTE]` + `> **Lernziele:** …` · `> [!IMPORTANT]` + `> **Hier Fachleute einbinden:** …` ·
  `> [!TIP]` + `> **Praxis-Check:** …` · `> [!WARNING]` + `> **Typische Fehler:** …` ·
  `> [!BEISPIEL]` + `> **Rechenbeispiel R3:** …` · `> [!STAND]` + `> **Stand:** …` ·
  `> [!DEFINITION]`. Der Titel steuert Farbe und Typ.
- Tabellen als Pipe-Tabellen mit Beschriftung darunter: `Table: Kurzer Titel`; darunter eine
  Zeile `Quelle: … (Stand TT.MM.JJJJ).` (wird als Quellenzeile unter der Tabelle gesetzt).
  Nummern setzt der Satz („Tabelle 3.2:“).
- Abbildungen: `![Beschriftung](05_figures/<Kxx>/<datei>.png)`, darunter eine Zeile `Quelle: … (Stand TT.MM.JJJJ).`;
  Skript und Daten in `05_figures/<Kxx>/`. Im Bild selbst kein Titel und keine Quellenzeile (Beschriftung und
  Quelle setzt der Satz); Achsen mit Einheit, deutsche Zahlenformate, Buchfarben (Dunkelblau #1B365D, Blau #2A7AB0,
  Grün #2E7D6B, Orange #C55A11, Ocker #B7791F, Grau #5F6B7A), Schrift Carlito (`07_build/fonts/`); Vorlage
  `07_build/muster/abbildung_muster.py`. Zeitreihen mit Zeitzone und Auflösung in der Beschriftung.
- Formeln in LaTeX-Syntax (`$…$`, `$$…$$`), Variablen direkt danach erklären; Dezimalkomma in Formeln als `{,}`
  (z. B. `$\eta = 0{,}55$`). Indizes mit Text in `\text{…}` (z. B. `$p_{\text{CO}_2}$`).
- Seitenumbruch nur mit `<!-- neue-seite -->`. Kein sonstiges HTML.
- Dollarzeichen im Text immer maskieren: `US-\$` bzw. `\$`. Ein unmaskiertes `$` startet im Satz einen
  Formelmodus.
- Zahlen deutsch: Dezimalkomma, Tausenderpunkt (1.234,5); Bereiche mit Halbgeviertstrich (4–7 ct/kWh);
  Datumsformat TT.MM.JJJJ; Uhrzeiten „12 Uhr“ bzw. „12:00 Uhr“ mit Zeitzone, wo es darauf ankommt; Einheiten: €/MWh,
  ct/kWh, €/MW/a, €/kW/a, €/MW je 4-h-Block, €/t CO₂, MW, MWh, GW, TWh, h, Hz, kV. Anführungszeichen „…“.
- Normen: „§ 51 Abs. 1 EEG“, „Art. 16 Abs. 8 Verordnung (EU) 2019/943“; „S.“ steht nur für Seite. Festlegungen:
  „BNetzA, Beschluss vom TT.MM.JJJJ – BK6-…“. Verweise auf Modelldokumentation mit „Ziffer“, nicht „Abschnitt“
  (Verwechslung mit Buchabschnitten).

**Layout (zentral in `07_build/typst/lehrbuch.typst`, Filter `07_build/filter/lehrbuch.lua`, unverändert aus
dem Vorprojekt)**

A4, Fließtext Caladea (metrisch gleich Cambria) 10,5 pt Blocksatz mit Silbentrennung, Überschriften/Tabellen/Kästen
Carlito (gleich Calibri), Primärfarbe Dunkelblau #1B365D, Deckblatt, Inhaltsverzeichnis, Kapitelkopf je Kapitel,
Kopfzeile mit lebendem Kolumnentitel, Fußzeile mit „Seite x von y“, Tabellen mit dunkelblauer Kopfzeile und
Zebrastreifen, Quellenzeilen, farbige Kästen je Typ. Layoutänderungen nur dort, nie per Direktformatierung in
einzelnen Dokumenten. Buchspezifische Angaben (Titel, Teile, Deckblatt, Stand, vertrauliche Unterlagen) nur in
`07_build/buch_config.yaml`.

## 6 Dateistruktur

```
/00_input            Eingaben (nicht verändern); vorprojekt_bess/, vertraulich/
/01_agenda           AGENDA_VORSCHLAG.md (+ .pdf), freigegebene AGENDA.md
/02_research         RESEARCH_PLAN.md, <Kapitel-ID>/notizen_*.md, SYNTHESE.md, W0_verifikation/
/03_chapters         <nn>_<slug>.md (ein Kapitel je Datei), vorwort.md, anhang_*.md
/04_models           m1_meritorder/, m2_erneuerbare/, m3_beschaffung/, m4_netz_endkunde/, daten/
/05_figures          Abbildungen je Kapitel (Skript, Daten, Bild, Beschriftung)
/06_review           Befundlisten je Kapitel, LEITFADEN_KAPITEL.md, VORLAGEN.md, Prüflisten der Phase 7
/07_build            build.py, buch.py, Filter, Vorlage, Schriften, buch_config.yaml; output/ (Builds)
/sources             SOURCES.csv, SOURCES_basis.csv, merge_sources.py, kapitel_ergaenzen.py, kapitel_abgleichen.py
CLAUDE.md  PROGRESS.md  DECISIONS.md  ANNAHMEN.md  GLOSSAR.md
```

## 7 Arbeitsweise mit Agenten

- Delegationsauftrag enthält immer: Ziel, Abgrenzung, Quellen-/Toolhinweise, Ausgabeformat
  (Datei, Struktur, Pflichtfelder je Aussage: Aussage, Zahl+Einheit, Stand bzw. Fassung, Quelle+URL,
  Qualität A/B/C, Fakt/Schätzung/Annahme, Volltext/Suchauszug), Aufwand (Tool-Budget, Abbruchkriterium),
  Rückmeldung (max. 15 Zeilen + offene Punkte; Details nur in Dateien). Vorlagen: `06_review/VORLAGEN.md`.
- Einzelne Faktenfrage: 1 Agent, 3–10 Tool-Aufrufe. Kapitelrecherche: 2–4 Agenten parallel, je 10–25 Aufrufe.
  Nie mehr als 5 Agenten gleichzeitig. Stoppen, wenn nichts Neues kommt.
- Subagents schreiben nur ihre zugewiesenen Dateien und committen nicht. Nur der Orchestrator bearbeitet
  `ANNAHMEN.md`, `DECISIONS.md`, `GLOSSAR.md`, `sources/SOURCES.csv` (über csv-Blöcke und `merge_sources.py`) und
  `03_chapters/anhang_loesungen.md` (erzeugt).
- Webabruf: Primärquellen im Volltext prüfen, u. a. gesetze-im-internet.de, recht.bund.de, eur-lex.europa.eu,
  dip.bundestag.de, bundesnetzagentur.de (Beschlussdatenbank), acer.europa.eu, netztransparenz.de,
  regelleistung.net, smard.de, energy-charts.info (inkl. API), eex.com, transparency.entsoe.eu (Webansicht),
  marktstammdatenregister.de, destatis.de, ag-energiebilanzen.de, umweltbundesamt.de, dehst.de. „Suchauszug“ nur,
  wenn eine Seite technisch nicht abrufbar ist (z. B. blockiert epexspot.com automatisierte Abrufe); solche Belege
  kommen auf die Verifikationsliste. Keine Sperren umgehen, keine Logins oder Registrierungen (auch keine
  API-Schlüssel). Lehnt das Berechtigungssystem eine Aktion ab, nicht auf anderem Weg versuchen, sondern melden.
- Marktdaten für die Modelle: als datierter Snapshot mit `MANIFEST.md` (Quelle, Endpunkt, Abrufdatum, Prüfsumme,
  Zeitraum, Zeitzone, Auflösung, Lizenz) unter `04_models/daten/`; was nicht primär zu beschaffen ist, nur als
  gekennzeichnete Annahme.
- Der Orchestrator committet nach jedem abgeschlossenen Schritt mit einer klaren Nachricht und hält `PROGRESS.md`
  aktuell.

## 8 Vertraulichkeit eigener Unterlagen (U1 …)

Unterlagen unter `00_input/vertraulich/` (z. B. Lieferverträge, PPAs, Gutachten, Angebote) stammen vom
Auftraggeber und sind anonymisiert. Regeln:

- Im Buch nur als „Unterlage U1 (anonymisiert)“ mit Fundstelle (z. B. „U1, Tab. 3“) bezeichnen. Keine Namen oder
  Hinweise auf Vertragspartner, Gutachter, Netzbetreiber, Standort, Projektnummer oder Dateinamen übernehmen; nicht
  versuchen, Beteiligte zu identifizieren.
- Keine Abbildungen oder längeren Textpassagen reproduzieren. Zahlen nur mit Fundstelle und nur, soweit der
  Auftraggeber die Verwendung freigegeben hat (D-Entscheidung).
- Analyse und Prüfpunkte: `02_research/00_unterlagen/<U-ID>_analyse.md`.
- Im Quellenverzeichnis nur mit Bezeichnung (Eintrag `vertraulich` in `07_build/buch_config.yaml`).

## 9 Material aus dem Vorprojekt

`00_input/vorprojekt_bess/` enthält Kapitel 2, 3, 11, 12 und 15, das Glossar und 150 Quellen des Lehrbuchs
„Ökonomie von Batteriespeichern in Deutschland“ (Stand 04.10.2026). Regeln:

- Hintergrund und Startwissen, keine fertige Quelle: Jede Zahl und Rechtsaussage vor Übernahme am Primärbeleg prüfen
  (Welle 0); die URLs stehen in `BESS_QUELLEN_Auswahl.csv`.
- Texte nicht abschreiben, sondern aus der breiteren Perspektive dieses Buchs neu schreiben. Rechenbeispiele und
  Modellwerte des Vorprojekts gelten nur für dessen Speicherfälle.
- Übernommene Quellen erhalten im neuen Register eigene IDs; die alte ID wird in der Notiz als Herkunft genannt.
- Verweise auf das vertrauliche „Erlösgutachten G1 (anonymisiert)“ des Vorprojekts nicht übernehmen.
