# Forty-Third Cross-Volume Wrapper Pass

Date: 2026-05-29.

Purpose: continue the #691 anti-wrapper audit by reading statement/proof units
whose titles, adjacency to assumptions, or proof shape suggested possible
overpromotion.  This pass focused on support calculations and hypothesis-local
algebra that should not be presented as structural propositions.

## Reclassified

- Vol II ch19c: `Hybrid coupling is additional structure` was changed from a
  proposition with a proof to a remark.  The content is important for the
  hybrid Standard Model definition, but its argument is a logical explanation
  of what data are not supplied by two separately specified sectors, not a
  theorem-level result.
- Vol II ch20c: `Endpoint finite part` was changed from proposition to lemma.
  It is a technical principal-value asymptotic used by the endpoint-exponent
  corollary.
- Vol V ch11: `Conjugacy-class normalization for primitive joining` and
  `Transposition class algebra: join and split factors` were changed from
  propositions to lemmas.  They are finite symmetric-group counting lemmas
  supporting the orbifold OPE discussion.
- Vol V ch12: `Trace-class estimate for one-channel sewing` was changed from
  proposition to lemma.  It is a Hilbert-space estimate used as an input to
  sewing convergence.
- Vol V ch13: `Level-one and level-two block coefficients` and `Level-three
  block coefficient and determinant` were changed from propositions to
  lemmas.  They are explicit Virasoro Gram-matrix computations.
- Vol VII ch13: `Zhukovsky Fourier transform` and `Single level-II nesting
  step` were changed from propositions to lemmas.  The first is a
  convention-sensitive contour identity; the second is a local nesting algebra
  check.
- Vol VII ch14: `Excited-state contour deformation in one species` and
  `Auxiliary-string kernel inverse` were changed from propositions to lemmas.
  Both are technical support identities in the mirror-TBA/Y-system chapter.
- Vol X ch12: `One-loop pion-gas correction to the condensate` was changed
  from proposition to lemma.  It is an effective-theory one-loop calculation
  with the scope already stated in the surrounding text.
- Vol XI ch05: `Rectangle coefficients` was changed from proposition to
  lemma.  It is the tree-level Symanzik coefficient calculation.
- Vol XI ch09: `L^q-density criterion for interacting negative-Sobolev
  moments` and `Finite lattice quartic tails` were changed from propositions
  to lemmas.  They are technical estimates in the stochastic-quantization
  proof stack.
- Vol XI ch10: `Finite TFFSA spectral-flow derivative` was changed from
  proposition to lemma.  It is a finite-matrix perturbation lemma used by the
  benchmark protocol.

## Read And Retained

- The `Local P-Q bridge` example in Vol VII ch15 is already in paragraph form,
  not theorem-family form; the assumption is explicitly identified as the
  nontrivial datum and the algebra below it is local bookkeeping.
- The higher-dimensional angular-counting statement in Vol II ch07 remains a
  conditional proposition because the title and hypotheses explicitly isolate
  the angular-domain input.
- The BFKL Mellin-eigenvalue computation in Vol II ch19 remains a proposition:
  it constructs the analytically regularized eigenvalue of the leading kernel,
  not merely a substitution.
- The planar circular Wilson-loop Gaussian-model result in Vol VII ch16 remains
  a theorem about the large-\(N\) Gaussian matrix model, while the separate QFT
  localization-to-Gieseker matching remains a hypothesis.
- The Zhu top-level action, finite-gauge surface character formula, unitarity
  bound, Ginsparg-Wilson Berezinian, and finite Grassmann reflection-positivity
  criterion were read as substantive structural statements and retained.

## Harness

- Updated `tools/audit_theorem_form.py` so the reviewed assumption-neighbor
  exception for the Zhukovsky Fourier transform records its new lemma status
  rather than the former proposition status.

## Verification

- `git diff --check`
- label/reference scan: all refs resolved
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`

This is a checkpoint, not closure of #691.  The remaining queue is now weighted
toward subtler cases: strong hypotheses followed by conditional structural
claims, and proposition-level calculations that may still need to be read in
their local context.
