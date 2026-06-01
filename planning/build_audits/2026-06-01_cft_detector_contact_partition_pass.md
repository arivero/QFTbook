# 2026-06-01 CFT detector-contact partition pass

## Scope

Advanced GitHub issue #519 on the CFT side of the energy-correlator program.
The pass targets the contact-term layer in Volume III, Chapter 10, where
energy correlators are first defined as products of null-infinity detectors.

## Manuscript changes

- Added `Detector Products and Diagonal Contacts` after the CFT energy
  correlator definition.
- Defined the finite positive calorimetric measure
  \(\varepsilon_X=\sum_a E_a\delta_{\mathbf n_a}\).
- Displayed the exact two-detector decomposition into off-diagonal and
  diagonal contributions.
- Added the general partition formula for \(k\)-detector products, making the
  diagonal contact strata explicit.
- Stated the total-energy Ward identity
  \(\mathcal G_2(1,1;\Psi)=\langle\Psi|(P^0)^2|\Psi\rangle\) as the
  normalization constraint on any extension across detector diagonals.
- Cross-linked the CFT detector-contact convention to the QCD EEC endpoint
  contact bookkeeping.

## Calculation companion

Added `calculation-checks/cft_energy_detector_contact_checks.py`.
It verifies, by exact rational arithmetic:

- two-detector product = off-diagonal term + diagonal contact term;
- pointwise disjoint detector tests have no diagonal contact;
- the constant-detector product reproduces the total-energy square;
- the three-detector partition decomposition reconstructs the full product.

## Status

This is a substantive #519 step but not a closure.  The all-order
renormalized light-ray OPE/mixing theorem, complete endpoint matching, and
high-loop/frontier energy-correlator development remain open.
