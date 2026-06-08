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

manifest_report=""
if ! manifest_report="$(python3 - "$ROOT" <<'PY'
from __future__ import annotations

from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
dossier_dir = root / "planning" / "chapter_dossiers"


def normalize_input(raw: str) -> str:
    path = raw.strip()
    if not path.endswith(".tex"):
        path += ".tex"
    if not path.startswith("monograph/tex/"):
        path = "monograph/tex/" + path
    return path


manifest_paths = sorted((root / "monograph" / "tex" / "volumes").glob("volume_*/volume_*_current.tex"))
manifest_keys: list[str] = []
errors: list[str] = []

for manifest in manifest_paths:
    for lineno, line in enumerate(manifest.read_text().splitlines(), start=1):
        for match in re.finditer(r"\\input\{([^}]+)\}", line):
            key = normalize_input(match.group(1))
            manifest_keys.append(key)
            if not (root / key).is_file():
                rel_manifest = manifest.relative_to(root)
                errors.append(f"{rel_manifest}:{lineno}: missing compiled source {key}")

seen_manifest: dict[str, int] = {}
for key in manifest_keys:
    seen_manifest[key] = seen_manifest.get(key, 0) + 1
for key, count in sorted(seen_manifest.items()):
    if count != 1:
        errors.append(f"compiled manifest source appears {count} times: {key}")

dossier_files = [
    path
    for path in sorted(dossier_dir.rglob("*.md"))
    if path.name != "README.md" and not path.name.endswith("_initial_audit.md")
]

dossier_by_source: dict[str, list[str]] = {}
for dossier in dossier_files:
    rel_dossier = str(dossier.relative_to(root))
    matches = [
        line.split(":", 1)[1].strip()
        for line in dossier.read_text().splitlines()
        if line.startswith("Source-File:")
    ]
    if len(matches) != 1:
        errors.append(f"{rel_dossier}: expected exactly one Source-File metadata line")
        continue
    key = matches[0]
    if not (root / key).is_file():
        errors.append(f"{rel_dossier}: Source-File target does not exist: {key}")
    dossier_by_source.setdefault(key, []).append(rel_dossier)

manifest_set = set(manifest_keys)
dossier_set = set(dossier_by_source)

for key in sorted(manifest_set - dossier_set):
    errors.append(f"missing dossier for compiled source: {key}")
for key in sorted(dossier_set - manifest_set):
    owners = ", ".join(dossier_by_source[key])
    errors.append(f"orphan dossier source key {key}: {owners}")
for key, owners in sorted(dossier_by_source.items()):
    if len(owners) != 1:
        errors.append(f"duplicate dossier source key {key}: {', '.join(owners)}")

matched_count = len(manifest_set & dossier_set)

# Negative-control fixture: simulating deletion of one dossier key must create
# a missing-source failure.  This keeps the bijection check from degrading into
# a count-only report.
if dossier_by_source:
    simulated = dict(dossier_by_source)
    simulated.pop(next(iter(simulated)))
    if not (manifest_set - set(simulated)):
        errors.append("negative-control fixture failed: simulated dossier deletion was not detected")
else:
    errors.append("negative-control fixture failed: no dossiers were available to delete")

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    raise SystemExit(1)

print(
    "Chapter dossier manifest audit clean: "
    f"manifest_count={len(manifest_keys)}, "
    f"dossier_count={len(dossier_files)}, "
    f"matched_count={matched_count}, "
    "deletion_negative_control=passed."
)
PY
)"; then
  failed=1
else
  echo "$manifest_report"
fi

if [[ "$failed" -ne 0 ]]; then
  echo "Chapter dossier metadata audit failed." >&2
  exit 1
fi

echo "Chapter dossier metadata audit clean."
