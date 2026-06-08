# Volume VII, Chapter 5 Dossier: Nonrenormalization and Holomorphy
Source-File: monograph/tex/volumes/volume_vii/chapter05_nonrenormalization_holomorphy.tex

## Logical Role

- Role in the monograph: formulate supersymmetric nonrenormalization as
  Wilsonian chiral-coordinate statements with regulator and anomaly
  hypotheses displayed.
- Immediate predecessor: supersymmetric Wilsonian schemes.
- Immediate successor: four-dimensional \(\mathcal N=1\) gauge dynamics.

## Definitions And Results

- Chiral \(F\)-term coordinate and full-superspace \(D\)-term coordinate.
- Perturbative Wilsonian superpotential argument.
- Tree-level elimination of a massive chiral block, stated as a holomorphic
  implicit-function theorem application and worked out for a quadratic
  heavy-field block.
- Spurion symmetry selection rule.
- Holomorphic gauge coupling and Wilsonian one-loop running, stated with
  weak-coupling patch, theta-periodicity, perturbative \(q_h^0\) projection,
  explicit \(q_h^0\) closure input, and spurion-ledger hypotheses.
- Konishi-type rescaling anomaly as a regulated super-Berezinian coordinate
  change, with the local \(W^\alpha W_\alpha\) coefficient derived from the
  chiral heat-kernel density and the chapter's gauge-coupling normalization.
- NSVZ coordinate formula from the holomorphic coupling, rescaling anomaly,
  canonical normalization, matter Konishi Jacobians, and the gauge-multiplet
  BV-complex rescaling Jacobian.
- NSVZ beta function displayed as a coordinate identity obtained by
  differentiating the holomorphic-canonical gauge-coordinate relation in the
  stated anomalous-dimension convention; the nontrivial inputs are the
  coordinate relation, the regulated rescaling anomaly, and the holomorphic
  Wilsonian one-loop running, not the final algebraic differentiation.
- Boundary between perturbative Wilsonian arguments and nonperturbative
  chiral dynamics.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\Phi^i\) | chiral superfields |
| \(t^A\) | chiral coupling coordinates |
| \(I_F,I_D\) | chiral and full-superspace local coordinates |
| \(X^a,\Phi^i\) | heavy and light chiral coordinates in a tree-level elimination patch |
| \(X_*^a(\Phi;t)\) | holomorphic solution of the heavy chiral equation \(\partial_{X^a}W=0\) |
| \(H_{ab}\) | heavy-block Hessian \(\partial_{X^a}\partial_{X^b}W\) |
| \(\tau\) | holomorphic gauge coupling |
| \(\tau_{\rm eff}\) | Wilsonian effective holomorphic gauge coordinate |
| \(q_h\) | weak-coupling instanton-counting coordinate \(\exp(2\pi i\tau)\) |
| \(B_0(t)\) | perturbative \(q_h^0\) coefficient in the holomorphic gauge beta component |
| \(b_0\) | one-loop holomorphic gauge coefficient |
| \(T(R)\) | representation index in the monograph trace convention |
| \(C_2(G)\) | adjoint index in the same trace convention |
| \(Z_i,\gamma_i\) | matter normalization coordinate and anomalous dimension convention |

## Claim Ledger

1. Perturbative Wilsonian loops generate full-superspace terms unless an
   infrared singularity is present; Wilsonian cutoff excludes that singularity.
2. Tree-level elimination of massive chiral fields stays in the chiral
   coordinate class because the heavy chiral equation with invertible Hessian
   has a holomorphic solution by the implicit-function theorem.
3. Holomorphic gauge coupling is one-loop exact as a Wilsonian coordinate only
   after an explicit \(q_h^0\) closure input is supplied.  Holomorphy and theta
   periodicity identify \(B_0(t)\) as the perturbative coefficient but do not
   exclude neutral holomorphic dependence on superpotential or mass spurions.
   Finite holomorphic coordinate changes depending on running couplings shift
   beta components by \(\beta_t^A\partial_AF\); only beta-vector-constant
   shifts are harmless.  The numerical coefficient
   \(b_0=3C_2(G)-\sum_iT(R_i)\) comes from the separate regulated one-loop
   determinant input.
