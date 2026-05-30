# 2026-05-30 TQFT Hypothesis/Fubini Pass

Scope:
- Continued the #691 theorem-family substance audit and the #698 TQFT proof-debt pass.
- Focused on finite gauge theory/state-sum gluing and topological sigma-model virtual integration.

Edits:
- Expanded finite groupoid gluing in Volume VIII, Chapter 11 by inserting a finite-groupoid Fubini lemma with the explicit automorphism-weight calculation.  The proof now shows how the image and kernel of
  `Aut_E(e) -> Aut_B(p(e))` combine to produce the groupoid cardinality measure and pushforward composition.
- Added an exact calculation-check companion for one-object finite groupoids `BK -> BH -> BL`, including non-injective cyclic homomorphisms where the image/kernel split is visible.
- Expanded Volume VIII, Chapter 6 to specify the virtual integration package required by the A-model formulas, including the genus-zero diagonal refined-pullback identity on boundary strata.  The small quantum product associativity statement is now explicitly conditional on this package, rather than presenting the virtual geometry as a formal path-integral consequence.
- Removed residual `worldsheet`/`closed-string` wording from the topological sigma-model chapter in favor of source-surface and closed-sector language.

Checks run:
- `python3 calculation-checks/finite_gauge_state_sum_checks.py`
- `python3 -m py_compile calculation-checks/finite_gauge_state_sum_checks.py`
- `python3 calculation-checks/topological_sigma_model_checks.py`
- `python3 -m py_compile calculation-checks/topological_sigma_model_checks.py`

Status:
- #691 remains open for continued proof-substance audit.
- #698 remains open; this pass closes one finite TQFT gluing proof gap and clarifies one virtual-geometry hypothesis boundary, but non-pointed categorical TQFT, localization compactness, and Donaldson--Seiberg--Witten RG comparison still require deeper development.
