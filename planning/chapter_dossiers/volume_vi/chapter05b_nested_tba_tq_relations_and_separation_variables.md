# Volume VI, Chapter 5B Dossier: Nested TBA, Baxter Relations, and Separation Variables

## Logical Role

- Role in the monograph: extend diagonal TBA to physical and auxiliary root
  densities, then connect Bethe equations to Baxter \(TQ\), Y-system, and
  separation-of-variables structures.
- Immediate predecessor: thermodynamic Bethe ansatz.
- Immediate successor: integrable RG flows and perturbed CFT.

## Definitions And Results

- Logarithmic nested equations for physical and auxiliary roots.
- Physical densities, auxiliary densities, and convolution kernels.
- Variational derivation of nested TBA pseudoenergy equations.
- Constant \(A_2\) magnonic Y-system example and golden-ratio plateau.
- Baxter polynomial and \(TQ\) relation for the \(XXX_{1/2}\) chain.
- Proof that polynomial \(TQ\) eigenvalues are equivalent to the Bethe
  equations for simple roots.
- Rank-one Baxter Casoratian/second-solution mechanism:
  \(\mathcal W^+/\mathcal W^-=a/d\) for two solutions of the same
  second-order finite-difference equation.
- Higher-rank \(T\)-system/Hirota relation.
- \(Q\)-operator and separation-of-variables definitions with proof boundary.
- Trigonometric rank-one \(q\)-oscillator \(L\)-operator in explicit
  six-vertex normalization, including the local RLL identity and the Fock
  realization of the Borel \(q\)-oscillator generators.
- Interface statement separating relativistic integrable QFT from planar
  gauge-theory integrability.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\rho_a,\rho_a^h\) | physical particle and hole densities |
| \(\sigma_r,\sigma_r^h\) | auxiliary root and hole densities |
| \(K_{AB}\) | derivative kernel coupling density labels |
| \(\epsilon_a,\eta_r\) | physical and auxiliary pseudoenergies |
| \(Y_A\) | plateau Y-function value |
| \(Q(u)\) | Baxter polynomial or \(Q\)-operator eigenvalue |
| \(\mathcal W[Q_1,Q_2]\) | half-shift Casoratian of two rank-one Baxter solutions |
| \(T_{a,s}(u)\) | transfer functions in a \(T\)-system |
| \(x_\alpha\) | separated variables |
| \(D,\mathsf a,\mathsf a^\dagger\) | q-oscillator Fock generators |
| \(L_{\mathcal F}^{(+)}(x)\) | trigonometric rank-one q-oscillator auxiliary \(L\)-operator |

## Claim Ledger

1. Nested TBA follows from the same entropy variation as diagonal TBA after
   physical and auxiliary densities are included in one constrained system.
2. Auxiliary roots enter the free energy through constraints because they do
   not carry direct one-particle energy in the examples treated here.
3. The constant \(A_2\) Y-system has the symmetric golden-ratio solution.
4. The \(XXX_{1/2}\) Bethe equations are equivalent to pole cancellation in
   the Baxter \(TQ\) equation for simple roots.
5. The Baxter Casoratian of two rank-one solutions obeys the first-order
   transport equation \(d\,\mathcal W^+=a\,\mathcal W^-\), making explicit the
   second-solution datum behind higher-rank Wronskian \(Q\)-systems.
6. The trigonometric rank-one q-oscillator \(L\)-operator satisfies the local
   six-vertex RLL identity in the stated normalization.
7. \(Q\)-operator and separation-of-variables constructions require
   representation-specific completeness theorems not supplied by the RTT
   algebra alone.

## Calculation Checks

- `calculation-checks/nested_bethe_ansatz_checks.py` verifies the \(TQ\)
  pole-cancellation calculation paired with this chapter.
- `calculation-checks/nested_integrability_checks.py` verifies the nested
  Cartan-form Bethe equations, dressed-vacuum pole cancellation, QQ/Hirota
  algebra, rank-one Baxter Casoratian transport, and the exact finite-basis
  q-oscillator local RLL convention.

## Audit Notes

- 2026-06-01 Vol VI/Q-system depth pass: inserted the Baxter Casoratian
  second-solution mechanism between the scalar \(TQ\) relation and the
  higher-rank QQ-system, so the later Wronskian/QSC language has an explicit
  finite-difference prototype with a paired exact recurrence check.

## Figures

- None in this chapter.
