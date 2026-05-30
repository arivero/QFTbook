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
- Definition `def:radial-ope-convergence-hypotheses`, now titled as inputs
  from radial reconstruction, which expands the cross-reference to Chapter 4's
  radial reconstruction hypothesis into the exact Euclidean inputs used by the
  OPE theorem and the additional Lorentzian analytic-continuation inputs used
  later without introducing a second assumption package;
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
- the connection between short-multiplet null descendants from Chapter 7 and
  the levelwise null-submodule quotients used in conformal block construction;
- conformal partial waves as shadow-projector/harmonic-analysis kernels,
  distinct from OPE-channel blocks and normalized together with their
  Plancherel density;
- the scalar Mellin representation as a constrained Mellin-Barnes transform
  on the affine space
  \(\delta_{ij}=\delta_{ji},\ \delta_{ii}=0,\ \sum_{j\ne i}\delta_{ij}
  =\Delta_i\), including the four-point variables
  \(\mathfrak s,\mathfrak t,\mathfrak u\), the gamma kernel, the exact
  compatibility with the chapter's reduced correlator
  \(\mathcal G(u,v)\), and the contour-shift derivation of OPE twist poles
  at \(\mathfrak s=\Delta-\ell+2m\);
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
- Definition `def:abstract-radial-ope-system`, specifying the additional
  positivity, convergence, all-tree compatibility, covariance, reflection
  positivity, and contact-term data required beyond the numerical list
  \(\{\Delta,\rho,\lambda\}\);
- Construction `cons:conditional-cft-reconstruction-from-ope`, assembling a
  separated-point Euclidean conformal hierarchy from an abstract radial OPE
  system and identifying the extra tube-domain hypotheses needed for the
  Lorentzian Wightman CFT.  This is deliberately no longer a theorem-family
  wrapper: the analytic and higher-coherence content sits in the definition
  of the abstract radial OPE system, while the construction verifies the
  assembly and patching of correlators from those inputs;
- Open Problem `op:bootstrap-completeness-from-ope-data`, separating the
  conditional construction from the inverse problem of deriving the
  full abstract radial OPE datum from complete all-primary four-point OPE data
  or complete generator four-point OPE data in \(D>2\), while explicitly
  rejecting the claim that a single four-point crossing equation determines a
  correlator or a CFT;
- the \(s\)- and \(t\)-channel radial convergence domains
  \(\mathcal D_s,\mathcal D_t\), their radial variables, and the derivation of
  identical-scalar crossing from permutation symmetry plus prefactor algebra;
- the generalized-free scalar four-point function as a worked crossing
  example, including the Wick-pairing formula
  \(\mathcal G_{\rm GFF}(u,v)=
  1+u^{\Delta_\phi}+(u/v)^{\Delta_\phi}\), the explicit crossing identity,
  the bilinear primary tower
  \(\Delta_{n,\ell}=2\Delta_\phi+2n+\ell\) with even \(\ell\), the finite
  primary projection in the two-particle radial Hilbert space, the leading
  normalized scalar coefficient \(a^{\rm GFF}_{0,0}=2\), and the matching of
  the \(s\)- and \(t\)-channel block expansions;
- the mixed-correlator scalar bootstrap datum for the
  three-dimensional Ising system, including the \(\mathbb Z_2\)-graded
  hypotheses on \(\sigma,\varepsilon\), the spin-\(\ell\) exchange sign,
  the \(\mathsf F_\pm^{ij,kl}\) crossing kernels, the five scalar crossing
  equations, their five-vector semidefinite-programming packaging, the
  positive-semidefinite even-sector OPE matrices, and the finite-functional
  exclusion certificate;
- companion scalar-block code in `calculation-checks/conformal_block_companion.py`
  implementing chapter-normalized global scalar blocks with the
  Dolan--Osborn hypergeometric closed forms in \(D=2\) and \(D=4\), the
  Dolan--Osborn/Hogervorst--Rychkov Casimir \(z\)-series recursion for
  \(D=3\) and other \(D>2\) numerical checks, the universal leading radial
  Gegenbauer/harmonic term, and the \(F_\pm\) crossing-kernel normalization
  used by the mixed-correlator section;
