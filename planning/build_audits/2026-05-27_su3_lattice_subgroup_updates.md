# 2026-05-27 SU(3) Lattice Subgroup Updates Audit

## Scope

- Added an explicit \(SU(3)\) link-update section to Volume XI Chapter 6.
- Defined the local \(SU(3)\) staple score
  \(\frac13\operatorname{Re}\operatorname{Tr}_3(U_eV_e)\).
- Explained why the \(SU(2)\) staple polar-form heat-bath reduction does not
  carry over to \(SU(3)\).
- Defined the three embedded \(SU(2)\) color-pair subgroups
  \(H_{12},H_{13},H_{23}\), proved that they generate \(SU(3)\), and stated
  exact finite subgroup heat-bath/Metropolis invariance.
- Added `calculation-checks/su3_lattice_update_checks.py`.

## Checks

- `python3 calculation-checks/su3_lattice_update_checks.py`: passed.
- `python3 -m py_compile calculation-checks/su3_lattice_update_checks.py`:
  passed.
- `git diff --check -- ...`: passed on all touched files in this pass.
- `tools/build_monograph.sh`: passed; strict text audit and final log scan
  clean.
- `pdfinfo monograph/tex/main.pdf`: 2171 pages.
