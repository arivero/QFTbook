# Build Audit: Volume VII Supersymmetric Gauge Foundations

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 03, `Supersymmetric Gauge Theory`,
so later holomorphy, SQCD, localization, and anomaly arguments rest on
explicit conventions rather than unstated physics shorthand.

## Substantive Edits

- Replaced the implicit curvature convention by the monograph's
  Hermitian-generator convention:
  `F_{mu nu}=i[nabla_mu,nabla_nu]=partial_mu A_nu-partial_nu A_mu-i[A_mu,A_nu]`.
- Added a proof that the finite gauge transformation sends
  `F_{mu nu}` to `u F_{mu nu} u^{-1}`, hence the kinetic and theta densities
  are gauge invariant.
- Made the matter moment map definition use a unitary representation and the
  dual pairing with the auxiliary field.
- Stated the FI centrality condition `zeta([X,Y]_H)=0`, making clear that FI
  data live only on abelian quotients.
- Added a full auxiliary `D`-field square-completion proof, deriving
  `D=-g^2(mu-zeta)^sharp` and
  `V_D=g^2 ||mu-zeta||^2/2`.
- Added a perturbative anomaly proposition proving
  `A_{R^vee}=-A_R`, vectorlike-pair cancellation, and anomaly cancellation
  for real representations such as the adjoint gaugino.
- Added `calculation-checks/susy_gauge_foundation_checks.py` and updated the
  Chapter 03 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_gauge_foundation_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_gauge_foundation_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the new
  gauge-foundation check and existing Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 1852 pages and file size 7381887 bytes.
