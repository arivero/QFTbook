# 2026-05-29 Sixth Cross-Volume Wrapper Pass

Scope: continuation of issue #691 anti-wrapper audit.  This pass read the
next short-proof queue entries across QED, conformal representation theory,
VOA formal calculus, global anomalies, supersymmetric moduli spaces,
Seiberg--Witten theory, and categorical symmetry.

Demotions made:

- Volume I, QED: demoted `Ward organization of the renormalized current` from
  proposition/proof form to convention and current-normalization prose.  The
  substance is the Abelian Ward identity \(Z_1=Z_\psi\) together with the
  explicit-coupling coordinate convention.
- Volume XII, eta invariants/global anomalies: demoted `Finite gauge
  transformation as determinant-line transport` from proposition/proof form to
  application prose.  The theorem-level input remains the quoted
  Bismut--Freed holonomy theorem.
- Volume VII, Seiberg--Witten theory: demoted `Mutually nonlocal light charges
  obstruct an electric frame` from proposition/proof form to conceptual
  symplectic-linear-algebra prose.

Strengthenings made:

- Volume IX, categorical symmetry: strengthened the reflection-positivity
  proof of the dagger structure by spelling out half-ball states, radial
  order reversal, null-junction quotienting, and unitarity of isotopy maps.
- Volume III, primary operators: expanded the spinful local conformal-current
  Ward identity proof from a compressed differentiation argument to the
  source-coupling derivation, including measure/source-weight cancellation and
  small-sphere charge orientation.
- Volume III, conformal group: strengthened the null quotient and unitarity
  test proof by spelling out the contravariant anti-involution, radical
  submodule argument, cyclic-sector qualification, and finite-level Gram
  matrix test.
- Volume V, VOA: strengthened the proof that locality gives the OPE by
  spelling out lower truncation, residue extraction, regularity after
  multiplication by \((z-w)^N\), and matrix-element equality in the
  \(|z|>|w|\) expansion.

Guard update: `tools/audit_theorem_form.py` now rejects recurrence of the
three newly demoted theorem titles.

Verification:

- `python3 tools/audit_theorem_form.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- stale-label scan for the three demoted labels
- `python3 tools/audit_unnumbered_display_labels.py`
- `git diff --check`
- `tools/build_monograph.sh`

The full build completed cleanly with `monograph/tex/main.pdf` at 2581 pages.
The short-proof heuristic queue moved from 38 to 31 candidates.  This is a
reading queue, not a defect count.
