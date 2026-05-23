#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEX_DIR="$ROOT/monograph/tex"

if ! command -v rg >/dev/null 2>&1; then
  echo "rg is required for monograph text audit" >&2
  exit 1
fi

FAIL_PATTERN='(253a|253b|253c|lecture[- ]notes?|QFT lecture|source spine|rewrite how|Draft scaffold|Logical Position|Construction Task|source-note|\\(chapter|section|subsection|subsubsection)\{[^}]*[Nn]ot [Ee]nough|\\(chapter|section|subsection|subsubsection)\{[^}]*[Ww]hat .* [Ii]s [Nn]ot|QFT *= *QM *\+ *locality|QM *\+ *locality|relativity forces field theory|path integral is an integral over all fields|gauge symmetry is a physical symmetry|renormalization is subtracting infinities|simplified definition|physicists.? definitions?|not a universal definition|not part of Definition|not primitive as a pointwise operator|\\b(slogan|slogans|lore|folklore)\\b|hand[- ]wavy|roughly speaking|well[- ]known|standard result|it is known|known theorem|one can show|can be shown|schematic|\\bmiracle\\b|surpris(e|es|ed|ing|ingly)|modern language|not a claim about|not a consequence of|Kallen(--|-|[[:space:]]+)Lehmann)'

set +e
RG_OUTPUT="$(rg -n "$FAIL_PATTERN" "$TEX_DIR" -g '*.tex' 2>&1)"
RG_STATUS=$?
set -e

if [[ "$RG_STATUS" -eq 2 ]]; then
  echo "$RG_OUTPUT" >&2
  echo "Strict monograph text audit pattern failed to compile." >&2
  exit 1
fi

if [[ "$RG_STATUS" -eq 0 ]]; then
  echo "$RG_OUTPUT"
  echo "Reader-facing monograph text failed strict harness audit." >&2
  exit 1
fi

echo "Strict monograph text audit clean."
