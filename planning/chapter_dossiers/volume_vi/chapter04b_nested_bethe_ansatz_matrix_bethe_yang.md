# Volume VI, Chapter 4B Dossier: Nested Bethe Ansatz and Matrix Bethe--Yang Equations

## Logical Role

- Role in the monograph: replace scalar Bethe--Yang phases by internal
  transfer-matrix eigenvalues and introduce nested roots for non-diagonal
  finite-volume scattering.
- Immediate predecessor: algebraic Bethe ansatz and transfer matrices.
- Immediate successor: form-factor bootstrap and local operators.

## Definitions And Results

- Matrix Bethe--Yang state and quantization equation.
- \(SU(N)\) nested Bethe roots attached to \(A_{N-1}\) Dynkin levels.
- Nested \(SU(N)\) Bethe equations in the rational normalization compatible
  with the \(XXX_{1/2}\) chapter.
- Proof that the equations are pole-cancellation conditions obtained by
  successive auxiliary transfer-matrix diagonalization.
- Exact \(SU(3)\), \(L=6\), \(M_1=2\), \(M_2=1\) worked configuration.
- Relativistic matrix Bethe--Yang equation with scalar and matrix scattering
  factors separated.
- Large-volume regime stated as a controlled approximation.
- Principal chiral model and Gross--Neveu family interpretation of auxiliary
  roots.

## Symbols

| Symbol | Meaning |
| --- | --- |
| \(\mathcal V_{\boldsymbol a}\) | internal species tensor product |
| \(\mathcal T_j\) | internal transfer matrix for transporting particle \(j\) |
| \(\tau_j\) | transfer-matrix eigenvalue |
| \(u_j^{(r)}\) | nested Bethe root at level \(r\) |
| \(M_r\) | number of roots at nesting level \(r\) |
| \(S_0(\theta)\) | scalar factor in a relativistic \(S\)-matrix |
| \(\widehat R(\theta)\) | matrix part of a relativistic \(S\)-matrix |

## Claim Ledger

1. Matrix Bethe--Yang quantization is scalar finite-volume phase times an
   internal transfer-matrix eigenvalue.
2. Auxiliary roots parametrize internal wavefunctions; they are not additional
   Hilbert-space particles.
3. The rational \(SU(N)\) nested equations follow from recursive
   pole-cancellation in auxiliary transfer matrices.
4. The \(SU(3)\) worked roots satisfy both first- and second-level equations
   and have energy \(E=2\).
5. Relativistic non-diagonal finite-volume equations require a stated
   large-volume regime; wrapping corrections belong to TBA.

## Calculation Checks

- `calculation-checks/nested_bethe_ansatz_checks.py` verifies the displayed
  \(SU(3)\) nested-root solution and energy.

## Figures

- None in this chapter.
