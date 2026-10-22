---
title: "Kapitel 2 · Strommärkte: Preisbildung, Handel und Bilanzierung"
subtitle: "Kapitelentwurf – Ökonomie von Batteriespeichern in Deutschland"
date: "04.10.2026"
kopfzeile-rechts: "Kapitel 2 · Stand 27.09.2026"
kapitel-start: 2
nummerierung: kapitelweise
inhaltsverzeichnis: true
toc-tiefe: 2
deckblatt-hinweis: "Keine Rechts-, Steuer- oder Anlageberatung. Erlösgutachten G1 anonymisiert verwendet."
---

# Strommärkte: Preisbildung, Handel und Bilanzierung

> [!NOTE]
> **Lernziele:** Nach diesem Kapitel können Sie
>
> - die Preisbildung am Day-Ahead- und Intraday-Markt aus Merit-Order und Residuallast herleiten und damit Knappheits- und Negativpreise erklären;
> - Tagesspreads (TB1, TB2, TB4), Preisdauerlinien und die Häufigkeit negativer Preise aus Marktdaten berechnen und dabei Stunden und Viertelstunden richtig zählen;
> - die Wirkung von PV-, Wind- und Speicherzubau, europäischer Marktkopplung und Gebotszonenzuschnitt auf Preisniveau und Spreads analysieren;
> - spreadbasierte Erlösangaben und Ausgleichsenergierisiken in Angeboten, Gutachten und Verträgen bewerten.

## Warum das für Investor und Fonds zählt {.unnumbered}

Ein Standalone-Speicher verdient am Strommarkt nur an Preisunterschieden: Er kauft Strom, wenn er billig ist, und verkauft ihn, wenn er teuer ist (Arbitrage). Wie groß, wie häufig und wie verlässlich diese Unterschiede sind, bestimmt die Arbitrageerlöse und zugleich die Opportunitätskosten, an denen sich die Gebote für Regelreserve ausrichten, also für Leistung, die ein Speicher den Übertragungsnetzbetreibern (ÜNB) zum Ausgleich kurzfristiger Ungleichgewichte bereithält (Kapitel 3). Die Marktregeln ändern sich laufend: Seit dem 01.10.2025 handelt der Day-Ahead-Markt in Viertelstunden, seit dem Handelstag 28.05.2026 gilt eine tiefere Preisuntergrenze, und über den Zuschnitt der deutschen Gebotszone wird weiter gestritten. Wer Marktdaten richtig liest, erkennt, ob ein Angebot, ein Erlösgutachten oder ein Vermarktungsvertrag mit tragfähigen Spreads rechnet oder mit einer günstigen Definition.

**Cashflow-Kompass:** Erlöse ● (Arbitrage, Opportunitätskosten der Regelreserve) · Betriebskosten ○ (Ausgleichsenergie, Handelskosten) · Investitionen – · Steuern – · Finanzierung ○ (Merchant-Anteil im Lender Case) · Fondsebene ○ (Erlösprognosen im NAV). **Werttreiber:** Erlösniveau und Erlösrisiko, Standortwert.

## Merit-Order, Residuallast und Knappheit

Am Day-Ahead-Markt geben Erzeuger, Verbraucher, Händler und Speicher bis zum Vortag Gebote für jede Lieferperiode des Folgetags ab. Die Börse ordnet die Verkaufsgebote nach steigendem, die Kaufgebote nach fallendem Preis; wo sich beide Kurven schneiden, liegt der Markträumungspreis. Er gilt für alle bezuschlagten Gebote einer Gebotszone, also eines Gebiets mit einheitlichem Großhandelspreis, und einer Lieferperiode. Die aufsteigend sortierte Angebotskurve heißt Merit-Order. Weil jeder bezuschlagte Anbieter denselben Preis erhält, lohnt es sich für ihn, zu seinen Grenzkosten zu bieten, also zu den Kosten einer zusätzlichen MWh: Er läuft, sobald der Preis diese Kosten deckt, und verdient die Differenz zum Preis (Einordnung). Für ein Gaskraftwerk gilt näherungsweise

$$c = \frac{p_{\text{Gas}}}{0{,}903 \cdot \eta_{\text{el}}} + \frac{e}{\eta_{\text{el}}} \cdot p_{\text{CO}_2} + c_{\text{var}}$$

mit $c$ als Grenzkosten in €/MWh Strom, $p_{\text{Gas}}$ als Gaspreis in €/MWh bezogen auf den Brennwert, $\eta_{\text{el}}$ als elektrischem Wirkungsgrad bezogen auf den Heizwert, $e$ als CO₂-Ausstoß in t je MWh Brennstoff (Heizwert), $p_{\text{CO}_2}$ als CO₂-Preis in €/t und $c_{\text{var}}$ als sonstigen variablen Kosten in €/MWh. Der Brennwert enthält auch die Wärme des Wasserdampfs im Abgas, der Heizwert nicht. Gas wird auf den Brennwert bezogen gehandelt, Kraftwerkswirkungsgrade beziehen sich meist auf den Heizwert. Der Faktor 0,903 rechnet vom einen Bezug auf den anderen um, wie es auch das Strom-Versorgungssicherheits-und-Kapazitätengesetz (StromVKG) beim Ausübungspreis tut [K03R-01, § 2 Nr. 33, Anlage 7; Kapitel 3].

Der Day-Ahead-Gaspreis am deutschen Handelspunkt THE (Trading Hub Europe) lag 2025 im Mittel bei 37,2 €/MWh (2024: 34,6 €/MWh) [K02M-01]. Für ein Gas-und-Dampfturbinen-Kraftwerk (GuD), das die Abwärme der Gasturbine in einer Dampfturbine nutzt, setzen wir 50 % Wirkungsgrad bezogen auf den Heizwert an (Annahme A-055, illustrativ): ein runder Rechenwert über den 37 %, die das StromVKG für die offene Gasturbine unterstellt [K03R-01, Anlage 7]; ein Wert für den deutschen Kraftwerksbestand ist nicht belegt. Allein der Brennstoff kostet damit 37,2 / 0,903 / 0,5 ≈ 82,4 €/MWh Strom. Hinzu kommen 0,2016 t CO₂ je MWh Brennstoff [K03R-01, Anlage 7] ÷ 0,5 ≈ 0,40 t je MWh Strom mal CO₂-Preis [LÜCKE: CO₂-Preis 2025 aus Primärquelle]. Schon der Brennstoffanteil liegt in der Größenordnung des Day-Ahead-Mittels 2025 von 89,32 €/MWh [K02M-02], ein Hinweis darauf, dass Gaskraftwerke in vielen Stunden den Preis setzen (Einordnung).

Wind- und Solaranlagen haben keine Brennstoffkosten. Sie bieten zu Grenzkosten nahe null, mit Förderung teils auch darunter (Abschnitt 2.2). Damit verschieben sie die Merit-Order nach rechts und drängen teurere Anlagen aus dem Markt. Für den Preis maßgeblich ist deshalb die Residuallast, also die Last abzüglich der Einspeisung aus Wind und Photovoltaik:

$$L^{\text{res}}_t = L_t - W_t - PV_t$$

mit der Last $L_t$, der Windeinspeisung $W_t$ und der PV-Einspeisung $PV_t$ in MW im Zeitschritt $t$. Die Residuallast müssen steuerbare Kraftwerke, Importe und Speicher decken. Ist sie niedrig, etwa an einem sonnigen und windigen Mittag, setzen billige oder negativ bietende Anlagen den Preis. Ist sie hoch, etwa an einem windstillen Winterabend, setzt ihn das teuerste noch benötigte Kraftwerk. Speicher treten am Markt zweimal auf: als Käufer auf der Nachfrageseite in Zeiten niedriger und als Verkäufer in der Merit-Order in Zeiten hoher Residuallast. Jede zusätzliche Ladung hebt den Preis im Tal, jede Entladung senkt ihn in der Spitze; mit wachsender Flotte schrumpft deshalb der Spread, von dem alle Speicher leben (Einordnung; Kapitel 4). Abbildung 2.1 zeigt die Preisbildung schematisch.

![Merit-Order ohne und mit PV-Einspeisung (schematisch): PV schiebt die Angebotstreppe nach rechts, die Nachfrage schneidet sie auf einer niedrigeren Stufe, der Markträumungspreis sinkt](05_figures/K02/02_merit_order_schema.png)

Quelle: schematische Darstellung, eigene Abbildung, ohne Zahlenwerte (Stand 27.09.2026).

Reicht die verfügbare Leistung kaum noch aus, bestimmen nicht mehr die Grenzkosten des letzten Kraftwerks den Preis, sondern die Zahlungsbereitschaft der Käufer; es entstehen Knappheitspreise. Sie sind selten, aber hoch. Die Jahreshöchstwerte des Day-Ahead-Preises in der deutsch-luxemburgischen Gebotszone DE-LU lagen bei 524,27 €/MWh (11.09.2023), 936,28 €/MWh (12.12.2024, 17–18 Uhr), 583,40 €/MWh (20.01.2025, 17–18 Uhr) und 747,10 €/MWh (24.06.2026, Viertelstunde ab 20:45 Uhr) [M1D-01; M1, Lauf 20260927-kapitel02]. Im kontinuierlichen Intraday-Handel erreichten mengengewichtete Durchschnittspreise am 07.01.2025 bis zu 1.056 €/MWh [K02M-01]. Über 300 €/MWh lag der Day-Ahead-Preis 2024 in 41 und 2025 in 40 Stunden [K02M-02], 2026 bis zum 26.09. in 38 Stunden (Stundenmittel) [M1, Lauf 20260927-kapitel02]. 2026 fielen alle 41 Viertelstundenpreise über 500 €/MWh auf Abende an sieben Tagen im Juni und September zwischen 18:45 und 22:30 Uhr [M1, Lauf 20260927-kapitel02], also dann, wenn die PV-Einspeisung wegfällt und die Residuallast steil ansteigt (Einordnung). Nach oben begrenzen die Börsenregeln den Preis bei +4.000 €/MWh (Kasten „Stand“ in Abschnitt 2.3); diese Grenze lag bisher weit über allen beobachteten Spitzen.

