# Volume VI, Chapter 2 Dossier: Two-Dimensional Scattering Analyticity And Bootstrap Data

## Logical Role

- Role in the monograph: add rapidity-plane analyticity and bound-state pole
  data after the factorized-scattering algebra has been defined.
- Immediate predecessor: factorized scattering, Yang--Baxter consistency, and
  Zamolodchikov--Faddeev operators.
- Immediate successor: form factors, local operators, and thermodynamic Bethe
  ansatz.

## Definitions And Results

- Physical rapidity strip \(0<\operatorname{Im}\theta<\pi\).
- Bootstrap datum consisting of meromorphic continuation, pole locations,
  residue/fusion couplings, and explicit horizontal-strip polynomial growth
  bounds away from the declared pole set; TBA use also requires a branch and
  kernel integrability hypothesis.
- Bound-state mass formula from a direct-channel pole, derived by analytic
  continuation of two-body rapidity kinematics with the mostly-plus
  convention \(s=-(p_a+p_b)^2\).
- Residue factorization through bound-state multiplicity space.
- Bound-state residue projection maps
  \(V_e\leftrightarrows V_a\otimes V_b\), with the sign fixed by
  one-particle positivity normalization.
- Fusing-angle kinematics from the complex on-shell momentum identity
  \(p_a(\theta+i\bar u)+p_b(\theta-i\bar u')=p_e(\theta)\).
  The component expansion now derives both the imaginary-momentum cancellation
  and the real mass relation, and checks that these imply the pole-location
  mass formula.
- Fusion equation for scattering of a bound state with a third particle,
  derived by a small-contour residue extraction of the factorized
  three-particle amplitude, under the stated no-extra-pole hypothesis.
- Finite residue-projection algebra for the fusion identity: if
  \(S_{ab}(\zeta)=iP_e/(\zeta-iu)+\text{regular}\) and the \(ak,bk\) product
  is holomorphic on the contour, then only \(B(iu)P_e\) enters
  \(-i\operatorname{Res}\), and projecting with the residue maps gives the
  bound-state scattering coordinate.
- CDD factor as a meromorphic scalar ambiguity satisfying unitarity and
  crossing.
- Elementary scalar block algebra: unitarity identity, pole lattice, and zero
  lattice.
- Crossing-symmetric CDD-pair diagnostic: the pair
  \([x]_\theta[1-x]_\theta\) satisfies scalar unitarity and crossing but has
  opposite signs for the two physical-strip residues, so direct-channel
  particle interpretation requires the full residue datum, not only the pole
  location.
- Operator-algebraic theorem boundary for wedge-local and local-algebra
  reconstruction.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\theta\) | rapidity difference |
| \(\mathcal S_{\rm phys}\) | physical rapidity strip |
| \(S_{ab}^{cd}(\theta)\) | two-body scattering amplitude |
| \(u_{ab}^{e}\) | fusing angle for bound state \(e\) |
| \(\Gamma_{ab}^{e,\alpha}\) | bound-state coupling/intertwiner |
| \(C(\theta)\) | CDD factor |
| \([x]_\theta\) | elementary meromorphic block |

## Claim Ledger

1. The physical strip is the analytic domain relating direct and crossed
   two-particle channels in rapidity variables.
2. A simple pole in the physical strip gives a kinematic mass relation for a
   possible bound state only after the direct-channel residue and positivity
   normalization have been specified.
3. A Hilbert-space bound-state interpretation requires explicit projection
   maps \(V_e\leftrightarrows V_a\otimes V_b\) and the correct positivity
   normalization of the residue.
4. The fusion equation is a small-contour residue identity; it requires the
   \(ak\) and \(bk\) factors to be holomorphic on the chosen contour.
5. The polynomial substrip growth bound is part of the bootstrap datum itself;
   sharper form-factor or TBA estimates are additional hypotheses.
6. Elementary scalar blocks supply controlled meromorphic zero-pole pairs and
   obey \([x]_\theta[x]_{-\theta}=1\).
7. CDD factors show that unitarity and crossing do not alone determine a
   unique amplitude; the crossing-symmetric scalar pair also shows that
   scalar unitarity and crossing do not by themselves make every
   physical-strip pole a positive direct-channel bound-state pole.
8. Local QFT realization requires local algebras or Wightman fields in
   addition to on-shell bootstrap data.

## Figures

- Rapidity strip with physical line, crossed line, and bound-state pole.
- Fusion triangle showing fusing angles.
- CDD zero-pole pair diagram.

## Calculation Checks

- `calculation-checks/integrable_scattering_bootstrap_checks.py`: checks the
  elementary scalar block unitarity identity, the crossing relation
  \([x]_{\ii\pi-\theta}=-[1-x]_\theta\), the CDD-pair
  unitarity/crossing identities, and the opposite signs of the two
  physical-strip residues.  It also checks the complex fusing-angle momentum
  identity and the resulting bound-state mass relation, plus an exact
  finite-rank noncommuting matrix model for the fusion residue projection.

## Audit Notes

- 2026-06-02 scalar-block residue-sign pass: removed the line-by-line
  hyperbolic cancellation from the chapter prose, kept the consequential
  physical-strip residue sign in the manuscript, and added a companion check
  for the elementary identities and crossing-pair residue signs.
- 2026-06-02 fusing-angle component pass: expanded the complex on-shell
  momentum identity into real and imaginary rapidity components, deriving the
  fusing-angle sine relation, the real fused mass, and the pole-location mass
  formula; extended the companion check accordingly.
- 2026-06-02 fusion residue-projection pass: added the finite algebra after
  the contour proof and extended the companion check to verify the sign,
  holomorphic-coefficient, and projection conventions of the fusion identity.
