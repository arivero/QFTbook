# Chapter 13: All-Loop Asymptotic Bethe Ansatz

## Source Position

This chapter follows the one-loop spin-chain construction and uses the
stringbook all-loop magnon-dispersion and asymptotic-Bethe-ansatz spine as a
source of integrability conventions.  The monograph argument remains a
QFT-side spectral problem: external string-theoretic comparisons are
motivational checks, not foundations.

## Notation Inventory

- `J`: vacuum R-charge or spin-chain length in the BMN vacuum.
- `h_stringbook`: stringbook integrability coupling, identified here with
  monograph `g=sqrt(lambda)/(4 pi)`.
- `P,K,H`: central charges in the centrally extended residual algebra.
- `x^pm`: Zhukovsky variables.
- `x(u)`: physical-branch Zhukovsky map with short cut `[-2g,2g]`.
- `gamma_cr`: right-endpoint crossing path on the shifted Zhukovsky
  `u`-surface.
- `q_r`: conserved magnon charges entering the dressing phase.
- `sigma`, `theta`: dressing factor and phase.
- `Xi_12`: stringbook-orientation rational scalar-crossing multiplier.
- `mathcal R_cr`: finite crossed-amplitude ratio `L_bar1 2/G_21` used to
  recover the scalar-crossing multiplier from the matrix channel.
- `mathsf C_1`: chosen first-magnon crossing continuation along `gamma_cr`.
- `mathcal M_{12}^{(2)}`: two-crossing scalar-branch displacement
  `Xi_12(1/x_1^pm,x_2^pm)/Xi_12(x_1^pm,x_2^pm)`.
- `mathcal F_{12}`: quotient of two scalar dressing branches, i.e. the CDD
  factor left undetermined by crossing and scalar unitarity.
- `chi(x,y)`: BES contour-integral kernel for the dressing phase.
- `mathcal L_g(z,w)`: logarithmic Gamma-function kernel inside the DHM
  double contour.
- `Delta(z,w)=z+z^{-1}-w-w^{-1}`: DHM Gamma-kernel pole-lattice coordinate.
- `chi_raw^{epsilon_x,epsilon_y}`: DHM unit-circle contour evaluated with
  the Cauchy kernels expanded in specified radial chambers.
- `Psi_x`, `Psi_y`, `mathcal C_g`: one-residue and double-residue contact
  corrections for local DHM sheet continuation in the stringbook orientation.
- `theta_raw^{-,+}`, `Delta_bar1 theta`: raw crossed-first-particle BES
  phase and its local residue correction.
- `S_mat`, `S_0`: matrix and scalar parts of the two-body magnon S-matrix.
- `S^{(1)}_{12}`, `mathcal S_{12}`: one-copy `su(2|2)_c` intertwiner and
  its unfixed common scalar in the stringbook dynamic spin-chain frame.
- `A_{12},...,L_{12}`: `su(2|2)_c` matrix S-matrix amplitudes.
- `d_{12}=x_2^- -x_1^+`, `n_{12}=x_2^+ -x_1^-`: generic row-chart
  denominators for the one-copy `su(2|2)_c` intertwiner.
- `beta_{12},...,ell_{12}`: row-reduced coefficients expressing
  `B_{12},...,L_{12}` as multiples of `A_{12}` in the generic
  intertwiner-rank certificate.
- `R^{BB}`, `R^{BF}`: finite boson-boson/fermion-fermion and mixed blocks
  used to check local matrix unitarity after factoring out `mathcal S_{12}`.
- `y,w`: level-II and level-III nested Bethe roots.
- `f(y,p)`, `S^{II,I}(y,p)`: one-defect nesting coefficient and the
  level-II/level-I scattering factor in the stringbook spin-chain basis.
- `v(y)=y+1/y`: rational rapidity entering level-II and level-III nested
  scattering.
- `M(y_1,y_2), N(y_1,y_2)`: `SU(2)`-invariant level-II matrix amplitudes.
- `gamma(w,y)`, `S^{III,II}(w,y)`: one-defect level-III coefficient and
  level-III/level-II scattering factor.
