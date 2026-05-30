# Strict Writing Harness

This file is the immediate hard gate for all reader-facing monograph drafting.

## Source-First Rule

For each chapter, work in this order:

1. locate the chapter in the source-note logical spine;
2. read the corresponding handwritten or transcribed source section;
3. compare student transcriptions only as non-authoritative aids;
4. identify rigorous external references for theorem-level claims;
5. write or update the chapter dossier;
6. draft the chapter;
7. audit before inclusion in compiled TeX.

No step may be skipped because the topic is familiar.

External references are study tools and theorem-boundary checks. They do not
license the manuscript to import a nontrivial physics claim as an unexplained
fact. If a claim is used in the logical development, the chapter must carry
its assumptions and argument, or else mark it as an external theorem with a
precise statement and state that the proof is outside the present scope.
Use the `quotedtheorem` environment for such imported mathematical theorems:
state the hypotheses and conclusion in the manuscript, state the local role
of the theorem immediately after it, name the external source or source
lineage in the theorem block or immediately following paragraph, and do not
attach a `proof` environment unless the proof is actually reproduced.  A
footnote is acceptable as bibliographic support, but the reader-facing text
must still say whose theorem or theorem-lineage is being quoted.

Every `quotedtheorem` is an active proof-debt marker until the surrounding
text gives a detailed mechanism in the monograph's notation.  The minimum
acceptable expansion is: identify the primitive objects, state the analytic or
algebraic lemma that carries the proof, explain how the hypotheses enter,
verify the local hypotheses used by the chapter, and spell out which part of
the conclusion is imported rather than derived.  A bare theorem statement plus
reference, even to standard mathematics, is not a finished treatment.  For
pure mathematical infrastructure the full proof may remain external, but the
reader must see the proof mechanism and the exact local role.  For theorem
claims whose conclusion is a QFT construction, observable, phase statement,
or anomaly, the final standard is a self-contained proof or an explicitly
marked proof obligation/status statement.

For theorem-level claims specifically about QFT, `quotedtheorem` is an
interim honesty boundary, not the final monograph standard.  Such a theorem
must either receive a self-contained proof somewhere in the monograph
proper, be downgraded to a clearly marked status statement, or be recorded as
an explicit proof obligation/open problem with the missing analytic steps
named.  Literature proofs in physics are starting material for scrutiny; they
are never authority by themselves.

The permission to invoke standard mathematics is narrower than the permission
to invoke standard physics.  Theorems in complex analysis, distribution
theory, spectral theory, semigroup theory, and functional analysis may be used
as named mathematical inputs after their hypotheses are stated and verified in
the local context.  A theorem whose conclusion is specifically a QFT object or
bridge -- for example existence of Wightman distributions from Schwinger data,
local commutativity from Euclidean symmetry, spectral support of reconstructed
vacuum functions, LSZ reduction from a Hilbert-space scattering theory, or an
anomaly formula for a field theory -- must be derived inside the monograph from
the named mathematical inputs and the stated QFT data.  A citation to OS,
Wightman, Haag--Ruelle, Epstein--Glaser, BV, or AQFT literature is not a
substitute for that derivation.

## Ambition And Frontier Rule

The monograph is not a textbook summary project.  Its target standard is the
highest level of mathematical and physical precision currently feasible, with
self-contained development of the essential physics and explicit theorem
boundaries where present mathematics is incomplete.  A chapter passes this
harness only if it does at least one of the following:

- proves or derives a load-bearing result from stated data;
- gives a rigorous formulation of a concept whose literature treatment is
  often ambiguous;
- constructs a substantial example that tests the definitions;
- compares frameworks by an explicit object-level map;
- identifies a genuine gap in present knowledge and formulates the problem in
  terms precise enough for future work.