Anlagen im künftigen Kapazitätsmarkt tauschen solche Spitzen gegen eine feste Vergütung. Nach dem StromVKG (ausgefertigt am 21.07.2026, erste Verpflichtungen ab 01.11.2031) zahlt eine bezuschlagte Anlage für jede Viertelstunde, in der der Day-Ahead-Preis ihren Ausübungspreis übersteigt, die Überschreitung für ihre gebotene reduzierte Leistung (nominale Leistung × Reduktionsfaktor) an den ÜNB, unabhängig vom Betrieb (Preisspitzenausgleich). Der Ausübungspreis bildet die variablen Kosten einer offenen Gasturbine nach, zuzüglich eines Abstands von 150 €/MWh und etwaiger Einspeise-Netzentgelte [K03R-01, § 81, Anlage 7]. Einzelheiten und Stand (27.09.2026, regulatorisch beweglich) behandelt Kapitel 3.

## PV, Wind, negative Preise und Kannibalisierung

Der Anteil erneuerbarer Energien an der Stromerzeugung in Deutschland lag 2025 bei 58,8 % von 437,6 TWh (2024: 58,5 %) [K02M-02]. Die öffentliche Nettoerzeugung aus Photovoltaik stieg 2023–2025 deutlich (Tabelle 2.1); vom 01.01. bis 26.09.2026 waren es 75,0 TWh, 20 % mehr als im Vorjahreszeitraum mit 62,3 TWh [M1D-04; M1, Lauf 20260927-kapitel02]. Die Forschungsstelle für Energiewirtschaft (FfE) beziffert den Solaranteil 2025 auf knapp 17 % [K02M-01]; bezogen auf die Erzeugung laut Bundesnetzagentur (BNetzA) wären es rund 16 %, weil sich die Bezugsgrößen unterscheiden. Die Windeinspeisung lag im Winter 2025 (Dezember bis Februar) um 35 % unter der des Vorjahreswinters [K02M-01].

Weil alle PV-Anlagen gleichzeitig einspeisen, fällt mittags die Residuallast und mit ihr der Preis (Abbildung 2.2). Im Sommerhalbjahr (April–September) 2024 lag der Day-Ahead-Preis um 14 Uhr im Mittel bei 19,3 €/MWh und um 20 Uhr bei 139,1 €/MWh, 2025 um 13 Uhr bei 9,5 und um 20 Uhr bei 143,4 €/MWh. Im Sommerhalbjahr 2026 fiel er in der Viertelstunde ab 13:45 Uhr auf 13,4 €/MWh und stieg ab 19:45 Uhr auf 209,7 €/MWh. Im Winter hat das Profil zwei Spitzen und eine flachere Mittagssenke; von Januar bis März 2026 lag der Preis um 8 Uhr bei 130,5, um 14 Uhr bei 71,4 und ab 17:45 Uhr bei 158,0 €/MWh [M1, Lauf 20260927-kapitel02]. Für einen Speicher heißt das: Im Sommer lohnt vor allem ein Zyklus vom Mittagstal in den Abend, im Winter können sich zwei Zyklen je Tag lohnen (Rechenbeispiel 2.1, Übung 2.3).

![Mittleres Tagesprofil der Day-Ahead-Preise DE-LU in €/MWh im Sommer (April–September) und Winter (übrige Monate) 2024 (Stunden) und 2026 (Viertelstunden, Winter nur Januar–März), Ortszeit, nominal](05_figures/K02/02_tagesprofile.png)

Quelle: eigene Berechnung, Modell M1 (Lauf 20260927-kapitel02); Day-Ahead DE-LU: energy-charts/SMARD [M1D-01] (Stand 27.09.2026).

Die klassische Kennzahl Peak/Base, das Verhältnis des mittleren Preises im Peak-Fenster (werktags 8–20 Uhr) zum mittleren Preis aller Stunden (Base), fiel von 1,11 (2024) auf 1,03 (2025); 2025 lag der Peak-Preis bei 92,3 €/MWh, der Off-Peak-Preis bei 87,7 €/MWh [K02M-01]. Sie taugt nicht mehr als Spread-Indikator, weil das Peak-Fenster die billigen PV-Mittagsstunden enthält; für Speicher zählt der Abstand zwischen Mittagstal und Morgen- oder Abendrampe.

**Negative Preise** entstehen, wenn Anbieter auch dann einspeisen, wenn sie für ihren Strom zahlen müssen, etwa weil ihre Anlagen technisch nicht flexibel sind oder weil eine Förderung den negativen Preis ausgleicht (Einordnung). Für Anlagen mit Inbetriebnahme ab dem 25.02.2025 entfällt der anzulegende Wert (Bezugsgröße der Marktprämie) nach § 51 EEG in jeder Viertelstunde mit negativem Day-Ahead-Preis, ohne Mindestdauer [W2V-01, W2V-06]. Für ältere Anlagen gelten Übergangsregeln, etwa eine Sechs-Stunden-Regel für Inbetriebnahmen 2016–2020 und keine Kürzung für Anlagen bis 2015 [VR3-30]; Einzelheiten behandelt Kapitel 12. Negative Day-Ahead-Preise gab es 2023 in 301, 2024 in 457 und 2025 in 573 Stunden [K02M-02; K02M-03]. Sie treten fast nur um die Mittagszeit auf: 2025 lagen 510 der 525 negativen Stunden bis September, 2026 1.772 der 1.836 negativen Viertelstunden zwischen 9 und 18 Uhr [M1D-01; eigene Auswertung]. Die meisten liegen zwischen 0 und −5 €/MWh [K02M-01]. Umso tiefer sind die Ausreißer: −500,00 €/MWh am 02.07.2023, −250,32 €/MWh am 11.05.2025 und −499,99 €/MWh am 01.05.2026 [M1D-01; M1, Lauf 20260927-kapitel02]. Im Winter sind negative Preise selten; im vierten Quartal 2025 gab es 199 negative Viertelstunden, und der tiefste Preis lag bei −5,09 €/MWh [M1, Lauf 20260927-kapitel02]. Das Erlösgutachten G1 (anonymisiert) weist für 2025 selbst einen Anteil negativer Preise von 6,5 % aus, bildet negative Preise in seinem Preismodell aber nicht ab (G1, Kap. 5.1; Kapitel 6, Prüfpunkt P3). Die Zählweise von Stunden und Viertelstunden erläutert Abschnitt 2.6.

**Kannibalisierung durch PV.** Je mehr PV-Anlagen gleichzeitig einspeisen, desto niedriger ist der Preis, den sie erzielen. Das Maß dafür ist der Wertfaktor (Capture-Rate), das Verhältnis des mit der Einspeisung gewichteten Preises zum zeitgewichteten Mittel:

$$CR = \frac{\sum_t PV_t \cdot p_t \,\big/ \sum_t PV_t}{\bar p}$$

mit $PV_t$ als Solareinspeisung und $p_t$ als Day-Ahead-Preis im Zeitschritt $t$ sowie $\bar p$ als zeitgewichtetem Mittelpreis des Jahres. Die ÜNB veröffentlichen den Jahresmarktwert Solar (JW Solar), den mit der Solareinspeisung gewichteten Jahrespreis; welche Marktwertgröße die Marktprämie einer Anlage bestimmt, behandelt Kapitel 12. Tabelle 2.1 stellt ihn der Nachrechnung aus Zeitreihen gegenüber.

| Kennzahl | 2023 | 2024 | 2025 | 01.01.–26.09.2026 |
|---|---:|---:|---:|---:|
| Day-Ahead-Mittel (€/MWh) | 95,18 | 78,51 | 89,32 | 107,04 |
| Jahresmarktwert Solar (ct/kWh) | n. v. | 4,624 | 4,508 | – |
| Wertfaktor Solar (JW Solar ÷ Mittel) | – | 0,589 | 0,505 | – |
| Capture-Rate Solar aus Zeitreihen (M1) | 0,759 | 0,592 | 0,514 | 0,515 |
| Solarerzeugung, öffentliche Nettoerzeugung (TWh) | 53,9 | 59,7 | 70,1 | 75,0 |

Table: Marktwert und Wertfaktor Solar 2023–2026

Quelle: Day-Ahead-Mittel [K02M-02, K02M-03; M1D-01]; JW Solar 2025 [K02M-05], 2024 [VR3-29]; n. v. = JW Solar 2023 in der Marktwertübersicht der ÜNB nicht mehr abrufbar; Capture-Rate und Erzeugung aus [M1D-04], Auswertung M1 (Lauf 20260927-kapitel02); Wertfaktor eigene Rechnung; 2026 ist ein Teiljahr; nominal (Stand 27.09.2026).

Der Wertfaktor sank von 0,589 (2024) auf 0,505 (2025): Eine MWh Solarstrom war 2025 am Markt nur gut halb so viel wert wie eine durchschnittliche MWh, 44,2 €/MWh weniger als das Mittel [K02M-05; eigene Rechnung]. Wind an Land erreichte 2025 einen Wertfaktor von 0,833, Wind auf See von 0,902 (Jahresmarktwerte 7,441 und 8,059 ct/kWh) [K02M-05; eigene Rechnung]. Wind weht auch nachts und im Winter und kannibalisiert sich deshalb weniger; windreiche Nächte schaffen im Winter Ladegelegenheiten, windarme Abende treiben die Spitzen (Einordnung). Für 2024 findet sich auch ein Wertfaktor von 0,582 (eigene Rechnung aus [VR3-29]); er bezieht den JW Solar auf ein Spotmittel von 7,946 ct/kWh statt auf das BNetzA-Mittel von 7,851 ct/kWh. Woher das Spotmittel stammt, ist offen. Für 2025 entspricht der allgemeine Jahresmarktwert der ÜNB (8,932 ct/kWh) genau dem BNetzA-Mittel [K02M-05; K02M-02], und die Nachrechnung aus Zeitreihen (0,592) stützt den höheren Wert. Kleine Abweichungen bleiben, weil die ÜNB mit ihrer Hochrechnung der Solareinspeisung gewichten, M1 mit der öffentlichen Nettoerzeugung [M1, Lauf 20260927-kapitel02]. Vorsicht bei der Bezeichnung: Der „Jahresmarktwert Solar nach § 33 EEG 2012“ (2025: 6,170 ct/kWh) ist eine andere Größe und kein Capture-Preis [K15M-01].

Auffällig ist 2026: Trotz 20 % mehr Solarstrom lag die Capture-Rate im Teiljahr mit 0,515 über dem Vorjahreszeitraum (0,474), und die negativen Stundenäquivalente sanken um 13 % [M1, Lauf 20260927-kapitel02]. Als Ursachen kommen mehr Speicher, die Abregelungsanreize des § 51 EEG für neue Anlagen, flexiblere Nachfrage und das Wetter infrage; belegt ist keine davon (Einschätzung). Für den Speicher ist die Kannibalisierung der PV die Kehrseite seines Geschäfts, denn das Mittagstal ist seine Einkaufsgelegenheit.

