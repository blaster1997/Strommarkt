---
title: "Kapitel 15 · Erweiterte Erlösstapel: PV, PPA, Tolling und weitere Segmente"
subtitle: "Ökonomie von Batteriespeichern in Deutschland"
date: "04.10.2026"
kopfzeile-rechts: "Kapitel 15 · Stand 28.09.2026"
kapitel-start: 15
nummerierung: kapitelweise
inhaltsverzeichnis: true
toc-tiefe: 2
deckblatt-hinweis: "Keine Rechts-, Steuer- oder Anlageberatung. Datenstand 27.09.2026; MiSpeL nach der Festlegung vom 01.10.2026."
---

# Erweiterte Erlösstapel: PV, PPA, Tolling und weitere Segmente

> [!NOTE]
> **Lernziele:** Nach diesem Kapitel können Sie
>
> - Erlössegmente eines Speichers nach Vertragsart (kontrahiert oder merchant, physisch oder finanziell), Steuerungsrecht und Risikoallokation klassifizieren;
> - die Wirkung eines PV-PPA, Hybrid-PPA oder Tolls auf Eigentümerwert, Opportunitätskosten und Indifferenzpreis mit Modellergebnissen berechnen;
> - den Status weiterer Segmente (Momentanreserve, § 13k und § 14c EnWG, Kapazitätsmarkt) für einen Standort beurteilen;
> - eine Erlösstrategie aus Merchant, Toll, PPA und Systemdienstleistungen für R2 und R3 entwerfen und nach Finanzierbarkeit bewerten.

## Warum das für Investor und Fonds zählt {.unnumbered}

Ein Standalone-Speicher verdient an Märkten; kommen Photovoltaik (PV), ein Stromliefervertrag (Power Purchase Agreement, PPA) oder ein Toll hinzu, also die Vermietung der Speicherkapazität gegen feste Zahlung (Kapitel 5), bestimmen Verträge mit, wer welchen Wert erhält. Im Modell M1 bringt dieselbe Anlage R3 (15 MWp PV, Speicher 10 MW/20 MWh nutzbar) ihrem Eigentümer 2025 bei perfekter Voraussicht und angenommenen Vertragspreisen zwischen 0,70 Mio. €/a (Hybrid-PPA, bei dem der Abnehmer den Speicher im Day-Ahead-Markt steuert) und 3,41 Mio. €/a (merchant als Mischspeicher, der aus PV und Netz lädt), brutto vor Vermarktungsentgelt [M1, Lauf 20260928-stacking]. Solche Verträge werden häufiger, laut Fachmedium zum Teil getrieben von Co-Location; Tolls überwiegen (Volumina in Kapitel 5) [K05M-06]. Verträge glätten Erlöse und heben den möglichen Fremdkapitalanteil (Gearing), binden aber Leistung, Energie und Netzanschluss; wer die Einzelerlöse addiert, überschätzt den Wert. Die Vertragsstruktur entscheidet damit über Erlösniveau, Finanzierbarkeit und Kontrahentenrisiko eines Fondsprojekts.

**Cashflow-Kompass:** Erlöse ● (PV-Erlös, PPA-Festpreis, Toll-Zahlung, Erlös der Merchant-Tranche, Systemdienstleistungen) · Betriebskosten ○ (Fehlmengen, Ausgleichsenergie, Vermarktungsentgelt) · Investitionen ○ (netzbildender Umrichter, Messkonzept) · Steuern ○ (Einordnung von PPA- und Toll-Zahlungen, Kapitel 17) · Finanzierung ● (kontrahierter Anteil, DSCR, Gearing) · Fondsebene ● (Kontrahenten, Bewertung langfristiger Verträge im NAV). **Werttreiber:** Erlösniveau, Opportunitätskosten, Erlösrisiko.

## Stacking-Logik und Taxonomie

Ein Erlösstapel (Value-Stacking) kombiniert mehrere Erlösquellen auf derselben Anlage. Schon Day-Ahead-Handel und Regelreserve konkurrieren um Leistung und Ladezustand (Kapitel 4). Mit PV, Verträgen und neuen Systemdienstleistungen kommen weitere knappe Größen hinzu: die Einspeise- und Bezugsleistung am gemeinsamen Netzverknüpfungspunkt (NVP), die Herkunft des geladenen Stroms und das Recht, über den Einsatz zu entscheiden. Formal ist der Wert eines Stapels das Optimum über alle Segmente zugleich; er liegt nie über der Summe der einzeln optimierten Erlöse:

$$W^{\text{Stapel}} = \max_{x \in X_1 \cap \dots \cap X_n} \sum_{s=1}^{n} R_s(x) \;\le\; \sum_{s=1}^{n} \max_{x \in X_s} R_s(x)$$

$x$ ist der Einsatzplan (Laden, Entladen, Regelleistung, PV-Einspeisung je Zeitschritt), $X_s$ die Menge der Pläne, die Segment $s$ zulässt, und $R_s(x)$ der Erlös des Segments in €/a. Die Differenz beider Seiten sind die Opportunitätskosten des Stapels. Verträge ändern zusätzlich, wem die Erlöse zufließen: Ein Festpreis ersetzt den Marktwert einer Menge, ein Toll die Markterlöse eines Teils der Leistung.

Den Abstand zeigt ein Überschlag mit M1 (2025, perfekte Voraussicht, eigene Rechnung). Die PV von R3 allein (776 k€/a nur Day-Ahead, mit Abregelung bei negativen Preisen) und ein Speicher wie R1 mit eigenem 10-MW-Anschluss (2.976 k€/a mit FCR und aFRR) erzielen getrennt zusammen 3.752 k€/a. Als Mischspeicher am gemeinsamen Anschluss erzielt R3 3.412 k€/a, rund 9 % weniger [M1, Läufe 20260928-stacking und 20260927-fcr125]. Der Abstand entsteht, weil PV und Speicher sich 12 MW Einspeisung teilen und der Speicher nur 5 MW aus dem Netz beziehen darf (A-054); Kapitel 14 vergleicht die Konfigurationen einschließlich der Anschlusskosten.

Vier Merkmale ordnen die Segmente. Erstens: kontrahiert oder merchant, also ob ein Vertrag oder der Markt den Preis bestimmt. Zweitens: physisch oder finanziell. Physisch liefert der Eigentümer Energie in den Bilanzkreis des Käufers oder überlässt ihm die Steuerung; finanziell verkauft er selbst am Markt, und die Parteien gleichen nur die Differenz zum Festpreis aus (virtuelles PPA, finanzieller Toll; Kapitel 5). Drittens: wer den Speicher disponiert; davon hängen die Opportunitätskosten ab. Viertens: wer Preis-, Mengen- und Profilrisiko trägt, also das Risiko, dass Preise, Erzeugung oder Einsatz vom Plan abweichen (Tabelle 15.1; PPA-Formen in Abschnitt 15.3).

| Segment | Vertragsart; Abwicklung | Disponiert | Preisrisiko | Mengen- und Profilrisiko | Beleg Deutschland |
|---|---|---|---|---|---|
| Merchant (Day-Ahead, Intraday, Regelreserve) | merchant; physisch | Eigentümer bzw. Optimierer | Eigentümer | Eigentümer | Kapitel 2–5 |
| PV-PPA pay-as-produced | kontrahiert (nur PV); physisch oder finanziell | Eigentümer, Speicher frei | Abnehmer | Abnehmer nimmt jede erzeugte MWh; Wetter beim Eigentümer | Brüssow, Form nicht genannt [VR3-07] |
| Band- oder Profil-PPA | kontrahiert; physisch oder finanziell | Eigentümer | Abnehmer (Bandmenge) | Eigentümer (Fehlmengen) | kein Beispiel mit Speicher belegt |
| Pay-as-nominated | kontrahiert; physisch nach Tagesprognose | Eigentümer | Abnehmer | Eigentümer (Prognose, Ausgleichsenergie) | DB Energie [VR3-08] |
| Hybrid-PPA mit Abnehmer-Dispatch | kontrahiert; physisch | Abnehmer | Abnehmer | Abnehmer (Profil) | Salzgitter [VR3-06] |
| Toll, Teil-Toll | kontrahiert; physisch, virtuell oder finanziell | Toller (finanziell: Eigentümer) | Toller | Eigentümer (Verfügbarkeit) | Brüssow, Speicher [VR3-07]; Kapitel 5 |
| Floor | teilweise kontrahiert (Put-Option); finanziell | Optimierer | unter dem Floor beim Garanten | Eigentümer | Kapitel 5 |
| Momentanreserve | reguliert, Festpreis; Vorhaltung | Eigentümer hält Leistung frei | fest für die Vertragslaufzeit | Eigentümer (Verfügbarkeit) | [K03M-06, K03M-29, K03M-40] |
| Kapazitätsmarkt | reguliert, Gebotswert; Zuverlässigkeitsoption | Eigentümer mit Verfügbarkeitspflicht | Spitzen über dem Ausübungspreis abgegeben | Eigentümer | Kapitel 3 [K03R-01] |

Table: Taxonomie der Erlössegmente

Quelle: VR3-06 bis VR3-08, K03M-06, K03M-29, K03M-40, K03R-01; Kapitel 3 und 5; eigene Einordnung (Stand 28.09.2026).

Daraus folgt zweierlei (Einordnung). Erstens fallen Kontrahierung und Steuerungsrecht auseinander: Beim finanziellen Toll ist der Preis gesichert, die Steuerung bleibt beim Eigentümer; beim Hybrid-PPA mit Abnehmer-Dispatch gibt er beides ab. Zweitens sagt „kontrahiert“ wenig über das Restrisiko: Ein PV-PPA sichert den Preis der PV-Menge, nicht den Speicher; ein Band-PPA sichert den Preis einer Menge, die der Eigentümer bei Fehlmengen zu Marktpreisen nachkauft.

## PV-Co-Location: Aufwertung des PV-Marktwerts und wem sie zusteht

Ein PV-Kraftwerk speist ein, wenn alle PV-Anlagen einspeisen, und erzielt deshalb weniger als den Durchschnittspreis. Der Jahresmarktwert Solar (JW Solar), der mit der Solareinspeisung gewichtete Preis (Kapitel 2), lag 2025 bei 45,08 €/MWh [K15M-01], das Mittel der Day-Ahead-Preise bei 89,32 €/MWh [M1D-01; VR3-29]. Der Wertfaktor (Capture-Rate) betrug damit 0,505 (2024: 0,59, je nach Bezugsmittel auch 0,58 [M1D-01, VR3-29; Kapitel 2]), für Wind an Land 2025 0,833 (eigene Rechnung aus [K15M-01, M1D-01]). Ein Speicher, der PV-Strom in teure Stunden verschiebt, hebt den Wert je erzeugter MWh. Diese Aufwertung (Capture-Uplift) misst

$$U = \frac{w^{\text{PV+S}} - w^{\text{PV}}}{w^{\text{PV}}}$$

mit $w^{\text{PV}}$ als Wert je MWh PV-Erzeugung ohne Speicher und $w^{\text{PV+S}}$ als Wert mit Speicher, beide in €/MWh erzeugter PV-Energie, nach Degradationskosten. M1 rechnet für R3 mit einem Grünstromspeicher, der nur PV-Strom lädt (Konfiguration A, Kapitel 14), nur Day-Ahead, bei perfekter Voraussicht und für 2025 sowie die 12 Monate bis 26.09.2026 (kurz 2025/26). PV allein erzielt 49,2 bzw. 61,6 €/MWh, weil sie bei negativen Preisen abregelt; ohne Abregelung wären es 45,95 bzw. 57,54 €/MWh. Mit 20 MWh steigt der Wert auf 89,4 bzw. 111,6 €/MWh (+82 bzw. +81 %), mit 55 MWh auf 120,1 bzw. 151,3 €/MWh (+144 bzw. +146 %); darüber flacht die Kurve ab, 80 MWh bringen +153 bzw. +155 % (Abbildung 15.1) [M1, Lauf 20260928-stacking].

Das Fenster 2025/26 (27.09.2025–26.09.2026) rechnet M1 ohne Hochrechnung (A-M1-33, D-027); die PV-Menge ist in beiden Zeiträumen auf 15.750 MWh skaliert (A-M1-31), und das Fenster überschneidet sich mit 2025 um gut drei Monate. Die lineare Hochrechnung des Teiljahrs 01.01.–26.09.2026 (A-M1-12) würde PV-bezogene Beträge überzeichnen: Es enthält den sonnenreichen Teil des Jahres, hochgerechnet ergäben sich 19.351 statt 15.750 MWh PV (+23 %). Für R2 ohne PV bleibt es bei dieser Hochrechnung (kurz 2026*).

