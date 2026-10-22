#!/usr/bin/python3
"""DOCX → PDF über LibreOffice (UNO), inklusive Aktualisierung aller Verzeichnisse.

Ein einfaches `soffice --convert-to pdf` aktualisiert das Inhaltsverzeichnis nicht.
Dieses Skript startet LibreOffice headless, öffnet die DOCX-Datei, aktualisiert
Verzeichnisse und Felder (zweimal, da sich Seitenzahlen verschieben können) und
exportiert ein PDF mit Lesezeichen und eingebetteten Schriften.

Aufruf (System-Python mit UNO-Bindung): /usr/bin/python3 pdf_export.py in.docx out.pdf
"""

from __future__ import annotations

import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time

import uno  # type: ignore
from com.sun.star.beans import PropertyValue  # type: ignore


def prop(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def export(docx: str, pdf: str) -> None:
    port = free_port()
    profile = tempfile.mkdtemp(prefix="lo_profile_")
    soffice = shutil.which("soffice") or "/usr/bin/soffice"
    proc = subprocess.Popen([
        soffice, "--headless", "--invisible", "--nologo", "--norestore", "--nodefault",
        f"--accept=socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext",
        f"-env:UserInstallation=file://{profile}",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        local = uno.getComponentContext()
        resolver = local.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local)
        ctx = None
        for _ in range(120):
            try:
                ctx = resolver.resolve(
                    f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext")
                break
            except Exception:
                time.sleep(0.5)
        if ctx is None:
            raise RuntimeError("LibreOffice nicht erreichbar")
        desktop = ctx.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)
        doc = desktop.loadComponentFromURL(
            uno.systemPathToFileUrl(os.path.abspath(docx)), "_blank", 0,
            (prop("Hidden", True),))
        indexes = doc.getDocumentIndexes()
        for _ in range(2):
            for i in range(indexes.getCount()):
                indexes.getByIndex(i).update()
            doc.getTextFields().refresh()
        filter_data = uno.Any("[]com.sun.star.beans.PropertyValue", tuple([
            prop("ExportBookmarks", True),
            prop("EmbedStandardFonts", True),
            prop("UseTaggedPDF", True),
            prop("ExportNotes", False),
            prop("ReduceImageResolution", False),
            prop("Quality", 95),
            prop("InitialView", 1),  # Lesezeichenleiste anzeigen
        ]))
        fd = PropertyValue()
        fd.Name = "FilterData"
        fd.Value = filter_data
        args = uno.Any("[]com.sun.star.beans.PropertyValue",
                       (prop("FilterName", "writer_pdf_Export"), fd))
        uno.invoke(doc, "storeToURL", (uno.systemPathToFileUrl(os.path.abspath(pdf)), args))
        doc.close(True)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=20)
        except subprocess.TimeoutExpired:
            proc.kill()
        shutil.rmtree(profile, ignore_errors=True)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Aufruf: pdf_export.py eingabe.docx ausgabe.pdf")
    export(sys.argv[1], sys.argv[2])
    print(f"PDF geschrieben: {sys.argv[2]}")