- the status boundary for the three-dimensional Ising numerical island:
  the mixed-correlator crossing and positivity system is derived in the
  chapter, while derivative truncations, block approximations, gap choices,
  and high-precision SDP islands require separately certified numerical
  input;
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
14. The Mellin amplitude is a gamma-normalized transform representation of a
    scalar correlator under stated analyticity and vertical-growth
    hypotheses.  OPE pole statements are residue statements for the full
    Mellin integrand, and gamma-kernel pole collisions must be separated from
    poles of the gamma-stripped amplitude \(M\).
15. In the chapter's four-point prefactor convention, the reduced correlator
    has Mellin powers
    \(u^{\mathfrak s/2}v^{(\mathfrak t-\Delta_2-\Delta_3)/2}\); the
    calculation check verifies this convention and the
    \(\mathfrak s=\tau+2m\) pole-to-OPE-exponent map.
16. For the generalized-free scalar example,
    \(v^{\Delta_\phi}\mathcal G_{\rm GFF}(u,v)\) and
    \(u^{\Delta_\phi}\mathcal G_{\rm GFF}(v,u)\) both reduce to the same three
    monomials
    \(v^{\Delta_\phi},(uv)^{\Delta_\phi},u^{\Delta_\phi}\).  The
    \(12\to34\) OPE identity block gives \(1\), the bilinear tower sums to
    \(u^{\Delta_\phi}+(u/v)^{\Delta_\phi}\), and the crossed channel has the
    same tower with the prefactor \((u/v)^{\Delta_\phi}\).
17. In the \(\sigma,\varepsilon\) mixed-correlator system, the scalar
    four-point prefactor in `eq:scalar-four-point-general` gives the exact
    ratios
    \(u^{\Delta_\sigma}v^{-(\Delta_\sigma+\Delta_\varepsilon)/2}\) and
    \(u^{(\Delta_\sigma+\Delta_\varepsilon)/2}v^{-\Delta_\sigma}\) for the
    two mixed crossing comparisons used in the five-vector system.
18. The exchange of the two scalar legs in a scalar-scalar-spin-\(\ell\)
    three-point tensor contributes precisely \((-1)^\ell\) to
    \(\lambda_{\varepsilon\sigma\mathcal O}\) relative to
    \(\lambda_{\sigma\varepsilon\mathcal O}\).
19. The five-vector packaging is algebraically equivalent to the five scalar
    crossing equations: even primaries enter through the quadratic form of
    \((\lambda_{\sigma\sigma\mathcal O},
    \lambda_{\varepsilon\varepsilon\mathcal O})\) against a vector of
    \(2\times2\) matrices, and odd primaries enter through
    \(\lambda_{\sigma\varepsilon\mathcal O}^2\vec{\mathsf V}_-\).
20. Reflection positivity gives positive-semidefinite even-sector OPE
    matrices after summing over degenerate even primaries with the same
    \((\Delta,\ell)\); the odd coefficients are ordinary nonnegative squares.
21. A mixed-correlator functional with positive identity contribution,
    positive-semidefinite even matrix action, and nonnegative odd action is an
    exclusion certificate.  Numerical derivative functionals become theorem
    evidence only after the conformal-block derivatives and semidefinite
    inequalities are certified.

## Figures

- Keep figures that show the separating sphere, radial ordering, or
  conformal-block channel.

## Checks

- Do not import analytic or numerical bootstrap claims into the core chapter.
- Every convergence claim must state the Hilbert-space and spectral
  hypotheses being used, and must use the same \(D_{\rm rad}\) spectrum
  condition as Chapter 4.
