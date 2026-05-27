# Volume VII, Chapter 1 Dossier: Supersymmetry Algebras And Representations

## Logical Role

- Role in the monograph: begin supersymmetric QFT from the Hilbert-space
  algebra and positivity constraints before superspace or Lagrangians.
- Immediate predecessor: spinor conventions and ordinary spin-statistics
  material from Volumes I and IV.
- Immediate successor: multiplets, superspace, and supersymmetric dynamics.

## Definitions And Results

- Four-dimensional mostly-plus \(\mathcal N=1\) supertranslation algebra.
- Particle supersymmetry representation as a Hilbert-space or one-particle
  spectral-subspace representation.
- Field-variable supersymmetry representation as an action on superfields,
  component variables, antifields, or local functionals.
- Rest-frame oscillator construction for massive representations.
- Massive \(\mathcal N=1\) oscillator module
  \(V_j\otimes\Lambda^\bullet\mathbb C^2\), including dimensions and
  little-group spin decomposition.
- Positivity of the supercharge anticommutator and equality of bosonic and
  fermionic state counts in a nonzero-energy multiplet.
- Massless helicity-pair construction from the rank-one supercharge norm
  matrix.
- Central charges and the BPS inequality for extended supersymmetry,
  derived from singular values of the rest-frame anticommutator block.
- Frontier boundary between algebraic representation theory and
  nonperturbative supersymmetric QFT realization.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(Q_\alpha\), \(\bar Q_{\dot\alpha}\) | Weyl supercharges |
| \(P_\mu\) | translation generator |
| \(\sigma^\mu_{\alpha\dot\beta}\) | mostly-plus Pauli matrices in the monograph convention |
| \((-1)^F\) | fermion-parity operator |
| \(Z^{IJ}\) | antisymmetric central-charge matrix |
| \(z_s\) | singular values of the central-charge matrix |
| \(M\) | invariant mass of an irreducible representation |

## Claim Ledger

1. Supersymmetry is represented by odd operators on a graded Hilbert space.
2. Positivity of \(\sum_\alpha Q_\alpha Q_\alpha^\dagger\) constrains masses
   and central charges.
3. The equal boson/fermion count follows from a trace with \((-1)^F\), not
   from a Lagrangian counting argument.
4. Massive \(\mathcal N=1\) multiplets are finite Clifford modules
   \(V_j\otimes\Lambda^\bullet\mathbb C^2\), with two bosonic copies of
   \(V_j\) and fermionic \(V_{j+1/2}\oplus V_{j-1/2}\) after
   little-group decomposition.
5. Massless \(\mathcal N=1\) multiplets have one null supercharge
   combination quotiented out, leaving a single fermionic oscillator and a
   helicity pair before CPT completion.
6. Multiplet shortening requires the central-charge inequality to be saturated.
   The inequality is the positivity condition \(m\ge z_s\) for every
   singular value of the central-charge matrix.
7. A particle supermultiplet is not the same object as an off-shell
   superfield multiplet; relating them requires dynamics, constraints,
   quotienting, and Hilbert-space or Euclidean reconstruction.

## Calculation Checks

- `calculation-checks/susy_representation_checks.py` verifies massive
  \(\mathcal N=1\) Fock dimensions, boson/fermion balance, the
  Clebsch--Gordan dimension identity for the one-oscillator spin sector, the
  rank-one massless norm matrix, and BPS-bound block eigenvalues
  \(2(m\pm z)\).

## Figures

- Massive rest-frame Clifford module diagram.
- Massless helicity multiplet ladder.
- BPS bound plane showing long and shortened representations.
