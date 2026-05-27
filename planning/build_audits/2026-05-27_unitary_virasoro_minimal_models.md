# Build Audit: Unitary Virasoro Minimal Models

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
  - `planning/build_audits/2026-05-27_unitary_virasoro_minimal_models.md`

## Content

This pass starts incorporating the 253c and stringbook unitary two-dimensional
CFT material that was previously only partially represented by the Ising
modular-data example.  Chapter 12 now has a dedicated unitary Virasoro
minimal-model section.  It derives the level-one and level-two descendant
Gram matrices from Virasoro commutators, states the unitary highest-weight
classification as a theorem boundary, records the Kac-table identification,
and derives the Ising spin level-two null vector.

The Ising spin four-point calculation is now treated as a local derivation:
the null vector gives the BPZ differential equation, the two holomorphic
solutions are displayed, and the crossing matrix fixes
`C_{sigma sigma epsilon}=1/2` up to the sign convention for `epsilon`.

The new public script `calculation-checks/cft_virasoro_minimal_checks.py`
checks the Kac-table arithmetic, Ising and tricritical-Ising weights, the
level-two Gram determinant and null vector, the BPZ ODE on the two Ising
blocks, and the crossing-matrix calculation fixing the structure constant.

## Verification

- `python3 calculation-checks/cft_virasoro_minimal_checks.py`
- `python3 -m py_compile calculation-checks/cft_virasoro_minimal_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `953efa14`, the full monograph build and
final log scan are clean at 1951 pages.
