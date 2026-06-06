# 2026-06-06 Issue #597 Hard-Scale Benchmark Ratio

## Scope

- Issue: #597, instanton physics-depth lane.
- Manuscript target: Volume II, Chapter 20, BPST instanton and semiclassical
  vertex section.
- Calculation companion: `calculation-checks/bpst_instanton_normalization_checks.py`.

## Substance Audit

- Added `ca:thooft-hard-scale-benchmark-ratio` immediately after the
  four-fermion benchmark gate.
- The new block extracts a center-stripped hard four-fermion benchmark
  coefficient
  \(C_{\mathcal S}\Lambda_{\rm ht}^{29/3}Q^{-35/3}
  \mathcal H_{\mathfrak h}(R)(1+\varepsilon_Q)\) for the
  \(SU(3)\), \(N_f=2\) differentiated-source channel.
- The purpose is amplitude comparison, not moduli-space extension: the finite
  determinant constant cancels from the two-scale ratio, while source shape,
  rank conditioning, shared orientation projection, size-window tails, and
  physical projection remain visible.
- The TeX contains no directive, planning, or issue-process language.

## Negative Controls

- The companion rejects using a determinant-only ratio as the hard benchmark.
- It rejects a fixed Wilsonian local vertex as a hard-scale amplitude ratio.
- It rejects identifying a mass-saturated vacuum coordinate with the
  differentiated four-fermion hard benchmark merely because a leading hard
  exponent can agree in the two-flavor window.
- It records that stale dimensionless source windows and changed rank
  conditioning alter the two-scale ratio rather than hiding in a normalization
  constant.

## Verification Results

- `python3 -m py_compile calculation-checks/bpst_instanton_normalization_checks.py`
  passed.
- `python3 calculation-checks/bpst_instanton_normalization_checks.py` passed.
- `tools/run_calculation_checks.sh --python-only --only
  bpst_instanton_normalization_checks` passed.
- Focused Ch20 negative-scope, theorem-form, unnumbered-display-label, and
  style-density audits passed.
- `tools/audit_chapter_dossiers.sh`, `tools/audit_monograph_text.sh`,
  `python3 tools/audit_calculation_check_inventory.py`, and
  `python3 tools/audit_calculation_evidence_contracts.py` passed.
- `python3 calculation-checks/scet_factorization_checks.py` passed after the
  hard-scale equation label was named as a benchmark decomposition rather than
  a process-factorization occurrence.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- Full `tools/build_monograph.sh` passed; `monograph/tex/main.pdf` rebuilt and
  log-scanned clean at 3406 pages.
- `git diff --check` passed during verification.

## Scope Boundary

This pass strengthens the comparison with a 't Hooft-style hard four-fermion
amplitude.  It does not close #597: full declared-scheme determinant
normalizations, multi-instanton boundary estimates, and broader
soliton/monopole/instanton chapter architecture remain open.
