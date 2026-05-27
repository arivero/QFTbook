# Build Audit: Holomorphic Gauge One-Loop Exactness

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 05, `Nonrenormalization and
Holomorphy`, at the point where the holomorphic Wilsonian gauge coupling was
previously summarized by a compact one-loop-exactness argument.

## Substantive Edits

- Replaced the short one-loop-exactness explanation by a named proposition
  with explicit hypotheses: weak-coupling Wilsonian patch,
  theta-periodicity, perturbative sector as the `q_h^0` coefficient, no
  negative weak-coupling powers, and no additional anomalous spurion
  coordinate with the gauge kinetic transformation law.
- Made the instanton-counting coordinate `q_h=exp(2 pi i tau)` explicit and
  separated perturbative `q_h^0` data from nonperturbative positive powers.
- Explained why finite holomorphic reference-coordinate changes alter only
  scale-independent constants.
- Extended `calculation-checks/susy_holomorphy_nsvz_checks.py` with a formal
  finite \(q\)-series projection check for the perturbative coefficient,
  finite scheme-shift invariance, and rejection of negative weak-coupling
  powers.
- Updated the Chapter 05 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_holomorphy_nsvz_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_holomorphy_nsvz_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the updated SUSY
  holomorphy/NSVZ check and the Wolfram gamma-trace gate.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed after rebasing onto `origin/main`;
  generated `monograph/tex/main.pdf` with 1960 pages and file size
  7846635 bytes.
