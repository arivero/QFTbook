# 2026-05-26 Issue #599: Kontsevich-Segal Functorial QFT

## Scope

Issue #599 required the monograph to replace brief orienting references to
the Kontsevich-Segal framework by a systematic foundational treatment:
Segal sewing, admissible complex metrics, K-S functorial data, comparison
with OS/Wightman/AQFT, OPE from sewing, and an honest construction-status
ledger.

## Manuscript Changes

- Added `volume_iv/chapter06_kontsevich_segal_functorial_qft.tex` and
  included it in Volume I after OS reconstruction, where it belongs in the
  foundations sequence.
- Proved the K-S allowability angle criterion from the \(q\)-form positivity
  definition, including the Lorentzian boundary and multi-time exclusion
  examples.
- Defined the K-S functorial datum, reflection positivity, Hilbert completion,
  and the route from K-S data to OS Schwinger functions under explicit
  distributional and spectral hypotheses.
- Added a quoted theorem for the Lorentzian-boundary construction and a
  sewing derivation of the OPE under annular spectral/nuclear assumptions.
- Added a construction-status ledger for free fields, constructive scalar
  models, Liouville, two-dimensional Yang-Mills, three-dimensional
  constructive models, four-dimensional Yang-Mills, fermions/gauge fields,
  and extended K-S structures.
- Updated forward/backward references in Volume I chapter 1, Volume III
  radial quantization, and Volume VIII Atiyah-Segal TQFT.

## Calculation Check

Added `calculation-checks/ks_allowability_checks.py`, which verifies:

- Euclidean metrics are allowable;
- Lorentzian metrics are boundary points, not interior allowable metrics;
- both \(i\epsilon\) sides of a Lorentzian metric are allowable;
- two-time real signatures remain outside the allowable domain;
- for representative diagonal metrics, the angle criterion agrees with
  positivity of all \(q\)-form diagonal coefficients.