## Day-Ahead und Intraday: Auktionen, kontinuierlicher Handel und Indizes

Ein Speicher baut seine Handelsposition in mehreren Stufen auf und korrigiert sie. Die Day-Ahead-Auktion legt am Vortag den Fahrplan fest. Drei Intraday-Auktionen und der kontinuierliche Intraday-Handel erlauben Anpassungen bis kurz vor Lieferung. Was danach noch vom Fahrplan abweicht, wird als Ausgleichsenergie abgerechnet (Abschnitt 2.4). Ein Speicher kann seine Day-Ahead-Position im Intraday-Handel umschichten, wenn sich die Preise verschieben; das kann Erlös bringen, kostet aber Zyklen und Handelsentgelte (Einordnung; Kapitel 4 und 5). Tabelle 2.2 fasst die Stufen zusammen.

**Day-Ahead.** Die europäischen Day-Ahead-Märkte sind in der einheitlichen Day-Ahead-Marktkopplung (Single Day-Ahead Coupling, SDAC) verbunden (Abschnitt 2.5). Eine gemeinsame Auktion bestimmt einmal täglich für jede Gebotszone und Lieferperiode einen Preis. Die Gebote schließen am Vortag um 12 Uhr (Beleg vom Juli 2024) [K02M-24, S. 3]; M1 unterstellt denselben Zeitpunkt (A-M1-05). Seit dem Liefertag 01.10.2025 (Handelstag 30.09.2025) ist die Lieferperiode die Viertelstunde, der Tag hat also 96 statt 24 Preise [W2V-11]. Das Erlösgutachten G1 datiert die Umstellung falsch auf den 01.05.2025 (Kapitel 6, Prüfpunkt P13).

Die Viertelstunde macht Preissprünge innerhalb einer Stunde sichtbar, vor allem an den Morgen- und Abendrampen. Was sie wert ist, zeigt der Vergleich derselben Preise mit ihren Stundenmitteln. Im vierten Quartal 2025 lag der mittlere TB2-Spread (Definition in Abschnitt 2.6) auf Viertelstunden bei 87,9 €/MWh, auf Stundenmitteln bei 79,9 €/MWh (+10,1 %), vom 01.01. bis 26.09.2026 bei 158,8 gegenüber 151,5 €/MWh (+4,8 %). Der Day-Ahead-Erlös von R1 bei perfekter Voraussicht (alle Preise vorab bekannt) steigt dadurch um 20,1 bzw. 9,4 %, der von R2 um 12,1 bzw. 4,8 % [M1, Lauf 20260927-kapitel02]. Das ist eine Obergrenze des Auflösungseffekts, weil Bieter bei Stundenprodukten anders geboten hätten. Der kürzere Speicher gewinnt mehr, weil die zusätzlichen Spitzen kurz sind. Auch die Extremwerte werden schärfer: Das höchste Stundenmittel 2026 lag bei 697,31 €/MWh, die höchste Viertelstunde bei 747,10 €/MWh [M1, Lauf 20260927-kapitel02].

> [!STAND]
> **Stand der Preisgrenzen:** Die harmonisierte Preisuntergrenze der SDAC sank ab dem Handelstag 28.05.2026 (Lieferung 29.05.2026) von −500 auf −600 €/MWh. Nach der Methodik sinkt sie um 100 €/MWh, wenn der Preis in mindestens zwei Lieferperioden an zwei Tagen innerhalb von 30 Tagen unter 70 % der Grenze fällt. Das geschah an den Liefertagen 26.04. und 01.05.2026; die neue Grenze gilt vier Wochen nach dem zweiten Ereignis [W2V-10]. Auch in DE-LU lagen an beiden Tagen mehrere Viertelstunden unter −350 €/MWh, am 01.05.2026 fünf bei −499,99 €/MWh [M1, Lauf 20260927-kapitel02]. Weitere Ereignisse dieser Art können die Grenze erneut senken (Einordnung). Die Anpassungsregel ist Teil der bestehenden Methodik; die Entscheidung 02/2026 der EU-Regulierungsagentur ACER vom 04.02.2026 hat sie bestätigt und Entkopplungsereignisse ausgenommen [K02M-21]. Die Obergrenze von +4.000 €/MWh gilt seit dem 10.05.2022; eine angekündigte Erhöhung auf +5.000 €/MWh wurde im September 2022 zurückgenommen, und bis zum 07.05.2026 ist keine weitere Änderung mitgeteilt [W2V-11]. Im kontinuierlichen Intraday-Handel gilt eine Preisspanne von ±9.999 €/MWh [W2V-12]. Auch die Preisgrenzen der Intraday-Kopplung passen sich nach derselben Logik an [K02M-22]; ihre Werte für die Intraday-Auktionen stehen in einem Anhang, der nicht geprüft ist [LÜCKE: Preisgrenzen IDA]. Eine tiefere Untergrenze erhöht den möglichen Ladeerlös eines Speichers in Extremstunden; wer in solchen Stunden einspeisen muss, trägt ein höheres Verlustrisiko (Einordnung).

**Intraday.** Nach der Day-Ahead-Auktion ändern sich Wetter-, Last- und Kraftwerksprognosen. Der kontinuierliche Intraday-Handel in der einheitlichen Intraday-Marktkopplung (Single Intraday Coupling, SIDC) gleicht das aus: Kauf- und Verkaufsgebote treffen sich laufend in einem Orderbuch, und jedes Geschäft hat seinen eigenen Preis. Gehandelt werden Mengen von 0,1 bis 999 MW in Preisschritten von 0,01 €/MWh [W2V-12]. Grenzüberschreitende Geschäfte schließen je nach Grenze 60 oder 30 Minuten vor Lieferung (Gate-Closure, Kasten „Stand“). Der Handelsschluss innerhalb Deutschlands ist nicht am Primärtext geprüft [LÜCKE: Gate-Closure im kontinuierlichen Intraday-Handel innerhalb Deutschlands].

Seit dem 13.06.2024 ergänzen drei europäische Intraday-Auktionen (IDA) den kontinuierlichen Handel. Sie bepreisen grenzüberschreitende Übertragungskapazität auch im Intraday-Zeitraum [K02M-14; K02M-15, Suchauszug]. Die IDA1 schließt am Vortag um 15 Uhr, die IDA2 um 22 Uhr, beide für den ganzen Liefertag; die IDA3 schließt am Liefertag um 10 Uhr für die Lieferung von 12 bis 24 Uhr [W2V-13]. Während der Auktionen ruht die grenzüberschreitende Kapazitätsvergabe im kontinuierlichen Handel. Die Auktionen unterstützen Stunden-, Halbstunden- und Viertelstundenprodukte; welche Auflösung in DE-LU gilt, nennt die Quelle nicht [K02M-14].

> [!STAND]
> **Stand der Intraday-Regeln:** Die EU-Strommarktreform verkürzt die grenzüberschreitende Gate-Closure im kontinuierlichen Handel von 60 auf 30 Minuten vor Lieferung; das erste Fenster europäischer Grenzen ging am 14.01.2026 live [W2V-12]. Für die Grenzen AT–DE und CZ–DE ist keine Ausnahme (Derogation) verzeichnet, dort gelten also vermutlich schon 30 Minuten. Es folgen NL im vierten Quartal 2026, BE und SE4 im ersten Quartal 2027, DK1 im dritten Quartal 2027, DK2 bis 01.09.2027 sowie FR, PL und NO2 im vierten Quartal 2028 (Übersicht vom 25.02.2026) [W2V-14]. Die Zeiten der drei Intraday-Auktionen gelten seit dem 13.06.2024 [K02M-14, W2V-13]. Vor Verwendung prüfen.

**Indizes.** Weil im kontinuierlichen Handel jedes Geschäft seinen eigenen Preis hat, arbeiten Gutachten und Verträge mit Indizes. Die Börse veröffentlicht lizenzpflichtige Indizes wie ID1 und ID3. Nach Sekundärangaben bilden sie das mengengewichtete Mittel des kontinuierlichen Handels in der letzten Stunde bzw. den letzten drei Stunden vor Lieferung ab; die Börsendefinitionen sind nicht am Primärtext geprüft [LÜCKE: Definitionen ID1/ID3]. Das Erlösgutachten G1 rechnet seinen Intraday-Erlös gegen ID1 (Kapitel 6). Frei verfügbar ist der ID-AEP der ÜNB, ein Viertelstundenindex aus den zuletzt vor Lieferbeginn abgeschlossenen Viertelstundengeschäften mit zusammen 500 MW, bei Bedarf ergänzt um Stundengeschäfte; bei weniger Volumen ist er nicht definiert [K02M-17, S. 8]. Er koppelt den Ausgleichsenergiepreis an den Intraday-Markt (Abschnitt 2.4) und ist nicht handelbar; M1 nutzt ihn nur für eine Obergrenze der Intraday-Erlöse (A-M1-08).

Der ID-AEP zeigt, wie viel Bewegung nach der Day-Ahead-Auktion noch in den Preisen steckt. Seine mittlere Tagesspanne (Maximum minus Minimum) betrug 2024 435,6 €/MWh, 2025 357,1 €/MWh und vom 01.01. bis 26.09.2026 424,7 €/MWh, gegenüber 111,2, 130,4 und 182,1 €/MWh im Day-Ahead. Je Viertelstunde wich er im Mittel um 31–36 €/MWh vom Day-Ahead-Preis ab [M1D-06; M1, Lauf 20260927-intraday]. Die Intraday-Spanne war damit 2024 rund viermal, 2026 gut doppelt so groß wie die Day-Ahead-Spanne; ein Teil der Viertelstundenschwankung wird seit Oktober 2025 schon im Day-Ahead bepreist (Einschätzung). FfE nennt für 2025 eine Standardabweichung der Intraday-Preise von 36,9 €/MWh, die höchste seit drei Jahren, ohne Index und Auflösung anzugeben [K02M-01]. Öffentliche Kennzahlen zu ID1-, ID3- oder IDA-Spreads mit belastbarer Quelle fehlen [LÜCKE: Intraday-Spreads 2023–2026]. Das höchstmögliche Potenzial zeigt M1: Ohne Regelreserve könnte R1 2025 bei perfekter Voraussicht gegen den ID-AEP zusätzlich zu 90,4 k€/MW/a am Day-Ahead-Markt bis zu 85,9 k€/MW/a erlösen; hält er Regelreserve vor, schrumpft der Zuwachs auf 4,3 k€/MW/a [M1, Lauf 20260928-intraday]. Beides sind Obergrenzen gegen einen nicht handelbaren Index. Welcher Teil davon erreichbar ist, behandelt Kapitel 4.

