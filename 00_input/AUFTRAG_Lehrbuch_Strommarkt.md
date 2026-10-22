# Auftrag: Lehrbuch „Der Strommarkt in Deutschland – vom Strom selbst bis zum Netz“

<kontext>
Ich (Auftraggeber) will den gesamten Strommarkt verstehen: was Strom physikalisch ist und wie das System im
Gleichgewicht bleibt, welche Märkte es gibt (Termin-, Day-Ahead-, Intraday-, Regelreserve- und Kapazitätsmärkte,
Märkte für Herkunftsnachweise), wie Preise entstehen, wie erneuerbare Energien gefördert und vermarktet werden
(EEG, Ausschreibungen, Marktprämie, Direktvermarktung, PPAs), wie das Netz aufgebaut, betrieben, angeschlossen,
ausgebaut und bezahlt wird, wie sich der Endkundenpreis zusammensetzt und welche Gesetze, Verordnungen und
Behörden das alles regeln, in Deutschland und in der EU. Ich bin wirtschaftlich versiert und kenne einzelne
Segmente aus Investitionen in Batteriespeicher, bin aber weder Energietechniker noch Energierechtler.

Zwei Grundlagen liegen vor: ein Wissensstand mit Ausgangshypothesen (`00_input/WISSENSSTAND_Strommarkt.md`) und
Material aus dem Vorprojekt „Ökonomie von Batteriespeichern in Deutschland“ (`00_input/vorprojekt_bess/`), das
mehrere Themen bereits an Primärquellen geprüft hat (Stand Oktober 2026). Beides ist Ausgangshypothese, nicht
Wahrheit: Du prüfst, aktualisierst und vertiefst es.

Warum das wichtig ist: Das Buch ist Grundlage für Investitions- und Geschäftsentscheidungen im Strommarkt. Falsche
oder veraltete Zahlen, verwechselte Einheiten (MW und MWh, Stunde und Viertelstunde), unklare Annahmen oder
übersehene Rechtsänderungen führen zu Fehlentscheidungen. Deshalb haben Quellenqualität, Datierung (Daten- und
Rechtsstand) und die Trennung von Fakt, Schätzung und Annahme Vorrang vor Umfang und Eleganz.
</kontext>

<eingaben>
- `00_input/WISSENSSTAND_Strommarkt.md` – geprüfte Befunde aus dem Vorprojekt (B-xx, mit Quellen), Hypothesen
  (H-xx), bewegliche Themen, vorläufige Gliederung, Datenquellen, offene Fragen.
- `00_input/vorprojekt_bess/` – Kapitel 2, 3, 11, 12 und 15 des Vorprojekts, sein Glossar und 150 geprüfte
  Quellen (Regeln in der dortigen README).
- `00_input/vertraulich/` – optional: vertrauliche Unterlagen des Auftraggebers (Regeln in Abschnitt 11).
- `07_build/` – Satzsystem aus dem Vorprojekt. Das Layout ist verbindlich und wird nicht neu gebaut;
  buchspezifische Angaben stehen in `07_build/buch_config.yaml`.
- `.claude/agents/`, `CLAUDE.md`, `06_review/LEITFADEN_KAPITEL.md`, `06_review/VORLAGEN.md` – vorbereitete
  Agentendefinitionen, Projektregeln, Leitfaden und Prüfvorlagen. Du prüfst sie in Phase 0 und passt sie an.
Lies die Dateien vollständig (die Vorprojekt-Kapitel mindestens querlesen), bevor du irgendetwas planst.
</eingaben>

## 1. Ziel und Erfolgskriterien

Erstelle ein deutschsprachiges Lehrbuch (Niveau berufsbegleitender Master / Professional), das den Strommarkt in
Deutschland vollständig erklärt, von der Physik des Stroms über Handel, Systemsicherheit, Kapazität, Förderung und
Netz bis zum Endkundenpreis, mit Fokus Deutschland und Einordnung im europäischen Binnenmarkt.

Das Buch ist erfolgreich, wenn ich nach der Lektüre:
1. das Stromsystem physikalisch und organisatorisch erklären kann: Leistung und Energie, Frequenz und
   Gleichgewicht, Netzebenen, Rollen (Erzeuger, Lieferanten, Händler, Bilanzkreisverantwortliche, Übertragungs-
   und Verteilnetzbetreiber, Messstellenbetreiber, Börsen, Regulierer);
