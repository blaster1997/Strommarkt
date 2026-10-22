---
title: "Kapitel 12 · EEG, Umlagen, MiSpeL und Messkonzepte"
subtitle: "Ökonomie von Batteriespeichern in Deutschland"
date: "04.10.2026"
kopfzeile-rechts: "Kapitel 12 · Stand 27.09.2026"
kapitel-start: 12
nummerierung: kapitelweise
inhaltsverzeichnis: true
toc-tiefe: 2
deckblatt-hinweis: "Keine Rechts-, Steuer- oder Anlageberatung. Die MiSpeL ist nach der Festlegung vom 01.10.2026 dargestellt (Erratum)."
---

# EEG, Umlagen, MiSpeL und Messkonzepte

> [!NOTE]
> **Lernziele:** Nach diesem Kapitel können Sie
>
> - die Marktprämie, die förderfähige Speichereinspeisung und die umlagebefreite Netzentnahme eines Monats nach den Abgrenzungsformeln berechnen;
> - Speicheroptionen und Fallkonstellationen A1–A11 einem Projekt zuordnen und ihre Voraussetzungen prüfen;
> - die Folgen von Netzladung, MiSpeL-Übergang und EEG 2027 für die Konfigurationen A, A_inno, B und C bewerten;
> - ein Messkonzept für R3 entwerfen.

## Warum das für Investor und Fonds zählt {.unnumbered}

Ein Speicher neben einer geförderten Photovoltaikanlage (PV) verändert nicht nur die Erlöse, sondern auch Förderanspruch und Abgaben. Ob er aus dem Netz laden darf, ohne die Förderung zu gefährden, welche Umlagen auf den Ladestrom entfallen und wie grüner und grauer Strom im Speicher getrennt werden, regeln das Erneuerbare-Energien-Gesetz (EEG), das Energiefinanzierungsgesetz (EnFG) und die Festlegung der Bundesnetzagentur (BNetzA) zur Marktintegration von Speichern und Ladepunkten (MiSpeL). Die BNetzA hat sie am 01.10.2026 beschlossen, mit Übergangszeit bis 30.09.2027. Nach Auslegung der BNetzA kann eine einzige Netzladung einem Grünstromspeicher die Förderung des Speicherstroms für ein ganzes Kalenderjahr nehmen, ein ungünstig platzierter Zähler Umlageprivilegien kosten. Für einen Fonds, der Co-Location-Projekte erwirbt, gehören Förderstatus, gewählte Option und Messkonzept deshalb in jede Due Diligence (Prüfung vor dem Erwerb), zumal sich der Rahmen 2026/2027 ändert.

**Cashflow-Kompass:** Erlöse ● (Marktprämie für PV- und Speicherstrom, Arbitrage aus Netzladung) · Betriebskosten ● (Umlagen auf Netzbezug und Hilfsstrom, Messkosten) · Investitionen ○ (Zähler, Aufbau der Mittelspannung) · Steuern ○ (Stromsteuer, Kapitel 17) · Finanzierung ○ (Förderung als gesicherter Erlösanteil) · Fondsebene ○ (Regulierungsrisiko). **Werttreiber:** Höhe der Marktprämie, Zulässigkeit der Netzladung, Umlagebefreiung.

## EEG-Grundlagen: Marktprämie, Ausschreibungen, negative Preise und EEG 2027

Das EEG fördert Strom aus erneuerbaren Energien (EE), nicht den Speicher. Strom, den ein Speicher aus einer geförderten Anlage aufnimmt und später einspeist, kann aber förderfähig bleiben, in derselben Höhe wie ohne Zwischenspeicherung (§ 19 Abs. 3 EEG) [W2V-03]. Hauptfall des Kapitels ist deshalb R3: 15 MWp PV (12 MW Wechselstromleistung, A-011) und ein Speicher mit 10 MW und in der Basis 20 MWh nutzbar (D-025, A-054) in vier Varianten (Kapitel 14): ein Grünstromspeicher, der nur PV-Strom lädt (A), derselbe mit Zuschlag aus der Innovationsausschreibung (A_inno), PV und Speicher mit getrennten Netzanschlüssen (B, D-024) und ein Mischspeicher, der auch aus dem Netz lädt (C). A, A_inno und C teilen einen Netzverknüpfungspunkt (NVP). Standalone-Speicher wie R1 und R2 berührt das Kapitel nur bei den Umlagen.

### Marktprämie und Ausschreibungen

PV-Anlagen dieser Größe verkaufen ihren Strom am Markt, meist über einen Direktvermarkter, und erhalten vom Netzbetreiber zusätzlich eine gleitende Marktprämie (geförderte Direktvermarktung):

$$MP = \max\left(AW - JW;\;0\right)$$

$MP$ ist die Marktprämie, $AW$ der anzulegende Wert und $JW$ der Jahresmarktwert Solar, also der mit der Solareinspeisung gewichtete Börsenpreis eines Jahres (Kapitel 2), alle in €/MWh, nominal [K15M-01]. Anlagen mit Inbetriebnahme oder Zuschlag vor dem 01.01.2023 rechnen mit dem Monatsmarktwert, alle übrigen sowie alle mit Abgrenzungs- oder Pauschaloption (§ 19 Abs. 3b, 3c EEG) mit dem Jahresmarktwert (Anlage 1 Nr. 2 EEG) [K12R-13]. Gezahlt wird auf die förderfähige eingespeiste Menge. Liegt der Marktwert über dem anzulegenden Wert, fällt die Prämie auf null, ohne dass der Betreiber etwas zurückzahlt (A-005); das ändert erst der Entwurf des EEG 2027 (Abschnitt 12.1.4). Der Jahresmarktwert Solar betrug 2024 46,24 und 2025 45,08 €/MWh [VR3-29, K15M-01]; das „MW Solar(a)“ nach § 33 EEG 2012 (2025: 61,70 €/MWh) ist eine andere Größe [K15M-01].

Den anzulegenden Wert großer Solaranlagen bestimmt eine Ausschreibung der BNetzA. Im Gebotstermin 01.03.2026 für Solaranlagen des ersten Segments lagen die Zuschlagswerte bei 3,99–5,10 ct/kWh, im Mittel 4,94 ct/kWh, bei einem Höchstwert von 5,79 ct/kWh [WS-18]. R3 setzt den Mittelwert an: $AW$ = 49,4 €/MWh (A-003). Mit dem Jahresmarktwert 2025 ergäbe das 49,4 − 45,08 = 4,32 €/MWh Marktprämie. Einen Jahresmarktwert 2026 gibt es noch nicht; M1 schätzt den mit dem nationalen Solarprofil gewichteten Day-Ahead-Preis vom 01.01. bis 26.09.2026 auf 55,10 €/MWh, für 2025 mit derselben Rechnung auf 45,95 gegenüber amtlich 45,08 €/MWh [M1, Lauf 20260927-kapitel02]. Auf diesem Niveau entfiele die Marktprämie. Das Kapitel rechnet deshalb mit 45,08 €/MWh als Basis und 55,10 €/MWh als Sensitivität (A-059). *Einschätzung:* Bei Zuschlagswerten um 5 ct/kWh ist die Marktprämie klein und wirkt vor allem als Absicherung gegen schwache Solarjahre; die Förderfähigkeit des Speicherstroms ist heute wenig wert, mehr bei höheren anzulegenden Werten wie in der Innovationsausschreibung.

### Negative Preise: § 51 und § 51a EEG

Seit dem Solarspitzengesetz von 2025 sinkt der anzulegende Wert auf null, solange der Spotmarktpreis negativ ist (§ 51 Abs. 1 EEG) [W2V-01]. Spotmarktpreis ist der Preis der vortägigen Auktion von Viertelstundenkontrakten (§ 3 Nr. 42a EEG) [W2V-06]; eine Mindestdauer gibt es nicht. Für R3 entfällt die Marktprämie in jeder Viertelstunde mit negativem Day-Ahead-Preis. M1 zählt 2025 2.299 solcher Viertelstunden (bis 30.09.2025 Stundenprodukte, je vier Viertelstunden gerechnet) und vom 01.01. bis 26.09.2026 1.836 [M1, Lauf 20260927-kapitel06]. Von Monat zu Monat schwankt die Zahl stark, im Juli 2025 48, im Juli 2026 306 [M1D-01, eigene Auswertung]. Die Übertragungsnetzbetreiber (ÜNB) veröffentlichen, in welchen Viertelstunden der anzulegende Wert über null liegt; nur für Einspeisung in diesen „AW>0-Zeiten“ zahlt der Netzbetreiber die Marktprämie, und die MiSpeL bildet das in den Formeln (24)–(31) ab [K12R-18, Abschn. 2.1.7].

Zum Ausgleich verlängert § 51a EEG den Förderzeitraum. Bei Solaranlagen wird die Zahl der betroffenen Viertelstunden mit 0,5 multipliziert und als „Volllastviertelstunden“ an das Förderende angehängt; für Solaranlagen mit Inbetriebnahme vor dem 25.02.2025 gilt das nicht [W2V-02, W2V-05]. Eine Monatstabelle nennt, wie viele Volllastviertelstunden auf einen Monat der Verlängerung angerechnet werden, von 73 im Dezember bis 508 im Juni [W2V-02]. 600 negative Viertelstunden ergeben 300 Volllastviertelstunden; Januar und Februar rechnen nur 87 + 189 = 276 an, die Förderung verlängert sich bis Ende März (bei Ende des regulären Zeitraums am 31.12.) [VR3-30]. *Einschätzung:* Der Ausgleich fällt erst nach 20 Jahren an; bei rund 10 % Diskontsatz (A-024, Mid 10,25 %) ist ein Euro im 21. Jahr heute rund 0,13 € wert.

*Einschätzung:* In negativen Viertelstunden kostet PV-Einspeisung den negativen Preis und bringt keine Prämie; ein Speicher kann den Strom in förderfähige Viertelstunden verschieben (Abschnitt 12.4), ein Mischspeicher stattdessen bezahlt aus dem Netz laden (Kapitel 14).