| Stufe | Handelsform | Lieferperiode | Gebotsschluss | Preisgrenzen |
|---|---|---|---|---|
| Day-Ahead (SDAC) | eine Auktion je Tag, ein Preis je Zone und Periode | Viertelstunde seit 01.10.2025, vorher Stunde | Vortag 12 Uhr | −600 bis +4.000 €/MWh |
| IDA1 / IDA2 (SIDC) | Auktion | Liefertag 0–24 Uhr; Auflösung in DE-LU offen | Vortag 15 bzw. 22 Uhr | nicht belegt |
| IDA3 (SIDC) | Auktion | Liefertag 12–24 Uhr | Liefertag 10 Uhr | nicht belegt |
| Kontinuierlicher Intraday (SIDC) | fortlaufender Handel, Preis je Geschäft | Produktliste nicht am Primärtext geprüft | grenzüberschreitend 60 oder 30 min vor Lieferung; national offen | ±9.999 €/MWh |
| Ausgleichsenergie | kein Handel; Abrechnung durch die ÜNB zum reBAP | Viertelstunde | nach Lieferung | keine eigene Kappung; Plattformpreise ±15.000 €/MWh (anpassbar), Knappheitskomponente 19.998 €/MWh bei Ausschöpfung (Abschnitt 2.4) |

Table: Handelsstufen am deutschen Strommarkt

Quelle: W2V-10 bis W2V-14, W2V-16; K02M-24; M1D-01; K02M-14, K02M-16, K02M-17 (Stand 27.09.2026).

## Bilanzkreise, Ausgleichsenergie und Prognosefehler

Jede Einspeise- und Entnahmestelle gehört zu einem Bilanzkreis, einem Energiemengenkonto. Der Bilanzkreisverantwortliche meldet am Vortag eine viertelstundenscharfe Prognose von Einspeisung und Entnahme. Weichen die tatsächlichen Mengen ab, gleichen die ÜNB die Differenz mit Regelreserve aus (Kapitel 3) und rechnen sie als Ausgleichsenergie zum regelzonenübergreifenden einheitlichen Bilanzausgleichsenergiepreis (reBAP) ab [K02M-16]. Der reBAP wird je Viertelstunde bestimmt. Seine Basis sind seit 2022 nicht mehr die Kosten der Regelarbeit, sondern die Preise der europäischen Plattformen PICASSO (Sekundärregelarbeit, aFRR) und MARI (Minutenreservearbeit, mFRR); die Richtung bestimmt der Saldo des Netzregelverbunds der deutschen ÜNB (NRV-Saldo), also das gesamte Ungleichgewicht [K02M-16; K02M-17, S. 1–6]. Defizite und Überschüsse der ÜNB aus dieser Abrechnung fließen in die Netzentgelte [K02M-17, S. 13].

Seit Juni 2022 berechnen die ÜNB den reBAP nach der harmonisierten europäischen Methode (Festlegung BK6-21-192 vom 28.04.2022) in drei Modulen; zum Liefertag 08.12.2022 wurden die Regeln des Regelarbeitsmarkts (Festlegung BK6-22-162 vom 31.10.2022) und die Knappheitskomponente angepasst [K02M-16; K02M-17, S. 1]. Nach der geltenden Modellbeschreibung (seit 01.11.2023) ist das erste Modul das mengengewichtete Mittel der Grenzpreise, zu denen Regelarbeit über PICASSO und MARI abgerufen wird [K02M-17, S. 4–6]. Das zweite koppelt den reBAP an den ID-AEP: Ab einem NRV-Saldo von 500 MW hält er einen Mindestabstand von 25 %, mindestens aber 10 €/MWh; zwischen 0 und 500 MW wächst der Abstand linear auf diesen Wert. Das dritte ist eine Knappheitskomponente, eine quadratische Funktion des NRV-Saldos, die ab 80 % der dimensionierten Regelleistung greift [K02M-17, S. 9–11]. Der reBAP ist bei Unterdeckung des Netzregelverbunds (Fehlmenge im Netz) das Maximum, bei Überdeckung (Überschuss) das Minimum der drei Module [K02M-17, S. 3]. Eine betragsmäßige Kappung sieht die geltende Modellbeschreibung nicht vor; die frühere Begrenzung auf den Intraday-Stundenpreis ± 100–250 €/MWh (2016) gilt nicht mehr [K02M-16]. Begrenzt sind aber die Preise, aus denen Modul 1 entsteht: Für die Grenzpreise von PICASSO und MARI gilt in der Übergangszeit eine Spanne von ±15.000 €/MWh. Diese harmonisierte Grenze kann sich nach der ACER-Methodik automatisch ausweiten, jedoch nicht über die absolute technische Grenze von ±99.999 €/MWh [W2V-16]; den aktuellen Stand behandelt Kapitel 3 (Kasten „Stand der Preisregeln“). Wird die gesamte Reserve ausgeschöpft, erreicht die Knappheitskomponente das Doppelte des höchsten zulässigen Intraday-Gebotspreises, derzeit 19.998 €/MWh, also mehr als die Übergangsgrenze [K02M-17, S. 10–12]. Modul 2 sorgt dafür, dass sich ein offenes Ungleichgewicht gegenüber dem Intraday-Handel nicht lohnt, Modul 3 verteuert Ungleichgewichte in knappen Lagen (Einordnung).

Die Ungleichgewichte entstehen vor allem aus Prognosefehlern bei Wind, PV und Last sowie aus Ausfällen (Einordnung). Für einen Speicher ist das zweischneidig. Er kann im Intraday-Handel die Prognosefehler anderer ausgleichen und daran verdienen. Eigene Abweichungen vom Fahrplan, etwa nach einem Ausfall oder bei falsch geschätztem Ladezustand, kosten dagegen Ausgleichsenergie zum reBAP. Ein Beispiel: Hat R1 für 18–19 Uhr 10 MW verkauft und fällt aus, fehlen im Bilanzkreis 10 MWh. Der Erlös aus dem Day-Ahead-Verkauf bleibt, die fehlende Menge wird aber je Viertelstunde zum reBAP abgerechnet; liegt der reBAP über dem Verkaufspreis, entsteht ein Verlust in Höhe der Differenz mal Menge. Wird der Ausfall früh genug erkannt, lässt sich die Position im Intraday-Handel schließen (Einordnung). 2025 lag der reBAP im Mittel bei 91,2 €/MWh, in 1 % der Viertelstunden unter −91,4 und in 1 % über 341,8 €/MWh; in 69 Viertelstunden überstieg er 1.000 €/MWh, in 17 fiel er unter −1.000 €/MWh. 2024 erreichte er mit 14.999,99 €/MWh genau die Grenze der Plattformpreise; vom 01.01. bis 10.09.2026 fiel er bis auf −6.642,8 €/MWh [M1D-05; M1, Lauf 20260927-kapitel02]. Die Knappheitskomponente setzte den Preis 2024, 2025 und 2026 (bis 10.09.) nur in 1, 3 und 6 Viertelstunden, die Kopplung an den ID-AEP dagegen in 17, 51 und 64 % der Viertelstunden [M1D-08; M1, Lauf 20260927-kapitel02]. Seit 2025 bestimmt also meist der Intraday-Index mit Auf- oder Abschlag den Preis der Ausgleichsenergie (Einordnung). Im Business Case ist Ausgleichsenergie eine Kostenposition, keine Erlösquelle.

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Ob ein Speicher bewusst offene Positionen halten darf, um vom reBAP zu profitieren, regeln der Bilanzkreisvertrag und die Vorgaben der BNetzA zur Bilanzkreistreue; die Einzelheiten sind nicht belegt [LÜCKE: Bilanzkreisvertrag, Bilanzkreistreue, Sanktionen]. Eine solche Strategie kann gegen Vertragspflichten verstoßen. Vor Abschluss eines Vermarktungsvertrags sollte ein Rechtsanwalt für Energierecht klären, wer Bilanzkreisverantwortlicher ist, wer Ausgleichsenergiekosten trägt, ob Abweichungsstrategien zulässig sind und wie Haftung und Sanktionen verteilt sind. Die Klausel-Checkliste steht in Kapitel 5.

## Europäische Kopplung, Engpässe und Gebotszonen

Die Marktkopplung vergibt die grenzüberschreitende Übertragungskapazität zusammen mit dem Strom. Rechnerisch fließt Strom aus Zonen mit niedrigem in Zonen mit hohem Preis, bis die Kapazität ausgeschöpft ist; erst dann weichen die Preise voneinander ab (vereinfacht; Einordnung). Deutschland war 2025 physikalisch Nettoimporteur, mit 76,2 TWh Import, 54,3 TWh Export und einem Saldo von 21,9 TWh, 22,6 % weniger als 2024 [K02M-02]. Deutsche Spreads hängen deshalb auch von Erzeugung und Flexibilität der Nachbarländer ab (Einschätzung).

Innerhalb einer Gebotszone gilt ein Preis, als gäbe es keine Netzengpässe. Engpässe im Inneren lösen die Netzbetreiber nachträglich durch Redispatch: Sie weisen Anlagen vor dem Engpass an, weniger, und Anlagen dahinter, mehr einzuspeisen (Kapitel 3 und 15) [LÜCKE: Redispatchmengen und -kosten 2024–2025 aus dem Monitoringbericht]. Die Überprüfung der Gebotszonen (Bidding Zone Review) des Verbands der europäischen ÜNB (ENTSO-E) vom 28.04.2025 untersuchte 14 alternative Zuschnitte für Nord- und Zentraleuropa. Für DE-LU zeigte die Aufteilung in fünf Zonen den höchsten monetarisierten Nutzen nach dem Kriterium der wirtschaftlichen Effizienz: 339 Mio. € im Zieljahr 2025, gemittelt über drei Klimajahre; alle geprüften Teilungen lagen bei 251–339 Mio. € [K02M-07; K02M-08, S. 8]. Der Wert ist die Summe der Wohlfahrtsänderungen in allen Ländern der Region Zentraleuropa, kein Nutzen allein für Deutschland, und entspricht weniger als 1 % der simulierten Systemkosten. Er entsteht, weil eingesparte Redispatchkosten (613 Mio. €) den Rückgang der Marktwohlfahrt (274 Mio. €) übersteigen [K02M-08, S. 8, 13]. Die Eingangsdaten stammen überwiegend aus 2019 [K02M-08, S. 6]. Mit den geschätzten Umstellungskosten müsste eine Teilung 4–9 Jahre bestehen, um sich zu lohnen; bei Einführung um 2030 wäre der Break-even Mitte bis Ende der 2030er-Jahre erreicht [K02M-08, S. 8, 14]. Die ÜNB Zentraleuropas betonen, das Ergebnis folge aus der vorgegebenen ACER-Methodik und lasse wichtige Aspekte außer Acht; die nächsten Schritte liegen bei den Mitgliedstaaten [K02M-07].