2. jeden Teilmarkt mit Produkten, Fristen, Preisregeln und Teilnehmern beschreiben und Preise daraus erklären kann:
   Terminmarkt (Futures, Forwards, Optionen), Day-Ahead, Intraday, Ausgleichsenergie, Regelreserve,
   Kapazitätsmechanismen, Herkunftsnachweise, PPAs;
3. Förderung und Vermarktung erneuerbarer Energien rechnen kann: Ausschreibungen, anzulegender Wert, Marktprämie,
   Marktwerte, Direktvermarktung, Regeln bei negativen Preisen, Differenzverträge;
4. Netzanschluss, Netzentgelte, Netzausbau, Engpassmanagement und ihre Kosten verstehe und den Endkundenpreis in
   seine Bestandteile zerlegen kann;
5. Rechtsgrundlagen und Zuständigkeiten (EnWG, EEG, KWKG, EnFG, StromStG, MsbG, Kapazitätsmarktgesetz,
   EU-Verordnungen und Netzkodizes, REMIT, Finanzmarktregeln) zuordnen und Änderungen in ihrer Wirkung
   einschätzen kann;
6. Geschäftsmodelle und Investitionen im Strommarkt (Erzeugung, Speicher, Handel, Vertrieb, Netz) plausibilisieren
   und ihre Risiken benennen kann, und weiß, wann ich Fachleute brauche.

## 2. Arbeitsweise: Phasen mit Freigaben

Arbeite strikt in Phasen. An jedem **STOP** hältst du an, legst das Ergebnis vor und wartest auf meine Freigabe
oder Änderungen. Beginne keine spätere Phase ohne Freigabe. Halte den Status in `PROGRESS.md` und jede
Entscheidung mit Datum und Begründung in `DECISIONS.md` fest.

### Phase 0 – Setup (ohne Webrecherche)
- Lies die Eingaben.
- Prüfe die Projektstruktur (Abschnitt 8) und ergänze fehlende Ordner.
- Prüfe das Satzsystem: `python3 07_build/build.py 07_build/muster/formatmuster.md` muss ein PDF erzeugen;
  sonst `bash 07_build/einrichten.sh` ausführen und erneut versuchen. Sichte das PDF mit `07_build/preview.py`.
- Prüfe `CLAUDE.md` (dauerhafte Projektregeln) und passe sie an; Custom-Subagents laden `CLAUDE.md`.
- Ergänze die Vorlagen `PROGRESS.md`, `DECISIONS.md`, `ANNAHMEN.md`, `GLOSSAR.md` und `sources/SOURCES.csv`.

### Phase 1 – Agenda-Vorschlag → **STOP**
Liefere `01_agenda/AGENDA_VORSCHLAG.md` (gesetzt als PDF) mit:
1. Buchziel und Leserprofil in je drei Sätzen.
2. 6–10 übergreifende Lernziele nach Bloom (messbare Verben: berechnen, erklären anhand von Daten, vergleichen,
   bewerten, entwerfen; keine Verben wie „verstehen“ oder „kennen“).
3. Zwei bis drei alternative Gliederungslogiken (z. B. „von der Physik zum Preis“, „entlang der Zeitachse vom
   Terminmarkt bis zur Echtzeit“, „entlang der Wertschöpfungskette Erzeugung – Handel – Netz – Vertrieb“) mit Vor-
   und Nachteilen und deine begründete Empfehlung.
4. Die empfohlene Gliederung: Teile, Kapitel, Unterkapitel; je Kapitel 2–4 Lernziele, zentrale Fragen, geplante
   Tabellen, Abbildungen, Rechenbeispiele und Modelle. Ausgangspunkt ist die vorläufige Gliederung im Wissensstand
   (Abschnitt 13); verbessere sie, wo nötig.
5. Abgleich mit der Pflicht-Themenliste (Abschnitt 3): Tabelle „Thema → Kapitel“, ohne Lücken.
6. Durchgängige Referenzfälle (Abschnitt 4.1) mit vorgeschlagenen Parametern, begründet, und wo sie vorkommen.
7. Umfangsschätzung (Seiten und Wörter je Kapitel) und Rechercheplan (welcher Agent, welche Quellentypen), mit
   Kennzeichnung, wo das Vorprojekt schon Vorarbeit geleistet hat.
8. Höchstens sieben Rückfragen an mich, priorisiert.
Dann **STOP**.

