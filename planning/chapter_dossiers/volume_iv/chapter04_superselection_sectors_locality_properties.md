# Volume IV Chapter 04 — Superselection Sectors and Locality Properties

## Source Position

This chapter develops the operator-algebraic meaning of sectors, split
inclusions, relative entropy, modular localization, and locality refinements
inside the foundational nonperturbative volume.  It is a bridge from local-net
axioms to charge-sector structure and sharp-algebra diagnostics.

## Notation Inventory

- `\mathcal A(O)`: local von Neumann algebra attached to a spacetime region.
- `\Omega`: vacuum vector for the represented net.
- `\rho`, `\sigma`: normal states or sector endomorphisms, depending on the
  subsection context.
- `S(\rho|\sigma)`: Araki relative entropy.
- `\Delta`, `J`: modular operator and modular conjugation.
- `DHR`: Doplicher--Haag--Roberts localized transportable sector datum.
- `X_q`, `\mu_N`, `\mathcal F_q`: pointed finite-sector object, recovered
  finite compact group, and charged degree in the finite DR diagnostic.
- `L_n`, `\mathbb C[z,z^{-1}]`, `E_{U(1)}`: compact \(U(1)\)
  character, Laurent representative-function algebra, and Haar expectation
  in the compact abelian Tannakian diagnostic.
- `f_{\ell,v}^W`, `\operatorname{Pol}(G)`, `\Delta_{\rm H}`,
  `\epsilon`, `S`, `h_G`: compact Peter--Weyl matrix coefficient,
  representative-function Hopf algebra, Hopf coproduct, counit, antipode, and
  Haar functional in the compact-group coordinate-algebra layer.
- `u`, `\rho`, `\mathcal F_{\rm alg}`: charged unitary, order-\(N\)
  localized automorphism, and crossed-product field core for the pointed
  invertible-sector example.
- `\Hilb_{\rm HS}`, `\pi`, `S`, `J`, `\Delta`: finite Hilbert-Schmidt
  standard-form model, left representation, Tomita operator, modular
  conjugation, and modular operator.
- `u_t=[D\psi:D\omega]_t`: Connes cocycle derivative comparing two faithful
  normal states in standard form.
- `e_+`, `W_R(a)`: future-right lightlike vector and inward translated
  right wedge used to fix the half-sided modular-inclusion sign.
- `\pi_{\sigma_-,\sigma_+}`, `B_L(R)`, `B_R(R)`, `m_\sigma`: soliton
  representation, far-tail order-parameter observables, and phase values
  used in the DHR kink-sector diagnostic.

## Claim Ledger

- Separates superselection-sector statements from perturbative particle
  language.
- Makes the Haag-duality input to localized endomorphisms explicit:
  localization outside \(\mathcal O\) first gives membership in the dual net
  \(\mathcal R^d(\mathcal O)\); Haag duality is the structural hypothesis that
  places images and intertwiners in the assigned local observable algebra.
- Treats relative entropy as a sharp-algebra quantity rather than a finite
  cutoff entropy slogan.
- Keeps split inclusions and regulator approximations logically distinct.
- Uses modular-localization statements only under their stated algebraic
  hypotheses.
- Anchors the Doplicher--Roberts compact-group output in a finite pointed
  sector calculation: tensor automorphisms of the fiber functor are characters
  and averaging over the reconstructed group projects to neutral degree.
- Adds a finite nonabelian \(S_3\) diagnostic for the
  Doplicher--Roberts/Tannakian output: the standard representation is
  faithful, the character ring gives
  \(V\otimes V\simeq 1\oplus\epsilon\oplus V\), and Haar averaging kills
  nontrivial matrix coefficients rather than merely nonzero Abelian degree.
- Adds the finite \(S_3\) regular charged-coordinate core
  \(\operatorname{Fun}(S_3)\): right translation rotates matrix-coefficient
  columns as charged multiplets, Haar expectation gives the fixed observable
  constants, and pointwise multiplication is tensor-product multiplication of
  matrix coefficients.
- Adds the compact abelian \(U(1)\) completion of the pointed diagnostic:
  tensor natural automorphisms of the forgetful functor are phases
  \(u_n=\lambda^n\), the representative-function algebra is
  \(\mathbb C[z,z^{-1}]\subset C(U(1))\), and Haar expectation keeps exactly
  charge zero.