![Wert je MWh PV-Erzeugung mit einem Grünstromspeicher wachsender Größe (15 MWp PV, 10 MW Speicher, 0–80 MWh nutzbar), nur Day-Ahead, perfekte Voraussicht, 2025 und 2025/26](05_figures/K15/15_capture_uplift.png)

Quelle: eigene Berechnung, Modell M1 Version 2.0.0 (Lauf 20260928-stacking; 2025/26 ohne Hochrechnung, A-M1-33); Daten: energy-charts/SMARD [M1D-01, M1D-04]; Parameter A-001, A-002, A-011, A-021 (Stand 28.09.2026).

Drei Vereinfachungen machen die Werte zur Obergrenze: M1 kennt alle Preise im Voraus, rechnet ohne Regelreserve und Förderung und ordnet den ganzen Speicherwert der PV zu (N16, Abschnitt 15.6). Die Größenordnung passt zu LevelTen, wonach ein Speicher die Capture-Werte einer deutschen PV-Anlage „um bis zu 80 %“ erhöhen kann [VR3-04]. Ein Überschlag der Recherche, der alle PV-Energie mit 87 % Wirkungsgrad zum 0,91-Fachen des Mittelpreises absetzt, ergibt rund +57 % (Schätzung, K15-Notiz); M1 liegt darüber, weil der Speicher mit Voraussicht in die teuersten Stunden verkauft: Die Einspeisung von R3 mit 20 MWh erzielt 2025 das 1,24-Fache des Mittelpreises [M1, Lauf 20260928-stacking].

**Wem die Aufwertung zusteht.** Keine öffentliche Quelle beziffert, wie sie zwischen PV-Betreiber, Speicherbetreiber und Abnehmer geteilt wird [LÜCKE: Aufteilung des Capture-Uplifts in deutschen Hybrid- und Co-Location-Verträgen]. Die Aufteilung folgt der Vertragsstruktur (Einordnung nach den Fallbeispielen in Abschnitt 15.3): Steuert der Abnehmer den Speicher, erhält er die Aufwertung und vergütet den Erzeuger über einen Preis; bei pay-as-nominated steckt sie im Hybridpreis, das Ausgleichsrisiko trägt der Erzeuger; im entbündelten Modell erhält der PPA-Käufer das PV-Profil, der Toller die Speicherarbitrage und der Eigentümer die Toll-Zahlung. Bei Merchant-Vermarktung behält der Eigentümer die Aufwertung samt Risiko.

Welcher Anteil beim Eigentümer ankommt, misst

$$\sigma^{\text{Eig}} = \frac{w^{\text{Eig}} - w^{\text{PV}}}{w^{\text{PV+S}} - w^{\text{PV}}}$$

mit $w^{\text{Eig}}$ als Erlös des Eigentümers je erzeugter MWh nach Vertrag. Bei $\sigma^{\text{Eig}} = 1$ behält er die ganze Aufwertung, bei $\sigma^{\text{Eig}} \le 0$ gibt er sie ganz ab. LevelTen sieht Hybrid-Angebote in Europa 24 % über Solar-PPAs (Q2 2026) [VR3-04]; auf den PV-PPA-Anker von 45 €/MWh gelegt, zahlt der Abnehmer 56 €/MWh (A-M1-28). Gilt dieser Preis je eingespeister MWh, erhält der Eigentümer von R3 mit 20 MWh 2025 (nur Day-Ahead, perfekt) für 12.820 MWh Einspeisung nach Degradationskosten 704,7 k€/a, je erzeugter MWh (15.750 MWh) also 44,7 €/MWh, weniger als PV allein (49,2 €/MWh); $\sigma^{\text{Eig}}$ liegt bei −0,11 [M1, Lauf 20260928-stacking; eigene Rechnung].

Unter diesen Annahmen geht die ganze Aufwertung an den Abnehmer, aus zwei Gründen: Der Aufschlag von 24 % gleicht nur aus, dass Abregelung und Speicherverluste die Menge um knapp ein Fünftel mindern (1,24 × 0,814 ≈ 1,01), und der Anker von 45 €/MWh liegt schon unter dem Merchant-Wert der PV von 49,2 €/MWh. Mit LevelTens Absolutwert für Hybride (rund 70,8 €/MWh, Abschnitt 15.3) erhielte der Eigentümer knapp ein Fünftel der Aufwertung ($\sigma^{\text{Eig}} \approx 0{,}19$; eigene Rechnung, weitere Preise in Übung 15.3). Ob deutsche Verträge so rechnen, ist offen; Preise nennt keiner.

## PPAs mit Speicherbezug: Formen und Fallbeispiele 2026

Ein PPA ist ein langfristiger Stromliefervertrag, physisch oder finanziell (virtuelles PPA, Abschnitt 15.1). Für PV mit Speicher unterscheiden sich die Formen darin, welche Menge der Festpreis erfasst. Beim **pay-as-produced** kauft der Abnehmer jede erzeugte MWh; der Speicher bleibt außerhalb des Vertrags. Beim **Band- oder Profil-PPA** liefert der Erzeuger eine feste Menge je Stunde oder ein vereinbartes Profil und kauft Fehlmengen nach; der Speicher formt die PV-Erzeugung zum Profil. Beim **pay-as-nominated** liefert er, was er am Vortag nach seiner Prognose nominiert hat, Abweichungen werden als Ausgleichsenergie abgerechnet (Kapitel 2); der Speicher gleicht sie aus. Ein **Hybrid-PPA** umfasst PV und Speicher in einem Vertrag, oft mit Profil- oder Grünstromvorgaben, im Extremfall steuert der Abnehmer den Speicher selbst. LevelTen beobachtet „Green BESS“-Verträge, bei denen der Speicher nur aus der verbundenen Anlage lädt; in Deutschland und Spanien waren Hybride im zweiten Quartal 2026 der häufigste Angebotstyp [VR3-04].

Drei deutsche Verträge aus 2026 zeigen die Bandbreite (Tabelle 15.2). Alle Angaben stammen aus Fachmedien (Qualität C); der „größte Hybrid-Deal“ in Deutschland und die erste Vermarktung einer förderfreien Anlagenkombination sind Selbstangaben der Unternehmen, Preise nennt keiner [VR3-06 bis VR3-08].

| Ankündigung | Projekt | PV; Speicher (h) | Speicher je PV | Struktur | Speicher disponiert | Laufzeit | Quelle |
|---|---|---|---|---|---|---|---|
| 06.07.2026 | Brüssow (BB), Enertrag | 44,5 MW; 5 MW/10 MWh (2,0) | 0,11 MW/MW | entbündelt: PV-PPA mit EDF Trading, Toll mit e2m; Speicher fünf Jahre grün, dann zwei Jahre grau; NVP geteilt mit 33 MW Wind und rund 20 MW Speicher | Toller | je 7 J. | VR3-07 |
| 06.08.2026 | Klein Belitz (MV), MaxSolar – DB Energie | 37 MWp; 15 MW/30 MWh (2,0) | 0,41 MW/MWp | pay-as-nominated nach Tagesprognose; förderfrei; rund 36.680 MWh/a | Erzeuger | 10 J.; Betrieb ab Sommer 2027 | VR3-08 |
| 16.09.2026 | zwei Standorte (BB, TH), Zelestra – Salzgitter Flachstahl | 147 MW (Einheit laut Artikel); 79 MW/237 MWh (3,0) | 0,54 MW/MW | Hybrid-PPA; Laden nur aus PV-Überschuss; 158 GWh/a | Abnehmer | n. a. | VR3-06 |

Table: Hybrid- und Co-Location-Verträge in Deutschland 2026

Quelle: VR3-06 bis VR3-08 (Fachmedien, Volltext); Speicher je PV und Speicherdauer eigene Rechnung; n. a. = nicht angegeben (Stand 27.09.2026).

> [!STAND]
> **Stand der PPA-Preise:** Deutsche PPA-Preise nach Struktur sind öffentlich nicht verfügbar [LÜCKE: deutsche PPA-Preise für pay-as-produced, Band und Hybrid; Abonnements von Pexapark, LevelTen oder Zeigo oder Indikationen von Abnehmern]. Belegt sind europäische Aggregate: der Pexapark-Index „Euro Composite“ mit 45 €/MWh im Juli 2026 [VR3-01, Qualität C] und LevelTens Angebotspreise für Hybrid-PPAs 24 % über Solar- und 15 % unter Wind-PPAs (Q2 2026) [VR3-04]. Ein Fachmedium nennt LevelTens Absolutwerte: Solar 56,59 €/MWh, Hybrid 81,68 US-\$/MWh, zum EZB-Kurs vom 08.06.2026 (1,1540 US-\$/€, ein Tag im Angebotsquartal) rund 70,8 €/MWh [VR3-03, Qualität C; SYN-01]. Seine Solar-Angabe von 74,85 US-\$/MWh unterstellt 1,32 US-\$/€, einen Kurs, der zu keinem EZB-Kurs 2026 passt; mit dem EZB-Kurs liegt Hybrid wie bei LevelTen (+24 %) 25 % über Solar, mit dem Kurs des Artikels nur 9 % (eigene Rechnung). Der Abstand zu Pexapark folgt aus Methode (Index aus Marktaktivität gegenüber Angebotspreisen einer Plattform), Technologiemix und Zeitpunkt (Einschätzung). Pexapark wies laut Fachmedium im November 2025 seit August 2025 keine handelbare Preisspanne für deutsche Solar-PPAs aus [VR3-02, 04.11.2025]; ein neuerer Stand ist nicht belegt. M1 rechnet deshalb mit Annahmen: PV-PPA 45 €/MWh, Sensitivität 40 und 55 (A-M1-27), Hybrid-PPA 56 €/MWh (A-M1-28), Band zum Marktwert minus 10 % (A-M1-29). Vor Verwendung durch Indikationen ersetzen.

M1 zerlegt den Wert eines Vertrags für den Eigentümer in drei Teile:

$$W^{\text{Eig}} = \underbrace{\sum_t \Delta_t\,\lambda_t\,g_t + R^{\text{RR}} - K^{\text{Deg}}}_{\text{Marktwert des Fahrplans}} + \underbrace{\sum_t \Delta_t\,(\bar{p} - \lambda_t)\,q_t}_{\text{Festpreiskomponente}} - \underbrace{\delta \sum_t \Delta_t\,m_t}_{\text{Fehlmengenaufschlag}}$$

$g_t$ ist die Nettoeinspeisung am NVP in MW im Zeitschritt $t$ der Dauer $\Delta_t$ in h, $\lambda_t$ der Day-Ahead-Preis in €/MWh, $R^{\text{RR}}$ der Erlös aus Regelleistung und $K^{\text{Deg}}$ die Degradationskosten in €/a, $\bar{p}$ der Vertragspreis in €/MWh und $q_t$ die Vertragsmenge in MW, $m_t$ die Fehlmenge in MW, die der Eigentümer zum Marktpreis zuzüglich des Aufschlags $\delta$ in €/MWh nachkauft. Die **Dispatchwirkung** ist der Marktwert des Fahrplans mit Vertrag minus dem ohne Vertrag; ist sie negativ, sind das die Opportunitätskosten des Vertrags. Den Preis, bei dem der Eigentümer mit Vertrag genauso dasteht wie merchant, nennt das Buch **Indifferenzpreis**:

$$\bar{p}^{*} = \bar{p} + \frac{W^{M} - W^{\text{Eig}}(\bar{p})}{Q}$$

mit $W^{M}$ als Eigentümerwert merchant in €/a und $Q = \sum_t \Delta_t\, q_t$ als Vertragsmenge in MWh/a; die Formel gilt näherungsweise, weil der Fahrplan kaum vom Preis abhängt. Liegt ein Angebot unter $\bar{p}^{*}$, zahlt der Eigentümer für die Absicherung.