### Phase 2 – Agenten-Setup und Rechercheplan → **STOP** (kurz)
Nach Freigabe der Agenda: Übertrage sie nach `01_agenda/AGENDA.md` und die Teile in `07_build/buch_config.yaml`.
Prüfe und schärfe die Subagents (Abschnitt 5), erstelle `02_research/RESEARCH_PLAN.md` (Aufträge je Agent nach
Abschnitt 5.2), beginnend mit Welle 0: Nachprüfung der Befunde des Vorprojekts und der beweglichen Themen am
Primärtext, Prüfung der Hypothesen. Zeig mir die Liste der Agenten und Aufträge. **STOP**.

### Phase 3 – Recherche in Wellen
Delegiere an die Recherche-Agenten. Jeder schreibt nach `02_research/<Kapitel-ID>/` eine Notizdatei mit Belegen
und einem csv-Block für das Quellenregister. Führe die Ergebnisse zusammen (`sources/merge_sources.py`), markiere
Widersprüche und Lücken in `02_research/SYNTHESE.md` und übernimm Annahmen nach `ANNAHMEN.md`.

### Phase 4 – Modelle
Der Modellierer baut die Rechenmodelle (Abschnitt 4.2) unter `04_models/`, getestet und dokumentiert, mit
Marktdaten als datiertem Snapshot. Jede Zahl, die ein Modell ins Buch liefert, ist reproduzierbar (Skript,
Parameterdatei, Lauf-ID).

### Phase 5 – Probekapitel → **STOP**
Schreibe zuerst zwei Probekapitel (ein Grundlagen- oder Regelwerkskapitel und ein Rechen- oder Marktkapitel,
z. B. „Day-Ahead-Markt und Marktkopplung“ und „EEG: Marktprämie und Direktvermarktung“), jeweils nach Autor →
Faktenprüfer → Autor → Lektor → Abschlussfaktencheck. Lege sie mir gesetzt als PDF zur Kalibrierung von Tiefe,
Stil, Umfang und Didaktik vor. **STOP**.

### Phase 6 – Alle Kapitel
Kapitelweise Schreib-Prüf-Schleife (Abschnitt 5.3, `06_review/LEITFADEN_KAPITEL.md`). Aktualisiere `PROGRESS.md`
nach jedem Kapitel. Nach jedem Teil des Buchs ein kurzer Statusbericht an mich (kein STOP, außer bei grundlegenden
Widersprüchen oder Scope-Fragen).

### Phase 7 – Gesamtredaktion und Build
Konsistenzprüfung (Begriffe, Zahlen, Einheiten, Referenzfälle, Querverweise, Kästen „Stand“), Glossar mit
englischen Entsprechungen, Abkürzungsverzeichnis, Annahmenverzeichnis, Quellenverzeichnis, Formelsammlung,
Modellhandbuch, Stichwortverzeichnis. Gesamtbuch als PDF (`07_build/buch.py`), DOCX nur als Rückfallebene. Prüfliste
vor Drucklegung (bewegliche Themen mit Termin und Wirkung) und Abschlussbericht mit offenen Punkten und
Empfehlungen.

## 3. Pflicht-Themenliste (die Agenda muss alles abdecken)

**A. Strom als physikalisches Gut:** Leistung und Energie, Strom, Spannung, Wirk- und Blindleistung, Frequenz
(50 Hz) und Gleichgewicht von Erzeugung und Verbrauch, Trägheit und Momentanreserve, Verluste, Gleich- und
Wechselstrom, Netzebenen; Erzeugungstechnologien (Wind, Photovoltaik, Biomasse, Wasser, Gas, Kohle, früher
Kernkraft) mit Kosten- und Fahrweisenprofil; Lastprofile; Speicher und Flexibilität; Sektorkopplung (Wärmepumpen,
E-Mobilität, Elektrolyse).

**B. Das Stromsystem in Zahlen und seine Akteure:** Erzeugung, Verbrauch, Importe und Exporte, installierte
Leistung, Anteile erneuerbarer Energien; Rollen und Marktkommunikation (Erzeuger, Lieferanten, Händler,
Direktvermarkter, Aggregatoren, Bilanzkreisverantwortliche, vier Übertragungsnetzbetreiber, Verteilnetzbetreiber,
Messstellenbetreiber, Börsen, Clearinghäuser); Liberalisierung und Entflechtung (Unbundling); Institutionen
(BNetzA mit Beschlusskammern, Bundeskartellamt, Markttransparenzstelle, BMWE bzw. zuständiges Ministerium, ACER,
ENTSO-E, EU-Kommission).

