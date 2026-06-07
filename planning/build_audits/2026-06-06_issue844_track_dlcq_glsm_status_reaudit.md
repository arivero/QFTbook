# Issue #844 track/DLCQ/GLSM status re-audit

## Scope

- Volume II Ch19b track-function measured-test surface.
- Volume II Ch20c DLCQ current-correlator residue surface.
- Volume VII Ch09 one-vortex source-frame calibration surface.

## Re-audit

- Demoted `ca:track-function-measured-test-budget` to
  `rem:track-function-measured-test-warning`.  The displayed
  \(B_{\rm tr}^{(m)}\) is a measured-test discrepancy and a
  non-identifiability warning for finite moment truncations, not a controlled
  approximation without a metric-determining test class and a quantitative
  moment estimate.
- Demoted `ca:qcd2-dlcq-current-correlator-residue-contract` to
  `rem:qcd2-dlcq-current-correlator-residue-map`.  The finite spectral
  representation is an exact resolvent identity; continuum current
  correlators still require source-vector, current-renormalization, endpoint,
  pole-window, spectral-weight, and \(K\to\infty\) estimates.
- Demoted `ca:glsm-one-vortex-source-frame-calibration` to
  `rem:glsm-one-vortex-source-frame-calibration-map`.  The retained
  \(J_{AB}/J_{CD}\) ratio is exact finite source-frame algebra; the amplitude
  inequality is conditional on separately supplied component and frame
  transport bounds in the same regulator convention.

## Verification Targets

- Focused companion checks for track observables, the 't Hooft/DLCQ model, and
  the 2D GLSM/Hori--Vafa lane.
- Focused theorem/display/negative-scope/style audits for the touched
  chapters.
- Dossier, monograph-text, calculation-inventory, evidence-contract, and diff
  hygiene audits.
- Full Python calculation suite and full monograph build before commit.