External references should be downloaded into `references/` or
`references/sound_references/` when detailed local analysis is needed.  Before
using such a reference for drafting, create a readable text sidecar when
possible, inspect the relevant theorem statements and conventions locally,
and record the exact role of the reference in the chapter dossier.  The
reference may guide proof infrastructure and convention checks; it must not
replace the monograph's own definitions, assumptions, and derivations for
central claims.

## No-Skip Source Coverage Rule

The 253a and 253b source notes are a coverage obligation for the core
monograph.  The 253c source notes are a coverage obligation for the CFT and
later special-topic volumes, with only the core CFT portion currently included
in the compiled manuscript.  A chapter may deepen, reorganize, correct, or
generalize the source material, but it may not silently omit a source
derivation, example, figure, definition, or conceptual distinction.  Each
source block must be accounted for in a dossier, audit note, or coverage
register as one of:

- incorporated in the compiled monograph;
- incorporated after a corrected derivation or notation change;
- deferred to a specified later core chapter;
- moved to a specified non-core or deprecated file because the topic is
  outside the current core scope.

Compression is not coverage.  A result stated without the source calculation
is a gap when the source calculation carries conceptual content.

## Modular Foundation Rule

No existing framework is the universal foundation of the monograph, and no
framework is valuable merely because it is axiomatic.  For every construction,
state the local framework and its data. Use Wightman, OS, AQFT, perturbative
AQFT, constructive, factorization, functorial, and Kontsevich--Segal-type
frameworks as theorem sources, comparison lenses, and example-building tools,
with their domains stated.  A framework discussion passes the harness only if
it produces nontrivial information: a theorem with hypotheses, a construction,
an example, a comparison map, a limitation, or a precise open problem.
Do not include a framework as a badge of rigor or as a merely formal bridge:
the treatment must either develop theory inside the framework, relate it
substantively to another formulation, or analyze substantial examples.

## Definition Integrity Rule

Every definition must state:

- ambient setting;
- input data and types;
- domains and codomains;
- support, topology, continuity, distributional, or operator-domain conditions;
- covariance, locality, positivity, spectral, grading, or functoriality
  conditions when relevant;
- whether the object is primitive or constructed.

Forbidden in reader-facing definitions:

- undefined symbols;
- pointwise operator fields without smearing;
- path-integral notation without status;
- gauge symmetry as ordinary physical symmetry without physical-observable
  definition;
- S-matrix formulas before asymptotic states and wave operators;
- slogan or analogy as definition.

## Logical And Philosophical Accuracy Rule

Every load-bearing passage must distinguish the following categories whenever
they could otherwise be conflated:

- object and representative;
- primitive datum and constructed object;
- definition, convention, assumption, theorem, criterion, conjecture, and open
  problem;
- physical observable and gauge-dependent coordinate;
- operator, distribution, function, formal variable, regulator-dependent
  coordinate, and integration functional;
- finite-regulator statement, perturbative formal-power-series statement, and
  nonperturbative continuum statement;
- equality, equivalence, isomorphism, duality, approximation, and matching of
  selected observables.

The main text must not use rhetorical or philosophical shortcuts to hide a
change of category.  If a construction uses a representative object, state the
equivalence relation and the invariant object.  If a formal expression is used
as a coordinate on a future construction, state what mathematical object the
coordinate is intended to represent and what remains to be proved.

## Positive Scope Prose Rule

Reader-facing prose must state what an object is, what data it uses, and what
claim it supports before discussing exclusions.  Backward corrective sentences
such as "This is not ...", "It is not, by itself, ...", "should not be read as
...", "not a substitute for ...", and "not merely ..." are forbidden in the
compiled TeX volumes.  Rewrite them as positive scope statements: name the
construction, theorem, datum, or approximation that is actually present, then
state the additional data required for any stronger conclusion.

Precise mathematical negation is allowed when it is the content of the claim:
for example a vanishing statement, a nonexistence theorem, a counterexample, a
failure of a hypothesis, or a definition of a complement.  The forbidden form
is the prose afterthought that corrects a possible misconception instead of
declaring the scope directly.

