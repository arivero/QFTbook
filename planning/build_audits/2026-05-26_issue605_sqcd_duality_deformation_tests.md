# Build Audit: SQCD Duality Deformation Tests

Date: 2026-05-26

Branch: `codex/susy-gauge-dynamics-localization`

Issue focus: #605, with overlap for #588's four-dimensional supersymmetric
gauge-theory foundations.

## Scope

This pass strengthens Volume VII Chapter 06 in the SQCD Seiberg-duality
section.  Earlier passes displayed field tables, anomaly matching, and NSVZ
arithmetic.  This pass adds the mass-deformation and Higgs-deformation
algebra that is usually summarized too quickly in the physics literature.

## Source And Convention Notes

- The pass is entirely intrinsic to four-dimensional QFT.  No superstring,
  D-brane, compactification, or holographic derivation is used.
- The magnetic meson normalization remains the Chapter 06 convention:
  `M` is the electric composite `tilde Q Q`, and the magnetic
  superpotential is `M q tilde q / mu_*`.
- The new proposition is a necessary-consistency test for the quoted
  nonperturbative duality input; it is not presented as a proof of the full
  infrared equivalence.

## Substantive Changes

- Added Proposition `prop:sqcd-seiberg-deformation-tests`.
- For an electric mass `m M^L_L`, displayed the magnetic `F_M` equation
  `q_L tilde q^L / mu_* + m = 0`, a rank-one Higgs representative, and the
  breaking `SU(N_f-N_c) -> SU(N_f-N_c-1)`.
- Identified the boundary case where initial magnetic rank `2` Higgses to
  trivial `SU(1)`, matching the `N_f=N_c+1` confining chiral description.
- For a rank-`r` electric meson expectation value, displayed the electric
  Higgsing `SU(N_c)->SU(N_c-r)`, the magnetic masses
  `(v_A/mu_*) q_A tilde q^A`, and the rank identity
  `(N_f-r)-(N_c-r)=N_f-N_c`.
- Extended `susy_n1_sqcd_duality_checks.py`, the calculation-check README,
  and the Chapter 06 dossier.

## Verification

- `python3 calculation-checks/susy_n1_sqcd_duality_checks.py`: passed.
- `tools/run_calculation_checks.sh`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `git diff --check`: passed.
- `tools/build_monograph.sh`: passed with a clean TeX log scan.
- `pdfinfo monograph/tex/main.pdf`: 1556 pages, 6149887 bytes.

## Status

This advances #605 by replacing another implicit Seiberg-duality consistency
argument with displayed field-theoretic algebra.  It closes no issue by
itself.
