---
title: "Kapitel 3 · Regelreserve, Systemdienstleistungen und Kapazitätsmechanismen"
subtitle: "Ökonomie von Batteriespeichern in Deutschland"
date: "04.10.2026"
kopfzeile-rechts: "Kapitel 3 · Stand 28.09.2026"
kapitel-start: 3
nummerierung: kapitelweise
inhaltsverzeichnis: true
toc-tiefe: 2
deckblatt-hinweis: "Keine Rechts-, Steuer- oder Anlageberatung. Erlösgutachten G1 anonymisiert verwendet."
---

# Regelreserve, Systemdienstleistungen und Kapazitätsmechanismen

> [!NOTE]
> **Lernziele:** Nach diesem Kapitel können Sie
>
> - Regelreserveprodukte (FCR, aFRR, mFRR) nach Aktivierung, Vergütungsregel, Zahlungsrichtung und Präqualifikation vergleichen;
> - Regelleistungserlöse für R1 und R2 aus Auktionsdaten berechnen und vom Referenzwert zum realistisch erzielbaren Erlös überleiten;
> - die Sättigung der Regelreservemärkte durch den Speicherzubau und die Tragfähigkeit neuer Segmente (Viertelstundenprodukte, Momentanreserve, Kapazitätsmarkt) für einen Fonds beurteilen.

## Warum das für Investor und Fonds zählt {.unnumbered}

Regelreserve war bisher die wichtigste Erlösquelle deutscher Großspeicher: Im Buchmodell M1 trug die Vorhaltung von Regelleistung 2024 und 2025 je nach Fall 67–95 % des Erlöses von R1, R2 und der G1-Konfiguration [M1, Lauf 20260928-standalone]; im Erlösgutachten G1 (anonymisiert) stammen rund 90 % des Erlöses 2027 aus der Sekundärregelreserve (G1, Abb. 16, abgelesen). Der Markt ist aber klein, und der Speicherzubau erreicht ihn: Die für aFRR präqualifizierte, also technisch zugelassene Batterieleistung entsprach Anfang 2026 schon 62–66 % der in Deutschland zugeschlagenen Menge, die aFRR-Leistungspreise lagen vom 01.01. bis 26.09.2026 um 28 % unter dem Vorjahreszeitraum [K03M-02; M1D-03, M1D-09; M1, Lauf 20260928-kapitel03]. Der Musterfonds R4 (484,8 MW) hielte rund 26 % dieser Menge je Richtung [Lauf M4-20260928-F06]. Wer Regelreserve im Business Case ansetzt, muss Preisregeln, Präqualifikation und Mengengerüst kennen und neue Segmente nach ihrem tatsächlichen Rechtsstand einordnen.

**Cashflow-Kompass:** Erlöse ● (Regelleistung, Regelarbeit, Kapazitätsvergütung für Verpflichtungen ab 11/2031, erste Zahlung frühestens 2033) · Betriebskosten ○ (Präqualifikation, Vermarktung, Pönalen) · Investitionen ○ (Speicherdauer, netzbildender Umrichter) · Steuern – · Finanzierung ○ (Anteil schwer prognostizierbarer Erlöse) · Fondsebene ● (Konzentration im aFRR-Markt). **Werttreiber:** Erlösniveau, Erlösrisiko, Regulierungsrisiko.

## Frequenzhaltung und Produktlogik

Im Stromnetz müssen Einspeisung und Entnahme in jedem Augenblick übereinstimmen, sonst weicht die Netzfrequenz vom Sollwert ab. Abweichungen gleichen die Übertragungsnetzbetreiber (ÜNB) mit Regelreserve in drei Stufen aus. Die Frequenzhaltungsreserve (Frequency Containment Reserve, FCR, Primärregelreserve) reagiert automatisch auf die Frequenzabweichung und muss innerhalb von 30 Sekunden vollständig aktiviert sein [K03M-08, S. 15]. Die automatische Frequenzwiederherstellungsreserve (aFRR, Sekundärregelreserve) löst sie ab; der Regler des ÜNB fordert sie an, voll wirken muss sie nach 5 Minuten. Die manuelle Frequenzwiederherstellungsreserve (mFRR, Minutenreserve) folgt mit 12,5 Minuten Vollaktivierungszeit und wird direkt oder nach Fahrplan abgerufen [K03M-08, S. 16–17; K03M-09, S. 9]. FCR ist symmetrisch: Wer 1 MW anbietet, muss es nach oben und nach unten erbringen. aFRR und mFRR werden getrennt als positive Reserve (mehr Einspeisung oder weniger Verbrauch) und negative Reserve (weniger Einspeisung oder mehr Verbrauch) ausgeschrieben. Ein Batteriespeicher erbringt positive Reserve durch Entladen, negative durch Laden und eignet sich technisch für alle drei Produkte.

Jedes Produkt hat zwei Bestandteile. Die **Regelleistung** vergütet das Vorhalten, also die Zusage, in einem Zeitfenster Leistung bereitzuhalten. Die ÜNB beschaffen sie täglich am Vortag in sechs Produktzeitscheiben zu je vier Stunden (00–04 bis 20–24 Uhr), im Buch „4-h-Block“ [K03M-08, S. 29; K03R-02, S. 4, 7; K03M-09, S. 19]. Die **Regelarbeit** vergütet die Energie, die bei einem Abruf tatsächlich fließt. Die ausgeglichenen Abweichungen rechnen die ÜNB mit den Bilanzkreisen zum Ausgleichsenergiepreis (reBAP) ab, dessen Berechnung Kapitel 2 beschreibt [K03M-09, S. 9].

Den Bedarf bemessen die ÜNB je Produkt verschieden. FCR wird für das kontinentaleuropäische Verbundnetz gemeinsam dimensioniert, nach einem Referenzstörfall von 3.000 MW oder probabilistisch, und nach Erzeugung und Last auf die ÜNB verteilt [K03M-03]. Der deutsche FCR-Bedarf lag 2021–2026 zwischen 528 und 584 MW [M1D-02; M1, Lauf 20260928-kapitel03]. aFRR und mFRR werden seit 09.12.2019, vollständig seit 03.10.2020, für jedes 4-h-Produkt dynamisch aus historischen Ungleichgewichten und Ausfallwahrscheinlichkeiten bemessen [K03M-03]. Bedarfe, Ergebnisse und anonyme Gebotslisten veröffentlichen die ÜNB täglich im Datencenter von regelleistung.net, ohne Angabe der Technologie [K03M-04]; den Speicheranteil an den Zuschlägen kann man deshalb nicht direkt ablesen. Tabelle 3.1 fasst die Produkte zusammen.

| Merkmal | FCR | aFRR | mFRR |
|---|---|---|---|
| Aktivierung | automatisch, frequenzabhängig | automatisch, Regler des ÜNB | direkt oder nach Fahrplan |
| Volle Erbringung | 30 s | 5 min | 12,5 min |
| Richtung | symmetrisch | positiv und negativ getrennt | positiv und negativ getrennt |
| Leistung: Produkt | 4-h-Block | 4-h-Block, zusätzlich Viertelstundengebote beschlossen | wie aFRR |
| Leistung: Vergütung | Einheitspreis (pay-as-cleared) | Gebotspreis (pay-as-bid) | Gebotspreis (pay-as-bid) |
| Arbeit: Vergütung | nicht gesondert | Grenzpreis (PICASSO), Max/Min-Abrechnung | Grenzpreis (MARI) |
| Präqualifikation Speicher | 15 min je Richtung; höchstens 80 % der Leistung | 60 min je Richtung | 60 min je Richtung |
| Präqualifizierte Batterieleistung (PQ) 01.01.2026 | 1,35 GW (26 % der FCR-PQ) | je Richtung 1,20 GW (5 % der aFRR-PQ) | 0,37/0,36 GW (1 % der mFRR-PQ) |

Table: Regelreserveprodukte im Vergleich

Quelle: K03M-08, S. 15–17, 29, 31, 50–51; K03M-09, S. 9; K03R-02; M1Q-01, Abschn. 2.7.1, 3.1.6; K03M-02 (Anteile eigene Rechnung) (Stand 28.09.2026).

## Vergütung, Preisregeln und europäische Plattformen

### Regelleistung: Einheitspreis und Gebotspreis

Für die Regelleistung gelten zwei Vergütungsregeln [K03M-08, S. 29, 31]. Bei FCR erhalten alle bezuschlagten Anbieter den Leistungspreis des höchsten noch bezuschlagten Gebots, den Grenzpreis (Einheitspreisverfahren, pay-as-cleared); die Aktivierung wird nicht gesondert vergütet. Bei aFRR und mFRR erhält jeder bezuschlagte Anbieter seinen eigenen Gebotspreis (Gebotspreisverfahren, pay-as-bid). Bei FCR kann ein Speicher als Preisnehmer niedrig bieten; bei aFRR bestimmt sein Gebot den Erlös, und jedes Gebot wägt Zuschlagschance gegen Preis ab. Nach unten begrenzen die Opportunitätskosten das Gebot, also der Erlös, den dieselbe Leistung im Day-Ahead- oder Intraday-Handel gebracht hätte (Kapitel 4).

Die ÜNB veröffentlichen FCR-Preise je MW und 4-h-Block, aFRR-Leistungspreise seit 2023 je MW und Stunde, als Durchschnitts- und Grenzpreis der Zuschläge [M1D-02, M1D-03]. Das Buch rechnet einheitlich in €/MW je 4-h-Block:

$$\pi_b = \pi^{h}_b \cdot h_b$$

mit $\pi_b$ als Leistungspreis in €/MW je 4-h-Block, $\pi^{h}_b$ als veröffentlichtem Preis in €/MW je Stunde und $h_b$ als Blockdauer, im Regelfall 4 h (bei der Zeitumstellung 3 oder 5 h). Ein aFRR-Preis von 18 €/MW je Stunde entspricht also 72 €/MW je 4-h-Block. Der Jahreserlös aus der Leistungsvorhaltung ist

$$R^{L} = \sum_{b=1}^{B} \left( \pi^{+}_{b}\, P^{+}_{b} + \pi^{-}_{b}\, P^{-}_{b} \right)$$

mit $B$ als Zahl der Blöcke im Jahr (2.190, im Schaltjahr 2.196), $\pi^{+}_{b}$ und $\pi^{-}_{b}$ als erhaltenen Leistungspreisen für positive und negative Reserve in €/MW je 4-h-Block und $P^{+}_{b}$, $P^{-}_{b}$ als bezuschlagter Leistung in MW. Setzt man den Durchschnittspreis der Zuschläge und die volle Leistung in allen Blöcken ein, ergibt sich der *Referenzwert*. Er ist weder Prognose noch Obergrenze: Ein Bieter kann bis zum Grenzpreis des Blocks erhalten, ein optimierender Speicher bietet aber nicht in jedem Block (Rechenbeispiel 3.1).

### Regelarbeit: Grenzpreis und Max/Min-Abrechnung

