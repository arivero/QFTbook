# u-Plane Wall-Normal Factor Pass

Date: 2026-05-31.

Scope:
- `monograph/tex/volumes/volume_viii/chapter08_witten_donaldson_seiberg_witten_comparison.tex`
- `calculation-checks/donaldson_sw_comparison_checks.py`
- `planning/chapter_dossiers/volume_viii/chapter08_witten_donaldson_seiberg_witten_comparison.md`

Purpose:
The Donaldson-Seiberg-Witten chapter already separated the full QFT
comparison theorem from the mathematical finite-dimensional Donaldson and
Seiberg-Witten invariants, but the \(u\)-plane wall-crossing paragraph still
compressed the local analytic source of the chamber jump.  This pass exposes
the wall-normal part of the Siegel-Narain theta kernel at the point of use.

Substantive changes:
- Introduced \(x_\lambda(\omega)=\langle\lambda,\omega\rangle\) for the
  normal coordinate to a reducible wall.
- Wrote the local completed-sign model
  \(E_t(x)=\operatorname{erf}(\sqrt{\pi t}\,x)\).
- Derived
  \[
    \frac{dE_t}{dx}=2\sqrt t\,\exp(-\pi t x^2)
  \]
  and the total jump
  \[
    \int_{-\infty}^{\infty}2\sqrt t\,e^{-\pi t x^2}\,dx=2.
  \]
- Clarified that flux sectors away from \(x_\lambda=0\) are smooth in the
  chamber period ray, while the wall jump is supported on the reducible-flux
  wall.
- Updated the conditional \(u\)-plane wall-crossing discussion to cite this
  local analytic model before invoking the remaining global determinant-line,
  singular-fiber, contact-term, and Wilsonian hypotheses.
- Added exact coefficient checks for the sign-factor jump and the
  delta-sequence concentration scale.

Remaining boundary:
This is a local analytic mechanism, not a proof of the full Donaldson-SW QFT
comparison.  The latter still requires construction of the twisted continuum
theory, \(Q\)-compatible Wilsonian flow, \(u\)-plane measure factors,
singular-fiber monopole replacement, contact terms, and determinant phases.
