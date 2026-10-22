# Wissensstand „Der Strommarkt in Deutschland“ · Ausgangshypothese

## 0 Status und Gebrauch

Dieses Dokument ist die **Ausgangshypothese**, nicht die Wahrheit. Es dient als Themenlandkarte, Prüfliste und
Startpunkt für Agenda und Welle 0. Es hat zwei Arten von Aussagen:

- **Befunde (B-xx, Abschnitt 2):** Aussagen, die das Vorprojekt „Ökonomie von Batteriespeichern in Deutschland“
  bis zum 04.10.2026 an Primärquellen geprüft hat. Die Quellenkürzel in eckigen Klammern verweisen auf
  `00_input/vorprojekt_bess/BESS_QUELLEN_Auswahl.csv` (mit URL, Abruf- und Stand-Datum). Befunde gelten mit ihrem
  Stand; sie sind in Welle 0 am Primärbeleg nachzuprüfen und erhalten im neuen Register eigene IDs.
- **Hypothesen (H-xx, Abschnitte 3–10 und 12):** Aussagen aus allgemeinem Wissen, ohne Recherche zusammengestellt.
  Sie sind vor jeder Verwendung am Primärtext zu prüfen: Norm in der geltenden Fassung, Festlegung oder
  Entscheidung im Volltext, Daten an der Quelle des Netzbetreibers, der Börse oder der amtlichen Statistik.

Daraus folgt:

- Zahlen, Daten, Normen und Aktenzeichen aus diesem Dokument dürfen nie ungeprüft in ein Kapitel übernommen werden.
- Wo die Prüfung eine Hypothese oder einen Befund widerlegt oder überholt, gilt der neue Befund; die Abweichung
  gehört in die Notiz der Welle 0.
- Fallnamen sind Kandidaten für Fallstudien; Tatsachen dazu nur aus öffentlich zugänglichen, datierten Quellen.

## 1 Leitfragen des Auftraggebers

1. Was ist Strom physikalisch, und warum prägen Gleichzeitigkeit von Erzeugung und Verbrauch, fehlende
   Speicherbarkeit im großen Maßstab und das Netz jeden Markt?
2. Welche Märkte gibt es, wer handelt dort was, wann und zu welchen Regeln, und wie hängen ihre Preise zusammen
   (Terminmarkt, Day-Ahead, Intraday, Ausgleichsenergie, Regelreserve, Kapazität, Herkunftsnachweise, PPAs)?
3. Wie werden erneuerbare Energien gefördert und vermarktet, was bringt eine Ausschreibung, und was ändert sich mit
   Differenzverträgen?
4. Wie funktioniert das Netz: Wer baut, betreibt und bezahlt es, wie kommt man an einen Anschluss, wie entstehen
   Engpässe und ihre Kosten?
5. Woraus besteht der Strompreis eines Haushalts und eines Industriebetriebs, und welche Teile lassen sich
   beeinflussen?
6. Welche Gesetze, Verordnungen, Festlegungen und Behörden regeln das alles, in Deutschland und in der EU, und was
   ändert sich gerade?
7. Woran erkenne ich bei einer Investition oder einem Vertrag im Strommarkt, ob Preise, Mengen und Regeln
   plausibel angesetzt sind?

## 2 Geprüfte Befunde aus dem Vorprojekt (Stand 27.09.–04.10.2026)

Die Kapitel des Vorprojekts in `00_input/vorprojekt_bess/` enthalten die Einzelheiten. Alle Befunde sind in
Welle 0 neu zu prüfen; die beweglichen unter ihnen stehen zusätzlich in Abschnitt 11.

**Großhandel und Preise**

- **B-01 Viertelstunde am Day-Ahead-Markt:** Seit dem Liefertag 01.10.2025 (Handelstag 30.09.2025) ist die
  Lieferperiode der europäischen Day-Ahead-Marktkopplung (SDAC) die Viertelstunde; ein Tag hat 96 statt 24 Preise.
  Gebotsschluss am Vortag 12 Uhr (Beleg vom Juli 2024) [K02M-24] (BESS-Kap. 2).
- **B-02 Preisgrenzen der SDAC:** Die harmonisierte Untergrenze sank ab dem Handelstag 28.05.2026 von −500 auf
  −600 €/MWh [W2V-10]; die ACER-Entscheidung 02/2026 vom 04.02.2026 bestätigt die Methodik [K02M-21]. Die
  Obergrenze liegt seit dem 10.05.2022 bei +4.000 €/MWh (BESS-Kap. 2, mit Hinweis auf eine angekündigte und nicht
  umgesetzte Erhöhung; prüfen).
- **B-03 Negative Preise:** Negative Day-Ahead-Preise gab es 2023 in 301, 2024 in 457 und 2025 in 573 Stunden
  laut BNetzA [K02M-02; K02M-03]; je nach Zählweise (Stunden, Viertelstunden, Stundenmittel) weichen die Werte für
  2025 leicht ab (BESS-Kap. 2).
- **B-04 Anteil erneuerbarer Energien:** 58,8 % der Stromerzeugung 2025 von 437,6 TWh (2024: 58,5 %), nach BNetzA
  [K02M-02]. Abgrenzung (brutto oder netto, öffentliche Erzeugung oder gesamt) bei jeder Verwendung angeben.
- **B-05 Intraday-Auktionen:** Seit dem 13.06.2024 gibt es drei europäische Intraday-Auktionen (IDA1 am Vortag
  15 Uhr, IDA2 am Vortag 22 Uhr, IDA3 am Liefertag 10 Uhr für 12–24 Uhr) [W2V-13; K02M-14]. Die grenzüberschreitende
  Gate Closure im kontinuierlichen Handel wird schrittweise auf 30 Minuten vor Lieferung verkürzt, mit
  Ausnahmen je Grenze (Übersicht vom 25.02.2026) [W2V-14].
