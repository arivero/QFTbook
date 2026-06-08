# Issue #855 Hadamard/Wick distinction regression repair

Date: 2026-06-08.

Scope:

- Targeted the Wick-products section of Volume XII Chapter 09 after the
  microlocal chapter became first in printed order.
- Repaired the surviving #740-style conflation between a generic smooth
  Hadamard-coordinate change and local covariant finite Wick-renormalization
  freedom.

Before:

- The microlocal chapter said that changing the parametrix scale or adding a
  smooth local bisolution changes the Wick square by \(c_1R+c_2m^2\).
- That compressed two different operations:
  a generic smooth Hadamard/reference change has diagonal \(w(x,x)\), while
  \(c_1R+c_2m^2\) is the restricted comparison between locally covariant Wick
  prescriptions under covariance, scaling, and field-equation assumptions.

After:

- The chapter now states the raw point-splitting coordinate relation
  \(H'=H+w\Rightarrow :\phi^2:_{H'}(f)=:\phi^2:_H(f)
  -\int f(x)w(x,x)\,{\rm dvol}\,\mathbf 1\).
- It explicitly says that \(w(x,x)\) is a smooth function and need not be a
  local curvature polynomial for a generic Hadamard-coordinate change.
- It separately states the local covariant finite Wick-square prescription
  freedom \(c_1R+c_2m^2\) only under the additional local covariance,
  scaling, and field-equation hypotheses.
- Cross-references now point to the point-splitting and pAQFT chapters as the
  detailed destinations for prescription changes and interacting
  Wick-polynomial transport.

Negative controls added:

- Wrong sign for \(H'=H+w\).
- Fitting an arbitrary three-point smooth diagonal by \(a_m m^2+a_RR\).

Boundary:

- This pass repairs a local-covariance distinction and executable regression
  check.  It does not prove the global Hollands-Wald classification, construct
  Hadamard states, or address the separate #854 equicausal pAQFT functional
  space issue.

Verification:

- `python3 calculation-checks/microlocal_spectrum_checks.py`
- `python3 tools/audit_theorem_form.py --root monograph/tex/volumes/volume_xii/chapter09_microlocal_spectrum_condition.tex`
- `python3 tools/audit_unnumbered_display_labels.py --root monograph/tex/volumes/volume_xii/chapter09_microlocal_spectrum_condition.tex`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii/chapter09_microlocal_spectrum_condition.tex --fail`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii/chapter09_microlocal_spectrum_condition.tex --fail --limit 40`
- `tools/audit_monograph_text.sh monograph/tex/volumes/volume_xii/chapter09_microlocal_spectrum_condition.tex`
- `tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `git diff --check`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`
