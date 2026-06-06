# Issue #630/#725 QCD sum-rule evidence-contract pass

Date: 2026-06-06

## Scope

- Advanced the QCD current-sum-rule section in Volume II Chapter 19 and the
  repository-wide evidence-contract program.
- Promoted `calculation-checks/qcd_sum_rule_checks.py` to the extended evidence
  tier with convention tags for the Euclidean momentum, Borel scale, spectral
  positivity, continuum-threshold, and OPE-coordinate conventions.
- Added a finite pole-residue conditioning formula to the SVZ extraction
  window: a quoted current coupling or decay constant must propagate both the
  zeroth-moment residual and the mass-window uncertainty through the exponential
  Borel weight.
- Added `check_residue_extraction_mass_uncertainty_bound()` to the companion
  so a residue estimate that ignores mass uncertainty fails.
- Updated the calculation-check README and the Chapter 19 dossier.

## Re-audit

- This pass is physics-facing: it strengthens how Euclidean current sum rules
  produce hadron mass and residue coordinates, rather than adding detached
  transform algebra.
- The monograph text continues to state that the actual spectral measure,
  OPE-tail control, continuum duality, positivity, and regulator matching are
  channel-dependent QCD inputs.
- The companion is exact finite algebra and residual propagation.  It does not
  claim independent phenomenological evidence for any hadron mass or pole
  residue.
- No directive, issue-tracking, GitHub, Claude-review, monitoring, or planning
  process language was added to monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/qcd_sum_rule_checks.py`
- `python3 calculation-checks/qcd_sum_rule_checks.py`
- `tools/run_calculation_checks.sh --python-only --only qcd_sum_rule`
- `python3 calculation-checks/scet_factorization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`
- focused theorem/display/scope/style audits for Volume II Chapter 19
- process-language scan of the touched monograph/check surfaces
- `python3 tools/audit_calculation_evidence_contracts.py`
- strict evidence-risk scan confirming `qcd_sum_rule_checks.py` leaves the
  remaining backlog; the strict remaining-risk count is now 44
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `tools/audit_monograph_text.sh`
- `git diff --check`
- full `tools/run_calculation_checks.sh --python-only`
- full `tools/build_monograph.sh`, clean at 3474 pages