- **B-06 Entkopplung:** Am 25./26.06.2024 kam es zu einer teilweisen Entkopplung der SDAC; der Bericht der SDAC
  vom 26.07.2024 beschreibt den Vorfall [K02M-24] (Fallkandidat).
- **B-07 Ausgleichsenergie:** Der regelzonenübergreifende einheitliche Bilanzausgleichsenergiepreis (reBAP) wird je
  Viertelstunde bestimmt; er beruht seit 2022 auf den Preisen der europäischen Regelarbeitsplattformen und ist an den
  Intraday-Markt gekoppelt; Modellbeschreibung ab 01.11.2023 [K02M-16; K02M-17].

**Regelreserve und Systemdienstleistungen**

- **B-08 Regelarbeit:** Seit dem 22.06.2022 wird Regelarbeit mit Viertelstundenprodukten und Vergütung zum
  Grenzpreis gehandelt, Gebotsschluss 25 Minuten vor der Lieferviertelstunde [K03M-08].
- **B-09 Viertelstundenprodukte der Regelleistung:** Beschluss BK6-25-212 der BNetzA vom 28.10.2025: Für aFRR- und
  mFRR-Leistung sind zusätzlich zu 4-h-Produkten Gebote für einzelne Viertelstunden zulässig; Umsetzung bis
  spätestens 28.10.2026 [K03R-02; W2V-15]. Starttermin prüfen.
- **B-10 Preisgrenzen der Regelarbeitsplattformen:** harmonisierte Grenze ±15.000 €/MWh in der Übergangszeit, nach
  ACER-Methodik ausweitbar bis zur technischen Grenze ±99.999 €/MWh [W2V-16].
- **B-11 Momentanreserve:** Seit dem 22.01.2026 beschaffen die ÜNB Momentanreserve marktgestützt nach § 12h EnWG
  in vier Produkten; erste Preisperiode bis 21.01.2028 [K03M-06; K03M-29; VR3-39].
- **B-12 „Nutzen statt Abregeln“:** Zielmodell nach § 13k EnWG ab 01.10.2026; Entlastungsregionen nach dem
  Umsetzungskonzept der ÜNB vom 01.04.2026 nur im Norden (50Hertz, TenneT) [VR3-32].
- **B-13 Lokale Flexibilitätsmärkte:** Die Pflicht der Verteilnetzbetreiber nach § 14c EnWG ist nach § 118 Abs. 28
  EnWG ausgesetzt, bis die BNetzA erstmals Spezifikationen genehmigt oder festlegt [SYN-17].

**Kapazität**

- **B-14 Kapazitätsmarkt:** Das Strom-Versorgungssicherheits-und-Kapazitätengesetz (StromVKG) wurde am 21.07.2026
  ausgefertigt [K03R-01]; die EU-Kommission hat die Beihilfe am 02.09.2026 genehmigt, erster Gebotstermin
  08.09.2026, Höchstwert 244.000 €/MW reduzierter Leistung und Jahr, Lieferung ab 01.11.2031 [W0R-10; W0R-11;
  K03R-01]. Ergebnisse und weitere Gebotstermine prüfen.

**Erneuerbare Energien**

- **B-15 Marktprämie:** Die gleitende Marktprämie ist die Differenz aus anzulegendem Wert und Marktwert, nicht
  negativ; Jahresmarktwert Solar 2024 46,24 und 2025 45,08 €/MWh [VR3-29; K15M-01].
- **B-16 Negative Preise:** Für Anlagen mit Inbetriebnahme ab 25.02.2025 entfällt der Anspruch in jeder
  Viertelstunde mit negativem Day-Ahead-Preis (§ 51 EEG in der Fassung des Solarspitzengesetzes); für ältere Anlagen
  gelten Übergangsregeln [W2V-01; W2V-06; W2V-05; VR3-30].
- **B-17 Ausschreibung Solar:** Gebotstermin 01.03.2026, erstes Segment: Zuschlagswerte 3,99–5,10 ct/kWh, Mittel
  4,94 ct/kWh, Höchstwert 5,79 ct/kWh [WS-18].
- **B-18 EEG 2027:** Regierungsentwurf vom 07.09.2026 (BT-Drs. 21/7867), Inkrafttreten geplant am 01.01.2027;
  zweiseitiger Differenzvertrag für Anlagen ab 100 kW außer Biomasse über einen Refinanzierungsbeitrag;
  Innovationsausschreibungen sollen entfallen [W2V-17; K12R-05; W0R-15]. Gesetzgebungsstand prüfen.

**Netz**

