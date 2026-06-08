# Chapter 11: Hydrodynamic Fluctuations And Long-Time Tails
Source-File: monograph/tex/volumes/volume_x/chapter11_hydrodynamic_fluctuations_long_time_tails.tex

## Source Position

This chapter completes the first Volume X pass through hydrodynamics by
developing the stochastic and Schwinger-Keldysh fluctuation layer after the
deterministic Ward-identity chapter, the SK hydrodynamic-action chapter, and
the nonequilibrium/open-system chapter.  It now also connects the finite
empirical-flow level-\(2.5\) construction of Chapter 10 to the Gaussian
current cost used in fluctuating hydrodynamics, keeping the finite
contraction exact and the continuum macroscopic-fluctuation functional
explicitly conditional on a hydrodynamic scaling limit.

## Notation Inventory

- `d`: number of spatial dimensions in \(\mathbb R_t\times\mathbb R^d\).
- `q_A`, `delta q_A`, `chi_AB`: conserved densities, fluctuations, and
  chemical-potential susceptibility matrix.
- `n`, `chi`, `sigma`, `D`: one diffusive charge density, susceptibility,
  conductivity, and diffusion constant \(D=\sigma/\chi\).
- `xi^i`: stochastic current noise with covariance \(2T\sigma\).
- `K^R_nn`, `G^sym_nn`: retarded source-response and symmetrized density
  correlators.
- `B_r`, `B_a`, `I_diff`: gauge-invariant SK variables and quadratic
  diffusion action inherited from Volume X Chapter 6.
- `r_+`, `r_-`, `q_+`, `q_-`, `j`, `Phi_cur`: finite bond jump
  intensities, empirical flows, net empirical current, and contracted
  finite current cost.
- `I_cur[n,j]`: Gaussian hydrodynamic current cost obtained from the finite
  contraction only after local-equilibrium diffusive scaling input.
- `lambda`, `phi`, `O`: hydrodynamic nonlinear vertex coefficient,
  diagonalized fluctuation mode, and scalar composite \(O=\lambda:\phi^2:\)
  used for the equilibrium tail laboratory.
- `I_d(z;D)`: basic two-diffusive-mode loop integral for the symmetrized
  scalar spectrum or for a Kubo-divided transport kernel, not a standalone
  retarded current correlator.
- `Lambda_hyd`: hydrodynamic ultraviolet cutoff.
- `Xi^{ij}`, `eta`, `zeta`: stochastic stress tensor and shear/bulk
  viscosities.
- `pi^i`, `nu`, `P_T`, `P_L`: momentum density, kinematic shear diffusion
  constant, and transverse/longitudinal momentum projectors used in the
  shear-stress tail.

## Claim Ledger

1. In the chemical-potential convention
   \(\chi_{AB}=\partial q_A/\partial\mu_B\), the hydrodynamic equal-time
   covariance is \(T\chi_{AB}\).
2. Linear stochastic diffusion with current noise \(2T\sigma\) gives
   \(G^{\rm sym}_{nn}=2T\sigma k^2/(\omega^2+(Dk^2)^2)\) and integrates to
   the static covariance \(T\chi\).
3. The density source-response kernel
   \(K^R_{nn}=\chi Dk^2/(Dk^2-i\omega)\) obeys the classical hydrodynamic FDT
   with the symmetrized correlator.
4. The stochastic diffusion equation is the Hubbard-Stratonovich form of the
   local SK diffusion action with imaginary coefficient \(T\sigma\).
5. The finite two-direction bond-flow cost contracts exactly to
   \[
     \Phi_{\rm cur}(j;r_+,r_-)
     =
     j\log((j+\sqrt{j^2+4r_+r_-})/(2r_+))
     -\sqrt{j^2+4r_+r_-}+r_++r_-.
   \]
   Its minimum is at \(j_0=r_+-r_-\), its quadratic curvature is
   \((r_++r_-)^{-1}\), and its current-reversal asymmetry is
   \(-j\log(r_+/r_-)\).
