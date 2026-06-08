# Chapter 06: Schwinger-Keldysh Hydrodynamic Effective Actions
Source-File: monograph/tex/volumes/volume_x/chapter06_schwinger_keldysh_hydrodynamic_effective_actions.tex

## Source Position

This chapter follows hydrodynamics from Ward identities by constructing the
real-time doubled effective action for multi-charge diffusion.  It connects
the SK generating functional, unitarity normalization, SK reality,
positivity, gauge-invariant hydrodynamic phase variables, KMS, noise, and
matrix-valued hydrodynamic response kernels.
The chapter is scoped to the ordinary normal-fluid retained sector; additional
slow fields require additional doubled variables and kernels.

## Notation Inventory

- `A^A_1`, `A^A_2`: background gauge fields on the two SK contours for
  the `A`-th conserved Abelian charge.
- `A^A_r`, `A^A_a`: average and difference sources.
- `varphi^A_1`, `varphi^A_2`: branch hydrodynamic phase fields.
- `B^A_s`, `B^A_r`, `B^A_a`: gauge-invariant source-phase combinations.
- `I_SK`: effective action defined by `Z = exp(i I_SK)`.
- `chi_AB`, `Sigma_AB`, `D_A^B`: susceptibility matrix, conductivity
  matrix, and diffusion endomorphism `D = Sigma chi^{-1}`.
- `n_A`, `j_A^i`: charge densities and spatial currents obtained from
  `a`-source variations.
- `E^A_i = partial_i A^A_{r0} - partial_t A^A_{ri}`: electric field in
  the chapter source convention.
- `K^R`: source-response kernel, distinguished from the commutator retarded
  function by source-coupling signs and local contact terms.
- `xi_Ai`: stochastic current noise after Hubbard-Stratonovich
  transformation.
- `S_slow`: declared retained slow sector inherited from Chapter 5; this
  chapter treats the ordinary charge-diffusion member explicitly.

## Claim Ledger

1. The finite closed-time-path trace algebra is recalled in prose and gives
   `I_SK[A_r,A_a=0]=0`, `I_SK[A_r,A_a]^*=-I_SK[A_r,-A_a]`, and
   `Im I_SK >= 0` on the branch connected to the diagonal.
2. The gauge-invariant hydrodynamic variables are
   \(B^A_{s\mu}=A^A_{s\mu}+\partial_\mu\varphi^A_s\).
3. The leading quadratic diffusion action is
   \[
     I_{\rm diff}=\int
     [\chi_{AB} B^A_{a0}B^B_{r0}
     -\Sigma_{AB} B^A_{ai}\partial_tB^B_{ri}
     +iT\Sigma_{AB} B^A_{ai}B^B_{ai}].
   \]
4. `a`-phase variation gives the continuity equation with
   \(n_A=\chi_{AB}B^B_{r0}\) and
   \(j_A^i=-\Sigma_{AB}\partial_tB^B_{ri}\).
5. At zero external source this continuity equation is diffusion:
   \(\partial_t n_A-D_A{}^B\nabla^2n_B=0\),
   \(D_A{}^B=\Sigma_{AC}(\chi^{-1})^{CB}\).
6. With scalar sources \(A^B_{r0}\), the density source-response kernel is
   \[
     K^R_{n_An_B}=[(Dk^2-i\omega 1)^{-1}k^2\Sigma]_{AB}.
   \]
7. For transverse vector source the same action gives Ohm response
   \(j_A^i=\Sigma_{AB}E^B_i\).
8. The positive imaginary term has a Hubbard-Stratonovich representation
   with noise correlator
   \(2T\Sigma_{AB}\,\delta_{ij}\delta(t-t')\delta^{(d)}(x-x')\).
9. Classical dynamical KMS fixes the noise matrix to \(T\Sigma_{AB}\) by
   the finite algebra \(C_{AB}=\Sigma_{AB}/\beta\).
10. The quadratic diffusion action is an ordinary normal-fluid construction;
    every additional retained slow field requires its own \(r/a\) variables,
    source normalization, symmetry/frame data, response and noise kernels,
    dynamical KMS transformation, and positivity constraints.
11. A microscopic derivation remains an open theorem boundary requiring a
    controlled real-time hydrodynamic scaling limit of the KMS QFT, proof of
    completeness of the retained slow sector, and regularity of the omitted
    complement.

## Calculation Checks

- `calculation-checks/sk_diffusion_action_checks.py` verifies the sourced
  density saddle and response kernel for both one charge and a noncommuting
  two-charge susceptibility/conductivity pair, transverse Ohm response, KMS
  coefficient algebra, matrix KMS noise algebra, and Hubbard-Stratonovich
  noise normalization.
- `calculation-checks/hydrodynamic_modes_checks.py` supplies the paired issue
  #884 negative control: an omitted relaxational order parameter whose gap
  scales to zero generates a nonlocal memory kernel rather than an analytic
  conserved-density-only correction.

## Audit Notes

- 2026-06-08 issue #884 pass: scoped the SK construction to the declared
  ordinary normal-fluid slow sector, stated the doubled-field data required
  for any additional retained slow variable, and changed the microscopic
  theorem boundary from conserved-density-only nonanalyticity to slow-sector
  completeness plus complement regularity.

## Figure Ledger

No figure is included.  A later visual pass should add a compact SK-contour
diagram and a pole diagram for the diffusion kernel.
