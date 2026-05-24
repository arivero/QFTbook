# Issue #331 Ising Scaling-Function Universality Pass

Date: 2026-05-24

## Files Touched

- `monograph/tex/volumes/volume_iii/chapter01_fixed_points_and_conformal_data.tex`
- `planning/chapter_dossiers/volume_iii/chapter01_fixed_points_conformal_data.md`

## Mathematical Point

The CFT opening chapter now defines universal Ising scaling functions as
separated-point continuum limits of normalized lattice observables after:

- analytic changes from microscopic couplings to relevant scaling coordinates;
- multiplicative normalization of scaling fields;
- subtraction of analytic background terms in the free energy.

The text also states which quantities are regulator data rather than universal
scaling functions: critical temperatures, lattice metric factors, field
normalizations, analytic backgrounds, and contact-term extensions.

## Conditional Determination Statement

The new proposition states a conditional theorem:

- if the regulator class has a continuum critical limit identified with a
  unitary Ising CFT;
- if spin and energy observables converge to \(\sigma\) and \(\varepsilon\);
- if the CFT OPE converges as a distribution on separated configurations;

then the critical separated-point scaling functions are determined by the
complete CFT data: primary spectrum, spins, \(\mathbb Z_2\) parity, two-point
normalizations, and OPE coefficients.  The proof uses convergent OPE
expansions on configuration-space charts and crossing/associativity on
overlaps.

For off-critical scaling functions, the manuscript now states that the
relevantly deformed continuum theory is additional input.  Conformal
perturbation theory near the critical point uses complete CFT data plus a
renormalized contact-term chart, while global massive scaling functions are
correlators of the deformed continuum theory.

## Numerical Status

The status remark now records that the \(D=3\) values
\(\Delta_\sigma=0.518148806(24)\) and
\(\Delta_\varepsilon=1.41262528(29)\) are numerical conformal-bootstrap
estimates for the candidate CFT.  Their parenthetical uncertainties are not
lattice-spacing convergence rates and are not rigorous errors for a
constructive lattice-to-CFT theorem.
