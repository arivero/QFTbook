# 2026-05-28 Issue #633: Six-Dimensional SCFT Depth Pass

## Scope

Reading-based correction to the reopened #633 backlog for Volume VII,
Chapter 11, `Six-Dimensional Superconformal Theories`.

The chapter already separated fixed-point data from tensor-branch effective
variables and treated the interacting `(2,0)` anomaly polynomial as protected
input rather than as a theorem constructed from first principles.  The
remaining gap was that the self-dual tensor sector, Green-Schwarz anomaly
matching, BPS string tension logic, and compactification matching were too
compressed.

## Manuscript Changes

- Added Definition `def:six-d-abelian-self-dual-tensor-datum`, distinguishing
  local two-form variables from the global differential-cohomology and charge
  lattice data needed for a self-dual tensor sector.
- Added the chiral two-form degree-of-freedom calculation, recording that a
  chiral two-form in six dimensions has three physical polarizations and that
  a free `(2,0)` tensor multiplet has eight bosonic on-shell polarizations.
  This was later demoted from proposition form in the anti-wrapper audit.
- Added Definition `def:six-d-tensor-branch-effective-datum`, listing the
  data of a tensor-branch EFT and making the chamber/tensionless-wall boundary
  explicit.
- Added Proposition `prop:six-d-green-schwarz-descent`, deriving the descent
  of the quadratic Green-Schwarz polynomial
  `(1/2) Omega^{IJ} X_I^{(4)} X_J^{(4)}` and explaining the factor of `1/2`.
- Added Proposition `prop:six-d-ade-anomaly-arithmetic`, displaying the ADE
  arithmetic behind the `(2,0)` anomaly coefficient and the cubic
  `A_{N-1}` scaling.
- Added Proposition `prop:six-d-bps-string-tension-central-charge`, deriving
  the BPS string tension from the tensor-branch central charge with an
  explicit status remark about the tensionless limit.
- Added the wrapped-string/Coulomb-branch mass-matching calculation, deriving the
  wrapped-string/W-boson matching and the scalar normalization
  `phi_5d = 2 pi R phi_6d`.

## Calculation Check

- Extended `calculation-checks/susy_abjm_6d_checks.py`.
- New checks cover chiral two-form degrees of freedom, ADE anomaly
  coefficients and tensor-branch dimensions, the quadratic Green-Schwarz
  descent factor, and wrapped-string/W-boson normalization.

## Verification

Passed before checkpoint:

- `python3 calculation-checks/susy_abjm_6d_checks.py`
- `python3 -m py_compile calculation-checks/susy_abjm_6d_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build and final log scan are clean.  The generated
`monograph/tex/main.pdf` has 2329 pages.
