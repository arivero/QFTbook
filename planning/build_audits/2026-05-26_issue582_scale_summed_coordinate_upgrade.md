# 2026-05-26 Issue #582 Scale-Summed Coordinate Upgrade

## Scope

- Volume XI, Chapter 9 now proves the scale-summed version of the dyadic-net
  coordinate supremum theorem.
- This theorem is the analytic form needed for model seminorms, where the
  testing scale \(\delta\simeq 2^{-m}\) ranges over all \(m\geq0\) and the
  parameter entropy grows with \(m\).

## Mathematical Content

- At physical scale \(m\), the base net and edge net sizes are assumed to
  obey
  \[
    |\mathcal X_{m,0}|\leq C_0 2^{Dm},\qquad
    |\mathcal E_{m,\ell}|\leq C_1 2^{Dm}2^{d\ell}.
  \]
- Coordinate moments carry a regularity slack:
  \[
    \mathbb E|Y_m(u)|^p\leq B_0^p2^{-p\sigma m},\qquad
    \mathbb E|Y_m(v)-Y_m(u)|^p
    \leq B^p2^{-p\sigma m}2^{-(d+\varepsilon)\ell}.
  \]
- Applying the fixed-scale dyadic-net theorem gives an \(L^p\) contribution
  at scale \(m\) proportional to
  \[
    2^{-(\sigma-D/p)m}.
  \]
- The all-scale supremum is controlled by summing this geometric series,
  which converges precisely when
  \[
    \sigma>D/p.
  \]
- The same proof carries a cutoff-increment factor \(2^{-\rho n}\) without
  changing the scale or net constants.

## Calculation Check

- `calculation-checks/constructive_scalar_spde_checks.py` now verifies an
  exact sample with \(p=2\), \(D=4\), \(\sigma=3\), and
  \(\varepsilon=2\):
  - the entropy slack \(\sigma-D/p=1\);
  - the fixed-scale constant \(27\);
  - the all-scale geometric constant \(54\);
  - the base entropy cancellation at \(m=5\);
  - cutoff factor propagation for \(\rho=2\), \(n=3\).

## Remaining Issue #582 Obligations

- Prove the actual coordinate moment and parameter-increment estimates for
  the dynamic \(\Phi^4_3\) \(\Pi\)- and \(\Gamma\)-coordinates in the finite
  negative-sector chart.
- Apply the scale-summed theorem and coordinate-to-model theorem to obtain
  the finite-sector random-model Cauchy estimate.
- Extend to the modelled-distribution solution sector and complete the
  SPDE-to-OS comparison.
