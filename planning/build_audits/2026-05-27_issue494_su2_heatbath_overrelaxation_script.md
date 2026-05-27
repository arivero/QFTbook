# 2026-05-27 Issue 494: SU(2) Heat-Bath/Overrelaxation Script

## Scope

This pass continues issue #494 by promoting the heat-bath and overrelaxation
layer from theorem-only manuscript content to a reader-facing finite-regulator
companion script.  The script is deliberately modest: it demonstrates exact
single-link conditional sampling and microcanonical overrelaxation for the
finite \(SU(2)\) Wilson lattice action, but it does not claim production
autocorrelation analysis or continuum extrapolation.

Touched files:

- `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py`
- `qft_scripts/README.md`
- `tools/run_qft_scripts_smoke.sh`
- `calculation-checks/heatbath_overrelaxation_checks.py`
- `calculation-checks/README.md`
- `monograph/tex/volumes/volume_xi/chapter06_monte_carlo_and_sign_problems.tex`
- `planning/chapter_dossiers/volume_xi/chapter06_monte_carlo_and_sign_problems.md`
- `planning/build_audits/2026-05-27_issue494_su2_heatbath_overrelaxation_script.md`

## Script Content

- Added `qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py`.
- Reused the existing unit-quaternion \(SU(2)\) and Wilson-loop operations
  from `qft_scripts/su2_gauge_4d_metropolis.py`.
- Implemented the local staple \(V_e\) such that the adjacent plaquette score
  is \(\operatorname{Re}_{\mathbb H}(U_eV_e)\).
- Implemented rejection sampling for the exact scalar quaternion density
  \(\sqrt{1-x_0^2}\exp(\beta c_ex_0)\,dx_0\) and uniform angular sampling on
  \(S^2\).
- Implemented the microcanonical overrelaxation map
  \(U_e\mapsto W_e^{-1}U_e^{-1}W_e^{-1}\).
- Added a smoke mode and included it in `tools/run_qft_scripts_smoke.sh`.

## Calculation Check Upgrade

Extended `calculation-checks/heatbath_overrelaxation_checks.py` so that it
now verifies the script's finite local identities:

- script staple score equals the direct adjacent plaquette score;
- script overrelaxation preserves the local score and unit-link constraint;
- script heat-bath update preserves the unit-link constraint.

## Verification

- `python3 qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py --smoke`:
  passed; emitted finite plaquette and \(1\times1\) Wilson-loop estimates in
  the expected \([-1,1]\) range.
- `python3 calculation-checks/heatbath_overrelaxation_checks.py`: passed;
  printed `All finite heat-bath and overrelaxation checks passed.`
- `python3 -m py_compile
  qft_scripts/su2_gauge_4d_heatbath_overrelaxation.py
  calculation-checks/heatbath_overrelaxation_checks.py`: passed.
- `tools/run_qft_scripts_smoke.sh`: passed, including the new
  \(SU(2)\) heat-bath/overrelaxation smoke run.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2090`.
