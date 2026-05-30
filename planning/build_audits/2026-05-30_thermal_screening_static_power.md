# Thermal Screening Static-Power Pass

## Scope

- Continued the later-volume depth and accuracy audit in Volume X,
  Chapter 7, `Thermal Gauge Theory And Screening`.
- Targeted the definition of static screening masses and their distinction
  from perturbative Debye matching coefficients.

## Finding

The chapter's unprojected static correlator displayed the large-distance
Yukawa power as \(r^{-(d-2)/2}\).  For an isolated scalar pole in \(d\)
spatial dimensions, the Fourier transform is controlled by
\[
  \frac{M^{d/2-1}}{(2\pi)^{d/2}r^{d/2-1}}K_{d/2-1}(Mr),
\]
so the asymptotic power is \(r^{-(d-1)/2}\).  The pure exponential belongs to
the transverse-projected transfer-matrix correlator.

## Change

- Corrected the screening asymptotic power in the chapter.
- Added the Bessel-function derivation from the static momentum-space pole.
- Added the transverse-projected correlator formula
  \(C_{\rm proj}(z)=Ze^{-M|z|}/(2M)+\cdots\).
- Added the spatial-transfer-matrix interpretation of screening masses in
  gauge-invariant channels.
- Clarified that the perturbative Debye pole is a gauge/regulator/scheme
  matching coefficient of the static effective theory, while physical
  screening masses are extracted from gauge-invariant static correlators.
- Added `calculation-checks/thermal_screening_checks.py`.

## Verification

- `python3 calculation-checks/thermal_screening_checks.py`

## Status

This fixes one concrete formula error and deepens the chapter's
nonperturbative definition of thermal screening.  It does not close any
broader QCD/thermal gauge-theory development issue.
