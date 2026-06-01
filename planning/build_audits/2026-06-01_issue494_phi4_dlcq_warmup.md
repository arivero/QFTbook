# Issue 494 scalar DLCQ warmup pass

Date: 2026-06-01

Issue context: GitHub #494, numerical methods with reader-facing finite
regulator scripts.

## Scope

This pass adds the \(1+1\)-dimensional scalar \(\phi^4\) DLCQ warmup requested
in the numerical-methods issue.  The finite construction works at fixed
harmonic resolution \(K\), keeps only positive longitudinal momenta, and makes
the omission of the \(p^+=0\) mode an explicit regulator choice.

The manuscript defines:

- positive-longitudinal bosonic occupation vectors
  \(\sum_{n=1}^K nN_n=K\);
- the free invariant mass \(M^2_{0,K}=Km^2\sum_nN_n/n\);
- the normal-ordered quartic operator \(Q_K\) with coefficient
  \(1/\sqrt{n_1n_2n_3n_4}\) and longitudinal momentum conservation;
- the finite matrix \(M_K^2=M_{0,K}^2+gK P_KQ_KP_K\);
- the zero-mode and \(K\to\infty\) counterterm obligations as separate
  continuum data.

It also derives the convention checks
\[
  \bra3Q_3\ket{1,1,1}=4\sqrt2,\qquad
  \bra{1,1,1}Q_3\ket{1,1,1}=36.
\]

## Files

- `monograph/tex/volumes/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.tex`
- `qft_scripts/phi4_dlcq.py`
- `qft_scripts/README.md`
- `tools/run_qft_scripts_smoke.sh`
- `calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `calculation-checks/README.md`
- `planning/chapter_dossiers/volume_xi/chapter10_hamiltonian_truncation_dlcq_benchmarks.md`

## Verification

- `python3 qft_scripts/phi4_dlcq.py --smoke`
- `python3 calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `python3 -m py_compile qft_scripts/phi4_dlcq.py calculation-checks/hamiltonian_truncation_dlcq_checks.py`
- `tools/run_qft_scripts_smoke.sh`
- `git diff --check`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `python3 tools/audit_theorem_form.py`
- `python3 tools/audit_unnumbered_display_labels.py`
- `tools/build_monograph.sh`

All checks passed.  The full monograph build completed cleanly at 2832 pages.

## Closure status

Issue #494 remains open.  This pass closes the scalar DLCQ warmup slice, but
the broader numerical-methods program can still be deepened with larger
nonintegrable spectra, systematic continuum extrapolations, and cluster-scale
production examples.
