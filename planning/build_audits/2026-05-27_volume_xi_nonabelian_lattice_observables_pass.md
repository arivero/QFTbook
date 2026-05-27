# 2026-05-27 Volume XI Nonabelian Lattice Observables Pass

## Scope

This pass deepens Volume XI, Chapter 5 beyond the abelian
\(\mathbb Z_2\) benchmark by adding the compact-group character expansion,
the \(SU(N)\) fundamental plaquette normalization, and the transfer-matrix
definition of static potentials and Creutz ratios.

## Substantive Additions

- Added the Peter--Weyl character expansion for smooth compact-group
  plaquette weights and formulated the finite-cutoff nonabelian spin-foam
  tensor-network expansion with link Haar projectors.
- Explained how Wilson-loop insertions become boundary spin networks in the
  same Haar-projector expansion.
- Derived the \(SU(N)\), \(N\ge3\), Wilson-weight normalization
  \[
    \left.\frac{d}{d\beta}
    \left\langle \frac1N\operatorname{Re}\operatorname{Tr}U_p
    \right\rangle_\beta\right|_{\beta=0}
    =
    \frac{1}{2N^2},
  \]
  giving the \(SU(3)\) coefficient \(1/18\).
- Added a static-potential section: normalized rectangular Wilson loops as
  transfer-matrix correlators, spectral extraction of the finite-lattice
  static energy, additive line-self-energy caveat, and Creutz-ratio
  perimeter cancellation.
- Added `calculation-checks/nonabelian_lattice_observable_checks.py` for the
  plaquette normalization, static single-state transfer ratio, and Creutz
  exponent cancellation.

## Verification

- Passed: `python3 calculation-checks/nonabelian_lattice_observable_checks.py`
- Passed: `python3 -m py_compile calculation-checks/nonabelian_lattice_observable_checks.py`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2230 pages.

## Remaining Work

- The chapter still needs a fuller treatment of improved gauge actions,
  explicit \(SU(3)\) algorithms tied to static-potential measurements,
  cluster-runnable Wilson-flow/static-potential tooling, and interacting
  continuum-control estimates.
