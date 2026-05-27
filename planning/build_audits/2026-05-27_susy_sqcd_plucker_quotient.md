# Build Audit: SUSY SQCD Plucker Quotient

Date: 2026-05-27

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 08, `Moduli Spaces In
Supersymmetric Quantum Field Theory`, by expanding the `N=1` SQCD branch
discussion with a fully worked classical quotient benchmark for
\(SU(2)\), \(N_f=2\).

## Substantive Edits

- Added a proposition constructing the classical \(SU(2)\), \(N_f=2\)
  affine chiral quotient from four doublets \(P_a^I\) and the antisymmetric
  gauge invariants \(V^{IJ}=\epsilon^{ab}P_a^I P_b^J\).
- Fixed the Pfaffian convention
  \(\operatorname{Pf}(V)=V^{12}V^{34}-V^{13}V^{24}+V^{14}V^{23}\) and proved
  that the reduced quotient is the Plucker hypersurface
  \(\operatorname{Pf}(V)=0\subset\bigwedge^2\mathbb C^4\).
- Included the converse reconstruction on a \(V^{12}\neq0\) chart, the
  invariant-ring generation explanation for \(SL(2,\mathbb C)\) doublets,
  and the dimension check \(6-1=8-3=5\).
- Extended `calculation-checks/susy_moduli_space_checks.py` with exact
  rational checks for the decomposable-two-form Pfaffian identity, the
  explicit converse reconstruction chart, and the quotient dimension ledger.
- Updated the Chapter 08 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_moduli_space_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the updated
  moduli-space quotient checks and the Wolfram gamma-trace gate.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean before the audit note; rerun after this note was
  added.
- `tools/build_monograph.sh`: passed; generated `monograph/tex/main.pdf`
  with 1967 pages and file size 7876855 bytes after rebasing onto
  `origin/main`.
