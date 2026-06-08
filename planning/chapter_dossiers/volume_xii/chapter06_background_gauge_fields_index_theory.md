# Chapter 06: Background Gauge Fields And Index Theory

## Source Position

This chapter opens the separate background-gauge/index-theory lane after the
fixed-background and semiclassical-backreaction material.  It returns to
background geometric fields, now including gauge bundles, and connects
curved-background QFT, fermion determinants, zero-mode Berezin integrals,
anomaly descent, and index-theoretic anomaly lines.

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
- `gamma^{ab}`: antisymmetrized Clifford product `1/2[gamma^a,gamma^b]`.
- `P=-(g^{mu nu}nabla_mu nabla_nu+Ecal)`: Laplace-type operator
  convention used for heat-kernel coefficients.
- `Omega_{mu nu}`: curvature of the auxiliary connection in a Laplace-type
  operator.
- `a_{2r}(P;x)`: local Seeley-DeWitt heat coefficients.
- `T_Delta(R)`: quadratic index in the monograph trace-delta normalization.
- `k`: instanton number in the fundamental bundle.
- `I_{2n+2}`: anomaly polynomial.
- `I_{2n}^{(1)}(alpha)`: descent form for infinitesimal gauge variation.
- `Det D`: determinant line over the background-field space.

## Claim Ledger

1. Defines the coupled chiral Dirac operator and its analytic Fredholm index.
2. Proves the McKean-Singer supertrace identity by nonzero-eigenvalue
   pairing.
3. Proves the Lichnerowicz formula with the chapter's Clifford and curvature
   conventions.
4. Defines Laplace-type heat coefficients and displays the first
   Seeley-DeWitt coefficients `a_0`, `a_2`, `a_4` with their transport
   recursion origin.
5. Replaces the quoted local index theorem by a Getzler-rescaling derivation
   of the local density `Ahat(TM) ch(E)`.
6. Derives the four-dimensional index formula
   `Ind D_A^+ = int(ch_2(E)-rank(E)p_1(TM)/24)`.
7. Converts the instanton part to the monograph trace-delta normalization:
   `int ch_2(E_R)=T_Delta(R) k`.
8. Works out `SU(N)` fundamental/adjoint instanton zero-mode indices and the
   Abelian `T^4` flux index.
9. Proves the finite-dimensional Berezin zero-mode selection rule.
10. Defines the anomaly polynomial and descent variation, with chirality-sign
   dependence stated explicitly.
11. Separates local anomalies as determinant-line curvature from global
   anomalies as determinant-line holonomy.

## Calculation Ledger

- `calculation-checks/background_index_theory_checks.py` verifies the
  `Ahat` expansion through degree eight, four-dimensional index coefficients,
  trace-delta `SU(N)` instanton indices, Abelian `T^4` flux index, six-form
  anomaly-polynomial coefficients, descent rational coefficients, and Dirac
  zero-mode selection-rule count.
- Existing related checks:
  `calculation-checks/anomaly_polynomial_descent_checks.py` and
  `calculation-checks/bpst_instanton_normalization_checks.py`.

## Figure Ledger

No figure is included.  Future render work should add a determinant-line
diagram over a loop in background-field moduli space and an index-density
flow from `I_{2n+2}` to descent.

## Anti-Wrapper Audit

- 2026-06-08 issue #729 printed-order pass: updated the source-position
  dossier so the index-theory lane begins after the fixed-background and
  semiclassical-backreaction material, rather than interrupting the
  microlocal-to-applications sequence.  The chapter remains the background
  gauge field, zero-mode, descent, and determinant-line input for global
  anomaly work.
- 2026-05-29: expanded the McKean-Singer proof to state the elliptic spectral
  inputs, heat-trace absolute convergence, multiplicity-preserving nonzero
  spectral pairing, and zero-mode contribution to the analytic index.
