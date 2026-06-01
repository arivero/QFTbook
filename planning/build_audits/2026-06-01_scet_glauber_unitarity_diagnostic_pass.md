# 2026-06-01 SCET Glauber Unitarity Diagnostic Pass

## Scope

Issue advanced: #630.

This pass adds a finite operator diagnostic for the Glauber-exchange boundary
in Volume II, Chapter 19b.  It is deliberately not stated as a factorization
theorem.  The finite statement records the unitary trace mechanism:

\[
  \operatorname{Tr}(M U_G\rho U_G^\dagger)
  =
  \operatorname{Tr}(M\rho)
\]

when the measurement is inclusive on the Glauber/spectator factor or when the
measurement operator commutes with the finite Glauber unitary \(U_G\).  The
same algebra records the obstruction: if a measurement projects onto a
spectator/color coordinate that does not commute with \(U_G\), the trace can
change and the Glauber coordinate must be included in the factorized datum or
the proposed factorization is false for that measurement.

The text explicitly separates this finite unitarity mechanism from the
continuum QCD proof burden: identifying the regulated Glauber region,
justifying eikonal approximations and contour deformations, proving the
inclusive/commuting measurement property, and bounding the smeared-cross-section
remainder.

## Calculation Check

Extended `calculation-checks/scet_factorization_checks.py` with a rational
orthogonal finite Glauber unitary:

- verifies \(U_G^\dagger U_G=1\);
- verifies inclusive trace invariance;
- verifies trace invariance for a commuting measurement;
- verifies that a noncommuting projector detects the Glauber rotation.

## Verification

Run clean before commit:

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

## Status

This closes one finite-algebra component of the SCET/Glauber rigor gap in
#630.  It does not close #630: full QCD factorization still requires the
continuum Glauber analysis, refined measured-observable factorization,
continuum JIMWLK control, and the other QCD-rigor subclusters.
