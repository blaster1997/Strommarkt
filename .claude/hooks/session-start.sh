#!/bin/bash
# SessionStart-Hook (nur Claude Code im Web): richtet die Satzumgebung ein (Pandoc, Typst, PyMuPDF, PyYAML,
# python-docx über 07_build/einrichten.sh). Idempotent; ohne Rückfrage; bricht die Sitzung nie ab.
set -uo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "${CLAUDE_PROJECT_DIR:-$(pwd)}" || exit 0
if [ -f 07_build/einrichten.sh ]; then
  bash 07_build/einrichten.sh || echo "Hinweis: Einrichtung der Satzumgebung fehlgeschlagen; bitte bash 07_build/einrichten.sh ausführen."
fi
exit 0
