# Chapter 14: Mirror TBA and the Y-System

## Source Position

This chapter follows the asymptotic Bethe ansatz and develops the finite-size
mirror-TBA and Y-system framework needed for wrapping interactions.

## Notation Inventory

- `E,p`: physical magnon energy and momentum.
- `tilde E, tilde p`: mirror energy and momentum.
- `x_Q^pm`: bound-state Zhukovsky variables.
- `R_Q,r_Q,xi_Q`: real mirror-momentum parameters used to put
  `x_Q^+` inside and `x_Q^-` outside the unit circle in the stringbook mirror
  sheet convention.
- `bullet_Q,y_pm,(v|M),(w|M)`: mirror node families.
- `eta=i/(2g)`: auxiliary mirror-string half-spacing.
- `v(y)=y+1/y`: auxiliary rapidity in the one-wing mirror Bethe-Yang
  subsystem.
- `F(y)`: product of level-I mirror scattering factors controlling whether
  a level-II root lies inside, outside, or on the unit `y`-circle.
- `epsilon_A`, `Y_A`: mirror pseudoenergies and Y-functions.
- `K_BA`: mirror scattering kernel.
- `rho_p,rho_L,rho_h`: one-species mirror particle, level, and hole
  densities used in the statistical-mechanical derivation of TBA.
- `K^dens(v,u)`: target-derivative density kernel
  `(2 pi i)^{-1} partial_u log S(v,u)` before conversion to the chapter's
  source-derivative kernel convention.
- `zeta`: one-species pseudoenergy satisfying
  `rho_p/rho_L=(1+exp zeta)^{-1}`.
- `K_n,K_mn,A_mn`: rational auxiliary-string kernels and the fused
  `A_infinity` string kernel used in the TBA-to-Y-system inversion.
- `s(u)=1/(2 cosh pi u)`: kernel whose inverse is represented by
  `f(u+i/2)+f(u-i/2)` under the stated strip analyticity assumptions.
- `Y_n^circ,Y^oplus,Y^ominus`: one-wing `n|w` and two-sheet `y` Y-functions
  used to derive the auxiliary-wing Y-system.
- `Y_{a,s}`: T-hook Y-system variables.
- `B_alpha(u)=(u-alpha+i/2)/(u-alpha-i/2)`: elementary shifted zero-pole source
  factor whose shifted product supplies a local analytic Y-system source.
- `u_j`: exact physical Bethe roots in excited-state TBA.
- `T_{a,s}`: Hirota T-functions.
- `Z_0^\vee`: mirror-sheet cut locus when inherited from the stringbook
  convention.

## Claim Ledger

- Defines the mirror transformation and emphasizes the non-relativistic
  difference from two-dimensional relativistic integrable QFT, using the
  stringbook sign convention `E=i tilde p`, `p=i tilde E`.
- Derives the mirror bound-state dispersion from double Wick rotation.
- Adds the sheet/branch status of physical versus mirror Zhukovsky variables.
- Adds and proves an explicit mirror Zhukovsky parametrization for real mirror
  momentum: `x_Q^+=r_Q xi_Q`, `x_Q^-=r_Q^{-1} xi_Q`,
  `xi_Q=(tilde p-i Q)/sqrt(Q^2+tilde p^2)`, including shortening,
  `log(x_Q^-/x_Q^+)=tilde E_Q`, the stringbook mirror momentum equation, and
  weak Boltzmann scaling `exp(-L tilde E_Q)=O(g^{2L})`.
- Defines a mirror-kernel datum as the scattering factor together with source
  and target contours, and adds the mirror Bethe-string node inventory.
- Adds the one-wing mirror auxiliary Bethe-Yang subsystem in the stringbook
  mirror orientation, including the mirror fermion boundary-condition sign.
- Proves the mirror-sheet modulus lemma for the level-II/level-I factor:
  elementary `y` roots are supported on `|y|=1` in the thermodynamic limit.
