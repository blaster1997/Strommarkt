# Leitfaden Kapitel · Schreib-Prüf-Schleife und Konventionen · Fassung vor Phase 5

Verbindlich für Autoren, Faktenprüfer, Lektoren und Modellierer. Er ergänzt `CLAUDE.md` und die
Agentendefinitionen und übernimmt die Erfahrungen des Vorprojekts (Lehrbuch „Ökonomie von Batteriespeichern in
Deutschland“, 26 Kapitel, 844 Seiten). Nach der Freigabe der Probekapitel (Phase 5) ergänzt der Orchestrator die
Kalibrierung (Tiefe, Umfang, Vorbilder) und datiert die Fassung neu.

## 1 Ablauf je Kapitel

1. **Autor:** Entwurf aus Recherchenotizen, `SYNTHESE.md`, `ANNAHMEN.md`, `DECISIONS.md` und Modellergebnissen.
   Dazu drei Dateien in `06_review/`:
   - `<Kxx>_loesungen_entwurf.md`: Lösungen im Format `## Kapitel <n>`, dann `### Übung <n>.<m>`; keine
     Vorbemerkungen, die in den Anhang gehören;
   - `<Kxx>_glossar_vorschlag.md`: Tabelle „| Begriff | Erklärung | Kap. |“, danach optional
     „**Ergänzungen bestehender Einträge (Vorschlag):**“ mit derselben Tabelle und zuletzt
     „**Englische Entsprechungen:**“ mit „| Begriff | englisch |“ (der Orchestrator übernimmt sie in
     `07_build/glossar_englisch.csv`; `buch.py` setzt daraus die Spalte „Englisch“ im Glossar);
   - `<Kxx>_autor_luecken.md`: Platzhalter `[LÜCKE: …]` und `[MODELL: …]` mit Fundstelle.
2. **Faktencheck v1** (vollständig) → `<Kxx>_faktencheck.md`.
3. **Autor korrigiert** → `<Kxx>_korrekturen.md` (Befund → Umsetzung oder begründete Ablehnung).
4. **Lektorat** mit Kürzung auf den Richtwert → `<Kxx>_lektorat.md`.
5. **Abschlussfaktencheck** (vollständig, einschließlich Wirkung des Lektorats) → `<Kxx>_faktencheck_v2.md`.
6. **Autor** setzt die Auflagen um.
7. **Orchestrator:** Sichtprüfung der Änderungen, Übernahme von Glossar (`07_build/glossar_merge.py`), Lösungen
   (`07_build/anhang_loesungen.py`), Quellen (`sources/merge_sources.py`, `sources/kapitel_ergaenzen.py`) und
   Annahmen, Satz als PDF, visuelle Prüfung, Freigabe mit D-Entscheidung, Eintrag in `PROGRESS.md`, Commit.

Nach der Freigabe gilt: Jede spätere inhaltliche Änderung (Erratum, Nachführung neuer Modellläufe oder Daten,
Gesamtredaktion) läuft über eine **Delta-Prüfung** des Faktenprüfers, die nur die geänderten Stellen und ihre Folgen
prüft (`<Kxx>_deltapruefung.md`).

Nur der Orchestrator bearbeitet `ANNAHMEN.md`, `DECISIONS.md`, `GLOSSAR.md`, `sources/SOURCES.csv` und
`03_chapters/anhang_loesungen.md`. Agenten schlagen Änderungen in ihren Review-Dateien vor. Kein git für Agenten.

## 2 Umfang

Richtwert je Kapitel: Agenda-Wörter × 1,3; Obergrenze × 1,4 (vor Phase 5 vorläufig; die Kalibrierung legt den
Faktor fest). Gezählt wird mit dem Regex `\S*[^\W_]\S*` über die ganze Datei einschließlich YAML-Kopf:

```bash
python3 -c "import re,sys; print(len(re.findall(r'\S*[^\W_]\S*', open(sys.argv[1], encoding='utf-8').read())))" 03_chapters/06_day_ahead.md
```

Füllsätze, Wiederholungen zwischen Abschnitten und doppelte Erklärungen sind nicht gewollt. Themen, die ein anderes
Kapitel ausführlich behandelt, per Querverweis („Kapitel 10“) statt erneut darstellen. Ist ein Kapitel an der
Grenze, wird eine Ergänzung durch Kürzung an anderer Stelle ausgeglichen.

## 3 Inhaltliche Konventionen