- Never formulate the OPE as a literal multiplication law in the
  local-operator space.  A separated pair of local insertions defines a
  sphere state; the OPE is convergence, in BPZ/radial Hilbert norm, of a
  sequence of finite local-operator states at the origin to that sphere
  state.
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
- Do not describe Mellin amplitudes as universally existing functions for all
  CFT correlators.  State the Mellin-representability, meromorphy, contour,
  and growth hypotheses before using contour shifts or OPE-pole language.
- Keep the three-dimensional Ising mixed-correlator section at the level of
  exact crossing, positivity, and finite-functional certificates unless a
  fully certified numerical bootstrap proof is supplied.  The quoted Ising
  dimensions remain external high-precision data.
- Run `calculation-checks/ising_mixed_bootstrap_checks.py` after changing the
  mixed-correlator prefactor, \(F_\pm\), spin-exchange, PSD, or five-vector
  conventions.
- Run `calculation-checks/conformal_block_companion.py` after changing scalar
  conformal-block normalizations, the \(D=2\)/\(D=4\)
  Dolan--Osborn hypergeometric formulas, the
  Dolan--Osborn/Hogervorst--Rychkov recursion used for \(D=3\) and other
  \(D>2\) checks, the arbitrary-\(D\) leading radial Gegenbauer convention, or
  the mixed-correlator \(F_\pm\) helper.  Do not identify this global-block
  script with the separate two-dimensional Virasoro-block problem, whose
  numerical treatment should use Zamolodchikov recursion data.

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
- 2026-05-25 issue #479 pass: added the generalized-free scalar four-point
  worked example with Wick-pairing definition, explicit reduced correlator,
  algebraic crossing check, bilinear primary tower, leading
  \(:\phi^2:/\sqrt2\) OPE coefficient, and \(s\)-/\(t\)-channel block
  expansions.
- 2026-05-24 issue #418 pass: retitled the OPE convergence input block and
  stated explicitly that the listed items are clauses of
  `hyp:radial-reconstruction-data`, not an independent duplicate set of
  assumptions.
- 2026-05-24 issue #422 pass: expanded the local OPE-block existence theorem
  to identify the null descendants supplied by saturated Chapter 7 unitarity
  bounds and to quotient the raw descendant space
  \(W_n\simeq\operatorname{Sym}^n(\mathbb C^D)\otimes V_{\Delta,\ell}\) by the
  level-\(n\) null radical before inverting the Gram matrix.
- 2026-05-24 follow-up pass: replaced literal product/equality language in
  the opening OPE formulation and reconstruction discussion by state-valued
  BPZ/radial-norm convergence of local-operator partial sums.
- 2026-05-25 issue #477 pass: added a Mellin-representation subsection for
  scalar correlators, including the constrained \(n\)-point definition, the
  four-point \((\mathfrak s,\mathfrak t,\mathfrak u)\) formula compatible with
  the existing prefactor, contour-shift pole extraction, Mack-polynomial
  residue interpretation, and the crossing action on Mellin variables.
- 2026-05-27 higher-dimensional CFT pass: added the
  \(\sigma,\varepsilon\) mixed-correlator bootstrap datum for the
  three-dimensional Ising system, derived the five crossing equations and
  five-vector positivity packaging from the chapter's conformal-block
  conventions, recorded the finite-functional exclusion certificate as a
  cone-separation criterion whose hard part is constructing and certifying
  the functional, separated numerical SDP islands as external/certification-boundary input, and added
  `calculation-checks/ising_mixed_bootstrap_checks.py` for the exact
  prefactor/sign/PSD/vector-packing algebra.
- 2026-05-27 companion-code follow-up: added
  `calculation-checks/conformal_block_companion.py` with reusable
  OPE-normalized global scalar block evaluators based on Dolan--Osborn
  hypergeometric closed forms in \(D=2,4\) and the
  Dolan--Osborn/Hogervorst--Rychkov Casimir recursion for \(D=3\) and generic
  \(D>2\) numerical checks, with explicit leading Gegenbauer/harmonic
  normalization tests and a note that Virasoro blocks require a separate
  Zamolodchikov-recursion companion.
