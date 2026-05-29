# Planar ABA local-algebra wrapper audit pass

Date: 2026-05-29.

This pass continued the theorem/proposition substance audit in the planar
asymptotic Bethe ansatz chapter.  The focus was the local
\(\mathfrak{su}(2|2)_{\rm c}\) intertwiner and nesting derivations, where
several finite convention checks had been written in proposition/proof form.

Changes made:

- The local intertwining and block-unitarity check was demoted from
  proposition/proof form to a worked paragraph.  The calculation verifies the
  chosen dynamic-frame amplitude chart and finite block unitarity; it is a
  local algebra check, not a proof of crossing or Yang--Baxter factorization.
- The single level-III nesting step was demoted from proposition/proof form to
  a worked paragraph.  The hard inputs are the level-II matrix, the contact
  term convention, and the graded exchange sign; after those inputs are fixed,
  the displayed one-body coefficient and scattering factor are obtained by a
  two-site substitution.
- The weak limit of the rank-one ABA orientation was demoted from
  proposition/proof form to a worked paragraph.  It is an important convention
  bridge between the \(SL(2)\)-vacuum and compact \(SU(2)\) orientations, but
  mathematically it is an ordinary weak-branch expansion of the Zhukovsky
  variables and the rational factor.
- `tools/audit_theorem_form.py` now rejects reintroduction of the three
  demoted titles as theorem-family wrappers.

Manual review notes:

- The generic rank certificate for the one-copy intertwiner remains
  proposition-level because it displays a row-echelon chart for the finite
  intertwining system and proves one-dimensionality of the generic solution
  space.
- The single level-II nesting step remains proposition-level because it
  derives the level-II one-defect factor from local exchange equations; it is
  the first genuine nesting move, not merely a convention expansion.
- The fusion of a Bethe string remains proposition-level in this pass because
  it combines adjacent-pole fusion, endpoint telescoping, central-charge
  shortening, and the scalar-fusion product while explicitly separating matrix
  projection and dressing-branch inputs.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; resulting PDF has
  2577 pages)
