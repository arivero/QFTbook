# Trotter And Faris-Lavine Dequotation Pass

Date: 2026-05-30

Scope:
- Volume I, Chapter 4, `qthm:trotter-product-formula-qm`.
- Volume I, Chapter 4, `qthm:faris-lavine-essential-self-adjointness`.

Edits:
- Replaced both `quotedtheorem` wrappers by local `theorem` environments.
- Strengthened the Trotter statement by replacing the vague phrase "suppose
  the hypotheses of the Trotter product formula hold" with explicit
  hypotheses:
  - real time: dense algebraic domain and essential self-adjointness of
    `A+B`;
  - Euclidean time: lower-semibounded closed quadratic forms with closed
    lower-semibounded form sum.
- Moved the existing Trotter mechanism into a proof environment: bounded
  operator Taylor/telescoping proof, then the unbounded form-sum/resolvent
  route and the real-time Chernoff derivative/stability argument on the
  algebraic core.
- Moved the existing Faris-Lavine mechanism into a proof environment:
  comparison Hamiltonian, oscillator graph estimate, commutator calculation,
  and Nelson commutator-theorem argument.
- Updated the Volume I Chapter 4 dossier.

Verification:
- `git diff --check`.
- `python3 tools/audit_theorem_form.py`.
- `python3 tools/audit_unnumbered_display_labels.py`.
- `tools/audit_negative_scope_prose.py`.
- `tools/audit_monograph_text.sh`.
- `tools/audit_chapter_dossiers.sh`.
- `tools/build_monograph.sh`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported 2623 pages.
