# Issue #597 instanton cross-chapter normalization and pair-counting repair

Date: 2026-06-06

## Scope

Addressed the fresh #597 review at `1d6b60db` concerning two concrete
instanton-amplitude failures:

- The parent Ch20 hard-scale benchmark ratio had not been updated with the
  Ch20D running collective-coordinate factor
  `Gamma_coll(Q)=(8 pi^2/g_ht^2(Q))^6`.
- The first Ch20D connected pair-cluster assembly used an ordered species sum
  without making the Mayer `1/2` pair symmetry factor explicit.

This is a physics-amplitude normalization and cluster-combinatorics repair,
not an ADHM/moduli-space expansion.

## Changes

- Propagated `Gamma_coll(Q)` into the Ch20 hard four-source benchmark
  coefficient, same-theory ratio, slope qualification, and negative controls.
- Declared `d nu_{sigma tau}^{ord}` in Ch20D as an ordered two-body measure
  with no hidden pair symmetry factor.
- Changed the first cluster source-amplitude assembly to
  `1/2 sum_{sigma,tau} A_{sigma tau}^{conn}` and stated how the factor counts
  identical and mixed unordered pairs.
- Extended `instanton_physical_amplitude_architecture_checks.py` with:
  - a cross-chapter TeX regression requiring `Gamma_coll` in both duplicate
    hard benchmark coefficient/ratio surfaces;
  - exact ordered/unordered pair-counting regressions for mixed and identical
    pairs.
- Extended `bpst_instanton_normalization_checks.py` so the parent benchmark
  model rejects pure-power-only hard-scale ratios.
- Updated the calculation-check README and Ch20/Ch20D dossiers.

## Re-audit Notes

- The monograph TeX changes contain physics statements only.  Issue/review and
  process notes remain in planning files.
- The pass repairs an internal contradiction between Ch20 and Ch20D, so it
  improves reader coherence rather than adding another local instanton cell.
- The pair-counting repair aligns the Ch20D amplitude cluster with the parent
  Mayer convention.

## Verification

- `python3 -m py_compile calculation-checks/instanton_physical_amplitude_architecture_checks.py calculation-checks/bpst_instanton_normalization_checks.py`
- `python3 calculation-checks/instanton_physical_amplitude_architecture_checks.py`
- `python3 calculation-checks/bpst_instanton_normalization_checks.py`
- `tools/run_calculation_checks.sh --python-only --only instanton_physical_amplitude_architecture`
- `tools/run_calculation_checks.sh --python-only --only bpst_instanton_normalization`
- `git diff --check`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20_chiral_axial_anomalies.tex --fail --limit 20`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_ii/chapter20d_instantons_and_physical_amplitudes.tex --fail --limit 20`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `tools/audit_monograph_text.sh`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

The full Python calculation suite passed.  The full monograph build completed
with clean log scan at 3473 pages.

## Monitoring

Before commit/posting, `claude_review.md` remained unchanged since
2026-06-03 07:48:35 local time.  The latest #597 comment was the review being
addressed here.  Fresh reviews also exist on #630 and #527 and should be
handled in separate focused passes.
