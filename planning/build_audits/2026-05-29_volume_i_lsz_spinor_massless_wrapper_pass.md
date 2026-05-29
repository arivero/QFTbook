# 2026-05-29 Volume I LSZ/Spinor/Massless Anti-Wrapper Pass

## Scope

Read the remaining Volume I theorem-family statements flagged by the
short-proof heuristic after the Chapter 11 pass, excluding the Chapter 10 Wick
combinatorics statements that had already been retained as genuine
finite-regulator graph-counting facts.

## Decisions

- Demoted `Invariant denominator coefficient and linear pole residues` from a
  proposition to a worked paragraph.  The distinction between the
  invariant-denominator coefficient and fixed-\(\vec k\) residues is important
  for LSZ normalization, but the proof is a partial-fraction calculation.
- Demoted `Spinor mass-shell residue and external factors` from a proposition
  to a worked paragraph.  The calculation remains in the text because it fixes
  spinor external-leg normalization, but its proof is a residue and spin-sum
  substitution.
- Demoted `Little algebra of a future null momentum` from a proposition to a
  worked paragraph.  The future-null stabilizer and \(ISO(2)\) commutators are
  essential representation-theoretic data, but the displayed proof is a direct
  Lorentz-algebra computation.

## Recurrence Guard

`tools/audit_theorem_form.py` now rejects these three titles if they reappear
in theorem-family environments.

## Verification

Run the theorem-form audit, text audits, label audit, diff check, and full
monograph build after the edit.
