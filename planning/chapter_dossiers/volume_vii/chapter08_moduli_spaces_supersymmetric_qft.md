# Chapter 08: Moduli Spaces In Supersymmetric Quantum Field Theory

## Source Position

Volume VII now separates supersymmetric vacuum spaces from the earlier exact
Wilsonian dynamics.  The chapter supplies moduli-space definitions before the
later lower-dimensional examples, protected sectors, and localization.

## Notation Inventory

- `Phi^i`, `W`, `F_i`, `mu`: chiral fields, superpotential, F-term equations,
  and moment map.
- `V`, `G_C`, `Z_F`, `I_F`: scalar representation, complexified reductive
  gauge group, F-flat locus, and F-term ideal.
- `M_cl`: classical Kahler or holomorphic quotient vacuum space.
- `M_ch,cl`, `M_mu,cl`: affine chiral quotient and symplectic vacuum
  quotient.
- `M`, `H_p`, `A_p`, `G_p`: quantum moduli space, Hilbert space, local
  operator algebra, and background response in vacuum `p`.
- `R_ch`, `ev_p`: chiral ring and evaluation homomorphism at a vacuum.
- `F`, `j_A^mu`, `Q_A`, `q_A`, `Hilb_q`: compact internal global symmetry,
  conserved currents, commuting charge operators, fixed charge vector, and
  the corresponding joint charge sector.
- `mu^A`, `H_mu`: chemical potentials and the Hamiltonian variational
  operator \(H-\mu^AQ_A\).
- `K_A`, `M_gap(p)`, `E_EFT(q,R)`: branch isometry vector fields, transverse
  mass scale of the branch EFT, and fixed-charge energy computed from the
  branch effective action.
- `Wightman-type data`: local operator-valued distributions, Hilbert spaces,
  vacuum sectors, correlation distributions, spectrum, locality, and
  covariance.
- `Kontsevich-Segal-type data`: geometric amplitudes, boundary state spaces,
  sewing maps, reflection pairings, and background-field dependence.
- `Q^a_i`, `tilde Q_a^i`, `M^i_j`: SQCD quarks, antiquarks, and mesons.
- `P_a^I`, `V^{IJ}`: \(SU(2)\), \(N_f=2\) doublet fields and antisymmetric
  meson/baryon Plucker coordinates.
- `Pf(V)`: Pfaffian
  \(V^{12}V^{34}-V^{13}V^{24}+V^{14}V^{23}\) for the \(SU(2)\),
  \(N_f=2\) quotient.
- `eq:su2-nf2-classical-plucker-hypersurface`: classical \(SU(2)\),
  \(N_f=2\) SQCD quotient as the Pfaffian/Plucker hypersurface.
- `eq:su2-nf2-quantum-deformed-pfaffian`: Wilsonian quantum-deformation
  input for the \(SU(2)\), \(N_f=2\) branch; the subsequent algebraic
  consequences are written in prose rather than as a theorem-family claim.
- `eq:su2-nf2-massive-vacua`: two isolated vacua after a nondegenerate
  antisymmetric mass deformation of the \(SU(2)\), \(N_f=2\) branch.
- `eq:su2-nf2-massive-superpotential-values`: corresponding superpotential
  values after solving the constrained \(F\)-term equations.
- The quantum-deformation calculation uses
  \(\operatorname{Pf}(V)=\Lambda_h^4\), including smoothness and the
  diagonal-mass two-vacuum check.
- `m_1`, `m_2`, `X`: diagonal mass-source parameters and the Lagrange
  multiplier used to impose the quantum-deformed Pfaffian constraint.
- `Lambda_0`: pure \(SU(2)\) holomorphic scale after the nondegenerate
  antisymmetric mass deformation, with
  \(\Lambda_0^6=m_1m_2\Lambda_h^4\).
- `M_H`, `mu_R`, `mu_C`: hyperkahler quotient and real/complex moment maps.
- `g_{i bar j}`: branch metric in the low-energy effective action.
- `q_i`, `tilde q_i`: rank-one \(U(1)\) hypermultiplet coordinates with
  charges \(+1\) and \(-1\).
- `z_i^(a)`, `p_i^(a)`: local base and cotangent coordinates on the
  \(q_a\neq0\) patch of the rank-one hyperkahler quotient.
- `zeta`: positive real FI parameter in the rank-one hypermultiplet model.
- `Theta`: holomorphic cotangent one-form \(\sum_i\tilde q_i\,dq_i\).
- `prop:n2-rank-one-hyperkahler-quotient`: explicit construction of the
  rank-one \(U(1)\) hypermultiplet Higgs branch as
  \(T^\ast\mathbb P^{N-1}\), including dimension, local coordinates, moment
  map solving, and one-form descent.

## Claim Ledger

