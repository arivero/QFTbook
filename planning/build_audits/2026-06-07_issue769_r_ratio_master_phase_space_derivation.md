# Issue #769 R-ratio master/phase-space derivation

## Scope

- Target issue: #769, loop-amplitude reconstruction to physical observables.
- Monograph target: Volume II, Chapter 6, inclusive vector-current
  form-factor closure.
- Companion target: `calculation-checks/generalized_unitarity_reduction_checks.py`.

This pass addresses the follow-up that the corrected R-ratio constants were
still imported as antenna tuples.  The goal is not another cancellation check:
it is to derive the virtual and real Laurent cells from separate regulated
routes before adding them.

## Repairs

- The TeX now derives the timelike virtual two-parton cell from the normalized
  spacelike one-loop form-factor pole kernel
  `-r_Gamma (eps^-2 + 3 eps^-1/2 + 4)` and the real part of
  `(-s-i0)^(-eps)`, so the `+7 pi^2/12` finite cell is no longer an inserted
  endpoint number.
- The real channel is now written as the `q qbar g` kernel
  `2 z/(x y) + x/y + y/x` integrated over the `D=4-2 eps` simplex phase space
  with the declared Born-normalization factor.  Beta-function reduction gives
  the displayed `2/eps^2 + 3/eps + 19/2 - 7 pi^2/6` cross-section-level cell.
- The companion expands the same factors in exact rational plus symbolic
  `pi^2` Laurent bookkeeping.  It rejects omitting the `D`-dimensional
  Born-normalization factor, omitting the timelike continuation, using an
  undeclared `O(eps^2)` common normalization, and relying only on final
  inclusive cancellation.
- Evidence-contract and inventory language now describes a form-factor
  master plus phase-space derivation rather than source-normalized tuple
  regression.

## Boundary

This is a process-level one-loop inclusive observable derivation.  It does not
claim to supply a full multi-scale production calculation, differential
event-shape subtraction, higher-loop master solution, or all-orders
factorization theorem.  It closes the specific evidence-independence gap for
the `R`-ratio finite virtual/real cells.

## Re-audit Correction

The original version of this pass still treated the four-dimensional
`2 z/(x y) + x/y + y/x` simplex kernel, together with an
`(1-eps/2)^(-1)` Born-normalization shortcut, as if it were the literal
all-epsilon real-channel formula.  Expanding that formula gives
`2/eps^2 + 4/eps + 21/2 - 7*pi^2/6`, not the standard real cell.

The repaired Chapter 6 block now displays the CDR tree current matrix element,
the Born spin average, and the corrected source-normalized real kernel
`2 z/(x y) + (1-eps)(x/y + y/x)` with prefactor
`exp(gamma eps)/Gamma(1-eps)`.  The companion check expands the same
soft/collinear Gamma functions and rejects the old four-dimensional shortcut
as a negative control.

## Verification

- `python3 -m py_compile calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- Focused Ch6 theorem-form, display-label, monograph-text, negative-scope,
  style-density, and leakage audits.
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- Calculation evidence-contract and inventory audits.
- Chapter dossier audit.
- `git diff --check`
- Full `tools/run_calculation_checks.sh --python-only`
- Full `tools/build_monograph.sh`