Für die Regelarbeit gilt seit dem Start des europäischen Zielmarktdesigns am 22.06.2022 die Vergütung zum Grenzpreis, mit Viertelstundenprodukten und einem Gebotsschluss (Gate Closure Time) 25 Minuten vor Beginn der Lieferviertelstunde; vorher galt auch hier der Gebotspreis [K03M-08, S. 3, 29 f. mit Fn. 16, 17; K03M-09, S. 14]. Die Arbeitsgebote werden in einer europäischen Merit-Order (Reihenfolge nach Preis; Kapitel 2) abgerufen: aFRR-Arbeit über die Plattform PICASSO, die den grenzüberschreitenden Grenzpreis (Cross-Border Marginal Price, CBMP) bei jeder Aktivierung, also alle vier Sekunden, ermittelt, mFRR-Arbeit über die Plattform MARI [K03M-08, S. 3, 31]. Die aFRR-Arbeit wird sekundengenau, die mFRR-Arbeit je Viertelstunde abgerechnet und je Gebot zu Viertelstundenwerten zusammengefasst [K03M-08, S. 50 mit Fn. 19, S. 51]. Für aFRR gilt eine Max/Min-Regel:

$$p^{\text{Abr},+}_{t} = \max\left(p^{\text{CBMP}}_{t};\, g^{+}\right), \qquad p^{\text{Abr},-}_{t} = \min\left(p^{\text{CBMP}}_{t};\, g^{-}\right)$$

mit $p^{\text{Abr}}_t$ als Abrechnungspreis im Zeitschritt $t$ (€/MWh), $p^{\text{CBMP}}_{t}$ als Grenzpreis von PICASSO und $g^{+}$, $g^{-}$ als eigenem Arbeitspreisgebot in positiver bzw. negativer Richtung [K03M-08, S. 51]. Die aktivierte Menge wird mit diesem Preis multipliziert; nicht gelieferte Arbeit (Untererfüllung) wird mit dem Grenzpreis bewertet und ist an den ÜNB zu zahlen [K03M-08, S. 51]. Im Regelfall gilt damit der Grenzpreis. Wird ein Anbieter außerhalb der Merit-Order abgerufen, was die ÜNB bei Verzögerungen der Optimierung als unvermeidbar bezeichnen [K03M-09, S. 19], erhält er mindestens sein positives Gebot und zahlt höchstens sein negatives (Einordnung).

### Zahlungsrichtungen

Die Leistungsvorhaltung zahlt immer der ÜNB; bei der Regelarbeit fließen Zahlungen je nach Vorzeichen von Menge und Arbeitspreis in beide Richtungen (Tabelle 3.2) [K03M-08, S. 49 f.]. Abgerechnet wird monatlich bis zum 15. Arbeitstag des Folgemonats durch den ÜNB, in dessen Regelzone die Anlage angeschlossen ist (Anschluss-ÜNB-Prinzip) [K03M-08, S. 50].

| Vorgang | Preis | Zahlung |
|---|---|---|
| Vorhaltung FCR, aFRR, mFRR | Leistungspreis | ÜNB an Anbieter |
| FCR-Aktivierung | – | keine gesonderte Vergütung |
| positive Regelarbeit (Speicher entlädt) | positiv | ÜNB an Anbieter |
| positive Regelarbeit | negativ | Anbieter an ÜNB |
| negative Regelarbeit (Speicher lädt) | positiv | Anbieter an ÜNB |
| negative Regelarbeit | negativ | ÜNB an Anbieter |
| Untererfüllung | Grenzpreis | Anbieter an ÜNB |

Table: Zahlungsströme der Regelreserve

Quelle: K03M-08, S. 31, 49–51; Zuordnung der Richtungen bei der Regelarbeit eigene Einordnung nach der Logik „Menge × Preis“; maßgeblich sind die Modalitäten für Regelreserveanbieter (MfRRA) (Stand 27.09.2026).

Für einen Speicher ist die aFRR-Arbeit schwer zu kalkulieren. Aktiviert wurden in Deutschland 2023–2026 im Mittel nur 2,5–4,5 % der zugeschlagenen Leistung, je MW vorgehaltener Leistung 221–391 MWh im Jahr. Die Verteilung ist schief: 2025 lag die aktivierte positive Leistung im Median bei 1 MW, in 10 % der Viertelstunden über 155 MW, im Maximum bei 1.587 MW (Abbildung 3.1) [M1D-07, M1D-09; M1, Lauf 20260928-kapitel03]. Der Erlös ist die Marge zwischen Abrechnungspreis und den Kosten, die Energie wieder zu beschaffen, und hängt an wenigen extremen Preisen: G1 nennt für 2025 mengengewichtete Mittelpreise von 1.640 €/MWh (positiv) und 1.478 €/MWh (negativ) bei Medianen von 245 und 266 €/MWh (G1, Kap. 5.2).

Arbeitspreise je Aktivierung sind nicht ohne Weiteres in der nötigen Auflösung verfügbar. M1 enthält die aFRR-Arbeit deshalb nicht; Annahme A-M1-09 setzt eine Marge von 0/2,5/5,0/9,1 € je MW vorgehaltener Leistung und Stunde an, wobei 9,1 € dem in G1 impliziten Wert entspricht: G1 setzt für 2027 im Szenario S3 (Mittelweg) rund 1,60 Mio. € aFRR-Arbeit an (real, Preisbasis 2025; G1, Abb. 16, abgelesen ±0,1 Mio. €), und 1,60 Mio. € / (10 MW × 2 Richtungen × 8.760 h) ≈ 9,1 € [M1, Lauf 20260928-triangulation]; enervis setzt aFRR-Arbeit in seinem Index mit null an [K06M-05]. Jeder Abruf kostet zudem Zyklen, die in die Garantieprüfung gehören (Kapitel 9): Bei der mittleren Aktivierung 2025 (221 MWh je MW) kämen R2 mit 10 MW positiver aFRR auf rund 40, R1 auf rund 110 Vollzyklen im Jahr (eigene Rechnung, je nach Platz in der Merit-Order).

![Aktivierte aFRR in Deutschland, 01/2023 bis 26.09.2026: a) Energie je Monat, positiv und negativ; b, c) Dauerlinien, also absteigend sortierte Viertelstundenmittel je Jahr (Ausschnitt bis 50 % der Viertelstunden)](05_figures/K03/03_afrr_aktivierung.png)

Quelle: netztransparenz.de, aktivierte aFRR, Viertelstundenmittel [M1D-07]; Auswertung Modell M1, Lauf 20260928-kapitel03 (Stand 28.09.2026).

### Europäische Plattformen

Die FCR-Leistung beschaffen die deutschen ÜNB gemeinsam mit anderen Ländern in der FCR-Kooperation; das Datencenter weist deren Ergebnisse mit aus [K03M-04]. Die aFRR-Leistung beschaffen Deutschland und Österreich seit dem Liefertag 01.02.2020 gemeinsam, heute in der Kooperation ALPACA, der Tschechien am 03.09.2025 beitrat [K03M-09, S. 28; K03R-02, S. 7 mit Fn. 10]. Für die Regelarbeit trat Deutschland PICASSO mit dem Start des Zielmarkts am 22.06.2022 bei, als die österreichisch-deutsche aFRR-Kooperation endete [K03M-08, S. 31; K03M-09, S. 14, 28], und MARI am 05.10.2022, dem Starttag der Plattform, als eines der ersten Länder [SYN-13].

> [!STAND]
> **Stand der Preisregeln:** Die Regeln dieses Abschnitts folgen dem ÜNB-Bericht nach Art. 60 der EU-Leitlinie über den Systemausgleich (EB-VO) vom Januar 2025 [K03M-08]. Den BNetzA-Beschluss BK6-25-033 vom 03.07.2025 (Regeln der FCR-Kooperation, u. a. Abrechnung zwischen den ÜNB; Suchauszug) [VR1-46] und die aktuelle Fassung der MfRRA haben wir nicht im Volltext geprüft. Die Preisgrenzen der Regelarbeit ändern sich: Nach der Entscheidung 09/2024 der EU-Regulierungsagentur ACER bleibt eine absolute technische Grenze von ±99.999 €/MWh bestehen; darunter gilt eine harmonisierte Grenze, die in der Übergangszeit ±15.000 €/MWh beträgt und danach, laut ÜNB ab Juli 2026, nach einem Mechanismus automatisch ausgeweitet werden kann [W2V-16; K03M-08, S. 3, 31]. Ob seit Juli 2026 eine Anpassung ausgelöst wurde, ist offen [LÜCKE: Stand der harmonisierten Preisgrenze nach 07/2026]. Vor Verwendung prüfen; Ist-Daten in Modellen nicht ohne Beleg kappen.

### Preisentwicklung 2021–2026

Tabelle 3.3 zeigt, dass es keinen einheitlichen „Regelreservepreis“ gibt. Die aFRR-Leistungspreise (positiv plus negativ) fielen vom 01.01. bis 26.09.2026 um 28 % unter den Vorjahreszeitraum, positive aFRR um 39 %, ihr Grenzpreis um 47 %, während FCR um 13 % stieg [M1D-02, M1D-03; M1, Lauf 20260928-kapitel03]. Im ersten Quartal 2026 lagen die aFRR-Durchschnittspreise 27 % (positiv) und 10 % (negativ) unter dem ersten Quartal 2025; die Primärdaten bestätigen damit einen Fachmedienbericht [K03M-14]. Die ÜNB erklären steigende Kosten der Regelleistung in sonnenreichen Zeitscheiben mit den Opportunitätskosten, die negative Day-Ahead-Preise für das Vorhalten erzeugen [K03M-08, S. 3]. Abbildung 3.2 zeigt die Monatswerte.

| Zeitraum | FCR | aFRR+ Ø | aFRR− Ø | aFRR ± Ø | aFRR+ Grenz | aFRR− Grenz |
|---|---:|---:|---:|---:|---:|---:|
| 2021 | 71,4 | 46,4 | 41,7 | 88,1 | 86,0 | 81,2 |
| 2022 | 92,4 | 53,6 | 54,6 | 108,2 | 76,6 | 86,5 |
| 2023 | 51,1 | 58,4 | 71,7 | 130,1 | 93,7 | 124,9 |
| 2024 | 65,1 | 52,6 | 43,4 | 95,9 | 72,4 | 58,1 |
| 2025 | 60,7 | 71,8 | 62,6 | 134,4 | 111,2 | 99,6 |
| 01.01.–26.09.2025 | 67,1 | 68,8 | 71,5 | 140,2 | 109,7 | 114,6 |
| 01.01.–26.09.2026 | 76,2 | 41,7 | 58,8 | 100,5 | 57,9 | 83,3 |
| Veränderung zum Vorjahreszeitraum | +13 % | −39 % | −18 % | −28 % | −47 % | −27 % |

Table: Leistungspreise FCR und aFRR 2021–2026 in €/MW je 4-h-Block (nominal)

Quelle: regelleistung.net, Ergebnisübersichten [M1D-02, M1D-03; Ergänzung 2021–2022: M1D-10, M1D-11], Auswertung Modell M1, Läufe 20260928-triangulation und 20260928-kapitel03; FCR Einheitspreis, aFRR Durchschnitts- (Ø) und Grenzpreis der Zuschläge, Mittel aller Blöcke; kreuzgeprüft mit GH-01 (Stand 28.09.2026).

![Monatsmittel der Leistungspreise für FCR (Einheitspreis) und aFRR positiv und negativ (Durchschnitts- und Grenzpreis der Zuschläge), 01/2021 bis 09/2026, in €/MW je 4-h-Block, nominal](05_figures/K03/03_leistungspreise_verlauf.png)

