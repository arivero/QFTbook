# Issue #844 Donaldson-SW proof-obligation status pass

Date: 2026-06-06

## Scope

- Re-audited the Volume VIII Chapter 8 Witten--Donaldson/Seiberg--Witten
  comparison surface flagged by the architecture issue.
- Reworded the central comparison apparatus from residual-budget and ledger
  language into a proof-obligation diagnostic: the finite telescope is
  conditional propagation of supplied estimates, not evidence that the
  intermediate QFT functionals or same-regulator bounds have been constructed.
- Retained the central comparison as a conjecture with Feehan--Leness and
  algebro-geometric theorem subclasses separated from the stronger QFT
  Wilsonian/RG construction problem.
- Updated the companion check to use proof-obligation map language and to
  reject dropping the singular-fiber replacement arrow without changing the
  comparison target.

## Re-audit

- This is an architecture/status correction rather than a new Donaldson or
  Seiberg-Witten formula.
- The physics endpoint remains the same: a constructed twisted QFT and
  Q-compatible Wilsonian flow must derive the Donaldson/SW comparison factors
  in one normalization before the final formula can be used as a QFT theorem.
- The finite check verifies exact telescoping and conditional norm propagation
  only; it does not claim to construct the UV theory, Coulomb branch flow,
  singular-fiber replacement, or determinant/contact normalization.
- No directive, issue-tracking, GitHub, Claude-review, monitoring, or
  planning process language was added to monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/donaldson_sw_comparison_checks.py`:
  pass.
- `python3 calculation-checks/donaldson_sw_comparison_checks.py`: pass.
- `tools/run_calculation_checks.sh --python-only --only donaldson_sw_comparison`:
  pass.
- Focused Volume VIII Chapter 8 theorem-form, display-label, negative-scope,
  and style-density audits: pass.
- Process-language scan of the touched monograph/check surfaces: no GitHub,
  issue, Claude-review, monitoring, directive, or planning terms found.
- `python3 tools/audit_calculation_check_inventory.py`: pass, reporting 253
  active scripts (251 Python, 2 Wolfram).
- `tools/audit_chapter_dossiers.sh`: pass.
- `python3 tools/audit_calculation_evidence_contracts.py`: pass, with the
  repository's nonblocking evidence-risk report.
- `tools/audit_monograph_text.sh`: pass.
- `git diff --check`: pass.
- `tools/run_calculation_checks.sh --python-only`: pass.
- `tools/build_monograph.sh`: pass; `monograph/tex/main.pdf` is 3475 pages.