> [!STAND]
> **Stand der Gebotszone:** Im Dezember 2025 legte das Bundesministerium für Wirtschaft und Energie einen Aktionsplan nach Art. 15 VO (EU) 2019/943 vor und behielt die einheitliche Gebotszone DE-LU bei (Suchauszug) [K02M-09, K02M-10]. Nach einer rechtswissenschaftlichen Analyse gibt es keine Handhabe, eine Teilung gegen den Willen Deutschlands durchzusetzen, solange Deutschland seinen Aktionsplan einhält; belegt ist das nur über Titel und Suchauszug [K02M-11]. Im September 2026 forderten Schleswig-Holstein und Hamburg erneut, regionale Gebotszonen zu prüfen (Suchauszug) [K02M-13]. Fristen, Rolle der EU-Kommission und nächste Überprüfung sind nicht am Primärtext geprüft [LÜCKE: Art. 14 und 15 VO (EU) 2019/943, Aktionsplan im Volltext]. Das Thema ist politisch beweglich und vor jeder Bewertung neu zu prüfen.

Für Speicher wäre eine Teilung erheblich: Day-Ahead-Preise, Spreads und Preisniveau hingen dann vom Standort ab, etwa Nord gegenüber Süd. Betroffen wäre die Standortbewertung für R1 und R2 im Raum Stuttgart und für G1 in Nordrhein-Westfalen (Kapitel 13); Richtung und Höhe sind nicht belegt (Einschätzung). Für einen Fonds gehört die Teilung deshalb als Szenario in die Risikoanalyse, nicht in den Basisfall. Der Vergleichsmarkt Italien zeigt, wie das aussieht: Er ist seit dem 01.01.2021 in sieben Marktzonen geteilt [K02M-25; K06M-13]; Kapitel 26 vertieft das.

## Marktdaten richtig lesen: Preisentwicklung 2023–2026

Die wichtigste Kennzahl für Arbitrage ist der TB-Spread (Top-Bottom), der Abstand zwischen den teuersten und den billigsten Zeitschritten eines Liefertags:

$$TB_n = \frac{1}{k}\sum_{i=1}^{k} p_{(N-i+1)} - \frac{1}{k}\sum_{i=1}^{k} p_{(i)}$$

mit $n$ als Speicherdauer in Stunden, $p_{(i)}$ als aufsteigend sortierten Preisen des Liefertags, $N$ als Zahl der Zeitschritte (24 oder 96) und $k = n$ bei Stunden- bzw. $k = 4n$ bei Viertelstundenpreisen. TB2 misst also, was ein 2-h-Speicher mit einem Zyklus je Tag ohne Verluste höchstens erzielen könnte; Reihenfolge, Wirkungsgrad und Zyklengrenze bleiben außer Betracht. Der Tagesspread ist Maximum minus Minimum; bei Stundenpreisen ist er gleich TB1. Tabelle 2.3 fasst die Marktdaten zusammen.

| Kennzahl | 2023 | 2024 | 2025 | 01.01.–26.09.2026 |
|---|---:|---:|---:|---:|
| Mittelwert (€/MWh) | 95,18 | 78,51 | 89,32 | 107,04 |
| Standardabweichung (€/MWh) | 47,6 | 52,7 | 52,5 | 67,3 |
| Ø Tagesspread Max − Min (€/MWh) | 97,9 | 111,2 | 130,4 | 182,1 |
| Ø TB1 / TB2 / TB4 (€/MWh) | 97,9 / 91,7 / 80,2 | 111,2 / 103,8 / 88,6 | 127,3 / 118,1 / 102,0 | 169,9 / 158,8 / 138,7 |
| TB2 Median (P10–P90) (€/MWh) | 83,2 (49,1–137,8) | 92,4 (41,5–162,4) | 108,4 (49,8–194,9) | 150,7 (52,9–238,1) |
| Minimum / Maximum (€/MWh) | −500,00 / 524,27 | −135,45 / 936,28 | −250,32 / 583,40 | −499,99 / 747,10 |
| Negative Preise | 301 h | 457 h | 525 h + 199 Vh (574,75 h-Äq.) | 1.836 Vh (459 h-Äq.) |
| Über 100 / 200 / 300 €/MWh (h bzw. h-Äq.) | 4.106 / 112 / 3 | 2.296 / 129 / 41 | 3.515,75 / 165,75 / 43,50 | 3.943,50 / 313,25 / 42,50 |

Table: Day-Ahead-Marktdaten DE-LU 2023–2026

Quelle: energy-charts/SMARD [M1D-01], Auswertung M1 (Lauf 20260927-kapitel02); Abgleich mit BNetzA [K02M-02, K02M-03] und FfE [K02M-01]. Auflösung bis 30.09.2025 Stunde, danach Viertelstunde; Vh = Viertelstunden, h-Äq. = Stundenäquivalente (Viertelstunden ÷ 4); auf Stundenmitteln über 300 €/MWh: 2025 40 h, 2026 38 h; 2026 Teiljahr; nominal (Stand 27.09.2026).

Drei Befunde prägen die Jahre 2023–2026. Erstens folgen die Spreads nicht dem Preisniveau: Von 2023 auf 2024 fiel das Mittel um 17,5 %, der TB2-Spread stieg um 13 %. 2025 stiegen beide um knapp 14 % [K02M-02; M1, Lauf 20260927-kapitel02; eigene Rechnung]; rechnet man auch das vierte Quartal mit Stundenmitteln, stieg der TB2-Spread um knapp 12 % auf 116,1 €/MWh [M1, Lauf 20260927-kapitel02]. Das Niveau folgt vor allem den Brennstoffpreisen, 2025 etwa dem höheren Gaspreis (Abschnitt 2.1), die Spreads dagegen dem Abstand zwischen Mittagstal und Abendspitze (Einordnung). Zweitens nahmen die Spreads 2026 kräftig zu. Vom 01.01. bis 26.09.2026 lag der TB2-Spread um 25 % über dem vollständig stündlichen Vorjahreszeitraum (158,8 gegenüber 127,4 €/MWh), auf Stundenmitteln immer noch um 19 %; nur rund 6 Prozentpunkte gehen also auf die Viertelstunde zurück [M1, Lauf 20260927-kapitel02]. Wie stark die Jahreszeit wirkt, zeigt das vierte Quartal 2025 mit einem mittleren TB2-Spread von nur 87,9 €/MWh (Abschnitt 2.3). Teiljahre sind deshalb nur mit dem Vorjahreszeitraum vergleichbar. Drittens sind die Tageswerte schief verteilt. Der Median liegt unter dem Mittel, und 2025 lag das 90-%-Quantil des TB2-Spreads fast viermal so hoch wie das 10-%-Quantil (194,9 gegenüber 49,8 €/MWh). Der Anteil der Tage mit einem TB2-Spread über 200 €/MWh stieg von 1,1 % (2023) über 4,1 % (2024) und 9,3 % (2025) auf 21,2 % im Teiljahr 2026 [M1, Lauf 20260927-kapitel02]. Ein großer Teil des Arbitrageerlöses fällt deshalb an wenigen Tagen an, und die Verteilung (Abbildung 2.3) sagt mehr als ihr Mittelwert.

![Verteilung des täglichen TB2-Spreads Day-Ahead DE-LU 2023 bis 26.09.2026 in €/MWh (Box: 25.–75. Perzentil, Antennen: 10.–90. Perzentil); ab 01.10.2025 Viertelstunden; nominal](05_figures/K02/02_tagesspreads_verteilung.png)

Quelle: eigene Berechnung, Modell M1 (Lauf 20260927-kapitel02); Day-Ahead DE-LU: energy-charts/SMARD [M1D-01] (Stand 27.09.2026).

Die Definition entscheidet über die Zahl. FfE nennt für 2025 einen mittleren täglichen Spread von 130,4 €/MWh [K02M-01]. Das ist der Tagesspread aus Maximum und Minimum auf der jeweils gehandelten Auflösung, wie die Nachrechnung zeigt; der TB2-Spread lag im selben Jahr bei 118,1 €/MWh [M1, Lauf 20260927-kapitel02]. Spreads sind deshalb nur mit Definition, Auflösung und Zeitraum vergleichbar.

Dasselbe gilt für negative Preise. Bis zum 30.09.2025 gab es Stundenpreise, seither Viertelstundenpreise. Für 2025 ergeben sich deshalb drei Zahlen: 525 negative Stunden bis September plus 199 negative Viertelstunden ab Oktober, zusammen 574,75 Stundenäquivalente; 576 Stunden mit negativem Stundenmittel; und 573 Stunden laut BNetzA, deren Zählweise für Oktober bis Dezember offen ist [K02M-02; M1, Lauf 20260927-kapitel02]. FfE nennt rund 575 Stunden [K02M-01]. Für 2026 stehen 1.836 negative Viertelstunden (459 Stundenäquivalente) 466 Stunden mit negativem Stundenmittel gegenüber. Eine einzelne negative Viertelstunde in einer sonst positiven Stunde zählt als Viertelstunde mit, im Stundenmittel oft nicht; umgekehrt zählt eine Stunde mit negativem Mittel voll, auch wenn nur zwei ihrer Viertelstunden negativ sind. Das Buch weist deshalb Stunden bis 30.09.2025 und Viertelstunden ab 01.10.2025 getrennt aus und nutzt Stundenäquivalente nur als Hilfsgröße.

Die Preisdauerlinie sortiert alle Preise eines Jahres absteigend. Sie zeigt, in wie vielen Stunden der Preis mindestens einen bestimmten Wert erreichte, und macht beide Enden sichtbar, die für Speicher zählen: die Spitzen links und die negativen Preise rechts. Weil Jahre unterschiedlich viele Zeitschritte haben, trägt Abbildung 2.4 sie über dem Anteil der Zeit auf. Die Linie für 2026 liegt in rund drei Vierteln der Zeit oberhalb der Vorjahre (bei 50 % der Zeit 111,7 gegenüber 79,6–98,0 €/MWh), im unteren Viertel aber darunter (bei 85 % der Zeit 31,2 gegenüber 32,7–49,8 €/MWh) [M1, Lauf 20260927-kapitel02]: höhere Spitzen und tiefere Täler zugleich, und genau das treibt die Spreads (Einordnung). Die Stundenmittel derselben Viertelstunden weichen vor allem an den Rändern ab.

