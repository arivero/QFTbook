# Epistemic And Rigor Standards

## Drafting Gate

No chapter may be drafted from generic QFT memory. Before reader-facing prose
is written, the chapter dossier must identify:

- source anchors in Xi Yin's QFT notes for the chapter's logical role;
- external references for theorem-level claims not proved in the chapter;
- all frameworks used in the chapter;
- all primitive data and constructed objects;
- all definitions introduced;
- all major claims and their status;
- all figures and their mathematical content;
- open questions and unresolved comparison issues.

If any of these entries is missing, the task is source study or dossier work,
not manuscript writing.

## Symbol Discipline

Every symbol in reader-facing prose must be introduced before load-bearing use.
At first introduction, specify the kind of object it denotes. Examples:

- \(D\): spacetime dimension.
- \(\mathbb M^D\): \(D\)-dimensional Minkowski affine space.
- \(\eta\): Lorentzian metric with the stated signature.
- \(\Hilb\): complex Hilbert space.
- \(U\): strongly continuous unitary representation with stated domain.
- \(P_\mu\): self-adjoint generators of translations on a common spectral
  calculus.
- \(\mathcal O\): open spacetime region with stated restrictions.
- \(\Obs(\mathcal O)\): local algebra assigned to \(\mathcal O\).
- \(\widehat\Phi(f)\): smeared operator-valued distribution with test function
  \(f\).

Notation introduced in one framework must not silently migrate into another.
For example, a Euclidean Schwinger function, a Lorentzian Wightman
distribution, a time-ordered Green function, and a regulated path-integral
correlator are different objects until a theorem or construction relates them.

## Definition Integrity

Definitions must be mathematically proper for the stated framework. A
definition must include:

- ambient category or analytic setting;
- data and their types;
- domains and codomains of maps;
- topology, continuity, measurability, distributional, or domain conditions
  when relevant;
- covariance, locality, positivity, reflection positivity, spectral, grading,
  or functoriality laws when relevant;
- statement of whether the object is primitive or constructed.

Forbidden definition patterns in reader-facing prose:

- pointwise fields without their smeared distributional meaning;
- path integrals without a regulator, measure, contour, Gaussian structure, or
  perturbative status;
- gauge symmetry defined as an ordinary physical symmetry before defining
  physical observables;
- S-matrix formulas before asymptotic states and wave operators;
- "definition" by slogan or analogy.

When the full mathematical definition is unavailable, the text must say which
working framework is being used and which comparison problem remains open.

## Claim Status

Every substantive statement must have one of the following statuses:

- definition;
- convention;
- assumption;
- construction;
- lemma, proposition, theorem, or corollary;
- example;
- physical principle with stated domain;
- regulated statement;
- continuum statement;
- controlled approximation;
- asymptotic expansion;
- formal calculation;
- perturbative statement;
- nonperturbative statement;
- numerical or computational observation;
- conjecture;
- lore, explicitly labelled as such;
- open problem.

The manuscript must not allow lore, formal calculation, or pedagogical habit to
carry a conclusion that requires a theorem or stated assumption.

The word "theorem" is reserved for a formulated mathematical statement in a
specified framework, with stated hypotheses, conclusion, and proof status.  A
statement often called a theorem in the physics literature but supported only
by perturbative evidence, examples, expected genericity, an unverified
regularity assumption, or an informal argument must be classified as a
conditional argument, conjecture, criterion, or open problem.  This rule is
especially important for scale-versus-conformal claims, RG monotonicity
claims, bootstrap claims, duality claims, and any statement involving a
continuum limit or an infinite-dimensional path integral.

Named physical principles must be unpacked into object-level claims before
they are used.  For example, anomaly matching is a statement about equality of
background-field anomaly classes modulo local counterterms, not a free-standing
explanatory phrase; universality is a statement about a specified limiting
object and equivalence relation; reconstruction is a theorem only after its
positivity, locality, covariance, and regularity hypotheses have been stated.

## Claim Certification

Before a claim appears in polished prose, it must satisfy at least one
certificate:

