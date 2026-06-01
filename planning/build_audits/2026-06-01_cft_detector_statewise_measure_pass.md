# CFT Detector Statewise-Measure Pass

Date: 2026-06-01.

Issue context: GitHub #519.

Scope:
- Strengthened
  `monograph/tex/volumes/volume_iii/chapter10_light_ray_operators_and_energy_correlators.tex`
  at the functional-analytic boundary between the CFT energy-detector
  hypothesis and detector products.
- Added `Finite Angular Partitions and Positivity` before the
  diagonal-contact subsection.
- Derived the statewise Riesz bound
  \[
    |\langle\Psi,\mathcal E(f)\Psi\rangle|
    \leq
    \|f\|_\infty\,\langle\Psi,P^0\Psi\rangle
  \]
  from positivity and \(\mathcal E(1)=P^0\).
- Identified the resulting finite positive regular Borel measure
  \(\mu_\Psi\) on the detector sphere for each finite-energy collider state.
- Added finite-bin calorimeter coordinates and the one-detector
  Cauchy--Schwarz positivity inequality.
- Explicitly separated this statewise one-detector measure statement from the
  stronger operator-valued-measure/domain problem and from detector-product
  contact extensions.

Calculation check:
- Extended `calculation-checks/cft_energy_detector_contact_checks.py` with
  exact rational checks of the finite-bin Riesz bound and
  Cauchy--Schwarz determinant before the existing contact-product checks.

Verification commands for this pass:
- `python3 calculation-checks/cft_energy_detector_contact_checks.py`
- `python3 -m py_compile calculation-checks/cft_energy_detector_contact_checks.py`
- `tools/run_calculation_checks.sh --python-only --only cft_energy_detector`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

Status:
- This closes a concrete finite-resolution positivity gap in the CFT
  energy-detector construction.
- It does not close #519.  The all-order renormalized light-ray OPE/mixing
  theorem, complete endpoint matching, and high-loop/frontier
  energy-correlator development remain open.
