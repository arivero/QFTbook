# Chapter 14: Mirror TBA and the Y-System
Source-File: monograph/tex/volumes/volume_vii/chapter14_planar_n4_mirror_tba_y_system.tex

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
- `mathcal I`: mirror-TBA node set containing `bullet_Q`, `y_pm^(alpha)`,
  `(v|M)^(alpha)`, and `(w|M)^(alpha)` for wings `alpha=L,R`.
- `nu_L=+1`, `nu_R=-1`: wing signs for the fermionic mirror chemical
  potentials.
- `d_A`: mirror-TBA driving term `L tilde E_A-mu_A`; only `bullet_Q` carries
  length energy, while `y_pm^(alpha)` carries `nu_alpha pi i`.
- `K^sb_AB`: target-first stringbook kernel
  `(2 pi i)^{-1} partial_v log S^sb_AB(u,v)`, related to the chapter
  source kernel by `K^sb_AB(u,v)=-K_BA(v,u)`.
- `mathcal R_m`: constituent-shift set
  `{-(m-1)/2, ..., (m-1)/2}` for a fused mirror string.
- `Phi_mn^{bullet bullet}`: rational fused mirror `bullet_m`--`bullet_n`
  scattering phase in stringbook orientation.
- `Theta_mn^{bullet bullet}`: endpoint dressing-phase combination built from
  the analytically continued `chi(x,y)`.
- `S^{y_pm bullet}`, `S^{(v|m) bullet}`: fused auxiliary-to-bullet phases
  used to define the target-first mirror-TBA kernels.
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
- `mathcal A_l`: strip of meromorphy
  `-l/2 < Im u < l/2` after explicitly removing state source factors.
- `Y^bullet_n,Y^oplus,Y^ominus,Y^triangle_n,Y^circ_n`: stringbook
  Y-system nodes mapped to `Y_{n,0}`, `Y_{1,pm1}^{-1}`,
  `Y_{2,pm2}`, `Y_{n+1,pm1}^{-1}`, and `Y_{1,pm(n+1)}^{-1}`.
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
- Adds an explicit status boundary for mirror magnons: they are analytically
  continued worldsheet/spin-chain excitations inherited from the relativistic
  string worldsheet mirror channel, not ordinary four-dimensional local QFT
  asymptotic particles.
- Derives the mirror bound-state dispersion from double Wick rotation.
- Adds the sheet/branch status of physical versus mirror Zhukovsky variables.
- Adds and proves an explicit mirror Zhukovsky parametrization for real mirror
  momentum: `x_Q^+=r_Q xi_Q`, `x_Q^-=r_Q^{-1} xi_Q`,
  `xi_Q=(tilde p-i Q)/sqrt(Q^2+tilde p^2)`, including shortening,
  `log(x_Q^-/x_Q^+)=tilde E_Q`, the stringbook mirror momentum equation, and
  weak Boltzmann scaling `exp(-L tilde E_Q)=O(g^{2L})`.
- Cross-references the same sheet convention to the Chapter 15
  fermionic-node large-`u` QSC bridge, without duplicating that later
  derivation inside the mirror-kernel setup.
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
  `zeta(u_j)=-2 pi i(n_j+1/2)` before specializing to the finite-size
  Bethe-root regularity equations of the planar N=4 integrability framework.
- Proves the one-species excited-state contour-deformation signs by residues:
  a crossed zero of `1+Y` contributes `-log S(u,u_j)` to the TBA driving
  term and `+ i tilde p(u_j)` to the energy; inverse mirror continuation
  gives the physical root contribution `E(u_j)`.
- States the general mirror TBA equation with contours, kernels, chemical
  potentials, and signs as part of the data.
- Adds the multi-species mirror-TBA node/source inventory: maps the
  stringbook `oplus`, `ominus`, `M|yw`, and `M|w` symbols to
  `y_+`, `y_-`, `(v|M)`, and `(w|M)`, states the left/right fermion
  chemical potentials, proves the target-first/source-kernel bridge, and
  records the node-by-node source families including the reversed-root
  denominator signs for `ominus` and `w` sources.
- Adds the fused mirror-kernel formula crosswalk from the stringbook:
  defines the constituent shift set, displays the rational
  `bullet_m`--`bullet_n` phase, the endpoint dressing combination, the
  `y_pm`--`bullet` and `(v|m)`--`bullet` phases, their reciprocal target/source
  orientations, and the auxiliary double-sum kernel reduction to the closed
  fused `K_mn` expression.  The global analytic continuation of `chi` remains
  an explicit dressing-phase boundary, not a finite fusion claim.