- `K^I,K^II,K^III`: nesting numbers for physical, level-II, and level-III
  excitations in one `su(2|2)_c` copy.
- `S_str`: string-basis nesting factor after absorbing half of the
  length-changing marker into bosons; this is a conventional integrability
  frame label, not a string-theory premise.
- `Z_L,Z,rho,rho_h`: ABA counting functions, occupied root density, and hole
  density used in the large-`L` finite-density limit.
- `K(u,v)`: phase-derivative kernel `(2 pi)^{-1} partial_u Theta(u,v)` in the
  ABA counting equation.
- `E_Q,p`: bound-state energy and momentum.
- `f(g)`: large-spin cusp scaling function.
- `hat sigma(t)`: Fourier-space BES inner-density fluctuation for the
  large-spin `SL(2)` root distribution.
- `K_0,K_dr,K_BES`: rational, dressing, and total BES kernels entering the
  large-spin scaling equation.
- `J_m`: Bessel function entering the signed-`t` Zhukovsky Fourier transform
  for `1/(x^pm)^m`.

## Claim Ledger

- Derives the magnon dispersion relation from the shortening condition and
  central charges.
- Adds a convention ledger aligning the chapter with the stringbook
  integrability convention and warning about reciprocal scalar-factor
  conventions in the literature.
- Adds BMN scaling as a normalization check rather than a proof input.
- Defines the Zhukovsky variables and charge conventions used in the ABA.
- Corrects and proves the Zhukovsky energy formula
  `H=1+2ig(1/x^+-1/x^-)`, including the physical branch and cut
  reciprocal relation.
- Defines the right-endpoint crossing path on the shifted Zhukovsky
  `u`-surface, with odd mod-two winding around `2g-i/2` for `x^+` and
  `2g+i/2` for `x^-`, and proves that this path sends
  `x^pm -> 1/x^pm`, inverts the momentum ratio, and flips the analytically
  continued energy.
- Separates the symmetry-fixed matrix part of the S-matrix from the scalar
  dressing factor, including the ten-amplitude one-copy intertwiner form.
- Adds the full stringbook `su(2|2)_c` ten-amplitude formulas in the dynamic
  spin-chain frame, defines the representation ratios
  `x^+=i d/b`, `x^-=-i a/c`, records the length-changing marker convention,
  and proves the highest-weight `Q` amplitude identity
  `A=(a_1/a_2)K+G=L+(a_2/a_1)H`.
- Adds a generic row-rank certificate for the one-copy `su(2|2)_c`
  intertwiner: after the dynamic-frame `Q` and `S` equations are reduced on
  the open set
  `x_1^pm x_2^pm d_12 n_12 a_1 a_2
  (x_1^-x_2^- -1)(x_1^+x_2^+ -1) != 0`, the nine equations
  `B=beta A`, ..., `L=ell A` have pivots in the nine non-`A` amplitude
  columns, so the generic solution space is one-dimensional and the choice
  `A=mathcal S_12 n_12/d_12` recovers the ten stringbook amplitudes.
- Defines the finite matrix blocks `R^{BB}` and `R^{BF}` and records their
  local analytic unitarity after the common one-copy scalar is factored out.
- Derives the stringbook scalar split
  `mathcal S_{12}=[(x_2^- -x_1^+)/(x_2^+-x_1^-)
  (1-1/(x_2^+x_1^-))/(1-1/(x_2^-x_1^+))]^{1/2} sigma_{12}` and checks that
  the compact `SU(2)` two-copy amplitude contains the expected rational
  factor times `sigma_{12}^2`.
- Adds the BES `chi(x,y)` contour-integral representation with its
  sheet-domain caveat.
