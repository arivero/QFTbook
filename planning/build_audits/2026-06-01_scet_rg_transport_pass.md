# SCET RG-Transport Pass

Date: 2026-06-01

Scope:

- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `calculation-checks/scet_factorization_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`

Purpose:

Issues #526 and #630 both ask that jet-substructure and SCET material avoid
the standard loose use of phrases such as "resummed at NLL" or "leading
power" without the data that make the statement meaningful.  This pass
upgrades the logarithmic-accuracy paragraph into an explicit transform-space
renormalization-group transport datum.  The chapter now names the transformed
hard, jet, and soft coordinates, states the anomalous-dimension consistency
condition, defines evolution kernels from natural scales to a common scale,
and explains precisely what LL/NLL/NNLL and primed labels do and do not
assert.

Logical boundary:

- The new material proves only the finite scalar RG-transport algebra once the
  SCET operator datum and anomalous dimensions have been supplied.
- It does not prove a QCD factorization theorem, Glauber cancellation,
  rapidity-factorization theorem, or a numerical error estimate outside the
  declared logarithmic hierarchy.

Calculation companion:

- `scet_factorization_checks.py` now includes an exact rational piecewise
  anomalous-dimension check: when
  \(\gamma_H+2\gamma_J+\gamma_S=0\), transport from natural scales to a later
  common scale is independent of the chosen common scale.  It also checks the
  finite bookkeeping of a paired hard-soft anomalous-dimension scheme shift.

Verification:

- `python3 calculation-checks/scet_factorization_checks.py`
- `python3 -m py_compile calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --list --only scet_factorization`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/build_monograph.sh`

Build result:

- Clean log scan.
- `monograph/tex/main.pdf` built successfully at 2836 pages.