Quelle: regelleistung.net [M1D-02, M1D-03, M1D-10, M1D-11]; Auswertung Modell M1, Lauf 20260928-kapitel03 (Stand 28.09.2026).

## Präqualifikation von Speichern

Wer Regelreserve anbietet, muss seine Anlage bei den ÜNB präqualifizieren, also technisch nachweisen, dass sie die Produkte erbringen kann. Maßgeblich sind die Präqualifikationsbedingungen (PQ-Bedingungen) der ÜNB in der Fassung 1.05 vom 05.07.2024 [M1Q-01; K03M-08, S. 19]. Für Speicher mit begrenztem Energieinhalt entscheidet das Zeitkriterium: Für aFRR muss die verfügbare Energie je Richtung 60 Minuten der vermarkteten Leistung abdecken, gegen Ende des Vermarktungsfensters zeitanteilig weniger; für FCR muss der Ladezustand so geführt werden, dass 15 Minuten in beide Richtungen möglich bleiben, und die Anlage muss 25 % mehr Leistung ein- und ausspeisen können, als sie vermarktet, ein 10-MW-Speicher also höchstens 8 MW FCR [M1Q-01, Abschn. 2.7.1, 2.7.2, 3.1.6]. Die nötige nutzbare Energie ergibt sich aus

$$E_{\text{nutz}} \ge \frac{P^{+} \cdot t^{+}}{\eta_{d}} + \eta_{c} \cdot P^{-} \cdot t^{-}$$

mit $E_{\text{nutz}}$ als nutzbarer Energie (MWh, nutzbares SOC-Fenster, also Bereich des Ladezustands, bei Betriebsbeginn, D-021), $P^{+}$ und $P^{-}$ als vermarkteter positiver und negativer Leistung (MW), $t^{+}$ und $t^{-}$ als geforderter Erbringungsdauer (aFRR 1 h, FCR 0,25 h) sowie $\eta_{d}$ und $\eta_{c}$ als Entlade- und Ladewirkungsgrad, in M1 je $\sqrt{0{,}87} \approx 0{,}933$ (A-001, A-M1-01). Positive Reserve braucht Energie im Speicher, negative Reserve freien Platz.

Für 10 MW aFRR in beide Richtungen braucht ein Speicher 10,72 + 9,33 = 20,05 MWh nutzbar (eigene Rechnung). R1 mit 20 MWh schafft zu Betriebsbeginn rechnerisch höchstens rund 9,98 MW symmetrisch und behält dann keine Energie für Arbitrage. Sinkt die nutzbare Energie mit der Alterung auf 80 %, sind es nur noch rund 8 MW (eigene Rechnung; Degradation und Augmentierung in Kapitel 9). R2 mit 55 MWh bindet für dieselben 10 MW nur 36 % seiner Energie. Die übrigen rund 35 MWh kann er aber nur handeln, soweit Leistung frei bleibt: Bei 10 MW symmetrischer aFRR auf einem 10-MW-Anschluss ist das ganze Leistungsband gebunden (Kapitel 4). M1 hält für R2 2025 deshalb im Mittel nur 8,6/8,1 MW positive/negative aFRR vor (Rechenbeispiel 3.1). 8 MW FCR binden rund 4 MWh, mit dem 25-%-Aufschlag aber die ganze Leistung (A-M1-20).

Die Energiebänder binden den Ladezustand: Mit Regelleistung fahren R1, R2 und die G1-Konfiguration in M1 nur 0,2–0,7 äquivalente Vollzyklen je Tag, bei reiner Day-Ahead-Arbitrage 1,2–1,7 (A-M1-10) [M1, Lauf 20260928-standalone]. Weil Regelleistung je MW und nicht je MWh bezahlt wird, erlöst R2 bei perfekter Voraussicht (alle Preise im Voraus bekannt) 2025 je MW nur 10 % mehr als R1 (327,2 gegenüber 297,6 k€/MW/a), je MWh nutzbar weniger als die Hälfte (59,5 gegenüber 148,8 k€/MWh/a) [M1, Lauf 20260928-standalone].

> [!STAND]
> **Stand der Präqualifikation:** Grundlage sind die PQ-Bedingungen vom 05.07.2024 [M1Q-01]. Änderungen 2025/2026, Regeln zum Pooling (Bündeln mehrerer Anlagen) für Speicher und etwaige Vorgaben zum Ladezustand bei Viertelstundenprodukten sind nicht geprüft [LÜCKE: PQ-Bedingungen nach 05.07.2024, Pooling, Zeitkriterium bei 15-min-Geboten]. Vor Verwendung beim Vermarkter und beim ÜNB prüfen.

> [!BEISPIEL]
> **Rechenbeispiel 3.1: aFRR-Leistungserlös von R2 – Referenzwert, perfekte Voraussicht, realistischer Fall**
>
> *Ziel:* den aFRR-Leistungserlös von R2 (10 MW / 55 MWh nutzbar) für 2025 und 01.01.–26.09.2026 in drei Stufen bestimmen. Lauf-IDs: 20260928-kapitel03 (Modell M1, Version 2.0.0) mit Erlösen aus 20260928-standalone; brutto, nominal; 2026 auf ein Jahr hochgerechnet (× 365/269, A-M1-12).
>
> *Schritt 1 – Preise:* aFRR positiv plus negativ, Durchschnitt der Zuschläge: 2025 71,8 + 62,6 = 134,4 €/MW je 4-h-Block, 2026 41,7 + 58,8 = 100,5 €/MW je 4-h-Block; Grenzpreise 2025 210,8 und 2026 141,2 €/MW je 4-h-Block (Tabelle 3.3).
>
> *Schritt 2 – Referenzwert:* 134,4 €/MW × 2.190 Blöcke × 10 MW = 2,94 Mio. €/a für 2025; 100,5 × 2.190 × 10 = 2,20 Mio. €/a für 2026. Zum Grenzpreis wären höchstens 4,62 bzw. 3,09 Mio. €/a möglich. Die Präqualifikation erlaubt R2 die vollen 10 MW je Richtung.
>
> *Schritt 3 – M1:* Bei perfekter Voraussicht optimiert M1 Day-Ahead-Handel, FCR und aFRR-Leistung gemeinsam und vergütet aFRR zum Durchschnittspreis. Im realistischen Fall entscheidet M1 am Vortag auf Basis einer Vergleichstagsprognose (A-M1-05), bietet aFRR zum 0,8-Fachen des Prognosepreises mit Zuschlag nur bis zum späteren Grenzpreis und Vergütung zum Gebot (A-M1-06) und rechnet mit 97 % Verfügbarkeit (A-020).
>
> | Größe | 2025 perfekt | 2025 realistisch | 2026 perfekt | 2026 realistisch |
> |---|---:|---:|---:|---:|
> | aFRR-Leistung (k€/a) | 2.439 | 1.571 | 1.170 | 791 |
> | in % des Referenzwerts | 83 | 53 | 53 | 36 |
> | Ø vorgehaltene aFRR positiv/negativ (MW) | 8,6 / 8,1 | 7,7 / 6,8 | 6,2 / 5,6 | 6,1 / 5,0 |
> | Day-Ahead (k€/a) | 818 | 511 | 1.687 | 1.209 |
> | FCR (k€/a) | 15 | 15 | 83 | 57 |
> | Summe (k€/a) | 3.272 | 2.096 | 2.940 | 2.057 |
> | Anteil aFRR-Leistung an der Summe (%) | 75 | 75 | 40 | 38 |
>
> Table: aFRR-Leistungserlös und Erlösmix R2 (brutto, nominal)
>
> Quelle: Modell M1, Läufe 20260928-kapitel03 und 20260928-standalone; Referenzwert und Grenzpreisschranke aus regelleistung.net [M1D-03]; ohne Intraday und aFRR-Arbeit (Stand 28.09.2026).
>
> *Deutung:* 2025 verdient ein perfekt optimierender Speicher mit aFRR 83 % des Referenzwerts, 2026 nur 53 %: Er weicht vor allem in den Day-Ahead-Handel aus, dessen Erlös sich verdoppelt; FCR bleibt klein. Die Summe sinkt deshalb viel weniger als der aFRR-Preis, im realistischen Fall nur um 2 %. Realistisch erreicht M1 bei aFRR 64 % (2025) bzw. 68 % (2026) der perfekten Voraussicht (Realisierungsgrad), weil die Gebote zwar in rund 90 % der Blöcke zum Zug kommen, aber nur den eigenen Preis bringen, im Mittel rund zwei Drittel des Durchschnittspreises [M1, Lauf 20260928-standalone]. Der aFRR-Leistungserlös ist also keine feste Größe, sondern der Aufschlag über den Opportunitätskosten der anderen Märkte.

## Viertelstundenprodukte für die Regelleistung

Die Regelarbeit wird seit 2022 in Viertelstunden gehandelt, die Regelleistung bisher nur in 4-h-Blöcken. Das ändert der Beschluss BK6-25-212 der Bundesnetzagentur vom 28.10.2025: Nach der damit genehmigten Änderung der MfRRA dürfen Anbieter für aFRR- und mFRR-Leistung zusätzlich zu den weiterhin bestehenden 4-h-Produkten Gebote für einzelne, auch nicht zusammenhängende Viertelstunden abgeben [K03R-02, S. 1–4, 7; W2V-15].

Vergeben wird weiter je 4-h-Zeitscheibe, auch wegen der ALPACA-Kooperation: Die Viertelstundengebote werden in Scheiben zu 1 MW zu synthetischen 4-h-Geboten mit Durchschnittspreis zusammengesetzt, die mit den echten 4-h-Geboten konkurrieren; Viertelstundengebote, die sich nicht zu vollständigen Blöcken ergänzen lassen, erhalten eine Absage [K03R-02, S. 7–9]. Der Durchschnittspreis dient „ausschließlich als Vergleichswert“ für den Zuschlag; eine eigene Preisregel enthält der Beschluss nicht, die MfRRA-Regeln zu Vergütung und Abrechnung gelten unverändert fort [K03R-02, S. 7 mit Fn. 11; W2V-15]. Welcher Preis bei einem synthetischen Gebot gezahlt wird, ergibt sich erst aus den MfRRA [LÜCKE: Vergütung von 15-min-Geboten nach MfRRA-Volltext]. Viertelstundenprodukte für FCR und im ALPACA-Gebiet sind nicht Gegenstand des Verfahrens [W2V-15].

Die ÜNB begründen die Änderung damit, dass 4-h-Blöcke eine Hürde für Photovoltaik seien und konventionellen Anlagen und Batteriespeichern Opportunitätskosten verursachten, zumal seit dem Day-Ahead-Handel in Viertelstunden ab 01.10.2025; sie erwarten sinkende Leistungspreise [K03R-02, S. 5–6]. Die Bundesnetzagentur erwartet Viertelstundengebote auch von Batteriespeichern, die Photovoltaik-Gebote zu vollständigen Blöcken ergänzen [K03R-02, S. 12].

**Einschätzung.** Für einen Speicher erweitern Viertelstundengebote die Optionen: Er kann Leistung gezielt in den Viertelstunden anbieten, in denen der Großhandel wenig bringt, und die übrigen für Arbitrage nutzen. Zugleich wächst die Konkurrenz durch Photovoltaik, was eher preissenkend auf die aFRR-Leistung wirkt, und der Zuschlag hängt daran, dass sich synthetische Blöcke schließen (Mengenrisiko). Eine Erlöswirkung ist nicht belegt; das Buch rechnet deshalb in der Basis mit 4-h-Blöcken und führt Viertelstundengebote als Szenario (A-041).

