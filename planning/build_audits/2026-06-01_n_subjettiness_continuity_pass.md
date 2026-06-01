# Minimized N-Subjettiness Continuity Pass

Date: 2026-06-01

Related issues:
- GitHub #526
- GitHub #630

Scope:
- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `calculation-checks/n_subjettiness_continuity_checks.py`
- `calculation-checks/README.md`
- `calculation-checks/INDEX.md`
- `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`
- `tools/run_calculation_checks.sh`

Purpose:
- Strengthen the modern jet-substructure section by formulating
  \(N\)-subjettiness as a nonperturbative calorimetric value functional on a
  positive jet energy measure, rather than as a statement about partonic
  histories or arbitrary axis labels.

Mathematical change:
- Added the globally minimized \(N\)-subjettiness functional on a compact jet
  patch,
  \[
    \tau_{N,\min}^{(\beta)}(\mu)
    =
    (M R_0^\beta)^{-1}
    \inf_{A\in Y^N}\int_Y \min_{a\in A}d(n,a)^\beta\,d\mu(n).
  \]
- Proved that minimizing axes exist by compactness of \(Y^N\), and that the
  minimized value is weakly continuous for measures with total mass bounded
  away from zero.
- Derived explicit soft-addition and collinear-recombination bounds for the
  minimized value.  This separates the physical observable from selected axis
  labels, which can jump at degenerate events.

Calculation check:
- Added `calculation-checks/n_subjettiness_continuity_checks.py`, using the
  exact \(N=1,\beta=2\) weighted-variance model to verify the soft bound, the
  collinear within-cluster variance identity, and value invariance under a
  discrete axis-label swap.
- Repaired `tools/run_calculation_checks.sh --list` for selections in which
  one language has zero checks, so targeted inventory verification does not
  fail under `set -u` on empty arrays.

Verification commands:
- `python3 calculation-checks/n_subjettiness_continuity_checks.py`
- `python3 -m py_compile calculation-checks/n_subjettiness_continuity_checks.py`
- `tools/run_calculation_checks.sh --list --only n_subjettiness`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

Remaining issue boundary:
- This pass does not close #526 or #630.  Modern jet-substructure work still
  needs stronger operator-level factorization and matching for additional
  observables such as refined jet grooming, track-assisted observables, and
  hadron-collider substructure in the presence of beam and Glauber data.
