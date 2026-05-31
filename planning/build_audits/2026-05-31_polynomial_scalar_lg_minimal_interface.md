# Polynomial Scalar LG Minimal-Model Interface Pass

Date: 2026-05-31

## Trigger

The stringbook Appendix K material on ordinary two-dimensional
Landau-Ginzburg scalar flows had not been incorporated with the monograph's
current rigor standard.  The relevant content is QFT-side, not string-side:
normal-ordered polynomial perturbations of the two-dimensional scalar field,
the contact-term equation of motion, and the expected relation to A-series
minimal models.

## Edits

- Added `Polynomial Scalar Landau--Ginzburg Interface` to Volume VI,
  Chapter 06.
- Defined the scalar covariance convention
  `C(x)=-kappa log(mu |x|)+C_smooth(x)` and the normal-ordered polynomial
  potential.
- Explained why Wick-polynomial collisions are locally integrable: products
  of Wick powers have only powers of logarithms, and
  `int_0^epsilon r |log r|^p dr` is finite.
- Derived the normal-ordered Schwinger-Dyson equation
  `partial barpartial varphi = pi kappa V'(varphi)` away from spectator
  insertions, with contact terms assigned to the source-extension scheme.
- For the even multicritical family, recorded the finite order-field quotient
  `1, varphi, ..., :varphi^{2m-4}:`, the equation-of-motion descendant power
  `2m-3`, and the `m-2` even tuning-ratio count.
- Kept the endpoint identification with `M(m,m+1)` as an RG construction
  problem requiring continuum-limit, stress-tensor, and local-operator
  matching.
- Updated the Volume VI Chapter 06 dossier, stringbook crosswalk, and
  calculation-check README.
- Extended `calculation-checks/integrable_rg_flow_checks.py` with the finite
  multicritical arithmetic ledger.

## Verification Plan

- Run the dedicated integrable RG-flow check.
- Run the standard text/proof/label/dossier audits and full monograph build
  before committing.