- Derives the pole-cancellation arrays for `(v|M)`/`M|yw` strings and pure
  `(w|M)` strings, with the real-center condition labeled as string-
  hypothesis input rather than a four-dimensional QFT theorem.
- Adds a self-contained one-species mirror-TBA derivation from the logarithmic
  Bethe-Yang equation, including the density equation, Fermi level-statistics
  entropy, constrained free-energy variation, pseudoenergy equation, and
  ground-state energy formula.
- Makes explicit the convention bridge to the stringbook: the density
  derivation uses a target-derivative kernel, while the chapter's multi-species
  equation uses source-derivative kernels; diagonal unitarity accounts for the
  resulting minus sign.
- Records the one-species excited-state defect source and the zero condition
  `zeta(u_j)=-2 pi i(n_j+1/2)` before specializing to exact physical Bethe
  roots in planar N=4.
- Proves the one-species excited-state contour-deformation signs by residues:
  a crossed zero of `1+Y` contributes `-log S(u,u_j)` to the TBA driving
  term and `+ i tilde p(u_j)` to the energy; inverse mirror continuation
  gives the physical root contribution `E(u_j)`.
- States the general mirror TBA equation with contours, kernels, chemical
  potentials, and signs as part of the data.
- Gives the excited-state energy formula with wrapping integral.
- Adds a self-contained derivation of the `A_infinity` auxiliary-string kernel
  inverse in Fourier variables, including the fused kernel symbol and the
  one-index kernel identity.
- Derives the one-wing `n|w` Y-system relation from the mirror TBA by applying
  the kernel inverse and then the strip-analytic inverse of `s`.
- Defines the planar `N=4` bulk T-hook domain, with `T_{0,s}` adjoined as a
  gauge boundary, proves the local Hirota origin of the interior Y-system
  relation, and proves cancellation of the four-function T-gauge redundancy
  in `Y_{a,s}`.  Boundary-node modifications are separated from the interior
  algebra.
- Warns that Y-system equations alone do not define the spectrum.
- Proves the local shifted zero-pole source-factor identity
  `B_a^+ B_a^-=(u-a+i)/(u-a-i)`, explaining how contour and sheet data enter
  analytic Y-system equations as rational source factors.
- Adds analytic Y-system data: shifted strips, meromorphy domains,
  discontinuities, and exact-root regularity conditions.
- Uses Konishi as the first wrapping test and separates finite-length
  correction from magnon-dispersion correction.
- Adds the weak-coupling Konishi root expansion and ABA coefficient.
- Adds a leading-Konishi-mirror-input assumption isolating the one-loop roots,
  antisymmetric mirror `SL(2)` bound-state sector, weak mirror Zhukovsky
  branch, leading dressing-phase status, and absence of a weak-coupling
  `mu`-term.
- Derives the leading mirror momentum measure
  `d tilde p_Q/du = 2 + O(g^2)` from the stringbook branch convention.
- Proves the algebraic rationalization of the weak Konishi mirror density:
  after `q=2u` and `u_*=1/(2 sqrt 3)`, the four physical-root factors combine
  into the two quartics `B_Q^-` and `B_Q^+`, giving the displayed rational
  `Y_Q^(0)(q/2)` integrand without relying on the Mathematica notebook as a
  black box.
- Proves the pole structure of the rational Konishi weak density used in the
  residue computation: the exact paired-root factorizations of `B_Q^-` and
  `B_Q^+`, the full cancellation of the apparent `Q=1` real poles at
  `q=+-1/sqrt(3)`, the absence of real contour poles after this cancellation,
  and the `q^{-12}` large-rapidity decay.
- Derives the residue reduction for the per-charge Konishi wrapping summand:
  the fourth-order residue at `q=iQ` is written as a third derivative of the
  regular part, the simple residues at `q=+-1/sqrt(3)+i(Q+-1)` are expressed
  with the explicit derivative of the vanishing quartic factor, and the
  resulting arithmetic in `Q(sqrt(3), i)` is reduced to the displayed rational
  summand `R_Q+864/Q^3-1440/Q^5`.
