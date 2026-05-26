# Build Audit: Issue 600 Torsionful Beta Package

- Branch: `codex/2d-cft-liouville-bcft-nlsm`
- Scope: issue #600 / Volume V Chapter 11 NLSM torsionful one-loop
  consistency pass.
- Substantive edits:
  - Added a torsionful-connection package to
    `monograph/tex/volumes/volume_v/chapter11_two_dimensional_sigma_models_orbifolds_twist_fields.tex`.
  - Defined `nabla^+` and `nabla^-`, fixed the `Gamma^- = Gamma - H/2`
    convention, and derived the Ricci decomposition into the symmetric
    metric coefficient `-H_i{}^{kl}H_{jkl}/4` and the antisymmetric
    coefficient `-nabla^k H_{kij}/2`.
  - Repackaged the one-loop hatted `G` and `B` Weyl-anomaly coefficients as
    `Ric(nabla^-) + 2 nabla^- d Phi`, including the dilaton-gradient
    `nabla Phi . H` term.
  - Stated the local `d beta^H = 0` Bianchi preservation and its role as the
    one-loop seed of the Curci--Paffuti consistency condition.
  - Extended `calculation-checks/nlsm_weyl_anomaly_checks.py` with exact
    coefficient checks for the torsionful Ricci package and an exterior
    `d^2=0` cancellation check for the local `H` beta representative.
  - Updated the Chapter 11 dossier.
- Verification completed before handoff:
  - `python3 calculation-checks/nlsm_weyl_anomaly_checks.py`
  - `tools/run_calculation_checks.sh`
  - `tools/audit_monograph_text.sh`
  - `tools/audit_chapter_dossiers.sh`
  - `git diff --check`
  - `tools/build_monograph.sh`
