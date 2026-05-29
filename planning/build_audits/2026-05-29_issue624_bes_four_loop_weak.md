# Issue #624: Weak BES Scaling Function Through First Dressing Term

## Scope

This pass deepens the all-loop cusp/BES part of Volume VII, Chapter 13.  The
target is the first weak-coupling coefficient where the dressing phase affects
the large-spin scaling function.  The calculation is carried out inside the
chapter's BES normalization rather than imported as a coefficient table.

## Manuscript Changes

- Extended Proposition `prop:planar-n4-bes-weak-scaling-function` from
  `O(g^6)` to the `g^8` term:

  `f(g)=8g^2-8 pi^2 g^4/3+88 pi^4 g^6/45
  -(584 pi^6/315+64 zeta(3)^2)g^8+O(g^10)`.

- Added the small-`g` kernel expansion
  `K_0(2gt,2gt')=1/2-g^2(t^2-t t'+t'^2)/4+O(g^4)`.
- Added the first dressing source
  `K_dr(2gt,0;g)=2 zeta(3) g^4 t+O(g^6)`, derived from
  `c_{2,3}(g)=4 zeta(3)g^3+O(g^5)` and `J_2(2gt)`.
- Derived the inner-density coefficient

  `sigma_2(t)=t/(e^t-1)(t^4/24+pi^2 t^2/12+zeta(3)t+11 pi^4/90)`.

- Evaluated

  `A_2=int (sigma_2/2 - t^2 sigma_1/4 + t^4 sigma_0/24) dt
       =73 pi^6/2520+zeta(3)^2`,

  which gives the displayed `g^8` scaling-function coefficient.

## Calculation Check

- Extended `calculation-checks/planar_n4_integrability_checks.py` so
  `check_bes_weak_scaling_function()` verifies:
  - the `sigma_2` moment algebra;
  - `A_2=73 pi^6/2520+zeta(3)^2`;
  - the resulting `g^8` coefficient
    `-(584 pi^6/315+64 zeta(3)^2)`.

## Remaining Issue #624 Items

The weak BES expansion is now developed through the first
dressing-sensitive term.  Remaining items include strong-coupling BES depth,
Bremsstrahlung integration with the Wilson-line material, classical
finite-gap/Pohlmeyer material, four-loop Konishi wrapping depth, and a
rigorous TBA/QSC comparison.
