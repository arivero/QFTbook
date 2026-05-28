# Volume VII, Chapter 1 Dossier: Supersymmetry Algebras And Representations

## Logical Role

- Role in the monograph: begin supersymmetric QFT from the Hilbert-space
  algebra and positivity constraints before superspace or Lagrangians.
- Immediate predecessor: spinor conventions and ordinary spin-statistics
  material from Volumes I and IV.
- Immediate successor: multiplets, superspace, and supersymmetric dynamics.

## Definitions And Results

- Four-dimensional mostly-plus \(\mathcal N=1\) supertranslation algebra.
- Haag--\(\L\)opusza\'nski--Sohnius classification theorem as a conditional
  massive-scattering theorem, with its hypotheses and boundaries stated
  explicitly.
- Direct algebraic derivation of the mixed supercharge anticommutator from
  Lorentz covariance, the Coleman--Mandula vector-charge exclusion, and
  positivity.
- Direct algebraic derivation of the scalar central-charge tensor structure
  \(\epsilon_{\alpha\beta}Z^{IJ}\), including antisymmetry of \(Z^{IJ}\) and
  the internal-invariance condition.
- Particle supersymmetry representation as a Hilbert-space or one-particle
  spectral-subspace representation.
- Field-variable supersymmetry representation as an action on superfields,
  component variables, antifields, or local functionals.
- Proposition that off-shell component fields are not particle states and
  that auxiliary fields contribute no independent one-particle oscillators in
  the free theory.
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
| \(B_A\), \(T_A\) | internal symmetry generator and its action on the supercharge index |
| \(\mathfrak g_{\bar0}\oplus\mathfrak g_{\bar1}\) | finite graded scattering-symmetry algebra |

## Claim Ledger

1. Supersymmetry is represented by odd operators on a graded Hilbert space.
2. The HLS theorem is a conditional classification theorem for finite graded
   symmetries of massive scattering theories, not a universal construction
   theorem for all QFTs.
3. Under the HLS hypotheses, odd generators are Weyl spinors, the mixed
   anticommutator is proportional to \(P_\mu\), and positivity normalizes it
   to \(2\delta^I{}_J\sigma^\mu P_\mu\).
4. The left-left anticommutator has only the scalar central-charge tensor
   \(\epsilon_{\alpha\beta}Z^{IJ}\); \(Z^{IJ}\) is antisymmetric and must be
   invariant under any retained internal symmetry.
5. Positivity of \(\sum_\alpha Q_\alpha Q_\alpha^\dagger\) constrains masses
   and central charges.
6. The equal boson/fermion count follows from a trace with \((-1)^F\), not
   from a Lagrangian counting argument.
7. Massive \(\mathcal N=1\) multiplets are finite Clifford modules
   \(V_j\otimes\Lambda^\bullet\mathbb C^2\), with two bosonic copies of
   \(V_j\) and fermionic \(V_{j+1/2}\oplus V_{j-1/2}\) after
   little-group decomposition.
8. Massless \(\mathcal N=1\) multiplets have one null supercharge
   combination quotiented out, leaving a single fermionic oscillator and a
   helicity pair before CPT completion.
9. Multiplet shortening requires the central-charge inequality to be saturated.
   The inequality is the positivity condition \(m\ge z_s\) for every
   singular value of the central-charge matrix.
10. A particle supermultiplet is not the same object as an off-shell
   superfield multiplet; relating them requires dynamics, constraints,
   quotienting, and Hilbert-space or Euclidean reconstruction.

## Calculation Checks

- `calculation-checks/susy_representation_checks.py` verifies massive
  \(\mathcal N=1\) Fock dimensions, boson/fermion balance, the
  Clebsch--Gordan dimension identity for the one-oscillator spin sector, the
  rank-one massless norm matrix, and BPS-bound block eigenvalues
  \(2(m\pm z)\).  It also checks the HLS central-charge combined-index
  symmetry, the finite \(T Z+Z T^T=0\) internal-invariance condition, and the
  Lorentz-representation dimension ledger for mixed and left-left Weyl
  products.

## Figures

- Massive rest-frame Clifford module diagram.
- Massless helicity multiplet ladder.
- BPS bound plane showing long and shortened representations.
