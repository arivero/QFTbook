# 2026-06-06 Issue #527 Detector-Inclusive Probability Bridge

## Scope

- Issue: #527, charged Haag--Ruelle/LSZ and infraparticle scattering.
- Manuscript target: Volume IV, Chapter 5, charged-sector soft
  representation discussion.
- Calculation companion: `calculation-checks/charged_flux_dressing_checks.py`.

## Substance Audit

- Added a new subsection, "Flux-Resolved Amplitudes and Detector-Inclusive
  Probabilities," immediately after the velocity-fibered soft representation.
- The new proposition separates three objects that must not be conflated:
  a flux-resolved dressed LSZ coefficient, the Bloch--Nordsieck sum over
  detector-unresolved photons, and detector coarse-graining over angular-flux
  cells.
- The finite-cutoff proof uses the coherent soft split
  \(F=F_{\lambda,E_T}\oplus F_{E_T,M}\).  Summing all unresolved photons
  cancels only the unresolved part of the virtual soft norm and leaves the
  resolved-window no-emission factor, which becomes
  \((E_T/M)^{A_{\beta\alpha}}\) at leading logarithmic order.
- The coarse-flux paragraph records that distinct sharp angular-flux sectors
  are orthogonal alternatives, so detector cells add probabilities, not
  amplitudes.
- The TeX contains no directive, planning, or issue-process language.

## Negative Controls

- The companion check rejects a fixed-photon-number reading by verifying that
  fixed unresolved photon-number terms decrease along an infrared sequence.
- It verifies the exact coefficientwise cancellation after the unresolved
  photon sum, rather than relying only on exponentiated prose.
- It rejects coherent amplitude summation across orthogonal flux-sector
  alternatives by comparing it with the projector probability.
- The chapter keeps total charge and angular flux distinct; detector
  inclusiveness is not used to collapse flux-sector selection to a charge-only
  rule.

## Verification Results

- `python3 -m py_compile calculation-checks/charged_flux_dressing_checks.py`
  passed.
- `python3 calculation-checks/charged_flux_dressing_checks.py` passed.
- `python3 calculation-checks/check_utils_checks.py` passed after the new
  finite-rate negative controls were routed through guarded numeric
  inequalities.
- `tools/run_calculation_checks.sh --python-only --only
  charged_flux_dressing_checks` passed.
- Focused Ch5 negative-scope, theorem-form, unnumbered-display-label, and
  style-density audits passed.
- `tools/audit_chapter_dossiers.sh`, `tools/audit_monograph_text.sh`,
  `python3 tools/audit_calculation_check_inventory.py`, and
  `python3 tools/audit_calculation_evidence_contracts.py` passed.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- Full `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` rebuilt
  and log-scanned clean at 3408 pages.
- `git diff --check` passed during verification.

## Scope Boundary

This pass improves the interface between flux-resolved charged LSZ data and
physical finite-resolution probabilities.  It does not close #527: the full
nonperturbative charged Haag--Ruelle theorem, the large-time
Dollard--Cook/Wilson-line estimates, and dressed-correlator boundary-value
theorems remain open.
