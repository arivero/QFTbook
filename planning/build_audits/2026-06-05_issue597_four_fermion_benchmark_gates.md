# Issue #597 four-fermion instanton benchmark gates

Date: 2026-06-05

## Scope

This pass addresses the instanton-depth concern that moduli-space data and
local vertex formulas can outpace the physical amplitude architecture.  It
adds an architecture-level benchmark ledger in Volume II Chapter 20 rather
than another ADHM or finite-identity cell.

The new controlled approximation,
`ca:thooft-four-fermion-benchmark-gate-ledger`, packages the gates that must
close before comparing a finite-regulator calculation with a 't Hooft-style
four-fermion instanton amplitude:

- center momentum conservation;
- classical/collective data;
- finite nonzero-mode determinant normalization;
- zero-mode source saturation;
- shared Haar projection;
- external-leg amputation;
- source conditioning;
- size-window and endpoint control;
- sector isolation;
- physical LSZ/OPE/hadronic/inclusive projection;
- finite scheme/frame transport.

The TeX block is intentionally not process metadata.  It is a manuscript
claim about the physical object being computed.  The process/evidence record
lives here and in the Chapter 20 dossier.

## Evidence Companion

`calculation-checks/bpst_instanton_normalization_checks.py` now includes
`check_thooft_four_fermion_benchmark_gate_ledger()`.  The check verifies the
finite gate list, the noncancellation-margin residual bound, and negative
controls for:

- off-shell center momentum;
- moduli/determinant density mistaken for the four-fermion amplitude;
- rank-collapsed source projections;
- unamputated external residues;
- colored Euclidean kernels treated as physical amplitudes;
- sector leakage;
- reusing a stale determinant constant after finite source/operator frame
  changes.

## Verification

- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization_checks`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail --limit 20`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The first full build exposed one overfull heading from the initial long title.
The title was shortened to `Instanton benchmark gates`, and the rerun completed
with a clean build/log scan at 3371 pages.
