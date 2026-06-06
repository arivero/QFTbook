# Issue #725: Extended Evidence-Contract Tier

## Scope

This pass responds to the June 6, 2026 #725 review that the monograph needs a
repo-enforced distinction between manuscript derivation routes and genuinely
independent verification routes for load-bearing claims.

The change is intentionally outside the monograph TeX.  It hardens the public
calculation-check evidence infrastructure so that representative high-risk
companions must record:

- the manuscript's primary derivation route;
- the independent verification route;
- convention dependencies and conversion-sensitive tags;
- domain and remainder assumptions;
- remaining unproved or conditional claims.

## Representative Coverage

The first extended-tier entries are the three examples named by the review as
standard failures to guard against:

- `instanton_physical_amplitude_architecture_checks.py`, for the distinction
  between finite source-channel checks and physical instanton-amplitude
  claims involving determinants, zero modes, projections, and endpoint
  control;
- `generalized_unitarity_reduction_checks.py`, for physical channel
  discontinuities, master transport, denominator-aware loop Jacobi checks,
  finite-field coefficient recovery, and observable assembly;
- `qcd_phase_checks.py`, for finite-density transport and spectral extraction
  conventions in the declared hydrodynamic frame.

## Audit Hardening

`tools/audit_calculation_evidence_contracts.py` now enforces the extended
fields and nonempty `convention_tags` for extended entries in
`calculation-checks/evidence_contracts.json`.  It also scans manifest
companions for exact self-confirming assignments, such as defining a physical
datum by assigning it from a reconstructed result.

This is a first enforced slice of the #725 standard, not a claim that the
whole monograph now has complete evidence contracts for every load-bearing
formula.

## Verification

- `python3 -m json.tool calculation-checks/evidence_contracts.json >/dev/null`
- `python3 -m py_compile tools/audit_calculation_evidence_contracts.py calculation-checks/instanton_physical_amplitude_architecture_checks.py calculation-checks/qcd_phase_checks.py calculation-checks/generalized_unitarity_reduction_checks.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/qcd_phase_checks.py`
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `tools/run_calculation_checks.sh --python-only --only qcd_phase`
- `tools/run_calculation_checks.sh --python-only --only generalized_unitarity_reduction`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` clean; `main.pdf` was already up to date and the
  log scan passed.