The local gate is

```bash
tools/audit_negative_scope_prose.py
```

and the full build runs it before LaTeX.

## Symbol Rule

Every symbol must be introduced with its type before load-bearing use. If a
symbol changes meaning across frameworks, rename it or explicitly declare the
change.

## Claim Certification Rule

Every load-bearing claim must be one of:

- definition or convention;
- assumption;
- construction;
- derivation in the chapter;
- theorem with hypotheses, reference, and a statement of whether the proof is
  included, sketched, or deliberately deferred;
- controlled approximation;
- formal calculation with formal status;
- conjecture or open problem.

Uncertified claims cannot appear in polished TeX.

A citation alone is not a certificate for a nontrivial physics claim. For
central physics claims, the monograph should give a self-contained derivation
or argument from the chapter's stated data. External theorem citations are
permitted only when the theorem is a mathematical input whose hypotheses,
domain, conclusion, and role in the local argument have been made explicit.
If those hypotheses are not verified in the chapter, the conclusion must be
phrased conditionally.

## Section-Level Depth Rule

Every reader-facing section must have a mathematical role.  A section passes
only if it contains all of the following:

- the primitive objects of that section, with ambient category or framework;
- the symbols used in load-bearing formulae, with domains and codomains when
  maps are involved;
- the status of the main statements: definition, construction, proposition,
  theorem with hypotheses, controlled approximation, example, or open problem;
- an argument, derivation, or construction whenever the section changes the
  reader's mathematical state.

A section that only announces a topic, lists literature themes, or gestures
toward later work is not acceptable in compiled TeX.  If a complete proof is
too long for the main flow, the section must state the theorem precisely and
point to a chapter appendix or a named later proof obligation.

Proofs must not use structural prose as a substitute for construction.  When
a statement asserts a coordinate change, a matching map, a quotient, a contact
term, a limiting object, a topology, a measure, or an equivalence of
functionals, the proof must construct the object or cite an earlier theorem in
the monograph that constructs it.  In particular:

- a phrase such as "absorbed into local coordinates" must be accompanied by
  the displayed coordinate map or by a recursive construction of that map;
- a phrase such as "suppressed by powers" must give the norm or seminorm, the
  exponent, the constants' dependencies, and the scale regime;
- a phrase such as "Legendre transformation gives" must identify the source
  space, the classical-field space, the convexity or Hessian hypothesis, and
  whether the object is a low-mode Legendre transform or a restriction of a
  larger functional;
- a phrase such as "same continuum limit" must state the object that
  converges and the topology or correlation-function sense of convergence.

Theorem-family environments must not be used for scope calibration,
terminology policing, or absence-of-construction statements.  If the content
is "this datum has only the following scope", "these are different kinds of
data", "this construction does not by itself prove X", or "this is a warning
about what a definition does not contain", use a remark, convention, status
paragraph, or open problem.  A proposition or theorem with a negative-looking
conclusion is allowed only when it proves a genuine mathematical fact, such as
an explicit counterexample, obstruction, nonexistence theorem, positivity
failure, or finite-dimensional lemma.  Its proof must do mathematical work
beyond unpacking the definition.

Long derivations should not be forced into theorem statements.  If the text
constructs an object step by step, use a construction or derivation paragraph
and reserve the theorem/proposition for the final checkable claim.  If a
statement consists mostly of setup data with a short proof that applies an
earlier theorem, move the setup into a definition or hypothesis and state the
application as a proposition or corollary.

Theorem-family environments must also pass a substance test.  A proposition,
theorem, lemma, or corollary is inappropriate when the proof merely repeats
the statement, substitutes one displayed formula into another, checks a
definition already present in the statement, or records a comparison-test
bound whose proof is the comparison test itself.  Such material belongs in
prose, a definition, an example, a criterion, or an estimate unless the
surrounding text supplies a genuinely load-bearing proof: construction of an
object, verification of hypotheses in a nontrivial framework, an estimate
with explicit constants and dependencies, a counterexample whose mechanism is
analyzed, or a reduction to an earlier theorem in the monograph with all
hypotheses checked.  Short proofs are allowed only when the mathematical
content is genuinely concentrated, not when a trivial observation has been
promoted to theorem status.

