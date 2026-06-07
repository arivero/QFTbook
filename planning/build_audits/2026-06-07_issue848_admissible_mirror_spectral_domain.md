# 2026-06-07 Issue #848 Admissible Mirror Spectral Domain

## Scope

- Target issue: #848, full mirror-QFT data beyond protected Hori--Vafa
  superpotentials.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`.
- Added `def:glsm-admissible-mirror-datum` and
  `eq:liouville-robin-finite-volume-quantization`.

## Quality Audit

- This pass addresses the critique that `mathfrak M_Lambda` was only a data
  interface.  The chapter now states what makes the package an admissible
  cutoff QFT datum: regulated functional integral, self-adjoint Hamiltonian
  domain, renormalized operator topology, noncompact spectral resolution,
  reflection relation, pole residues, and source/contact terms.
- The text now separates three claims that should not be collapsed:
  existence of an admissible mirror datum, universality or rigidity among
  choices of finite-field `K` and boundary data, and the final GLSM/mirror
  duality assertion.
- The new finite-volume Robin quantization cell makes the physics point at
  the Hamiltonian level: changing the wall/self-adjoint-domain datum changes
  the regulated radial energy levels, then survives as the continuum phase
  density.  This is not a tangential mathematical addition; it is directly
  about what Hilbert space the mirror QFT claims to match.

## Verification

- Focused companion:
  `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`;
  `PYTHONPATH=calculation-checks python3 calculation-checks/susy_2d_lg_glsm_checks.py`;
  `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`.
- Focused chapter audits:
  `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`;
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`;
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`;
  TeX leakage scan for review/directive/process strings.
- Planning/metadata audits:
  `python3 -m json.tool calculation-checks/evidence_contracts.json`;
  `python3 tools/audit_calculation_check_inventory.py`;
  `python3 tools/audit_calculation_evidence_contracts.py`;
  `tools/audit_chapter_dossiers.sh`.
- Global verification:
  `tools/run_calculation_checks.sh --python-only`;
  `tools/build_monograph.sh`;
  `git diff --check`.
