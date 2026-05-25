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
The detailed angular derivation is four-dimensional.  Any \(D>4\) logarithmic
power statement must be separated as a conditional Gegenbauer/angular-tube
generalization, not inferred from the displayed \(D=4\) Lehmann ellipse.
The chapter must also derive Watson's theorem for elastic form factors in the
same partial-wave normalization before using phase information in dispersion
relations.

The chapter must not present these statements as slogans. It must state the
hypotheses:

- four-dimensional massive local theory;
- stable lightest identical scalar external particles of mass \(m\);
- no massless channels;
- fixed physical \(s>4m^2\) for angular analyticity;
- fixed real \(t<0\) for the dispersion relation;
- polynomial boundedness when the contour at infinity is discarded;
- separate polynomial-boundedness domains: physical-region bounds, fixed-\(t\)
  cut-plane bounds, and angular-tube bounds at \(0<t<t_0\); the Froissart
  comparison uses the angular-tube estimate;
- \(\mathcal M(s,t)\) is a polynomial-growth holomorphic germ on the
  complexified on-shell invariant surface, with physical values and cut
  discontinuities understood as distributional boundary values in the topology
  fixed in the preceding analyticity chapter;
- for confining gauge theories, the external particles are stable
  gauge-invariant one-particle states in the physical Hilbert space, such as
  glueballs or hadrons, and the positive mass gap is an input to the bound
  rather than a conclusion of the scattering argument;
- separation between the conditional finite-subtraction bootstrap to two
  subtractions and the stronger Lukaszuk-Martin/Yndurain theorem-level input
  that supplies two subtractions without assuming finite subtractions first;
- conditional status of these analyticity and boundedness hypotheses, since
  only restricted versions are presently theorem-level consequences of robust
  axiom systems;
- possible pole terms are omitted only in the displayed clean formula and would
  be added as residues.
- for Watson's theorem: a one-channel elastic interval, a Hermitian local
  operator with the channel quantum numbers, real analyticity of the form
  factor, and the same \(S_A=1+2i\beta a_A\) normalization as the scattering
  partial waves.

## Symbol Inventory

- \(s,t,u\): mostly-plus Mandelstam invariants with \(s+t+u=4m^2\) for equal
  masses; physical \(s\)-channel scattering has \(t,u\le0\), while positive
  \(t\) in the Lehmann-ellipse discussion is a crossed-channel timelike
  invariant.
- \(x=\cos\theta=1+2t/(s-4m^2)\): angular variable.
- \(x_t(s)=(s+4m^2)/(s-4m^2)\): location of the two-particle \(t\)-channel threshold in the \(x\)-plane.
- \(t_0\): nearest positive-\(t\) singularity controlling the Lehmann ellipse at high energy.
- \(\gamma_s\): ellipse contour in the complex \(x\)-plane with foci \(\pm1\).
- \(P_\ell,Q_\ell\): Legendre polynomial and Legendre function of the second kind.
- \(S_\ell(s)\): identical-boson partial-wave \(S\)-matrix eigenvalue, even \(\ell\).
- \(\beta(s)=\sqrt{1-4m^2/s}=2p/\sqrt s\): two-body elastic kinematic factor,
  distinct from the Kallen--Lehmann spectral measure \(d\rho\).
- \(w_\ell(s)=1-\operatorname{Re}S_\ell(s)\): positive unitarity weight, \(0\le w_\ell\le2\).
- \(\sigma_{\mathrm{tot}}\): total cross section in this normalization.
- \(N\): number of subtractions.
- \(P_{N-1}(s;t)\): subtraction polynomial.
- \(\lambda=(D-3)/2\): Gegenbauer index in \(D\) spacetime dimensions.
- \(C_\ell^\lambda(x)\): Gegenbauer polynomial replacing \(P_\ell(x)\) for
  \(D>4\).
- \(g_\ell^{(D)}\): degree-\(\ell\) spherical-harmonic degeneracy on
  \(S^{D-2}\), growing as \(O(\ell^{D-3})\).
