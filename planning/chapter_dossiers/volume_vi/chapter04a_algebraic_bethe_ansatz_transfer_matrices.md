# Volume VI, Chapter 4A Dossier: Algebraic Bethe Ansatz and Transfer Matrices
Source-File: monograph/tex/volumes/volume_vi/chapter04a_algebraic_bethe_ansatz_transfer_matrices.tex

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
  cyclicity, with partial trace over auxiliary spaces separated from the
  noncommutative quantum-space operator product.
- Rational \(SU(2)\) \(R(u)=u\,1+iP\) normalization.
- \(XXX_{1/2}\) algebraic Bethe ansatz, including the \(A,B,C,D\)
  decomposition, pseudovacuum actions, corrected \(AB/DB\) exchange signs in
  the \(R(u)=u1+iP\), \(L(u)=R(u-i/2)\) convention, Bethe vector, transfer
  eigenvalue, and Bethe equations.
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
   auxiliary trace; the proof uses cyclicity only in \(V_0\otimes V_{0'}\),
   not in the quantum space \(\mathcal H_L\).
3. The rational \(SU(2)\) \(R\)-matrix satisfies the Yang--Baxter equation by
   symmetric-group flip relations.
4. The component RTT relations give
   \(A(u)B(v)=\frac{u-v-i}{u-v}B(v)A(u)+\frac{i}{u-v}B(u)A(v)\) and
   \(D(u)B(v)=\frac{u-v+i}{u-v}B(v)D(u)-\frac{i}{u-v}B(u)D(v)\) in the
   chapter convention.
5. The unwanted terms in the algebraic Bethe ansatz vanish exactly when the
   Bethe equations hold.
6. The transfer eigenvalue is polynomial exactly when the apparent poles at
   Bethe roots cancel.
7. The displayed Hamiltonian normalization gives
   \(E=\sum_j(u_j^2+1/4)^{-1}\).

## Calculation Checks

- `calculation-checks/nested_bethe_ansatz_checks.py` checks the rational
  Yang--Baxter equation, transfer-matrix commutativity, the corrected
  \(AB/DB\) exchange signs, one-magnon spectra at \(L=4,6,8\), and \(TQ\)
  pole cancellation.

## Figures

- None in this chapter.

## Audit Notes

- 2026-05-30 partial-trace proof pass: retained transfer-matrix
  commutativity as proposition-level finite-dimensional integrability
  machinery, but expanded the proof so that the equality
  \(t(u)t(v)=\operatorname{tr}_{0,0'}T_0(u)T_{0'}(v)\), auxiliary-only trace
  cyclicity, and meromorphic continuation off the invertibility locus are
  explicit.
