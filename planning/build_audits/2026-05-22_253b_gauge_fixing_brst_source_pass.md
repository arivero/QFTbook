# 253b Gauge Fixing, Ghosts, and BRST Source Pass

Date: 2026-05-22

## Source Scope

- Primary handwritten source:
  `references/253b lecture notes 2023.pdf`, pp. 169--181.
- Rendered source images:
  `/tmp/253b_169_181-169.png`--`/tmp/253b_169_181-181.png`.
- Operational transcription:
  `transcription/tex/253b/scattering_rg_qcd.tex`, gauge-fixing and BRST block.
- Comparison transcription:
  `references/253b transcribed lecture notes.tex`, same block.

## Manuscript Scope

- `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`.
- Rendered manuscript check:
  `/tmp/qft_brst_cert3-355.png`--`/tmp/qft_brst_cert3-363.png`
  covering printed pages 338--346.

## Certified Content

- Distinguished the finite-dimensional gauge group \(G\) from the
  infinite-dimensional gauge-transformation group
  \(\mathcal G=C^\infty(M,G)\).
- Added condensed coordinate notation \(\xi^\alpha\), with
  \(\alpha=(a,x)\), and the summation/integration convention.
- Restored the source-level Faddeev--Popov derivation:
  local gauge slice \(F^A[\phi]=0\), orbit coordinates, local determinant,
  right-Haar measure, and division by
  \(\int_{\mathcal G}[D\xi]_{\rm H}\).
- Added the ghost determinant and \(B_A\)-field representation before
  specializing to Lorenz gauge.
- Made the \(b_A=-\bar c_A\) convention explicit so the condensed source
  formulas and the conventional antighost formulas have consistent signs.
- Added the condensed BRST transformations
  \(s\phi=c^\alpha S_\alpha\phi\), \(sb_A=-B_A\),
  \(sc^\alpha=-\frac12 f^\alpha{}_{\beta\gamma}c^\beta c^\gamma\), and the
  \(Q_B\) convention \(\delta_BX=i\epsilon Q_B\cdot X\).
- Expanded the nilpotence proof to include general fields in condensed
  notation, the ghost, the gauge field, and matter fields.
- Restored the source proof that deformation of \(F^A\) changes the action by a
  BRST-exact insertion and hence leaves transition amplitudes between
  BRST-closed boundary states invariant, under the stated measure and boundary
  assumptions.
- Restored the exact-state equivalence
  \(|\Psi\rangle\sim|\Psi\rangle+Q|\chi\rangle\) and the BRST cohomology
  quotient for the physical state space.
- Added and rendered the gauge-orbit/gauge-slice figure corresponding to the
  handwritten p. 171 figure.

## Verification

- `tools/build_monograph.sh` clean.
- `tools/audit_monograph_text.sh` clean.
- `git diff --check` clean.
- Figure render checked at `/tmp/qft_brst_cert3-356.png`: the figure appears in
  logical order, has no overlap, and shows the orbit/slice/representatives
  needed by the source.

## Remaining Boundary

- This pass certifies the local perturbative Faddeev--Popov/BRST construction.
  Global Gribov issues and the full BV formalism remain later developments,
  not omissions from pp. 169--181.
