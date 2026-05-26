# Volume XI, Chapter 5 Dossier: Wilson Lattice Gauge Theory

## Logical Role

- Role in the monograph: define compact lattice gauge theory as a
  nonperturbative finite-regulator path integral.
- Immediate predecessor: continuum limits and scaling windows.
- Immediate successor: Monte Carlo/sign problems and rigorous lattice RG.

## Definitions And Results

- Link variables and lattice gauge transformations.
- Plaquette holonomy.
- Wilson plaquette action and Haar-measure partition function.
- Finite periodic \(\mathbb Z_2\) gauge model as a fully explicit compact
  gauge benchmark.
- Exact finite \(\mathbb Z_2\) character expansion: partition function as
  closed plaquette surfaces and Wilson-loop expectation as surfaces with
  prescribed boundary.
- Continuum expansion of plaquette holonomy.
- Wilson loop operators.
- Reflection positivity and transfer-matrix statement.
- Fermion and chiral-gauge-theory regulator boundary.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(U_\mu(x)\) | gauge link variable |
| \(U_{\mu\nu}(x)\) | plaquette holonomy |
| \(S_W\) | Wilson lattice action |
| \(\beta\) | lattice gauge coupling parameter |
| \(W_R(C)\) | Wilson loop in representation \(R\) |
| \(T=e^{-aH}\) | transfer matrix |
| \(U_e,U_p\) | \(\mathbb Z_2\) link variable and plaquette product |
| \(t=\tanh\beta\) | strong-coupling expansion coordinate |
| \(A\subset P\) | plaquette subset / \(\mathbb Z_2\)-two-chain |

## Claim Ledger

1. Wilson lattice gauge theory is a gauge-invariant compact group integral at
   finite cutoff.
2. The plaquette expansion matches the continuum Yang--Mills action after
   fixing trace normalization.
3. Wilson loops are finite-regulator gauge-invariant line probes.
4. The finite \(\mathbb Z_2\) character expansion is an exact surface
   representation at finite cutoff: \(Z\) sums closed plaquette surfaces and
   \(\langle W(C)\rangle\) sums surfaces with boundary \(C\).
5. Chiral gauge theories require additional determinant-phase and anomaly
   control beyond the vectorlike Wilson action.

## Companion Scripts

- `qft_scripts/z2_gauge_3d_metropolis.py --smoke`: finite periodic
  three-dimensional \(\mathbb Z_2\) gauge sampler for plaquette and
  rectangular Wilson-loop measurements.

## Calculation Checks

- `calculation-checks/z2_gauge_metropolis_checks.py` verifies the local
  link-flip plaquette-score change, detailed balance, gauge invariance, and
  the \(1\times1\) Wilson-loop/plaquette identity used by the companion
  script.

## Figures

- Plaquette orientation diagram may be added later.