Hypothesis-loaded conclusions obey the same rule.  If a statement assumes the
existence of the scaling limit, the universal source functional, the complete
OPE convergence package, or the common limiting CFT data, and the conclusion
only unpacks those assumptions, use a hypothesis followed by a conditional
consequence/status paragraph.  Reserve theorem-family form for the additional
mathematical work: constructing the limit, proving tightness or positivity,
verifying a contraction estimate, deriving a reconstruction theorem, or
showing that concrete microscopic models satisfy the hypotheses.  In
particular, Ising or RG ``universality'' statements whose substance is in the
universality hypothesis are not theorem-level claims in this monograph.

Finite comparison algebra, such as sine-law/Casimir ratio identities or
large-\(N\) Taylor expansions used only as reference curves, belongs in prose
or in an example unless the surrounding statement derives an actual spectral,
operator, or path-integral object.  A theorem-family title advertising
``comparison algebra'' is a failed wrapper: the reader needs to know the
finite identities and the dynamical status separately, not see them packaged
as a proved physical result.

Formula-verification wrappers obey the same rule.  Exact finite-basis GEVP
diagonalization, Richardson cancellation, finite normal Gaussian factors,
basic \(Q\)-exact deformation identities, heat-kernel substitutions, thermal
free-kernel Fourier inversions, and BCFW on-shell preservation are useful
derivation steps, but they are not theorem-family claims unless the statement
adds a genuine estimate, construction, or nontrivial hypothesis verification
beyond the displayed algebra.

General methodology must live at its natural level of generality.  Numerical
methods, spectral-extraction procedures, bootstrap algorithms, RG comparison
machinery, localization templates, and finite-dimensional linear-algebra
devices should be developed in the methodological chapter or section where
their hypotheses are natural.  A specialized theory chapter may apply such a
method only after naming the general source and then stating the additional
model-specific data: operators, symmetry channels, regulator choices,
renormalization coordinates, limits, and diagnostics.  Do not let a general
method appear to be a special structure of \( \mathcal N=1 \) SYM, QCD,
Ising, Liouville, Chern--Simons matter, or any other example merely because
the example is where the method was first written down.

If the specialized chapter has no concrete result to extract with the
method, do not expose the method there.  In that case the chapter should stop
at the model-specific data and the diagnostic requirement.  Generic
finite-matrix estimates, algorithmic equations, and residual criteria belong
in the methodological chapter; a specialized chapter earns their reappearance
only by carrying out an actual model-specific calculation or comparison.

Proof audits must read the mathematical substance of each proof under review:
the statement, hypotheses, dependencies, and proof body must be checked
together.  Text searches for phrases such as "immediate" or length scans may
only build a review queue; they do not certify a proof.  A proof passes the
audit only when the reader can identify the exact construction, estimate,
algebraic computation, or theorem reduction that carries the stated conclusion.

A `proof` environment may not be attached directly to a definition,
convention, status paragraph, or explanatory calculation.  If a convention
has a coordinate check, place the check in prose.  If a definition has a
nontrivial consequence, state a separate lemma or proposition and prove that
claim.

Known proofs should be developed when they are part of the monograph's
logical spine.  Highly technical proofs may be placed in chapter appendices or
technical subsections, but the main text must point to the proof and state the
precise theorem being proved.  Do not omit a key argument because it is long.

Do not promote an expected large-class statement to a theorem because the
physics literature uses that name.  In CFT, RG flow, bootstrap, anomaly,
duality, large-\(N\), or continuum-limit contexts, theorem labels require a
specified framework, hypotheses, conclusion, and proof status.  Otherwise the
claim must be stated as a conditional argument, conjecture, criterion, formal
calculation, or open problem.