**C. Großhandel:** Preisbildung (Merit Order, Grenzkosten, Knappheitspreise, negative Preise, Rolle von Gas- und
CO₂-Preis), Börsen und OTC-Handel; Terminmarkt (Futures und Forwards, Base, Peak und weitere Profile, Woche bis
Jahr, Optionen, Clearing, Sicherheitsleistungen und Margining, Liquidität); Day-Ahead-Markt (europäische
Marktkopplung SDAC, Algorithmus, Gebotsarten, Viertelstundenauflösung, Preisgrenzen); Intraday (Auktionen und
kontinuierlicher Handel, grenzüberschreitender Handel SIDC); PPAs (physisch und finanziell, Pay-as-produced,
Baseload, Profil- und Volumenrisiko), Herkunftsnachweise; Preisprognosen und Fundamentalmodelle; Wertfaktoren und
Kannibalisierung.

**D. Bilanzkreise und Ausgleichsenergie:** Bilanzkreissystem, Fahrpläne, Abrechnung (MaBiS), Ausgleichsenergiepreis
(reBAP) und seine Bestandteile, Anreize und Risiken für Bilanzkreisverantwortliche.

**E. Regelreserve und Systemdienstleistungen:** FCR, aFRR, mFRR (Leistungs- und Arbeitsmärkte, europäische
Plattformen, Präqualifikation, Preisregeln, Viertelstundenprodukte); Engpassmanagement (Redispatch 2.0,
Countertrading, Netzreserve, Einspeisemanagement), Kosten und Wälzung; Momentanreserve, Blindleistung,
Schwarzstartfähigkeit, Spannungshaltung; Flexibilitätsinstrumente (§ 13k EnWG „Nutzen statt Abregeln“, § 14a EnWG
steuerbare Verbrauchseinrichtungen, § 14c EnWG lokale Flexibilität), Lastmanagement.

**F. Versorgungssicherheit und Kapazität:** Energy-only-Markt und „Missing Money“, Versorgungssicherheitsmonitoring,
Reserven (Netzreserve, Kapazitätsreserve, Sicherheitsbereitschaft), Kapazitätsmarkt nach dem
Strom-Versorgungssicherheits-und-Kapazitätengesetz (StromVKG; Ausschreibungen, Reduktionsfaktoren,
Verpflichtungen), Kraftwerksstrategie, EU-Beihilferecht für Kapazitätsmechanismen; Vergleich mit anderen Ländern.

**G. Erneuerbare Energien und Förderung:** Geschichte und Logik des EEG (Einspeisevergütung, gleitende Marktprämie,
anzulegender Wert, Marktwerte), Ausschreibungen (Wind an Land, Solar erstes und zweites Segment, Biomasse,
Innovationsausschreibungen, Windenergie auf See nach WindSeeG; Gebotsverfahren, Höchstwerte, Realisierungsfristen,
Pönalen), Direktvermarktung (Pflicht, Vermarkter, Entgelte, sonstige Direktvermarktung), Regeln bei negativen
Preisen (§ 51 EEG, Solarspitzengesetz), Finanzierung des EEG (Wegfall der EEG-Umlage, EEG-Konto, Bundeshaushalt),
Differenzverträge (EU-Strommarktreform, EEG 2027), KWKG, Herkunftsnachweisregister und Doppelvermarktungsverbot.

**H. Das Netz:** Struktur (Übertragung und Verteilung, Spannungsebenen, Interkonnektoren, HGÜ), Netzbetrieb und
Systemführung, Netzanschluss (EnWG und EEG, Reifegradverfahren, Baukostenzuschuss, flexible
Netzanschlussvereinbarungen), Netzausbau (Netzentwicklungsplan, Bundesbedarfsplan, Genehmigung), Netzentgelte (Kostenwälzung,
Arbeits- und Leistungspreis, Sonderformen, Reform AgNes), Anreizregulierung (Erlösobergrenzen,
Regulierungsperioden), Gebotszone DE-LU und Gebotszonenüberprüfung, Messwesen und Digitalisierung (MsbG, Smart Meter,
Marktkommunikation).

**I. Endkundenmarkt:** Zusammensetzung des Strompreises (Beschaffung und Vertrieb, Netzentgelte, Messung, Umlagen nach
EnFG und KWKG, Offshore-Netzumlage, Konzessionsabgabe, Stromsteuer, Umsatzsteuer), Tarife (Grundversorgung,
Sonderverträge, dynamische Tarife), Lieferantenwechsel, Entlastungen für Industrie (Strompreiskompensation,
besondere Ausgleichsregelung, ermäßigte Stromsteuer), Beschaffungsstrategien von Lieferanten und Großverbrauchern
(Tranchen, strukturierte Beschaffung, Hedging), Risikomanagement (Preis-, Volumen-, Profil-, Kredit- und
Ausgleichsenergierisiko).

