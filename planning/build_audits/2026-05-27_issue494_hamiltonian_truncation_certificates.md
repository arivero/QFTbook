# 2026-05-27 Issue 494: Hamiltonian-Truncation Spectral Certificates

## Scope

This pass continues issue #494 by strengthening the Hamiltonian truncation
and DLCQ chapter with finite-matrix certification statements.  The goal is to
make the numerical scripts mathematically interpretable before any continuum
claim is attempted.

Touched files:

- `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`
- `calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.md`
- `planning/build_audits/2026-05-27_issue494_hamiltonian_truncation_certificates.md`

## Manuscript Content

- Added `Finite-Matrix Spectral Certificates`.
- Defined residual certificates for finite Hermitian truncation matrices.
- Proved that a residual bounds the distance to the finite spectrum.
- Proved a spectral-projector leakage estimate when the target cluster is
  separated from the rest of the finite spectrum.
- Recorded the exact finite Schur self-energy and the separate obligation to
  bound the error made when it is replaced by a local counterterm.

## Companion Check

Added `calculation-checks/hamiltonian_truncation_dlcq_checks.py`.

The check verifies:

- the Ising energy-deformation Bogoliubov block spectrum through the public
  `qft_scripts/tcsa_ising_energy_benchmark.py` module;
- the finite large-\(N\) two-dimensional QCD DLCQ quadratic-form identity
  through `qft_scripts/thooft_dlcq.py`;
- the residual-to-spectrum certificate;
- the spectral-projector leakage estimate;
- the Feshbach determinant identity for a finite Hermitian block matrix.

## Verification

- `python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py`:
  passed.
- `python3 -m py_compile
  calculation-checks/hamiltonian_truncation_dlcq_checks.py`: passed.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2091`.
