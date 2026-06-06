# 2026-06-06 Issue #630 Charge Diffusion Spectral Window

## Scope

- Volume X Chapter 12, `QCD Phase Structure, Plasma, and Dense Matter`.
- Target: complete the first-order QCD transport extraction triad by adding a
  finite conserved-charge/electrical-conductivity response window after the
  existing shear and bulk/sound windows.

## Substance

- Added `ca:qcd-finite-charge-diffusion-spectral-window` immediately after the
  momentum-projected baryon-current proposition.
- The new block starts from the convective-current projection, then constructs
  the contact-subtracted density diffusion pole
  `G^R=-chi_q gamma_q/(gamma_q-i omega)`.
- The conductivity is reconstructed as
  `Sigma_q^inc=chi_q gamma_q/k^2`, separating pole width, susceptibility
  residue, regular background, near-critical charge modes, sound mixing, and
  raw-current Drude weight.
- Extended `qcd_phase_checks.py` so the evidence object is a generated
  retarded density kernel and sampled spectral function, not the final
  conductivity formula read backward.

## Quality Audit

- Physics-facing depth: this targets the real-time extraction of a QCD
  transport coefficient from a finite spectral window.
- Not a tangential mathematics pass: no new formal hydrodynamic framework is
  introduced; the existing response-window architecture is applied to the
  missing conserved-charge channel.
- The chapter remains honest about scope: the finite window checks the
  extraction once an isolated diffusion pole exists; it does not prove that
  continuum QCD has such a pole in every phase.
- Planning and GitHub coordination language remains outside monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase`
- `tools/run_calculation_checks.sh --python-only`
- Focused Chapter 12 theorem-form, display-label, negative-scope, and
  style-density audits
- Process-language scan on touched monograph/check files
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/build_monograph.sh`