**J. Regulierung des Handels und des Marktes:** EU-Binnenmarktrecht (Verordnung (EU) 2019/943, Richtlinie (EU)
2019/944, Reform des Strommarktdesigns 2024), Netzkodizes (CACM, FCA, Electricity Balancing, System Operation),
REMIT (Insiderhandel, Marktmanipulation, Meldepflichten), Finanzmarktregeln für Energiederivate (MiFID II, EMIR),
Wettbewerbs- und Kartellaufsicht, Energiekrisenrecht 2022/2023 (Strompreisbremse, Erlösabschöpfung).

**K. CO₂ und Brennstoffe:** EU-Emissionshandel (EU-ETS und ETS 2), Gasmarkt und Gaspreise als Preistreiber,
Kohle- und Kernenergieausstieg, Brennstoffwechsel, Wirkung auf Merit Order und Spreads.

**L. Europa und Vergleichsmärkte:** Marktkopplung und flussbasierte Kapazitätsberechnung, Nachbarländer und
Stromaustausch; Vergleichsmärkte (Vorschlag: Großbritannien, Frankreich, Nordeuropa; in Phase 1 begründet
festlegen) mit Marktdesign, Förderung und Kapazitätsmechanismen.

**M. Investitionen und Geschäftsmodelle:** Erlös- und Kostenlogik von Erzeugung, Speicher, Handel, Vertrieb und
Netz; Risiken; Kennzahlen; was ein Investor an Marktdesign und Regulierung prüfen muss.

**N. Fallstudien:** Energiekrise 2022, negative Preise und Solarspitzen, Dunkelflauten, Kernenergieausstieg 2023,
Ereignisse der Marktkopplung, Ausschreibungsrunden ohne Gebote; Referenzfälle R1–R6 durchgehend.

## 4. Referenzfälle und Modelle

### 4.1 Durchgängige Referenzfälle (in allen passenden Kapiteln weiterführen)
Parameter in Phase 1 vorschlagen und begründen; alle Zahlen sind Annahmen mit A-ID und werden als D-Entscheidung
festgehalten.
- **R1 Haushalt:** Haushaltskunde mit typischem Jahresverbrauch, Standardlastprofil, ohne und mit Wärmepumpe oder
  E-Auto; Grundversorgung, Festpreisvertrag, dynamischer Tarif.
- **R2 Industriekunde:** mittelständischer Industriebetrieb mit Leistungsmessung, strukturierter Beschaffung über
  Terminmarkt und Spotmarkt, Netzentgelten nach Leistungspreis und Entlastungsregeln.
- **R3 Windpark an Land:** Windpark mit EEG-Zuschlag, Direktvermarktung und Marktprämie, Regeln bei negativen
  Preisen, Redispatch.
- **R4 Solarpark mit PPA:** Freiflächenanlage ohne Förderung mit PPA (Pay-as-produced oder Baseload), Herkunftsnachweisen
  und Profil- und Kannibalisierungsrisiko.
- **R5 Gaskraftwerk:** GuD-Anlage oder Gasturbine mit Spark Spread, Terminmarktabsicherung, Regelreserve und
  Kapazitätsmarkt.
- **R6 Batteriespeicher:** Großbatteriespeicher (Anschluss an das Vorprojekt), Arbitrage, Regelreserve,
  Netzentgelte und Baukostenzuschuss.

### 4.2 Modelle (Python, zusätzlich Excel, wo es dem Leser hilft)
- **M1 Merit Order und Kraftwerkseinsatz:** vereinfachtes Fundamentalmodell (Kraftwerkspark nach
  Technologieklassen, Residuallast aus realen Last- und Einspeisereihen, Brennstoff- und CO₂-Preise), Preise je
  Stunde oder Viertelstunde, Spark und Dark Spreads, Deckungsbeiträge und „Missing Money“, Szenarien; Abgleich mit
  realen Day-Ahead-Preisen.
- **M2 Erneuerbare: Marktwerte, Förderung und PPA:** Marktwerte und Wertfaktoren aus realen Preis- und
  Einspeisereihen, Marktprämie nach EEG mit Regeln bei negativen Preisen, Direktvermarktungskosten, Vergleich mit
  Differenzvertrag und PPA (Pay-as-produced, Baseload) für R3 und R4.
