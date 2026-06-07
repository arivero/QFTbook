# 2026-06-07 Issue #597 Mass/Source RG Channel Transport Audit

## Scope

This pass deepens the instanton physical-amplitude chapter at the determinant,
source, and projection layer.  It deliberately does not expand the ADHM or BPST
moduli-space analysis.

## Substance

The new gate separates the RG covariance of the undifferentiated instanton
source functional from the RG covariance of source-differentiated channel
coefficients.  The finite light-fermion nonzero-mode determinant cancels the
full two-flavor zero-mode determinant flow before differentiation.  After
differentiation, an \(r\)-source coefficient carries \(r\gamma_m\) until it is
paired with the renormalized source/operator projection covector.

The companion finite check models vacuum, mass-assisted, and hard source
coordinates as exact rational weights.  It rejects using a formally invariant
density as a projected hard amplitude, and it rejects vacuum-reference
calibration when the source/operator projection factor is missing.

## Quality Boundary

This is a physics-depth bridge for issue #597 because it concerns determinant
normalization, anomalous dimensions, source differentiation, and physical
projection.  It remains below the full directive-0 bar: it does not compute the
continuum Pauli-Villars constant, the full 't Hooft four-point normalization,
or a Lorentzian scattering theorem.

## Verification Plan

- Run the instanton physical-amplitude companion directly and through the
  calculation-check harness.
- Run chapter-local theorem/display/style/prose audits on the instanton
  physical-amplitude chapter.
- Run the evidence-contract and dossier inventory audits.
- Run the full Python calculation-check suite and monograph build before
  committing.
