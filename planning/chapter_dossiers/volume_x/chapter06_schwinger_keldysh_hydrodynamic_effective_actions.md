# Chapter 06: Schwinger-Keldysh Hydrodynamic Effective Actions

## Source Position

This chapter follows hydrodynamics from Ward identities by constructing the
real-time doubled effective action for charge diffusion.  It connects the SK
generating functional, unitarity normalization, SK reality, positivity,
gauge-invariant hydrodynamic phase variables, KMS, noise, and hydrodynamic
response kernels.

## Notation Inventory

- `A_1`, `A_2`: background gauge fields on the two SK contours.
- `A_r`, `A_a`: average and difference sources.
- `varphi_1`, `varphi_2`: branch hydrodynamic phase fields.
- `B_s`, `B_r`, `B_a`: gauge-invariant source-phase combinations.
- `I_SK`: effective action defined by `Z = exp(i I_SK)`.
- `chi`, `sigma`, `D`: susceptibility, conductivity, and diffusion constant.
- `n`, `j^i`: charge density and spatial current obtained from
  `a`-source variations.
- `E_i = partial_i A_{r0} - partial_t A_{ri}`: electric field in the chapter
  source convention.
- `K^R`: source-response kernel, distinguished from the commutator retarded
  function by source-coupling signs and local contact terms.
- `xi_i`: stochastic current noise after Hubbard-Stratonovich transformation.

## Claim Ledger

1. The SK generating functional obeys
   `I_SK[A_r,A_a=0]=0`, `I_SK[A_r,A_a]^*=-I_SK[A_r,-A_a]`, and
   `Im I_SK >= 0`.
2. The gauge-invariant hydrodynamic variables are
   \(B_{s\mu}=A_{s\mu}+\partial_\mu\varphi_s\).
3. The leading quadratic diffusion action is
   \[
     I_{\rm diff}=\int
     [\chi B_{a0}B_{r0}-\sigma B_{ai}\partial_tB_{ri}
     +iT\sigma B_{ai}B_{ai}].
   \]
4. `a`-phase variation gives the continuity equation with
   \(n=\chi B_{r0}\) and \(j^i=-\sigma\partial_tB_{ri}\).
5. At zero external source this continuity equation is diffusion:
   \(\partial_t n-D\nabla^2n=0\), \(D=\sigma/\chi\).
6. With scalar source \(A_{r0}\), the density source-response kernel is
   \[
     K^R_{nn}=\chi Dk^2/(Dk^2-i\omega).
   \]
7. For transverse vector source the same action gives Ohm response
   \(j^i=\sigma E_i\).
8. The positive imaginary term has a Hubbard-Stratonovich representation
   with noise correlator
   \(2T\sigma\,\delta_{ij}\delta(t-t')\delta^{(d)}(x-x')\).
9. Classical dynamical KMS fixes the noise coefficient to \(T\sigma\) by
   the finite algebra \(c=\sigma/\beta\).
10. A microscopic derivation remains an open theorem boundary requiring a
    controlled real-time hydrodynamic scaling limit of the KMS QFT.

## Calculation Checks

- `calculation-checks/sk_diffusion_action_checks.py` verifies the sourced
  density saddle and response kernel, transverse Ohm response, KMS
  coefficient algebra, and Hubbard-Stratonovich noise normalization.

## Figure Ledger

No figure is included.  A later visual pass should add a compact SK-contour
diagram and a pole diagram for the diffusion kernel.
