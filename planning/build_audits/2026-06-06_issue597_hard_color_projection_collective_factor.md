# Build Audit: Issue 597 Hard Color Projection And Collective Factor

Date: 2026-06-06

## Scope

- Volume II Chapter 20D, instantons as physical amplitudes.
- Physics-facing instanton amplitude pass, not an ADHM or moduli-space
  expansion.
- Added the hard-channel color-orientation Haar tensor for the embedded
  charge-one two-frame and made the antisymmetric color projection part of the
  source amplitude.
- Repaired the hard `SU(3)`, `N_f=2` coefficient after review: restored the
  running bosonic collective-coordinate factor
  `(8 pi^2/g_ht^2(Q))^6` in the hard coefficient, OPE split, assembled
  amplitude, same-theory ratio, and logarithmic slope statement.
- Replaced the proper-time Dirac fundamental fermion `Pf` convention with a
  determinant convention and added the associated negative control.

## Quality Re-Audit

- This pass addresses physical instanton amplitudes rather than easier
  moduli-space geometry: source color projection, zero-mode/fluctuation
  normalization, hard-scale running, and same-channel observable bookkeeping.
- The repair keeps the chapter consistent with the parent anomaly/instanton
  chapter's hard-momentum scaling formula.
- The new exact checks reject:
  - replacing the two-frame Haar tensor by an orientation-volume constant;
  - symmetric color-pair sources masquerading as hard amplitudes;
  - coefficients or ratios that keep only the pure `Q^(-35/3)` power and omit
    the running collective-coordinate Jacobian;
  - a Pfaffian half-convention substituted for Dirac fundamental determinants.
- No directive, GitHub, monitoring, or review-process language was inserted
  into monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- Focused Chapter 20D audits: theorem form, unnumbered display labels,
  negative-scope prose, style density.
- Process-language scan of the touched TeX/check surfaces.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only` passed; Wolfram checks were
  not selected.
- `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` built cleanly at
  3456 pages.