> [!STAND]
> **Stand der Viertelstundenprodukte:** Beschluss vom 28.10.2025, Umsetzung bis spätestens 28.10.2026 mit vier Wochen Vorankündigung auf regelleistung.net; Widerrufsvorbehalt [K03R-02, S. 9, 15; W2V-15]. Bis einschließlich Liefertag 28.09.2026 weist die Ergebnisübersicht nur 4-h-Produkte aus [SYN-08]. Fachmedien nannten zuletzt einen Start ab Oktober 2026 (Entelios, 13.08.2026) [K03R-10]. Den Starttermin vor Verwendung prüfen.

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Ob bei synthetischen 4-h-Geboten der eigene Viertelstundenpreis oder der Durchschnittspreis gezahlt wird und ob für Viertelstundengebote dasselbe Zeitkriterium der Präqualifikation gilt, klären Vermarkter und ein Rechtsanwalt für Energierecht anhand der geänderten MfRRA. Der Vermarktungsvertrag (Kapitel 5) sollte regeln, wer über die Produktwahl entscheidet und wie Absagen unvollständiger Blöcke in die Leistungskennzahlen eingehen.

## Mengengerüst: Bedarf gegenüber Speicherflotte und Sättigung

Ob Regelreserve-Erlöse tragen, entscheidet das Mengengerüst: die ausgeschriebene Leistung je Produkt gegenüber der Leistung, die Speicher und andere Anlagen anbieten. Tabelle 3.5 stellt beides gegenüber; drei Befunde folgen daraus.

Erstens ist der Markt klein. Die in Deutschland zugeschlagene aFRR-Leistung lag 2023–2026 stabil bei rund 1,8–1,9 GW je Richtung (Stichprobe), angeboten wurden 2026 im Mittel 4,4 GW positive und 3,8 GW negative Leistung [M1D-03, M1D-09; M1, Lauf 20260928-kapitel03]. Dazu kommen 584 MW FCR für Deutschland. Modo beziffert den deutschen Markt für FCR und aFRR auf rund 4,5 GW [K06M-02, K06M-04]; das passt zur Summe der Zuschlagsmengen (eigene Rechnung). Diese Summe zählt jede Richtung einzeln. Weil ein Speicher dieselbe Leistung zugleich positiv und negativ vorhalten kann, genügen rund 2,5–2,7 GW Speicherleistung (1,9 GW aFRR je Richtung und 0,6 GW FCR, mit dem 25-%-Aufschlag 0,7 GW), um den deutschen Bedarf zu decken (eigene Rechnung). Ein Projekt mit 10 MW ist rund 0,5 % der aFRR-Menge je Richtung, ein Portfolio wie R4 mit 15 × 10 MW rund 8 %, genug, um mit eigenen Geboten Preise zu bewegen (Einschätzung; A-M1-11).

Zweitens wächst die präqualifizierte Batterieleistung schnell. Für aFRR stieg sie von 0,33 GW (02/2024) auf 1,20 GW je Richtung (01.01.2026), von 17–18 % auf 62–66 % der Zuschlagsmenge (eigene Rechnung), für FCR von 0,81 auf 1,35 GW (Tabelle 3.5) [K03M-02]. Präqualifiziert heißt aber nicht angeboten: Eine Anlage kann für mehrere Produkte zugelassen sein, ihre Leistung jedoch nur einmal vermarkten, und die Werte je Produkt dürfen nicht addiert werden [K03M-02]. Insgesamt sind für positive aFRR 24,9 GW präqualifiziert, vor allem Wasserkraft und Gaskraftwerke [K03M-02]. Am 15.10.2025 waren 2,4 GW Großspeicher in Betrieb und 5,0 GW in Planung [K03M-07]; Modo erwartete im April 2026 für 2030 einen Bestand von 15,4 GW [K06M-03].

Drittens reagieren die Preise, aber nicht linear. 2025 stiegen die aFRR-Preise trotz fast verdoppelter Batterie-PQ, 2026 fielen sie um 28 %, während FCR teurer wurde (Tabelle 3.3). Zwei Kräfte wirken gegeneinander: Mehr Angebot drückt die Preise, höhere Opportunitätskosten heben sie (Einordnung; Rechenbeispiel 3.1).

| Größe | 2024 | 2025 | 2026 | 2030 |
|---|---|---|---|---|
| aFRR-Zuschlagsmenge DE, Ø positiv/negativ (GW) | 1,93 / 1,77 | 1,91 / 1,80 | 1,93 / 1,81 | n. v. |
| aFRR angeboten DE, Ø positiv/negativ (GW) | 4,38 / 3,57 | 4,26 / 3,63 | 4,42 / 3,76 | n. v. |
| Batterie-PQ aFRR positiv/negativ (GW) | 0,33 / 0,31 (02/2024) | 0,56 / 0,55 (03/2025) | 1,20 / 1,20 (01/2026) | n. v. |
| Batterie-PQ in % der Zuschlagsmenge | 17 / 18 | 29 / 31 | 62 / 66 | – |
| FCR-Bedarf DE (MW) | 564 | 528 | 584 | n. v. |
| Batterie-PQ FCR (GW) | 0,81 (02/2024) | 0,94 (03/2025) | 1,35 (01/2026) | n. v. |
| Großspeicher in Betrieb (GW) | n. v. | 2,4 (15.10.2025) | n. v. | 15,4 (Modo, Prognose) |

Table: Bedarf an Regelreserve gegenüber Speicherflotte

Quelle: K03M-02 (Batterie-PQ); regelleistung.net [M1D-02, M1D-03, M1D-09], Auswertung Modell M1, Lauf 20260928-kapitel03 (Zuschlagsmenge: Stichprobe 1. und 15. je Monat, nur deutsche Gebote; 2026 bis 26.09.; seit 10/2025 weist die Ergebnisübersicht die Menge vollständig aus, 2026: 2,03/1,86 GW, damit 59–65 %); K03M-07; K06M-03 (Stand 30.04.2026); Anteile eigene Rechnung; n. v. = nicht verfügbar; PQ-Werte nicht über Produkte addierbar (Stand 28.09.2026).

![Präqualifizierte Batterieleistung (GW, Stand je Punkt) gegenüber dem mittleren Leistungspreis im Quartal des Stands, a) aFRR, b) FCR; Linien: Mittel 2023–2026 der Zuschlagsmenge bzw. des deutschen FCR-Bedarfs, Großspeicherflotte](05_figures/K03/03_saettigung.png)

Quelle: K03M-02; K03M-07; regelleistung.net [M1D-02, M1D-03, M1D-09]; Auswertung Modell M1, Lauf 20260928-kapitel03; FCR wird in der Kooperation beschafft (Stand 28.09.2026).

**Einschätzung zur Sättigung.** Abbildung 3.3 zeigt bisher Punkte, keine Kurve: Bei aFRR positiv stieg der Quartalspreis von 22,8 (Q1 2024) auf 50,9 (Q1 2025) und fiel auf 37,0 €/MW je 4-h-Block (Q1 2026), während der Batterieanteil an der Quartalsmenge von 17 über 30 auf 62 % wuchs [M1, Lauf 20260928-kapitel03]. Wir erwarten, dass sich die aFRR-Leistungspreise mit wachsender Flotte den Opportunitätskosten der Speicher annähern. Dann schrumpft der Aufschlag der Regelreserve über der Arbitrage, der Gesamterlös weniger, solange die Spreads halten; Rechenbeispiel 3.1 zeigt dieses Ausweichen schon 2026.

Wann die Sättigung eintritt, hängt an Teilnahmequote und Abgrenzung. Modo nimmt seit Juli 2026 an, dass nur rund die Hälfte der neuen Speicherleistung an Systemdienstleistungen teilnimmt [VR2-20]; Anfang 2026 war ebenfalls rund die Hälfte des Bestands für aFRR präqualifiziert (1,20 von 2,4 GW, Stichtage verschieden) [K03M-02, K03M-07]. Rechnet man in Speicherleistung (2,5–2,7 GW), wäre der Bedarf damit bei rund 5 GW installierter Leistung gedeckt, dem Bestand, den Modo für Ende 2026 erwartet [K06M-02]; in der Modo-Abgrenzung mit 4,5 GW Marktgröße erst bei rund 9 GW (eigene Rechnung, Größenordnung). Die engere Schwelle wäre damit um 2027 erreicht, die weitere vor 2030. Für einen Fonds folgt daraus: Regelreserve-Erlöse ab 2027 gehören in einen Sättigungspfad mit Mengen- und Preisannahme und einer Zuschlagsquote als Sensitivität (A-023), nicht in eine Fortschreibung des Ist-Niveaus. Wie Anbieter das modellieren, behandelt Kapitel 6; den Vergleichsmarkt Großbritannien, wo die Speichererlöse schon 2022–2024 deutlich fielen (Suchauszug) [VR2-25], Kapitel 26.

> [!BEISPIEL]
> **Rechenbeispiel 3.2: Wie viel aFRR-Leistungserlös unterstellt G1?**
>
> *Ziel:* den aFRR-Leistungsansatz des Erlösgutachtens G1 (anonymisiert) für 2027 am Referenzwert messen (Prüfpunkte P1, P2, P17). Lauf-ID: 20260928-kapitel03 (Modell M1) mit Erlösen der G1-Konfiguration (10 MW / 49,5 MWh nutzbar) aus 20260928-standalone; M1 brutto, nominal; G1 real, Preisbasis 2025.
>
> *Schritt 1 – Referenzwert:* Mit den G1-Preisen 2025 von 72 €/MW (positiv) und 62 €/MW (negativ) je 4-h-Block (G1, Kap. 5.2) ergeben sich (72 + 62) × 2.190 × 10 MW ≈ 2,93 Mio. €/a, mit dem Ist-Jahresmittel 2025 2,94 Mio. €/a [M1D-03]; die G1-Basis entspricht dem Ist.
>
> *Schritt 2 – G1-Ansatz:* Für 2027 (S3, im Buch Basisfall) setzt G1 rund 2,40 Mio. € aFRR-Leistungserlös an (G1, Abb. 16, abgelesen ±0,1 Mio. €), 82 % des Referenzwerts. Dafür muss die Anlage in fast jedem Block 10 MW je Richtung bezuschlagt bekommen, wie G1 unterstellt (G1, Kap. 7.1), und das Preisniveau 2025 muss halten.
>
> *Schritt 3 – Preisniveau 2026:* Zum Durchschnittspreis 01.01.–26.09.2026 beträgt der Referenzwert 2,20 Mio. €/a; der G1-Ansatz liegt 9 % darüber und verlangte Zuschläge in fast allen Blöcken zu rund 110 statt 100,5 €/MW je 4-h-Block (Schranke zum Grenzpreis 3,09 Mio. €/a).
>
> *Schritt 4 – optimierender Speicher:* M1 verdient mit der G1-Konfiguration bei perfekter Voraussicht 2025 2,48 Mio. € mit aFRR-Leistung, etwas mehr als der G1-Ansatz, zu Preisen 2026 nur 1,21 Mio. €/a, im realistischen Fall 1,60 bzw. 0,82 Mio. €/a [M1, Lauf 20260928-kapitel03].
>
> *Deutung:* Für 2025 ist der G1-Ansatz mit einem perfekt optimierenden Speicher vereinbar, für das Preisniveau 2026 nicht mehr (P17). Dass Speicher auch 2027 in fast jedem Block zum Zug kommen (P1) und der Wettbewerb nur über einen gesetzten Preisfaktor wirkt (P2), stellt das Mengengerüst dieses Abschnitts in Frage. Die vollständige Nachrechnung steht in Rechenbeispiel 6.2.

