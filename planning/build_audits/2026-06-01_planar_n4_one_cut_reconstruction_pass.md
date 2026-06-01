# 2026-06-01 Planar N=4 One-Cut Reconstruction Pass

## Scope

Volume VII, Chapter 13 stated the one-cut large-spin \(SL(2)\) cusp
resolvent after the differentiated continuum Bethe equation.  The displayed
answer was correct, but the scalar reconstruction step was too compressed:
the endpoint \(a=1/2\), primitive, discontinuity, and density normalization
should be consequences of the Riemann-Hilbert data rather than an asserted
formula.

## Manuscript Changes

- Replaced the jump from the boundary-value equation to the resolvent by an
  explicit scalar reconstruction using
  \(R_a(z)=\sqrt{z^2-a^2}\) and \(H_a(z)=-1/(zR_a(z))\).
- Derived the distributional boundary source
  \(H_{a,+}+H_{a,-}=(2\pi/a)\delta(y)\), fixing \(a=1/2\).
- Integrated the fixed differential to obtain
  \(G_0(z)=-i\log((\sqrt{4z^2-1}+i)/(\sqrt{4z^2-1}-i))\) with
  \(G_0(\infty)=0\).
- Added the density-normalization calculation using
  \(y=(2\cosh t)^{-1}\).
- Extended the planar integrability calculation check to verify the density
  normalization.
- Updated the calculation-check ledger and chapter dossier.

## Verification

- `python3 calculation-checks/planar_n4_integrability_checks.py`: passed.
- `python3 -m py_compile calculation-checks/planar_n4_integrability_checks.py`:
  passed.
- `git diff --check`: passed.
- `python3 tools/audit_theorem_form.py`: passed.
- `python3 tools/audit_unnumbered_display_labels.py`: passed.
- `tools/audit_negative_scope_prose.py`: passed.
- `tools/audit_monograph_text.sh`: passed.
- `tools/audit_chapter_dossiers.sh`: passed.
- `tools/build_monograph.sh`: passed; rebuilt
  `monograph/tex/main.pdf`.
- `pdfinfo monograph/tex/main.pdf | rg '^Pages:'`:
  `Pages:           2807`.