- **B-19 Netzentgeltreform AgNes:** Festlegungsentwurf der Großen Beschlusskammer der BNetzA vom 06.08.2026
  (GBK-25-01-1#3) [W0R-01; W0R-02]. Stand des Verfahrens prüfen.
- **B-20 Netzanschluss:** Gesetzentwurf der Bundesregierung zum Netzanschlusspaket (07.09.2026), Stellungnahme des
  Bundesrates und Gegenäußerung (30.09.2026) [K11O-02; K11O-03]; Reifegradverfahren der ÜNB für Anschlüsse an das
  Übertragungsnetz, Verfahrensdokumentation vom 27.04.2026 [K11O-04]; Anschlusspflicht nach § 8 EEG [K11O-05].
- **B-21 Baukostenzuschuss:** Der BGH hat mit Beschluss vom 15.07.2025 (EnVR 1/24) einen Baukostenzuschuss für
  einen netzgekoppelten Batteriespeicher gebilligt [K11R-02].
- **B-22 Speicher und Netzentgelte:** Festlegung „MiSpeL“ der BNetzA vom 01.10.2026 zu Mischspeichern und
  Abgrenzung von Strommengen [K12R-17; K12R-18]; rund 2,4 GW und 3,2 GWh Großbatteriespeicher in Betrieb am
  15.10.2025 [K03M-07].

## 3 Strom, Technik und System in Zahlen (Hypothesen)

- **H-01 Leistung und Energie:** Leistung (kW, MW, GW) ist eine Momentangröße, Energie (kWh, MWh, TWh) das Produkt
  aus Leistung und Zeit. Preise im Großhandel gelten je MWh, Kapazitäts- und Regelleistungsentgelte je MW und
  Zeitraum, Netzentgelte teils je kWh und teils je kW. Verwechslungen sind die häufigste Fehlerquelle.
- **H-02 Gleichgewicht und Frequenz:** Im synchronen Verbundnetz Kontinentaleuropas beträgt die Sollfrequenz
  50 Hz; Ungleichgewichte zeigen sich als Frequenzabweichung. Gegen Abweichungen wirken nacheinander Momentanreserve
  (Trägheit), Primärregelung (FCR), Sekundärregelung (aFRR) und Minutenreserve (mFRR). Prüfen: Zeitkriterien und
  Dimensionierung bei ENTSO-E und den ÜNB.
- **H-03 Netzebenen:** Höchstspannung (220 und 380 kV) als Übertragungsnetz, Hochspannung (110 kV), Mittelspannung
  und Niederspannung (0,4 kV) als Verteilnetz; die Netzentgeltsystematik zählt sieben Netz- und Umspannebenen.
  Prüfen: StromNEV bzw. Nachfolgeregelung, Monitoringbericht.
- **H-04 Erzeugung:** Erzeugungstechnologien unterscheiden sich in Investitions- und Grenzkosten, Flexibilität und
  Verfügbarkeit (Wetterabhängigkeit). Kennzahlen: installierte Leistung, gesicherte Leistung, Volllaststunden,
  Erzeugung. Prüfen: Marktstammdatenregister, AGEB, energy-charts, SMARD.
- **H-05 Ausstiege:** Die letzten drei Kernkraftwerke gingen am 15.04.2023 vom Netz; der Kohleausstieg ist nach dem
  Kohleverstromungsbeendigungsgesetz spätestens 2038 vorgesehen, im Rheinischen Revier früher. Prüfen: KVBG in der
  geltenden Fassung, Stilllegungsauktionen und Überprüfungen.
- **H-06 Verbrauch und Sektorkopplung:** Der Stromverbrauch soll durch Wärmepumpen, E-Mobilität, Rechenzentren und
  Elektrolyse steigen; Szenarien weichen stark voneinander ab. Prüfen: Szenariorahmen zum Netzentwicklungsplan,
  Langfristszenarien, Versorgungssicherheitsmonitoring.
- **H-07 Statistikbegriffe:** Brutto- und Nettostromerzeugung, öffentliche Nettoerzeugung (energy-charts),
  Bruttostromverbrauch, Netzlast, Residuallast. Jede Zahl braucht ihre Abgrenzung; Quellen weichen dadurch um
  mehrere Prozentpunkte voneinander ab.

## 4 Akteure, Rollen und Institutionen (Hypothesen)

- **H-08 Übertragungsnetzbetreiber:** vier ÜNB mit Regelzonen (50Hertz, Amprion, TenneT, TransnetBW), verbunden im
  Netzregelverbund; dazu mehrere Hundert Verteilnetzbetreiber. Prüfen: Anzahl und Eigentümerstrukturen
  (Monitoringbericht von BNetzA und Bundeskartellamt).
- **H-09 Entflechtung:** Netzbetrieb ist von Erzeugung und Vertrieb zu trennen (§§ 6 ff. EnWG); kleinere
  Verteilnetzbetreiber sind teilweise ausgenommen. Prüfen: Schwellenwerte und Formen (Eigentums-, Rechts-,
  operationelle und buchhalterische Entflechtung).
- **H-10 Marktrollen:** Erzeuger, Lieferanten, Händler, Direktvermarkter, Aggregatoren, Bilanzkreisverantwortliche,
  Netzbetreiber, Messstellenbetreiber, Börsen (EEX, EPEX SPOT, Nord Pool), Clearinghaus (ECC), Broker. Marktlokation
  und Messlokation als Grundbegriffe der Marktkommunikation. Prüfen: Festlegungen der BNetzA zur Marktkommunikation,
  Lieferantenwechsel (Beschleunigung auf 24 Stunden seit 2025 nach § 20a EnWG).
- **H-11 Institutionen:** BNetzA mit Beschlusskammern und Großer Beschlusskammer (erweiterte Festlegungskompetenz
  nach dem EuGH-Urteil vom 02.09.2021, C-718/18, zur Unabhängigkeit der Regulierungsbehörde), Landesregulierungsbehörden,
  Bundeskartellamt und Markttransparenzstelle, zuständiges Bundesministerium (BMWE), Umweltbundesamt
  (Herkunftsnachweisregister, DEHSt für den Emissionshandel), ACER, ENTSO-E, EU-Kommission. Prüfen: Zuständigkeiten
  und die Ablösung von Verordnungen (StromNZV, StromNEV) durch Festlegungen.

## 5 Großhandel (Hypothesen)

- **H-12 Preisbildung:** Am Day-Ahead-Markt gilt ein einheitlicher Preis je Gebotszone und Lieferperiode
  (Pay-as-clear). Er wird von der teuersten noch benötigten Anlage gesetzt (Merit Order); in Knappheit bestimmen
  Zahlungsbereitschaft und Flexibilität den Preis, bei Überangebot entstehen negative Preise. Gas- und CO₂-Preis
  prägen den Strompreis, solange Gaskraftwerke häufig preissetzend sind. Prüfen: Preissetzungsanalysen (ACER,
  Studien).
- **H-13 Börsen und OTC:** Strom wird an Börsen und außerbörslich (OTC, bilateral oder über Broker) gehandelt;
  OTC-Geschäfte können zum Clearing registriert werden. Prüfen: Marktanteile Börse und OTC, Monitoringbericht.
- **H-14 Terminmarkt:** An der EEX werden Futures für Deutschland (Phelix DE) mit Lieferperioden von Tag, Wochenende,
  Woche, Monat, Quartal und Jahr gehandelt, als Base (alle Stunden) und Peak (werktags 8–20 Uhr), finanziell erfüllt;
  dazu Optionen. Clearing über die European Commodity Clearing mit Initial und Variation Margin. Forwards sind die
  OTC-Entsprechung, meist physisch erfüllt. Prüfen: Produktspezifikationen, Liquidität je Laufzeit, Umstellung auf
  Viertelstundenprodukte am Kurzfristterminmarkt.
- **H-15 Day-Ahead-Markt:** Mehrere nominierte Strommarktbetreiber (NEMOs) bieten Day-Ahead-Handel in Deutschland
  an; der gemeinsame Algorithmus (Euphemia) koppelt die Gebotszonen unter Berücksichtigung der Übertragungskapazitäten.
  Gebotsarten: Einzel-, Block- und komplexe Gebote. Prüfen: Gebotsarten nach der Umstellung auf
  Viertelstunden.
- **H-16 Intraday:** kontinuierlicher Handel über die europäische Plattform SIDC und lokal bis kurz vor Lieferung
  (innerhalb einer Regelzone bis 5 Minuten vorher), daneben die Intraday-Auktionen (B-05). Prüfen: Fristen, Produkte,
  Volumen.
- **H-17 PPAs:** Stromabnahmeverträge zwischen Erzeuger und Abnehmer, physisch (mit Lieferung über Bilanzkreise)
  oder finanziell (virtuell, als Differenzausgleich); Profile Pay-as-produced, Baseload, Pay-as-nominated; Risiken:
  Preis, Volumen, Profil, Ausgleichsenergie, Kredit, Kannibalisierung. Prüfen: Marktdaten (Preisindizes sind meist
  Anbieterdaten, Qualität C), Musterverträge (EFET), Bilanzierung.
- **H-18 Herkunftsnachweise:** Das Herkunftsnachweisregister beim Umweltbundesamt stellt Herkunftsnachweise aus;
  für EEG-geförderten Strom gibt es keine (Doppelvermarktungsverbot), dafür Regionalnachweise. Prüfen: §§ 79–80 EEG,
  HkRNDV, Preise (meist Anbieterdaten).
- **H-19 Wertfaktoren und Kannibalisierung:** Der Marktwert von Solar- und Windstrom liegt unter dem Base-Preis,
  weil viel Erzeugung gleichzeitig anfällt; der Abstand wächst mit dem Ausbau, Speicher und Flexibilität verringern
  ihn. Prüfen: Monats- und Jahresmarktwerte auf netztransparenz.de, eigene Rechnung in M2.
- **H-20 Preisprognosen:** Langfristige Strompreisprognosen beruhen meist auf Fundamentalmodellen mit Annahmen zu
  Brennstoff- und CO₂-Preisen, Zubau, Nachfrage und Marktdesign; ihre Bandbreite ist groß. Prüfen: veröffentlichte
  Szenarien (Studien, Netzentwicklungsplan), Methodenbeschreibungen der Anbieter.

## 6 Bilanzkreise, Regelreserve und Systemsicherheit (Hypothesen)

- **H-21 Bilanzkreise:** Jede Einspeise- und Entnahmestelle ist einem Bilanzkreis zugeordnet; der
  Bilanzkreisverantwortliche muss ihn je Viertelstunde ausgeglichen halten und Fahrpläne anmelden. Abweichungen
  rechnen die ÜNB als Ausgleichsenergie zum reBAP ab (B-07); Abrechnung nach den Marktregeln für die Bilanzkreisabrechnung
  (MaBiS). Prüfen: Festlegungen der BNetzA, Standardbilanzkreisvertrag, Knappheitskomponente.
- **H-22 Regelreserve:** FCR, aFRR und mFRR werden von den ÜNB ausgeschrieben, Leistung und Arbeit getrennt;
  Regelarbeit über die europäischen Plattformen PICASSO (aFRR) und MARI (mFRR). Anbieter brauchen eine
  Präqualifikation. Prüfen: Plattformbeitritte, Bedarf, Kostenentwicklung (regelleistung.net).
- **H-23 Engpassmanagement:** Redispatch 2.0 seit 01.10.2021 (Einbeziehung von Anlagen ab 100 kW und Ablösung des
  Einspeisemanagements), Countertrading, Netzreserve (§ 13d EnWG), besondere netztechnische Betriebsmittel; die
  Kosten werden über die Netzentgelte gewälzt und betragen mehrere Milliarden Euro je Jahr. Prüfen: Quartals- und
  Jahresberichte der BNetzA zu Netz- und Systemsicherheitsmaßnahmen.
- **H-24 Weitere Systemdienstleistungen:** Spannungshaltung und Blindleistung, Schwarzstartfähigkeit,
  Momentanreserve (B-11), marktgestützte Beschaffung nach § 12h EnWG. Prüfen: Festlegungen und Stand je Produkt.
- **H-25 Steuerbare Verbrauchseinrichtungen:** Nach § 14a EnWG dürfen Verteilnetzbetreiber Wärmepumpen, Wallboxen
  und andere steuerbare Verbrauchseinrichtungen bei Netzengpässen dimmen; im Gegenzug sinken die Netzentgelte
  (Festlegungen der BNetzA, anwendbar seit 01.01.2024). Prüfen: Module, Mindestleistung, Übergangsregeln.

## 7 Versorgungssicherheit und Kapazität (Hypothesen)

- **H-26 Energy-only-Markt:** Deutschland hat sich 2016 (Strommarktgesetz) für einen Energy-only-Markt mit
  Reserven entschieden; Kritiker verweisen auf „Missing Money“ für Spitzenlastkraftwerke. Mit dem StromVKG (B-14)
  kommt ein zentraler Kapazitätsmarkt hinzu. Prüfen: Gesetzesbegründung, Monitoringbericht zur Versorgungssicherheit
  (§ 51 EnWG).
- **H-27 Reserven:** Netzreserve (§ 13d EnWG), Kapazitätsreserve (§ 13e EnWG), Sicherheitsbereitschaft von
  Braunkohlekraftwerken (§ 13g EnWG). Prüfen: Umfang, Fristen, Verhältnis zum Kapazitätsmarkt.
- **H-28 Kraftwerksstrategie:** Ausschreibungen für neue steuerbare (wasserstofffähige) Gaskraftwerke wurden seit
  2023 vorbereitet und mehrfach umgeplant. Prüfen: Verhältnis zum StromVKG und Stand der Ausschreibungen.
- **H-29 EU-Rahmen:** Kapazitätsmechanismen sind nach der Verordnung (EU) 2019/943 an eine Analyse der
  Ressourcenadäquanz, CO₂-Grenzwerte und Beihilferecht gebunden; die Reform des Strommarktdesigns 2024 hat sie
  erleichtert. Prüfen: Art. 20–27 der Verordnung in der geltenden Fassung, Beihilfeleitlinien.

## 8 Erneuerbare Energien und Förderung (Hypothesen)

- **H-30 Entwicklung des EEG:** Einspeisevergütung seit 2000, optionale Marktprämie seit 2012, Pflicht zur
  Direktvermarktung für neue größere Anlagen ab 2014 (Schwellen schrittweise gesenkt), Ausschreibungen seit 2015/2017.
  Prüfen: Fassungen und Schwellenwerte.
- **H-31 Ausschreibungen:** Die BNetzA schreibt Wind an Land, Solar (erstes und zweites Segment), Biomasse und
  Innovationsanlagen zu festen Gebotsterminen aus; Zuschlag nach Gebotspreis (Pay-as-bid), Höchstwerte durch
  Festlegung der BNetzA, Sicherheiten und Realisierungsfristen; bei Wind an Land ein Referenzertragsmodell.
  Prüfen: Gebotstermine, Volumen, Ergebnisse der Runden 2025–2026, Unterzeichnungen.
- **H-32 Windenergie auf See:** Ausschreibungen nach WindSeeG für zentral voruntersuchte und nicht zentral
  voruntersuchte Flächen, mit dynamischem Gebotsverfahren und Zahlungen der Bieter; eine Runde im Jahr 2025 soll ohne
  Gebote geblieben sein. Prüfen: Ergebnisse, Gesetzesänderungen, Übergang zu Differenzverträgen.
- **H-33 Direktvermarktung:** Anlagenbetreiber verkaufen ihren Strom über Direktvermarkter an der Börse und erhalten
  die Marktprämie vom Netzbetreiber; daneben die sonstige Direktvermarktung ohne Förderung (z. B. über PPA).
  Prüfen: Schwellen, Entgelte (meist Anbieterdaten), Fernsteuerbarkeit.
- **H-34 Finanzierung:** Die EEG-Umlage wurde zum 01.07.2022 auf null gesenkt und mit dem
  Energiefinanzierungsgesetz (EnFG) ab 2023 abgeschafft; das EEG-Konto der ÜNB wird seither aus dem Bundeshaushalt
  (Klima- und Transformationsfonds) ausgeglichen. Prüfen: Höhe der Zahlungen, Prognosen der ÜNB, Haushalt.
- **H-35 KWKG und Biomasse:** Zuschläge für Strom aus Kraft-Wärme-Kopplung nach dem KWKG, Umlage nach dem EnFG;
  Laufzeit und Verlängerung des KWKG prüfen; Biomasse mit eigenen Ausschreibungen und Flexibilitätszuschlag.
- **H-36 Differenzverträge:** Nach der Reform des EU-Strommarktdesigns (Verordnung (EU) 2024/1747) soll die direkte
  Preisförderung neuer Anlagen ab Mitte 2027 grundsätzlich über zweiseitige Differenzverträge oder gleichwertige
  Instrumente laufen; das EEG 2027 (B-18) setzt das um. Prüfen: Art. 19d der Verordnung, Fristen, Ausnahmen.

## 9 Das Netz (Hypothesen)

- **H-37 Netzausbau:** Bedarf über Szenariorahmen, Netzentwicklungspläne (Strom und Offshore), Bundesbedarfsplan
  und Energieleitungsausbaugesetz; Genehmigung über Bundesfachplanung und Planfeststellung (NABEG) bzw. Länder;
  Hochspannungs-Gleichstrom-Übertragung (HGÜ) für Nord-Süd-Korridore. Prüfen: aktueller Netzentwicklungsplan,
  Monitoring der BNetzA zum Netzausbau, Kosten.
- **H-38 Netzentgelte:** Netzbetreiber erhalten Erlösobergrenzen nach der Anreizregulierung (ARegV) mit
  Regulierungsperioden und Effizienzvergleich; die Entgelte werden von oben nach unten gewälzt; Arbeits- und
  Grundpreis für Standardlastprofilkunden, Leistungs- und Arbeitspreis für Kunden mit Leistungsmessung;
  Sonderformen (§ 19 StromNEV, individuelle Netzentgelte); Verteilung von Mehrkosten in Regionen mit hohem
  EE-Ausbau; Zuschüsse des Bundes zu den Übertragungsnetzentgelten. Prüfen: geltende Rechtsgrundlagen (Ablösung von
  StromNEV und ARegV durch Festlegungen), Höhe der Entgelte, AgNes (B-19).
- **H-39 Gebotszone:** Die gemeinsame Gebotszone Deutschland–Luxemburg besteht seit 01.10.2018 (Trennung von
  Österreich); die europäische Gebotszonenüberprüfung hat eine Aufteilung Deutschlands untersucht. Prüfen:
  Ergebnisbericht der ÜNB, Position der Bundesregierung, Entscheidung und nächste Schritte.
- **H-40 Kapazitätsberechnung:** In der Region Core gilt seit 08.06.2022 die flussbasierte Marktkopplung; nach
  Art. 16 Abs. 8 der Verordnung (EU) 2019/943 müssen ÜNB mindestens 70 % der Kapazität für den grenzüberschreitenden
  Handel bereitstellen (mit Aktionsplänen und Ausnahmen). Prüfen.
- **H-41 Messwesen:** Das Messstellenbetriebsgesetz regelt den Rollout intelligenter Messsysteme mit Pflichtfällen
  und Preisobergrenzen; das Gesetz zum Neustart der Digitalisierung der Energiewende (2023) hat ihn beschleunigt.
  Prüfen: Pflichtfälle, Fristen, Rolloutstand.
- **H-42 Netzanschluss:** Anschlusspflicht für EEG-Anlagen (§ 8 EEG) und allgemein nach §§ 17 ff. EnWG;
  Überzeichnung der Anschlusskapazität durch Speicher-, Rechenzentrums- und Industrieanfragen; Reifegradverfahren und
  Netzanschlusspaket (B-20); flexible Netzanschlussvereinbarungen; Baukostenzuschuss (B-21). Prüfen.

## 10 Endkundenmarkt, Regulierung des Handels, CO₂ und Brennstoffe (Hypothesen)

- **H-43 Strompreisbestandteile:** Beschaffung und Vertrieb, Netzentgelte, Messstellenbetrieb, Umlagen nach EnFG und
  KWKG (KWKG-Umlage, Offshore-Netzumlage, Aufschlag für besondere Netznutzung), Konzessionsabgabe, Stromsteuer,
  Umsatzsteuer. Prüfen: Werte des Jahres (netztransparenz.de, BNetzA-Monitoringbericht, BDEW-Strompreisanalyse als
  Sekundärquelle).
- **H-44 Stromsteuer:** Regelsatz 2,05 ct/kWh; für das produzierende Gewerbe sowie Land- und Forstwirtschaft ab 2026
  auf den EU-Mindestsatz gesenkt, für Haushalte nicht. Prüfen: StromStG in der geltenden Fassung.
- **H-45 Tarife:** Grundversorgung (§ 36 EnWG) und Ersatzversorgung (§ 38 EnWG), Sonderverträge, dynamische Tarife
  (seit 01.01.2025 von allen Lieferanten anzubieten, § 41a EnWG), zeitvariable Netzentgelte im Rahmen von § 14a EnWG.
  Prüfen.
- **H-46 Entlastungen der Industrie:** Strompreiskompensation für indirekte CO₂-Kosten, Besondere Ausgleichsregelung
  nach EnFG für Umlagen, individuelle Netzentgelte, ermäßigte Stromsteuer; Pläne für einen Industriestrompreis nach
  neuem EU-Beihilferahmen. Prüfen: Rechtsstand und Antragsbedingungen.
- **H-47 Beschaffung und Risikomanagement:** Lieferanten und Großverbraucher beschaffen in Tranchen über den
  Terminmarkt und strukturieren den Rest über Spot- und Intradaymärkte; Risiken: Preis, Volumen, Profil,
  Ausgleichsenergie, Kredit und Liquidität (Margining). Prüfen: Fachliteratur, Praxisleitfäden (Qualität B/C).
- **H-48 REMIT:** Verbot von Insiderhandel und Marktmanipulation im Energiegroßhandel, Registrierungs-, Melde- und
  Veröffentlichungspflichten (Verordnung (EU) Nr. 1227/2011, geändert 2024 durch REMIT II). Prüfen: Fassung,
  Pflichten, Durchsetzung durch BNetzA und ACER.
- **H-49 Finanzmarktrecht:** Energiederivate können Finanzinstrumente nach MiFID II sein (Ausnahme für
  Nebentätigkeiten), mit Meldepflichten und Clearingpflichten nach EMIR. Prüfen: KWG, WpIG, EMIR 3.
- **H-50 Energiekrise:** Notfallmaßnahmen 2022/2023: Erlösobergrenze für inframarginale Erzeuger nach Verordnung
  (EU) 2022/1854, Strompreisbremse mit Abschöpfung von Überschusserlösen in Deutschland. Prüfen: Zeiträume, Wirkung,
  Rückzahlungen.
- **H-51 CO₂:** Der EU-Emissionshandel (EU-ETS) deckt Stromerzeugung und Industrie ab; ein zweites System (ETS 2)
  für Gebäude und Verkehr soll später starten, Startjahr möglicherweise verschoben. Prüfen: Preise, Marktstabilitätsreserve,
  Starttermin ETS 2, nationaler Brennstoffemissionshandel (BEHG).
- **H-52 Gas:** Der Gaspreis (Handelspunkte THE und TTF) bestimmt die Grenzkosten von Gaskraftwerken und damit oft
  den Strompreis; 2022 stieg er auf ein Vielfaches des Vorkrisenniveaus. Prüfen: Preisreihen, Gasspeicher, Rolle von
  LNG.

## 11 Bewegliche Themen (Prüfliste für Welle 0 und vor Drucklegung)

| Nr. | Thema | Was zu prüfen ist |
|---|---|---|
| T1 | EEG 2027 und Differenzverträge | Gesetzgebung (BT-Drs. 21/7867), Inkrafttreten, Übergangsregeln, beihilferechtliche Genehmigung |
| T2 | Ausschreibungen nach EEG und WindSeeG | Gebotstermine, Volumen, Höchstwerte, Ergebnisse, Runden ohne Gebote |
| T3 | Kapazitätsmarkt (StromVKG) | Ergebnisse des Gebotstermins 08.09.2026, weitere Termine, Reduktionsfaktoren, Kraftwerksstrategie |
| T4 | Netzentgeltreform AgNes | endgültige Festlegung, Inkrafttreten, Übergang, Wirkung auf Einspeiser, Speicher und Verbraucher |
| T5 | Netzanschlusspaket und Reifegradverfahren | Gesetzgebung, Baukostenzuschuss, Verfahren bei ÜNB und VNB |
| T6 | Regelreserve | Start der Viertelstundenprodukte (BK6-25-212), Plattformen, Preisgrenzen, Präqualifikation |
| T7 | Flexibilität | § 13k EnWG nach dem Start am 01.10.2026, § 14a, § 14c, MiSpeL, Momentanreserve |
| T8 | Day-Ahead und Intraday | Preisgrenzen (B-02), Viertelstundenprodukte am Terminmarkt, 30-Minuten-Gate-Closure |
| T9 | Gebotszone | Ergebnis der Gebotszonenüberprüfung, Entscheidung, Engpassberichte |
| T10 | Endkundenpreisbestandteile | Umlagen, Netzentgelte und Zuschüsse des Bundes, Stromsteuer für das Folgejahr |
| T11 | CO₂ und Gas | EU-ETS, ETS 2, Gaspreise, Gasspeicher |
| T12 | EU-Recht | Umsetzung der Strommarktreform 2024, REMIT II, Netzkodizes (Revision CACM, Electricity Balancing), Netzpaket der Kommission |
| T13 | Messwesen | Rolloutstand intelligenter Messsysteme, Preisobergrenzen, Pflichtfälle |
| T14 | Ablösung der Verordnungen | Ersatz von StromNZV, StromNEV und ARegV durch Festlegungen der BNetzA, Übergangsfristen |

Table: Bewegliche Themen für Welle 0

Quelle: Ausgangshypothese des Auftraggebers und Prüfliste des Vorprojekts (Stand 04.10.2026).

Ereignisse nach dem 04.10.2026 sind in Welle 0 gezielt zu suchen: Beschlüsse von Bundestag und Bundesrat (EEG 2027,
Netzanschlusspaket), Festlegungen der BNetzA (AgNes, Regelreserve, Marktkommunikation), Ergebnisse der
Ausschreibungen nach StromVKG, EEG und WindSeeG, Veröffentlichungen der ÜNB zu Umlagen und Netzentgelten des
Folgejahres (üblich bis Mitte Oktober bzw. Ende des Jahres) und Entscheidungen auf EU-Ebene.

## 12 Europa, Vergleichsmärkte und Kandidaten für Fallstudien

- **H-53 EU-Rahmen:** Binnenmarktrecht mit Verordnung (EU) 2019/943 und Richtlinie (EU) 2019/944, geändert durch die
  Reform des Strommarktdesigns 2024 (Verordnung (EU) 2024/1747, Richtlinie (EU) 2024/1711); Netzkodizes und
  Leitlinien (CACM, FCA, Electricity Balancing, System Operation); ACER-Methodiken. Prüfen: Fassungen und Fristen.
- **H-54 Vergleichsmärkte** (Vorschlag, in Phase 1 begründet festlegen): Großbritannien (eigenes Marktdesign nach
  dem Austritt aus der EU, Differenzverträge seit 2014, Kapazitätsmarkt, Entscheidung gegen regionale Preise),
  Frankreich (Kernenergie, Nachfolge der regulierten Kernstrom-Zuteilung ARENH, Kapazitätsmechanismus),
  Nordeuropa (Wasserkraft, mehrere Gebotszonen, Nord Pool). Ergänzend als Kontrast: Spanien/Portugal
  („iberische Ausnahme“ 2022) und Texas (ERCOT, Energy-only mit hohen Preisgrenzen). Prüfen.
- **H-55 Kandidaten für Fallstudien** (Tatsachen nur aus Primärquellen; Auswahl in Phase 1 begründen):
  - Energiekrise 2022: Gas- und Strompreise, Margining und Liquiditätshilfen, Notfallrecht, Strompreisbremse;
  - negative Preise und Solarspitzen 2023–2026, Solarspitzengesetz (B-03, B-16);
  - Dunkelflauten im Winter 2024/2025 mit Preisspitzen am Day-Ahead-Markt;
  - Entkopplung der SDAC im Juni 2024 (B-06);
  - Abschaltung der letzten Kernkraftwerke am 15.04.2023;
  - Ausschreibungsrunde für Windenergie auf See ohne Gebote (2025);
  - Großstörung auf der Iberischen Halbinsel am 28.04.2025 (Systemsicherheit, Spannungshaltung);
  - Streichung des Bundeszuschusses zu den Übertragungsnetzentgelten für 2024 nach dem Haushaltsurteil des
    Bundesverfassungsgerichts vom 15.11.2023.

## 13 Vorläufige Gliederung (Ausgangspunkt für Phase 1)

| Teil | Kapitel | Inhalt in Stichworten |
|---|---|---|
| I Grundlagen: Strom, System und Akteure | 1 Strom als Ware | Leistung und Energie, Gleichgewicht, Frequenz, Besonderheiten gegenüber anderen Rohstoffen, Marktkompass |
| | 2 Erzeugung, Verbrauch und Flexibilität | Technologien, Kosten, Lastprofile, Residuallast, Speicher, Sektorkopplung, Systemzahlen |
| | 3 Akteure, Rollen und Institutionen | Liberalisierung, Entflechtung, Marktrollen, Marktkommunikation, Behörden, EU-Ebene |
| II Großhandel | 4 Preisbildung und Merit Order | Grenzkosten, Pay-as-clear, Knappheit, negative Preise, Gas und CO₂, Spreads |
| | 5 Terminmarkt und Risikomanagement | Futures, Forwards, Optionen, Base und Peak, Clearing, Margining, Hedging |
| | 6 Day-Ahead-Markt und Marktkopplung | SDAC, Euphemia, Viertelstunde, Gebotsarten, Preisgrenzen, Entkopplung |
| | 7 Intraday-Handel | kontinuierlicher Handel, SIDC, Intraday-Auktionen, Prognosefehler, Viertelstunden |
| | 8 PPAs und Herkunftsnachweise | Vertragsarten, Profile, Risiken, Preisbildung, Herkunftsnachweise und Regionalnachweise |
| III Systembilanz und Systemsicherheit | 9 Bilanzkreise und Ausgleichsenergie | Bilanzkreissystem, Fahrpläne, MaBiS, reBAP, Anreize |
| | 10 Regelreserve | FCR, aFRR, mFRR, Plattformen, Präqualifikation, Preisregeln, Kosten |
| | 11 Engpassmanagement und Netzreserve | Redispatch 2.0, Countertrading, Netzreserve, Kosten und Wälzung |
| | 12 Systemdienstleistungen und Flexibilität | Momentanreserve, Blindleistung, Schwarzstart, § 13k, § 14a, § 14c |
| IV Versorgungssicherheit und Kapazität | 13 Versorgungssicherheit und Missing Money | Energy-only, Monitoring, Reserven, Investitionsanreize |
| | 14 Kapazitätsmärkte | StromVKG, Kraftwerksstrategie, EU-Rahmen, Vergleich mit Großbritannien, Frankreich, Italien |
| V Erneuerbare Energien und Förderung | 15 Das EEG: Logik und Finanzierung | Vergütung, Marktprämie, Marktwerte, EEG-Konto, Wegfall der Umlage |
| | 16 Ausschreibungen nach EEG und WindSeeG | Verfahren, Höchstwerte, Ergebnisse, Realisierung, Windenergie auf See |
| | 17 Direktvermarktung und negative Preise | Direktvermarkter, sonstige Direktvermarktung, § 51 EEG, Solarspitzengesetz |
| | 18 Differenzverträge, KWKG und Ausblick | EU-Strommarktreform, EEG 2027, KWKG, Biomasse |
| VI Das Netz | 19 Netzstruktur und Netzbetrieb | Ebenen, ÜNB und VNB, Interkonnektoren, HGÜ, Systemführung, Messwesen |
| | 20 Netzanschluss | Anschlusspflicht, Reifegradverfahren, Baukostenzuschuss, flexible Anschlüsse, Netzanschlusspaket |
| | 21 Netzentgelte und Regulierung | Anreizregulierung, Erlösobergrenzen, Entgeltbildung, Sonderformen, AgNes |
| | 22 Netzausbau und Gebotszone | NEP, Bundesbedarfsplan, Kosten, Gebotszonenüberprüfung, flussbasierte Kapazitätsberechnung |
| VII Endkundenmarkt | 23 Der Strompreis für Endkunden | Bestandteile, Umlagen, Steuern, Tarife, dynamische Tarife, Entlastungen |
| | 24 Vertrieb und Beschaffung | Lieferanten, Grundversorgung, Beschaffungsstrategien, Risiken, Industriebeschaffung |
| VIII Europa | 25 Europäischer Strombinnenmarkt und Vergleichsmärkte | EU-Recht, Netzkodizes, REMIT, Finanzmarktrecht, Vergleichsmärkte |
| IX Fallstudien | 26 Fallstudien | Energiekrise 2022, negative Preise, Dunkelflaute, R1–R6 im Zusammenhang |

Table: Vorläufige Gliederung

Quelle: Ausgangshypothese des Auftraggebers (vor Prüfung); entspricht den Teilen in `07_build/buch_config.yaml`.

## 14 Datenquellen (zu prüfen)

- **Preise und Mengen:** energy-charts.info (Fraunhofer ISE, mit API), SMARD (BNetzA, Download und API),
  netztransparenz.de (ÜNB: Marktwerte, reBAP, Umlagen, Hochrechnungen, Redispatch), regelleistung.net
  (Ausschreibungsergebnisse), EEX-Transparenzplattform und EEX-Marktdaten (Abrufbarkeit prüfen), EPEX SPOT
  (blockiert automatisierte Abrufe teilweise; dann über SMARD oder energy-charts belegen).
- **Europa:** ENTSO-E-Transparenzplattform (Webansicht; die API verlangt eine Registrierung, die nicht vorgenommen
  wird), ACER-Marktberichte, JAO (Kapazitäten der Region Core), Nord Pool.
- **Statistik und Monitoring:** Monitoringbericht von BNetzA und Bundeskartellamt, Marktstammdatenregister, AGEB,
  Destatis, BNetzA-Berichte zu Netz- und Systemsicherheit, Versorgungssicherheitsmonitoring, EEG-Statistik und
  Ausschreibungsergebnisse der BNetzA.
- **Recht:** gesetze-im-internet.de, recht.bund.de (Bundesgesetzblatt), dip.bundestag.de, eur-lex.europa.eu,
  Beschlussdatenbank der BNetzA, ACER-Entscheidungen.
- **Preise für Brennstoffe und CO₂:** EEX (Emissionsberechtigungen, Gas), DEHSt, ICE nur zur Einordnung.
- **Vorprojekt:** 150 geprüfte Quellen in `00_input/vorprojekt_bess/BESS_QUELLEN_Auswahl.csv`.

## 15 Offene Fragen an den Auftraggeber (für Phase 1)

1. Perspektive: eher Investor (Erzeugung, Speicher, Netz), eher Händler und Vertrieb oder eher Großverbraucher?
   Oder alle gleich gewichtet?
2. Tiefe der Physik und Technik: nur so viel, wie für Märkte nötig, oder mit eigenem Technikteil?
3. Vergleichsmärkte: Großbritannien, Frankreich und Nordeuropa oder andere (z. B. Italien als Anschluss an das
   Vorprojekt)?
4. Tiefe von Recht und Regulierung: Überblick mit Normen oder Prüfniveau mit Fallgruppen?
5. Werden die Modelle zusätzlich als Excel-Arbeitsmappen gebraucht?
6. Zielumfang (Seiten) und Zielgruppe einer möglichen Weitergabe des Buchs.
7. Gibt es eigene vertrauliche Unterlagen (U1 …), etwa Lieferverträge, PPAs oder Gutachten, und dürfen deren Zahlen
   im Buch erscheinen?
