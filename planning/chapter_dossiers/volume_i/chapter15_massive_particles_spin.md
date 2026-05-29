# Volume I, Chapter 15 Dossier: Massive Particles and Spin

## Source Placement

- Follows scattering observables and unitarity.
- Begins the particle-classification and spinning-external-state arc.
- Precedes spinor fields, Grassmann variables, and spinorial LSZ.
- Source material used:
  - foundations transcript file, lines 6024--6909 in the current transcript
    source range,
    with the handwritten pages pp. 146--165 rendered and checked on
    2026-05-22;
  - `references/sound_references/straumann_poincare_representations_0809.4942.pdf`
    and text sidecar, especially Sections 2--3.

## External Reference Boundary

- Straumann is used for Wigner--Mackey representation theory:
  projective representations lift to the universal cover; massive
  one-particle irreducible representations are induced from irreducible
  representations of the \(SU(2)\) little group.
- The chapter states the representation-theoretic result and uses it to
  organize covariant field intertwiners.
- No full Mackey theorem proof is reproduced.

## Framework

- Four-dimensional Minkowski spacetime with mostly-plus metric.
- Massive one-particle subspace \(\Hilb_1\) with covariantly normalized
  generalized momentum states.
- Massive little group \(SO(3)\) and its double cover \(SU(2)\).
- Covariant local fields transforming in finite-dimensional Lorentz
  representations.
- Gamma-matrix conventions are now centralized in
  `monograph/tex/volumes/volume_i/chapter16a_spinor_conventions.tex`; this chapter supplies the
  spin-\(\frac12\) particle-intertwiner normalizations compatible with that
  appendix.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Sigma_m^+\) | positive-energy mass shell |
| \(p_R\) | reference rest momentum \((m,\vec0)\) |
| \(L(p)\) | standard Lorentz transformation sending \(p_R\) to \(p\) |
| \(N(\vec p)\) | delta-normalization boost factor \((m/\omega_{\vec p})^{1/2}\) |
| \(W(\Lambda,p)\) | Wigner rotation \(L(\Lambda p)^{-1}\Lambda L(p)\) |
| \(Q(p)\) | momentum-dependent little-group change of spin frame |
| \(j\) | spin label of an irreducible \(SU(2)\) representation |
| \(D^{(j)}\) | spin-\(j\) little-group representation |
| \(F_L(p)\) | distributional spin-frame map \(V_j\to\Hilb_1\) |
| \(R\) | finite-dimensional Lorentz representation carried by a field index |
| \(u_A{}^\sigma(p)\) | vacuum-to-particle intertwiner |
| \(\gamma^\mu\) | gamma matrices with mostly-plus Clifford relation |
| \(S^{\mu\nu}\) | spinor Lorentz generators |
| \(\not p\) | \(p_\mu\gamma^\mu\) |
| \(u^\sigma(p),v^\sigma(p)\) | spinor polarization wavefunctions |
| \(\mathcal U^\sigma(p),\mathcal V^\sigma(p)\) | delta-normalized spinor polarizations |
| \(\beta\) | \(\ii\gamma^0\), defining the Lorentz-invariant spinor pairing |
| \(\gamma_5\) | chirality matrix in the displayed Clifford basis |
| \(\Pi_\pm(p)\) | projectors onto \(\not p=\pm i m\) eigenspaces |

## Claims Established

- Massive spin is the irreducible representation label of the \(SU(2)\)
  little group.
- The covariant and delta-function normalizations are related by the
  boost/Jacobian factor \(N(\vec p)=(m/\omega_{\vec p})^{1/2}\).
- The delta-normalized Lorentz transformation of spin states carries the
  factor \(((\Lambda p)^0/p^0)^{1/2}\), while the covariantly normalized
  transformation does not.
- Wigner rotations govern Lorentz transformations of one-particle spin states.
- Wigner rotations obey a cocycle identity, and a different choice of
  standard boosts is a momentum-dependent change of spin frame over the mass
  shell.
- Projective rotation representations become honest representations on the
  universal cover; endpoint-fixed path homotopy gives the \(SU(2)\) lift, the
  \(2\pi\)/\(4\pi\) distinction, and the allowed spin labels
  \(j=0,\frac12,1,\ldots\).
- The source row-index convention for little-group matrices is recorded and
  reconciled with the column-vector convention used in the monograph.
- Spin-frame components of wavefunctions and dual external states transform
  oppositely, leaving amplitudes frame independent.
- Covariant field indices and one-particle spin labels are connected by
  intertwiners.
- Vacuum-to-particle wavefunctions obey an equivariance condition relating
  Lorentz covariance of the field to the Wigner transformation of particle
  spin.
- A field has nonzero overlap with a spin-\(j\) particle when its Lorentz
  representation contains spin \(j\) upon restriction to the little group.
- Spin-\(\frac12\) intertwiners obey momentum-space Dirac equations as a
  consequence of the Clifford realization of the Lorentz representation.
- In an explicit mostly-plus Clifford basis, the Pauli rotation
  \(\exp(-\ii\theta\sigma_3/2)\), rest spinors, \(\gamma_5\), and
  \(\mathcal V_R^\sigma=\gamma_5\mathcal U_R^\sigma\) reproduce the
  handwritten spinor convention.
- The displayed Clifford basis, \(\beta\)-pairing, spinor Lorentz generators,
  and \(\gamma_5\) agree with the chapter-local Weinberg-compatible
  convention dictionary.
- The \(\beta\)-pairing, delta-normalized spinor inner products, and spin
  sums are fixed with their signs and factors of \(p^0\); these identities
  supply the algebra for later spinorial LSZ.
- The 2026-05-27 formalization pass added labeled statements
  `def:massive-one-particle-spin-datum`,
  `def:massive-standard-rest-momentum-normalization`,
  `def:massive-wigner-rotation`, the massive Wigner transformation-law
  calculation, the massive-cover spin-label calculation, `def:massive-spin-frame`,
  `prop:massive-wigner-cocycle-spin-frame-change`,
  `prop:covariant-field-intertwiner-equivariance`, and
  `prop:massive-dirac-projectors-spin-sums`.
- `calculation-checks/massive_spin_checks.py` verifies the mass-shell
  Jacobian, Wigner cocycle, spin-frame unitary covariance, \(SU(2)\) central
  signs, and the explicit mostly-plus gamma-matrix projector and spin-sum
  algebra.

## Figure Requirements

- Double-cover diagram showing the lift from \(SO(3)\) to \(SU(2)\) and the
  \(2\pi\)/\(4\pi\) distinction.
- Endpoint-fixed path-homotopy diagram showing homotopic paths and the
  noncontractible \(2\pi\) loop whose square is contractible.

## Exclusions

- No Grassmann path integral.
- No canonical quantization of spinor fields.
- No detailed Weyl/Majorana construction; those belong in the next chapter.
- No massless little group or helicity; that begins after the massive spinor
  chapter.
