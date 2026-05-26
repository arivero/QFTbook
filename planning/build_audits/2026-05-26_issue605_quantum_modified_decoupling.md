# Build Audit: Issue #605 SQCD Quantum-Modified Decoupling Pass

## Scope

- Branch: `codex/susy-gauge-dynamics-localization`.
- Issue: #605, general four-dimensional \(\mathcal N=1\) SQCD foundations.
- Files edited:
  - `monograph/tex/volumes/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.tex`.
  - `calculation-checks/susy_n1_sqcd_duality_checks.py`.
  - `calculation-checks/README.md`.
  - `planning/chapter_dossiers/volume_vii/chapter06_four_dimensional_n1_gauge_dynamics.md`.

## Source Leads

- Internal monograph context: the Chapter 06 ADS instanton calculation,
  holomorphic decoupling proposition, and SQCD duality phase ledger.
- Stringbook convention comparison: `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`
  around the supersymmetric gauge dynamics appendix material.
- Local reference payload: `references/seiberg_electric_magnetic_duality/hep-th-9411149.eprint`,
  used only as a historical/status comparison; the monograph text states
  hypotheses and gives the algebraic derivations directly.
- No string compactification or superstring material was imported.

## Substantive Changes

- Expanded the \(N_f=N_c\) quantum-modified constraint into a
  hypothesis-bounded chiral-ring statement.
- Added a uniqueness proof for the field-independent quantum modification
  from dimension, flavor, baryon, \(R\)-charge, and holomorphic-scale data.
- Added the \(N_f=N_c+1\) confining chiral-sector superpotential as an
  explicit input with a dimension/\(R\)-charge check.
- Derived the \(N_f=N_c\) quantum-modified constraint from the
  \(N_f=N_c+1\) confining superpotential plus a holomorphic mass deformation
  and scale matching.
- Extended the exact arithmetic check script to cover the new
  quantum-modified and mass-decoupling algebra.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py` passed.
- `tools/run_calculation_checks.sh` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf` with 1549 pages.

## Status

The pass materially advances issue #605 but does not close it: the broader
four-dimensional \(\mathcal N=1\) gauge-dynamics program still needs more
self-contained instanton, anomaly, and infrared-comparison development.
