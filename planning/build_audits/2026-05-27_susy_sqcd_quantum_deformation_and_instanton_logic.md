# Build Audit: SUSY SQCD Quantum Deformation And Instanton Logic

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII's supersymmetric gauge-dynamics material by
making the \(N=1\) SQCD logic more explicit and by expanding Chapter 08's
\(SU(2)\), \(N_f=2\) quantum-modified branch into a self-contained algebraic
derivation.

## Substantive Edits

- Added a Chapter 06 logic-of-argument paragraph explaining that the
  \(N_f=N_c-1\) first-principles instanton calculation is the constructive
  ADS seed, while holomorphy and mass decoupling are controlled extensions
  with separate assumptions.
- Recast the Chapter 08 \(N=1\) SQCD branch table as an orientation ledger,
  not a proof, and defined the microscopic quark, antiquark, meson, baryon,
  and quotient-coordinate conventions before using the ledger.
- Added a proposition for the \(SU(2)\), \(N_f=2\) quantum-deformed
  Pfaffian branch: the Wilsonian deformation is stated as input, smoothness
  is proved by the Pfaffian gradient, a nondegenerate mass source is reduced
  to Darboux form, the constrained \(F\)-terms are solved, and the two
  superpotential values are matched to pure \(SU(2)\) by holomorphic
  threshold scale matching.
- Extended `calculation-checks/susy_moduli_space_checks.py` with exact
  rational checks for Pfaffian-gradient signs, smoothness away from the
  origin, the two massive vacua, and
  \(\Lambda_0^6=m_1m_2\Lambda_h^4\).
- Updated the Chapter 06 and Chapter 08 dossiers and the calculation-check
  README.

## Verification

- `python3 calculation-checks/susy_moduli_space_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the updated
  moduli-space checks and the Wolfram gamma-trace gate.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean before the audit note; rerun after this note was
  added.
- `tools/build_monograph.sh`: passed; generated `monograph/tex/main.pdf`
  with 1973 pages and file size 7900498 bytes after rebasing onto
  `origin/main`.