> [!STAND]
> **Stand:** § 51 und § 51a EEG in der Fassung vom 27.09.2026 (EEG 2023, zuletzt geändert durch Gesetz vom 18.12.2025) [W2V-01, W2V-02]. Für Anlagen mit Inbetriebnahme oder Gebotstermin vom 01.01.2023 bis 24.02.2025 gilt die Fassung vom 24.02.2025 (§ 100 Abs. 46 EEG) [W2V-05], also eine Staffel nach der Dauer negativer Preise (4-3-2-1-Stunden-Regel) [VR3-30]. Frühere Jahrgänge haben eigene Regeln: 2021–2022 eine Vier-Stunden-Regel, 2016–2020 eine Sechs-Stunden-Regel ohne Verlängerung, bis 2015 keine Kürzung [VR3-30, Folie 10]. Das zählt, wenn ein Fonds Speicher an Bestands-PV nachrüstet. Anlagen vor dem 25.02.2025 können freiwillig in die neue Regel wechseln und erhalten dann 0,6 ct/kWh mehr anzulegenden Wert (§ 100 Abs. 47 EEG) [W2V-05], frühestens zum Ende des Jahres, in dem ein intelligentes Messsystem eingebaut wird, und unter Beihilfevorbehalt (§ 101 Abs. 1 EEG) [VR3-30, Folie 11]. Der Entwurf des EEG 2027 setzt das Ende der Vergütung bei negativen Preisen fort [K12R-05, S. 2–3]. Vor Verwendung prüfen.

### Innovationsausschreibung und Anlagenkombination

Die Innovationsausschreibung fördert unter anderem Anlagenkombinationen aus erneuerbaren Anlagen und Speichern an einem gemeinsamen NVP (§ 2 Nr. 1 Buchst. b der Innovationsausschreibungsverordnung, InnAusV) [K12R-02; VR3-26]. Im Gebotstermin 01.05.2026 wurden 475 MW ausgeschrieben und 27 Gebote über 482,4 MW bezuschlagt, zu 4,75–5,61 ct/kWh, mengengewichtet 5,34 ct/kWh, bei einem Höchstwert von 7,13 ct/kWh (bekanntgegeben am 25.06.2026) [VR3-23]. R3 rechnet in Variante A_inno mit 53,4 €/MWh (A-004).

Der höhere anzulegende Wert hat Bedingungen [W2V-08]. Nach § 13 Abs. 4 InnAusV ist „der zwischengespeicherte Strom ausschließlich in den anderen Anlagenteilen zu erzeugen“, und zwar während der gesamten Zahlungsdauer (Abs. 5 in Verbindung mit § 2 Nr. 1 Buchst. b); der Speicher darf nie aus dem Netz laden. Nach Abs. 2 Satz 1 Nr. 1 entfällt die Marktprämie, wenn die installierte Leistung des Speichers nicht mindestens 25 % der Gesamtleistung der Kombination entspricht „und“ seine Kapazität nicht mindestens eine „Einspeicherung von zwei Stunden der Arbeit der Nennleistung“ ermöglicht; ein Umweltgutachter weist das jährlich nach (Satz 2). Maßgeblich ist die Ladeseite: Ein Speicher mit 10 MW und 20 MWh nutzbar nimmt am NVP rund 21,4 MWh auf (20/√0,87, D-021, A-M1-01), rund 2,1 Stunden Nennleistung; auch die 25 % hält R3 mit 10 MW neben 15 MWp PV ein (rund 40 %, eigene Rechnung). Offen ist, ob die Verordnung den NVP oder die Batterie meint; bezieht man die zwei Stunden auf die Batterie, liegen 20 MWh nutzbar genau an der Grenze. Offen ist auch, ob die Prämie nach dem Wortlaut erst entfällt, wenn beide Mindestgrößen verfehlt sind. *Einschätzung:* Der Puffer ist klein; weil der Umweltgutachter die Mindestgrößen jährlich prüft, kann die Alterung des Speichers (Kapitel 9) ihn aufzehren.

Ein Zuschlag erlischt, wenn die Anlage nicht binnen 30 Monaten nach öffentlicher Bekanntgabe des Zuschlags in Betrieb geht (Abs. 1); werden mehr als 5 % der Gebotsmenge entwertet, fällt eine Pönale von 60 €/kW an (Abs. 3). Außerdem schließt die MiSpeL Anlagenkombinationen mit Speicher nach der InnAusV von der Abgrenzungsoption aus [K12R-18, Abschn. 3.1.1 Nr. 6]: A_inno kann nicht zum Mischspeicher werden.

> [!STAND]
> **Stand:** InnAusV in der Fassung vom 27.09.2026 (zuletzt geändert durch Gesetz vom 21.02.2025) [W2V-08]; letzte belegte Runde am 01.05.2026 [VR3-23]. Nach dem Regierungsentwurf des EEG 2027 entfallen die Innovationsausschreibungen: § 39n EEG wird durch Resilienzausschreibungen nach Art. 26 der EU-Netto-Null-Industrie-Verordnung (NZIA) ersetzt, und die InnAusV tritt am 01.01.2027 statt am 31.12.2028 außer Kraft [W2V-17]. Die Begründung nennt das „strenge Ausschließlichkeitsprinzip für zugebaute Speicher“ einen Fehlanreiz [W2V-17, S. 213, 256]. Bestehende Zuschläge blieben im bisherigen EEG (Abschnitt „EEG 2027“); ob die InnAusV-Pflichten fortgelten, ist offen. Vor Verwendung prüfen.

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Anlagenkombination nach InnAusV. Vor dem Erwerb eines Projekts mit Innovationszuschlag sollte ein Rechtsanwalt für Energierecht klären, auf welchen Bezugspunkt sich die Mindestgrößen nach § 13 Abs. 2 InnAusV beziehen, wie das „und“ zu lesen ist und ob die Mindestdauer auch nach Alterung des Speichers erreicht sein muss; welche Folge ein Verstoß gegen das Netzladeverbot nach Abs. 4 hat, etwa durch Hilfsstrom oder negative Regelreserve, wobei die Marktprämie der ganzen Kombination betroffen sein kann; und wie bestehende Zuschläge übergeleitet werden, wenn die InnAusV nach dem Entwurf des EEG 2027 am 01.01.2027 außer Kraft tritt.

### EEG 2027: Differenzvertrag und Refinanzierungsbeitrag

Die Bundesregierung hat am 07.09.2026 den Entwurf eines neuen EEG vorgelegt (Bundestagsdrucksache, BT-Drs. 21/7867), das am 01.01.2027 in Kraft treten soll [W2V-17]. Kern ist ein zweiseitiger Differenzvertrag (Contract for Difference, CfD) für Anlagen ab 100 kW außer Biomasse. Er ergänzt die Marktprämie um einen Refinanzierungsbeitrag [W2V-17, S. 4]. Nach § 21d Abs. 1 des Entwurfs zahlt ihn der Betreiber einer Anlage mit wirksamem Zuschlag auf jede erzeugte und eingespeiste Kilowattstunde, wenn der Jahresmarktwert eines Kalenderjahres über dem anzulegenden Wert liegt. Das gilt auch für Strom, den er in der sonstigen Direktvermarktung verkauft, etwa über einen Liefervertrag (Power Purchase Agreement, PPA) [W2V-17, S. 23–24]. Über § 19 Abs. 3–3b gilt das auch für zwischengespeicherte Mengen [W2V-17, S. 180]. Befreit ist nach § 21e nur, wer dauerhaft auf die Marktprämie verzichtet; die Erklärung in Textform wirkt ab dem 1. Januar des Folgejahres und ist nur einmal möglich, spätestens bis zum Ablauf des zehnten Kalenderjahres nach Inbetriebnahme [W2V-17, S. 23–24]. Wer nur in Jahren mit hohem Marktwert in einen PPA wechselt, entgeht dem Beitrag nicht. Die Höhe regelt Anlage 1 Nr. 4: die volle Differenz, gemindert in Viertelstunden mit niedrigem Spotpreis [W2V-17, S. 65]. Ohne diese Minderung (A-060, Obergrenze) gilt

$$Z = \left(AW - JW\right)\cdot F$$

mit der Zahlung $Z$ des Netzbetreibers in € (negativ: Refinanzierungsbeitrag des Betreibers) und der Bemessungsmenge $F$ in MWh. Der Wortlaut nennt jede eingespeiste Kilowattstunde; ob beim Mischspeicher nur der förderfähige Anteil zählt, ist offen. Mit $AW$ = 49,4 €/MWh und einem Jahresmarktwert von 55,10 €/MWh zahlte eine Anlage mit Gebotstermin ab 2027 bis zu 5,70 €/MWh zurück, statt wie heute null zu erhalten. R3 und A_inno (Gebotstermine 2026) blieben im bisherigen Recht (§ 100 Abs. 1 Nr. 1 Buchst. b) [W2V-17, S. 61, 243]. *Einschätzung:* Weil Prämie und Beitrag am Jahresmarktwert hängen und nicht am Erlös der einzelnen Anlage, bleibt der Anreiz erhalten, PV-Strom mit dem Speicher in teure Stunden zu verschieben; die Minderung nach Nr. 4.2 schwächt ihn ab.

> [!STAND]
> **Stand:** Regierungsentwurf BT-Drs. 21/7867 vom 07.09.2026 (Vorabfassung), erste Lesung am 24.09.2026 [W0R-15, W2V-17]; geplantes Inkrafttreten 01.01.2027 [W2V-17]. Für den 05.10.2026 ist eine öffentliche Anhörung im Ausschuss für Wirtschaft und Energie angesetzt [K12R-12]. Gelesen sind Vorblatt, §§ 19, 21d, 21e, 100, Anlage 1 Nr. 4 und Teile der Begründung. Offen sind Beschluss, beihilferechtliche Genehmigung, § 21 EnFG und die Fortgeltung der InnAusV-Pflichten. Vor Verwendung prüfen.

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Differenzvertrag und Speicherstrom. Ein Rechtsanwalt für Energierecht sollte klären, worauf sich der Refinanzierungsbeitrag nach § 21d EEG 2027 (Entwurf) bei der Abgrenzungsoption bemisst, ob ein Wechsel in die sonstige Direktvermarktung oder ein dauerhafter Verzicht nach § 21e für das Projekt sinnvoll ist, ob Ausschließlichkeits- und Abgrenzungsoption unverändert bleiben, wie negative Preise im Differenzvertrag behandelt werden und ob Übergangsregel und InnAusV-Pflichten für Zuschläge vor 2027 so bleiben.

## Umlagen und Speicherprivilegien nach dem EnFG

### Umlagebefreiung nach § 21 EnFG

Eine EEG-Umlage gibt es seit 2023 nicht mehr; den Saldo des EEG-Kontos gleicht der Bund aus (§ 6 Abs. 1 EnFG) [K12R-16], seit 01.01.2025 aus dem Kernhaushalt [K12R-05, S. 6]. Die Privilegien für Speicher betreffen deshalb die Umlagen nach dem EnFG auf Netzentnahmen, also KWKG-Umlage und Offshore-Netzumlage (§ 2 Nr. 7 EnFG) [K12R-16], 2026 0,446 bzw. 0,941 ct/kWh, zusammen 13,87 €/MWh [K12R-07, K12R-08]. Hinzu kommt der Aufschlag für besondere Netznutzung, früher § 19-StromNEV-Umlage: 2026 1,559 ct/kWh auf die ersten 1.000 MWh je Abnahmestelle und 0,050 ct/kWh darüber; über § 19 Abs. 2 Satz 16 StromNEV sind die nach § 21 EnFG privilegierten Mengen frei [K12R-09; K12R-17, S. 22–23].