![Preisdauerlinien der Day-Ahead-Preise DE-LU 2023 bis 26.09.2026 in €/MWh über dem Anteil der Zeit; 2026 zusätzlich als Stundenmittel (gestrichelt); Achse auf −200 bis 500 €/MWh begrenzt; nominal](05_figures/K02/02_preisdauerlinien.png)

Quelle: eigene Berechnung, Modell M1 (Lauf 20260927-kapitel02); Day-Ahead DE-LU: energy-charts/SMARD [M1D-01] (Stand 27.09.2026).

Für eigene Auswertungen eignen sich die Day-Ahead-Preise der energy-charts-Schnittstelle (Daten der BNetzA/SMARD, Lizenz CC BY 4.0) [M1D-01] sowie reBAP und ID-AEP von netztransparenz.de [M1D-05, M1D-06]. Zu jeder Kennzahl gehören Auflösung, Zeitzone (Ortszeit mit 23- und 25-Stunden-Tagen bei der Zeitumstellung), Zeitraum und Preisbasis (nominal).

## Was die Preise für Speichererlöse bedeuten

Für einen Zyklus je Tag lässt sich der Day-Ahead-Erlös eines Speichers direkt aus den Preisen berechnen:

$$R_d = E^{\text{ent}} \cdot \bar p^{\text{top}}_d - E^{\text{lade}} \cdot \bar p^{\text{bottom}}_d - c_{\text{deg}} \cdot E^{\text{ent}} = E^{\text{ent}} \cdot TB_{n,d} - \left(E^{\text{lade}} - E^{\text{ent}}\right) \cdot \bar p^{\text{bottom}}_d - c_{\text{deg}} \cdot E^{\text{ent}}$$

mit $R_d$ als Tageserlös in €, $E^{\text{ent}} = E \cdot \sqrt{\eta}$ als am Netzverknüpfungspunkt abgegebener und $E^{\text{lade}} = E / \sqrt{\eta}$ als bezogener Energie in MWh, $E$ als nutzbarer Kapazität, $\eta$ als Wirkungsgrad über einen Zyklus (A-001, A-M1-01), $\bar p^{\text{top}}_d$ und $\bar p^{\text{bottom}}_d$ als Mittel der teuersten und billigsten Zeitschritte in €/MWh und $c_{\text{deg}}$ als Degradationskosten je entladener MWh (A-002). Die zweite Form zeigt: Der TB-Spread bestimmt den Erlös, die Verluste kosten zusätzlich den Ladepreis auf die Mehrenergie. An Tagen mit negativen Preisen kehrt sich das um. Am 11.05.2025 lagen die zwei billigsten Stunden bei −250,32 und −230,98 €/MWh, die zwei teuersten bei 124,86 und 117,11 €/MWh (TB2 = 361,64 €/MWh) [M1, Lauf 20260927-kapitel02; M1D-01]. Nach der Formel, ohne Leistungsgrenze, hätte R1 mit einem Zyklus vor Degradation 7.417 € verdient, ohne Verluste nur 7.233 €, weil er für die zusätzlich geladenen 2,79 MWh bezahlt wird (eigene Rechnung).

Die Spreads bestimmen auch, was Regelreserve mindestens kosten muss: Wer Leistung für Regelreserve vorhält, verzichtet in dieser Zeit auf Arbitrage, und diese Opportunitätskosten bilden die Untergrenze vernünftiger Regelleistungsgebote (Kapitel 3 und 6). Mit den Spreads ist auch das Gewicht der Arbitrage im Erlösmix gestiegen. Im Modell M1 trug der Day-Ahead-Handel bei R1 mit Regelreserve 2025 nur 5 % des Erlöses, im Teiljahr 2026 23 % (perfekte Voraussicht) [M1, Lauf 20260928-standalone]; Kapitel 4 behandelt die Aufteilung auf die Märkte. Ob der Speicherzubau die Spitzen schon dämpft, ist offen. Laut Marktstammdatenregister waren am 15.10.2025 rund 2,4 GW und 3,2 GWh Großbatteriespeicher in Betrieb [K03M-07], nach FfE Ende 2025 3,9 GWh, über alle Segmente einschließlich Heimspeichern knapp 25 GWh [K02M-01]. Die Zahl der Stunden über 300 €/MWh blieb 2024 und 2025 mit 41 und 40 praktisch gleich [K02M-02]. Im Teiljahr 2026 waren es dagegen 38 Stunden gegenüber 24 im Vorjahreszeitraum (Stundenmittel), dazu 41 Viertelstunden über 500 €/MWh [M1, Lauf 20260927-kapitel02]. Daraus ist eine Dämpfung weder belegt noch widerlegt, weil Gaspreis, Winterwind und Importe zugleich wirkten (Einschätzung) [LÜCKE: quantitative Wirkung der Speicherflotte auf Preisspitzen].

Für die Bewertung folgt daraus eine Vorsichtsregel (Einschätzung). Der mittlere TB2-Spread schwankte 2023–2026 zwischen 91,7 und 158,8 €/MWh, und die Marktregeln änderten sich in derselben Zeit mehrfach. Wer den Erlös einer Anlage auf ein einzelnes Basisjahr stützt, übernimmt dessen Wetter, Brennstoffpreise und Regeln. Erlösgutachten sollten deshalb mehrere Jahre und das jüngste Ist ausweisen und erklären, welche Spreads sie für die Zukunft ansetzen (Kapitel 6).

> [!BEISPIEL]
> **Rechenbeispiel 2.1: Tagesarbitrage R1 – Spread-Rechnung gegenüber Dispatch-Modell**
>
> *Ziel:* den theoretischen Day-Ahead-Erlös von R1 (10 MW/20 MWh nutzbar) mit einem Zyklus je Tag aus TB2 berechnen und mit dem Modell M1 vergleichen. Lauf-IDs: 20260927-kapitel02 (Marktkennzahlen und typische Tage; M1 Version 1.1.0) und 20260927-standalone (Jahreserlöse „nur Day-Ahead“; Version 1.0.0); Preise bis Liefertag 26.09.2026 [M1D-01]. Alle Werte brutto, nominal, ohne Regelreserve und Intraday.
>
> *Schritt 1 – Energiemengen:* Mit $\eta = 0{,}87$ (A-001), symmetrisch aufgeteilt (A-M1-01), gibt R1 je vollem Durchlauf des nutzbaren Fensters $E^{\text{ent}} = 20 \cdot \sqrt{0{,}87} = 18{,}655$ MWh ab und bezieht $E^{\text{lade}} = 20 / \sqrt{0{,}87} = 21{,}442$ MWh (D-021); die Differenz beträgt 2,79 MWh. Degradationskosten: 2,3 €/MWh (A-002).
>
> *Schritt 2 – zwei typische Tage 2026:* M1 wählt je Jahreszeit einen Dienstag bis Donnerstag, dessen TB2 und Tagesmittel den Medianen am nächsten liegen (Sommer: Juni–August, Winter: Januar–Februar 2026; Auswahlregel A-M1-16). Am Sommertag 09.07.2026 kosteten die acht billigsten Viertelstunden (13:30–15:15 Uhr) im Mittel 36,59 €/MWh, die acht teuersten (19:45–22:00 Uhr) 216,13 €/MWh. Die Formel ergibt 18,655 × 216,13 − 21,442 × 36,59 − 2,3 × 18,655 = 4.031,9 − 784,6 − 42,9 = 3.204 €. Die Tagesoptimierung in M1 berücksichtigt dagegen die zeitliche Reihenfolge, die Leistungsgrenze von 10 MW, einen Ladezustand von 50 % zu Tagesbeginn und -ende (A-M1-02) und höchstens zwei Zyklen je Tag (A-021):
>
> | Tag | Raster | $\bar p^{\text{top}}$ / $\bar p^{\text{bottom}}$ (€/MWh) | Formel (€) | Optimierung (€) | Zyklen |
> |---|---|---:|---:|---:|---:|
> | Sommer, 09.07.2026 | Viertelstunde | 216,13 / 36,59 | 3.204 | 2.957 | 1,78 |
> | Sommer, 09.07.2026 | Stundenmittel | 212,01 / 40,82 | 3.037 | 2.653 | 1,83 |
> | Winter, 05.02.2026 | Viertelstunde | 139,85 / 87,30 | 694 | 611 | 1,43 |
> | Winter, 05.02.2026 | Stundenmittel | 138,57 / 87,61 | 663 | 530 | 0,93 |
>
> Table: Tagesarbitrage R1 an typischen Tagen 2026 (nach Degradation)
>
> Quelle: M1, Lauf 20260927-kapitel02 (Stand 27.09.2026).
>
> *Zählweise der Zyklen:* M1 zählt am Netzverknüpfungspunkt entladene Energie ÷ nutzbare Energie (A-021). Ein voller Durchlauf des nutzbaren Fensters von R1 zählt damit als 0,93 Zyklen, und die Grenze von 2,0 entspricht batterieseitig rund 2,14 Durchläufen. Am Wintertag (Stundenmittel) fährt M1 genau einen solchen Durchlauf. Wie eine Herstellergarantie Zyklen zählt, ist im Vertrag zu prüfen; beim Vergleich ist die Zählweise zu nennen (Kapitel 9).
>
> *Schritt 3 – Jahreswert aus TB2:* Der mittlere TB2-Spread betrug 2025 118,1 €/MWh und vom 01.01. bis 26.09.2026 158,8 €/MWh; im Jahresmittel kosteten die billigsten Zeitschritte $\bar p^{\text{bottom}}$ = 35,8 bzw. 30,4 €/MWh, die teuersten brachten $\bar p^{\text{top}}$ = 153,9 bzw. 189,2 €/MWh [M1, Lauf 20260927-kapitel02]. Auf 365 Tage gerechnet (2026 linear hochgerechnet, wie in M1, A-M1-12) ergibt die Formel die Werte der folgenden Tabelle; der Verlustterm bewertet 365 × 2,79 MWh = 1.017 MWh/a Mehrenergie zum mittleren Ladepreis. Hinzu kommen 15,7 k€/a Degradationskosten.
>
> *Schritt 4 – Vergleich mit M1:* Über das ganze Jahr optimiert, erlöst R1 nur am Day-Ahead-Markt bei perfekter Voraussicht 903,8 k€/a (2025) bzw. 1.184,3 k€/a (2026, hochgerechnet) mit 1,63 bzw. 1,70 Zyklen je Tag (M1-Zählweise). Im realistischen Fall mit Vergleichstagsprognose (Vortag bzw. Vorwoche, A-M1-05) und 97 % Verfügbarkeit (A-020) sind es 706,6 bzw. 939,8 k€/a, also 78 bzw. 79 % davon [M1, Lauf 20260927-standalone].
>
> | k€/a (vor Degradation) | 2025 | 2026 (hochgerechnet) |
> |---|---:|---:|
> | TB2 ohne Verluste (365 × 20 MWh × TB2) | 862,2 | 1.159,3 |
> | TB2-Spread-Term mit Verlusten (365 × 18,655 MWh × TB2) | 804,2 | 1.081,3 |
> | abzüglich Verlustterm (1.017 MWh/a × $\bar p^{\text{bottom}}$) | 36,4 | 30,9 |
> | Spread-Rechnung mit Verlusten | 767,8 | 1.050,4 |
> | M1 perfekte Voraussicht (Jahresoptimierung) | 903,8 | 1.184,3 |
> | M1 realistisch, ohne Verfügbarkeitsabzug (÷ 0,97) | 728,5 | 968,8 |
> | M1 realistisch (97 % Verfügbarkeit) | 706,6 | 939,8 |
>
> Table: Arbitrageerlös R1 nur Day-Ahead: Spread-Rechnung gegenüber M1
>
> Quelle: M1, Läufe 20260927-kapitel02 und 20260927-standalone; eigene Rechnung (Stand 27.09.2026).
>
> *Deutung:* Die Spread-Rechnung liegt zwischen den beiden Modellwerten, und drei Effekte erklären die Abstände. Erstens die Zyklen: M1 fährt bei perfekter Voraussicht bis zu zwei Zyklen je Tag, etwa an Wintertagen mit Morgen- und Abendspitze (Übung 2.3), und kann Energie über Mitternacht verschieben. Schon die verlustfreie Rechnung liegt deshalb 4,6 bzw. 2,1 % unter M1, der Spread-Term 11,0 bzw. 8,7 %. Zweitens die Randbedingungen: Die Formel ignoriert Ladedauer (2,14 h bei 10 MW), Reihenfolge und Ladezustand am Tagesende und überschätzt deshalb an einzelnen Tagen; an den typischen Tagen erreicht die Tagesoptimierung trotz 1,78 bzw. 1,43 Zyklen (die Formel entspricht 0,93) nur 92 bzw. 88 % der Formel. Drittens Voraussicht und Verfügbarkeit: Die Formel unterstellt, dass man die teuersten und billigsten Zeitschritte kennt und die Anlage immer verfügbar ist. Der realistische Fall rechnet mit Vergleichstagsprognosen und 97 % Verfügbarkeit; die Spread-Rechnung liegt auch über seinem Wert ohne Verfügbarkeitsabzug. Die Viertelstunde verstärkt die Unterschiede: Sie hebt den Wert der Tagesoptimierung um 11,5 % (Sommer) bzw. 15,2 % (Winter), den der Formel nur um 5,5 bzw. 4,6 %. Der TB2-Spread liefert damit die richtige Größenordnung, aber keinen Erlös. Wie viel ein Speicher tatsächlich erreicht, klärt erst ein Dispatch-Modell mit Reihenfolge, Zyklen und Prognosen (Kapitel 4).

