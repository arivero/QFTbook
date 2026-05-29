# 2026-05-29 Fourth Cross-Volume Wrapper Pass

Scope: continuation of issue #691 anti-wrapper audit.  This pass read the
next broad-heuristic cluster in Volume II and classified the claims by
substance rather than by title.

Demotions made:

- Volume II, QCD: demoted `Leading Sudakov factor in the back-to-back EEC`
  from proposition/proof form to a scoped fixed-coupling leading-logarithmic
  calculation inside the EEC factorization datum.
- Volume II, QCD: demoted `Number and momentum sum rules at one loop` from
  proposition/proof form to a distributional \(D_0\)-kernel check in prose.
- Volume II, Standard Model: demoted `Kernel of the minimal Standard Model
  representations` from proposition/proof form to finite center-charge
  arithmetic in prose.
- Volume II, Standard Model: demoted `Tree-level matching to Fermi theory`
  from proposition/proof form to the low-energy coefficient calculation
  obtained by solving the massive charged-vector equation in a derivative
  expansion.

Strengthenings made:

- Volume II, QCD: strengthened the zero-recoil Isgur--Wise normalization proof
  by spelling out the leading-static-theory scope, background heavy-flavor
  source normalization, phase choice for the isolated light-cloud states, and
  the velocity-state normalization fixing the coefficient \(2v^\mu\).
- Volume II, anomalies: strengthened the relative BRST-class proposition by
  making explicit the Chevalley--Eilenberg role of the ghost, the
  variational-bicomplex step turning an integrated zero into a total
  derivative, the local counterterm/coboundary relation, and the boundary or
  inflow hypotheses.

Guard update: `tools/audit_theorem_form.py` now rejects recurrence of the four
newly demoted theorem titles.

Verification:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed cleanly with `monograph/tex/main.pdf` at 2581 pages.
The broad overinclusive heuristic count moved from 200 to 194 candidates.
