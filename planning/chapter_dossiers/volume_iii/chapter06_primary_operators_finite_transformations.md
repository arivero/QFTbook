# Volume III, Chapter 6 Dossier: Primary Operators And Finite Transformations

## Logical Role

- Role in the monograph: derive primary-operator transformation laws from
  radial module data, source-contact conventions, and conformal-current Ward
  identities.
- Immediate predecessor: conformal charges and Ward identities.
- Immediate successor: unitarity bounds and short multiplets.

## Definitions And Results

The chapter establishes:

- spin representations \(\rho\) of \(SO(D)\), the vector space \(V_\rho\),
  and infinitesimal spin matrices \(S_{\mu\nu}\);
- primary state data at the origin:
  \(K_\mu|\mathcal O\rangle=0\), radial dimension \(\Delta\), and spin under
  rotations;
- the terminology distinction between global primaries/quasi-primaries and
  Virasoro primaries in \(D=2\), together with the statement that in \(D\ge3\)
  the finite conformal algebra supplies the intrinsic primary notion used in
  this volume;
- conformal generalized Verma modules
  \(M(\Delta,\rho)=U(\mathfrak g_{\mathbb C})
  \otimes_{U(\mathfrak l\oplus\mathfrak n_-)}V_{\Delta,\rho}\), their
  level spaces \(\operatorname{Sym}^n(\mathbb C^D)\otimes V_\rho\), singular
  vectors, null submodules, irreducible quotients, and the relation to the
  finite conformal-algebra Kac determinant and BGG organization;
- translations from the origin and the descendant Taylor expansion;
- sources \(\eta^a\in V_\rho^\vee\), their conformal source variation, and
  the induced contact operator on insertions;
- the spinful local conformal-current Ward identity;
- infinitesimal transformations for translations, rotations, dilatations, and
  special conformal transformations;
- finite transformation laws, including the one-parameter-flow verification
  from the infinitesimal contact operator, elementary-generator sign checks,
  tensor index conventions, and the restriction to separated points;
- inversion, including the extra representation choice needed for spin.
- descendant transformation laws as direct consequences of the primary datum,
  the conformal-algebra action on
  \(\operatorname{Sym}^n(\mathbb C^D)\otimes V_\rho\), and decomposition into
  irreducible rotation representations.

## Claims To Verify

1. The source for a spin-\(\rho\) primary is valued in the dual
   representation \(V_\rho^\vee\).
2. The spin-source variation determines the contact operator appearing in the
   local current Ward identity.
3. The small-sphere charge action agrees with the contact operator.
4. The finite primary transformation law is the integrated form of the
   infinitesimal Ward action on the connected conformal group.
5. The inversion matrix is an \(O(D)\) element of determinant \(-1\), so spin
   inversion data require a specified extension beyond \(SO(D)\).
6. In \(D=2\), a statement about a primary in this volume means a global
   primary unless full Virasoro symmetry and the \(L_n,\bar L_n\) annihilation
   condition for \(n>0\) have been specified.
7. A primary multiplet before null quotient is a generalized Verma module
   induced from the parabolic \(\mathfrak l\oplus\mathfrak n_-\), with levels
   organized by symmetric powers of the translation representation.

## Figures

- No figure is required for this chapter unless future work needs a diagram of
  source/contact support on collision diagonals.

## Checks

- Keep all spin signs tied to the chosen convention
  \(\rho(R)=\exp(-\frac i2\omega^{\mu\nu}S_{\mu\nu})\).
- Keep finite transformation statements separated from coincident-point
  contact extensions, which belong to the source functional.
- 2026-05-23 spin-source pass: added spin sources, the primary contact
  operator, the spinful local current Ward identity, finite transformation
  cocycle conventions, tensor determinant-factor derivations, and the
  orientation-reversing qualification for inversion with spin.
- 2026-05-24 issue #284 pass: added the global-primary/quasi-primary/Virasoro
  primary terminology remark, separating the \(D\ge3\) finite-algebra usage
  from the stronger \(D=2\) Virasoro-primary condition.
- 2026-05-24 issue #285 pass: added the conformal generalized Verma module
  definition, PBW level decomposition, singular-vector/null-submodule quotient
  language, and the Kac-determinant/BGG framework pointer.
- 2026-05-24 issue #420 pass: inserted the flow derivation of the finite
  primary transformation law from \(\delta_\epsilon\mathcal O\), including the
  \(M_s=\Omega_sR_s\) infinitesimal decomposition, the fixed-final-coordinate
  differentiation, and explicit translation, dilatation, rotation, and special
  conformal checks.
- 2026-05-24 issue #423 pass: Chapter 3 now back-references
  `eq:primary-spin-current-ward` and identifies the stress-tensor derivative
  contact term that becomes the spin rotation term in this chapter's primary
  Ward identity.
- 2026-05-29 anti-wrapper pass: expanded the spinful local conformal-current
  Ward-identity proof from a compressed differentiation statement into the
  source-coupling derivation, including the measure/source-weight cancellation,
  dual spin action, separated-point functional derivatives, and small-sphere
  charge orientation.
- 2026-05-29 eighth anti-wrapper pass: demoted the translation-from-origin
  descendant-field identity from proposition form to convention-level prose,
  while keeping the distributional smearing qualification and radial-state
  convergence caveat explicit.
- 2026-05-30 anti-wrapper pass: demoted the elementary finite conformal
  transformation list and the tensor-primary finite transformation rewrite
  from theorem-family form to paragraph-level derivations.  The finite primary
  transformation theorem remains because it integrates the infinitesimal Ward
  action; the demoted material is coordinate/sign bookkeeping derived from it.