§ 21 EnFG regelt drei Dinge [W2V-09]. Erstens entfällt die Umlage auf Netzentnahmen zur Zwischenspeicherung in dem Umfang, in dem der Speicher im selben Kalenderjahr Strom ins Netz einspeist; bei Strommengen mit unterschiedlich hoher Umlagepflicht gilt das im Verhältnis der Verbrauchsmengen (Abs. 1) [K12R-04]. Zweitens sind Speicherverluste umlagefrei, soweit die gespeicherte Energie nicht wieder entnommen wird (Abs. 2). Drittens werden die Mengen je 15-Minuten-Intervall als niedrigerer Wert ermittelt, kurz Minimumregel (Abs. 4 Satz 3 und 4):

$$N_q = \min\left(B_q;\;L_q\right), \qquad E^{\text{Sp}}_q = \min\left(E_q;\;S_q\right)$$

$q$ bezeichnet eine Viertelstunde, $B_q$ und $E_q$ den Netzbezug und die Netzeinspeisung am NVP, $L_q$ den Stromverbrauch (Ladung) und $S_q$ die Stromerzeugung (Entladung) des Speichers, alle in MWh. $N_q$ ist die Ladung, die als Netzstrom gilt, $E^{\text{Sp}}_q$ die Einspeisung, die als Speicherstrom gilt. Eine ausdrückliche Vorrangregel enthält § 21 EnFG nicht; die Zuordnung folgt aus dem Minimum je Viertelstunde, die Befreiung aus der Jahresbilanz [W2V-09]. Die MiSpeL nennt diese Zuordnung „Speichervorrang“ und rechnet ein Beispiel: Lädt der Speicher in einer Viertelstunde 100 kWh, während die Anlage 130 kWh aus dem Netz bezieht und die PV 50 kWh erzeugt, gelten nach der Minimumregel alle 100 kWh als Netzstrom [K12R-18, Abschn. 2.1.5]. PV-Strom zählt nur als grüne Ladung, soweit der Netzbezug derselben Viertelstunde unter der Ladung liegt, gleich welcher Verbraucher ihn auslöst. Mess- und eichrechtskonform erfasst oder abgegrenzt werden müssen die Mengen in jedem Fall, viertelstündlich gemessen nur, wenn das Minimum nicht anders sichergestellt ist (Abs. 4) [W2V-09]; die Mengen sind bis 31. Mai mitzuteilen (Abs. 7) [K12R-04].

Nach Wirksamwerden der MiSpeL lassen sich die Privilegien nach § 21 Abs. 1–4 EnFG nur nach deren Anlage 1 in Anspruch nehmen, auch für Standalone-Speicher [K12R-17, S. 1–2]. Im Übergang bis 30.09.2027 gilt Anlage 1 nur im Einverständnis mit Netz- und Messstellenbetreiber (Tenorziffer, TZ 9a) [K12R-17, S. 3], sonst bleibt es bei § 21 EnFG in der bisherigen Anwendung (*Einschätzung*). Für einen rein netzgekoppelten Speicher ohne sonstigen Verbrauch (Fall A10) ist der umlagebelastete Netzbezug null [K12R-18, S. 96–97]. Sonstiger Verbrauch ist der Verbrauch anderer Geräte als Speicher und bidirektionaler Ladepunkte hinter dem Netzanschluss; Hilfsverbräuche, die ausschließlich dem Speicher dienen, etwa seine Kühlung, darf der Betreiber als Speicherverbrauch erfassen [K12R-18, S. 25; K12R-17, S. 34] (Abschnitt 12.4.2).

### Stromsteuer, Netzentgelte und Herkunftsnachweise

Die Stromsteuer behandelt Kapitel 17: Zurückgespeister Ladestrom von Speichern, die im Marktstammdatenregister (MaStR) registriert sind, ist nicht belastet (§ 5 Abs. 4 Stromsteuergesetz, StromStG) [K17R-01]; offen sind die Steuer auf Umwandlungsverluste und die Entlastung des Hilfsstroms (A-047). Die MiSpeL regelt die Stromsteuer nicht; § 11a Abs. 3 der Stromsteuer-Durchführungsverordnung verweist auf § 21 EnFG [K12R-17, S. 22].

Netzentgelte behandelt Kapitel 11. § 118 Abs. 6 Satz 3 EnWG befreit Speicher nur, „soweit“ sie den entnommenen Strom zeitlich verzögert zurückspeisen, und erklärt § 21 EnFG für entsprechend anwendbar [SYN-03]. Die Zuordnung nach Anlage 1 wirkt damit nach Verständnis der BNetzA mittelbar auch auf die Netzentgeltbefreiung und den Aufschlag für besondere Netznutzung [K12R-17, S. 22–23]. Die neue Netzentgeltsystematik (AgNes) kann das ablösen (Stand 27.09.2026; AgNes-Entwurf vom 06.08.2026, Kapitel 11) [W0R-01; K12R-17, S. 23].

Ob für zwischengespeicherten PV-Strom Herkunftsnachweise (Registereinträge über die Herkunft von EE-Strom) entstehen, ist hier nicht recherchiert; vor einer Grünstromvermarktung beim Register des Umweltbundesamts klären.

## Ausschließlichkeits-, Abgrenzungs- und Pauschaloption

Für zwischengespeicherten Strom kann der Betreiber den Förderanspruch über eine von drei Optionen geltend machen, an einer Einspeisestelle mit mehreren Speichern nur einheitlich über eine (§ 19 Abs. 3 EEG) [W2V-03]. Einspeisestelle ist der Punkt, über den die Anlagen hinter einem Anschluss ins Netz einspeisen, bei R3 der gemeinsame NVP.

| Merkmal | Ausschließlichkeitsoption (§ 19 Abs. 3a) | Abgrenzungsoption (§ 19 Abs. 3b) | Pauschaloption (§ 19 Abs. 3c) | Alternative ohne Speicherförderung |
|---|---|---|---|---|
| Voraussetzung | im Kalenderjahr ausschließlich EE-Strom (oder Grubengas) eingespeichert | förderfähiger Anteil nach Festlegung der BNetzA (MiSpeL, Anlage 1) | nur Solaranlagen und Speicher desselben Betreibers, Solar höchstens 30 kW | Speicher entlädt nicht, während eingespeist wird |
| Netzladung | nein; sonst nach BNetzA Förderverlust im Kalenderjahr | ja | ja | ja |
| Geförderter Speicherstrom | gesamte Speichereinspeisung in AW>0-Zeiten | Wirkungsgrad × PV-Ladung in AW>0-Zeiten | gesamte Einspeisung an der Einspeisestelle, höchstens 500 kWh je kW Solarleistung und Jahr | keiner |
| Umlageprivileg (§ 21 EnFG) | ausgeschlossen | nach Anlage 1 | nach § 21 Abs. 4a EnFG (Anlage 2) | keines |
| Anwendbar | geltendes Recht | ab Bekanntgabe (TZ 8), bis 30.09.2027 nur mit Einverständnis von NB und MSB (TZ 9a) | frühestens ab Monatserstem nach EU-Beihilfegenehmigung (TZ 9b) | geltendes Recht (Auslegung der BNetzA) |
| R3 | Variante A | Variante C | ohne Bedeutung | Rückfall für C im Übergang |

Table: Optionen für zwischengespeicherten Strom

Quelle: § 19 Abs. 3–3c und § 100 Abs. 34 EEG [W2V-03, W2V-05]; MiSpeL-Festlegung vom 01.10.2026, Tenor TZ 8, 9a, 9b (S. 2–3), und Anlage 1, S. 11–13 [K12R-17, K12R-18]; NB = Netzbetreiber, MSB = Messstellenbetreiber (Stand 01.10.2026).

Den förderfähigen Anteil der Abgrenzungsoption bestimmt die MiSpeL als Festlegung nach § 85d EEG [K12R-03]. Für R1–R4 und die Anlage aus dem Erlösgutachten G1 (anonymisiert) ist die Pauschaloption ohne Bedeutung [W2V-03; K12R-17, S. 71–72]. Abgrenzungs- und Pauschaloption sind erst anzuwenden, „wenn und soweit“ die Festlegungen nach § 85d wirksam werden (§ 100 Abs. 34 EEG) [W2V-03, W2V-05].

Die letzte Spalte zeigt die „Alternative zur Ausschließlichkeitsoption“ der BNetzA: Netzladung ist erlaubt, gefördert wird aber nur die Einspeisung direkt aus der EE-Anlage [K12R-18, S. 11–12]. Arbitrage mit Umlageprivileg erlauben nur Abgrenzungs- und Pauschaloption (Übersicht 2 der Anlage 1) [K12R-18, S. 13].

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Hilfsstrom unter der Ausschließlichkeitsoption. Die BNetzA sichert die Ausschließlichkeit, indem im Speicher nichts verbraucht wird, während Netzbezug besteht, und rechnet zeitgleichen Netzbezug an Z1 vorrangig dem Speicher zu [K12R-18, S. 11, 14–15]. Ein eigener Hilfsstromzähler hinter Z1 schützt deshalb nicht: Zieht der Hilfsstrom in einer Ladeviertelstunde Netzstrom, etwa weil eine Wolke die PV-Leistung drückt, entfällt die Förderung des Speicherstroms für das Kalenderjahr; liegt er hinter dem Speicherzähler, genügt jeder zeitgleiche Netzbezug. Schutz bieten nur eine eigene Entnahmestelle für den Hilfsstrom oder eine Steuerung, die Ladeleistung plus Hilfsstrom in jeder Ladeviertelstunde unter der PV-Leistung hält. Ob zeitgleicher Netzbezug für Hilfsstrom als Einspeicherung von Netzstrom gilt, sollten ein Rechtsanwalt für Energierecht und der Messstellenbetreiber vor Baubeginn klären. Umlageprivilegien, auch für Hilfsstrom als Speicherverbrauch, gibt es unter dieser Option nicht [K12R-18, S. 11].

## MiSpeL: Status, Fallkonstellationen und Formeln

Die MiSpeL-Festlegung der BNetzA (Az. 618-25-02) konkretisiert Regeln aus EEG und EnFG: den förderfähigen Anteil der Speichereinspeisung nach § 19 Abs. 3b EEG und die Umlageprivilegien nach § 21 Abs. 1–4 EnFG (Anlage 1, Abgrenzungsoption) sowie die Pauschaloption (Anlage 2) [K12R-17, S. 1–2; K12R-19]. Nach einer Konsultation von Eckpunkten ab 18.09.2025 folgte am 05.08.2026 ohne erneute Konsultation ein Arbeitsstand [K12R-01, W2V-18], am 01.10.2026 der Beschluss [K12R-17, K12R-20].

