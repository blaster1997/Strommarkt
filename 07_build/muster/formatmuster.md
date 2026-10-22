---
title: "Kapitel 1 · Formatmuster"
subtitle: "Der Strommarkt in Deutschland – Aufbau und Satz eines Kapitels (alle Zahlen fiktiv)"
date: "TT.MM.JJJJ"
kopfzeile-rechts: "Kapitel 1 · Stand TT.MM.JJJJ"
kapitel-start: 1
nummerierung: kapitelweise
inhaltsverzeichnis: true
toc-tiefe: 2
deckblatt-hinweis: "Formatmuster mit fiktiven Zahlen. Keine Rechts-, Steuer- oder Anlageberatung."
---

# Formatmuster: Aufbau und Satz eines Kapitels

> [!NOTE]
> **Lernziele:** Nach diesem Muster können Sie
>
> - die neun Bausteine eines Kapitels in der vorgeschriebenen Reihenfolge anordnen,
> - Kästen, Tabellen, Abbildungen und Formeln so auszeichnen, dass der Satz sie richtig setzt,
> - Belege, Annahmen, Lücken und Modellwerte im Text eindeutig kennzeichnen.

Dieses Muster zeigt jedes Satzelement des Lehrbuchs einmal. **Alle Zahlen sind fiktiv** und dienen nur der
Darstellung; sie dürfen nicht in Kapitel übernommen werden. Die verbindlichen Regeln stehen in `CLAUDE.md` § 5
und im Leitfaden `06_review/LEITFADEN_KAPITEL.md`.

## Warum das für Investoren und Marktteilnehmer zählt {.unnumbered}

Hier stehen drei bis fünf Sätze, warum das Kapitel für Investoren, Erzeuger, Händler, Lieferanten und große
Verbraucher wichtig ist. Danach folgt der Marktkompass: Er nennt, welche Ebenen des Stromsystems das Kapitel
berührt und welche Rolle sie darin spielen.

| Ebene | Rolle in Kapitel 1 |
|---|---|
| Physik und Technik | Leistung und Energie, Gleichgewicht von Erzeugung und Verbrauch |
| Großhandel | Preisbildung über die Merit Order am Day-Ahead-Markt |
| System und Netz | Engpässe, Ausgleichsenergie |
| Förderung | Marktprämie für erneuerbare Anlagen |
| Regulierung | Rechtsgrundlagen und Festlegungen |
| Endkundenpreis | Beschaffungskosten als Preisbestandteil |

Table: Marktkompass Kapitel 1

Quelle: eigene Darstellung (Stand TT.MM.JJJJ).

## Fließtext, Belege und Kennzeichnung

Der Kerninhalt steht überwiegend in Fließtext. Jede Zahl trägt Einheit, Stand und Beleg: Der mittlere
Day-Ahead-Preis des Musterjahres lag bei 85,0 €/MWh [MU-01] (fiktiv). Belege stehen als Quellenkürzel in eckigen
Klammern; das Kürzel verweist auf `sources/SOURCES.csv` und im Buch auf das Quellenverzeichnis. Annahmen tragen
ihre ID aus `ANNAHMEN.md`, etwa ein Wirkungsgrad von 55 % (A-001, fiktiv). Schätzungen nennen ihre Herleitung
(eigene Rechnung). Einordnungen, die kein Befund sind, heißen „Einordnung“ oder „Einschätzung“.

Leistung und Energie werden nie verwechselt: Ein Kraftwerk mit 100 MW Leistung erzeugt in einer Viertelstunde
25 MWh. Preise nennen Gebotszone, Lieferperiode und Auflösung (Stunde oder Viertelstunde). Fehlt ein belastbarer
Beleg, wird nichts erfunden, sondern die Lücke benannt [LÜCKE: Preisgrenzen der Intraday-Auktionen, Stand 2026].
Fehlt ein Modellwert, steht ein Platzhalter mit genauer Größe [MODELL: M1 – mittlerer Day-Ahead-Preis in €/MWh,
Szenario Basis, Jahr 2030]. Normen werden vollständig zitiert, etwa § 51 Abs. 1 EEG; „S.“ steht nur für Seite.
Beträge in fremder Währung tragen Kurs und Datum, das Dollarzeichen ist maskiert: US-\$ 3,0/MMBtu (fiktiv).

> [!DEFINITION]
> **Definition:** Ein Kasten dieser Art erklärt einen Fachbegriff beim ersten Auftreten. Der Begriff wandert als
> Vorschlag in `06_review/<Kxx>_glossar_vorschlag.md`; das Glossar pflegt der Orchestrator.

### Formeln

Formeln stehen in LaTeX-Syntax, Variablen werden direkt danach erklärt, das Dezimalkomma wird als `{,}` gesetzt:

$$GK = \frac{p_{\text{Gas}} + p_{\text{CO}_2} \cdot e}{\eta}$$

mit $GK$ als Grenzkosten der Stromerzeugung in €/MWh, $p_{\text{Gas}}$ als Gaspreis in €/MWh Brennstoff,
$p_{\text{CO}_2}$ als CO₂-Preis in €/t, $e$ als Emissionsfaktor in t CO₂ je MWh Brennstoff und $\eta$ als
elektrischem Wirkungsgrad. Für ein fiktives Gaskraftwerk mit $\eta = 0{,}55$ gilt
$GK = (35 + 70 \cdot 0{,}2) / 0{,}55 \approx 89{,}1$ €/MWh.

### Tabellen

