# 2026-06-01 Issue #630 PDF Moment Light-Ray Pass

Scope: Volume II, Chapter 19, PDF/DGLAP rigor uplift.

Change made:
- Added a local-moment extraction paragraph after the renormalized quark and
  gluon light-ray PDF definitions.
- Derived the left-endpoint Taylor expansion of the Wilson-line bilocal from
  the transporter differential equation.
- Fixed the sign convention for the forward quark moment operator as
  `bar q (-i Dleft_n)^N gamma.n q`; this sign is forced by the free-target
  phase `exp(i lambda P.n)` in the chapter's Fourier convention.
- Recorded the gluon moment-index shift caused by the conventional `1/x` in
  the gluon PDF definition: the `N`-th moment uses `N-1` left covariant
  derivatives.
- Clarified that symmetric traceless local tensors are a local-coordinate
  presentation of the same leading-twist tower, while off-forward total
  derivatives are retained in the GPD polynomiality section.

Calculation check:
- Extended `calculation-checks/qcd_dglap_checks.py` with exact rational
  complex-phase bookkeeping for the quark and gluon light-ray moment
  conventions.

Issue status:
- This closes a concrete PDF/light-ray moment-normalization gap in #630.
- #630 remains open because it is a comprehensive QCD rigor-uplift umbrella:
  continuum factorization, stronger Glauber/SCET theorems, JIMWLK limits,
  confinement diagnostics, and other QCD clusters remain.
