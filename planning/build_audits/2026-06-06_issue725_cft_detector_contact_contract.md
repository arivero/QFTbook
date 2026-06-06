# 2026-06-06 Issue #725 CFT Detector-Contact Contract Pass

## Scope

- Targeted `calculation-checks/cft_energy_detector_contact_checks.py`, the
  Volume III Chapter 10 companion for statewise detector measures, diagonal
  contacts, and finite light-ray OPE charts.
- Promoted the companion to an extended evidence contract in
  `calculation-checks/evidence_contracts.json`.
- Added one reader-facing clarification in the detector-products subsection:
  the constant detector test fixes only the total diagonal contact mass, while
  localized finite bins require the contact measure along the diagonal.

## Substance Added

- Added an evidence contract covering target claims, independent construction,
  imported assumptions, negative controls, scope boundary, derivation and
  verification routes, convention dependencies, domain/remainder assumptions,
  and remaining conditional inputs.
- Added an exact rational negative control for bin-resolved contact data:
  a shifted diagonal contact measure can preserve
  `G_2(1,1)=<P^0^2>` while giving the wrong same-bin detector product for a
  localized calorimeter bin.
- Updated the calculation-check README and Chapter 10 dossier so the finite
  companion is recorded as checking partition/contact/chart algebra after the
  QFT inputs have been supplied.

## Quality Re-Audit Notes

- This pass is infrastructure and scope discipline, not a construction of the
  CFT detector product measure or a Lorentzian light-ray OPE theorem.
- The physics depth comes from protecting the operational detector statement:
  contact terms are measured by finite angular bins, not repaired only at the
  constant-test sum rule.
- The new negative control blocks a plausible but underpowered shortcut in
  which the correct total contact mass is assigned to the wrong angular
  diagonal cell.
