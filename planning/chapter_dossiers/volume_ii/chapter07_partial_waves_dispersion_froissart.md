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
relations.  It must also include the high-energy small-angle development that
uses the same partial-wave normalization: the impact-parameter limit, eikonal
unitarity, exponentiation of leading ladder and crossed-ladder exchange under
explicit eikonal hypotheses, and the Sommerfeld--Watson/Regge-pole
organization of fixed-\(t\) high-energy amplitudes.

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
- \(\langle s\rangle=(1+s^2)^{1/2}\): polynomial weight used in the
  fixed-\(t\) Schwartz seminorm.
- \(p_{r,N}(\varphi)\): Schwartz seminorm controlling a tempered fixed-\(t\)
  boundary distribution.
- \(\varphi_{R,\Delta}\): translated energy packet centered at \(R\) and of
  width \(\Delta\), used to express distributional high-energy growth.
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
- \(q=\sqrt{-t}\): transverse momentum transfer in the small-angle
  high-energy limit.
- \(b=(\ell+\frac12)/p\): impact parameter associated with large angular
  momentum \(\ell\), where \(p=\frac12\sqrt{s-4m^2}\).
- \(S(s,b)\): impact-parameter elastic \(S\)-matrix envelope obtained as the
  weak large-\(\ell\) limit of \(S_\ell(s)\).
- \(\Gamma(s,b)=1-S(s,b)\): impact-parameter profile function.
- \(\chi(s,b)\): eikonal phase, with \(\operatorname{Im}\chi\ge0\) encoding
  \(|S|\le1\) when \(S=\exp(i\chi)\).
- \(\chi_1(s,b)\): leading Born eikonal phase, the two-dimensional Fourier
  transform of \(\mathcal M_{\rm Born}/(2s)\).
- \(z_t=1+2s/(t-4m^2)\): crossed \(t\)-channel angular variable used in the
  Sommerfeld--Watson representation.
- \(\tau=\pm1\): Regge signature, projecting even or odd angular momentum.
- \(a_\tau(J,t)\): signature-projected partial wave analytically continued to
  complex angular momentum \(J\).
- \(\alpha(t)\): Regge trajectory, the location of a complex-\(J\) pole.
- \(r_\tau(t)\), \(\mathfrak r_\tau(t)\): partial-wave and high-energy Regge
  residues.
- \(\eta_\tau(\alpha)=(1+\tau e^{-i\pi\alpha})/\sin\pi\alpha\): Regge
  signature factor.

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
10a. Tempered fixed-\(t\) LSZ boundary values imply polynomial growth only
    after smearing with Schwartz energy packets:
    \[
      |\langle\mathcal M_t,\varphi_{R,\Delta}\rangle|
      \le C_{\varphi,t}(1+|R|+\Delta)^{N_t}.
    \]
    This is the direct consequence of Wightman temperedness; pointwise
    cut-plane bounds and angular-tube bounds require additional analyticity
    and boundary-regularity input.
10b. Temperedness alone cannot imply pointwise polynomial bounds.  The
    chapter constructs a smooth nonnegative \(L^1\) function
    \[
      f(s)=\sum_{n\ge1} e^{n^2}\psi(e^{3n^2}(s-n))
    \]
    which defines a tempered distribution but has
    \(f(n)\ge e^{n^2}\).  This proves that the Jin--Martin pointwise upgrade
    needs genuine analytic machinery and cannot be replaced by an appeal to
    Wightman temperedness.
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
19. In the high-energy small-angle limit, the ordered partial-wave expansion
    has the impact-parameter form
    \[
      \mathcal M_{\rm ord}(s,-q^2)
      =
      2is\int d^2b\,e^{iq\cdot b}\Gamma(s,b)+o(s),
      \qquad \Gamma=1-S,
    \]
    where \(S(s,b)\) is the weak large-\(\ell\) envelope of \(S_\ell(s)\).
