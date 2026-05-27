# Build Audit: Volume X Hydrodynamic Scaling and Force-Basis Pass

## Scope

- Branch: `main`.
- Files edited:
  - `monograph/tex/volumes/volume_x/chapter05_hydrodynamics_from_ward_identities.tex`
  - `planning/chapter_dossiers/volume_x/chapter05_hydrodynamics_from_ward_identities.md`
  - `calculation-checks/hydrodynamic_modes_checks.py`
  - `calculation-checks/README.md`

## Substantive Changes

- Added a hydrodynamic scaling-family definition so constitutive relations
  are stated as asymptotic claims on slowly varying states and sources after
  thermodynamic limit and contact-term subtraction.
- Expanded frame language to include scalar variable redefinitions and
  Landau matching conditions for \(\varepsilon\) and \(n_A\).
- Derived the sourceful ideal Euler equation and the reduction
  \(a^\mu+\Delta^{\mu\nu}\partial_\nu\log T
  =Tn_A V_A^\mu/(\varepsilon+p)\).
- Classified the first-order parity-even dissipative structures in Landau
  frame as \(\sigma^{\mu\nu}\), \(\vartheta\), and transverse charge forces
  \(V_A^\mu\), rather than simply asserting the constitutive relations.
- Extended the public hydrodynamic calculation check to verify the
  sourceful Euler force-basis identity.

## Verification Plan

- `python3 calculation-checks/hydrodynamic_modes_checks.py`
- `python3 -m py_compile calculation-checks/hydrodynamic_modes_checks.py`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/build_monograph.sh`

## Verification Results

- `python3 calculation-checks/hydrodynamic_modes_checks.py`: passed.
- `python3 -m py_compile calculation-checks/hydrodynamic_modes_checks.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed, including final log scan.
- Generated PDF: `monograph/tex/main.pdf`, 1947 pages.
