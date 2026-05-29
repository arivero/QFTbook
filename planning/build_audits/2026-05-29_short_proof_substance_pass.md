# Short-proof substance pass

Date: 2026-05-29.

This pass continued issue #691 by regenerating a narrow queue of theorem-family
items whose proof blocks were exceptionally short after the earlier
anti-wrapper passes.  The queue contained four items.  Each was read in local
chapter context before editing.

Actions taken:

- Strengthened the Haag--Ruelle filtered-creator proposition.  The proof now
  constructs the double-cone truncations \(B_R\), proves the Schwartz tail
  estimate in operator norm, states the Fourier convention for
  \(\widehat\chi\), and applies the joint spectral theorem directly to
  \(B\Omega\).
- Strengthened the Haag--Ruelle point-field projection proposition.  The proof
  now treats \(\hat\phi(x)\Omega\) as a distributional rigged-Hilbert object,
  derives the one-particle form factor from translation covariance, derives
  its constancy from scalar Lorentz covariance and multiplicity one, and only
  then smears to obtain a Hilbert vector.
- Demoted the continuous-spin alternative from proposition/proof form to a
  worked paragraph.  The joint spectral-measure rotation argument remains
  explicit.
- Demoted the Ramond zero-mode bound from corollary/proof form to a worked
  paragraph.  The \(r=s=0\) anticommutator and positivity argument remain
  explicit.
- Updated the corresponding chapter dossiers and extended
  `tools/audit_theorem_form.py` so the demoted titles cannot reappear as
  theorem-family wrappers.

Verification run before checkpoint:

- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- stale-label search for the two removed theorem-family labels
- short-proof queue scan: zero remaining candidates under the current
  narrow line-count heuristic
- `git diff --check`
- `tools/build_monograph.sh` (clean build and log scan; resulting PDF has
  2577 pages)
