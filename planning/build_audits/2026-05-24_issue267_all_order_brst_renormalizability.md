# Issue #267 All-Order BRST Renormalizability Audit

## Scope

- Oldest active GitHub issue addressed: `#267`, asking for an explicit
  all-order BRST/Slavnov--Taylor renormalizability theorem.
- Manuscript files:
  - `monograph/tex/volumes/volume_ii/chapter18_gauge_fixing_ghosts_and_brst_cohomology.tex`
  - `monograph/tex/volumes/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.tex`
- Dossiers:
  - `planning/chapter_dossiers/volume_ii/chapter18_gauge_fixing_ghosts_brst.md`
  - `planning/chapter_dossiers/volume_ii/chapter24_bv_master_formalism_gauge_effective_actions.md`

## Content Added

- Added Theorem `thm:all-order-slavnov-taylor-restoration`.
- The theorem states the perturbative all-order result with hypotheses:
  compact semisimple gauge group, off-shell nilpotent classical BRST
  differential, power-counting renormalizable local coordinate system including
  evanescent variables, a quantum-action-principle subtraction scheme, and
  vanishing local gauge-anomaly class in \(H^{1,D}(s_0\mid d)\).
- Added an induction proof:
  - define the linearized Slavnov operator \(\mathcal B_X\);
  - use locality of the order-\(N\) breaking \(\Delta_N\);
  - derive \(\mathcal B_{S_0}\Delta_N=0\) from the Slavnov consistency
    identity;
  - use the vanishing anomaly class to write \(a_N=s_0 b_N+d r_N\);
  - cancel the breaking by the local counterterm \(-\int b_N\);
  - identify the remaining finite ambiguity with \(H^{0,D}(s_0\mid d)\) and
    exact redefinitions.
- Added a BV chapter cross-reference explaining that the theorem is the
  gauge-fixed Yang--Mills form of perturbative BV master-equation restoration.
- Added the local/global anomaly boundary: global gauge anomalies are not
  detected by \(H^{1,D}(s_0\mid d)\).

## Verification

- `git diff --check`
- `tools/audit_monograph_text.sh`
- `tools/audit_chapter_dossiers.sh`
- `tools/build_monograph.sh`

All checks completed cleanly on 2026-05-24.
