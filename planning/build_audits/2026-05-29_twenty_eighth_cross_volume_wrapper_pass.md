# Twenty-Eighth Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading another high-signal subset of short or cue-heavy
theorem-family entries.  This pass focused on statements whose displayed
calculation is correct but whose role in the monograph is explanatory,
diagnostic, or algebraic rather than theorem-level.

## Demoted From Theorem-Family Form

- `Mass gap from Euclidean clustering` is now a spectral-consequence
  paragraph.  The spectral-theorem support argument remains, but the
  nontrivial constructive input is explicitly identified as the preceding
  Euclidean clustering theorem.
- `Bounded Wick-cylinder comparison for stable quartic cutoffs` is now a
  comparison paragraph with a labelled equation.  Later uses now refer to the
  equation rather than to a corollary wrapper.
- `Linking phase in finite BF theory` is now an exact finite-sum computation
  paragraph.  The cochain equation, chain pairing, and linking-number phase
  remain explicit.
- `Banks--Casher relation under a spectral-density hypothesis` is now a
  spectral-density paragraph.  The thermodynamic spectral-density hypothesis
  is named as the substantive input, and the eigenvalue-pair calculation is
  retained.
- `Single-channel finite-volume pole reconstruction` is now a resonance
  reconstruction-target paragraph.  It states the algebraic second-sheet pole
  target while no longer presenting analytic continuation control as a
  proposition-level conclusion.

## Guardrail Update

`tools/audit_theorem_form.py` now rejects the five demoted titles if they are
reintroduced as theorem/proposition/lemma/corollary wrappers.

## Retained After Reading

The Kallen--Lehmann representation for \(W_2\), stress-tensor OPE and
Virasoro algebra, integrated nonsinglet axial Ward identity, mixed-covariance
criterion for common Wick limits, Baldin sum rule, functoriality of the free
scalar field, QME preservation by BV pushforward, special-conformal
invariance from radial spectrum positivity, regulator-comparison criterion
for OS-positive stochastic limits, gap-stable Ritz counting, and scalar
Haag--Ruelle map construction remain theorem-family candidates for now.  Each
one packages a reusable spectral, contour, Ward-identity, Gaussian,
dispersion, functorial, BV, representation-theoretic, convergence,
min--max, or scattering construction rather than a one-line algebraic check.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 555.
- Proof environments: 550.
- Strict regenerated high-signal short/cue-heavy queue: 20 candidates.  My
  current estimate is that roughly five to ten of this strict queue may still
  require demotion or reframing, with perhaps another ten to twenty softer
  cases likely to appear in the broader second pass.

## Verification

- Stale-label scan for the five removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2579 pages.