- it is a definition or convention introduced in the text;
- it is derived in the text from named assumptions;
- it is quoted as a theorem with hypotheses, reference, conclusion, and proof
  status;
- it is a controlled approximation with expansion parameter and error class;
- it is labelled formal, heuristic, conjectural, or open.

Uncertified claims are draft debt.

Self-contained development is the default.  A nontrivial physics claim may not
be imported from an external reference merely because the reference is sound.
When the claim is part of the book's logical construction, the text must give
the definition, assumptions, and derivation or argument needed by the reader.
Large external theorems may be used as inputs only after the theorem is stated
with its hypotheses and domain, the chapter explains how those hypotheses
enter, and the proof status is explicit.

Proofs must construct the load-bearing objects named in their statements.  If
a theorem asserts a change of coordinates, a matching map, a limiting object,
a quotient, a contact distribution, a state space, a measure, or a topology,
the proof must display that object or explicitly invoke a previously stated
theorem that constructs it.  Phrases such as "is absorbed into a coordinate
change", "is suppressed by powers", "the Legendre transform gives", "locality
implies", or "the same argument shows" are not proof steps unless the map,
norm, exponent, differentiability hypothesis, and object being compared have
already been stated.

Whenever a proof uses an approximation or truncation, the text must state the
truncation parameter, the norm or seminorm in which the error is estimated,
the exponent or order of the remainder, the constants' allowed dependencies,
and the limiting regime.  A finite-order perturbative theorem must say the
loop order and expansion variables.  A nonperturbative theorem must say the
space of objects and the topology of convergence.

Long technical arguments are not optional.  If a proof is too long for the
main flow of a chapter, move the detailed proof to a chapter appendix or a
clearly labelled technical subsection, and keep an exact pointer in the main
text.  Do not replace a key derivation by a citation, a slogan, or a
structural summary when the argument is within the intended scope of the
monograph.

## Limits

All limiting procedures require explicit meaning when used for substantive
claims:

- continuum limit;
- infinite-volume limit;
- thermodynamic limit;
- infinite-time or scattering limit;
- adiabatic limit;
- weak-coupling limit;
- large-\(N\) limit;
- semiclassical limit;
- derivative expansion;
- operator-product or short-distance limit;
- conformal bootstrap truncation;
- lattice spacing removal;
- ultraviolet or infrared cutoff removal.

Specify the object that converges and the intended sense of convergence:
norm, weak, strong, distributional, correlation-function, matrix-element,
operator-algebraic, probabilistic, or another stated sense.

## Framework-Specific Standards

### Path Integrals

Distinguish finite-dimensional oscillatory integrals, finite-dimensional
Euclidean integrals, Gaussian measures, regulated lattice or cutoff path
integrals, perturbative formal expansions, constructive measures, BRST/BV
gauge-fixed integrals, and heuristic continuum notation.

### Wick Rotation

Wick rotation requires analytic, spectral, reflection-positivity, boundary, or
contour-deformation input. A substitution \(t=-i\tau\) is notation, not a
justification.

### Scattering

The S-matrix is first a nonperturbative comparison between in and out
asymptotic particle states when the required long-time limits exist. LSZ is the
bridge from local correlation functions to scattering matrix elements.

### Gauge Theory

Gauge transformations are redundancies of description. Physical symmetries
must be defined by their action on gauge-invariant observables, sectors,
defects, or background fields.

### Renormalization

Renormalization is the structure of scale-dependent effective description and
continuum limits. Counterterms, beta functions, and subtraction schemes are
coordinate tools within specified frameworks.

### Particles

Particles arise from spectral and asymptotic structure. A Wigner one-particle
representation, a free Fock representation, a local observable net, and an
asymptotic scattering space are distinct mathematical objects.

## Self-Contained Proof Depth

Full proofs are expected for central results when the proof is within the
scope of the book. Proof sketches are allowed for large external theorems only
when the missing technical ingredients and references are named.

For foundational topics, the manuscript may use layered precision:

1. the construction needed for the physics logic;
2. a theorem under stronger mathematical hypotheses;
3. a comparison explaining which physical claims remain beyond current
   rigorous frameworks.
