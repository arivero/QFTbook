# 2026-06-06 Issue #725/#769 Cutkosky Closure Independence Audit

## Scope

- Target issues: #725 evidence independence and #769 loop-amplitude
  reconstruction.
- Chapter touched: Volume II, Chapter 6, master-discontinuity closure block.
- Companion check:
  `calculation-checks/generalized_unitarity_reduction_checks.py`.

## Substance Audit

- Fresh review identified that `check_master_discontinuity_closure_gate()` set
  the physical Cutkosky datum equal to the reconstructed discontinuity, so the
  advertised closure passed by construction.
- The repair uses the scalar \(\lambda\phi^4\) bubble as the minimal physical
  closure example:
  \[
    \mathcal U_s =
    i\,{1\over 2!}\lambda^2\int d\Phi_2 =
    {i\lambda^2\over 16\pi},
    \qquad
    c_s\,\operatorname{Disc}\widehat B =
    {\lambda^2\over2}{i\over8\pi}.
  \]
- This is a physics-depth repair: it compares a positive-energy state-sum
  normalization with a transported master boundary-value jump.  It does not
  claim a complete nonabelian amplitude, a general multi-master solution, or
  closure of #769.

## Exact Checks Added

- The companion computes \(\pi d\Phi_2=1/8\) from the center-of-mass
  delta-function reduction of the ordered massless two-body phase space.
- The physical side uses the unordered identical-particle factor \(1/2!\) and
  the tree amplitude \(\mathcal M_4^{(0)}=-\lambda\).
- The master side independently uses the bubble coefficient \(\lambda^2/2\)
  and the transported bubble jump \(i/(8\pi)\).
- Negative controls reject:
  - omitting the identical-state factor;
  - a wrong master jump that would pass only if the physical datum were defined
    from the reconstruction itself;
  - raw contour values, Euclidean master values, wrong sheet, omitted lower
    sector, and untransported subtraction branch shortcuts.

## Verification Plan

- Run the focused generalized-unitarity companion.
- Run Ch6 theorem/display/scope/style audits.
- Run dossier, monograph text, calculation inventory, and evidence-contract
  audits.
- Run the full Python calculation suite and full monograph build.

## Verification Results

- `python3 -m py_compile
  calculation-checks/generalized_unitarity_reduction_checks.py` passed.
- `python3 calculation-checks/generalized_unitarity_reduction_checks.py`
  passed.
- `tools/run_calculation_checks.sh --python-only --only
  generalized_unitarity_reduction` passed.
- Ch6 theorem-form, unnumbered-display-label, negative-scope, and
  style-density audits passed.
- `python3 tools/audit_calculation_evidence_contracts.py` passed with the
  standing risk report only.
- `tools/audit_chapter_dossiers.sh`, `tools/audit_monograph_text.sh`, and
  `python3 tools/audit_calculation_check_inventory.py` passed.
- Full `tools/run_calculation_checks.sh --python-only` passed.
- Full `tools/build_monograph.sh` passed and produced
  `monograph/tex/main.pdf` at 3404 pages.
