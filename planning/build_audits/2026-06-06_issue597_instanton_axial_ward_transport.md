# Issue #597 Instanton Axial Ward Transport Audit

## Scope

- Volume II Ch20D, immediately after the chirality-source selection rule.
- Target: connect the hard instanton zero-mode source determinant to the
  anomalous axial Ward convention in parent Ch20 before the hard benchmark is
  read as a physical amplitude.
- This is source/Ward/amplitude structure, not an ADHM or moduli-space
  expansion.

## Changes

- Added `prop:instanton-axial-ward-source-transport`.
- The new proposition proves the finite \(N_f=2\) identity
  `(4 partial_theta + V_A^src)(e^{i theta} det C_zm)=0`, with
  `V_A C_zm = -2 i C_zm`.
- Updated `instanton_physical_amplitude_architecture_checks.py` with an exact
  rational complex determinant variation check and negative controls for
  source-only, theta-only, and wrong-sign theta rotations.
- Updated the calculation-check README and Ch20D dossier.

## Re-Audit

- The added TeX is physics derivation and source-coordinate logic only.  No
  directive, review, monitoring, or issue-process language was added to the
  monograph.
- The pass strengthens the chapter's amplitude flow: a hard instanton source
  coefficient is not merely a chirality selection; it sits on an anomalous
  Ward orbit with the theta phase before pole, OPE, susceptibility, or
  inclusive projection.