Abbildung 15.2 und Rechenbeispiel 15.1 zeigen die Ergebnisse für R3 mit 20 MWh. Die Varianten haben verschiedene Referenzen: Der PV-PPA wird am merchant vermarkteten Mischspeicher (C) gemessen; die Hybrid-PPAs rechnet M1 wie den Salzgitter-Vertrag mit Grünstrombindung (A-M1-28, A-M1-29) und misst sie am Grünstromspeicher (A), der bei perfekter Voraussicht schon merchant 516 k€/a (2025) bzw. 412 k€/a (2025/26) weniger erzielt als C [M1, Lauf 20260928-stacking]. Das ist die operative Differenz mit ungeförderter PV, vor Anschluss- und Messkosten; Kapitel 14 rechnet mit geförderter PV und nach diesen Kosten und kommt für 2025 auf 463 k€/a.

![Eigentümerwert von R3 (20 MWh) merchant, mit PV-PPA, entbündeltem Toll und Hybrid-PPA, 2025 und 2025/26; Balken perfekte Voraussicht (Abnehmer-Dispatch nur Day-Ahead), Rauten merchant realistisch](05_figures/K15/15_ppa_varianten.png)

Quelle: eigene Berechnung, Modell M1 Version 2.0.0 (Lauf 20260928-stacking; 2025/26 ohne Hochrechnung, A-M1-33); Daten: energy-charts/SMARD [M1D-01, M1D-04], regelleistung.net [M1D-02, M1D-03]; PPA-Preise als Annahmen A-M1-27 bis A-M1-29 (Anker [K15M-01, VR3-01, VR3-04]), Toll-Preis A-038 (Stand 28.09.2026).

Ob ein PPA in Viertelstunden mit negativem Preis zahlt, ist Verhandlungssache; eine Marktpraxis ist nicht belegt (K15-Notiz, N6). Für neue PV-Anlagen entfällt dort ohnehin die Marktprämie (§ 51 EEG, Kapitel 12) [W2V-01]. Ohne Negativpreisklausel bleibt jede erzeugte MWh den Vertragspreis wert, und M1 regelt weniger ab. Mit Klausel steigt der Indifferenzpreis stark, weil die verbleibende Vertragsmenge in teureren Stunden liegt (Rechenbeispiel 15.1).

> [!IMPORTANT]
> **Hier Fachleute einbinden:** PPA- und Toll-Vertrag. Rechtsanwalt für Energierecht und Direktvermarkter zu Mengendefinition (PV-Zähler oder NVP, erzeugte oder eingespeiste Menge), Negativpreis- und Abregelungsklauseln, Fehlmengen- und Ausgleichsenergieregeln, Nominierungspflichten bei pay-as-nominated, Vorrang am NVP gegenüber einem Toll, Grünstrombindung und ihrer Dauer, Herkunftsnachweisen, Preisanpassung bei Gesetzesänderung (etwa EEG 2027, Kapitel 12), Sicherheiten und Kündigung bei Kontrollwechsel, im Toll-Vertrag zur Weiterreichung von Preisspitzenausgleich und Verfügbarkeitspflichten eines Kapazitätsvertrags und zu den Leistungsbändern der Momentanreserve (Abschnitt 15.5). Rechtsanwalt für Kapitalmarktrecht zur Frage, ob ein finanzielles PPA Melde- und Handelspflichten auslöst (EMIR, MiFID II, REMIT; Kapitel 5).

## Tolls, Floors und virtuelle Tolls in Kombination mit PV und PPA

Kapitel 5 erklärt Toll, Floor und virtuellen Toll am Standalone-Speicher. Mit PV kommen drei Fragen hinzu: wer den gemeinsamen NVP zuerst nutzt, ob für den Toller eine Grünstrombindung gilt und wie Erlöse von PV und Speicher abgegrenzt werden.

**Entbündelt.** Im Brüssow-Modell verkauft der Eigentümer die PV-Erzeugung per PPA und vermietet den Speicher per Toll [VR3-07]. M1 bildet das mit einem PV-PPA zu 45 €/MWh und einem Toll über die volle Leistung ab: 105 k€/MW/a bei 20 MWh (Anker für 2 h, A-038) und 177,1 k€/MW/a bei 55 MWh (unbelegte Hochrechnung, A-M2-15). Der Eigentümer erhält 1.752 bzw. 2.459 k€/a (2025) und 1.748 bzw. 2.451 k€/a (2025/26); der Betrag hängt an PV-Menge, PPA-Preis und Toll-Zahlung, kaum an Marktpreisen und Voraussicht. Merchant erzielt der Mischspeicher (20 bzw. 55 MWh, Bezug 5 bzw. 10 MW, A-054) bei realistischer Voraussicht 2.489 bzw. 2.784 k€/a (2025) und 2.458 bzw. 2.891 k€/a (2025/26) [M1, Lauf 20260928-stacking]. Die Differenz ist der Preis der Sicherheit: brutto rund 320–740 k€/a (2025) bzw. 440–710 k€/a (2025/26), nach 6 % Vermarktungsentgelt auf den Speichererlös (C abzüglich PV allein; A-015), das bei der Toll-Zahlung entfällt (A-M2-42), rund 200–630 bzw. 320–620 k€/a (eigene Rechnung, Einschätzung). Ob sich die Sicherheit lohnt, zeigt erst eine Bewertung über die Laufzeit (Kapitel 5 und 18).

**NVP-Vorrang und Grünstrombindung.** Teilen PV-PPA und Toll einen NVP, konkurrieren PV-Einspeisung und Speicherentladung in sonnigen Stunden um die Einspeiseleistung (N1). Wer Vorrang hat, regelt der Vertrag; für Brüssow ist das nicht veröffentlicht [VR3-07]. Muss der Toller grün laden, verliert er Netzarbitrage und negative Regelleistung aus Netzbezug. In M1 kostet die Grünstrombindung den merchant vermarkteten Speicher von R3 bei realistischer Voraussicht 346 k€/a im Jahr 2025 (C 2.489 gegenüber A 2.143 k€/a) und 272 k€/a 2025/26 (operativ, PV ungefördert; nach Anschluss- und Messkosten mit geförderter PV 2025 rund 295 k€/a, Kapitel 14) [M1, Lauf 20260928-stacking; eigene Rechnung]. Ein Toll für einen Grünstromspeicher sollte deshalb deutlich unter dem für einen Mischspeicher liegen (Einschätzung). Der Wechsel in Brüssow erlaubt Netzladung in den letzten zwei Toll-Jahren; warum nach fünf Jahren gewechselt wird, nennt die Quelle nicht [LÜCKE: Grund für den Wechsel von Grün- auf Graustrom im Brüssow-Vertrag].

**Bilanzkreis.** Mit Marktprämie über die Abgrenzungsoption verlangt die MiSpeL-Festlegung vom 01.10.2026, die gesamte Einspeisung an der Einspeisestelle „in einem“ gesonderten Bilanz- oder Unterbilanzkreis zu bilanzieren (Voraussetzung 4) [K12R-18, Abschn. 3.1.1 Nr. 4, S. 21; K12R-17, S. 25]; PV-PPA und Toll bei verschiedenen Händlern passen dazu schwer (Einschätzung, Kapitel 12). M1 rechnet die PPA-Fälle deshalb mit ungeförderter PV (A-M1-26).

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Entbündelte Verträge am gemeinsamen NVP. Rechtsanwalt für Energierecht und Direktvermarkter klären vor Vertragsschluss neben der Bilanzkreispflicht der MiSpeL (Kasten in Abschnitt 12.4), wer Ausgleichsenergie aus PV-Prognosefehlern und Speicherabweichungen trägt, wie Einspeisebegrenzungen am NVP auf PPA-Menge und Toll-Verfügbarkeit angerechnet werden und was ein Wechsel von grün auf grau für Förderung und Umlagen bedeutet (Kapitel 12).

**Floor und finanzieller Toll.** Ein Floor wirkt nur auf die Auszahlung, nicht auf den Einsatz (N10; Kapitel 5); bei Co-Location muss der Vertrag aber festlegen, welcher Erlös gegen ihn zählt: der des Speichers allein, was eine Zuordnung der PV-Energie im Speicher verlangt (N16), oder der des Gesamtsystems (Einschätzung). Beim finanziellen Toll bleibt die Steuerung beim Eigentümer [K05M-08]; das erleichtert die gemeinsame Optimierung mit der PV am NVP, lässt aber ein Basisrisiko zwischen tatsächlichem Erlös und der Referenz des Ausgleichs, dessen Bemessung die geprüften Quellen nicht beschreiben (Einschätzung; Kapitel 5).

## Weitere Segmente mit Status-Ampel

Tabelle 15.3 fasst den Stand von Segmenten, die neu, regional oder noch ohne Markt sind, für die Referenzfälle zusammen; die Mechanik von Momentanreserve und Kapazitätsmarkt erklärt Kapitel 3. Die Ampel bewertet den Zugang: grün heißt in Kraft und zugänglich, gelb zugänglich mit offenen Bedingungen oder erst später, rot für die Referenzfälle ausgeschlossen oder ohne Markt, grau nicht bewertet. Kein Segment erreicht für R1–R3 grün.

| Segment | Stand | Vergütung | Zugang R1–R3 | Ampel | Quelle |
|---|---|---|---|---|---|
| Momentanreserve (§ 12h EnWG) | marktgestützte Beschaffung seit 22.01.2026 | Festpreis, bei Angebot für die Vertragslaufzeit gesichert; Premium bis 888,50, Basis bis 109,50 €/MWs/a, verfügbarkeitsabhängig | nur mit netzbildendem Umrichter; in der Mittelspannung mit Zustimmung des Netzbetreibers | gelb | K03M-06, K03M-29, K03M-40 |
| „Nutzen statt Abregeln“ (§ 13k EnWG) | Zielmodell ab 01.10.2026 | Erstattung je zugeteilter und verbrauchter MWh; Höhe nicht ausgewertet | keine Entlastungsregion bei TransnetBW und Amprion; Speicher als Entlastungsanlage offen | rot (R1–R3); gelb im Norden | VR3-32, W2V-07 |
| Lokale Flexibilitätsmärkte (§ 14c EnWG) | Pflicht ausgesetzt bis zur ersten Genehmigung oder Festlegung von Spezifikationen durch die BNetzA (§ 118 Abs. 28 EnWG); keine bekannt | kein Markt belegt | – | rot | SYN-17 |
| Kapazitätsmarkt (StromVKG) | in Kraft; Termine 18.05.2027, 01.12.2027, 01.10.2029; Lieferung ab 01.11.2031 | Gebotswert je MW reduzierter Leistung; Preisspitzenausgleich | Erzeugungskapazitäten (18.05.2027) für R1/R2 praktisch nicht zugänglich, Kapazitäten ab 01.12.2027; Reduktionsfaktoren offen; Basisfall null (A-040) | gelb | K03R-01 |
| Behind-the-Meter | nicht recherchiert | – | für 10-MW-Fondsprojekte Nische (Einschätzung) | grau | – |
| Wind-Co-Location | NVP-Teilung belegt; Innovationsausschreibung offen für Wind (entfällt nach Entwurf EEG 2027) | Wertfaktor Wind an Land 2025: 0,833 | nicht modelliert | grau | VR3-07, VR3-23, K15M-01 |

Table: Weitere Segmente: Status-Ampel für die Referenzfälle

Quelle: wie angegeben; Kapitel 3 und 12; K15-Notiz; Ampel eigene Einordnung (Stand 28.09.2026).

**Momentanreserve.** Drei Punkte der Vergütung werden leicht falsch gelesen. Erstens gilt der Festpreis nicht nur bis 21.01.2028: Wer bis dahin anbietet, sichert die Preise der ersten Periode ohne Indexierung für die gewählte Erbringungsdauer von 24 bis 120 Monaten, bei 0 bis 35 Monaten Vorlauf. Die Übertragungsnetzbetreiber (ÜNB) können die Preise mit Zustimmung der Bundesnetzagentur auch vor Periodenende ändern, wenn der Bedarf einer Region gedeckt ist, bis auf null, aber nur für danach eingereichte Angebote; für die erste Periode erwarten sie das nicht [K03M-29, Nr. 1.1, 1.5, 1.6, 6.2]. Nötig sind eine Netzanschlusszusage und ein Einheitenzertifikat, ein Typzertifikat nach einem Hinweis des Forums Netztechnik/Netzbetrieb im VDE (FNN), das die Momentanreserve-Eigenschaften der Einheit belegt [K03M-29, Nr. 3.2, 9.2, 10.2]. Kann die Einheit bis zum Ende des Vorlaufs nicht liefern, verfällt das Angebot; ein neues gilt zu den dann gültigen Preisen [K03M-29, Nr. 3.7]. Für R1 oder R2 mit netzbildendem Umrichter (Inbetriebnahme 01.07.2027) ist das Angebotsfenster eine befristete Option auf einen kontrahierten Festpreisbaustein für bis zu zehn Jahre (Einschätzung).

