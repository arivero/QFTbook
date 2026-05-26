# Volume VIII, Chapter 3 Dossier: BF Theory

## Logical Role

- Role in the monograph: first explicit cohomological gauge-theory example
  after the functorial target structure.  The chapter now gives a concrete
  model in which ordinary gauge symmetry, higher-form gauge symmetry,
  reducibility, BV field content, finite sums, and extended observables can
  all be checked explicitly.
- Immediate predecessor: bordism functoriality and extraction from local QFT.
- Immediate successor: Chern--Simons theory and broader cohomological gauge
  theories.

## Definitions And Results

- Classical BF fields \(A\) and \(B\) on a principal \(G\)-bundle.
- Nonabelian BF action
  \(S_{\rm BF}=2\pi i\int_M\langle B\wedge F_A\rangle\), with the
  curvature and invariant pairing defined before use.
- Variation of the action and derivation of the equations of motion
  \(F_A=0\) and \(\dd_A B=0\), including the covariant Leibniz sign.
- Ordinary gauge symmetry
  \(A^g=g^{-1}Ag+g^{-1}\dd g\), \(B^g=g^{-1}Bg\), matched to the
  infinitesimal convention \(\delta_cA=\dd_Ac\), \(\delta_cB=[B,c]\).
- \(B\)-field shift symmetry, its boundary term, and the reducibility chain
  that forces ghosts-for-ghosts in BV.
- Compact abelian normalization using differential-character language, with
  Wilson and surface operators normalized by \(2\pi i\).
- Finite \(\mathbb Z_N\) cochain model with normalized partition function,
  finite Fourier projection, and derivation of
  \(Z_{\rm BF}^{(N)}=|H^1(K;\mathbb Z_N)|/|H^0(K;\mathbb Z_N)|\).
- Wilson/surface linking phase derived from the finite cochain constraint
  \(\delta a=-p\sigma_\Sigma\).
- Metric-independence statement separated into classical metric independence
  and the quantum BV condition needed after gauge fixing.
- Boundary symplectic form and continuum nonabelian BV-BFV open problem.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(M\) | oriented smooth \(D\)-manifold |
| \(P\) | principal \(G\)-bundle |
| \(A\) | connection one-form |
| \(B\) | \((D-2)\)-form valued in the dual adjoint bundle |
| \(F_A\) | curvature of \(A\) |
| \(d_A\) | covariant exterior derivative |
| \(\eta\) | shift-symmetry parameter |
| \(N\) | positive integer level in compact abelian BF theory |
| \(a\) | \(\mathbb Z_N\)-valued one-cochain in the finite model |
| \(b\) | finite Lagrange multiplier in \(\operatorname{Hom}(C^2,\mathbb Z_N)\) |
| \(\delta_r\) | cellular coboundary \(C^r\to C^{r+1}\) |
| \(W_q(\gamma)\) | finite Wilson operator of charge \(q\) on a closed one-cycle |
| \(V_p(\Sigma)\) | finite surface operator of charge \(p\) on a closed \((D-2)\)-cycle |
| \(\sigma_\Sigma\) | Poincare-dual two-cochain representing \(\Sigma\) |

## Claim Ledger

1. The BF equations of motion follow directly from varying \(A\) and \(B\).
2. The finite gauge-transformation convention is consistent with
   \(\delta_cA=\dd_Ac\); this sign convention must be preserved in later
   BV-BF discussions.
3. The \(B\)-shift symmetry is reducible on the flat-connection locus, and
   off shell in the abelian case.
4. The normalized finite abelian BF partition function is the groupoid
   cardinality of flat \(\mathbb Z_N\)-bundles on a connected cell complex.
5. The Wilson/surface correlation phase is
   \(\exp(-2\pi i pq\,\operatorname{Lk}(\gamma,\Sigma)/N)\) in the chapter's
   finite constraint convention.
6. Metric independence requires both metric-free classical action and
   anomaly-free gauge fixing/regularization.

## Calculation Checks

- `calculation-checks/bf_theory_checks.py` verifies finite Fourier
  projection, the finite partition-function identity, cellular Wilson gauge
  invariance, and the linking-phase sign in exact finite arithmetic.

## Remaining Deepening Targets

- Develop the full nonabelian BV action for BF theory in components after
  the general BV chapter has fixed the reducible-gauge notation.
- Add explicit low-dimensional examples: two-dimensional BF as a finite group
  gauge theory, three-dimensional BF and abelian linking, and four-dimensional
  BF with surface operators.
- Integrate the continuum boundary theory with the BV-BFV gluing chapter
  once that chapter has a complete boundary semidensity construction.

## Figures

- Field-degree tower for BF theory and ghosts-for-ghosts.
- Wilson loop/surface linking diagram.
