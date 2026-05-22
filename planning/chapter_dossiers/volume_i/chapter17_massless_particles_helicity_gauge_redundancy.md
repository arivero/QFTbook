# Volume I, Chapter 17 Dossier: Massless Particles, Helicity, and Gauge Redundancy

## Source Placement

- Follows spinor fields and spinorial LSZ.
- Begins the massless-particle and gauge-field sequence.
- Precedes Maxwell constraints, gauge fixing, QED, and radiative corrections.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 8011--8365;
  - `references/sound_references/straumann_poincare_representations_0809.4942.pdf`
    and text sidecar, especially the massless representation discussion.

## External Reference Boundary

- Straumann is used for the Wigner classification of massless helicity
  representations and the role of the little group \(E(2)\).
- The chapter treats helicity representations with trivial little-group
  translation subgroup.
- Continuous-spin representations are recorded only as a separate
  representation-theoretic class; they are not developed.

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

## Claims Established

- The massless little group is \(ISO(2)\), or its double cover.
- The \(ISO(2)\) structure is exhibited by explicit four-vector matrices for
  \(M_{12}\), \(A\), \(B\), and \(T(\alpha,\beta)\).
- Since \(N_1,N_2\) commute, fixed-reference-momentum generalized states may
  be labeled by their eigenvalues \((a,b)\); \(J_3\) rotates these labels.
- The helicity sectors used here are the irreducible sectors in which the
  translation subgroup acts trivially.
- Nonzero \((a,b)\) gives the continuous-spin class, while \(a=b=0\) gives
  the helicity sectors used for photons and the gauge fields developed here.
- The helicity label \(h\) is the eigenvalue of angular momentum along the
  momentum direction and lies in \(\frac12\mathbb Z\).
- Delta-normalized and covariantly normalized massless states differ by the
  displayed square-root Jacobian; the two conventions are kept distinct.
- The standard transformation \(L(k)\) is a helicity-frame choice; changing it
  conjugates the Wigner cocycle and multiplies one-particle wavefunction
  components by the inverse helicity character.
- For helicity \(\pm1\), the vector polarization representative shifts by a
  multiple of \(k_\mu\) under the null-translation part of the little group.
- The one-photon vector intertwiner calculation shows explicitly that the
  null-translation part produces the representative shift proportional to the
  reference covector \(q_\mu\).
- Changing the helicity frame changes vector polarization representatives by
  the dual helicity phase together with a \(k_\mu\)-shift.
- The antisymmetric field-strength matrix element is invariant under this
  shift and is the local photon observable used in the next chapter.
- Polarization sums require a representative choice, but representative
  dependence drops out after contraction with gauge-invariant or conserved
  data.

## Figure Requirements

- A figure showing the massless little-group action: \(SO(2)\) rotation gives
  helicity phase, while the translation subgroup shifts vector polarization
  representatives along the lightlike momentum direction.

## Exclusions

- No Maxwell action or constraint analysis.
- No gauge fixing.
- No photon propagator.
- No QED coupling or Ward identity derivation beyond the representative-level
  conservation statement needed for polarization sums.
