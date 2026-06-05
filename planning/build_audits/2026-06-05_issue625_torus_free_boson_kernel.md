# Issue #625 Torus Free-Boson Kernel Pass

## Scope

- Volume V, Chapter 12: `ex:torus-free-boson-green-kernel`.
- Companion evidence: `calculation-checks/cft_higher_genus_sewing_checks.py`.
- Inventory updates: calculation-check README and Chapter 12 dossier.

## Substance

- Added an explicit genus-one free-boson Green-kernel calculation inside the
  higher-genus sewing section.
- The new example distinguishes the abstract sewing trace from a concrete
  worldsheet correlator:
  the torus scalar Green function exists only after constant-mode subtraction,
  vertex correlators require target-charge neutrality from the zero-mode
  integral, normal ordering subtracts diagonal self-contractions, and the
  additive Green constant is a vertex-normalization convention.
- The text identifies the higher-genus continuation as a prime-form,
  period-matrix, zero-mode, normal-ordering, and Szego-kernel problem rather
  than as a consequence of finite graph-genus bookkeeping.

## Verification

Completed on 2026-06-05:

- `python3 -m py_compile calculation-checks/cft_higher_genus_sewing_checks.py`
- `python3 calculation-checks/cft_higher_genus_sewing_checks.py`
- `tools/run_calculation_checks.sh --python-only --only cft_higher_genus_sewing`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_v/chapter12_vertex_operator_algebras_modular_sewing_and_logarithmic_cft.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- metadata-leak scan for process language in touched monograph/check files
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
