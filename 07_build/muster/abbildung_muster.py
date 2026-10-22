#!/usr/bin/env python3
"""Formatmuster für Abbildungen: Buchfarben, Schrift Carlito, deutsche Zahlenformate, Achsen mit Einheit,
kein Titel und keine Quellenzeile im Bild (beides setzt der Buchsatz). Die Werte sind fiktiv.

Aufruf: python3 07_build/muster/abbildung_muster.py  → 07_build/muster/abb_muster_meritorder.png
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

HERE = Path(__file__).resolve().parent
SCHRIFTEN = HERE.parent / "fonts"
for f in SCHRIFTEN.glob("Carlito-*.ttf"):
    font_manager.fontManager.addfont(str(f))

# Buchfarben (CLAUDE.md § 5): Dunkelblau, Blau, Grün, Orange, Ocker, Grau
NAVY, BLAU, GRUEN, ORANGE, OCKER, GRAU = "#1B365D", "#2A7AB0", "#2E7D6B", "#C55A11", "#B7791F", "#5F6B7A"

plt.rcParams.update({"font.family": "Carlito", "font.size": 9, "axes.edgecolor": GRAU, "axes.labelcolor": "#1A1A1A",
                     "xtick.color": GRAU, "ytick.color": GRAU, "axes.spines.top": False, "axes.spines.right": False})


def de(x, _pos=None, nachkomma=0):
    s = f"{x:,.{nachkomma}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


# Fiktive Angebotskurve: (Technologie, Leistung in GW, Grenzkosten in €/MWh, Farbe)
bloecke = [("Wind und Solar", 30, 0, GRUEN), ("Biomasse und Wasser", 8, 20, BLAU), ("Braunkohle", 12, 55, GRAU),
           ("Steinkohle", 8, 80, NAVY), ("Gas (GuD)", 15, 90, OCKER), ("Gas (Gasturbine)", 6, 140, ORANGE)]
nachfrage = 62  # GW, fiktiv

fig, ax = plt.subplots(figsize=(16 / 2.54, 7.5 / 2.54), dpi=300)
x = 0
for name, leistung, kosten, farbe in bloecke:
    ax.bar(x, kosten if kosten > 0 else 1.5, width=leistung, align="edge", color=farbe, edgecolor="white",
           linewidth=0.6, label=name)
    x += leistung
ax.axvline(nachfrage, color=ORANGE, linewidth=1.4, linestyle="--")
ax.text(nachfrage + 0.8, 150, "Nachfrage (fiktiv)", color=ORANGE, va="top")
ax.axhline(90, xmax=nachfrage / (x + 2), color=NAVY, linewidth=0.9, linestyle=":")
ax.text(1, 93, "Markträumender Preis 90 €/MWh (fiktiv)", color=NAVY)
ax.set_xlim(0, x + 2)
ax.set_ylim(0, 160)
ax.set_xlabel("Kumulierte Leistung in GW")
ax.set_ylabel("Grenzkosten in €/MWh")
ax.xaxis.set_major_formatter(FuncFormatter(de))
ax.yaxis.set_major_formatter(FuncFormatter(de))
ax.grid(axis="y", color="#C9D3E0", linewidth=0.6)
ax.set_axisbelow(True)
ax.legend(frameon=False, loc="upper left", ncol=2, fontsize=7.5, bbox_to_anchor=(0.0, 0.88))
fig.tight_layout()
fig.savefig(HERE / "abb_muster_meritorder.png")
print(HERE / "abb_muster_meritorder.png")
