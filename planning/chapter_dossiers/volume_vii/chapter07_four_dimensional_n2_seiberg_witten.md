# Chapter 07: Four-Dimensional N=2 Gauge Dynamics And Seiberg-Witten Theory

## Source Position

Volume VII proceeds from four-dimensional `N=1` holomorphic dynamics to the
first `N=2` exact low-energy gauge-theory structure.  The chapter is placed
before moduli-space, lower-dimensional supersymmetric examples, and
localization so that special geometry, BPS central charges, and Abelian
Wilsonian dynamics are available for later use.

## Notation Inventory

- `G`, `g`, `r`: compact gauge group, Lie algebra, and rank.
- `phi`, `u_k`: vector-multiplet scalar and gauge-invariant Coulomb
  coordinates.
- `a^I`, `a_{D,I}`, `F(a)`, `tau_IJ`: special coordinates, dual periods,
  prepotential, and Abelian coupling matrix.
- `gamma=(n_m^I,n_{e,I})`, `Z_gamma`: electromagnetic charge and central
  charge.
- `Sigma_u`, `lambda_SW`, `A_I`, `B^I`: Seiberg-Witten curve, differential,
  and symplectic cycle basis.
- `M_{Lambda^2}`, `M_{-Lambda^2}`, `M_infty`: monodromy matrices in the
  pure gauge-algebra `su(2)` example.
- `M_gamma`: Picard-Lefschetz monodromy associated to a massless
  hypermultiplet of charge `gamma=(n_m,n_e)`.
- `a_D^(m)`: local dual period branch that vanishes at the monopole point.
- `c_-`: nonzero local slope of the dyonic vanishing period at
  `u=-Lambda^2`.

## Claim Ledger

- Defines Coulomb-branch coordinates and repeats the monograph gauge-coupling
  convention at the first use of `N=2` gauge dynamics.
- Defines special coordinates, the prepotential, electric-magnetic duality,
  and the BPS central charge.
- Proves local existence of the prepotential from symmetry of the period
  coupling.
- Derives the weak-coupling monodromy at infinity from the one-loop
  prepotential and the Weyl action `a -> -a`.
- Derives the finite monodromies from Picard-Lefschetz transformations for
  charges `(1,0)` and `(1,-1)`, and checks their product gives
  `M_infty`.
- Derives the pure `su(2)` curve
  `y^2=(x^2-Lambda^4)(x-u)` from the two finite singularities, the residual
  `u -> -u` action, nodal-fiber monodromy, and the weak-coupling cusp.
- Displays hypergeometric representatives for the electric period and the
  monopole-vanishing dual period, and states the Picard-Fuchs equation
  `(u^2-Lambda^4) Pi'' + Pi/4 = 0`.
- Computes the monopole mass near `u=Lambda^2`:
  `M_(1,0)=|u-Lambda^2|/(sqrt(2)|Lambda|)+O(|u-Lambda^2|^2)`.
- Identifies the dyonic vanishing central charge `a_D-a` at `u=-Lambda^2`
  and records its linear mass behavior.
- States the weak-coupling BPS tower `(1,n)`, the vector multiplet `(0,1)`,
  the strong-coupling chamber with only `(1,0)` and `(1,-1)` hypermultiplets,
  and the marginal-stability wall condition.
- Records the theorem boundary for turning Seiberg-Witten dynamics into a
  nonperturbative construction of four-dimensional supersymmetric QFT.

## Calculation Checks

- `calculation-checks/sw_su2_periods.py` verifies the monodromy matrices, the
  finite-monodromy product, the Picard-Fuchs equation for the displayed
  hypergeometric periods, the large-\(u\) asymptotic of \(a(u)\), logarithmic
  growth of \(a_D(u)\), and linear vanishing of \(a_D\) at the monopole point.

## Figure Ledger

No figure is included in this pass.  Future figures should include the
two-singularity \(u\)-plane with monodromy loops and a branch-cut picture of
the elliptic curve cycle degeneration.