- Defines classical supersymmetric vacuum equations and quotient data.
- States the precise affine chiral quotient and symplectic quotient data and
  proves their coordinate-ring comparison under explicit Kempf-Ness
  hypotheses.
- Works out the rank-one abelian quotient
  `C[x,y]^{C^*}=C[xy]` and its moment-map quotient, fixing the quotient
  convention used later in rank-one gauge-theory examples.
- Defines quantum moduli spaces as vacuum families together with low-energy
  Hilbert, operator, metric, and background-response data.
- Relates chiral rings to holomorphic functions under explicit separation and
  reducedness hypotheses.
- Adds the fixed-charge/large-charge probe of a branch: defines charge
  sectors, chemical potentials, homogeneous charged saddles on the cylinder,
  and the Noether map from branch EFT data to fixed-charge energy.
- States the conformal bridge precisely: via the state-operator theorem,
  large-charge local operators of definite scaling dimension encode
  fixed-charge energy eigenstates, so the Hellerman large-charge expansion
  supplies asymptotic charged-sector information about the branch EFT rather
  than a full construction of the quantum vacuum datum.
- Reframes Open Problem 93.3 as a special supersymmetric test case of the
  larger reconstruction problem from Wightman-type local QFT data to
  Kontsevich-Segal-type geometric amplitude and sewing data.
- Records `N=1` SQCD branch behavior and `N=2` Coulomb/Higgs/mixed branch
  structures, while explicitly marking the SQCD table as an orientation
  ledger rather than a proof.
- Derives the classical \(SU(2)\), \(N_f=2\) SQCD quotient
  \(\mathcal M_{\mathrm{ch},\mathrm{cl}}\simeq
  \{\operatorname{Pf}(V)=0\}\subset\bigwedge^2\mathbb C^4\), with explicit
  doublet coordinates, Pfaffian convention, converse reconstruction on a
  nonzero Plucker chart, and dimension check.
- Separates the Wilsonian quantum-deformation input
  \(\operatorname{Pf}(V)=\Lambda_h^4\) from its algebraic consequences, then
  derives smoothness for \(\Lambda_h\neq0\), reduces a nondegenerate
  antisymmetric mass matrix to Darboux form, solves the constrained
  \(F\)-term equations, and matches the two superpotential values to pure
  \(SU(2)\) by holomorphic threshold scale matching.
- Proves the rank-one \(\mathcal N=2\) hypermultiplet quotient
  \(\{\mu_C=0,\mu_R=\zeta\}/U(1)\simeq T^\ast\mathbb P^{N-1}\) for
  \(\zeta>0\), including the elementary real-moment representative,
  local cotangent coordinates, and preservation of the canonical holomorphic
  one-form on overlaps.
- Identifies singularities as loci where the low-energy theory changes and
  records the domain of validity of branch effective actions.

## Calculation Checks

- `calculation-checks/susy_moduli_space_checks.py` verifies the rank-one
  abelian invariant-ring calculation, the matching real/complex quotient
  dimension count, F-term ideal equivariance for an invariant
  superpotential, and the rank-one hyperkahler quotient dimension, one-form
  descent, and cotangent transition algebra for \(T^\ast\mathbb P^{N-1}\),
  together with the \(SU(2)\), \(N_f=2\) Pfaffian/Plucker identity,
  converse reconstruction chart, quotient dimension ledger, nonzero
  quantum-deformation smoothness test, diagonal-mass two-vacuum algebra, and
  holomorphic threshold scale matching.

## Figure Ledger

No figure is included in this pass.  Later figures should show the quotient
construction, SQCD branch cases, and the `N=2` Coulomb branch with singular
local models.

## Audit Notes

- 2026-05-30 anti-wrapper pass: demoted the classical \(SU(2)\), \(N_f=2\)
  Pfaffian/Plucker quotient from proposition/proof form to derivation prose.
  The invariant-theory calculation, converse chart, quotient dimension count,
  and convention definitions are retained.
- 2026-05-30 follow-up anti-wrapper pass: demoted the quantum-deformation
  algebra block from lemma/proof form as well.  The nonperturbative content is
  the Wilsonian input \(\operatorname{Pf}(V)=\Lambda_h^4\); smoothness,
  Darboux reduction, the two-vacuum solution, and threshold matching are
  finite algebraic consequences and are now presented as such.
- 2026-05-30 moduli-construction clarification: expanded Open
  Problem~93.3 so it explicitly distinguishes chiral-ring reconstruction of
  reduced holomorphic coordinates from fixed-charge/large-charge
  reconstruction of asymptotic branch EFT data.
- 2026-05-30 Wightman-to-KS refinement: sharpened Open Problem~93.3 so the
  moduli-space datum is treated as an output of the structural passage from
  local Wightman data to KS-style boundary/sewing/amplitude data.
