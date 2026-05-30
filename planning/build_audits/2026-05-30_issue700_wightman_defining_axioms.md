# Issue #700 Wightman Defining-Property Pass

## Scope

This pass addresses the foundational Volume IV Chapter 1 case in GitHub issue
#700.  The chapter used Wightman data in prose before giving any formal
definition of the central object; the first formal definition was only the
late observable-subpresentation definition.  The fix is to make the Wightman
field presentation itself the first mathematical object of the chapter.

## Manuscript Changes

- Added Definition `def:cyclic-wightman-field-presentation` at the opening of
  Volume IV, Chapter 1.  It aggregates the Hilbert-space data, vacuum,
  strongly continuous Poincare representation, common invariant domain,
  field-label adjunction and parity, operator-valued tempered distributions,
  domain adjunction, covariance, spectrum condition, graded locality, and
  cyclicity.
- Separated the pure vacuum sector condition
  \(E_P(\{0\})\mathcal H=\mathbb C\Omega\) from the base cyclic presentation,
  so the cluster/unique-vacuum theorem remains a theorem rather than an
  axiom smuggled into the definition.
- Rewrote downstream theorem statements and prose to refer to the named
  definition: cluster decomposition, Wightman reconstruction, PCT, and
  observable Wightman subpresentations.
- Corrected the cluster theorem notation from an undefined `E({0})` to the
  joint translation spectral measure `E_P({0})`.
- Added a new chapter dossier recording notation, claim ledger, proof
  boundaries, figures, and the issue #700 audit note.

## Accuracy Boundary

The new definition is still a presentation-level axiom package.  It does not
construct a nontrivial interacting QFT, prove essential self-adjointness of
field closures, or identify a generated field algebra with an AQFT local net.
Those remain separate construction/comparison problems.

## Verification Completed

- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`, clean full build and log scan; output:
  `monograph/tex/main.pdf` at 2670 pages.
