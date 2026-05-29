# Twenty-Fifth Cross-Volume Wrapper and Hypothesis-Status Pass

Date: 2026-05-29.

## Purpose

Continue #691 by reading another set of theorem-family statement-proof units
where the heading advertised a theorem but the proof was a convention check,
coefficient calculation, quotient dictionary, or consequence of a stronger
input already assumed.  The pass focused on demoting items that should remain
visible as derivations but should not pretend to be independent theorem-level
machinery.

## Demoted From Theorem-Family Form

- `Classical quotient and chiral functions` is now a quotient-dictionary
  paragraph under an explicit Kempf--Ness comparison input.  The coordinate
  ring and polystable-orbit warning remain.
- `Mass degeneracy inside an isolated pure-SYM multiplet` is now a spectral
  consequence paragraph.  The domain and atom-existence caveats remain.
- `Lorentz covariance forces the supercharge anticommutator` is now a
  representation-theoretic paragraph following the quoted HLS theorem.
- `Heavy-light decay-constant scaling` is now an HQET matching calculation.
- `B+L anomaly and B-L mixed-gauge cancellation` is now a Standard Model
  anomaly-coefficient calculation, with the \(\nu^c\) caveat retained.
- `Spin covariance and chirality trace` is now a spinor-convention calculation.
- `Bogoliubov normalization and particle number` is now a mode-normalization
  calculation in the curved-spacetime particle-creation chapter.
- `\(\mathcal N=4\) determinant cancellation on \(S^4\)` is now a localization
  determinant cancellation paragraph.
- `Pure SYM discrete chiral anomaly` is now an anomaly-phase calculation, still
  separated from the Wilsonian glueball hypothesis that follows it.
- `Verlinde defect fusion and modular covariance` is now a modular-defect
  calculation under the rational diagonal CFT assumptions.
- `Lorentz covariance of chiral and Majorana reductions` is now a local spinor
  representation paragraph.
- `Displacement normalization of the small cusp` is now a consequence
  paragraph under the shape-variation Ward-identity input; the finite-part
  Fourier calculation remains.

## Retained After Reading

The integrated nonsinglet axial Ward identity was read and retained as
theorem-family content because it states a regulator-dependent Ward identity
with contact terms and a thermal integrated consequence, not merely a charge
sum.  The finite Grassmann reflection-positivity criterion, transfer-matrix
commutativity, K-S positive-energy cylinder, strong-coupling area mechanism,
and stochastic/SPDE tightness or scale-gap criteria also remain active
theorem-family candidates for now: each carries reusable machinery, estimates,
or a controlled-regime statement rather than just a substitution.

## Counts After This Pass

- Theorem/proposition/lemma/corollary environments: 574.
- Proof environments: 569.
- Strict regenerated high-signal short/cue-heavy queue: 21 candidates under
  the current heuristic.  This is still only a reading queue; it contains
  genuine short proofs as well as possible demotion targets.

## Verification

- Stale-label scan for the twelve removed labels: clean.
- `python3 tools/audit_theorem_form.py`: clean.
- `tools/audit_negative_scope_prose.py`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `python3 tools/audit_unnumbered_display_labels.py`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: clean.
- `pdfinfo monograph/tex/main.pdf`: 2578 pages.
