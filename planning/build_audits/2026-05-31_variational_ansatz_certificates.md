# 2026-05-31 Variational ansatz certificate pass

## Scope

This pass continues the numerical-evidence lane of the statmech-to-QFT
crosswalk in Volume XI, Chapter 10.

## Monograph changes

- Added `Variational Ansatz Certificates`.
- Defined finite variational ansatz data
  \((V,A,\Theta,\Psi,\mathcal S,\mathcal E_{\rm samp})\), covering
  tensor-network, DMRG/MERA, and neural-state calculations as finite
  Hilbert-space methods before continuum interpretation.
- Derived the finite energy-variance certificate
  \[
    \Delta_\psi^2=\|(A-E_\psi)\psi\|^2/\|\psi\|^2
  \]
  and its spectral/projector leakage consequences.
- Derived the finite ground-projector leakage estimate when the ground energy
  and finite gap are independently certified.
- Derived the tangent-gradient formula for smooth normalized ansatz families,
  identifying variational stationarity as residual orthogonality to tangent
  directions.
- Derived the finite local-energy mean and variance identities used by
  sampled neural-state and variational Monte Carlo calculations.

## Companion checks

- Extended `calculation-checks/hamiltonian_truncation_dlcq_checks.py` with a
  deterministic finite-matrix check of the variance/residual identity,
  spectral-distance and ground-projector bounds, tangent-gradient formula,
  and local-energy mean/variance identities.

## Theorem-form note

The new material uses definitions and derivational prose rather than theorem
wrappers.  The identities are finite linear algebra and finite sampling
identities; the QFT content lies in the regulator, symmetry-sector,
sampling-error, and continuum-extrapolation hypotheses that must accompany
them.
