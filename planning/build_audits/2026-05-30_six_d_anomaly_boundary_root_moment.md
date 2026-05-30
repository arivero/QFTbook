# Six-Dimensional Anomaly Boundary Root-Moment Pass

## Scope

- Reviewed `claude_review.md` and the open proof-debt backlog.
- Targeted the Volume VII six-dimensional SCFT depth-pass-B lane (#626) and
  the quoted-theorem discipline around the \((2,0)\) anomaly polynomial.

## Change

- Kept the \((2,0)\) anomaly polynomial as a quoted theorem: the chapter still
  does not construct the interacting six-dimensional local QFT from first
  principles.
- Expanded the local theorem boundary immediately after the quoted theorem:
  the text now isolates the interacting anomaly excess
  \(I_8[\mathfrak g]-r_{\mathfrak g}I_8(1)\), explains its tensor-branch
  Green--Schwarz role, and derives the simply laced root-system identities
  \(\sum_{\alpha>0}\alpha\otimes\alpha=h^\vee\id\) and
  \(d_{\mathfrak g}=r_{\mathfrak g}(h^\vee_{\mathfrak g}+1)\).
- Extended `calculation-checks/susy_abjm_6d_checks.py` to verify the
  positive-root second moment for the \(A\) and \(D\) series and the ADE
  dimension/root-count relation.

## Status

This is a proof-boundary strengthening, not a closure of #626.  The remaining
six-dimensional depth pass still includes a fuller treatment of defects,
compactification data, and non-Lagrangian construction status.
