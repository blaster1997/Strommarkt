#!/usr/bin/env python3
"""Kontaktbögen eines PDFs für die visuelle Layoutprüfung erzeugen.

Jeder Bogen zeigt mehrere Seiten nebeneinander (Standard 3 × 2). Vor jeder Übergabe
eines Lieferobjekts werden die Bögen gesichtet (CLAUDE.md §5).

Aufruf: python3 07_build/preview.py datei.pdf --ziel <ordner> [--spalten 3 --zeilen 2 --dpi 55]
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pymupdf


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pdf", type=Path)
    ap.add_argument("--ziel", type=Path, required=True)
    ap.add_argument("--spalten", type=int, default=3)
    ap.add_argument("--zeilen", type=int, default=2)
    ap.add_argument("--dpi", type=int, default=55)
    args = ap.parse_args()

    src = pymupdf.open(str(args.pdf))
    width, height = src[0].rect.width, src[0].rect.height
    per_sheet = args.spalten * args.zeilen
    args.ziel.mkdir(parents=True, exist_ok=True)
    for sheet_no, start in enumerate(range(0, src.page_count, per_sheet), start=1):
        doc = pymupdf.open()
        page = doc.new_page(width=args.spalten * width, height=args.zeilen * height)
        for i, pno in enumerate(range(start, min(start + per_sheet, src.page_count))):
            col, row = i % args.spalten, i // args.spalten
            rect = pymupdf.Rect(col * width, row * height, (col + 1) * width, (row + 1) * height)
            page.show_pdf_page(rect, src, pno)
            page.draw_rect(rect, color=(0.6, 0.6, 0.6), width=2)
        out = args.ziel / f"{args.pdf.stem}_bogen_{sheet_no:02d}.png"
        page.get_pixmap(dpi=args.dpi).save(str(out))
        print(out)


if __name__ == "__main__":
    main()
