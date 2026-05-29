# Fortieth Cross-Volume Wrapper Pass

Date: 2026-05-29.

Scope: continued issue #691 anti-wrapper audit, with this pass focused on
short proof environments in the singular-SPDE constructive chapter.  The
semantic criterion was whether the numbered statement contained an independent
mathematical construction or estimate, rather than merely recording that a
previously assumed comparison, convergence, or moment hypothesis may be
transported through an elementary limiting argument.

## Demoted or Reclassified

- `Closedness of OS reflection positivity under weak convergence` was demoted
  from proposition to remark.  The bounded-cylinder part is weak convergence
  of bounded continuous quadratic forms; the polynomial-cylinder extension is
  the standard truncation step once uniform integrability is separately
  available.  The final constructive input is the moment estimate, not this
  transport observation.

- `Regulator comparison criterion for OS-positive stochastic limits` was
  demoted from proposition to remark.  Its content records what a genuine
  lattice/Fourier-Galerkin comparison theorem must deliver; it does not prove
  that analytic comparison.  The text now states positively that the
  comparison estimate is a separate constructive theorem.

- `Polynomial OS observables from exponential moments` was demoted from
  proposition to remark.  The argument is a useful uniform-integrability
  observation based on exponential moment bounds, but the substantive part in
  a constructive field theory remains the proof of those exponential moment
  bounds for the chosen regulator family.

- `Scale-summed dyadic-net coordinate upgrade` was reclassified from theorem
  to corollary.  The proof applies the preceding dyadic-net theorem at each
  physical scale and sums a geometric series.  This is important infrastructure
  but not an independent theorem.

- `Kernel criterion for projective dual-norm bounds` was reclassified from
  proposition to lemma and retitled `Projective kernel estimate for dual-norm
  bounds`.  The proof is a projective-crossnorm/Bochner-integral estimate used
  by later model-kernel bounds; lemma status matches its role.

## Guardrails Added

The theorem-form audit now rejects any reintroduction of the three SPDE
transport criteria, and the old projective-kernel criterion title, as numbered
theorem-family wrappers.

## Read and Retained

The following short candidates were read and retained because their proof
content is mathematical rather than wrapper-like:

- `Common pole extraction in a restored massive multiplet`, whose proof uses a
  spectral decomposition, a generalized eigenvalue problem, and an explicit
  exponentially small excited-state remainder.

- `Forward spin-polarizability and GDH sum rules`, whose proof uses odd
  forward-dispersion analyticity, a subtraction condition, the optical theorem,
  and the low-energy theorem.

- `Existence and uniqueness of the MS pole recursion`, whose proof is a finite
  filtered recursion under an explicit nonresonance/invertibility hypothesis.

## Current Inventory and Estimate

After this pass the monograph contains:

- theorem: 93
- proposition: 360
- lemma: 30
- corollary: 11
- theorem-family total: 494
- proof: 489
- remark: 308

A broader heuristic scan of short proofs, low-structure proofs, and
criterion/bridge/comparison-style titles flags 81 remaining candidates.  Many
are expected false positives: compact spectral, representation-theoretic, and
finite-dimensional algebraic proofs often look short syntactically while still
doing real work.  Based on the hit rate from the recent semantic passes, the
working estimate is that roughly 20--40 theorem-family statements still need
demotion or reclassification, and roughly 40--70 additional proof environments
need strengthening, retitling, or tighter hypotheses.  This estimate should
not be treated as closure; every proof still needs to be read semantically.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- direct missing-label scan: `missing_count 0`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` gives `Pages: 2592`

