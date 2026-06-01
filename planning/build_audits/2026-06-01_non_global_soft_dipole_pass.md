# Non-global soft-dipole pass

Date: 2026-06-01

Issue context: GitHub #630 and #526, QCD/jet-substructure rigor uplift.

## Scope

This pass adds a finite-regulator layer for non-global soft measurements in
Volume II, Chapter 19b.  The standard particle-physics phrase "non-global
logarithms" is replaced by an explicit finite angular-cell datum:

- measured veto cells \(\mathcal M\);
- unmeasured cells \(\mathcal U\);
- positive cell-integrated eikonal rates \(K_{ij}^c\) for each ordered dipole;
- finite gap coordinates \(G_{ij}(L)\);
- the finite nonlinear soft-dipole evolution equation.

The text derives the first two terms of the small-\(L\) expansion directly.
The first derivative is the direct veto rate \(-A_{ij}\).  The second
derivative separates the global Sudakov square from the first non-global
coefficient
\[
  \mathcal N_{ij}
  =
  \sum_{u\in\mathcal U}K_{ij}^{u}
  \bigl(A_{iu}+A_{uj}-A_{ij}\bigr).
\]
This identifies the mathematical mechanism: an unmeasured emission is
real--virtual balanced at first order, but its real branch creates two new
dipoles that may later radiate into the measured region.  The chapter keeps
the scope honest: this finite large-\(N_c\), strongly energy-ordered
soft-dipole datum is not a full QCD factorization theorem, and finite color,
Glauber exchange, recoil, collinear-neighborhood regulators, and matching to
hard/collinear functions remain separate data.

## Files

- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `calculation-checks/qcd_non_global_log_checks.py`
- `calculation-checks/README.md`
- `calculation-checks/INDEX.md`
- `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`

## Verification

- `python3 calculation-checks/qcd_non_global_log_checks.py`
- `python3 -m py_compile calculation-checks/qcd_non_global_log_checks.py`
- `tools/run_calculation_checks.sh --list --only qcd_non_global --skip-wolfram`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2828 pages.

## Closure status

Issues #630 and #526 remain open.  This pass closes one concrete
non-global-measurement rigor gap, but the broader QCD/jet agenda still tracks
stronger SCET/Glauber proofs, measured-observable factorization/resummation,
boosted/electroweak jets, and other QCD rigor subclusters.
