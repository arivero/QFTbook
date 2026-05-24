# Volume III, Chapter 9 Dossier: Operator Product Expansion

## Logical Role

- Role in the monograph: formulate the OPE as a convergent radial Hilbert-space
  expansion under stated hypotheses and connect OPE coefficients to
  conformal-block decompositions and positivity.
- Immediate predecessor: correlation functions and conformal frames.
- Immediate successor: later special volumes on bootstrap, two-dimensional
  CFT, supersymmetry, or integrability.

## Definitions And Results

The chapter establishes:

- the radial Hilbert-space statement of OPE convergence for insertions inside
  a separating sphere;
- Definition `def:radial-ope-convergence-hypotheses`, which expands the
  cross-reference to Chapter 4's radial reconstruction hypothesis into the
  exact Euclidean inputs used by the OPE theorem and the additional Lorentzian
  analytic-continuation inputs used later;
- the use of the same nonnegative self-adjoint radial Hamiltonian
  \(D_{\rm rad}\) specified in Chapter 4's radial reconstruction hypothesis;
- the separation between Euclidean radial Hilbert-space convergence and
  Lorentzian Wightman boundary-value convergence;
- a tube-domain continuation criterion for Lorentzian OPE convergence in a
  fixed Wightman ordering, with the radial bounds \(|\rho|,|\bar\rho|<1\) as
  channel conditions;
- the local operator expansion into primaries and descendants;
- coefficient functions as distributions or analytic functions on the
  convergence domain;
- conformal blocks as sums over descendant states in a fixed conformal
  multiplet;
- the scalar four-point Casimir equation with the \(u,v\) differential
  operator displayed, the two Frobenius branches \(\Delta\) and \(D-\Delta\),
  and the radial descendant/Gram-matrix construction proving local existence
  and uniqueness of the OPE-normalized block;
- the finite-level quotient Gram-matrix projector used in the radial block
  expansion, including null descendant removal before matrix inversion;
- conformal partial waves as shadow-projector/harmonic-analysis kernels,
  distinct from OPE-channel blocks and normalized together with their
  Plancherel density;
- the Lorentzian inversion formula as a boundary theorem extracting a
  spin-analytic meromorphic OPE coefficient from the crossed-channel double
  discontinuity, subject to stated Euclidean OPE convergence, tube
  analyticity, reflection-positivity, and Regge-boundedness hypotheses;
- the Hogervorst--Rychkov radial variable \(\rho=z/(1+\sqrt{1-z})^2\) and the
  interpretation of \(|\rho|<1\) as the radial-ordering domain for the
  channel expansion, together with the theorem that the radial block series
  converges absolutely and locally uniformly in the full \(\rho\)-unit disk,
  equivalently on the cut \(z\)-plane \(\mathbb C\setminus[1,\infty)\) for the
  chosen branch;
- reflection-positivity constraints on OPE coefficient matrices;
- OPE associativity as equality of nested spectral expansions in a common
  Euclidean radial domain, followed by analytic continuation of the
  separated-point correlator;
- Definition `def:abstract-radial-ope-datum`, specifying the additional
  positivity, convergence, all-tree compatibility, covariance, reflection
  positivity, and contact-term data required beyond the numerical list
  \(\{\Delta,\rho,\lambda\}\);
- Theorem `thm:conditional-cft-reconstruction-from-ope`, reconstructing a
  separated-point Euclidean conformal hierarchy from an abstract radial OPE
  datum and identifying the extra tube-domain hypotheses needed for the
  Lorentzian Wightman CFT;
- Open Problem `op:bootstrap-completeness-from-ope-data`, separating the
  conditional reconstruction theorem from the inverse problem of deriving the
  full abstract radial OPE datum from complete all-primary four-point OPE data
  or complete generator four-point OPE data in \(D>2\), while explicitly
  rejecting the claim that a single four-point crossing equation determines a
  correlator or a CFT;
- the \(s\)- and \(t\)-channel radial convergence domains
  \(\mathcal D_s,\mathcal D_t\), their radial variables, and the derivation of
  identical-scalar crossing from permutation symmetry plus prefactor algebra;
- the boundary between core OPE machinery and later specialized bootstrap
  methods.

## Claims To Verify

1. OPE convergence is a Hilbert-space norm statement under radial
   reconstruction, discreteness, and finite-multiplicity assumptions in the
   Euclidean radial domain.
2. Correlator convergence follows by pairing the inside state with exterior
   states at larger radius.
3. Positivity of squared OPE coefficients is a Gram-matrix statement in a
   reflection-positive channel.
4. Angular variables use \(n_x\)-type notation so that \(\vac\) remains
   reserved for the vacuum.
5. A conformal block is an OPE-boundary-condition solution of the Casimir
   equation; a conformal partial wave is the single-valued Euclidean harmonic
   that combines the block and its shadow block and is normalized as part of
   the principal-series Plancherel resolution.
6. The scalar Casimir equation has two local branches with radial exponents
   \(\Delta\) and \(D-\Delta\); the OPE block is selected by normalizing the
   \(\Delta\) branch and setting the shadow-branch coefficient to zero.
7. Local existence and uniqueness of the OPE-normalized block follow from the
   finite-level descendant construction, invertibility of Gram matrices after
   quotienting null descendants, and radial OPE convergence.
8. Lorentzian inversion is used only as a theorem under its analytic and Regge
   hypotheses; the double discontinuity is a Lorentzian branch-cut datum, not a
   Euclidean projection operation.