## Praxis-Check und typische Fehler {.unnumbered}

> [!TIP]
> **Praxis-Check:** Marktdaten in Angeboten, Gutachten und Verträgen
>
> - Welche Spread-Definition gilt (Maximum minus Minimum, TB1, TB2, TB4), auf welcher Auflösung (Stunde, Viertelstunde, Stundenmittel) und für welchen Zeitraum (Kalenderjahr, Teiljahr, Monat)?
> - Enthält eine Arbitrage-Rechnung Wirkungsgrad, Zyklengrenze (mit Zählweise: am Netzverknüpfungspunkt oder batterieseitig), Leistungsgrenze, zeitliche Reihenfolge und Verfügbarkeit, und mit welcher Voraussicht rechnet sie?
> - Wie werden negative Preise gezählt (Stunden, Viertelstunden, Stundenäquivalente, Stundenmittel), und passt die Zählweise zum Vergleichsjahr?
> - Ist das Basisjahr gegen das jüngste Ist geprüft? Der TB2-Spread lag 2026 bis September 25 % über dem Vorjahreszeitraum, auf Stundenmitteln 19 %.
> - Entsprechen Preisgrenzen und Marktregeln dem aktuellen Stand (Day-Ahead −600/+4.000 €/MWh, Intraday ±9.999 €/MWh, Viertelstunde seit 01.10.2025)?
> - Wird Intraday gegen handelbare Preise oder gegen einen Index gerechnet (ID1, ID3, ID-AEP), und sind die Daten lizenzrechtlich nutzbar?
> - Wer ist Bilanzkreisverantwortlicher, wer trägt die Ausgleichsenergiekosten, und schließt der Vertrag Abweichungsstrategien aus?
> - Wie berücksichtigt das Gutachten eine mögliche Teilung der Gebotszone, und enthält der Vermarktungsvertrag eine Anpassungsklausel für geänderte Marktregeln?
> - Sind Datenquelle, Datenstand und Preisbasis (nominal) genannt?

> [!WARNING]
> **Typische Fehler:**
>
> - Den Tagesspread (2025: 130,4 €/MWh) als Arbitrage-Spread lesen; der TB2-Spread lag bei 118,1 €/MWh, und Spread mal Kapazität mal 365 ist noch kein Erlös.
> - Negative Stunden 2024 mit negativen Viertelstunden 2026 vergleichen (457 h gegenüber 1.836 Vh).
> - Das Teiljahr 2026 als Jahreswert lesen: Es enthält den Sommer, aber kein viertes Quartal.
> - Peak/Base als Spread-Indikator verwenden (2025: 1,03).
> - Den Umstellungstermin der Viertelstunde falsch ansetzen, wie G1 mit dem 01.05.2025 statt dem 01.10.2025.
> - Den „Jahresmarktwert Solar nach § 33 EEG 2012“ (2025: 6,170 ct/kWh) statt des JW Solar (4,508 ct/kWh) als Capture-Preis verwenden.
> - Den ID-AEP oder einen Börsenindex wie einen handelbaren Preis behandeln.
> - Ausgleichsenergie als Erlösquelle einplanen oder den reBAP für gedeckelt halten: Er erreichte 2024 die Plattformgrenze von 15.000 €/MWh, und die Knappheitskomponente kann darüber liegen.
> - In Modellen und Stresstests noch mit der alten Untergrenze von −500 €/MWh rechnen.

## Zusammenfassung {.unnumbered}

1. Der Day-Ahead-Preis entsteht aus der Merit-Order; die Residuallast entscheidet, welche Anlage ihn setzt. PV senkt die Mittagspreise, windarme Winterabende treiben die Preise; bei Knappheit entstehen Spitzen bis 936,28 €/MWh (2024).
2. Negative Preise nahmen von 301 (2023) über 457 (2024) auf 573 Stunden (2025) zu; die meisten liegen knapp unter null. Die Ausreißer erreichten 2023 und 2026 die damalige Untergrenze von −500 €/MWh; seit dem Handelstag 28.05.2026 liegt sie bei −600 €/MWh.
3. Die Capture-Rate Solar fiel laut Nachrechnung von 0,759 (2023) auf 0,514 (2025; Wertfaktor der ÜNB 0,505). Im Teiljahr 2026 lag sie trotz 20 % mehr Solarstrom mit 0,515 über dem Vorjahreszeitraum (0,474); die Ursache ist nicht belegt.
4. Die Spreads folgen nicht dem Preisniveau. Der mittlere TB2-Spread stieg von 91,7 (2023) auf 118,1 €/MWh (2025) und lag 2026 bis September 25 % über dem Vorjahreszeitraum (auf Stundenmitteln 19 %); die Tageswerte sind schief verteilt.
5. Die Viertelstunde seit dem 01.10.2025 erhöht die Spreads und den Arbitragewert kurzer Speicher, ändert aber auch die Zählung: Stunden und Viertelstunden sind getrennt auszuweisen.
6. Intraday-Auktionen und kontinuierlicher Handel bepreisen Prognosefehler; die Tagesspanne des Intraday-Index ID-AEP ist zwei- bis viermal so groß wie die des Day-Ahead-Preises, der Index ist aber nicht handelbar.
7. Der reBAP rechnet Abweichungen in drei Modulen ohne eigene Kappung ab. Begrenzt sind nur die Plattformpreise des ersten Moduls (±15.000 €/MWh, anpassbar); diese Grenze erreichte er 2024, die Knappheitskomponente kann darüber liegen. Für den Speicher ist Ausgleichsenergie Kosten- und Vertragsrisiko, keine Erlösquelle.
8. Für R1 lag die TB2-Rechnung 2025 und 2026 zwischen dem realistischen und dem perfekten Modellwert. Die Gebotszonenteilung bleibt ein Standortrisiko, das als Szenario zu prüfen ist; der von ENTSO-E ermittelte Nutzen betrifft die ganze Region und liegt unter 1 % der Systemkosten.

## Übungen {.unnumbered}

**Übung 2.1 (Herleiten).** (a) Berechnen Sie die Grenzkosten eines GuD-Kraftwerks mit 58 % Wirkungsgrad bezogen auf den Heizwert (Umrechnungsfaktor 0,903) beim Gaspreis 2025 von 37,2 €/MWh (Brennwert), 0,2016 t CO₂ je MWh Brennstoff (Heizwert) und einem CO₂-Preis von 60 €/t (Wirkungsgrad und CO₂-Preis sind Annahmen der Übung; sonstige variable Kosten vernachlässigen). (b) Erklären Sie mit Merit-Order und Residuallast, warum der Day-Ahead-Preis am 11.05.2025 von 13 bis 14 Uhr bei −250,32 €/MWh und am 20.01.2025 von 17 bis 18 Uhr bei 583,40 €/MWh lag. (c) Welcher Teil des Preises vom 20.01.2025 lässt sich nicht aus den Grenzkosten nach (a) erklären, und wie nennt man ihn? (d) Warum gibt es im kontinuierlichen Intraday-Handel keinen einheitlichen Preis je Lieferperiode, und was folgt daraus für Intraday-Erlösangaben in Gutachten?

