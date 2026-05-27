# Build Audit: Volume VII Superspace Component Conventions

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

## Scope

This pass strengthens Volume VII Chapter 02, `Superspace, Superfields, and
Local Actions`, by making the chiral superspace coefficient convention
explicit and pairing it with a finite Grassmann-algebra calculation check.
The goal is to prevent later nonrenormalization, gauge-dynamics, and
instanton formulae from inheriting hidden factor-of-two or sign assumptions.

## Substantive Edits

- Fixed the chapter's \(\theta^2\) convention to
  `theta^2 = theta^alpha theta_alpha`, so with
  `epsilon^{12}=epsilon_{12}=1` the top monomial is
  `theta^2 = 2 theta^1 theta^2`.
- Updated the chiral-multiplet transformation proof to use
  `d theta^2 / d theta^alpha = 2 theta_alpha` under this convention.
- Added a proposition deriving the nilpotent Taylor coefficient of a chiral
  `F`-term:
  `[W(Phi)]_{theta^2}=F^i partial_i W - (1/2) partial_i partial_j W
  psi^{i alpha} psi^j_alpha`.
- Replaced the duplicated Wess-Zumino `F`-term Taylor derivation by a
  reference to the new proposition, keeping the component Lagrangian tied to
  the stated convention.
- Added `calculation-checks/susy_superspace_component_checks.py` and updated
  the Chapter 02 dossier and calculation-check README.

## Verification

- `python3 calculation-checks/susy_superspace_component_checks.py`: passed.
- `python3 -m py_compile calculation-checks/susy_superspace_component_checks.py`:
  passed.
- `tools/run_calculation_checks.sh`: passed, including the new superspace
  component convention check and the existing Wolfram gamma-trace check.
- `tools/audit_monograph_text.sh`: clean.
- `tools/audit_chapter_dossiers.sh`: clean.
- `git diff --check`: clean.
- `tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 1855 pages and file size 7391505 bytes.
