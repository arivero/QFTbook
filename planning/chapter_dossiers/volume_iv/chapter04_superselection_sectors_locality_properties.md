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
- `u`, `\rho`, `\mathcal F_{\rm alg}`: charged unitary, order-\(N\)
  localized automorphism, and crossed-product field core for the pointed
  invertible-sector example.
- `\Hilb_{\rm HS}`, `\pi`, `S`, `J`, `\Delta`: finite Hilbert-Schmidt
  standard-form model, left representation, Tomita operator, modular
  conjugation, and modular operator.
- `u_t=[D\psi:D\omega]_t`: Connes cocycle derivative comparing two faithful
  normal states in standard form.

## Claim Ledger

- Separates superselection-sector statements from perturbative particle
  language.
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

## Figure Ledger

- No figure obligations are currently recorded for this dossier beyond the
  chapter's manuscript figures.

## Calculation Checks

- `calculation-checks/dhr_dr_reconstruction_checks.py` verifies the finite
  pointed \(\mathbb Z/N\mathbb Z\) diagnostic for Doplicher--Roberts
  reconstruction: tensor automorphisms form \(\mu_N\), the fixed-degree
  projection keeps exactly degree zero, the crossed-product field core is
  associative with the stated involution and gauge-fixed algebra, and the
  finite nonabelian \(S_3\) diagnostic has the correct representation law,
  faithful standard representation, character-ring tensor products, and
  Haar projection onto the trivial isotypic part.
- `calculation-checks/tomita_standard_form_checks.py` verifies the finite
  matrix-algebra standard-form formulae: \(S=J\Delta^{1/2}\), modular
  eigenvalues on matrix units, \(J L_A J=R_{A^*}\), modular automorphism by
  density-matrix conjugation, the KMS boundary relation for the inverse
  modular flow in the chapter convention, and the noncommuting finite-density
  Connes cocycle identities.
- `calculation-checks/kms_foundation_checks.py` verifies the finite
  Gibbs-trace KMS strip boundary relation used as the trace-class model for
  Definition~\ref{def:kms-state}.

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