- Adds the local DHM residue-continuation rule underlying the stringbook
  notebook's analytic continuation: crossing \(x\) inward subtracts the
  `z=x` residue, crossing \(y\) inward adds the corresponding `w=y`
  residue in the stringbook sign convention, and crossing both variables
  subtracts the double-residue contact term `i mathcal L_g(x,y)`, producing
  the notebook's final `-i mathcal L_g(x,y)` contribution.
- Derives the DHM Gamma-kernel pole lattice
  `Delta(z,w)=+/- i n/g`, `n>=1`, and states the corresponding admissibility
  hypotheses for one-residue, contact, and four-kernel crossed-BES
  continuations.  This makes explicit when local Cauchy residues are the only
  residues crossed.
- Applies the local DHM rule to the four-kernel BES phase for a crossed first
  particle, deriving the residue combination
  `-Psi(x1+,x2+)+Psi(x1+,x2-)+Psi(x1-,x2+)-Psi(x1-,x2-)` and explicitly
  separating this local contour algebra from the global Janik scalar
  monodromy.
- Proves dressing scalar unitarity in the charge-expansion domain:
  antisymmetry of `q_r(1)q_s(2)-q_s(1)q_r(2)` gives `theta_21=-theta_12` and
  hence `sigma_12 sigma_21=1`, while leaving crossing as separate monodromy
  data.
- Derives the weak-coupling DHM/BES coefficient extraction directly from the
  contour integral: expand the gamma-function logarithm, take the Laurent
  coefficient of `(z+z^{-1}-w-w^{-1})^N`, and obtain the residue formula for
  the order-`g^N` contribution to `c_{r,s}(g)`.
- Evaluates that Laurent coefficient in closed form by converting it to a
  two-variable Fourier coefficient of `(-4 sin A sin B)^N`; this gives the
  Gamma-function formula for `C^{(N)}_{r,s}` and its parity/support
  restrictions without hiding the step behind a citation.
- Corrects the convention-sensitive distinction between the coefficient order
  and the physical perturbative order: in the stringbook/DHM convention
  `c_{2,3}(g)=4 zeta(3) g^3-40 zeta(5) g^5+O(g^7)`, while the first weak
  dressing contribution to anomalous dimensions is order `g^6` because the
  charges contribute `q_2 q_3=O(g^3)`.
- Adds a dressing-phase status ledger: AFS, Hernandez-Lopez, crossing, BES,
  and the weak `c_{2,3}` onset.
- Adds the explicit crossing scalar-factor equation and warns that the
  crossing path winds around shifted Zhukovsky branch points rather than
  acting as a sheet-free substitution.
- Derives the crossing scalar convention algebra in the stringbook
  orientation: the common reciprocal literature convention is exactly the
  inverse rational multiplier, while the naive substitution
  `x_1^pm -> 1/x_1^pm` is not a convention-independent identity.  The
  genuine crossing equation remains a scalar-factor monodromy input.
- Ports the stringbook notebook's finite crossed-amplitude channel check:
  forming `L_bar1 2/G_21` with `S_21=S_12^{-1}` and substituting the
  stringbook scalar split recovers
  `sigma_bar1 2 sigma_12=Xi_12` in the positive square-root chamber; this
  explains the rational multiplier's matrix-channel origin while keeping the
  global scalar branch as separate analytic data.
- Derives the scalar crossing monodromy cocycle: if a scalar branch satisfies
  Janik crossing on two successive first-magnon crossing segments, then
  `sigma^{[gamma C_1 C_1]}_12/sigma^{[gamma]}_12 =
  Xi_12(1/x_1^pm,x_2^pm)/Xi_12(x_1^pm,x_2^pm)`, with the expanded rational
  double-crossing multiplier and the reciprocal-convention inverse stated
  explicitly.  Homotopy and minimal BES-branch uniqueness remain analytic
  inputs rather than finite algebra.
- Classifies the local CDD ambiguity left by crossing and scalar unitarity:
  the quotient `mathcal F=sigma'/sigma` must obey
  `mathcal F^{[gamma C_1]} mathcal F^{[gamma]}=1` and
  `mathcal F^{[gamma P]}_{21} mathcal F^{[gamma]}_{12}=1`; conversely any
  non-zero meromorphic factor with these two properties preserves the same
  scalar crossing multiplier and unitarity.  The text records the induced
  zero/pole propagation and makes explicit that the BES CDD-free branch is a
  minimality/analyticity choice, not a finite algebra consequence.
