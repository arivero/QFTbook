# Volume I, Chapter 17 Dossier: Massless Particles, Helicity, and Gauge Redundancy

## Source Placement

- Follows spinor fields and spinorial LSZ.
- Begins the massless-particle and gauge-field sequence.
- Precedes Maxwell constraints, gauge fixing, QED, and radiative corrections.
- Includes a four-dimensional on-shell tree-amplitude interlude after the
  helicity and representative construction; this interlude uses the already
  defined scattering-kernel/LSZ status and does not redefine \(S\).
- Source material used:
  - `transcription/tex/253a/foundations.tex`, lines 8011--8365 as an
    approximate source range;
  - `references/sound_references/straumann_poincare_representations_0809.4942.pdf`
    and text sidecar, especially the massless representation discussion.

## External Reference Boundary

- Straumann is used for the Wigner classification of massless helicity
  representations and the role of the little group \(E(2)\).
- The chapter treats helicity representations with trivial little-group
  translation subgroup.
- Continuous-spin representations are recorded only as a separate
  representation-theoretic class; they are not developed.
- Spinor-helicity, Parke--Taylor, and BCFW are included only at tree level for
  complexified four-dimensional massless on-shell amplitudes.  They are
  presented as consequences of helicity weights, locality, factorization, and
  large-\(z\) behavior, not as nonperturbative definitions of gauge-theory
  scattering.

## Framework

- Four-dimensional Minkowski spacetime with mostly-plus metric.
- Positive-energy massless one-particle orbit \(k^2=0\), \(k^0>0\).
- Unitary representations of the double cover of the proper orthochronous
  Poincare group.
- Generalized fixed-momentum bases and sharp helicity states are understood in
  the rigged-Hilbert-space sense established in Chapter 2.
- Covariant polarization representatives are used as representatives modulo
  shifts proportional to the lightlike momentum.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(q\) | reference lightlike momentum \((\kappa,0,0,\kappa)\) |
| \(L(k)\) | standard Lorentz transformation sending \(q\) to \(k\) |
| \(Q(k)\) | massless little-group change of helicity frame |
| \(\chi_h\) | helicity character of the little group |
| \(M^{\mu\nu}\) | Lorentz generators in the four-vector representation |
| \(A,B\) | four-vector null-translation generators \(M_{01}+M_{31}\), \(M_{02}+M_{32}\) |
| \(J_3\) | rotation generator around the direction of \(q\) |
| \(N_1,N_2\) | null-translation little-group generators |
| \(a,b\) | generalized eigenvalues of \(N_1,N_2\) at fixed reference momentum |
| \(h\) | helicity eigenvalue |
| \(F_L(k)\) | distributional helicity-frame map \(V_h\to\Hilb_{1,h}\) |
| \(\epsilon_\mu^h(k)\) | vector polarization representative |
| \(c_h\) | scalar coefficient of a little-group gauge shift |
| \(A_\mu\) | vector-potential representative |
| \(F_{\mu\nu}\) | gauge-invariant field strength |
| \(n^\mu\) | auxiliary vector used to choose polarization representatives |
| \(\Pi_{\mu\nu}(k;n)\) | transverse polarization projector |
| \(\lambda_a,\widetilde\lambda_{\dot a}\) | spinor-helicity factors of a complex null momentum |
| \(\langle ij\rangle,[ij]\) | holomorphic and antiholomorphic spinor contractions |
| \(A_n(1^{h_1},\ldots,n^{h_n})\) | color-ordered tree partial amplitude |
| \(z\) | BCFW complex deformation parameter |
| \(B_\infty\) | possible boundary contribution at \(z=\infty\) in BCFW recursion |

## Claims Established

- The massless orbit and the standard-section choice \(L(k)\) are defined
  explicitly; changes \(L(k)\mapsto L(k)Q(k)\) are helicity-frame changes.
- The massless little group is \(ISO(2)\), or its double cover.
- The \(ISO(2)\) structure is exhibited by explicit four-vector matrices for
  \(M_{12}\), \(A\), \(B\), and \(T(\alpha,\beta)\).
- The Lie algebra of the future-null little group is proven from the Lorentz
  algebra, and the null-translation matrices are checked to preserve \(\eta\),
  fix \(q\), and add parameters under multiplication.
- Since \(N_1,N_2\) commute, fixed-reference-momentum generalized states may
  be labeled by their eigenvalues \((a,b)\); \(J_3\) rotates these labels.
- The helicity sectors used here are the irreducible sectors in which the
  translation subgroup acts trivially.
- Nonzero \((a,b)\) gives the continuous-spin class, while \(a=b=0\) gives
  the helicity sectors used for photons and the gauge fields developed here.
- The continuous-spin alternative is derived in prose from the joint spectral
  measure of the commuting little-group translations: a nonzero
  translation-eigenvalue radius forces a full \(SO(2)\) orbit and an infinite
  tower of angular modes, while the finite-helicity sectors are the
  \(\rho=0\) case.
- The helicity label \(h\) is the eigenvalue of angular momentum along the
  momentum direction and lies in \(\frac12\mathbb Z\).
- Delta-normalized and covariantly normalized massless states differ by the
  displayed square-root Jacobian; the two conventions are kept distinct.
- The standard transformation \(L(k)\) is a helicity-frame choice; changing it
  conjugates the Wigner cocycle and multiplies one-particle wavefunction
  components by the inverse helicity character.
