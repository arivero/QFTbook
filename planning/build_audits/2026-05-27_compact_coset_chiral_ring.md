# Build Audit: Compact Coset Chiral Ring

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 2D CFT superconformal-coset rigor.
- Base checked against `origin/main` at `4fc87eee`.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter15_two_dimensional_superconformal_algebras.tex`
  - `calculation-checks/superconformal_algebra_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter15_two_dimensional_superconformal_algebras.md`
  - `planning/source_inventory/stringbook_crosswalk.md`
  - `planning/build_audits/2026-05-27_compact_coset_chiral_ring.md`

## Content

This pass strengthens the compact supersymmetric `SU(2)_k/U(1)` coset
interface.  Chapter 15 now derives the protected NS chiral-primary fusion
ring from the parent `SU(2)_{k-2}` fusion rule, additive `U(1)_R` charge,
and the maximal chiral charge `c/3`.  With `K=k-2`, the result is the
truncated `A`-series ring `C[x]/(x^(K+1))`, with `x^ell` identified with
the compact-coset chiral primary `Psi^{su}_{ell/2,-ell/2}`.

The text explicitly separates this protected chiral-algebra equality from
the dynamical Landau-Ginzburg/GLSM flow theorem, which remains coordinated
with Volume VII.  The calculation companion now checks the multiplication
table, associativity, nilpotence threshold, NS-to-R charge map, and
agreement with the `A`-series Ramond charge ledger in exact rational
arithmetic.

## Verification

- `python3 calculation-checks/superconformal_algebra_checks.py`
- `python3 -m py_compile calculation-checks/superconformal_algebra_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `4fc87eee`, the full monograph build and
final log scan are clean at 1975 pages.
