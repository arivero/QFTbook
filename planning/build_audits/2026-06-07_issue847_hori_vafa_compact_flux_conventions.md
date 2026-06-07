# 2026-06-07 Issue #847 Hori--Vafa Compact Flux Conventions

## Scope

- Responds to #847: the Hori--Vafa lane in Volume VII Chapter 09 used the
  period-one FI coordinate as though `exp(t)` were a physical fugacity.
- Keeps the repair in the physics of compact gauge flux, theta periodicity,
  vortex-sector weights, and observable amplitudes.  The goal is not another
  finite mirror residue cell.

## Changes

- Replaced the ambiguous FI notation by `tau=theta/(2 pi)+i r`,
  `T=2 pi i tau=-2 pi r+i theta`, and `q=exp(T)`.
- Added the component compact-flux convention:
  `k=(2 pi)^{-1} int F in Z`, `S_theta=-i theta k`, and a positive-vortex
  topological weight `exp((-2 pi r+i theta)k)=q^k`.
- Propagated `T` through the Hori--Vafa dual superpotential, mirror torus
  constraints, Coulomb branch equations, projective-space residue coordinate,
  stable-map/vortex fugacity, and hypersurface singular coordinate.
- Restricted the mirror conjecture to superpotential data that preserves the
  phase isometries being dualized unless extra mirror input is supplied, and
  recorded the flux/cocharacter lattice data for global gauge form
  `U(1)^s/Gamma`.
- Replaced the flavor-attached vortex-sector language by a common gauge-flux
  sector.  The index `i` now labels the dual disorder/source projection to
  `exp(-Y_i)`, not an independent topological sector in the original GLSM.
- Added exact companion checks rejecting nonperiodic `exp(tau)` fugacities and
  flavor-labelled topological sectors under equal-charge flavor rotations.

## Quality Re-Audit

- The repair addresses the physical normalization chain behind the instanton
  amplitude: compact flux, theta periodicity, FI weight, and the original-to-dual
  operator map.  It does not import Hori--Vafa signs as authority.
- The vortex section remains amplitude-facing.  The common flux chart supplies
  collective coordinates, but the coefficient still depends on nonzero-mode
  determinants, Berezin saturation, source projections, determinant-line
  orientation, and operator-map normalization.
- The projective-space residue and stable-map formulas remain protected
  observable tests after the vortex-normalized fugacity is supplied; they are
  not promoted to a full QFT mirror proof.

## Verification

- `python3 -m py_compile calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 calculation-checks/susy_2d_lg_glsm_checks.py`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `git diff --check`
- `bash tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter09_two_dimensional_supersymmetric_models.tex --window 120 --stride 60 --fail --limit 20`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/run_calculation_checks.sh --python-only --only susy_2d_lg_glsm`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
