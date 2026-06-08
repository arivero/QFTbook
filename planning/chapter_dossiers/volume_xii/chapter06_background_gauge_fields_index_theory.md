# Chapter 06: Background Gauge Fields And Index Theory
Source-File: monograph/tex/volumes/volume_xii/chapter06_background_gauge_fields_index_theory.tex

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
- `D_A=i gamma^mu nabla_mu`, `D_A^+`, `D_A^-`: self-adjoint Euclidean
  coupled Dirac operator and chiral pieces; raw `gamma^mu nabla_mu` is
  anti-self-adjoint.
- `Gamma`: chirality operator on `S^+ op S^-`.
- `P_+`, `P_-`: positive chiral Laplacians
  `(D_A^+)^* D_A^+` and `D_A^+ (D_A^+)^*`.
- `Ahat(TM)`, `ch(E)`: characteristic classes in the local index theorem.
- `gamma^{ab}`: antisymmetrized Clifford product `1/2[gamma^a,gamma^b]`.
- `P=-(g^{mu nu}nabla_mu nabla_nu+Ecal)`: Laplace-type operator
  convention used for heat-kernel coefficients.
- `E_A=-Scal/4 + gamma^{ab}F^E_ab/2`: Laplace-type endomorphism for
  `D_A^2`, whose signs are opposite to the zero-order terms in `D_A^2`.
- `Omega_{mu nu}`: curvature of the auxiliary connection in a Laplace-type
  operator.
- `a_{2r}(P;x)`: local Seeley-DeWitt heat coefficients.
- `T_Delta(R)`: quadratic index in the monograph trace-delta normalization.
- `k`: instanton number in the fundamental bundle.
- `I_{2n+2}`: anomaly polynomial.
- `I_{2n}^{(1)}(alpha)`: descent form for infinitesimal gauge variation.
- `Det D`: determinant line over the background-field space.

## Claim Ledger

1. Defines the self-adjoint Euclidean coupled chiral Dirac operator
   `D_A=i gamma^mu nabla_mu` and its analytic Fredholm index.
2. Proves formal adjointness by integration by parts, states the `H^1`
   domains, and identifies `D_A^-=(D_A^+)^*`.
3. Proves the McKean-Singer supertrace identity using the positive chiral
   Laplacians by nonzero-eigenvalue pairing.
4. Proves the Lichnerowicz formula with the chapter's Clifford and curvature
   conventions, and separates the zero-order signs in `D_A^2` from the
   Laplace-type endomorphism `E_A`.
5. Defines Laplace-type heat coefficients and displays the first
   Seeley-DeWitt coefficients `a_0`, `a_2`, `a_4` with their transport
   recursion origin.
6. Quotes the local Atiyah-Singer index theorem as analytic input rather than
   compressing a full Getzler proof, and keeps the radial-gauge homotopy signs
   and Chern-Weil normalizations explicit.
7. Derives the four-dimensional index formula
   `Ind D_A^+ = int(ch_2(E)-rank(E)p_1(TM)/24)`.
8. Converts the instanton part to the monograph trace-delta normalization:
   `int ch_2(E_R)=T_Delta(R) k`.
9. Works out `SU(N)` fundamental/adjoint instanton zero-mode indices and the
   Abelian `T^2`/`T^4` flux indices.
10. Proves the finite-dimensional Berezin zero-mode selection rule.
11. Defines the anomaly polynomial and descent variation, with chirality-sign
   dependence stated explicitly.
12. Separates local anomalies as determinant-line curvature from global
   anomalies as determinant-line holonomy.

## Calculation Ledger

- `calculation-checks/background_index_theory_checks.py` verifies the
  `Ahat` expansion through degree eight, four-dimensional index coefficients,
  trace-delta `SU(N)` instanton indices, Abelian `T^2`/`T^4` flux indices,
  six-form anomaly-polynomial coefficients, descent rational coefficients, the
  Euclidean `i gamma.nabla` flat-torus Fourier convention, radial-gauge
  homotopy signs, Lichnerowicz versus Laplace-type endomorphism signs, and
  Dirac zero-mode selection-rule count.
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
- 2026-06-08 issue #909 Euclidean Dirac convention pass: made
  `D_A=i gamma^mu nabla_mu` the canonical self-adjoint operator, recorded that
  raw `gamma^mu nabla_mu` is anti-self-adjoint, stated `H^1` domains and
  positive chiral Laplacians, fixed Lichnerowicz/Laplace-type signs, and
  propagated the convention to Euclidean Fujikawa heat-kernel uses.  The
  cross-volume audit found no Volume XI continuum heat-kernel use requiring a
  change and qualified the Volume VII two-dimensional GLSM fluctuation operator
  as a complex first-order operator whose heat kernel is taken through
  `D_F^dagger D_F`, not through raw `gamma^mu nabla_mu`.
- 2026-06-08 issue #910 local-index proof audit: replaced the compressed
  Getzler proof claim with a quoted local Atiyah-Singer theorem, corrected the
  radial-gauge homotopy coefficients for the spin and bundle connections, and
  added explicit `T^2` line-bundle and `T^4` product-flux convention checks.