- **M3 Beschaffung und Risiko:** Beschaffung von R1 und R2 über Terminmarkt (Base und Peak in Tranchen) und
  Spotmarkt, Profil- und Volumenrisiko, Ausgleichsenergie, Sicherheitsleistungen; Absicherung von R5.
- **M4 Netz und Endkundenpreis:** Zerlegung des Endkundenpreises für R1 und R2, Netzentgelte nach Arbeits- und
  Leistungspreis, Umlagen und Steuern, Wirkung von Reformen (z. B. Netzentgeltreform, Entlastungen) als
  Szenarien.
Jedes Modell: README, Parameterdatei, Tests, ein dokumentierter Beispiellauf mit den Referenzfällen, Lauf-IDs
(`M<n>-JJJJMMTT-<Kürzel>`).

## 5. Multi-Agenten-Orchestrierung

Du bist Orchestrator und Hauptautor. Du planst, delegierst, führst zusammen und entscheidest. Subagents arbeiten in
eigenem Kontextfenster und sehen unseren Dialog nicht: Alles, was sie brauchen (Ziel, Dateipfade, Entscheidungen,
Referenzfälle, Qualitätsregeln), muss im Auftragstext oder in `CLAUDE.md` stehen.

### 5.1 Agenten (Dateien unter `.claude/agents/`, vorbereitet)
Jede Datei: YAML-Frontmatter mit `name`, `description` (präzise, handlungsorientiert), `tools` (nur die nötigen),
darunter der Systemprompt.

| name | Aufgabe | Tools |
|---|---|---|
| `markt-rechercheur` | Großhandel (Termin, Day-Ahead, Intraday), Börsen, PPAs, Herkunftsnachweise, Bilanzkreise und Ausgleichsenergie, Regelreserve- und Kapazitätsmärkte, Preise, CO₂ und Gas, Vergleichsmärkte | Read, Write, WebSearch, WebFetch |
| `regulierungs-rechercheur` | EnWG, EEG, WindSeeG, KWKG, EnFG, StromStG, MsbG, StromVKG, Netzzugangs- und Entgeltverordnungen, ARegV, EU-Recht und Netzkodizes, REMIT, MiFID II, EMIR, Festlegungen der BNetzA | Read, Write, WebSearch, WebFetch |
| `netz-technik-rechercheur` | Physik, Erzeugungstechnik, Netzstruktur und -betrieb, Systemdienstleistungen, Engpassmanagement, Netzausbau, Netzanschluss, Messwesen, Flexibilität | Read, Write, WebSearch, WebFetch |
| `endkunden-rechercheur` | Endkundenpreise und ihre Bestandteile, Tarife, Vertrieb, Beschaffung, Entlastungen, Verbrauchsstatistik | Read, Write, WebSearch, WebFetch |
| `modellierer` | Modelle M1–M4 bauen, testen, dokumentieren; Datensnapshots; Abbildungen | Read, Write, Edit, Bash, Glob, Grep |
| `autor` | Kapitel nach Kapitelvorlage schreiben, nur aus geprüften Notizen | Read, Write, Edit, Glob, Grep |
| `faktenpruefer` | Jede Zahl und Aussage gegen Quelle prüfen; Einheit, Auflösung, Stand, Rechtsstand, Rechenweg; Befundliste | Read, Write, WebSearch, WebFetch, Glob, Grep |
| `lektor` | Didaktik (Lernziele ↔ Inhalt ↔ Übungen), Verständlichkeit, Konsistenz, Stil | Read, Write, Edit, Glob, Grep |

### 5.2 Delegationsvorlage (jeder Auftrag enthält alle Punkte)
1. **Ziel:** Welche Frage ist zu beantworten, wofür wird das Ergebnis im Buch gebraucht?
2. **Abgrenzung:** Was gehört ausdrücklich nicht dazu (verhindert Doppelarbeit mit anderen Agenten)?
3. **Quellen- und Toolhinweise:** bevorzugte Primärquellen, Vorarbeiten aus dem Vorprojekt, Suchstrategie.
4. **Ausgabeformat:** Datei, Struktur, Pflichtfelder je Aussage (Aussage, Zahl und Einheit, Stand bzw. Fassung,
   Quelle und URL, Qualität A/B/C, Fakt/Schätzung/Annahme, Volltext oder Suchauszug).
5. **Aufwand:** Budget an Tool-Aufrufen und Abbruchkriterium.
6. **Rückmeldung:** kurze Zusammenfassung (höchstens 15 Zeilen) plus Liste offener Punkte; Details nur in Dateien.

