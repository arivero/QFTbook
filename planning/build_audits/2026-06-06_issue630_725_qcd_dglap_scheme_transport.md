# Issue #630/#725 QCD DGLAP scheme-transport pass

Date: 2026-06-06

## Scope

- Advanced Volume II Chapter 19's DIS/DGLAP section and the
  repository-wide evidence-contract program.
- Added `ca:qcd-dglap-scheme-covariant-moment-transport`, making the
  physical target a tested color-singlet structure-function moment rather than
  an independently measured colored parton probability.
- Promoted `calculation-checks/qcd_dglap_checks.py` to the extended evidence
  tier with convention tags for trace-delta color normalization,
  plus-distribution endpoints, DGLAP normalization, and coefficient/PDF scheme
  coordinates.
- Added a finite rational scheme-covariance check: under \(f'=Sf\) and
  \(C'=CS^{-1}\), a scale-dependent finite scheme change requires
  \(P'=SPS^{-1}+(\mu\partial_\mu S)S^{-1}\).

## Re-audit

- This is physics-facing DGLAP content: it strengthens how scaling violations
  of measured DIS moments are separated from auxiliary factorization scheme
  coordinates.
- The companion still does not claim to prove all-order DIS factorization,
  endpoint/small-\(x\) resummation, or nonperturbative PDF existence.
- Negative controls reject PDF-only transforms, wrong-side coefficient
  transforms, and similarity-only kernels when \(S\) depends on scale.
- No directive, issue-tracking, GitHub, Claude-review, monitoring, or planning
  process language was added to monograph TeX.

## Verification

- `python3 -m py_compile calculation-checks/qcd_dglap_checks.py`: pass.
- `python3 calculation-checks/qcd_dglap_checks.py`: pass.
- `tools/run_calculation_checks.sh --python-only --only qcd_dglap`: pass.
- `python3 calculation-checks/scet_factorization_checks.py`: pass after
  updating the textual-review anchors shifted by the Chapter 19 insertion.
- `tools/run_calculation_checks.sh --python-only --only scet_factorization`:
  pass.
- Focused Volume II Chapter 19 theorem-form, display-label, negative-scope,
  and style-density audits: pass.
- Process-language scan of the touched monograph/check surfaces: no GitHub,
  issue, Claude-review, monitoring, directive, or planning terms found.
- `python3 tools/audit_calculation_evidence_contracts.py`: pass, with the
  repository's nonblocking evidence-risk report.
- Strict evidence-risk scan: `qcd_dglap_checks.py` no longer appears in the
  risk report; remaining strict backlog count is 43.
- `python3 tools/audit_calculation_check_inventory.py`: pass, reporting 253
  active scripts (251 Python, 2 Wolfram).
- `tools/audit_chapter_dossiers.sh`: pass.
- `tools/audit_monograph_text.sh`: pass.
- `git diff --check`: pass.
- `tools/run_calculation_checks.sh --python-only`: pass.
- `tools/build_monograph.sh`: pass; `monograph/tex/main.pdf` is 3475 pages.
