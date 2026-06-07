# 2026-06-07 Issue #848 Boundary/Defect Probe

## Scope

- Target issue: #848, full mirror-QFT data beyond protected
  superpotential/residue information.
- Chapter touched:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion touched: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Metadata touched: calculation README, evidence contract, and Volume VII
  Chapter 9 dossier.

## Substance Audit

This pass targets the remaining boundary/defect part of the full mirror-QFT
claim.  Matching spectra, protected chiral rings, local source vectors, and
asymptotic Liouville data still does not identify annulus amplitudes,
boundary-state one-point functions, defect-twined traces, or defect fusion.

The chapter now adds `ca:glsm-mirror-boundary-defect-gate`, a finite cylinder
regulator comparison.  It requires closed-channel boundary vectors,
open-channel traces, Cardy residuals, boundary-source residuals, defect
operators commuting with the preserved algebra, defect fusion residuals, and
defect-twined traces.  The cigar/Liouville ledger now points `C_bdry` to these
annulus and defect observables rather than leaving "boundary matching" as an
unexpanded phrase.

## Companion Evidence

`check_full_mirror_boundary_defect_probe_obstruction()` constructs:

- two boundary vectors with the same protected boundary one-point row and the
  same self-cylinder amplitude, but different annulus amplitude against a probe
  boundary;
- two diagonal defect operators that commute with the finite Hamiltonian,
  square to the same identity fusion channel, and agree on the protected
  subspace, but have different defect-twined traces;
- a residual telescope showing that omitting the boundary-source residual
  underbudgets the comparison.

This is a finite obstruction cell for boundary/defect-blind shortcuts.  It
does not derive the cigar/Liouville boundary state category, open-channel
spectrum, exact Liouville branes, or defect fusion category.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail --limit 20`
- `tools/audit_monograph_text.sh`
- TeX process-leakage scan on the edited chapter
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `git diff --check`
- full `tools/run_calculation_checks.sh --python-only`
- full `tools/build_monograph.sh`

All targeted and repository-wide checks passed before landing.  The full build
completed with a clean log scan for `monograph/tex/main.pdf`.