## Momentanreserve, Blindleistung, Redispatch und weitere Systemdienstleistungen

**Momentanreserve.** Rotierende Maschinen geben bei einem Frequenzeinbruch sofort und ohne Regelung Energie aus ihrer Trägheit ab; diese Momentanreserve wirkt vor der FCR. Batteriespeicher können sie nur mit netzbildenden Umrichtern bereitstellen, die dieses Verhalten nachbilden [VR3-39]. Seit 22.01.2026 beschaffen die ÜNB Momentanreserve marktgestützt nach § 12h EnWG und der Festlegung BK6-23-010 vom 22.04.2025, in vier Produkten (positiv und negativ, jeweils Basis und Premium) [K03M-05, K03M-06, VR3-39]. Statt einer Auktion gelten bundesweit einheitliche Festpreise, bei Angebot ohne Indexierung für die Vertragslaufzeit von 2 bis 10 Jahren gesichert (erste Preisperiode bis 21.01.2028, vorher anpassbar): Premium höchstens 888,50, Basis höchstens 109,50 €/MWs/a, je nach Verfügbarkeit; unter 90 % (Premium) bzw. 30 % (Basis) entfällt die Vergütung [K03M-06; K03M-29, Nr. 1.1, 1.6, 5.3, 5.11, 6.2; K03M-40, Abschn. 4.2]. Die Einheit Megawattsekunde (MWs) misst Energie: 1 MWs ist 1 MW während einer Sekunde. Bezahlt wird je Jahr die Energie, die eine Anlage augenblicklich bereitstellen kann:

$$R^{\text{MR}} = E_{\text{MR}} \cdot FP$$

mit $R^{\text{MR}}$ als Jahreserlös bei voller Verfügbarkeit (€/a), $E_{\text{MR}}$ als anrechenbarer Momentanreserve (MWs) und $FP$ als Festpreis (€/MWs/a). Anrechenbar sind höchstens 12,5 MWs je MW Nennleistung und Richtung (halbe Anlaufzeitkonstante von höchstens 25 s mal Nennleistung), und dafür muss in jeder Viertelstunde Leistung frei bleiben [K03M-29, Nr. 3.4, 3.8, 4.3, 4.12]; Einzelheiten in Kapitel 15. Modo nannte im März 2026 8–20 k€/MW/a für Speicher mit netzbildendem Umrichter [K06M-02]; zum Premium-Preis entspräche das rund 9–23 MWs je MW über beide Richtungen (eigene Rechnung). Einschätzung: Momentanreserve ist eine Option für neue Projekte, deren Wert von den Mehrkosten des Umrichters (Kapitel 7, 8), der anrechenbaren Menge, der erreichbaren Verfügbarkeit und dem Angebotszeitpunkt abhängt. Für R1 und R2 setzt das Buch im Basisfall null an.

**Blindleistung.** Blindleistung hält die Spannung im Netz. Nach der Festlegung BK6-23-072 vom 25.06.2024 beschaffen die ÜNB und Verteilnetzbetreiber mit Hochspannungsnetz sie marktgestützt, soweit sie über die technischen Anschlussregeln hinausgeht; Betreiber von Nieder- und Mittelspannungsnetzen sind ausgenommen, und die Bundesnetzagentur erwartet ein kleines Marktvolumen (Suchauszug) [K03R-08]. R1 und R2 sind in der Mittelspannung angeschlossen; im Basisfall erzielen sie keinen Blindleistungserlös (Einschätzung).

**Redispatch und „Nutzen statt Abregeln“.** Beides sind Instrumente gegen Netzengpässe (Kapitel 15). Nach § 13k EnWG dürfen nur registrierte zusätzliche zuschaltbare Lasten in Entlastungsregionen teilnehmen, also dort, wo sie sonst abgeregelten Strom abnehmen; ob ein Batteriespeicher selbst Entlastungsanlage sein kann, regelt der Wortlaut nicht ausdrücklich [W2V-07]. Entlastungsregionen gibt es nach dem Umsetzungskonzept der ÜNB vom 01.04.2026 derzeit nur in den nördlichen Gebieten von 50Hertz und TenneT; TransnetBW und Amprion halten eine spätere Ausweisung für möglich bzw. notwendig [VR3-32, S. 17–18]. Für R1 und R2 im Raum Stuttgart bringt § 13k im Basisfall nichts. Ob und wie Speicher für Schwarzstartfähigkeit (Netzwiederaufbau nach einem Ausfall) vergütet werden, ist nicht geprüft [LÜCKE: Schwarzstart – Beschaffung und Zugang für Speicher].

Tabelle 3.6 fasst den Stand aller Segmente zusammen.

| Segment | Status | Datum | Zugang für R1/R2 | Erlös R1/R2 im Basisfall |
|---|---|---|---|---|
| FCR-Leistung (4-h-Block) | in Kraft | laufend | ja, PQ 15 min, höchstens 8 MW | ja; Preise 2026 gestiegen |
| aFRR-Leistung (4-h-Block) | in Kraft | laufend | ja, PQ 60 min | ja; Preise 2026 −28 % |
| aFRR-/mFRR-Leistung, Viertelstundengebote | beschlossen | 28.10.2025; Umsetzung bis 28.10.2026 | ja | Szenario (A-041) |
| Regelarbeit aFRR (PICASSO), mFRR (MARI) | in Kraft | seit 22.06.2022 | ja | nicht in M1; Marge 0–9,1 €/MW je Stunde (A-M1-09) |
| Momentanreserve | in Kraft | seit 22.01.2026; Festpreis bei Angebot bis 21.01.2028 für die Vertragslaufzeit gesichert | nur mit netzbildendem Umrichter; in MS mit Zustimmung des Netzbetreibers | 0; Option |
| Blindleistung | in Kraft | Festlegung 25.06.2024 | MS-Netzbetreiber beschaffen nicht marktgestützt; Teilnahme von MS-Anlagen bei ÜNB/HS-Netzbetreibern offen | 0 |
| § 13k „Nutzen statt Abregeln“ | in Kraft; Umsetzungskonzept der ÜNB | Konzept 01.04.2026 | derzeit keine Entlastungsregion bei TransnetBW | 0 (Kapitel 15) |
| Schwarzstart | nicht geprüft | – | – | Lücke |
| Kapazitätsmarkt: Langzeitkapazitäten | in Kraft; EU-Genehmigung 02.09.2026, Umfang ungeprüft | Gebotstermine 08.09. und 29.12.2026 | nein (≥ 10 h) | 0 |
| Kapazitätsmarkt: Erzeugungskapazitäten | in Kraft; EU-Genehmigung 02.09.2026, Umfang ungeprüft | Gebotstermin 18.05.2027 | formal ja (§ 2 Nr. 10); für R1/R2 mit Inbetriebnahme 2027 praktisch nein (Mindestinvestition nach Zuschlag, § 14; Lesart) | 0 (A-040) |
| Kapazitätsmarkt: Kapazitäten | in Kraft; EU-Genehmigung 02.09.2026, Umfang ungeprüft | 01.12.2027, 01.10.2029; Lieferung ab 01.11.2031 | ja; Reduktionsfaktor offen | Upside ab 11/2031 |

Table: Statusübersicht der Segmente für Standalone-Speicher R1 und R2

Quelle: K03M-06, K03M-08, K03M-29, K03R-01, K03R-02, K03R-08 (Suchauszug), M1Q-01, VR3-32, VR3-39, W0R-10, W0R-11, W2V-07, W2V-15; ANNAHMEN A-040, A-041, A-M1-09; eigene Einordnung; MS/HS = Mittel-/Hochspannung (Stand 28.09.2026).

> [!STAND]
> **Stand der Systemdienstleistungen:** Preisperiode der Momentanreserve bis 21.01.2028, Mengenveröffentlichung ab Q1/2027 [K03M-06, K03M-29]; Blindleistung nur als Suchauszug belegt [K03R-08]; Zielmodell nach § 13k laut ÜNB-Konzept ab 01.10.2026 [VR3-32]. Vor Verwendung prüfen.

## Kapazitätsmarkt und Zugang für Speicher

**Gesetz und Zeitplan.** Mit dem Strom-Versorgungssicherheits-und-Kapazitätengesetz (StromVKG), ausgefertigt am 21.07.2026, führt Deutschland einen zentralen Kapazitätsmarkt ein: Die Bundesnetzagentur schreibt gesicherte Leistung für den Erbringungszeitraum 01.11.2031 bis 31.10.2032 aus; die Verpflichtungen laufen in Verpflichtungsjahren ab dem 01.11.2031 [K03R-01, §§ 1, 2 Nr. 9, 41, § 3]. Bezuschlagte Anbieter erhalten eine Kapazitätsvergütung in Höhe ihres eigenen Gebotswerts je MW reduzierter Leistung und Jahr [K03R-01, § 2 Nr. 15, 22, § 74 Abs. 1]. Die reduzierte Leistung ist die gebotene nominale Leistung mal einem Reduktionsfaktor, der den gesicherten Beitrag einer Technologie in Knappheitsstunden abbildet [K03R-01, § 2 Nr. 30, § 22]:

$$V = GW \cdot P_{\text{red}} = GW \cdot P_{\text{nom}} \cdot RF$$

mit $V$ als Kapazitätsvergütung (€/a), $GW$ als Gebotswert (€/MW reduzierter Leistung und Jahr), $P_{\text{red}}$ als reduzierter Leistung (MW), $P_{\text{nom}}$ als gebotener nominaler Leistung (MW) und $RF$ als Reduktionsfaktor. Stromspeicheranlagen gelten als Erzeugungsanlagen und gehören zu den energiebegrenzten Technologieklassen; ihr Reduktionsfaktor hängt an der Höchsterbringungsdauer, den vollen Stunden, in denen sie die gebotene nominale Leistung ins Netz einspeisen können [K03R-01, § 2 Nr. 4, 10, 18, 37, § 22 Abs. 3]. Tabelle 3.7 zeigt die drei Ausschreibungsarten.

| Merkmal | Langzeitkapazitäten | Erzeugungskapazitäten | Kapazitäten |
|---|---|---|---|
| Gebotstermine | 08.09.2026, 29.12.2026 | 18.05.2027 | 01.12.2027, 01.10.2029 |
| Volumen | je 4,5 GW | 2 GW | nach Anlage 1; 2027: 75 %, 2029: 100 % |
| Zugelassen | Erzeugungsanlagen mit 10 h zu 80 % der installierten Leistung | sämtliche Erzeugungsanlagen | Erzeugungsanlagen und regelbare Lasten |
| Standortkriterium (§ 12 Abs. 3) | ja | ja | nein |
| Verpflichtungszeitraum | 15 Jahre | 15 Jahre | 1, 7 oder 15 Jahre |
| Mindestinvestition (§ 14) | 431.000 €/MW red. | 431.000 €/MW red. | 7 Jahre: 201.000, 15 Jahre: 431.000 €/MW red. |
| Höchstwert (§ 39) | 244.000 €/MW red./a | 244.000 €/MW red./a | je Laufzeit durch die BNetzA |
| Reduktionsfaktor Speicher | Anlage 4, erst ab 10 h | Anlage 3, je Höchsterbringungsdauer, Mittel über 15 Jahre | Anlage 3, je Höchsterbringungsdauer |