6. Under a stated local-equilibrium diffusive scaling limit, the finite
   curvature in item 5 becomes the Gaussian current functional
   \[
     (4T)^{-1}\int (j+D\nabla n)\sigma^{-1}(j+D\nabla n),
   \]
   subject to the continuity equation.  This is a controlled scaling
   implication, not a microscopic QFT theorem.
7. Quadratic hydrodynamic current vertices produce hydrodynamic loops whose
   local analytic parts renormalize transport coefficients and whose
   nonanalytic parts are universal within the effective theory.
8. For one diffusive mode and scalar composite \(O=\lambda:\phi^2:\), the
   symmetrized/equilibrium time-domain tail is
   \(2\lambda^2(T\chi)^2(8\pi Dt)^{-d/2}\).  This scalar example is not a
   spatial-current example until a symmetry-allowed vector or tensor vertex is
   supplied.
9. The symmetrized scalar spectrum has exponent \(d/2-1\), the retarded
   correlator has exponent \(d/2\) after the low-frequency KMS/FDT factor, and
   the Kubo-divided transport kernel again has exponent \(d/2-1\).  In \(d=2\)
   this becomes the pair \((-i\omega)\log(-i\omega)\) in the retarded
   correlator and \(\log(-i\omega)\) in the transport coefficient.
10. The basic loop integral has nonanalytic part
   \[
     \Gamma(1-d/2)(4\pi)^{-d/2}(2D)^{-d/2}z^{d/2-1},
   \]
   with logarithmic replacement in even spatial dimension.  The
   Schwinger-parameter derivation is recorded as a worked calculation rather
   than a proposition.
11. In \(d=3\), an explicit cutoff integral separates the analytic
   \(\Lambda_{\rm hyd}\) term from the universal
   \(-z^{1/2}/(4\pi(2D)^{3/2})\) term.
12. Stress-noise positivity follows by decomposing symmetric tensors into
   traceless and trace parts, giving \(4T\eta s_T^2+2T\zeta(\operatorname{tr}s)^2\).
13. Momentum tails arise from the convective stress
    \(\pi^i\pi^j/(\varepsilon+p)\) and transverse momentum diffusion
    \(\nu=\eta/(\varepsilon+p)\).  The \(d=3\) shear-stress example carries the
    transverse angular average \(7/15\), the longitudinal sound-projector
    average \(2/15\), a retarded \((-i\omega)^{3/2}\) branch, and a
    Kubo-divided viscosity correction proportional to \((-i\omega)^{1/2}\).
14. A microscopic QFT theorem requires a constructed hydrodynamic scaling
    limit and controlled thermodynamic, real-time, and low-frequency limits.

## Calculation Checks

- `calculation-checks/hydrodynamic_long_time_tail_checks.py` verifies the
  static covariance normalization, classical FDT, finite bond-current
  contraction and quadratic curvature, Gaussian time-domain tail, loop
  nonanalytic coefficients, the \(d=3\) cutoff split, the FDT exponent shift
  between symmetrized, retarded, and Kubo-divided transport objects,
  shear-stress transverse/longitudinal projector averages, retarded-to-kernel
  square-root scaling, and stress-noise tensor positivity.

## Audit Notes

- 2026-05-31: Added finite-cell current-fluctuation bridge.  The exact
  finite statement is the two-direction bond-flow contraction and its
  Gallavotti-Cohen asymmetry; the macroscopic current functional is explicitly
  presented as a consequence of additional hydrodynamic scaling input.
- 2026-06-08 issue #890 audit: retyped the \(\lambda:\phi^2:\) laboratory as
  a scalar symmetrized/equilibrium tail, separated the FDT-shifted retarded
  nonanalyticity from the Kubo-divided transport-kernel nonanalyticity, added
  the \(d=2\) logarithmic transport consequence, and supplied the
  symmetry-allowed \(T^{xy}_{\rm conv}=\pi^x\pi^y/(\varepsilon+p)\) shear-loop
  projector calculation.

## Figure Ledger

No figure is included in this pass.  Future figures should show the
two-hydrodynamic-mode loop, the branch of \(z^{1/2}\) for retarded response,
and the separation of microscopic, hydrodynamic-cell, and external scales.
