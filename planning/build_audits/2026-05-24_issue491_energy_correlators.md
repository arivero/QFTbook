# Issue #491 Energy Correlators Audit

## Scope

- Oldest open GitHub issue addressed after #247.
- Added a detailed QCD-side detector-observable treatment in the QCD chapter.
- Added a compiled CFT chapter on light-ray operators and energy correlators.
- Updated master architecture, project decisions, and chapter dossiers.

## Manuscript Changes

- `volume_ii/chapter19_qcd_renormalization_asymptotic_freedom_and_dis.tex`
  now defines the energy-flow detector as a stress-tensor flux limit, states
  positivity and total-energy hypotheses, formulates calorimetric measures,
  derives soft/collinear continuity for smeared detector observables, defines
  the normalized \(e^+e^-\) EEC, and introduces multipoint energy correlators
  and energy-flow polynomials.
- `volume_iii/chapter10_light_ray_operators_and_energy_correlators.tex`
  now gives the CFT-side construction: wavepacket collider states, energy
  detectors at null infinity, averaged null energy light-ray operators,
  conformal-collider one-point functions, the \(t_2,t_4\) positivity
  inequalities, the CFT EEC, and the light-ray OPE theorem boundary.

## Verification

- `git diff --check`: clean.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `tools/build_monograph.sh`: clean, including final log scan.