- **Marktkompass:** Jedes Kapitel nennt nach dem Abschnitt „Warum das für Investoren und Marktteilnehmer zählt“ die
  berührten Ebenen (Physik und Technik, Großhandel, System und Netz, Förderung, Regulierung, Endkundenpreis) mit
  ihrer Rolle im Kapitel; so sieht der Leser, wo das Kapitel im Gesamtsystem steht.
- **Perspektiven:** Wo eine Regel Erzeuger, Verbraucher, Händler, Netzbetreiber, Speicher oder den Staat
  unterschiedlich trifft, die Seiten mit ihren Zahlen darstellen.
- **Leistung und Energie:** MW und MWh nie verwechseln; Produkte für Leistung (Regelleistung, Kapazität) in
  €/MW je Zeitraum, Produkte für Energie in €/MWh; eine Viertelstunde mit 100 MW sind 25 MWh.
- **Zeit:** Auflösung (Stunde oder Viertelstunde) und Zeitraum bei jedem Preis und jeder Menge; Handelstag und
  Liefertag unterscheiden; Uhrzeiten in MEZ/MESZ (Ortszeit) und nur, wo nötig, in UTC mit Kennzeichnung; Zählungen
  vor und nach dem 01.10.2025 (Viertelstunde am Day-Ahead-Markt) nicht ohne Umrechnung vergleichen.
- **Preise:** Markt, Gebotszone, Lieferperiode, Base oder Peak, Mittelwert oder mengengewichtet; Großhandelspreise
  in €/MWh, Endkundenpreise in ct/kWh mit netto oder brutto und Kundengruppe; nominal oder real mit Basisjahr.
- **Statistik:** Brutto- oder Nettoerzeugung, öffentliche Erzeugung oder gesamt, installierte oder gesicherte
  Leistung; jede Zahl mit ihrer Abgrenzung, Abweichungen zwischen Quellen erklären.
- **Recht:** Norm mit Paragraf bzw. Artikel, Absatz, Satz und Fassung; „S.“ nur für Seite. Festlegungen „BNetzA,
  Beschluss vom TT.MM.JJJJ – BK6-…“ mit Tenorziffer, wenn zitiert; Gesetzgebung mit Drucksache und Stand. Streitige
  Fragen als streitig darstellen, mit beiden Lesarten und Quelle. Keine Beratungsformulierungen; Handlungsbedarf als
  „Hier Fachleute einbinden“.
- **Berufsbezeichnungen:** „Rechtsanwalt für Energierecht“ (eine Fachanwaltschaft für Energierecht gibt es nicht);
  „Fachanwalt für …“ nur mit einer Bezeichnung nach der Fachanwaltsordnung (z. B. Bank- und Kapitalmarktrecht,
  Steuerrecht, Verwaltungsrecht); Steuerberater, Wirtschaftsprüfer.
- **Modellzahlen** nur aus `04_models/*/ergebnisse/<lauf-id>/kapitelzahlen.md` bzw. den Laufordnern, immer mit
  Lauf-ID. Quellenzeilen mit Modellwerten tragen das Datum der Lauf-ID als Stand. Nach einem Neulauf keine Werte
  aus Archivläufen mehr zitieren, außer ausdrücklich als Archivwert gekennzeichnet. Modellpreise sind keine
  Prognosen. Fehlt ein Wert: `[MODELL: <Modell> – <Größe, Einheit, Fall, Zeitraum, Szenario>]` und Eintrag in
  `<Kxx>_autor_luecken.md`.
- **Verweise auf Modelldokumentation** mit „Ziffer“ (z. B. „M1-README, Ziffer 4“), nie mit „Abschnitt“.
- **Quellen:**
  - Quellen-IDs in eckigen Klammern; mehrere mit Komma, Bereiche mit „bis“ ([K06M-03 bis K06M-07]).
  - Belege, die nur als Suchauszug vorliegen, im Text als „(Suchauszug)“ kennzeichnen.
  - Qualität-C-Quellen nie als einzige Quelle für eine tragende Zahl.
  - Prüfvermerke des Orchestrators in den Notizen haben Vorrang vor dem Agententext.
  - Befunde aus dem Vorprojekt nur mit neuer ID und nach Prüfung am Primärbeleg.
- **Kästen „Stand“:** Prüfdatum („am TT.MM.JJJJ geprüft“), Fundstelle (Norm, Drucksache, Festlegung), Status
  (Entwurf, beschlossen, in Kraft ab, wirkt ab) und nächstes erwartetes Ereignis. Gleiche Themen in allen Kapiteln
  mit gleichem Prüfdatum und gleicher Formulierung; Fristen, die vom Ausgang eines Verfahrens abhängen, nie als
  festen Tag darstellen.
