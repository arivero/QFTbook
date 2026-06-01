# Glauber remainder diagnostic pass

Date: 2026-06-01.

Issue context: GitHub #526 and #630, modern jet-substructure and QCD
factorization rigor.

## Scope

Volume II, Chapter 19b already contained a finite Glauber unitarity diagnostic:
inclusive or commuting measurements are unchanged by a finite Glauber unitary,
while noncommuting measurements can detect the rotation.  This pass adds the
missing quantitative layer.  The goal is not to prove continuum QCD
factorization, but to make the finite algebraic quantity that a continuum
proof must bound completely explicit.

## Manuscript changes

- Defined
  \[
    \Delta_G(M,\rho)=
    \operatorname{Tr}(MU_G\rho U_G^\dagger)-\operatorname{Tr}(M\rho).
  \]
- Used cyclicity to derive
  \[
    \Delta_G(M,\rho)=
    \operatorname{Tr}((U_G^\dagger M U_G-M)\rho).
  \]
- Added the operator/trace-norm estimate
  \[
    |\Delta_G(M,\rho)|\le
    \|U_G^\dagger M U_G-M\|\,\|\rho\|_1.
  \]
- Added the Duhamel commutator representation for \(U_G=\exp(\ii K_G)\),
  isolating \([M,K_G]\) as the finite obstruction coordinate.

## Calculation check

`calculation-checks/scet_factorization_checks.py` now verifies, with exact
rational matrices, the cyclic remainder identity and a finite Hilbert--Schmidt
Cauchy--Schwarz bound for a noncommuting measurement.

This narrows the SCET/Glauber rigor gap in #526/#630.  It remains a finite
diagnostic only: the continuum task still requires identifying the regulated
Glauber region, controlling the eikonal and contour-deformation steps, and
bounding the corresponding smeared-cross-section remainder.
