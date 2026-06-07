# Issue #848 Background-Response Gate

## Target

- GitHub issue: #848, full GLSM/Hori--Vafa and cigar/Liouville mirror-QFT data.
- Chapter target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Planning target:
  `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`.

## Substance

- Added `rem:glsm-mirror-background-response-obligation` after the
  operator/source warning.  The new gate treats the stress-tensor multiplet,
  vector and axial current multiplets, background flavor sources,
  gravitational and `R`-current contact terms, and cigar/Liouville
  dilaton/background-charge coupling as full mirror-QFT data.
- Introduced the mixed finite-regulator kernel
  `G^{bg}_{AI,Lambda}(beta)` and residual bound
  `B^{bg}_{AI,Lambda}(beta)`.  This makes background-coupled generating
  functionals a required comparison target, beyond the twisted
  superpotential, flat spectrum, flat source metric, or a single contact
  convention.
- Added `check_full_mirror_background_response_obstruction()` to the GLSM
  companion.  The finite model gives two candidate mirrors with the same
  spectrum, same flat source resolvent, and same protected source projection;
  their background rows differ.  A local contact patch can match one
  Euclidean probe, but the second probe still detects the wrong
  stress-tensor/current row.
- Updated the calculation README, evidence-contract tags, and Ch09 dossier
  so this is recorded as a background-response/current-multiplet gate rather
  than a new protected Hori--Vafa identity.

## Re-Audit Notes

- The TeX insertion stays in the monograph voice and contains no directive,
  review, monitor, or issue-management language.
- The pass targets physics depth: the data are curved/background-coupled QFT
  response functions and Ward/contact-term structure, not an additional
  finite lemma adjacent to the superpotential presentation.
- The new gate leaves #848 open: it does not prove full mirror equivalence,
  finite-field Kahler uniqueness, Liouville reflection normalization, the
  full continuous Plancherel measure, or complete defect/boundary-state
  matching.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 -m json.tool calculation-checks/evidence_contracts.json >/tmp/qft_evidence_contracts.jsoncheck`
- `git diff --check -- monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex calculation-checks/susy_2d_lg_glsm_checks.py calculation-checks/README.md calculation-checks/evidence_contracts.json planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `rg -n "directive|claude_review|monitor|open issue|GitHub issue|depth-pass|unprecedented|planning doc|agent|review" monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

All verification commands above passed; the `rg` leakage scan returned no
matches.
