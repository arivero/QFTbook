# Forty-Fifth Cross-Volume Wrapper Pass

Date: 2026-05-29.

Purpose: continue issue #691, with emphasis on assumption/hypothesis versus
proposition/theorem status.  The pass read title-risk and proof-substance
clusters rather than relying on proof length alone.

## Demoted or Reframed

- Volume II, chapter 10: `Scheme equivalence for matched physical observables`
  was moved from theorem form to a remark with derivation prose.  The content
  is finite-regulator coordinate consistency plus matched source/field
  normalization data, not a theorem-level QFT result.
- Volume II, chapter 13: `Flat-space renormalized trace identity` was
  lowered from proposition to lemma.  It is a useful finite-part/contact
  identity, but the surrounding contact-distribution proposition carries the
  substantive source-functional statement.
- Volume II, chapter 19b: `Fixed-order finiteness criterion for IRC-safe
  measurements` was moved out of proposition/proof form into a controlled
  approximation.  The statement is conditional on fixed-order soft/collinear
  factorization and KLN or PDF factorization input; it is not a
  nonperturbative theorem about arbitrary jet measurements.
- Volume III, chapter 5: `Stress-tensor OPE and the Virasoro algebra` was
  lowered from proposition to lemma.  It is the contour-algebra consequence of
  the already defined two-dimensional stress-tensor OPE.
- Volume VI, chapter 9: `KZ equations from the endpoint Ward identities` was
  lowered from theorem to proposition.  The derivation is a Ward/OPE residue
  computation inside the WZW endpoint, not a theorem of independent analytic
  construction.
- Volume VI, chapter 9: `Symmetric-space Lax equivalence` was lowered from
  proposition to lemma.  The coefficient comparison is useful but elementary
  once the symmetric-space Maurer-Cartan split and equation of motion are in
  place.
- Volume VI, chapter 9: `Algebraic Yang-Baxter identity for the displayed
  sausage matrix` was moved from proposition/proof to an exact symbolic
  verification example.  The text keeps the sparse-tensor rational-function
  verification and its meromorphic conclusion, but it no longer presents the
  finite algebra check as a proposition.
- Volume IX, chapter 3: `Cocharacter criterion for the monopole singularity`
  was lowered from proposition to lemma.  It is the local cocharacter-lattice
  classification of the prescribed singularity, not the full construction of a
  line-operator sector.
- Volume X, chapter 12: `Integrated nonsinglet axial Ward identity` was
  lowered from proposition to lemma.  It is the local change-of-variables Ward
  identity used in the chiral-restoration discussion.
- Volume XI, chapter 9: `Dyadic Cauchy criterion for random models` was
  lowered from theorem to proposition.  It is an important convergence
  proposition in the regularity-structure proof infrastructure, but the
  theorem-level burden remains the construction of the BPHZ random model and
  its analytic estimates.

## Strengthened Scope Rather Than Demoted

- Volume VII, chapter 5: `Wilsonian one-loop exactness of the holomorphic
  gauge coordinate` was retained as a proposition, but a scope paragraph was
  added before it.  The text now says explicitly that the input is a
  weak-coupling Wilsonian patch with a chiral local gauge-kinetic coordinate
  and a complete anomalous-spurion ledger.  Existence of such a patch for a
  concrete regulator is part of the supersymmetric Wilsonian-definition
  problem, not a consequence of the holomorphy argument.

## Read and Retained in This Pass

- McKean-Singer identity: retained as a proposition because the proof uses the
  elliptic spectral pairing and heat-trace cancellation.
- Fusion identity as a residue identity: retained as a proposition because it
  performs the bound-state pole extraction with explicit meromorphic and
  contour hypotheses.
- Axis trace nonuniqueness: retained as a proposition because it constructs a
  nonzero smooth tempered wave solution with vanishing axis trace on a slab,
  using finite propagation.
- Largest-time identity for a scalar graph: retained as a proposition because
  the proof is a regularized distributional circling identity, not a mere
  substitution.
- BPHZ finiteness and Zimmermann identities: retained at theorem/proposition
  level after reading the sector/Taylor-remainder estimates and normal-product
  forest argument.
- Local BV-BRST comparison for Yang-Mills: retained as theorem-level local
  homological machinery, with Koszul-Tate acyclicity and nonminimal-doublet
  contraction as the real hypotheses.
- Kontsevich-Segal allowability argument criterion, microlocal product
  criterion, and Hadamard coefficient recursion: retained as theorem-level
  analytic machinery after reading the proofs.
- The current SPDE convergence propositions were read as proof infrastructure.
  Most were retained because they contain kernel estimates, Wick covariance
  estimates, compactness/tightness arguments, or explicit scale-net
  conversions rather than one-line substitutions.

## Harness Update

`tools/audit_theorem_form.py` now rejects reintroduction of the demoted
theorem-family titles:

- `Fixed-order finiteness criterion for IRC-safe measurements`
- `Algebraic Yang-Baxter identity for the displayed sausage matrix`
- `Scheme equivalence for matched physical observables`

## Inventory After Edits

- theorem: 87
- proposition: 300
- lemma: 87
- corollary: 10
- theorem-family total: 484
- proof environments: 479
- controlled approximations: 70
- examples: 75
- remarks: 312

The broad title screen now leaves 31 theorem/proposition candidates with
words such as `criterion`, `identity`, `equivalence`, `comparison`,
`convergence`, or `normalization`.  Several are genuine mathematical
machinery; the remaining estimate is about 10-20 further demotions or
reclassifications, plus 15-30 proof-scope or hypothesis-clarity improvements
after semantic reading.  This is not closure of #691.
