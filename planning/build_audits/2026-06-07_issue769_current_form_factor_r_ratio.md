# Issue 769: Inclusive Vector-Current Form-Factor Closure

## Scope

- Monograph target: Volume II, Chapter 6, generalized unitarity to finite
  observables.
- Companion target: `calculation-checks/generalized_unitarity_reduction_checks.py`.
- Physics aim: move the production lane from a purely abstract hard-plus-real
  ledger to a concrete current-channel closure, without turning Chapter 6 into
  a full event-shape or jets chapter.

## Added Monograph Content

- Inserted `ca:inclusive-current-form-factor-ratio-closure` after the
  one-loop virtual-to-observable assembly block.
- The block uses the one-flavor massless vector-current channel underlying the
  perturbative \(e^+e^-\) \(R\)-ratio.
- It keeps the cut-reconstructed one-loop virtual form-factor interference
  separate from the integrated real \(q\bar q g\) channel:
  \[
    -2/\epsilon^2-3/\epsilon-8+\pi^2/6,
    \qquad
    2/\epsilon^2+3/\epsilon+19/2-\pi^2/6.
  \]
- The assembled result gives \(1+a_s C_F\,3/2\), hence
  \(1+\alpha_s/\pi\) for \(SU(3)\), only after the real channel and
  subtraction convention are carried with the virtual form factor.

## Companion Evidence

- Added exact `LaurentPi2` arithmetic, storing the coefficients of
  \(1/\epsilon^2\), \(1/\epsilon\), rational finite terms, and \(\pi^2\)
  finite terms separately.
- Added `check_inclusive_current_form_factor_r_ratio_closure()`.
- Positive checks:
  - double and single infrared poles cancel;
  - the \(\pi^2\) terms cancel symbolically;
  - the remaining coefficient is \(3/2\) in the \(a_s C_F\) normalization;
  - \(C_F=4/3\) converts this to the \(1+\alpha_s/\pi\) \(SU(3)\) coefficient.
- Negative controls:
  - virtual-only form factor still has infrared poles;
  - the finite virtual form-factor term is not the inclusive observable;
  - omitting the real endpoint finite cell changes the coefficient;
  - the wrong real-channel analytic-continuation sign leaves a \(\pi^2\)
    residue;
  - a finite subtraction-scheme shift must be transported to the real channel.

## Re-audit Notes

- This pass is intentionally process-facing: it tests how a reconstructed
  virtual amplitude becomes a physical inclusive coefficient.
- It does not claim to derive all differential jet/event-shape subtractions.
  Those remain the role of the later measurement-cell, factorization, and jets
  chapters.
- No planning, review, monitoring, or issue-directive language was inserted
  into the monograph TeX.
