# 2026-05-30 FZZT Shift-Ratio Pass

Scope:
- Continued #697 in Volume V, Chapter 13.
- Focused on the FZZT boundary-Liouville one-point theorem boundary.

Edits:
- Added an explicit finite-difference check paragraph after the conversion
  from the alpha-basis FZZT one-point function to the momentum-space
  wavefunction.
- Wrote the \(b\)-shift ratio and the independent \(b^{-1}\)-shift ratio
  obeyed by \(U_s(\alpha)\) in the chapter normalization.
- Separated what is directly checked from what remains theorem-boundary:
  the full boundary bootstrap/sewing construction must still supply the
  degenerate boundary connection coefficients, reflection relation,
  nonresonance hypotheses, and growth conditions.
- Extended `calculation-checks/liouville_bpz_checks.py` to compare the
  displayed gamma-function representative against both shift ratios.

Checks run:
- `python3 calculation-checks/liouville_bpz_checks.py`
- `python3 -m py_compile calculation-checks/liouville_bpz_checks.py`

Status:
- #697 remains open.  This pass reduces the FZZT one-point black-box content,
  but the analytic boundary-Liouville sewing problem, boundary two-point
  functions, and full Cardy-Lewellen/nonrational sewing closure remain proof
  obligations.
