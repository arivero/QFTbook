#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TEX_DIR="$ROOT/monograph/tex"

cd "$TEX_DIR"
mkdir -p build
BUILD_LOG="$TEX_DIR/build/latexmk.out"
"$ROOT/tools/audit_monograph_text.sh"
latexmk -xelatex -interaction=nonstopmode main.tex 2>&1 | tee "$BUILD_LOG"

FINAL_LOG_ISSUE_PATTERN="(^!|LaTeX Error|Package [A-Za-z]+ Error|Package amsmath Warning: Foreign command|Package hyperref Warning: Token not allowed|Emergency stop|Fatal error|Undefined control sequence|Reference .* undefined|Citation .* undefined|Missing .* inserted|Overfull|Underfull|already defined|multiply defined|xdvipdfmx:warning)"
BUILD_LOG_FATAL_PATTERN="(^!|LaTeX Error|Package [A-Za-z]+ Error|Package amsmath Warning: Foreign command|Package hyperref Warning: Token not allowed|Emergency stop|Fatal error|Undefined control sequence|Missing .* inserted|xdvipdfmx:warning)"

if command -v rg >/dev/null 2>&1; then
  if rg -n "$FINAL_LOG_ISSUE_PATTERN" main.log; then
    echo "Monograph build completed, but final log scan found issues above." >&2
    exit 1
  fi
  if rg -n "$BUILD_LOG_FATAL_PATTERN" "$BUILD_LOG"; then
    echo "Monograph build completed, but log scan found issues above." >&2
    exit 1
  fi
else
  if grep -nE "$FINAL_LOG_ISSUE_PATTERN" main.log; then
    echo "Monograph build completed, but final log scan found issues above." >&2
    exit 1
  fi
  if grep -nE "$BUILD_LOG_FATAL_PATTERN" "$BUILD_LOG"; then
    echo "Monograph build completed, but build log scan found issues above." >&2
    exit 1
  fi
fi

echo "Monograph build and log scan clean: $TEX_DIR/main.pdf"
