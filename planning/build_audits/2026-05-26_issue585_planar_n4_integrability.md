# Build Audit: Issue #585 Planar N=4 Integrability

## Scope

- Added four Volume VII chapters:
  - `chapter12_planar_n4_spectral_problem_spin_chains.tex`
  - `chapter13_planar_n4_asymptotic_bethe_ansatz.tex`
  - `chapter14_planar_n4_mirror_tba_y_system.tex`
  - `chapter15_planar_n4_quantum_spectral_curve_hexagon.tex`
- Integrated them into `volume_vii_current.tex`.
- Added `calculation-checks/planar_n4_integrability_checks.py`.
- Updated calculation-check README, chapter dossiers, and stringbook
  crosswalk.

## Mathematical Content

- Planar single-trace local-operator space defined as a cyclic quotient.
- One-loop `SU(2)` scalar-sector Hamiltonian derived and normalized.
- Coordinate Bethe ansatz and one-loop Konishi roots carried to the anomalous
  dimension.
- All-loop magnon dispersion derived from the centrally extended shortening
  condition.
- Asymptotic Bethe equations stated with scalar dressing factor and proof
  boundary.
- Mirror TBA, excited-state energy, and T-hook Y-system stated with required
  analytic data.
- QSC Pmu system stated and reduced to the one-loop Baxter equation under
  explicit weak-coupling degeneration assumptions.
- Hexagon form-factor framework recorded with its derivation boundary.

## Verification

- `python3 calculation-checks/planar_n4_integrability_checks.py`

Full manuscript audits and build are recorded in the commit workflow that
closes issue #585.