- States the BES/crossing scalar-factor input as a quoted theorem with its
  framework assumptions.
- Adds an explicit asymptotic Bethe-Yang regime assumption: the ABA is a
  long-chain quantization rule for fixed-magnon or controlled high-density
  root configurations as `L -> infinity`, with wrapping/mirror winding
  suppressed.  This is deliberately distinguished from thermodynamic Bethe
  ansatz.
- Adds and proves a finite-density ABA counting equation: from
  `L p(u_j)+sum Theta(u_j,u_k)=2 pi I_j`, empirical measures normalized by
  `1/L` converge to `rho(v) dv`, and the available-level density satisfies
  `rho+rho_h=Z'(u)/(2 pi)=p'(u)/(2 pi)+int K(u,v)rho(v)dv`.  The text states
  the branch/no-crossed-singularity hypotheses and emphasizes that this is
  still ABA, not mirror TBA.
- Gives the stringbook rank-one all-loop asymptotic Bethe equation and
  cyclicity in the `SL(2)`-vacuum orientation, rather than conflating it with
  the compact one-loop `SU(2)` chamber convention of Chapter 12.
- Proves the first single-defect nested Bethe step in the stringbook
  orientation: the mixed `su(2|2)_c` amplitude ratios imply
  `f(y,p)=a(p)/(y-x^+(p))` and
  `S^{II,I}(y,p)=(y-x^-(p))/(y-x^+(p))` by the two adjacent-transposition
  coefficient equations.
- Adds the two-defect level-II scattering datum: the `M,N` amplitudes, the
  `M+N=-1` ungraded fermion sign, the rational `M-N` eigenvalue, and the
  same-site `phi_2 Z^+` contact coefficient.
- Proves the single level-III nesting step from the `M,N` amplitudes after
  accounting for the fermionic exchange sign, deriving
  `S^{III,II}(w,y)=(w-v(y)-i/(2g))/(w-v(y)+i/(2g))`.
- Displays the level-III rational self-scattering factor following this
  nesting step.
- Proves the single-copy closed-chain nested Bethe-Yang equations by
  transporting level-I, level-II, and level-III excitations around their
  corresponding ZF chains; records the nesting numbers
  `K^I=N_1+N_2+N_3+N_4`, `K^II=2N_2+N_3+N_4`, and `K^III=N_2+N_4`.
- Adds a string-basis frame ledger for `S^{I,I}`, `S^{II,I}`,
  `S^{III,II}`, and `S^{III,III}`, and states the reciprocal auxiliary
  insertion for the alternative `SL(2)` vacuum nesting.
- Proves the weak-coupling reduction of the rank-one all-loop ABA:
  the physical outside branch gives
  `x^pm=(u+-i/2)/g-g/(u+-i/2)+O(g^3)`, the stringbook rational factor tends
  to the `SL(2)` phase `(u_j-u_k-i)/(u_j-u_k+i)`, its reciprocal gives the
  compact `SU(2)` phase of Chapter 12, and
  `H-1=2g^2/(u^2+1/4)+O(g^4)`.
- Expands the bound-state fusion block: constructs the `Q`-string endpoints,
  proves momentum and energy telescoping, derives the shortening dispersion,
  proves the level-II auxiliary-factor telescoping, and defines the fused
  `SL(2)` scalar product used in bound-state Bethe-Yang equations.  The
  remaining matrix-intertwiner projection and scalar-branch pole normalization
  are marked as boundary inputs rather than hidden in the endpoint algebra.
