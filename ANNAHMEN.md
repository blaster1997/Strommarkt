# Annahmen

Typ: F = auf Fakt gestützt (Quelle), S = Schätzung (Herleitung), A = Annahme (Begründung). Low, Mid und High
bezeichnen niedrigen, mittleren und hohen Zahlenwert. IDs: A-001 bis A-099 übergreifend (u. a. Parameter der
Referenzfälle R1–R6), A-M1 bis A-M4 Modellannahmen, A-Kxx-yy Annahmen einzelner Kapitel. Jede Annahme mit Einheit,
Bezugsjahr, nominal oder real und, wo nötig, Auflösung und Gebotszone. Nur der Orchestrator pflegt diese Datei;
Agenten schlagen Annahmen in ihren Notizen oder in `04_models/<modell>/ANNAHMEN_VORSCHLAG.md` vor.

## Übergreifende Annahmen

| ID | Annahme | Wert | Typ | Herkunft / Begründung | Status | verwendet in |
|---|---|---|---|---|---|---|
| A-001 | R1a Haushalt: Jahresverbrauch, Netzebene, Messung | 3.500 kWh/a; Niederspannung; Standardlastprofil, konventionelle Messung | F | Abnahmefall Haushaltskunde, Monitoringbericht 2025, S. 164 [P1S-01] | vorgeschlagen (D-005) | Kap. 1, 2, 23, 25, 26; M4 |
| A-002 | R1 Lastprofil | Standardlastprofil Haushalt des BDEW in der geltenden Fassung | A | gilt für Kunden ohne Leistungsmessung; Fassung in Welle 1 prüfen | vorgeschlagen (D-005) | M4 |
| A-003 | R1b Zusatzverbrauch Wärmepumpe | 4.000 kWh/a über eigenen Zählpunkt, steuerbar nach § 14a EnWG | S | rund 14.000 kWh Wärme ÷ Jahresarbeitszahl 3,5 (Vorabrecherche P1-E); in Welle 1 belegen; Vergleichswert Heizstrom 7.500 kWh/a [P1S-01, S. 181] | vorgeschlagen (D-005) | Kap. 2, 15, 25, 26; M4 |
| A-004 | R1c Zusatzverbrauch E-Auto | 2.500 kWh/a, Wallbox 11 kW; Gesamtverbrauch R1c rund 10.000 kWh/a | S | 14.000 km/a × 18 kWh/100 km; über 6.000 kWh/a Pflichtfall iMSys [P1E-21]; in Welle 1 belegen | vorgeschlagen (D-005) | Kap. 15, 25, 26; M4 |
| A-005 | R1 Netzgebiet | Mittelwerte des Monitoringberichts; Sensitivität Netzgebiet Nord und Süd | A | Übertragbarkeit der Rechnung; regionale Spreizung als Sensitivität | vorgeschlagen (D-005) | Kap. 23, 25; M4 |
| A-006 | R1 Tarife | Grundversorgung, Festpreis 12 Monate, dynamischer Tarif (R1c) | A | Grundformen nach § 36 und § 41a EnWG | vorgeschlagen (D-005) | Kap. 26; M4 |
| A-007 | R1/R2 Bezugsjahre | Ist 2025 und 2026, Planjahr 2027 | A | Umlagen und Netzentgelte 2027 erscheinen bis Ende 2026 | vorgeschlagen (D-005) | M4 |
| A-010 | R2 Industriekunde: Verbrauch, Leistung, Netzebene | 24 GWh/a; Jahreshöchstlast 4.000 kW; 6.000 h/a; Mittelspannung (10/20 kV); RLM | F | Abnahmefall Industriekunde, Monitoringbericht 2025, S. 164–165 [P1S-01] | vorgeschlagen (D-005) | Kap. 3, 7, 23, 25, 27; M3, M4 |
| A-011 | R2 Branche und Entlastungen | produzierendes Gewerbe, Stromsteuerentlastung § 9b StromStG; Basis ohne BesAR; Variante stromkostenintensiv mit Industriestrompreis | A | zeigt Wirkung der Entlastungen [P1E-08] | vorgeschlagen (D-005) | Kap. 25; M4 |
| A-012 | R2 Lastgang | synthetisches Profil: Zweischichtbetrieb werktags mit Grundlast, kalibriert auf 6.000 h | A | realer Lastgang nicht öffentlich; Profil in M3 dokumentiert | vorgeschlagen (D-005) | M3 |
| A-013 | R2 Beschaffung | Tranchen Base/Peak über drei Jahre vor Lieferung, Rest Day-Ahead und Intraday; Vergleich Festpreis-Vollversorgung | A | typische Industriebeschaffung; Rückrechnung 2021–2026 | vorgeschlagen (D-005) | Kap. 7, 27; M3 |
| A-014 | R2/R4 PPA | Abnahme der Erzeugung von R4 für zehn Jahre, Pay-as-produced oder Baseload | A | Verbraucher- und Erzeugersicht im selben Vertrag | vorgeschlagen (D-005) | Kap. 10; M2, M3 |
| A-015 | R2 Netzentgelt | Leistungs- und Arbeitspreis über 2.500 h; keine Bandlastsonderform (Schwelle 7.000 h nicht erreicht) | A | Schwelle in Welle 0 prüfen | vorgeschlagen (D-005) | Kap. 23; M4 |
| A-020 | R3 Windpark: Größe und Standort | 30 MW (5 × 6 MW), Niedersachsen, Regelzone TenneT, Hochspannung | A | übliche Anlagengröße (MaStR in Welle 1 prüfen); Bezug zu Redispatch, § 13k, Gebotszone | vorgeschlagen (D-005) | Kap. 2–5, 8, 9, 12, 14, 18–22, 24, 28, 29; M2 |
| A-021 | R3 Standortgüte und Erzeugung | 80 % des Referenzstandorts; 2.600 Volllaststunden; 78 GWh/a | S | mittlerer Binnenlandstandort; Volllaststunden in Welle 1 belegen | vorgeschlagen (D-005) | M2 |
| A-022 | R3 Zuschlag | Gebotstermin 01.08.2026; Zuschlagswert 4,79 ct/kWh (mengengewichtetes Mittel); anzulegender Wert mit Korrekturfaktor | F | BNetzA-Ergebnis [P1M-11, Suchauszug]; Korrekturfaktor in Welle 0 am Normtext | vorgeschlagen (D-005) | Kap. 19, 20; M2 |
| A-023 | R3 Inbetriebnahme und Rechtsrahmen | Inbetriebnahme 2028; 20 Jahre Förderung nach dem Recht des Zuschlags; Variante Differenzvertrag EEG 2027 | A | Übergangsrecht EEG 2027 in Welle 0 prüfen | vorgeschlagen (D-005) | Kap. 18, 21; M2 |
| A-024 | R3 Vermarktung | Direktvermarktung mit Marktprämie; Vermarktungsentgelt und Prognosegüte als Bandbreite (Welle 1) | A | Anbieterangaben Qualität C, deshalb Bandbreite | vorgeschlagen (D-005) | Kap. 20; M2 |
| A-025 | R3 Abregelung | Anteil Ausfallarbeit durch Redispatch aus BNetzA-Daten der Region | S | Herleitung in Welle 2 | vorgeschlagen (D-005) | Kap. 14; M2 |
| A-030 | R4 Solarpark: Größe und Standort | 20 MWp Modulleistung, 17 MW Wechselrichterleistung, Freifläche Süddeutschland | A | übliche PPA-Anlage; DC/AC-Verhältnis in Welle 1 prüfen | vorgeschlagen (D-005) | Kap. 5, 9, 10, 12, 20, 29; M2 |
| A-031 | R4 Erzeugung | 1.050 kWh/kWp; 21 GWh/a | S | Abgleich mit realen Einspeisereihen in M2 | vorgeschlagen (D-005) | M2 |
| A-032 | R4 Förderung | keine; sonstige Direktvermarktung; Herkunftsnachweise an Abnehmer | A | Gegenmodell zu R3 | vorgeschlagen (D-005) | Kap. 10; M2 |
| A-033 | R4 PPA | zehn Jahre mit R2; Pay-as-produced Festpreis oder Baseload 2,4 MW (21 GWh ÷ 8.760 h) | A | Profil-, Volumen- und Kannibalisierungsrisiko | vorgeschlagen (D-005) | Kap. 10; M2 |
| A-034 | R4 Betrieb | Inbetriebnahme 2027; Abregelung bei negativen Preisen; Variante mit Speicher am selben Anschluss | A | Bezug zum Vorprojekt (PV und Speicher) | vorgeschlagen (D-005) | Kap. 10, 20; M2 |
| A-040 | R5a GuD-Bestand | 450 MW_el; Wirkungsgrad 57 % (Heizwert); ohne Wärmeauskopplung; Süddeutschland | A | Spark Spread, Absicherung, Regelreserve, Netzreserve; Wirkungsgrad in Welle 1 belegen | vorgeschlagen (D-005) | Kap. 5–7, 11, 13, 16, 27, 29, 30; M1, M3 |
| A-041 | R5b Neubau Gasturbine | 300 MW; Wirkungsgrad 37 % (Heizwert); wasserstofffähig; Gebot im Kapazitätsmechanismus | A | 37 % nach StromVKG-Referenzanlage (Herkunft B-14; Welle 0 prüfen) | vorgeschlagen (D-005) | Kap. 16, 17; M1 |
| A-042 | R5 Brennstoff und CO₂ | Gas THE; EUA; Emissionsfaktor Erdgas nach StromVKG Anlage 7 | F | Faktor in Welle 0 am Normtext prüfen | vorgeschlagen (D-005) | M1, M3 |
| A-043 | R5 Absicherung und Regelreserve | Clean Spark Spread des Folgejahres in Tranchen; 50 MW aFRR | A | verbindet Kap. 7, 13, 27 | vorgeschlagen (D-005) | M1, M3 |
| A-050 | R6 Batteriespeicher: Größe und Anschluss | 50 MW; 100 MWh nutzbar (2 h); eigenständig; 110 kV; Niedersachsen | A | typische Größe aktueller Großprojekte; Alternative 10 MW/20 MWh wie Vorprojekt (Rückfrage 5) | vorgeschlagen (D-005) | Kap. 1, 2, 8, 9, 13–15, 17, 22, 23, 29; M1 |
| A-051 | R6 Inbetriebnahme und Netz | 2027; Netzentgeltbefreiung § 118 Abs. 6 EnWG; Baukostenzuschuss nach Preisblatt | A | Stand in Welle 0 prüfen; Anschluss an BESS-Kap. 11 | vorgeschlagen (D-005) | Kap. 22, 23 |
| A-052 | R6 Technik | Wirkungsgrad, Alterung, Zyklen aus dem Vorprojekt nach Prüfung | A | keine Neuberechnung, wenn belegt | vorgeschlagen (D-005) | M1 |
| A-053 | R6 Erlösquellen | Day-Ahead, Intraday, FCR, aFRR, technologieoffene Kapazitätsauktion 2027, Momentanreserve | A | Erlösstapel und Grenzen | vorgeschlagen (D-005) | Kap. 13, 15, 17, 29; M1 |
