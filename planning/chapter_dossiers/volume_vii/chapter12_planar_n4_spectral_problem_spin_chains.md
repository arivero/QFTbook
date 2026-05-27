# Chapter 12: Planar N=4 Supersymmetric Yang-Mills as a Spectral Problem

## Source Position

This chapter begins the planar-integrability block after the core
supersymmetric QFT examples.  It rewrites the stringbook spin-chain material
as a local-operator spectral problem in four-dimensional gauge theory.  The
current pass adds the missing finite-\(N\) SCFT datum before the planar limit,
so the spin chain is visibly a sector of \(\mathcal N=4\) SYM rather than a
replacement for the QFT.

## Notation Inventory

- `G`, `g`: gauge group and Lie algebra.
- `Phi^I`: six real adjoint scalars of the \(\mathcal N=4\) multiplet.
- `lambda^A_alpha`: four adjoint Weyl fermions.
- `tau`: complexified Yang-Mills coupling
  `theta/(2 pi)+4 pi i/g_YM^2`.
- `C_2(g)`: adjoint quadratic Casimir.
- `a,c`: four-dimensional conformal anomaly coefficients.
- `O_C^(k)`: half-BPS single-trace representative in `[0,k,0]`.
- `P^{IJ,KL}`: projector onto symmetric traceless `SO(6)` tensors.
- `mathbb O^{IJ}`: canonically normalized stress-tensor-multiplet primary.
- `mathcal Z_J`: planar-normalized chiral primary built from one complex
  scalar.
- `lambda`: 't Hooft coupling `g_YM^2 N`.
- `g`: integrability coupling `sqrt(lambda)/(4 pi)`.
- `V`: one-letter space of elementary fields and covariant derivatives.
- `H_L^cyc`: cyclic single-trace spin-chain quotient.
- `S`: closed sector of one-letter space under planar mixing.
- `tau`: cyclic shift on spin-chain sites.
- `X,Z`: two complex scalars defining the `SU(2)` scalar sector.
- `P_{j,j+1}`: adjacent spin permutation.
- `I,P,K`: identity, permutation, and trace maps in the `SO(6)` scalar chain.
- `H_XXX`: one-loop Heisenberg Hamiltonian.
- `u_j,p_j`: Bethe rapidities and momenta.
- `D_+`: lightlike covariant derivative in the `SL(2)` sector.

## Claim Ledger

- Defines the intrinsic \(\mathcal N=4\) Yang-Mills field datum, including
  six scalars, four Weyl fermions, \(SU(4)_R\), and the complexified coupling
  convention.
- Displays the \(\mathcal N=1\) vector-plus-three-adjoints presentation as
  bookkeeping and states explicitly that it is not the full R-symmetry.
- Proves one-loop ordinary and holomorphic beta-function cancellation from
  field content.
- Quotes exact finiteness/marginality with regulator-level hypotheses rather
  than treating it as a one-line folklore consequence.
- Computes the free-field anomaly coefficients to get
  `a=c=dim(g)/4`, with `SU(N)` and `U(N)` specializations.
- Defines the half-BPS `[0,k,0]` representatives, separates them from the
  Konishi long multiplet, and quotes protected dimensions and two/three-point
  nonrenormalization.
- Derives the stress-tensor-multiplet two-point normalization from Wick
  contractions and the symmetric-traceless `SO(6)` projector.
- Proves the leading planar chiral-primary normalization:
  cyclic planar Wick contractions give the unit two-point function for
  `mathcal Z_J`, the extremal pair-of-pants color graph gives the raw factor
  `J J1 J2 N^(J-1)`, and the normalized OPE coefficient is
  `sqrt(J1 J2 (J1+J2))/N`.  The finite-\(N\) trace-relation and multi-trace
  caveat remains explicit.
- Defines the planar single-trace operator space as a cyclic quotient before
  introducing spin-chain language.
- Adds the planar two-point inner product and quotient status of spin-chain
  representatives.
- Adds a two-site scalar mixing proposition with color-locality and BPS
  protection fixing the identity term.
- Adds the full one-loop `SO(6)` scalar density
  `K+2I-2P` and proves its holomorphic `SU(2)` reduction.
- States and derives the one-loop `SU(2)` Hamiltonian from nearest-neighbor
  planar mixing, BPS protection of the identity term, and the adjacent
  exchange coefficient.
- Derives the coordinate Bethe ansatz with the explicit two-magnon contact
  equation, the chamber exchange coefficient
  `(u_1-u_2-i)/(u_1-u_2+i)`, and the inverse Bethe-Yang phase entering the
  closed-chain equations.  This fixes a convention-sensitive sign/inverse
  distinction relative to the ordered wavefunction.
- Derives the cyclic closed-chain quantization by comparing
  `Psi(n_1,n_2)` with `Psi(n_2,n_1+L)` and then states the factorized
  `M`-magnon equation using the finite XXX transfer-matrix theorem from the
  integrability background chapter.
- Carries the one-loop Konishi descendant calculation to
  `gamma_K^(1)=3 lambda/(4 pi^2)`.
- Separates the asymptotic long-chain problem from finite-length wrapping.
- Records the `SL(2)`, `SU(2|3)`, and full oscillator-module sector hierarchy
  and the range growth of the long-range dilatation operator.

## Figure Ledger

No figure is included in this pass.  A future figure should show the cyclic
single-trace word and the adjacent exchange interaction.

## Calculation Checks

- `calculation-checks/susy_n4_scft_checks.py` verifies one-loop and
  holomorphic beta-function cancellation, `a=c=dim(g)/4`, idempotence and
  dimension of the `SO(6)` symmetric-traceless projector, the
  stress-tensor-multiplet two-point normalization factor, and the planar
  chiral two-point/OPE coefficient arithmetic including the pair-of-pants
  cyclic factor.
- `calculation-checks/planar_n4_integrability_checks.py` verifies the
  one-magnon finite-difference spectrum and the displayed cyclic Konishi
  Bethe roots.
- The same script verifies the two-magnon contact equation, the rapidity form
  of the chamber exchange coefficient, the inverse relation between that
  coefficient and the Bethe-Yang phase, and the finite length-four Konishi
  two-magnon eigenvector/cyclicity condition.
- The same script checks that the `SO(6)` trace operator vanishes on the
  holomorphic `X,Z` subsector.
- Same script now also checks BMN scaling and bound-state dispersion
  normalizations that depend on the chapter's coupling convention.

## Source Notes

- Stringbook source consulted:
  `/Users/xiyin/PhysicsLogic/references/stringbook/string notes.tex`,
  especially the \(\mathcal N=4\) SCFT, half-BPS operator, and spin-chain
  setup paragraphs around the local labels `sec:nfsymsca`, `sec:gravkk`,
  and `sec:spinchainfirst`.
- Local reference payload for this pass:
  `references/susy_gauge_dynamics_localization/issue588_n4_scft/`.
- Scope boundary: this chapter uses the stringbook conventions only as QFT
  convention guidance.  String compactification, AdS/CFT, and superstring
  dynamics are not part of the monograph argument here.
