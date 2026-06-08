# 2026-06-08 Issues #903/#904 Point-Splitting Stress Audit

## Scope

Addressed two coupled Volume XII Chapter 2 defects:

- #903: construct the conserved point-split scalar stress tensor rather than
  only listing desired properties;
- #904: correct the scalar trace identity for the chapter's mostly-plus
  convention and Klein--Gordon operator \(P=-\Box+m^2+\xi R\).

This is physics-facing infrastructure for composite observables,
semiclassical source terms, cosmological stress tensors, and trace anomalies.
The repair focuses on the QFT object being measured: the renormalized stress
tensor as a conserved local observable, not merely on curvature-tensor
bookkeeping.

## Substance

- Displayed the scalar bidifferential operator with parallel transport,
  symmetrized point splitting, curvature terms, mass term, and the
  equation-of-motion improvement
  \(\eta_D=D/[2(D+2)]\), hence \(\eta_4=1/3\).
- Made the Hadamard-parametrix bisolution defect explicit:
  \(\omega_2\) is a bisolution but \(H_{\epsilon,\mu}\) has smooth local
  \(P_xH\) and \(P_yH\) defects.
- Proved the logical shape of the conservation repair: the naive polarized
  Hilbert tensor has a local divergence defect, and the \(\eta_4\)
  improvement cancels it before residual conserved local terms are classified.
- Strengthened the finite-local-freedom hypotheses with weak regularity,
  smooth parameter dependence, locality, and almost-homogeneous scaling, so
  nonpolynomial functionals such as
  \(\int\sqrt{|g|}\,m^4F(R/m^2)\) are not silently admitted.
- Corrected the trace identity to
  \[
    T^\mu{}_\mu
    =
    -m^2\phi^2
    +(D-1)(\xi-\xi_c)\Box\phi^2 .
  \]
- Corrected the de Sitter diagnostic: for the massless conformal scalar,
  \(I_{\mu\nu}\) and \(J_{\mu\nu}\) vanish on four-dimensional constant
  curvature, and the \(m\)-dependent finite terms vanish at \(m=0\).

## Re-Audit

- Physics depth: the pass repairs the existence and conservation of the
  observable that sources semiclassical gravity and defines energy density,
  pressure, and trace response.
- Coherence: the TeX construction, finite companion, README, evidence
  contract, and dossier now carry the same convention.
- Scope restraint: no directive/planning prose was added to monograph TeX.
- Boundary: the analytic Hadamard coefficient identities and Hollands-Wald
  classification theorem remain theorem boundaries; the companion checks
  verify algebraic consequences and negative controls.

## Verification

- `python3 calculation-checks/point_splitting_stress_checks.py`
- `python3 tools/audit_style_density.py --root monograph/tex/volumes/volume_xii/chapter02_point_splitting_stress_tensor.tex --fail`
- `bash tools/audit_chapter_dossiers.sh`
- `python3 tools/audit_calculation_evidence_contracts.py`
- `python3 tools/audit_calculation_check_inventory.py`
- `python3 tools/audit_negative_scope_prose.py --root monograph/tex/volumes/volume_xii/chapter02_point_splitting_stress_tensor.tex`
- `tools/run_calculation_checks.sh --python-only`
- `tools/build_monograph.sh`

All listed gates passed.  The negative-scope prose audit initially caught a
corrective phrasing around Borel's lemma; the final text states the locality
requirement positively and the rerun is clean.
