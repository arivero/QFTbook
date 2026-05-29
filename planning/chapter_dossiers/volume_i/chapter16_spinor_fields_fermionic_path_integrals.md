# Volume I, Chapter 16 Dossier: Spinor Fields, Fermionic Statistics, and Grassmann Path Integrals

## Source Placement

- Follows the massive-particle spin and spinor-intertwiner chapter.
- Develops the Dirac field operator, the CAR local algebra, Weyl and Majorana
  projections, finite-dimensional Berezin calculus, the Grassmann path
  integral, and the spinorial pole structure needed for external fermions.
- Precedes massless helicity, gauge redundancy, Maxwell theory, and QED.
- Source material used:
  - foundations transcript file, lines 6773--8175 in the current transcript
    source range,
    with handwritten pp. 165--189 checked on 2026-05-22;
  - source visual trace pages 166--189 for the Dirac/Weyl/Majorana,
    Grassmann mechanics, coherent-state path integral, spinor spectral pole,
    spinorial LSZ, and first four-fermion vertex block;
  - manuscript visual trace pages 286--298 for the spinor-Grassmann chapter;
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
- The Dirac adjoint, chirality matrix, Majorana conjugation matrix, and
  two-component sign conventions are fixed globally in
  `monograph/tex/volumes/volume_i/chapter16a_spinor_conventions.tex`.
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
| \(b_\sigma^\dagger,d_\sigma^\dagger\) | charged particle and antiparticle creation operators |
| \(a_\sigma^\dagger,c_\sigma\) | trial oscillators for the commutator/CAR comparison |
| \(\mathcal U^\sigma,\mathcal V^\sigma\) | delta-normalized spinor polarizations |
| \(\Delta_+\) | positive-frequency scalar two-point distribution |
| \(P_\pm\) | chiral projectors \((1\pm\gamma_5)/2\) |
| \(B\) | matrix implementing complex conjugation on gamma matrices |
| \(\Pi V\) | purely odd affine superspace with structure sheaf \(\Lambda(V^\vee)\) |
| \(R_{\overline 0}\oplus R_{\overline 1}\) | supercommutative test algebra |
| \(\operatorname{Ber}\) / Berezinian line | line of Berezinian densities |
| \(\Lambda_N\) | Grassmann algebra on \(N\) generators |
| \(\eta_a,\bar\eta_a\) | finite-dimensional Grassmann generators |
| \(\chi_a,\pi_a\) | constraints and canonical momenta |
| \(A\) | invertible matrix in a Berezin Gaussian integral |
| \(J,\bar J\) | Grassmann sources |
| \(\ket{\eta},\langle\!\langle\chi|\) | fermionic coherent ket and dual coherent bra |
| \(\beta_{\mathrm T}\) | Euclidean inverse temperature for the fermionic trace |
| \(S_F\) | free Dirac Feynman two-point function |
| \(Z_\psi\) | spinor one-particle pole residue |
| \(K_{\alpha\beta}{}^{\gamma\delta}\) | four-fermion vertex spinor-index kernel |
| \(p_!\) | finite-dimensional Berezin pushforward along a purely odd fiber |
| \(Q,Q^\dagger,H,I_W\) | supercharges, Hamiltonian, and Witten index |
| \(\widehat A(TM),\operatorname{ch}(E)\) | index-density characteristic classes |

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
- The chapter now explicitly includes a local spinor-convention section for the
  Weinberg-compatible gamma basis and the same-signature comparison with the
  Wess-Bagger-type chiral basis.
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
  the one-step overlap identities.
- The ordinary fermionic thermal trace yields anti-periodic Euclidean
  boundary conditions, while the supertrace with \((-1)^F\) yields periodic
  fermionic boundary conditions.
- Berezin integration over a finite odd fiber is formulated as a functorial
  pushforward \(p_!\) of Berezinian densities; staged integration is
  associativity of ordered coefficient extraction.
- In one-dimensional supersymmetric quantum mechanics with superpotential
  \(W\), the Hamiltonian \(H=\{Q,Q^\dagger\}/2\) pairs all positive-energy
  states by fermion parity, so the Witten index is the even minus odd
  dimension of the zero-energy subspace.
- For \(W(x)=mx^2/2\), \(m>0\), the even zero mode
  \(\exp(-mx^2/2)\) is square-integrable and the odd candidate
  \(\exp(mx^2/2)\) is not, giving \(I_W=1\); the oscillator supertrace
  gives the same result by an explicit geometric-series cancellation.