Zweitens sind 888,50 und 109,50 €/MWs/a Höchstwerte: Premium zahlt 805 €/MWs/a zuzüglich eines verfügbarkeitsabhängigen Teils bis 83,50 (voll erst bei 100 % Verfügbarkeit), Basis 76 zuzüglich bis 33,50 €/MWs/a (voll ab 90 %). Unter 90 % (Premium) bzw. 30 % (Basis) Verfügbarkeit entfällt die Vergütung für den ganzen Abrechnungszeitraum, in der Regel ein Kalenderjahr: eine Klippe statt einer Vertragsstrafe [K03M-29, Nr. 1.4, 1.7; K03M-40, Abschn. 4.2]. Was die technischen Anschlussregeln (TAR) des Netzbetreibers ohnehin verlangen, wird nicht vergütet, soweit sie eine Anlaufzeitkonstante vorschreiben: Diese wird abgezogen; eine geforderte Fähigkeit ohne Anlaufzeitkonstante mindert die Vergütung nicht [K03M-29, Nr. 10.5]. Schreiben die TAR künftig Anlaufzeitkonstanten vor, schrumpft die vergütete Menge (Einschätzung). Am Höchstspannungsnetz verlangen die ÜNB seit 16.12.2024 netzbildende Eigenschaften [K07O-01], am Hochspannungsnetz sieht ein Normentwurf sie vor [K07O-02]; ab 110 kV wird Netzbildung damit absehbar Anschlussbedingung (Einschätzung, Kapitel 7), für R1–R3 in der Mittelspannung nicht. Ob diese Anforderungen eine Anlaufzeitkonstante vorschreiben, die nach Nr. 10.5 abgezogen würde, ist offen. Drittens ist die anrechenbare Menge begrenzt:

$$E_{\text{MR}} = \tfrac{1}{2}\, m\, T_A\, P_N \;\le\; 12{,}5\ \text{MWs je MW und Produkt}$$

$E_{\text{MR}}$ ist die anrechenbare Momentanreserve in Megawattsekunden (MWs), $m$ ein vom Anbieter für die Vertragslaufzeit gewählter Skalierungsfaktor ($0 < m \le 1$), $T_A$ die Anlaufzeitkonstante in Sekunden (höchstens 25 s) und $P_N$ die Nennleistung in MW; je Einheit sind ein positives und ein negatives Produkt zulässig. Verfügbar ist die Einheit in einer Viertelstunde nur, wenn rund $0{,}04 \cdot m \cdot T_A$ der Nennleistung frei bleiben, bei $m = 1$ und 25 s also die volle Nennleistung, soweit keine Überlast angerechnet wird [K03M-29, Nr. 3.4, 3.8, 4.3–4.5, 4.10, 4.12]. Je frei gehaltenem MW sind das rund 12,5 MWs je Richtung, zum Premiumpreis bei voller Verfügbarkeit rund 11 k€/MW/a je Produkt und 22 k€/MW/a für beide (eigene Rechnung, Obergrenze; Modo im März 2026: 8–20 k€/MW/a [K06M-02]). R2 erzielte 2026* merchant realistisch rund 206 k€/MW/a [M1, Lauf 20260927-fcr125]. Momentanreserve ist also ein kleiner Baustein, der lohnt, wenn eine Überlastreserve des Umrichters das Band stellt oder das Band wenig Arbitrage verdrängt. Wie sie sich mit Regelleistung stapelt, hängt an deren Abrufen; M1 bildet sie nicht ab (N12) [LÜCKE: Mehrkosten netzbildender Umrichter und Überlastreserve für R1/R2]. Für 15-jährige Kapazitätsverträge verlangt das StromVKG von Anlagen ab 10 MW oder mit Hochspannungsanschluss Momentanreserve von mindestens installierter Leistung × 9 s / 2; Batteriespeicher erbringen sie über Überlast oder einen überdimensionierten Umrichter, angerechnet wird nur Umrichterleistung über 130 % der vereinbarten Netzanschlusskapazität [K03R-01, § 16 Abs. 1, 2].

**„Nutzen statt Abregeln“.** Entlastungsregionen für das Zielmodell ab 01.10.2026 (tägliche Ausschreibung der ÜNB, Erstattung je zugeteilter und verbrauchter MWh nach einem Referenzpreis [VR3-32]) gibt es nur im Norden bei 50Hertz und TenneT; TransnetBW und Amprion weisen keine aus, halten eine spätere Ausweisung aber für möglich bzw. notwendig [VR3-32, S. 17–18]. R1–R3 im Raum Stuttgart erzielen damit derzeit nichts, ebenso die Konfiguration des Erlösgutachtens G1 (anonymisiert) in Nordrhein-Westfalen (G1, Kap. 1.1) [VR3-32]. Ob ein Batteriespeicher selbst Entlastungsanlage sein kann, regelt der Wortlaut nicht ausdrücklich; die Entnahmestelle darf keine anderen Verbraucher oder Stromspeicher versorgen, die Kriterien der Zusätzlichkeit legt die Bundesnetzagentur fest [W2V-07] [LÜCKE: § 13k – Vergütungshöhe nach Kap. 6.3 des ÜNB-Konzepts und Zulassung von Speichern].

**§ 14c und Kapazitätsmarkt.** Die Pflicht der Verteilnetzbetreiber zur marktgestützten Beschaffung von Flexibilität nach § 14c EnWG ist nach § 118 Abs. 28 EnWG ausgesetzt, bis die Bundesnetzagentur erstmals Spezifikationen genehmigt oder festlegt [SYN-17]; eine solche Entscheidung und ein Marktvolumen sind nicht belegt [LÜCKE: Stand einer BNetzA-Genehmigung oder -Festlegung nach § 14c Abs. 2/3 EnWG]. Beim Kapazitätsmarkt (Zugang und Termine: Tabelle 15.3, Kapitel 3; Basisfall null, A-040) zählt für den Stapel die Gegenleistung der Zuverlässigkeitsoption: Bezuschlagte Anlagen müssen in Hochpreisviertelstunden verfügbar sein und zahlen „unabhängig vom tatsächlichen Betrieb“ jede Preisspitze über ihrem anlagenspezifischen Ausübungspreis zurück, den Preisspitzenausgleich [K03R-01, §§ 65, 81]. Läuft zugleich ein Toll, erntet der Toller die Spitzen, während der Eigentümer als Kapazitätsverpflichteter zahlt; der Toll-Vertrag muss den Ausgleich deshalb weiterreichen (Einschätzung). Mit festen Schwellen von 300–350 €/MWh statt des täglichen Ausübungspreises und einem Zeitfaktor von 0,25 h je Viertelstunde (Auslegung, Kapitel 3) hätte der Ausgleich 2024–2026 je MW reduzierter Leistung 1–8 k€/a betragen, bei wörtlicher Lesung ohne Zeitfaktor bis zum Vierfachen [M1, Lauf 20260928-kapitel03].

**Behind-the-Meter und Wind.** Speicher hinter dem Netzanschluss eines Industriekunden (Behind-the-Meter), etwa zur Kappung von Lastspitzen, hat die Recherche nicht untersucht [LÜCKE: Behind-the-Meter – Lastspitzenkappung, § 19 Abs. 2 StromNEV, Erlösniveau]; für Fondsprojekte ist das eine Nische, deren Erlös an Lastgang, Netzentgelten und Bonität eines Kunden hängt (Einschätzung). Wind-Co-Location ist belegt, etwa als geteilter NVP in Brüssow [VR3-07]; die Innovationsausschreibung, die nach dem Entwurf des EEG 2027 entfällt (Kapitel 12), lässt Wind mit Speicher zu [VR3-23], am Gebotstermin 01.05.2026 nahmen laut Fachmedium aber nur PV-Speicher-Kombinationen teil [VR3-24]. Weil Wind an Land 2025 mit einem Wertfaktor von 0,833 weit über PV lag, ist die Aufwertung je MWh kleiner (Einschätzung); M1 rechnet Wind nicht [LÜCKE: Wind-Co-Location – Erlös- und NVP-Effekte]. Blindleistung (für R1 und R2 im Basisfall ohne Erlös) und Schwarzstart behandelt Kapitel 3.

> [!STAND]
> **Stand der weiteren Segmente:** Momentanreserve: Festpreise der ersten Periode für Angebote bis 21.01.2028, vorher für neue Angebote änderbar; kontrahierte Mengen veröffentlichen die ÜNB ab dem ersten Quartal 2027 [K03M-06, K03M-29]; Netzbildung am Hochspannungsnetz bisher nur im Normentwurf [K07O-02]. § 13k: Zielmodell ab 01.10.2026 nach dem ÜNB-Konzept vom 01.04.2026; Regionen ändern sich mit sechs Monaten Vorlauf [VR3-32]. § 14c: ausgesetzt nach § 118 Abs. 28 EnWG, keine Festlegung bekannt [SYN-17]. Kapazitätsmarkt: Zuschläge der ersten Runde (Langzeitkapazitäten, für R1–R3 nicht zugänglich) bis 03.11.2026; Anwendung nach Maßgabe der Beihilfegenehmigung (§ 87); Reduktionsfaktoren nach Anlage 3 vor den Terminen 2027 [K03R-01, W0R-10]. MiSpeL (Stand 03.10.2026): Festlegung vom 01.10.2026, wirksam ab Bekanntgabe, im Amtsblatt angekündigt für 07.10.2026, bis 30.09.2027 nur im Einverständnis mit Netz- und Messstellenbetreiber anwendbar (TZ 9a); Bilanzkreisvoraussetzung wie im Arbeitsstand [K12R-17, S. 2–3, 7; K12R-18, S. 21; K12R-02]. EEG 2027: Regierungsentwurf vom 07.09.2026, die Innovationsausschreibung soll entfallen [W2V-17]; die Anhörung im Ausschuss am 05.10.2026 steht aus [K12R-12] (Kapitel 12). Vor Verwendung prüfen.

## Wirkung auf die Erlösprognose: Nebenbedingungen und Opportunitätskosten

Liefer-, Verfügbarkeits- und Vorhaltepflichten binden Leistung, Ladezustand und Anschluss. Entgangene Arbitrage- und Regelreserveerlöse sind Opportunitätskosten und gehören als Nebenbedingung in den Dispatch (Tabelle 15.4), nicht als pauschaler Abschlag hinterher. Ihre Höhe hängt weniger am Vertragstyp als an der Strafe für Abweichungen; alle folgenden Werte stammen aus M1 für R3 mit 20 bzw. 55 MWh im Jahr 2025, in Klammern für 2025/26 (C mit 5 bzw. 10 MW Bezug, A-054) [M1, Lauf 20260928-stacking].

Ein Band-PPA, dessen Fehlmengen der Eigentümer zum Day-Ahead-Preis plus 5 €/MWh nachkauft, bindet den Speicher kaum: Die Opportunitätskosten betragen 0,6 bzw. 1,3 k€/a (1,0 bzw. 1,3). Kosten Fehlmengen 50 €/MWh über dem Marktpreis, was einer Lieferpflicht aus eigener Erzeugung nahekommt, steigen die Opportunitätskosten auf 43,0 bzw. 63,9 k€/a (49,6 bzw. 73,2). Ein PV-PPA pay-as-produced ohne Negativpreisklausel verändert den Einsatz stärker, weil jede erzeugte MWh den Vertragspreis bringt: M1 regelt weniger ab und nutzt Anschluss und Speicher für PV-Strom, der am Markt wenig wert ist. Das kostet 46 bzw. 80 k€/a (41 bzw. 72), mit Klausel nur 8 bzw. 10 k€/a (3 bzw. 5). Am teuersten ist die Grünstrombindung, wie sie etwa der Salzgitter-Vertrag vorsieht [VR3-06]: 516 bzw. 784 k€/a (412 bzw. 676) bei perfekter, 346 bzw. 458 k€/a (272 bzw. 400) bei realistischer Voraussicht (C gegenüber A, operativ, PV ungefördert, eigene Rechnung). Ein Toll nimmt dem Eigentümer bei proportionaler Aufteilung von Leistung und Energie genau den getollten Anteil; die Merchant-Tranche (Kapitel 5) wird nicht schlechter vermarktet (R2, Rechenbeispiel 15.2). Alle Werte sind eher Untergrenzen der Opportunitätskosten: M1 enthält weder Intraday-Handel noch aFRR-Arbeit (A-M1-08, A-M1-09), und Pflichten, die in volatilen Stunden binden, kosten dort zusätzlich (Einschätzung).

