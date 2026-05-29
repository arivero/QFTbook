# 2026-05-29 Third Cross-Volume Wrapper Pass

Scope: continuation of issue #691 anti-wrapper audit.  Read the next
high-scoring theorem/proof candidates produced by the broad local heuristic
and separated genuine analytic estimates from convention checks and finite
algebra.

Demotions made:

- Volume XI, Chapter 5: demoted `Finite \(\mathbb Z_2\) character expansion`
  from proposition/proof form to an exact finite algebraic expansion in prose,
  with equation labels for the partition function and Wilson-loop numerator.
- Volume I, Chapter 16a: demoted `Two-component sign and contraction
  identities` and `Same-metric Wess-Bagger phase translation` to explicit
  convention checks in prose.
- Volume I, Chapter 16: demoted `Free Dirac equations and charge convention`
  to a direct consequence of the defining intertwiners and oscillator charge
  commutators.
- Volume I, Chapter 20: demoted `Charge normalization of the electron
  current` to the distributional plane-wave normalization calculation
  \(F(0)+G(0)=1\).
- Volume II, Chapter 10: demoted `Positive-ray Borel control in the stable
  quartic model` to a zero-dimensional model calculation rather than a
  theorem-level QFT statement.
- Volume II, Chapter 4: demoted `Outgoing pole gives decay in time and growth
  in space` to explanatory resonance-pole prose.

Strengthenings made:

- Volume I, Chapter 9: strengthened the subtracted Stieltjes/contact-term
  proposition by spelling out why equality of \((N+1)\)-st derivatives leaves
  a global polynomial ambiguity and why polynomial momentum terms are
  derivatives of the coincident-point delta distribution.
- Volume VII, Chapter 10: strengthened the ABJM kernel lemma by making the
  positive trace-class computation use \(T^*T\) and the Hilbert--Schmidt norm,
  avoiding a formal delta-function trace.

Candidates read and retained for later review rather than demotion:

- `Trace-class normalization of the ABJM kernel`: retained as a genuine
  trace-class lemma after the proof was tightened.
- `Local \(KG^2\) shell bound in dynamic \(\Phi^4_3\)`: retained as a real
  dyadic \(L^1\) estimate, not a wrapper.
- `Localized-parameter form of Noether's theorem`: retained as a structural
  local-parameter identity central to current insertions and Ward identities.
- `Subtracted Stieltjes form and contact terms`: retained and strengthened.
- `Narrow pole on the adjacent sheet`: retained as a contraction-mapping
  statement proving existence and uniqueness of the nearby second-sheet pole.

Guard update: `tools/audit_theorem_form.py` now rejects recurrence of the
newly demoted theorem titles.

Verification:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh`

The broad overinclusive heuristic count moved from 207 to 200 candidates.
The rebuilt PDF has 2581 pages.