> [!STAND]
> **Stand:** Die am 01.10.2026 beschlossene MiSpeL wirkt ab Bekanntgabe (TZ 8); veröffentlicht wurde sie am 01.10.2026 auf der Verfahrensseite, im Amtsblatt der BNetzA angekündigt für 07.10.2026 [K12R-17, S. 2, 7]. Bis 30.09.2027 gilt sie nur im Einverständnis von Netz- und Messstellenbetreiber (TZ 9a), die Pauschaloption frühestens ab dem Monatsersten nach der beihilferechtlichen Genehmigung (TZ 9b) [K12R-17, S. 3]. Gegenüber dem Arbeitsstand vom 05.08.2026 sind Fallkonstellationen für Speicher, Formelsatz, Monatssaldierung, der pauschale Wirkungsgrad von 0,85 und die Auslegung zur Netzladung unter der Ausschließlichkeitsoption unverändert [K12R-02, K12R-18]. Neu sind die Abgrenzung des Speicherverbrauchs (Anlage 1, Abschn. 3.2.4), Aussagen der Begründung zur gleichstromseitigen Kopplung und der Einschub „im Rahmen ihrer energiewirtschaftlichen Aufgaben“, der die Mitwirkungspflicht von Netz- und Messstellenbetreiber begrenzt (TZ 7) [K12R-17, S. 2, 91]. Beschwerden haben keine aufschiebende Wirkung [K12R-17, S. 94]. Offen sind der Tag der Bekanntgabe, die Umsetzung in der Marktkommunikation und die Ergebnisse des Workshops vom 02.10.2026. Vor Verwendung prüfen.

### Voraussetzungen der Abgrenzungsoption

„EE-Anlage“ umfasst keine reinen Speicher; mehrere Solaranlagen hinter derselben Einspeisestelle gelten als eine EE-Anlage, wenn sie einen anzulegenden Wert und einheitliche AW>0-Zeiten haben. „Stromspeicher“ erfasst ausdrücklich auch Mischspeicher, die im Kalenderjahr auch Netzstrom einspeichern [K12R-18, S. 7–8].

Mit geförderter EE-Anlage verlangt Anlage 1 acht Voraussetzungen [K12R-18, Abschn. 3.1.1]. (1) Alle EE-Anlagen, Speicher und Ladepunkte hinter der Einspeisestelle sind in der Direktvermarktung. Mindestens eine EE-Anlage erhält die Marktprämie über die Abgrenzungsoption, weitere dürfen ungefördert direkt vermarktet werden (sonstige Direktvermarktung). Abnahme durch den Netzbetreiber, Einspeisevergütung und Mieterstromzuschlag sind ausgeschlossen. (2, 3) Netzeinspeisung und Netzbezug an der Stelle laufen vollständig über Anlage 1; Pauschal- und Ausschließlichkeitsoption sind dort ausgeschlossen. (4) Die gesamte Einspeisung wird „in einem gesonderten Bilanzkreis oder Unterbilanzkreis“ bilanziert, in der Regel beim Direktvermarkter (Bilanzkreis: Kapitel 2). (5) Die Marktprämie wird mit dem Jahresmarktwert berechnet. (6) Hinter der Einspeisestelle liegt keine nach InnAusV geförderte Kombination mit Speicher. (7) Die Option steht Neu- und Bestandsanlagen offen, (8) ab Wirksamwerden der Festlegung. Gibt es keine geförderte EE-Anlage, etwa weil die PV ihren Strom ungefördert über einen PPA verkauft, gelten die Voraussetzungen 4–6 nicht und die Formelsätze nur für die Umlageprivilegien [K12R-17, S. 1, TZ 1; K12R-18, Abschn. 3.1.2, 10.1].

### Fallkonstellationen A1–A11

Anlage 1 unterscheidet elf Fallkonstellationen nach den Anlagen hinter der Einspeise- und Entnahmestelle. Z1 ist der Zweirichtungszähler an dieser Stelle, also ein Zähler, der Bezug und Einspeisung getrennt erfasst, Z2 der Zähler am Speicher oder Ladepunkt [K12R-18, Übersicht 1].

| Fall | Konstellation | Sonstiger Verbrauch | Zähler | Bezug im Buch |
|---|---|---|---|---|
| A1 | geförderte EE-Anlage und Speicher | mit oder ohne | Z1, Z2 | R3 Variante C (Regelfall) |
| A2–A4 | Ladepunkt: bidirektional an der EE-Anlage (A2) oder mit Speicher, vereinfacht (A3) bzw. mit gesondert gemessenen Speicherverlusten (A4) | mit oder ohne | Z1, Z2; A4 mit Z3 | – |
| A5 | mehrere gleichartige EE-Anlagen mit gemeinsamer Messung (§ 24 Abs. 3 EEG) und Speicher | mit oder ohne | Z1, Z2 | PV-Anlagen mit unterschiedlichem anzulegendem Wert, z. B. Bauabschnitte mit eigenen Zuschlägen |
| A6 | zusätzlich verschiedenartige Erzeugung, z. B. Solar und Wind | mit oder ohne | Z1, Z2, Z4 | Hybridpark am geteilten Anschluss |
| A7 | separat belieferte Wärmepumpe | mit oder ohne | Z1, Z2, ZW | – |
| A8 | Speicher in Co-Location mit EE-Anlage, vereinfacht | ohne | nur Z1 | R3 Variante C ohne Speicherzähler |
| A9 | unterschiedlich umlagepflichtige Netzbezüge, z. B. Besondere Ausgleichsregelung | mit | Z1, Z2 | Speicher beim Industriekunden |
| A10 | rein netzgekoppelter Speicher, vereinfacht | ohne | nur Z1 | R1, R2, G1, B ohne sonstigen Verbrauch, auch mit Hilfsstrom als Speicherverbrauch |
| A11 | Speicher oder Ladepunkt ohne Erzeugung, vereinfacht | beim Speicher mit | nur Z1; keine privilegierten Speicherverluste | R1, R2, G1, B mit sonstigem Verbrauch an der Entnahmestelle |

Table: Fallkonstellationen der Abgrenzungsoption

Quelle: MiSpeL-Festlegung vom 01.10.2026, Anlage 1, Übersicht 1 (S. 9), Übersicht 4 (S. 90), Fn. 1 (S. 7), Abschn. 3.2.4 (S. 25), 8 (S. 72–75), 10.2 und 10.3 (S. 94–102) [K12R-18]; Abschn. 5 (Arbeitsstand, S. 40–41) [W0R-06]; bei A5–A7 und A9 kommt bei Kombination mit A4 Z3 hinzu (Stand 01.10.2026).

A8, A10 und A11 sind vereinfachte Alternativen zu A1 mit nur einem Zähler. In A8 gilt der gesamte Netzbezug als umlagereduzierend; förderfähig ist die Einspeisung abzüglich des Netzbezugs, anteilig gekürzt, was etwas weniger Förderung ergibt als A1 [K12R-18, S. 72–75]. In A10 ist der gesamte Netzbezug umlagebefreit [K12R-18, S. 96–97]. Beide setzen voraus, dass es keinen sonstigen Verbrauch gibt, weil Z1 allein nicht trennt, ob Netzbezug in den Speicher oder zu anderen Verbrauchern fließt; beide rechnen ihn ganz dem Speicher zu [K12R-18, S. 97, 99]. Gibt es ihn, braucht die Co-Location den Speicherzähler Z2 (A1); ein Speicher ohne Erzeugung wählt zwischen A1 und A11. A11 befreit den Netzbezug nur bis zur Höhe der Netzeinspeisung und kennt keine privilegierten Speicherverluste: Umlagebelastet bleiben der sonstige Verbrauch und alle Speicherverluste, bei 87 % Wirkungsgrad rund 13 % der Ladung [K12R-18, S. 100–101]. In A1 sind die Verluste dagegen anteilig privilegiert. Ein Standalone-Speicher wie R1 kann A10 ohne Umlagen erreichen, auch mit Hilfsstrom über dieselbe Entnahmestelle, wenn dieser nur dem Speicher dient und als Speicherverbrauch erfasst wird [K12R-18, S. 25, 96–99; K12R-17, S. 34] (Nachweis und Unterzähler offen, Kasten in 12.5); A11 gilt nur bei sonstigem Verbrauch, etwa wenn Hilfsverbräuche auch anderen Zwecken dienen oder als sonstiger Verbrauch erfasst sind. Unter A11 wären bei R1 rund 720 MWh Verluste im Jahr 2028 umlagebelastet, mit den Zyklen aus M1 [M2, Lauf M2-20260928-P04; Rechenbeispiel 11.3], bei 365 Vollzyklen rund 1.000 MWh (13 % von rund 7.800 MWh Ladung, A-052). *Eigene Schätzung:* Das kostet 10–14 k€/a KWKG- und Offshore-Netzumlage und 11–13 k€/a Aufschlag für besondere Netznutzung, weil die Verluste neben dem Hilfsstrom (196 MWh) überwiegend in die erste GWh zu 15,59 €/MWh fallen; zusammen rund 21–27 k€/a (Preisstand 2026), dazu gegebenenfalls Netzentgelte (Kapitel 11).

### Formelsatz

Für die Basisfälle A1–A4 enthält Anlage 1 einen Formelsatz mit 33 Größen. Die Tabelle fasst ihn zusammen; die Nummern folgen der Anlage.

| Nr. | Größe | Rechenregel | Zweck |
|---|---|---|---|
| (1), (2) | Netzladung und Speichereinspeisung je Viertelstunde | MIN[Z1-Bezug; Z2-Verbrauch]; MIN[Z1-Einspeisung; Z2-Erzeugung] | Minimum nach § 21 Abs. 4 EnFG |
| (3)–(6) | Monatssummen | Netzbezug, Netzeinspeisung (Z1); Speicherverbrauch, Speichererzeugung (Z2) | Messwerte |
| (9), (10) | Netzstrom und EE-Strom im Speicher | Σ(1); (5) − (9) | grüne Ladung |
| (11)–(13) | Speichereinspeisung, Fremdtankstrom, berücksichtigungsfähige Speichereinspeisung | Σ(2); MAX[(6) − (5); 0]; MAX[(11) − (12); 0] | (12) vor allem bei Ladepunkten |
| (14), (15) | Wirkungsgrad, EE-Speichererzeugung | A1: (6)/(5), A2–A4: 0,85; (14) × (10) | grüne Entladung |
| (16) | saldierungsfähige Netzeinspeisung | MAX[(13) − (15); 0] | zurückgespeister Netzstrom |
| (17)–(19) | Speicherverluste, Anteil, privilegierte Verluste | MAX[(5) − (6); 0]; (16)/(6); (18) × (17) | nur A1 und A4 |
| (20)–(22) | umlagereduzierende Menge, umlagebelasteter Netzbezug | MIN[(16) + (19); (3)]; (3) − (20); Jahressumme | Umlagen |
| (23)–(26) | förderfähige Einspeisung direkt aus der EE-Anlage | Summe der Z1-Einspeisung minus (2) in AW>0-Zeiten | Förderung PV |
| (27)–(31) | förderfähige EE-Speichereinspeisung | Anteil der Speichereinspeisung in AW>0-Zeiten × MIN[(13); (15)] | Förderung Speicher |
| (32), (33) | förderfähige Netzeinspeisung | (26) + (31); Jahressumme | Summe |

