# 2026-06-01 Track-Function Operator and Moment-Tower Pass

## Scope

Issues advanced: #526 and #630.

This pass strengthens the track-function part of Volume II, Chapter 19b.  The
chapter now defines a track function as a renormalized gauge-invariant
collinear source matrix element paired with a charged-track energy-fraction
measurement operator.  The text separates this nonperturbative QCD operator
datum from the short-distance partonic coefficient into which the track
coordinate is inserted.

The pass also extends the finite-kernel real--virtual track-function evolution
from normalization and first moment to the moment-generating equation
\[
  \mu\partial_\mu M_i(\nu)=
  \sum_{j,k}\int dz\,K_{i\to jk}(z)
  \{M_j(z\nu)M_k((1-z)\nu)-M_i(\nu)\}
\]
and the resulting full moment tower.  This is the algebraic reason that a
track-based observable needs a distributional nonperturbative input, or an
equivalently complete moment sequence in a fixed scheme, rather than a single
average charged fraction.

## Calculation Check

Extended `calculation-checks/track_function_moment_checks.py`:

- exact rational preservation of normalization;
- exact rational first-moment evolution;
- exact rational moment-tower evolution through powers 0--4 for both quark
  and gluon test species in the finite-kernel model.

## Verification

Run clean before commit:

- `python3 calculation-checks/track_function_moment_checks.py`
- `python3 -m py_compile calculation-checks/track_function_moment_checks.py`
- `tools/run_calculation_checks.sh --python-only --only track_function_moment`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

## Status

This closes the track-function operator-datum and moment-tower subgap for the
current chapter treatment.  Issues #526 and #630 remain open: full closure
still requires stronger measured-observable factorization examples, stronger
Glauber/factorization infrastructure, continuum JIMWLK control, and broader
modern jet-substructure/QCD rigor development.
