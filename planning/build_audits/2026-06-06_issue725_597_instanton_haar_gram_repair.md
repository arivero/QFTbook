# Issue #725/#597 instanton Haar-Gram evidence repair

## Target

Repair the remaining evidence-independence weakness in the BPST instanton
orientation companion.  The manuscript already derives the shared four-slot
\(SU(2)\) orientation projector by projecting onto the two-dimensional
invariant-tensor subspace and inverting its Gram matrix.  The executable check
still instantiated the resulting \(1/3,-1/6,-1/6,1/3\) coefficients directly,
so it would not catch a common copied-coefficient error.

## Change

- `calculation-checks/bpst_instanton_normalization_checks.py` now constructs
  the two invariant tensors, computes their finite Gram matrix, inverts it,
  and uses that inverse to build the four-slot Haar projector.
- The check verifies the Gram matrix, the derived coefficient matrix, and
  projector idempotence over all finite core/color tensor components before
  using the projector in the four-source instanton orientation tests.
- `calculation-checks/README.md` and the Chapter 20 dossier now record that
  the shared-orientation projector is evidence-backed by Gram inversion rather
  than copied from the displayed formula.

## Re-audit

This is a physics-amplitude evidence repair.  The orientation average is the
spin/color tensor normalization inside the four-source instanton amplitude; it
is not a standalone group-theory annex.  The pass keeps the monograph surface
unchanged because the TeX proof already displays the Gram-inversion mechanism.

## Verification

- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization_checks`
- Focused Chapter 20 theorem-form, unnumbered-display-label,
  negative-scope, and style-density audits.
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- Metadata/process-leak scan on the touched TeX/check/README files.
- `tools/run_calculation_checks.sh --python-only`
- `git diff --check`
- `tools/build_monograph.sh` clean; `monograph/tex/main.pdf` remains
  3411 pages.

The ordinary evidence-contract audit is clean.  The stricter global
risk-report mode remains outside this pass: it still tracks other unmanifested
risk-class companions elsewhere in the repository, not this BPST companion.