| Nr. | Nebenbedingung | Bindet | Stand in M1 2.0.0 |
|---|---|---|---|
| N1 | Einspeise- und Bezugsgrenze am NVP | Anschluss | umgesetzt (fest); zeitvariable Grenzen offen |
| N2 | PV-Bilanz: Einspeisung + Ladung + Abregelung = Erzeugung | PV-Energie | umgesetzt |
| N3 | Grünstrombindung, auch Wechsel von grün auf grau | Ladequelle | umgesetzt; Wechsel offen |
| N4 | Mischspeicher mit Mengenabgrenzung (MiSpeL) | Förderung | angenähert; Monatsabrechnung im Nachlauf |
| N5 | Marktprämie mit Solarspitzenregel (§ 51 EEG) | Förderung | umgesetzt |
| N6 | PV-PPA pay-as-produced | Vertragsmenge | umgesetzt, mit und ohne Negativpreisklausel |
| N7 | Band- oder Profil-PPA | Lieferprofil | Monatsband mit Fehlmengenaufschlag; Ausgleich zum Ausgleichsenergiepreis (reBAP) offen |
| N8 | Pay-as-nominated | Nominierung, Reserve für Abweichungen | offen |
| N9 | Toll | Leistung und Energie | umgesetzt |
| N10 | Floor | Auszahlung | keine Dispatchwirkung; Auszahlung in M2 |
| N11 | Regelreserve-Vorhaltung | Leistungs- und Energieband | umgesetzt |
| N12 | Momentanreserve | Leistungsband | offen |
| N13 | § 13k „Nutzen statt Abregeln“ | Ladestrom in Ereignissen | inaktiv (keine Region) |
| N14 | Degradation und Zyklen | Zyklenbudget | umgesetzt |
| N15 | Unsicherheit und Voraussicht | Prognose | realistisch nur merchant; PPA-Fälle perfekt |
| N16 | Erlöszuordnung PV → Speicher | Abgrenzung | Obergrenze: ganzer Speicherwert zur PV |

Table: Nebenbedingungen N1–N16 und ihr Stand im Modell M1

Quelle: K15-Notiz (N1–N16); Modell M1 2.0.0, Lauf 20260928-stacking, Zusammenfassung Ziffer 5 (Stand 28.09.2026).

Mit jedem Vertrag wächst die Prognosekomplexität (Einordnung): gemeinsame Optimierung von PV und Speicher am NVP mit zeitvariablen Grenzen, Vertragspflichten als harte Nebenbedingungen, PV-Wetterjahre und Preispfade samt Korrelation, weil sonnenreiche Jahre die Capture-Preise drücken, bei pay-as-nominated eine zweistufige Rechnung (Abschnitt 15.8). M1 kennt im realistischen Fall die PV-Erzeugung (A-M1-22), ohne Prognosefehler und Ausgleichsenergie, und rechnet die PPA-Fälle nur bei perfekter Voraussicht. Ein Kalibrierfaktor darf nicht zusätzlich auf realistische M1-Werte gelegt werden, sonst zählen Verfügbarkeit und Voraussicht doppelt (Kapitel 6).

Vorsicht verlangt auch der Realisierungsgrad, das Verhältnis von realistischem Fall und perfekter Voraussicht (Kapitel 4). Für R3 als Mischspeicher beträgt er in M1 73 % (2025) und 77 % (2025/26), für R2 als Standalone-Speicher nur 64 % (2025) bzw. 70 % (2026*) [M1, Lauf 20260928-stacking; eigene Rechnung]. Der Unterschied ist kein Vorteil der Co-Location: Die PV-Erlöse gelten im realistischen Fall als bekannt (A-M1-22), und die Verfügbarkeit von 97 % wirkt nur auf den Mehrerlös des Speichers (A-M1-25). Zieht man überschlägig den Wert der PV allein (776 bzw. 970 k€/a) ab, realisiert der Speicher von R3 rund 65 bzw. 67 %, ähnlich wie R2 (eigene Rechnung).

## Wirkung auf Bewertung und Finanzierung

Tabelle 15.5 fasst als Einschätzung zusammen, wie die Segmente gegenüber merchant wirken.

| Segment | Erlösniveau Eigentümer | Volatilität | Opportunitätskosten | Prognosekomplexität | Finanzierbarkeit |
|---|---|---|---|---|---|
| PV-PPA pay-as-produced, Speicher merchant | − bis + je nach Preis | − | klein | + | + für den PV-Teil |
| Hybrid-PPA mit Profil, grün | − | − | hoch (Grünstrombindung) | ++ | + bei Bonität des Abnehmers |
| Hybrid-PPA mit Abnehmer-Dispatch | −− bei Preisen nach Solar-PPA + 24 % | −− | Speicherwert beim Abnehmer | − | ++ bei Bonität des Abnehmers |
| Toll (80 %), auch neben PV-PPA | − | −− in der Laufzeit | getollter Anteil | − in der Laufzeit | ++ |
| Floor | − (Prämie) | − nach unten | keine | + | + |
| Momentanreserve | + klein | − | Leistungsband | 0 | + klein |
| Kapazitätsmarkt (ab 11/2031) | + offen | − | Verfügbarkeitspflicht | + | + falls zugänglich |

Table: Wirkungsmatrix der Segmente gegenüber merchant (Einschätzung)

Quelle: eigene Einschätzung nach Modell M1, Lauf 20260928-stacking, Vorrecherche VR3 (Abschnitt B.8), Kapitel 3 und 5, A-033; ++/+ steigt stark/steigt, 0 kaum Änderung, −/−− sinkt/sinkt stark (Stand 28.09.2026).

**Kontrahierter Anteil.** Welcher Anteil der Erlöse gesichert ist, hängt daran, ob man Zeit oder Wert misst. Ein 80-%-Toll in den Betriebsjahren 2–8 eines 20-jährigen Projekts (A-038) deckt 0,8 × 7/20 = 28 % der Kapazitätsjahre, barwertgewichtet bei 10,25 % (A-024), vor Steuern und bei gleichbleibenden Erlösen aber rund 42 % (eigene Rechnung):

$$\phi_{\text{Wert}} = \alpha \cdot \frac{\sum_{t=2}^{8} (1+r)^{-t}}{\sum_{t=1}^{20} (1+r)^{-t}}$$

mit $\alpha$ als Toll-Anteil der Leistung und $r$ als Diskontsatz. Ungesichert bleibt dennoch der größere Teil, rund 58 % des Barwerts: Jahr 1 (11 %), Merchant-Tranche der Jahre 2–8 (10 %) und Merchant-Tail (37 %; eigene Rechnung). Sinken die Merchant-Erlöse über die Zeit, steigt der kontrahierte Anteil. Ein PV-PPA sichert nur den Preis der PV-Menge: Bei R3 ist die PV-Erzeugung von 15.750 MWh zu 45 €/MWh rund 0,71 Mio. €/a wert, 21–29 % des Merchant-Werts von C bei perfekter bzw. realistischer Voraussicht 2025 und 2025/26 (eigene Rechnung aus [M1, Lauf 20260928-stacking]).

**Diskontierung.** Getrennt abgezinst (Kapitel 18) gelten 9,0 % für Toll-Zahlungen eines Tollers mit Investment Grade und 10,25 % für Merchant-Erlöse (A-025, A-024). Für PPAs ist die Zuordnung feiner (Einschätzung): Der Festpreis sichert den Preis, nicht die Menge (Abschnitt 15.1). Nur der Teil, dessen Preis und Menge mit hoher Sicherheit feststehen, verdient den niedrigeren Satz, und nur so lange, wie der Vertrag läuft und der Abnehmer zahlt [LÜCKE: Diskontsätze und DSCR für PPA-gesicherte Erlöse bei Co-Location]. Ein Hybrid-PPA mit Abnehmer-Dispatch wirkt für den Eigentümer wie ein Toll mit Mengenrisiko: Der Preis je MWh steht fest, die Menge hängt an Sonne, Abregelung und Speicherverlusten.

**DSCR und Gearing.** Banken bemessen Fremdkapital je Erlösart. M2 rechnet mit einer Schuldendienstdeckung (DSCR) von 1,20 auf Toll-, 1,30 auf Floor- und 2,00 auf Merchant-Erlöse und mit Gearing-Kappen von 80, 60 und 40 % (A-033, A-034, A-M2-06; Kapitel 5 und 20). Für PPA-Erlöse fehlt ein belegter Wert; Co-Location-Projekte stellten 2025 nur 12 % der 82 von Modo erfassten europäischen Speichertransaktionen (nach Anzahl) [K20F-08]. Nach M2 senkt ein 80-%-Toll die Standardabweichung des Nettoerlöses 2030 um 79 % (R2 mit Toll zu 177,1 k€/MW/a: von 18,2 auf 3,8 k€/MW/a nominal), den Kapitalwert von R2 sichert er aber kaum: Der P90 des NPV nach Unternehmenssteuern steigt getrennt abgezinst nur von −1,82 auf −1,65 Mio. € und fällt einheitlich auf −1,90 Mio. €, weil nach Ende des Tolls der Merchant-Tail das Risiko trägt und der Toll den Erwartungswert senkt [M2, Lauf M2-20260928-P04 · Zusatz K05; Kapitel 5, Rechenbeispiel 5.4]. Wie er Kapitalwert, DSCR und Gearing im Basisfall verändert, zeigt Rechenbeispiel 15.2, Schritt 6.

**Laufzeiten und Kontrahenten.** Tolls laufen fünf bis sieben Jahre (Kapitel 5), die PPAs der Tabelle 15.2 sieben bzw. zehn Jahre [VR3-07, VR3-08], Mini-Perm-Kredite sieben Jahre mit mindestens 60 % Tilgung (A-035). Danach tragen der Merchant-Tail und eine Refinanzierung den Wert; eine Grünstrombindung, die über das Vertragsende hinaus gilt, schmälert ihn (Einschätzung). Mit PPA und Toll hängt ein Projekt an zwei Vertragspartnern, deren Bonität öffentlich nicht belegt ist. Bedienen wenige Abnehmer und Toller mehrere der rund 15 Projekte des Musterfonds R4 (A-018), entsteht Klumpenrisiko (Kapitel 5 und 25).

**Bewertung im NAV.** Ein Festpreisvertrag stabilisiert den Cashflow, nicht unbedingt den Wert, den ein Fonds ausweist (Einschätzung). Steigen die Marktwerte wie beim PV-PPA von 2025 auf 2025/26, fällt der Wert des Vertrags für den Eigentümer: Bei R3 (20 MWh, 45 €/MWh) lag der Marktwert der Vertragsmenge 2025/26 12,5 €/MWh über dem Vertragspreis (2025: 1,4 €/MWh), die Festpreiskomponente bei rund −196 k€/a; mit der Dispatchwirkung stand der Eigentümer 236 k€/a schlechter als merchant (perfekte Voraussicht, brutto) [M1, Lauf 20260928-stacking; Rechenbeispiel 15.1]. Ob die Bewertung solche Verträge mit Marktwerten ansetzt und damit Schwankungen in den Nettoinventarwert (NAV) trägt, bestimmen Bewertungsrichtlinie und Rechnungslegung; die Frage gehört an KVG und Wirtschaftsprüfer (Kasten unten, Kapitel 19).

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Steuer und KVG. Steuerberater und Wirtschaftsprüfer zur steuerlichen und bilanziellen Einordnung von PPA-, Toll- und Momentanreservezahlungen (Leistungsentgelt, Miete oder Leasing, Derivat), zur Umsatzsteuer bei finanziell abgewickelten PPAs und zu Fehlmengen- und Ausgleichszahlungen (Kapitel 17). KVG, gegebenenfalls mit BaFin-Klärung, zur Bewertung langfristiger PPA- und Toll-Verträge im NAV des Spezial-AIF (A-018), zu Kontrahentenlimits im Risikomanagement und zur Frage, ob finanzielle PPAs oder Tolls der Projektgesellschaften aufsichtsrechtlich als Derivate zählen (Kapitel 22).

