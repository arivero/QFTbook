# Issue #906 Unruh KMS And Detector Audit

## Scope

- Target chapter: `monograph/tex/volumes/volume_xii/chapter04_unruh_effect_modular_theory.tex`.
- Issue repaired: separate the distributional wedge two-point KMS theorem from
  bounded-algebra KMS, and replace the detector switched-contour shortcut with
  a stationary spectral KMS and controlled switching treatment.

## Substance Audit

- The free-field theorem is now stated as a distributional two-point
  boundary-value result.  Wick-polynomial expressions are described as an
  unbounded analytic core, while the bounded Weyl/von Neumann KMS statement is
  explicitly tied to Bisognano--Wichmann and the free quasifree Weyl
  construction.
- The detector section now distinguishes finite switched probability from the
  stationary transition rate.  Detailed balance is derived from the spectral
  KMS theorem for positive-type stationary distributions, not from an
  unjustified contour shift of a finite switched integral.
- The switching family \(\chi_T(\tau)=\chi(\tau/T)\) is normalized by
  \(T_{\rm eff}=T\|\chi\|_2^2\).  The finite probability is written as a
  spectral convolution, and the stationary rate is recovered through an
  approximate-identity limit with an explicit \(O(T^{-1})\) condition.
- The chapter includes the normalized four-dimensional massless scalar
  stationary excitation rate
  \(E/(2\pi)(e^{2\pi E/a}-1)^{-1}\) and the corresponding de-excitation rate.
- Negative controls are carried in the calculation check: finite switching
  smearing breaks exact detailed balance at finite width, while a compact
  smooth switch cannot serve as the holomorphic strip regulator needed by a
  contour proof.

## Physics-Depth Reaudit

- The added material is physics-facing: it moves from formal wedge analyticity
  to the actual detector probability/rate distinction, switching limit,
  spectral response, and normalized Planck spectrum.
- The pass avoids tangential algebraic inflation.  The bounded algebra result
  is recorded only to fix theorem status; the detailed development is on the
  detector observable and its physical limiting procedure.

## Verification

- Passed: `python3 calculation-checks/unruh_boost_geometry_checks.py`.
- Passed: `python3 calculation-checks/check_utils_checks.py`.
- Passed: focused prose/dossier/evidence audits:
  `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii/chapter04_unruh_effect_modular_theory.tex --fail`,
  `bash tools/audit_chapter_dossiers.sh`,
  `python3 tools/audit_calculation_evidence_contracts.py`,
  `python3 tools/audit_calculation_check_inventory.py`, and
  `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii/chapter04_unruh_effect_modular_theory.tex`.
- Passed: `tools/run_calculation_checks.sh --python-only`.
- Passed: `tools/build_monograph.sh`.
