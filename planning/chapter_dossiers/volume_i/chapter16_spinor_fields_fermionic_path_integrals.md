# Volume I, Chapter 16 Dossier: Spinor Fields, Fermionic Statistics, and Grassmann Path Integrals

## Source Placement

- Follows the massive-particle spin and spinor-intertwiner chapter.
- Develops the Dirac field operator, the CAR local algebra, Weyl and Majorana
  projections, finite-dimensional Berezin calculus, the Grassmann path
  integral, and the spinorial pole structure needed for external fermions.
- Precedes massless helicity, gauge redundancy, Maxwell theory, and QED.
- Source material used:
  - `transcription/tex/253a/foundations.tex`, roughly lines 6773--8175,
    with handwritten pp. 165--189 checked on 2026-05-22;
  - source visual trace
    `monograph/tex/build/source_visual_trace/253a_trace-166.png`--`253a_trace-189.png`
    for the Dirac/Weyl/Majorana, Grassmann mechanics, coherent-state path
    integral, spinor spectral pole, spinorial LSZ, and first four-fermion
    vertex block;
  - manuscript visual trace
    `monograph/tex/build/manuscript_visual_trace/chapter16_spinor_grassmann-286.png`--`chapter16_spinor_grassmann-298.png`;
  - `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
    section "The path integral", subsection "Path integral with
    Grassmann-odd field variables", used to sharpen the coherent-state
    completeness relation, ordered Berezin measure, and thermal
    anti-periodic boundary-condition derivation;
  - `references/sound_references/straumann_poincare_representations_0809.4942.pdf`
    and text sidecar for free-field representation and spin-statistics
    context;
  - `references/sound_references/fredenhagen_rejzner_paqft_1208.1428.pdf`
    and text sidecar for the CAR and functional-integral setting.

## External Reference Boundary

- The chapter verifies locality for the free Dirac field built from the
  spinor one-particle data of Chapter 15.
- The ordinary-commutator trial field is included only as a locality check:
  it shows the nonvanishing spacelike scalar part and fixes the CAR sign
  used in the actual local spinor algebra.
- The full spin-statistics theorem is cited only as a theorem-level statement
  under Wightman-type assumptions; its proof is not reproduced.
- The Berezin path integral is constructed first in finite dimension and then
  used as the regulated model for the continuum notation.
- Spinorial LSZ and the first fermionic vertex appear only after the
  nonperturbative scattering and LSZ framework has already been established.

## Framework

- Four-dimensional Minkowski spacetime with mostly-plus metric.
- Gamma matrices obey \(\{\gamma^\mu,\gamma^\nu\}=2\eta^{\mu\nu}\).
- Spinor fields are operator-valued distributions on a common dense domain,
  with a fermion-parity grading.
- Fermionic path-integral variables are odd coordinates on finite-dimensional
  configuration superspaces in a regulator, understood as locally
  super-ringed spaces or through functor-of-points language.
- Berezin integration is an algebraic functional on Berezinian densities, not
  a Borel measure; continuum fermionic path integrals are formal regulated
  limits of finite-dimensional Berezin integrals.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\psi_\alpha,\bar\psi^\alpha\) | Dirac spinor field and Dirac adjoint |
| \(\beta\) | \(\ii\gamma^0\), used in \(\bar\psi=\psi^\dagger\beta\) |
| \(b_\sigma^\dagger,d_\sigma^\dagger\) | creation operators for charged spin-\(\frac12\) particle and antiparticle |
| \(a_\sigma^\dagger,c_\sigma\) | trial oscillators used only to compare ordinary commutators with CAR |
| \(\mathcal U^\sigma,\mathcal V^\sigma\) | delta-normalized spinor polarizations from Chapter 15 used in the sign check |
| \(\Delta_+\) | positive-frequency scalar two-point distribution |
| \(P_\pm\) | chiral projectors \((1\pm\gamma_5)/2\) |
| \(B\) | matrix implementing complex conjugation on gamma matrices |
| \(\Pi V\) | purely odd affine superspace with structure sheaf \(\Lambda(V^\vee)\) |
| \(R_{\overline 0}\oplus R_{\overline 1}\) | supercommutative test algebra used for functor-of-points language |
| \(\operatorname{Ber}\) / Berezinian line | line whose densities are integrated by Berezin integration |
| \(\Lambda_N\) | Grassmann algebra on \(N\) generators |
| \(\eta_a,\bar\eta_a\) | finite-dimensional Grassmann generators |
| \(\chi_a,\pi_a\) | second-class constraints and canonical momenta in finite-dimensional Grassmann mechanics |
| \(A\) | invertible matrix in a Berezin Gaussian integral |
| \(J,\bar J\) | Grassmann sources |
| \(\ket{\eta},\langle\!\langle\chi|\) | fermionic coherent ket and dual coherent bra |
| \(\beta_{\mathrm T}\) | Euclidean inverse temperature for the fermionic trace |
| \(S_F\) | free Dirac Feynman two-point function |
| \(Z_\psi\) | spinor one-particle pole residue |
| \(K_{\alpha\beta}{}^{\gamma\delta}\) | local spinor-index kernel of the first four-fermion vertex |

## Claims Established

- The free Dirac field built from spin-\(\frac12\) one-particle data is local
  when its creation and annihilation operators obey CAR.
- If the same spinor mode expansion is equipped with ordinary commutators,
  the field commutator contains
  \(m(\Delta_+(x-y)+\Delta_+(y-x))\), which is nonzero at spacelike
  separation; hence the commutator sign fails locality.
- Its anticommutator is a Dirac differential operator applied to the
  Pauli--Jordan distribution, hence has causal support.
- Chiral and Majorana spinor fields are Lorentz-covariant reductions of the
  Dirac representation under stated algebraic conditions.
- The matrix \(B=\gamma_2\) in the displayed gamma basis implements charge
  conjugation, and the Majorana condition is checked directly against
  Lorentz covariance and chirality projection.
- Fermionic operator fields and fermionic path-integral variables are distinct
  objects: the former are Hilbert-space operator-valued distributions with
  graded locality, while the latter are Grassmann-odd coordinates on a
  supergeometric configuration object.
- A finite Grassmann field configuration space is a locally super-ringed space,
  such as \((\{\ast\},\Lambda(V^\vee))\) in the purely odd affine case, and
  the functor of points assigns \(R_{\overline1}\otimes V\) to a
  supercommutative test algebra \(R\).
- Berezin integration extracts the top coefficient relative to an ordered
  Berezinian element and transforms with the inverse determinant in odd
  coordinates; it is not a countably additive Borel measure.
- Finite-dimensional Grassmann first-order mechanics has second-class
  constraints; the Dirac bracket gives
  \(\{\eta_\alpha,\eta_\beta\}_{\mathrm D}
    =\frac12(M^{-1})_{\alpha\beta}\).
- The \(N=2\) Grassmann oscillator quantizes to the two-state Hilbert space
  with Hamiltonian eigenvalues \(-\omega/4\) and \(+\omega/4\).
- Berezin integration is the finite-dimensional algebraic operation whose
  Gaussian integral produces determinants and fermionic Wick signs.
- The Grassmann path integral is obtained from coherent-state resolutions of
  identity for a two-state fermionic system, including the endpoint signs in
  the elementary overlap identities.
- The ordinary fermionic thermal trace yields anti-periodic Euclidean
  boundary conditions, while the supertrace with \((-1)^F\) yields periodic
  fermionic boundary conditions.
- The Dirac propagator is the inverse of \(\not\partial+m\) with the Feynman
  boundary value.
- In an interacting theory with an isolated charged massive spin-\(\frac12\)
  pole, the spinor two-point function has a pole residue determined by the
  spinor intertwiners; spinorial LSZ external factors are those residues.
- Locality of the isolated spinor pole fixes the equality of the charge
  conjugate residues in the pole part of the anticommutator.
- The first four-fermion interaction
  \(-\frac g2(\bar\psi\psi)^2\) gives the direct-minus-exchange vertex
  \(K_{\alpha\beta}{}^{\gamma\delta}
  =\ii g(\delta_\alpha{}^\gamma\delta_\beta{}^\delta
  -\delta_\alpha{}^\delta\delta_\beta{}^\gamma)\).

## Figure Requirements

- Two-state fermionic oscillator figure showing the creation and annihilation
  maps.
- Time-slicing figure for the coherent-state path integral, with \(\eta_n\)
  at slice endpoints and \(\chi_n\) on intervals.
- Spinorial LSZ residue figure for representative outgoing charge \(+\) and
  outgoing charge \(-\) pole extractions.
- Four-fermion direct/exchange contraction figure with the relative fermion
  sign displayed.

## Exclusions

- No massless helicity representations.
- No Maxwell gauge constraints.
- No QED vertices or radiative corrections.
- No proof of the general spin-statistics theorem.
- No use of fermionic diagrams before the spinorial LSZ pole has been stated.
