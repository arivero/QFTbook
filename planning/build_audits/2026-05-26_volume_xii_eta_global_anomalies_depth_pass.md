# Volume XII Chapter 7 Eta-Invariants and Global-Anomalies Depth Pass

Date: 2026-05-26.

## Scope

- Rewrote the eta-invariant/global-anomaly chapter around the actual
  determinant-line holonomy problem rather than a thin sequence of named
  formulae.
- Added definitions of self-adjoint odd-dimensional Dirac operators, eta
  functions, reduced eta invariants, spectral flow, determinant-line fibers,
  Pfaffian lines, and mod-two indices.
- Proved the integer jump of \(\xi=(\eta+h)/2\) at a simple crossing and
  derived the cylinder variation formula for \(\xi\) modulo integers from the
  APS theorem, including the orientation-reversal term
  \(\xi(-B)=-\xi(B)+h(B)\).
- Stated the APS, Bismut--Freed holonomy, and Witten mapping-torus mod-two
  index theorems explicitly as mathematical inputs, with hypotheses and
  convention choices separated from the QFT interpretation.
- Added a TikZ figure showing the APS cylinder and the mapping-torus passage
  from local variation to global holonomy.
- Added a detailed Witten \(SU(2)\) global anomaly example, including the
  trace-delta Dynkin index formula, the \(2j\equiv1\pmod4\) parity criterion,
  first representation table, and the distinction between vanishing local
  cubic anomaly and nontrivial Pfaffian holonomy.
- Rewrote the Dai--Freed inflow discussion as a boundary-line
  trivialization statement and kept the interacting-QFT anomaly-line
  construction as an explicit open problem.

## Calculation Checks

- Added `calculation-checks/eta_global_anomaly_checks.py`.
- The script checks APS orientation bookkeeping, the first \(SU(2)\)
  trace-delta Dynkin indices, Witten's parity criterion, Pfaffian-sign
  multiplicativity, vanishing of the \(SU(2)\) cubic weight sum, and cylinder
  congruence arithmetic.
- Updated `calculation-checks/README.md` and the chapter dossier to include
  the new check.

## Verification

- `python3 calculation-checks/eta_global_anomaly_checks.py`
- `python3 -m py_compile calculation-checks/eta_global_anomaly_checks.py`
- `python3 calculation-checks/inflow_anomaly_line_checks.py`
- `python3 calculation-checks/background_index_theory_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/build_monograph.sh`

The first build produced a PDF but failed the final log scan because the
section title `The Witten \(SU(2)\) Global Anomaly` caused a hyperref PDF
bookmark warning.  The title was changed to use `\texorpdfstring`, and the
subsequent full build and log scan were clean.

The clean build produced `monograph/tex/main.pdf` with 1832 pages, creation
time Tue May 26 20:52:42 2026 EDT, and file size 7,294,433 bytes.

## Residual Work

- The APS, Bismut--Freed, and five-dimensional mod-two-index theorems remain
  quoted mathematical inputs.  A later global-analysis appendix could develop
  their proofs at the level needed for the monograph's foundational standard.
- The interacting-QFT anomaly-line open problem remains unresolved; the
  chapter now gives the free-fermion model and the precise structure that a
  general construction must reproduce.