- \(A\): collective channel label for Watson's theorem, including internal
  quantum numbers and angular momentum.
- \(\mathcal F_A^\pm(s)\): upper/lower boundary values of the
  vacuum-to-two-particle partial-wave form factor.
- \(\delta_A(s)\): elastic phase shift defined by
  \(S_A(s)=e^{2i\delta_A(s)}\).
- \(\Omega_A(s)\): Omnes function with boundary phase \(\delta_A(s)\).

## Claim Ledger

1. The physical angular interval is \(-1\le x\le1\). Crossed-channel singularities lie outside this interval for \(s>4m^2\).
2. Analyticity in a neighborhood of \([-1,1]\) gives an ellipse with foci \(\pm1\), the Lehmann ellipse.
3. Cauchy's formula and the \(P_\ell Q_\ell\) kernel expansion imply convergence of the partial-wave expansion inside this ellipse.
   The text should record both the \([-1,1]\) integral definition of \(Q_\ell\)
   and the \(\zeta\)-integral representation used to see exponential
   large-\(\ell\) decay.
4. In the identical scalar convention used here,
   \[
     \mathcal A(s,x)=-16\pi i\beta(s)^{-1}\sum_{\ell\ even}(2\ell+1)(S_\ell-1)P_\ell(x),
   \]
   where \(\beta(s)=\sqrt{1-4m^2/s}\).
5. For real \(x\) inside the ellipse,
   \[
     \operatorname{Im}\mathcal A(s,x)=16\pi\beta^{-1}\sum_{\ell\ even}(2\ell+1)P_\ell(x)(1-\operatorname{Re}S_\ell).
   \]
6. Unitarity gives \(0\le1-\operatorname{Re}S_\ell\le2\).
7. The optical theorem is
   \[
     \sigma_{\mathrm{tot}}=(s(s-4m^2))^{-1/2}\operatorname{Im}\mathcal A(s,1).
   \]
8. A box-profile comparison and Legendre lower bound at \(x>1\) give the Froissart-Martin mechanism.
9. Polynomial boundedness at the ellipse edge yields \(\sigma_{\mathrm{tot}}\lesssim (4\pi/t_0)\log^2s\), with constants depending on the precise boundedness exponent until the two-subtraction refinement is invoked.
   The bound here is an angular-tube bound at \(x=1+2t/(s-4m^2)>1\), distinct
   from physical real-angle bounds and from fixed-\(t<0\) cut-plane bounds.
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
14. The \(D>4\) estimate \(\sigma_{\mathrm{tot}}\le C(\log s)^{D-2}\) is a
    separate conditional statement: assume a higher-dimensional angular tube
    whose Gegenbauer coefficients decay like
    \(\exp[-\ell\eta_*(s)]\), then combine unitarity with
    \(\sum_{\ell\le L}g_\ell^{(D)}=O(L^{D-2})\).
15. For confining gauge theories satisfying the massive hypotheses, the
    Froissart amplitude is the amplitude between gauge-invariant hadronic or
    glueball asymptotic states.  Four-dimensional pure Yang--Mills requires a
    separately supplied positive mass gap and construction of the corresponding
    physical Hilbert space.
16. In a one-channel elastic interval, unitarity gives the form-factor
    discontinuity
    \[
      \mathcal F_A^+-\mathcal F_A^-
      =
      2i\beta a_A^*\mathcal F_A^+ .
    \]
    With \(a_A=e^{i\delta_A}\sin\delta_A/\beta\) and
    \(\mathcal F_A^-=(\mathcal F_A^+)^*\), this gives
    \(\mathcal F_A^+=e^{2i\delta_A}\mathcal F_A^-\), hence
    \(e^{-i\delta_A}\mathcal F_A^+\in\mathbb R\).
17. For the standard two-pion examples, the isovector vector form factor has
    phase \(\delta^1_1\) and the isoscalar scalar form factor has phase
    \(\delta^0_0\) below the first inelastic threshold in the corresponding
    channel.