Table: Ausschreibungen nach dem StromVKG

Quelle: K03R-01, §§ 3–6, 12–14, 23, 39, Anlagen 1, 3, 4 (Volltextauszug vom 27.09.2026); red. = reduzierte Leistung (Stand 27.09.2026).

**Langzeitkriterium.** Für Langzeitkapazitäten zugelassen sind nur Anlagen, die mindestens 10 aufeinanderfolgende Stunden 80 % ihrer installierten Leistung einspeisen können; energiebegrenzte Anlagen müssen das „jederzeit spätestens nach 3 Stunden“ können [K03R-01, § 12 Abs. 5]. Ein 10-MW-Speicher braucht also 80 MWh am Netzverknüpfungspunkt (Anschlusspunkt ans Netz), nach A-M1-01 rund 86 MWh nutzbar. R1 (18,7 MWh am Netzverknüpfungspunkt), R2 (51,3 MWh) und G1 (46,2 MWh) scheiden aus, auch mit kleinerem Gebot, weil das Kriterium an der installierten Leistung ansetzt (eigene Rechnung). Anlage 4 gibt Batterien Reduktionsfaktoren erst ab 10 Stunden Höchsterbringungsdauer, von 0,58 bei 10 h bis 0,89 bei 24 h, bei einem technischen Verfügbarkeitsfaktor von 1,00 und einem Zyklenwirkungsgrad von 0,92; Gas- und Dampfturbinenkraftwerke erhalten 0,85, Photovoltaik 0,02 [K03R-01, Anlage 4].

**Höchsterbringungsdauer und Reduktionsfaktor.** Bei 10 MW beträgt die Höchsterbringungsdauer für R1 1 h, für R2 5 h und für G1 4 h; mit 9 MW Gebot käme R1 auf 2 h (eigene Rechnung; wo gemessen wird, ist eine Auslegungsfrage). Die Faktoren nach Anlage 3 für die übrigen Segmente ermittelt die Bundesnetzagentur aus dem Versorgungssicherheitsmonitoring und veröffentlicht sie spätestens sechs Wochen vor der Bekanntmachung einer Ausschreibung; für 2027 darf sie eine vereinfachte Formel nutzen [K03R-01, § 23 Abs. 1, Anlage 3 Nr. 2.2.3]. Für Speicher mit 1–9 h liegen sie noch nicht vor [LÜCKE: Reduktionsfaktoren nach Anlage 3 für Batterien mit 1–9 h].

**Pflichten.** Bei Verpflichtungen über 7 oder 15 Jahre muss der Bieter nach dem Zuschlag bis zum Abschluss der vorläufigen Präqualifizierung 201.000 bzw. 431.000 € je MW reduzierter Leistung in die Anlage investieren; angerechnet werden nur Investitionen nach dem Zuschlag (bei Langzeitkapazitäten auch der letzten 12 Monate davor) [K03R-01, § 14, Anlage 5]. Nach unserer Lesart kommen für einen Speicher, der 2027 in Betrieb geht, damit nur einjährige Verpflichtungen in Betracht, sofern er nicht erweitert wird (Einschätzung). Anders bei Projekten, die erst nach dem Zuschlag gebaut werden: Ihre Errichtung zählt als Neuinvestition, sodass auch 7- oder 15-jährige Verpflichtungen in Betracht kommen; Modernisierungen zählen erst 25 Jahre nach Inbetriebnahme [K03R-01, Anlage 5 Nr. 2.3.1, 2.3.3].

Im Verpflichtungszeitraum muss der Anbieter die gebotene nominale Leistung verfügbar halten; der ÜNB prüft das in allen Hochpreisviertelstunden, in denen der Day-Ahead-Preis den täglich ermittelten Aktivierungspreis (unten) übersteigt [K03R-01, §§ 65, 66 Abs. 2]. Der Verfügbarkeitsindikator berücksichtigt bei Speichern Ladezustand, Regenerationszeiten zwischen Hochpreisphasen, Zyklenwirkungsgrad und technischen Verfügbarkeitsfaktor; vorgehaltene positive Regelleistung und abgerufene negative Regelarbeit werden der erbrachten Energie zugerechnet [K03R-01, Anlage 6 Nr. 1, 3.2.2]. Fehlmengen kosten Ausgleichszahlungen, je Monat höchstens anteilig das Doppelte der Kapazitätsvergütung [K03R-01, § 76 Abs. 2, 3]. Scheitert die Realisierung, fällt eine Pönale von 1,5 Gebotswerten (15 Jahre) bzw. einem Gebotswert (7 Jahre) je MW reduzierter Leistung an [K03R-01, § 64]. Bei 15-Jahres-Verträgen müssen Anlagen ab 10 MW oder mit Hochspannungsanschluss zudem Momentanreserve bereitstellen, bei Batteriespeichern zählt nur Umrichterleistung oberhalb von 130 % der vereinbarten Netzanschlusskapazität [K03R-01, § 16 Abs. 1, 2].

**Preisspitzenausgleich.** Der Kapazitätsverpflichtete zahlt dem ÜNB „unabhängig vom tatsächlichen Betrieb“ für jede Viertelstunde, in der der Day-Ahead-Preis den anlagenspezifischen Ausübungspreis übersteigt, das Produkt aus gebotener reduzierter Leistung und Preisüberschreitung [K03R-01, § 81 Abs. 2, 3; § 2 Nr. 34]:

$$A = P_{\text{red}} \cdot \sum_{v} \max\left(0;\; p_v - K_v\right) \cdot \Delta t$$

mit $A$ als Preisspitzenausgleich (€), $P_{\text{red}}$ wie oben, $p_v$ als Day-Ahead-Preis der Viertelstunde $v$ (€/MWh), $K_v$ als Ausübungspreis (€/MWh) und $\Delta t$ als Zeitfaktor. Das Gesetz nennt keinen Zeitfaktor. Wir lesen den Ausgleich als Betrag je Viertelstunde, also reduzierte Leistung × Preisüberschreitung × 0,25 h. Bei wörtlicher Lesung ohne Zeitfaktor wäre er viermal so hoch (Auslegung).

Der Aktivierungspreis bildet die tagesaktuellen variablen Kosten einer offenen Gasturbine nach, mit 37 % Wirkungsgrad, dem Erdgas-Spotpreis (mit dem Faktor 0,903 auf den unteren Heizwert umgerechnet), einem CO₂-Faktor von 201,6 g/kWh und dem CO₂-Preis, dazu 50 €/MWh übrige Kosten und ein Abstand von 150 €/MWh; der Ausübungspreis berücksichtigt zusätzlich arbeitsbezogene Einspeise-Netzentgelte [K03R-01, Anlage 7 Nr. 1–3]. Mit den Brennstoffpreisen von G1 (Erdgas 32 €/MWh, CO₂ 65 €/t; G1, Tab. 8) liegt der Aktivierungspreis überschlägig bei rund 330 €/MWh: Brennstoff 32 / 0,903 / 0,37 ≈ 96, CO₂ 0,2016 t/MWh / 0,37 × 65 €/t ≈ 35, übrige Kosten 50 und Abstand 150 €/MWh (eigene Schätzung mit den konstanten Modellannahmen von G1, Preisbasis 2025; Gaspreis wie im Gesetz auf den oberen Heizwert bezogen [K03R-01, § 2 Nr. 33]). Je 10 €/MWh Gaspreis ändert sich der Wert um rund 30 €/MWh, je 10 €/t CO₂ um rund 5 €/MWh.

**Wirtschaftliche Lesart (Einordnung).** Der Anbieter verkauft dem System eine Kaufoption auf den Spotpreis mit dem Ausübungspreis als Basispreis; die Kapazitätsvergütung ist die Prämie (Zuverlässigkeitsoption). Ein Speicher, der in Hochpreisviertelstunden entlädt, gibt auf der reduzierten Leistung den Erlös oberhalb des Ausübungspreises ab; ist er leer oder anders gebunden, zahlt er trotzdem. Er tauscht also Spitzenerlöse gegen eine feste Zahlung. Der Ausgleich wird monatlich abgerechnet, die Vergütung erst binnen 60 Werktagen nach Ende eines Verpflichtungsjahres gezahlt [K03R-01, § 74 Abs. 3, § 82]. Für einen Mitte 2027 in Betrieb genommenen Speicher beginnt die Verpflichtung im fünften Betriebsjahr, die erste Kapazitätszahlung fließt frühestens Anfang 2033 (eigene Rechnung).

**Beihilfevorbehalt.** Die Europäische Kommission hat die Beihilfe am 02.09.2026 genehmigt [W0R-10]. Nach § 87 dürfen die Vorschriften zu Volumen und Terminen, Teilnahme, reduzierter Leistung, Zuschlag, Verfügbarkeit und Zahlungen nur nach Maßgabe dieser Genehmigung angewandt werden [K03R-01, § 87]. Ob sie alle Segmente abdeckt, haben wir nicht geprüft [LÜCKE: Umfang der Beihilfegenehmigung vom 02.09.2026].

**Vergleichsmarkt Italien.** Italien schreibt Speicherkapazität zentral aus (MACSE) und vergütet je MWh: In der ersten Auktion (30.09.2025, Lieferjahr 2028) wurden 10 GWh zu durchschnittlich 12.959 €/MWh/a vergeben [K05M-18], bei im Mittel rund 6,7 h Speicherdauer rund 87 k€/MW/a (eigene Rechnung; Kapitel 5, 26).

> [!STAND]
> **Stand Kapazitätsmarkt:** StromVKG ausgefertigt am 21.07.2026 (BGBl. 2026 I Nr. 210a), EU-Genehmigung am 02.09.2026 [K03R-01, W0R-10]. Erster Gebotstermin für Langzeitkapazitäten am 08.09.2026 (Eckdaten in Tabelle 3.7); Zuschläge bis 03.11.2026; der zweite Termin wird am 10.11.2026 bekanntgemacht [W0R-10, W0R-11]. Fachmedien melden eine deutliche Überzeichnung (Suchauszug) [W0R-12]; Umweltverbände haben Beschwerde bei der Kommission eingelegt (Suchauszug) [W0R-14]. Reduktionsfaktoren nach Anlage 3 und Höchstwerte für Kapazitäten veröffentlicht die Bundesnetzagentur vor den Terminen 2027. Vor Verwendung prüfen.

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Ein Rechtsanwalt für Energie- und Beihilferecht sollte klären, (1) ob ein Batteriespeicher an der Ausschreibung für Erzeugungskapazitäten vom 18.05.2027 praktisch teilnehmen kann, einschließlich Standortkriterium (§ 12 Abs. 3), Mindestinvestition nach dem Zuschlag (§ 14, Anlage 5) und Momentanreservepflicht (§ 16); (2) ob Bestandsspeicher nur einjährige Verpflichtungen eingehen können und ob Investitionen zur Erfüllung von § 16 (Anlage 5 Nr. 2.4) allein anrechenbar sind; (3) wie Verfügbarkeitspflicht und Preisspitzenausgleich mit Regelreserve und Arbitrage zusammenwirken (Anlage 6 Nr. 3.2.2), ob der Vermarktungsvertrag das abbildet und mit welchem Zeitfaktor der Preisspitzenausgleich je Viertelstunde zu berechnen ist; (4) wo die Höchsterbringungsdauer gemessen wird und ob ein kleineres Gebot eine höhere Dauerklasse begründen darf; (5) welchen Umfang die Beihilfegenehmigung hat (§ 87). Ein technischer Berater prüft Verfügbarkeitsfaktor und Zyklenwirkungsgrad der Anlage gegenüber den Werten der Bundesnetzagentur.

