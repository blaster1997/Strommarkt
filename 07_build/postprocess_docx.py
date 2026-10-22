#!/usr/bin/env python3
"""Nachbearbeitung der von Pandoc erzeugten DOCX-Datei.

1. Kästen: Absätze zwischen den Marken §§KASTEN-START:<typ>§§ und §§KASTEN-ENDE§§
   (gesetzt vom Lua-Filter) werden in eine einzellige Tabelle mit Farbbalken und
   Hintergrund verschoben. Das bleibt in Word und LibreOffice stabil, auch wenn der
   Kasten Listen oder Tabellen enthält.
2. Datentabellen: einheitliches Tabellenlayout (Kopfzeile dunkelblau, dezente
   Zebrastreifen, horizontale Linien, wiederholte Kopfzeile, keine Zeilentrennung).
3. Seitenumbrüche: Marke §§SEITENUMBRUCH§§ wird zu „Seitenumbruch vor“ am
   folgenden Absatz.

Aufruf: python3 postprocess_docx.py datei.docx [--ausgabe ziel.docx]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

sys.path.insert(0, str(Path(__file__).resolve().parent / "templates"))
from make_reference_docx import (  # noqa: E402
    KASTEN_FARBEN, NAVY, PPR_ORDER, RULE, insert_ordered,
)

TEXT_WIDTH_TWIPS = int((21.0 - 2.5 - 2.3) * 567)
BAND_FILL = "F3F6FA"

TBLPR_ORDER = ["tblStyle", "tblpPr", "tblOverlap", "bidiVisual", "tblStyleRowBandSize",
               "tblStyleColBandSize", "tblW", "jc", "tblCellSpacing", "tblInd", "tblBorders",
               "shd", "tblLayout", "tblCellMar", "tblLook", "tblCaption", "tblDescription"]
TCPR_ORDER = ["cnfStyle", "tcW", "gridSpan", "hMerge", "vMerge", "tcBorders", "shd", "noWrap",
              "tcMar", "textDirection", "tcFitText", "vAlign", "hideMark"]
RPR_ORDER = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike",
             "outline", "shadow", "emboss", "imprint", "noProof", "snapToGrid", "vanish",
             "webHidden", "color", "spacing", "w", "kern", "position", "sz", "szCs", "highlight",
             "u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em", "lang",
             "eastAsianLayout", "specVanish", "oMath"]

BODY_STYLES = {None, "Compact", "BodyText", "FirstParagraph", "Normal"}


def el(tag: str, **attrs):
    node = OxmlElement(tag)
    for key, val in attrs.items():
        node.set(qn(f"w:{key}"), str(val))
    return node


def text_of(node) -> str:
    return "".join(t.text or "" for t in node.iter(qn("w:t")))


def p_style(p) -> str | None:
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        return None
    ps = ppr.find(qn("w:pStyle"))
    return ps.get(qn("w:val")) if ps is not None else None


def set_p_style(p, style_id: str):
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = el("w:pPr")
        p.insert(0, ppr)
    insert_ordered(ppr, el("w:pStyle", val=style_id), PPR_ORDER)


def get_ppr(p):
    ppr = p.find(qn("w:pPr"))
    if ppr is None:
        ppr = el("w:pPr")
        p.insert(0, ppr)
    return ppr


def borders(tag: str, spec: dict):
    node = el(tag)
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        if side in spec:
            val, sz, color = spec[side]
            if val == "nil":
                node.append(el(f"w:{side}", val="nil"))
            else:
                node.append(el(f"w:{side}", val=val, sz=sz, space=0, color=color))
    return node


# ---------------------------------------------------------------------------
# 1. Kästen
# ---------------------------------------------------------------------------
def build_box(typ: str, content: list):
    line, fill = KASTEN_FARBEN.get(typ, KASTEN_FARBEN["merke"])
    tbl = el("w:tbl")
    tblpr = el("w:tblPr")
    tbl.append(tblpr)
    insert_ordered(tblpr, el("w:tblW", w=5000, type="pct"), TBLPR_ORDER)
    insert_ordered(tblpr, borders("w:tblBorders", {
        "top": ("nil", 0, ""), "bottom": ("nil", 0, ""), "right": ("nil", 0, ""),
        "left": ("single", 36, line), "insideH": ("nil", 0, ""), "insideV": ("nil", 0, "")}),
        TBLPR_ORDER)
    insert_ordered(tblpr, el("w:tblLayout", type="fixed"), TBLPR_ORDER)
    mar = el("w:tblCellMar")
    for side, val in (("top", 110), ("left", 200), ("bottom", 70), ("right", 170)):
        mar.append(el(f"w:{side}", w=val, type="dxa"))
    insert_ordered(tblpr, mar, TBLPR_ORDER)
    insert_ordered(tblpr, el("w:tblLook", val="0000", firstRow=0, lastRow=0, firstColumn=0,
                             lastColumn=0, noHBand=1, noVBand=1), TBLPR_ORDER)
    grid = el("w:tblGrid")
    grid.append(el("w:gridCol", w=TEXT_WIDTH_TWIPS))
    tbl.append(grid)
    tr = el("w:tr")
    trpr = el("w:trPr")
    n_par = sum(1 for c in content if c.tag == qn("w:p"))
    if n_par <= 14 and not any(c.tag == qn("w:tbl") for c in content):
        trpr.append(el("w:cantSplit"))
    tr.append(trpr)
    tc = el("w:tc")
    tcpr = el("w:tcPr")
    insert_ordered(tcpr, el("w:tcW", w=5000, type="pct"), TCPR_ORDER)
    insert_ordered(tcpr, borders("w:tcBorders", {
        "top": ("nil", 0, ""), "bottom": ("nil", 0, ""), "right": ("nil", 0, ""),
        "left": ("single", 36, line)}), TCPR_ORDER)
    insert_ordered(tcpr, el("w:shd", val="clear", color="auto", fill=fill), TCPR_ORDER)
    tc.append(tcpr)
    for node in content:
        for p in ([node] if node.tag == qn("w:p") else []):
            if p_style(p) in BODY_STYLES:
                set_p_style(p, "KastenText")
        if node.tag == qn("w:p") and p_style(node) == "KastenTitel":
            for run in node.iter(qn("w:r")):
                rpr = run.find(qn("w:rPr"))
                if rpr is None:
                    rpr = el("w:rPr")
                    run.insert(0, rpr)
                insert_ordered(rpr, el("w:color", val=line), RPR_ORDER)
        tc.append(node)
    if not len(tc) or tc[-1].tag != qn("w:p"):
        tc.append(el("w:p"))
    # letzter Absatz im Kasten ohne Abstand nach
    last_p = [n for n in tc if n.tag == qn("w:p")][-1]
    insert_ordered(get_ppr(last_p), el("w:spacing", after=0), PPR_ORDER)
    tr.append(tc)
    tbl.append(tr)
    return tbl


def spacer_paragraph(pts: float = 6):
    p = el("w:p")
    ppr = el("w:pPr")
    ppr.append(el("w:pStyle", val="Abstand"))
    ppr.append(el("w:spacing", before=0, after=0, line=int(pts * 20), lineRule="exact"))
    p.append(ppr)
    return p


def convert_boxes(body) -> int:
    count = 0
    while True:
        start = None
        for child in body:
            if child.tag == qn("w:p") and text_of(child).startswith("§§KASTEN-START:"):
                start = child
                break
        if start is None:
            return count
        typ = text_of(start).split(":", 1)[1].strip("§")
        content, node = [], start.getnext()
        while node is not None and not (node.tag == qn("w:p")
                                        and text_of(node).startswith("§§KASTEN-ENDE")):
            nxt = node.getnext()
            content.append(node)
            node = nxt
        end = node
        for c in content:
            body.remove(c)
        box = build_box(typ, content)
        start.addprevious(box)
        body.remove(start)
        if end is not None:
            end.addprevious(spacer_paragraph())
            body.remove(end)
        else:
            box.addnext(spacer_paragraph())
        count += 1


# ---------------------------------------------------------------------------
# 2. Datentabellen
# ---------------------------------------------------------------------------
def is_box(tbl) -> bool:
    grid = tbl.find(qn("w:tblGrid"))
    rows = tbl.findall(qn("w:tr"))
    return (len(rows) == 1 and grid is not None and len(grid) == 1
            and tbl.find(".//" + qn("w:tcPr") + "/" + qn("w:shd")) is not None)


CHAR_TWIPS = 88          # mittlere Zeichenbreite Calibri 9 pt (≈ 4,4 pt)
CELL_PAD = 2 * 90 + 40   # linker + rechter Zellrand + Reserve
MAX_TOKEN = 26           # lange Einzelwörter (z. B. URLs) nicht zur Mindestbreite machen


def text_units(word: str) -> float:
    """Geschätzte Breite eines Wortes in Durchschnittszeichen (Großbuchstaben, Ziffern breiter)."""
    units = 0.0
    for ch in word:
        if ch.isupper() or ch in "%&@MW":
            units += 1.3
        elif ch.isdigit():
            units += 1.1
        elif ch in "il.,;:!|'":
            units += 0.6
        else:
            units += 1.0
    return units


def auto_column_widths(tbl, total: int = TEXT_WIDTH_TWIPS) -> None:
    """Spaltenbreiten nach dem Prinzip des HTML-Auto-Layouts setzen.

    Mindestbreite = längstes Wort der Spalte, Wunschbreite = längster Zellinhalt.
    Passt alles, wird proportional zur Wunschbreite gestreckt; sonst erhält jede
    Spalte ihre Mindestbreite und der Rest wird nach (Wunsch − Minimum) verteilt.
    """
    if tbl.find(".//" + qn("w:gridSpan")) is not None:
        return
    rows = tbl.findall(qn("w:tr"))
    if not rows:
        return
    ncols = len(rows[0].findall(qn("w:tc")))
    mins, maxs = [0] * ncols, [0] * ncols
    for row in rows:
        cells = row.findall(qn("w:tc"))
        if len(cells) != ncols:
            return
        for j, tc in enumerate(cells):
            txt = " ".join(text_of(p) for p in tc.iter(qn("w:p"))).strip()
            longest = max((text_units(w) for w in txt.split()), default=1.0) + 1.0
            mins[j] = max(mins[j], min(longest, MAX_TOKEN))
            maxs[j] = max(maxs[j], text_units(txt))
    minw = [m * CHAR_TWIPS + CELL_PAD for m in mins]
    maxw = [max(M * CHAR_TWIPS + CELL_PAD, lo) for M, lo in zip(maxs, minw)]
    if sum(maxw) <= total:
        widths = [w * total / sum(maxw) for w in maxw]
    elif sum(minw) >= total:
        widths = [w * total / sum(minw) for w in minw]
    else:
        extra = total - sum(minw)
        span = [hi - lo for lo, hi in zip(minw, maxw)]
        widths = [lo + extra * d / sum(span) for lo, d in zip(minw, span)]
    widths = [int(round(w)) for w in widths]
    grid = tbl.find(qn("w:tblGrid"))
    new_grid = el("w:tblGrid")
    for w in widths:
        new_grid.append(el("w:gridCol", w=w))
    if grid is not None:
        tbl.replace(grid, new_grid)
    else:
        tbl.find(qn("w:tblPr")).addnext(new_grid)
    tblpr = tbl.find(qn("w:tblPr"))
    insert_ordered(tblpr, el("w:tblW", w=total, type="dxa"), TBLPR_ORDER)
    insert_ordered(tblpr, el("w:tblLayout", type="fixed"), TBLPR_ORDER)
    for row in rows:
        for j, tc in enumerate(row.findall(qn("w:tc"))):
            tcpr = tc.find(qn("w:tcPr"))
            if tcpr is None:
                tcpr = el("w:tcPr")
                tc.insert(0, tcpr)
            insert_ordered(tcpr, el("w:tcW", w=widths[j], type="dxa"), TCPR_ORDER)


def style_table(tbl):
    tblpr = tbl.find(qn("w:tblPr"))
    if tblpr is None:
        tblpr = el("w:tblPr")
        tbl.insert(0, tblpr)
    insert_ordered(tblpr, el("w:tblW", w=5000, type="pct"), TBLPR_ORDER)
    insert_ordered(tblpr, borders("w:tblBorders", {
        "top": ("single", 10, NAVY), "bottom": ("single", 10, NAVY),
        "left": ("nil", 0, ""), "right": ("nil", 0, ""),
        "insideH": ("single", 4, RULE), "insideV": ("nil", 0, "")}), TBLPR_ORDER)
    mar = el("w:tblCellMar")
    for side, val in (("top", 40), ("left", 90), ("bottom", 40), ("right", 90)):
        mar.append(el(f"w:{side}", w=val, type="dxa"))
    insert_ordered(tblpr, mar, TBLPR_ORDER)

    rows = tbl.findall(qn("w:tr"))
    header_rows = [r for r in rows if r.find(qn("w:trPr") + "/" + qn("w:tblHeader")) is not None]
    if not header_rows and rows:
        look = tblpr.find(qn("w:tblLook"))
        if look is not None and look.get(qn("w:firstRow")) in ("1", "true"):
            header_rows = [rows[0]]
    body_index = 0
    for row in rows:
        trpr = row.find(qn("w:trPr"))
        if trpr is None:
            trpr = el("w:trPr")
            row.insert(0, trpr)
        if trpr.find(qn("w:cantSplit")) is None:
            trpr.insert(0, el("w:cantSplit"))
        is_head = row in header_rows
        if is_head and trpr.find(qn("w:tblHeader")) is None:
            trpr.append(el("w:tblHeader"))
        fill = NAVY if is_head else (BAND_FILL if body_index % 2 == 1 else None)
        if not is_head:
            body_index += 1
        for tc in row.findall(qn("w:tc")):
            tcpr = tc.find(qn("w:tcPr"))
            if tcpr is None:
                tcpr = el("w:tcPr")
                tc.insert(0, tcpr)
            if fill:
                insert_ordered(tcpr, el("w:shd", val="clear", color="auto", fill=fill), TCPR_ORDER)
            insert_ordered(tcpr, el("w:vAlign", val="top" if not is_head else "bottom"),
                           TCPR_ORDER)
            for p in tc.iter(qn("w:p")):
                if p_style(p) in BODY_STYLES:
                    set_p_style(p, "TabelleKopf" if is_head else "TabelleText")
                if is_head:
                    for rpr in p.iter(qn("w:rPr")):
                        for col in rpr.findall(qn("w:color")):
                            rpr.remove(col)
    auto_column_widths(tbl)


# ---------------------------------------------------------------------------
# 3. Seitenumbrüche
# ---------------------------------------------------------------------------
def convert_page_breaks(body) -> int:
    count = 0
    markers = [c for c in body if c.tag == qn("w:p") and text_of(c) == "§§SEITENUMBRUCH§§"]
    for m in markers:
        target = m.getnext()
        while target is not None and target.tag == qn("w:p") \
                and text_of(target) == "§§SEITENUMBRUCH§§":
            target = target.getnext()
        if target is not None and target.tag == qn("w:sdt"):
            inner = target.find(".//" + qn("w:p"))
            target = inner if inner is not None else target
        if target is not None and target.tag == qn("w:p"):
            insert_ordered(get_ppr(target), el("w:pageBreakBefore"), PPR_ORDER)
            body.remove(m)
        else:
            # vor Tabellen: winziger Absatz mit hartem Umbruch
            for child in list(m):
                if child.tag != qn("w:pPr"):
                    m.remove(child)
            ppr = get_ppr(m)
            insert_ordered(ppr, el("w:spacing", before=0, after=0, line=20, lineRule="exact"),
                           PPR_ORDER)
            run = el("w:r")
            run.append(el("w:br", type="page"))
            m.append(run)
        count += 1
    return count


def tighten_lists(doc) -> None:
    """Kompaktere Listeneinzüge (0,7 cm je Ebene, 0,5 cm hängend)."""
    try:
        numbering = doc.part.numbering_part.element
    except Exception:
        return
    for lvl in numbering.iter(qn("w:lvl")):
        level = int(lvl.get(qn("w:ilvl"), "0"))
        ppr = lvl.find(qn("w:pPr"))
        if ppr is None:
            ppr = el("w:pPr")
            lvl.append(ppr)
        insert_ordered(ppr, el("w:ind", left=397 * (level + 1), hanging=284), PPR_ORDER)


def space_after_tables(body) -> None:
    """Abstand nach Datentabellen, damit folgende Kästen/Absätze nicht anstoßen."""
    for tbl in [c for c in body if c.tag == qn("w:tbl")]:
        nxt = tbl.getnext()
        if nxt is None or nxt.tag != qn("w:p") or p_style(nxt) != "Abstand":
            tbl.addnext(spacer_paragraph(8))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("docx", type=Path)
    ap.add_argument("--ausgabe", type=Path)
    args = ap.parse_args()
    doc = Document(str(args.docx))
    body = doc.element.body
    n_pb = convert_page_breaks(body)
    n_tab = 0
    for tbl in list(body.iter(qn("w:tbl"))):
        if not is_box(tbl):
            style_table(tbl)
            n_tab += 1
    space_after_tables(body)
    n_box = convert_boxes(body)
    tighten_lists(doc)
    doc.save(str(args.ausgabe or args.docx))
    print(f"Nachbearbeitung: {n_box} Kästen, {n_tab} Tabellen, {n_pb} Seitenumbrüche")


if __name__ == "__main__":
    main()
