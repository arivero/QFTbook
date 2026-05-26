# 2026-05-26 Issue #591: Symmetric-Product Orbifold CFTs

## Scope

Issue #591 asked for explicit symmetric-product orbifold material beyond the
general finite-orbifold and twist-weight discussion: sector labels,
centralizer projection, central charge, partition functions, twist OPEs, and
deformation operators.

## Manuscript Changes

- Added a dedicated symmetric-product section to
  `volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`.
- Defined \(\operatorname{Sym}^N(\mathcal C)=\mathcal C^{\otimes N}/S_N\),
  the cycle-type partition \(\lambda=(1^{m_1}\cdots N^{m_N})\), and the
  centralizer \(C_\lambda=\prod_K(\mathbb Z_K^{m_K}\rtimes S_{m_K})\).
- Derived central-charge additivity, long-string weights, the centralizer
  invariant sector Hilbert space, and the Hecke-transform generating
  function for torus partition functions from the commuting-pair orbifold
  sum.
- Added the cycle-type bare twist weights, monodromy multiplication in twist
  OPEs, join/split interpretation of transposition twists, discrete-torsion
  status for \(S_N\), normalized two-cycle deformation operators, and the
  distinction between seed, single-cycle, and multi-cycle current-current
  deformations.

## Calculation Check

Added `calculation-checks/symmetric_product_orbifold_checks.py`, which
verifies:

- \(S_N\) centralizer orders and conjugacy-class exhaustion;
- \(c(\operatorname{Sym}^N)=Nc_0\);
- length-two and length-three twist weights for \(c_0=6\);
- cycle-type weights and transposition join weight shifts;
- the normalization count for the conjugacy-class sum over transpositions.
