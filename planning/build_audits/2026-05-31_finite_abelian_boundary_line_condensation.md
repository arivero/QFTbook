# Finite Abelian Boundary Line-Condensation Pass

Date: 2026-05-31

## Trigger

GitHub issue #703 tracks finite-locality and finite-gauge/TQFT laboratories
absorbed from the statmech project.  After the toric-code, locality-flow, and
finite-Hall passes, the remaining finite-gauge/TQFT boundary example needed
an exact algebraic model rather than a generic statement about boundaries.

## Edits

- Added a finite Abelian boundary and line-condensation section to Volume
  VIII, Chapter 11.
- Defined the untwisted three-dimensional finite Abelian line-label group
  \(\mathcal C_A=A\oplus\widehat A\), its braiding pairing, and its
  topological spin.
- Defined bosonic Lagrangian line-condensation boundary data, including both
  maximal braiding isotropy and trivial spin on condensed lines.
- Proved the finite cylinder-sector theorem
  \[
    \mathcal H_{\rm cyl}(L_0,L_1)=
    \mathbb C[\mathcal C_A/(L_0+L_1)],
    \qquad
    \dim\mathcal H_{\rm cyl}(L_0,L_1)=|L_0\cap L_1|.
  \]
- Worked out the \(A=\mathbb Z_N\) electric/magnetic boundary examples,
  giving \(N\) sectors for equal rough/smooth boundary pairs and one sector
  for the mixed pair.
- Added `calculation-checks/finite_gauge_boundary_checks.py` to verify the
  exact finite algebra.
- Updated the calculation-check manifest, Volume VIII Chapter 11 dossier, and
  statmech crosswalk.

## Verification Plan

- Run the new finite-gauge boundary calculation check.
- Run theorem-form, display-label, text, negative-scope, and chapter-dossier
  audits.
- Build the monograph and scan the log.
- Comment on #703 as another finite-gauge/TQFT boundary subpass while keeping
  the issue open for non-Abelian/twisted boundary examples and deeper
  thermodynamic Hall-response stability estimates.
