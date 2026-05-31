# Finite Subgroup Boundary and Relative DW Pass

Date: 2026-05-31

## Trigger

Issue #703 keeps the finite-locality and finite-gauge/TQFT laboratories open
after the Abelian line-condensation pass.  The next missing finite boundary
laboratory was the nonabelian subgroup boundary, together with the twisted
Dijkgraaf--Witten boundary anomaly-cancellation condition.

## Edits

- Added a subgroup-boundary section to Volume VIII, Chapter 11.
- Defined a subgroup boundary \(B_H\) as an \(H\)-reduction of the boundary
  \(G\)-bundle, both in bundle language and in triangulated finite-label
  language.
- Proved that the interval field groupoid between \(H_0\) and \(H_1\)
  boundaries is \(G//(H_0\times H_1)\), with simple sectors
  \(H_0\backslash G/H_1\), stabilizer
  \(H_0\cap gH_1g^{-1}\), and groupoid cardinality
  \(|G|/(|H_0||H_1|)\).
- Defined a relative Dijkgraaf--Witten boundary datum
  \((H,\beta)\) by \(\delta\beta=i^*\omega\).
- Wrote the explicit bulk-boundary state-sum weight with inverse boundary
  \(\beta\)-factor and proved the local boundary Pachner cancellation.
- Added `calculation-checks/finite_gauge_subgroup_boundary_checks.py` to
  verify double-coset sectors, stabilizer weights, groupoid cardinality, and
  relative cochain cancellation in exact finite examples.
- Updated the calculation-check manifest, chapter dossier, and statmech
  crosswalk.

## Verification Plan

- Run the new subgroup-boundary calculation check.
- Run theorem-form, display-label, strict text, negative-scope, and
  chapter-dossier audits.
- Build the monograph and scan the log.
- Comment on #703 with the completed finite subgroup-boundary subpass while
  keeping the issue open for deeper Hall stability, junction composition, and
  remaining statmech crosswalk tracks.
