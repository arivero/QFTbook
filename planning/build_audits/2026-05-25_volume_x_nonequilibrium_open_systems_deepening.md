# Volume X Nonequilibrium Open-System Deepening Audit

## Scope

This pass addresses the later-volume thinness directive for Volume X,
Chapter 10.  The chapter is rewritten from a definition-level sketch into a
derivation-level treatment of nonequilibrium steady states, reservoir
entropy production, weak-coupling GKSL limits, Schwinger-Keldysh influence
functionals, and Markovian hydrodynamic relaxation.

## Edits

- Rewrote
  `monograph/tex/volumes/volume_x/chapter10_nonequilibrium_steady_states_open_systems.tex`.
- Defined steady states as positive invariant functionals and reservoir
  steady states as local weak limits.
- Derived the reservoir entropy-production formula with explicit current
  sign convention.
- Added the linear-response force vector and Onsager positivity statement.
- Added the weak-coupling Hamiltonian setup, Hermitian coupling convention,
  bath spectral matrices, Bohr-frequency decomposition, and Davies/GKSL
  generator.
- Proved positivity of the bath spectral matrix by the positive-type
  function and Bochner argument.
- Stated the finite-dimensional van Hove/Davies-limit hypotheses used in the
  chapter.
- Proved trace preservation and complete positivity of the finite-dimensional
  GKSL semigroup using the Dyson-Phillips jump expansion.
- Derived the KMS detailed-balance ratio by spectral resolution and applied
  it to a two-level system.
- Added the quadratic Schwinger-Keldysh influence functional with explicit
  retarded and noise kernels.
- Derived the Ornstein-Uhlenbeck Einstein relation
  \(D_n=\gamma\chi T\) by the stationary Fokker-Planck current.
- Added `calculation-checks/nonequilibrium_open_system_checks.py` and
  documented it in `calculation-checks/README.md`.
- Rewrote the Volume X Chapter 10 dossier.

## Verification

- `python3 calculation-checks/nonequilibrium_open_system_checks.py` passed.
- `tools/audit_monograph_text.sh` passed.
- `tools/audit_chapter_dossiers.sh` passed.
- `git diff --check` passed.
- `tools/build_monograph.sh` passed.
- `pdfinfo monograph/tex/main.pdf` reports 1324 pages.
