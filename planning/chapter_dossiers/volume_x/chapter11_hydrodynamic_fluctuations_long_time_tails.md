# Chapter 11: Hydrodynamic Fluctuations And Long-Time Tails

## Source Position

This chapter completes the first Volume X pass through hydrodynamics by
developing the stochastic and Schwinger-Keldysh fluctuation layer after the
deterministic Ward-identity chapter, the SK hydrodynamic-action chapter, and
the nonequilibrium/open-system chapter.

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
- `lambda`, `phi`: hydrodynamic nonlinear current vertex and diagonalized
  fluctuation mode.
- `I_d(z;D)`: basic two-diffusive-mode loop integral.
- `Lambda_hyd`: hydrodynamic ultraviolet cutoff.
- `Xi^{ij}`, `eta`, `zeta`: stochastic stress tensor and shear/bulk
  viscosities.
- `pi^i`, `nu`: momentum density and kinematic shear diffusion constant.

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
5. Quadratic hydrodynamic current vertices produce hydrodynamic loops whose
   local analytic parts renormalize transport coefficients and whose
   nonanalytic parts are universal within the effective theory.
6. For one diffusive mode and \(J=\lambda:\phi^2:\), the time-domain tail is
   \(2\lambda^2(T\chi)^2(8\pi Dt)^{-d/2}\).
7. The basic loop integral has nonanalytic part
   \[
     \Gamma(1-d/2)(4\pi)^{-d/2}(2D)^{-d/2}z^{d/2-1},
   \]
   with logarithmic replacement in even spatial dimension.  The
   Schwinger-parameter derivation is recorded as a worked calculation rather
   than a proposition.
8. In \(d=3\), an explicit cutoff integral separates the analytic
   \(\Lambda_{\rm hyd}\) term from the universal
   \(-z^{1/2}/(4\pi(2D)^{3/2})\) term.
9. Stress-noise positivity follows by decomposing symmetric tensors into
   traceless and trace parts, giving \(4T\eta s_T^2+2T\zeta(\operatorname{tr}s)^2\).
10. Momentum tails arise from the convective stress
    \(\pi^i\pi^j/(\varepsilon+p)\) and transverse momentum diffusion
    \(\nu=\eta/(\varepsilon+p)\).
11. A microscopic QFT theorem requires a constructed hydrodynamic scaling
    limit and controlled thermodynamic, real-time, and low-frequency limits.

## Calculation Checks

- `calculation-checks/hydrodynamic_long_time_tail_checks.py` verifies the
  static covariance normalization, classical FDT, Gaussian time-domain tail,
  loop nonanalytic coefficients, the \(d=3\) cutoff split, and stress-noise
  tensor positivity.

## Figure Ledger

No figure is included in this pass.  Future figures should show the
two-hydrodynamic-mode loop, the branch of \(z^{1/2}\) for retarded response,
and the separation of microscopic, hydrodynamic-cell, and external scales.