**Übung 2.2 (Rechnen).** Nutzen Sie Tabelle 2.3. (a) Berechnen Sie den Anteil der Zeit mit negativen Preisen 2024 (8.784 h), 2025 (8.760 h) und im Teiljahr 2026 (01.01.–26.09.2026 = 6.455 h). (b) Erklären Sie, warum für 2025 die Werte 573, 574,75 und 576 Stunden nebeneinander stehen. (c) Ein Verkäufer schreibt: „2026 gab es bis September 1.836 negative Stunden, viermal so viele wie 2024.“ Korrigieren Sie die Aussage. (d) Lesen Sie aus Abbildung 2.4 ab, in welchem Anteil der Zeit der Preis 2026 (Viertelstunden, durchgezogene Linie) unter 50 €/MWh lag. Warum ist der Anteil negativer Preise aus (a) in der Abbildung kaum zu erkennen, und warum lässt sich aus der Preisdauerlinie kein TB2-Spread ablesen?

**Übung 2.3 (Rechnen).** Am 20.01.2025 lagen die Day-Ahead-Preise in den Stunden ab 3, 4, 8, 9, 12, 13, 17 und 18 Uhr bei 114,41, 115,45, 431,99, 291,70, 176,00, 171,39, 583,40 und 473,28 €/MWh. 3 und 4 Uhr waren die billigsten, 17 und 18 Uhr die teuersten Stunden des Tages, 12 und 13 Uhr die billigsten zwischen Morgen- und Abendspitze [M1D-01; M1, Lauf 20260927-kapitel02]. (a) Berechnen Sie TB2 und den Erlös von R1 mit einem Zyklus nach der Formel aus Abschnitt 2.7, ohne Degradation und ohne Leistungsgrenze. (b) Berechnen Sie den Erlös mit zwei Zyklen (Nacht → Morgen, Mittag → Abend), beginnend und endend mit leerem Speicher. (c) Was folgt daraus für die Aussagekraft von TB2?

**Übung 2.4 (Analysieren).** (a) Berechnen Sie, um wie viele €/MWh der Jahresmarktwert Solar 2024 (Tabelle 2.1) unter dem Mittelpreis lag, einmal mit dem BNetzA-Mittel (7,851 ct/kWh) und einmal mit dem Spotmittel (7,946 ct/kWh). Vergleichen Sie mit 2025, und begründen Sie, welche Bezugsgröße Sie verwenden. (b) Analysieren Sie qualitativ, wie (i) weiterer PV-Zubau, (ii) weiterer Speicherzubau, (iii) eine Teilung der Gebotszone, (iv) ein windarmer Winter und (v) mehr grenzüberschreitende Übertragungskapazität den TB2-Spread am Standort von R1 verändern könnten. Kennzeichnen Sie, was belegt und was Einschätzung ist.

**Übung 2.5 (Bewerten).** Ein Verkäufer begründet den Kaufpreis für R1 so: „Der mittlere Tagesspread 2025 betrug 130,4 €/MWh; 130,4 €/MWh × 20 MWh × 365 Tage ergeben einen Arbitrageerlös von rund 952 k€/a.“ (a) Prüfen Sie die Rechnung und die verwendete Definition. (b) Stellen Sie sie den Werten aus Rechenbeispiel 2.1 gegenüber und nennen Sie drei Gründe für die Abweichung. (c) Welche Angaben fordern Sie vom Verkäufer an?

**Übung 2.6 (Entscheiden).** Ein Optimierer bietet an, Ihren Speicher zusätzlich „gegen den reBAP“ zu fahren: In Viertelstunden mit erwartet hohem reBAP weiche der Speicher bewusst vom Fahrplan ab, der Fonds erhalte die Hälfte des Mehrerlöses. Entscheiden Sie in höchstens sechs Sätzen, ob Sie das Angebot annehmen, und nennen Sie die Vertragspunkte und Fachleute, die Sie vorher einbinden.

Die Lösungen stehen im Anhang A unter Kapitel 2.

## Quellen und Stand {.unnumbered}

Qualität nach dem Quellenregister: A = Primärquelle, B = anerkannte Sekundärquelle, C = Fachmedium oder Anbieter; „Suchauszug“ = nicht im Volltext geprüft.

- [G1] Erlösgutachten G1 (anonymisiert, vertraulich), Bericht vom 27.08.2026 (B).
- [K02M-01] Forschungsstelle für Energiewirtschaft (FfE): German electricity prices on the EPEX Spot exchange in 2025 (20.01.2026; B).
- [K02M-02] Bundesnetzagentur: Daten zum Strommarkt 2025, Pressemitteilung (05.01.2026; A).
- [K02M-03] Bundesnetzagentur: Daten zum Strommarkt 2023, Pressemitteilung (03.01.2024; A).
- [K02M-05] ÜNB (netztransparenz.de): Marktwertübersicht, Jahresmarktwerte nach EEG (Jahreswerte 2025; A).
- [K02M-07], [K02M-08] ENTSO-E: Bidding Zone study released (28.04.2025; A); Bidding Zone Review of the 2025 Target Year, Main Report (04/2025; A; Volltext S. 1–8, 13–14).
- [K02M-09] Bundesministerium für Wirtschaft und Energie: Aktionsplan Gebotszone (12/2025; A; Suchauszug).
- [K02M-10] energiezukunft: Deutschland will einheitliche Stromgebotszone beibehalten (12/2025; C; Suchauszug).
- [K02M-11] Stiftung Umweltenergierecht: Keine Handhabe für eine einseitige Gebotszonenteilung (2026; B; Suchauszug).
- [K02M-13] ms-aktuell: Strompreiszone – Norden erhöht Druck (07.09.2026; C; Suchauszug).
- [K02M-14] ENTSO-E: Intraday Auctions on SIDC (abgerufen 27.09.2026; A).
- [K02M-15] EPEX SPOT: Intraday Auctions implemented across Europe on 13 June 2024 (13.06.2024; A; Suchauszug).
- [K02M-16] Amprion: Informationen zum Ausgleichsenergiepreis (reBAP) (abgerufen 27.09.2026; A).
- [K02M-17] ÜNB: Modellbeschreibung der reBAP-Berechnung ab 01.11.2023 (01.11.2023; A).
- [K02M-21], [K02M-22] ACER: Decision No 02/2026 (SDAC, 04.02.2026) und No 03/2026 (SIDC, 02/2026), harmonisierte Preisgrenzen (A; Entscheidungstexte ohne Anhang I, gelesen über den ENTSO-E-Spiegel).
- [K02M-24] NEMO Committee: SDAC-Bericht zur Teilentkopplung vom 25.06.2024 (26.07.2024; A).
- [K02M-25] Terna: Le nuove zone del mercato elettrico, Lightbox (08.02.2021; A; ID als Vorschlag).
- [K03M-07] Bundesnetzagentur: Themenseite Stromspeicher (17.03.2026, Daten Stand 15.10.2025; A).
- [K03R-01] Strom-Versorgungssicherheits-und-Kapazitätengesetz (StromVKG), § 2 Nr. 33, § 81 und Anlage 7 (Ausfertigung 21.07.2026; A).
- [K06M-13] Modo Energy: July 2026 Italy Forecast (07/2026; B; Suchauszug).
- [K15M-01] ÜNB (netztransparenz.de): Marktwertübersicht, MW Solar(a) nach § 33 EEG 2012 (2026; A).
- [VR3-29] DGS: Der Jahresmarktwert Solar 2025, Datenbasis netztransparenz.de und energy-charts (15.01.2026; B).
- [VR3-30] Clearingstelle EEG|KWKG: Das Solarspitzengesetz, Folien (02.07.2025; A).
- [W2V-01], [W2V-06] EEG 2023, § 51 und § 3 Nr. 42a (Stand 18.12.2025; A).
- [W2V-10] NEMO Committee: SDAC Communication Note, Harmonised Minimum Clearing Price −600 EUR/MWh ab 28.05.2026 (07.05.2026; A).
- [W2V-11] NEMO Committee: SDAC, Informationsseite und Mitteilungsliste, Umstellung auf Viertelstunden (Mitteilungen bis 07.05.2026; A).
- [W2V-12] NEMO Committee: Continuous trading (SIDC), Products Available und Cross-Zonal Gate Closure Times (abgerufen 27.09.2026; A).
- [W2V-13] NEMO Committee: Intraday Auctions (IDA), Gate Closure Times (abgerufen 27.09.2026; A).
- [W2V-14] ENTSO-E: Border-based derogation overview for 30-minute IDCZGCT (25.02.2026; A).
- [W2V-16] ACER: Entscheidung 09/2024, Anhang Ia, Methodik der Regelarbeitspreise mit harmonisierten Höchst- und Mindestpreisen (2024; A).
- [M1D-01], [M1D-04], [M1D-06] Day-Ahead-Preise, Solarerzeugung (energy-charts) und ID-AEP (netztransparenz.de), Snapshot bis 26.09.2026 (A); [M1D-05], [M1D-08] reBAP und AEP-Module (netztransparenz.de), Daten bis 10.09.2026 (A).
- [M1] Begleitmodell M1: Läufe 20260927-kapitel02 (Version 1.1.0), 20260927-standalone und 20260927-intraday (Version 1.0.0) (27.09.2026), 20260928-standalone und 20260928-intraday mit Regelreserve (Version 2.0.0, FCR-Faktor 1,25; 28.09.2026); eigene Berechnung.
- ANNAHMEN A-001, A-002, A-020, A-021, Modellannahmen A-M1-01, -02, -05, -08, -12, -16; A-055 (Wirkungsgrad GuD); Buchkonvention „nutzbar“ nach Entscheidung D-021 (Stand 27.09.2026).

**Stand:** 27.09.2026; Marktdaten bis Liefertag 26.09.2026, reBAP und AEP-Module bis 10.09.2026. Beweglich sind die Preisgrenzen der Day-Ahead- und Intraday-Kopplung (Untergrenze −600 €/MWh seit Handelstag 28.05.2026, Anpassungsregel), die Preisgrenzen der Regelarbeitsplattformen, die grenzüberschreitende Gate-Closure (Umstellung auf 30 Minuten bis 2028), die Intraday-Auktionen, die reBAP-Methodik, der Kapazitätsmarkt nach StromVKG (Kapitel 3) und die Gebotszonendebatte; diese Punkte sind vor Verwendung zu prüfen. Mit „Suchauszug“ gekennzeichnete Belege stehen auf der Verifikationsliste der Faktenprüfung.
