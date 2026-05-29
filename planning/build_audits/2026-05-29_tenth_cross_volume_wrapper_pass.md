# Tenth Cross-Volume Wrapper Pass

Date: 2026-05-29

Scope: continued issue #691 after the ninth anti-wrapper checkpoint.  This
pass first read the remaining compact-proof queue in context, then switched to
an assumption/definition-heavy scan for proofs whose conclusion was carried
mainly by the hypothesis or by a finite algebraic convention.

## Demotions

Demoted seven theorem-family wrappers to prose calculations or conditional
construction paragraphs:

- `path-integral Schwinger limits as Wightman data`.
- `Fermionic coherent-state resolution`.
- `Physical-axis unitarity excludes the resonance pole`.
- `EEC sum rules and the contact term`.
- `Chamber jump as a BV boundary term`.
- `Why equation-of-motion operators are coordinates`.
- `Fusion of the finite condensation defect`.

The mathematical content was kept in the manuscript.  The point of the demotion
is that the theorem-level work is elsewhere: OS reconstruction itself, finite
Berezin algebra, exact partial-wave unitarity, the definition of the
calorimetric observable, Stokes on the compactified moduli problem, the
SMEFT quotient datum, or the construction of the topological surface-network
defect.

## Strengthened Retained Statements

- Expanded the time-ordered Wightman-piece compatibility proof to make the
  local chamber cover, adjacent spacelike transpositions, and sheaf gluing of
  distributions explicit.
- Expanded the Schwinger-model anomaly-induced mass proof to state the
  distributional operator identity, the no-external-line sector, and the shared
  contact-term convention.
- Expanded Wess--Zumino consistency from descent using the BRST descent tower
  and the \(I_{D-1}^{(2)}\) coboundary.
- Expanded staggered Thirring reflection positivity by separating the free
  mid-link crossing factor, the quartic boundary links, the positive-side
  even generator, and the nonnegative finite crossing-factor expansion.

## Guardrails

`tools/audit_theorem_form.py` now rejects recurrence of all seven demoted
titles as theorem-family wrappers.

## Verification

Commands run before the full build:

- stale-label scan for all removed labels.
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_unnumbered_display_labels.py`

Final checkpoint verification completed:

- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` (`Pages: 2583`)

The full build and final log scan are clean.

## Remaining Queue

The `<=115`-word immediate-proof heuristic queue is now four items:

- `Fredholm expansion and canonical coefficients`.
- `Kernel of the causal propagator`.
- `Unitary implementation of an invariant state`.
- `Chern--Weil transgression`.

These were read in context during this pass and look like genuine compact
infrastructure rather than wrappers.  They should remain visible for future
manual audit, but padding them merely to defeat a length heuristic would be the
wrong correction.
