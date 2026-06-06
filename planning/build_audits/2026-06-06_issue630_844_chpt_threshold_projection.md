# 2026-06-06 issue #630/#844 ChPT threshold projection audit

## Target

- Volume II, Chapter 21:
  `ca:chpt-pion-threshold-observable-projection`.
- Calculation evidence:
  `check_threshold_pion_scattering_projection()` in
  `calculation-checks/chpt_nlo_checks.py`.

## Scope Judgment

This pass develops the physical-observable side of the ChPT section.  It does
not add another formal status map.  The new block asks how the local chiral
amplitude becomes a measured low-energy pion-scattering quantity.

The pass is deliberately narrow: it projects the leading massive-spurion
amplitude to the \(S\)-wave threshold coordinates \(a_0^0,a_0^2\), displays the
local \(O(p^4)\) \(C_4,C'_4\) projection matrix, and separates one-loop,
mass-spurion, and first-omitted \(O(p^6)\) terms before any fit of local
constants is interpreted.

## Re-Audit Notes

- Physics depth: improved.  The text now follows the ChPT amplitude through
  external-state, isospin, and partial-wave projection to threshold
  observables.
- Architecture: improved.  The local \(p^4\) constants are no longer allowed to
  look like direct predictions when loop and residual terms have not been
  subtracted.
- Scope boundary: retained.  The pass does not compute the full massive
  one-loop \(\pi\pi\) amplitude, determine the physical low-energy constants
  from QCD, or replace Roy/lattice/experimental threshold input.
- Directive hygiene: satisfied.  This planning file carries the issue/audit
  language; the TeX remains reader-facing monograph content.

## Evidence Contract

The companion finite check verifies:

- the leading massive-spurion amplitude gives the Weinberg threshold values;
- the chiral-limit amplitude used at physical threshold gives the wrong
  \(I=2\) result and is rejected;
- the local \(C_4,C'_4\) projection matrix for \(a_0^0,a_0^2\) is obtained by
  direct isospin and partial-wave projection;
- the local matrix is invertible only after loop and residual terms have been
  separated;
- silently absorbing loop or \(O(p^6)\) residual terms shifts the fitted local
  constants by a bounded but nonzero amount.
