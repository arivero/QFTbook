# OS Argument-Domain Exhaustion Pass

Date: 2026-06-01.

Scope:
- Advanced GitHub issue #695 by tightening the corrected OS-II analytic
  theorem in the Osterwalder--Schrader reconstruction chapter.

Manuscript changes:
- Replaced the qualitative convex-geometry paragraph in Step 3 of
  `thm:corrected-os-ii-analytic-theorem` with an explicit finite
  bridge-insertion induction.
- The proof now defines \(B_k(a)=[-a,a]^k\), starts from the one-gap bridge
  interval, and shows directly that \(B_{k-1}(a)\subset c_{k-1}^{(N)}\)
  implies \(B_k(a)\subset c_k^{(N+1)}\) by choosing the split with empty left
  block, arbitrary bridge angle, and right block carrying the remaining
  \(k-1\) arguments.
- The exhaustion statement is now
  \[
    [-\pi/2+\epsilon,\pi/2-\epsilon]^k\subset c_k^{(k)},
  \]
  which is the exact strict half-plane exhaustion needed before the
  linear-growth-to-polynomial-tube-bound step.

Calculation check:
- Extended `calculation-checks/os_tube_sign_checks.py` beyond sign
  conventions to check the finite insertion schedule: the strict \(k\)-gap
  argument box is reached in \(k\) bridge-insertion steps from the one-gap
  interval.

Verification:
- `python3 calculation-checks/os_tube_sign_checks.py`
- `python3 -m py_compile calculation-checks/os_tube_sign_checks.py`
- `tools/run_calculation_checks.sh --python-only --only os_tube_sign`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
