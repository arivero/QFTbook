# Volume I/III theorem-form cleanup pass

Date: 2026-05-29.

This pass continued the issue #691 proof-substance audit by reading the next
fresh short-proof candidates in context.  The goal was to separate actual
structural propositions from local coordinate, residue, or differentiation
calculations.

Changes made:

- The free scalar covariance statement in Volume I Chapter 2 was demoted from
  proposition/proof form to a worked paragraph.  The calculation is the
  second-quantized one-particle covariance check for the free mass-shell
  kernel, not a theorem about interacting fields.
- The infinitesimal translation covariance statement in Volume I Chapter 3 was
  demoted from proposition/proof form to prose.  It is obtained by
  differentiating the finite covariance definition and fixing the sign
  convention for smeared distributions.
- The Cauchy-data solution formula in Volume I Chapter 6 was demoted from
  proposition/proof form to prose.  It is the Fourier-coordinate solution of a
  two-by-two linear system for the positive- and negative-frequency
  coefficients.
- The finite-dimensional Gaussian source functional in Volume I Chapter 8 was
  demoted from proposition/proof form to prose.  The completion-of-the-square
  calculation remains explicit, with the continuum-regulator questions named
  after the calculation.
- The Noether identity in Volume I Chapter 7 remains proposition-level, but the
  proof was expanded to state its actual structural inputs: the first
  variational identity, the off-shell variational-symmetry identity, jet-level
  equality before integration, and the improvement ambiguity.
- The infinitesimal stress-tensor transformation, Schwarzian cocycle, and
  inversion factors in Volume III were demoted from theorem-family form to
  worked paragraphs.  Their equations remain labelled and the finite
  stress-tensor transformation now refers directly to the Schwarzian cocycle
  and linearization equations.
- `tools/audit_theorem_form.py` now rejects reintroduction of the demoted
  titles as theorem-family wrappers.

Manual review notes:

- The free scalar microcausality proposition in Volume I Chapter 2 remains
  theorem-family content in this pass because it identifies the commutator with
  the Pauli--Jordan distribution and then proves spacelike vanishing from the
  support/antisymmetry structure.
- The localized-parameter Noether proposition remains theorem-family content:
  it is the first point where the current is characterized as a response to a
  localized source, not merely as a constant-parameter conservation law.
- The finite Schwarzian stress-tensor transformation remains proposition-level:
  it integrates the infinitesimal Ward action into a finite affine/projective
  cocycle and derives the plane-cylinder Casimir shift.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; resulting PDF has
  2577 pages)
