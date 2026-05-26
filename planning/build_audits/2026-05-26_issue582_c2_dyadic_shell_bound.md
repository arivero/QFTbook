# 2026-05-26 Issue #582 C2 Dyadic Shell Bound

## Scope

- Volume XI, Chapter 9 now proves a uniform dyadic shell increment estimate
  for the dynamic \(\Phi^4_3\) two-loop local coordinate \(C_2\).
- This sharpens the previous logarithmic growth result into the form needed
  when cutoff increments are separated scale by scale.

## Mathematical Content

- With \(M_N=2^N\), define
  \[
    D_N=\{(p,q): |p|_\infty, |q|_\infty, |p+q|_\infty\leq 2^N\}.
  \]
- Positivity of the Fourier summand gives
  \(C_2(M_{N+1})-C_2(M_N)\geq0\).
- The dyadic annulus estimate from the logarithmic-growth proof gives the
  block contribution \(A_m2^{-|\ell-s|}\) for
  \(B_\ell\times B_s\).
- If \((p,q)\in D_{N+1}\setminus D_N\), then at least one of the two
  momentum scales is in the top three annuli:
  \[
    \max(\ell,s)\geq N-1,\qquad \ell,s\leq N+1.
  \]
  Otherwise both \(|p|_\infty\) and \(|q|_\infty\) are \(<2^{N-1}\), hence
  \(|p+q|_\infty<2^N\), contradicting shell membership.
- The remaining finite shell sum is bounded by
  \[
    \sum_{\substack{0\leq\ell,s\leq N+1\\\max(\ell,s)\geq N-1}}
    2^{-|\ell-s|}
    \leq 9.
  \]

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies the
  finite shell sum for a sample center scale and checks that it is bounded by
  \(9\).

## Remaining Issue #582 Obligations

- Use the local-coordinate estimates in the complete negative-sector BPHZ
  coordinate estimates.
- Prove nested and non-nested relative-scale bounds for the renormalized
  two-loop kernels.
- Verify the \(\Pi\)- and \(\Gamma\)-coordinate estimates needed by the
  random-model Cauchy theorem.
