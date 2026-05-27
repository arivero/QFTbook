# 2026-05-26 Volume XI Wilson Lattice Area-Bound Audit

## Scope

- Deepened Volume XI, Chapter 5 by turning the finite \(\mathbb Z_2\)
  character expansion into an explicit surface-counting statement.
- Added the minimal area \(A_{\min}(C)\), excess-area counts \(N_C(n)\), closed
  surface counts \(N_0(n)\), and the finite entropy hypothesis
  \(N_C(n)\leq K(C)\rho^n\).
- Proved the finite-regulator area estimate directly from the exact
  character expansion, with the fixed-cutoff status separated from continuum
  confinement.
- Added the one-cube example
  \(\langle W(C)\rangle=(t+t^5)/(1+t^6)\).

## Calculation Checks

- Added `calculation-checks/z2_strong_coupling_surface_checks.py`, which
  enumerates small cubical plaquette complexes over \(\mathbb F_2\).
- The script verifies:
  - the one-cube numerator and denominator polynomials;
  - the \(2\times1\) rectangular surface counts in a \(2\times1\times1\) box;
  - the exact rational arithmetic in the displayed entropy-bound estimate.

## Verification

- `python3 calculation-checks/z2_strong_coupling_surface_checks.py`
- `python3 -m py_compile calculation-checks/z2_strong_coupling_surface_checks.py`
- `python3 calculation-checks/z2_gauge_metropolis_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and log scan were clean.  `pdfinfo` reports
`Pages: 1839` for `monograph/tex/main.pdf`.

## Residual Work

- The nonabelian strong-coupling expansion and cluster expansion belong to a
  later deeper pass that should align Volume XI examples with the Volume II
  lattice Yang--Mills chapter.
- This pass proves a finite-cutoff strong-coupling estimate.  It does not
  claim a four-dimensional continuum confinement theorem.