Table: Formelübersicht der Basisfälle A1–A4

Quelle: MiSpeL-Festlegung vom 01.10.2026, Anlage 1, Abschn. 4.2–4.4, S. 32–40 [K12R-18]; (7) und (8) betreffen nur A4 (Stand 01.10.2026).

Für R3 zählen die Förder- und Umlageformeln des Falls A1, gerechnet je Kalendermonat. Förderfähig ist zum einen die Einspeisung direkt aus der EE-Anlage in AW>0-Zeiten, also die Netzeinspeisung an Z1 abzüglich der Speichereinspeisung nach der Minimumregel (23–26). Zum anderen ist die Speichereinspeisung förderfähig, aber höchstens in Höhe der grünen Entladung (15), also gemessener Wirkungsgrad des Monats (14) × EE-Strom im Speicher (10), und nur mit dem Anteil, den der Speicher in AW>0-Zeiten einspeist (27–31). Das gilt für einen Speicher ohne Ladepunkt, sofern der Fremdtankstrom (12) null ist, die Entladung des Monats also die Ladung nicht übersteigt. Die Summe ist die förderfähige Netzeinspeisung des Monats (32). Wann geladen wurde, spielt keine Rolle: Auch PV-Strom aus einer negativen Viertelstunde wird förderfähig, wenn der Speicher ihn später in AW>0-Zeiten einspeist.

Für die Umlagen gilt die Kette (16)–(21). Umlagebefreit ist zunächst der zurückgespeiste Netzstrom, die saldierungsfähige Netzeinspeisung (16): Speichereinspeisung abzüglich grüner Entladung. Hinzu kommen die privilegierten Speicherverluste (19), die dem Anteil dieses Netzstroms an der Entladung folgen. Befreit ist beides zusammen, höchstens aber der Netzbezug (20); der Rest des Netzbezugs bleibt umlagebelastet (21).

### Monatssaldierung und Jahresabrechnung

Anlage 1 rechnet mit Viertelstundenwerten, ordnet und saldiert aber je Kalendermonat („kalendermonatliche Saldierungsperiode“); die Jahreswerte sind die Summe der Monatswerte, Formeln (22) und (33) [K12R-18, Abschn. 2.1.4]. § 21 Abs. 1 EnFG spricht dagegen vom Kalenderjahr [K12R-04]. *Einschätzung:* Bei täglichen Zyklen fällt die Monatsgrenze für die Umlagen kaum ins Gewicht; wichtig ist sie für Formel (14): Endet der Monat mit vollerem Speicher, als er begann, sinken der rechnerische Wirkungsgrad und mit ihm die förderfähige Menge. Der Vermarkter sollte den Ladezustand an Monatsgrenzen deshalb steuern. Abgerechnet wird jährlich.

### Netzladung beim Grünstromspeicher

Die BNetzA legt die Ausschließlichkeitsoption streng aus. Wird auch nur einmal Netzstrom eingespeichert, entfällt die Förderfähigkeit der Speichereinspeisung „für das gesamte Kalenderjahr“; Umlageprivilegien nach § 21 EnFG sind unter dieser Option „naturgemäß ausgeschlossen“ [K12R-18, Abschn. 2.1.3, S. 11]. *Einschätzung:* Netzladung entsteht schneller als geplant, etwa beim Abruf negativer Regelreserve, beim Nachladen auf einen Mindestladezustand oder durch Hilfsstrom; wegen der Minimumregel genügt eine Viertelstunde mit Netzbezug während der PV-Ladung (Kasten in Abschnitt 12.3). M1 rechnet Variante A mit strengem Netzladeverbot; was eine Netzladung kostet, zeigt Schritt 8 des Rechenbeispiels.

### Wirkung auf die Konfigurationen A, A_inno, B und C

| Merkmal | A Grünstromspeicher | A_inno | B getrennt | C Mischspeicher |
|---|---|---|---|---|
| Anschluss | gemeinsamer NVP | gemeinsamer NVP, Anlagenkombination | je ein Anschluss für PV und Speicher | gemeinsamer NVP |
| Regel für den Speicherstrom | Ausschließlichkeitsoption | InnAusV; Abgrenzungsoption ausgeschlossen | keine Förderung; Speicher als Fall A10, auch mit Hilfsstrom als Speicherverbrauch; bei sonstigem Verbrauch A11 oder A1 | Abgrenzungsoption, Fall A1 (A8 nur ohne sonstigen Verbrauch und ohne Z2) |
| Netzladung | im ganzen Kalenderjahr nie | während der gesamten Zahlungsdauer nie | frei | frei |
| Förderfähiger Speicherstrom | gesamte Speichereinspeisung in AW>0-Zeiten | nach Zuschlag; der Speicher lädt nur aus der Kombination (§ 13 Abs. 4) | – | Wirkungsgrad × PV-Ladung in AW>0-Zeiten |
| Umlagen auf Ladestrom | keine Netzladung; Hilfsstrom ohne Umlageprivileg | wie A | null bei A10; bei sonstigem Verbrauch A11 (Umlagen auf alle Verluste) oder A1 mit Z2 | Formeln (16)–(21) |
| Bedingung am 01.10.2026 | geltendes Recht (Auslegung der BNetzA) | geltendes Recht; entfällt ab 2027 laut Entwurf | § 21 EnFG, später Anlage 1 | MiSpeL ab Bekanntgabe; bis 30.09.2027 Einverständnis von NB und MSB |

Table: Regulatorische Wirkung der Konfigurationen von R3

Quelle: § 19 EEG, § 13 InnAusV, § 21 EnFG [W2V-03, W2V-08, W2V-09]; MiSpeL-Festlegung vom 01.10.2026 [K12R-17, K12R-18]; BT-Drs. 21/7867 [W2V-17]; Konfiguration B nach D-024 (Stand 01.10.2026).

Die Erlöse der Varianten vergleicht Kapitel 14; mit Regelreserve und optimierter Bezugsleistung lag B 2025 in M1 vor C [M1, Lauf 20260927-colocation].

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Mischspeicher im Übergang. Die Abgrenzungsoption gilt bis 30.09.2027 nur mit Einverständnis von Netz- und Messstellenbetreiber (TZ 9a) [K12R-17, S. 3]. Ein Rechtsanwalt für Energierecht sollte klären, ab welchem Tag die Festlegung wirksam ist und ob nach Lesart A die „Alternative zur Ausschließlichkeitsoption“ je Viertelstunde wirkt und die PV in Viertelstunden ohne Speichereinspeisung förderfähig bleibt oder nach Lesart B die PV-Einspeisung an einem gemischten Einspeisepunkt ohne Abgrenzung insgesamt nicht nachweisbar förderfähig ist. Zu klären sind außerdem, wie sich das Einverständnis vertraglich sichern lässt, ob Netz- und Messstellenbetreiber es erteilen müssen (TZ 7) [K12R-17, S. 2], ob Standalone-Speicher ohne Einverständnis bei § 21 EnFG in der bisherigen Anwendung bleiben, ob für Einspeisung zu negativen Preisen die Umlageprivilegien entfallen, wie das Hintergrundpapier allgemein sagt, Anlage 1 aber nicht erkennen lässt [K12R-21, S. 2; K12R-18, S. 33–36], und ob eine Anlagenkombination nach InnAusV ihren Zuschlag aufgeben und mit welchen Folgen in die Abgrenzungsoption wechseln kann oder ob ihr Ausschluss mit den InnAusV-Vorgaben entfällt [K12R-17, S. 26–27]. Das Buch rechnet für R3 im Basisfall erst ab 01.10.2027 damit (A-042).

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Bilanzkreis bei entbündelten Verträgen. Mit Marktprämie verlangt Voraussetzung 4 einen gesonderten Bilanz- oder Unterbilanzkreis für die gesamte Einspeisung [K12R-18, Abschn. 3.1.1 Nr. 4]. Ein PV-PPA mit Händler X und ein Batterie-Toll mit Händler Y am selben NVP, wie sie ein 2026 veröffentlichtes deutsches Projekt kombiniert [VR3-07], passen dazu nur schwer (*Einschätzung*). Rechtsanwalt für Energierecht und Direktvermarkter sollten prüfen, ob Unterbilanzkreise eines Händlers mit Weiterreichung an den zweiten Vertragspartner genügen und wer bei Engpässen am NVP Vorrang hat. Ausweichwege sind getrennte Anschlüsse (B) oder ungeförderte PV, für die die Bilanzkreisvoraussetzung nicht gilt [K12R-18, Abschn. 3.1.2] (Kapitel 14 und 15).

## Messkonzept für R3: Zähler, Mittelspannung und Hilfsenergie

Ein Messkonzept legt fest, welche Zähler wo sitzen, welche Mengen sie erfassen und wie daraus Förderung, Umlagen und Bilanzierung berechnet werden. Abgestimmt wird es mit dem Netzbetreiber (NB) und dem Messstellenbetreiber (MSB), der die Zähler einbaut, betreibt und abliest. Anlage 1 verlangt viertelstundengenaue, mess- und eichrechtskonforme Messeinrichtungen, „in der Regel“ Zweirichtungszähler, und eine strenge Messtrennung: Hinter dem Speicherzähler Z2 darf es keinen anderen Verbrauch und keine andere Erzeugung geben, vor Z2 keinen Speicherverbrauch und keine Speichererzeugung [K12R-18, Abschn. 3.2.1, 3.2.4]. Für R3 in Variante C (Fall A1) ergeben sich vier Messpunkte (Abbildung 12.1).