20. Impact-parameter unitarity is the pointwise identity
    \(2\operatorname{Re}\Gamma=|\Gamma|^2+1-|S|^2\), giving
    \(\sigma_{\rm tot}=2\int d^2b\,\operatorname{Re}\Gamma\),
    \(\sigma_{\rm el}=\int d^2b\,|\Gamma|^2\), and
    \(\sigma_{\rm inel}=\int d^2b(1-|S|^2)\) at leading high energy.
21. If \(S=\exp(i\chi)\), the leading eikonal phase is fixed by the Born
    amplitude:
    \[
      \chi_1(s,b)=\frac1{2s}\int\frac{d^2Q}{(2\pi)^2}
      e^{-iQ\cdot b}\mathcal M_{\rm Born}(s,-Q^2).
    \]
22. Under the stated eikonal-propagator and integrable-remainder hypotheses,
    the sum of \(n\)-rung ladder and crossed-ladder graphs gives
    \(2is\int d^2b\,e^{iq\cdot b}[-(i\chi_1)^n/n!]\), hence the exponent
    \(1-e^{i\chi_1}\).
23. Regge theory requires an additional complex-angular-momentum hypothesis:
    the signature partial waves \(a_\tau(J,t)\) must be meromorphic with
    sufficient vertical-strip decrease.  The Sommerfeld--Watson contour then
    reproduces the integer-spin partial-wave sum by residues.
24. A simple Regge pole \(a_\tau(J,t)=r_\tau(t)/(J-\alpha(t))+\cdots\)
    contributes
    \[
      \mathcal M_\tau^{\rm pole}(s,t)
      =
      \eta_\tau(\alpha(t))\mathfrak r_\tau(t)
      (s/s_0(t))^{\alpha(t)}(1+O(s^{-1})).
    \]
    If \(\alpha(M_n^2)=n\) with the correct signature, the same pole gives
    the usual spin-\(n\) exchanged-particle pole in the crossed channel.
25. A single uncompensated Pomeron pole with \(\alpha_P(0)>1\) cannot be the
    full asymptotic answer under the massive Froissart--Martin hypotheses.
    Eikonal saturation of a phase behaving as \(s^\Delta e^{-\mu b}\) gives a
    radius \(R(s)\sim(\Delta/\mu)\log s\), explaining how area growth becomes
    compatible with a \(\log^2s\) bound once the analyticity hypotheses are
    also imposed.

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
- Eikonal impact-parameter schematic showing fast lines, exchanged quanta,
  \(b=(\ell+\frac12)/p\), and \(S(b)=e^{i\chi(b)}\).
- Complex-\(J\) Sommerfeld--Watson/Regge schematic showing integer-spin
  poles, deformed contour, Regge pole \(J=\alpha(t)\), and the resulting
  \(s^{\alpha(t)}\) contribution.

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
- 2026-05-25 issue #457 pass: added the high-energy small-angle section.  It
  derives the impact-parameter representation from the large-\(\ell\)
  partial-wave limit, states the exact impact-parameter unitarity identities,
  defines the eikonal phase and its Born transform, proves leading ladder plus
  crossed-ladder exponentiation through eikonal propagators/Wilson-line
  ordering, and develops the Sommerfeld--Watson Regge-pole representation with
  signature factors, particle-pole recovery, and the relation between Pomeron
  growth, eikonal saturation, and Froissart behavior.
- 2026-05-25 issue #495 pass: added the self-contained tempered-distribution
  proof of distributional polynomial growth for fixed-\(t\) LSZ boundary
  values, including the Schwartz seminorm bound and translated energy-packet
  estimate.  The text now states precisely that this is the boundedness
  supplied immediately by Wightman temperedness, while Jin--Martin pointwise
  cut-plane boundedness and angular-tube boundedness are stronger inputs.
- 2026-05-26 issue #495 pass: added the smooth \(L^1\) spike construction
  proving that temperedness alone does not imply pointwise polynomial
  boundedness of any chosen representative.  This pins down the logical gap
  that the Jin--Martin/Jost--Lehmann--Dyson/Bros--Epstein--Glaser analytic
  machinery must close.