- Adds the compact Peter--Weyl coordinate algebra layer: finite-dimensional
  unitary representation matrix coefficients span \(\operatorname{Pol}(G)\),
  tensor products give multiplication, group multiplication gives the Hopf
  coproduct, and Haar integration projects to the trivial block.  This is the
  compact coordinate algebra produced after the DHR hypotheses and fiber
  functor have been constructed; it is not presented as a proof of those
  local-QFT hypotheses.
- Adds the local charged-field-core assembly behind
  Doplicher--Roberts reconstruction: for a double cone \(\mathcal O\), the
  algebraic span of \(A\psi_{\rho,i}^{\mathcal O}\) has multiplication
  \((A\psi_{\rho,i})(B\psi_{\sigma,j})
  =A\rho(B)\psi_{\rho,i}\psi_{\sigma,j}\), Haag duality keeps
  \(\rho(B)\) local, fusion decomposes the product into irreducible charged
  blocks, conjugate sectors control the involution, Haar expectation recovers
  \(\mathcal R(\mathcal O)\), and charged locality is distinguished from
  observable locality.
- Adds a constructive kink-sector diagnostic: if a sector with far-left and
  far-right order-parameter tail limits were localized in a bounded DHR
  region relative to a single vacuum phase, DHR equivalence on the spacelike
  complement would force the two tail values to equal that vacuum value.  A
  genuine kink with distinct asymptotic phases is therefore a solitonic
  boundary-condition sector, not a bounded-region DHR charge unless an
  additional localization theorem is proved.
- Constructs the finite pointed field-algebra core as a crossed product
  \(\mathcal A\rtimes_\rho\mathbb Z_N\), verifies multiplication,
  involution, gauge action, fixed algebra, and sector implementation.
- Works out the finite-dimensional Tomita--Takesaki standard form for a
  faithful matrix state as an example, including cyclic/separating
  standardness, the explicit Tomita polar decomposition, commutant
  identification, modular automorphisms, and the sign relating modular flow
  to the chapter's KMS convention.
- Works out the finite-dimensional Connes cocycle model as an example:
  \(\Delta_{\psi|\omega}^{it}\Delta_\omega^{-it}\) is left multiplication by
  \(u_t=\rho_\psi^{it}\rho_\omega^{-it}\), and this algebra unitary satisfies
  the cocycle law and implements the change of modular flow.
- Works out trace-class Gibbs states as a finite/semifinite model for the
  KMS strip condition, while keeping the modular KMS theorem as the
  operator-algebraic statement relevant to type-III local QFT algebras.
- Adds a free bosonic Fock phase-space benchmark for the
  Buchholz--Wichmann nuclearity bound: the finite-volume occupation-number
  product formula and lattice shell estimate give
  \(\log Z_B(\beta,L)\le C\beta^{-(D-1)}\), clarifying the mode-counting
  scale behind the local nuclearity map without replacing the split theorem.