9. The radial-block expansion is explicitly the Hogervorst--Rychkov radial
   expansion, with the chosen square-root branch tied to the radial-ordering
   domain.  The map
   \(\rho=(1-\sqrt{1-z})/(1+\sqrt{1-z})\) is a Cayley transform from
   \(\operatorname{Re}\sqrt{1-z}>0\) to \(|\rho|<1\), and radial Hilbert-space
   spectral estimates give absolute, locally uniform block convergence on
   compact subdisks.  At \(z=1/2\), \(\rho=3-2\sqrt2\).
10. Lorentzian OPE convergence is obtained as a tube-domain analytic
    continuation plus Wightman boundary value; real timelike configurations
    require an \(i\epsilon\) ordering and remain controlled only when the
    corresponding radial variables stay in a compact subdomain
    \(|\rho|,|\bar\rho|\le q<1\).
11. Crossing is not a termwise equality of two channel expansions at distinct
    OPE corners.  It follows from equality of Euclidean separated-point
    correlators, convergence of each channel expansion in its own radial
    domain, and analytic continuation on the common connected domain.
12. Radial block coefficients use finite-dimensional quotient Gram matrices
    \(M^{(n)}\) at each descendant level; null descendants are removed because
    reflection positivity makes them zero against all physical states.
13. Reconstruction from OPE data is theorem-level only for an abstract radial
    OPE datum with all-tree convergence, channel compatibility, positivity,
    and distributional/contact-term prescriptions.  Complete all-primary
    four-point OPE data may be rigid enough to determine a CFT under
    generator/completeness hypotheses, but a single four-point crossing
    equation is underdetermined and does not even determine its correlator
    without extra data.

## Figures

- Keep figures that show the separating sphere, radial ordering, or
  conformal-block channel.

## Checks

- Do not import analytic or numerical bootstrap claims into the core chapter.
- Every convergence claim must state the Hilbert-space and spectral
  hypotheses being used, and must use the same \(D_{\rm rad}\) spectrum
  condition as Chapter 4.
- Every Lorentzian convergence claim must identify the Wightman ordering,
  tube component, radial-variable domain, and boundary-value interpretation.
- Do not use ``conformal block'' and ``conformal partial wave''
  interchangeably; later inversion formulae use the latter.
- Do not invoke Lorentzian inversion without recording the double
  discontinuity, the spin range or subtractions, and the analyticity/Regge
  conditions that suppress contour arcs.
- Do not derive crossing by skipping the channel domains; display the
  \(s\)- and \(t\)-channel radial variables and identify the analytic
  continuation step.
- Do not describe radial block construction as an inverse of one infinite Gram
  matrix; use levelwise quotient projectors.

## Audit Notes

- 2026-05-24 issue pass: addressed #273 by displaying the scalar Casimir
  differential operator in \(u,v\), recording the \(z,\bar z\) form, stating
  the \(\Delta\) and \(D-\Delta\) Frobenius branches, and proving local
  existence/uniqueness of the OPE-normalized block through the finite-level
  descendant Gram construction.
- 2026-05-24 issue pass: addressed #274 by adding a subsection distinguishing
  OPE-normalized conformal blocks from shadow-projector conformal partial
  waves and recording the associated Plancherel normalization convention.
- 2026-05-24 issue pass: addressed #275 by adding the scalar Caron-Huot
  Lorentzian inversion formula, defining the double discontinuity and pole
  extraction convention, stating the theorem-boundary hypotheses, and naming
  the Hogervorst--Rychkov radial coordinate used in the radial expansion.
- 2026-05-24 issue pass: addressed #276 by renaming the radial theorem as a
  Euclidean theorem, adding a Lorentzian tube-domain continuation proposition,
  and recording the \(i\epsilon\), light-cone, and \(\rho,\bar\rho\) domain
  conditions needed for Lorentzian OPE convergence.
- 2026-05-24 issue pass: addressed #277 by expanding the crossing discussion
  to show nested-OPE associativity, the \(s\)- and \(t\)-channel convergence
  domains, and the prefactor derivation of
  \(v^{\Delta_\phi}\mathcal G(u,v)=u^{\Delta_\phi}\mathcal G(v,u)\).
- 2026-05-24 issue pass: addressed #278 by spelling out the raw descendant
  space, null quotient, quotient Gram matrix, level projector, and levelwise
  contraction formula for radial conformal-block coefficients.
- 2026-05-24 issue #288 pass: added a conditional radial reconstruction
  theorem from abstract OPE data and isolated the all-primary/generator
  four-point OPE inverse problem from the underdetermined single-correlator
  crossing problem.
- 2026-05-24 issue #293 pass: stated and proved the Hogervorst--Rychkov
  radial block convergence theorem in the \(\rho\)-disk, including the Cayley
  map from the cut \(z\)-plane and the value \(\rho(1/2)=3-2\sqrt2\).
- 2026-05-24 issue #297 pass: changed the OPE convergence proof to use
  \(D_{\rm rad}\) by name and explicitly identify it as the nonnegative
  self-adjoint radial Hamiltonian from
  `hyp:radial-reconstruction-data`.
- 2026-05-24 issue #337 pass: added
  `def:radial-ope-convergence-hypotheses`, making the scope of the
  reflection-positive radial OPE theorem a direct expansion of Chapter 4's
  radial reconstruction data, with Euclidean and Lorentzian inputs separated.