| Zähler | Ort | Misst | Rolle |
|---|---|---|---|
| Z1 | NVP, Übergabe an das Netz in der Mittelspannung | Netzbezug (3) und Netzeinspeisung (4) je Viertelstunde | Bilanzierung, Förderung, Umlagen; Pflicht |
| Z2 | Mittelspannungsabgang des Speichers, netzseitig der Speichertransformatoren (Vorschlag) | Speicherverbrauch (5) und Speichererzeugung (6) | Wirkungsgrad und grüne Ladung; Pflicht in A1 |
| Z-PV | Abgang der PV-Stationen | PV-Erzeugung | nicht in den Formeln, keine Mehrförderung; Betriebsüberwachung, Ertragsprüfung, Plausibilisierung (Einschätzung) |
| Z-Hilf | eigene Versorgung der Hilfsaggregate außerhalb von Z2 | Hilfsstrom | Kosten, Umlagen, Stromsteuer (A-047) |

Table: Zähler im Messkonzept R3, Variante C

Quelle: MiSpeL-Festlegung vom 01.10.2026, Anlage 1 [K12R-18]; Lage von Z2 (in der Festlegung nicht geregelt) und Hilfsstrom nach dem Vorab-Dialog [WS-00] und A-058 (Stand 01.10.2026).

**Z1.** In der Mittelspannung erfolgt die Messung in der Regel als registrierende Leistungsmessung (RLM), also mit einem Zähler, der die Leistung je Viertelstunde aufzeichnet und fernausgelesen wird, über Messwandler (Vorab-Dialog [WS-00]). Anlage 1 schreibt weder eine Zählerart noch die Spannungsebene von Z2 vor [K12R-18, Abschn. 3.2.1–3.2.6; K12R-17, S. 28].

**Z2 auf der Mittelspannungsseite.** Der Vorab-Dialog schlägt den Mittelspannungsabgang des Speichers vor, mit drei Gründen [WS-00]: Die Verluste der Speichertransformatoren liegen dann hinter Z2 und zählen zu den anteilig privilegierten Speicherverlusten; ein Zähler im Mittelspannungsabgang ersetzt mehrere Zähler auf der Niederspannungsseite mit sehr hohen Strömen; und der gemessene Wirkungsgrad entspricht dem, den das Netz sieht. Das passt zur Definition des Round-Trip-Wirkungsgrads (RTE) im Buch, die den Mittelspannungstransformator einschließt (A-001). Voraussetzung ist ein Aufbau, in dem die Speichereinheiten an eigenen Mittelspannungsabgängen ohne PV-Stationen hängen. *Einschätzung:* Gemessener Wirkungsgrad und förderfähige Menge sinken dadurch etwas; bei 4,32 €/MWh Marktprämie wiegt das wenig gegenüber dem Umlagevorteil.

**Hilfsenergie.** Klimatisierung, Batteriemanagement, Brandschutz und Transformatorleerlauf brauchen 2,0/2,5/4,0 % der Ladeenergie (Low/Mid/High). Für einen Speicher mit 20 MWh nutzbar sind das bei 2,5 % mindestens rund 196 MWh im Jahr (A-052, Wert für R1). Für diesen Hilfsstrom gibt es zwei Wege. Er kann eine eigene Versorgung mit eigenem Zähler außerhalb von Z2 erhalten. Dann ist er sonstiger Verbrauch und trägt, soweit er aus dem Netz kommt, Umlagen und Stromsteuer (A-047); wird er so über dieselbe Entnahmestelle geführt, scheiden die vereinfachten Fälle A8 und A10 aus. Oder er liegt hinter Z2 und zählt zu den Speicherverlusten; das lässt die Festlegung nur für Verbräuche zu, die ausschließlich dem Speicher dienen [K12R-18, S. 25]. Das Buch wählt für R3 C den eigenen Zähler (A-058). Für den Grünstromspeicher A genügt das nicht (Kasten in Abschnitt 12.3).

**A8 als Sparvariante.** Ohne sonstigen Verbrauch genügt Z1 (Fall A8, Abschnitt 12.4.2). Sind die Messeinrichtungen für A1 vorhanden, ist A8 nicht anwendbar; die Wahl bindet und lässt sich frühestens mit Wirkung für ein folgendes Kalenderjahr umstellen [K12R-18, Abschn. 3.2.3]. Die Kosten eines Messkonzepts nach Anlage 1 schätzt der Vorab-Dialog auf 30 k€ einmalig und 5 k€ im Jahr (A-008, Schätzung ohne Angebot).

**Kopplung.** R3 ist wechselstromseitig gekoppelt (AC-Kopplung): Speicher und PV haben eigene Umrichter und treffen sich auf der Wechselstromseite. Bei gleichstromseitiger Kopplung (DC-Kopplung) teilen sich Batterie und PV-Module einen Wechselrichter; ein Wechselstrom-Messpunkt nur für den Speicher fehlt dann (Einschätzung). Die Festlegung schreibt weder AC- noch DC-Zähler vor; ist die PV gleichstromseitig mit dem Speicher verbunden, verlangt die BNetzA eine geeichte DC-Messung [K12R-17, S. 31–32].

![Messkonzept R3 (Mischspeicher, Fall A1) als Einlinienbild: Z1 am Netzverknüpfungspunkt, Z2 im Mittelspannungsabgang des Speichers, PV- und Hilfsstromzähler außerhalb von Z2; Pfeile zeigen Energieflüsse.](05_figures/K12/12_messkonzept_r3.png)

Quelle: Eigene Darstellung nach MiSpeL-Festlegung vom 01.10.2026, Anlage 1 [K12R-18], und Vorab-Dialog [WS-00]; Auslegung R3 nach D-025 und A-054 (Stand 01.10.2026).

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Zählerposition, Verluste und Hilfsstrom. Die Festlegung regelt nicht, ob Z2 auf der Mittel- oder der Niederspannungsseite der Speichertransformatoren sitzen muss und ob Transformatorverluste hinter Z2 wie Leitungsverluste [K12R-17, S. 34] als Speicherverbrauch gelten dürfen (Lesart A, anteilig privilegiert) oder sonstiger Verbrauch sind (Lesart B, umlagebelastet). Offen ist auch, welche Hilfsverbräuche ausschließlich dem Speicher dienen, etwa Brandschutz oder Transformatorleerlauf, wie das dem Messstellenbetreiber nachgewiesen wird und ob ein Standalone-Speicher damit A10 ohne Unterzähler nutzen kann; ebenso, ob Netzentgelt- und Stromsteuerbefreiung (§ 118 Abs. 6 Satz 3 EnWG, § 11a Abs. 3 StromStV) Speicherverluste und so erfassten Hilfsstrom umfassen [K12R-17, S. 22–23]. Messkonzept, Zählerplatz und Zuordnung des Hilfsstroms sollten mit Netz- und Messstellenbetreiber schriftlich abgestimmt und von einem Rechtsanwalt für Energierecht geprüft werden, die Stromsteuer von einem Steuerberater; die Unterlagen des Workshops vom 02.10.2026 sind auszuwerten.

## Rechenbeispiel am Referenzfall R3 {.unnumbered}

