# 2026-05-30 Kallen-Lehmann Spectral Measure Proof Pass

## Scope

Anti-wrapper/proof-substance pass on Volume I, Chapter 9,
`chapter09_kallen_lehmann_spectral_representation_and_particle_content.tex`.

The proposition titled `Two-point spectral measure of a scalar field` is a
foundational statement and should remain theorem-family content, but its
earlier proof relied too directly on the formal vector
\(\widehat\phi(0)\vac\).  Since local fields are operator-valued
distributions, the literal Hilbert-space object is the smeared vector
\(\widehat\phi(f)\vac\), and the spectral measure is characterized by its
action on test functions.

## Changes

- Replaced the point-field definition of \(\nu_\phi(\Delta)\) by the precise
  characterization
  \[
    W_2(f)=\int\widetilde f(-p)\,\dd\nu_\phi(p)
  \]
  for Schwartz \(f\).
- Added the equivalent smeared inner-product formula
  \[
    \langle\widehat\phi(f)\vac,\widehat\phi(g)\vac\rangle
    =
    \int \overline{\widetilde f(p)}\widetilde g(p)\,\dd\nu_\phi(p).
  \]
- Identified the familiar expression
  \(\langle\vac|\widehat\phi(0)E(\Delta)\widehat\phi(0)|\vac\rangle\) as
  shorthand, not a literal vector-valued point-field definition.
- Rewrote the proof so positivity comes from Hilbert-space positivity of
  smeared fields, existence and uniqueness of the measure comes from the
  Bochner--Schwartz theorem for positive-type tempered distributions, support
  comes from the spectrum condition, and Lorentz invariance comes from
  uniqueness of the Fourier--Stieltjes measure.

## Status

The proposition survives the audit as genuine foundational content.  This
pass removes a point-field shortcut that would otherwise look more rigorous
than it actually was.
