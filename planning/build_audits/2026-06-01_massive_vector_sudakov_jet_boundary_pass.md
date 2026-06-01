# Massive-Vector Sudakov Jet-Boundary Pass

Date: 2026-06-01.

Issue context: GitHub #526 and #630.

Scope:
- Strengthened the high-energy electroweak/boosted-jet boundary in
  `monograph/tex/volumes/volume_ii/chapter19b_jets_ir_safe_observables_and_hadronization.tex`.
- Added `Massive-Vector Sudakov Boundaries` as a controlled-approximation
  section rather than a theorem.
- Derived the one-line soft-collinear phase-space area
  \(A_V(L)=\frac14 L^2\), \(L=\log(Q^2/M_V^2)\), from the finite chart
  \(0<y<L\), \(0<x<y/2\).
- Separated the scalar one-line Sudakov coordinate from the full
  electroweak charge-density-matrix datum, real-emission inclusiveness,
  resonance or narrow-width status for boosted objects, and QCD
  nonperturbative coordinates.

Calculation check:
- Extended `calculation-checks/scet_factorization_checks.py` with exact
  rational checks of the triangular massive-vector phase-space area, exponent
  coefficient, and additivity under subdivision of the logarithmic
  \(y\)-interval.

Verification commands for this pass:
- `python3 calculation-checks/scet_factorization_checks.py`
- `python3 -m py_compile calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

Status:
- This closes a concrete electroweak/boosted-jet boundary gap in the modern
  jet-substructure chapter.
- It does not close #526 or #630.  The remaining issues still include deeper
  measured-observable factorization examples, stronger Glauber/factorization
  infrastructure, continuum JIMWLK control, and other QCD-rigor clusters.