> [!BEISPIEL]
> **Rechenbeispiel R3: Monatsabrechnung Juli für den Mischspeicher (Variante C, Fall A1)**
>
> *Grundlage:* eigene Rechnung nach dem Formelsatz der MiSpeL-Anlage 1 (Festlegung vom 01.10.2026) [K12R-18]. Der Monat ist stilisiert: Die Zahl negativer Viertelstunden stammt aus dem Preis-Snapshot, alle übrigen Mengen sind Annahmen (A-056, A-057). M1 (Version 2.0.0, Lauf 20260927-colocation) rechnet das Beispiel nach und bestätigt alle Werte bis auf Rundungen (Marktprämie 6.739,54 €). Mit Viertelstundenflüssen des Juli 2026 (nur Day-Ahead, perfekte Voraussicht, Hilfsstrom nach A-052 (2,5 % der Ladung); brutto, nominal) erzeugt die PV 2.288 MWh, und R3 C lädt 1.055 MWh, davon 58 % aus der PV (Beispiel: 40 %); förderfähig sind 1.868 MWh (1.560), umlagebelastet 11,4 MWh (13,75). Im Januar 2026 stammen 90 % der Ladung aus dem Netz.
>
> *Schritt 1 – Anlage:* R3 in der Basisauslegung nach D-025 (A-054): 15 MWp PV (12 MW Wechselstrom, A-011) und ein AC-gekoppelter Speicher mit 10 MW, 20 MWh nutzbar und 5 MW Bezugsleistung. Z1 misst am NVP, Z2 im Mittelspannungsabgang des Speichers, der Hilfsstrom hat einen eigenen Zähler (A-058). Die MiSpeL ist wirksam, Netz- und Messstellenbetreiber haben zugestimmt, die PV erhält die Marktprämie nach dem Jahresmarktwert.
>
> *Schritt 2 – PV-Erzeugung im Juli:* 15 MWp × 1.050 kWh/kWp = 15.750 MWh im Jahr (A-011). Für den Monatsanteil dient die Tabelle in § 51a Abs. 2 EEG, weil sie den Jahresgang der Solarerzeugung nachbildet (*Einschätzung*); sie verteilt 3.800 Volllastviertelstunden auf die Monate, davon 498 auf den Juli [W2V-02, VR3-30]: 15.750 MWh × 498/3.800 = 2.064 MWh (A-056; Näherung ohne Standortprofil).
>
> *Schritt 3 – Mengen des Monats:*
>
> | Größe | Menge | Herleitung |
> |---|---:|---|
> | Viertelstunden mit negativem Day-Ahead-Preis (AW = 0) | 306 | Juli 2026, an 14 Tagen [M1D-01, eigene Auswertung]; zum Vergleich Juli 2025: 48 |
> | PV-Erzeugung in diesen Viertelstunden | 640 MWh | 76,5 h, im Mittel rund 8,4 MW (Annahme) |
> | Speicherverbrauch an Z2, Formel (5) | 1.000 MWh | rund 1,4 Vollzyklen je Tag nach der Zählweise von A-021 (870 ÷ 31 ÷ 20; batterieseitig 1,5); erlaubt sind 2 |
> | davon zeitgleich aus dem Netz, (9) | 600 MWh | Laden zu niedrigen und negativen Preisen, höchstens 5 MW |
> | davon aus der PV, (10) | 400 MWh | je 200 MWh in negativen und in positiven Viertelstunden |
> | Speichererzeugung an Z2, (6) | 870 MWh | Wirkungsgrad 87 % (A-001); Ladezustand am Monatsende wie am Anfang |
> | Hilfsstrom (eigener Zähler) | 25 MWh | 2,5 % der Ladung (A-052): 12 MWh aus der PV zu positiven Preisen, 5 MWh während der Entladung, 8 MWh aus dem Netz in Viertelstunden ohne Entladung und ohne Ladung |
> | Netzbezug an Z1, (3) | 608 MWh | 600 + 8 |
> | Speichereinspeisung nach Minimumregel, (11) | 865 MWh | 870 − 5; Z1 sieht in Entladeviertelstunden ohne PV nur den Saldo |
> | PV-Direkteinspeisung, alle in AW>0-Zeiten | 1.212 MWh | 2.064 − 400 − 12 − 440 (in negativen Viertelstunden abgeregelt: 640 − 200) |
> | Speichereinspeisung in AW>0-Zeiten, (29) | 865 MWh | Entladung nur zu positiven Preisen |
>
> Table: Stilisierte Monatsmengen Juli für R3, Variante C
>
> Quelle: Snapshot Day-Ahead-Preise DE-LU [M1D-01], eigene Zählung; übrige Mengen Annahmen des Rechenbeispiels auf Basis von A-001, A-011, A-021, A-052 und A-054; Nachrechnung und Modellmonate: M1 2.0.0, Lauf 20260927-colocation (Stand 27.09.2026).
>
> *Schritt 4 – Förderung:* Wirkungsgrad (14) = 870/1.000 = 0,87. EE-Speichererzeugung (15) = 0,87 × 400 = 348 MWh. Fremdtankstrom (12) = MAX[870 − 1.000; 0] = 0, also berücksichtigungsfähige Speichereinspeisung (13) = 865 MWh. Förderfähige Speichereinspeisung (31) = 865/865 × MIN[865; 348] = 348 MWh. Förderfähige PV-Direkteinspeisung (26) = 1.212 MWh. Insgesamt förderfähig sind (32) = 1.560 MWh. Von 865 MWh Speicherstrom sind nur 348 MWh förderfähig: Wirkungsgrad mal PV-Ladung.
>
> *Schritt 5 – Umlagen:* Saldierungsfähige Netzeinspeisung (16) = 865 − 348 = 517 MWh. Speicherverluste (17) = 1.000 − 870 = 130 MWh, davon privilegiert (19) = 517/870 × 130 = 77,25 MWh. Umlagebefreit ist (20) = MIN[517 + 77,25; 608] = 594,25 MWh; umlagebelastet bleiben (21) = 608 − 594,25 = 13,75 MWh. Das sind die 8 MWh Hilfsstrom aus dem Netz, 5 MWh Hilfsstrom während der Entladung, der die anerkannte Speichereinspeisung schmälert, und 0,75 MWh aus der anteiligen Verlustzurechnung. Zu 13,87 €/MWh KWKG- und Offshore-Netzumlage (Abschnitt 12.2.1) kosten die 13,75 MWh rund 190 €, mit dem Aufschlag für besondere Netznutzung rund 405 €; die Befreiung der 594,25 MWh ist ohne Aufschlag rund 8,2 k€ wert.
>
> *Schritt 6 – Marktprämie:* Mit $AW$ = 49,4 €/MWh (A-003) und dem Jahresmarktwert 2025 von 45,08 €/MWh [K15M-01] ergeben sich 1.560 MWh × 4,32 €/MWh = 6.739 € (nominal, vor Entgelt des Direktvermarkters), davon Speicheranteil 348 MWh × 4,32 €/MWh = 1.503 €. Ohne Speicher wären 2.064 − 640 = 1.424 MWh förderfähig gewesen (6.152 €). Der Speicher holt 200 × 0,87 = 174 MWh aus negativen Viertelstunden in förderfähige Zeiten, verliert aber 13 % auf die 200 MWh PV-Ladung zu positiven Preisen (26 MWh), und 12 MWh PV decken Hilfsstrom: per saldo 136 MWh oder 588 € mehr. Bei einem Jahresmarktwert von 55,10 €/MWh (M1-Schätzung für 2026, A-059) entfiele die Prämie ganz.
>
> *Schritt 7 – Ohne Abgrenzungsoption:* Fehlt sie (A-042), verliert der Speicherstrom die Förderung, im Juli 1.503 €; nach Lesart B stünde die ganze Monatsprämie von 6.739 € in Frage (Kasten „Mischspeicher im Übergang“).
>
> *Schritt 8 – Eine Netzladung beim Grünstromspeicher (A):* Lädt A ein einziges Mal Netzstrom, etwa weil ein Abruf negativer Regelreserve die Einspeisung übersteigt, verliert der Speicherstrom nach der Auslegung der BNetzA die Förderung des Kalenderjahres [K12R-18, S. 11]. M1 berechnet für A mit 20 MWh im Kalenderjahr 2025 5.737 MWh Speichereinspeisung und 13.129 MWh förderfähige Einspeisung insgesamt, mit perfekter Voraussicht, nur Day-Ahead, 2,3 €/MWh Degradation und höchstens zwei Vollzyklen je Tag (A-002, A-021) [M1, Lauf 20260927-colocation]. Bei 4,32 €/MWh kostet die eine Netzladung rund 25 k€, wenn nur der Speicherstrom betroffen ist, und bis rund 57 k€, wenn nach Lesart B auch die PV-Direkteinspeisung die Prämie verliert; mit 55 MWh nutzbar sind es allein für den Speicher rund 48 k€. Bei einem Jahresmarktwert über 49,4 €/MWh kostet sie nichts.
>
> *Deutung:* Im Juli ist die Förderung des Speicherstroms rund 1,5 k€ wert, die Umlagebefreiung rund 8,2 k€ (ohne Aufschlag). *Einschätzung:* Die Abgrenzungsoption lohnt vor allem, weil sie PV-Prämie und Umlagebefreiung trotz Netzladung sichert; die Speicherförderung selbst ist bei heutigen Marktwerten ein kleiner Posten. Das Messkonzept wirkt direkt: Hilfsstrom während der Entladung schmälert die anerkannte Speichereinspeisung, ein niedriger gemessener Wirkungsgrad die förderfähige Menge.

## Praxis-Check und typische Fehler {.unnumbered}

> [!TIP]
> **Praxis-Check:** Prüffragen für Angebote, Verträge und Due Diligence bei Co-Location
>
> - Welchen Förderstatus hat die PV (Gebotstermin, anzulegender Wert, Inbetriebnahme), welche Fassung von § 51 EEG gilt, welche Speicheroption ist einheitlich gewählt, und wird mit Monats- oder Jahresmarktwert gerechnet?
> - Liegt ein Zuschlag aus der Innovationsausschreibung vor? Dann gelten Netzladeverbot über die gesamte Zahlungsdauer, Mindestgrößen des Speichers (25 % der Leistung, Einspeicherung von zwei Stunden Nennleistung; ob auch nach Alterung, klären) mit jährlichem Gutachten und der Ausschluss der Abgrenzungsoption.
> - Grünstromspeicher: Schließen Steuerung und Vermarktungsvertrag jede Netzladung aus, auch durch negative Regelreserve, Hilfsstrom und PV-Schwankungen in der Viertelstunde, und wer haftet für den Förderverlust eines Jahres?
> - Mischspeicher: Ist das Projekt gegen die Festlegung vom 01.10.2026 geprüft, sind Fallkonstellation und Formelsatz festgelegt, und liegt das Einverständnis von Netz- und Messstellenbetreiber bis 30.09.2027 schriftlich vor?
> - Sind alle Anlagen hinter der Einspeisestelle in der Direktvermarktung, läuft die Einspeisung in einem Bilanzkreis, und passen PPA, Toll und Vermarktungsvertrag dazu?
> - Sind Z1 und Z2 mess- und eichrechtskonform mit Viertelstundenwerten, wo sitzt Z2, ist die Messtrennung hinter Z2 eingehalten, und ist der Speicher AC-gekoppelt (sonst geeichte DC-Messung)?
> - Wie ist der Hilfsstrom versorgt und gemessen, hat der Netzbetreiber die Zuordnung schriftlich bestätigt, und hat ein Grünstromspeicher dafür eine eigene Entnahmestelle? Bei Standalone-Speichern: A10, A11 oder A1 mit Speicherzähler?
> - Wer ermittelt die Monatsmengen nach Anlage 1, wer meldet bis 31. Mai nach § 21 EnFG, und ist der Speicher im Marktstammdatenregister registriert?
> - Welche Übergangsregeln des EEG 2027 treffen das Projekt, wie wirkt ein Refinanzierungsbeitrag auf Kaufpreis und Finanzierung, und ist ein dauerhafter Verzicht auf die Marktprämie (§ 21e, Entwurf) erwogen?

> [!WARNING]
> **Typische Fehler:**
>
> - Analysen nach dem MiSpeL-Arbeitsstand ungeprüft übernehmen oder das Einverständnis von Netz- und Messstellenbetreiber im Übergang übersehen.
> - Einen Grünstromspeicher „ausnahmsweise“ aus dem Netz laden, etwa für negative Regelreserve, und damit die Förderung des Speicherstroms für das ganze Jahr riskieren.
> - Annehmen, ein eigener Hilfsstromzähler schütze den Grünstromspeicher vor Netzladung.
> - Die gesamte Entladung eines Mischspeichers als förderfähig ansetzen statt Wirkungsgrad × PV-Ladung in AW>0-Zeiten.
> - Die grüne Ladung aus Monatssummen von PV-Erzeugung und Ladung ableiten statt aus dem Minimum je Viertelstunde.
> - Bei neuen Anlagen die Marktprämie mit dem Monatsmarktwert oder dem „MW Solar(a)“ statt mit dem Jahresmarktwert rechnen.
> - Den PV-Zähler für förderrelevant halten oder Verbräuche, die auch anderen Zwecken dienen, hinter den Speicherzähler legen.
> - Unter dem EEG-2027-Entwurf dem Refinanzierungsbeitrag mit einem PPA ausweichen wollen.

## Zusammenfassung {.unnumbered}

