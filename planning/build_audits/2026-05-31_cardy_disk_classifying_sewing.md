# Cardy Disk Classifying Sewing Pass

Date: 2026-05-31

GitHub issue: #697, Volume V CFT quoted-theorem proof debt.

## Scope

Volume V, Chapter 14 already displayed the boundary four-point
Cardy--Lewellen equation and recorded the Frobenius-algebra mechanism for
rational BCFT.  The diagonal Cardy disk one-point discussion still compressed
one low-genus sewing constraint into the statement that disk one-point
functions solve bulk-boundary sewing because the modular \(S\)-matrix
diagonalizes fusion.

## Change

Expanded the diagonal Cardy disk sewing mechanism:

- separated the raw disk coefficient \(B_a{}^i=S_{ai}/\sqrt{S_{0i}}\) from
  the normalized classifying coordinate
  \(\widehat B_a(i)=\sqrt{S_{0i}}B_a{}^i/S_{0a}\);
- identified \(\widehat B_a(i)=S_{ia}/S_{0a}\) as the Verlinde fusion-ring
  character in the diagonal Cardy theory;
- wrote the classifying-algebra product \(e_i e_j=\sum_k N_{ij}{}^k e_k\);
- wrote the disk two-bulk identity-channel sewing equation
  \(\chi_a(e_i e_j)=\chi_a(e_i)\chi_a(e_j)\);
- explained that this is a normalized classifying-algebra statement, not an
  equality between raw physical bulk OPE constants and fusion coefficients.

## Calculation Check

Extended `calculation-checks/bcft_cardy_checks.py` to verify in the Ising
Cardy example that the normalized disk coordinate equals the Verlinde fusion
character and obeys the two-bulk classifying sewing identity exactly.
