# SCET zero-bin overlap pass

Date: 2026-06-01

Issue context: GitHub #526 and #630, modern jet-substructure and QCD
factorization rigor.

## Scope

This pass strengthens the SCET/factorization section of Volume II Chapter 19b
by making the zero-bin/overlap subtraction entry mathematically explicit.  The
new finite-regulator model uses momentum cells for collinear and soft
approximations, identifies their common soft-collinear corner, and writes the
matched singular coordinate as an inclusion--exclusion formula.

The point is conceptual and algebraic: a zero-bin is not an optional phrase
and not a claim that an overlap integral disappears.  In a particular
regulator, such as dimensional regularization, an overlap integral may be
scaleless and vanish after analytic continuation; the factorization datum
still has to specify which overlap coordinate is being subtracted and how
finite convention changes are paired between the collinear and soft
coordinates.

## Files

- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `calculation-checks/scet_factorization_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`

## Verification

All checks passed in this edit pass:

- `python3 calculation-checks/scet_factorization_checks.py`
- `python3 -m py_compile calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --list --only scet_factorization`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh` (clean at 2835 pages)

## Closure status

Issues #526 and #630 remain open.  This pass closes one finite overlap
subtraction gap, while the broader jet-substructure and QCD-rigor issues still
include deeper SCET/Glauber factorization, resummation, boosted/electroweak jet
regimes, and other nonperturbative QCD operator developments.
