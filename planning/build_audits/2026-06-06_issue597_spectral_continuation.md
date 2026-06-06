# Issue #597 spectral-continuation instanton pass

## Target

- Issue: #597, instanton physics-depth lane.
- Manuscript target: Volume II, Chapter 20, BPST instanton and semiclassical
  vertex.
- Calculation companion: `calculation-checks/bpst_instanton_normalization_checks.py`.

## Change

- Added `ca:instanton-spectral-continuation-source-correlator` immediately after
  the Euclidean-to-physical instanton residual budget.
- The new block writes the dispersion coordinate
  `G_I^E(Q_E^2)=P_N(Q_E^2)+int rho_I(s)/(s+Q_E^2) ds+R_disp`.
- It separates local contact polynomials from physical discontinuities and
  defines the spectral-bin functional
  `W_{I,Delta}=int w_Delta(s) rho_I(s) ds`.
- The residual bound now includes dispersion, inverse-problem, contact/subtraction
  transport, unitarity-cut, and infrared projection errors.

## Re-audit

- This is physics-observable architecture, not another instanton moduli-space
  cell.
- It addresses the concern that a Euclidean instanton source coefficient, even
  after the BPST measure and fluctuation determinant are assembled, is not yet a
  rate or spectral observable.
- The monograph TeX contains no issue/process bookkeeping; this planning file
  carries the audit trail.

## Companion evidence

- Added `check_instanton_spectral_continuation_gate()`.
- Positive checks:
  - finite Stieltjes source value versus spectral-bin functional;
  - contact polynomial changes Euclidean source values but no separated bin;
  - second Euclidean point detects a one-point spectral ambiguity;
  - residual majorant for the spectral projection.
- Negative controls:
  - treating a Euclidean Stieltjes value as the spectral bin;
  - using one spacelike value to identify a physical bin;
  - omitting the inverse-problem residual from the projection budget.

## Verification plan

- Focused BPST companion syntax and run.
- Focused Ch20 theorem-form, unnumbered-label, negative-scope, and style-density
  audits.
- Calculation inventory/evidence and dossier/text audits.
- Full monograph build.
