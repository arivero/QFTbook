# Volume VIII, Chapter 4 Dossier: Chern--Simons Theory

## Logical Role

- Role in the monograph: provide the first nontrivial three-dimensional
  topological gauge theory after BF theory.
- Immediate predecessor: BF theory.
- Immediate successor: cohomological field theories and twists.

## Definitions And Results

- Chern--Simons functional with a fixed invariant bilinear form.
- Variation and flat-connection equation of motion.
- Level quantization from large gauge transformations.
- Phase space on a spatial surface and its symplectic form.
- Wilson lines and framing dependence.
- Explicit \(SU(2)_k\) modular \(S\)-matrix, quantum dimensions, normalized
  unknot and Hopf-link expectation values.
- Verlinde fusion formula and closed-surface state-space dimensions.
- Boundary polarization, chiral Wess--Zumino--Witten action, the
  Polyakov--Wiegmann identity, cancellation of the Chern--Simons boundary
  variation, and the level-\(k\) affine current algebra.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(M\) | oriented three-manifold |
| \(G\) | compact gauge group |
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
2. Integral level gives gauge invariance of \(\exp(iS_{\rm CS})\) on closed
   manifolds for the stated trace normalization.
3. Boundary conditions or boundary degrees of freedom are part of the theory.
4. Framing is part of the quantum Wilson-line definition.
5. For \(SU(2)_k\), the modular \(S\)-matrix is a finite sine transform and
   is orthogonal.
6. Normalized \(S^3\) unknot and Hopf-link amplitudes are \(S_{0a}/S_{00}\)
   and \(S_{ab}/S_{00}\), respectively.
7. Verlinde fusion gives the truncated \(SU(2)\) Clebsch--Gordan rule, and
   \(\dim\mathcal H(\Sigma_g)=\sum_x(S_{0x})^{2-2g}\).
8. In holomorphic boundary polarization, the on-shell Chern--Simons variation
   is \(k(2\pi)^{-1}\int A_z\,\delta A_{\bar z}\); the gauged chiral WZW
   boundary action cancels it, and its Polyakov--Wiegmann identity gives the
   level-\(k\) affine current algebra.

## Calculation Checks

- `calculation-checks/chern_simons_su2_modular_checks.py` verifies the
  \(SU(2)_k\) sine-transform orthogonality, quantum dimensions, Hopf-link
  normalizations, Verlinde fusion coefficients, and sphere/torus state-space
  dimensions for finite ranges of \(k\).

## Figures

- Spatial surface with Wilson line punctures may be added later.