- Explains the operational content of a split inclusion by constructing normal
  product states for \(\mathcal R(\mathcal O_1)\) and
  \(\mathcal R(\mathcal O_2)'\) after spatially representing the type-I
  interpolant as \(\mathcal B(\mathcal K)\otimes 1\).
- Expands the nuclearity-to-split theorem boundary by separating Banach
  nuclearity from von-Neumann normality: the text now identifies the summable
  separated normal functionals on
  \(\mathcal R(\mathcal O_1)\bar\otimes\mathcal R(\mathcal O_2)'\) as the
  actual bridge to the Doplicher--Longo split criterion, and explains why the
  positive collar, locality, and spectral condition are needed beyond the
  formal nuclear decomposition.
- Verifies the right-wedge light-ray modular-inclusion sign in the chapter's
  Bisognano--Wichmann convention: for \(W_R(a)=W_R+a e_+\),
  \(\sigma_t^{W_R}\mathcal R(W_R(a))
   =\mathcal R(W_R(e^{-2\pi t}a))\), so the inward future-lightlike translate
  is left half-sided in the stated definition.
- Identifies the physical light-ray translation which realizes the abstract
  Borchers--Wiesbrock affine representation in a Poincare-covariant net:
  with \(U(x)=\exp(i x^\mu P_\mu)\) and mostly-plus metric,
  \(U(ae_+)=\exp[-ia(P^0-P^1)]\) and \(P^0-P^1\ge0\) follows directly from
  the joint spectrum condition.  This fixes the Stone sign convention without
  replacing the converse Borchers--Wiesbrock reconstruction theorem.
- Adds a finite-dimensional diagnostic for half-sided modular inclusions: a
  finite-dimensional injective endomorphism of the subspace \(\mathcal N\) is
  automatically onto, so half-sided modular inclusion collapses to ordinary
  modular invariance; the Borchers--Wiesbrock translation semigroup is thereby
  isolated as an infinite-dimensional standard-subspace phenomenon.

## Figure Ledger

- No figure obligations are currently recorded for this dossier beyond the
  chapter's manuscript figures.

## Calculation Checks

- `calculation-checks/dhr_dr_reconstruction_checks.py` verifies the finite
  pointed \(\mathbb Z/N\mathbb Z\) diagnostic for Doplicher--Roberts
  reconstruction: tensor automorphisms form \(\mu_N\), the fixed-degree
  projection keeps exactly degree zero, the crossed-product field core is
  associative with the stated involution and gauge-fixed algebra, the local
  charged-field-core convention \(\rho^q(A)u^q=u^qA\) holds, conjugation by
  \(u^q\) recovers \(\rho^q\), the compact \(U(1)\) Laurent charge-lattice
  diagnostic has the stated multiplication,
  involution, Haar projection, and tensor-exponent additivity, and the
  finite nonabelian \(S_3\) diagnostic has the correct representation law,
  faithful standard representation, character-ring tensor products, and
  Haar projection onto the trivial isotypic part.  It also verifies the
  \(S_3\) regular charged-coordinate core: right translation of matrix
  coefficients, Haar expectation onto constants, and the exterior-square
  sign representation.  The same finite \(S_3\) coefficient system checks
  the Peter--Weyl Hopf coordinate algebra: matrix coefficients span
  \(\operatorname{Fun}(S_3)\), the coproduct/counit/antipode identities hold
  pointwise, Haar is left and right invariant, and multiplication is
  compatible with the group-law coproduct.
- `calculation-checks/tomita_standard_form_checks.py` verifies the finite
  matrix-algebra standard-form formulae: \(S=J\Delta^{1/2}\), modular
  eigenvalues on matrix units, \(J L_A J=R_{A^*}\), modular automorphism by
  density-matrix conjugation, the KMS boundary relation for the inverse
  modular flow in the chapter convention, and the noncommuting finite-density
  Connes cocycle identities.
- `calculation-checks/kms_foundation_checks.py` verifies the finite
  Gibbs-trace KMS strip boundary relation used as the trace-class model for
  Definition~\ref{def:kms-state}.
- `calculation-checks/free_fock_nuclearity_checks.py` verifies the
  finite-mode bosonic product formula, the sup-norm lattice shell count used
  in the phase-space estimate, and finite-cutoff samples of the
  \(\beta^{D-1}\log Z_B\) scaling bound.
- `calculation-checks/split_nuclearity_normality_checks.py` verifies the
  finite split-product and nuclearity-normality algebra: tensor density
  matrices give normal product states, positivity holds on \(C^*C\), and a
  finite-rank nuclear map gives the separated bilinear expansion that models
  the infinite split proof.
- `calculation-checks/unruh_boost_geometry_checks.py` verifies the
  complex-boost and wedge-geometry signs used here and in Volume XII,
  including the \(i\pi\) right-to-left wedge map and the lightlike
  half-sided-inclusion convention
  \(\Delta^{it}=U(\Lambda_R(-2\pi t))\), and the mostly-plus sign
  \(U(ae_+)=\exp[-ia(P^0-P^1)]\) for the positive physical light-ray
  generator.

## Audit Notes

- 2026-05-29 eighth anti-wrapper pass: demoted the finite-dimensional
  first-variation identity for relative entropy from proposition form to a
  calculation paragraph.  The AQFT substance remains the regulator/split
  inclusion passage and the insistence that Araki relative entropy is the
  primary sharp-algebra object.
- 2026-05-30 DHR/DR proof-boundary pass: expanded the reconstruction
  discussion after the Doplicher--Roberts quoted theorem.  The chapter now
  separates the QFT-specific burden (DHR localization, transportability, Haag
  duality, symmetric exchange, conjugates, finite statistics) from the
  Tannakian compact-group output, displays the charged-field intertwining and
  Cuntz-type relations, and records why long-range Gauss-law, Wilson-line,
  infraparticle, and confining sectors require localization categories beyond
  bounded-region DHR sectors.
- 2026-05-30 finite pointed DR diagnostic pass: added the
  \(\mathbb Z/N\mathbb Z\) pointed category calculation after the
  Doplicher--Roberts theorem boundary and paired it with an exact modular
  arithmetic calculation check.
- 2026-05-30 pointed crossed-product field-algebra pass: expanded the finite
  pointed diagnostic into an explicit \(\mathcal A\rtimes_\rho\mathbb Z_N\)
  field-core example and extended the calculation check to cover
  associativity, involution, and fixed-point projection.
- 2026-05-30 nonabelian DR diagnostic pass: added an \(S_3\) representation
  category check after the Doplicher--Roberts theorem boundary.  The new text
  separates the finite visible calculation (faithful standard representation,
  tensor-product character ring, Haar killing of nontrivial matrix
  coefficients) from the deep Tannakian converse that every tensor natural
  automorphism is evaluation at a group element.
- 2026-05-31 finite nonabelian DR field-core pass: added the
  \(\operatorname{Fun}(S_3)\) regular charged-coordinate model, making visible
  how matrix coefficients transform under the reconstructed group, how Haar
  expectation recovers observables, and how multiplication realizes
  tensor-product fusion before the analytic DHR localization burden is added.
- 2026-06-01 finite Tannakian converse pass: added the
  \(\operatorname{Fun}(G)\) Peter--Weyl reconstruction argument showing that a
  left-equivariant unital \(*\)-automorphism of the finite regular algebra is
  a right translation \(x\mapsto xh\), hence that a tensor natural
  automorphism of the forgetful fiber functor is evaluation at a unique group
  element in the finite-group case.  The DHR/DR theorem boundary is now
  narrowed to the compact completion and the local-QFT construction of the
  sector category and field algebra.
- 2026-06-01 local DR field-core pass: added the local algebraic field-core
  construction between the DR theorem statement and the finite diagnostics.
  The new text explains which part is formal algebra forced by the
  intertwining relation, where Haag duality enters the product, how fusion and
  conjugates close the core, why Haar expectation recovers the observable
  local algebra, and why the analytic completion/locality theorem remains the
  nontrivial field-algebra reconstruction boundary.
- 2026-05-30 Bisognano--Wichmann proof-mechanism pass: added the Wightman
  polynomial-core/Tomita-operator setup, the complex-boost strip function,
  the spectral-condition tube input, the locality step at imaginary boost
  \(\ii\pi\), the \(2\pi\)-KMS boundary relation for wedge boosts, and the
  polar-decomposition route to the modular conjugation.  This strengthens the
  quoted theorem boundary without claiming that the full BW theorem has been
  reproved from bare AQFT axioms.
- 2026-05-30 Bisognano--Wichmann dequote pass: removed the wedge BW
  `quotedtheorem` wrapper.  The general theorem is now an explicit boundary
  remark, while the local proved result is a theorem on the Wightman
  polynomial-core wedge KMS strip.  The proof spells out the mostly-plus
  tube-analyticity damping sign, the complex-boost wedge map, graded locality,
  and the remaining closed-Tomita-operator domain theorem that is still part
  of the external BW boundary.
- 2026-05-30 nuclearity/split mechanism pass: expanded the phase-space
  theorem discussion with the normal tensor-product criterion for split
  inclusions, the way energy-damped nuclearity controls bilinear functionals
  on \(\mathcal M_1\odot\mathcal M_2'\), the role of the positive collar in
  analytic imaginary-time translation, the distinction between one-scale
  nuclearity and uniform small-\(\beta\) phase-space bounds, and the separate
  hypotheses behind type-\(\mathrm{III}_1\) sharp local algebras.
- 2026-05-30 split-criterion boundary tightening: separated the elementary
  direction from a type-I interpolant to a normal tensor-product
  representation from the deep Doplicher--Longo converse used by the
  nuclearity-to-split theorem.
- 2026-05-30 Borchers--Wiesbrock proof-mechanism pass: clarified
  standardness for half-sided modular inclusions, introduced the associated
  standard real subspaces, explained how half-sidedness becomes an invariant
  modular-dilation condition on those subspaces, and separated the deep
  construction of the positive translation group from the elementary
  differentiation that gives the displayed commutator.
- 2026-05-30 modular-theory quoted-theorem expansion pass: expanded the
  Tomita--Takesaki and Connes cocycle quoted-theorem boundaries.  The chapter
  now records the two-core \(S_0/F_0\) adjoint mechanism, the left Hilbert
  algebra multiplier route to modular invariance and \(J\mathcal R J\), and
  the relative-Tomita/standard-form mechanism behind Connes' cocycle relation.
- 2026-05-30 finite standard-form pass: inserted a fully proved
  finite-dimensional Tomita--Takesaki model for a faithful matrix state and
  paired it with `tomita_standard_form_checks.py`.
- 2026-05-30 finite Connes cocycle pass: promoted the finite type-I cocycle
  check from a remark to a proved proposition and extended
  `tomita_standard_form_checks.py` to verify the relative modular product,
  cocycle law, and modular-flow implementation in a noncommuting density
  example.
- 2026-05-30 modular finite-example anti-wrapper pass: demoted the finite
  Tomita standard-form and finite Connes cocycle blocks from proposition form
  to examples.  The calculations and companion checks remain, but the text
  now presents them as finite type-I normalization models for the quoted
  operator-algebraic theorems rather than theorem-level QFT results.
- 2026-05-30 finite Gibbs KMS anti-wrapper pass: demoted the trace-class
  Gibbs KMS block from proposition form to an example.  The strip
  verification remains explicit, but theorem-family rank is reserved for the
  modular KMS property, where Tomita--Takesaki theory replaces trace
  cyclicity in type-III local algebras.
- 2026-05-30 free Fock nuclearity benchmark pass: added the finite-volume
  bosonic occupation-number product formula and shell-count estimate
  \(\log Z_B\le C\beta^{-(D-1)}\) before the nuclearity/split quoted theorem,
  with a paired calculation check.  The text explicitly keeps the local
  split theorem as the operator-algebraic input beyond the global box trace.
- 2026-05-30 right-wedge half-sided sign pass: expanded the
  Borchers--Wiesbrock example so the inward lightlike translate of the right
  wedge is explicitly shown to be left half-sided with the chapter's
  \(\Delta^{it}=U(\Lambda_R(-2\pi t))\) convention, and extended the boost
  geometry calculation check to guard this sign.
- 2026-05-31 finite-dimensional half-sided diagnostic pass: inserted the
  rank argument showing that half-sided modular invariance is automatically
  two-sided in finite dimension, isolating the nontrivial
  Borchers--Wiesbrock content in infinite-dimensional standard-subspace
  geometry rather than in the displayed commutator.
- 2026-06-01 physical light-ray translation pass: aligned the
  Borchers--Wiesbrock Stone sign with the monograph's mostly-plus Poincare
  convention, defined \(P_+^{\rm phys}=P^0-P^1\), proved positivity from the
  joint spectrum condition, and showed that \(U(ae_+)\) satisfies the same
  affine modular covariance as the left half-sided version of the abstract
  translation reconstructed from a half-sided modular inclusion.  The pass
  also corrected the right/left dilation-factor assignment in the quoted
  Borchers--Wiesbrock statement so it matches the chapter's definition of
  half-sidedness.
- 2026-05-31 DHR kink-sector diagnostic pass: inserted a constructive
  broken-phase test showing that weak far-tail order-parameter limits are
  incompatible with bounded-region DHR localization unless the two asymptotic
  phases equal the reference vacuum phase.  This makes the DHR/DR theorem
  boundary concrete in an interacting low-dimensional setting.
- 2026-05-31 split product-state pass: added the explicit spatial
  construction of normal product states across
  \(\mathcal R(\mathcal O_1)\) and \(\mathcal R(\mathcal O_2)'\) from a
  type-I interpolant, sharpening the meaning of split independence before the
  later nuclearity-to-split theorem boundary.
- 2026-05-31 split/nuclearity normality pass: expanded the
  nuclearity-to-split mechanism beyond phase-space counting by making the
  separated normal predual functionals visible.  The text now warns that an
  arbitrary Banach nuclear decomposition need not have normal coefficient
  functionals and identifies the collar/locality/spectral-condition estimates
  as the actual load-bearing analytic step.
- 2026-06-01 compact \(U(1)\) Tannakian completion pass: added the
  charge-lattice representative-function algebra between the finite
  \(\mathbb Z/N\mathbb Z\) and \(S_3\) diagnostics.  This makes the compact
  analytic completion visible in the simplest infinite compact group while
  keeping the DHR field-algebra reconstruction as the QFT theorem boundary.
- 2026-06-01 compact Peter--Weyl coordinate-algebra pass: added the compact
  representative-function Hopf \(*\)-algebra \(\operatorname{Pol}(G)\) after
  the finite Tannakian converse, with product, coproduct, counit, antipode,
  Haar functional, Peter--Weyl density, and the reconstruction of \(G\) from
  the \(C^*\)-completion kept distinct from the DHR local-QFT theorem
  boundary.
- 2026-06-01 Haag-duality DHR-containment pass: expanded the endomorphism
  setup so the use of Haag duality is displayed by the commutant calculation
  \(\rho(A)\in\mathcal R(\mathcal O_1^\perp)'\) and the corresponding
  intertwiner calculation.  The text now states that without Haag duality the
  construction naturally lands in the dual net.
