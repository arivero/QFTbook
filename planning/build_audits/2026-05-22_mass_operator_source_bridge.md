# 2026-05-22 Mass-Operator Source Bridge Audit

## Scope

This pass strengthens the source-dependent operator bridge by adding a worked
finite-regulator example for the scalar mass operator \(O_m=\phi^2/2\).  The
purpose is to connect BPHZ normal products, Wilsonian insertion functionals,
and 1PI insertion kernels by explicit maps.

## Manuscript Changes

- Updated
  `monograph/tex/volumes/volume_ii/chapter12_renormalized_operators_and_minimal_subtraction.tex`.
- Added "A Worked Insertion: The Mass Operator in \(\phi^4\)."
- Defined the insertion bubble
  \(\mathcal I_{A,B}(Q)\) and its finite-regulator covariance split into
  low-low, high-high, and mixed assignments.
- Wrote the zeroth-order Wilsonian insertion for
  \(O_m=\phi^2/2\), including the identity contribution from shell
  contraction.
- Wrote the one-loop Wilsonian mass-insertion correction from the high-high
  bubble and its local source-coordinate counterterm.
- Wrote the BPHZ normal-product subtraction for the two-field 1PI insertion
  kernel at a nonexceptional source-momentum subtraction configuration
  \(\mathcal Q_\mu\).
- Added a figure showing the insertion-bubble split and the maps to the
  Wilsonian insertion, low-field 1PI insertion, and local source map.
- Wrote the low-field 1PI insertion kernel and the source-coordinate
  normalization condition that fixes \(K_m^{(2)}(\mathcal Q_\mu)=1\).

## Planning Updates

- Updated the renormalized-operators dossier with the new construction task,
  claim, figure requirement, and audit note.
- Updated the master architecture and dependency map so the next target is
  multi-insertion contact-term conventions and observable correlator
  tightening.

## Verification

- Ran `git diff --check`; no whitespace errors.
- Built the monograph with `tools/build_monograph.sh`; the strict monograph
  text audit and LaTeX log scan were clean.
- Rendered and inspected the new insertion-matching figure page at
  `/tmp/qft_mass_operator_source_bridge_final-282.png`; the covariance labels,
  arrows, boxes, caption, and adjacent equations were legible and nonoverlapping.
