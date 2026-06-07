# 2026-06-07 Issue #849 Higgs-Metric Nonrenormalization

## Scope

- Target issue: #849, Vol VII Ch08 follow-up on deriving Higgs-branch metric
  nonrenormalization instead of asserting it.
- Related issue: #810, which improved the statement but left the mechanism
  underderived.
- Monograph target:
  `monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`.
- Companion target: `calculation-checks/susy_moduli_space_checks.py`.

## Quality Audit

- The previous chapter text had correct quotient geometry and a useful ADHM
  example, but the Higgs-metric protection claim still read like a theorem
  label attached to the quotient rather than a Wilsonian mechanism.
- This pass makes the local two-derivative counterterm the object of study:
  `Delta S_H^(2)` and `Delta g_mn(q)` are introduced on a smooth fully
  Higgsed stratum with a transverse mass gap.
- The mechanism now separates \(4d\ \mathcal N=2\), \(3d\ \mathcal N=4\), and
  \(2d\ \mathcal N=(4,4)\) theorem boundaries; it distinguishes perturbative
  Wilsonian metric protection from global nonperturbative continuum equality.
- The counterterm filter classifies coordinate representatives, FI/mass
  transport, vector/coupling-spurion \(D\)-terms, torsion/Wess--Zumino data,
  and singular or mixed-branch operators.  This prevents the quotient metric
  from being oversold as a statement about every point or every two-dimensional
  branch coupling.
- The background-field cell gives a finite determinant ledger for a fully
  Higgsed tangent fluctuation, including gauge field, complex vector scalar,
  eaten hyper scalars, Faddeev--Popov ghosts, auxiliary contacts, and fermions.
  The companion check includes negative controls for missing ghosts, missing
  eaten hypermultiplets, and mass/tangent-vertex splitting.
- Boundary retained: the finite script is evidence for the local
  Ward/counterterm bookkeeping and the one-loop cancellation.  It is not a
  construction of the global continuum nonrenormalization theorem, the
  noncompact throat, boundary-condition data, or the interacting infrared SCFT.

## Verification

- `python3 -m py_compile calculation-checks/susy_moduli_space_checks.py`
- `python3 calculation-checks/susy_moduli_space_checks.py`
- `tools/run_calculation_checks.sh --python-only --only susy_moduli_space`
- `python3 tools/audit_theorem_form.py monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_unnumbered_display_labels.py monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex --window 120 --stride 60 --fail --limit 20`
- `rg -n "directive|claude_review|monitor|open issue|GitHub issue|depth-pass|unprecedented|planning doc|agent|review" monograph/tex/volumes/volume_vii/chapter08_moduli_spaces_supersymmetric_qft.tex`
  returned no matches.
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `tools/audit_chapter_dossiers.sh`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh` (clean, 3504 pages)