Tabellen dienen Vergleichen und Zahlen. Die Beschriftung steht unter der Tabelle mit `Table:`, darunter die
Quellenzeile; die Nummer („Tabelle 1.2“) setzt der Satz.

| Technologie | Leistung (GW, fiktiv) | Grenzkosten (€/MWh, fiktiv) |
|---|---:|---:|
| Wind und Solar | 30 | 0 |
| Biomasse und Wasser | 8 | 20 |
| Braunkohle | 12 | 55 |
| Steinkohle | 8 | 80 |
| Gas (GuD) | 15 | 90 |
| Gas (Gasturbine) | 6 | 140 |

Table: Angebotskurve eines fiktiven Marktes

Quelle: Formatmuster, fiktive Werte (Stand TT.MM.JJJJ).

### Abbildungen

Abbildungen entstehen mit einem Skript in `05_figures/<Kxx>/` (hier `07_build/muster/abbildung_muster.py`). Im
Bild stehen weder Titel noch Quelle; Beschriftung und Quellenzeile setzt der Satz.

![Merit Order eines fiktiven Marktes: Die teuerste noch benötigte Anlage bestimmt den Preis](07_build/muster/abb_muster_meritorder.png)

Quelle: Formatmuster, fiktive Werte (Stand TT.MM.JJJJ).

> [!STAND]
> **Stand:** Regulatorisch bewegliche Inhalte erhalten einen Kasten „Stand“ mit Datum der Prüfung, Fundstelle,
> Status (Entwurf, beschlossen, in Kraft ab) und dem nächsten erwarteten Ereignis, etwa einer Ausschreibungsrunde
> oder einem Gesetzentwurf im Verfahren. Vor Verwendung prüfen.

> [!IMPORTANT]
> **Hier Fachleute einbinden:** Stellen, an denen ein Rechtsanwalt für Energierecht, ein Steuerberater, ein
> Wirtschaftsprüfer oder ein Fachanwalt für Bank- und Kapitalmarktrecht nötig ist, stehen in diesem Kasten. Das
> Buch ist keine Rechts-, Steuer- oder Anlageberatung.

## Rechenbeispiel am Referenzfall {.unnumbered}

> [!BEISPIEL]
> **Rechenbeispiel R5: Grenzkosten und Clean Spark Spread (fiktiv)**
>
> *Ziel:* prüfen, ob das Gaskraftwerk des Referenzfalls R5 in einer Stunde Strom erzeugt. Alle Werte fiktiv,
> Lauf-ID des Modells: [Lauf M1-JJJJMMTT-XX].
>
> *Schritt 1 – Eingaben:* Gaspreis 35 €/MWh, CO₂-Preis 70 €/t, Emissionsfaktor 0,2 t/MWh, Wirkungsgrad 55 %
> (A-001, fiktiv); Day-Ahead-Preis 95 €/MWh.
>
> *Schritt 2 – Rechnung:* $GK = (35 + 70 \cdot 0{,}2) / 0{,}55 = 89{,}1$ €/MWh; Clean Spark Spread
> $95 - 89{,}1 = 5{,}9$ €/MWh.
>
> *Schritt 3 – Ergebnis:* Der Spread ist positiv; das Kraftwerk erzeugt, solange Anfahrkosten und Mindestlaufzeit
> den Deckungsbeitrag nicht übersteigen (eigene Rechnung).

## Praxis-Check und typische Fehler {.unnumbered}

> [!TIP]
> **Praxis-Check:** Checklisten und Prüffragen für Datenreihen, Verträge, Gutachten und Prognosen stehen als
> Aufzählung:
>
> - Welche Gebotszone, Zeitzone (MEZ oder MESZ), Lieferperiode und Auflösung hat eine Preisreihe?
> - Ist ein Preis ein Base-, Peak- oder Profilpreis, und für welchen Zeitraum gilt er?

> [!WARNING]
> **Typische Fehler:**
>
> - Leistung (MW) und Energie (MWh) verwechseln.
> - Stunden- und Viertelstundenwerte ohne Umrechnung vergleichen.

## Zusammenfassung {.unnumbered}

Fünf bis acht Kernaussagen in ganzen Sätzen fassen das Kapitel zusammen. Sie wiederholen keine Zahlen ohne
Beleg.

## Übungen {.unnumbered}

1. *Rechnen.* Berechnen Sie die Grenzkosten des fiktiven Gaskraftwerks bei einem CO₂-Preis von 100 €/t.
2. *Bewerten.* Beurteilen Sie, welche Anlage in der fiktiven Merit Order den Preis setzt, wenn die Nachfrage auf
   50 GW sinkt.
3. *Entscheiden.* Welche Daten fordern Sie an, bevor Sie einer Preisprognose für das Jahr 2030 folgen?

Die Lösungen stehen im Anhang A unter Kapitel 1.

## Quellen und Stand {.unnumbered}

**Marktdaten:** [MU-01] Formatmuster, fiktive Quelle (Stand TT.MM.JJJJ).

**Recht:** Normen mit Fassung und Datum, Festlegungen mit Aktenzeichen und Datum, Entscheidungen mit Gericht,
Datum und Aktenzeichen.

**Modelle:** M1, Lauf M1-JJJJMMTT-XX (Version x.y.z).

**Annahmen:** A-001 (fiktiv).

**Stand:** TT.MM.JJJJ; Markt- und Rechtsstand TT.MM.JJJJ. Neu zu prüfen sind die Inhalte der Kästen „Stand“.
