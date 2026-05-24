# Volume II, Chapter 7 Dossier: Partial Waves, Dispersion Relations, and High-Energy Bounds

## Source Position

- Primary local source: second-sequence handwritten/transcribed material, pages 41--55.
- Reader-facing chapter follows immediately after analyticity, crossing, and Landau singularities.
- Role in the monograph: derive consequences of analyticity, crossing, mass gap, and partial-wave unitarity before renormalization begins.

## Construction Task

This chapter should explain how angular analyticity gives a Lehmann ellipse,
how partial-wave unitarity turns positivity into an angular-momentum cutoff,
how polynomial boundedness gives the Froissart-Martin logarithmic bound, and
how fixed-\(t\) dispersion relations with subtractions arise.

The chapter must not present these statements as slogans. It must state the
hypotheses:

- four-dimensional massive local theory;
- stable lightest identical scalar external particles of mass \(m\);
- no massless channels;
- fixed physical \(s>4m^2\) for angular analyticity;
- fixed real \(t<0\) for the dispersion relation;
- polynomial boundedness when the contour at infinity is discarded;
- separation between the conditional finite-subtraction bootstrap to two
  subtractions and the stronger Lukaszuk-Martin/Yndurain theorem-level input
  that supplies two subtractions without assuming finite subtractions first;
- conditional status of these analyticity and boundedness hypotheses, since
  only restricted versions are presently theorem-level consequences of robust
  axiom systems;
- possible pole terms are omitted only in the displayed clean formula and would
  be added as residues.

## Symbol Inventory

- \(s,t,u\): Mandelstam invariants with \(s+t+u=4m^2\) for equal masses.
- \(x=\cos\theta=1+2t/(s-4m^2)\): angular variable.
- \(x_t(s)=(s+4m^2)/(s-4m^2)\): location of the two-particle \(t\)-channel threshold in the \(x\)-plane.
- \(t_0\): nearest positive-\(t\) singularity controlling the Lehmann ellipse at high energy.
- \(\gamma_s\): ellipse contour in the complex \(x\)-plane with foci \(\pm1\).
- \(P_\ell,Q_\ell\): Legendre polynomial and Legendre function of the second kind.
- \(S_\ell(s)\): identical-boson partial-wave \(S\)-matrix eigenvalue, even \(\ell\).
- \(w_\ell(s)=1-\operatorname{Re}S_\ell(s)\): positive unitarity weight, \(0\le w_\ell\le2\).
- \(\sigma_{\mathrm{tot}}\): total cross section in this normalization.
- \(N\): number of subtractions.
- \(P_{N-1}(s;t)\): subtraction polynomial.

## Claim Ledger

1. The physical angular interval is \(-1\le x\le1\). Crossed-channel singularities lie outside this interval for \(s>4m^2\).
2. Analyticity in a neighborhood of \([-1,1]\) gives an ellipse with foci \(\pm1\), the Lehmann ellipse.
3. Cauchy's formula and the \(P_\ell Q_\ell\) kernel expansion imply convergence of the partial-wave expansion inside this ellipse.
   The text should record both the \([-1,1]\) integral definition of \(Q_\ell\)
   and the \(\zeta\)-integral representation used to see exponential
   large-\(\ell\) decay.
4. In the identical scalar convention used here,
   \[
     \mathcal A(s,x)=-16\pi i\rho(s)^{-1}\sum_{\ell\ even}(2\ell+1)(S_\ell-1)P_\ell(x),
   \]
   where \(\rho(s)=\sqrt{1-4m^2/s}\).
5. For real \(x\) inside the ellipse,
   \[
     \operatorname{Im}\mathcal A(s,x)=16\pi\rho^{-1}\sum_{\ell\ even}(2\ell+1)P_\ell(x)(1-\operatorname{Re}S_\ell).
   \]
6. Unitarity gives \(0\le1-\operatorname{Re}S_\ell\le2\).
7. The optical theorem is
   \[
     \sigma_{\mathrm{tot}}=(s(s-4m^2))^{-1/2}\operatorname{Im}\mathcal A(s,1).
   \]
8. A box-profile comparison and Legendre lower bound at \(x>1\) give the Froissart-Martin mechanism.
9. Polynomial boundedness at the ellipse edge yields \(\sigma_{\mathrm{tot}}\lesssim (4\pi/t_0)\log^2s\), with constants depending on the precise boundedness exponent until the two-subtraction refinement is invoked.
10. Fixed-\(t\) polynomial boundedness gives an \(N\)-subtracted dispersion relation with a subtraction polynomial and cut integrals.
    The compact right/left-cut formula should be accompanied by the explicit
    \(s'\)- and crossed \(u'\)-channel version, with \(u=4m^2-s-t\).
11. The subtraction-count argument uses the positive elastic unitarity integral
    \[
      \operatorname{Im}\mathcal A(s,0)\ge
      \frac{1}{32\pi\sqrt{s(s-4m^2)}}\int_{-(s-4m^2)}^0
      dt\,|\mathcal A(s,t)|^2,
    \]
    and distinguishes fixed-\(t\) uniformity from stronger fixed-angle
    uniformity.
12. Conditional subtraction-count statement: if a fixed-\(t\) dispersion
    representation with some finite subtraction number exists, Froissart plus
    positivity of absorptive derivatives reduces the genuine subtraction count
    to two in the massive scalar setting.
13. Stronger theorem-level input: the Lukaszuk-Martin/Yndurain result supplies
    the missing axiomatic step, namely two subtractions without an independent
    finite-subtraction premise.  The chapter must cite it and must not conflate
    it with the conditional bootstrap.

## Figure Requirements

- Complex \(x\)-plane with physical interval, crossed-channel cuts, possible bound-state poles, and Lehmann ellipse.
- Partial-wave profile showing positive weights and the box comparison.
- Fixed-\(t\) dispersion contour with right and left cuts and subtraction circles.
- Effective-radius schematic for the \(D\)-dimensional scaling
  \(\sigma_{\mathrm{tot}}\asymp R_{\mathrm{eff}}^{D-2}\), explicitly marked
  as a restatement of the bound rather than an additional assumption.

## Audit Notes

- Avoid reader-facing references to source pages or course numbers.
- Avoid negative framing as a main section. Caveats about massless particles and gravity belong in a final scope paragraph.
- Ensure all nonstandard symbols are defined before use.
- 2026-05-22 source pass: handwritten pp. 41--55 checked against the chapter;
  missing \(Q_\ell\) representation, explicit crossed dispersion form,
  unitarity/subtraction details, and effective-radius figure were added.
- 2026-05-24 issue pass: separated the conditional bootstrap to \(N=2\) from
  the stronger Lukaszuk-Martin/Yndurain two-subtraction theorem and recorded
  the citations in the chapter.
