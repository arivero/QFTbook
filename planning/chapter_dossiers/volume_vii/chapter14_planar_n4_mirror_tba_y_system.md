# Chapter 14: Mirror TBA and the Y-System

## Source Position

This chapter follows the asymptotic Bethe ansatz and develops the finite-size
mirror-TBA and Y-system framework needed for wrapping interactions.

## Notation Inventory

- `E,p`: physical magnon energy and momentum.
- `tilde E, tilde p`: mirror energy and momentum.
- `x_Q^pm`: bound-state Zhukovsky variables.
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
- `Y_{a,s}`: T-hook Y-system variables.
- `u_j`: exact physical Bethe roots in excited-state TBA.
- `T_{a,s}`: Hirota T-functions.
- `Z_0^\vee`: mirror-sheet cut locus when inherited from the stringbook
  convention.

## Claim Ledger

- Defines the mirror transformation and emphasizes the non-relativistic
  difference from two-dimensional relativistic integrable QFT.
- Derives the mirror bound-state dispersion from double Wick rotation.
- Adds the sheet/branch status of physical versus mirror Zhukovsky variables.
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
- States the general mirror TBA equation with contours, kernels, chemical
  potentials, and signs as part of the data.
- Gives the excited-state energy formula with wrapping integral.
- States the T-hook Y-system relation, derives its local Hirota origin, and
  warns that Y-system equations alone do not define the spectrum.
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
- Displays the weak asymptotic `Y_Q^{(0)}(u)` used for Konishi, the change of
  variables `q=2u`, the real-line rational integral `I_Q`, the residue
  summand, the exact telescoper for the non-zeta rational part, and the final
  `324 + 864 zeta(3) - 1440 zeta(5)` coefficient.

## Figure Ledger

No figure is included in this pass.  A future figure should show the T-hook
node domain.

## Calculation Checks

- `calculation-checks/planar_n4_integrability_checks.py` verifies a local
  Hirota-to-Y-system algebra identity.
- The same script verifies the mirror double-Wick dispersion identity.
- The same script checks the mirror auxiliary-string derivation: the
  one-particle modulus identity, inside/outside support signs, `M|yw`
  pole/zero positions, and pure `w`-string spacings.
- The same script checks the one-species mirror-TBA variational algebra on a
  finite grid: constrained entropy variation, stationarity of the grand
  functional, free-energy identity, source-kernel sign conversion, and the
  excited-state zero condition.
- The same script verifies Konishi four-loop wrapping coefficient arithmetic,
  the stringbook `u`-integrand to `q=2u` rational-integrand conversion,
  numerical real-line integrals for the first four mirror charges, and the
  exact telescoping identity for the rational non-zeta tail.

## External References Used In Current Pass

- Stringbook anchors:
  `/Users/xiyin/ResearchIdeas/stringbook/texsource/string notes.tex`,
  especially the mirror Bethe-string derivation, mirror TBA/Konishi block
  around the weak `Y_{n,0}` formula, and wrapping integral.
- Stringbook notebook anchor:
  `/Users/xiyin/ResearchIdeas/stringbook/codes/mirror TBA and wrapping corrections.nb`.
- Downloaded local study copies under
  `references/planar_n4_integrability/`: Bajnok--Janik `0807.0399` for the
  displayed post-residue per-`Q` summand and telescoping target,
  Arutyunov--Frolov `0901.1417`/`0903.0141` for mirror branch and TBA
  assumption checks, and Arutyunov--Frolov--Suzuki `1002.1711` for
  weak-Konishi mirror-TBA normalization comparison.
- The monograph presents the finite rational integral and telescoping
  derivation explicitly; the external TeX sources are convention checks and
  source anchors, not replacements for the derivation.
