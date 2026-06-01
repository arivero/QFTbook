# Soft-drop finite-tree margins pass

Date: 2026-06-01

Issue context: GitHub #526, modern jet-substructure rigor gate.

## Scope

This pass strengthens the soft-drop part of Volume II, Chapter 19b.  The
chapter already separated the \(\beta_{\rm SD}>0\) groomed-four-vector IRC
statement from the \(\beta_{\rm SD}=0\) mMDT counterexample.  The new material
adds the finite-event object underneath that classification: soft drop as a
deterministic recursion on a finite Cambridge--Aachen declustering tree.

The pass defines the branch energies, branch angle, soft-drop decision margin
\(m_v^{\rm SD}\), and harder-branch margin \(m_v^{\rm hard}\).  It explains
that a finite event is genuinely "away from grooming boundaries" only when
the visited soft-drop inequalities, harder-child choices, and clustering
comparisons have positive margins.  On such a chart, the retained leaf set is
locally constant and smooth groomed observables inherit the local soft and
collinear behavior of the retained-momentum map.  Boundary hypersurfaces are
not silently discarded; they require separate distributional treatment when
the observable is singular or endpoint-resummed.

## Files

- `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`
- `calculation-checks/soft_drop_irc_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_ii/chapter19b_jets_ir_safe_observables_hadronization.md`

## Verification

- `python3 calculation-checks/soft_drop_irc_checks.py`
- `python3 -m py_compile calculation-checks/soft_drop_irc_checks.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2826 pages.

## Closure status

Issue #526 remains open.  This pass closes the finite-tree/margin
bookkeeping gap for soft drop, but the full issue still tracks measured
groomed-function-specific factorization/resummation examples, deeper SCET
coverage, and broader modern jet-substructure development.