- Displays the weak asymptotic `Y_Q^{(0)}(u)` used for Konishi, the change of
  variables `q=2u`, the real-line rational integral `I_Q`, the residue
  summand, the exact telescoper for the non-zeta rational part, and the final
  `324 + 864 zeta(3) - 1440 zeta(5)` coefficient.

## Figure Ledger

No figure is included in this pass.  A future figure should show the T-hook
node domain.

## Calculation Checks

- `calculation-checks/planar_n4_integrability_checks.py` verifies the local
  Hirota-to-Y-system algebra: the `1+Y` and `1+1/Y` identities, the full
  interior T-hook Y-system product relation, Hirota covariance under the
  four-function T-gauge, and exact cancellation of T-gauge factors in
  `Y_{a,s}`.
- The same script verifies the mirror double-Wick dispersion identity.
- The same script verifies the mirror Zhukovsky sheet parametrization, including
  inside/outside status, shortening, stringbook mirror-momentum sign, and weak
  Boltzmann scaling.
- The same script checks the mirror auxiliary-string derivation: the
  one-particle modulus identity, inside/outside support signs, `M|yw`
  pole/zero positions, and pure `w`-string spacings.
- The same script checks the one-species mirror-TBA variational algebra on a
  finite grid: constrained entropy variation, stationarity of the grand
  functional, free-energy identity, source-kernel sign conversion, and the
  excited-state zero condition.
- The same script checks the excited-state contour-deformation residue signs:
  source orientation `-log S`, product orientation, energy residue
  `+i tilde p`, and inverse mirror continuation to physical energy.
- The same script checks the auxiliary-wing TBA-to-Y-system kernel algebra:
  the fused `A_mn` Fourier symbol, tridiagonal inverse, `A^{-1}K` identities,
  `s^{-1}` shift symbol, and boundary-source algebra for the `n|w` Y-system.
- The same script checks the local analytic Y-system source factor
  `B_a^+B_a^-=(u-a+i)/(u-a-i)`, its inverse orientation, and finite products
  of shifted zero-pole sources.
- The same script verifies Konishi four-loop wrapping coefficient arithmetic,
  the exact weak-density rationalization behind the `q=2u` integrand, the
  exact paired-root factorization of the Konishi quartics, the `Q=1`
  removable-pole cancellation, the `q^{-12}` large-rapidity leading-power
  check, exact symbolic Laurent extraction of the fourth-order and simple
  upper-half-plane residues, the stringbook `u`-integrand to
  rational-integrand conversion, numerical real-line integrals for the first
  four mirror charges, and the exact telescoping identity for the rational
  non-zeta tail.

## External References Used In Current Pass

- Stringbook anchors:
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`,
  especially the mirror Bethe-string derivation, mirror TBA/Konishi block
  around the weak `Y_{n,0}` formula, and wrapping integral.
- Stringbook notebook anchor:
  `/Users/xiyin/PhysicsLogic/references/stringbook/Code repository/mirror TBA and wrapping corrections.nb`.
- Scope boundary: `string` in `Bethe string`, `mirror string`, or
  `stringbook` is integrability/source terminology here.  No string-theoretic
  construction is used as a premise for the QFT TBA/Y-system claims.
- Downloaded local study copies under
  `references/planar_n4_integrability/`: Bajnok--Janik `0807.0399` for the
  displayed post-residue per-`Q` summand and telescoping target,
  Arutyunov--Frolov `0901.1417`/`0903.0141` for mirror branch and TBA
  assumption checks, and Arutyunov--Frolov--Suzuki `1002.1711` for
  weak-Konishi mirror-TBA normalization comparison.
- The monograph presents the finite rational integral and telescoping
  derivation explicitly; the external TeX sources are convention checks and
  source anchors, not replacements for the derivation.