- Gives the excited-state energy formula with wrapping integral.
- Adds a self-contained derivation of the `A_infinity` auxiliary-string kernel
  inverse in Fourier variables, including the fused kernel symbol and the
  one-index kernel identity.
- Derives the one-wing `n|w` Y-system relation from the mirror TBA by applying
  the kernel inverse and then the strip-analytic inverse of `s`.
- Proves the precise domain and failure mode of the `s`-kernel inverse: on a
  regular closed strip it is the shift operator, while boundary zero modes and
  shifted zero-pole factors carry exactly the source data that the local
  Y-system would otherwise forget.
- Defines the planar `N=4` bulk T-hook domain, with `T_{0,s}` adjoined as a
  gauge boundary, proves the local Hirota origin of the interior Y-system
  relation, and proves cancellation of the four-function T-gauge redundancy
  in `Y_{a,s}`.  Boundary-node modifications are separated from the interior
  algebra.
- Warns that Y-system equations alone do not define the spectrum.
- Proves the local shifted zero-pole source-factor identity
  `B_a^+ B_a^-=(u-a+i)/(u-a-i)`, explaining how contour and sheet data enter
  analytic Y-system equations as rational source factors.
- Adds explicit analytic Y-system data in the stringbook convention: the
  stringbook-to-T-hook node map, strip assumptions, first Zhukovsky
  branch-point lattice, central fermionic cut inversion
  `Y_{2,pm2,+}=1/Y_{1,pm1,-}`, source-factor recording rule, and exact-root
  regularity conditions inside the mirror-TBA framework.  The text states that
  global analytic continuation is
  an independent datum to be checked against the mirror sheet and dressing
  branch, not a consequence of local Hirota algebra or of literature authority.
- Adds a forward status pointer to the Chapter 15 TBA-to-QSC charge record:
  local Y-system ratios are separated from restored source data, the central
  fermionic large-`u` coefficient, `P`-power charge gaps, and the physical
  QSC root assignment.
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
- The same script checks the multi-species mirror-TBA node/source inventory:
  length-driving support only on `bullet_Q`, left/right fermion boundary
  phases, the `M=1` boundary in the `bullet_Q` equation, the
  target-first/source-kernel sign bridge, and the ratio signs from reversed
  `ominus` and `w` roots.
- The same script checks the fused mirror-kernel formula crosswalk: finite
  `bullet_m`--`bullet_n` rational unitarity, endpoint dressing antisymmetry
  for an antisymmetric mock `chi`, `y_-` as the inverse-sheet `y_+` formula,
  exact endpoint telescoping of the square-root packages, reciprocal auxiliary
  orientations, exact auxiliary pole-multiplicity reduction, and equality of
  the auxiliary double-sum derivative with the closed fused `K_mn` kernel.
- The same script checks the excited-state contour-deformation residue signs:
  source orientation `-log S`, product orientation, energy residue
  `+i tilde p`, and inverse mirror continuation to physical energy.
- The same script checks the auxiliary-wing TBA-to-Y-system kernel algebra:
  the fused `A_mn` Fourier symbol, tridiagonal inverse, `A^{-1}K` identities,
  `s^{-1}` shift symbol, and boundary-source algebra for the `n|w` Y-system.
- The same script checks the `s`-inverse data-loss mechanism: an explicit
  boundary zero mode, its closest strip-boundary poles, and the shifted
  zero-pole factor that leaves rational source memory.
- The same script checks the local analytic Y-system source factor
  `B_a^+B_a^-=(u-a+i)/(u-a-i)`, its inverse orientation, and finite products
  of shifted zero-pole sources.
- `calculation-checks/planar_n4_reader_companion_checks.py` and
  `calculation-checks/planar_n4_reader_companion_checks.wl` provide compact
  reader-facing checks of the Hirota-to-Y identities, shifted source factor,
  finite-grid mirror-TBA pseudoenergy/Y-form equivalence, and the
  `A_infinity` inverse symbol.
- The same script checks the analytic Y-system strip/cut bookkeeping:
  stringbook-to-T-hook node map, nearest branch-point lattice outside the open
  strip, integer central fermion cut shifts, central cut inversion, and finite
  source-power accounting.
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
