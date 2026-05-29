# Planar QSC wrapper-boundary audit pass

Date: 2026-05-29.

This pass continued the assumption/theorem audit in the planar QSC chapter,
with emphasis on statements whose proofs were finite coefficient algebra after
substantial analytic QSC input had already been assumed.

Changes made:

- The collapsed-cut digamma package was demoted from lemma/proof form to a
  worked paragraph.  The substantive meromorphic uniqueness statement remains
  Lemma `lem:qsc-half-integer-digamma-primitive`; the package is the
  specialization obtained by multiplying that primitive by a polynomial
  quotient and reading off residues, logarithmic asymptotics, and shift
  defects.
- The small-spin QSC slope was demoted from proposition/proof form to a worked
  extraction.  The local analytic small-spin QSC germ is now stated explicitly
  as Assumption `ass:qsc-small-spin-germ`, including the gauge choice, leading
  `P`-functions, regularity split, large-`u` coefficients, and charge
  relations.  The subsequent paragraph derives the Bessel slope formula from
  those data.
- The planar-integrability crosswalk now describes the small-spin slope result
  as a coefficient extraction from an analytic germ, rather than as an
  independent proof of the full QSC small-spin construction.
- `tools/audit_theorem_form.py` now rejects reintroduction of the two demoted
  titles as theorem-family wrappers.

Manual review notes:

- The half-integer digamma primitive remains lemma-level because it contains a
  uniqueness statement for meromorphic solutions of a difference equation,
  modulo an entire bounded periodic ambiguity.
- The twist-two Baxter family remains proposition-level because the proof gives
  a finite telescoping certificate for the Baxter equation and derives endpoint
  logarithmic derivatives through Legendre and Chu--Vandermonde identities.
- The displacement-normalization relation for the small cusp remains
  proposition-level because the proof extracts a universal logarithmic
  coefficient from the finite-part Fourier transform of the displacement
  two-point distribution under a stated defect Ward identity.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; 2577-page PDF)
