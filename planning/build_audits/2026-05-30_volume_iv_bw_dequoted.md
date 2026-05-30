# Volume IV Bisognano--Wichmann Dequote Audit

Date: 2026-05-30

## Issue Context

- GitHub issue: #695, foundational reconstruction/AQFT proof debt.
- Local target: Volume IV, Chapter 4, where the wedge Bisognano--Wichmann
  theorem was still carried as a `quotedtheorem` even though the chapter had a
  substantial analytic proof mechanism immediately afterward.

## Changes Made

- Replaced the wedge Bisognano--Wichmann `quotedtheorem` with an explicit
  theorem-boundary remark.
- Isolated the locally proved content as a theorem:
  Wightman polynomial-core wedge KMS strip analyticity.
- The theorem now states the fields, common Wightman domain, wedge polynomial
  algebra, boost automorphism, strip \(0<\operatorname{Im}z<2\pi\), boundary
  values, and graded-observable distinction.
- The proof spells out the spectral-condition tube mechanism in mostly-plus
  signature: for \(p,\eta\in\overline V_+\), \(p\cdot\eta\le0\), so
  \(\exp(p\cdot\eta)\) supplies damping after the complex shift
  \(\xi\mapsto\xi-\ii\eta\).
- The PCT corollary now relies on its displayed modular-covariance hypothesis
  instead of citing the old quoted theorem label.

## Remaining Boundary

The closed-operator identification
\[
  \overline{S_{W_R,0}}=J_{W_R}\Delta_{W_R}^{1/2}
\]
and the full wedge modular-conjugation theorem remain part of the external
Bisognano--Wichmann boundary.  They are named explicitly rather than hidden
behind a local theorem label.

## Verification Plan

- Confirm that the old `thm:bisognano-wichmann-wedges` label is absent.
- Run theorem-form, display-label, prose, dossier, and full-build audits.
