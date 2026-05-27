# Volume VII, Chapter 5 Dossier: Nonrenormalization and Holomorphy

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
- Holomorphic gauge coupling and Wilsonian one-loop exactness, stated with
  weak-coupling patch, theta-periodicity, perturbative \(q_h^0\) projection,
  and spurion-ledger hypotheses.
- Konishi-type rescaling anomaly as a regulated super-Berezinian coordinate
  change, with the local \(W^\alpha W_\alpha\) coefficient derived from the
  chiral heat-kernel density and the chapter's gauge-coupling normalization.
- NSVZ coordinate formula from the holomorphic coupling, rescaling anomaly,
  canonical normalization, matter Konishi Jacobians, and the gauge-multiplet
  BV-complex rescaling Jacobian.
- NSVZ beta function as a coordinate identity obtained by differentiating the
  holomorphic-canonical gauge-coordinate relation in the stated
  anomalous-dimension convention.
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
3. Holomorphic gauge coupling is one-loop exact as a Wilsonian coordinate
   after the perturbative sector is identified as the \(q_h^0\) coefficient;
   finite holomorphic reference-coordinate changes are scale independent.
4. The Konishi rescaling anomaly is a local Jacobian statement inside a
   declared regulator; its chiral representative is fixed by gauge invariance,
   chirality, locality, the component heat-kernel anomaly, and the
   \(1/(4g^2)\operatorname{tr}(F^2)\) normalization.
5. Canonical gauge couplings differ by rescaling anomalies.
6. The holomorphic-canonical coordinate relation is derived by combining the
   classical canonical coordinate \(8\pi^2/g^2\), the matter shifts
   \(-T(R_i)\log Z_i\), the adjoint gauge-complex shift
   \(C_2(G)\log g^2\), and a finite \(\mu\)-independent scheme constant.
7. The NSVZ beta-function formula is a coordinate identity in the declared
   canonical coupling and anomalous-dimension convention; finite canonical
   reparametrizations change the displayed denominator by reparametrizing the
   beta-vector field.

## Calculation Checks

- `calculation-checks/susy_holomorphy_nsvz_checks.py` verifies the quadratic
  chiral-elimination formula, the derivative identity after eliminating a
  heavy chiral coordinate, the holomorphic gauge-coupling \(q_h^0\)
  perturbative projection and finite scheme-shift invariance, Konishi and
  vector-multiplet coordinate shifts, and the rational algebra that
  differentiates the holomorphic-canonical coordinate relation into the NSVZ
  beta function.

## Figures

- None in this chapter.