- **Vertrauliche Unterlagen:** nur „Unterlage U1 (anonymisiert)“ mit Fundstelle (Tab., Kap.), keine nachgebauten
  Abbildungen, keine Namen oder Dateinamen (CLAUDE.md § 8).
- **Ereignisse und Unternehmen:** nur belegte Tatsachen mit Datum; keine Spekulation über Motive oder
  Marktmissbrauch.

## 4 Schreibweisen

- Einheiten: kW, MW, GW; kWh, MWh, GWh, TWh; €/MWh, ct/kWh, €/MW/a, €/kW/a, €/MW je 4-h-Block, €/t CO₂, Hz, kV;
  Mio. €, Mrd. €; Prozentpunkte (ausgeschrieben). Thermische Größen mit Index (MW_th, MWh_th), wo Verwechslung droht.
- Währungen: £ und US-\$ immer mit Kurs und Datum.
- **Dollarzeichen maskieren:** `US-\$` bzw. `\$`. Ein unmaskiertes `$` startet einen Formelmodus.
- Formeln in LaTeX, Dezimalkomma `{,}`, Variablen direkt danach erklären; Indizes mit Text in `\text{…}`.
- Zahlen deutsch (1.234,5), Bereiche mit Halbgeviertstrich, Datum TT.MM.JJJJ, Anführungszeichen „…“.
- Abkürzungen beim ersten Auftreten ausschreiben (z. B. „Übertragungsnetzbetreiber (ÜNB)“, „Single Day-Ahead
  Coupling (SDAC)“); englische Marktbegriffe beim ersten Auftreten mit deutscher Erklärung.

## 5 Abbildungen und Tabellen

- Abbildungen liegen unter `05_figures/<Kxx>/` mit Skript, Daten und `<name>.md` (Beschriftungsvorschlag und
  Quelle). Im Bild weder Titel noch Quelle. Vorlage: `07_build/muster/abbildung_muster.py`.
- Zeitreihen aus realen Daten (Snapshot mit Manifest), Zeitachse mit Zeitzone und Auflösung; Preisachsen in
  €/MWh, Mengenachsen in MW oder GW (Leistung) bzw. MWh oder TWh (Energie).
- Gitterlinien auf sinnvollen Grenzen; Legende ohne Überdeckung der Daten; Schrift ab 7 pt bei 16 cm Satzbreite.
- Im Kapitel eine Beschriftung von höchstens 30 Wörtern, darunter die Zeile `Quelle: … (Stand TT.MM.JJJJ).`
- Tabellen als Pipe-Tabellen mit `Table:` und Quellenzeile; breite Tabellen auf höchstens sechs Spalten.

## 6 Didaktik

- Jedes Lernziel braucht Inhalt und mindestens eine Übung; jede Übung eine Lösung.
- Rechenbeispiele am Referenzfall mit Ziel, Eingaben (A-IDs), Schritten und Ergebnis; Werte aus dem Modell mit
  Lauf-ID.
- Praxis-Check nach dem gesamten Kerninhalt und den Rechenbeispielen, dann typische Fehler, Zusammenfassung,
  Übungen, Quellen und Stand.
- Einordnungen, die keine Befunde sind, als „Einordnung“ oder „Einschätzung“ kennzeichnen.
- Zusammenhänge zwischen Märkten ausdrücklich zeigen (z. B. wie der Day-Ahead-Preis den Marktwert, die
  Marktprämie und den Endkundenpreis beeinflusst); Querverweise auf die Kapitel, die den anderen Teil erklären.
- Wichtige Befunde klar, aber sachlich benennen (z. B. „Der Marktwert sinkt mit dem Ausbau schneller als der
  Base-Preis“).

## 7 Nach der Freigabe (Phase 7)

- Konsistenzprüfung: `python3 07_build/querverweise.py` (Verweise ohne Ziel), Lektoren je Buchteil (Begriffe,
  Leitzahlen, Referenzfälle, Einheiten).
- Listen: `python3 07_build/offene_punkte.py` (Lücken, Verifikationsliste, Kästen „Stand“).
- Register: `python3 sources/kapitel_abgleichen.py --schreiben` und `python3 sources/merge_sources.py`.
- Stichwörter: `python3 07_build/stichwoerter.py`; Gesamtbuch: `python3 07_build/buch.py`.
- Prüfliste vor Drucklegung: bewegliche Themen mit Stand im Buch, nächstem Ereignis, betroffenen Kapiteln und
  Rechnungen; Widersprüche zwischen Kästen „Stand“ auflösen; Werte des Folgejahres (Umlagen, Netzentgelte,
  Steuern) nachführen.
