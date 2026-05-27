# Build Audit: Torus One-Point Blocks and Defect Lines

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 253c unitary-CFT absorption.
- Base checked against `origin/main` at `9f5f8a64`.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
  - `calculation-checks/cft_voa_modular_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.md`
  - `planning/source_inventory/stringbook_crosswalk.md`
  - `planning/source_inventory/253a_253b_no_skip_coverage_register.md`
  - `planning/build_audits/2026-05-27_torus_one_point_defect_lines.md`

## Content

This pass adds the genus-one one-point and topological-defect layer to the
Volume V algebraic 2D CFT chapter.  Chapter 12 now defines chiral torus
one-point trace blocks, states Zhu modular covariance with explicit
rationality and \(C_2\)-cofiniteness hypotheses, and explains the coefficient
tensor required for full-CFT one-point functions.  It also defines diagonal
Verlinde defect operators, proves their fusion from the simultaneous
diagonalization form of the Verlinde formula, proves the temporal-defect to
spatial-defect modular \(S\)-move, and works the Ising spin-flip and
Kramers--Wannier lines including the spin-field one-point selection rule.

The calculation companion now checks the Ising Verlinde defect eigencharacters
over \(\mathbb Q(\sqrt2)\), their fusion-ring multiplication, the exact
temporal-to-spatial defect \(S\)-move multiplicity matrices, and the
spin-flip selection rule for the Ising spin one-point function.

## Verification

- `python3 calculation-checks/cft_voa_modular_checks.py`
- `python3 -m py_compile calculation-checks/cft_voa_modular_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and final log scan are clean at 1960 pages.
