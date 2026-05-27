# Build Audit: Unitary Minimal-Model Modular Data

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 253c unitary-CFT absorption.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
  - `calculation-checks/cft_virasoro_minimal_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`
  - `planning/source_inventory/stringbook_crosswalk.md`
  - `planning/source_inventory/253a_253b_no_skip_coverage_register.md`
  - `planning/build_audits/2026-05-27_unitary_minimal_modular_data.md`

## Content

This pass extends the previous Ising-focused minimal-model development to the
full diagonal unitary Virasoro minimal-model series \(\mathcal M(m,m+1)\).
Chapter 12 now states the A-series \(S,T\) modular data for all \(m\ge3\),
spells out the Kac-table field-identification quotient, proves that the
identification is fixed-point-free, records the quotient normalization, and
derives the finite fusion rule as the \(SU(2)_{m-2}\times SU(2)_{m-1}\)
product fusion summed over the two representatives of the target orbit.

The calculation companion now checks the modular sine formula, \(S\)-matrix
orthogonality, \(S^2\), Verlinde integrality, and agreement with the exact
\(SU(2)\)-quotient fusion rule for \(m=3,\ldots,7\).  It also checks that the
general formula reproduces the displayed Ising \(S\)-matrix.

## Verification

- `python3 calculation-checks/cft_virasoro_minimal_checks.py`
- `python3 -m py_compile calculation-checks/cft_virasoro_minimal_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing context was checked against `origin/main` at `86502e68`, the
full monograph build and final log scan are clean at 1955 pages.
