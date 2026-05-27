# Build Audit: Elliptic Genus and Superconformal Coordination

## Scope

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Issue context: #606 stringbook-depth / 253c unitary-CFT absorption.
- Base checked against `origin/main` at `de2e2958`.
- Files touched:
  - `monograph/tex/volumes/volume_v/chapter15_two_dimensional_superconformal_algebras.tex`
  - `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
  - `calculation-checks/superconformal_algebra_checks.py`
  - `calculation-checks/README.md`
  - `planning/chapter_dossiers/volume_v/chapter15_two_dimensional_superconformal_algebras.md`
  - `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
  - `planning/source_inventory/stringbook_crosswalk.md`
  - `planning/build_audits/2026-05-27_elliptic_genus_superconformal_coordination.md`

## Content

This pass adds the elliptic-genus layer to the Volume V two-dimensional
superconformal chapter and coordinates it with the Volume VII
Landau--Ginzburg/GLSM development.  Chapter 15 now defines the compact unitary
\(\mathcal N=(2,2)\) Ramond--Ramond trace datum, states the trace-class and
finite-multiplicity hypotheses needed for the index, proves right-moving
localization from the Ramond zero-mode anticommutator, derives the
spectral-flow elliptic law with Jacobi index \(c/6\), and marks the full
modular Jacobi-form statement as a sewing theorem requiring spin-CFT modular
covariance rather than a consequence of the local mode algebra alone.

The chapter also adds a finite Landau--Ginzburg protected-index shadow:
assuming an isolated quasihomogeneous superpotential is realized by a compact
unitary \(\mathcal N=2\) fixed point and Jacobi-ring classes become NS chiral
primaries, spectral flow by \(\eta=-1/2\) shifts their left Ramond charges by
\(-c_{\mathrm{LG}}/6\).  Volume VII now points back to this CFT derivation and
records the same finite \(\chi_y\) polynomial as a necessary protected check,
while reserving RG-flow realization and full elliptic-genus equality for the
supersymmetric-field-theory construction.

The calculation companion now checks the spectral-flow/Jacobi elliptic
multiplier law, its composition cocycle, the \(A_k\) Landau--Ginzburg
\(\chi_y\) charge polynomial, and the Witten-index count for \(A_k\) and
quintic examples.

## Verification

- `python3 calculation-checks/superconformal_algebra_checks.py`
- `python3 -m py_compile calculation-checks/superconformal_algebra_checks.py`
- `tools/run_calculation_checks.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

After rebasing onto `origin/main` at `de2e2958`, the full monograph build and
final log scan are clean at 1966 pages.
