# Volume III, Chapter 8 Dossier: Correlation Functions And Conformal Frames

## Logical Role

- Role in the monograph: classify scalar and spinning two- and three-point
  structures, introduce conformal frames for higher-point correlators, and
  relate radial inner products to two-point coefficients.
- Immediate predecessor: unitarity bounds and short multiplets.
- Immediate successor: operator product expansion.

## Definitions And Results

The chapter establishes:

- the use of the common vacuum \(\ket{\vac}\) only after Chapter 4 identifies
  the flat Poincare vacuum, conformal vacuum, and zero-energy cylinder ground
  state;
- Lemma `lem:vacuum-k-invariance-from-radial-spectrum`, deriving
  \(\widehat K_\mu\ket{\vac}=0\) from
  \(\widehat D_{\rm rad}\ket{\vac}=0\),
  \([\widehat D_{\rm rad},\widehat K_\mu]=-\widehat K_\mu\), and the
  nonnegative spectrum of \(\widehat D_{\rm rad}\);
- Definition `def:separated-euclidean-cft-correlator`, making the chapter's
  configuration space and separated-distribution status explicit;
- Proposition `prop:scalar-one-point-selection-rule`, proving the scalar
  one-point selection rule from translations and dilatations;
- conformally invariant coordinate combinations and cross-ratios;
- scalar two- and three-point functions from Ward identities;
- Theorem `thm:scalar-three-point-kinematics`, deriving the scalar
  three-point exponents from conformal-frame transitivity and inversion
  weights;
- spinning tensor structures with stated representation data;
- Definition `def:inversion-stt-parallel-transport` and Proposition
  `prop:spinning-two-point-structures`, formalizing inversion transport and
  the vector/STT two-point structures;
- the Osborn--Petkou parity-even stress-tensor three-point basis, including
  the explicit \(h^1,\ldots,h^5\) tensors, the three \(D\ge4\) structures,
  the conservation equations fixing dependent coefficients, and the
  three-dimensional Schouten degeneration to two parity-even structures;
- radial conjugation and BPZ-type bra construction from cylinder-time limits;
- Definition `def:ordered-four-point-conformal-frame`, Theorem
  `thm:four-point-cross-ratio-completeness`, and Proposition
  `prop:scalar-four-point-prefactor-covariance`, giving the ordered
  four-point frame, the residual stabilizer dimension count, and the scalar
  four-point prefactor covariance proof;
- conformal frames and residual stabilizer groups;
- positivity conditions on two-point coefficient matrices.

## Claims To Verify

1. Coordinate dependence of scalar correlators follows from translations,
   rotations, dilatations, and special conformal Ward identities.
2. Vacuum invariance in correlation-function formulas must refer back to the
   Chapter 4 vacuum-identification section rather than silently conflating the
   flat, conformal, and cylinder vacua.
3. Special conformal invariance of the vacuum must be derived from radial
   spectral positivity and the conformal commutator, not inserted as an
   independent assumption.
4. Tensor structures require explicit \(SO(D)\) representation data and are
   not determined by scalar formulas.
5. The radial inner product is positive after reflection positivity and the
   null quotient; two-point coefficient matrices are Gram matrices.
6. Angular coordinates on \(S^{D-1}\) are denoted by \(n\)-type symbols in
   sections where the vacuum \(\vac\) is also present.
7. The count of parity-even separated \(TTT\) structures is three only for
   \(D\ge4\); in \(D=3\) the Osborn--Petkou structures obey
   \(\mathcal I^{(1)}-\mathcal I^{(2)}+2\mathcal I^{(3)}=0\), leaving two
   parity-even structures before any parity-odd \(D=3\) structure is added.
8. The scalar-scalar-stress Ward coefficient uses the pointwise identity
   \(n^\mu n_\mu=1\) on the unit sphere to reduce
   \(n^\mu n^\nu(n_\mu n_\nu-\delta_{\mu\nu}/D)\) to \(1-1/D\).

## Figures

- Use figures only for conformal frames or residual stabilizer action.

## Checks

- Avoid numerical CFT data unless accompanied by a source policy or removed.
- Keep the distinction between separated-point correlators and contact-term
  extensions explicit.
- 2026-05-24 issue #291 pass: tied the \(TTT\) count to the
  Osborn--Petkou basis, displayed the collinear-frame independence check, and
  made the \(D=3\) two-structure relation explicit.
- 2026-05-24 issue #292 pass: expanded the scalar-scalar-stress Ward
  angular projection to show explicitly where \(n^\mu n_\mu=1\) enters.
- 2026-05-24 issue #295 pass: the chapter opening now points to
  Section `sec:flat-conformal-cylinder-vacua` before using the common vacuum
  in conformal Ward identities and radial cylinder limits.
- 2026-05-24 issue #296 pass: added Lemma
  `lem:vacuum-k-invariance-from-radial-spectrum`, proving
  \(\widehat K_\mu\ket{\vac}=0\) from the radial spectrum condition and
  \([\widehat D_{\rm rad},\widehat K_\mu]=-\widehat K_\mu\).
- 2026-05-24 issue #395 pass: the displayed \(D=3\) parity-even \(TTT\)
  two-structure count now carries explicit references to Maldacena--Zhiboedov
  and to the Costa--Penedones--Poland--Rychkov / Costa--Hansen--Penedones--
  Trevisani spinning-correlator technology.
- 2026-05-28 density/formalization pass: promoted separated correlators,
  one-point selection, spinning two-point structures, scalar three-point
  kinematics, four-point frame completeness, and four-point prefactor
  covariance to formal environments.  Added
  `calculation-checks/cft_correlator_kinematics_checks.py` to guard the
  three-point exponent algebra, four-point inversion weights, and residual
  four-point quotient dimension.
