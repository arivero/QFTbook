# 2026-06-06 Issue #597 Primed Determinant Remainder Repair

## Trigger

- Fresh #597 review observed that
  `ca:instanton-primed-determinant-source-response` wrote an exactly linear
  determinant equality while the operator family still contained an
  unspecified `O(epsilon^3)` Hessian perturbation.
- The previous linear log-series tail bound controlled only
  `Tr log(1 + epsilon G R)`, not the determinant contribution of a nonlinear
  operator-family term.

## Repair

- Rewrote the block so the displayed determinant equality is explicitly for
  the retained exactly linear determinant coordinate
  `K_lin(epsilon)=K + epsilon R`.
- Added the full-family case
  `K_full(epsilon)=K + epsilon R + epsilon^3 T(epsilon)`.
- Added the separate operator-family remainder
  `R_op = -1/2 Tr' log(1 + (1+X)^{-1}Y)` and its finite-norm bound.
- Stated the Dirac analogue without the bosonic `1/2` factor.

## Companion Evidence

- Extended `check_primed_determinant_source_response()` with a nonzero cubic
  operator perturbation.
- The check verifies that:
  - the old exactly-linear tail bound does not bound the cubic operator
    response;
  - the linear tail plus the new operator-family bound does bound it;
  - the perturbation remains inside the finite resolvent domain.

## Scope

- This is a logical-gap repair in the fluctuation/determinant part of the
  instanton amplitude calculation.
- It does not compute the continuum determinant constant and does not add
  moduli-space geometry.
