# 2026-05-29 Issue #630 QCD Current Sum-Rule Pass

## Scope

Advanced the QCD rigor-uplift issue by adding a self-contained framework for
Euclidean current sum rules and Borel/Laplace coordinates in Volume II Chapter
19.

## Manuscript Changes

- Added `Euclidean Current Sum Rules and Borel Windows`.
- Defined the renormalized color-singlet current correlator
  \(\Pi_J(Q^2;\mu)\), its subtracted dispersion representation, and the
  spectral density \(\rho_J(s;\mu)\).
- Stated the spacelike current OPE with explicit scheme dependence of local
  operator coordinates.
- Defined the Borel--Laplace functional and derived:
  - annihilation of subtraction polynomials;
  - \(\mathcal B[(s+Q^2)^{-1}]=M^{-2}e^{-s/M^2}\);
  - \(\mathcal B[(Q^2)^{-m}]=((m-1)!(M^2)^m)^{-1}\).
- Added a controlled-approximation datum for a Borel window, separating exact
  dispersion/OPE statements from pole-plus-continuum spectral modeling.
- Added a mass-estimator lemma showing the logarithmic Borel derivative is a
  weighted average over retained spectral atoms, not automatically a proof of
  single-state dominance.

## Calculation Checks

- Added `calculation-checks/qcd_sum_rule_checks.py`.
- The script verifies the Borel kernel limit, polynomial subtraction
  annihilation, inverse-power OPE terms, and mass-estimator weighted-average
  identity.

## Ledger Updates

- Updated `calculation-checks/README.md`.
- Updated the Volume II Chapter 19 dossier.
- Updated `claude_review.md` so #630 no longer lists QCD current sum rules as
  untouched; #630 remains open for the remaining QCD rigor-uplift clusters.

## Verification

- `python3 calculation-checks/qcd_sum_rule_checks.py`: passed.
- `python3 -m py_compile calculation-checks/qcd_sum_rule_checks.py`: passed.
- `git diff --check`: passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `bash tools/audit_chapter_dossiers.sh`: passed.
- `bash tools/build_monograph.sh`: passed; generated
  `monograph/tex/main.pdf` with 2553 pages and a clean log scan.
