# Free Fock Nuclearity Benchmark Pass

## Scope

- Continued issue #695, the foundational AQFT proof-debt lane.
- Targeted Volume IV, Chapter 4, in the type-III local algebra and
  phase-space-bound section.

## Finding

The chapter stated the Buchholz--Wichmann nuclearity condition and the
quoted split-consequence theorem, with a functional-analytic mechanism
paragraph.  It benefited from a concrete calculation showing where an
exponential \(\beta^{-s}\) phase-space scale comes from in a familiar QFT
model.

## Change

- Added a free bosonic Fock phase-space benchmark:
  - finite-mode occupation-number trace factorization;
  - torus one-particle energies
    \(\epsilon_n=((2\pi/L)^2|n|^2+m^2)^{1/2}\);
  - logarithmic product formula
    \(\log Z_B=\sum_n-\log(1-\exp[-\beta\epsilon_n])\);
  - sup-norm lattice shell count
    \(N_s(k)=(2k+1)^s-(2k-1)^s\);
  - small-shell/large-shell estimate isolating the logarithmic singularity
    of \(-\log(1-\exp[-x])\) near \(x=0\) from its exponential tail, giving
    \(\log Z_B(\beta,L)\le C_{s,m,L}\beta^{-s}\), \(s=D-1\).
- Kept the theorem boundary honest: the local nuclearity map is not the
  global box Gibbs trace, and the split theorem still requires the local
  operator-algebraic nuclearity/normality argument.
- Added `calculation-checks/free_fock_nuclearity_checks.py`.
- Updated the calculation-check README and chapter dossier.

## Verification

- `python3 calculation-checks/free_fock_nuclearity_checks.py`

## Status

This strengthens the nuclearity/split exposition within #695.  It does not
close #695 because the full quoted-theorem proof-debt lane still includes
OS boundary-value infrastructure, DHR/DR reconstruction, Bisognano--Wichmann,
Borchers--Wiesbrock, nuclearity/split beyond this benchmark, and substantial
interacting examples.
