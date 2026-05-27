# 2026-05-27 Issue #628 QCD Phase-Structure Chapter Pass

## Scope

- Reviewed live GitHub issue #628 and `claude_review.md`.
- Confirmed that Volume X had thermal gauge screening but no dedicated QCD
  phase-structure chapter.

## Manuscript Changes

- Added Volume X Chapter 12, `QCD Phase Structure, Plasma, and Dense Matter`.
- Defined a QCD phase datum with pressure, exact symmetries, order parameters,
  limit prescriptions, and status labels.
- Added center-deconfinement definitions and a finite-volume center-symmetry
  proof for charged Polyakov loops.
- Added a chiral-symmetry section with a self-contained Banks--Casher proof
  under explicit spectral-density hypotheses.
- Derived the free QCD Stefan--Boltzmann pressure at zero and finite baryon
  chemical potential.
- Added HTL-domain status language and a proof of the magnetic \(g^6T^4\)
  Linde scale.
- Added Kubo-based QGP transport definitions, finite-density sign-problem
  proof, CFL order-parameter datum and Goldstone count, and a confinement
  criteria comparison.

## Calculation Checks

- Added `calculation-checks/qcd_phase_checks.py` for the finite algebra behind
  the pressure coefficients, baryon-chemical-potential coefficients,
  Banks--Casher kernel normalization, Linde power counting, and CFL Goldstone
  count.

## Verification

- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 -m py_compile calculation-checks/qcd_phase_checks.py`
- Edited-file long-line scan.
- `git diff --check --` on the edited manuscript, calculation-check,
  dossier, and audit files.
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'` reported `Pages:           2143`.