> [!BEISPIEL]
> **Rechenbeispiel 3.3: Kann R2 am Kapazitätsmarkt teilnehmen, und was kostet der Preisspitzenausgleich?**
>
> *Ziel:* Zugang und Gegenleistung für R2 illustrieren (keine Prognose); eigene Rechnung nach StromVKG [K03R-01], Day-Ahead-Auswertung aus Modell M1, Lauf 20260928-kapitel03 (Version 2.0.0), brutto, nominal; 2026 = 01.01.–26.09.2026, annualisiert.
>
> *Schritt 1 – Langzeitkapazitäten:* nötig 10 h × 0,8 × 10 MW = 80 MWh am Netzverknüpfungspunkt; R2 liefert 55 × 0,933 = 51,3 MWh und ist ausgeschlossen.
>
> *Schritt 2 – Kapazitäten ab 01.12.2027:* Höchsterbringungsdauer bei 10 MW: 51,3 / 10 = 5,1, also 5 h; bei 8,55 MW Gebot 6 h. Die reduzierte Leistung ist 10 MW × RF(5 h) bzw. 8,55 MW × RF(6 h); beide Faktoren sind noch nicht veröffentlicht. Als Bestandsanlage kommt nach unserer Lesart nur eine einjährige Verpflichtung ohne Mindestinvestition in Frage.
>
> *Schritt 3 – Ausübungspreis:* ohne Einspeiseentgelte gleich dem Aktivierungspreis, überschlägig rund 330 €/MWh (Schätzung oben); M1 rechnet mit festen Schwellen $S$ von 300 und 350 €/MWh. Über 350 €/MWh lag der Day-Ahead-Preis 2025 in 12 Stunden und 27 Viertelstunden, vom 01.01. bis 26.09.2026 in 102 Viertelstunden.
>
> *Schritt 4 – Ausgleich je MW reduzierter Leistung:* $\sum \max(0;\, p_v - S) \cdot \Delta t$ über alle Zeitschritte (bis 30.09.2025 Stunden mit $\Delta t$ = 1 h, danach Viertelstunden mit 0,25 h) ergibt bei $S$ = 300/350 €/MWh 7,6/5,7 k€/MW/a (2024), 2,6/1,2 k€/MW/a (2025) und 6,8/4,7 k€/MW/a (2026, annualisiert). Stundenwerte glätten Viertelstundenspitzen; 2024/2025 ist der Ausgleich daher eher unterschätzt.
>
> *Schritt 5 – Spitzenerlös von R2:* In Zeitschritten über $S$ = 300 bzw. 350 €/MWh verdiente R2 mit dem Day-Ahead-Handel 2025 104 bzw. 60 k€/a (13 bzw. 7 % des Day-Ahead-Erlöses), 2026 225 bzw. 164 k€/a (13 bzw. 10 %).
>
> *Schritt 6 – Schwelle für das Gebot:* Die Teilnahme lohnt, wenn
>
> $$GW \ge \frac{A}{P_{\text{red}}} + k_{\text{SOC}} + k_{\text{Pön}}$$
>
> mit $A / P_{\text{red}}$ als erwartetem Ausgleich (Schritt 4), $k_{\text{SOC}}$ als Kosten der Ladezustandsreserve in Hochpreisphasen und $k_{\text{Pön}}$ als erwarteter Pönale, jeweils in €/MW reduzierter Leistung und Jahr. Der Reduktionsfaktor kürzt sich heraus, bestimmt aber die Vergütung je MW nominal ($GW \cdot RF$).
>
> Quelle: K03R-01, §§ 2, 12, 14, 22, 81, Anlage 7; Modell M1, Lauf 20260928-kapitel03, Zusammenfassung, Tabelle 5; A-M1-01; eigene Rechnung (Stand 28.09.2026).
>
> *Deutung:* Zu den Preisen 2024–2026 kostet der Preisspitzenausgleich je MW reduzierter Leistung nur 1–8 k€/a (bei wörtlicher Lesung ohne Zeitfaktor viermal so viel, 2026 rund 27 statt 6,8 k€/MW/a), gegenüber einem Höchstwert von 244.000 € je MW reduzierter Leistung und Jahr in den Segmenten Langzeit- und Erzeugungskapazitäten; für Kapazitäten legt die Bundesnetzagentur die Höchstwerte noch fest. Der eigentliche Preis sind die Verfügbarkeitspflicht und der Verzicht auf künftige Knappheitserlöse, die ein Kapazitätsmarkt gerade verhindern soll (Einschätzung). Für R2 ist der Kapazitätsmarkt ein Upside ab 11/2031, abhängig vom Reduktionsfaktor; im Basisfall setzt das Buch null an (A-040).

## Praxis-Check und typische Fehler {.unnumbered}

> [!TIP]
> **Praxis-Check:** Prüffragen für Erlösgutachten, Vermarktungsangebote und die Due Diligence
>
> - Welche Produkte (FCR, aFRR positiv und negativ, mFRR; 4-h-Blöcke oder Viertelstundengebote) sind unterstellt, und stimmen die Preisregeln: FCR-Leistung zum Einheitspreis, aFRR- und mFRR-Leistung zum Gebotspreis, Regelarbeit zum Grenzpreis mit Max/Min-Abrechnung?
> - In welcher Einheit stehen die Preise (€/MW je Stunde oder je 4-h-Block), welches Preisjahr ist die Basis, und wie weit liegt es hinter dem jüngsten Ist?
> - Welcher Anteil des Referenzwerts wird angesetzt, mit welcher Zuschlagsquote und Gebotsstrategie, und in welche Märkte weicht die Anlage aus, wenn Regelreserve sinkt?
> - Gibt es ein Mengengerüst (Bedarf, Batterie-PQ, Teilnahmequote), und welchen Anteil der Zuschlagsmenge halten Projekt und Portfolio?
> - Ist aFRR-Arbeit getrennt ausgewiesen, mit belegter Marge, Zahlungsrichtung und Preisgrenzen, und deckt die Batteriegarantie die zusätzlichen Zyklen?
> - Liegt die Präqualifikation vor; bleiben neben den Zeitkriterien (FCR 15 min und höchstens 80 %, aFRR 60 min je Richtung) Energie und Leistung für Arbitrage; wer trägt Kosten und Risiko der Präqualifikation im EPC- und Vermarktungsvertrag?
> - Kann der Vermarkter Viertelstundengebote abgeben, und wie sind Absagen und Pönalen bei Nichterbringung geregelt (Kapitel 5)?
> - Momentanreserve oder Blindleistung im Plan: netzbildender Umrichter, anrechenbare MWs, Verfügbarkeit neben Handel und Regelreserve (Premium ≥ 90 %), Spannungsebene und Zustimmung des Netzbetreibers, Angebotszeitpunkt (Preisbindung)?
> - Kapazitätsmarkt im Plan: Segment, Höchsterbringungsdauer, Reduktionsfaktor, Laufzeit, Mindestinvestition, Preisspitzenausgleich, Verfügbarkeitspflicht, Pönalen, Zahlungszeitpunkt (frühestens 2033), Beihilfevorbehalt; sind Antragsfenster der Präqualifizierung (§ 26), Gebots- und Realisierungssicherheit (§§ 42, 43) und Funktionsnachweis (§§ 69, 80) in Zeitplan und Liquidität eingeplant?

> [!WARNING]
> **Typische Fehler:**
>
> - aFRR-Preise je Stunde mit Preisen je 4-h-Block verwechseln (Faktor 4).
> - Den Referenzwert als Erlös oder als Obergrenze lesen; ein optimierender Speicher erreichte 2026 nur 53 % davon, zum Grenzpreis wäre mehr möglich.
> - aFRR-Arbeit nach Gebotspreis rechnen, Zahlungsrichtungen übersehen oder mit Mittelpreisen rechnen, obwohl wenige Extrempreise den Erlös tragen.
> - Präqualifizierte Leistung über Produkte addieren oder mit angebotener Leistung gleichsetzen.
> - Einen Preisrückgang auf alle Produkte übertragen: 2026 fiel aFRR um 28 %, FCR stieg um 13 %.
> - Regelleistungserlöse je MW auf längere Speicher übertragen, als wüchsen sie mit der Speicherdauer.
> - Erlöse einer Einzelanlage linear auf ein Portfolio hochrechnen, das 8 % des Marktes hält.
> - Kapazitätsmarkterlöse für 2–5-h-Speicher im Langzeitsegment oder vor 11/2031 ansetzen oder den Preisspitzenausgleich vergessen.
> - Momentanreserve-Festpreise ohne netzbildenden Umrichter und anrechenbare Menge in Erlöse umrechnen.

## Zusammenfassung {.unnumbered}

1. Regelreserve gibt es in drei Stufen (FCR, aFRR, mFRR) mit je zwei Erlöskomponenten: Leistung für das Vorhalten, Arbeit für den Abruf. FCR-Leistung wird zum Einheitspreis, aFRR- und mFRR-Leistung zum Gebotspreis vergütet, Regelarbeit seit 22.06.2022 zum Grenzpreis (aFRR über PICASSO, mFRR seit 05.10.2022 über MARI), bei aFRR mit Max/Min-Abrechnung.
2. Leistung zahlt immer der ÜNB, bei der Regelarbeit fließen Zahlungen je nach Vorzeichen von Menge und Preis in beide Richtungen. aFRR-Arbeit hängt an wenigen extremen Preisen und lässt sich mit öffentlichen Daten nicht belastbar kalkulieren.
3. Die Präqualifikation verlangt Energie: 10 MW symmetrische aFRR binden rund 20 MWh nutzbar. R1 bleibt dann zu Betriebsbeginn keine Energie für Arbitrage, R2 rund 35 MWh, nutzbar aber nur mit freier Leistung; mit der Alterung sinkt die präqualifizierbare Leistung. Regelleistung vergütet MW, nicht MWh.
4. Der Referenzwert ist weder Prognose noch Obergrenze. Ein perfekt optimierender Speicher R2 erreichte 2025 83 %, 2026 53 % davon, weil er vor allem in Day-Ahead-Handel auswich; der realistische Gesamterlös sank nur um 2 % auf 2,06 Mio. €/a.
5. Der aFRR-Markt ist mit rund 1,8–1,9 GW je Richtung klein; die präqualifizierte Batterieleistung erreichte Anfang 2026 62–66 % davon, die Preise fielen 2026 um 28 %. Weil ein Speicher beide Richtungen zugleich vorhält, decken rund 2,5–2,7 GW Speicherleistung den deutschen Bedarf. Sättigung hängt an Menge, Teilnahmequote und Opportunitätskosten und gehört ab 2027 als Pfad in jeden Business Case.
6. Viertelstundengebote kommen bis spätestens 28.10.2026 zusätzlich zu den 4-h-Blöcken, mit unveränderten Vergütungsregeln und offener Erlöswirkung. Momentanreserve setzt einen netzbildenden Umrichter voraus; Blindleistung und § 13k bringen R1 und R2 im Basisfall nichts (Einschätzung).
7. Der Kapazitätsmarkt verpflichtet ab 11/2031 und zahlt erstmals Anfang 2033. 2–5-h-Speicher sind vom Langzeitsegment ausgeschlossen, sonst hängt ihr Wert an unveröffentlichten Reduktionsfaktoren. Die Vergütung tauscht Spitzenerlöse gegen eine feste Zahlung; im Basisfall setzt das Buch null an.

