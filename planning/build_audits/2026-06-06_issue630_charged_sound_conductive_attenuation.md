# Issue #630 charged sound conductive attenuation correction

Date: 2026-06-06

## Scope

This pass addresses the review finding that the Volume X Chapter 12 QCD
transport window used the neutral-fluid sound attenuation formula at finite
baryon density.  The affected blocks are:

- `ca:qcd-hydrodynamic-response-window`;
- `ca:qcd-finite-bulk-sound-spectral-window`;
- `ca:qcd-transport-closure-window`;
- `check_finite_bulk_sound_spectral_window()` and
  `check_qcd_transport_closure_window()` in
  `calculation-checks/qcd_phase_checks.py`.

## Substance

- The chapter now derives the one-charge Landau-frame longitudinal matrix with
  thermodynamic derivatives
  `beta_1=(partial p/partial epsilon)_n`,
  `beta_2=(partial p/partial n)_epsilon`, and
  `alpha_i=T partial(mu_B/T)`.
- The finite-density sound attenuation is now
  `Gamma_s=gamma_visc+Gamma_cond`, with
  `Gamma_cond=Sigma_B^inc beta_2 (alpha_1+n_B alpha_2/w)/c_s^2`.
- The bulk-from-sound estimator is now
  `zeta=w(Gamma_s-Gamma_cond)-2(d-1)eta/d`, so the neutral estimator is
  explicitly a charge-decoupled special case rather than the generic finite
  density formula.
- The same-state transport datum now includes `n_B`, `beta_{1,2}`, and
  `alpha_{1,2}`, and the closure residual includes `R_cond` for conductive
  sound uncertainty.

## Negative Controls

- The old neutral estimator
  `w Gamma_s-2(d-1)eta/d` is rejected at finite density because it
  misidentifies conductive damping as bulk viscosity.
- Missing charged-sound derivative data is rejected as an incomplete
  same-state transport datum.
- The residual budget rejects omitted conductive uncertainty.
- The check distinguishes zero density from charge-decoupling: the conductive
  term vanishes in the charge-conjugation/`beta_2=0` case, not merely because a
  symbol named density was set to zero while the thermodynamic coupling was
  left on.

## Evidence Companion

`qcd_phase_checks.py` now constructs the exact rational longitudinal
determinant

```text
d(omega,k)=omega^3+i A k^2 omega^2-c_s^2 k^2 omega+i B k^4
```

with `A=gamma_visc+Sigma alpha_2` and
`B=Sigma(alpha_1 beta_2-alpha_2 beta_1)`.  It then recovers

- `Gamma_s=A+B/c_s^2`;
- `D_B=-B/c_s^2`;
- `Gamma_cond=Gamma_s-gamma_visc`.

The companion uses the exact sample
`w=12`, `n_B=6`, `eta=3/2`, `zeta=5/2`, `Sigma=3/5`,
`beta=(1/4,1/2)`, and `alpha=(1/3,1)`, giving
`c_s^2=1/2`, `gamma_visc=3/8`, `Gamma_cond=1/2`,
`Gamma_s=7/8`, and `D_B=1/10`.

## Verification

- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase`
- `tools/run_calculation_checks.sh --python-only`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_x/chapter12_qcd_phase_structure_plasma_dense_matter.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/build_monograph.sh`

The full monograph build completed with a clean log scan at 3456 pages.

No issue-tracking, review-monitoring, or planning directive language was added
to the monograph TeX.
