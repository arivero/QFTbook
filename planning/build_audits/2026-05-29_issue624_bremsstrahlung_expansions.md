# Issue #624: Bremsstrahlung Function Expansions

## Scope

This pass deepens the Wilson-line cusp/Bremsstrahlung part of Volume VII,
Chapter 15.  The exact planar formula was already present; this pass derives
its weak- and strong-coupling consequences from the Bessel ratio so that the
normalizations are explicit and checkable.

## Manuscript Changes

- Added the weak/strong Bremsstrahlung expansion derivation to
  `monograph/tex/volumes/volume_vii/chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`.
- Starting from

  `B(lambda)=sqrt(lambda) I_2(sqrt(lambda))/(4 pi^2 I_1(sqrt(lambda)))`,

  derived

  `B(lambda)=lambda/(16 pi^2)-lambda^2/(384 pi^2)
  +lambda^3/(6144 pi^2)-lambda^4/(92160 pi^2)+O(lambda^5)`.

- Converted the same weak series to the spectral-problem coupling
  `g=sqrt(lambda)/(4 pi)`:

  `B(g)=g^2-(2 pi^2/3)g^4+(2 pi^4/3)g^6
  -(32 pi^6/45)g^8+O(g^10)`.

- Derived the strong expansion from the large-positive-`z` asymptotics of
  modified Bessel functions:

  `B(lambda)=sqrt(lambda)/(4 pi^2)-3/(8 pi^2)
  +3/(32 pi^2 sqrt(lambda))+3/(32 pi^2 lambda)
  +63/(512 pi^2 lambda^(3/2))+O(lambda^(-2))`.

- Clarified that this is a near-BPS generalized-cusp datum, while the
  lightlike cusp and large-spin scaling function are different analytic
  limits of cusp data.

## Calculation Check

- Extended `check_bremsstrahlung_weak_series()` in
  `calculation-checks/planar_n4_integrability_checks.py` so it verifies:
  - the exact weak Bessel-series division through the four displayed orders;
  - the large-`z` modified-Bessel ratio
    `I_2/I_1=1-3/(2z)+3/(8z^2)+3/(8z^3)+63/(128z^4)+...`;
  - the displayed strong Bremsstrahlung coefficients through
    `lambda^{-3/2}`.

## Remaining Issue #624 Items

Bremsstrahlung weak/strong normalization is now developed from the exact
Wilson-loop formula.  Remaining #624 items include strong-coupling BES depth
beyond the status line, classical finite-gap/Pohlmeyer material, four-loop
Konishi wrapping depth, and a rigorous TBA/QSC comparison.
