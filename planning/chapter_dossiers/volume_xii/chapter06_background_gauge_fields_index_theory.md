# Chapter 06: Background Gauge Fields And Index Theory

## Source Position

This chapter follows Hawking radiation by returning to background geometric
fields, now including gauge bundles.  It connects curved-background QFT,
fermion determinants, zero-mode Berezin integrals, anomaly descent, and
index-theoretic anomaly lines.

## Notation Inventory

- `M^{2n}`: closed oriented Riemannian spin manifold.
- `S^+`, `S^-`: chiral spinor bundles.
- `E`: Hermitian vector bundle with unitary connection.
- `F_E`: skew-Hermitian curvature in characteristic-class convention.
- `F_phys`: Hermitian curvature in physics convention, related by
  `F_E=-i F_phys`.
- `D_A`, `D_A^+`, `D_A^-`: coupled Dirac operator and chiral pieces.
- `Gamma`: chirality operator on `S^+ op S^-`.
- `Ahat(TM)`, `ch(E)`: characteristic classes in the local index theorem.
- `T_Delta(R)`: quadratic index in the monograph trace-delta normalization.
- `k`: instanton number in the fundamental bundle.
- `I_{2n+2}`: anomaly polynomial.
- `I_{2n}^{(1)}(alpha)`: descent form for infinitesimal gauge variation.
- `Det D`: determinant line over the background-field space.

## Claim Ledger

1. Defines the coupled chiral Dirac operator and its analytic Fredholm index.
2. Proves the McKean-Singer supertrace identity by nonzero-eigenvalue
   pairing.
3. States the Atiyah-Singer local index theorem as mathematical input, with
   the characteristic-class convention made explicit.
4. Derives the four-dimensional index formula
   `Ind D_A^+ = int(ch_2(E)-rank(E)p_1(TM)/24)`.
5. Converts the instanton part to the monograph trace-delta normalization:
   `int ch_2(E_R)=T_Delta(R) k`.
6. Works out `SU(N)` fundamental/adjoint instanton zero-mode indices and the
   Abelian `T^4` flux index.
7. Proves the finite-dimensional Berezin zero-mode selection rule.
8. Defines the anomaly polynomial and descent variation, with chirality-sign
   dependence stated explicitly.
9. Separates local anomalies as determinant-line curvature from global
   anomalies as determinant-line holonomy.

## Calculation Ledger

- `calculation-checks/background_index_theory_checks.py` verifies the
  four-dimensional index coefficients, trace-delta `SU(N)` instanton
  indices, Abelian `T^4` flux index, six-form anomaly-polynomial
  coefficients, descent rational coefficients, and Dirac zero-mode
  selection-rule count.
- Existing related checks:
  `calculation-checks/anomaly_polynomial_descent_checks.py` and
  `calculation-checks/bpst_instanton_normalization_checks.py`.

## Figure Ledger

No figure is included.  Future render work should add a determinant-line
diagram over a loop in background-field moduli space and an index-density
flow from `I_{2n+2}` to descent.
