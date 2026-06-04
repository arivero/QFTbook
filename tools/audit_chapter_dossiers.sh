#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DOSSIER_DIR="$ROOT/planning/chapter_dossiers"

if ! command -v rg >/dev/null 2>&1; then
  echo "rg is required for chapter dossier metadata audit" >&2
  exit 1
fi

SOURCE_PATTERN='(Source Position|Source Placement|Source Spine|Primary Source Anchors|Logical Role|Scope)'
SYMBOL_PATTERN='(Notation Inventory|Symbols|Symbol Inventory|Definitions and Symbols|Definitions And Results|Construction Task)'
CLAIM_PATTERN='(Claim Ledger|Claims Established|Claims To Establish|Claims to Derive|Claims To Verify)'
FIGURE_PATTERN='(Figure Ledger|Figure Requirements|Figures|Figure And Render Checks)'

failed=0

check_heading_group() {
  local file="$1"
  local label="$2"
  local pattern="$3"

  if ! rg -q "^## ${pattern}$" "$file"; then
    echo "$file: missing ${label} metadata heading" >&2
    failed=1
  fi
}

check_forbidden_literal() {
  local file="$1"
  local label="$2"
  local needle="$3"
  local matches

  if [[ -f "$file" ]] && matches="$(rg -nF "$needle" "$file")"; then
    echo "$file: stale ${label}" >&2
    echo "$matches" >&2
    failed=1
  fi
}

while IFS= read -r file; do
  base="$(basename "$file")"
  case "$base" in
    README.md|*_initial_audit.md)
      continue
      ;;
  esac

  if ! rg -q '^# ' "$file"; then
    echo "$file: missing top-level title" >&2
    failed=1
  fi

  check_heading_group "$file" "source/logical-position" "$SOURCE_PATTERN"
  check_heading_group "$file" "symbol/definition" "$SYMBOL_PATTERN"
  check_heading_group "$file" "claim" "$CLAIM_PATTERN"
  check_heading_group "$file" "figure" "$FIGURE_PATTERN"
done < <(find "$DOSSIER_DIR" -type f -name '*.md' | sort)

CONFINEMENT_DOSSIER="$DOSSIER_DIR/volume_ix/chapter04_confinement_screening_oblique_confinement.md"
check_forbidden_literal \
  "$CONFINEMENT_DOSSIER" \
  "continuum-confinement criterion phrase from superseded #757/#765 scope" \
  "converts screening, clustering, endpoint, and condensate data into positive"
check_forbidden_literal \
  "$CONFINEMENT_DOSSIER" \
  "continuum-confinement premise from superseded #757/#765 scope" \
  "infrared clustering/static spectral control"

if [[ "$failed" -ne 0 ]]; then
  echo "Chapter dossier metadata audit failed." >&2
  exit 1
fi

echo "Chapter dossier metadata audit clean."
