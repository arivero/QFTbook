# Issue #927 Soft-Mass Spectral Bridge Audit

## Scope

- Target chapter:
  `monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex`.
- Target check:
  `calculation-checks/susy_yang_mills_deformation_ladder_checks.py`.
- Target dossier:
  `planning/chapter_dossiers/volume_vii/chapter07b_susy_yang_mills_family_spectra.md`.

## Substance Audit

- Replaced the Abelian sine-ratio transfer paragraph with a derivative
  criterion:
  \(\log(R_k(t_1)/R_k(t_0))=\int\Gamma_k(t)\,dt\).
- Added a controlled small-soft-gaugino-mass spectral bridge segment:
  common regulator/tuning path, renormalized perturbing Hamiltonian
  derivative, finite-volume Riesz projections, Feynman-Hellmann identities
  for local-channel masses and flux-sector tensions, and ratio-response
  control.
- Added explicit failure diagnostics: level collision, spectral-gap closure,
  string breaking, line-lattice change, regulator/Pfaffian or
  reflection-positivity failure, and nonuniform continuum/thermodynamic
  limits.
- Upgraded the deformation-ladder calculation companion to an extended
  evidence contract with finite matrix checks for projection transport and a
  negative control rejecting constant ratio transport when the logarithmic
  response is nonzero.

## Physics-Depth Reaudit

- This pass develops physics architecture rather than another finite identity:
  the new bridge identifies the operator whose matrix elements move masses
  and string tensions under a soft gaugino mass.
- The bridge remains honestly local in the soft-mass parameter.  It does not
  claim a theorem reaching the bosonic Yang-Mills endpoint; extending the
  local segment through decoupling remains the open regulator-level problem.
- The Abelianized Seiberg-Witten sine ratio is treated as an initial datum
  requiring response control, not as evidence for bosonic \(k\)-string
  equality.

## Verification

- Passed: `python3 calculation-checks/susy_yang_mills_deformation_ladder_checks.py`.
- Passed: `python3 tools/audit_calculation_evidence_contracts.py`.
- Passed: `bash tools/audit_chapter_dossiers.sh`.
- Passed: `python3 tools/audit_calculation_check_inventory.py`.
- Passed: `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex --fail`.
- Passed: `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex`.
- Passed: `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter07b_susy_yang_mills_family_spectra.tex`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/run_calculation_checks.sh --python-only`.
- Passed: `tools/build_monograph.sh` after shortening the status-table
  entry that initially produced an overfull line.
- Passed: `git diff --check`.