For invariance, anomaly, duality, matching, universality, or reconstruction
claims, the text must identify the object being compared and the equivalence
relation.  Examples: equality of generating functionals, equality of cocycle
classes modulo local counterterms, convergence of correlation functions in a
stated limit, equivalence of local nets, or isomorphism of representation
data.  A named principle without this object-level statement is not certified.

In supersymmetric material, a particle supermultiplet is a Hilbert-space
representation object, while an off-shell superfield multiplet is a
field-variable object.  Do not infer particle content from auxiliary-field
bookkeeping without specifying dynamics, constraints, gauge quotienting, and
quantization or reconstruction.

Supersymmetric Wilsonian claims require an explicit scheme.  Before using
holomorphy, exact superpotentials, quantum moduli spaces, Seiberg-Witten data,
duality tests, or nonrenormalization statements as physics, the text must
state the regulated field-variable space, the Wilsonian functional, the Ward
identity or controlled breaking, the coarse-graining map, the local coordinate
chart, the operator-insertion prescription, and the relation to the 1PI
effective action if a 1PI statement is being made.

Do not conflate a BV/off-shell-superfield formulation of supersymmetric
Wilsonian integration with a manifest supersymmetric ultraviolet
regularization.  BV can state the symmetry, master equation, and canonical
coarse-graining problem after a regulator has been supplied; it does not by
itself define the regulated BV Laplacian, integration cycle, cutoff propagator,
or decoupling limit.  Dimensional reduction is to be treated as a formal
perturbative prescription whose algebraic consistency must be checked at the
loop order being used, especially for epsilon tensors, chiral matrices, and
evanescent tensor structures.  Higher-derivative heat-kernel and
Pauli--Villars-type supersymmetric regulators are candidate constructions
until their regulator fields, transformations, BV pairing, Ward identities,
local counterterms, decoupling, and anomaly class have been explicitly
verified.

Supersymmetric examples in different dimensions must state their own ambient
data.  A two-dimensional Landau--Ginzburg, sigma-model, GLSM, or Calabi--Yau
claim must specify the supersymmetry algebra, target or superpotential data,
regularization status, RG statement, chiral-ring object, and infrared CFT
claim separately.  A three-dimensional Chern--Simons--matter claim must specify
the level, gauge global form, spin or spin-c structure, framing convention,
parity-anomaly counterterm, matter representation, monopole-operator
definition, and boundary condition when relevant.  A six-dimensional SCFT
claim must state whether it is using a nonperturbative definition, a
tensor-branch effective theory, an anomaly polynomial, compactification data,
or an extended-operator diagnostic; none of these is automatically a
Lagrangian definition of the theory.

Supersymmetric localization claims require a localization datum.  Before a
localized integral, JK residue, saddle determinant, instanton contribution, or
zero-size-instanton term is used, the text must state the integration cycle,
odd symmetry, \(Q^2\), deformation, convergence and boundary conditions,
fixed-locus normal complex, zero-mode treatment, singular strata, and contour
or residue prescription.  Infinite-dimensional localization is not certified
by citing finite-dimensional equivariant localization unless the regulator or
limiting argument is part of the construction.

Donaldson/Seiberg-Witten comparisons must be written as QFT comparison
problems with a theorem-status ledger.  Before claiming an equality or
explanation of Donaldson and monopole invariants, the text must state the
twisted \(\mathcal N=2\) Yang--Mills theory, instanton moduli-space data,
Donaldson observables, Coulomb-branch Wilsonian effective action, Abelian
monopole/dyon EFT, singular loci, contact terms, wall-crossing or \(u\)-plane
terms, observable map, and metric-dependence control.  It must also identify
which pieces are established differential-geometric theorems, which are
finite-dimensional localization/gluing statements, and which are still
physical RG assumptions requiring further proof.