## Modellübung: vom Day-Ahead-LP zum Hybrid- und Toll-Modell

Kapitel 4 hat das lineare Programm (LP) von M1 formuliert: Laden $c_t$, Entladen $d_t$, Ladezustand $s_t$, Regelleistung $f_k$ und $a^{\pm}_k$, Zielfunktion Handelserlös minus Degradationskosten plus Leistungspreise. M1 2.0.0 erweitert es in vier Stufen [M1, Lauf 20260928-stacking]; jede Gleichung beantwortet eine Vertragsfrage.

*Stufe 1 – PV und gemeinsamer NVP (N1–N3).* Das PV-Potenzial $G_t$ teilt sich in direkte Einspeisung $e_t$, Ladung aus PV $c^{\text{PV}}_t$ und Abregelung $k_t$; der Speicher lädt zusätzlich $c^{\text{N}}_t$ aus dem Netz, und beide Richtungen am NVP sind begrenzt:

$$G_t = e_t + c^{\text{PV}}_t + k_t, \qquad e_t + d_t - c^{\text{N}}_t \le P^{\text{exp}}, \qquad c^{\text{N}}_t - e_t - d_t \le P^{\text{imp}}$$

Für R3 gelten $P^{\text{exp}}$ = 12 MW und $P^{\text{imp}}$ = 5 MW (Mischspeicher C mit 20 MWh; mit 55 MWh 10 MW, A-054); die Speicherbilanz aus Kapitel 4 erhält $c_t = c^{\text{PV}}_t + c^{\text{N}}_t$, die Bänder der Regelleistung gelten am NVP. Der Grünstromspeicher (A) setzt $c^{\text{N}}_t = 0$ und darf negative Regelleistung nur durch weniger Einspeisung erbringen (A-M1-21). Einen Wechsel von grün auf grau wie in Brüssow bildet dieselbe Bedingung mit einem Stichtag ab (N3; in M1 noch nicht umgesetzt). Für eine PV mit Anschluss ab 01.01.2027 sähe der Entwurf des Netzanschlusspakets nur einen Anspruch auf einen Anschluss mit Einspeisegrenze 70 % der installierten Leistung vor, mehrere Anlagen am NVP in Summe (§ 8 Abs. 1 EEG-E) [K11O-02]; was das für $P^{\text{exp}}$ bedeutet und ob der Speicher mitzählt, ist eine Rechtsfrage (Abschnitt 14.2).

*Stufe 2 – PV-PPA pay-as-produced (N6).* Die Zielfunktion erhält den Term $\sum_t \Delta_t\,(\bar{p} - \lambda_t)\,(G_t - k_t)$ für die Menge am PV-Zähler, mit Negativpreisklausel nur für $\lambda_t \ge 0$. Zusammen mit dem Marktwert macht er jede nicht abgeregelte MWh den Vertragspreis $\bar{p}$ wert, gleich ob sie eingespeist oder gespeichert wird; das erzeugt die Dispatchwirkung (Abschnitte 15.3 und 15.6).

*Stufe 3 – Band (N7).* Mit der Nettoeinspeisung $g_t$ gilt $m_t \ge q_t - g_t$ und $m_t \ge 0$; die Zielfunktion verliert $\delta \sum_t \Delta_t\, m_t$. Die Festpreiskomponente $\sum_t \Delta_t (\bar{p} - \lambda_t) q_t$ hängt nicht vom Fahrplan ab. Ob ein Band den Speicher bindet, entscheidet in M1 deshalb allein der Aufschlag $\delta$, nicht das Profil: Mit $\delta = 0$ ändert sich der Fahrplan gar nicht.

*Stufe 4 – Toll (N9).* Für den Eigentümer gelten bei Nennleistung $P_N$ und nutzbarer Energie $E$ die Grenzen $c_t, d_t \le (1-\alpha)\,P_N$ und $0 \le s_t \le (1-\alpha)\,E$; die Regelleistungsbänder schrumpfen ebenso. Weil das LP linear homogen ist, also mit halber Leistung und Energie genau den halben Erlös liefert, beträgt der Erlös der Merchant-Tranche exakt das $(1-\alpha)$-Fache des Merchant-Erlöses. Abweichungen entstehen erst durch ganzzahlige Gebotsgrößen der Regelleistung (1 MW [M1Q-02]; M1 rundet ab) und durch einen Energieanteil, der nicht $(1-\alpha)\,E$ entspricht (A-M1-30; Übung 15.4).

Die Momentanreserve (N12) ließe sich als weiteres Band ergänzen: In jeder Viertelstunde, für die Verfügbarkeit gemeldet wird, bleibt $b = 0{,}04\, m\, T_A\, P_N$ frei, also

$$d_t - c_t + b \le P_N, \qquad c_t - d_t + b \le P_N$$

mit einem Erlös von $E_{\text{MR}} \cdot FP$ je Produkt, $FP$ als Festpreis in €/MWs/a (Abschnitt 15.5). Für pay-as-nominated (N8, in M1 offen) bräuchte das Modell eine Nominierungsstufe am Vortag auf Basis der PV-Prognose und eine Echtzeitstufe, in der der Speicher Prognosefehler ausgleicht und Restabweichungen zum reBAP (Kapitel 2) abgerechnet werden; die Verteilung der Prognosefehler ist nicht beschafft (A-M1-22).

## Rechenbeispiele am Referenzfall {.unnumbered}

> [!BEISPIEL]
> **Rechenbeispiel 15.1: R3 mit PV-PPA pay-as-produced gegenüber Hybrid-PPA mit Profil** (Modell M1 2.0.0, Lauf 20260928-stacking; perfekte Voraussicht; Day-Ahead, FCR, aFRR; brutto vor Vermarktungsentgelt, nominal, k€/a)
>
> *Schritt 1 – Eingaben:* R3 mit 15 MWp PV, 12 MW Wechselstromleistung und 15.750 MWh im Jahr 2025 (A-011, A-M1-31), Speicher 10 MW/20 MWh nutzbar; Anschluss wie C (12 MW Einspeisung, 5 MW Bezug) bzw. A (A-054, D-025); PV ungefördert (A-M1-26). PV-PPA: 45 €/MWh finanziell auf die Menge am PV-Zähler (A-M1-27). Hybrid-PPA mit Profil: Monatsband mit 50 % der PV-Monatsmenge, gleichmäßig über 24 Stunden, Preis 10 % unter dem Marktwert der Bandmenge, Fehlmengen zum Day-Ahead-Preis plus 5 €/MWh, Grünstromspeicher (A-M1-29). Alle Vertragspreise sind unbelegte Annahmen.
>
> *Schritt 2 – Referenzen:* Merchant erzielt der Mischspeicher C 3.412,2, der Grünstromspeicher A 2.896,3 k€/a; realistisch 2.489,0 bzw. 2.143,0 k€/a.
>
> *Schritt 3 – PV-PPA ohne Klausel:* Vertragsmenge ist die nicht abgeregelte Erzeugung von 15.268 MWh mit einem Marktwert von 46,42 €/MWh. Festpreiskomponente (45 − 46,42) × 15.268 MWh = −21,7 k€/a. Dispatchwirkung −46,1 k€/a: M1 regelt nur 482 statt 2.089 MWh ab, weil jede erzeugte MWh den Vertragspreis bringt. Eigentümerwert 3.344,4 k€/a, 67,8 k€/a unter C; Indifferenzpreis 45 + 67,8 k€ / 15.268 MWh = 49,4 €/MWh.
>
> *Schritt 4 – mit Negativpreisklausel:* Vertragsmenge nur in Viertelstunden mit $\lambda_t \ge 0$, 11.600 MWh zu 65,45 €/MWh Marktwert. Festpreiskomponente (45 − 65,45) × 11.600 MWh = −237,2, Dispatchwirkung −8,1, zusammen −245,3 k€/a; Indifferenzpreis 66,1 €/MWh. Die Klausel kostet den Eigentümer bei 45 €/MWh 177,5 k€/a mehr.
>
> *Schritt 5 – Hybrid-PPA mit Profil:* Bandmenge 7.875 MWh, im Jahresmittel rund 0,9 MW. Ihr Marktwert beträgt 81,84 €/MWh, weil das Band auch Abend- und Nachtstunden enthält; der Preis liegt bei 73,65 €/MWh. Festpreiskomponente (73,65 − 81,84) × 7.875 MWh = −64,4 k€/a; Fehlmengen 3.228 MWh × 5 €/MWh = −16,1 k€/a; Opportunitätskosten des Speichers 0,6 k€/a. Eigentümerwert 2.815,1 k€/a, 81,2 k€/a unter A und 597,2 k€/a unter C; Indifferenzpreis 84,0 €/MWh.
>
> *Schritt 6 – Varianten:* Tabelle 15.6 zeigt die Abstände für 2025 und 2025/26 (Referenzen 2025/26: C 3.192,4, A 2.780,6 k€/a).
>
> | Variante (R3, 20 MWh) | Referenz | Wert 2025 | Δ 2025 | Δ 2025/26 | Indifferenzpreis 2025 und 2025/26, €/MWh |
> |---|---|---:|---:|---:|---:|
> | PV-PPA 45 €/MWh | C | 3.344,4 | −67,8 | −236,3 | 49,4 / 60,1 |
> | PV-PPA 45 €/MWh mit Negativpreisklausel | C | 3.166,9 | −245,3 | −411,3 | 66,1 / 78,3 |
> | PV-PPA 40 bzw. 55 €/MWh | C | – | −144,0 / +85,4 | −314,6 / −79,4 | – |
> | merchant Grünstromspeicher (A) | C | 2.896,3 | −516,0 | −411,8 | – |
> | Band 50 %, Abschlag 10 %, Aufschlag 5 €/MWh | A | 2.815,1 | −81,2 | −100,5 | 84,0 / 108,2 |
> | Band, Abschlag 0 bzw. 20 % | A | – | −16,7 / −145,6 | −17,0 / −183,9 | 84,0 / 108,2 |
> | Band, Aufschlag 50 €/MWh | A | 2.717,0 | −179,3 | −189,4 | 96,4 / 119,5 |
> | Band 30 bzw. 70 % der PV-Menge | A | – | −48,1 / −115,1 | −59,7 / −141,8 | 83,8–84,1 / 108,0–108,3 |
>
> Table: Eigentümerwert von R3 mit PV-PPA und Hybrid-PPA mit Profil, k€/a, und Indifferenzpreis, €/MWh
>
> Quelle: Modell M1 2.0.0, Lauf 20260928-stacking (perfekte Voraussicht; Day-Ahead, FCR, aFRR; brutto vor Vermarktungsentgelt; nominal); 2025/26 = 12 Monate bis 26.09.2026 ohne Hochrechnung (A-M1-33); Vertragspreise A-M1-27, A-M1-29 (Stand 28.09.2026).
>
> *Ergebnis:* Der Hybrid-PPA mit Profil hat gegenüber seiner Referenz kaum Dispatchwirkung; sein Preis sind Abschlag und Fehlmengen, die größte Last ist die Grünstrombindung (gegenüber C 516 k€/a 2025 und 412 k€/a 2025/26, operativ). Erst eine harte Lieferpflicht (Aufschlag 50 €/MWh) bindet den Speicher mit 43 bzw. 50 k€/a. Der PV-PPA ist ein Tausch: 2025 lag der Marktwert der PV-Menge mit 46,4 €/MWh nahe am Vertragspreis, 2025/26 bei 57,5 €/MWh, und der Indifferenzpreis stieg von 49,4 auf 60,1 €/MWh. Der Abstand zum Festpreis von 45 €/MWh ist der Preis der Absicherung: 2025 stammen 1,4 €/MWh aus der Festpreiskomponente (Marktwert über Festpreis) und 3,0 €/MWh aus der Dispatchwirkung, 2025/26 12,5 und 2,6 €/MWh. Eine Negativpreisklausel hebt den Indifferenzpreis um 16,7 (2025) bzw. 18,2 €/MWh (2025/26). Alle Eigentümerwerte gelten bei perfekter Voraussicht und sind Obergrenzen. Die Opportunitätskosten (Dispatchwirkung, Grünstrombindung) sind wegen fehlender Märkte eher Untergrenzen; mit realistischer Voraussicht ist die Grünstrombindung aber kleiner (346 statt 516 k€/a 2025; Abschnitt 15.6).

