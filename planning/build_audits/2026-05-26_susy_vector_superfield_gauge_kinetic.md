# Build Audit: SUSY Vector-Superfield Gauge Kinetic Coefficient

- Date: 2026-05-26.
- Branch: `codex/susy-gauge-dynamics-localization`.
- Scope: Volume VII Chapter 2 superspace/vector-superfield convention check.

## Substantive Edits

- Added a self-contained derivation of the bosonic
  \(\theta^2\)-coefficient of \(W^\alpha W_\alpha\) in Abelian
  Wess--Zumino gauge, including the inverse epsilon-raising convention,
  ordered-pair versus unrestricted antisymmetric summation, and the
  \(\sigma^{\mu\nu}\)-matrix contraction.
- Added `calculation-checks/susy_vector_superfield_checks.py`, an exact
  finite exterior-algebra script checking the spinor-index convention and the
  recovery of
  \(-F_{\mu\nu}F^{\mu\nu}/(4g^2)+D^2/(2g^2)\) after adding the Hermitian
  conjugate.
- Updated the Chapter 2 dossier and calculation-check index.

## Verification

- `python3 calculation-checks/susy_vector_superfield_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_vector_superfield_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the new
  vector-superfield check.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed after this audit note update.
- `tools/build_monograph.sh`: passed after replacing one long typewriter path
  in Chapter 2; final log scan clean.
- Post-rebase `tools/build_monograph.sh`: passed; final log scan clean.
- Built PDF: `monograph/tex/main.pdf`, 1950 pages, 7,799,946 bytes, created
  Tue May 26 22:59:48 2026 EDT.
