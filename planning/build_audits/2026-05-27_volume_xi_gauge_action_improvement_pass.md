# 2026-05-27 Volume XI Gauge-Action Improvement Pass

## Scope

This pass continues issue #631 by adding a finite-regulator treatment of
plaquette-plus-rectangle improved gauge actions to Volume XI, Chapter 5.

## Substantive Additions

- Added a tree-level improved gauge-action section after the continuum
  plaquette expansion.
- Defined the plaquette-plus-rectangle family as a local gauge-invariant
  regulator action, with the Wilson action as a special case.
- Derived the continuum normalization equation \(c_0+8c_1=1\) from the
  leading squared area of the two \(1\times2\) rectangles in each coordinate
  plane.
- Derived the tree-level derivative-artifact cancellation equation
  \(c_0+20c_1=0\) from the centered rectangle flux expansion.
- Solved the two equations to obtain the tree-level Symanzik coefficients
  \(c_1=-1/12\) and \(c_0=5/3\).
- Added a caution separating tree-level improvement, loop-level interacting
  improvement, Iwasaki-style RG-improved coefficients, and
  reflection-positivity/transfer-matrix reconstruction.
- Added `calculation-checks/gauge_action_improvement_checks.py` to verify the
  finite arithmetic in the derivation.

## Verification

- Passed: `python3 calculation-checks/gauge_action_improvement_checks.py`
- Passed: `python3 -m py_compile calculation-checks/gauge_action_improvement_checks.py`
- Passed: primitive-fraction scan on touched files.
- Passed: `git diff --check` on touched files.
- Passed: `tools/build_monograph.sh`
- Built PDF: `/Users/xiyin/QFT/monograph/tex/main.pdf`, 2232 pages.

## Remaining Work

- Chapter 5 still needs a fuller nonabelian interacting Symanzik operator
  basis, smearing as a finite-regulator map on links, lattice perturbation
  and tadpole-improvement conventions, and stronger links to the numerical
  toolkit requested in #631.