> [!BEISPIEL]
> **Rechenbeispiel 15.2: R2 mit 80-%-Toll als Nebenbedingung im Dispatch** (Modell M1 2.0.0, Lauf 20260928-stacking; perfekt und realistisch mit 97 % Verfügbarkeit; Day-Ahead, FCR, aFRR; brutto vor Vermarktungsentgelt, nominal; Bewertung Modell M2, Lauf M2-20260928-P04)
>
> *Schritt 1 – Eingaben:* R2 mit 10 MW/55 MWh nutzbar, Anschluss 10 MW (A-M1-07), FCR mit Faktor 1,25 im Leistungsband (A-M1-20). Ein Toller mietet 8 MW (A-038); der Eigentümer vermarktet 2 MW. Wie Verträge die Energie aufteilen, nennen öffentliche Quellen nicht (A-M1-30).
>
> *Schritt 2 – Virtuelle Aufteilung:* Mit 2 MW und 11 MWh, also 20 % von Leistung und Energie, erzielt der Eigentümer in allen vier Fällen genau 20,0 % des vollen Merchant-Erlöses (Tabelle 15.7), weil das LP linear homogen ist. Die pauschale 20-%-Rechnung in M2 ist damit richtig.
>
> *Schritt 3 – Gebotsraster:* Regelleistung nur in ganzen MW [M1Q-02] senkt den Anteil auf 19,6–19,8 %, 2026* realistisch von 411,5 auf 407,6 k€/a.
>
> *Schritt 4 – Energieanteil:* Behält der Eigentümer nur 4 MWh (2 h), sinkt sein Anteil auf 15,7–18,5 %; mit 22 MWh (11 h) steigt er auf 20,7–22,9 %. Mit 4 MWh stammen 2026* realistisch 229,6 der 322,8 k€/a aus aFRR, mit 22 MWh 350,2 der 471,2 k€/a aus dem Day-Ahead-Handel. Die Spanne von 148 k€/a entspricht 7 % des vollen Merchant-Erlöses.
>
> | Erlös der Merchant-Tranche | 2025 perfekt | 2025 realistisch | 2026* perfekt | 2026* realistisch |
> |---|---:|---:|---:|---:|
> | R2 voll merchant (10 MW/55 MWh) | 3.271,9 | 2.096,4 | 2.939,5 | 2.057,5 |
> | 2 MW/11 MWh, virtuelle Aufteilung | 654,4 (20,0 %) | 419,3 (20,0 %) | 587,9 (20,0 %) | 411,5 (20,0 %) |
> | dazu Gebotsraster 1 MW | 648,2 (19,8 %) | 415,7 (19,8 %) | 576,4 (19,6 %) | 407,6 (19,8 %) |
> | 2 MW/4 MWh | 595,2 (18,2 %) | 388,6 (18,5 %) | 474,5 (16,1 %) | 322,8 (15,7 %) |
> | 2 MW/22 MWh | 694,1 (21,2 %) | 434,9 (20,7 %) | 653,7 (22,2 %) | 471,2 (22,9 %) |
>
> Table: Erlös der Merchant-Tranche bei 80-%-Toll (R2), k€/a und Anteil am vollen Merchant-Erlös
>
> Quelle: Modell M1 2.0.0, Lauf 20260928-stacking; Gebotsraster [M1Q-02]; Energieanteil A-M1-30; brutto vor Vermarktungsentgelt, nominal; 2026* hochgerechnet (A-M1-12) (Stand 28.09.2026).
>
> *Schritt 5 – Toll-Zahlung im Jahresvergleich:* 8 MW × 177,1 k€/MW/a = 1.416,8 k€/a, fest nominal; der Preis ist eine unbelegte Hochrechnung (A-M2-15, Spanne 150–200 k€/MW/a nach A-M2-39). Mit dem Erlös der Merchant-Tranche 2026* (realistisch, virtuell) erhielte der Eigentümer 1.416,8 + 411,5 = 1.828,3 k€/a statt 2.057,5 k€/a merchant; mit 6 % Vermarktungsentgelt nur auf Merchant-Erlöse (A-015, A-M2-42) 1.803,6 statt 1.934,1 k€/a. Gleichauf lägen beide bei einem Toll-Preis von 205,8 k€/MW/a vor bzw. 193,4 k€/MW/a nach Entgelt, dem Jahresgleichstand 2026* (eigene Rechnung).
>
> *Schritt 6 – Bewertung:* Der Jahresvergleich ist keine Bewertung: Der Toll zahlt von 07/2028 bis 06/2035 einen festen Nominalpreis, die Merchant-Erlöse folgen einem Pfad. Nach M2 (Erwerbersicht, Investitionsentscheidung (FID) am 31.12.2026, nominal, nach Entgelt und Unternehmenssteuern, getrennt abgezinst wie in Abschnitt 15.7) hat R2 merchant einen Kapitalwert (NPV) von 1,11 Mio. € und eine EK-IRR von 13,9 % bei 40 % Fremdkapital und einer kleinsten DSCR von 2,98. Mit 80-%-Toll zu 150/177,1/200 k€/MW/a betragen der NPV −0,08/0,70/1,34 Mio. €, die EK-IRR 13,6/18,7/24,7 %, das Fremdkapital 67/75/80 % der Gesamtinvestition und die kleinste DSCR 1,33/1,31/1,32 [M2, Lauf M2-20260928-P04; Projekt-IRR in Kapitel 5, Rechenbeispiel 5.4]. Den Merchant-NPV erreicht der Toll bei 191,8 k€/MW/a, einheitlich mit 10,25 % abgezinst erst bei 201,8 k€/MW/a (Gleichstandspreis; Kapitel 5, Tabelle 5.8). Anders als der Jahresgleichstand aus Schritt 5 erfasst er Erlöspfad, Risikoeffekt und Merchant-Tail über die Laufzeit; dass beide Werte nahe beieinanderliegen, ist keine gegenseitige Bestätigung.
>
> *Ergebnis:* Für den Erlös der Merchant-Tranche entscheidend ist die vertragliche Aufteilung der Energie, die öffentliche Verträge nicht nennen: Sie verschiebt ihn um bis zu sieben Prozentpunkte des Merchant-Erlöses, das Gebotsraster nur um 0,2–0,4 Prozentpunkte. Über die Laufzeit kostet der Toll zu 177,1 k€/MW/a 0,41 Mio. € Kapitalwert (nach Unternehmenssteuern, getrennt abgezinst) und hebt Fremdkapital und EK-IRR; das Urteil hängt am unbelegten Toll-Preis.

## Praxis-Check und typische Fehler {.unnumbered}

> [!TIP]
> **Praxis-Check:** Prüffragen für Angebote, Verträge und Due Diligence bei PV, PPA und Toll
>
> - Gegen welche Referenz ist ein Vertragsangebot gerechnet (Mischspeicher oder Grünstromspeicher, perfekte oder realistische Voraussicht), und ist der Indifferenzpreis einschließlich Dispatchwirkung bekannt?
> - Auf welche Menge bezieht sich der Preis (PV-Zähler oder NVP, erzeugt oder eingespeist), wie sind negative Preise, Abregelung, Fehlmengen und Ausgleichsenergie geregelt, und wer trägt PV-Prognosefehler?
> - Wer disponiert den Speicher, wer hat Vorrang am NVP, gilt eine Grünstrombindung, wie lange, und ist ihr Preis (C gegenüber A) im Vertrag vergütet?
> - Wie wird der Capture-Uplift geteilt, und steht die Aufteilung ausdrücklich im Preis?
> - Passt die Vermarktungsstruktur zur Bilanzkreispflicht bei Marktprämie und MiSpeL (Kapitel 12)?
> - Nennt der Toll die überlassene Energie in MWh, die Ladezustandsregeln und die Zyklengrenze, nicht nur die Leistung (Kapitel 5)?
> - Momentanreserve: netzbildender Umrichter, anrechenbare MWs, erreichbare Verfügbarkeit (Premium mindestens 90 %, sonst entfällt die Jahresvergütung), Zustimmung des Netzbetreibers, Angebot bis 21.01.2028? Schreiben die TAR des Netzbetreibers eine Anlaufzeitkonstante vor, die von der vergüteten Menge abgezogen wird?
> - Kapazitätsmarkt: Wer zahlt den Preisspitzenausgleich, wenn ein Toller die Spitzen erntet, und vertragen sich Verfügbarkeitspflicht und Toll- oder PPA-Pflichten?
> - Welche DSCR setzt die Bank auf PPA-, Toll- und Merchant-Erlöse, und wie viel Wert liegt nach Vertragsende im Merchant-Tail?
> - Wie bewertet die KVG langfristige PPA- und Toll-Verträge im NAV, und wie viele Projekte des Fonds hängen am selben Abnehmer oder Toller?

> [!WARNING]
> **Typische Fehler:**
>
> - Erlöse von Speicher, PV und Vertrag addieren, obwohl Liefer- und Verfügbarkeitspflichten Leistung, Ladezustand und Anschluss binden; die Opportunitätskosten gehören als Nebenbedingung in den Dispatch.
> - Einen Vertragspreis mit dem Merchant-Wert bei perfekter Voraussicht oder mit der falschen Referenz vergleichen.
> - Den Capture-Uplift von +81–82 % als Erlös des Eigentümers lesen; wem er zusteht, entscheidet der Vertrag.
> - Hybrid-Aufschläge ohne Mengenbasis und Basispreis vergleichen: +24 % je eingespeister MWh auf einen Anker unter dem Merchant-Wert der PV können weniger sein als ein PV-PPA je erzeugter MWh.
> - Ein Teiljahr mit PV linear hochrechnen: Enthält es den Sommer, überzeichnet das alle PV-bezogenen Beträge (R3 im Teiljahr 2026: +23 % PV-Menge).
> - Europäische PPA-Indizes oder die Modellannahmen A-M1-27 bis A-M1-29 als deutsche Marktpreise zitieren.
> - Einen Band-PPA mit Nachkauf zum Marktpreis für eine harte Bindung des Speichers halten oder eine echte Lieferpflicht übersehen.
> - Beim Toll 20 % des Merchant-Erlöses ansetzen, obwohl der Toller mehr als 80 % der Energie erhält.
> - Realisierungsgrade von Co-Location- und Standalone-Projekten vergleichen, ohne den PV-Anteil herauszurechnen.
> - Momentanreserve als Festpreis mal MWs rechnen, ohne Verfügbarkeit, freies Leistungsband und netzbildenden Umrichter; § 13k außerhalb der Entlastungsregionen oder den Kapazitätsmarkt vor 11/2031 ansetzen.

## Zusammenfassung {.unnumbered}

1. Ein Erlösstapel ist das gemeinsame Optimum aller Segmente und liegt nie über der Summe der Einzelerlöse. Segmente unterscheiden sich nach Vertragsart, Abwicklung, Steuerungsrecht und Risikoallokation; Kontrahierung und Steuerung fallen oft auseinander.
2. Ein Grünstromspeicher hebt in M1 den Wert je MWh PV-Erzeugung mit 20 MWh um 81–82 %, mit 55 MWh um 144–146 % (2025 und 2025/26; perfekte Voraussicht, nur Day-Ahead, Obergrenze). Keine öffentliche Quelle beziffert, wem die Aufwertung zusteht; bei einem Hybridaufschlag von 24 % auf die eingespeiste Menge geht sie unter den Modellannahmen ganz an den Abnehmer, weil der Aufschlag nur die Mengenminderung ausgleicht und der Anker von 45 €/MWh unter dem Merchant-Wert der PV liegt.
3. Deutsche Hybrid- und Co-Location-Verträge 2026 decken drei Muster ab: Abnehmer-Dispatch (Salzgitter), pay-as-nominated (DB Energie) und entbündelt mit PV-PPA und Toll (Brüssow). Preise nennt keiner; europäische Anker sind 45 €/MWh (Pexapark) und +24 % für Hybride (LevelTen).
4. Die Opportunitätskosten eines Vertrags hängen an der Strafe für Abweichungen: Ein Band mit Nachkauf zum Marktpreis kostet den Speicher unter 2 k€/a, eine harte Lieferpflicht 43–73 k€/a, die Grünstrombindung 272–784 k€/a (R3, 2025 und 2025/26; operativ, PV ungefördert).
5. Ein PV-PPA zu 45 €/MWh lag 2025 4,4 €/MWh unter dem Indifferenzpreis von 49,4 €/MWh, 2025/26 15,1 €/MWh unter 60,1 €/MWh; der Abstand ist der Preis der Absicherung. Eine Negativpreisklausel hebt den Indifferenzpreis um 17–18 €/MWh.
6. Bei proportionaler Aufteilung erhält der Eigentümer eines 80-%-Tolls genau 20 % des Merchant-Erlöses; der Energieanteil verschiebt das auf 16–23 %. Nach M2 senkt ein Toll zu 177,1 k€/MW/a (unbelegt) den NPV von R2 um 0,41 Mio. € (nach Unternehmenssteuern, getrennt abgezinst) und hebt das Fremdkapital von 40 auf 75 % (Kapitel 5, 18 und 20).
7. Momentanreserve ist ein kleiner Festpreisbaustein mit Mindestverfügbarkeit (darunter entfällt die Jahresvergütung), zu sichern durch ein frühes Angebot, spätestens bis 21.01.2028; § 13k bringt R1–R3 derzeit nichts, § 14c ist ausgesetzt, der Kapazitätsmarkt ist ein Upside ab 11/2031 und verlangt eine Regel zum Preisspitzenausgleich im Toll-Vertrag.
8. Verträge erhöhen den kontrahierten Anteil am Wert stärker als am Zeitraum: Ein 80-%-Toll in den Jahren 2–8 deckt 28 % der Kapazitätsjahre, aber rund 42 % des Barwerts (vor Steuern). Für PPA-Erlöse fehlen belegte Diskontsätze und DSCR, und ein Festpreis stabilisiert den Cashflow, nicht unbedingt den NAV.

