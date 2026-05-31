# Nested Bethe Pole-Cancellation Wrapper Demotion

Date: 2026-05-31

Scope:

- Volume VI, Chapter 4B, `chapter04b_nested_bethe_ansatz_matrix_bethe_yang.tex`.
- GitHub issue context: #691 anti-wrapper audit for theorem-family statements
  whose proofs are only local algebra or straightforward substitutions.

Change:

- Demoted the former proposition "Pole cancellation gives the nested
  equations" to a paragraph-level derivation.
- Preserved the dressed-vacuum eigenvalue, the twisted nested Bethe equation,
  the residue equation, and the reduction to the homogeneous untwisted chain.
- Added explicit prose that the calculation is a residue computation inside
  the dressed-vacuum formula, not an independent theorem.
- Updated the chapter dossier to call the result a derivation and to point to
  both calculation scripts that check the SU(3) example and the
  dressed-vacuum pole-factorization identity.
- Added a theorem-form audit guard so the demoted proposition title is flagged
  if it is reintroduced.

Verification planned:

- `python3 calculation-checks/nested_bethe_ansatz_checks.py`
- `python3 calculation-checks/nested_integrability_checks.py`
- `python3 -m py_compile calculation-checks/nested_bethe_ansatz_checks.py calculation-checks/nested_integrability_checks.py tools/audit_theorem_form.py`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