- Expands the one-loop `SL(2)` large-spin cusp derivation: states the
  noncompact one-loop Bethe equation, defines the scaled root density and
  resolvent, solves the one-cut Riemann-Hilbert problem with
  `G_0(z)=-i log((sqrt(4z^2-1)+i)/(sqrt(4z^2-1)-i))`, derives the density,
  and extracts `Delta-S-L=8g^2 log S+O(S^0 g^2,g^4)` from
  `G_0(i/(2S))`.
- Adds the all-loop large-spin BES bridge from the `SL(2)` ABA: states the
  fixed-twist/large-spin assumptions, defines the inner-density fluctuation
  `hat sigma(t)`, gives the rational and dressing BES kernels in the
  stringbook convention, proves the branch-sensitive Fourier transform of
  `1/(x^pm)^m`, and derives the BES integral equation for `hat sigma`.
- Corrects the Fourier-transform convention to keep the stringbook signed
  ratio `J_m(2gt)/t`; writing it as `J_m(2g|t|)/|t|` with the same lower
  sign loses the parity factor in the `x^-` transform.
- Defines the monograph scaling-function normalization
  `Delta-S-L=f(g) log S+O(S^0)` and derives
  `f(g)=8g^2-8 pi^2 g^4/3+88 pi^4 g^6/45+O(g^8)` from the BES equation,
  including the power-counting reason that the dressing kernel first affects
  the scaling function at order `g^8`.
- Records the strong-coupling BES status in the same normalization,
  `f(g)=4g-3 log(2)/pi+O(1/g)`, and warns that some Wilson-line conventions
  call half of this quantity `Gamma_cusp`.

## Figure Ledger

No figure is included in this pass.  A future figure should show physical and
crossed Zhukovsky sheets.

## Calculation Checks

- `calculation-checks/planar_n4_integrability_checks.py` verifies the
  central-extension dispersion identity and the weak-coupling expansion.
- The same script checks the Zhukovsky defining equation, large-`u`
  expansion, cut reciprocal boundary values, `x^pm` shortening relation, and
  corrected energy formula.
- It tracks the square-root branch of `x(u+i/2)` and `x(u-i/2)` around the
  shifted crossing endpoints, checking that the lower loop flips only `x^+`,
  the upper loop flips only `x^-`, and the combined crossing path flips both
  variables while preserving shortening, inverting momentum, and flipping the
  continued energy.
- It also checks the stringbook-orientation crossing RHS against its exact
  reciprocal convention and verifies, both on physical-branch samples and on
  an algebraic counterexample, that it is not invariant under a naive
  sheet-free `x -> 1/x` substitution.
- It checks the finite crossed-amplitude channel algebra from the stringbook
  notebook: the squared `L_bar1 2/G_21` ratio becomes one exactly when the
  scalar product uses `Xi_12`, the reciprocal multiplier fails, and the
  positive real chamber fixes the unsquared square-root branch.
- It checks the scalar crossing monodromy cocycle exactly: the sheet-shifted
  multiplier is different from the physical one, the double-crossing ratio is
  `Xi_12(1/x_1^pm,x_2^pm)/Xi_12(x_1^pm,x_2^pm)`, the expanded product agrees
  with that quotient, the two-step branch recursion reproduces it, and the
  reciprocal scalar convention inverts it.
- It checks the CDD quotient equations exactly: multiplying a scalar branch
  by a crossing-odd and swap-odd CDD factor preserves Janik crossing and
  scalar unitarity, leaves regular double crossing unchanged, fails if the
  CDD factor is crossing-even, and propagates divisor signs correctly under
  crossing, exchange, and double crossing.
- It checks dressing scalar unitarity by evaluating the antisymmetric charge
  expansion on physical-branch `x^pm` samples and verifying
  `theta_12+theta_21=0`, `sigma_12 sigma_21=1`, and the squared-factor
  version used in the `SU(2)` ABA.
- It checks the DHM weak dressing coefficients by Laurent-expanding the
  contour-integrand monomial `(z+z^{-1}-w-w^{-1})^N`, comparing the residue
  prefactors against the closed weak formula on an exact rectangular grid in
  `N,r,s`, verifying parity/minimal-order selection, and confirming that the
  first charge-dressed weak term scales as `g^6`.