18. The Omnes representation requires additional analyticity, zero/pole, and
    growth hypotheses beyond Watson's theorem.  Watson fixes the elastic-cut
    boundary phase; it does not determine the full form factor by itself.

## Figure Requirements

- Complex \(x\)-plane with physical interval, crossed-channel cuts, possible bound-state poles, and Lehmann ellipse.
- Partial-wave profile showing positive weights and the box comparison.
- Fixed-\(t\) dispersion contour with right and left cuts and subtraction circles.
- Elastic form-factor cut diagram showing upper/lower boundary values,
  scattering phase \(S_A=e^{2i\delta_A}\), and the rotated real form factor.
- Effective-radius schematic for the \(D\)-dimensional scaling
  \(\sigma_{\mathrm{tot}}\asymp R_{\mathrm{eff}}^{D-2}\), explicitly marked
  as a restatement of the conditional higher-dimensional bound rather than an
  additional assumption.

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
- 2026-05-24 issue pass: separated the \(D=4\) Lehmann-ellipse derivation from
  the \(D>4\) Gegenbauer/angular-tube generalization and added the degeneracy
  counting needed for the \((\log s)^{D-2}\) power.
- 2026-05-24 issue pass: separated physical-region, fixed-\(t\) cut-plane, and
  angular-tube polynomial bounds; the Froissart comparison now explicitly uses
  the angular-tube bound.
- 2026-05-24 issue pass: added the confining-gauge-theory scope of the bound:
  external states are gauge-invariant hadrons or glueballs, and the
  Yang--Mills mass gap is a separate input/open construction problem.
- 2026-05-24 issue #511 pass: the Froissart--Martin theorem proof now derives
  the \(4\pi/t_0\) and \((1-\delta)^{-2}\) coefficients from the box-profile
  lower bound, \(W=(s-4m^2)\sigma_{\rm tot}/(16\pi)\), the
  \(y-1=2(1-\delta)\sqrt{t_*/s}+O(s^{-1})\) angular-distance estimate, and the
  angular-tube polynomial upper bound at
  \(x_*(s)=1+2t_*/(s-4m^2)\).  The proof spends an auxiliary Legendre margin
  \(\delta_0<\delta\) to obtain the displayed coefficient without hiding an
  \(\varepsilon\) loss in the logarithmic scale.
- 2026-05-24 issue #390 pass: split the forward absorptive estimate into
  the optical-theorem inequality
  \(\operatorname{Im}\mathcal M(s,0)\ge
  \sqrt{s(s-4m^2)}\,\sigma_{\rm el}(s)\) and a separate equality chain for
  \(\sigma_{\rm el}\), so the final \(L^2\) integral is explicitly a lower
  bound, not an equality with the total absorptive part.
- 2026-05-24 issue #425 pass: renamed the partial-wave kinematic factor from
  \(\rho(s)\) to \(\beta(s)\), keeping \(\rho\) exclusively for spectral
  measures and densities.
- 2026-05-24 issue #435 pass: linked the chapter's \(s,t,u\) variables to the
  part-wide mostly-plus Mandelstam convention and made the physical
  \(s\)-channel sign \(t\le0\) distinct from positive crossed-channel
  singularities.
- 2026-05-25 issue #453 pass: added Watson's theorem for elastic form factors
  after the partial-wave normalization.  The manuscript now states the
  one-channel elastic hypotheses, derives the form-factor discontinuity
  \(\mathcal F_A^+-\mathcal F_A^-=2i\beta a_A^*\mathcal F_A^+\), obtains the
  phase relation \(\mathcal F_A^+=e^{2i\delta_A}\mathcal F_A^-\), records the
  two-pion vector and scalar examples, gives the coupled-channel matrix
  replacement, and separates the Omnes construction from Watson's theorem by
  listing the extra analyticity, zero/pole, and growth inputs.