- The Wigner cocycle identity and the frame-change law are proven as a
  proposition.
- For helicity \(\pm1\), the vector polarization representative shifts by a
  multiple of \(k_\mu\) under the null-translation part of the little group.
- The little-group null-translation polarization shift is proven explicitly
  from the displayed \(T(\alpha,\beta)\) matrix.
- The one-photon vector intertwiner calculation shows explicitly that the
  null-translation part produces the representative shift proportional to the
  reference covector \(q_\mu\).
- Changing the helicity frame changes vector polarization representatives by
  the dual helicity phase together with a \(k_\mu\)-shift.
- The antisymmetric field-strength matrix element is invariant under this
  shift and is the local photon observable used in the next chapter.
- The field-strength matrix element is promoted to a proposition proving
  descent to the helicity line.
- Polarization sums require a representative choice, but representative
  dependence drops out after contraction with gauge-invariant or conserved
  data.
- The auxiliary-vector projector formula is proven to annihilate \(k\) and
  \(n\), and its representative dependence is shown to vanish against
  conserved data.
- In four dimensions a complex null momentum is represented by
  \(p_{a\dot a}=\lambda_a\widetilde\lambda_{\dot a}\), modulo
  \((\lambda,\widetilde\lambda)\mapsto(t\lambda,t^{-1}\widetilde\lambda)\).
  The mostly-plus invariant is
  \(\langle ij\rangle[ji]=2p_i\cdot p_j\) with the
  \(p_{a\dot a}=p^0\mathbf 1+p^i\sigma_i\) convention.
- The spinor-helicity frame and mostly-plus determinant identity are now
  boxed as a definition/proposition.
- A helicity amplitude has little-group weight
  \(A_n(\ldots,t_i\lambda_i,t_i^{-1}\widetilde\lambda_i,\ldots)
  =t_i^{-2h_i}A_n\).
- Spinor-helicity polarization representatives are displayed with a reference
  spinor; changing the reference spinor shifts the polarization by a multiple
  of the null momentum.
- The three-point color-ordered Yang--Mills amplitudes are fixed by locality,
  mass dimension, and little-group weights:
  \[
    A_3(1^-,2^-,3^+)=
    \frac{\langle12\rangle^3}{\langle23\rangle\langle31\rangle},
    \qquad
    A_3(1^+,2^+,3^-)=
    \frac{[12]^3}{[23][31]}.
  \]
- The Parke--Taylor MHV formula is stated for tree amplitudes with two
  negative-helicity gluons:
  \[
    A_n(1^+,\ldots,r^-,\ldots,s^-,\ldots,n^+)
    =
    \frac{\langle rs\rangle^4}
    {\langle12\rangle\langle23\rangle\cdots\langle n1\rangle}.
  \]
- The adjacent-negative Parke--Taylor formula is now stated as a theorem under
  explicit tree-level factorization, three-point input, and good-shift
  hypotheses; the general nonadjacent placement is kept as the standard
  closed form with the channel-count caveat stated.
- The BCFW shift
  \(\widehat{\widetilde\lambda}_i=\widetilde\lambda_i+z\widetilde\lambda_j\),
  \(\widehat\lambda_j=\lambda_j-z\lambda_i\) preserves on-shellness and total
  momentum.  Cauchy's theorem gives the recursion with possible boundary term
  \(B_\infty\), and tree-level Yang--Mills good shifts have \(B_\infty=0\).
- The BCFW on-shell kinematics and the recursion formula with boundary term
  are now explicit proposition/theorem statements with proofs.
- The five-point MHV example is worked through a single nonzero BCFW
  factorization channel and gives
  \[
    A_5(1^-,2^-,3^+,4^+,5^+)
    =
    \frac{\langle12\rangle^4}
    {\langle12\rangle\langle23\rangle\langle34\rangle
     \langle45\rangle\langle51\rangle}.
  \]

## Figure Requirements

- A figure showing the massless little-group action: \(SO(2)\) rotation gives
  helicity phase, while the translation subgroup shifts vector polarization
  representatives along the lightlike momentum direction.
- A BCFW factorization figure showing a complex on-shell pole decomposing a
  color-ordered tree amplitude into two lower-point amplitudes and an
  intermediate propagator.

## Exclusions

- No Maxwell action or constraint analysis.
- No gauge fixing.
- No photon propagator.
- No QED coupling, loop amplitude technology, or gauge-fixed propagator
  derivation.  The only perturbative amplitudes included here are tree-level
  on-shell Yang--Mills partial amplitudes used to connect helicity
  representation theory to modern scattering-amplitude variables.

## Audit Notes

- 2026-05-25 issue #456 pass: added spinor-helicity variables, little-group
  weights, spinorial polarization representatives, color-ordered three-gluon
  amplitudes, the Parke--Taylor MHV formula, BCFW recursion with its boundary
  term, a BCFW factorization figure, and the five-point MHV worked example.
- 2026-05-27 issue #615 pass: formalized the massless-orbit section,
  little-group algebra, helicity representation, Wigner cocycle,
  polarization representative shift, field-strength descent, polarization
  projector, spinor-helicity determinant convention, Parke--Taylor theorem,
  and BCFW recursion.  Added `calculation-checks/massless_helicity_checks.py`.
