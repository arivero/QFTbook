# Issue 494 scalar Hamiltonian-truncation benchmark pass

Date: 2026-06-01

Issue context: GitHub #494, numerical methods with reader-facing finite
regulator scripts.

## Scope

This pass adds a nonintegrable scalar Hamiltonian-truncation benchmark to the
Volume XI numerical-methods program.  The existing Ising energy benchmark is
exactly solvable; the new script and manuscript section instead construct the
finite normal-ordered \(1+1\)-dimensional \(\phi^4\) matrix in a free massive
Fock basis.  The finite datum records:

- Fourier-mode cutoff \(N\);
- particle-number cutoff \(P_{\max}\);
- free-energy cutoff \(E_{\rm cut}\);
- total momentum sector \(P_{\rm tot}\);
- normal ordering relative to the massive free vacuum;
- the projected matrix
  \(H_\Lambda=H_0+\lambda P_\Lambda\int:\phi_N^4:/4! P_\Lambda\).

The manuscript derives the mode-expanded finite interaction, states why the
projected matrix is Hermitian at finite cutoff, and gives a zero-mode
normalization check
\[
  \bra2\int_0^L:\phi_0(x)^4:\,\dd x\ket2=\frac{3}{Lm^2}.
\]
The text explicitly separates this finite regulator benchmark from any
continuum \(\phi^4_2\) claim, which still requires counterterms and cutoff
analysis.

## Files

- `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`
- `qft_scripts/phi4_hamiltonian_truncation.py`
- `qft_scripts/README.md`
- `tools/run_qft_scripts_smoke.sh`
- `calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.md`

## Verification

- `python3 qft_scripts/phi4_hamiltonian_truncation.py --smoke`
- `python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `python3 -m py_compile qft_scripts/phi4_hamiltonian_truncation.py calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2830 pages.

## Closure status

Issue #494 remains open.  This pass closes the missing nonintegrable scalar
finite-matrix benchmark slice, but the broader numerical-methods program can
still be deepened with production continuum extrapolations, larger
nonintegrable spectra, and cluster-scale examples.
