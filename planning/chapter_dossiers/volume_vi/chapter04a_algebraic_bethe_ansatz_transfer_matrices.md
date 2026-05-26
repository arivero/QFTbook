# Volume VI, Chapter 4A Dossier: Algebraic Bethe Ansatz and Transfer Matrices

## Logical Role

- Role in the monograph: build the finite-dimensional transfer-matrix
  machinery that non-diagonal integrable QFT needs before matrix Bethe--Yang
  equations and nested TBA can be stated.
- Immediate predecessor: Yang--Baxter consistency and internal symmetry.
- Immediate successor: nested Bethe ansatz and matrix Bethe--Yang equations.

## Definitions And Results

- Auxiliary space, quantum space, inhomogeneous monodromy matrix.
- RTT relation derived by moving an auxiliary \(R\)-matrix through the
  monodromy product one site at a time.
- Transfer matrix as an auxiliary trace.
- Transfer-matrix commutativity from RTT and finite-dimensional trace
  cyclicity.
- Rational \(SU(2)\) \(R(u)=u\,1+iP\) normalization.
- \(XXX_{1/2}\) algebraic Bethe ansatz, including the \(A,B,C,D\)
  decomposition, pseudovacuum actions, Bethe vector, transfer eigenvalue,
  and Bethe equations.
- Pole-cancellation interpretation of the Bethe equations.
- Hamiltonian, energy, and momentum normalization used in the calculation
  checks.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(V\) | finite-dimensional auxiliary or one-site space |
| \(R(u)\) | spectral-parameter \(R\)-matrix |
| \(V_0,V_{0'}\) | auxiliary spaces |
| \(\mathcal H_L\) | \(L\)-site quantum space |
| \(T_0(u)\) | monodromy matrix |
| \(t(u)\) | transfer matrix \(\operatorname{tr}_{V_0}T_0(u)\) |
| \(A,B,C,D\) | entries of the \(SU(2)\) monodromy matrix |
| \(\Omega_L\) | ferromagnetic reference vector |
| \(u_j\) | Bethe roots |
| \(H_{XXX}\) | periodic \(XXX_{1/2}\) Hamiltonian |

## Claim Ledger

1. The RTT relation follows directly from the Yang--Baxter equation applied at
   each quantum site.
2. Transfer matrices commute because RTT permits conjugation inside the
   auxiliary trace.
3. The rational \(SU(2)\) \(R\)-matrix satisfies the Yang--Baxter equation by
   symmetric-group flip relations.
4. The unwanted terms in the algebraic Bethe ansatz vanish exactly when the
   Bethe equations hold.
5. The transfer eigenvalue is polynomial exactly when the apparent poles at
   Bethe roots cancel.
6. The displayed Hamiltonian normalization gives
   \(E=\sum_j(u_j^2+1/4)^{-1}\).

## Calculation Checks

- `calculation-checks/nested_bethe_ansatz_checks.py` checks the rational
  Yang--Baxter equation, transfer-matrix commutativity, one-magnon spectra at
  \(L=4,6,8\), and \(TQ\) pole cancellation.

## Figures

- None in this chapter.