4. The Konishi rescaling anomaly is a local Jacobian statement inside a
   declared regulator; its chiral representative is fixed by gauge invariance,
   chirality, locality, the component heat-kernel anomaly, and the
   \(1/(4g^2)\operatorname{tr}(F^2)\) normalization.
5. Canonical gauge couplings differ by rescaling anomalies.
6. The holomorphic-canonical coordinate relation is derived by combining the
   classical canonical coordinate \(8\pi^2/g^2\), the matter shifts
   \(-T(R_i)\log Z_i\), the adjoint gauge-complex shift
   \(C_2(G)\log g^2\), and a finite \(\mu\)-independent scheme constant.
7. The NSVZ beta-function formula is recorded as a coordinate identity in the
   declared canonical coupling and anomalous-dimension convention, not as an
   independent theorem; finite canonical reparametrizations change the
   displayed denominator by reparametrizing the beta-vector field.

## Calculation Checks

- `calculation-checks/susy_holomorphy_nsvz_checks.py` verifies the quadratic
  chiral-elimination formula, the derivative identity after eliminating a
  heavy chiral coordinate, the loop-supergraph Grassmann-measure ledger
  leaving one full \(d^4\theta\) integral in a connected Wilsonian loop graph,
  the holomorphic gauge-coupling \(q_h^0\) perturbative projection, the
  neutral-spurion \(q_h^0\) closure boundary and running-coupling
  finite-redefinition term, the separate vector/matter one-loop shell
  coefficient \(3C_2(G)-\sum_iT(R_i)\), the sign equivalence between
  \(d\tau/d\log\mu=-b_0/(2\pi i)\),
  \(dX_h/d\log\mu=b_0\), and
  \(d\log q_h/d\log\mu=-b_0\), Konishi and vector-multiplet coordinate
  shifts, and the rational algebra that differentiates the
  holomorphic-canonical coordinate relation into the NSVZ beta function.

## Audit Notes

- 2026-06-02 holomorphic-running sign pass: corrected the Wilsonian
  holomorphic gauge coordinate running to
  \(d\tau/d\log\mu=-b_0/(2\pi i)\), consistent with
  \(\operatorname{Im}\tau=4\pi/g_h^2\), asymptotic freedom,
  \(dX_h/d\log\mu=b_0\), the NSVZ coordinate section, and the SU(2)
  Seiberg--Witten perturbative prepotential convention.  Added the sign
  equivalence to the paired calculation check.
- 2026-06-02 Wilsonian superpotential pass: expanded the perturbative
  nonrenormalization mechanism from a compressed supergraph slogan into a
  local D-algebra argument.  The text now shows that a connected loop graph
  leaves one full superspace measure after spanning-tree Grassmann delta
  identifications, and that converting the resulting local \(D\)-term into a
  chiral \(F\)-term would require the nonlocal chiral projector with an
  inverse \(\Box\), i.e. precisely the infrared singularity absent from the
  Wilsonian low-momentum expansion.  Added the corresponding finite
  graph-measure ledger to the paired calculation check.
- 2026-06-02 holomorphic one-loop coefficient pass: tightened the
  one-loop-exactness proof by assigning the value of \(b_0\) to the regulated
  one-loop determinant.  The text now separates the background-field shell
  determinant, whose vector/ghost and matter contributions give
  \(3C_2(G)-\sum_iT(R_i)\), from the holomorphic \(q_h\)-expansion sector
  bookkeeping.  The paired check verifies this finite coefficient bookkeeping
  and its \(X_h\)-running sign.
- 2026-06-05 issue #794 pass: corrected the one-loop exactness boundary.  The
  chapter now says theta periodicity and weak-coupling regularity only isolate
  the \(q_h^0\) perturbative coefficient \(B_0(t)\); they do not prove that
  \(B_0\) is independent of neutral superpotential or mass-spurion invariants.
  Added an explicit \(q_h^0\) closure hypothesis, the finite coordinate-change
  formula
  \(d(\tau+F(t))/d\log\mu=d\tau/d\log\mu+\beta_t^A\partial_AF\), and a
  neutral-spurion example showing the allowed failure mode.

## Figures

- None in this chapter.