Entanglement in QFT is an AQFT/local-algebraic topic before it is a CFT
calculation topic.  Any use of entropy, replica constructions, or modular
Hamiltonians must state the algebraic object, factorization or split-property
assumption, type-III issue, regulator or relative-entropy prescription, and
analytic-continuation hypothesis.

Every example used in the main text must do at least one of the following:

- verify a definition in a nontrivial case;
- show that a hypothesis is necessary;
- compute an invariant introduced in the chapter;
- mark the boundary of a theorem.

Examples that only decorate the prose fail the harness.

## Soft Phrase Audit Rule

Reader-facing prose must not use community habit as a substitute for data.
During every audit pass, search for soft phrases such as "usual",
"standard", "well-known", "schematic", "formal", "one can show", and "it is
known".  Each occurrence must be classified as one of:

- a harmless fixed name or convention already defined in the text;
- a displayed shorthand whose regulated or distributional meaning is stated
  immediately nearby;
- a theorem-level input with hypotheses and proof status;
- a phrase to be rewritten into explicit assumptions, definitions, or a
  conditional statement.

The words themselves are not banned, since terms such as standard boost or
standard representation can be mathematically precise after definition.  What
is forbidden is using them to hide hypotheses, domains, convergence,
normalization, or proof obligations.

Use the standard mathematical name when one exists.  Reserve "datum" for a
genuinely novel structured input whose components must be declared together;
otherwise prefer names such as representation, correspondence, functional,
operator family, amplitude, chart, table, spectral problem, or theorem.  Use
"ledger" only for an actual finite bookkeeping table whose entries are later
checked, not as a synonym for discussion or list.  Use "certified" or
"certification" only for source-coverage and calculation-check status, not as
a decorative assurance in the reader-facing text.  High-density clusters of
these terms should be treated as an audit finding even when every individual
occurrence is locally defensible.

## Positive Formulation Rule

The main text explains objects by their data, definitions, assumptions, and
consequences. It should not be organized around:

- slogans;
- lore or folklore;
- generic textbook correction;
- wrong pictures used as foils;
- "what it is not" framing;
- surprise or exception language where a clean domain statement is available.

Negative clarification is allowed only in a remark, footnote, or appendix after
the positive construction has been given and only to prevent a specific
misreading.

## Figure Rule

Figures are part of the mathematical exposition.  Every floated figure in the
compiled monograph must have a `fig:` label and must be referenced from the
surrounding text with a `Figure~\ref{fig:...}` callout that states its local
role.  Inline TikZ is reserved for notation-sized schematics placed adjacent
to the formula they abbreviate; caption-worthy diagrams belong in floated
figures.  Semantic distinctions in figures must remain readable in grayscale
through line style, weight, marker shape, or direct labeling, not color alone.
Spacetime-axis conventions must either follow the project default, time
vertical and space horizontal, or state the local departure before the figure.
The detailed project policy is `planning/figure_style_guide.md`; the audit
tool is

```bash
tools/audit_figures.py
```

and `tools/audit_figures.py --strict` is the gate once the existing figure
backlog has been fully remediated.

## QFT Ordering Rule

- Kallen--Lehmann spectral representation appears early.
- Perturbation theory for Green functions may precede scattering.
- The S-matrix is nonperturbative first.
- LSZ follows the nonperturbative scattering construction.
- Perturbative S-matrix diagrams follow LSZ.

## Gauge And RG Separation Rule

- Spectral representations are statements about operators acting on the
  relevant positive Hilbert space, or about explicitly stated indefinite
  gauge-fixed spaces.  Gauge-variant propagators must not be treated as
  physical spectral measures.
- Gauge-theory Wilsonian or effective-action claims require one of two
  finite-cutoff frameworks: a BV formulation with the regulated odd
  symplectic space, master action, half-density, BV Laplacian, integration
  cycle, and coarse-graining map stated; or a lattice formulation with compact
  link-variable configuration space, Haar measure, gauge-invariant
  observables, and blocking or scaling map stated.  Any claimed alternative
  must be reduced explicitly to equivalent data before it is used.
