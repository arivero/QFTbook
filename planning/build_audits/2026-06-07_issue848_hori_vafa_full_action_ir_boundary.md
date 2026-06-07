# 2026-06-07 Issue #848 Hori--Vafa Full-Action/IR Boundary Pass

## Scope

- Target issue: #848, Vol VII Ch09 full mirror-QFT data beyond protected
  twisted superpotentials.
- Related issues: #847 Hori--Vafa conventions and #725 evidence independence;
  the latest #847/#725 determinant/Fujikawa follow-up was folded into this
  pass because it touches the same chapter and companion.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Companion target: `calculation-checks/susy_2d_lg_glsm_checks.py`.
- Dossier target:
  `planning/chapter_dossiers/volume_vii/chapter09_two_dimensional_supersymmetric_models.md`.

## Source/Recheck Inputs

- Re-read issue #848 body and current #847/#725 state.
- Re-read the fresh #847/#725 follow-up on commit `7aaf131b`: missing
  Hermitian Dirac square, hidden `1/(4 pi)` determinant density, kinematic
  sign extraction, and assigned Fujikawa index.
- Checked `claude_review.md`; no new review directives since
  `2026-06-03 07:48:35 PDT`.
- Consulted the local stringbook source ranges cited by #848:
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`
  lines `12242--12321` and `22483--22740`.

## Quality Audit

- The previous chapter status labels correctly named Hori--Vafa and
  cigar/Liouville as conjectural full-QFT statements, but still let the
  proposed mirror look like it was specified mostly by periodic variables and
  a twisted superpotential.  This pass makes the conjecture an IR equivalence
  of regulated QFTs and defines the missing mirror-QFT datum: Kahler/D-term
  functional, measure, counterterms, global/orbifold data, noncompact boundary
  conditions, and Wilsonian map to the IR.
- The charged-chiral local dualization now records the classical dual D-term
  Legendre potential, the domain `Y + bar Y > 0`, the singular boundary, and
  the induced-measure/anomaly obligation.  This makes clear that a mirror
  coordinate and a protected F-term do not define the full mirror theory.
- The cigar/Liouville section now includes the intermediate dual D-term action,
  exact cigar metric/dilaton normalization, central charge, continuous and
  discrete spectral labels, spectral-flow momentum/winding lattice, reflection
  amplitude, normalized asymptotic Liouville action, and the marginality check
  for the Liouville exponential.
- The companion adds finite full-action/IR boundary checks and
  cigar/Liouville spectral-data cells.  These are still not a proof of the
  full dualities; they reject the shortcuts that #848 identified.
- The adjacent #847/#725 re-audit corrects the determinant/Fujikawa bridge:
  the chapter now displays the charged-chiral quadratic action, the Hermitian
  corrected Dirac square, the local determinant density with explicit
  `1/(4 pi)` factor, the `1/(2 pi)` twisted-`F` component normalization, and
  the same-convention heat-kernel trace `Tr_reg gamma_*=-Q k` whose
  mass-rotation Jacobian shifts theta by `+Q alpha`.
- The companion no longer uses a one-point response sign or assigned zero
  modes for that cell.  It checks Hermiticity of the curvature term, extracts
  the determinant coefficient after division by the signed analytic logarithm
  for both charge signs and mass orderings, and computes the signed chiral
  trace from finite flux Dirac-complex ranks and the heat-kernel coefficient.
- Remaining #848 obligations are deliberately retained: finite-field
  `K(Y,bar Y)` control, exact spectral-measure and pole-residue matching,
  rigidity/classification of allowed deformations, operator completeness, and
  boundary-state/defect matching.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
