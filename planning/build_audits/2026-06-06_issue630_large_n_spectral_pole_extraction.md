# Issue 630 Large-N Spectral Pole Extraction Build Audit

## Scope

- Added `ca:qcd-large-n-spectral-pole-extraction` to Volume II Ch19 immediately
  after normalized single-trace factorization and before Eguchi--Kawai volume
  reduction.
- The new block separates planar color topology from the spectral and
  scattering data needed to interpret large-\(N_c\) two-point functions as
  narrow meson/glueball pole data: positive spectral measure, isolated window,
  residue lower bound, continuum/background budget, threshold separation, and
  width scaling from on-shell couplings.
- Extended `calculation-checks/large_n_topology_checks.py` with exact finite
  spectral-moment arithmetic: the isolated-pole estimator bound,
  missing-residue-margin failure mode, first-moment ambiguity, and meson versus
  glueball width powers.
- Updated the Ch19 dossier, calculation-check README, and the factorization
  textual-candidate review anchors shifted by the Ch19 insertion.

## Verification

- `python3 -m py_compile calculation-checks/large_n_topology_checks.py`
- `python3 calculation-checks/large_n_topology_checks.py`
- `tools/run_calculation_checks.sh --python-only --only large_n_topology`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
- `git diff --check`

All selected checks passed.  Wolfram Language checks were not selected.  The
first monograph build caught a single overfull box in the controlled-approximation
title; the title was shortened to `Large-\(N_c\) spectral pole datum`, and the
subsequent build/log scan was clean at 3452 pages.

## Re-audit Notes

- This is a physics-depth boundary pass rather than another finite color-cell
  insertion: it says exactly what additional spectral information is required
  before the large-\(N_c\) expansion becomes hadron pole physics.
- The insertion is local and architectural, placed between factorization and
  volume reduction so the chapter flow moves from color topology to spectrum
  extraction before other large-\(N_c\) applications.
- No directive, monitoring, or GitHub-process language was added to the
  monograph TeX.
