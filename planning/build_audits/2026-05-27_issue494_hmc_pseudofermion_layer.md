# 2026-05-27 Issue 494: HMC And Pseudofermion Finite-Regulator Layer

## Scope

Issue #494 asks for production-grade numerical infrastructure and careful
finite-regulator statements.  This pass strengthens Volume XI, Chapter 6 by
adding the theorem-level HMC/RHMC layer that was previously absent from the
Monte Carlo chapter.

Touched files:

- `monograph/tex/volumes/volume_xi/chapter06_monte_carlo_and_sign_problems.tex`
- `calculation-checks/hmc_pseudofermion_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_xi/chapter06_monte_carlo_and_sign_problems.md`
- `planning/build_audits/2026-05-27_issue494_hmc_pseudofermion_layer.md`

## Mathematical Content Added

- Added a finite-regulator HMC setup for a configuration manifold
  \(Q_\Lambda\), target measure \(Z^{-1}e^{-S(q)}dq\), phase space
  \(\Gamma_\Lambda\), Hamiltonian \(H\), reference measure \(d\lambda\), and
  momentum-flip involution \(R\).
- Proved the HMC Metropolis-correction theorem from the precise hypotheses:
  \(\Phi_*(d\lambda)=d\lambda\) and \(R\Phi R=\Phi^{-1}\).  The proof uses
  the involutive proposal \(G=R\Phi\) and the pairwise identity
  \(e^{-H(z)}a(z)=e^{-H(Gz)}a(Gz)\).
- Proved leapfrog volume preservation and reversibility in finite Euclidean
  phase space by explicit kick/drift Jacobians and conjugation by \(R\).
- Explained the compact-gauge HMC analogue on a finite cotangent bundle with
  Haar/Liouville measure, while separating force construction and ergodicity
  from the detailed-balance theorem.
- Proved the pseudofermion determinant identity
  \(\int_{\mathbb C^N}e^{-\phi^\dagger A^{-1}\phi}\,d^{2N}\phi=\pi^N\det A\)
  for positive Hermitian finite matrices.
- Stated RHMC as exact sampling of the rationalized finite determinant
  \(1/\det r_m(A)\), and separated this exact statement from any
  approximation or reweighting claim for \(\det A^\alpha\).
- Added the pointwise RHMC spectral action-error bound
  \(|\phi^\dagger(r_m(A)-A^{-\alpha})\phi|\le\delta\|\phi\|^2\).

## Calculation Check

Added `calculation-checks/hmc_pseudofermion_checks.py`, which verifies:

- determinant one for one-dimensional quadratic leapfrog;
- \(RLR=L^{-1}\) for the same leapfrog map;
- pairwise Metropolis balance in both energy orderings;
- the diagonalized pseudofermion determinant factor;
- the rational pseudofermion action-error bound.

## Verification

- `python3 calculation-checks/hmc_pseudofermion_checks.py`: passed; printed
  `All HMC and pseudofermion checks passed.`
- `python3 -m py_compile calculation-checks/hmc_pseudofermion_checks.py`:
  passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2088`.
