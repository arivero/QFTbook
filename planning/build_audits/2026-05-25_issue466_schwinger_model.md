# Issue #466 Audit: Schwinger Model

## Scope

- GitHub issue: #466, "[Vol IV] Schwinger model (2D QED) absent."
- Manuscript loci:
  - `monograph/tex/volumes/volume_iv/volume_iv_current.tex`
  - `monograph/tex/volumes/volume_ii/chapter20b_schwinger_model_two_dimensional_qed.tex`
- Calculation-check locus:
  - `calculation-checks/schwinger_model_checks.py`
- Dossier locus:
  - `planning/chapter_dossiers/volume_ii/chapter20b_schwinger_model.md`

## Content Added

- Added the Schwinger model as a compiled chapter immediately after the local
  anomaly chapter in Volume IV.
- Defined the \(1+1\)-dimensional Abelian gauge theory, the compact connection
  normalization \(e a_\mu\), the electric field \(E=F_{01}\), the unit vector
  and axial currents, and the external probe-charge convention.
- Added the local gauge-invariant observable-sector definition and the
  Gauss-law constraint for external probes.
- Applied the two-dimensional anomaly to the dynamical gauge field to obtain
  \(\partial_\mu J_A^\mu=(e/\pi)E\).
- Proved directly from Maxwell's equation plus the anomaly that
  \((\Box-e^2/\pi)E=0\).
- Derived the bosonization current dictionary from current conservation and
  fixed its coefficient with the Schwinger term.
- Stated the exact current-generating functional equivalence between the
  massless Dirac current algebra and the compact scalar.
- Integrated out the algebraic electric field and derived the exact scalar
  mass \(m_{\rm Sch}^2=e^2/\pi\) and the operator equation
  \((\Box-m_{\rm Sch}^2)E=0\) away from insertions.
- Added a Schwinger-model figure linking the fermionic gauge theory, current
  algebra, anomaly equation, and exact massive scalar.
- Derived the screened static potential
  \(V_{\rm Sch}(R)=Q^2(1-e^{-m_{\rm Sch}R})/(2m_{\rm Sch})\).
- Added the massive-fermion sine-Gordon perturbation, the theta-shift
  interpretation of fractional probes, and the leading string tension for
  fractional probes at \(\theta=0\),
  \(\sigma(Q)=\kappa M(1-\cos(2\pi Q/e))+O(M^2)\).

## Verification

- Passed: `python3 calculation-checks/schwinger_model_checks.py`.
- Passed: `git diff --check`.
- Passed: `tools/audit_monograph_text.sh`.
- Passed: `tools/audit_chapter_dossiers.sh`.
- Passed: `tools/build_monograph.sh`.
- Passed: `pdfinfo monograph/tex/main.pdf` reports 859 pages.
- Rendered and inspected physical pages 713--715 at 144 dpi.  The
  Schwinger-model figure and the principal mass, screening, and
  fractional-probe formulas are legible and non-overlapping.