## Übungen {.unnumbered}

**Übung 3.1 (Rechnen und Vergleichen).** (a) Rechnen Sie die aFRR-Leistungspreise vom 01.01. bis 26.09.2026 aus Tabelle 3.3 (Durchschnitts- und Grenzpreis, positiv und negativ) in €/MW je Stunde um. (b) Wie viel nutzbare Energie müsste ein Speicher zu Betriebsbeginn haben, damit er 10 MW symmetrische aFRR auch bei 80 % Restkapazität präqualifizieren kann (Wirkungsgrad je Richtung 0,933)? Was folgt daraus für R1 (20 MWh nutzbar)? (c) Berechnen Sie für R1 zu Betriebsbeginn den Referenzwert und die Schranke zum Grenzpreis, auf ein Jahr mit 2.190 Blöcken hochgerechnet. (d) M1 errechnet für R1 im selben Zeitraum (annualisiert) 1,66 Mio. €/a aFRR-Leistungserlös bei perfekter Voraussicht und 1,15 Mio. €/a im realistischen Fall [M1, Lauf 20260928-standalone]. Erklären Sie beide Abstände. (e) Vergleichen Sie für R1 die höchstens zulässige FCR-Leistung mit symmetrischer aFRR nach gebundener Energie und Leistung, Referenzwert 2026, Vergütung von Leistung und Arbeit sowie Gebotsstrategie. Welches Produkt passt besser zu R1?

**Übung 3.2 (Rechnen und Prüfen).** (a) Ein Speicher bietet positive aFRR-Arbeit zu 150 €/MWh und negative zu 20 €/MWh an; in negativer Richtung zahlt der Anbieter bei positivem Preis (Tabelle 3.2). Bestimmen Sie für je 1 MWh Abrechnungspreis, Zahlungsrichtung und Betrag, wenn der Grenzpreis von PICASSO (i) in positiver Richtung 400 €/MWh, (ii) in positiver Richtung 120 €/MWh bei Abruf außerhalb der Merit-Order, (iii) in negativer Richtung −50 €/MWh, (iv) in negativer Richtung 60 €/MWh bei Abruf außerhalb der Merit-Order beträgt. (b) G1 setzt für 2027 rund 1,60 Mio. € aFRR-Arbeit an (10 MW je Richtung). Rechnen Sie das in eine Marge je MW vorgehaltener Leistung und Stunde und, mit der mittleren Aktivierung 2025 von 221 MWh (positiv) und 230 MWh (negativ) je MW und Jahr, in eine Marge je aktivierter MWh um. Beurteilen Sie mit den G1-Preisangaben aus Abschnitt 3.2, was die Annahme voraussetzt.

**Übung 3.3 (Bewerten).** Ein Verkäufer argumentiert, die aFRR-Preise seien 2025 trotz fast verdoppelter Batterie-Präqualifikation gestiegen, Sättigung sei deshalb kein Thema. (a) Stellen Sie mit den Tabellen 3.3 und 3.5 den Batterieanteil an der Zuschlagsmenge 2024–2026 den Jahrespreisen gegenüber. (b) Nennen Sie drei Gründe, warum Preise und Präqualifikation nicht im Gleichschritt laufen, und bewerten Sie das Argument. (c) Bei welcher installierten Speicherleistung wäre der Bedarf gedeckt, wenn 70 % statt 50 % der Speicher teilnehmen? Rechnen Sie mit der Speicherleistung je Richtung und mit der Marktgröße von 4,5 GW nach Modo, erklären Sie den Unterschied und ordnen Sie die Schwellen zeitlich ein. (d) Wie sollte der Business Case von R2 aFRR-Leistungserlöse ab 2027 ansetzen?

**Übung 3.4 (Rechnen und Entscheiden).** (a) Bis zu welcher nominalen Leistung erreicht die G1-Konfiguration (49,5 MWh nutzbar; Energie am Netzverknüpfungspunkt nach A-M1-01) 5 bzw. 6 h Höchsterbringungsdauer, und wann lohnt sich ein kleineres Gebot? (b) Welche installierte Leistung dürfte ein Speicher mit 55 MWh nutzbar höchstens haben, um das Langzeitkriterium zu erfüllen? (c) An einem Beispieltag mit fiktiven Preisen liegt der Day-Ahead-Preis in vier Viertelstunden bei 400, 650, 900 und 380 €/MWh, der Ausübungspreis bei 330 €/MWh. Berechnen Sie den Preisspitzenausgleich für 5 MW reduzierte Leistung. Was bleibt dem Speicher, wenn er in diesen Viertelstunden mit 10 MW entlädt, und was zahlt er, wenn er leer ist? (d) Unter welchen Bedingungen sollte R2 an der Ausschreibung vom 01.12.2027 teilnehmen?

**Übung 3.5 (Bewerten und Entscheiden).** Ein Verkäufer legt für R2 (Inbetriebnahme 2027) einen Businessplan vor: aFRR-Leistung 2,94 Mio. €/a real konstant ab 2028, aFRR-Arbeit 1,60 Mio. €/a, Momentanreserve 150 k€/a ab 2027, Blindleistung 20 k€/a, Kapazitätsmarkt 50 k€/MW/a ab 2028 und 10 % Aufschlag auf die aFRR-Leistung durch Viertelstundengebote. Prüfen Sie jede Position mit Tabelle 3.6 und den Abschnitten 3.2–3.7. Entscheiden Sie in höchstens acht Sätzen, welche Positionen in den Basisfall, welche als Upside und welche gestrichen werden.

Die Lösungen stehen im Anhang A unter Kapitel 3.

## Quellen und Stand {.unnumbered}

Qualität nach dem Quellenregister: A = Primärquelle, B = anerkannte Sekundärquelle, C = Fachmedium oder Anbieter; „Suchauszug“ = nicht im Volltext geprüft.

**Gesetze und Behördenentscheidungen:** [K03R-01] Strom-Versorgungssicherheits-und-Kapazitätengesetz (StromVKG), Ausfertigung 21.07.2026, Volltextauszug mit Anlagen 1–7 vom 27.09.2026 (A) · [K03R-02], [W2V-15] BNetzA, Beschluss BK6-25-212 vom 28.10.2025 (A) · [W2V-16] ACER-Entscheidung 09/2024, Annex Ia (A; Fassung mit Änderungsverfolgung) · [W2V-07] § 13k EnWG (A) · [K03R-08] BNetzA, Festlegung BK6-23-072 (25.06.2024; A; Suchauszug) · [VR1-46] BNetzA, Beschluss BK6-25-033, Regeln der FCR-Kooperation (03.07.2025; A; Suchauszug) · [W0R-10], [W0R-11] BNetzA, Bekanntmachung 1. Gebotstermin (03.09.2026) und Pressemitteilung (21.07.2026) (A).

**Netzbetreiber und Marktdaten:** [K03M-02] ÜNB, Präqualifizierte Leistungen in Deutschland (01.01.2026; A) · [K03M-03] ÜNB, Dimensionierung Regelreservebedarf (A) · [K03M-04] ÜNB, Wo finde ich welche Daten? (A) · [K03M-05], [K03M-06], [K03M-29], [K03M-40], [VR3-39] ÜNB, Momentanreserve: Themenseiten, FAQ v3.1 (27.04.2026), Anbieterleitfaden v1.03 (03.06.2026; A) · [K03M-07] BNetzA, Themenseite Stromspeicher (17.03.2026; A) · [K03M-08] ÜNB, Beschreibung Systemausgleich und Regelreservemärkte (01/2025; A) · [K03M-09] ÜNB, Erläuterungen zu Daten Regelenergie (10.07.2023; A) · [SYN-13] ENTSO-E, Go-Live of MARI (06.10.2022; A) · [VR3-32] ÜNB, Umsetzungskonzept § 13k EnWG (01.04.2026; A) · [M1Q-01] ÜNB, PQ-Bedingungen 1.05 (05.07.2024; A) · [M1D-01 bis M1D-03, M1D-07, M1D-09, M1D-10, M1D-11] Primärdaten energy-charts, regelleistung.net und netztransparenz.de, Snapshot bis 26.09.2026 mit Ergänzung 2021–2022 (A) · [SYN-08] regelleistung.net, Ergebnisübersicht aFRR, Liefertage 26.09. und 28.09.2026 (A) · [GH-01] Kreuzprüfungsdatensatz, Commit b4070b9 (B).

**Research, Fachmedien und Vergleichsmärkte:** [K06M-02], [K06M-03], [K06M-04] Modo Energy, Ausblick Deutschland (16.03.2026), Prognose-Update (04/2026), Modellannahmen (B) · [VR2-20] Modo Energy, Changelog Juli 2026 (B) · [VR2-25] Modo Energy, Sättigung in Deutschland, Lehren aus Großbritannien (10/2025; B; Suchauszug) · [K06M-05] ESS News, enervis-Index (31.08.2026; C) · [K03M-14] pv magazine, Erlöspotenziale Q1 2026 (09.04.2026; C) · [K03R-10] Regelleistung Online (09.03.2026) und Entelios (13.08.2026), Start der Viertelstundenprodukte (C) · [W0R-12], [W0R-14] Fachmedien zum Kapazitätsmarkt (C; Suchauszüge) · [K05M-18] Terna, MACSE-Ergebnis 2028 (2025; A).

**Fallstudie und Modelle:** [G1-00] Erlösgutachten G1 (anonymisiert), Stand 27.08.2026 (B) · [M1] Begleitmodell M1, Version 2.0.0: Läufe 20260928-standalone, 20260928-triangulation, 20260928-kapitel06 und 20260928-kapitel03 (28.09.2026; eigene Berechnung).

**Annahmen:** A-001, A-020, A-023, A-040, A-041, A-M1-01, A-M1-05, A-M1-06, A-M1-09 bis A-M1-12, A-M1-20; Buchkonvention „nutzbar“ nach D-021.

**Stand:** 28.09.2026; Marktdaten bis Liefertag 26.09.2026. Beweglich und vor Verwendung zu prüfen sind der Start der Viertelstundenprodukte (bis 28.10.2026), die harmonisierte Preisgrenze der Regelarbeit nach 07/2026, die PQ-Bedingungen, die Mengen und Festpreise der Momentanreserve ab 2027/2028, die Ergebnisse der Kapazitätsmarkt-Ausschreibungen (Zuschläge bis 03.11.2026), die Reduktionsfaktoren nach Anlage 3 und der Umfang der Beihilfegenehmigung.
