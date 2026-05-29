# 2026-05-29 Thirty-First Cross-Volume Wrapper Pass

## Scope

This pass continues GitHub issue #691 after commit `cf5a417b`.  The emphasis
was on statements where the named theorem-family wrapper overstated a direct
calculation, an exact finite-regulator identity, or a consequence whose real
content is already contained in the hypotheses.

## Demotions

Eleven theorem-family wrappers were demoted:

- Volume I, Chapter 15: massive Wigner transformation law, keeping the induced
  representation and mass-shell half-density calculation in prose.
- Volume II, Chapter 16: finite-regulator Wetterich equation, keeping the
  fixed-cutoff Legendre-transform derivation explicit.
- Volume II, Chapter 19: colored-partition growth and the flux-string
  Hagedorn scale, keeping the saddle/asymptotic estimate under the neighboring
  controlled-approximation warning.
- Volume II, Chapter 24: component form of the quantum master equation,
  keeping the BV-Laplacian exponential calculation.
- Volume X, Chapter 5: first-order hydrodynamic entropy-production positivity.
- Volume X, Chapter 10: finite Markov reservoir entropy production.
- Volume VII, Chapter 2: component Wess--Zumino Lagrangian from superspace.
- Volume VII, Chapter 4: finite circle-Darboux model of BV pushforward.
- Volume XI, Chapter 4: finite-size scaling from an RG chart; this was
  explicitly a consequence of the finite-size scaling datum rather than an
  independent theorem.
- Volume XII, Chapter 10: associativity and first commutator of the pAQFT
  Hadamard star product.
- Volume XII, Chapter 11: pushforward covariance of the Einstein--Langevin
  source under a linear retarded solution map.

The theorem-form audit guardrail was extended with these titles.

## Retained After Reading

The following short candidates were read but retained because the compact proof
is backed by real analytic, geometric, or functional-analytic content rather
than by mere substitution:

- Fredholm expansion and canonical coefficients.
- Endpoint finite part and endpoint exponents in large-\(N\) two-dimensional
  QCD.
- Exact bosonized local gauge sector of the Schwinger model.
- BV pushforward with fluctuation boundary.
- Rindler normal form of a nonextremal horizon.
- Triangulation independence of the finite-gauge cocycle weight.
- Finite Grassmann reflection-positivity criterion.
- Finite-codimension critical surface from the stable-manifold chart.
- Polyakov--Wiegmann identity in the chapter normalization.
- Integrated nonsinglet axial Ward identity.

## Counts

After this pass:

- theorem environments: 96
- proposition environments: 383
- lemma environments: 29
- corollary environments: 10
- proof environments: 513
- total theorem-family environments: 518

The high-confidence remaining-demotion estimate is now roughly 5--10.  A
separate, slower second pass is still needed for borderline cases where the
substance is not in a trivial proof but in hypotheses that require more
justification or a clearer status label.

## Verification

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- stale-label scan for all eleven removed theorem-family labels
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reports `Pages: 2581`
