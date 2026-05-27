# Volume VII, Chapter 3 Dossier: Supersymmetric Gauge Theory

## Logical Role

- Role in the monograph: introduce supersymmetric gauge theory as
  field-variable data after superspace and local actions.
- Immediate predecessor: superspace, chiral superfields, local actions, and
  Wilsonian-scheme cautions.
- Immediate successor: supersymmetric Wilsonian schemes, holomorphy, and exact
  dynamics.

## Definitions And Results

- Gauge group \(G\), Lie algebra \(\mathfrak g\), and fixed invariant trace
  bilinear form in the Hermitian-generator convention inherited from the
  Yang-Mills foundation chapter.
- Curvature definition \(F_{\mu\nu}=i[\nabla_\mu,\nabla_\nu]\), finite gauge
  transformation, curvature covariance, and gauge-invariant kinetic/theta
  densities.
- Monograph Yang--Mills coupling convention
  \(-\frac{1}{4g^2}\operatorname{tr}F_{\mu\nu}F^{\mu\nu}\).
- Off-shell vector multiplet \((A_\mu,\lambda,\bar\lambda,D)\).
- Superfield gauge transformation and chiral field strength \(W_\alpha\).
- Matter chiral multiplets in a representation \(R\).
- Moment-map definition of the \(D\)-term coupling, FI centrality condition,
  and explicit auxiliary \(D\)-field elimination.
- Perturbative local gauge anomaly as a consistency condition.
- Conjugate-pair and real-representation perturbative gauge-anomaly
  cancellation.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(G\) | compact gauge group |
| \(\mathfrak g\) | Lie algebra of \(G\) |
| \(\operatorname{tr}\) | invariant bilinear form fixing coupling normalization |
| \(A_\mu\) | gauge connection representative |
| \(F_{\mu\nu}\) | curvature of \(A_\mu\) |
| \(V\) | real vector superfield |
| \(W_\alpha\) | chiral gauge field-strength superfield |
| \(R\) | matter representation |
| \(\mu_R\) | moment map of the matter representation |
| \(\zeta\) | FI functional, defined only on the abelian quotient |
| \(\eta^\sharp\) | trace-dual of \(\mu_R-\zeta\) used in the D-term potential |

## Claim Ledger

1. The vector multiplet is an off-shell field-variable object, not particle
   data.
2. The chosen trace convention fixes the Yang--Mills kinetic normalization
   used later in anomalies and beta functions.
3. The Hermitian curvature convention transforms covariantly and produces
   gauge-invariant kinetic and theta densities.
4. The superfield strength transforms covariantly and produces a
   gauge-invariant chiral kinetic term.
5. Matter \(D\)-terms are encoded by a moment map; eliminating the auxiliary
   field gives \(V_D=g^2 \|\mu_R-\zeta\|^2/2\) with FI terms only on abelian
   factors.
6. Vanishing of the perturbative gauge anomaly is a quantum consistency
   condition, separate from the classical superspace construction.
7. Vectorlike conjugate pairs and real representations have zero
   perturbative cubic gauge anomaly; the vector-multiplet adjoint gaugino is
   therefore locally gauge-anomaly free.

## Calculation Checks

- `calculation-checks/susy_gauge_foundation_checks.py` verifies the
  auxiliary \(D\)-field square completion, FI centrality for an `su(2)`
  semisimple factor, vectorlike `U(1)` anomaly cancellation, and the
  conjugate-representation anomaly sign.

## Figures

- Vector multiplet component ladder.
- Gauge-superfield transformation diagram.
- Moment-map coupling diagram.
