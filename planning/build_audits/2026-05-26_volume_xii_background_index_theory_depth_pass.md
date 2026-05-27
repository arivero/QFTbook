# Volume XII Chapter 6 Background Index-Theory Depth Pass

Date: 2026-05-26.

## Scope

- Replaced the thin background-gauge-field and index-theory chapter with a self-contained development of the analytic index of the chiral Dirac operator, including the Euclidean spinor and bundle conventions used later in anomaly calculations.
- Added an explicit McKean--Singer supertrace proof that the heat-kernel supertrace is the Fredholm index, separating the proven functional-analytic step from the differential-geometric local index theorem that is used as a theorem input.
- Fixed the convention ledger for characteristic classes, distinguishing skew-Hermitian mathematical curvature from Hermitian physics curvature and distinguishing representation traces in the Chern character from the Yang--Mills kinetic trace convention.
- Added worked four-dimensional examples: SU(N) instanton indices in trace-delta normalization, the SU(2) fundamental and adjoint special cases, chirality reversal under orientation reversal, and an Abelian line-bundle flux index on T4.
- Added a finite-dimensional Berezin proof of the fermion zero-mode selection rule and connected it to the instanton 't Hooft vertex without treating Grassmann integration as an ordinary measure.
- Expanded the anomaly-polynomial and descent discussion with explicit four-dimensional terms and a determinant-line formulation of local curvature and global holonomy anomalies.

## Calculation Checks

- Added `calculation-checks/background_index_theory_checks.py` for exact rational checks of the four-dimensional index density, SU(N) trace-delta instanton indices, Abelian T4 flux index, six-form anomaly-polynomial coefficients, descent normalization, and Dirac zero-mode counting.
- Updated `calculation-checks/README.md` so the new script is part of the public calculation-check inventory.
- Cross-checked the new chapter against the existing anomaly-descent and BPST-instanton normalization scripts.

## Verification

- `python3 calculation-checks/background_index_theory_checks.py`
- `python3 -m py_compile calculation-checks/background_index_theory_checks.py`
- `python3 calculation-checks/anomaly_polynomial_descent_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/build_monograph.sh`

The first full build after the large rewrite failed the log scan because one theorem sentence produced an overfull hbox. The theorem statement was reformatted with a displayed local-density formula, after which the full monograph build and log scan were clean.

The clean build produced `monograph/tex/main.pdf` with 1828 pages, creation time Tue May 26 20:42:59 2026 EDT, and file size 7,276,858 bytes.

## Residual Work

- Add a figure or commutative diagram for the determinant line, its Bismut--Freed connection, and eta-invariant holonomy once the surrounding families-index material is expanded.
- Return in a later anomaly-line pass to the interacting-QFT status of determinant lines and relative theories, where the current chapter intentionally records the geometric free-fermion model rather than claiming a general non-perturbative theorem.
