# Issue #725/#630 shear retarded-kernel evidence repair

## Target

Repair the evidence-independence weakness in the finite QCD shear spectral
window.  The previous companion check correctly propagated width/residue
errors, but it chose the width from \(\eta k^2/w\) and therefore did not
independently construct the retarded response whose spectral peak is being
fit.

## Manuscript Change

- Volume X, Chapter 12 now displays the contact-subtracted transverse momentum
  retarded pole kernel
  \[
    G^R_{\pi_x\pi_x}(\omega,k)
    =-\frac{w\gamma_k}{\gamma_k-i\omega}.
  \]
- The text derives the positive-frequency spectral peak from the chapter's
  \(\rho=-2\operatorname{Im}G^R\) convention and identifies the pole location,
  enthalpy residue, and viscosity reconstruction \(w\gamma_k/k^2\).
- The finite-window caveats remain: a QCD extraction still needs contact
  subtraction, frame choice, regular-background control, near-critical and
  long-time-tail budgets, and continuum/finite-volume errors.

## Companion Evidence

- Replaced `check_finite_shear_spectral_window_bookkeeping()` with
  `check_finite_shear_spectral_window_from_retarded_kernel()`.
- The check constructs \(G^R\), computes \(\rho=-2\operatorname{Im}G^R\),
  samples \(\rho(\omega)/\omega\) at two rational positive frequencies, solves
  for the pole width and peak amplitude, and reconstructs \(\eta\).
- Negative controls reject the wrong retarded sign, the width-only shortcut
  that misses the enthalpy residue, and an uncorrected two-sample extraction in
  the presence of a separately generated regular background.
- `qcd_phase_checks.py` now carries an explicit evidence contract and is
  registered in `calculation-checks/evidence_contracts.json` under QCD
  thermodynamics and hydrodynamic response.

## Re-audit

This is a physics-facing evidence repair.  It does not claim to derive a shear
pole from continuum QCD.  It strengthens the finite companion so that the
extraction algebra starts from a retarded response function and generated
spectral data, rather than from the final transport formula.

## Verification

- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase_checks`
- Focused Chapter 12 theorem-form, unnumbered-display-label,
  negative-scope, and style-density audits.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- `tools/build_monograph.sh` clean, producing
  `monograph/tex/main.pdf` at 3411 pages.

The stricter `audit_calculation_evidence_contracts.py --fail-on-risk-report`
mode was not used as a pass criterion: it still correctly reports other
unmanifested risky companions elsewhere in the repository.  The QCD phase
companion is no longer among those non-blocking risk-report entries.