- The periodic-fermion worldline supertrace for a twisted spin Dirac operator
  is expanded in normal coordinates; finite-mode Gaussian determinant ratios
  give \(\widehat A(TM)\), the bundle curvature gives
  \(\operatorname{ch}(E)\), and the fermion zero-mode Berezin integral extracts
  the top-degree component of
  \(\widehat A(TM)\operatorname{ch}(E)\).
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
- The 2026-05-27 formalization pass added labeled statements
  `def:free-dirac-spinor-intertwiner-data`,
  `def:free-charged-dirac-field-car`,
  `prop:free-dirac-locality-selects-car`,
  `def:finite-fermionic-configuration-superspace`,
  `prop:finite-berezin-gaussian-contractions`,
  and the fermionic trace endpoint-sign calculation.  The purely odd
  Berezinian transformation and the one-mode coherent-state resolution are now
  recorded as coefficient-extraction/time-slicing prose rather than
  theorem-family claims.
- The 2026-05-29 anti-wrapper audit demoted the free Dirac equation and
  oscillator charge convention from theorem form to explanatory prose, because
  it is a direct consequence of the defining intertwiners and charge
  commutators rather than an independent result.
- The 2026-05-29 continuing anti-wrapper audit demoted the one-mode
  coherent-state resolution from proposition form to construction prose; the
  finite two-state Berezin calculation remains in the text.
- `calculation-checks/spinor_grassmann_checks.py` verifies the finite sign
  algebra behind the Dirac phase equations, \(U(1)\) charge convention, CAR
  locality sign, odd Dirac bracket, Berezinian inverse determinant, one-pair
  Berezin Gaussian, and coherent-state trace endpoint signs.
- The 2026-05-28 follow-up formalized the remaining long prose blocks:
  `def:dirac-weyl-majorana-local-spinor-data`,
  the chiral/Majorana Lorentz-covariance reduction paragraph,
  `def:finite-odd-first-order-mechanics`,
  `prop:odd-second-class-dirac-brackets`,
  `def:finite-grassmann-algebra-berezin-derivative`,
  `def:finite-berezin-pushforward`,
  `prop:finite-berezin-pushforward-functoriality`,
  `def:susy-qm-witten-index-datum`,
  harmonic supersymmetric oscillator index calculation,
  `def:twisted-dirac-index-periodic-worldline-datum`,
  `ex:periodic-fermion-worldline-index-density`,
  `def:free-dirac-functional-integral-datum`,
  paragraph "Free Dirac propagator as Feynman inverse",
  `def:isolated-spinor-one-particle-pole-datum`,
  `prop:locality-fixes-conjugate-spinor-pole-residue`,
  paragraph "Spinor mass-shell residue and external factors",
  `def:spinorial-lsz-pole-assignment`, and the worked paragraph
  "First four-fermion direct-minus-exchange vertex".

## Anti-Wrapper Audit

- 2026-05-29: demoted the first four-fermion direct-minus-exchange vertex from
  proposition/proof to a worked paragraph.  The sign derivation remains
  explicit because it is useful for fermionic Feynman rules, but it is a local
  first-order Wick-contraction calculation rather than theorem-level material.
- 2026-05-29 ninth pass: demoted the purely odd Berezinian
  inverse-determinant transformation from proposition form to algebra prose,
  keeping the locally super-ringed-space interpretation and the finite
  coefficient-extraction calculation explicit.

## Figure Requirements

- Two-state fermionic oscillator figure showing the creation and annihilation
  maps.
- Time-slicing figure for the coherent-state path integral, with \(\eta_n\)
  at slice endpoints and \(\chi_n\) on intervals.
- Spinorial LSZ residue figure for representative outgoing charge \(+\) and
  outgoing charge \(-\) pole extractions.
- Four-fermion direct/exchange contraction figure with the relative fermion
  sign displayed.

## Calculation Checks

- `calculation-checks/susy_qm_index_checks.py` verifies the harmonic SUSY-QM
  supertrace identity, zero-mode index count, two-variable Berezin Pfaffian
  extraction, and the \(\widehat A\)-series coefficients through degree six.
- `calculation-checks/spinor_grassmann_checks.py` verifies finite sign and
  normalization algebra for the spinor-field and Grassmann path-integral
  sections formalized on 2026-05-27.

## Exclusions

- No massless helicity representations.
- No Maxwell gauge constraints.
- No QED vertices or radiative corrections.
- No proof of the general spin-statistics theorem.
- No use of fermionic diagrams before the spinorial LSZ pole has been stated.
