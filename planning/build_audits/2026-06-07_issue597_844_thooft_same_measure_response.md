# Issue #597/#844: same-measure source response in the hard instanton amplitude

## Scope

- Monograph file: `monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex`.
- Companion: `calculation-checks/instanton_physical_amplitude_architecture_checks.py`.
- Planning records: Ch20D dossier and calculation-check inventory.

## Status correction

The front-door source-functional route is now
`constr:instanton-source-functional-route` rather than a
`controlledapproximation`.  Its role is an extraction/provenance map: the
one-instanton sector first defines a finite-regulator source functional, and a
physical amplitude is obtained only after source differentiation,
source-dependent fluctuation averaging, collective integration, and the named
physical projection.  It is not itself an approximation estimate.

## Physics-depth repair

The amputated 't Hooft four-point assembly now carries the normal-mode source
response inside the same retained hard measure as the zero-mode slots, Haar
tensor, amputation/crossing data, size window, and pre-projection coordinate:

`A_4^amp = exp(i theta) int (1 + q_2 + q_3 + r_nz/src) dmu_hard^0`.

The omitted normal-source response is controlled only in the absolute
hard-measure norm, up to the coordinate, amputation, projection, and
sector-isolation residuals.  A relative statement still needs a separate
noncancellation margin.

## Negative Controls Added

The companion now rejects:

- determinant-normalized zero-mode answers used as the hard amplitude;
- retaining only the Gaussian `q_2` response while dropping the first cubic
  covariance `q_3`;
- multiplying by an unweighted normal-source quotient after the signed
  hard-window projection;
- inserting a source quotient from a shifted source frame;
- assigning zero residual budget to the omitted normal-source remainder.

## Self-Audit

This pass deepens the instanton chapter in the requested physics direction.  It
does not add ADHM or moduli-space geometry.  The new text addresses the hard
part of the amplitude calculation: source-dependent fluctuations around the
instanton saddle must be integrated in the same regulator, source frame, and
physical measure as the density and zero-mode factors.

Remaining risk: the chapter is long, and Ch20D still deserves a fresh
end-to-end prose read after the current issue-driven insertions.  The present
edit is localized and covered by focused finite checks, but it does not claim a
complete continuum derivation of the original four-point amplitude.
