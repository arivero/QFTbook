# 2026-05-30 Modular-Theory Quoted-Theorem Expansion

## Scope

This pass responds to the stricter quoted-theorem standard: a
`quotedtheorem` is a proof-debt marker until the text exposes the proof
mechanism in the monograph's notation.  The edited target is Volume IV,
Chapter 4, where Tomita--Takesaki modular automorphisms and Connes' cocycle
derivative are foundational operator-algebraic inputs for local QFT.

## Manuscript Change

- Expanded the Tomita--Takesaki quoted theorem with the two antilinear core
  operators `S_0(A Omega)=A^* Omega` and `F_0(B Omega)=B^* Omega`.
- Displayed the adjoint relation on `R Omega` and `R' Omega`, including the
  use of `AB=BA`, and explained closability and polar decomposition.
- Added the left Hilbert algebra mechanism: multiplication on `R Omega`,
  closure of the involution, stability under `Delta^{it}`, bounded left
  multipliers, and the route to `Delta^{it} R Delta^{-it}=R` and
  `J R J=R'`.
- Expanded Connes' cocycle theorem with the standard-form datum, natural cone
  representatives, relative Tomita operator, relative modular operator, the
  algebra-membership assertion for
  `Delta_{psi|omega}^{it} Delta_omega^{-it}`, and the cocycle calculation.
- Tightened `planning/12_strict_writing_harness.md` so every quoted theorem
  requires local proof-mechanism exposition rather than a bare statement plus
  citation.

## Issue Alignment

- #695: addresses the Tomita--Takesaki and Connes-cocycle part of the
  foundational/AQFT quoted-theorem proof-debt cluster.
- #691: reinforces the distinction between genuine theorem machinery and
  formula-level checks.

## Remaining Proof Debt

This pass does not close #695.  The quoted theorem inventory across the whole
monograph still contains many targets, including OS boundary-value
infrastructure if we decide to internalize the pure-analysis proof, anomaly
conclusions, constructive/stochastic QFT theorem packages, CFT modular and
sewing theorems, SUSY dynamics status statements, integrability theorem
boundaries, and TQFT/RG mechanism claims.
