# Track-observable lift pass

Date: 2026-06-01

Issue context: GitHub #526, modern jet substructure with rigorous track
functions and track-based observables.

## Scope

This pass strengthens the track-function section of Volume II Chapter 19b by
adding the missing observable-lifting layer.  The finite definition starts
from a partonic short-distance configuration, assigns a track random variable
to every labeled parton, forms the random charged-track energy measure, and
defines the lifted coefficient for an energy polynomial by conditional
expectation.

The pass emphasizes the diagonal/contact bookkeeping: a two-point track-based
energy polynomial contains second track moments on repeated parton labels,
not the square of the first charged-energy moment.  It also records the
first- and second-moment collinear composition identities behind the
track-function renormalization problem.

## Files

- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `calculation-checks/track_observable_lift_checks.py`
- `calculation-checks/README.md`
- `calculation-checks/INDEX.md`
- `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`

## Verification

All checks passed in this edit pass:

- `python3 calculation-checks/track_observable_lift_checks.py`
- `python3 -m py_compile calculation-checks/track_observable_lift_checks.py`
- `tools/run_calculation_checks.sh --list --only track_observable_lift`
- `tools/run_calculation_checks.sh --python-only --only track_observable_lift`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh` (clean at 2834 pages)

## Closure status

Issue #526 remains open.  This pass closes one concrete track-based
observable gap, while the broader issue still includes more SCET-level
factorization/resummation examples and other modern jet-substructure regimes.