- Whenever BV is first introduced or used as a load-bearing framework, the
  text must define the graded field-antifield space, ghost number, parity,
  left/right variational derivatives, antibracket, classical master equation,
  gauge-fixing Lagrangian submanifold, half-density or measure datum,
  BV Laplacian, quantum master equation, and the relation between the master
  equation and gauge-fixed Ward identities.  Later uses may cite this chapter,
  but they must state the finite-cutoff BV data relevant to the calculation.
- A gauge-fixed Wilsonian path integral is gauge-consistent only through the
  quantum BV master equation for the cutoff half-density before gauge-fixing
  restriction.  The Slavnov-Taylor identities are the gauge-fixed projection
  of this equation, and a Wilsonian step in continuum gauge theory must be a
  BV pushforward preserving it.
- The 1PI renormalization group is a comparison of scale-dependent
  coordinates on the 1PI effective action.
- The Wilsonian renormalization group is a cutoff-dependent action flow
  defined by integrating out modes while preserving low-momentum observables.
- Physical scaling limits are statements about correlation functions,
  operator dimensions, spectra, or other specified observables.  These three
  RG notions may be related only after the map between their data is stated.
- A high-scale perturbative RG continuation is not a physical Wilsonian
  cutoff theory.  Treating its endpoint as a UV cutoff, or treating omitted
  operators as absent up to that endpoint, is an additional hypothesis that
  must be stated with its finite-regulator, BV, lattice, or constructive
  framework.
- Standard Model claims must identify which part of the hybrid definition
  they use: nonperturbative QCD matrix elements, the all-orders
  renormalized perturbative electroweak construction, the QCD--electroweak
  coupling through specified color-gauge-invariant local QCD operators,
  weak-effective-theory matching, or perturbative RG continuation of
  renormalized coupling coordinates.  Do not describe the Standard Model
  prediction framework as a finite-cutoff EFT; cutoffs are auxiliary
  regulators to be removed or extra Wilsonian/EFT data in a different
  problem.  The electroweak component of the baseline hybrid Standard Model
  is the all-orders renormalized perturbative chiral gauge theory, not a
  finite-cutoff electroweak theory.
  Coupling a Wightman QCD sector to perturbative electroweak fields is
  additional structure, not automatic juxtaposition: the current/scalar-density
  operator schemes, Ward identities, anomaly contact terms, and mixed-correlator
  prescription must be stated.
  Do not present \(SU(3)_c\times SU(2)_L\times U(1)_Y\) as the gauge group of
  a completed hybrid quantum theory.  It is local charge, representation, and
  bundle/global-form bookkeeping; the color and electroweak factors have
  different mathematical statuses in the hybrid Standard Model definition.
  If a cutoff-like parameter appears in a Standard Model discussion, state
  whether it is merely auxiliary electroweak regularization, weak-EFT
  Wilsonian data, a proposed hybrid construction with continuum Wightman QCD
  and regulated electroweak/source variables, or a proposed full coupled
  regulator.  The first case must be removed or matched away.  The hybrid
  construction case is not the baseline definition and is admissible only if
  the QCD sector remains a continuum Wightman theory and the mixed generating
  functionals, contact terms, and electroweak Ward/BV identities at finite
  electroweak cutoff are specified.  The full coupled regulator case must also
  regulate the color sector and solve the chiral-gauge regulator problem.
  Do not import phenomenology folklore as a theory definition, and do not call
  a quantity a prediction until the required inputs, regulators, matching maps,
  and observable definitions have been specified.
- Beyond-Standard-Model particle-physics models are never accepted as
  explanations, motivations, or UV completions by default.  They may appear
  only as precisely stated mathematical hypotheses added to the hybrid
  definition: either finite EFT extensions with stated operators and matching
  assumptions, or theories with a robust nonperturbative regulator or
  constructive framework.  Literature popularity, phenomenological fashion,
  or perturbative Lagrangian writing is not evidence for physical existence.

