# 2026-05-27 Issue 494: Ising TFFSA Connected Spin Block

## Scope

This pass continues issue #494 by adding a reader-facing finite TFFSA-style
benchmark for the massive Ising spin perturbation.  It is deliberately a
finite connected-block normalization check, not a production computation of
the magnetic-Ising spectrum.

Touched files:

- `qft_scripts/tffsa_ising_spin_connected.py`
- `qft_scripts/README.md`
- `tools/run_qft_scripts_smoke.sh`
- `calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `calculation-checks/README.md`
- `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`
- `planning/chapter_dossiers/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.md`
- `planning/build_audits/2026-05-27_issue494_tffsa_ising_spin_connected.md`

## Manuscript Content

- Added a zero-momentum connected TFFSA block with basis
  `vacuum + two-particle pairs`.
- Declared all symbols: mode labels, rapidities, free energies, densities,
  diagonal convention, and crossed connected form-factor entries.
- Proved the finite matrix is Hermitian and that the zero-coupling spectrum
  is the free finite-volume spectrum.
- Connected the script to the benchmark protocol.

## Companion Script

Added `qft_scripts/tffsa_ising_spin_connected.py`.

The script:

- constructs the finite zero-total-momentum basis;
- assembles off-diagonal spin-field matrix elements from the even Ising
  form-factor family and free Bethe-state density factors;
- keeps the disconnected vacuum-expectation diagonal convention explicitly;
- checks Hermiticity in smoke mode;
- emits JSON with finite eigenvalues and free energies.

## Verification

- `python3 qft_scripts/tffsa_ising_spin_connected.py --smoke`: passed.
- `python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py`:
  passed.
- `python3 -m py_compile qft_scripts/tffsa_ising_spin_connected.py
  calculation-checks/hamiltonian_truncation_dlcq_checks.py`: passed.
- `tools/run_qft_scripts_smoke.sh`: passed, including the new TFFSA
  connected-block script.
- `git diff --check`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed and rebuilt `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`: `Pages: 2092`.