### 5.3 Aufwandsregeln und Qualitätsschleifen
- Einzelne Faktenfrage: 1 Agent, 3–10 Tool-Aufrufe. Kapitelrecherche: 2–4 Agenten parallel, je 10–25 Aufrufe.
  Nie mehr als 5 Agenten gleichzeitig. Stoppe, wenn neue Quellen nichts Neues mehr liefern.
- Schreib-Prüf-Schleife je Kapitel: `autor` → `faktenpruefer` (Befundliste mit Schweregrad) → `autor` korrigiert →
  `lektor` → Abschlussfaktencheck → Orchestrator gibt frei. Der Faktenprüfer prüft ohne Kenntnis des
  Schreibprozesses, nur gegen Text und Quellen.
- Widersprüchliche Quellen: nicht glätten, sondern beide Werte mit Quelle nennen und erklären, warum sie sich
  unterscheiden (Stichtag, Definition, Auflösung, Abgrenzung, Methodik, Region).

## 6. Quellen- und Qualitätsregeln

- **Rangfolge:** (1) Gesetze, Verordnungen und EU-Rechtsakte in amtlicher Fassung, Gesetzesmaterialien,
  Festlegungen und Beschlüsse der BNetzA, Entscheidungen von ACER, EU-Kommission und Gerichten → (2) Daten und
  Veröffentlichungen der Netzbetreiber und Börsen (netztransparenz.de, regelleistung.net, SMARD, energy-charts, EEX,
  EPEX SPOT, ENTSO-E-Transparenzplattform), amtliche Statistik (Destatis, AGEB), Monitoringberichte von BNetzA und
  Bundeskartellamt → (3) anerkannte Studien (Fraunhofer, FfE, Agora Energiewende, EWI, DIW, Öko-Institut, IEA,
  ACER-Marktberichte, Ember) → (4) Kanzlei- und Fachmedien → (5) Anbieter- und Marketingseiten (nur Einordnung,
  nie einzige Quelle für eine Zahl).
- **Vorprojekt:** Befunde aus `00_input/vorprojekt_bess/` gelten mit ihrem Stand; vor Verwendung am Primärbeleg
  neu prüfen.
- **Datierung:** Jede Zahl mit Einheit, Stand und Quelle; jede Rechtsaussage mit Norm (Paragraf, Absatz, Satz,
  Nummer) und Fassung bzw. Aktenzeichen und Datum. Regulatorisch bewegliche Themen ausdrücklich kennzeichnen (Kasten
  „Stand“) und zu Beginn von Phase 3 sowie vor der Drucklegung neu prüfen; die Liste steht im Wissensstand
  (Abschnitt 11).
- **Kennzeichnung:** Fakt (mit Quelle) / Schätzung (mit Herleitung) / Annahme (mit Begründung). Annahmen zentral in
  `ANNAHMEN.md` mit ID (`A-xxx`).
- **Ebenen und Einheiten nie vermischen:** Leistung (MW, GW) und Energie (MWh, TWh); elektrisch und thermisch
  (MW_el, MWh_th); Stunden- und Viertelstundenwerte; Base, Peak und Profil; Handelstag und Liefertag; MEZ und MESZ;
  Gebotszone; Großhandels- und Endkundenpreis; netto und brutto (Umsatzsteuer); ct/kWh und €/MWh; nominal und real;
  installierte Leistung, gesicherte Leistung und Erzeugung.
- **Keine erfundenen Zahlen, Quellen, Normen oder Aktenzeichen.** Wenn nichts Belastbares zu finden ist: Lücke
  benennen.
- **Zitate:** Inhalte in eigenen Worten; wörtliche Zitate nur kurz und selten.
- **SOURCES.csv-Spalten:** id, titel, herausgeber, url, abrufdatum, stand_der_quelle, typ, qualität, kapitel.
- **Rechtliche Grenzen:** Das Buch ist keine Rechts-, Steuer- oder Anlageberatung. Stellen, an denen Fachleute
  nötig sind, als Kasten „Hier Fachleute einbinden“ markieren.

## 7. Didaktisches Kapiteldesign (Backward Design + Bloom)

