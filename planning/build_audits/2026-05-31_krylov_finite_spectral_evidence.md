# 2026-05-31 Krylov finite spectral evidence pass

## Scope

This pass develops the numerical-evidence lane of the statmech-to-QFT
crosswalk in Volume XI, Chapter 10.

## Monograph changes

- Added `Krylov Data as Finite Spectral Evidence`.
- Defined the finite Krylov spectral certificate
  \((V_m,T_m,R_m)\) for a Hermitian truncation matrix and seed vector.
- Derived the exact Lanczos Ritz-residual identity
  \[
    \|(A-\theta)V_my\|=\beta_m |y_m|
  \]
  as a finite-matrix residual certificate.
- Derived the finite Krylov spectral-measure moment identity through degree
  \(2m-1\), emphasizing that the Krylov quadrature measure certifies the
  cyclic seed spectral measure rather than the whole finite Hilbert space.
- Added the symmetry-sector and seed-overlap obligations needed before
  finite Krylov data can be interpreted as evidence for a QFT spectrum.

## Companion checks

- Extended `calculation-checks/hamiltonian_truncation_dlcq_checks.py` with a
  deterministic Krylov/Lanczos check of the residual formula and moment
  exactness.

## Theorem-form note

The new material is presented as a definition plus derivational prose rather
than as a theorem-family wrapper.  The exact identities are finite linear
algebra; their role is to certify numerical evidence and to expose the
separate continuum and sector-coverage hypotheses.
