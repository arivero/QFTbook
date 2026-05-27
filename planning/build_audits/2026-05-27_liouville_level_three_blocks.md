# Build Audit: Liouville Level-Three Virasoro Blocks

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT conformal-block rigor.
- Base checked against `origin/main` at `759bab3d`.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter13_liouville_cft.tex`
  - `calculation-checks/liouville_bpz_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter13_liouville_cft.md`
  - `planning/source_inventory/stringbook_crosswalk.md`
  - `planning/build_audits/2026-05-27_liouville_level_three_blocks.md`

## Content

This pass extends the Liouville conformal-block derivation from level two to
level three.  Chapter 13 now writes the ordinary Virasoro block through
\(f_3\), states the required nondegeneracy condition as a level-dependent
Gram-matrix hypothesis, and derives the level-three projector formula from
the finite Shapovalov matrix in the ordered basis
\((L_{-3}|h\rangle,L_{-2}L_{-1}|h\rangle,L_{-1}^3|h\rangle)\).

The new text displays the full level-three Gram matrix, factors its
determinant into the level-two Kac factor and the genuinely level-three
factor, identifies the descendant three-point vectors, and proves
\(f_3=B_3^{\mathsf T}G_3^{-1}A_3\).  It also checks the \(c\to\infty\)
limit against the level-three global \(SL_2\) block coefficient, separating
the finite Virasoro calculation from the still-open all-level
Zamolodchikov-residue normalization problem.

The calculation companion now verifies the level-three determinant
factorization, an exact rational sample for the \(f_3\) projector, and the
global-block denominator.  The Chapter 13 dossier and stringbook crosswalk
were updated accordingly.

## Verification

- `python3 calculation-checks/liouville_bpz_checks.py`
- `python3 -m py_compile calculation-checks/liouville_bpz_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `759bab3d`, the full monograph build and
final log scan are clean at 1970 pages.
