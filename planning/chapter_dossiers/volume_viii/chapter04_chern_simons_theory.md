# Volume VIII, Chapter 4 Dossier: Chern--Simons Theory

## Logical Role

- Role in the monograph: provide the first nontrivial three-dimensional
  topological gauge theory after BF theory.
- Immediate predecessor: BF theory.
- Immediate successor: cohomological field theories and twists.

## Definitions And Results

- Defines the Chern--Simons defining datum
  `mathfrak C=(G,lambda,mathfrak f,mathfrak L,mathfrak b)`, separating the
  compact gauge group, integral level/differential-cohomology lift, framing
  anomaly datum, line-operator datum, and boundary/polarization datum.
- States the conditional quantum Chern--Simons hypothesis `Z_mathfrak C`:
  finite-dimensional surface state spaces, framed-link cobordism amplitudes,
  functorial gluing, flat-connection semiclassical critical points, modular
  line data when available, and WZW boundary cancellation in holomorphic
  polarization.
- Chern--Simons functional with a fixed invariant bilinear form.
- Variation and flat-connection equation of motion.
- Level quantization from large gauge transformations.
- Wess--Zumino extension independence from the same integral level:
  two extensions differ by a closed three-manifold winding integral, giving a
  \(2\pi k\mathbb Z\) ambiguity in the action.
- Phase space on a spatial surface and its symplectic form.
- Wilson lines and framing dependence.
- Explicit \(SU(2)_k\) modular \(S\)-matrix, quantum dimensions, normalized
  unknot and Hopf-link expectation values.
- Verlinde fusion formula and closed-surface state-space dimensions.
- Boundary polarization, chiral Wess--Zumino--Witten action, the
  Polyakov--Wiegmann identity, cancellation of the Chern--Simons boundary
  variation, and the level-\(k\) affine current algebra.
- Mode-residue extraction of the affine current algebra: the double pole in
  the boundary current OPE gives the central term
  \(k m\kappa^{ab}\delta_{m+n,0}\), and the resulting loop-algebra cocycle is
  checked against the Jacobi identity.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(M\) | oriented three-manifold |
| \(G\) | compact gauge group |
| \(\lambda\), \(\check\lambda\) | integral level and differential-cohomology lift |
| \(\mathfrak C\) | Chern--Simons defining datum |
| \(Z_{\mathfrak C}\) | conditional quantum Chern--Simons theory |
| \(A\) | connection |
| \(S_{\rm CS}\) | Chern--Simons action |
| \(k\) | level |
| \(\mathcal M_{\rm flat}(\Sigma,G)\) | moduli space of flat \(G\)-connections |
| \(S_{ab}\) | \(SU(2)_k\) modular \(S\)-matrix |
| \(d_a\) | quantum dimension of Wilson-line label \(a\) |
| \(N_{ab}^{\phantom{ab}c}\) | Verlinde fusion coefficient |
| \(S_{{\rm WZW},k}(g)\) | boundary Wess--Zumino--Witten functional |
| \(J^a(z)\) | boundary affine current |

## Claim Ledger

1. Classical Chern--Simons equations are \(F_A=0\).
2. The local Chern--Simons functional is only one representative of the full
   defining datum; integral level, framing anomaly, line labels, and boundary
   polarization must be supplied before "the Chern--Simons theory" has a
   definite meaning.
3. Integral level gives gauge invariance of \(\exp(iS_{\rm CS})\) on closed
   manifolds for the stated trace normalization.
4. Boundary conditions or boundary degrees of freedom are part of the theory.
5. Framing is part of the quantum Wilson-line definition.
6. For \(SU(2)_k\), the modular \(S\)-matrix is a finite sine transform and
   is orthogonal.
7. Normalized \(S^3\) unknot and Hopf-link amplitudes are \(S_{0a}/S_{00}\)
   and \(S_{ab}/S_{00}\), respectively.
8. Verlinde fusion gives the truncated \(SU(2)\) Clebsch--Gordan rule, and
   \(\dim\mathcal H(\Sigma_g)=\sum_x(S_{0x})^{2-2g}\).
9. In holomorphic boundary polarization, the on-shell Chern--Simons variation
   is \(k(2\pi)^{-1}\int A_z\,\delta A_{\bar z}\); the gauged chiral WZW
   boundary action cancels it, and its Polyakov--Wiegmann identity gives the
   level-\(k\) affine current algebra.
10. The affine mode commutator follows from contour residues of the OPE:
   \(\operatorname{Res}_{z=w} z^m/(z-w)^2=mw^{m-1}\), so the central
   extension coefficient is \(k m\), not an arbitrary mode convention.

## Proof Obligations And Boundaries

- The chapter does not claim a regulator-level construction of the full
  Chern--Simons path integral.  It records the conditional quantum datum and
  uses modular-functor/geometric-quantization consequences only with that
  boundary stated.
- The integral level must be understood globally, preferably as a
  differential-cohomology lift of a class in \(H^4(BG;\mathbb Z)\), not merely
  as the coefficient of a local trivialization formula.
- The framing anomaly is part of the quantum datum.  Link expectations and
  closed-manifold partition functions are not unframed scalar invariants
  unless the relevant anomaly has been cancelled or a framing convention has
  been fixed.

## Calculation Checks

- `calculation-checks/chern_simons_su2_modular_checks.py` verifies the
  finite-gauge-transgression coefficient, Wess--Zumino extension-ambiguity
  coefficient, Abelian total-derivative sign, holomorphic-polarization
  boundary variation, Polyakov--Wiegmann cross-term coefficient,
  affine-current mode-residue extraction, the finite \(\mathfrak{su}_2\)
  central-extension Jacobi identity, and the \(SU(2)_k\) sine-transform
  orthogonality, quantum dimensions, Hopf-link normalizations, Verlinde
  fusion coefficients, and sphere/torus state-space dimensions for finite
  ranges of \(k\).

## Figures

- Spatial surface with Wilson line punctures may be added later.

## Audit Notes

- 2026-05-30 issue #700 defining-property pass: added the upfront
  Chern--Simons defining datum and conditional quantum Chern--Simons
  hypothesis, then redirected the phase-space and Wilson-line prose to those
  named objects so the chapter no longer treats the local action alone as the
  definition of the theory.
- 2026-06-02 issue #562 assertion-as-derivation continuation: tightened the
  global relation between bulk level quantization and boundary Wess--Zumino
  extension independence without promoting the coefficient bookkeeping to a
  theorem.  The companion check now verifies the \(2\pi k\mathbb Z\) WZ
  ambiguity from the same \(24\pi^2\) winding normalization as the bulk
  finite-gauge transgression.
- 2026-06-03 issue #562 affine-current pass: expanded the boundary-current
  algebra paragraph with the contour-residue derivation of the mode bracket
  and the loop-cocycle Jacobi check, with exact finite \(\mathfrak{su}_2\)
  coverage in the companion script.