1. Das EEG fördert Speicherstrom nur mittelbar, in derselben Höhe wie PV-Strom und über eine von drei Optionen. Die Marktprämie, anzulegender Wert minus Jahresmarktwert, betrüge für R3 mit dem Wert 2025 4,32 €/MWh; 2026 kann sie null sein.
2. Für neue Anlagen entfällt die Prämie in jeder Viertelstunde mit negativem Day-Ahead-Preis, der Ausgleich nach § 51a kommt erst am Ende der Förderdauer. Ein Speicher kann PV-Strom aus diesen Viertelstunden in förderfähige Zeiten verschieben.
3. § 21 EnFG befreit Netzentnahmen zur Zwischenspeicherung von Umlagen, soweit im Kalenderjahr zurückgespeist wird. Gezählt wird je Viertelstunde das Minimum aus Netzbezug und Ladung; eine ausdrückliche Vorrangregel gibt es nicht.
4. Der Grünstromspeicher darf nie Netzstrom laden; nach der Auslegung der BNetzA kostet schon eine Netzladung die Förderung des Speicherstroms für das Kalenderjahr, bei R3 mit dem Jahresmarktwert 2025 rund 25 k€, nach Lesart B mit der PV-Prämie bis rund 57 k€.
5. Die MiSpeL ordnet viertelstündlich gemessene Mengen in elf Fallkonstellationen je Kalendermonat zu. Förderfähig ist höchstens Wirkungsgrad × PV-Ladung, eingespeist in AW>0-Zeiten; umlagebelastet bleibt im Beispiel im Wesentlichen der Hilfsstrom.
6. Die am 01.10.2026 beschlossene MiSpeL wirkt ab Bekanntgabe, bis 30.09.2027 aber nur mit Einverständnis von Netz- und Messstellenbetreiber; das Buch rechnet für R3 C im Basisfall ab 01.10.2027 mit der Abgrenzungsoption.
7. Das Messkonzept entscheidet mit: Z1 am NVP, Z2 am Speicher, strikte Messtrennung, Hilfsstrom außerhalb von Z2. Bei Standalone-Speichern entscheidet nach Lesart des Buchs die Erfassung des Hilfsstroms: als Speicherverbrauch Fall A10 ohne Umlagen, als sonstiger Verbrauch A11 mit Umlagen auf alle Verluste oder A1 mit Speicherzähler.
8. Der Entwurf des EEG 2027 führt für Gebotstermine ab 2027 Differenzverträge mit Refinanzierungsbeitrag ein, auch für zwischengespeicherten Strom und in der sonstigen Direktvermarktung; befreit ist nur, wer dauerhaft auf die Marktprämie verzichtet. Die Innovationsausschreibung soll nach dem Entwurf zum 01.01.2027 enden.

## Übungen {.unnumbered}

**Übung 12.1 (Rechnen).** Die PV von R3 speist im August 1.500 MWh in Viertelstunden mit positivem Day-Ahead-Preis ein. In 160 Viertelstunden ist der Preis negativ; dort erzeugt die PV 300 MWh, von denen der Speicher 120 MWh aufnimmt und abends mit 87 % Wirkungsgrad in AW>0-Zeiten einspeist; der Rest wird abgeregelt. (a) Berechnen Sie die Marktprämie des Monats für Direkteinspeisung und Speicheranteil mit $AW$ = 49,4 €/MWh (A-003) und $JW$ = 45,08 €/MWh sowie mit dem Zuschlagswert von A_inno, 53,4 €/MWh (A-004). (b) Wie viele Volllastviertelstunden schreibt § 51a EEG gut, und wann wirken sie? (c) Welche Zahlung ergäbe der Differenzvertrag des EEG-2027-Entwurfs bei $JW$ = 55,10 €/MWh, vereinfacht mit voller Differenz, was erhält die Anlage nach geltendem Recht, und könnte sie dem Beitrag mit einem PPA für dieses Jahr ausweichen?

**Übung 12.2 (Rechnen).** R3 in Variante C, Fall A1, im September: Speicherverbrauch an Z2 800 MWh, davon zeitgleich aus dem Netz 560 MWh; Speichererzeugung an Z2 688 MWh; Speichereinspeisung nach Minimumregel 684 MWh, davon 650 MWh in AW>0-Zeiten (34 MWh bei Abrufen positiver Regelreserve in Viertelstunden mit negativem Preis); Netzbezug an Z1 575 MWh; PV-Direkteinspeisung in AW>0-Zeiten 1.100 MWh. (a) Berechnen Sie die Formeln (10), (14), (15), (16), (19), (20), (21), (31) und (32) sowie die Marktprämie mit 4,32 €/MWh. (b) Der Vermarkter hätte 40 MWh der PV-Ladung ebenso aus dem Netz laden können; die PV hätte diese 40 MWh dann in AW>0-Zeiten direkt eingespeist. Wie ändern sich förderfähige Menge, Marktprämie und umlagebelasteter Netzbezug? Was folgt daraus für den Grundsatz „Preis vor Farbe“: Der Mischspeicher lädt, wenn Strom billig ist, gleich ob grüner Strom aus der PV oder grauer aus dem Netz?

**Übung 12.3 (Zuordnen).** Nennen Sie für jedes Projekt Option, Fallkonstellation und nötige Zähler sowie eine offene Frage: (a) R2 als Standalone-Speicher, Hilfsstrom über denselben Anschluss; (b) R3 Variante C, AC-gekoppelt, Hilfsstrom mit eigenem Zähler; (c) R3 Variante A; (d) R3 Variante C, deren PV ungefördert über einen PPA verkauft; (e) 15 MWp PV, 5 MW Wind und ein Speicher an einem Anschluss; (f) R3 Variante A_inno.

**Übung 12.4 (Bewerten und Entscheiden).** Ein Vermarkter bietet an, den Grünstromspeicher R3 A zusätzlich in negativer Sekundärregelleistung (aFRR) zu vermarkten, und stellt 40 k€/a Mehrerlös in Aussicht (Annahme). (a) Wann führt ein Abruf zu Netzladung, und welche Folgen hat diese nach § 19 Abs. 3a EEG und der Auslegung der BNetzA für Speicherförderung, Umlagen und PV-Förderung? (b) Beziffern Sie den Förderverlust eines Jahres mit 5.737 MWh Speichereinspeisung und 13.129 MWh förderfähiger Einspeisung insgesamt [M1, Lauf 20260927-colocation] bei Jahresmarktwerten von 45,08 und 55,10 €/MWh. (c) Entscheiden Sie: annehmen, ablehnen oder auf Variante C wechseln? Nennen Sie Bedingungen, Zeitpunkt und die Regelungen im Vermarktungsvertrag. (d) Was ändert sich bei A_inno? (e) Alternativ erhält der Speicher einen eigenen Netzanschluss (Variante B). Bewerten Sie B gegenüber A und C: Was gilt für Speicherförderung, PV-Prämie, Netzladung und Umlagen auf Ladestrom und Hilfsstrom, welche Kosten kommen hinzu, und wann ist B die bessere Wahl? Nettowerte 2025 mit 20 MWh nach M1 (nur Day-Ahead): A 1.465,2, B 1.589,3, C 1.630,6 k€/a [M1, Lauf 20260927-colocation].

**Übung 12.5 (Entwerfen).** Entwerfen Sie das Messkonzept für R3 in Variante C als Einlinienbild mit Zählerliste. Legen Sie Lage und Art von Z1 und Z2 fest, führen Sie den Hilfsstrom, begründen Sie A1 statt A8, und formulieren Sie fünf Punkte, die Sie mit Netz- und Messstellenbetreiber schriftlich vereinbaren. Wie ändert sich das Konzept, wenn der Speicher gleichstromseitig an die PV-Wechselrichter gekoppelt wäre, und wie, wenn die PV über einen PPA mit Händler X und der Speicher über einen Toll mit Händler Y vermarktet würde?

Die Lösungen stehen im Anhang A unter Kapitel 12.

## Quellen und Stand {.unnumbered}

Qualität nach dem Quellenregister: A = Primärquelle, B = anerkannte Sekundärquelle, C = Fachmedium oder Anbieter.

**Gesetze und Verordnungen (A):** [W2V-01] § 51 EEG · [W2V-02] § 51a EEG · [W2V-03, K12R-03] § 19 EEG · [W2V-05] § 100 EEG · [W2V-06] § 3 EEG · [W2V-08] § 13 InnAusV · [W2V-09, K12R-04] § 21 EnFG · [K17R-01] StromStG · [SYN-03] § 118 EnWG, jeweils Fassung am 27.09.2026 · [K12R-13] EEG Anlage 1 Nr. 2 · [K12R-16] EnFG § 2 Nr. 7 und § 6 (Fassung vom 18.12.2025).

**Behörden und Entwürfe (A):** [K12R-17 bis K12R-21] MiSpeL-Festlegung vom 01.10.2026 (Tenor mit Begründung, Anlage 1, Anlage 2, Pressemitteilung, Hintergrundpapier) · [K12R-01, W2V-18, W0R-04] MiSpeL-Verfahrensseite (Stand 01.10.2026) · [K12R-02, W0R-06] MiSpeL-Anlage 1, Arbeitsstand 05.08.2026 · [K12R-05, W2V-17] BT-Drs. 21/7867, Regierungsentwurf EEG 2027 (07.09.2026) · [W0R-15] Bundestag, Textarchiv KW 39 (24.09.2026) · [K12R-12] Bundestag, Anhörung zum EEG 2027 (05.10.2026) · [W0R-01] AgNes-Festlegungsentwurf (06.08.2026, nur Verweis) · [WS-18] BNetzA, Ausschreibung Solar erstes Segment, Gebotstermin 01.03.2026 (veröffentlicht 12.05.2026) · [VR3-23] BNetzA, Innovationsausschreibung, Gebotstermin 01.05.2026 (bekanntgegeben 25.06.2026).

**Marktdaten und Fachquellen:** [K15M-01] ÜNB, Marktwertübersicht (A) · [K12R-07, K12R-08, K12R-09] ÜNB, KWKG-Umlage, Offshore-Netzumlage und Aufschlag für besondere Netznutzung 2026 (A) · [M1D-01] Day-Ahead-Preise DE-LU, energy-charts, Snapshot 01.01.2023–26.09.2026 (A) · [VR3-29] DGS, Jahresmarktwert Solar 2025 (B) · [VR3-30] Clearingstelle EEG|KWKG, Solarspitzengesetz (02.07.2025; A) · [VR3-26] Next Kraftwerke, Innovationsausschreibung (C) · [VR3-07] ESS News, PPA und Toll an einem Projekt (06.07.2026; C) · [WS-00] Vorab-Dialog des Auftraggebers (interne Ausgangshypothese, C).

**Modelle:** M1, Läufe 20260927-kapitel02 (Solarmarktwert) und 20260927-kapitel06 (negative Viertelstunden); M1 2.0.0, Lauf 20260927-colocation (MiSpeL-Monatsabrechnung R3 C, Nachrechnung des Rechenbeispiels, Netzladung bei A, Varianten A, B, C); M2, Lauf M2-20260928-P04 (A11, R1).

**Annahmen und Entscheidungen:** A-001 bis A-005, A-008, A-011, A-021, A-024, A-042, A-047, A-052, A-054, A-056 bis A-060, A-M1-01; D-021, D-024, D-025.

**Stand:** 27.09.2026, MiSpeL 01.10.2026. Neu zu prüfen sind die Umsetzung der MiSpeL, das EEG 2027 im parlamentarischen Verfahren, § 118 Abs. 6 EnWG und AgNes (Entwurf vom 06.08.2026), die Umlagesätze einschließlich Aufschlag, der Jahresmarktwert Solar 2026 und die Stromsteuer auf Umwandlungsverluste und Hilfsstrom; Einzelheiten nennen die Stand-Kästen.
