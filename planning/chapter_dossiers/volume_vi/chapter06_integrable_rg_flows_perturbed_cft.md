# Chapter 06: Integrable RG Flows And Perturbed Two-Dimensional CFT

## Source Position

Volume VI now moves from exact finite-size thermodynamics to RG-flow
interpretation.  The chapter uses the preceding factorized scattering,
form-factor, and TBA chapters as local inputs and prepares later model
chapters on sine-Gordon, affine Toda, sigma models, and bridges to CFT.

## Notation Inventory

- `C`: ultraviolet two-dimensional CFT.
- `O`: relevant scalar primary of dimension `Delta_O < 2`.
- `g_Lambda`, `O_Lambda`: regulator-dependent perturbing coordinate and
  insertion.
- `M`, `R`, `r=MR`: mass scale, circle circumference, dimensionless size.
- `E_0(R)`, `c_eff(R)`: finite-size vacuum energy and scaling function.
- `epsilon_a(theta;r)`, `varphi_ab`: TBA pseudoenergy and scattering kernel.
- `Y_a`, `L(x)`: plateau \(Y\)-variable and Rogers dilogarithm.
- `Theta`, `G_Theta`, `C(R)`: stress-tensor trace, connected trace
  two-point distribution, and Zamolodchikov \(C\)-function.
- `Delta c_{N,Lambda}^Theta`, `R_N`, `R_Lambda`, `R_cont`,
  `R_Fub`, `R_loc`, `R_Theta`, `R_TBA`: retained trace form-factor
  central-charge coordinate and the particle-tail, rapidity-tail,
  contact/source, Fubini, local-reconstruction, trace-normalization, and
  TBA-endpoint residuals.
- `varphi`, `V(varphi)`, `g_l`, `K`, `kappa`: ordinary scalar
  Landau-Ginzburg field, normal-ordered polynomial potential, polynomial
  source coordinates, highest degree, and logarithmic covariance coefficient.

## Claim Ledger

- Defines a regulated CFT perturbation by source-functional data.
- Adds the ordinary polynomial scalar Landau-Ginzburg interface: defines the
  normal-ordered polynomial source-coordinate system, proves local integrability of
  logarithmic Wick-product collisions, derives the normal-ordered
  Schwinger-Dyson equation of motion, and identifies the finite order-field
  quotient for the even multicritical family while keeping the minimal-model
  endpoint as an RG construction problem.
- Derives the finite-size scaling function used to compare UV and IR data.
- States and proves the Zamolodchikov-normalized trace sum rule from the
  radial \(C\)-function derivative datum.
- Derives the form-factor trace-sum-rule coefficient \(9/E^4\) under
  absolute spectral convergence, making trace normalization a local check of
  proposed integrable flows.
- Adds a retained trace form-factor \(c\)-sum certificate that separates the
  positive local-observable coordinate from particle/rapidity tails,
  contact/source extensions, Fubini domination, local operator reconstruction,
  trace normalization, and TBA endpoint identification.
- States TBA finite-size energy as a construction from diagonal scattering
  data plus mirror-channel hypothesis.
- Proves the plateau dilogarithm formula under explicit constant-kernel
  assumptions.
- Records that scattering/TBA data require form-factor normalization before
  they determine local operator limits.

## Calculation Checks

- `calculation-checks/integrable_rg_flow_checks.py` verifies the minimal-model
  \(\phi_{1,3}\) arithmetic, the polynomial scalar LG multicritical ledger,
  source-scaling signs, massless dispersion identities, the \(9/E^4\)
  trace-sum-rule coefficient, and the
  central-charge targets for the \(\mathcal M(m,m+1)\to\mathcal M(m-1,m)\)
  flow family.  It also checks the retained trace form-factor \(c\)-sum
  certificate with monotone positive approximants, observable and
  TBA-comparison residual telescopes, and negative controls against exact
  endpoint overread, omitted trace/local reconstruction residuals, and signed
  residual cancellation.

## Figure Ledger

No figure is included in this pass.  Future render work should add a
rapidity-cylinder diagram showing massive and massless TBA channels and a
flow chart linking CFT perturbing data, factorized scattering, TBA, and form
factors.

## Audit Notes

- 2026-06-04: #728 pass focused on Ch06 observable architecture: trace
  form-factor sums are now tied to the \(c\)-theorem/TBA comparison only
  after reconstruction, normalization, contact, Fubini, and tail residuals
  are declared.