## Übungen {.unnumbered}

**Übung 15.1 (Klassifizieren).** Ordnen Sie fünf Verträge nach den Spalten der Tabelle 15.1 ein und geben Sie an, wer den Capture-Uplift erhält: (a) Brüssow, (b) MaxSolar – DB Energie, (c) Zelestra – Salzgitter, (d) der 80-%-Teil-Toll SMAREG 12 (Kapitel 5), (e) R2 mit Momentanreserve Premium, angeboten im Dezember 2027 über 120 Monate. Welche Angaben fehlen in allen öffentlichen Quellen, und warum braucht der Fonds sie?

**Übung 15.2 (Rechnen).** R3 mit 20 MWh, 2025, perfekte Voraussicht: merchant C 3.412,2 k€/a. PV-PPA zu 45 €/MWh ohne Klausel: Vertragsmenge 15.268 MWh, Marktwert 46,42 €/MWh, Marktwert des Fahrplans 3.366,1 k€/a; mit Klausel: 11.600 MWh, 65,45 €/MWh, 3.404,1 k€/a. (a) Berechnen Sie Festpreiskomponente, Dispatchwirkung, Eigentümerwert und Indifferenzpreis. (b) Was kostet die Klausel bei 45 €/MWh in k€/a, und um wie viel hebt sie den Indifferenzpreis, 2025 und 2025/26 (dort Abstand zu C −236,3 ohne und −411,3 k€/a mit Klausel, Indifferenzpreis 60,1 bzw. 78,3 €/MWh)? (c) Warum liegt der PV-PPA zu 55 €/MWh 2025 über merchant (+85,4 k€/a), 2025/26 aber darunter (−79,4 k€/a)? (d) Gegen welche Referenz messen Sie einen Hybrid-PPA mit Grünstrombindung, und wie gehen Sie mit dem Abstand von C zu A um?

**Übung 15.3 (Rechnen und Bewerten).** R3 mit 20 MWh, 2025, nur Day-Ahead, perfekt: PV allein 49,2 €/MWh, mit Grünstromspeicher 89,4 €/MWh je erzeugter MWh (15.750 MWh); grüne Einspeisung 12.820 MWh mit 110,9 €/MWh Marktwert; Degradationskosten 13,2 k€/a beim Eigentümer. (a) Berechnen Sie den Uplift in % und k€/a. (b) Ein Abnehmer bietet 56 €/MWh je eingespeister MWh und disponiert den Speicher. Wie verteilt sich der Uplift? (c) Bei welchem Preis je eingespeister MWh erhielte der Eigentümer die Hälfte? (d) Was verlangen Sie im Term Sheet, und was ändert sich, wenn Sie merchant auch Regelreserve vermarkten könnten (A mit Regelreserve: 2.896,3 k€/a)?

**Übung 15.4 (Rechnen und Bewerten).** Nutzen Sie Tabelle 15.7. (a) Berechnen Sie für 2026* (realistisch) den Jahreserlös des Eigentümers mit 80-%-Toll zu 150, 177,1 und 200 k€/MW/a, vor und nach 6 % Vermarktungsentgelt auf Merchant-Erlöse, und den Jahresgleichstand. (b) Ein Toller bietet 177,1 k€/MW/a für 8 MW, verlangt aber 51 MWh; der Eigentümer behält 2 MW/4 MWh. Was kostet das 2025 und 2026* (realistisch) gegenüber der virtuellen Aufteilung, und welchen Aufschlag je MW verlangen Sie? (c) Nennen Sie drei Gründe, warum der Jahresvergleich keine Bewertung ersetzt.

**Übung 15.5 (Beurteilen).** Ein Entwickler bewirbt R2 (Raum Stuttgart, Mittelspannung, Inbetriebnahme 01.07.2027) mit Zusatzsegmenten: Momentanreserve Premium in beiden Richtungen mit 10 MW, 250 k€/a ab 2028; „Nutzen statt Abregeln“ 40 k€/a; Kapazitätsmarkt ab 2028 mit 60 k€/MW/a neben einem 80-%-Toll. (a) Prüfen Sie jede Position mit Tabelle 15.3; berechnen Sie die Obergrenze der Momentanreserve. (b) Was muss bis wann vorliegen, damit die Momentanreserve als Festpreisbaustein zählt? (c) Welche Klausel braucht der Toll-Vertrag für den Kapazitätsmarkt? (d) Entscheiden Sie in höchstens fünf Sätzen: Basisfall, Upside oder streichen.

**Übung 15.6 (Entwerfen und Bewerten).** R3 mit 20 MWh soll in den Musterfonds R4. Zur Wahl stehen: (A) merchant als Mischspeicher; (B) PV-PPA pay-as-produced zu 45 €/MWh, Speicher merchant; (C) entbündelt mit PV-PPA und Toll über 10 MW zu 105 k€/MW/a; (D) Hybrid-PPA mit Profil als Grünstromspeicher. (a) Stellen Sie mit Abbildung 15.2 und Tabelle 15.6 Eigentümerwert 2025 und 2025/26, Opportunitätskosten und kontrahierten Anteil gegenüber (2025/26: Marktwert der Bandmenge 106,0 €/MWh, Vertragsmenge des PV-PPA 15.672 MWh). (b) Bewerten Sie die Varianten nach Finanzierbarkeit (Tabelle 15.5, A-033, A-034) und Risiko. Gegen welchen Erlös bemessen Sie einen Floor für R3, welches Basisrisiko bleibt, und was folgt für die Bank? (c) Entwerfen Sie eine Strategie, auch kombiniert, begründen Sie sie in höchstens acht Sätzen und nennen Sie Informationen und Fachleute, die Sie vor Unterzeichnung brauchen. Übertragen Sie Ihre Strategie in zwei Sätzen auf R2 (Toll-Anteil, Energieanteil, Momentanreserve).

Die Lösungen stehen im Anhang A unter Kapitel 15.

## Quellen und Stand {.unnumbered}

Qualität nach dem Quellenregister: A = Primärquelle, B = anerkannte Sekundärquelle, C = Fachmedium oder Anbieter.

**PPA-Markt und Verträge:** [VR3-01] ESS News, Pexapark-Index Juli 2026 (24.08.2026; C) · [VR3-02] PV Tech, Pexapark (04.11.2025; C) · [VR3-03] PV Tech, LevelTen Q2 2026 (23.07.2026; C) · [VR3-04] LevelTen, Hybrid-PPAs (23.07.2026; B) · [VR3-06] ESS News, Zelestra–Salzgitter (16.09.2026; C) · [VR3-07] ESS News, Brüssow (06.07.2026; C) · [VR3-08] pv magazine, MaxSolar–DB Energie (06.08.2026; C) · [K05M-06] ESS News, Pexapark-Volumen (08.07.2026; C) · [K05M-08] enspired, Route-to-Market (15.07.2026; C) · [K05M-10] Next Kraftwerke, Toll SMAREG 12 (23.02.2026; C) · [K06M-02] Modo, Investment Outlook (16.03.2026; B) · [K20F-04] ESS News, Finanzierung Standalone und Co-Location (01.04.2026; C) · [K20F-08] Modo, Finanzierungsbericht 2025 (11.03.2026; B).

**Marktwerte und Marktdaten:** [K15M-01] ÜNB, Marktwertübersicht (A) · [VR3-29] DGS, Jahresmarktwert Solar 2025 (15.01.2026; B) · [M1D-01 bis M1D-04] energy-charts und regelleistung.net, Snapshot bis 26.09.2026 (A) · [M1Q-02] ÜNB, Ausschreibungs- und Gebotsverfahren (A) · [SYN-01] EZB-Referenzkurs (A).

**Recht und Regulierung:** [W2V-01] § 51 EEG · [W2V-07] § 13k EnWG · [K11O-02] BT-Drs. 21/7866, Regierungsentwurf Netzanschlusspaket (07.09.2026) · [K12R-17, K12R-18] MiSpeL-Festlegung vom 01.10.2026 (Tenor mit Begründung, Anlage 1) · [K12R-02] MiSpeL-Anlage 1, Arbeitsstand 05.08.2026 · [K03R-01] StromVKG · [W0R-10] BNetzA, erster Gebotstermin · [K03M-06] ÜNB, Momentanreserve · [K03M-29] ÜNB, FAQ Momentanreserve v3.1 (27.04.2026) · [K03M-40] ÜNB, Anbieterleitfaden Momentanreserve v1.03 (03.06.2026) · [VR3-32] ÜNB, Umsetzungskonzept § 13k (01.04.2026) · [VR3-23] BNetzA, Innovationsausschreibung 01.05.2026 · [VR3-24] pv magazine, Innovationsausschreibung (26.06.2026; C) · [SYN-17] §§ 14c, 118 Abs. 28 EnWG · [W2V-17] Regierungsentwurf EEG 2027 (07.09.2026) · [K12R-12] Bundestag, Anhörung zum EEG 2027 (05.10.2026) · [K07O-01] ÜNB, Anforderungen am Höchstspannungsnetz (16.12.2024) · [K07O-02] E VDE-AR-N 4120/A1:2026-05 (Entwurf); alle A, soweit nicht anders angegeben.

**Modelle:** M1 Version 2.0.0, Lauf 20260928-stacking (2025 und 2025/26; Werte 2025 und Toll R2 wie im Archivlauf 20260927-stacking), Lauf 20260927-fcr125, Lauf 20260928-kapitel03 (Preisspitzenausgleich); Kapitelzahlen `kapitelzahlen_k12_k15.md` und `kapitelzahlen_k14_k15_20260928.md` (D-027). M2 Version 1.4.0, Lauf M2-20260928-P04 mit Zusatz K05 (Abschnitt 15.7, Rechenbeispiel 15.2; D-028).

**Annahmen und Entscheidungen:** A-001, A-002, A-011, A-015, A-018, A-021, A-024, A-025, A-033 bis A-035, A-038, A-040, A-054; A-M1-07 bis A-M1-09, A-M1-12, A-M1-20 bis A-M1-22, A-M1-25 bis A-M1-31, A-M1-33; A-M2-06, A-M2-15, A-M2-39, A-M2-42; D-021, D-024 bis D-028, D-032, D-048, D-060, D-061, D-064, D-069, D-071; Widerspruch S-W33.

**Stand:** 28.09.2026 (MiSpeL, Netzbildung und EEG 2027: 03.10.2026), Datenstand 27.09.2026, Marktdaten bis Liefertag 26.09.2026. Neu zu prüfen sind PPA- und Toll-Preise, Tag der Bekanntgabe und Umsetzung der MiSpeL, das EEG 2027 nach der Anhörung, Anschlussregeln zur Netzbildung ab 110 kV, der Start des Zielmodells nach § 13k (01.10.2026), Preise, Mengen und Regeln der Momentanreserve, die Reduktionsfaktoren und Ergebnisse des Kapazitätsmarkts und § 14c EnWG.
