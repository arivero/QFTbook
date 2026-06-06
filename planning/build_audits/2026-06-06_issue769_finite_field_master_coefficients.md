# 2026-06-06 Issue #769 Finite-Field Master Coefficients

## Target

- Open issue: #769, loop-level generalized unitarity and integral reduction.
- Chapter touched: Volume II, Chapter 6, generalized-unitarity/master-integral
  reconstruction layer.
- Companion touched: `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Change

- Added `ca:finite-field-master-coefficient-reconstruction` after the
  dual-contour coefficient-extraction block and before physical
  master-discontinuity closure.
- The new block treats finite-field sampling as an exact rational
  master-coefficient reconstruction method:
  - declare the reduced master basis and common denominator \(D_{\rm ff}(x)\);
  - exclude bad primes and bad sample points where denominators, IBP pivots,
    or contour-pairing determinants vanish;
  - interpolate the cleared numerator over \(\mathbb F_p\);
  - lift to \(\mathbb Q(x)\) only after coefficient bounds and validation;
  - keep master branch, subtraction, lower-sector constants, and observable
    assembly as separate physical data.
- Extended the companion with `check_finite_field_master_coefficient_reconstruction()`.
  The check reconstructs two rational coefficient functions from modular
  samples after denominator clearing, validates at a withheld point, lifts the
  small integer numerators, evaluates the exact rational coefficients at a
  physical point, and rejects:
  - denominator-omitted polynomial interpolation;
  - a bad prime zeroing the normalization denominator;
  - singular interpolation samples;
  - using exact coefficients with Euclidean master values as a physical-branch
    shortcut.
- Updated the calculation inventory and the Chapter 6 dossier.

## Re-Audit

This pass is meant to answer a real remaining #769 gap: finite-field/symbolic
coefficient reconstruction for modern loop amplitudes.  The monograph text
does not present finite-field algebra as a separate mathematical ornament.
It is tied to master coefficients in a declared loop-amplitude reduction and
then explicitly stops before physical branch transport and observable
assembly.  No issue or directive metadata was inserted into TeX.

## Verification Plan

- Focused companion syntax and run.
- Targeted `generalized_unitarity_reduction` harness.
- Focused Chapter 6 theorem/display/prose/style audits.
- Dossier, text, calculation inventory, and evidence-contract audits.
- Full Python calculation suite.
- Full monograph build.
