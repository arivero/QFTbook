# 2026-06-01 ANEC Modular Entropy-Squeeze Pass

## Scope

Issue advanced: #519.

This pass strengthens the ANEC part of Volume III, Chapter 10.  The previous
text named relative-entropy monotonicity and said that region/complement
entropy variations cancel.  The chapter now displays the one-sided derivative
bookkeeping:

- for a positive null cut \(R_{s\varphi}\subset R_0\), monotonicity gives a
  nonpositive derivative of the region relative entropy;
- the null-cut modular Hamiltonian differentiates to the right half-line
  stress-tensor integral with the minus sign;
- for the complementary cut, monotonicity gives a nonnegative derivative and
  the modular Hamiltonian differentiates to the left half-line integral with
  the plus sign;
- equality of region and complement entropy first variations in the
  split-regulated pure-state exhaustion squeezes the same entropy derivative
  between the two modular-energy bounds;
- compatibility of those two bounds is exactly the nonnegative full null-line
  ANEC integral.

The result remains a theorem-boundary mechanism rather than a monograph-local
proof of the full null-cut modular-Hamiltonian theorem.

## Calculation Check

Extended `calculation-checks/conformal_collider_checks.py` with an exact
rational finite check of:

- the right null-cut modular-variation sign;
- the complementary null-cut modular-variation sign;
- the region/complement relative-entropy derivative inequalities;
- the fact that a compatible entropy squeeze implies a nonnegative full
  null-line integral.

## Verification

Run clean before commit:

- `python3 calculation-checks/conformal_collider_checks.py`
- `python3 -m py_compile calculation-checks/conformal_collider_checks.py`
- `tools/run_calculation_checks.sh --python-only --only conformal_collider`
- `git diff --check`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/audit_negative_scope_prose.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

## Status

This closes one sign-sensitive modular-ANEC exposition gap inside #519.  It
does not close #519: the all-order renormalized light-ray OPE/mixing theorem,
complete endpoint matching beyond the displayed leading structures, and the
high-loop/frontier energy-correlator program remain open.