- It checks the local DHM analytic-continuation residue bookkeeping on a
  finite Laurent model of the Gamma-kernel expansion, including the
  single-residue signs and the necessity/sign of the double-residue contact
  term.  The same check now verifies the crossed-first-particle four-kernel
  BES phase residue signs and confirms that reversing them does not restore
  the outside branch.
- It checks the DHM Gamma-kernel pole lattice: numerator and denominator
  Gamma singularities occur at `Delta=+/- i n/g`, explicit endpoint pole
  divisors can be realized by solving `x+1/x`, and representative admissible
  samples stay away from the finite pole lattice.
- It ports the local finite checks from the stringbook `su(2|2) spin
  chain.nb` notebook: the ten-amplitude formulas satisfy the
  highest-weight `Q` relation, the boson-boson/fermion-fermion and mixed
  finite blocks obey `R_12 R_21=1` after the common scalar is removed, and the
  stringbook scalar split reproduces the compact `SU(2)` rational factor.
- It checks the generic `su(2|2)_c` row-rank certificate exactly over the
  rationals: the nine row-chart equations have rank nine in the ten
  amplitudes, recover the displayed ten-amplitude formulas after fixing
  `A=mathcal S_12 n_12/d_12`, and preserve the two highest-weight `Q`
  relations.
- It checks the single level-II nesting step by evaluating the two local
  coefficient equations and their cleared polynomial identities for
  non-singular complex samples.
- It checks the two-defect level-II matrix eigenvalues and unitarity, the
  graded conversion of `M+N=-1` to trivial level-III vacuum scattering, the
  two level-III local coefficient equations, and their cleared rational
  identities.
- It checks closed-chain nesting frame conventions: string-basis level-I and
  level-II frame ratios, reciprocal `SU(2)`/`SL(2)` auxiliary factors,
  level-III inverse orientation, and the nesting-number bookkeeping.
- It checks the finite-density ABA counting normalization on a toy diagonal
  phase: the empirical measure is normalized by `1/L`, the limiting mass is
  `M/L`, and the level density is `Z'(u)/(2 pi)`.
- It checks the weak rank-one ABA orientation: physical-branch `x^pm`
  expansion, momentum ratio, anomalous-energy normalization, the stringbook
  `SL(2)` rational factor, and the reciprocal compact `SU(2)` phase.
- The same script now checks BMN scaling, bound-state dispersion, bound-state
  fusion telescoping, fused scalar-product indexing, and weak coefficient
  arithmetic relevant to cusp/Bremsstrahlung comparisons.
- It checks the one-loop `SL(2)` large-spin cusp resolvent: physical
  square-root branch normalization, derivative formula, discontinuity and
  positivity of the density, and extraction of the `8g^2 log S` term with
  the constant `4g^2 log 4`.
- It checks the signed-`t` Zhukovsky Fourier transform used in the BES
  bridge: exact Bessel recurrence, contour phase for the upper branch, lower
  branch conjugation, and the even-`m` parity failure of the absolute-value
  rewrite.
- It checks the weak BES scaling-function expansion: the `sigma_0` and
  `sigma_1` density coefficients, the Bose-integral coefficients
  `A_0=pi^2/24` and `A_1=-11 pi^4/360`, the resulting
  `8g^2-8 pi^2 g^4/3+88 pi^4 g^6/45` scaling function, and the `g^8`
  onset of the dressing-kernel contribution.

## External References Used In Current Pass

- Downloaded local study copies under
  `references/planar_n4_integrability/` for convention comparison only:
  Bajnok--Janik `0807.0399`, Arutyunov--Frolov `0901.1417` and `0903.0141`,
  and Arutyunov--Frolov--Suzuki `1002.1711`.
- The monograph text does not import a claim solely by citation.  The
  downloaded sources were used to check convention-sensitive wording about
  ABA, mirror branches, and wrapping assumptions against the stringbook spine.
