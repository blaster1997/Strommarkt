#!/usr/bin/env bash
# Richtet die Satzumgebung ein (idempotent, für Claude Code im Web als Setup-Skript oder SessionStart-Hook).
# Python-Pakete aus 07_build/requirements.txt (Pandoc kommt mit pypandoc_binary, Typst als Python-Paket).
# Die Schriften Caladea und Carlito liegen in 07_build/fonts und brauchen keine Installation.
set -uo pipefail
cd "$(dirname "$0")/.." || exit 0

installieren() {
  python3 -m pip install -q -r "$1" 2>/dev/null \
    || python3 -m pip install -q --break-system-packages -r "$1" 2>/dev/null \
    || python3 -m pip install -q --user -r "$1"
}

if python3 -c "import typst, pypandoc, pymupdf, yaml, docx" 2>/dev/null; then
  echo "Satzumgebung vorhanden."
else
  installieren 07_build/requirements.txt && echo "Satzumgebung eingerichtet."
fi

# Bibliotheken der Rechenmodelle (ab Phase 4), falls schon angelegt
if [ -f 04_models/requirements.txt ]; then
  installieren 04_models/requirements.txt && echo "Modellbibliotheken eingerichtet."
fi
exit 0
