# 2026-05-28 -- Issue #633, Volume XII microlocal Hadamard recursion uplift

## Target

Issue #633 flags Volume XII chapter 09 as a Tier-A theorem-density gap: the
chapter stated the Hadamard parametrix but did not derive the transport
equations for `U`, the logarithmic coefficients `v_j`, or the coincidence
recursion that later point-splitting and curved-background chapters rely on.

## Changes

- Corrected the chapter's Klein-Gordon convention to the Volume XII operator
  `P_M=-nabla^mu nabla_mu+m^2+xi R`.
- Added a local normal-neighborhood construction of Synge's function,
  `sigma_epsilon`, the van Vleck determinant, and the leading coefficient
  `U=Delta^{1/2}`.
- Proved the transport equation
  `2 sigma^{;mu} nabla_mu U + (Box sigma - 4) U = 0`.
- Added a theorem deriving the four-dimensional Hadamard recursion for
  `v_0` and `v_{j+1}`, including the coincidence formulas
  `v_0(x,x)=1/2(m^2+(xi-1/6)R)` and
  `v_{j+1}(x,x)=P v_j|/[2(j+1)(j+2)]`.
- Clarified the distinction between the operator principal symbol and the
  metric Hamiltonian used to orient null bicharacteristics.
- Expanded `microlocal_spectrum_checks.py` to verify the diagonal recursion
  coefficients in exact rational arithmetic.

## Verification

- `python3 calculation-checks/microlocal_spectrum_checks.py`
- `python3 -m py_compile calculation-checks/microlocal_spectrum_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

## Status

This materially addresses the Hadamard-parametrix part of the Volume XII
chapter 09 Tier-A finding in #633.  The issue remains open because other
Tier-A items remain: BPHZ theorem density, bound-state pole structure, CFT
fixed-point theorem density, and the 6D `(2,0)` chapter.