Plane jedes Kapitel rückwärts: erst Lernziele, dann Nachweis (Übungen), dann Inhalt. Kapitelvorlage:
1. Lernziele (2–4, messbare Bloom-Verben, aufsteigende Stufe bis „bewerten“ oder „entwerfen“)
2. Warum das für Investoren und Marktteilnehmer zählt (3–5 Sätze) mit Marktkompass (berührte Ebenen)
3. Kerninhalt in Fließtext, mit Formeln, Tabellen, Abbildungen (Python-Grafiken aus realen Daten, wo möglich)
4. Rechenbeispiel am Referenzfall, Schritt für Schritt, reproduzierbar aus `04_models/`
5. Praxis-Check: Checkliste oder Prüffragen für Daten, Verträge, Prognosen, Angebote
6. Typische Fehler und Fallstricke
7. Zusammenfassung (5–8 Kernaussagen)
8. Übungen: 3–6 Aufgaben (Rechnen, Bewerten, Entscheiden) mit Lösungen im Anhang
9. Quellen des Kapitels und „Stand“-Vermerk

## 8. Dateistruktur

```
/00_input      Eingaben (nicht verändern); vorprojekt_bess/, vertraulich/
/01_agenda     AGENDA_VORSCHLAG.md, freigegebene AGENDA.md (je mit PDF)
/02_research   RESEARCH_PLAN.md, SYNTHESE.md, W0_verifikation/,
               <Kapitel-ID>/notizen_*.md
/03_chapters   <nn>_<slug>.md (ein Kapitel je Datei), vorwort.md, anhang_*.md
/04_models     m1_meritorder/, m2_erneuerbare/, m3_beschaffung/,
               m4_netz_endkunde/, daten/
/05_figures    Abbildungen je Kapitel (Skript, Daten, Bild, Beschriftung)
/06_review     Befundlisten je Kapitel, Leitfaden, Vorlagen, Prüflisten
/07_build      Satzsystem (build.py, buch.py, Filter, Vorlage, Schriften,
               buch_config.yaml), output/
/sources       SOURCES.csv, SOURCES_basis.csv, Skripte zum Register
CLAUDE.md  PROGRESS.md  DECISIONS.md  ANNAHMEN.md  GLOSSAR.md
```

## 9. Stil

Deutsch, sachlich, klar, für einen wirtschaftlich versierten Leser ohne energietechnische oder juristische
Ausbildung. Fachbegriffe beim ersten Auftreten erklären und ins Glossar übernehmen; Normen vollständig zitieren
(§ 51 Abs. 1 EEG). Physik so weit erklären, wie sie für Märkte und Netz nötig ist, ohne Herleitungen aus der
Elektrotechnik. Überwiegend Fließtext; Tabellen für Vergleiche und Zahlen; Aufzählungen nur für Checklisten. Jede
Zahl mit Einheit, Stand und Quelle. Formeln mit Variablenerklärung. Keine Werbesprache, keine Füllsätze.

## 10. Satz und Layout

Jedes Lieferobjekt (Agenda, Kapitel, Buch, Berichte) wird aus Markdown mit `07_build/build.py` gesetzt und als PDF
ausgeliefert; das Gesamtbuch mit `07_build/buch.py`. Layout, Kästen, Tabellen- und Abbildungsstil sind aus dem
Vorprojekt übernommen und bleiben unverändert (`07_build/typst/lehrbuch.typst`). Die Markdown-Konventionen stehen in
`CLAUDE.md` § 5, ein vollständiges Beispiel in `07_build/muster/formatmuster.md`. Vor jeder Übergabe visuell prüfen
(`07_build/preview.py`).

## 11. Vertraulichkeit eigener Unterlagen

Unterlagen unter `00_input/vertraulich/` sind vertraulich und anonymisiert. Im Buch erscheinen sie nur unter ihrer
Bezeichnung („Unterlage U1 (anonymisiert)“) mit Fundstelle; keine Namen, keine Hinweise auf Beteiligte, keine
nachgebauten Abbildungen, keine längeren Zitate; Zahlen nur nach meiner Freigabe (D-Entscheidung). Im
Quellenverzeichnis nur mit Bezeichnung (`vertraulich` in `07_build/buch_config.yaml`). Das vertrauliche
Erlösgutachten des Vorprojekts wird nicht verwendet.

## 12. Erster Schritt

Führe jetzt Phase 0 und Phase 1 aus. Recherchiere vor dem Agenda-Vorschlag nur so viel im Web, wie nötig ist, um
die Gliederung aktuell und vollständig zu machen (z. B. Stand der beweglichen Themen aus dem Wissensstand, Struktur
vergleichbarer Lehrbücher und Studiengänge zur Energiewirtschaft, Monitoringbericht von BNetzA und
Bundeskartellamt). Dann **STOP** mit dem Agenda-Vorschlag und deinen Rückfragen.