## Calculation-Check Rule

All verification gates for ordinary monograph development are local repository
commands.  Do not introduce `.github/workflows/`, GitHub Actions jobs, or
required GitHub status checks unless the author explicitly asks for a GitHub
CI gate.

When a passage depends on convention-sensitive finite algebra, the manuscript
must be accompanied, when feasible, by a public check in
`calculation-checks/`.  This applies especially to gamma-matrix and spinor
conventions, anomaly coefficients, color-factor normalizations,
Feynman-parameter reductions, conformal blocks, superfield identities, and
supersymmetry transformations.

Committed Mathematica checks should be plain Wolfram Language `.wl` files,
not notebook-only `.nb` files.  Run them through

```bash
tools/run_calculation_checks.sh
```

or directly with

```bash
/Applications/Wolfram.app/Contents/MacOS/WolframKernel -script calculation-checks/<file>.wl
```

when Wolfram executables are not visible on `PATH`.  The repository harness
prefers `WolframKernel -script` over `wolframscript -file` when both are
available, because the kernel entrypoint is the direct local batch runner and
avoids `wolframscript` startup/pathologies on some macOS installations.  A
calculation check does not
replace a derivation in the text; it certifies sign, normalization, and finite
algebra used by that derivation.  Computationally heavy checks, numerical
summations, conformal-block recursion, large symbolic reductions, and loop
integral bookkeeping that may grow combinatorially should be implemented in
Python, with Wolfram Language used only for compact reader-facing symbolic
cross-checks.

Executable verification is mandatory.  If a commit introduces or edits a
Wolfram Language check or the calculation-check harness, the verification note
must name the actual backend used, for example
`WolframKernel -script calculation-checks/gamma_trace_checks.wl`, and record
the success marker printed by the script.  A missing `wolframscript` on `PATH`,
a skipped Wolfram pass, or a Python-only pass is not a valid verification of a
Wolfram Language file.  Each committed `.wl` check must print a line of the
form `All Wolfram Language ... passed.`, and
`tools/run_calculation_checks.sh` must fail if that marker is absent.

In `.wl` files, continued arithmetic must keep a binary operator at the end of
the preceding line, not as the first nonspace token of the next line.  A
newline followed by a leading operator can be parsed by `wolframscript -file`
as a new statement.  The calculation harness rejects committed `.wl` checks
with such leading-operator continuations before execution.

## Companion-Script Rule

Numerical examples for lattice Monte Carlo, Hamiltonian truncation, DLCQ,
TBA, period integrals, and similar finite-regulator computations belong in
`qft_scripts/`, not in `calculation-checks/`.  A companion script is
reader-facing infrastructure.  It must declare the finite object being
computed, the regulator parameters, the limiting claim that remains to be
proved or extrapolated, and a smoke mode that runs quickly.  The smoke harness
is

```bash
tools/run_qft_scripts_smoke.sh
```

and the policy is recorded in `planning/14_code_policy.md`.

A companion script never replaces a derivation in the manuscript.  The
chapter that cites it must state the finite theorem or controlled
approximation being illustrated.  Passing the smoke harness certifies only
the finite computation and internal consistency checks named in the chapter,
not a continuum limit, spectrum theorem, or physical QFT construction.

## Compilation Gate

Only chapters that pass this harness may be included in the compiled
manuscript. Draft files may remain on disk but must stay out of volume include
files.

## Audit Questions

- What is the framework?
- What are the primitive data?
- What is constructed?
- Are all symbols defined?
- Are all definitions proper?
- What is the first nontrivial claim?
- Where is that claim proved, argued, or classified?
- If an external theorem is cited, are its hypotheses, conclusion, and local
  role stated, and is the proof status clear?
- Are all limits and approximations stated?
- Are all figures mathematical content?
- Does the chapter preserve the source-order spine?
