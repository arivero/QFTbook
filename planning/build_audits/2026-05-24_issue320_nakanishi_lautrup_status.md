# Issue #320 Audit: Nakanishi--Lautrup Integration Status

## Scope

- GitHub issue: `#320`, asking whether the Nakanishi--Lautrup field \(B^a\)
  is integrated over or kept as an external auxiliary field.
- Manuscript files checked:
  - `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`
  - `monograph/tex/volumes/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.tex`

## Resolution

- The BRST/Faddeev--Popov chapter now states immediately after the
  delta-functional representation that \(B_A\) is an integrated auxiliary
  variable, not an external background field or physical degree of freedom.
- The covariant-gauge section now displays the fixed-regulator Gaussian
  \(B\)-integral and its result:
  \[
    \int[DB]\,
    \exp\left\{
    i\int\left(B^a\partial^\mu A_\mu^a+
    {g_{\rm YM}^2\xi\over2}B^aB^a\right)
    \right\}
    =
    {\cal N}_B(\xi)
    \exp\left\{
    -{i\over2g_{\rm YM}^2\xi}
    \int(\partial^\mu A_\mu^a)^2
    \right\}.
  \]
- The BV chapter now states that \((\bar c^a,B^a)\) belongs to the nonminimal
  integration sector and that \(B^a\) is Gaussian-integrated after restriction
  to the gauge-fixing Lagrangian submanifold.
- Chapter dossiers were updated so later development keeps the same convention.

## Convention Check

- The signs match the manuscript's Minkowski convention
  \(\mathcal L_{\rm gf+gh}=B\,\partial A+(g_{\rm YM}^2\xi/2)B^2-\bar c\,
  \partial D c\).  Completing the square gives
  \(B^a=-(g_{\rm YM}^2\xi)^{-1}\partial^\mu A_\mu^a\) and hence
  \(\mathcal L_{\rm gf}=-(2g_{\rm YM}^2\xi)^{-1}(\partial A)^2\).
- The normalization \({\cal N}_B(\xi)\) is field independent and therefore
  cancels from normalized correlators.
