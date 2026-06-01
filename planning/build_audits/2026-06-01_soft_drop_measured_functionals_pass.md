# Soft-drop measured-functionals pass

Date: 2026-06-01

Issue context: GitHub #526, modern jet-substructure rigor gate.

## Scope

This pass sharpens the mMDT part of Volume II, Chapter 19b.  The earlier
soft-drop classification established that the \(\beta_{\rm SD}=0\) groomed
four-vector is not collinear safe as a standalone observable.  The new
paragraph makes the measurement-level distinction explicit: mMDT safety
statements must be attached to a specified functional of the retained
constituents.

The chapter now defines the finite homogeneous angular moment
\[
  G_\kappa(S)
  =
  \frac{1}{E_S^2R_0^\kappa}
  \sum_{\ell,m\in S}E_\ell E_m\,\theta_{\ell m}^{\kappa},
  \qquad \kappa>0 ,
\]
and checks the one-prong collinear split directly.  For mMDT with
\(0<z<z_{\rm cut}\), the recursion deletes the softer daughter and
\(G_\kappa\) remains zero, just as for the unsplit one-particle jet.  For
\(\beta_{\rm SD}>0\), the two collinear daughters are retained at sufficiently
small angle and the moment equals
\[
  2z(1-z)(\theta/R_0)^\kappa ,
\]
which tends to zero.  By contrast the retained-energy fraction changes from
\(1\) to \(1-z\) in the same mMDT collinear split and is therefore not
collinear safe as a standalone measurement.

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

Issue #526 remains open.  This pass closes the finite mMDT measured-functional
distinction needed after the finite-tree margin pass, but the issue still
tracks measured-function-specific factorization/resummation examples, deeper
SCET coverage, boosted/electroweak jets, and broader modern jet-substructure
development.
