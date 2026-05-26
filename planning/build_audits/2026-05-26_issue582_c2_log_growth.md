# 2026-05-26 Issue #582 C2 Log Growth

## Scope

- Volume XI, Chapter 9 now derives the sharp spatial Fourier-cutoff formula
  for the dynamic \(\Phi^4_3\) two-loop local coordinate \(C_2(M)\).
- The chapter proves matching logarithmic upper and lower ultraviolet growth
  bounds for this coordinate.

## Mathematical Content

- With \(a_n=|n|^2+m^2\), the retarded heat kernel and stationary covariance
  give
  \[
    C_2(M)=2(2\pi)^{-6}
    \sum_{|p|_\infty,|q|_\infty,|p+q|_\infty\leq M}
    \frac{1}{a_pa_q(a_p+a_q+a_{p+q})}.
  \]
- The upper bound uses dyadic annuli \(B_\ell\).  The contribution of
  \(B_\ell\times B_s\) is bounded by \(C_m2^{-|\ell-s|}\), and summing this
  over \(\ell,s\leq\lceil\log_2(1+M)\rceil\) gives \(O(\log M)\).
- The lower bound uses positive boxes \(P_\ell\) for
  \(2\leq \ell\leq\lfloor\log_2M\rfloor-2\).  Each block contributes a
  positive \(m\)-dependent constant, giving \(\Omega(\log M)\).

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies the
  finite dyadic sum of \(2^{-|\ell-s|}\), its diagonal lower bound, and the
  exact lower positive-box block factor \(2^{-12}\) for a sample scale.

## Remaining Issue #582 Obligations

- Turn the \(C_1\) and \(C_2\) Fourier-coordinate estimates into the complete
  negative-sector coordinate estimates for the BPHZ model.
- Prove the nested and non-nested relative-scale sector bounds for the
  renormalized two-loop kernels.
- Verify the \(\Pi\)- and \(\Gamma\)-coordinate estimates entering the
  random-model Cauchy theorem.
